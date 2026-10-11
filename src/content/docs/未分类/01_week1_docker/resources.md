---
title: "Week 1 学习资源"
description: "学习策略：不要「通读」，而是「带着问题读」。每次读之前先问自己： 1. 这个东西怎么并发？ 2. 这个东西怎么复现/复用？ 3. 这个东西怎么自动判分？"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\01_week1_docker\\resources.md"
---
# Week 1 学习资源

> **学习策略**：不要「通读」，而是「带着问题读」。每次读之前先问自己：
> 1. 这个东西怎么并发？
> 2. 这个东西怎么复现/复用？
> 3. 这个东西怎么自动判分？

→ 参见 [mindset.md](../00_core_concepts/mindset.md) 了解三个灵魂问题
→ 参见 [06_references/official_sources.md](../06_references/official_sources.md) 查看本地整理的官方资料摘要

---

## 1. Docker 官方文档（必读章节）

### 核心概念
- **Docker Overview**: https://docs.docker.com/get-started/overview/
  - 重点理解：Docker 架构（Client-Server-daemon）、镜像 vs 容器、UnionFS
  - 面试关联：白板画 Docker 架构图

- **Understand images, containers, and storage**: https://docs.docker.com/storage/
  - 重点理解：镜像分层、存储驱动（OverlayFS vs Btrfs vs DeviceMapper）
  - 面试关联：解释为什么 16 个容器共享知识库只需要 11.6GB 磁盘

- **Resource limits**: https://docs.docker.com/engine/containers/resource_constraints/
  - 重点理解：CPU 限制（`--cpus` vs `--cpu-shares`）、内存限制、OOM 行为
  - 面试关联：16 个容器怎么配 cgroup

### 网络与安全
- **Docker networking**: https://docs.docker.com/network/
  - 重点理解：bridge 网络、host 网络、none 网络的区别
  - 面试关联：容器之间怎么通信

- **Docker security**: https://docs.docker.com/engine/security/
  - 重点理解：Namespaces、Cgroups、Capabilities、seccomp
  - 面试关联：容器内的 root 为什么不等于宿主的 root

### 实操
- **Dockerfile best practices**: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
  - 重点理解：层缓存优化、多阶段构建、`.dockerignore`
  - 面试关联：为什么 COPY requirements.txt 要在 COPY src/ 前面

- **Docker Compose overview**: https://docs.docker.com/compose/
  - 重点理解：YAML 语法、`--scale` 参数、服务依赖
  - 面试关联：`docker-compose up --scale worker=16` 底层做了什么

---

## 2. 《Docker 从入门到实践》（推荐章节）

> GitHub 地址：https://github.com/yeasy/docker_practice
> 在线阅读：https://yeasy.gitbook.io/docker_practice/

### 必读章节

| 章节 | 对应面试考点 | 优先级 |
|------|------------|--------|
| Docker 入门 → 基本概念 | 镜像、容器、仓库的关系 | P0 |
| 容器 → 资源限制 | cgroups 的 cpu/memory 限制 | P0 |
| 容器 → 仓库管理 | 镜像 tag、push/pull | P1 |
| 镜像 → Dockerfile | 层缓存、构建优化 | P0 |
| 镜像 → 多阶段构建 | 减小镜像大小 | P1 |
| 镜像 → 实现原理 | OverlayFS、layer、content-addressable | P0 |
| 容器 → 底层实现 | namespace、cgroup、rootfs | P0 |
| 网络 → 原理 | veth pair、bridge、iptables | P1 |
| 安全 → 安全防护 | capability、seccomp、User Namespace | P1 |

### 建议阅读顺序

```
第一轮（理解核心概念）：
  1. 基本概念（30 min）
  2. Dockerfile（30 min）
  3. 镜像实现原理（45 min）  ← 重点！
  4. 容器底层实现（45 min）  ← 重点！

第二轮（深入理解）：
  5. 资源限制（30 min）
  6. 多阶段构建（20 min）
  7. 网络原理（30 min）
  8. 安全防护（30 min）

第三轮（白板练习）：
  9. 关上书，白板画出容器 = Namespace + Cgroups + UnionFS 的关系图
  10. 白板画出 OverlayFS 的 lowerdir/upperdir/mergedir 结构
  11. 口述 `docker run --cpus=1 --memory=512m` 背后发生了什么
```

