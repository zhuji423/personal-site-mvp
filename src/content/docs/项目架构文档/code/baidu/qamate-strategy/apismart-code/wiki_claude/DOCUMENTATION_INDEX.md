---
title: "QAMate / ITP 文档索引"
description: "这份索引是主控整合文档，不重新展开所有技术细节，而是回答三个问题："
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\wiki_claude\\DOCUMENTATION_INDEX.md"
---
# QAMate / ITP 文档索引

## Thinking Process

这份索引是主控整合文档，不重新展开所有技术细节，而是回答三个问题：

1. 新同学应该先读哪一份文档。
2. 遇到具体问题时应该跳到哪一份文档的哪一类章节。
3. 这次分析的边界、证据口径、风险优先级是什么。

本轮执行采用 Claude team/subagent 的写作分工：`arch-writer` 负责架构深潜，`topo-writer` 负责系统拓扑和生命周期，`manual-writer` 负责维护手册。主控只做任务拆分、产物检查、交叉索引和最终收口。

重要边界：

- Core 只分析 `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt` 以及它直接依赖的支撑配置，例如 `App.java`、`RequestFilter.java`、`FilterConfig.java`、`ContextHolder.java`、环境配置和 Feign 配置。
- `apiExecutor`、`api-smart-dispatch`、`inner-os/itp` 按计划正常分析。
- 文档引用真实文件路径和行号；涉及 token、密码、数据库连接串、内网凭据时，只指出风险和位置，不复制完整敏感值。
- 本次只新增 `wiki_claude` 文档，不修改 Java 业务代码、配置语义、接口路径或数据库结构。

## 产物清单

| 文档 | 负责 agent | 用途 | 推荐读者 |
| --- | --- | --- | --- |
| `ARCHITECTURE_DEEP_DIVE.md` | `arch-writer@qamate-docs-v2` | 解释系统为什么这样拆、核心链路怎么走、隐性依赖和 TOP 风险在哪里。 | 想先理解全局架构、调用链、风险的人。 |
| `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` | `topo-writer@qamate-docs-v2` | 解释四个组件的运行拓扑、协议、目录地图、启动和回调生命周期。 | 想排查“服务是否连通、谁先启动、谁回调谁”的人。 |
| `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` | `manual-writer@qamate-docs-v2` | 给维护者的操作手册：关键类、配置字典、复杂函数、常见排障动作。 | 要改代码、排故障、查配置的人。 |
| `DOCUMENTATION_INDEX.md` | main coordinator | 串联上面三份文档，提供阅读路线和问题入口。 | 所有人。 |

## 先读哪一份

如果你完全没有后端背景，先读 `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md`。它把服务解释成不同柜台、把 HTTP API 解释成窗口、把调度器解释成闹钟加派单台，适合作为第一张地图。

如果你已经知道系统有 Core、dispatch、executor，但不知道请求怎么跑完，读 `ARCHITECTURE_DEEP_DIVE.md`。它从架构模式、业务流向、隐性依赖、设计模式、风险评估五个维度展开。

如果你要立刻维护代码，读 `DEVELOPER_MAINTENANCE_MANUAL_FULL.md`。它有关键类表、40 项配置字典、复杂函数拆解和常见维护动作。

## 核心链路入口

### 链路 1：Core 创建调度任务

读：

- `ARCHITECTURE_DEEP_DIVE.md` 的“apismart 计划创建”。
- `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的“复杂函数 1：Core ApiPlanServiceImpl.createApiPlan()”。
- `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` 的“阶段 3：Core apismart 通过 Feign 调 dispatch”。

关键代码：

- `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ApiPlanController.java`
- `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ApiPlanServiceImpl.java`
- `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/client/DispatchClient.java`
- `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/controller/openapi/JobApiController.java`
- `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/model/XxlJobInfo.java`

### 链路 2：dispatch 触发 executor 执行计划

读：

- `ARCHITECTURE_DEEP_DIVE.md` 的“apismart 计划执行”。
- `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` 的“启动/握手时序图”和“阶段 2：executor 暴露 XXL-JOB handler”。
- `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的“复杂函数 2：apiExecutor PlanRunner.startRunPlan()”。

关键代码：

- `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobScheduleHelper.java`
- `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobTriggerPoolHelper.java`
- `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/jobhandler/PlanHandler.java`
- `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/runner/impl/PlanRunner.java`
- `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/runner/impl/CaseRunner.java`

