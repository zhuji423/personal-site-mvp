---
title: "架构深度解析报告 (QAMate & ITP)"
description: "思考过程（Thinking Process）： 1. 确定受众：面向熟悉 Python、对 Java 仅停留在语法层面的研发人员。因此在剖析中，我将使用部分 Python 生态（如 Flask/Django, requests, Celer"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\wiki\\ARCHITECTURE_DEEP_DIVE.md"
---
# 架构深度解析报告 (QAMate & ITP)

> **思考过程（Thinking Process）**：
> 1.  **确定受众**：面向熟悉 Python、对 Java 仅停留在语法层面的研发人员。因此在剖析中，我将使用部分 Python 生态（如 Flask/Django, requests, Celery）作为类比，帮助理解 Java 生态（Spring Boot, Feign, XXL-JOB）。
> 2.  **提取核心域**：从提供的元数据和 `AGENTS.md`、`COMPLEX_FUNCTIONS_ANNOTATIONS.md` 中提取关键逻辑链路。系统分为 `core`（业务编排调度）、`apiExecutor`（实际执行）和 `api-smart-dispatch`（分布式调度）三大核心模块，外加遗留的 `itp` 体系，典型的**微服务+管道过滤器+任务调度**模式。
> 3.  **追踪核心链路**：`core` 作为中枢，调用了 `api-smart-dispatch`。后者完成调度后，通过 `JobCompleteHelper.callServerPlanEnd` 异步回调；同时 `core` 还会直接下发任务给 `apiExecutor` 执行（通过 `/executor/task/case/submit`）。这里面充满了大量的异步等待、状态机变更。
> 4.  **识别深层依赖与风险**：
>     *   `RequestFilter.doFilter` 中的请求级指标统计（Metric tags）有基数爆炸风险（在 Python Prometheus Client 中同样是致命错误）。
>     *   `FeignConfig` 中的鉴权复用了 `RequestContextHolder`，把网络层与 MVC 请求生命周期深度绑定，这是非常严重的隐性依赖（类似 Flask 的 global `request` 对象在异步协程/Celery Worker中抛错）。
>     *   `OpenApiToken` 中写死了各种 Super Token，存在越权和泄露风险。

---

## 1. 全局架构图景 (Global Architecture)

项目采用的是**事件驱动与分布式调度混合的微服务架构**（Microservices with Event-driven & Scheduled Dispatching）。整个系统可划分为现行系统 (`qamate-server`) 以及 遗留体系 (`inner-os/itp`)。

对于熟悉 Python 的开发者，这很像是一套用 FastAPI 接客（`core`），底层依赖 Celery/Airflow 进行分布式任务分发（`api-smart-dispatch`），最后由多个独立运行的无状态 Worker（`apiExecutor`）来实际吞吐任务的系统。

### 核心微服务依赖图

```mermaid
graph TD
    User((Client / User)) -->|HTTP Rest / API| RequestFilter(core: RequestFilter 鉴权)
    RequestFilter -->|Valid Token| CoreController(core: *Controller)
    CoreController -->|1. 任务流编排| CoreService(core: *Service)
    
    subgraph `qamate-server` (现行核心产品线)
        CoreService -->|2. Feign Client (DispatchClient)| A[api-smart-dispatch (XXL-JOB内核)]
        A -->|3. 定时/触发调度任务| ExecutorController(apiExecutor: TaskController)
        
        CoreService -->|2. 直连下发 /executor| ExecutorController
        ExecutorController -->|5. 异步/多线程执行| Runner(apiExecutor: Runner/Service)
        
        Runner -->|6. 执行结果上报| CoreService
        A -->|4. JobComplete回调| CoreService
    end

    subgraph `inner-os/itp` (遗留 LTS)
        ITP_Web(ITP Web) --> ITP_TaskTracker(Task Tracker)
        ITP_Web -.->|Legacy Data| DB_Legacy[(Legacy DB)]
    end
    
    DB_Qamate[(MySQL / 分库分表)] --- CoreService
    ThirdParty(UUAP / Kami / Lumos / QF) -.->|依赖/鉴权| CoreService
```

---

## 2. 核心业务流向 (Core Business Flow)

关键业务路径为**测试计划的提交至最终执行与回调闭环**：

