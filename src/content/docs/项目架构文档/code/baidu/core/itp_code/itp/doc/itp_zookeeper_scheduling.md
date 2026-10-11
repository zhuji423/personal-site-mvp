---
title: "ITP 系统中 ZooKeeper 的应用与调度模式"
description: "在 ITP 系统中，ZooKeeper ZK 扮演着 注册中心 Registry 与 协调器 Coordinator 的核心角色，支撑着 LTS Lightweight Task Scheduler 任务调度系统的正常运转。"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_code\\itp\\doc\\itp_zookeeper_scheduling.md"
---
# ITP 系统中 ZooKeeper 的应用与调度模式

在 ITP 系统中，ZooKeeper (ZK) 扮演着 **注册中心 (Registry)** 与 **协调器 (Coordinator)** 的核心角色，支撑着 LTS (Lightweight Task Scheduler) 任务调度系统的正常运转。

## 1. ZooKeeper 的核心实现

LTS 框架通过 ZooKeeper 实现了分布式节点的发现与治理，具体实现在以下几个方面：

### 1.1 节点注册与发现 (Registry)
*   **实现位置**: `lts-core` 模块中的 `com.lts.core.registry` 包。
*   **工作机制**: 
    -   系统启动时，`JobTracker`、`TaskTracker` 和 `JobClient` (ITP-Web) 会将自己的节点信息（IP、端口、NodeGroup）以临时节点的形式注册到 ZK 的特定路径下。
    -   当有新节点加入或旧节点宕机时，ZK 的 Watcher 机制会通知调度中心同步节点列表。
*   **注册地址配置**: 在配置文件中通常以 `zookeeper://host:port` 的形式指定。

### 1.2 客户端实现 (ZK Client)
ITP 目前集成了两种 ZK 客户端实现，增强了连接的鲁棒性：
-   **ZkClient**: 位于 `com.lts.zookeeper.zkclient`。
-   **Curator**: 位于 `com.lts.zookeeper.curator`（推荐使用，提供了重试策略和更高层级的 API）。

### 1.3 Master 选举
*   **JobTracker HA**: 通过 ZK 的集群选主机制，保证 `JobTracker` 集群中只有一个主节点负责核心调度逻辑，实现高可用。

---

## 2. 核心生产/消费调度模块

ITP 的任务调度遵循经典的 **生产-消费** 模型，ZooKeeper 负责牵线搭桥。

### 2.1 生产者 (Producer): ITP-Web (JobClient)
*   **核心模块**: `itp-web`
*   **职责**:
    -   连接 ZK 获取活跃的 `JobTracker` 地址列表。
    -   用户触发测试计划后，封装 `Job` 对象并通过 `JobClient` 提交给 `JobTracker`。
    -   接收任务执行完成的反馈回调。

### 2.2 调度器/中转站 (Scheduler/Broker): LTS JobTracker
*   **核心模块**: `lts-jobtracker`
*   **职责**:
    -   作为 ZK 中的核心监听节点，管理所有 `TaskTracker` 的在线状态。
    -   接收 `JobClient` 的任务并持久化到任务队列。
    -   根据 ZK 中维护的负载情况，高效地将任务分配（分发或被拉取）给健康的 `TaskTracker`。

### 2.3 消费者 (Consumer): ITP-TaskTracker (TaskTracker)
*   **核心模块**: `itp-tasktracker`
*   **职责**:
    -   启动后在 ZK 注册为活跃执行节点。
    -   根据节点配置（如最大线程数）向 `JobTracker` 拉取（Pull）或接收推送的任务。
    -   执行具体的测试逻辑（HTTP/Dubbo/SQL 等），并在执行结束后通过连接上报状态。

---

## 3. 关键调度链路梳理

1.  **节点入群**: `JobTracker` 和 `TaskTracker` 启动 -> 在 ZK 注册临时节点。
2.  **生产者发布**: `ITP-Web` -> 查 ZK 获知 `JobTracker` 地址 -> 提交任务。
3.  **调度分发**: `JobTracker` -> 监控 ZK 获知 `TaskTracker` 负载 -> 任务队列匹配。
4.  **消费执行**: `TaskTracker` -> 从 `JobTracker` 拿任务 -> 业务执行 -> 反馈结果。

---

## 4. 组织架构与拓扑逻辑 (Ecosystem View)

从集合与层级的视角来看，ITP 的调度体系遵循以下逻辑：

### 4.1 LTS 框架作为“生命共同体”
LTS 提供了一个封闭且稳定的拓扑模型。所有的业务组件（Web, TT）必须封装成 LTS 定义的组件身份，才能在这个生态中通过 Netty 进行二进制通信。

### 4.2 ZooKeeper 作为“分布式大脑”
ZK 并不参与任务执行，但它分管了所有的“连接关系”：
*   **分管权限**：定义了哪些 NodeGroup 属于哪些 JobTracker 调度。
*   **分管流量**：通过维护健康的节点集合（Live Nodes Service），为 JobTracker 提供负载均衡的依据。
*   **分管状态**：确保分布式环境下的任务不重、不漏（通过全局锁和序列节点）。

### 4.3 生产与消费的“插件化”实现
*   **生产 (ITP-Web)**：是业务需求的转换器，把 ITP 的测试计划转化为 LTS 的任务。
*   **消费 (ITP-TaskTracker)**：是执行能力的驱动器，它挂载在 LTS 的 Worker 接口上，实现了 ITP 独有的自动化执行插件。
