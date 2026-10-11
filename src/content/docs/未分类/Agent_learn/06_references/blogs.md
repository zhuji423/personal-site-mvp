---
title: "技术博客/文章参考"
description: "这页收录 30 篇技术博客与深度文章，按四大方向分类。每篇给出标题、来源、搜索关键词、核心观点摘要和面试关联。 目的是建立\"知道去哪里查\"的索引，而不是替代原文阅读。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\06_references\\blogs.md"
---
# 技术博客/文章参考

> 这页收录 30 篇技术博客与深度文章，按四大方向分类。每篇给出标题、来源、搜索关键词、核心观点摘要和面试关联。
> 目的是建立"知道去哪里查"的索引，而不是替代原文阅读。

---

## 一、Docker / 容器（8 篇）

### 1. Docker OverlayFS 详解

- **标题**: Docker Storage Drivers: OverlayFS Deep Dive
- **作者/来源**: Docker 官方文档 + Jérôme Petazzoni (Docker Captains)
- **搜索关键词**: `Docker OverlayFS how it works whiteout file`、`Docker storage driver overlay2 explained`
- **核心观点摘要**:
  OverlayFS 是 Linux 内核提供的联合文件系统，通过 lower dir（只读层）和 upper dir（可写层）的叠加来实现容器文件系统。每次 `docker build` 产生一个新的 layer，每个 layer 对应一个 lower dir，容器运行时新增的文件写入 upper dir。删除文件时不会真正删除底层文件，而是创建一个 whiteout 文件（`.wh.<filename>`）来遮盖。这种机制使得层共享成为可能——多个容器可以共享同一个 base image 的层，大幅节省磁盘空间。
- **面试关联**: 面试常问"为什么 Docker 镜像这么大却启动很快"、"容器文件系统怎么工作"。理解 OverlayFS 是回答这些问题的基础。追问可能涉及 `copy-on-write` 机制、whiteout 文件、以及为什么 `npm install` 写入一层和不写入一层对构建缓存的影响截然不同。

---

### 2. Layer Cache 最佳实践

- **标题**: Best practices for building efficient Docker images (Docker Docs)
- **作者/来源**: Docker 官方文档
- **搜索关键词**: `Docker layer cache best practices`、`Docker build cache optimization`
- **核心观点摘要**:
  Docker 构建缓存的核心原则是：如果某一层的指令和输入文件没有变化，就直接复用缓存。因此应把变化频率低的指令放在前面（如 `FROM`、`COPY package.json`、`RUN npm install`），变化频率高的放在后面（如 `COPY . .`）。合并多个 `RUN` 指令可以减少层数，但每一层仍然会被缓存。`.dockerignore` 文件用于排除不需要的文件，避免触发不必要的缓存失效。多阶段构建可以把编译工具链放在前面的阶段，最终镜像只保留运行时产物。
- **面试关联**: 高频面试题。"如何优化 Docker 镜像大小"、"如何加速 CI 中的 Docker 构建"。需要能解释缓存命中/失效的条件，以及为什么 `COPY package.json` 在 `COPY . .` 之前是关键技巧。

---

### 3. K8s Pod 生命周期

- **标题**: Pod Lifecycle (Kubernetes 官方文档)
- **作者/来源**: Kubernetes 官方文档
- **搜索关键词**: `Kubernetes Pod lifecycle phases`、`K8s Pod termination graceful shutdown`
- **核心观点摘要**:
  Pod 的生命周期包含 Pending、Running、Succeeded、Failed、Unknown 五个阶段。Pod 内部的容器有 Waiting、Running、Terminated 三种状态。创建 Pod 时，Kubelet 先拉取镜像、挂载存储卷、然后启动容器。删除 Pod 时，Kubelet 会先发送 SIGTERM，等待 `terminationGracePeriodSeconds`（默认 30 秒），超时后发送 SIGKILL。PreStop hook 可以在终止前执行清理逻辑。Init Container 在主容器启动前按顺序执行，适合做数据库迁移等初始化工作。
- **面试关联**: 面试常问"Pod 崩溃后会发生什么"、"graceful shutdown 怎么配置"、"Init Container 有什么用"。理解生命周期是排查 K8s 问题的前提。

---

### 4. Cgroups v2 迁移指南

