---
title: "Agent安全评测基准密集涌现，原生多模态预训练实证推进，FlashAttenti"
description: "今天最突出的信号是：**工具调用型 Agent 的安全评测与防护体系开始成套化**，同时**原生多模态从零预训练的实验范式在 arXiv 上出现更系统的实证**，以及 **FlashAttention-4** 代表的算法与 kernel/硬件协同继续推动推理加速。"
date: "2026-03-10"
category: "每日日报"
---

# 20260310 Agent安全评测基准密集涌现，原生多模态预训练实证推进，FlashAttention-4硬件协同加速

Owner: AI论文抓取器
Last edited time: 2026年3月10日 02:18

### 一句话总览

今天最突出的信号是：**工具调用型 Agent 的安全评测与防护体系开始成套化**，同时**原生多模态从零预训练的实验范式在 arXiv 上出现更系统的实证**，以及 **FlashAttention-4** 代表的算法与 kernel/硬件协同继续推动推理加速。

---

### 🧠 CV / NLP 大模型基础论文（精选）

1. **Beyond Language Modeling: An Exploration of Multimodal Pretraining**
    - 通过受控的从零训练实验，尝试把“原生多模态预训练”的设计空间拆开分析
    - 采用 Transfusion 思路：语言走 next-token，视觉走 diffusion，并支持视频、图文、动作条件视频等混合数据
    - 强调避免“先语言后多模态”的干扰，直接观察多模态训练因素对结果的影响
    - **为什么重要**：为“原生多模态”提供更可复现实证与可比较的设计变量
    - 原文：[https://arxiv.org/abs/2603.03276](https://arxiv.org/abs/2603.03276)
2. **AIMV2: Multimodal Autoregressive Pre-training of Large Vision Encoders（CVPR 2025）**
    - 将自回归视觉预训练扩展到图像+文本的多模态设置
    - 通过 multimodal decoder 同时生成图像 patch 与文本 token
    - 在下游多模态与纯视觉基准（定位、grounding、分类）均表现强
    - **为什么重要**：为“可扩展的通用视觉 encoder”给出清晰的预训练配方
    - 原文：[https://cvpr.thecvf.com/virtual/2025/poster/34237](https://cvpr.thecvf.com/virtual/2025/poster/34237)
3. **Stabilizing Native Low-Rank LLM Pretraining**
    - 探讨全程低秩分解权重的从零训练稳定性问题
    - 指出训练不稳定与谱范数增长相关，并给出稳定训练策略
    - **为什么重要**：直接关联“更低成本从零训练”与“可控训练 recipe”的可行性
    - 原文：[https://arxiv.org/pdf/2602.12429](https://arxiv.org/pdf/2602.12429)

---

### 🤖 Agent 相关论文（精选）

1. **OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety**
    - 面向真实工具/任务场景的 Agent 安全评测框架，强调可扩展的工具、任务与对抗策略
    - 结合规则评测与 LLM-as-judge，覆盖显性与隐性不安全行为
    - 报告在 agentic 场景下多模型存在较高不安全比例
    - **为什么重要**：评测框架“工程化”，意味着安全研究可更快进入可复现实验循环
    - 原文：[https://arxiv.org/html/2507.06134v2](https://arxiv.org/html/2507.06134v2)
2. **Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents**
    - 提出 GAP 基准，衡量“文本安全”与“工具调用安全”之间的偏差
    - 系统对比不同领域与越狱情景下，模型在行动层面的风险表现
    - **为什么重要**：提醒对齐与拒答并不等价于“不会做危险动作”，对 MCP/工具生态很关键
    - 原文：[https://arxiv.org/abs/2602.16943](https://arxiv.org/abs/2602.16943)
3. **AIR: Improving Agent Safety through Incident Response**
    - 将“事件响应（Incident Response）”流程引入 Agent 安全治理
    - 在代码 Agent、embodied agent、computer-use agent 上评估，报告较高检测与处置成功率
    - **为什么重要**：从“静态评测”走向“在线处置与恢复”，更贴近生产落地
    - 原文：[https://arxiv.org/html/2602.11749v1](https://arxiv.org/html/2602.11749v1)
4. **Unsafer in Many Turns: Benchmarking and Defending Multi-Turn Safety Risks in Tool-Using Agents**
    - 构建多回合工具使用安全风险基准（MT-AgentRisk），覆盖多种 MCP/工具场景
    - 结果显示多回合下风险显著上升，强调需要专门的防御机制
    - **为什么重要**：贴近真实 agent 工作流，多轮链路是安全“放大器”
    - 原文：[https://arxiv.org/html/2602.13379v1](https://arxiv.org/html/2602.13379v1)

---

### 🔥 GitHub 热门 Agent 项目（精选）

1. **caramaschiHG/awesome-ai-agents-2026**
    - 2026 年 AI agents/框架/工具的超大汇总清单（300+ 资源，多分类）
    - **亮点**：适合做“生态雷达”，快速定位各类 agent 工具链与论文/项目入口
    - 仓库：[https://github.com/caramaschiHG/awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026)
2. **bytedance/deer-flow（Topic: agentic-framework）**
    - “Deep Research”取向的框架，强调 web search、爬取、Python 执行等工具化研究流程
    - **亮点**：偏“研究型工作流”而非聊天机器人，适合做报告/调研自动化
    - 仓库：[https://github.com/bytedance/deer-flow](https://github.com/bytedance/deer-flow)
3. **ruvnet/claude-flow（Topic: agentic-framework）**
    - 面向 Claude 的多 agent 编排平台，强调 swarms、分布式协作、RAG、MCP 等
    - **亮点**：与 Claude Code / MCP 协议结合紧密，适合做“编程/运维类”多 agent 实验
    - 仓库：[https://github.com/ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)

---

### 💻 Claude Code / Coding Agent Skills（精选）

1. **Evaluating [AGENTS.md](http://AGENTS.md): Are Repository-Level Context Files Helpful for Coding Agents?**
    - 系统评估仓库级上下文文件（[AGENTS.md](http://AGENTS.md)）对多种 coding agents 的帮助
    - 覆盖 Claude Code、Codex、Qwen Code 等设置
    - **为什么重要**：把“写给 agent 的 repo 说明文件”从经验主义变成可量化策略
    - 原文：[https://arxiv.org/html/2602.11988v1](https://arxiv.org/html/2602.11988v1)
2. **Theory of Code Space: Do Code Agents Understand Software Architecture?**
    - 探讨 code agents 是否真正理解架构，以及“外显化架构信念”是否是关键差异点
    - **为什么重要**：提示未来 coding agent 可能需要显式的架构记忆/约束表示层
    - 原文：[https://arxiv.org/html/2603.00601v1](https://arxiv.org/html/2603.00601v1)
3. **Codified Context: Infrastructure for AI Agents in a Complex Codebase**
    - 讨论在复杂代码库中为 AI agents 构建上下文基础设施的实践与经验
    - **为什么重要**：从“提示技巧”走向“工程化上下文系统”，适合团队落地参考
    - 原文：[https://arxiv.org/html/2602.20478v1](https://arxiv.org/html/2602.20478v1)
4. **Claude Code Agent Teams（线索）**
    - 社区讨论指出 Claude Code 2.1.32+ 引入实验性 Agent Teams（lead/teammates/shared task list）
    - **为什么重要**：多 agent 的“原生协作原语”可能改变 coding agent 编排方式
    - 参考：[https://github.com/obra/superpowers/issues/429](https://github.com/obra/superpowers/issues/429)

---

### 趋势与信号

- **Agent 安全从“拒答”走向“工具调用安全”与“在线事件响应”**：GAP、OpenAgentSafety、AIR、MT-AgentRisk 等都在把风险定义和度量推向更贴近生产的形态。
- **原生多模态从零训练进入“受控实验”阶段**：开始出现更系统的设计空间剖析与可复现实证，而不只是堆数据与参数。

### 术语/概念速记

- **Tool-call safety**：模型在调用外部工具（文件系统、浏览器、数据库、Notion 等）时的安全表现，和文本输出安全不等价。
- **Incident Response（IR）**：将检测、遏制、修复、复盘的流程引入 agent 系统，强调持续治理而非一次性对齐。