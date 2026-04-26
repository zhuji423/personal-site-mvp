---
title: "Agent安全对齐框架MOSAIC与工具自进化EvoTool双线突破，VLA持续学-2"
description: "**一句话总览**：Agent 安全对齐进入可训练阶段（MOSAIC 框架跨模型泛化），工具使用策略自进化（EvoTool 模块化演化范式确立），VLA 预训练模型展现持续学习抗遗忘能力，多 Agent 编排框架与 Coding Agent 工具链持续涌现。"
date: "2026-03-08"
category: "每日日报"
---

# 20260308 Agent安全对齐框架MOSAIC与工具自进化EvoTool双线突破，VLA持续学习抗遗忘实证，多Agent编排与Coding Agent生态加速成熟

Owner: AI论文抓取器
Last edited time: 2026年3月8日 01:35

<aside>
📌

**一句话总览**：Agent 安全对齐进入可训练阶段（MOSAIC 框架跨模型泛化），工具使用策略自进化（EvoTool 模块化演化范式确立），VLA 预训练模型展现持续学习抗遗忘能力，多 Agent 编排框架与 Coding Agent 工具链持续涌现。

</aside>

---

## 🧠 CV / NLP 大模型基础论文

### 1. Beyond Language Modeling: An Exploration of Multimodal Pretraining

- **要点**：
    - 系统探索多模态预训练范式，超越纯语言建模框架
    - 涵盖文本、图像等多模态信号的联合预训练策略
    - 来自 Meta/NYU 等团队，作者阵容包括 Shengbang Tong、Rob Fergus 等
    - 对 VLM 预训练方法论提出新实证视角
    - 为下一代多模态基础模型提供设计参考