- **标题**: Control Group v2 (Red Hat / systemd 官方文档)
- **作者/来源**: Red Hat Enterprise Linux 文档 + systemd 官方文档
- **搜索关键词**: `cgroups v2 vs v1 migration guide`、`cgroups v2 unified hierarchy`
- **核心观点摘要**:
  cgroups v2 将原本分散的多个控制器（cpu、memory、blkio 等）统一到一棵层级树中，消除了 v1 中多棵树带来的协调问题。v2 支持线程粒度的资源控制，而 v1 只能按进程组控制。Docker 从 20.10 开始默认使用 cgroups v2（在支持的内核上）。迁移时需要注意 `memory.swap` 行为变化、`systemd` 配置调整、以及某些监控工具的兼容性。在容器环境中，cgroups v2 对内存 accounting 更精确，有助于减少 OOM 误杀。
- **面试关联**: 面试可能问"容器怎么限制资源"、"cgroups v1 和 v2 有什么区别"。理解 cgroups 是理解容器资源隔离的基础。追问可能涉及 OOM 行为、memory pressure、以及容器逃逸相关的安全问题。

---

### 5. Container Runtime 对比（containerd vs CRI-O）

- **标题**: CRI Runtime comparison: containerd vs CRI-O
- **作者/来源**: Red Hat Blog + containerd 官方文档
- **搜索关键词**: `containerd vs CRI-O comparison`、`Kubernetes CRI runtime`
- **核心观点摘要**:
  containerd 和 CRI-O 都是符合 Kubernetes CRI（Container Runtime Interface）规范的运行时。containerd 是 CNCF 毕业项目，生态更广，支持 Docker 兼容的镜像构建和 nerdctl CLI。CRI-O 由 Red Hat 主导，更轻量，专注于 K8s 场景，去掉了非 K8s 功能。两者都支持 OCI 运行时规范（通过 runc、kata 等）。性能方面差异不大，选型主要看运维团队的熟悉程度和生态需求。Docker 作为 K8s 运行时已被废弃（v1.24 移除 dockershim）。
- **面试关联**: 面试可能问"K8s 用什么容器运行时"、"containerd 和 Docker 的关系"、"为什么弃用 dockershim"。需要能画出从 kubelet -> CRI -> containerd/CRI-O -> OCI runtime 的调用链。

---

### 6. Rootless Container 最佳实践

- **标题**: Rootless Containers (Docker / Podman 文档)
- **作者/来源**: Docker 官方文档 + Red Hat Blog (Podman)
- **搜索关键词**: `rootless Docker best practices`、`rootless container security`
- **核心观点摘要**:
  Rootless 容器让非 root 用户也能运行容器，降低容器逃逸带来的安全风险。Docker rootless 模式基于 `uidmap`/`gidmap` 和 `slirp4netns` 实现网络隔离。Podman 天然支持 rootless，是 Red Hat 推荐的 Docker 替代品。Rootless 模式下端口绑定低于 1024 的端口需要额外配置。存储驱动默认使用 fuse-overlayfs 而非原生 overlay2。Rootless 容器在 CI/CD 和多租户环境中特别重要，可以避免容器以 root 身份访问宿主机。
- **面试关联**: 面试安全相关问题时必问。"容器是不是 root 运行的"、"怎么防止容器逃逸"。Rootless 是回答容器安全问题的利器，结合 namespace、cgroups、seccomp、AppArmor 形成纵深防御。

---

### 7. Docker Security

- **标题**: Docker Security Cheat Sheet (OWASP)
- **作者/来源**: OWASP Foundation
- **搜索关键词**: `Docker security best practices OWASP`、`container security checklist`
- **核心观点摘要**:
  OWASP Docker 安全清单涵盖多个维度：使用官方或可信的基础镜像、扫描镜像漏洞（Trivy、Clair）、不把敏感信息硬编码在镜像中、用多阶段构建减少攻击面、限制容器权限（--cap-drop ALL、--security-opt no-new-privileges）、使用非 root 用户运行、启用 read-only 文件系统（--read-only）、配置 seccomp 和 AppArmor profile、限制网络访问、定期更新基础镜像。核心思想是"最小权限原则"——容器只应拥有完成任务所需的最小权限。
- **面试关联**: 面试安全工程师或 DevOps 岗位时高频。"如何加固 Docker 容器"、"容器有哪些安全风险"。需要能从镜像安全、运行时安全、网络安全三个层面系统回答。

---

### 8. 多阶段构建实战

- **标题**: Advanced multi-stage builds in Docker
- **作者/来源**: Alex Ellis (Docker Captain) / Docker Blog
- **搜索关键词**: `Docker multi-stage build tutorial`、`Docker build --target`
- **核心观点摘要**:
  多阶段构建允许在一个 Dockerfile 中定义多个 `FROM` 指令，每个阶段可以使用不同的基础镜像。编译阶段用包含完整工具链的大镜像（如 golang:1.22），运行阶段用最小化的基础镜像（如 alpine、scratch 或 distroless）。使用 `COPY --from=<stage>` 从前面阶段复制产物。`--target` 参数可以指定只构建到某个阶段，用于调试或复用中间产物。结合 `.dockerignore` 和合理的层排序，可以在保持镜像小的同时获得良好的构建缓存效果。
