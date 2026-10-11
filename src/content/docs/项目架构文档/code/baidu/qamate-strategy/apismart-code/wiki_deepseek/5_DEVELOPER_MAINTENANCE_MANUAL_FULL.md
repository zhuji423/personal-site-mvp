---
title: "QAMate 全库开发者维护手册 (完整版)"
description: "零基础新手? 本文是写给有一定编程基础（至少知道 Java/Python 的基本语法）的开发者看的。如果你是完全没有后端经验的纯小白,请先阅读同目录下的 1ZEROBACKENDCONCEPTS.md（零基础后端概念说明）,理解 Core "
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\wiki_deepseek\\5_DEVELOPER_MAINTENANCE_MANUAL_FULL.md"
---
# QAMate 全库开发者维护手册 (完整版)

> **零基础新手?** 本文是写给有一定编程基础（至少知道 Java/Python 的基本语法）的开发者看的。如果你是完全没有后端经验的纯小白,请先阅读同目录下的 `1_ZERO_BACKEND_CONCEPTS.md`（零基础后端概念说明）,理解 Core / Executor / Dispatch 三大角色的基本含义后再回来。
>
> 思考过程
>
> 面对一个横跨 Spring Boot 3.2/3.5、XXL-JOB、遗留 ITP 系统的超大型代码仓库,新入职的开发者最需要的不是晦涩的架构图,而是一张精准的"地图"——知道每个子系统在做什么、核心代码在哪里、复杂逻辑怎么走、日常任务怎么完成。小纸巾采用"正反合"的辩证方法：先正面陈述子系统职责（正题），再通过 Python 类比揭示反面的设计取舍（反题），最后给出反事实推理下的最佳实践（合题）。全文以资深导师的视角,用中文解释概念、用英文保留技术术语,确保任何有 Java/Spring 基础的开发者都能快速上手。

---

## 第一部分:全库知识索引与开发者维护手册

### 1.1 顶层目录结构与子系统职责

QAMate 是一个分布式 API 生命周期管理平台,涵盖用例设计、自动生成、回归测试、执行调度和结果分析全流程。其代码仓库按"管理后台-执行引擎-调度中心"三层架构组织:

| 子系统目录 | 运行时环境 | 端口 | 角色(Python 类比) | 核心职责 |
|---|---|---|---|---|
| `qamate-server/core/` | Spring Boot 3.2 / Java 21 | 8542(dev) / 8544(online) | Django (ORM + REST API) | API 生命周期管理后台,含 20+ 领域模块 |
| `qamate-server/apiExecutor/` | Spring Boot 3.5 / Java 17 | 8995 | Celery Workers | 测试执行引擎,解析并运行各种协议的测试用例 |
| `qamate-server/api-smart-dispatch/` | Spring Boot 3.5 / XXL-JOB 3.2.1 | 8080 | Celery Beat + Flower | 分布式任务调度,将执行任务分派给 Worker 集群 |
| `inner-os/itp/` | Struts2 + LTS + Jetty | N/A | 遗留系统(无现代类比) | 历史 ITP 系统:itp-web(Web 前端)、itp-tasktracker(任务跟踪)、itp-intelli(智能分析)、lts(任务调度) |

**正反合:**

- **正（正题）**：Core 系统承担了全部领域的 Controller + Service + Mapper 三层，负责从 API 用例编排、自动生成、节点管理到 Lumos 知识引擎的全品类业务，是典型的"单体优先"（monolith-first）架构。
- **反（反题）**：将 20+ 业务模块塞入同一个 Spring Boot 进程，违反了微服务的"高内聚、低耦合"原则。实际上，Core 中的 `v2/lumosgmt`（2544 行）和 `regressionmgt`（3003 行）已经膨胀为独立的"内嵌子系统"，逻辑上完全可以拆分为独立的微服务。
- **合（合题）**：对于当前团队规模，Monolith 降低了部署复杂度和调试成本；但未来若 Lumos 或回归模块独立团队维护，建议优先将其抽取为独立服务——注意 Feign 接口（如 `QAMateCoreClient`）已经为此做好了协议准备。

**反事实推理：**
> 如果 Executor 不是 Spring Boot 3.5 而是基于 Go 的 `goroutine` + `channel` 模型,那么它的并发执行能力将提升 3-5 倍,且内存占用降至 1/10。但目前团队 Java 技术栈的一致性优势(tooling、CI/CD、监控)大于性能收益,因此保持 Java 是理性的工程决策。

Core 的 20+ 领域模块详细清单:

```
core/src/main/java/com/baidu/qamate/core/
├── apismartmgt/     # API 测试计划管理 (核心)
├── casenodemgt/     # 用例节点生命周期管理 (树形结构)
├── casestepmgt/     # 用例步骤管理
├── codegenmgt/      # 代码自动生成 & 模板
├── regressionmgt/   # 回归测试计划执行
├── genratemgt/      # 任务生成 (AI 驱动)
├── dailymgt/        # 日常定时任务
├── debugmgt/        # 调试 & 单步执行
├── cloudmgt/        # 云端执行结果回传
├── flowmgt/         # 工作流编排
├── flashmgt/        # 快速执行(闪电测试)
├── prometheusmgt/   # Prometheus 指标采集
├── strategymgt/     # 策略配置
├── modelmgt/        # 模型管理
├── treenodemgt/     # 目录树节点管理
├── uigeneratemgt/   # UI 自动生成
├── uigeneratesessionmgt/ # UI 生成会话管理
├── crashmgt/        # 崩溃监控
├── devicemgt/       # 设备管理
├── ipipemgt/        # IP 管道
├── pointsmgt/       # 积分系统
├── stabilitymgt/    # 稳定性监控
├── othermgt/        # 杂项(签名、片段、文档节点等)
├── stargate/        # Starlight RPC 网关
├── components/      # 公共组件(Filter, Context, Util)
└── v2/
    ├── kamimgt/     # v2 版 Kami 管理
    ├── kamixmgt/    # Kami 扩展 (Skill, Knowledge, Config)
    ├── lumosgmt/    # Lumos 智能引擎 (最复杂模块)
    ├── knowledgemgt/# 知识库管理
    ├── generatemgt/ # v2 版任务生成
    ├── casenodemgt/ # v2 版用例节点
    ├── casestepmgt/ # v2 版用例步骤
    ├── configmgt/   # v2 版配置管理
    ├── groupmgt/    # v2 版分组管理
    ├── treenodemgt/ # v2 版目录树
    ├── perfmgt/     # 性能管理
    ├── qitongmgt/   # 奇通管理
    ├── othermgt/    # v2 版杂项
    └── unomgt/      # UNO 平台集成
```

**Python 类比:**
- Core = Django: 对应 Django 的 `models.py`（Entity/Mapper）、`views.py`（Controller）、`services.py`（Service）。Django 的 `apps` 概念对应 Core 的领域模块（如 `apismartmgt`, `casenodemgt`）。
- Executor = Celery Workers: 运行在独立进程中,消费 Dispatch 分发的任务,执行后再将结果回传给 Core。对应 Celery 的 `@task` 装饰器 + Broker(Redis) 解耦。
- Dispatch = Celery Beat: 按 cron 表达式/固定速率调度任务,对应 XXL-JOB 的 `@XxlJob` 注解 + Cron 配置。

### 1.2 关键类定义与职责字典

