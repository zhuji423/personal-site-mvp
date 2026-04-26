---
title: "原生多模态预训练实验框架确立，MOSAIC安全对齐持续引领Agent工具安全，Co"
description: "**一句话总览**：原生多模态预训练实验框架（Beyond Language Modeling）为视觉-语言基础模型设计空间提供实证指引；MOSAIC 安全对齐框架持续引领 Agent 多步工具安全研究；多语言对齐反噬（Alignment as Iatrogenesis）揭示安全机制语言依赖性；Co..."
date: "2026-03-09"
category: "每日日报"
---

# 20260309 原生多模态预训练实验框架确立，MOSAIC安全对齐持续引领Agent工具安全，Coding Agent技能生态与Harness系统加速成熟

Owner: AI论文抓取器
Last edited time: 2026年3月9日 02:18

<aside>
📅

**一句话总览**：原生多模态预训练实验框架（Beyond Language Modeling）为视觉-语言基础模型设计空间提供实证指引；MOSAIC 安全对齐框架持续引领 Agent 多步工具安全研究；多语言对齐反噬（Alignment as Iatrogenesis）揭示安全机制语言依赖性；Coding Agent 技能生态与 Harness 性能系统加速成熟。

</aside>

---

## 🧠 CV / NLP 大模型基础论文

### 1. Beyond Language Modeling: An Exploration of Multimodal Pretraining

- **要点**：
    - 采用 Transfusion 框架，对语言使用 next-token prediction、对视觉使用 diffusion，从零开始进行受控预训练实验
    - 训练数据涵盖文本、视频、图文对甚至动作条件视频，系统隔离影响多模态预训练的关键因素
    - 为原生多模态模型设计空间提供了实证清晰度，消除了语言预训练的干扰
