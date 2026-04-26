---
title: "MOSAIC让“拒绝”成为可学习动作，LiveAgentBench推动真实任务评测"
description: "今天的信号很集中：**Agent 安全对齐开始“把拒绝当作动作来学”**，**Agent 评测开始贴近真实工作与真实任务**，以及**推理加速继续沿着算法 × kernel × 硬件协同设计推进并开源落地**。"
date: "2026-03-10"
category: "每日日报"
---

# 20260310 MOSAIC让“拒绝”成为可学习动作，LiveAgentBench推动真实任务评测，FlashAttention-4开源提速

Owner: AI论文抓取器
Last edited time: 2026年3月10日 06:18

### 一句话总览

今天的信号很集中：**Agent 安全对齐开始“把拒绝当作动作来学”**，**Agent 评测开始贴近真实工作与真实任务**，以及**推理加速继续沿着算法 × kernel × 硬件协同设计推进并开源落地**。

### 🧠 CV / NLP 大模型基础论文

#### FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

- 提出算法与 kernel pipeline 的协同设计，面向“硬件不对称扩展”场景做加速优化
- 继续沿着 FlashAttention 系列路线，把注意力算子从“论文技巧”推进为可复用的工程组件
- 明确给出开源代码路径，并计划集成到主流库，降低落地门槛
- **为什么重要**：推理与训练的瓶颈越来越集中在 attention kernel 与内存带宽，FlashAttention 系列的迭代通常会快速进入生态并影响大量模型的端到端吞吐
- 原文：[https://arxiv.org/abs/2603.05451](https://arxiv.org/abs/2603.05451)

### 🤖 Agent 相关论文

#### Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use (MOSAIC)

- 指出 agent 的安全机制与 chat safety 不同：多步工具调用中“一次失误即可造成不可逆损害”
- 提出 MOSAIC：将推理过程结构化为 **plan → check → act/refuse**，把“拒绝”作为一等动作显式建模
- 使用基于偏好的强化学习（pairwise trajectory comparisons），在缺乏轨迹级标签的情况下学习安全决策
- **为什么重要**：把“是否执行下一步工具调用”纳入可学习的决策空间，可能成为 tool-using agent 的主流安全后训练范式
- 原文：[https://arxiv.org/html/2603.03205v1](https://arxiv.org/html/2603.03205v1)

#### LiveAgentBench: Comprehensive Benchmarking of Agentic Systems (PDF)

- 以真实用户案例构造评测数据，覆盖工作学习、日常生活、信息访问处理等多类真实任务
- 关注 agent 在长链路任务中的多模态处理、工具使用、错误恢复与稳健性
- **为什么重要**：从“单点能力”走向“真实任务闭环”的评测，是筛选/迭代 agent 系统的必要前提
- 原文：[https://arxiv.org/pdf/2603.02586](https://arxiv.org/pdf/2603.02586)

#### AgentVista: Evaluating Multimodal Agents in Ultra-Challenging Realistic Visual Scenarios

- 面向更贴近现实的视觉场景，强调跨图像检索、核验、计算等 interleaved tool use 的多步链路
- 提供公开网站与代码仓库，便于复现与对比
- **为什么重要**：多模态 agent 的短板往往出现在“看懂 + 查证 + 计算 + 反事实核验”的组合任务，强难度基准有助于拉开差距
- 原文：[https://arxiv.org/html/2602.23166v1](https://arxiv.org/html/2602.23166v1)

#### How Well Does Agent Development Reflect Real-World Work?

- 提出统一的任务复杂度度量，用于把不同 benchmark 上的 agent 活动放到同一坐标系
- 用“自主度前沿（performance frontier across task complexity）”刻画不同系统在真实工作复杂度上的能力边界
- **为什么重要**：有助于把分散的评测分数转译为“在哪类复杂任务上可以放权给 agent”
- 原文：[https://arxiv.org/html/2603.01203v2](https://arxiv.org/html/2603.01203v2)

### 🔥 GitHub 热门 Agent 项目

#### GitHub Topics: agentic-framework（热点项目聚合）

- deer-flow（Deep Research 框架，带 web search / crawling / python 执行等）
- claude-flow（面向 Claude 的 multi-agent orchestration，强调 swarms / RAG / Claude Code / MCP）
- **为什么重要**：从“单体 agent”转向“编排平台 + 协议（如 MCP）+ 工具链”的趋势持续强化
- 原文：[https://github.com/topics/agentic-framework](https://github.com/topics/agentic-framework)

### 💻 Claude Code / Coding Agent Skills

#### Everything Claude Code（harness / hooks / quality gate 体系）

- 将自身定位为“agent harness performance optimization system”，强调可测可控的执行框架
- 更新包含 hooks 可靠性、运行时 profile 控制、/quality-gate 等命令
- **为什么重要**：coding agent 的工程化正在从“提示词技巧”走向“执行 harness、质量门控、可观测性与回放”
- 原文：[https://github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)

#### Claude Code 仓库 issue：Agent Teams 相关问题与诉求（信号）

- 出现“team lead 配置不继承”“希望支持自定义 teammates”等讨论
- **为什么重要**：说明 Agent Teams 生态在快速迭代中，用户开始要求更强的可配置性与一致性
- 原文：[https://github.com/anthropics/claude-code/issues/32368](https://github.com/anthropics/claude-code/issues/32368)

### 趋势与信号

- **安全对齐从“输出内容安全”迁移到“行动安全”**：把拒绝与检查机制内生到多步执行策略（MOSAIC）
- **评测从“能力题”转向“工作流题”**：LiveAgentBench、复杂度度量等开始强调真实任务闭环
- **系统性能继续由 kernel/硬件协同牵引**：FlashAttention-4 的 co-design 与开源落地会快速扩散到生态

### 术语/概念速记

- **Act/Refuse as Actions**：把“执行/拒绝”作为策略动作，而非生成后再做静态过滤
- **Trajectory Preference RL**：用成对轨迹偏好比较学习策略，避免依赖轨迹级强标注
- **Autonomy Frontier**：在任务复杂度坐标系上刻画 agent 可自主承担的边界