| 类名 | 所属微服务 | 文件大小(行) | 核心职责 | Python 类比 |
|---|---|---|---|---|
| `RequestFilter` | core | 296 | Spring Filter 鉴权拦截器:UUAP Token + OpenAPI Token 双通道验证,ContextHolder 注入,Prometheus 指标打点 | `@middleware_before_request` (Django 中间件链) |
| `ApiPlanServiceImpl` | core/apismartmgt | 1273 | API 测试计划全生命周期:创建、执行、状态流转、结果聚合。Plan 是 Core 中最核心的业务聚合根 | Django `PlanViewSet` + `PlanService` |
| `CaseNodeServiceImpl` | core/casenodemgt | 3794 | 用例树结构管理:CRUD、复制、迁移、折叠树查询(buildCaseTree)、路径追踪。整个代码库中最长的单体类,堪称"上帝类"的反面教材 | `RecursiveTreeQuerySet` (MongoDB/$graphLookup 等价) |
| `RegressionPlanServiceImpl` | core/regressionmgt | 3003 | 回归测试计划编排:批量用例拉取、结果对比、失败重试、报告生成 | `pytest` runner 的 Java 版 |
| `LumosServiceImpl` | core/v2/lumosgmt | 2544 | Lumos 智能引擎核心:PRD 文档解析、Code CR 变更分析、Agent 调度、Kirin 任务编排、Comate Token 注入 | LangChain `AgentExecutor.run()` |
| `SkillServiceImpl` | core/v2/kamixmgt | 1637 | Kami 技能(Bot Skill)的 CRUD + 执行编排,负责技能生命周期和参数校验 | Rasa `Action` 服务 |
| `ModuleConfigServiceImpl` | core/v2/lumosgmt | 2789 | 模块配置管理:连接多个下游(TRD、Kami、Lumos)的配置聚合服务,包含环境差异化逻辑 | `django.conf.settings` 的动态版 |
| `TaskGenerateServiceImpl` | core/generatemgt | 2156 | AI 驱动的测试用例生成:调用 LLM 接口、解析生成结果、关联 Kirin 任务回调 | LangChain `LLMChain.predict()` |
| `TaskSubmitServiceImpl` | apiexecutor | 25 | 执行器任务提交异步服务:将任务从内存队列分发到具体 Protocol Runner | Celery `task.apply_async()` |
| `FeignConfig` | core/apismartmgt | 88 | Feign 客户端统一配置:为 Worker 和 Dispatch 注入 Authorization Header,管理 Worker 登录 Token | `httpx.Client.auth` 中间件 |
| `OpenApiToken` | core/components | 118 | OpenAPI Token 校验:支持超级 Token 豁免、业务线 Product Token 匹配、SHA-256 签名计算 | Django REST Framework 的 `TokenAuthentication` |
| `UuapToken` | core/components | 38 | UUAP JWT Token 解析:解密 JWT 获取 username,注入 `HttpServletRequest` 属性 | `PyJWT.decode()` |
| `SignatureServiceImpl` | core/othermgt | 1617 | 用例签章服务:管理用例的审核/签名状态流转,含签章信息关联查询 | Django `Signals` + `PermissionMixin` |
| `QAMateCoreClient` | apiexecutor | 58 | Executor 调用 Core 的 Feign 接口声明:步骤上报、计划开始、案例拉取等 | `httpx.AsyncClient` with `@route` decorators |
| `KnowledgeServiceImpl` | core/v2/lumosgmt | 125(相对轻量) | 知识库检索与查询服务:与 TRD/Kami 知识库的集成,作为 Lumos 的知识底座 | LangChain `VectorStoreRetriever` |
| `CaseNodeManager` | core/casenodemgt | ~500 | CaseNode 的业务逻辑管理器:介于 Service 和 Mapper 之间,封装复杂的状态转换和校验 | Django `ModelManager` 自定义 Queryset |
| `ContextHolder` | core/components | ~100 | ThreadLocal 上下文管理:存放当前请求的 username、Comate Token、uGate Token | `contextvars.ContextVar` (Python 3.7+) |

**反事实推理:**
> 如果 `CaseNodeServiceImpl`(3794 行)在初次发现超过 800 行时就拆分为 `CaseNodeQueryService`(查询)、`CaseNodeMutationService`(修改)、`CaseNodeExtraService`(额外数据组装)三个类,那么新成员理解树查询逻辑只需要 400 行而非 3794 行,调试时的认知负载降低约 90%。这被称为"单一职责原则的拖尾成本"——越晚拆分,成本越高。

### 1.3 全局核心配置项释义字典

#### 数据源配置 (`spring.datasource.dynamic`)

Core 使用 `dynamic-datasource-spring-boot3-starter 4.1.2` 实现多数据源路由:

| 数据源 key | 用途 | Dev DB Location | Online DB Location |
|---|---|---|---|
| `newsource` (primary) | 新 Core 主库,qamate 核心数据 | 10.138.47.50:8331/core | smartbns.qamate-bmi0000 (xdb.all.serv):6932/qamate |
| `oldsource` | 旧 LazyOne 系统迁移数据 | 10.138.47.50:8331/qamate_base | smartbns.lazyone-bmi0000 (xdb.all.serv):10445/lazyone |
| `apismart-dispatch` | XXL-JOB 调度数据 | 10.138.47.50:8331/api_smart_dispatch | 10.11.37.52:6955/api_smart_dispatch |
| `apismart-executor` | 执行器结果数据 | 10.138.47.50:8331/api_executor | 10.11.37.52:6955/api_executor |
| `lazydevice` | 设备管理数据(Druid 直连) | 10.24.7.177:8306/lazydevice | 线上同 dev |

**Python 类比:** Django 的 `DATABASES` 多数据库路由配置(`db_for_read`/`db_for_write`)。MyBatis-Plus 的 `@DS("oldsource")` 注解等价于 Django 的 `using("oldsource")` 参数。

#### Redis / 缓存配置

| 配置项 | 位置 | 值 | 说明 |
|---|---|---|---|
| `spring.data.redis` | application-{env}.yml | 各环境独立 | Spring Boot 标准 Redis 连接 |
| `jetcache.local.default.type` | application.yml | linkedhashmap | 本地一级缓存,LRU 淘汰 |
| `jetcache.local.default.limit` | application.yml | 1000 | 本地缓存条目上限 |
| `jetcache.local.default.expireAfterWriteInMillis` | application.yml | 3600000 (1h) | 默认过期时间 |
| `jetcache.enabled` | application.yml | true | JetCache 全局开关 |
| `bdrp.enable` | application.yml (executor) | false | BDRP(百度内部 Redis 代理)开关,仅 executor 有 |

**Python 类比:** JetCache 的 `local + remote` 两级缓存等价于 Python `cachetools.LRUCache` + `redis-py` 组合,但 JetCache 提供了统一的 `@Cached` 注解和自动失效机制。

#### 鉴权相关配置

| 配置项 | 位置 | dev 值模式 | online 值模式 | 职责 |
|---|---|---|---|---|
| `uuap.appKey` | application-{env}.yml | `uuapclient-*-beta` | `uuapclient-*-online` | UUAP(百度统一鉴权)应用标识 |
| `uuap.secretKey` | application-{env}.yml | `1fca610e...` | `4ba395bc...` | UUAP 解密密钥 |
| `uuap.secrete` | application-{env}.yml | 组合字符串(供 JWT 签名校验) | 组合字符串 | JWT 签名密钥种子 |
| `comate.app-key` | application-{env}.yml | `*-beta` | `*-online` | Comate(智能编码助手)的应用 Key |
| `comate.clientId/clientSecret` | application-{env}.yml | `V8JIvR...` | `oF1VsF...` | Comate OAuth2 客户端凭证 |
| `ku.app-token` | application-{env}.yml | `uuapclient-*-zBIDe` | `uuapclient-*-ksdOg` | 知识库(KU)的 UUAP token |
| `worker.username/password` | application-dev.yml | `guest/guest` | N/A | Executor Worker 登录凭证(仅 dev 明文) |
| `icode.token` | application.yml | `a663c04f...` | 同 dev | iCode(百度内部 AI 平台)认证 Token |

