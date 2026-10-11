---
title: "ITP 系统任务执行路径深度解析"
description: "本文档详细梳理了 ITP 系统中不同触发场景下的任务执行路径，特别是 Web、LTS JobTracker、Dubbo 和 TaskTracker 之间的交互关系。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\itp_execution_paths.md"
---
# ITP 系统任务执行路径深度解析

本文档详细梳理了 ITP 系统中不同触发场景下的任务执行路径，特别是 Web、LTS (JobTracker)、Dubbo 和 TaskTracker 之间的交互关系。

## 1. 页面调试 (Page Debug / Immediate Execution)
**场景**: 用户在 Web 编辑用例页面点击“调试”或“立即运行”，期望立即看到单个用例的执行结果。

*   **触发方式**: Web 前端发起 HTTP 请求 (如 `/itp/testnode/debug` 或 `/itp/testnode/run` )。
*   **执行入口**: `TestNodeAction.run` 或 `DebugAction`。
*   **调用链路**: 
    1.  **Web 层**: `TestNodeAction` 接收请求，解析参数。
    2.  **Facade 层**: 调用 `LtsClientFacade`，判断为调试模式。
    3.  **RPC 层**: 绕过 LTS 调度，直接调用 Dubbo 接口 `com.baidu.itp.core.submit.JobSubmit.submit`。
    4.  **TaskTracker 层**: `ItpJobDirectRunner` 响应 Dubbo 请求，在本机线程池中立即执行 `ItpJobRunner.run`。
*   **是否经过 JobTracker**: **否**。
*   **是否使用 Dubbo**: **是** (直连插队)。
*   **核心考量**: 牺牲调度可控性，换取**毫秒级响应**和简单的反馈链路。

## 2. 手动计划执行 (Manual Plan Execution)
**场景**: 用户在 Web 计划列表点击“运行”，执行一个包含几百个用例的测试计划。

*   **触发方式**: Web 前端发起 HTTP 请求 (如 `/itp/testplan/run/{id}` )。
*   **执行入口**: `TestPlanAction.runPlan(Integer id)`。
*   **调用链路**:
    1.  **Web 层**: `TestPlanAction` 校验权限，创建 `PlanExecution` 记录 (Status: WAITING)。
    2.  **LTS Client**: 调用 `itpJobClient.submitRealtimeJob`，将任务封装为 LTS Job。
    3.  **LTS JobTracker**: Job 被提交到 `ExecutableJobQueue` (持久化队列) 排队。
    4.  **调度分发**: JobTracker 根据 TaskTracker 负载，将任务 Push 或被 Pull 到执行节点。
    5.  **TaskTracker 层**: 收到任务，执行 `ItpJobRunner`。
*   **是否经过 JobTracker**: **是**。
*   **是否使用 Dubbo**: **否**。
*   **核心考量**: **稳定性**与**容错**。LTS 保证任务不丢失，且在执行节点宕机时能自动重试。

## 3. API 触发定时计划 (Cron/Scheduled Plan)
*   **触发方式**:
    1.  **配置定时**: 用户保存计划时设置 Cron 表达式 (`TestPlanAction.update`).
    2.  **触发执行**: LTS JobTracker 内置的 Cron 调度器自动触发。
*   **入口**: `TestPlanAction` (配置侧) / `LTS JobTracker` (触发侧)。
*   **执行路径**:
    *   **提交**: `ItpJobClient.submitCrontabJob` -> LTS `CronJobQueue` (入队)
    *   **触发**: LTS Timer -> `ExecutableJobQueue` -> `TaskTracker`
*   **是否使用 Dubbo**: **否**。
*   **原因**: 定时任务是 LTS 的核心强项。它完全依赖 LTS 的 Cron 调度器来保证并在分布式环境下的准时触发（不重复、不漏跑）。

## 4. API 触发用例调试 (API Triggered Case Debug)
*   此处的“API 触发”通常指外部 CI 流水线或脚本通过 OpenAPI 触发单用例/小规模执行。
*   **场景 A: 流水线预检 (Check API)**
    *   **入口**: `CheckApiAction.suiteApiCheckAsync`
    *   **路径**: `CheckServiceImpl` -> 本地/异步逻辑。
    *   **是否使用 Dubbo**: **否**（通常在 Web 端进行静态规则校验或逻辑检查，不直接下发 TaskTracker 执行）。
*   **场景 B: 单用例执行 (Run Case API)**
    *   如果 API 也就是 Web 前端调用的同一个“调试接口”（如 `/itp/testnode/run` 或 `/itp/debug`）：
    *   **是否使用 Dubbo**: **是**（大概率）。
    *   **原因**: 为了给 API 调用方（如 IDE 插件、调试工具）提供毫秒级的响应，往往复用 Dubbo 的 `JobSubmit` 直连通道。

---

## 总结：调度策略矩阵

| 触发场景 | 业务入口 | 通道技术 | 是否插队 (Dubbo) | 核心考量 |
| :--- | :--- | :--- | :--- | :--- |
| **页面调试** | 立即运行 (Debug) | **Dubbo** | **YES** | **极低延迟**，需同步/快速异步获取结果 |
| **手动计划** | 计划运行 (Run) | LTS (Realtime) | NO | **稳定性**，任务量大，需排队和持久化 |
| **定时计划** | 自动调度 (Cron) | LTS (Cron) | NO | **准确性**，依赖调度中心的 Cron 管理 |
| **API 触发** | CI/Api 调用 | LTS / Dubbo | 取决于接口 | 长任务走 LTS，短调试走 Dubbo |

**结论**: 除了“调试/立即执行”类的高实时性操作使用了 Dubbo 的“绿色通道”外，**ITP 的绝大多数批量、定时、长运行任务都严格遵循 LTS 的标准调度路径**，以确保在大并发下的系统稳定性。