1.  **用户请求与边界防御（Gateway/Filter）**：
    请求发起后，首先进入 `core/src/main/java/com/baidu/qamate/core/components/config/RequestFilter.java`（约第 116 行）。这里拦截所有请求进行鉴权，并在 MDC（Mapped Diagnostic Context，类似 Python 的 `contextvars`）中注入 `traceId`，保障多线程和微服务间的日志链路不断。
2.  **业务编排（Controller -> Service -> Manager）**：
    调用到达 `core`，采用经典的 Java 分层架构。Controller 接参验证，Service 进行业务逻辑组装，Manager 负责外部依赖调用。
3.  **微服务间调度（Manager -> Dispatch/Executor）**：
    *   **主链路 A (调度中心)**：`core` 内部使用 `DispatchClient`，通过 Feign（类似于 Python 中的 `requests` 或 `httpx`，但通过接口声明自动生成客户端）调用调度服务 `/apismart/dispatch/api/*`。在这里，`api-smart-dispatch` （基于 XXL-JOB 的二次开发）接收并持久化任务，关联 `planId`（核心数据模型 `XxlJobInfo`）。
    *   **主链路 B (直连执行)**：通过 `UrlConfig.INTERFACE_DEBUG_TASK_CREATE` 等配置，直连调用 `apiExecutor` 模块下的 `/executor/task/case/submit`，绕过 XXL-JOB 的重型控制。
4.  **执行与回调闭环（Callback & Async Cleanup）**：
    *   如果由 `api-smart-dispatch` 触发，任务执行结束后，调度中心会进入 `JobCompleteHelper.callServerPlanEnd` 进行扫尾，并且携带 `QAMate-ModuleId` 与 `QAMate-Token` 主动回调回 `core` 通知计划终结。

---

## 3. 隐性依赖与副作用 (Hidden Dependencies & Side Effects)

1.  **上下文生命周期泄漏 (ThreadLocal Coupling)**：
    *   **具体代码**：`core/src/main/java/.../FeignConfig.java` (~第45行)。
    *   **现象**：`RequestContextHolder.currentRequestAttributes()` 被直接嵌在 Feign (HTTP Client) 的拦截器中。
    *   **隐患**：`RequestContextHolder` 是基于 `ThreadLocal` 的。在 Python 中这就如同在一个由 Celery 启动的后台协程里，强行去读取 Flask 的 `request` 全局对象。如果系统在**异步线程**或者**定时任务**中调用外部依赖，会直接抛出 `IllegalStateException` 崩溃，属于极易踩坑的隐性耦合。
2.  **Metrics 基数爆炸风险**：
    *   **具体代码**：`RequestFilter.java` (~第173行)。
    *   **现象**：指标统计时将 `username` 或其他高基数(动态)属性作为 `tags` 传递给 Prometheus 计数器（`registry.counter()`）。
    *   **隐患**：如果在极短时间内涌入大量不同用户，Prometheus Server 会面临“基数爆炸”导致内存溢出；此外如果不做 Memoize 缓存，每次 `registry.counter()` 可能都在竞争锁以注册新指标，极大拖慢请求。
3.  **硬编码认证系统 (Hard-Coded Tokens)**：
    *   **具体代码**：`OpenApiToken.java` (~31-46行)。
    *   **现象**：硬编码了 `SUPER_QAMATE_TOKEN`, `TESTONE_QAMATE_TOKEN`。这种“只要遇到这个魔法字符串就放行”的逻辑会在不同的人员变动中成为无人敢删的神奇依赖，一旦泄露，全盘瓦解。

---

## 4. 设计模式与代码风格 (Design Patterns & Style)

1.  **责任链机制 (Filter Chain / Interceptors)**：
    `RequestFilter.doFilter` 展示了 Java 中经典的责任链模式。通过一层层的 Filter 剥离 Header 抽取、限流、鉴权逻辑。但是目前该方法臃肿（单函数近100行），没有利用好模式本身“解耦”的特点，把业务指标、Token 提取全塞在一起了。
2.  **工厂与代理模式 (Feign Clients)**：
    系统重度使用了 Spring Cloud Feign (`DispatchClient.java`, `WorkerClient.java`)。这是一个动态代理模式（Dynamic Proxy），开发者只用编写 Interface 接口，底层代理会拦截函数调用并将其转变为真正的 HTTP 请求。