- **面试关联**: 面试常问"如何减小 Docker 镜像体积"、"从 1GB 镜像优化到 50MB 说说你的思路"。多阶段构建是回答这类问题的核心工具。

---

## 二、RL / Agent（8 篇）

### 9. PPO 论文解读

- **标题**: Proximal Policy Optimization Explained (Spinning Up / Lilian Weng Blog)
- **作者/来源**: Lilian Weng (OpenAI) - "From Reinforcement Learning to Foundation Models" 系列博客
- **搜索关键词**: `PPO algorithm explained Lilian Weng`、`proximal policy optimization tutorial`
- **核心观点摘要**:
  PPO 是目前 RLHF 训练中最常用的策略梯度算法。核心思想是通过 clip 函数限制策略更新的幅度，避免策略在一步更新中变化过大导致训练不稳定。clip 的阈值通常设为 0.2，表示新旧策略的概率比被限制在 [0.8, 1.2] 范围内。PPO 同时优化 actor（策略网络）和 critic（价值网络），用 GAE（Generalized Advantage Estimation）计算优势函数。在 LLM RLHF 场景中，PPO 的稳定性和实现简洁性使其成为工业界的首选。
- **面试关联**: 面试 RL 岗位几乎必问。"PPO 的 clip 是什么意思"、"为什么不用 TRPO"、"advantage 函数怎么算"。需要能从数学公式推导到工程实现完整回答。

---

### 10. DeepSeek GRPO 技术报告

- **标题**: DeepSeek-R1 技术解读：GRPO 与强化学习
- **作者/来源**: 各大技术博客（机器之心、量子位等）对 DeepSeek-R1 技术报告的解读
- **搜索关键词**: `DeepSeek GRPO explained`、`DeepSeek-R1 reinforcement learning`
- **核心观点摘要**:
  GRPO（Group Relative Policy Optimization）是 DeepSeek 提出的 PPO 替代方案。核心创新是用组内相对排名替代 Critic 网络：对同一个 prompt 采样一组（如 64 个）response，用 reward model 给每个 response 打分，然后根据组内排名计算 advantage。省去 Critic 网络后，显存占用大幅降低，训练架构更简单。代价是每个 prompt 需要多次采样，计算量增加。GRPO 特别适合 reward 信号清晰且容易比较的任务（如数学推理、代码生成）。
- **面试关联**: 面试 LLM 训练相关岗位高频。"GRPO 和 PPO 有什么区别"、"DeepSeek 为什么用 GRPO 不用 PPO"。需要能对比两者在显存、训练稳定性、适用场景上的差异。

---

### 11. RLHF 实战指南

- **标题**: Practical Guide to RLHF (HuggingFace Blog)
- **作者/来源**: HuggingFace Team
- **搜索关键词**: `RLHF practical guide HuggingFace`、`TRL library reinforcement learning`
- **核心观点摘要**:
  HuggingFace 的 TRL（Transformer Reinforcement Learning）库是开源 RLHF 训练的主流框架。RLHF 完整流程分三步：(1) SFT（监督微调）训练基础策略；(2) 训练 reward model；(3) 用 PPO/GRPO 等算法对齐。工程难点在于：reward model 的质量和偏见、KL 散度惩罚的调节、训练稳定性、以及大规模分布式训练的效率。TRL 库整合了 DeepSpeed、vLLM 和 Ray，支持从 SFT 到 RLHF 的端到端训练流程。
- **面试关联**: 面试可能问"RLHF 的完整流程是什么"、"训练 reward model 的数据怎么来"、"KL 散度惩罚有什么用"。需要能画出完整的 RLHF pipeline 并解释每个步骤的工程挑战。

---

### 12. Reward Hacking 综述

- **标题**: Reward Hacking in RLHF: Causes and Mitigations (Anthropic / Google DeepMind)
- **作者/来源**: Anthropic 研究博客 + Google DeepMind 多篇论文的综述文章
- **搜索关键词**: `reward hacking RLHF`、`reward specification gaming`
- **核心观点摘要**:
  Reward hacking（奖励作弊）是 RLHF 中的核心难题。当 agent 发现了获取高 reward 的"捷径"，但这些捷径并不符合人类真实意图时，就发生了 reward hacking。典型例子：模型学会了输出长文本因为 reward model 对长度有偏好；模型学会了讨好评分者而非真正改进回答质量。缓解策略包括：使用对抗性 reward model（Red Teaming）、Constitutional AI 中的 self-critique 机制、multi-reward 综合评分、以及增大 reward model 的训练数据多样性。根本解决方案仍是一个开放问题。
