---
title: "Agent评测基准加速演进，GUI 多模态评测走向真实流程，Coding GUI"
description: "过去 24 小时的核心信号是：**Agent 评测从“静态任务”走向“可复现的长程流程与可靠性画像”**，同时 **GUI/多模态 Agent 基准快速扩张**，以及 **Coding/GUI Agent 开源生态在 GitHub Trending 上继续聚合**。"
date: "2026-03-10"
category: "每日日报"
---

# 20260310 Agent评测基准加速演进，GUI/多模态评测走向真实流程，Coding/GUI Agent开源项目升温

Owner: AI论文抓取器
Last edited time: 2026年3月10日 08:18

### 一句话总览

过去 24 小时的核心信号是：**Agent 评测从“静态任务”走向“可复现的长程流程与可靠性画像”**，同时 **GUI/多模态 Agent 基准快速扩张**，以及 **Coding/GUI Agent 开源生态在 GitHub Trending 上继续聚合**。

---

### 🤖 Agent 相关论文（3–5 条）

1. **ProBench: Benchmarking GUI Agents with Accurate Process Information**  
    - 指向 GUI Agent 评测的关键痛点：仅看“最终界面状态”会遗漏大量过程信息（中间步骤是否正确、是否走了弯路等）。
    - 提出能更准确捕捉“过程”的评测设计，用于多步链式 GUI 操作任务。
    - 对真实移动端场景更友好，适合衡量长程交互中的稳定性与可解释失败。
    - **影响/为什么重要**：GUI Agent 若要落地，必须能被“按过程”评估与回放复现，否则难以工程化迭代。
    - 原文：[https://arxiv.org/abs/2511.09157](https://arxiv.org/abs/2511.09157)
2. **InnoGym: Benchmarking the Innovation Potential of AI Agents**  
    - 不只衡量“答对没”，还要衡量“方法是否新”。
    - 提出 *performance gain*（相对已知最优解的提升）与 *novelty*（方法差异）两类指标。
    - 配套 iGym 执行环境，强调长程、可复现评测。
    - **影响/为什么重要**：对科研/工程自动化 agent 来说，“能提出新方案”与“能稳定产出”同等关键。
    - 原文：[https://arxiv.org/html/2512.01822v2](https://arxiv.org/html/2512.01822v2)
    - 代码/框架：[https://github.com/zjunlp/igym](https://github.com/zjunlp/igym)
3. **The World Won’t Stay Still: Programmable Evolution for Agent Benchmarks**  
    - 把“环境会变化”显式建模为 agent 评测问题：工具、页面、规则变化时，agent 是否还能工作。
    - 给出可控的环境演化轨迹生成方法，用于测鲁棒性。
    - **影响/为什么重要**：现实系统里 UI、API、权限经常变，静态 benchmark 容易高估 agent 可靠性。
    - 原文：[https://arxiv.org/html/2603.05910v1](https://arxiv.org/html/2603.05910v1)
4. **AgentVista: Evaluating Multimodal Agents in Ultra-Challenging Realistic Visual Scenarios**  
    - 面向“真实视觉场景 + 工具调用”的多模态 agent 评测。
    - 强调跨域综合能力，而不是单一技能（如只做 VQA 或只做 Web 操作）。
    - **影响/为什么重要**：多模态 agent 走向现实任务时，需要在视觉理解、检索、计算、决策之间稳定闭环。
    - 原文：[https://arxiv.org/html/2602.23166v1](https://arxiv.org/html/2602.23166v1)
    - 代码：[https://github.com/hkust-nlp/AgentVista](https://github.com/hkust-nlp/AgentVista)
5. **Towards a Science of AI Agent Reliability**  
    - 提出将可靠性拆为四维：一致性、鲁棒性、可预测性、安全性，并给出 12 个可操作指标。
    - 指出“单一成功率”会掩盖真实失败模式。
    - **影响/为什么重要**：给生产级 agent 的评测提供更接近工程的指标体系。
    - 原文：[https://arxiv.org/html/2602.16666v1](https://arxiv.org/html/2602.16666v1)

---

### 🧠 CV / NLP 大模型基础论文（3–5 条）

> 过去 24 小时内，本轮抓取到的“新论文”里，和 **推理加速/注意力内核** 直接相关的公开条目偏少；但从近两天信号看，社区讨论依旧围绕“更贴近硬件的算子协同设计”展开（如 FlashAttention 系列思路）。
> 

（若你希望我把范围从 24h 放宽到 72h，我可以补齐更完整的加速/attention 新作列表。）

---

### 🔥 GitHub 热门 Agent 项目（3–5 条）

1. **alibaba/page-agent**（in-page GUI agent）  
    - 在网页内用自然语言驱动 GUI 操作的 Agent。
    - **亮点**：更贴近“浏览器里干活”的真实场景。
    - 仓库：[https://github.com/alibaba/page-agent](https://github.com/alibaba/page-agent)
2. **NousResearch/hermes-agent**  
    - “可成长”的 agent 项目，近期热度上升。
    - **亮点**：更偏框架化的 agent 形态，利于二次开发与集成。
    - 仓库：[https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
3. **msitarzewski/agency-agents**  
    - 多角色“AI agency”组合（前端、社区、评审等角色）。
    - **亮点**：强调角色分工与交付物，适合参考其工作流设计。
    - 仓库：[https://github.com/msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
4. **karpathy/autoresearch**  
    - 用 agent 在单卡训练实验上做自动化 research loop（改代码→训练→比较→保留/丢弃）。
    - **亮点**：把“实验迭代”显式产品化，适合研究团队借鉴。
    - 仓库：[https://github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)

（Trending 页面快照：[https://github.com/trending）](https://github.com/trending）)

---

### 💻 Claude Code / Coding Agent Skills（3–5 条）

1. **alirezarezvani/claude-skills**  
    - 面向 Claude Code / Codex 等的技能与插件集合。
    - **亮点**：更接近“可安装的技能市场”模式。
    - 仓库：[https://github.com/alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
2. **google-gemini/gemini-cli（讨论区）**：Behavioral Eval Framework / Cross-agent benchmarking  
    - 围绕 CLI agent 的行为评测框架：覆盖、分类法、跨 agent 对比。
    - **亮点**：更“工程化”的 eval 规划，适合作为内部评测体系搭建参考。
    - 讨论：[https://github.com/google-gemini/gemini-cli/discussions/19604](https://github.com/google-gemini/gemini-cli/discussions/19604)

---

### 趋势与信号

- **评测从“终态正确”→“过程可复现 + 环境可演化 + 可靠性画像”**（GUI Agent、长程交互、动态环境成为关键变量）。
- **多模态 Agent 评测继续往“真实视觉场景 + 工具链闭环”推进**，基准更难但更接近落地。
- **开源生态继续聚合在“GUI/网页操作 agent + 多角色工作流 + coding skills 插件化”三条线。**

### 术语/概念速记

- **Process-aware evaluation（过程感知评测）**：不只看最终结果，还要记录并判定中间步骤是否正确。
- **Evolving benchmarks（演化式基准）**：评测环境随时间变化，检验 agent 的鲁棒性与适应能力。