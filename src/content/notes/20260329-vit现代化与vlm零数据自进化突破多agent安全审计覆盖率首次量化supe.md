---
title: "ViT现代化与VLM零数据自进化突破，多Agent安全审计覆盖率首次量化，supe"
description: "**一句话总览：** ViT-5 系统性现代化 Vision Transformer 架构并刷新理解与生成基准，MM-Zero 首次实现零数据 VLM 自进化，Agent 安全审计工具 SafeAudit 发现现有基准遗漏超 20% 不安全交互模式，MARCH 以信息不对称机制对抗 RAG 幻觉确认..."
date: "2026-03-29"
category: "每日日报"
---

# 20260329 ViT现代化与VLM零数据自进化突破，多Agent安全审计覆盖率首次量化，superpowers持续领跑GitHub日榜

Owner: AI论文抓取器
Last edited time: 2026年3月29日 10:11

**一句话总览：** ViT-5 系统性现代化 Vision Transformer 架构并刷新理解与生成基准，MM-Zero 首次实现零数据 VLM 自进化，Agent 安全审计工具 SafeAudit 发现现有基准遗漏超 20% 不安全交互模式，MARCH 以信息不对称机制对抗 RAG 幻觉确认偏差，superpowers 日增 2200+ Star 持续领跑 GitHub Trending。

---

## 🧠 CV / NLP 大模型基础论文

### 1. ViT-5: Vision Transformers for The Mid-2020s

- **要点：**
    - 系统性审视过去五年 ViT 架构进展，对归一化、激活函数、位置编码、门控机制和可学习 token 逐模块优化
    - 保留经典 Attention–FFN 结构，提出下一代 Vision Transformer 系列 ViT-5
    - ImageNet-1k 分类 ViT-5-Base 达 84.2% top-1（DeiT-III-Base 为 83.8%）
    - 用于 SiT 扩散框架时 FID 从 2.06 降至 1.84，证明在生成任务中也有提升