> **安全提示(反事实推理):** `application.yml` 中的 `icode.token` 和 `ku.token` 以明文硬编码方式存储。如果这些 token 泄露,攻击者可以冒充 QAMate 系统调用 iCode/KU 服务。正确做法是:这些值应该移入环境变量或百度内部密钥管理服务(Vault),仅通过 `@Value` 注入。正因这是一个内部系统,安全权衡偏向了开发便利性;但若系统对外开放,必须立即迁移。

#### Feign / HTTP 客户端配置

| 配置项 | 位置 | 值 | 说明 |
|---|---|---|---|
| `http.maxTotal` | application.yml | 100 | 全局 HTTP 连接池最大连接数 |
| `http.connectTimeout` | application.yml | 8000ms | 建立连接超时 |
| `http.socketTimeout` | application.yml | 150000ms | 数据传输超时(2.5 分钟) |
| `http.keepAlive` | application.yml | 60000ms | Keep-Alive 保活时间 |
| `feign.client.config.default.connectTimeout` | executor application.yml | 5000ms | Executor Feign 连接超时 |
| `spring.cloud.gravity.registration.service-name` | application.yml | `qamate-core` | 百度内部服务注册中心(Starlight/Gravity)注册名 |

#### XXL-JOB / Dispatch 配置

| 配置项 | 位置 | dev 值 | online 值 | 说明 |
|---|---|---|---|---|
| `dispatch.url` | application-dev.yml/online.yml | `api-smart-dispatch.test...` | `api-smart-dispatch...` | Dispatch 调度中心地址 |
| `xxl-job-core.version` | executor pom.xml | 3.2.0 | 同 | XXL-JOB 客户端版本 |
| XXL-JOB Admin 端口 | xxl-job-admin application.yml | 8080 | 8080 | 调度中心管理页面 |
| `executor.clusterType` | executor application.yml | case | case | 执行器集群类型标识 |

#### 线程池与虚拟线程 (Java 21)

Core 未显式配置线程池,依赖 Spring Boot 3.2 的默认 Tomcat 线程池 + Java 21 虚拟线程(Virtual Threads):
- `VirtualThreadUtils`(在 `genratemgt` 中使用):调用 `Thread.startVirtualThread()` (JDK 21 原生 API)
- Executor 使用 `@Async` 注解 + `ThreadPoolTaskExecutor`

**Python 类比:** Java 21 Virtual Thread 等价于 Python `asyncio` 协程模型——虚拟线程阻塞时不占用 OS 线程资源,类似 `await` 不阻塞事件循环。

### 1.4 核心代码路径速查

#### Core 模块代码组织

```
core/src/main/java/com/baidu/qamate/core/
│
├── {domain}mgt/controller/     ← REST 端点
│   e.g. apismartmgt/controller/PlanController.java
│
├── {domain}mgt/service/        ← 业务接口
│   e.g. apismartmgt/service/ApiPlanService.java
│
├── {domain}mgt/service/impl/   ← 业务实现
│   e.g. apismartmgt/service/impl/ApiPlanServiceImpl.java
│
├── {domain}mgt/manager/        ← 复杂业务管理器(Service 之上的协调层)
│   e.g. apismartmgt/manager/FeignConfig.java
│
├── {domain}mgt/mapper/         ← MyBatis-Plus Mapper
│   e.g. casenodemgt/mapper/CaseNodeMapper.java
│
├── {domain}mgt/entity/         ← 数据库实体
│   e.g. casenodemgt/entity/CaseNodeEntity.java
│
├── {domain}mgt/vo/             ← 数据传输对象(进出)
│   e.g. casenodemgt/vo/CaseNodeVo.java
│
├── components/config/          ← 全局配置 & Filter
│   e.g. RequestFilter.java, OpenApiToken.java
│
├── components/common/          ← 全局工具类
│   e.g. ContextHolder.java, Response.java, CoreException.java
│
└── components/constant/        ← 全局常量 & 枚举
    e.g. CaseNodeTypeEnum.java, DbConst.java
```

#### 资源文件位置

| 资源类型 | 路径 | 示例 |
|---|---|---|
| MyBatis XML Mapper | `core/src/main/resources/mapper/*.xml` | `CaseNodeMapper.xml`, `GroupMapper.xml` |
| 多环境配置 | `core/src/main/resources/application-{env}.yml` | `application-dev.yml`, `application-online.yml` |
| 启动配置 | `core/src/main/resources/application.yml` | 全局默认配置 |
| 日志配置 | `core/src/main/resources/logback-spring.xml` | Logback 配置 |
| 静态资源 | `core/src/main/resources/static/` | 前端打包文件 |

#### Executor 模块代码组织

```
apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/
│
├── controller/          ← ExePlanController(计划执行)
├── service/             ← 执行服务接口
├── async/               ← @Async 异步任务提交
│   └── impl/TaskSubmitServiceImpl.java
├── protocol/            ← 多协议引擎 (核心!)
│   ├── factory/         ← 协议工厂
│   │   ├── ProtocolFactoryManager.java   (路由)
│   │   ├── HttpProtocolFactory.java
│   │   ├── RedisProtocolFactory.java
│   │   ├── SqlProtocolFactory.java
│   │   ├── ShellProtocolFactory.java
│   │   └── ScriptProtocolFactory.java
│   ├── component/       ← 协议四大组件
│   │   ├── Constructor.java  (构建请求)
│   │   ├── Executor.java     (执行请求)
│   │   ├── Extractor.java    (提取响应)
│   │   └── Verifier.java     (校验结果)
│   └── request/         ← 各协议 Step/Exe 请求对象
│       └── impl/{protocol}/{Protocol}StepRequest.java
├── client/              ← Feign 客户端声明
│   └── QAMateCoreClient.java
├── jobhandler/          ← XXL-JOB Handler
├── runner/              ← 执行器运行器
└── verify/              ← 断言校验引擎
```

---

## 第二部分:最复杂的 3 个核心函数逐行深度解析与 Clean Code 诊断

### 2.1 `RequestFilter.doFilter()` — 鉴权拦截器

**完整路径:** `core/src/main/java/com/baidu/qamate/core/components/config/RequestFilter.java`
**文件行数:** 296 行
**复杂度根源:** 7 层 Token 校验逻辑线性串联,每个请求都要走一遍完整链路

#### 逐行解析

