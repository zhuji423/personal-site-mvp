---
title: "ITP-Web 接口与实现梳理"
description: "ITP-Web 采用典型的 Spring MVC 架构，Action 层负责接收 HTTP 请求，Service 层负责业务逻辑。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\itp_web_interfaces.md"
---
# ITP-Web 接口与实现梳理

ITP-Web 采用典型的 Spring MVC 架构，Action 层负责接收 HTTP 请求，Service 层负责业务逻辑。

## 1. 测试计划管理 (TestPlanAction)
**基础路径**: `/itp/testplan`

| 接口描述 | 方法 | URL | 对应 Service 方法 | ServiceImpl 实现 |
| :--- | :--- | :--- | :--- | :--- |
| 获取测试计划列表 | GET | `/` | `testPlanService.queryByCondition` | `TestPlanServiceImpl` |
| 按ID获取计划详情 | GET | `/{id}` | `testPlanService.queryById` | `TestPlanServiceImpl` |
| 创建测试计划 | POST | `/` | `testPlanService.insert` | `TestPlanServiceImpl` |
| 修改测试计划 | PUT | `/{id}` | `testPlanService.update` | `TestPlanServiceImpl` |
| 复制测试计划 | POST | `/copy/{testplanId}` | `testPlanService.copy` | `TestPlanServiceImpl` |
| 运行测试计划 | POST | `/run/{id}` | `jobClient.submitJob` (LTS 提交) | `JobClientFactoryBean` (LTS 客户端) |

## 2. 测试节点/用例管理 (TestNodeAction)
**基础路径**: `/itp/testnode`

| 接口描述 | 方法 | URL | 对应 Service 方法 | ServiceImpl 实现 |
| :--- | :--- | :--- | :--- | :--- |
| 获取节点信息 | GET | `/{id}` | `testNodeService.queryById` | `TestNodeServiceImpl` |
| 保存节点 | POST | `/` | `testNodeService.insert` | `TestNodeServiceImpl` |
| 更新节点 | PUT | `/{id}` | `testNodeService.update` | `TestNodeServiceImpl` |
| 后向运行 | POST | `/runAfter` | `jobClient.submitJob` | `JobClientFactoryBean` |

## 3. 测试分组管理 (TestGroupAction)
**基础路径**: `/itp/testgroup`

| 接口描述 | 方法 | URL | 对应 Service 方法 | ServiceImpl 实现 |
| :--- | :--- | :--- | :--- | :--- |
| 获取分组列表 | GET | `/` | `testGroupService.queryByCondition` | `TestGroupServiceImpl` |
| 运行分组 | POST | `/run` | `jobClient.submitJob` | `JobClientFactoryBean` |

## 4. API 接口 (api 子目录)
**例如**: `CheckApiAction`, `TestPlanApiAction` 等。这些接口通常用于外部 CI/CD 调用。

| 接口描述 | 方法 | URL | 对应 Service 方法 | ServiceImpl 实现 |
| :--- | :--- | :--- | :--- | :--- |
| 任务校验 | POST | `/itp/api/testgroup/check` | `checkService.doCheckByApi` | `CheckServiceImpl` |
| 异步校验 | POST | `/itp/api/testgroup/check/suiteCheckAsync` | `checkService.doAsyncCheck` | `CheckServiceImpl` |
| 获取执行详情 | GET | `/itp/api/testgroup/check/getCheckDetail/{id}` | `checkService.getCheckExeDetail` | `CheckServiceImpl` |

## 5. 通讯录及系统管理 (UserAction, ProductAction 等)
*   **UserAction**: 负责用户信息获取。通过 `AuthService` (实现类 `AuthServiceImpl`) 校验 UUAP Token。
*   **ProductAction**: 负责产品线管理。对应 `ProductService` (实现类 `ProductServiceImpl`)。

## 6. WebSocket 接口
*   **路径**: `/itp/websocket`
*   **实现类**: `com.baidu.itp.web.websocket.WebsocketEndPoint`
*   **职责**: 为前端提供实时执行进度推送。

# ITP-Web 核心接口实现详述

ITP-Web 承担了任务发起与管理的重责。以下针对核心 Action 及其 Service 实现进行深度解析。

## 1. 测试计划执行 (TestPlanAction & LtsClientFacade)

### 接口：运行计划 (POST `/itp/testplan/run/{id}`)
*   **入口函数**: `TestPlanAction.runPlan(Integer id, ...)`
*   **核心逻辑实现**:
    1.  **权限校验**: 通过 `AuthService` 验证当前用户是否有运行该计划的权限。
    2.  **创建执行记录**: 插入一条新的 `PlanExecution` 记录到数据库，标记为“等待执行”。
    3.  **调用 Facade**: 调用 `ltsClientFacade.runPlan(recordId)`。
*   **LtsClientFacade 实现细则**:
    -   **并发逻辑**: 检查计划配置的 `concurrency`。
        -   **串行执行**: 调用 `itpJobClient.submitRealtimeJob`。
            -   构建 LTS `Job` 对象，设置 `TaskTrackerNodeGroup`。
            -   将 `planId`、`recordId`、`runType` 等业务信息封装进 `Job` 的 `params`。
            -   使用 `jobClient.submitJob(job)` 提交到 LTS JobTracker。
        -   **并行执行**: 
            -   调用 `testNodeService.queryLeafSuite` 获取所有叶子测试套件。
            -   利用 `GroupOptimizeUtil` 根据历史执行时长或智能分组算法将套件分组。
            -   为每个分组创建一个独立的 LTS Job 并提交，实现分布式并行执行。

## 2. 测试集/用例管理 (TestNodeAction)

### 接口：保存/更新用例 (POST/PUT `/itp/testnode`)
*   **实现函数**: `TestNodeServiceImpl.insert/update`
*   **具体逻辑**:
    1.  **JSON 格式处理**: 对用例中的 Request/Response 模板进行格式化验证。
    2.  **变量提取**: 自动分析用例定义中的 `${var}` 占位符。
    3.  **版本控制**: 如果是在分支上操作，会涉及 `TestNodeBranchServiceImpl` 来管理不同版本的用例快照。
    4.  **历史记录**: 调用 `OpLogServiceImpl` 记录用户的每一次修改操作，用于审计。

## 3. CI/CD 接口集群 (CheckApiAction)

### 接口：流水线异步校验 (POST `/itp/api/testgroup/check/suiteCheckAsync`)
*   **实现函数**: `CheckServiceImpl.doAsyncCheck`
*   **具体逻辑**:
    1.  **参数初始化**: 校验流水线传来的 `projectId`、`versionId` 是否存在。
    2.  **创建预检记录**: 在 `itp_check_exe_detail` 表中初始化一条 ID。
    3.  **异步化处理**: 利用 Spring `@Async` 或内部线程池开启后台任务。
    4.  **执行校验**: 循环调用 `CheckService.doCheck` 对指定的 Suite 进行静态扫描（如：协议一致性、必填项校验、断言逻辑检查）。
    5.  **实时状态**: 执行过程中不断更新该 ID 对应的状态，前端或流水线通过 `getCheckDetail` 轮询结果。

## 4. WebSocket 进度推送 (WebsocketEndPoint)
*   **逻辑实现**:
    -   TaskTracker 在执行完每个用例后会向 ITP-Web 发送回调。
    -   ITP-Web 收到回调后，根据 `planId` 找到对应的 WebSocket Session。
    -   `WebsocketEndPoint` 将最新的执行进度、结果摘要通过长连接推送至前端。
