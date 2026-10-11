---
title: "Thinking Process"
description: "这份维护手册按“先找入口、再找跨服务契约、最后找配置和副作用”的顺序写成。证据只来自当前仓库，行号使用 nl -ba 或同等带行号输出核对；路径均为仓库内真实路径。Core 的范围严格收敛到 apismartmgt 与直接支撑配置，不把 l"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\wiki_claude\\DEVELOPER_MAINTENANCE_MANUAL_FULL.md"
---
# Thinking Process

这份维护手册按“先找入口、再找跨服务契约、最后找配置和副作用”的顺序写成。证据只来自当前仓库，行号使用 `nl -ba` 或同等带行号输出核对；路径均为仓库内真实路径。Core 的范围严格收敛到 `apismartmgt` 与直接支撑配置，不把 lumos、kamix、debug 等 Core 其他业务域写成主体。

阅读时可以把系统想成一家餐厅：

- Core / apismartmgt 是前台和订单本：创建测试计划、保存计划、查询结果。
- api-smart-dispatch 是排班表和叫号器：决定什么时候把计划交给执行工位。
- apiExecutor 是后厨执行工位：真正拿到用例、环境、脚本并执行。
- inner-os/itp 是老餐厅和旧仓库：仍有旧的调度、RPC、密码处理和 LTS 任务模型。

重要提醒：本文只说明敏感配置“存在硬编码风险”和行号，不复制完整 token、密码、数据库连接串、内网凭据。

## 概念 101：首次维护前必须建立的直觉

### 微服务

【正面】微服务把一个大系统拆成多个独立服务，每个服务专心做一类事，像餐厅把前台、排班、后厨分开。  
【反面】服务之间要通过网络说话，任何一边接口、地址、token、字段变动，另一边都可能坏。  
【反事实】如果没有微服务，所有逻辑塞在一个进程里，改起来少一层网络风险，但排班、执行、页面、数据库会彼此缠住，发布和扩容都困难。  
【合】微服务不是“更简单”，而是把“一个大复杂”变成“多个小复杂 + 通信契约”。  
【本系统中的实例】Core 通过 `DispatchClient` 调 dispatch，接口路径集中在 `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/client/DispatchClient.java:15-61`；apiExecutor 通过 `QAMateCoreClient` 回调 Core，路径见 `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/common/conf/feign/client/QAMateCoreClient.java:23-57`。

### REST API

【正面】REST API 是服务之间用 HTTP 路径传递请求的约定，像“把订单放到指定窗口”。  
【反面】路径、方法、请求体字段没有编译期强约束，改错后通常运行时才暴露。  
【反事实】如果没有 REST API，可能用共享数据库或本地方法直接调用，短期少写接口，长期更难拆分和追踪。  
【合】维护 REST API 的核心不是记路径，而是同时看调用方和接收方。  
【本系统中的实例】Core 暴露 `/apismart/plan/create`、`/apismart/plan/run` 等入口，见 `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ApiPlanController.java:27-143`；dispatch 统一接 `/api/{uri}`，见 `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/controller/openapi/JobApiController.java:36-57`。

### Feign

【正面】Feign 把“发 HTTP 请求”包装成 Java 接口，维护者看到方法就能知道要调哪个外部接口。  
【反面】Feign 的 header、token、超时常藏在配置类里，排障时不能只看接口。  
【反事实】如果不用 Feign，就要手写 HTTP 客户端、拼 URL、拼 JSON，重复代码多，错误更隐蔽。  
【合】Feign 像电话簿：接口文件写号码，配置文件写通话规则。  
【本系统中的实例】`DispatchClient` 指定 `url = "${dispatch.url}"` 并使用 `FeignConfig`，见 `DispatchClient.java:15-18`；`FeignConfig` 给 dispatch 加 `XXL-JOB-ACCESS-TOKEN`、`userName`、`userToken`，且存在硬编码敏感值风险，见 `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/FeignConfig.java:35-43`。

### Controller / Service / Manager / Mapper / Entity / VO 分层

【正面】分层让入口、业务、外部调用、数据库对象、传输对象各司其职。  
【反面】小改动可能穿过多层，初学维护者容易只改 Controller 而忘了 Service 或 Mapper。  
【反事实】如果没有分层，所有逻辑写在一个类里，找起来直接，但每次修改都容易牵连无关逻辑。  
【合】可以把它看成“接待员 -> 主管 -> 外联/仓库 -> 表格/单据”的交接链。  
【本系统中的实例】Core apismart 计划创建入口在 `ApiPlanController.java:59-63`，实际业务在 `ApiPlanServiceImpl.java:267-340`，调度外联在 `DispatchClient.java:26-61`，计划表对象在 `ApiPlanEntity.java:23`，数据库访问在 `ApiPlanMapper.java:16`。

### 异步回调

【正面】异步回调让执行方不必一直占着调用方连接，任务结束后再通知。  
【反面】通知失败、重复通知、状态乱序都会带来隐性状态问题。  
【反事实】如果没有异步回调，Core 要一直等待执行结束，长任务会拖垮请求连接。  
【合】像餐厅取餐牌：下单后先离开，叫号器再通知你。  
【本系统中的实例】dispatch 完成后调用 Core `/core/apismart/plan/exe/end`，请求构造在 `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobCompleteHelper.java:207-232`。

### 线程池与 ThreadLocal

【正面】线程池复用线程，减少频繁创建线程的成本；ThreadLocal 把“当前请求用户/模块”等上下文放在线程旁边。  
【反面】线程复用后，如果上下文不清理，下一个任务可能读到上一个任务留下的数据。  
【反事实】如果不用线程池，每个任务都新建线程，简单但高并发时开销大；如果不用 ThreadLocal，每个方法都要显式传用户、模块、traceId。  
【合】线程池像复用工位，ThreadLocal 像工位抽屉；下班不清抽屉，下一位会拿错东西。  
【本系统中的实例】Core 的 `ContextHolder` 使用 `TransmittableThreadLocal` 保存 user、moduleId 和 token，见 `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/components/common/ContextHolder.java:12-15`，清理方法在 `ContextHolder.java:60-65`；apiExecutor 的 `PlanRunner` 明确说线程和实例会复用，因此执行后清理上下文，见 `PlanRunner.java:289-296`。

