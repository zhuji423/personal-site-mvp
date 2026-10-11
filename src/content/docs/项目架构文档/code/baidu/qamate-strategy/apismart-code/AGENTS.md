---
title: "AGENTS 指南"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy\\apismart-code\\AGENTS.md"
---
# AGENTS 指南

## 范围与全局视图
- 该工作区包含两套独立产品线：`baidu/qamate-server`（现行服务）与 `baidu/inner-os/itp`（遗留 ITP + LTS）。
- 除非任务明确要求，不做跨产品线重构；优先在单一栈内完成改动。
- `qamate-server` 目前有 3 个协作服务：`core`（业务编排）、`apiExecutor`（执行引擎）、`api-smart-dispatch`（调度中心）。
- 关键链路：`core` 通过 `DispatchClient` 调用 `api-smart-dispatch` 的 `/apismart/dispatch/api/*`；调度完成后 `api-smart-dispatch` 在 `JobCompleteHelper.callServerPlanEnd` 回调 `core`。
- 另一条关键链路：`core` 通过 `UrlConfig.INTERFACE_DEBUG_TASK_CREATE` 调用 `apiExecutor` 的 `/executor/task/case/submit`，由 `TaskController` 接收并下发执行。

## 架构与代码模式
- `core` 采用高模块化结构（`com/baidu/qamate/core/*mgt`），常见分层是 `controller -> service -> manager -> mapper/entity/vo`（例：`apismartmgt`）。
- `core` 对外系统交互主要走 Feign（例：`apismartmgt/manager/client/DispatchClient.java`、`WorkerClient.java`）。
- `core` 鉴权/回调白名单集中在 `components/config/FilterConfig.java`；新增异步回调接口要同步更新白名单。
- `core` 环境切换 URL 集中在 `components/config/UrlConfig.java`，通过 `EnvironmentModule.getEnv()` 选择。
- `apiExecutor` 为控制器入口型：`controller/*` 接请求，`runner/*` + `async/*` + `service/*` 执行业务。
- `api-smart-dispatch` 基于 XXL-JOB 二次开发：主应用在 `xxl-job-admin`，开放 API 入口在 `controller/openapi/JobApiController.java`，调度核心在 `service/impl/XxlJobServiceImpl.java`。
- `api-smart-dispatch` 关键数据模型是 `XxlJobInfo`（含 `planId` 关联），大量能力通过 `*ByPlanId` 接口暴露，和 `core` 的测试计划强绑定。

## 构建与 CI（项目特定）
- `qamate-server/core`：`core/ci.yml` 映射 `dev-build.sh`（`-Pdev`）、`build.sh`（`-Ptest`）、`test-aird-build.sh`（`-Ptest-aird`）、`publish.sh`（`-Ponline`）。
- `qamate-server/apiExecutor`：`build.sh` 与 `publish.sh` 都默认 `-Dmaven.test.skip=true`，并将部署资产打到 `output/`（jar + protoc + Python + logconfig + worker 脚本）。
- `qamate-server/api-smart-dispatch`：`ci.yml` 使用 JDK17/Maven3.8.6，`build.sh` 执行 `mvn package`，`postBuild.sh` 固定产物路径为 `output/api-smart-dispatch.jar`。
- `api-smart-dispatch` 模块为 `xxl-job-core` + `xxl-job-admin`（见 `api-smart-dispatch/pom.xml`），日常改动通常落在 `xxl-job-admin`。
- `inner-os/itp` 构建入口是仓库根脚本（`build-web.sh`、`build-tt.sh`、`build-executor.sh` 等），由 `inner-os/itp/ci.yml` profile 编排。
- 遗留 ITP 仍依赖旧工具链（JDK8 / Maven3.0.x）；`qamate-server` 各服务多为 JDK17/21。

## 运行时与集成注意事项
- POM 依赖大量内网仓库（`maven.baidu-int.com` / `maven.scm.baidu.com`）；缺少内网环境时构建常失败。
- `core` 使用多数据源与多外部系统（UUAP、dispatch、worker、kami/ku/lumos/qianfan），配置集中在 `application-*.yml`。
- `api-smart-dispatch` 默认上下文路径是 `/apismart/dispatch`（`xxl-job-admin/src/main/resources/application.properties`），`core` 的 `DispatchClient` 已按此路径对接。
- `api-smart-dispatch` OpenAPI 校验 `XXL-JOB-ACCESS-TOKEN`，并依赖请求头 `userName`/`userToken` 构造登录上下文（见 `JobApiController`）。
- `api-smart-dispatch` 在任务回调后会向 `core` 发送计划结束通知，并携带 `QAMate-ModuleId`、`QAMate-Token` 头（见 `JobCompleteHelper.callServerPlanEnd`）。
- 三个 qamate 服务的 Docker 镜像都包含内部 agent（如 SkyWalking / RASP / log-agent），环境变量会直接影响启动与可观测性。

## 约定与护栏（给 Agent）
- 涉及调度相关需求时，优先同时检查 `core` 与 `api-smart-dispatch` 的接口契约，不只改单边。
- 不要随意修改 `/apismart/dispatch/api/*`、`/executor/*`、`/core/*` 这些跨服务已消费的路径与字段语义。
- 非配置治理任务，不要清理或抽离现有硬编码 URL/凭据块；先保持行为兼容。
- 该仓库大量脚本默认跳过测试；若新增测试，需在变更说明里明确手工执行方式。
- 新增后端代码优先沿用现有命名与分层风格（`*mgt`、`controller`、`manager`、`mapper`、`vo`）。