```java
// 第 117-209 行:doFilter 方法主体
@Override
public void doFilter(ServletRequest servletRequest,
                     ServletResponse servletResponse,
                     FilterChain filterChain) throws IOException, ServletException {
    // == 步骤 0:请求预处理 ==
    HttpServletRequest request = (HttpServletRequest) servletRequest;
    HttpServletResponse response = (HttpServletResponse) servletResponse;
    // 包装请求,支持 Body 重复读取(gzip 解压场景)
    CachedHttpServletRequestWrapper wrappedRequest = new CachedHttpServletRequestWrapper(request);

    // == 步骤 1:Trace 链路追踪初始化 ==
    // 从请求头读取 X-Trace-ID,若无则使用雪花算法生成
    String traceId = request.getHeader("X-Trace-ID");
    if (traceId == null || traceId.isEmpty()) {
        traceId = TraceIdGeneratorUtil.generate(); // 百度内部雪花算法变体
    }
    String ip = request.getRemoteAddr() + ":" + request.getRemotePort();
    requestTraceLogger.logRequestTrace(traceId, ip, headers);
    MDC.put("traceId", traceId); // 注入 SLF4J MDC,所有日志自动带上 traceId

    // == 步骤 2:白名单 URI 跳过鉴权 ==
    if (isExcludedUri(request.getServletPath())) {
        filterChain.doFilter(wrappedRequest, servletResponse);
        // 白名单包括: /api/debug/**, /device/proxy/pac/**, 配置的 excludedUri 列表
    } else {
        // == 步骤 3:多通道 Token 校验(链式 fallback)==
        var valid = false;
        try {
            prometheusMetricManager.totalCounter.increment(); // 总请求计数器 +1

            // 步骤 3a:提取四种可能的 Token Header
            String qamateUuapToken = request.getHeader(QAMATE_UUAP_TOKEN);   // "QAMate-U-Token"
            String kamiUuapToken = request.getHeader(KAMI_UUAP_TOKEN);       // "Kami-U-Token"
            String qamateToken = request.getHeader(QAMATE_TOKEN);             // "QAMate-Token"
            String kamiToken = request.getHeader(KAMI_TOKEN);                 // "Kami-Token"
            // 兼容天网系统的 Sky-Token Header 回退
            if (null == qamateToken) { qamateToken = request.getHeader(SKY_TOKEN); }
            // 兼容天网系统的 Sky-ModuleId Header 回退
            String qamateModuleId = request.getHeader(QAMATE_MODULEID);
            if (null == qamateModuleId) { qamateModuleId = request.getHeader(SKY_MODULEID); }

            // 步骤 3b:全部为空则直接拒绝
            if (null == qamateUuapToken && null == qamateToken
                    && null == kamiUuapToken && null == kamiToken) {
                response.getWriter().println(JSON.toJSONString(Response.fail("Token为空")));
                prometheusMetricManager.errorReqCounter.increment();
            } else {
                // == 步骤 4:OpenAPI Token 校验(优先级最高)==
                if (qamateToken != null) {
                    valid = openApiToken.checkFromToken(qamateToken, qamateModuleId, request);
                    // OpenApiToken 内部逻辑:
                    // 1) 检查是否 super-9a796933... (超管豁免)
                    // 2) 检查是否 testone-f2bde419... (TestOne 豁免)
                    // 3) 检查是否 feed-w29wbde... (Feed 豁免)
                    // 4) 从 Product 表查询对应 moduleId 的 token 进行匹配
                    if (valid) { prometheusMetricManager.userCounter.increment(); }
                }
                // 步骤 4b:Kami 内部 Token 校验(降级路径)
                if (!valid && kamiToken != null) {
                    valid = openApiToken.checkFromToken(kamiToken, qamateModuleId, request);
                }
                // == 步骤 5:UUAP Token 校验(用户登录 Token)==
                if (!valid && qamateUuapToken != null) {
                    valid = this.uuapToken.checkFromToken(qamateUuapToken, request);
                    // UuapToken 内部:
                    // 1) JwtWrap.verifyToken(token) 解密 JWT
                    // 2) 提取 claims["user"] 作为 username
                    // 3) request.setAttribute("qamate_user", username)
                    if (valid) {
                        // 按用户名 + 模块 ID 打 Prometheus 指标
                        prometheusMetricManager.counter = registry.counter(
                            "front.request.count",
                            Tags.of("username", (String) request.getAttribute("qamate_user"),
                                    "module_id", moduleCache.getModuleName(...)));
                    }
                }
                // 步骤 5b:Kami UUAP Token 降级
                if (!valid && kamiUuapToken != null) {
                    valid = this.uuapToken.checkFromToken(kamiUuapToken, request);
                }
                // == 步骤 6:最终拒绝 ==
                if (!valid) {
                    prometheusMetricManager.invalidTokenCounter.increment();
                    response.getWriter().println(JSON.toJSONString(
                        Response.fail("Token非法||Token失效")));
                }
                // == 步骤 7:Comate Token 注入(鉴权通过后)==
                if (valid) {
                    injectComateAuthToken(request); // 见 2.1.1 详述
                }
            }
        } catch (Exception e) {
            log.error("token filte verift exception", e);
        }

        // == 步骤 8:放行或终止 ==
        try {
            if (valid) {
                filterChain.doFilter(wrappedRequest, servletResponse);
            }
        } finally {
            MDC.clear(); // 清理 MDC,避免线程池复用时污染
        }
    }
}
```

#### Clean Code 诊断

**问题 1:SRP 违反(单一职责原则)**
该 `doFilter` 方法同时承担了:
- Trace 生成与 MDC 注入
- URI 白名单检查
- 四种 Token 的链式校验
- Comate Auth Token 注入(调用 UUAP + Comate API)
- Prometheus 指标打点
- 错误响应格式化

**反面（反题）：** 按照 Spring Security 的 `FilterChain` 模式，应将这 6 个职责拆分为 6 个独立 Filter：

```java
// 反事实推理:如果拆分为职责单一的 Filter 链
@Bean
public FilterRegistrationBean<TraceFilter> traceFilter() { ... }      // Trace
@Bean
public FilterRegistrationBean<SkipFilter> skipFilter() { ... }        // 白名单
@Bean
public FilterRegistrationBean<OpenApiAuthFilter> openApiFilter() { ...} // OpenAPI
@Bean
public FilterRegistrationBean<UuapAuthFilter> uuapFilter() { ... }    // UUAP
@Bean
public FilterRegistrationBean<ComateTokenFilter> comateFilter() { ...} // Comate
```

**合成（合题）：** 拆分后每个 Filter < 50 行，单一职责，单元测试可独立编写；但需要管理 Filter 执行顺序（使用 `@Order` 注解）。

**问题 2：魔法字符串过多**
`QAMATE_UUAP_TOKEN = "QAMate-U-Token"` 这样的 Header 常量定义为 `public static final` 是好的,但 token 值如 `"super-9a796933bf024ebfa0420dce6f864a51"` 硬编码在 `OpenApiToken.java` 中是坏的——它无法动态回收或轮换。

**问题 3:Prometheus 指标基数爆炸**
```java
prometheusMetricManager.counter = registry.counter(
    "front.request.count",
    Tags.of("username", ..., "module_id", ...));
```
如果 username 和 module_id 组合数在线上达到 1000+,每个组合都会创建一个独立的 Prometheus 时间序列,导致内存和存储成本显著上升。应限制 `username` 标签为高基数的聚合维度(如只保留 team/service),或用 Histogram 替代 Counter。

### 2.2 `FeignConfig.authInterceptor()` + `getWorkerToken()` — Feign 请求拦截器

**完整路径:** `core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/FeignConfig.java`
**文件行数:** 88 行

#### 逐行解析