### 调度器与 XXL-JOB

【正面】调度器负责按时间触发任务，XXL-JOB 提供任务注册、触发、日志、回调等框架能力。  
【反面】调度器有自己的数据库、线程、token 和执行器注册机制，配置错了不会直接体现在 Core。  
【反事实】如果没有调度器，Core 只能立即执行，无法稳定支持 cron、补偿、失败重试和执行器管理。  
【合】调度器像值班表，XXL-JOB 是值班表系统。  
【本系统中的实例】dispatch 的调度扫描线程在 `JobScheduleHelper.start()`，见 `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobScheduleHelper.java:37-230`；任务与 Core 计划绑定字段是 `XxlJobInfo.planId`，见 `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/model/XxlJobInfo.java:12-15`。

### ORM / Mapper / Entity

【正面】ORM 和 Mapper 把数据库表操作包装成对象和接口，维护者不用到处拼 SQL。  
【反面】字段含义、数据源选择、XML SQL 仍然会影响行为。  
【反事实】如果不用 ORM，每处都手写 SQL，短期直观，长期字段变更成本高。  
【合】Entity 是表格里的“一行数据”，Mapper 是“查表/改表的窗口”。  
【本系统中的实例】Core 计划表对象 `ApiPlanEntity` 在 `ApiPlanEntity.java:23`，访问接口 `ApiPlanMapper` 在 `ApiPlanMapper.java:16`；Mapper XML 位置由 `mybatis-plus.mapper-locations` 指定，见 `baidu/qamate-server/core/src/main/resources/application.yml:56-57`。

## 部分 A：全库知识索引

### 1. Core / apismartmgt

职责：管理 API Smart 计划、计划执行记录、执行结果、脚本任务、分支任务、diff 字段和告警检查。边界：只负责“计划和结果的业务语义”，不直接执行用例，也不负责定时扫描；定时交给 dispatch，执行交给 apiExecutor。

关键证据：

- Core 服务基础路径是 `/core`，见 `baidu/qamate-server/core/src/main/resources/application.yml:58-61`。
- apismart 计划入口是 `/apismart/plan`，见 `ApiPlanController.java:27`；创建入口 `/create` 调 `createApiPlan`，见 `ApiPlanController.java:59-63`；手动执行入口 `/run` 调 `runApiPlan`，见 `ApiPlanController.java:87-90`。
- apismart 执行器回调/查询入口在 `/apismart/plan/executor`，见 `ApiPlanExeController.java:21-48`。
- Core 调 dispatch 的契约集中在 `DispatchClient`，包括创建、更新、删除、触发、启动、暂停、日志查询，见 `DispatchClient.java:26-61`。
- apismart 相关白名单包含 `/apismart/plan/run`、`/apismart/plan/execute/status`、`/apismart/plan/agile/run`、`/apismart/skill/save`、`/apismart/skill/usage/record`，见 `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/components/config/FilterConfig.java:98-103`。
- RequestFilter 的鉴权入口会读取 `QAMate-Token`、`QAMate-ModuleId` 等 header，见 `RequestFilter.java:44-49` 和 `RequestFilter.java:144-164`。

Core apismart 边界外依赖只作为外部依赖看待：

- 环境详情来自 Core 公共 `EnvService`，`ApiPlanServiceImpl` 注入点见 `ApiPlanServiceImpl.java:104-106`。
- 计划树和用例树依赖回归/用例公共服务，注入点见 `ApiPlanServiceImpl.java:94-102`。
- 这些依赖影响 apismart 计划参数生成，但本文不展开其业务域。

### 2. apiExecutor

职责：接收调度任务，拉取 Core 中的计划、用例、环境、脚本，按 setup / case / teardown 顺序执行，并把结果写回 Core 或上传结果文件。

关键证据：

- 服务基础路径是 `/executor`，端口默认 8995，见 `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application.yml:2-5`。
- `TaskController` 的任务入口是 `/task/case/submit`，见 `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/controller/TaskController.java:26-39`。
- XXL-JOB handler 名称是 `planExeHandler`，见 `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/jobhandler/PlanHandler.java:28-39`。
- `PlanRunner.startRunPlan()` 是计划执行入口，见 `PlanRunner.java:83-96`。
- `QAMateCoreClient` 调 Core 拉计划用例、环境详情、计划开始、步骤结果，见 `QAMateCoreClient.java:33-53`。

### 3. api-smart-dispatch

职责：基于 XXL-JOB 做 API Smart 调度中心，保存计划对应任务、根据 cron 触发任务、管理执行器注册和日志，并在任务完成后回调 Core。

关键证据：

- dispatch 默认上下文路径是 `/apismart/dispatch`，见 `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application.properties:1-3`。
- OpenAPI 统一入口是 `/api/{uri}`，见 `JobApiController.java:36-57`。
- OpenAPI 校验 `XXL-JOB-ACCESS-TOKEN`，见 `JobApiController.java:66-68`；并用 `userName` / `userToken` 构造登录上下文，见 `JobApiController.java:70-76`。
- `XxlJobInfo.planId` 是 dispatch 任务与 Core 计划的绑定点，见 `XxlJobInfo.java:12-15`。
- `JobScheduleHelper.start()` 扫描即将触发的任务并推入触发池，见 `JobScheduleHelper.java:37-230`。
- `JobCompleteHelper.callServerPlanEnd()` 回调 Core 计划结束，见 `JobCompleteHelper.java:207-232`。

### 4. inner-os/itp

职责：遗留 ITP / LTS 系统，包含老的智能服务入口、Dubbo/Hessian 服务暴露、密码字段处理和 LTS 轻量任务调度。

关键证据：