- **影响**：多模态预训练正从"语言+视觉对齐"走向"原生多模态联合建模"，本文为该方向提供重要实证基础
- **链接**：[arxiv.org/abs/2603.03276](http://arxiv.org/abs/2603.03276)

### 2. Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning

- **要点**：
    - 发现预训练 Vision-Language-Action (VLA) 模型在持续学习中表现出显著的抗遗忘能力
    - 大规模预训练从根本上改变了持续学习的动态特性
    - 即使"遗忘"的技能也能通过少量微调快速恢复
    - 简单的 replay 策略即可支持模型持续获取新技能
    - 来自 UT Austin 团队（Yuke Zhu 组）
- **影响**：VLA 模型的抗遗忘特性意味着通用机器人基础模型可以通过持续学习不断扩展能力，降低重训成本
- **链接**：[arxiv.org/abs/2603.03818](http://arxiv.org/abs/2603.03818)

### 3. Bootstrapping Frozen OCR with Visual Prompts (Whisperer)

- **要点**：
    - 提出 Whisperer 视觉提示框架，通过扩散模型预处理器在像素空间适配输入
    - 无需修改冻结 OCR 模型权重即可提升识别效果
    - 学习像素级视觉提示（visual prompts）来引导下游任务
    - 方法通用，可适配多种冻结视觉模型
    - 为"不改模型改输入"的范式提供新思路
- **影响**：视觉提示学习（Visual Prompting）正在成为高效适配冻结视觉模型的重要手段
- **链接**：[arxiv.org/html/2603.05276v1](http://arxiv.org/html/2603.05276v1)

### 4. Separators in Enhancing Autoregressive Pretraining (Mamba-CV)

- **要点**：
    - 探索 Mamba 状态空间模型在计算机视觉中的应用
    - 研究分隔符（Separators）对自回归预训练的增强效果
    - Mamba 作为 Transformer 的替代架构在视觉领域持续获得关注
    - 涉及序列建模效率与长程依赖建模的平衡
- **影响**：非 Transformer 架构在视觉领域的探索加速，Mamba 在 CV 中的潜力进一步被挖掘
- **链接**：[arxiv.org/html/2603.03806v1](http://arxiv.org/html/2603.03806v1)

---

## 🤖 Agent 相关论文

### 1. MOSAIC: Learning When to Act or Refuse — Agent 安全对齐框架

- **要点**：
    - 提出 Plan → Check → Act/Refuse 循环，将安全决策变为可学习的一等动作
    - 使用偏好式强化学习（pairwise trajectory comparison）训练 Agent 安全行为
    - 跨三个模型家族（Qwen2.5-7B、Qwen3-4B、Phi-4）零样本泛化
    - 有害行为减少最高 50%，注入攻击拒绝率提升 20%+，隐私泄露显著降低
    - MOSAIC 训练的开源模型在安全性上**超越未加安全脚手架的 GPT-4o 和 GPT-5**
- **影响**：Agent 安全对齐进入"可训练、可泛化"阶段，MOSAIC 证明安全不是规模的副产品而是需要显式设计的能力
- **链接**：[arxiv.org/abs/2603.03205](http://arxiv.org/abs/2603.03205)

### 2. EvoTool: Self-Evolving Tool-Use Policy Optimization

- **要点**：
    - 将 Agent 工具使用策略分解为 Planner、Selector、Caller、Synthesizer 四个模块
    - 提出 Trajectory-Grounded Blame Attribution：基于轨迹诊断定位故障模块
    - Feedback-Guided Targeted Mutation：仅编辑出错模块，避免全局回归
    - Diversity-Aware Population Selection：保留互补候选策略，防止模式坍缩
    - 在 ToolBench/RestBench/τ-Bench/BFCL 四个基准上超越 SOTA 5+ 分
- **影响**：工具使用策略优化从"整体提示搜索"进化为"模块化归因+定向突变"，EvoTool 确立了自进化 Agent 的新范式
- **链接**：[arxiv.org/abs/2603.04900](http://arxiv.org/abs/2603.04900)

### 3. AgentVista: Ultra-Challenging Realistic Visual Scenarios Benchmark

- **要点**：
    - 首个面向通用多模态 Agent 的超高难度真实场景评测基准
    - 聚焦长时程、交叉工具使用、真实视觉输入的复杂任务
    - 填补了现有多模态 Agent 评测在真实性与难度上的空白
    - 强调视觉检查与多工具交叉使用的反复迭代
- **影响**：Agent 评测从"合成场景"走向"真实世界超高难度"，推动多模态 Agent 向实用化发展
- **链接**：[arxiv.org/html/2602.23166v1](http://arxiv.org/html/2602.23166v1)

### 4. MagicAgent: Towards Generalized Agent Planning

- **要点**：
    - 来自荣耀与复旦大学联合团队
    - 目标是构建通用化的 Agent 规划能力
    - 涵盖多步推理、工具调用、跨领域任务规划
    - 模型即将开源
- **影响**：国内团队在 Agent 通用规划领域的重要尝试，产学研结合加速落地
- **链接**：[arxiv.org/html/2602.19000v2](http://arxiv.org/html/2602.19000v2)

---

## 🔥 GitHub 热门 Agent 项目

### 1. agno-agi/agno ⭐ 38.5k

- **简介**：构建、运行、管理大规模 Agentic 软件的全栈框架
- **亮点**：支持多 Agent 编排、工具调用、可观测性，Python 原生
- **仓库**：[github.com/agno-agi/agno](http://github.com/agno-agi/agno)

### 2. oh-my-openagent (OmO) ⭐ 37.6k

- **简介**：号称"最佳 Agent Harness"，前身为 oh-my-opencode
- **亮点**：
    - 集成 Claude Code 兼容层、后台 Agent、专业化 Agent（oracle/librarian/frontend engineer）
    - 内置 LSP/AST 工具、MCP 支持
    - v3.10.0 新增 HTTP Hook 安全加固
- **仓库**：[github.com/code-yeongyu/oh-my-openagent](http://github.com/code-yeongyu/oh-my-openagent)

### 3. MassGen ⭐ 817

- **简介**：开源多 Agent 扩展系统，在终端中自主编排前沿模型协作
- **亮点**：
    - 每个 Agent 独立解决完整问题，通过冗余与迭代精炼协作
    - 共识投票机制选出最佳答案
    - 支持多轮精炼与重启
- **仓库**：[github.com/massgen/MassGen](http://github.com/massgen/MassGen)

### 4. ComposioHQ/awesome-claude-skills ⭐ 41.4k

- **简介**：精选 Claude Skills 资源列表，涵盖自定义 Claude AI 工作流
- **亮点**：社区驱动的 Claude 能力扩展生态，涵盖 Skills、工具链、最佳实践
- **仓库**：[github.com/ComposioHQ/awesome-claude-skills](http://github.com/ComposioHQ/awesome-claude-skills)

---

## 💻 Claude Code / Coding Agent Skills

### 1. GitHub Copilot CLI 1.0 正式发布

- **要点**：
    - GitHub Copilot CLI 正式 GA，版本号升至 1.0
    - 新增 `exit` 裸命令退出、Enter 键提交表单、跨平台 `command` 字段别名
    - Hook 配置支持 `timeout` 作为 `timeoutSec` 的别名
    - 修复 meta+control 键组合处理
- **影响**：CLI 形态的 Coding Agent 正式进入生产就绪阶段
- **链接**：[github.com/github/copilot-cli/releases](http://github.com/github/copilot-cli/releases)

### 2. Everything Claude Code (ECC) v1.8.0

- **要点**：
    - 992 个测试、56 个 Skills、33 个 Commands、14 个 Agents
    - 覆盖 Claude Code、Codex、Cursor、OpenCode 四大编码 Harness
    - v1.7.0 新增 Cursor CLI/IDE 目标转换与演示构建工作流
    - 可复用的研究、内容、融资 Skills
- **影响**：Claude Code 的 Skills/Commands 生态持续膨胀，跨 Harness 兼容成为趋势
- **链接**：[github.com/affaan-m/everything-claude-code](http://github.com/affaan-m/everything-claude-code)

### 3. Compound Engineering Plugin v0.5.0 — Cursor 格式转换

- **要点**：
    - `--to cursor` 将 Claude Code 插件转换为 Cursor 格式
    - Agents → `.cursor/rules/*.mdc`，Commands → `.cursor/commands/*.md`
    - MCP servers → `.cursor/mcp.json`
    - 同时支持 Cursor IDE 和 Cursor CLI（`cursor-agent`）
- **影响**：Coding Agent 插件生态开始实现跨平台互操作
- **链接**：[github.com/EveryInc/compound-engineering-plugin](http://github.com/EveryInc/compound-engineering-plugin)

### 4. Cline vs Cursor vs Roo Code vs Claude Code — 2026 竞争格局讨论

- **要点**：
    - Cline 坚持 human-in-the-loop 审查模式（每个文件写入和终端命令需确认）
    - Cursor 倾向更自主的执行方式
    - 社区围绕"自主性 vs 可控性"展开深度讨论
    - 不同工具在不同场景下各有优势
- **影响**：Coding Agent 的核心设计分歧——自主执行 vs 人类审查——正在塑造不同的产品定位
- **链接**：[github.com/cline/cline/issues/9174](http://github.com/cline/cline/issues/9174)

---

## 📊 趋势与信号

- **Agent 安全对齐成为独立研究方向**：MOSAIC 证明安全不是规模的自然涌现，需要显式的推理结构与训练机制
- **工具使用策略自进化**：EvoTool 的模块化归因+定向突变范式可能成为 Agent 工具优化的标准方法
- **VLA 持续学习**：预训练 VLA 的抗遗忘特性为通用机器人基础模型的持续扩展打开大门
- **Coding Agent 跨平台互操作**：Skills/Commands/MCP 格式正在从单一工具走向跨 Harness 标准化
- **多 Agent 编排持续升温**：MassGen（共识投票）、OmO（专业化 Agent 协作）代表不同的多 Agent 协作哲学

---

## 📖 术语/概念速记

| 术语 | 解释 |
| --- | --- |
| **MOSAIC** | Modular Safety-Aligned Inference and Control，Agent 安全对齐框架，结构化为 Plan→Check→Act/Refuse 循环 |
| **EvoTool** | 自进化工具使用策略框架，通过 Blame Attribution + Targeted Mutation 优化模块化 Agent |
| **VLA** | Vision-Language-Action 模型，将视觉、语言、动作统一的机器人基础模型 |
| **Agent Harness** | 编码 Agent 的运行框架/外壳，管理 Agent 的 Skills、Commands、MCP 等 |
| **GRPO** | Group Relative Policy Optimization，组相对策略优化，MOSAIC 训练中使用的 RL 方法 |