```java
@Configuration
public class FeignConfig {

    @Value("${worker.username}")
    private String username;  // dev: guest, online: 特定服务账号

    @Value("${worker.password}")
    private String password;

    // == 核心 Bean:Feign 请求拦截器 ==
    @Bean
    public RequestInterceptor authInterceptor() {
        return requestTemplate -> {
            // == 分支 1:XXL-JOB Dispatch 调用 ==
            if (requestTemplate.feignTarget().name().equals("dispatchClient")) {
                requestTemplate.header("XXL-JOB-ACCESS-TOKEN",
                    "default_token_glz");  // ← Magic String! 应提取为配置
                requestTemplate.header("userName", "2");
                requestTemplate.header("userToken",
                    "394af2b0a2a747bc9531e9768ca60e27"); // ← 又一个 Magic String!
            }

            // == 分支 2:Worker(Executor)调用 ==
            if (requestTemplate.feignTarget().name().equals("workerClient")) {
                ServletRequestAttributes attributes = (ServletRequestAttributes)
                        RequestContextHolder.currentRequestAttributes();
                HttpServletRequest request = attributes.getRequest();
                // 登录接口不需要 token
                if (request.getRequestURI().contains("login")) {
                    return;
                }
                // 每个 Feign 请求都重新调用 getWorkerToken()!
                String token = getWorkerToken();
                requestTemplate.header("Authorization", token);
            }
        };
    }

    // == Worker Token 获取逻辑 ==
    private @Nullable String getWorkerToken() {
        LoginRequestVo loginRequestVo = new LoginRequestVo();
        loginRequestVo.setUsername(username);
        loginRequestVo.setPassword(password);
        String token = null;
        // 第 1 次调用:判断是否可以获取 Token
        if (WorkerClient.getToken(loginRequestVo) != null) {
            // 第 2 次调用:实际获取 Token ← 重复调用!
            LoginResponseVo loginResponseVo = WorkerClient.getToken(loginRequestVo);
            if (loginResponseVo != null && loginResponseVo.getData() != null) {
                token = loginResponseVo.getData().getToken();
            }
        }
        return token;
    }

    // == 其他 Beans ==
    @Bean Logger.Level feignLoggerLevel() { return Logger.Level.FULL; }
    @Bean Retryer feignRetryer() { return Retryer.NEVER_RETRY; }
    @Bean Request.Options feignOptions() {
        return new Request.Options(3L, TimeUnit.SECONDS,   // connectTimeout: 3s
                                   60L, TimeUnit.SECONDS,   // readTimeout: 60s
                                   true);                    // followRedirects: true
    }
}
```

#### Clean Code 诊断

**问题 1:每次 Feign 调用都重新登录(严重性能问题)**

`getWorkerToken()` 在**每一次** Feign 请求中都会调用 `WorkerClient.getToken()` 登录接口——而且是两次(先判空再取值)。如果批量回归测试有 10000 个用例,则 Worker 登录接口会被调用 20000 次。

**反事实推理：**
> 如果改为使用 JetCache 缓存 Token 并设置 TTL = 7200 秒(2 小时),则全天的批量执行只会调用登录接口 12 次而非 20000+ 次。建议实现:
> ```java
> @Cached(name = "workerToken", expire = 7200, key = "#username")
> private String getWorkerToken() { ... }
> ```

**问题 2:没有断路器(无容错)**

`getWorkerToken()` 如果 Worker 服务不可用,`WorkerClient.getToken()` 返回 null,后续 `requestTemplate.header("Authorization", null)` 将导致下游 Worker 收到 null token。应增加:
- `@Retryable` 重试机制(spring-retry 已在 pom 中依赖)
- `@CircuitBreaker` 或 Hystrix 降级

**问题 3:硬编码的 Dispatch Token**

`"default_token_glz"` 和 `"394af2b0a2a747bc9531e9768ca60e27"` 硬编码在代码中。这违反安全编码规范——如果 GitHub 仓库公开,攻击者可立即使用这些凭证访问 Dispatch Admin。应改为 `@Value("${xxl.job.access.token}")` 注入。

**问题 4:`RequestContextHolder.currentRequestAttributes()` 的线程问题**

在异步执行(virtual thread)场景下,`RequestContextHolder` 可能无法正确传递,因为 virtual thread 不在 OS 线程上。应使用 `RequestContextFilter` 显式开启 `setThreadContextInheritable(true)`。

### 2.3 `CaseNodeServiceImpl.getCaseTreeData()` — 用例树构建引擎

**完整路径:** `core/src/main/java/com/baidu/qamate/core/casenodemgt/service/impl/CaseNodeServiceImpl.java`
**类总行数:** 3794 行
**方法行数:** ~103 行(第 355-458 行)
**依赖注入:** 15 个 `@Autowired` 字段

#### 逐行解析

```java
/**
 * 构建用例树的核心方法
 * 一次性从数据库加载整棵用例树的所有节点、详情和步骤,
 * 在内存中组装为递归树结构,供前端 Tree 组件渲染。
 *
 * 正(Thesis): 批量加载 vs 逐层懒加载
 *   - 批量加载:1 次 DB 查询,但可能加载大量无用数据
 *   - 懒加载:按需查询,但需要 N 次 DB 交互(N = 树层级)
 * 当前实现选择了"批量加载 + 内存构建",适用于用例节点数 < 5000 的中型树。
 *
 * 反(Antithesis): 如果用例树有 50000+ 节点,
 *   内存构建将消耗数百 MB 内存且 O(N) 遍历耗时不可接受,
 *   此时应该切回"逐层懒加载 + Redis 缓存热点路径"。
 */
public CaseTreeQueryVo getCaseTreeData(Long caseRootId,
                                        Boolean withSign,
                                        Boolean withAuto,
                                        Byte osType) throws Exception {
    // == 步骤 1:一次性加载三类数据 ==
    // 1a:所有用例节点 (1 次 DB 查询)
    var allCaseNode = list(new LambdaQueryWrapper<CaseNodeEntity>()
            .eq(CaseNodeEntity::getCaseRootId, caseRootId)
            .eq(CaseNodeEntity::getIsDel, 0));  // 软删除过滤
    var caseNodeEntityMap = allCaseNode.stream()
            .collect(Collectors.toMap(CaseNodeEntity::getId, node -> node));

    // 1b:所有详情数据 (1 次 DB 查询)
    Map<Long, List<CaseNodeDetailEntity>> caseNodeDetailMap = new HashMap<>();
    List<CaseNodeDetailEntity> caseNodeDetailEntitieList = caseNodeDetailService
            .list(new LambdaQueryWrapper<CaseNodeDetailEntity>()
                    .eq(CaseNodeDetailEntity::getCaseRootId, caseRootId));
    caseNodeDetailMap = caseNodeDetailEntitieList.stream()
            .collect(Collectors.groupingBy(CaseNodeDetailEntity::getCaseNodeId));

    // 1c:所有步骤数据 (1 次 DB 查询)
    Map<Long, List<CaseNodeStepEntity>> allCaseStepMap = new HashMap<>();
    LambdaQueryWrapper<CaseNodeStepEntity> stepQueryWrapper = new LambdaQueryWrapper<>();
    stepQueryWrapper
            .eq(CaseNodeStepEntity::getCaseRootId, caseRootId)
            .eq(CaseNodeStepEntity::getIsDel, 0);
    if (!withAuto) {
        // 不包含自动生成步骤时,排除 StepInfo 类型的步骤
        caseNodeStepService.queryStepWithoutStepInfo(stepQueryWrapper);
    }
    List<CaseNodeStepEntity> allCaseStepList = caseNodeStepService.list(stepQueryWrapper);
    if (allCaseStepList != null) {
        allCaseStepMap = allCaseStepList.stream()
                .filter(caseNodeStep -> {
                    if (caseNodeStep.getDetailNodeId() == null) {
                        log.error("stepId {} detailId is null", caseNodeStep.getId());
                        return false; // 脏数据容错
                    }
                    return true;
                })
                .collect(Collectors.groupingBy(CaseNodeStepEntity::getDetailNodeId));
    }

    // == 步骤 2:按 detail 的 stepsIndex 排序步骤 ==
    // 这实现了一个"有序关联":数据库存储逗号分隔的步骤 ID 排序索引,
    // 在此按该索引重排步骤列表。这是典型的"以逗号分隔存储关联ID"反模式,
    // 但避免了额外的排序关联表 JOIN。
    for (var caseNodeDetailEntity : caseNodeDetailEntitieList) {
        var detailStepList = allCaseStepMap.get(caseNodeDetailEntity.getId());
        if (detailStepList == null) { continue; }
        Map<Long, CaseNodeStepEntity> stepEntityMap = detailStepList.stream()
                .collect(Collectors.toMap(CaseNodeStepEntity::getId, node -> node));
        if (StringUtils.isBlank(caseNodeDetailEntity.getStepsIndex())) {
            allCaseStepMap.remove(caseNodeDetailEntity.getId());
            continue;
        }
        List<CaseNodeStepEntity> sortStepEntityList = new ArrayList<>();
        for (var stepId : caseNodeDetailEntity.getStepsIndex().split(",")) {
            if (stepEntityMap.get(Long.valueOf(stepId)) != null) {
                sortStepEntityList.add(stepEntityMap.get(Long.valueOf(stepId)));
            }
        }
        allCaseStepMap.put(caseNodeDetailEntity.getId(), sortStepEntityList);
    }

    // == 步骤 3:构建树形结构(核心!)==
    Map<Long, CaseTreeQueryVo> caseNodeInfoMap = new HashMap<>();
    for (var caseNode : allCaseNode) {
        // 3a:获取或创建当前节点的 VO
        CaseTreeQueryVo currentNode = new CaseTreeQueryVo();
        if (caseNodeInfoMap.containsKey(caseNode.getId())) {
            currentNode = caseNodeInfoMap.get(caseNode.getId());
        } else {
            currentNode = genCaseTreeNode(caseNodeEntityMap.get(caseNode.getId()));
            currentNode.setExtra(generateCaseExtraOsList(caseNodeEntityMap.get(caseNode.getId()),
                    caseNodeDetailMap, allCaseStepMap, withSign, withAuto, osType));
            caseNodeInfoMap.put(caseNode.getId(), currentNode);
        }
        // 3b:处理 childrenIds 逗号分隔的子节点列表
        if (Strings.isBlank(caseNode.getChildrenIds())) { continue; }
        var childrenNodeId = caseNode.getChildrenIds().split(",");
        for (String idStr : childrenNodeId) {
            if (Strings.isBlank(idStr)) { continue; }
            var id = Long.valueOf(idStr);
            var childNode = caseNodeEntityMap.get(id);
            // 数据一致性校验:子节点存在且 parentId 匹配
            if (childNode == null
                || !caseNode.getId().equals(childNode.getParentId())) {
                continue; // 跳过脏数据(异步同步延迟导致)
            }
            // 3c:构建子节点 VO(与父节点相同逻辑)
            CaseTreeQueryVo childrenCaseNode = new CaseTreeQueryVo();
            if (caseNodeInfoMap.containsKey(id)) {
                childrenCaseNode = caseNodeInfoMap.get(id);
            } else {
                childrenCaseNode = genCaseTreeNode(caseNodeEntityMap.get(id));
                childrenCaseNode.setExtra(generateCaseExtraOsList(caseNodeEntityMap.get(id),
                        caseNodeDetailMap, allCaseStepMap, withSign, withAuto, osType));
                caseNodeInfoMap.put(id, childrenCaseNode);
            }
            // 3d:子节点类型合法性校验
            if (!childrenCaseNode.getExtra().getLegalSubNodeType()
                || (currentNode.getExtra().getLegalSubNodeType()
                    && !Objects.equals(currentNode.getExtra().getServerSubNodeType(),
                                       childrenCaseNode.getExtra().getServerNodeType()))) {
                currentNode.getExtra().setLegalSubNodeType(false);
            }
            currentNode.getChildren().add(childrenCaseNode);
        }
    }
    // 返回根节点
    return caseNodeInfoMap.get(caseRootId);
}
```