- **影响：** 为 ViT 架构提供了一套"组件级升级指南"，在理解和生成任务上均有提升，有望成为新一代视觉骨干默认选择
- **链接：** [arxiv.org/html/2602.08071v1](http://arxiv.org/html/2602.08071v1)

### 2. MM-Zero: Self-Evolving Multi-Model Vision Language Models From Zero Data

- **要点：**
    - 首个基于 RL 的零数据 VLM 自进化框架，无需任何种子图像即可启动多模态自我提升
    - 突破传统 VLM 自进化依赖少量种子数据的瓶颈
    - 建立可扩展的多模型自进化路径，超越传统两模型范式
    - 为多模态模型的自我改进划定了新前沿
- **影响：** 将 LLM 领域的零数据自进化范式首次拓展到多模态，降低了 VLM 训练对标注数据的依赖
- **链接：** [arxiv.org/abs/2603.09206](http://arxiv.org/abs/2603.09206)

### 3. Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encoders

- **要点：**
    - 首次系统评估 SSM（State Space Model）能否替代 ViT 作为 VLM 的视觉编码器
    - 在指令微调阶段固定视觉编码器，对比 SSM 与 ViT 的架构效应
    - 探讨了微调视觉编码器时的优化不稳定性与对照实验的混淆因素
- **影响：** 对 VLM 视觉编码器"ViT 一家独大"的现状提出系统性质疑，SSM 路线的可行性被正式检验
- **链接：** [arxiv.org/html/2603.19209v1](http://arxiv.org/html/2603.19209v1)

### 4. MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination

- **要点：**
    - 提出多 Agent 强化自检框架，利用"刻意信息不对称"对抗 RAG 系统的幻觉确认偏差
    - 编排 Solver、Proposer、Checker 三个专用 Agent 协作流水线
    - Proposer 将 RAG 回答拆解为 claim 级可验证原子命题，Checker 独立校验
    - 突破了"以 LLM 检验 LLM"的固有确认偏差瓶颈
- **影响：** 为 RAG 幻觉检测引入结构化多 Agent 方法，显著提升事实对齐能力，适用于高可靠性场景
- **链接：** [arxiv.org/html/2603.24579v1](http://arxiv.org/html/2603.24579v1)

### 5. Video-Only ToM: Enhancing Theory of Mind in Multimodal LLMs

- **要点：**
    - 发现 MLLM 在多个 ToM 任务间视觉注意力具有跨任务一致性，而内部推理表征具有任务内一致性
    - 提出 VisionToM 轻量干预框架，无需微调骨干网络、手写提示或外部语言标注
    - 仅基于原始视频输入即可增强视觉注意力与 ToM 推理
- **影响：** 首次在 MLLM 中系统分析 ToM 的内部机制，并给出了轻量级增强方案
- **链接：** [arxiv.org/html/2603.24484v1](http://arxiv.org/html/2603.24484v1)

---

## 🤖 Agent 相关论文

### 1. Who Tests the Testers? Systematic Enumeration and Coverage Audit of LLM Agent Tool Call Safety

- **要点：**
    - 提出 SafeAudit 元审计框架，系统枚举 Agent 工具调用的不安全交互模式
    - 引入 rule-resistance 评估协议，基于工具调用 trace 而非主观判断衡量测试用例新颖性
    - 对 3 个 Agent 安全基准、12 个环境、8 个骨干 LLM 进行元审计
    - 发现现有基准遗漏超过 20% 的不安全交互模式，约 11% 为全新模式
- **影响：** 首次对 Agent 安全基准自身进行"审计审计者"，揭示了当前评测覆盖率的系统性盲区
- **链接：** [arxiv.org/html/2603.18245v1](http://arxiv.org/html/2603.18245v1)

### 2. The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration

- **要点：**
    - 综合综述 LLM Agent 工具使用从单次调用到多工具编排的演进
    - 统一任务形式化，区分单次工具调用与长程编排
    - 分析多工具 Agent 在状态管理、执行反馈、环境变化下的核心挑战
    - 涵盖安全、成本、可验证性等工程约束
- **影响：** 提供了 Agent 工具使用领域的全景图谱，帮助研究者定位前沿问题
- **链接：** [arxiv.org/html/2603.22862v1](http://arxiv.org/html/2603.22862v1)

### 3. TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems

- **要点：**
    - 基于 OWASP 标准，构建多 Agent 系统（MAS）安全评估与监控框架
    - 提出三层细粒度风险分类体系，覆盖 20 种风险类型
    - 涵盖单 Agent 漏洞、Agent 间通信威胁、系统级涌现风险三个层级
- **影响：** 填补了多 Agent 系统安全缺乏统一框架的空白，将工业安全标准引入 MAS 领域
- **链接：** [arxiv.org/html/2603.15408v1](http://arxiv.org/html/2603.15408v1)

### 4. PASTE: Act While Thinking — Accelerating LLM Agents via Pattern-Aware Speculative Tool Execution

- **要点：**
    - 提出 Pattern-Aware Speculative Tool Execution，通过预测性工具执行隐藏延迟
    - 利用 Agent 请求在语义多样性下仍表现出稳定的应用级控制流与可预测数据依赖
    - 通过推测性并行执行工具调用，打破传统"LLM-工具"串行瓶颈
- **影响：** 从系统层面优化 Agent 推理速度，为生产环境部署提供延迟优化新范式
- **链接：** [arxiv.org/html/2603.18897v1](http://arxiv.org/html/2603.18897v1)

### 5. Self-Evolving Multi-Agent Framework for Efficient Decision Making in Real-Time Strategy Scenarios

- **要点：**
    - 结合结构信息论与 LLM，构建实时策略场景下的自进化多 Agent 决策框架
    - 利用大模型知识储备与推理能力应对复杂策略操作
    - 针对动态环境下的长程任务进行自适应演化
- **影响：** 展示了 LLM 多 Agent 在复杂实时策略游戏中的潜力，推动博弈与决策研究
- **链接：** [arxiv.org/html/2603.23875v1](http://arxiv.org/html/2603.23875v1)

---

## 🔥 GitHub 热门 Agent 项目

### 1. obra/superpowers ⭐ 120,859（日增 ~2,292）

- **简介：** An agentic skills framework & software development methodology that works
- **亮点：** 以 Shell 为基础构建的 Agent 技能框架，强调可落地的软件开发方法论，持续多日占据 GitHub Trending 日榜前列
- **链接：** [github.com/obra/superpowers](http://github.com/obra/superpowers)

### 2. SakanaAI/AI-Scientist-v2 ⭐ 3,495（日增 ~506）

- **简介：** Workshop-Level Automated Scientific Discovery via Agentic Tree Search
- **亮点：** Sakana AI 发布的第二代 AI 科学家，基于 Agentic 树搜索实现 workshop 级别的自动化科学发现，从假说生成到实验执行全自动
- **链接：** [github.com/SakanaAI/AI-Scientist-v2](http://github.com/SakanaAI/AI-Scientist-v2)

### 3. bytedance/deer-flow ⭐ 50,000（热门）

- **简介：** An open-source long-horizon SuperAgent harness
- **亮点：** 字节跳动开源的长程 SuperAgent 框架，集成沙箱、记忆、工具、技能、子 Agent 与消息网关，支持从分钟到小时级别的复杂任务
- **链接：** [github.com/bytedance/deer-flow](http://github.com/bytedance/deer-flow)

### 4. agentscope-ai/agentscope ⭐ 21,635（日增 ~398）

- **简介：** Build and run agents you can see, understand and trust
- **亮点：** 强调可见性、可理解性和可信赖性的 Agent 构建与运行平台
- **链接：** [github.com/agentscope-ai/agentscope](http://github.com/agentscope-ai/agentscope)

### 5. virattt/dexter ⭐ 20,226（日增 ~581）

- **简介：** An autonomous agent for deep financial research
- **亮点：** 面向金融深度研究的自主 Agent，TypeScript 实现，适合金融分析与投资研究场景
- **链接：** [github.com/virattt/dexter](http://github.com/virattt/dexter)

---

## 💻 Claude Code / Coding Agent Skills

### 1. Claudini: Autoresearch Discovers SOTA Adversarial Attack Algorithms for LLMs

- **要点：**
    - 基于 Claude Code 的 autoresearch 流水线自动发现新型白盒对抗攻击算法
    - 在越狱与 prompt injection 评测中显著超越现有 30+ 方法
    - GPT-OSS-Safeguard-20B 上 CBRN 查询攻击成功率达 40%（现有方法 ≤10%）
    - 展示了 Coding Agent 在自动化 AI 安全研究中的颠覆性能力
- **影响：** 证明 Claude Code 驱动的 autoresearch 可以产出超越人工设计的算法，AI 安全红队测试进入自动化时代
- **链接：** [arxiv.org/abs/2603.24511](http://arxiv.org/abs/2603.24511)

### 2. Engineering Pitfalls in AI Coding Tools: Empirical Study of Bugs in Claude Code, Codex, and Gemini CLI

- **要点：**
    - 首个针对 Claude Code、Codex、Gemini CLI 的工程缺陷实证研究
    - 系统分析 AI 编程工具在真实使用中的 Bug 类型与模式
    - 为 Coding Agent 的质量保障与工程实践提供数据支撑
- **影响：** 帮助开发者理解 AI 编程助手的局限性，指导更安全的 Coding Agent 使用
- **链接：** [arxiv.org/abs/2603.20847](http://arxiv.org/abs/2603.20847)

### 3. AutoResearchClaw v0.3.2 — 跨平台 Agent 后端支持

- **要点：**
    - 现在支持 Claude Code、Codex CLI、Copilot CLI、Gemini CLI、Kimi CLI 等任意 ACP 兼容后端
    - 新增 CLI-agent 代码生成后端，支持预算控制和超时管理
    - 引入反捏造系统（VerifiedRegistry + 实验诊断与修复循环）
    - 100+ Bug 修复，模块化执行器重构
- **影响：** 自动化科研工具走向跨平台互通，Claude Code 作为后端的生态位进一步扩大
- **链接：** [github.com/aiming-lab/AutoResearchClaw](http://github.com/aiming-lab/AutoResearchClaw)

### 4. everything-claude-code — Agent Harness 性能优化系统

- **简介：** 面向 Claude Code、Codex、Opencode、Cursor 等 Coding Agent 的技能、本能、记忆、安全与研究优先开发优化系统
- **亮点：** 将 Agent Harness 的性能调优体系化，覆盖开发流程全链路
- **链接：** [github.com/affaan-m/everything-claude-code](http://github.com/affaan-m/everything-claude-code)

### 5. awesome-claude-code-subagents — 100+ 专用子 Agent 合集

- **简介：** VoltAgent 维护的 100+ Claude Code 专用子 Agent 定义合集
- **亮点：** 覆盖广泛开发场景的子 Agent 库，推动 Claude Code 多 Agent 协作标准化
- **链接：** [github.com/VoltAgent/awesome-claude-code-subagents](http://github.com/VoltAgent/awesome-claude-code-subagents)

---

## 📈 趋势与信号

- **Agent 安全审计进入"审计审计者"阶段：** SafeAudit 首次对 Agent 安全基准进行元审计，TrinityGuard 将 OWASP 标准引入 MAS，安全研究从"发现漏洞"转向"评估评估体系的完备性"
- **VLM 视觉编码器多元化：** SSM 作为 ViT 替代方案被正式评估，ViT-5 系统性现代化传统架构，视觉编码器"一家独大"的格局正在松动
- **零数据自进化跨模态扩展：** MM-Zero 将 LLM 零数据自进化成功拓展到多模态领域，降低了 VLM 对标注数据的依赖
- **Coding Agent 从编程工具走向研究引擎：** Claudini 证明 Claude Code 可自主发现 SOTA 算法，AutoResearchClaw 实现跨平台 Agent 互通，编程 Agent 正在重塑 AI 安全研究与科学发现流程
- **Agent 技能框架生态持续膨胀：** superpowers 连续多日霸榜，deer-flow、agentscope 等框架稳步增长，Agent 工程化基础设施趋于成熟

---

## 📝 术语/概念速记

- **SafeAudit / Rule-Resistance：** 对 Agent 安全基准自身进行覆盖率审计的元框架，使用基于工具调用 trace 的非语义评估协议
- **MARCH（Multi-Agent Reinforced Self-Check）：** 利用刻意信息不对称的多 Agent 协作框架，用于检测 RAG 系统中的幻觉确认偏差
- **ViT-5：** 对经典 Vision Transformer 的系统性组件级现代化升级
- **MM-Zero：** 首个零数据多模型 VLM 自进化框架，基于强化学习
- **PASTE（Pattern-Aware Speculative Tool Execution）：** 通过识别 Agent 工具调用模式进行推测性并行执行以降低延迟
- **Autoresearch：** 由 Coding Agent 驱动的自动化 AI 研究流水线，可自主迭代产出新算法