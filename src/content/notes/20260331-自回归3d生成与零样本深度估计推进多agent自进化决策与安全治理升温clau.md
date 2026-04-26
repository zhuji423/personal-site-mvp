---
title: "自回归3D生成与零样本深度估计推进，多Agent自进化决策与安全治理升温，Clau"
description: "**一句话总览**：CV 方向自回归 3D Gaussian 生成与零样本深度估计同步突破；Agent 领域自进化决策框架 SEMA 与多 Agent 安全治理持续升温；GitHub 上 hermes-agent 与 VibeVoice 双双爆发；Claude Code 创始人 Boris Cher..."
date: "2026-03-31"
category: "每日日报"
---

# 20260331 自回归3D生成与零样本深度估计推进，多Agent自进化决策与安全治理升温，Claude Code创始人公开15个隐藏技巧

Owner: AI论文抓取器
Last edited time: 2026年3月31日 10:19

**一句话总览**：CV 方向自回归 3D Gaussian 生成与零样本深度估计同步突破；Agent 领域自进化决策框架 SEMA 与多 Agent 安全治理持续升温；GitHub 上 hermes-agent 与 VibeVoice 双双爆发；Claude Code 创始人 Boris Cherny 公开 15 个隐藏/低利用率特性引发社区热议。

---

## 🧠 CV / NLP 大模型基础论文

### 1. GaussianGPT：自回归 3D Gaussian 场景生成