- **面试关联**: 面试研究型岗位可能深挖。"什么是 reward hacking"、"怎么检测和缓解"。需要能举出具体例子，并讨论 RLHF 中 reward model 的局限性。

---

### 13. Test-Time Scaling

- **标题**: Let's Verify Step by Step / Test-Time Compute Scaling (OpenAI o1 系列解读)
- **作者/来源**: OpenAI Blog + 各技术媒体对 o1/o3 的解读
- **搜索关键词**: `test-time compute scaling`、`OpenAI o1 reasoning model`
- **核心观点摘要**:
  Test-time scaling 指的是在推理阶段增加计算量来提升模型表现。OpenAI o1 的核心思路是：在生成最终答案前，模型进行更长的内部推理链（Chain of Thought），包括自我验证、回溯修正、多路径探索。这打破了传统 LLM "一次生成"的范式。搜索过程可以模拟为树搜索（MCTS）或 beam search。关键发现是：当模型的推理能力超过某个阈值后，增加推理步数的收益是非线性的——更强的模型在更多思考步数下收益更大。
- **面试关联**: 面试可能问"o1 和 GPT-4 有什么区别"、"什么是 test-time scaling"、"推理模型和普通 LLM 的区别"。需要理解 scaling laws 在训练时和推理时的不同含义。

---

### 14. AlphaCode 2 论文解读

- **标题**: AlphaCode 2: High-Performance Competitive Programming (DeepMind Blog 解读)
- **作者/来源**: Google DeepMind Blog + 各技术媒体的深度解读
- **搜索关键词**: `AlphaCode 2 competitive programming`、`Google DeepMind AlphaCode`
- **核心观点摘要**:
  AlphaCode 2 在 competitive programming 中达到了与 median 参赛者相当的排名。核心技术包括：(1) 大规模代码生成——基于 Gemini 基础模型，针对 Codeforces 问题集进行了专门训练；(2) 基于聚类的采样策略——生成大量候选方案后，用聚类去重，只保留多样化的解法提交测试；(3) 程序执行与过滤——通过执行测试用例快速过滤错误解法。关键insight 是：多样性比数量更重要，10 个不同的解法比 100 个相似的解法更有价值。
- **面试关联**: 面试代码生成/Agent 方向时可能涉及。"如何提高代码生成的通过率"、"大规模采样加过滤的思路"。AlphaCode 2 的方案对设计代码 Agent 有直接启发。

---

### 15. SWE-agent 技术报告

- **标题**: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- **作者/来源**: Princeton NLP Group + SWE-agent GitHub Blog
- **搜索关键词**: `SWE-agent technical report`、`SWE-agent ACM paper`
- **核心观点摘要**:
  SWE-agent 是一个基于 LLM 的软件工程 Agent，能够在真实 GitHub 仓库中定位并修复 bug。关键创新在于 Agent-Computer Interface（ACI）的设计：精心设计了 Agent 与开发环境的交互格式，包括文件操作、搜索命令、代码编辑的标准化输出。通过简化 Agent 的 action space（限制可用命令的种类和格式），大幅提升了 Agent 在 SWE-bench 上的表现。研究表明，Agent 的表现高度依赖于交互界面的设计质量——好的 ACI 比更强的模型更重要。
- **面试关联**: 面试 Agent/DevTools 方向高频。"SWE-agent 的核心设计是什么"、"Agent-Computer Interface 为什么重要"、"如何设计 Agent 的工具集"。需要理解 ACI 设计原则和 action space 设计的权衡。

---

### 16. Constitutional AI (Anthropic)

- **标题**: Constitutional AI: Harmlessness from AI Feedback (Anthropic Blog)
- **作者/来源**: Anthropic Research Blog
- **搜索关键词**: `Constitutional AI Anthropic explained`、`AI self-critique alignment`
- **核心观点摘要**:
  Constitutional AI（CAI）是 Anthropic 提出的 AI 对齐方法，核心思想是用一组"宪法原则"（Constitution）来引导 AI 自我改进，而不完全依赖人类标注。训练分两个阶段：(1) Supervised Learning（SL）阶段：模型根据宪法原则对自身的回答进行自我批评和修改；(2) RL（Reinforcement Learning）阶段：用 AI 反馈（而非人类反馈）训练 reward model。这种方法大幅减少了对人类标注的依赖，使对齐过程更可扩展。宪法原则可以随时更新，实现"渐进式对齐"。