- `WebApplication` 是 ITP intelli 入口，并导入 Dubbo provider XML，见 `baidu/inner-os/itp/itp/itp-intelli/src/main/java/com/baidu/itp/intelli/WebApplication.java:21-23`。
- `WebApplication` 通过 Hessian 暴露/代理测试节点、计划、同步数据服务，见 `WebApplication.java:30-55`。
- `PasswordHandler` 对数据库字符串字段加 `encrypt::` 前缀并调用 DES-CBC 工具，见 `baidu/inner-os/itp/itp/itp-core/src/main/java/com/baidu/itp/core/handler/PasswordHandler.java:18-26` 和 `PasswordHandler.java:44-51`。
- DES-CBC 的 key/iv 硬编码，存在密钥治理风险，见 `baidu/inner-os/itp/itp/itp-core/src/main/java/com/baidu/itp/core/utils/DesCbcDecryptorUtil.java:16-20`。
- LTS Admin 配置了 Zookeeper 注册中心、队列和数据库配置，见 `baidu/inner-os/itp/lts/lts-admin/src/main/resources/lts-admin.cfg:5-25`。

## 关键类定义表

### Core / apismartmgt 关键类

| 层 | 类 / 接口 | 行号 | 维护含义 |
|---|---|---:|---|
| controller | `ApiPlanController` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ApiPlanController.java:28` | 计划列表、详情、创建、更新、删除、启停、执行入口。 |
| controller | `ApiPlanExeController` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ApiPlanExeController.java:22` | 执行器拉取用例、结果、日志、计划参数。 |
| controller | `ApiSkillController` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ApiSkillController.java:30` | API 技能保存和查询。 |
| controller | `ScriptTaskController` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ScriptTaskController.java:33` | 脚本模板、引用、测试、类型变更。 |
| controller | `ApismartBranchController` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/controller/ApismartBranchController.java:35` | 分支创建、分支任务、变更刷新和执行。 |
| service | `ApiPlanServiceImpl` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ApiPlanServiceImpl.java:92` | 计划创建、运行、参数生成和调度调用核心。 |
| service | `ApiPlanExeServiceImpl` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ApiPlanExeServiceImpl.java:74` | 执行记录、用例结果、日志聚合。 |
| service | `CallbackServiceImpl` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/CallbackServiceImpl.java:43` | 执行完成后告警/回调处理。 |
| service | `ScriptTaskServiceImpl` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ScriptTaskServiceImpl.java:44` | 脚本任务与 Worker 文件交互。 |
| service | `ApismartBranchServiceImpl` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ApismartBranchServiceImpl.java:68` | 分支、目录、任务同步等复杂逻辑。 |
| manager | `DispatchClient` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/client/DispatchClient.java:20` | Core 到 dispatch 的 Feign 契约。 |
| manager | `WorkerClient` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/client/WorkerClient.java:21` | Core 到 Worker 的 Feign 契约。 |
| manager | `FeignConfig` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/manager/FeignConfig.java:27` | Feign header、token、超时、重试策略。 |
| entity | `ApiPlanEntity` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/entity/ApiPlanEntity.java:23` | API Smart 计划持久化对象。 |
| entity | `ApiPlanExeEntity` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/entity/ApiPlanExeEntity.java:23` | 计划执行记录对象。 |
| entity | `ExeCaseResultEntity` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/entity/ExeCaseResultEntity.java:24` | 用例执行结果对象。 |
| entity | `ExeStepResultEntity` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/entity/ExeStepResultEntity.java:24` | 步骤执行结果对象。 |
| entity | `ScriptTaskEntity` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/entity/ScriptTaskEntity.java:22` | 脚本任务对象。 |
| mapper | `ApiPlanMapper` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/mapper/ApiPlanMapper.java:16` | 计划表访问。 |
| mapper | `ApiPlanExeMapper` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/mapper/ApiPlanExeMapper.java:16` | 计划执行表访问。 |
| mapper | `ExeCaseResultMapper` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/mapper/ExeCaseResultMapper.java:18` | 用例结果表访问。 |
| mapper | `ScriptTaskMapper` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/mapper/ScriptTaskMapper.java:16` | 脚本任务表访问。 |
| vo | `ApiPlanCreateParamVo` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/vo/plan/ApiPlanCreateParamVo.java:13` | 创建/更新/执行计划的入参。 |
| vo | `ApiPlanVo` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/vo/plan/ApiPlanVo.java:17` | 计划参数主体。 |
| vo | `PlanParamsVo` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/vo/plan/PlanParamsVo.java:17` | 传给执行器的计划参数。 |
| vo | `DispatchRequestVo` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/vo/dispatch/DispatchRequestVo.java:15` | 发给 dispatch 的请求体。 |
| vo | `DispatchResponseVo` | `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/vo/dispatch/DispatchResponseVo.java:11` | dispatch 响应体。 |

### apiExecutor 关键类