- **要点**：提出完全自回归的 3D 生成方法，用 next-token prediction 直接生成 3D Gaussians
- 使用稀疏 3D 卷积自编码器 + 向量量化将 Gaussian 原语压缩为离散 token
- 因果 Transformer 搭配 3D Rotary Positional Embedding 实现序列化空间生成
- 支持 completion、outpainting、温度可控采样等灵活生成模式
- **影响**：将自回归范式从 2D 扩展到显式 3D 表征，为可控 3D 内容生成开辟新路径
- **链接**：[arXiv:2603.26661](https://arxiv.org/abs/2603.26661)

### 2. FOSSA / ZEDD：零样本散焦深度估计基准与模型

- **要点**：提出 ZEDD 真实世界散焦深度估计基准，场景数量达前代 8.3 倍
- 设计 Transformer 架构 FOSSA，含 Stack Attention 层与焦距嵌入
- 开发合成焦点栈训练流水线，可复用大规模 RGBD 数据集
- 在多项基准上误差降低高达 **55.7%**
- **影响**：零样本泛化深度估计的实用性大幅提升，推动 DfD 方向进入可部署阶段
- **链接**：[arXiv:2603.26658](https://arxiv.org/abs/2603.26658)

### 3. Through the Lens of Contrast：VLM 对比自进化视觉推理（ICLR 2026 Oral）

- **要点**：提出对比驱动的自改进框架，无需外部标注即可提升 VLM 视觉推理能力
- 被 ICLR 2026 接收为 **Oral** 论文
- 跨 CV/AI/CL/LG 多领域交叉
- **影响**：VLM 自进化训练范式的里程碑工作，零数据自改进成为主流研究方向
- **链接**：[arXiv:2603.02556](https://arxiv.org/abs/2603.02556)

### 4. Opportunistic Motion：稀疏视角下的精细几何与外观重建

- **要点**：利用物体被人操控时的"机会运动"获取额外虚拟视角
- 使用 2D Gaussian Splatting + 交替最小化联合优化 6DoF 轨迹与原语参数
- 提出球谐反射方向探测的新外观模型，分离漫反射与镜面反射
- **影响**：为极稀疏视角的 3D 重建提供全新思路，利用日常交互动作即可提升重建质量
- **链接**：[arXiv:2603.26665](https://arxiv.org/abs/2603.26665)

---

## 🤖 Agent 相关论文

### 1. SEMA：自进化多 Agent 实时策略决策框架

- **要点**：面向 RTS 场景的多 Agent 协作框架，解决 LLM 推理延迟与规划一致性问题
- 基于结构熵的动态观测裁剪，将高维游戏状态压缩为核心语义
- 混合知识-记忆机制融合微轨迹、宏经验与层级领域知识
- StarCraft II 多地图实验中决策延迟降低 **50%+**，胜率领先
- **影响**：Agent 自进化与实时决策的交叉成为新焦点，混合记忆机制具有广泛迁移价值
- **链接**：[arXiv:2603.23875](https://arxiv.org/abs/2603.23875)

### 2. TrinityGuard：多 Agent 系统统一安全防护框架

- **要点**：面向多 Agent 系统的统一安全框架，覆盖 Deep Research Agent 等多种架构
- 提供全面的 Pass Rate 评测，量化防御能力
- 支持多种代表性多 Agent 系统的安全评估
- **影响**：多 Agent 安全从单点检测走向统一治理，推动生产级 MAS 的可信部署
- **链接**：[arXiv:2603.15408](https://arxiv.org/abs/2603.15408)

### 3. Clawed and Dangerous：开放 Agentic 系统信任治理

- **要点**：系统分析开放 Agentic 系统（编程助手、浏览器副驾驶、企业自动化）的安全治理
- 核心论点：这类系统的安全挑战不是单次攻击鲁棒性，而是「**持续不确定性下的 Agentic 行为治理**」
- 涵盖运行时计划生成、不可信自然语言输入、代理权限委托等
- **影响**：为 Agent 安全研究提供从「点防御」到「系统治理」的范式转变
- **链接**：[arXiv:2603.26221](https://arxiv.org/abs/2603.26221)

### 4. WildClawBench：真实场景 Agent 端到端评测

- **要点**：InternLM 团队发布的 in-the-wild Agent 基准，60 个原创任务覆盖足球集锦剪辑、邮件协商、矛盾检索等
- 所有前沿模型得分均低于 **0.6**，表明当前 Agent 能力仍有显著差距
- **影响**：Agent 评测从合成场景走向真实复杂任务，为能力瓶颈提供量化参考
- **链接**：[github.com/InternLM/WildClawBench](http://github.com/InternLM/WildClawBench)

---

## 🔥 GitHub 热门 Agent 项目

### 1. microsoft/VibeVoice ⭐ 30,698（+2,492/天）

- **简介**：微软开源的前沿语音 AI 项目
- **亮点**：开源 Frontier Voice AI，今日新增 star 数全站第一
- **链接**：[github.com/microsoft/VibeVoice](http://github.com/microsoft/VibeVoice)

### 2. NousResearch/hermes-agent ⭐ 18,723（+1,851/天）

- **简介**："The agent that grows with you"——可持续进化的 AI Agent 框架
- **亮点**：NousResearch 出品，强调 Agent 自适应成长，今日爆发式增长
- **链接**：[github.com/NousResearch/hermes-agent](http://github.com/NousResearch/hermes-agent)

### 3. agentscope-ai/HiClaw ⭐ v1.0.8

- **简介**：开源协作式多 Agent 操作系统，基于 Matrix 协议的 Human-in-the-Loop 任务协调
- **亮点**：Manager-Workers 架构，所有 Agent 对话实时可见，支持随时人工介入
- **链接**：[github.com/agentscope-ai/hiclaw](http://github.com/agentscope-ai/hiclaw)

### 4. Gen-Verse/OpenClaw-RL

- **简介**："Train any agent simply by talking"——通过自然语言对话反馈训练个性化 Agent
- **亮点**：全异步 RL 框架，支持终端/GUI/SWE/Tool-call 多场景，Track 2 已发布
- **链接**：[github.com/Gen-Verse/OpenClaw-RL](http://github.com/Gen-Verse/OpenClaw-RL)

---

## 💻 Claude Code / Coding Agent Skills

### 1. Boris Cherny（Claude Code 创始人）公开 15 个隐藏特性

- **要点**：3 月 30 日 Boris Cherny 在 X 上分享了 15 个 Claude Code 隐藏/低利用率特性
- 涵盖日常高频使用的生产力技巧
- 社区迅速整理为结构化文档并收录至 best-practice 仓库
- **影响**：官方视角的最佳实践指南，对 Claude Code 用户的工作流优化有直接价值
- **链接**：[claude-boris-15-tips-30-mar-26](https://github.com/shanraisshan/claude-code-best-practice/blob/main/tips/claude-boris-15-tips-30-mar-26.md)

### 2. agent-skill-manager (asm) ⭐ — 2,600+ Skills

- **要点**：跨 Agent 通用技能管理器，一个 CLI/TUI 管理 Claude Code、Codex、Cursor、Windsurf 等 10+ Agent 的技能
- 支持安装、搜索、审计、组织所有 Agent 技能
- **影响**：Coding Agent 技能生态碎片化问题的统一解决方案
- **链接**：[github.com/luongnv89/asm](http://github.com/luongnv89/asm)

### 3. Claude Code Skill Evals 正式上线（March 2026）

- **要点**：Claude Code 技能系统新增 Skill Evals 功能
- 区分两类技能：**Capability Uplift**（填补模型能力缺口，逐渐淡出）vs **Encoded Preference**（编码工作流偏好，持续保留）
- 支持 Benchmark Mode、A/B 测试、Trigger Tuning
- **影响**：技能质量从「主观感受」走向「可量化评测」，推动技能生态标准化

### 4. shanraisshan/claude-code-best-practice ⭐ 26,316（+1,108/天）

- **要点**：Claude Code 最佳实践合集，持续更新社区智慧
- 今日新增超过 1,100 star，位居 GitHub 日榜前列
- **影响**：Claude Code 社区知识沉淀的核心仓库
- **链接**：[github.com/shanraisshan/claude-code-best-practice](http://github.com/shanraisshan/claude-code-best-practice)

---

## 📈 趋势与信号

- **自回归 3D 生成**：GaussianGPT 将自回归范式推入显式 3D 表征，与 PERSIST 的持久 3D 状态世界模型形成互补
- **Agent 自进化与安全治理并行**：SEMA 自进化决策 + TrinityGuard/Clawed and Dangerous 安全治理，两条主线同步加速
- **真实场景评测成标配**：WildClawBench 将 Agent 评测拉入真实复杂任务，前沿模型得分 < 0.6 暴露能力缺口
- **Claude Code 技能生态标准化**：Skill Evals 上线 + asm 跨平台管理 + 创始人公开最佳实践，技能生态进入工程化阶段

---

## 📖 术语/概念速记

- **Opportunistic Motion**：利用人对物体的日常操控产生的"机会运动"作为额外虚拟视角来源
- **Structural Entropy**：基于图论的信息度量，SEMA 用于从高维游戏状态中提取核心拓扑语义
- **Skill Evals**：Claude Code 新功能，将技能分为 Capability Uplift（能力补充型）和 Encoded Preference（偏好编码型）两类并支持量化评测