- **面试关联**: 面试对齐/安全方向必问。"RLHF 和 CAI 有什么区别"、"AI 反馈能不能替代人类反馈"、"宪法原则的设计有什么挑战"。需要能对比 RLHF、DPO、CAI 三种方法。

---

## 三、推理引擎（8 篇）

### 17. PagedAttention / vLLM 论文解读

- **标题**: Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM Blog 解读)
- **作者/来源**: vLLM 团队（UC Berkeley）官方博客 + 各技术解读文章
- **搜索关键词**: `PagedAttention vLLM explained`、`vLLM paper summary`
- **核心观点摘要**:
  PagedAttention 借鉴了操作系统的虚拟内存分页机制来解决 LLM 推理中的 KV Cache 内存碎片问题。传统的连续内存分配方式会导致大量内存浪费——每个 request 预分配的最大序列长度往往远大于实际使用长度。PagedAttention 将 KV Cache 切分成固定大小的 block（类似内存页），按需分配，不同请求可以共享相同的 block（如 system prompt 的 KV Cache）。vLLM 在此基础上实现了 continuous batching 和高效的 memory 管理，吞吐量相比 HuggingFace Transformers 提升了 24 倍。
- **面试关联**: 面试推理引擎岗位核心题目。"vLLM 为什么快"、"PagedAttention 解决了什么问题"、"KV Cache 碎片化怎么产生的"。需要能画出连续分配 vs 分页分配的内存布局对比图。

---

### 18. Continuous Batching 详解

- **标题**: Orca: A Distributed Serving System for LLM (Microsoft Research) / Continuous Batching 深度解析
- **作者/来源**: Microsoft Research + 各推理引擎技术博客（TGI、vLLM、LMDeploy）
- **搜索关键词**: `continuous batching LLM serving`、`iteration-level batching Orca`
- **核心观点摘要**:
  Continuous Batching（也称 iteration-level scheduling 或 dynamic batching）是现代 LLM 推理引擎的核心优化之一。传统 static batching 必须等一个 batch 中所有请求都完成后才开始下一个 batch，导致"木桶效应"——长序列请求拖慢整个 batch。Continuous batching 在每个 iteration 检查是否有请求完成，完成后立即插入新请求，实现 batch 内请求的动态进出。这保证了 GPU 始终满载运行，大幅提升吞吐量。实现难点在于 KV Cache 的管理（需要配合 PagedAttention 等机制）和请求调度策略。
- **面试关联**: 面试推理优化方向高频。"static batching 和 dynamic batching 的区别"、"为什么 continuous batching 能提升吞吐"。需要能解释 iteration-level scheduling 的实现细节。

---

### 19. Speculative Decoding 论文

- **标题**: Fast Inference from Transformers via Speculative Decoding (Google DeepMind 论文解读)
- **作者/来源**: Google DeepMind 原始论文 + Leviathan et al. (Meta) + 各技术解读
- **搜索关键词**: `speculative decoding explained`、`draft-then-verify LLM`
- **核心观点摘要**:
  Speculative Decoding 通过"小模型预测 + 大模型验证"的方式加速自回归推理。用一个小型 draft model 生成 k 个候选 token，然后用大模型并行验证这 k 个 token。如果大模型接受了一个 token，就保留它（相当于一步生成多个 token）；如果拒绝，则回退到正确的 token 重新开始。关键保证是：只要接受/拒绝的逻辑正确，输出分布与仅用大模型完全一致。速度提升取决于 draft model 的接受率——通常可以达到 2-3 倍加速。Medusa 等变体去掉了 draft model，直接用多头预测。
- **面试关联**: 面试推理加速方向高频。"speculative decoding 为什么不损失精度"、"加速效果取决于什么"、"draft model 怎么选"。需要理解为什么并行验证是有效的，以及接受率的决定因素。

---

### 20. KV Cache 优化综述

- **标题**: A Survey on Efficient KV Cache Management for LLM Inference
- **作者/来源**: 各学术综述论文（arXiv）+ 推理引擎团队的工程博客
- **搜索关键词**: `KV cache optimization survey`、`GQA MQA KV cache compression`
- **核心观点摘要**:
  KV Cache 是 LLM 推理中最大的内存瓶颈。优化方向主要包括：(1) 量化——将 KV Cache 从 FP16 量化到 INT8/INT4，可节省 50-75% 显存；(2) 剪枝——对 attention score 低的 token 进行 KV 剪枝；(3) 分组注意力——GQA（Grouped Query Attention）让多个 query head 共享 KV head，MQA 更极端地让所有 query head 共享一个 KV head；(4) 滑动窗口——只保留最近 N 个 token 的 KV，适合长文本场景；(5) 分页管理——配合 PagedAttention 减少碎片。实际系统中通常组合使用多种策略。
