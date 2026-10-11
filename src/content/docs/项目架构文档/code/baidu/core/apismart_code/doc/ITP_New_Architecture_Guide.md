---
title: "ITP 新旧架构深度对比指南 (LTS vs XXL-JOB)"
description: "本文档旨在帮助开发人员理解从老一代 ITP LTS 框架 迁移到新一代 apismart XXL-JOB 框架 后的架构变化，特别是核心组件的映射关系及设计理念的差异。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\apismart_code\\doc\\ITP_New_Architecture_Guide.md"
---
# ITP 新旧架构深度对比指南 (LTS vs XXL-JOB)

本文档旨在帮助开发人员理解从老一代 ITP (LTS 框架) 迁移到新一代 apismart (XXL-JOB 框架) 后的架构变化，特别是核心组件的映射关系及设计理念的差异。

## 1. 核心组件映射与对比

在 apismart (新 ITP) 中，架构被简化，组件职责发生了合并。

| 角色功能 | ITP (LTS 架构) | apismart (XXL-JOB 架构) | 变化核心 |
| :--- | :--- | :--- | :--- |
| **注册中心** | **Zookeeper (ZK)** | **XXL-JOB Admin (调度中心)** | 去除 ZK 依赖，改用 HTTP 心跳注册 |
| **调度大脑** | **JobTracker** | **XXL-JOB Admin (调度中心)** | 调度与管理合二为一 |
| **任务执行** | **TaskTracker** | **apiExecutor (执行器)** | 角色一致，均为无状态节点 |
| **任务提交** | **JobClient (ITP-Web)** | **(消失/融合)** -> Admin Console / API | 生产者角色被淡化，转为配置化 |
| **数据存储** | MySQL / Mongo | MySQL | 强依赖 DB 实现分布式锁 |

---

## 2. 深入理解 apismart 的“执行器”与“注册中心”

### 2.1 注册中心 (Registry) -> 实际上是 Admin
在 apismart 中，没有独立的 ZK 集群来做注册中心。
*   **组件**: `api-smart-dispatch` (即 xxl-job-admin)。
*   **机制**:
    *   **被动接收**: Admin 提供了一个 RESTful API (`/api/registry`)。
    *   **数据存储**: 注册信息存储在 MySQL 表 `xxl_job_registry` 中。
    *   **故障摘除**: Admin 后台线程每 30 秒检查一次注册表，剔除超过 90 秒未续期的节点。

### 2.2 执行器 (Executor) -> apiExecutor
这是业务代码实际运行的地方。
*   **组件**: `apiExecutor` (Spring Boot 应用)。
*   **配置**:
    *   在 `XxlJobConfig.java` 中读取 `xxl.job.admin.addresses`。
    *   启动时，`XxlJobSpringExecutor` 会启动一个后台线程。
*   **自动注册**:
    *   执行器每隔 30 秒，向配置的 `adminAddresses` 发起 HTTP 请求，汇报自己的 AppName (如 `xxl-job-executor-sample`) 和 IP:Port。
    *   这就是为什么你看不到 ZK 的原因，**注册行为变成了 HTTP 请求**。

---

## 3. 它们怎么实现“对方没有的概念”？

这是两种框架最根本的设计冲突点。

### 3.1 XXL-JOB 如何实现 LTS 的 "JobClient" (提交者)？
LTS 强调“提交者”是因为它的任务往往是动态生成的（Producer-Consumer 模型）。XXL-JOB 默认没有独立的 Client。

*   **实现方式 1：Web 图形化配置 (主)**
    *   XXL-JOB 认为任务大多数是**静态的**（Cron 定时任务）。
    *   **替代方案**: 管理员直接在 Admin 控制台录入任务信息。这相当于“人工 Client”。
*   **实现方式 2：Admin API (辅)**
    *   如果业务需要动态提交任务，可以使用 Admin 提供的 OpenAPI (`/jobinfo/add` 或 `/jobinfo/trigger`)。
    *   **逻辑**: 你的业务系统 (ITP-Web) 直接调用 Admin 的 HTTP 接口。
    *   **本质**: 此时，ITP-Web 充当了轻量级的 JobClient。

### 3.2 LTS 如何实现 XXL-JOB 的 "Admin" (管理台)？
LTS 也有 `lts-admin`，但功能很弱，主要看日志。LTS 缺乏一个中心化的、强管控的“任务管理中心”。