| 类 / 接口 | 行号 | 维护含义 |
|---|---:|---|
| `TaskController` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/controller/TaskController.java:27` | 外部任务提交入口。 |
| `PlanHandler` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/jobhandler/PlanHandler.java:28` | XXL-JOB 计划执行 handler，名称 `planExeHandler` 在 `PlanHandler.java:39`。 |
| `ExecutorConfiguration` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/async/ExecutorConfiguration.java:19` | 线程池配置。 |
| `TaskSubmitServiceImpl` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/async/impl/TaskSubmitServiceImpl.java:10` | 任务提交服务。 |
| `Delegator` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/runner/impl/Delegator.java:17` | 根据任务类型分派到 CaseRunner 或 PlanRunner。 |
| `PlanRunner` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/runner/impl/PlanRunner.java:66` | 计划执行管线核心。 |
| `CaseRunner` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/runner/impl/CaseRunner.java:47` | 单用例执行核心。 |
| `QAMateCoreClient` | `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/common/conf/feign/client/QAMateCoreClient.java:24` | 执行器回调 / 拉取 Core 数据的 Feign 契约。 |

### api-smart-dispatch 关键类

| 类 / 接口 | 行号 | 维护含义 |
|---|---:|---|
| `JobApiController` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/controller/openapi/JobApiController.java:37` | dispatch OpenAPI 总入口。 |
| `XxlJobServiceImpl` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/service/impl/XxlJobServiceImpl.java:35` | 任务增删改、按 planId 启停触发。 |
| `XxlJobInfo` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/model/XxlJobInfo.java:10` | XXL-JOB 任务模型，包含 `planId`。 |
| `JobScheduleHelper` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobScheduleHelper.java:22` | cron 扫描和时间轮。 |
| `JobTriggerPoolHelper` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobTriggerPoolHelper.java:26` | 快慢触发线程池。 |
| `JobCompleteHelper` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobCompleteHelper.java:34` | 执行完成回调和丢失任务补偿。 |

### inner-os/itp 关键类

| 类 / 配置 | 行号 | 维护含义 |
|---|---:|---|
| `WebApplication` | `baidu/inner-os/itp/itp/itp-intelli/src/main/java/com/baidu/itp/intelli/WebApplication.java:23` | ITP intelli Spring Boot 入口。 |
| Hessian Bean | `WebApplication.java:30-55` | 旧系统远程服务代理。 |
| `PasswordHandler` | `baidu/inner-os/itp/itp/itp-core/src/main/java/com/baidu/itp/core/handler/PasswordHandler.java:16` | MyBatis 字符串加解密 TypeHandler。 |
| `DesCbcDecryptorUtil` | `baidu/inner-os/itp/itp/itp-core/src/main/java/com/baidu/itp/core/utils/DesCbcDecryptorUtil.java:14` | DES-CBC 加解密工具，密钥硬编码。 |
| `TaskTracker` | `baidu/inner-os/itp/lts/lts-tasktracker/src/main/java/com/lts/tasktracker/TaskTracker.java:23` | LTS 任务执行节点。 |
| `JobPullMachine` | `baidu/inner-os/itp/lts/lts-tasktracker/src/main/java/com/lts/tasktracker/support/JobPullMachine.java:30` | TaskTracker 向 JobTracker 拉任务。 |
| `JobClient` | `baidu/inner-os/itp/lts/lts-jobclient/src/main/java/com/lts/jobclient/JobClient.java:41` | LTS 客户端提交任务。 |

## 全局配置项释义字典

| # | 配置项 | 位置 | 用途 | 风险点 | 改动影响 |
|---:|---|---|---|---|---|
| 1 | `server.servlet.context-path=/core` | `baidu/qamate-server/core/src/main/resources/application.yml:58-61` | Core HTTP 根路径。 | 改动会导致所有 `/core/*` 调用失效。 | apiExecutor、dispatch 回调路径都要同步改。 |
| 2 | `spring.profiles.active=dev` | `baidu/qamate-server/core/src/main/resources/application.yml:87-88` | Core 默认环境。 | 本地默认可能误连测试资源。 | 影响所有环境地址和数据源选择。 |
| 3 | `mybatis-plus.mapper-locations` | `baidu/qamate-server/core/src/main/resources/application.yml:56-57` | Mapper XML 加载位置。 | 路径错会导致 SQL 找不到。 | 数据访问启动失败或接口运行失败。 |
| 4 | `management.endpoints...include=prometheus` | `baidu/qamate-server/core/src/main/resources/application.yml:16-20` | 暴露 Prometheus 指标。 | 指标暴露路径也在白名单中。 | 监控采集会变化。 |
| 5 | `http.maxTotal` | `baidu/qamate-server/core/src/main/resources/application.yml:98-100` | HTTP 连接池总量和并发。 | 太小会阻塞外部调用，太大会压垮下游。 | 影响 Core 调外部服务吞吐。 |
| 6 | `http.socketTimeout` | `baidu/qamate-server/core/src/main/resources/application.yml:101-104` | HTTP 读超时。 | 超时过大拖慢线程释放。 | 影响慢调用排障和重试策略。 |
| 7 | `spring.datasource.dynamic.primary` | `baidu/qamate-server/core/src/main/resources/application-dev.yml:4-8` | Core 默认数据源。 | 默认源选错会读写错库。 | 影响所有未显式指定数据源的 Mapper。 |
| 8 | `spring.datasource.dynamic.datasource.newsource.*` | `baidu/qamate-server/core/src/main/resources/application-dev.yml:9-13`, `baidu/qamate-server/core/src/main/resources/application-online.yml:9-13` | Core 主业务库。 | 存在硬编码数据库连接/密码风险。 | 改错会导致 Core 主数据不可用。 |
| 9 | `apismart-dispatch` 数据源 | `baidu/qamate-server/core/src/main/resources/application-dev.yml:19-23`, `baidu/qamate-server/core/src/main/resources/application-online.yml:19-23` | Core 读取 dispatch 数据。 | 存在硬编码数据库连接/密码风险。 | 影响 apismart 调度日志/状态关联。 |
| 10 | `apismart-executor` 数据源 | `baidu/qamate-server/core/src/main/resources/application-dev.yml:24-28`, `baidu/qamate-server/core/src/main/resources/application-online.yml:24-28` | Core 读取 executor 数据。 | 存在硬编码数据库连接/密码风险。 | 影响执行结果/执行记录关联。 |
| 11 | `oldsource` 数据源 | `baidu/qamate-server/core/src/main/resources/application-dev.yml:29-33`, `baidu/qamate-server/core/src/main/resources/application-online.yml:14-18` | 旧数据源。 | 遗留库口径可能和新库不同。 | 影响兼容/迁移查询。 |
| 12 | `uuap.*` | `baidu/qamate-server/core/src/main/resources/application-dev.yml:53-65`, `baidu/qamate-server/core/src/main/resources/application-online.yml:51-62` | 登录鉴权和 token 生成。 | 存在硬编码 appKey/secret 风险。 | 改错会导致登录和鉴权失败。 |
| 13 | `ku.app-token` | `baidu/qamate-server/core/src/main/resources/application-dev.yml:68-71`, `baidu/qamate-server/core/src/main/resources/application-online.yml:64-67` | 知识库 OpenAPI token。 | 敏感 token 硬编码。 | 影响知识库相关鉴权。 |
| 14 | `dispatch.url` | `baidu/qamate-server/core/src/main/resources/application-dev.yml:98-100`, `baidu/qamate-server/core/src/main/resources/application-online.yml:94-95` | Core 调 dispatch 的 base URL。 | 环境错配会把计划发到错误调度中心。 | 计划创建、更新、手动执行都受影响。 |
| 15 | `worker.url` | `baidu/qamate-server/core/src/main/resources/application-dev.yml:117-121`, `baidu/qamate-server/core/src/main/resources/application-online.yml:112-116` | Core 调 Worker 的地址。 | 用户名/密码硬编码。 | 影响脚本上传、脚本任务。 |
| 16 | `comate.clientSecret` | `baidu/qamate-server/core/src/main/resources/application-dev.yml:135-141`, `baidu/qamate-server/core/src/main/resources/application-online.yml:43-49` | Comate 用户 token 获取。 | 敏感密钥硬编码。 | 影响 RequestFilter 注入 comate token。 |
| 17 | `FilterConfig.whitePathList` | `FilterConfig.java:51-107` | 免鉴权路径。 | 白名单过宽会绕过鉴权。 | 新回调接口若没加入可能被拒；误加入则暴露接口。 |
| 18 | `FeignConfig` dispatch header | `FeignConfig.java:35-43` | Core 调 dispatch 的 token 和用户上下文。 | `XXL-JOB-ACCESS-TOKEN` / user token 硬编码风险。 | 和 dispatch `xxl.job.accessToken` 必须一致。 |
| 19 | `FeignConfig.feignOptions` | `FeignConfig.java:84-87` | Feign 连接/读取超时。 | 读取 60 秒会占用线程。 | 影响 dispatch/worker 调用失败速度。 |
| 20 | `server.servlet.context-path=/executor` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application.yml:2-5` | 执行器 HTTP 根路径。 | Core 或外部调用路径依赖它。 | 改动需同步所有调用方。 |
| 21 | `apiExecutor spring.datasource.*` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:11-15`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:11-15` | 执行器数据库。 | 存在硬编码数据库连接/密码风险。 | 影响执行记录写入和查询。 |
| 22 | `qamate.core.url` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:24-28`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:24-28` | apiExecutor 回调 / 拉取 Core。 | 环境错配会把结果写到错误 Core。 | 计划执行数据会串环境。 |
| 23 | `executor.cluster` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:30-33`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:30-33` | 执行器集群名称和地址。 | 与 dispatch 执行器配置不一致会调不到。 | 影响任务路由。 |
| 24 | `xxl.job.admin.addresses` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:46-50`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:43-47` | 执行器注册到哪个调度中心。 | 环境错配会注册错调度中心。 | 任务无法触发或触发到错环境。 |
| 25 | `xxl.job.admin.accessToken` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:46-51`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:43-48` | 执行器和 dispatch 的 access token。 | token 硬编码。 | token 不一致会注册/回调失败。 |
| 26 | `xxl.job.executor.port` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:52-56`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:49-53` | 执行器监听端口。 | 端口冲突或防火墙会导致调度失败。 | dispatch 触发不到 executor。 |
| 27 | `file.root.path` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:38-40`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:35-37` | 脚本/文件根目录。 | 本地绝对路径和线上路径不同。 | 影响脚本读取和结果落盘。 |
| 28 | `script.path` | `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-dev.yml:42-44`, `baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:39-41` | 脚本执行目录和用户。 | 权限错会导致脚本执行失败。 | 影响脚本类用例。 |
| 29 | `dispatch server.servlet.context-path` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application.properties:1-3` | dispatch 根路径。 | Core Feign 已写 `/apismart/dispatch/api/*`。 | 改动会破坏 Core 到 dispatch。 |
| 30 | `dispatch spring.datasource.*` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-dev.properties:38-42`, `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:38-42` | dispatch XXL-JOB 库。 | 存在硬编码数据库连接/密码风险。 | 影响调度任务、日志、执行器注册。 |
| 31 | `xxl.job.accessToken` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application.properties:39-40`, `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:55-56` | dispatch OpenAPI token。 | token 硬编码。 | 必须和 Core `FeignConfig`、executor 配置一致。 |
| 32 | `xxl.job.triggerpool.fast.max` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application.properties:48-50` | 快慢触发线程池大小。 | 太小积压，太大压垮执行器。 | 影响调度峰值吞吐。 |
| 33 | `xxl.job.logretentiondays` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application.properties:52-53` | 调度日志保留天数。 | 太短不利排障，太长占库。 | 影响历史问题追踪。 |
| 34 | `qamate.core.planend` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-dev.properties:77`, `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:77` | dispatch 回调 Core 计划结束 URL。 | 地址错会导致计划永远不结束。 | 影响计划状态闭环。 |
| 35 | `qamate.moduleid` / `qamate.token` | `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-dev.properties:78-79`, `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:78-79` | 回调 Core 鉴权 header。 | token 硬编码。 | 和 Core RequestFilter 校验强绑定。 |
| 36 | ITP Nacos global properties | `baidu/inner-os/itp/itp/itp-tasktracker/src/main/profiles/dev/nacos-config.xml:12-15` | ITP TaskTracker 配置中心。 | 用户名/密码硬编码。 | 配置拉取失败会影响旧任务执行。 |
| 37 | LTS `registryAddress` | `baidu/inner-os/itp/lts/lts-admin/src/main/resources/lts-admin.cfg:5-7` | LTS Zookeeper 注册中心。 | 地址不可用会导致节点发现失败。 | JobTracker/TaskTracker 无法组成集群。 |
| 38 | LTS `configs.job.queue` | `baidu/inner-os/itp/lts/lts-admin/src/main/resources/lts-admin.cfg:18-25` | LTS 任务队列存储。 | 数据库凭据硬编码。 | 影响旧调度任务存取。 |
| 39 | ITP Dubbo registry/protocol | `baidu/inner-os/itp/itp/itp-intelli/src/main/profiles/prod/dubbo-provider.xml:17-21` | 旧 Dubbo 服务注册和暴露。 | 注册中心或端口变动会影响调用方。 | 旧 RPC 调用不可用。 |
| 40 | DES-CBC key/iv | `baidu/inner-os/itp/itp/itp-core/src/main/java/com/baidu/itp/core/utils/DesCbcDecryptorUtil.java:16-20` | 旧密码字段加解密。 | 固定密钥硬编码，且 DES 算法过旧。 | 改动会导致历史密文无法解密。 |

## 部分 B：代码逻辑补完

### 复杂函数 1：Core `ApiPlanServiceImpl.createApiPlan()`

位置：`baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/service/impl/ApiPlanServiceImpl.java:267-340`

#### 逐段解释

1. 参数校验：`planName`、`moduleId`、`planParams`、`cronType` 必填，见 `ApiPlanServiceImpl.java:269-274`。这一步像前台确认订单上至少有菜名、桌号、内容和上菜时间类型。
2. Diff 计划专项校验：如果 `isDiffPlan=true`，必须有 `cloudParams`，且第一组参数里必须同时有 `testEnvParam` 和 `stableEnvParam`，见 `ApiPlanServiceImpl.java:275-288`。Diff 像“同一道菜做两份对比”，缺任一环境都不能比。
3. 补环境详情：调用 `addEnvDetail(apiPlanCreateParamVo)`，见 `ApiPlanServiceImpl.java:290`；该方法遍历 `cloudParams` 并对 test/stable 环境调用 `fillEnvDetail`，见 `ApiPlanServiceImpl.java:343-369`。
4. 组装并保存 `ApiPlanEntity`：把模块、cron、计划名、计划参数 JSON、enable、用户、时间写入实体，见 `ApiPlanServiceImpl.java:292-315`。
5. 处理目录树：如果入参有 `treeNodeIdList`，调用 `updateTreeNodeListInfos` 和 `regressionPlanService.getFinalForest` 生成完整树并写入 `nodeTree`，见 `ApiPlanServiceImpl.java:303-311`。
6. 生成执行参数：保存后拿到 `planId`，再调用 `generatePlanParams(...)`，见 `ApiPlanServiceImpl.java:316-319`。注意：执行参数依赖数据库生成的计划 ID。
7. 调 dispatch 创建任务：把 `planId`、计划名、用户、cron、cronType、executorParam 包成 `DispatchRequestVo`，见 `ApiPlanServiceImpl.java:321-330`；再调用 `dispatchClient.addDispatchJob`，见 `ApiPlanServiceImpl.java:331-335`。
8. 处理调度响应：dispatch 返回 code 不等于 200 就抛异常，见 `ApiPlanServiceImpl.java:337-339`；方法有 `@Transactional`，见 `ApiPlanServiceImpl.java:268`，因此异常会回滚 Core 计划保存。

#### 诊断

- SRP：偏重。一个函数同时做参数校验、环境补全、树展开、数据库保存、执行参数生成、远程调度创建。
- CQS：违反倾向明显。它返回 `planId`，但同时修改数据库并调用远程服务。
- 隐藏状态：依赖 `ContextHolder.getUser()` 写更新用户，见 `ApiPlanServiceImpl.java:313` 和 `ApiPlanServiceImpl.java:319`；维护时要确认 RequestFilter 是否已正确写入上下文。
- 性能：`getFinalForest` 和 `generatePlanParams` 可能访问其他服务/数据库，创建计划不是单纯插表。
- 安全：调 dispatch 的鉴权不在本函数里，而在 `FeignConfig` 中硬编码 header，见 `FeignConfig.java:35-43`；这是敏感配置治理风险。
- 事务风险：本地数据库事务包住远程 dispatch 调用。若 Core 保存成功后 dispatch 调用超时但实际创建成功，可能出现“Core 回滚、dispatch 已创建”的跨服务不一致。

#### 重构建议

- 抽出 `validateCreatePlanParam()`、`buildApiPlanEntity()`、`buildDispatchRequest()` 三个私有方法，先降低阅读成本。
- dispatch 调用建议放在“本地事务提交后”的补偿型流程，或者引入可重试的 outbox 记录，避免远程调用参与数据库事务。
- 将 dispatch token/userName/userToken 从 `FeignConfig` 硬编码迁移到安全配置中心，保持当前 header 名不变。
- Diff 校验不要只检查 `cloudParams[0]`，如果业务允许多组环境，应逐组校验。

### 复杂函数 2：apiExecutor `PlanRunner.startRunPlan()`

位置：`baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/runner/impl/PlanRunner.java:86-297`

#### 逐段解释

1. 读取执行身份：取 `logId`、`planExeId`、`planId`、diff 字段和 diff 模式，见 `PlanRunner.java:86-92`。
2. 设置追踪号并通知 Core 开始：`TraceUtil.setTraceId` 后调用 `planExecuteService.callServerStart(planId, planExeId)`，见 `PlanRunner.java:92-96`。
3. 初始化计划状态和环境对象：默认状态设为 `RUNNING`，创建 test/stable 环境对象，见 `PlanRunner.java:97-102`。
4. 从 Core 拉环境详情：如果有 `envId`，调用 `planExecuteService.getEnvDetail`；如果拉不到，就用入参携带的 `envDetail`，见 `PlanRunner.java:103-121`。
5. 用户参数覆盖计划配置：`userParams` 中的全局变量和 serverConfig 覆盖环境详情，见 `PlanRunner.java:123-131`；具体覆盖逻辑在 `updateEnvDetail()`，见 `PlanRunner.java:299-350`。
6. 拉用例列表：如果目录为空，插入执行计划记录并成功结束，见 `PlanRunner.java:135-143`；否则调用 `planExecuteService.getPlanCaseList(folderIdList)`，见 `PlanRunner.java:147-159`。
7. 顺序执行 setup / case / teardown：三段都是先从 Core 拉 caseInfo，再填充环境和 diff 字段，再转成 `RunnerTask`，最后调用 `run(...)`，见 `PlanRunner.java:164-197`、`PlanRunner.java:199-237`、`PlanRunner.java:240-278`。
8. 根据聚合状态告诉 XXL-JOB 成败：如果 `taskHolder.planExeStatus != RUN_SUCCESS`，调用 `XxlJobHelper.handleFail`，见 `PlanRunner.java:282-288`。
9. 清理上下文：代码注释明确说明线程和 `PlanRunner` 实例会复用，所以计划结束要清理，见 `PlanRunner.java:289-296`。

#### 诊断

- SRP：过重。它同时负责环境解析、用户参数覆盖、拉用例、顺序编排、执行、状态聚合、清理。
- CQS：明显命令式函数，无返回值但有大量外部副作用：通知 Core、插库、执行用例、写日志、设置 XXL-JOB 状态。
- 隐藏状态：`taskHolder` 是实例字段，见 `PlanRunner.java:78`；因为 `PlanRunner` 是 prototype，但注释又说明线程和实例会复用，必须依赖 `runTeardown()` 清理，见 `PlanRunner.java:360-362`。
- 性能：setup/case/teardown 全部串行，且代码 TODO 写明后续支持并发，见 `PlanRunner.java:164`。大计划会被最长用例拖慢。
- 安全：日志会输出环境详情和 caseFileInfo，见 `PlanRunner.java:132-133`、`PlanRunner.java:193-196`、`PlanRunner.java:233-236`，如果环境参数含敏感变量，日志可能泄露。
- 稳定性：在 setup 阶段先 `fillCaseFileDtoEnv(caseFileDto, ...)` 再判断 `caseFileDto == null`，见 `PlanRunner.java:174-181`，理论上存在空指针风险。

#### 重构建议

- 先修正空指针顺序：拉取 `caseFileDto` 后先判空，再填充环境。
- 把 setup/case/teardown 的重复逻辑抽成 `runCaseGroup(label, ids, ...)`，统一日志、判空、参数填充。
- 把 `taskHolder` 改成方法内局部聚合对象，或者在 `try/finally` 中强制清理，避免异常路径绕过 `runTeardown()`。
- 给日志增加脱敏：环境参数、serverConfig、caseFileInfo 输出前过滤 token/password/secret/key。
- 并发化前先定义顺序约束：setup 必须先于 case，teardown 是否在 case 失败后仍执行，需要明确业务规则。

### 复杂函数 3：dispatch `JobCompleteHelper.callServerPlanEnd()`

位置：`baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobCompleteHelper.java:207-243`

#### 逐段解释

1. 加载当前 profile：通过 `DynamicConfigLoader.getActiveProfile()` 获取环境名并加载 profile 配置，见 `JobCompleteHelper.java:209-218`。
2. 读取回调配置：从配置中读 `qamate.core.planend`、`qamate.moduleid`、`qamate.token`，见 `JobCompleteHelper.java:220-223`。
3. 构造请求体：写入 `planExeId`、`status`、`endTime` 秒级时间戳，见 `JobCompleteHelper.java:224-227`。
4. 构造鉴权 header：写 `Content-Type`、`QAMate-ModuleId`、`QAMate-Token`，见 `JobCompleteHelper.java:228-231`。
5. HTTP POST 到 Core：调用 `HttpClientUtil.doPost(planEndUrl, request.toString(), headers)`，见 `JobCompleteHelper.java:232`。
6. 解析响应：把返回字符串解析成 JSON，`code == 0` 认为成功，否则打印错误日志，见 `JobCompleteHelper.java:233-240`。
7. 异常吞掉：catch 只记录 `planExeId` 和异常信息，见 `JobCompleteHelper.java:241-243`。

#### 诊断

- SRP：偏重但范围可控。它既读取配置，又构造请求，又发 HTTP，又解释响应。
- CQS：纯命令式函数，没有返回值；失败只写日志，不把失败反馈给上层。
- 隐藏状态：依赖 `DynamicConfigLoader` 的当前 profile 和配置文件；运行环境决定最终回调地址。
- 性能：每次回调都尝试加载 profile 配置，见 `JobCompleteHelper.java:209-218`，高频回调时有重复成本。
- 安全：`qamate.token` 在配置文件中硬编码，见 `application-dev.properties:77-79` 和 `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:77-79`；日志打印 request 和 response，虽然 request 不含 token，但 response 可能包含敏感信息，见 `JobCompleteHelper.java:233`。
- 可靠性：HTTP 失败无重试、无持久化补偿、无告警升级。Core 没收到结束通知时，计划可能长时间停留在运行中。

#### 重构建议

- 配置读取改为启动时注入或缓存，避免每次回调加载 profile。
- 函数返回明确结果对象，例如 `CallbackResult(success, code, message)`，让上层可以重试或统计。
- 增加有限重试和失败落库，后续由补偿线程重放。
- token 使用配置中心或密钥管理；日志禁止打印包含 token/password/secret 的响应体。

### 复杂函数 4：dispatch `JobScheduleHelper.start()`

位置：`baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/java/com/xxl/job/admin/scheduler/thread/JobScheduleHelper.java:37-230`

#### 逐段解释

1. 创建 schedule 线程并对齐秒级时间，见 `JobScheduleHelper.java:37-52`。
2. 计算预读数量：快慢触发池大小乘以 20，见 `JobScheduleHelper.java:54-55`。这是用触发池容量估算未来 5 秒能处理多少任务。
3. 每轮开启事务和调度锁：获取事务和 `scheduleLock()`，见 `JobScheduleHelper.java:64-69`。
4. 查询即将触发的任务：`scheduleJobQuery(nowTime + PRE_READ_MS, preReadCount)`，见 `JobScheduleHelper.java:71-72`。
5. 处理严重超时任务：超过预读窗口则按 misfire 策略选择是否立即触发，并刷新下次触发时间，见 `JobScheduleHelper.java:78-95`。
6. 处理轻微超时任务：直接触发并刷新；如果下一次仍在 5 秒内，则放入时间轮，见 `JobScheduleHelper.java:96-120`。
7. 处理未来 5 秒内任务：放入时间轮并刷新下次触发时间，见 `JobScheduleHelper.java:122-133`。
8. 更新任务触发信息并提交事务，见 `JobScheduleHelper.java:138-154`。
9. 创建 ringThread：每秒取当前秒和上一秒的时间轮数据，逐个触发任务，见 `JobScheduleHelper.java:181-230`。

#### 诊断

- SRP：重。一个方法创建两个线程、管理锁、事务、扫描、时间轮和触发。
- CQS：命令式启动函数，副作用是启动后台线程并持续修改数据库触发时间。
- 隐藏状态：`ringData` 是 static `ConcurrentHashMap`，见 `JobScheduleHelper.java:28-32`；多个实例或测试场景下状态共享。
- 性能：预读数量依赖触发池大小，`triggerpool.fast.max` 和 `slow.max` 配置见 `application.properties:48-50`，配置过大可能造成瞬时触发洪峰。
- 安全：调度本身不处理鉴权，但它触发的 executorParam 可能来自 Core 计划参数，不能在日志中无脑输出。
- 事务风险：catch 后 finally 仍 commit，见 `JobScheduleHelper.java:147-154`；若循环中部分更新异常，需要确认事务管理器是否已标记 rollback-only。

#### 重构建议

- 把 scheduleThread 和 ringThread 的 Runnable 拆成独立私有类，便于单测。
- 明确异常时事务 rollback 规则，避免 catch 后继续 commit。
- 对 `ringData` 封装访问方法，方便观测当前时间轮积压。
- 把预读数量和触发池配置加入监控，避免只靠日志排查调度延迟。

## 常见维护动作

### 新增或修改 apismart 计划接口

1. 先看 `ApiPlanController.java:27-143` 确认入口路径。
2. 再看 `ApiPlanServiceImpl.java:92-134` 注入的依赖，判断是否会跨服务。
3. 如果要调用 dispatch，同步核对 `DispatchClient.java:26-61` 和 dispatch `JobApiController.java:94-127`。
4. 如果是异步回调入口，同步检查 `FilterConfig.java:51-107` 是否需要白名单；白名单不要随意扩大。

### 排查“计划创建成功但没有调度”

1. Core 是否调用 `dispatchClient.addDispatchJob`：`ApiPlanServiceImpl.java:321-335`。
2. Core 的 `dispatch.url` 是否指向正确环境：`application-dev.yml:98-100` 或 `baidu/qamate-server/core/src/main/resources/application-online.yml:94-95`。
3. Core Feign header token 是否和 dispatch `xxl.job.accessToken` 一致：`FeignConfig.java:39-42` 与 `application.properties:39-40`。
4. dispatch OpenAPI 是否收到 `/api/jobInfoAdd`：`JobApiController.java:94-98`。
5. dispatch 库中 `XxlJobInfo.planId` 是否存在：模型字段见 `XxlJobInfo.java:12-15`。

### 排查“计划一直运行中”

1. apiExecutor 是否调用 Core 开始：`PlanRunner.java:92-96`。
2. `PlanRunner` 是否在失败时调用 `XxlJobHelper.handleFail`：`PlanRunner.java:282-288`。
3. dispatch callback 是否调用 `callServerPlanEnd`：`JobCompleteHelper.java:194-203`。
4. `qamate.core.planend` 是否正确：`application-dev.properties:77` 或 `baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:77`。
5. 回调 token/moduleId 是否能通过 Core RequestFilter：`JobCompleteHelper.java:228-232` 与 `RequestFilter.java:147-164`。

### 修改敏感配置

不要在文档或提交说明中复制完整值。当前仓库已有多处硬编码风险：

- Core 通用 token 和外部系统密钥：`application.yml:45-50`、`application.yml:119-146`。
- Core 环境数据库密码：`application-dev.yml:9-38`、`baidu/qamate-server/core/src/main/resources/application-online.yml:9-28`。
- Core dispatch Feign header token：`FeignConfig.java:39-42`。
- apiExecutor 数据库和 XXL-JOB token：`application-dev.yml:11-15`、`application-dev.yml:46-51`、`baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:11-15`、`baidu/qamate-server/apiExecutor/executor-server/src/main/resources/application-prod.yml:43-48`。
- dispatch 数据库、accessToken、回调 token：`baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:38-42`、`baidu/qamate-server/api-smart-dispatch/xxl-job-admin/src/main/resources/application-prod.properties:55-79`。
- ITP Nacos、LTS、DES 密钥：`nacos-config.xml:12-15`、`lts-admin.cfg:23-25`、`baidu/inner-os/itp/itp/itp-core/src/main/java/com/baidu/itp/core/utils/DesCbcDecryptorUtil.java:16-20`。

## 维护护栏

- 不要随意修改 `/apismart/dispatch/api/*`、`/executor/*`、`/core/*` 这些跨服务已消费路径。
- Core 只把 apismart 作为主体维护；看到 lumos/kamix/debug 依赖时，先判断是不是 apismart 的直接依赖。
- 新增回调接口时同时检查白名单、鉴权 header、调用方配置。
- 调度相关问题必须同时看 Core `DispatchClient` 和 dispatch `JobApiController` / `XxlJobServiceImpl`。
- 执行相关问题必须同时看 dispatch 触发、apiExecutor handler、`PlanRunner`、Core 回调。
- 对 token、密码、数据库连接串只做脱敏描述，不复制完整值。