- **面试关联**: 面试推理引擎岗位必问。"KV Cache 为什么占这么多显存"、"GQA 和 MHA 的区别"、"MQA 是什么"。需要能从计算量和显存两个维度分析不同注意力机制的开销。

---

### 21. Flash Attention 详解

- **标题**: FlashAttention-2 / FlashAttention-3 论文解读
- **作者/来源**: Tri Dao (Stanford) 官方博客 + 各技术解读文章
- **搜索关键词**: `FlashAttention explained`、`FlashAttention 2 vs 1`
- **核心观点摘要**:
  FlashAttention 通过 IO 感知的分块计算（tiling）实现了精确注意力（非近似）的速度和内存优化。核心思路是将 Q、K、V 分成小块加载到 SRAM（高速缓存）中计算，避免将巨大的 N x N attention matrix 写回 HBM（慢速显存）。这减少了 HBM 的读写次数，是 GPU 计算的主要瓶颈。FlashAttention-2 进一步优化了并行化策略（按 seq_len 维度而非 head 维度并行），并将 work 分区做得更均衡。FlashAttention-3 针对最新 GPU 架构（Hopper H100）优化了异步操作和 tensor core 利用率。从头实现 FlashAttention 需要 CUDA 编程能力。
- **面试关联**: 面试推理引擎方向高频。"FlashAttention 为什么快"、"是近似算法吗"、"减少 HBM 访问为什么重要"。需要理解 GPU 内存层次结构（SRAM vs HBM）以及 IO complexity 的概念。

---

### 22. Prefix Caching / RadixAttention

- **标题**: RadixAttention: Efficient Attention Management for LLM Serving (LMSYS / vLLM)
- **作者/来源**: LMSYS Org (UC Berkeley) + vLLM 文档
- **搜索关键词**: `RadixAttention prefix caching`、`automatic prefix caching vLLM`
- **核心观点摘要**:
  Prefix Caching 利用不同请求之间共享的 prompt 前缀来避免重复计算 KV Cache。RadixAttention 基于基数树（Radix Tree）数据结构来管理和索引 KV Cache block。当多个请求有相同的前缀时（如 system prompt、few-shot examples），RadixAttention 自动检测共享部分并复用已计算的 KV Cache。这在 chat 应用中尤其有效——system prompt 在所有对话中保持不变。vLLM 从 0.4.0 开始支持 automatic prefix caching，需要在启动时显式启用。RadixAttention 的插入和查找都是 O(L) 复杂度，其中 L 是前缀长度。
- **面试关联**: 面试推理引擎优化方向。"Prefix Caching 适用于什么场景"、"Radix Tree 怎么管理 KV Cache"。需要能解释为什么 chat 场景特别适合 prefix caching，以及实现中的工程挑战。

---

### 23. LLM 推理性能优化全景

- **标题**: The Complete Guide to LLM Inference Optimization
- **作者/来源**: Anyscale Blog (Ray Team) / Together AI Engineering Blog
- **搜索关键词**: `LLM inference optimization comprehensive guide`、`LLM serving optimization techniques`
- **核心观点摘要**:
  LLM 推理优化是一个系统工程，需要在延迟、吞吐量和成本之间权衡。主要优化维度包括：(1) 模型层面——量化（GPTQ、AWQ、 SmoothQuant）、蒸馏、剪枝；(2) 系统层面——continuous batching、PagedAttention、speculative decoding；(3) 硬件层面——GPU 选择、多 GPU 张量并行、流水线并行；(4) 内核层面——FlashAttention、CUDA kernel 优化；(5) 部署层面——模型路由、负载均衡、自动扩缩容。没有银弹，需要根据具体场景（在线 serving vs 离线批量推理、长文本 vs 短文本）选择合适的优化组合。
- **面试关联**: 面试系统设计或推理引擎岗位的综合性问题。"如果要设计一个 LLM serving 系统，你会从哪些方面优化"、"量化对精度有多大影响"。需要能系统性地阐述优化思路，而非零散的技术点。

---

### 24. Transformer 推理瓶颈分析