### 链路 3：结果回流和计划结束

读：

- `ARCHITECTURE_DEEP_DIVE.md` 的“结果回流”。
- `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` 的“阶段 4：回调闭环”。
- `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的“复杂函数 3：dispatch JobCompleteHelper.callServerPlanEnd()”。

关键代码：

- `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/common/conf/feign/client/QAMateCoreClient.java`
- `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/service/impl/PlanExecuteServiceImpl.java`
- `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobCompleteHelper.java`
- `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ApiPlanController.java`
- `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ApiPlanServiceImpl.java`

## 问题到文档的映射

| 你遇到的问题 | 优先阅读 |
| --- | --- |
| 不知道四个组件分别负责什么 | `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` 的“任务 1：全景拓扑” |
| 不知道服务启动后谁注册谁、谁回调谁 | `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` 的“任务 4：启动生命周期” |
| 不知道为什么系统是微服务 + 调度 + 执行器组合 | `ARCHITECTURE_DEEP_DIVE.md` 的“维度 A：全局架构图景” |
| 计划创建成功但 dispatch 没有任务 | `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的“排查计划创建成功但没有调度” |
| 计划一直运行中 | `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的“排查计划一直运行中” |
| 要改 apismart 计划接口 | `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的“新增或修改 apismart 计划接口” |
| 要查配置项用途 | `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的“全局配置项释义字典” |
| 要评估安全风险 | `ARCHITECTURE_DEEP_DIVE.md` 的“维度 E：TOP 5 潜在风险评估” |
| 要理解 ThreadLocal / MDC / traceId | `ARCHITECTURE_DEEP_DIVE.md` 的“维度 C：隐性依赖与副作用” |
| 要理解 ITP / LTS 遗留体系 | 三份文档中搜索 `ITP`、`LTS`、`TaskTracker`、`JobTracker` |

## 风险总览

本轮文档中反复出现的 TOP 风险如下：

1. 跨服务 token、数据库凭据、旧 DES-CBC key/iv 存在硬编码风险。文档只给位置，不复写值。
2. Core、dispatch、executor 之间存在同步调用和异步回调组合，任一环节地址、token、路径或执行 ID 不一致，都会导致计划状态闭环中断。
3. ThreadLocal / MDC / traceId 依赖线程上下文，在线程复用和白名单路径中需要特别关注清理与传递。
4. 调度触发池、executor 线程池、回调逻辑会在高峰期互相放大压力，需要从队列、超时、重试和拒绝策略一起评估。
5. ITP / LTS 遗留体系使用旧工具链、旧 RPC、旧加密方式，迁移或兼容时不能只看 qamate-server 新服务。

## 维护护栏

改 apismart 相关需求时，先确认它属于哪条链路：

- 只影响 Core 页面/接口：优先看 `core/apismartmgt/controller -> service -> mapper/entity/vo`。
- 影响计划创建、启停、触发：同时看 Core `DispatchClient` 和 dispatch `JobApiController` / `XxlJobServiceImpl`。
- 影响执行过程：同时看 executor `PlanHandler`、`PlanRunner`、`CaseRunner`、`Processor`。
- 影响计划结束状态：同时看 executor 回调 Core、dispatch `JobCompleteHelper.callServerPlanEnd()`、Core `/apismart/plan/exe/end`。
- 影响旧系统兼容：再看 `inner-os/itp`，不要把 LTS 和 XXL-JOB 的调度模型混为一谈。

不要随意修改这些跨服务契约：

- `/apismart/dispatch/api/*`
- `/executor/*`
- `/core/*`
- `QAMate-ModuleId`
- `QAMate-Token`
- `XXL-JOB-ACCESS-TOKEN`
- `planId`
- `planExeId`
- `jobId`

## 验证记录

已完成的主控校验：

- 3 个 writer agent 均只写入自己的目标 Markdown 文件。
- 3 份正文合计超过 1000 行，包含源码路径、行号、Mermaid 图、正反合与反事实说明。
- 已确认 Core 分析重点放在 `apismartmgt`，其他 Core 域只作为支撑配置或外部依赖出现。
- 已确认敏感配置采取“引用位置、不复写完整值”的写法。
- 本轮没有修改业务代码。

## 推荐阅读顺序

1. `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md`
2. `ARCHITECTURE_DEEP_DIVE.md`
3. `DEVELOPER_MAINTENANCE_MANUAL_FULL.md`
4. 回到本索引，根据具体问题跳转

