---
title: "LTS JobTracker 接口与实现梳理"
description: "JobTracker 是 LTS 框架的核心节点，负责任务调度。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\lts_jobtracker_interfaces.md"
---
# LTS JobTracker 接口与实现梳理

JobTracker 是 LTS 框架的核心节点，负责任务调度。

## 1. Remoting 协议接口 (基于 Netty)
所有 JobClient 和 TaskTracker 与 JobTracker 的交互都通过 `RemotingDispatcher` 进行分发。

| RequestCode | 处理逻辑类 | 说明 |
| :--- | :--- | :--- |
| `SUBMIT_JOB` | `JobSubmitProcessor` | 处理 JobClient 提交的任务，存入可执行任务队列。 |
| `JOB_PULL` | `JobPullProcessor` | TaskTracker 主动来拉取任务时，从队列分发任务给它。 |
| `JOB_COMPLETED` | `JobCompletedProcessor` | TaskTracker 执行完上报状态，JobTracker 将其移入已执行队列。 |
| `CANCEL_JOB` | `JobCancelProcessor` | 取消正在执行或等待执行的任务。 |
| `BIZ_LOG_SEND` | `JobBizLogProcessor` | 接收并存储业务执行日志。 |

## 2. HTTP 运维命令接口 (HttpCmdServer)
JobTracker 暴露了一个端口供运维管理，主要命令如下：

| 命令类 | 请求参数 | 说明 |
| :--- | :--- | :--- |
| `AddJobHttpCmd` | JSON 格式的 Job 属性 | 通过 HTTP 接口直接添加任务。 |
| `LoadJobHttpCmd` | - | 强制触发加载某些任务（例如从数据库重新加载）。 |

## 3. 核心管理组件 (JobTrackerAppContext)
这些组件虽然不是外部接口，但支撑了接口的实现逻辑：

*   **ExecutableJobQueue**: 待执行任务队列（如 `MysqlExecutableJobQueue`）。
*   **ExecutingJobQueue**: 正在执行中的任务队列。
*   **CronJobQueue**: Cron 表达式定时任务队列。
*   **ChannelManager**: 管理所有与 JobTracker 连接的客户端（Netty Channel）。
*   **JobReceiver**: 对应 `JobSubmitProcessor` 的底层逻辑，接收任务并入库。
*   **JobSender**: 对应 `JobPullProcessor` 的底层逻辑，负责将任务推送给 TaskTracker。

## 4. 任务状态变迁实现
1.  **提交**: `JobSubmitProcessor` -> `JobReceiver.receive` -> 插入 `ExecutableJobQueue`。
2.  **分发**: `JobPullProcessor` -> `JobSender.send` -> 分发给 `TaskTracker` 并移入 `ExecutingJobQueue`。
3.  **完成**: `JobCompletedProcessor` -> `JobCompletedChain` -> 标记成功/失败 -> 移出 `ExecutingJobQueue` -> 存入 `ExecutedJobQueue`。

# LTS JobTracker 核心处理器实现详述

JobTracker 通过不同的 `RemotingProcessor` 来处理不同类型的请求。以下是各个处理器的核心逻辑实现。

## 1. 任务提交处理器 (JobSubmitProcessor)
*   **入口方法**: `processRequest`
*   **核心逻辑**:
    1.  **Job 校验**: 检查 Job 的 `nodeGroup` 是否合法，业务参数是否缺失。
    2.  **分类分发**:
        -   **Cron Job**: 如果任务带 Cron 表达式，则调用 `CronJobQueue.add`，并由定时线程监控执行时间。
        -   **Immediate Job**: 实时任务则直接调用 `ExecutableJobQueue.add` 持久化到数据库（如 `itp_executable_job` 表）。
    3.  **反馈客户端**: 返回 `SUBMIT_SUCCESS` 响应。

## 2. 任务分发处理器 (JobPullProcessor)
*   **入口方法**: `processRequest`
*   **具体实现逻辑**:
    1.  **请求参数解析**: 获取 TaskTracker 上报的当前空闲线程数、内存负载等信息。
    2.  **筛选算法**: 
        -   从 `ExecutableJobQueue` 中查询匹配该 `nodeGroup` 且优先级最高的任务。
        -   考虑负载均衡：确保任务不会集中分发给某一个高负载的 TaskTracker。
    3.  **状态流转**: 
        -   将选中的任务从 `ExecutableJobQueue` 移除，并存入 `ExecutingJobQueue`（表示正在执行）。
        -   通过 Netty Channel 将 Job 报文发送给 TaskTracker。

## 3. 任务回执处理器 (JobCompletedProcessor)
*   **入口方法**: `processRequest`
*   **具体实现逻辑**:
    1.  **状态更新**: 根据 TaskTracker 回传的 `Action`（执行成功、重试、延时重试），更新任务状态。
    2.  **队列操作**: 
        -   如果是 `Success/Failed`，则从 `ExecutingJobQueue` 删除。
        -   将最终执行历史写入 `ExecutedJobQueue` (对应数据库表 `itp_executed_job`)。
    3.  **Client 通知**: 
        -   如果原任务配置了 `feedback`，则调用 `JobFeedbackQueue` 准备将结果异步推送回 ITP-Web 的 `JobCompletedHandler`。

## 4. 其它管理组件

-   **JobReceiver**: `JobSubmitProcessor` 的底层逻辑支撑，负责将不同协议（HTTP/Remoting）提交的任务统一标准化。
-   **JobSender**: `JobPullProcessor` 的底层逻辑支撑，负责任务的序列化、网络发送及发送失败的自动重连。
-   **ChannelManager**: 维护一个长连接池，实时监控所有 TaskTracker 的探活状态，若某个连接断开，会自动将该节点正在执行的任务重新置为 `Executable` 状态（任务重分配逻辑）。