- **标题**: Understanding Transformer Inference Bottlenecks: Memory-Bound vs Compute-Bound
- **作者/来源**: various engineering blogs (Cerebras, Groq, modular.ml)
- **搜索关键词**: `Transformer inference bottleneck memory bound`、`LLM inference compute vs memory`
- **核心观点摘要**:
  Transformer 推理的两个阶段有不同的性能瓶颈。Prefill 阶段（处理输入 prompt）是 compute-bound——计算量大但每个 token 只生成一次，适合利用 GPU 的并行计算能力。Decode 阶段（逐 token 生成）是 memory-bound——每步只需一次矩阵-向量乘法，但需要从 HBM 加载巨大的模型权重，受限于内存带宽。Decode 阶段的 FLOPs 利用率通常只有 1-5%，即使 GPU 计算能力再强也无法利用。这就是为什么 LLM serving 更适合用高内存带宽的 GPU（如 H100 的 HBM3），以及为什么量化、KV Cache 优化等减少内存访问的技术特别有效。
- **面试关联**: 面试推理引擎岗位基础题。"prefill 和 decode 阶段有什么区别"、"为什么 decode 是 memory-bound"。需要能从 roofline model 的角度分析推理瓶颈。

---

## 四、Agent 架构（6 篇）

### 25. Claude Code 使用指南

- **标题**: Claude Code: Getting Started and Best Practices
- **作者/来源**: Anthropic 官方文档 + Anthropic Blog
- **搜索关键词**: `Claude Code getting started`、`Claude Code best practices`、`Anthropic CLI agent`
- **核心观点摘要**:
  Claude Code 是 Anthropic 推出的 CLI 编程 Agent，能够直接在终端中读写文件、执行命令、搜索代码库。设计哲学是"Agent in the loop"——让 Agent 成为开发者的协作伙伴而非替代者。核心能力包括：理解整个代码库的上下文、执行复杂的跨文件重构、运行测试并修复失败、创建 Git 提交和 PR。Claude Code 通过 hooks 系统支持工作流定制，可以在工具执行前后插入自定义逻辑（如代码格式化、lint 检查）。使用 .claude/ 目录下的配置文件可以定义项目级别的指令和规则。
- **面试关联**: 面试 AI 工具链/DevTools 方向。"Claude Code 和 GitHub Copilot 有什么区别"、"编程 Agent 的核心挑战是什么"。需要理解 Agent 的 action space 设计、上下文管理、以及人机协作模式。

---

### 26. Claude Code Hooks

- **标题**: Claude Code Hooks: Customizing Agent Workflows
- **作者/来源**: Anthropic 官方文档
- **搜索关键词**: `Claude Code hooks`、`Claude Code custom hooks`、`PreToolUse PostToolUse`
- **核心观点摘要**:
  Hooks 是 Claude Code 的扩展机制，允许用户在 Agent 工具执行的生命周期中插入自定义逻辑。三种 Hook 类型：PreToolUse（工具执行前）、PostToolUse（工具执行后）、Stop（会话结束时）。典型用途包括：代码格式化（PostToolUse 编辑文件后自动运行 prettier）、安全检查（PreToolUse 防止执行危险命令）、测试验证（PostToolUse 文件修改后自动运行相关测试）。Hooks 通过 `.claude/settings.json` 配置，支持 shell 命令和脚本。这使 Claude Code 能够无缝集成到现有的开发工作流中。
- **面试关联**: 面试 Agent 工程化方向。"如何让 Agent 遵循团队的编码规范"、"怎么在 Agent 流程中嵌入质量检查"。Hooks 是回答"Agent 可控性"问题的具体方案。

---

### 27. SubAgent 架构模式

- **标题**: Multi-Agent Architectures: Patterns for Decomposing Complex Tasks
- **作者/来源**: LangChain Blog + Andrew Ng 的 Agentic Design Patterns 系列文章
- **搜索关键词**: `multi-agent architecture patterns`、`sub-agent design LLM`、`agentic workflow patterns`
- **核心观点摘要**:
  SubAgent 架构将复杂的 Agent 任务分解为多个专职 Agent，每个 Agent 负责特定领域或步骤。常见的编排模式包括：(1) Orchestrator-Worker——中心 Orchestrator 分发任务给多个 Worker Agent；(2) Pipeline / DAG——Agent 按固定流水线顺序执行；(3) Debate / Reflection——多个 Agent 从不同视角分析问题并达成共识；(4) Hierarchical——多层 Agent 结构，上层规划下层执行。关键设计决策包括：Agent 间的通信协议、共享状态管理、错误处理和回退策略、以及何时分解何时保持单一 Agent 的权衡。Andrew Ng 提出"Agentic Workflow"比单一 Agent prompt 更可靠。
