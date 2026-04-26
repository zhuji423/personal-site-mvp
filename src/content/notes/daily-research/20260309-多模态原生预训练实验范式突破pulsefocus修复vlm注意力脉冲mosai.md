---
title: "多模态原生预训练实验范式突破，PulseFocus修复VLM注意力脉冲，MOSAI"
description: "**一句话总览**：多模态原生预训练（Beyond Language Modeling）从零实验框架由 Meta/NYU 确立，VLM 多图推理注意力脉冲问题被 PulseFocus 首次发现并修复；Agent 安全对齐框架 MOSAIC 与多模态 Web Agent 对抗训练持续推进；learn-..."
date: "2026-03-09"
category: "每日日报"
---

# 20260309 多模态原生预训练实验范式突破，PulseFocus修复VLM注意力脉冲，MOSAIC安全对齐持续引领Agent工具安全，learn-claude-code登顶GitHub Trending

Owner: AI论文抓取器
Last edited time: 2026年3月9日 03:20

<aside>
📅

**一句话总览**：多模态原生预训练（Beyond Language Modeling）从零实验框架由 Meta/NYU 确立，VLM 多图推理注意力脉冲问题被 PulseFocus 首次发现并修复；Agent 安全对齐框架 MOSAIC 与多模态 Web Agent 对抗训练持续推进；learn-claude-code 以日增 950+ Star 登顶 GitHub Trending，Coding Agent 技能生态与 Harness 编排系统加速成熟。

</aside>

---

## 🧠 CV / NLP 大模型基础论文

### 1. Beyond Language Modeling: An Exploration of Multimodal Pretraining

**要点：**

- Meta FAIR 与 NYU 联合发布，基于 Transfusion 框架（语言用 next-token prediction，视觉用 diffusion）从零进行多模态预训练
- 实验覆盖文本、视频、图文对、动作条件视频等多种数据类型
- 隔离影响原生多模态预训练的关键因素，不依赖语言预训练的干扰
- 为「原生多模态」路线提供了首个系统性消融实验框架

**影响**：这是多模态预训练设计空间的首次系统性实证研究，为后续原生多模态模型（非语言预训练+视觉微调）奠定实验基线。