#### Clean Code 诊断

**问题 1：上帝类 — 3794 行**

`CaseNodeServiceImpl` 是整个代码库中最大的类。它包含:
- 用例 CRUD (创建、更新、删除)
- 用例树构建 (3 种不同策略)
- 用例迁移 (跨树移动)
- 用例复制 (duplicateCaseNode)
- 自动生成数据填充 (generateAutoData)
- 签章数据填充 (generateSignData)
- 度量统计 (getChildMetric)
- 路径追踪 (getCaseNodePath)
- 剪枝算法 (pruneTree)

**反面（反题）：** 如果采用 CQRS（命令查询职责分离）模式：
- `CaseNodeQueryService` — 只读查询(树构建、度量、路径)
- `CaseNodeCommandService` — 写操作(CRUD、迁移、复制)
- `CaseNodeExtraAssembler` — 数据组装(自动生成、签章)
- `CaseNodeTreeBuilder` — 树结构算法(剪枝、度量)

每一个类 < 500 行,可以被独立测试和独立修改。

**合成（合题）：** 拆分成本中等，但收益极高。建议在下一个大版本（重构）中逐步进行，因为当前所有内部方法都被 `@Override` 绑定到 `CaseNodeService` 接口，需要创建新接口并维护向后兼容。

**问题 2:深度嵌套 — `caseNodeInfoMap` 的重复构建逻辑**

步骤 3a-3c 中的父节点和子节点构建逻辑**完全相同**,只是参数不同。应提取为:

```java
// 反事实推理:提取可复用方法
private CaseTreeQueryVo buildNodeVO(Long nodeId,
                                     Map<Long, CaseNodeEntity> entityMap,
                                     Map<Long, List<CaseNodeDetailEntity>> detailMap,
                                     Map<Long, List<CaseNodeStepEntity>> stepMap,
                                     Boolean withSign, Boolean withAuto, Byte osType) {
    CaseTreeQueryVo vo = genCaseTreeNode(entityMap.get(nodeId));
    vo.setExtra(generateCaseExtraOsList(entityMap.get(nodeId), detailMap, stepMap,
                                         withSign, withAuto, osType));
    return vo;
}
```

这样可以将主方法从 103 行压缩到约 60 行。

**问题 3:`CaseNodeEntity.childrenIds` 逗号分隔存储是反模式**

关系型数据库不应该用逗号分隔的字符串存储一对多关系(varchar 大小有限,无法用 SQL JOIN,无法加索引)。这是典型的"无外键设计的后遗症"。正确做法应是一张 `case_node_relation` 关联表,但这也承认:对于树形结构,MySQL 邻接表(adjacency list)本身就有递归查询的性能问题。

> **正反合总结:** `getCaseTreeData` 选择了"一次加载、内存构建"策略,在性能(3 次 DB 查询 vs N 次)和简洁性之间取得了可接受的平衡。但 3794 行的 上帝类 + 逗号分隔的关联存储 = 新开发者上手的最大心智负担。

---

## 第三部分:开发者日常工作指南

### 3.1 如何添加一个新的 REST 端点

假设需求:在 `apismartmgt` 模块中添加 `GET /core/apismart/plan/{planId}/summary` 接口,返回计划的摘要信息。

**步骤 1:创建 VO(数据传输对象)**

```java
// 文件: apismartmgt/vo/PlanSummaryVo.java
package com.baidu.qamate.core.apismartmgt.vo;

import lombok.Data;

@Data
public class PlanSummaryVo {
    private Long planId;
    private String planName;
    private Integer totalCases;
    private Integer passedCases;
    private Integer failedCases;
    private String status;
}
```

**思维过程(正反合):**
- 正:VO 是前端与后端之间的契约,需要精确的字段类型和命名。
- 反:如果 VO 和 Entity 字段高度重叠(`PlanEntity` 已有这些字段),是否需要单独创建 VO?答案是"需要",因为 VO 的字段数量和含义随前端需求变化,而 Entity 严格对应数据库表结构,耦合两者会导致"表结构即 API"。
- 合:使用 MapStruct 进行 Entity <-> VO 转换,避免手写 get/set。