3.  **分层架构模式 (Layered Architecture)**：
    严格遵守 `com.baidu.qamate.core.*mgt` 领域按 `Controller -> Service -> Manager -> Mapper/Entity/VO` 分层。该模式有助于约束团队边界，但容易产生大量的“贫血模型”（Anemic Domain Model），即数据实体 (`VO`/`Entity`) 中完全没有逻辑，所有的逻辑都堆积在 `Service` 的大函数里。

---

## 5. 潜在风险评估 (Top 5 Technical Debts & Risks)

结合 20 年的架构经验，本项目有以下 5 大最危险的漏洞与架构债务：

### 1) 安全维度：越权访问与硬编码后门 (High Risk)
*   **证据**：`OpenApiToken.checkFromToken` 行 31-46。
*   **描述**：代码层写死了部分 Super Tokens。由于微服务系统横向扩展，这意味着任何知道此魔术字符串的内网人员，都可以伪装成高权限模块进行越权调用。
*   **修复**：废弃对称式的静态 Token，统一升级为 OIDC/OAuth2 架构下的 JWT (JSON Web Tokens)，借助非对称加密进行鉴权拆分。

### 2) 稳定性维度：同步调用造成的线程池雪崩 (Critical Risk)
*   **证据**：`FeignConfig.getWorkerToken()` 行 60-72 甚至在发送请求**之前**又发起了另一个**同步**的 HTTP 登录请求来获取 Token。
*   **描述**：在并发陡增的高峰，每一个到 Worker 的发件请求都会被阻塞，导致 Servlet 线程池和 Feign 线程排队激增。只要 `WorkerClient` 网络一端稍微抖动，上游服务将被迅速“拖死”。
*   **修复**：引入 `OAuthTokenManager` 进行旁路异步刷新与本地缓存；或者使用 Token 异步续租机制。

### 3) 内存与并发维度：非流式请求缓冲导致 OOM (Medium Risk)
*   **证据**：`RequestFilter.java` 行 120-123 使用 `CachedHttpServletRequestWrapper` 包装了当前 ServletRequest 请求体。
*   **描述**：当面临例如大规模文件上传或海量 Case XML 体的下发时，`CachedHttpServletRequestWrapper` 通常会将整个请求体一次性读入到内存空间。多个大请求并发会瞬间打爆 JVM 的 Heap 内存（OOM）。
*   **修复**：对大体积接口路径 (`isExcludedUri` 衍生机制) 设置绕过包装器机制；对输入层设置硬性的 Max-Body-Size。

### 4) 可扩展性维度：ITP 遗留黑盒与包冲突 (High Risk)
*   **证据**：根据 `AGENTS.md`，遗留 ITP 是 `JDK8 / Maven3.0.x`。
*   **描述**：如果未来发生合仓打包或者由于二方库存放在内网引起依赖交叉（POM依赖大量内网源），旧时代的低版本 Jackson/Guava 包极有可能会侵入 `core` (JDK17/21) 中造成 `NoSuchMethodError`，这种类加载层面的毒药会引起不可预知的回滚。
*   **修复**：严守服务物理边界，通过 gRPC 或 HTTP 清晰划分 `qamate-server` 和 `itp` 接口，绝不允许引用共同的基础 Jar 模块（禁止 common-lib 分享）。

### 5) 并发安全维度：日志 TraceId 跨异步丢失 (Medium Risk)
*   **证据**：`RequestFilter.java` 中利用 `MDC.put("traceId", traceId)`，最后 `MDC.clear()`。
*   **描述**：在 Java 中 MDC 是绑定在当前线程池线程的。下层的 `apiExecutor` 和 `TaskService` 中有诸多“异步下发”和“重跑逻辑”（多线程）。一旦发生新线程启动，MDC 信息丢失，导致生产报错时完全无法在这个“分布式调用图”里把日志串起来。
*   **修复**：确保所有的 `ExecutorService` 包装使用安全扩展（例如 Spring Cloud Sleuth 方案或自行实现的 `TraceContextAwareThreadPool`），拷贝父线程 MDC 上下文到子线程。