*   **实现方式：业务代码自建**
    *   在 LTS 架构下，开发者通常需要在自己的 Web 系统 (ITP-Web) 里开发一套表格页面，用来展示任务、记录任务状态。
    *   **逻辑**: 开发者不得不重复造轮子，在数据库里记录 `TaskID`，然后由 Web 系统去查询状态。
    *   **代价**: 这也是 ITP 旧架构复杂的原因之一 —— 业务系统承担了太多的管理职责。

### 3.3 XXL-JOB 如何实现 LTS 的 "Zookeeper" (协调者)？
LTS 依赖 ZK 做节点发现和 JobTracker 的主从选举。XXL-JOB 去掉了 ZK。

*   **实现方式：DB 锁 + HTTP**
    *   **选主**: XXL-JOB Admin 并不需要选主（它是无状态的集群），但在触发任务时，利用 MySQL 的 `for update` (行锁) 来防止任务被重复触发。
    *   **发现**: 执行器直接把 IP 告诉 Admin（写入 DB）。Admin 调度时查询 DB 获取 IP 列表，然后通过 HTTP RPC 也就是 `XxlJobRemotingUtil` 发送调度请求。

### 3.4 框架详细对比表 (Cheat Sheet)

为了方便快速查阅，以下是两个框架维度的详细对比：

| 维度 | **apismart (XXL-JOB)** | **ITP (LTS)** | 关键差异 |
| :--- | :--- | :--- | :--- |
| **架构哲学** | **中心化** (Centralized) | **去中心化** (Decentralized) | XXL-JOB 调度中心掌握绝对控制权；LTS 节点相对平等，依赖 ZK 协调。 |
| **基础依赖** | **MySQL** (核心依赖) | **Zookeeper** (注册/协调) + MySQL/Mongo (存储) | XXL-JOB 部署更轻量，只需 DB；LTS 运维组件更复杂。 |
| **角色组成** | 1. 调度中心 (Admin)<br>2. 执行器 (Executor) | 1. 调度器 (JobTracker)<br>2. 执行器 (TaskTracker)<br>3. 提交者 (JobClient)<br>4. 监控台 (LTS-Admin) | XXL-JOB 只有两层角色，简化了系统拓扑。 |
| **任务提交方式** | **图形化 Web 配置** (主流) <br>或 API 触发 | **代码 SDK 提交** (JobClient.submitJob) | XXL-JOB 偏向静态配置与 Cron；LTS 偏向动态生成的实时任务。 |
| **通信交互** | **Push 模式** (调度中心 -> 执行器) | **Push/Pull 结合** (JobTracker <-> TaskTracker) | XXL-JOB 逻辑更简单直接；LTS 负载均衡能力理论更强。 |
| **高可用机制** | **DB 锁** (Cluster)<br>无状态 Admin 集群 | **ZK 选主** (Master-Slave)<br>JobTracker 主备切换 | XXL-JOB 利用 DB 行锁防止重复调度；LTS 利用 ZK 节点争抢。 |
| **执行器注册** | **HTTP 周期性轮询** (Embed Server) | **ZK 临时节点** (Watch 机制) | XXL-JOB 采用心跳检测 (30s)，感知有延迟；LTS 基于 ZK Watch 实时性更高。 |
| **管理后台** | **功能强大** (任务管理、日志、统计) | **功能较弱** (主要看节点状态) | XXL-JOB 的 Admin 是核心生产力工具；LTS Admin 仅是辅助。 |
| **适合场景** | 通用的定时任务、Cron 作业 | 实时性要求极高、任务量巨大的动态任务 | 一般企业级应用首选 XXL-JOB。 |

## 4. 总结：新旧架构思维转换

*   **从 "Push" 到 "Config"**:
    *   **旧 (LTS)**: 我有代码，我要把任务 Push 进去跑。
    *   **新 (apismart)**: 我把执行逻辑写好 (`@XxlJob`)，在 Admin 配好时间，等它来调我。

*   **从 "ZK 协调" 到 "DB 中心"**:
    *   **旧**: 依赖 ZK 保持集群状态，运维复杂。
    *   **新**: 依赖 MySQL 保持状态，运维极其简单，但对 DB 压力稍大（适合中小规模）。

---

## 5. 相关工具

### 5.1 EPLog 日志查询

日志查看页面：https://neweplog.baidu-int.com/index.html?owner=itp&logId={trace_id}

也可以使用脚本查询日志，详见 [scripts/query_eplog.py](./scripts/query_eplog.py)

```bash
# 安装依赖
pip install websockets

# 查询日志
python scripts/query_eplog.py <trace_id>

# 示例
python scripts/query_eplog.py P872756_1769597615000 --timeout 30
```