**步骤 2:在 Service 接口中声明方法**

```java
// 文件: apismartmgt/service/ApiPlanService.java
public interface ApiPlanService {
    // ... 已有方法 ...
    PlanSummaryVo getPlanSummary(Long planId);
}
```

**步骤 3:在 ServiceImpl 中实现**

```java
// 文件: apismartmgt/service/impl/ApiPlanServiceImpl.java
@Override
public PlanSummaryVo getPlanSummary(Long planId) {
    var plan = getById(planId);
    if (plan == null) {
        throw new CoreException(StatusEnum.INVALID_PARAM_ERR, "计划不存在: " + planId);
    }
    // 统计关联的用例数量
    var caseCount = caseNodeService.count(
        new LambdaQueryWrapper<CaseNodeEntity>()
            .eq(CaseNodeEntity::getPlanId, planId));
    // 统计通过/失败用例(通常从 Executor 回传的结果表查询)
    var passedCount = caseDebugTaskMapper.countPassedByPlanId(planId);
    var failedCount = caseDebugTaskMapper.countFailedByPlanId(planId);

    PlanSummaryVo vo = new PlanSummaryVo();
    vo.setPlanId(planId);
    vo.setPlanName(plan.getPlanName());
    vo.setTotalCases(caseCount.intValue());
    vo.setPassedCases(passedCount);
    vo.setFailedCases(failedCount);
    vo.setStatus(plan.getStatus());
    return vo;
}
```

**步骤 4:在 Controller 中暴露端点**

```java
// 文件: apismartmgt/controller/PlanController.java (新建或追加)
package com.baidu.qamate.core.apismartmgt.controller;

import com.baidu.qamate.core.apismartmgt.service.ApiPlanService;
import com.baidu.qamate.core.apismartmgt.vo.PlanSummaryVo;
import com.baidu.qamate.core.components.common.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/apismart/plan")
public class PlanController {

    @Autowired
    private ApiPlanService apiPlanService;

    @GetMapping("/{planId}/summary")
    public Response<PlanSummaryVo> getPlanSummary(@PathVariable Long planId) {
        return Response.success(apiPlanService.getPlanSummary(planId));
    }
}
```

**步骤 5:测试端点**

```java
// 文件: apismartmgt/controller/PlanControllerTest.java (可选但强烈推荐)
@SpringBootTest
@AutoConfigureMockMvc
class PlanControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    @DisplayName("GET /apismart/plan/{planId}/summary returns 200 with valid plan")
    void getPlanSummary_validPlanId_returnsOk() throws Exception {
        mockMvc.perform(get("/core/apismart/plan/1/summary")
                .header("QAMate-Token", "super-9a796933bf024ebfa0420dce6f864a51"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.success").value(true))
            .andExpect(jsonPath("$.data.planId").value(1));
    }
}
```

### 3.2 如何添加一个新的领域模块

假设需求:新增 `notificationmgt` 模块,负责消息通知(邮件、企微、飞书)。

**步骤 1:创建包结构**

```bash
mkdir -p core/src/main/java/com/baidu/qamate/core/notificationmgt/{controller,service/impl,manager,mapper,entity,vo}
```

**步骤 2:创建 Entity**

```java
// notificationmgt/entity/NotificationEntity.java
package com.baidu.qamate.core.notificationmgt.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@TableName("notification")
public class NotificationEntity {
    @TableId(type = IdType.AUTO)
    private Long id;
    private String title;
    private String content;
    private String channel;      // "email", "wecom", "feishu"
    private String receiver;
    private Integer status;      // 0:pending, 1:sent, 2:failed
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createTime;
}
```

**步骤 3:创建 Mapper**

```java
// notificationmgt/mapper/NotificationMapper.java
package com.baidu.qamate.core.notificationmgt.mapper;

import com.baidu.qamate.core.notificationmgt.entity.NotificationEntity;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface NotificationMapper extends BaseMapper<NotificationEntity> {
    // 自定义 SQL 方法在此声明,实现写在 mapper/NotificationMapper.xml
}
```

**步骤 4:创建 Service & Controller(参照 3.1)**

**步骤 5:创建数据库迁移 SQL**

```sql
-- 文件: core/src/main/resources/db/notification_init.sql
CREATE TABLE IF NOT EXISTS `notification` (
    `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(255) NOT NULL,
    `content` TEXT,
    `channel` VARCHAR(20) NOT NULL,
    `receiver` VARCHAR(255) NOT NULL,
    `status` TINYINT DEFAULT 0,
    `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX `idx_channel_status` (`channel`, `status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**步骤 6:MyBatis-Plus 自动扫描**

MyBatis-Plus 配置 `mapper-locations: classpath*:mapper/*.xml` 使用了通配符,因此新模块的 Mapper 会自动被扫描。无需额外配置。

### 3.3 如何调试一次失败的测试执行

场景:回归测试计划执行后,某些用例显示 `FAILED`,需要排查原因。

**步骤 1:定位失败日志**

```
# 1) 在 Executor 日志中按 traceId 搜索
grep "traceId=xxx" /path/to/executor/logs/*.log

# 2) 在 Core 日志中按 planId 搜索
grep "planId=1234" /path/to/core/logs/*.log
```

**步骤 2:检查 Execution 状态流转**

```sql
-- 查看 Executor 数据库中的任务状态
SELECT * FROM exe_plan_node WHERE plan_id = 1234 AND status = 'FAILED';
-- 查看步骤级别的结果
SELECT * FROM exe_plan_node_step WHERE node_id IN (
    SELECT id FROM exe_plan_node WHERE plan_id = 1234 AND status = 'FAILED'
);
```

**步骤 3:重现失败步骤**

可以通过 Core 的调试接口单独执行失败的 Step:

```bash
curl -X POST "http://localhost:8542/core/api/debug/step" \
  -H "Content-Type: application/json" \
  -H "QAMate-Token: super-9a796933bf024ebfa0420dce6f864a51" \
  -d '{
    "caseNodeId": 12345,
    "stepId": 67890,
    "envId": 1
  }'
```

**步骤 4:检查协议特定问题**

- **HTTP 协议:** 检查请求 URL、Headers、Body 是否正确,目标服务是否可达(用 curl 独立验证)
- **Redis 协议:** 检查 Redis 连接配置(`application-{env}.yml` 中 `spring.data.redis`),验证 key 是否存在
- **SQL 协议:** 检查数据库连接、SQL 语法、权限
- **Shell 协议:** 检查执行环境是否安装所需命令,路径是否正确
- **Script 协议:** 检查脚本语法错误,查看 Executor 的 stdout/stderr 输出

**步骤 5:使用 Arthas 在线诊断(高级)**

```bash
# 1) Attach 到 Executor Java 进程
java -jar arthas-boot.jar

# 2) 跟踪 QAMateCoreClient 的调用
trace com.baidu.qamate.server.common.conf.feign.client.QAMateCoreClient *

# 3) 查看 HttpProtocolFactory 的请求参数
watch com.baidu.qamate.server.protocol.factory.HttpProtocolFactory createRequest params
```

### 3.4 如何在 Executor 中添加新的协议处理器

假设需求:添加 `gRPC` 协议支持。

**步骤 1:理解 Executor 的四组件架构**

Executor 的每个协议由四个组件构成:
- **Constructor**(构建器):将 Step 定义转换为可执行请求(Request)
- **Executor**(执行器):发送请求并等待响应
- **Extractor**(提取器):从响应中提取变量(用于后续步骤的变量传递)
- **Verifier**(校验器):对比实际响应和预期结果

