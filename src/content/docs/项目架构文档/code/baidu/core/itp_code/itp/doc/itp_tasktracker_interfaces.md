---
title: "ITP-TaskTracker 接口与实现梳理"
description: "ITP-TaskTracker 是 ITP 系统的任务执行引擎，它既作为 LTS 的执行节点接收 JobTracker 分派的任务，也通过 Dubbo 暴露直接提交任务的接口。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\itp_tasktracker_interfaces.md"
---
# ITP-TaskTracker 接口与实现梳理

ITP-TaskTracker 是 ITP 系统的任务执行引擎，它既作为 LTS 的执行节点接收 JobTracker 分派的任务，也通过 Dubbo 暴露直接提交任务的接口。

## 1. Dubbo 远程服务接口 (JobSubmit)
**接口定义**: `com.baidu.itp.core.submit.JobSubmit`

| 方法名 | 说明 | 入参 | 实现类 | 实现逻辑 |
| :--- | :--- | :--- | :--- | :--- |
| `submit` | 提交任务 | `JobWrapper` | `ItpJobDirectRunner` | 开启线程池，调用 `ItpJobRunner.run` |

## 2. LTS 任务执行入口 (JobRunner)
**接口定义**: `com.lts.tasktracker.runner.JobRunner`

| 实现类 | 说明 | 核心方法 |
| :--- | :--- | :--- |
| `ItpJobRunner` | 任务执行总入口 | `run(Job job)` |

### 执行流转过程 (ItpJobRunner.run):
1.  **解析 Job**: 从 LTS Job 中提取 `testPlanId` 或 `testCaseId`。
2.  **上下文初始化**: `testPlanExecuteContext.init`。
3.  **任务分发**:
    *   如果是计划任务 -> 调用 `PlanJobRunner.run`。
    *   如果是单用例/分组任务 -> 调用 `CaseJobRunner.run`。

## 3. 核心执行器实现 (Internal Implementation)

### 3.1 PlanJobRunner (计划执行)
*   **职责**: 按照用例树或顺序执行测试计划中的所有用例。
*   **关键方法**: `runPlan`, `runDiffPlan`。
*   **依赖服务**:
    *   `InfoFacde`: 获取计划、分组、用例、中间件等基础数据。
    *   `AtomicRunner`: 单个算子的执行入口。

### 3.2 AtomicRunner (原子执行器)
*   **职责**: 处理单个节点（用例）的执行生命周期，包括前置操作、执行、断言、后置操作。
*   **核心实现**:
    *   通过 `ExecutorFactory` 创建对应的执行器（如 `HttpExecutor`, `DubboExecutor`, `SqlExecutor`, `MongoExecutor` 等）。
    *   调用 `AbstractExecutor.execute`。

### 3.3 常用执行器实现 (com.baidu.itp.tasktracker.executor)
*   **HttpExecutor**: 调用 `OkHttpClient` 或 `RestTemplate` 发起 HTTP 请求。
*   **DubboExecutor**: 通过 Dubbo 泛化调用执行远程服务测试。
*   **JsonRpcExecutor**: 执行 JSON-RPC 协议测试。
*   **SqlExecutor / RedisExecutor / MongoExecutor**: 执行数据库或中间件操作及断言。

## 4. 其它内部组件
*   **KirinDataService**: 实现类 `KirinDataServiceImpl`，负责将执行数据推送到麒麟平台。
*   **SeasonApiService**: 实现类 `SeasonApiServiceImpl`，负责处理分季执行逻辑。
*   **UicService**: 实现类 `UicServiceImpl`，负责用户权限等内部系统对接。

# ITP-TaskTracker 核心任务流转实现详述

ITP-TaskTracker 负责解析任务并调动各协议执行器完成测试。其核心类及方法逻辑如下：

## 1. 任务执行总入口 (ItpJobRunner)

### 方法：任务分发 (`run` 方法)
*   **具体逻辑**:
    1.  **MDC 上下文设置**: 设置 `traceId` 到日志上下文中，确保全链路日志可追踪。
    2.  **Job 参数解析**: 从 `com.lts.core.domain.Job` 中提取 `planId`、`recordId`、`subIds` 等关键业务参数。
    3.  **模式判断**:
        -   如果是计划运行 (Plan)：调用 `planRunner.run()`。
        -   如果是单用例/分组运行 (Case/Group)：调用 `caseRunner.run()`。
    4.  **异常捕获与反馈**: 如果执行过程中发生 `ItpException`，捕获异常并将结果标记为 `failed` 返回给 JobTracker。

## 2. 计划级执行器 (PlanJobRunner)

### 方法：顺序运行 (`runPlan` 方法)
*   **具体逻辑**:
    1.  **全局参数初始化**: 创建 `GlobalParam`，包含本次运行所需的共享数据（如多步用例间的变量传递 Map）。
    2.  **BNS 动态解析**: 如果配置了 BNS（Baidu Name Service），调用相关服务解析出真实的下游 IP 列表，用于服务发现。
    3.  **循环迭代**: 反复迭代计划中的每一个 `TestNode`（用例或步骤）。
    4.  **调用原子执行器**: 对每一个 `TestNode`，调用 `AtomicRunner.runCase` 并更新执行上下文中的变量。
    5.  **失败处理逻辑**:
        -   根据 `failStrategy` 决定是跳过继续执行，还是立即终止计划。
        -   如果是重试逻辑，则重新分发当前用例进入 `RetryHandler`。

## 3. 原子执行逻辑 (AtomicRunner)

### 方法：用例全生命周期处理 (`runCase` 方法)
*   **具体逻辑**:
    1.  **前置插件处理 (BeforeCaseOperator)**: 通过 SPI 加载并执行所有前置钩子函数。
    2.  **变量替换**: 调用 `ArgUtil.replace`，将 Request 模板中的占位符（由 `${}` 标记）替换为 `GlobalParam` 或动态数据中的真实值。
    3.  **登录态注入**: 根据配置的 `LoginType`，调用相应的登录插件获取 Session/Cookie，并注入到 Request Header 中。
    4.  **核心执行**: 
        -   根据 `ProtocolEnum` 获取 `HttpExecutor`、`DubboExecutor` 等。
        -   调用 `executor.execute()`，拿到 `OpResponse` 对象。
    5.  **结果校验 (Assertion)**:
        -   **JSON 校验**: 支持完全匹配、子集匹配及 正则匹配。
        -   **DB 校验**: 执行 SQL 查询并在结果集中校验目标字段。
    6.  **后置处理与持久化**: 将执行结果摘要、请求体、返回体、耗时等信息组装成 `PlanExeDetailWithBLOBs` 并保存至数据库。

## 4. 各协议执行器 (Executor 系列)

-   **HttpExecutor**: 封装了 `OkHttpClient` 及其拦截器，处理超时重试、HTTPS 证书跳过等底层逻辑。
-   **DubboExecutor**: 利用 Dubbo 的 `GenericService` (泛化调用)，无需依赖业务 JAR 包即可发起任何接口的测试。
-   **SqlExecutor**: 基于 Druid 线程池，执行 SQL 脚本并处理结果集转换，支持多种数据库类型映射。