---

## 3. SWE-bench 源码阅读指南

> **SWE-bench**：一个用于评估 LLM 代码修复能力的 benchmark，包含真实的 GitHub issue、代码修复和测试用例。它的 evaluation harness 是 Agent 验证基础设施的绝佳参考实现。

### 基本信息

| 项目 | 信息 |
|------|------|
| GitHub | https://github.com/princeton-nlp/SWE-bench |
| Paper | https://arxiv.org/abs/2310.06770 |
| 语言 | Python |
| 核心文件数 | ~20 |

### 核心文件路径与阅读重点

| 路径 | 作用 | 阅读重点 |
|------|------|----------|
| `swebench/harness/constants.py` | 常量定义 | 环境变量、路径、超时、实例结构 |
| `swebench/harness/docker.py` | Docker 容器管理 | 容器创建/启动/销毁、并发控制、资源限制、状态重置 |
| `swebench/harness/run_evaluation.py` | 评测主流程 | patch 应用、测试执行、结果收集、判分链路 |
| `swebench/harness/utils.py` | 工具函数 | 日志解析、结果抽取、辅助逻辑 |
| `swebench/metrics/get_outputs.py` | 结果格式化 | 汇总输出、标准化结果结构 |
| `swebench/metrics/verify.py` | reward 判定逻辑 | `resolve_status`、通过率、是否引入新失败 |
| `docker/Dockerfile` | 环境构建参考 | 多阶段构建、依赖安装、环境配置 |
| `docs/evaluation.md` | 评测文档 | Harness 的整体流程说明 |

### 精读顺序（3-4 小时）

```
Step 1: 理解数据模型（30 min）
  → swebench/harness/constants.py
  → 理解 Instance（一个评测实例）的结构
  → 理解 TestSpec（测试规范）的定义

Step 2: 理解 Docker 管理（60 min）  ← 最重要
  → swebench/harness/docker.py
  → 重点理解：
    - make_instance_container()：怎么创建容器
    - run_instance_test()：怎么在容器中跑测试
    - 并发控制：怎么同时跑多个容器
    - 资源限制：CPU/内存怎么配
    - 容器生命周期：创建→执行→回收

Step 3: 理解评测流程（30 min）
  → swebench/harness/run_evaluation.py
  → 重点理解完整的 Harness 流程：
    1. 加载 instance 数据
    2. 创建 Docker 容器
    3. 应用 patch
    4. 运行测试
    5. 收集结果
    6. 计算 reward（resolve_status）

Step 4: 理解 reward 逻辑（30 min）
  → swebench/metrics/verify.py
  → 重点理解：
    - 怎么判断一个 patch 是否「真正修复了 bug」
    - 不只是测试通过率，还有「是否引入了新的失败」
    - 测试用例的 PASS_TO_FAIL 和 FAIL_TO_PASS 逻辑

Step 5: 白板练习（30 min）
  → 关上代码，画出 SWE-bench Harness 的架构图
  → 口述完整的评测流程
  → 思考：如果让你基于 SWE-bench 搭一个支持 16 并发的 RL 验证环境，你会怎么改？
```

### SWE-bench 的关键设计决策（面试中要提到的）

```
1. 每个实例（instance）用独立的 Docker 容器验证
   → 隔离性：不同 bug 的修复互不影响
   → 可复现性：相同的 Docker 镜像 + 相同的 patch = 相同的结果

2. 镜像预构建（不每次重新构建）
   → 构建好的镜像存储在 Docker Hub 或本地 registry
   → 启动时间从「构建 10 分钟」降到「拉取 30 秒」

3. 测试规范（TestSpec）预先定义
   → 每个 instance 的测试命令、patch 路径、环境变量都是预定义的
   → 不是运行全部测试，而是只运行相关的测试子集

4. reward 判定逻辑严格
   → 不仅仅是「patch 后测试通过」
   → 还要检查「没有引入新的失败」（PASS_TO_FAIL = 0）
   → 防止模型通过删测试来「作弊」
```

---

## 4. 推荐的 Docker 练习项目

