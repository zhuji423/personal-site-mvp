---
title: "VLA可解释性与原生多模态预训练突破，Agent安全综述密集涌现，Qwen-Age"
description: "**一句话总览**：VLA 模型可解释性研究开辟新方向，原生多模态预训练实证为视觉基础模型提供设计指南；Agent 安全从对齐框架到 Agentic Web 全链路综述密集发布；Qwen-Agent 生态爆发登顶 GitHub Trending，Claude Code 社区工具链持续膨胀。"
date: "2026-03-08"
category: "每日日报"
---

# 20260308 VLA可解释性与原生多模态预训练突破，Agent安全综述密集涌现，Qwen-Agent登顶GitHub Trending

Owner: AI论文抓取器
Last edited time: 2026年3月8日 07:33

<aside>
📅

**一句话总览**：VLA 模型可解释性研究开辟新方向，原生多模态预训练实证为视觉基础模型提供设计指南；Agent 安全从对齐框架到 Agentic Web 全链路综述密集发布；Qwen-Agent 生态爆发登顶 GitHub Trending，Claude Code 社区工具链持续膨胀。

</aside>

---

## 🧠 CV / NLP 大模型基础论文

### 1. Observing and Controlling Features in Vision-Language-Action Models

- **要点**：
    - 首次系统性地将 LLM 机械可解释性方法迁移到 VLA 模型
    - 提出 **feature-observability**（特征可观测性）与 **feature-controllability**（特征可控性）两大核心概念
    - 通过线性分类器在表征空间中观测线性编码的特征，并展示如何控制这些特征影响输出行为
    - 揭示了 VLA 因多模态输入/输出及 Transformer+Diffusion 混合架构而具有更高复杂性