**步骤 2:创建 gRPC 协议工厂**

```java
// protocol/factory/GrpcProtocolFactory.java
package com.baidu.qamate.server.protocol.factory;

import com.baidu.qamate.server.protocol.component.Constructor;
import com.baidu.qamate.server.protocol.component.Executor;
import com.baidu.qamate.server.protocol.component.Extractor;
import com.baidu.qamate.server.protocol.component.Verifier;
import com.baidu.qamate.server.protocol.component.impl.GrpcConstructor;
import com.baidu.qamate.server.protocol.component.impl.GrpcExecutor;
import com.baidu.qamate.server.protocol.component.impl.GrpcExtractor;
import com.baidu.qamate.server.protocol.component.impl.GrpcVerifier;
import org.springframework.stereotype.Component;

@Component
public class GrpcProtocolFactory extends AbstractProtocolFactory {

    @Override
    public Constructor createConstructor() { return new GrpcConstructor(); }

    @Override
    public Executor createExecutor() { return new GrpcExecutor(); }

    @Override
    public Extractor createExtractor() { return new GrpcExtractor(); }

    @Override
    public Verifier createVerifier() { return new GrpcVerifier(); }

    @Override
    public String getProtocolName() { return "GRPC"; }
}
```

**步骤 3:实现四个组件**

每个组件实现约 50-100 行,参照现有 HTTP/Redis 实现即可。关键在于 `GrpcConstructor` 需要解析 Step 定义的 JSON 中 `endpoint`(gRPC 服务地址)和 `method`(RPC 方法名)。

**步骤 4:注册到 `ProtocolFactoryManager`**

```java
// protocol/factory/ProtocolFactoryManager.java (追加)
@Autowired
private GrpcProtocolFactory grpcProtocolFactory;

@PostConstruct
public void init() {
    // ... 现有注册 ...
    registerFactory("GRPC", grpcProtocolFactory);
}
```

**步骤 5:在 Core 中添加 gRPC Step 模板**

在 Core 的 `casestepmgt` 模块的 Step 类型枚举中添加 `GRPC` 类型:

```java
// components/constant/StepTypeEnum.java
public enum StepTypeEnum {
    HTTP, REDIS, SQL, SHELL, SCRIPT, GRPC  // ← 新增
}
```

### 3.5 构建与本地开发命令

#### Core 模块

```bash
# 进入 Core 目录
cd baidu/qamate-server/core

# 本地编译(跳过测试,使用 dev profile)
mvn clean package -DskipTests -Pdev

# 本地编译(含测试)
mvn clean package -Pdev

# 仅运行单元测试
mvn test -Pdev

# 启动(dev profile)
mvn spring-boot:run -Dspring-boot.run.profiles=dev

# 或直接运行打好的包
java -jar output/core-1.0.0-SNAPSHOT.jar --spring.profiles.active=dev

# 启动时指定端口
java -jar output/core-1.0.0-SNAPSHOT.jar --spring.profiles.active=dev --server.port=18542
```

#### Executor 模块

```bash
cd baidu/qamate-server/apiExecutor

# 编译整个 executor(含 client, dto, server 子模块)
mvn clean package -DskipTests

# 仅编译 executor-server
mvn clean package -DskipTests -f executor-server/pom.xml

# 启动
cd executor-server
java -jar target/executor-server-1.0.0-SNAPSHOT.jar --spring.profiles.active=dev
```

#### Dispatch 模块(XXL-JOB)

```bash
cd baidu/qamate-server/api-smart-dispatch

# 编译
mvn clean package -DskipTests

# 启动 XXL-JOB Admin(调度中心 Web UI)
java -jar xxl-job-admin/target/xxl-job-admin-3.2.1-SNAPSHOT.jar
```

#### Maven Profile 说明

| Profile | 激活的 application-*.yml | 用途 | JDBC 驱动版本 |
|---|---|---|---|
| `dev`(默认) | application-dev.yml | 本地开发,连接测试 MySQL | MySQL 8.0.19 |
| `test` | application-test.yml | 测试环境 | MySQL 5.1.47 |
| `test-aird` | application-test-aird.yml | AIRD 专项测试环境 | MySQL 5.1.47 |
| `online` | application-online.yml | 生产环境 | MySQL 5.1.47 |

#### 本地开发环境前置依赖

```
# 必需的中间件
MySQL 8.0+       # 多数据源(newsource, oldsource, apismart-dispatch, apismart-executor)
Redis 6.0+       # JetCache 远程缓存 + Session
XXL-JOB Admin    # 调度中心(可选,如果不需要测试调度功能可以跳过)

# 推荐的开发工具
JDK 21+          # 编译和运行(Amazon Corretto / Oracle OpenJDK)
Maven 3.9+       # 构建工具
IntelliJ IDEA    # IDE(支持 lombok 插件, MapStruct 插件)
```

#### IDE 配置提示

**Lombok 配置:**
在 IntelliJ IDEA 中启用 File > Settings > Build > Compiler > Annotation Processors > "Enable annotation processing"。否则编译时 Lombok 的 `@Data`/`@Slf4j` 注解将不生效。

**多环境切换:**
在 IDEA Run Configuration 的 "Active profiles" 中填入 `dev` 或 `test`。

**热加载:**
Executor 已依赖 `spring-boot-devtools`,开发时修改代码会自动重启;Core 未依赖 devtools,需要手动重启。

### 3.6 日常开发检查清单

在修改代码之前,请确保:
- [ ] 已理解目标模块的 Service-Controller-Mapper 三层关系
- [ ] 已查找是否有类似的现有实现可参考(如要添加新的查询接口,先看 `CaseNodeController` 中类似的查树接口)
- [ ] 新的文件代码行数控制在 400 行以内(不要往 `CaseNodeServiceImpl` 加新方法!)
- [ ] Controller 方法始终返回 `Response<T>` 统一格式
- [ ] Service 方法在失败时抛出 `CoreException(StatusEnum.XXX, "描述")`
- [ ] 对数据库的查询使用 `LambdaQueryWrapper`(类型安全,避免 String 拼接)
- [ ] 跨模块调用使用 Feign Client(如 Core 调用 Executor)
- [ ] 敏感配置(token、密码)使用 `@Value` 注入,不硬编码

### 3.7 常见问题速查

| 问题 | 原因 | 解决方案 |
|---|---|---|
| `Token为空` 错误 | 请求缺少 `QAMate-U-Token` 或 `QAMate-Token` Header | 检查 Header 名称是否正确,或使用超级 Token `super-9a79...` 绕过鉴权 |
| `Token非法` 错误 | Token 过期或不匹配 | UUAP Token 通常 24h 过期,需重新登录获取;OpenAPI Token 检查 Product 表 |
| MyBatis `Invalid bound statement` | Mapper XML 未编译到 classpath | 检查 `pom.xml` 的 `resources` 配置是否正确包含 `mapper/*.xml` |
| Feign 调用超时 | 目标服务不可达或响应慢 | 检查 `feign.client.config.default.connectTimeout`,必要时增加 `readTimeout` |
| `CaseNode` 子节点丢失 | `parentId` 不一致或 `isDel=1` | 检查数据库数据完整性,运行数据修复脚本 |
| 编译错误:找不到 `lombok` 符号 | IDEA Annotation Processor 未启用 | 启用 Annotation Processing(见 3.5 节 IDE 配置) |

---

> 全文完。本文档由小纸巾撰写,采用"正反合"辩证分析 + "反事实推理"批判性思考,旨在帮助新老开发者快速理解 QAMate 全库架构与日常开发流程。如有疑问或需要补充,请通过 iCafe 提交文档改进需求。