### 初级（1-2 天）

**练习 1: Dockerfile 层缓存优化**
```
目标：理解层缓存命中规则
任务：
1. 写一个 Dockerfile（随便什么项目）
2. 故意把变化频繁的 COPY 放在前面，观察每次构建时间
3. 调整 Dockerfile 顺序（COPY requirements.txt 先，COPY src/ 后）
4. 对比构建时间差异
5. 用 docker history <image> 查看每层大小

验证点：
- 改代码后，pip install 层是否命中缓存？
- 构建时间减少多少？
```

**练习 2: 容器资源限制实验**
```
目标：理解 cgroups 的实际效果
任务：
1. 启动一个没有资源限制的容器，运行 stress --cpu 4
2. 观察宿主机的 CPU 使用率（应该飙到 100%）
3. 启动一个有资源限制的容器：docker run --cpus=1 stress --cpu 4
4. 观察宿主机 CPU 使用率（应该只有 ~12.5%，因为限制了 1 核）
5. 同理测试 --memory 限制，运行 stress --vm 1 --vm-bytes 2G

验证点：
- cpu.shares vs --cpus 的区别（软限制 vs 硬限制）
- 内存超限后 OOM Killer 的行为
```

### 中级（2-3 天）

**练习 3: 并发 Worker 实现**
```
目标：实现方案 2（Python Docker SDK）
任务：
1. 创建一个简单的 Docker 镜像（python 脚本，接收参数，返回结果）
2. 用 Python Docker SDK 创建 16 个容器并发执行
3. 用 Semaphore 控制并发度
4. 收集所有容器的输出，计算 reward
5. 输出汇总统计（通过率、平均 reward、吞吐量）

验证点：
- 16 并发 vs 1 串行的总时间差异
- Semaphore 是否正确控制了并发度（同时最多 16 个容器）
- 容器清理是否完整（docker ps 看不到残留容器）
```

**练习 4: Warm Pool 实现**
```
目标：理解 warm pool 的原理和效果
任务：
1. 预创建 16 个容器（运行 tail -f /dev/null）
2. 实现容器池的 acquire/release 逻辑
3. 测量「从池中取出容器 + 执行 + 归还」的延迟
4. 对比「每次创建新容器」的延迟
5. 实现状态重置（git checkout .）

验证点：
- warm pool 的延迟是否 < 0.5s？
- 对比 cold start 的延迟差多少倍？
- 重置后容器状态是否真正干净？
```

### 高级（3-5 天）

**练习 5: 基于 SWE-bench Harness 的 RL 验证环境**
```
目标：将 SWE-bench 的 Harness 改造成支持 RL 训练的验证环境
任务：
1. 精读 SWE-bench 源码
2. 修改 docker.py 支持并发执行（当前是串行）
3. 添加 warm pool 支持
4. 实现 reward function（binary + continuous）
5. 将结果存储为 RL 训练数据格式（state, action, reward 序列）
6. 实现 Best-of-N 验证（N=16，选 reward 最高的 patch）

验证点：
- 16 并发下的吞吐量是多少（tasks/minute）？
- reward 分布是否合理（有没有 reward hacking）？
- 数据格式是否符合 PPO/GRPO 训练的要求？
```

---

## 5. 补充阅读

### Linux Namespace 深入
- **Namespaces in operation**: https://lwn.net/Articles/531114/ (LWN 系列文章)
- **man pages**: `man 7 namespaces`, `man 2 unshare`, `man 2 clone`

### Linux Cgroups 深入
- **Cgroups v2 documentation**: https://www.kernel.org/doc/Documentation/admin-guide/cgroup-v2.rst
- **Docker cgroups 配置**: https://docs.docker.com/config/containers/resource_constraints/

### OverlayFS 深入
- **OverlayFS kernel documentation**: https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt
- **Understanding OverlayFS**: https://www.redhat.com/en/blog/understanding-overlayfs

### Kubernetes 基础（扩展阅读，非本周必须）
- **Kubernetes 官方文档**: https://kubernetes.io/docs/home/
- **Kubernetes 核心概念**: https://kubernetes.io/docs/concepts/
- 重点读：Pod、Deployment、Service、ConfigMap、Secret
