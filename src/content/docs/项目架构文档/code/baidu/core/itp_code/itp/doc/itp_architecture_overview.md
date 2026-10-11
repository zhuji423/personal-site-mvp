---
title: "ITP 系统架构与接口梳理"
description: "ITP Intelligent Test Platform 是一个分布式自动化测试平台。其核心组件包括："
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\itp_architecture_overview.md"
---
# ITP 系统架构与接口梳理

## 1. 整体架构概述

ITP (Intelligent Test Platform) 是一个分布式自动化测试平台。其核心组件包括：

*   **ITP-Web**: 后台管理系统。负责测试用例维护、测试计划配置、任务触发、报表展示等。它是用户交互的主要入口。
*   **LTS JobTracker**: 任务调度调度中心。基于 LTS (Lightweight Task Scheduler) 框架，负责任务的接收、分配、重试监控以及状态管理。
*   **ITP-TaskTracker**: 任务执行节点。负责具体的测试用例执行（HTTP, Dubbo, SQL, Mongo 等），并向 JobTracker 上报执行结果。

### 核心任务流转
1.  **用户** 在 `ITP-Web` 发起执行请求。
2.  `ITP-Web` 调用 `JobClient` 将任务提交给 `LTS JobTracker`。
3.  `LTS JobTracker` 根据配置将任务下发给可用的 `ITP-TaskTracker`。
4.  `ITP-TaskTracker` 的 `JobRunner` 接收并解析任务，开始执行具体的测试逻辑。
5.  执行完成后，`ITP-TaskTracker` 返回执行结果给 `LTS JobTracker`。
6.  `LTS JobTracker` 更新任务状态，并通知 `ITP-Web`（通过 `JobCompletedHandler`）。

---

## 2. 模块职责详述

### 2.1 ITP-Web
*   **职责**: 业务配置、权限控制、数据持久化、结果聚合展示、OpenAPI。
*   **通信接口**: 提供 HTTP/RESTful 接口供前端调用，提供部分 API 供外部系统集成。

### 2.2 ITP-TaskTracker
*   **职责**: 具体的测试执行引擎。支持多种协议的 Executor。
*   **通信接口**: 作为 LTS 的从节点，通过 Remoting 协议与 JobTracker 通信；同时也通过 Dubbo 暴露直接提交任务的接口。

### 2.3 LTS JobTracker
*   **职责**: 任务调度中枢。处理任务提交、分配、拉取、反馈、容错。
*   **通信接口**: 基于 Netty 的私有 Remoting 协议（与 JobClient 和 TaskTracker 通信）；提供 HTTP 运维命令接口。

---

## 3. 文档目录
*   [ITP-Web 接口梳理](./itp_web_interfaces.md)
*   [ITP-TaskTracker 接口梳理](./itp_tasktracker_interfaces.md)
*   [LTS JobTracker 接口梳理](./lts_jobtracker_interfaces.md)