- **影响**：为下一代原生多模态基础模型的架构选择和数据配比提供了关键实验依据，有望加速视觉-语言统一预训练范式的收敛
- **链接**：[arxiv.org/abs/2603.03276](http://arxiv.org/abs/2603.03276)

### 2. Pretrained VLAs are Surprisingly Resistant to Forgetting

- **要点**：
    - 发现预训练 Vision-Language-Action（VLA）模型在持续学习中对遗忘的抵抗力远超从零训练的小型策略模型
    - 简单的 Experience Replay（ER）在 VLA 上效果极佳，甚至可以在小回放数据量下实现零遗忘
    - 预训练是下游持续学习性能的关键因素：大预训练模型可在小回放缓冲区下同时缓解遗忘并保持前向学习能力
- **影响**：为具身智能领域的持续学习提供了重要实证，表明大规模预训练 VLA 天然具备抗遗忘优势，降低了实际部署中的数据需求
- **链接**：[arxiv.org/abs/2603.03818](http://arxiv.org/abs/2603.03818)

### 3. Alignment as Iatrogenesis: Language-Dependent Reversal of Safety Interventions in LLM Multi-Agent Systems Across 16 Languages

- **要点**：
    - 跨 16 种语言实证揭示：安全对齐在非英语语言空间中可能产生反效果（iatrogenesis）
    - 提出语言空间（language space）是对齐结果的结构性决定因素，英语验证的安全性无法迁移至其他语言
    - 将对齐重新定义为行为干预而非单向安全机制，类比临床领域的风险代偿与安全替代效应
- **影响**：对多语言 LLM 的安全部署提出根本性挑战，提示当前以英语为中心的对齐策略存在系统性盲区
- **链接**：[arxiv.org/abs/2603.04904](http://arxiv.org/abs/2603.04904)

### 4. DEP: A Decentralized Large Language Model Evaluation Protocol

- **要点**：
    - 提出去中心化 LLM 评测协议，支持断点续评、并发请求和拥塞控制
    - 远程设置下用户无法访问 ground truth，实现数据隔离与防泄漏评测
    - 截至 2026 年 2 月已适配超过 60 个 benchmark，持续推动社区共建
- **影响**：为 LLM 评测提供了标准化、低成本、防泄漏的基础设施，有望成为社区统一评测的关键协议
- **链接**：[arxiv.org/abs/2603.01167](http://arxiv.org/abs/2603.01167)

---

## 🤖 Agent 相关论文

### 1. MOSAIC: Safe Multi-Step Tool Use Alignment for Agentic Reasoning Models

- **要点**：
    - 提出 plan → check → act/refuse 循环，将安全推理与拒绝作为一等公民动作
    - 使用基于偏好的强化学习（pairwise trajectory comparisons）进行训练，无需轨迹级标签
    - 针对 Agent 多步工具调用场景中的不可逆伤害（文件访问、凭据输入等）提供显式安全决策
- **影响**：填补了 Agent 安全对齐在多步工具使用场景中的空白，MOSAIC 框架已成为近期 Agent 安全研究的核心参考
- **链接**：[arxiv.org/abs/2603.03205](http://arxiv.org/abs/2603.03205)

### 2. MA-CoNav: Master-Slave Multi-Agent Framework with Hierarchical Collaboration for Embodied VLN

- **要点**：
    - 提出主从多 Agent 框架，有机整合高层语言指令理解、细粒度环境感知、层级任务规划、实时动作执行与经验反思学习
    - 针对长时域具身视觉-语言导航任务设计，弥补了分布式协作在视觉导航中的系统性应用缺口
    - 引入双层反思机制提升 Agent 在复杂环境中的适应能力
- **影响**：为具身 Agent 的多层协作提供了统一框架，推动 VLN 从单 Agent 向多 Agent 协作范式演进
- **链接**：[arxiv.org/abs/2603.03024](http://arxiv.org/abs/2603.03024)

### 3. Act-Observe-Rewrite (AOR): LLM Agent Self-Improving Robot Manipulation

- **要点**：
    - 提出 Act–Observe–Rewrite 框架，LLM Agent 通过视觉观察和结构化结果在试验间合成全新可执行 Python 控制器代码
    - 将完整底层电机控制实现作为 LLM 推理单元，而非依赖预定义技能库
    - 无需梯度更新、演示或奖励工程即可改进机器人操作策略
- **影响**：突破了 LLM 在具身操作中的代码生成范式，从一次性计划合成升级为迭代式底层控制优化
- **链接**：[arxiv.org/abs/2603.04466](http://arxiv.org/abs/2603.04466)

### 4. Defensive Refusal Bias: How Safety Alignment Fails Cyber Defenders (ICLR 2026)

- **要点**：
    - 基于 NCCDC 2,390 个真实案例，揭示 LLM 对合法防御性网络安全任务的拒绝偏差
    - 安全微调的前沿 LLM 在防御请求包含与攻击类似语言时倾向于拒绝协助
    - 揭示安全对齐的互补失败模式：不仅要防止滥用，也要避免拒绝合法使用
- **影响**：ICLR 2026 接收论文，为 Agent 安全对齐的精细化提供了重要实证，直接影响安全 Agent 在网络安全领域的可用性
- **链接**：[arxiv.org/abs/2603.01246](http://arxiv.org/abs/2603.01246)

---

## 🔥 GitHub 热门 Agent 项目

### 1. karpathy/autoresearch ⭐

- **简介**：Karpathy 发布的自主 AI 研究框架，让 AI Agent 在单 GPU nanochat 训练设置上自主实验过夜
- **亮点**：
    - Agent 自动修改代码、训练 5 分钟、检查结果、保留或丢弃并重复
    - 研究者不直接修改 Python 文件，而是编程 `program.md` Markdown 文件来设置自主研究组织
    - 支持多 Agent 扩展，迭代优化"研究组织代码"
- **链接**：[github.com/karpathy/autoresearch](http://github.com/karpathy/autoresearch)

### 2. Gen-Verse/OpenClaw-RL ⭐

- **简介**：通过自然对话反馈训练个性化 AI Agent 的全异步 RL 框架
- **亮点**：
    - v1 版本于 2026 年 2 月发布，支持"只需对话即可训练任何 Agent"
    - 已集成 SDFT 和 SDPO 等新方法
    - RL 服务器自动收集对话轨迹、计算奖励并训练模型
- **链接**：[github.com/Gen-Verse/OpenClaw-RL](http://github.com/Gen-Verse/OpenClaw-RL)

### 3. VoltAgent/awesome-agent-skills ⭐

- **简介**：500+ Agent 技能合集，涵盖 Claude Code、Codex、Gemini CLI、Cursor 等主流 Coding Agent
- **亮点**：
    - 收录来自官方开发团队和社区的技能
    - 兼容多种 Agent 运行时
    - 持续更新，成为 Coding Agent 技能生态的重要索引
- **链接**：[github.com/VoltAgent/awesome-agent-skills](http://github.com/VoltAgent/awesome-agent-skills)

### 4. microsoft/agent-framework ⭐ 7.1k

- **简介**：微软官方开源 Agent 框架
- **亮点**：
    - 提供标准化组件和编排机制
    - 1.1k Fork，活跃的社区生态
    - 持续发布新版本
- **链接**：[github.com/microsoft/agent-framework](http://github.com/microsoft/agent-framework)

---

## 💻 Claude Code / Coding Agent Skills

### 1. Everything Claude Code (ECC) v1.8.0 — Harness Performance System

- **要点**：
    - 2026 年 3 月发布，ECC 正式定位为 Agent Harness 性能系统
    - 新增 Hook 可靠性大修：SessionStart root fallback、Stop-phase session summaries、脚本化 Hooks
    - 新增 Harness 命令：`/harness-audit`、`/loop-start`、`/loop-status`、`/quality-gate`、`/model-route`
    - NanoClaw v2 支持模型路由、技能热加载、会话分支/搜索/导出/压缩/指标
    - 997 项内部测试全部通过
- **影响**：标志着 Coding Agent 从配置工具向性能编排系统的范式升级
- **链接**：[github.com/affaan-m/everything-claude-code](http://github.com/affaan-m/everything-claude-code)

### 2. Claude Code Ultimate Guide — Agent Teams 工作流

- **要点**：
    - 系统化文档覆盖从入门到高级用户的完整 Claude Code 使用指南
    - 包含多 Agent 团队工作流（Agent Teams）的生产级模板
    - 强调信任验证、MCP 安全（24 个 CVE、655 个恶意技能）
    - Claude Code 生成代码的逻辑错误率为人类编写代码的 1.75 倍，需要系统性验证
- **影响**：为 Claude Code 用户提供了最全面的安全实践和工作流参考
- **链接**：[github.com/FlorianBruniaux/claude-code-ultimate-guide](http://github.com/FlorianBruniaux/claude-code-ultimate-guide)

### 3. Agentlytics — 统一 Coding Agent 分析仪表盘

- **要点**：
    - 支持 Cursor、Windsurf、Claude Code、VS Code Copilot、Zed、Antigravity、OpenCode、Codex 等 12+ Agent
    - 统一分析不同 Coding Agent 的使用数据
    - 轻量级 npm 包
- **影响**：填补了跨 Coding Agent 使用分析的空白，为开发者选择和优化 Agent 工具提供数据支撑
- **链接**：[github.com/f/agentlytics](http://github.com/f/agentlytics)

### 4. SimulateDev — 编程 Agent CI 自动化

- **要点**：
    - 通过代码运行 Cursor、Windsurf、Claude Code 等 AI 编程 Agent
    - 支持端到端自动化：从特性实现到 Pull Request
    - Claude Code 支持 Headless 模式，完整集成
- **影响**：推动 Coding Agent 从交互式使用向 CI/CD 自动化集成演进
- **链接**：[github.com/saharmor/simulatedev](http://github.com/saharmor/simulatedev)

---

## 📈 趋势与信号

- **多模态原生预训练范式趋于收敛**：Beyond Language Modeling 等工作为从零开始的多模态预训练提供了实验框架，VLA 抗遗忘研究进一步验证了大规模预训练的持续学习优势
- **Agent 安全对齐进入精细化阶段**：MOSAIC 框架持续引领多步工具安全，Defensive Refusal Bias 揭示了对齐的互补失败模式，多语言对齐反噬研究挑战了以英语为中心的安全假设
- **Coding Agent 从工具走向系统**：ECC v1.8.0 定位为 Harness 性能系统，Agentlytics 提供跨 Agent 分析，SimulateDev 推动 CI 自动化，技能生态（500+ skills）持续膨胀
- **自主研究 Agent 崛起**：Karpathy 的 autoresearch 标志着 AI Agent 从辅助编码向自主科研的范式拓展

---

## 📝 术语/概念速记

| 术语 | 解释 |
| --- | --- |
| **Transfusion** | 一种多模态预训练框架，对语言使用 next-token prediction、对视觉使用 diffusion |
| **MOSAIC** | 微软提出的 Agent 安全对齐框架，结构化为 plan → check → act/refuse 循环 |
| **Iatrogenesis** | 医学术语"医源性伤害"，此处类比安全对齐本身可能在非英语语言中产生反效果 |
| **Experience Replay (ER)** | 持续学习中的经典方法，从过去经验中随机采样回放以缓解遗忘 |
| **AOR** | Act–Observe–Rewrite，LLM Agent 通过迭代重写底层控制代码改进机器人操作 |
| **Agent Harness** | 用于管理、测试和编排 Coding Agent 行为的性能系统框架 |
| **NanoClaw** | ECC 中的轻量级 Agent 运行时，支持模型路由和技能热加载 |