**原文链接**：[arXiv:2603.03276](https://arxiv.org/html/2603.03276v1)

---

### 2. PulseFocus: Decoding the Pulse of Reasoning VLMs in Multi-Image Understanding

**要点：**

- 发现推理型 VLM 在 Chain-of-Thought 生成过程中存在 text-to-image 注意力「脉冲」现象：注意力分散且无法聚焦到任务相关图像
- 揭示了注意力在不同图像间的系统性位置偏差
- 提出 PulseFocus：training-free 推理时方法，将 CoT 推理结构化为交错的 think/focus 块并加入软注意力门控
- 在 BLINK benchmark（+3.7%）和 MuirBench（+1.07%）上取得一致提升

**影响**：首次揭示多图推理中 VLM 注意力失焦的根本原因，PulseFocus 作为零训练即插即用方案具有很强的实用价值。

**原文链接**：[arXiv:2603.04676](https://arxiv.org/html/2603.04676v1)

---

### 3. HALP: Detecting Hallucinations in VLMs without Generating a Single Token

**要点：**

- 提出无需生成任何 token 即可检测 VLM 幻觉的方法
- 利用模型内部表征（注意力/隐状态）直接判断输出可信度
- 可作为推理前的预筛选机制，大幅降低幻觉内容传播风险

**影响**：VLM 幻觉检测从「生成后检查」迈向「预生成检测」，对部署可信多模态系统意义重大。

**原文链接**：[arXiv:2603.05465](https://arxiv.org/list/cs.CV/recent)

---

### 4. Mario: Multimodal Graph Reasoning with Large Language Models

**要点：**

- 提出图条件视觉-语言模型（Graph-conditioned VLM），在拓扑结构下对齐图像与文本
- 引入 modality-adaptive graph instruction tuning，按节点选择最优模态
- 打破了 GraphLLM 依赖固定模态模板的范式
- 在节点分类和链接预测上达到 SOTA

**影响**：首次将多模态图推理与 LLM 深度融合，为知识图谱、社交网络等场景开辟新方向。

**原文链接**：[arXiv:2603.05181](https://arxiv.org/html/2603.05181v1)

---

### 5. UniM: A Unified Any-to-Any Interleaved Multimodal Benchmark

**要点：**

- 首个统一的「任意模态到任意模态」交错多模态评测基准
- 覆盖文本、图像、视频等多种模态的交错输入输出
- 为衡量原生多模态模型的真实能力提供标准化评测

**影响**：填补了交错多模态评测的空白，推动多模态模型从「单任务评测」向「真实交互评测」演进。

**原文链接**：[arXiv:2603.05075](https://arxiv.org/html/2603.05075v1)

---

## 🤖 Agent 相关论文

### 1. MOSAIC: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use

**要点：**

- 来自 Microsoft Research，针对 Agent 多步工具调用的安全对齐框架
- 将推理结构化为 **plan → check → act or refuse** 循环，安全推理和拒绝作为一等公民
- 使用基于偏好的强化学习（pairwise trajectory comparisons），无需轨迹级标签
- 解决了现有对齐方法在序列决策、对抗性工具反馈、过度自信推理中的失效问题

**影响**：MOSAIC 是目前最系统的 Agent 工具安全对齐框架，对 Agent 生产部署安全性具有里程碑意义。

**原文链接**：[arXiv:2603.03205](https://arxiv.org/html/2603.03205v1)

---

### 2. Dual-Modality Multi-Stage Adversarial Safety Training for Multimodal Web Agents

**要点：**

- 针对多模态 Web Agent 的跨模态攻击问题，提出双模态多阶段对抗安全训练框架
- 将多模态 Agent 安全建模为二人博弈
- 设计 HTML 注入机制，聚焦敏感数据泄露威胁
- 实证表明多模态 Agent 在视觉攻击下脆弱性显著增加

**影响**：首个系统性研究多模态 Web Agent 跨模态攻击的工作，为 Agent 部署安全提供新视角。

**原文链接**：[arXiv:2603.04364](https://arxiv.org/html/2603.04364v1)

---

### 3. AgentAlign: Safety Alignment for Agentic LLMs

**要点：**

- 利用抽象行为链（abstract behavior chains）作为安全对齐数据合成的媒介
- 在模拟环境中用多样化工具实例来实例化行为链
- 生成高度真实且可执行的指令，捕获复杂多步动态
- 解决了 LLM 从「知识提供者」转向「动作执行者」后的安全缺陷

**影响**：为 Agent 后训练阶段的安全对齐提供了可扩展的数据合成框架。

**原文链接**：[arXiv:2505.23020](https://arxiv.org/abs/2505.23020)

---

### 4. PlanGEN: Multi-Agent Framework for Planning and Reasoning Trajectories

**要点：**

- 提出模型无关、易扩展的 Agent 框架，包含约束 Agent、验证 Agent、选择 Agent 三组件
- 引入约束引导的迭代验证机制，增强推理时算法（Best of N、Tree-of-Thought、REBASE）
- 适应实例级复杂度而非任务级统一处理

**影响**：将约束满足与推理时搜索算法有机结合，为复杂规划问题提供了更可靠的 Agent 解决方案。

**原文链接**：[arXiv:2502.16111](https://arxiv.org/abs/2502.16111)

---

### 5. ToolSafe: Proactive Step-level Guardrail for LLM-based Agent Tool Invocation

**要点：**

- 构建 TS-Bench：首个步骤级工具调用安全检测基准
- 开发 TS-Guard：基于多任务强化学习的护栏模型
- 在执行前主动检测不安全工具调用，而非事后检查
- 输出可解释的安全判断和反馈

**影响**：将 Agent 安全从「事后审查」推进到「执行前主动拦截」，是 Agent 部署安全的重要补充。

**原文链接**：[arXiv:2601.10156](https://arxiv.org/html/2601.10156v1)

---

## 🔥 GitHub 热门 Agent 项目

### 1. learn-claude-code ⭐ 23,607 (+953/天)

**简介**：shareAI-lab 出品，"Bash is all you need" —— 从零到一构建一个类 Claude Code 的 nano agent。

**亮点功能**：

- 纯 TypeScript 实现，极简架构
- 从基础 Chat → 文件读取 → 命令执行 → 代码搜索逐步构建完整 Coding Agent
- 极佳的教学价值，适合理解 Coding Agent 内部原理

**仓库链接**：[github.com/shareAI-lab/learn-claude-code](http://github.com/shareAI-lab/learn-claude-code)

---

### 2. CyberStrikeAI ⭐ 2,084 (+242/天)

**简介**：Go 语言构建的 AI 原生安全测试平台，集成 100+ 安全工具。

**亮点功能**：

- 智能编排引擎，自动协调多种安全测试工具
- 角色化测试：预定义安全角色，模拟不同攻击者视角
- 技能系统：专业化测试技能模块化管理
- 全生命周期管理能力

**仓库链接**：[github.com/Ed1s0nZ/CyberStrikeAI](http://github.com/Ed1s0nZ/CyberStrikeAI)

---

### 3. ruflo ⭐ 19,500

**简介**：领先的 Claude Agent 编排平台，支持多 Agent 集群部署与自治工作流协调。

**亮点功能**：

- 企业级架构，分布式 swarm 智能
- RAG 集成，原生 Claude Code / Codex 支持
- 可构建对话式 AI 系统和自治工作流

**仓库链接**：[github.com/ruvnet/ruflo](http://github.com/ruvnet/ruflo)

---

### 4. claude-mem ⭐ 33,200

**简介**：Claude Code 插件，自动捕获编码会话中的所有操作，用 AI 压缩后注入未来会话上下文。

**亮点功能**：

- 基于 Anthropic agent-sdk 的 AI 压缩
- 自动持久化会话记忆
- 跨会话上下文注入，解决 Coding Agent 的「失忆」问题

**仓库链接**：[github.com/thedotmack/claude-mem](http://github.com/thedotmack/claude-mem)

---

### 5. VoltAgent ⭐ 持续上升

**简介**：端到端 AI Agent 工程平台，开源 TypeScript 框架 + VoltOps 运维控制台。

**亮点功能**：

- Memory、RAG、Guardrails、Tools、MCP、Voice、Workflow 全栈支持
- 多 Agent 系统：专业化 Agent 在 Supervisor 协调下协作
- 可观测性、自动化、部署、评测一体化

**仓库链接**：[github.com/VoltAgent/voltagent](http://github.com/VoltAgent/voltagent)

---

## 💻 Claude Code / Coding Agent Skills

### 1. Claude Code v2.1.71 发布（March 6, 2026）

**要点：**

- 最新版系统提示已更新，包含约 40 条系统提醒
- Piebald AI 团队持续追踪，自 v2.0.14 以来已记录 121 个版本的系统提示变更
- 社区发现 [CLAUDE.md](http://CLAUDE.md) 知识检索在长会话中偶尔失效（Issue #32161）

**影响**：系统提示的持续优化直接影响 Claude Code 的行为可控性和安全边界。

**参考链接**：[github.com/Piebald-AI/claude-code-system-prompts](http://github.com/Piebald-AI/claude-code-system-prompts)

---

### 2. Everything Claude Code v1.8.0 — Harness Performance System

**要点：**

- 正式定位为「Agent Harness 性能系统」，不再只是配置包
- Hook 可靠性大修：SessionStart root fallback、Stop 阶段会话总结
- 新增运行时控制：`ECC_HOOK_PROFILE=minimal|standard|strict`
- 新增 harness 命令：`/harness-audit`、`/loop-start`、`/quality-gate`、`/model-route`
- NanoClaw v2：模型路由、技能热加载、会话分支/搜索/导出/压缩/指标
- 跨 harness 一致性：Claude Code、Cursor、OpenCode、Codex 行为统一
- 997 项内部测试全部通过

**影响**：Coding Agent 从「单工具」进化为「可编排 Harness 系统」，标志着 Coding Agent 工程化成熟度的新阶段。

**参考链接**：[github.com/affaan-m/everything-claude-code](http://github.com/affaan-m/everything-claude-code)

---

### 3. Awesome Agent Skills — 500+ 技能生态

**要点：**

- VoltAgent 团队维护，收录 500+ Agent 技能
- 兼容 Claude Code、Codex、Antigravity、Gemini CLI、Cursor 等
- 涵盖官方开发团队和社区贡献的技能
- 强调生产使用前需安全审计

**影响**：Agent 技能生态爆发式增长，但供应链安全（655 个恶意技能已被识别）成为新关注焦点。

**参考链接**：[github.com/VoltAgent/awesome-agent-skills](http://github.com/VoltAgent/awesome-agent-skills)

---

### 4. Agentlytics — 统一 Coding Agent 分析面板

**要点：**

- 支持 Cursor、Windsurf、Claude Code、VS Code Copilot、Zed、Antigravity、OpenCode 等 12+ 工具
- 统一分析 AI 编码 Agent 的使用数据
- npm 包形式发布，开箱即用

**影响**：随着 Coding Agent 工具碎片化，统一可观测性工具成为刚需。

**参考链接**：[github.com/f/agentlytics](http://github.com/f/agentlytics)

---

### 5. [AGENTS.md](http://AGENTS.md) 标准化问题浮出水面

**要点：**

- OpenClaw 项目 Issue #32363 揭示 [AGENTS.md](http://AGENTS.md) 中 `YYYY-MM-DD` 为字面量而非动态替换
- 导致 Agent 基于训练截止日期猜测时间（如 Claude Sonnet 4.6 猜测约 2025 年 7 月，实际为 2026 年 3 月）
- 反映 [AGENTS.md](http://AGENTS.md) 开放标准在实际使用中的边界问题

**影响**：随着 [AGENTS.md](http://AGENTS.md) 成为 Coding Agent 互通的事实标准，其规范性和可靠性问题亟待解决。

**参考链接**：[github.com/openclaw/openclaw/issues/32363](http://github.com/openclaw/openclaw/issues/32363)

---

## 📡 趋势与信号

- **原生多模态预训练持续升温**：Meta/NYU 的 Beyond Language Modeling 和 UniM benchmark 表明，「先训语言再接视觉」的范式正被「从零多模态」取代
- **Agent 安全对齐框架密集涌现**：MOSAIC、Dual-Modality Adversarial Training、AgentAlign、ToolSafe 四篇论文同时推进，Agent 安全从「单点防御」走向「系统化框架」
- **VLM 注意力机制被深入剖析**：PulseFocus 揭示的注意力脉冲问题和 HALP 的零生成幻觉检测，标志着 VLM 可靠性研究进入新阶段
- **Coding Agent 生态工程化加速**：Harness 系统（ECC v1.8.0）、技能生态（500+ Skills）、统一分析（Agentlytics）、跨工具互通（[AGENTS.md](http://AGENTS.md)）四条线并进
- **learn-claude-code 登顶 Trending 说明什么**：开发者对 Coding Agent 内部原理的需求爆发，从「使用 Agent」转向「理解和构建 Agent」

---

## 📖 术语/概念速记

| 术语 | 解释 |
| --- | --- |
| **Transfusion** | Meta 提出的混合预训练框架：语言部分用 next-token prediction，视觉部分用 diffusion |
| **PulseFocus** | 推理时注意力修复方法，将 CoT 结构化为 think/focus 交错块 |
| **MOSAIC** | Microsoft 的 Agent 安全对齐框架：plan → check → act or refuse 循环 |
| **Agent Harness** | Coding Agent 的编排运行时系统，管理 Hook、模型路由、技能加载等 |
| [**AGENTS.md**](http://AGENTS.md) | Coding Agent 互通开放标准文件，定义 Agent 行为规范 |
| **TS-Bench / TS-Guard** | 首个步骤级工具调用安全检测基准和护栏模型 |