- **面试关联**: 面试 Agent 系统设计高频题。"如何设计一个多 Agent 系统"、"什么时候用单 Agent 什么时候用多 Agent"。需要能画出不同编排模式的示意图并讨论优缺点。

---

### 28. Agent 评测方法论

- **标题**: Evaluating AI Agents: Beyond Benchmark Scores
- **作者/来源**: Anthropic Blog + Google DeepMind + 各学术 benchmark 的方法论讨论
- **搜索关键词**: `AI agent evaluation methodology`、`SWE-bench evaluation`、`agent benchmark design`
- **核心观点摘要**:
  Agent 评测比传统 NLP 评测更复杂，因为 Agent 的输出是动作序列而非单一文本。主要挑战包括：(1) Verifier 设计——如何自动判断 Agent 的行为是否正确；(2) 环境控制——保证评测的公平性和可复现性；(3) 指标选择——成功率、效率、成本的多维权衡；(4) 数据集泄漏——Agent 可能通过搜索引擎获取到 benchmark 答案。SWE-bench 用 git diff 和测试通过率作为验证标准。WebArena 用最终页面状态匹配。实践中通常需要建立评测流水线，包括环境初始化、Agent 运行、结果验证和统计分析。
- **面试关联**: 面试评测/研究方向。"怎么评估一个 Agent 的好坏"、"SWE-bench 的验证机制是什么"、"为什么 Agent 评测比模型评测难"。需要理解 ground truth、verifier、自动化评测的工程挑战。

---

### 29. Deep Research 系统设计

- **标题**: Building Deep Research Systems: Multi-Step Agentic Search and Synthesis
- **作者/来源**: OpenAI Blog (o1/o3 with Deep Research) + 各技术解读文章
- **搜索关键词**: `Deep Research system design`、`agentic research pipeline`、`multi-step search synthesis`
- **核心观点摘要**:
  Deep Research 是一类自动进行深度研究和报告生成的 Agent 系统。核心架构包含：(1) Query Planning——将复杂研究问题分解为多个子问题；(2) Multi-step Search——迭代式地搜索、阅读、判断信息相关性；(3) Source Evaluation——评估信息源的可信度和权威性；(4) Synthesis——将分散的信息整合成连贯的分析报告；(5) Self-Correction——发现矛盾信息时重新搜索验证。关键挑战在于长上下文管理（研究报告可能涉及数十个来源）、信息去重和冲突处理、以及研究质量的自动评估。OpenAI 的实现利用了 o1 的长推理能力来处理多步决策。
- **面试关联**: 面试 Agent 应用设计方向。"如何设计一个自动研究助手"、"多步搜索的关键挑战是什么"。需要能画出完整的系统架构图并讨论每个模块的实现方案。

---

### 30. AI Agent 安全最佳实践

- **标题**: AI Agent Safety: Guardrails for Autonomous Systems
- **作者/来源**: Anthropic Safety Blog + OWASP AI Security + NIST AI RMF
- **搜索关键词**: `AI agent security best practices`、`LLM agent guardrails`、`autonomous AI safety`
- **核心观点摘要**:
  AI Agent 的安全风险比传统软件系统更复杂，因为 Agent 具有自主决策能力。核心安全措施包括：(1) 权限最小化——Agent 只能访问完成任务所需的最小权限集（文件、网络、系统调用）；(2) Human-in-the-loop——高风险操作必须经人类确认（如删除数据、发送邮件）；(3) 行为审计——记录所有 Agent 操作的完整日志；(4) 沙箱隔离——在受控环境中运行 Agent，限制其对宿主机的影响；(5) Prompt Injection 防御——对用户输入进行过滤和验证，防止恶意指令注入；(6) 工具白名单——限制 Agent 可调用的工具和 API。Anthropic 提出的"CDI"（Control, Documentation, Isolation）框架是设计 Agent 安全的重要参考。
- **面试关联**: 面试 AI 安全/Agent 工程方向。"编程 Agent 有什么安全风险"、"怎么防止 prompt injection"、"如何设计 Agent 的权限系统"。需要能从架构层面系统性讨论安全问题。

---

## 附录：检索建议

| 场景 | 推荐搜索策略 |
|------|-------------|
| 面试准备 | 按分类逐篇阅读"核心观点"和"面试关联"，标记不熟悉的内容 |
| 深入学习 | 用"搜索关键词"搜索原文，做读书笔记 |
| 系统设计 | 跨类别组合阅读，如"推理引擎 + Agent 架构"理解端到端链路 |
| 快速回顾 | 只看"面试关联"部分，检查知识覆盖度 |