- **影响**：为具身智能模型的安全部署和行为调控提供了可解释性工具，有望成为 VLA 安全审计的基础方法
- **链接**：[arxiv.org/html/2603.05487v1](http://arxiv.org/html/2603.05487v1)

### 2. Beyond Language Modeling: An Exploration of Multimodal Pretraining

- **要点**：
    - 通过**从头预训练**的受控实验，隔离影响多模态预训练的关键因素
    - 采用 **Transfusion** 框架：语言用 next-token prediction，视觉用 diffusion
    - 训练数据涵盖文本、视频、图文对，甚至 action-conditioned video
    - 为原生多模态模型的设计空间提供了实证清晰度
- **影响**：填补了原生多模态预训练（非语言预训练后适配）的实证空白，为下一代视觉基础模型的架构选择提供直接参考
- **链接**：[arxiv.org/html/2603.03276v1](http://arxiv.org/html/2603.03276v1)

### 3. NoLan: Mitigating Object Hallucinations in LVLMs via Dynamic Suppression of Language Priors

- **要点**：
    - 系统性实验回答了「VLM 幻觉主要来自视觉编码器还是语言解码器？」
    - 结论：**语言解码器的强先验**是对象幻觉的主要来源
    - 提出 NoLan 方法，通过动态抑制语言先验来缓解幻觉
    - 实验设计清晰，结论有指导意义
- **影响**：为 VLM 幻觉缓解指明了方向——重点应放在语言解码端而非视觉编码端
- **链接**：[arxiv.org/html/2602.22144v1](http://arxiv.org/html/2602.22144v1)

### 4. Discovering Implicit Large Language Model Alignment Objectives

- **要点**：
    - 提出框架自动发现 LLM 对齐过程中的**隐式目标**
    - 在多任务、多模型规模、多对齐算法上验证鲁棒性
    - 能捕获 >90% 的奖励模型行为
    - 案例研究成功识别出伴随期望行为出现的**潜在错误对齐激励**
- **影响**：为更透明和安全的 AI 对齐提供关键工具，可用于提前发现对齐中的隐患
- **链接**：[arxiv.org/html/2602.15338v1](http://arxiv.org/html/2602.15338v1)

---

## 🤖 Agent 相关论文

### 1. MOSAIC: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use

- **要点**：
    - 来自 **Microsoft Research**，解决 Agent 多步工具调用的安全问题
    - 提出 **plan → check → act or refuse** 推理循环，将安全决策显式化
    - 使用基于偏好的强化学习（pairwise trajectory comparisons）训练，无需轨迹级标签
    - 将 refusal（拒绝执行）作为一等公民动作
- **影响**：首个系统性解决 Agent 多步工具安全的后训练框架，对 Agent 产品化部署有重要参考价值
- **链接**：[arxiv.org/html/2603.03205v1](http://arxiv.org/html/2603.03205v1)

### 2. From Secure Agentic AI to Secure Agentic Web: Challenges, Threats, and Future Directions

- **要点**：
    - 综述式论文，提供从 Secure Agentic AI 到 Secure Agentic Web 的**过渡视角**
    - 组件对齐的威胁分类：prompt abuse、environment injection、memory attacks、toolchain abuse、model tampering、agent network attacks
    - 防御策略覆盖 prompt hardening、safety-aware decoding、权限控制、运行时监控、持续红队测试、协议级安全
- **影响**：为 Agent 安全研究提供了最全面的威胁分类和防御框架参考
- **链接**：[arxiv.org/html/2603.01564v1](http://arxiv.org/html/2603.01564v1)

### 3. David vs. Goliath: Verifiable Agent-to-Agent Jailbreaking via Reinforcement Learning

- **要点**：
    - 研究 Agent 间的自动化红队对抗（Agent-to-Agent Jailbreaking）
    - 使用强化学习自动发现安全对齐系统中的漏洞
    - 强调可验证性——攻击结果可被系统性验证
    - 讨论了双重用途风险与负责任披露
- **影响**：揭示多 Agent 系统中 Agent 间对抗的现实威胁，推动防御机制的迭代
- **链接**：[arxiv.org/pdf/2602.02395](http://arxiv.org/pdf/2602.02395)

### 4. ViPlan: A Benchmark for Visual Planning with Symbolic Predicates and VLMs

- **要点**：
    - 首个支持符号规划与 VLM 直接规划对比的开源视觉规划 Benchmark
    - VLM-as-grounder（符号+VLM）在 Blocksworld 中解题率 46%，远超 VLM-as-planner 的 9%
    - 涵盖 Blocksworld 与家庭机器人仿真环境
- **影响**：为 Agent 视觉规划能力评测提供标准化工具，验证了符号规划+VLM 组合路线的优势
- **链接**：[arxiv.org/html/2505.13180v2](http://arxiv.org/html/2505.13180v2)

---

## 🔥 GitHub 热门 Agent 项目

### 1. Qwen-Agent（QwenLM/Qwen-Agent）⭐ 14,666 — 🔺696 stars/天

- **简介**：基于 Qwen>=3.0 的 Agent 框架，支持 Function Calling、MCP、Code Interpreter、RAG、Chrome 扩展等
- **亮点**：生态完整度极高，MCP 原生支持，今日 GitHub Trending 第二
- **链接**：[github.com/QwenLM/Qwen-Agent](http://github.com/QwenLM/Qwen-Agent)

### 2. VoltAgent（VoltAgent/voltagent）⭐ 6,400

- **简介**：开源 TypeScript AI Agent 工程平台，包含框架 + VoltOps 运维控制台
- **亮点**：Memory、RAG、Guardrails、Tools、MCP、Voice、Workflow 全栈支持，支持多 Agent 协作与 Supervisor 编排
- **链接**：[github.com/VoltAgent/voltagent](http://github.com/VoltAgent/voltagent)

### 3. Google Gemini CLI（google-gemini/gemini-cli）⭐ 96,700

- **简介**：开源 AI Agent，将 Gemini 能力直接带入终端
- **亮点**：支持 MCP Server/Client，CLI 原生交互，持续活跃更新
- **链接**：[github.com/google-gemini/gemini-cli](http://github.com/google-gemini/gemini-cli)

### 4. Microsoft Agent Framework ⭐ NEW

- **简介**：微软官方发布的 Agent 构建、编排与部署框架，支持 Python 和 .NET
- **亮点**：多 Agent 工作流编排，Azure 生态集成，双语言支持
- **链接**：[github.com/microsoft/agent-framework](http://github.com/microsoft/agent-framework)

### 5. AgentScope（agentscope-ai/agentscope）

- **简介**：面向生产环境的 Agent 框架，核心理念是「Build and run agents you can see, understand and trust」
- **亮点**：设计理念顺应模型能力增长，利用模型推理与工具使用能力而非约束性 prompt
- **链接**：[github.com/agentscope-ai/agentscope](http://github.com/agentscope-ai/agentscope)

---

## 💻 Claude Code / Coding Agent Skills

### 1. Everything Claude Code v1.8.0 — Harness Performance System 发布

- **要点**：
    - ECC 正式定位为 **Agent Harness Performance System**（Agent 运行时性能系统）
    - 新增 Hook 可靠性大修：SessionStart root fallback、Stop-phase session summaries
    - 新增 Hook 运行时控制：`ECC_HOOK_PROFILE=minimal|standard|strict`
    - 新增 harness 命令：`/harness-audit`、`/loop-start`、`/loop-status`、`/quality-gate`、`/model-route`
    - **NanoClaw v2**：model routing、skill hot-load、session branch/search/export/compact/metrics
    - **跨 Harness 一致性**：Claude Code、Cursor、OpenCode、Codex 行为对齐
    - 997 项内部测试全部通过
- **影响**：将 Claude Code 从配置工具升级为完整的 Agent 运行时管理平台，跨工具一致性对多工具用户尤其重要
- **链接**：[github.com/affaan-m/everything-claude-code](http://github.com/affaan-m/everything-claude-code)

### 2. Claude Code Ultimate Guide v3.30.2

- **要点**：
    - 涵盖从入门到高级用户的全面文档，包含 Agent 工作流模板
    - 包含 274 道交互式测验题
    - 新增 Agent Teams 工作流指南（多 Agent 协作编排）
    - 每日更新，最近更新于 2026-03-05
- **影响**：目前最完整的 Claude Code 社区文档，Agent Teams 指南填补了多 Agent 编程协作的实践空白
- **链接**：[github.com/FlorianBruniaux/claude-code-ultimate-guide](http://github.com/FlorianBruniaux/claude-code-ultimate-guide)

### 3. Claude Code Plan System 重构提案（Issue #30438）

- **要点**：
    - 提议将 Plan Mode 重构为一等公民 Plan System
    - 包含 6 个新 Plan Tools + Draft Mode（原 Plan Mode 更名）+ Plan TUI
    - Draft Mode 定位为「纯推理沙盒」——Claude 不会自动执行
    - Plan 作为持久化、命名的编排对象，协调现有 Agent、TeamCreate、EnterWorktree、Task 工具
- **影响**：若落地，将显著提升 Claude Code 的复杂任务规划能力和可预测性
- **链接**：[github.com/anthropics/claude-code/issues/30438](http://github.com/anthropics/claude-code/issues/30438)

### 4. Awesome Claude Skills ⭐ 41,400（ComposioHQ）

- **要点**：精选 Claude Skills 资源与工具合集，涵盖自定义 Claude AI 工作流的最佳实践
- **影响**：Claude 技能生态持续膨胀，已成为 AI 编程助手领域的核心社区资源之一
- **链接**：[github.com/ComposioHQ/awesome-claude-skills](http://github.com/ComposioHQ/awesome-claude-skills)

---

## 📈 趋势与信号

- **Agent 安全从单点到全链路**：MOSAIC（多步工具安全）→ Secure Agentic Web（全栈安全综述）→ Agent-to-Agent Jailbreaking（对抗性测试），安全研究已覆盖 Agent 生命周期全链路
- **VLA/VLM 可解释性升温**：从幻觉检测（NoLan）到特征控制（VLA feature-controllability），可解释性正从 LLM 扩展到多模态/具身模型
- **Agent 框架军备竞赛白热化**：Qwen-Agent、VoltAgent、Microsoft Agent Framework、AgentScope 同时活跃，框架层竞争进入「生态完整度」比拼阶段
- **Coding Agent 从工具到平台**：Everything Claude Code 定位 Harness Performance System、Plan System 提案、跨工具一致性，标志着 Coding Agent 正在从「辅助工具」演进为「开发运行时平台」

---

## 📖 术语/概念速记

| 术语 | 解释 |
| --- | --- |
| **VLA（Vision-Language-Action Model）** | 结合视觉、语言和动作输出的多模态模型，用于具身智能/机器人 |
| **Feature-observability / Feature-controllability** | VLA 可解释性中的两个核心概念：能否观测模型内部特征、能否控制特征影响输出 |
| **Transfusion** | 混合预训练框架，语言部分用 next-token prediction，视觉部分用 diffusion |
| **MOSAIC** | Microsoft 提出的 Agent 安全后训练框架，通过 plan-check-act/refuse 循环实现安全决策 |
| **Agent Harness** | Agent 运行时管理层，负责 hook、session、模型路由等基础设施 |
| **Draft Mode** | Claude Code 中原 Plan Mode 的重命名，强调「纯推理沙盒，不自动执行」 |