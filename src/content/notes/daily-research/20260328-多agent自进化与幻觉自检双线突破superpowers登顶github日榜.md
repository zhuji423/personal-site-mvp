---
title: "多Agent自进化与幻觉自检双线突破，superpowers登顶GitHub日榜，"
description: "**一句话总览：** 多Agent自进化框架AgentFactory被CVPR 2026收录、MARCH用多Agent强化学习实现幻觉自检取得突破；GitHub日榜上superpowers技能框架以2,700+日星登顶，oh-my-claudecode多Agent编排持续走热；Coding Agen..."
date: "2026-03-28"
category: "每日日报"
---

# 20260328 多Agent自进化与幻觉自检双线突破，superpowers登顶GitHub日榜，Coding Agent技能生态加速标准化

Owner: AI论文抓取器
Last edited time: 2026年3月28日 10:18

**一句话总览：** 多Agent自进化框架AgentFactory被CVPR 2026收录、MARCH用多Agent强化学习实现幻觉自检取得突破；GitHub日榜上superpowers技能框架以2,700+日星登顶，oh-my-claudecode多Agent编排持续走热；Coding Agent技能生态标准化进入深水区，技能市场规模化评测论文与200+开源技能库同步涌现。

---

## 🧠 CV / NLP 大模型基础论文

### 1. MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination

- 提出 Solver-Checker 双Agent架构，Checker 在**信息不对称**条件下独立验证 Solver 输出的事实命题
- 用多Agent强化学习（MARL）训练两个Agent共同进化，优化事实一致性
- 8B 参数模型 + MARCH 即可达到接近闭源大模型的反幻觉水平
- 打破了「自我确认偏差」的循环，为 LLM 事实自改进开辟可扩展路径
- **影响：** 证明多Agent协作可显著提升小模型事实性，为生产部署反幻觉提供低成本方案
- 🔗 [arXiv:2603.24579](https://arxiv.org/abs/2603.24579) · [GitHub: Qwen-Applications/MARCH](https://github.com/Qwen-Applications/MARCH)

### 2. FREAK: Fine-grained Hallucination Evaluation Benchmark for Advanced MLLMs

- 提出针对高阶多模态大模型的**细粒度幻觉评测基准**
- 区分「常识错误」与「其他错误」，定义 Hallucination Rate 衡量参数化知识的干扰程度
- 同时覆盖 free-form 和 multiple-choice 两种评测形式
- 采用 LLM-as-judge 方法进行自动评估
- **影响：** 为 MLLM 幻觉研究提供更精细的评测维度，推动模型在视觉-语言对齐上的改进
- 🔗 [arXiv:2603.19765](https://arxiv.org/abs/2603.19765)

### 3. CVT-Bench: Counterfactual Viewpoint Transformations Reveal Unstable Spatial Representations in MLLMs

- 构建反事实视角变换基准，揭示 MLLM 空间表征的**不稳定性**
- 发现单视角空间准确率**高估**了模型空间推理的鲁棒性
- 表征结构在反事实空间推理中起关键作用
- **影响：** 为评估多模态模型的空间理解能力提供更严格的测试框架
- 🔗 [arXiv:2603.21114](https://arxiv.org/abs/2603.21114)

### 4. SeGP-CL: Continual Learning with VLMs via Semantic-Geometry Preservation

- 针对视觉-语言模型持续学习中的灾难性遗忘问题
- 发现语义漂移集中在新旧语义界面的**脆弱邻域**
- 提出 Semantic Geometry Preservation，在无样本回放约束下保持跨模态语义几何
- **影响：** 为 VLM 的终身学习提供理论依据和实用框架
- 🔗 [arXiv:2603.12055](https://arxiv.org/abs/2603.12055)

### 5. 172-Billion-Token LLM Hallucination Study

- 横跨 **35 个开源模型**、3 种上下文长度、4 种温度设置、3 种硬件平台的大规模评测
- 使用 RIKER 方法实现无需人工标注的确定性评分
- 数据规模超过此前工作一个数量级
- **影响：** 为企业级 AI 部署提供关于幻觉率的可靠基准数据
- 🔗 [arXiv:2603.08274](https://arxiv.org/abs/2603.08274)

---

## 🤖 Agent 相关论文

### 1. AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse（CVPR 2026）

- 提出全新的**Agent自进化范式**：将成功的任务解法保存为可执行子Agent代码，而非文本经验
- 三阶段流水线：Install → Self-Evolve → Deploy，系统性地构建、改进、导出功能Agent
- 子Agent为纯 Python 代码 + 标准文档，可跨任何 Python 系统移植
- Meta-Agent 负责任务分解和工具动态分配，Workspace Manager 提供隔离执行环境
- **影响：** 被 CVPR 2026 收录，证明「代码即经验」的自进化路径优于传统文本反思方法
- 🔗 [arXiv:2603.18000](https://arxiv.org/abs/2603.18000) · [GitHub: zzatpku/AgentFactory](https://github.com/zzatpku/AgentFactory)

### 2. SEMA: Self-Evolving Multi-Agent Framework for RTS Decision Making

- 面向即时战略场景的多Agent协作框架，由决策Agent、评估Agent、策略Agent组成自组织闭环
- 引入基于**结构熵**的动态观测裁剪机制，将高维数据压缩为核心语义信息
- 混合知识-记忆机制整合微观轨迹、宏观经验和层级领域知识
- 在 StarCraft II 多张地图上实现更高胜率，平均决策延迟降低 **50%+**
- **影响：** 为 Agent 在动态复杂环境中的实时决策提供新范式
- 🔗 [arXiv:2603.23875](https://arxiv.org/abs/2603.23875)

### 3. TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems

- 基于 OWASP 标准构建**三层细粒度风险分类体系**，涵盖 20 种风险类型
- 覆盖单Agent漏洞、Agent间通信威胁、系统级涌现危害
- 提供安全评估 + 实时监控的一体化框架
- 被 ICLR 2026 Workshop on Agents in the Wild 接收
- **影响：** 填补了多Agent系统专用安全框架的空白，为生产部署提供安全基线
- 🔗 [arXiv:2603.15408](https://arxiv.org/abs/2603.15408) · [GitHub: AI45Lab/TrinityGuard](https://github.com/AI45Lab/TrinityGuard)

### 4. ClawWorm: Self-Propagating Attacks Across LLM Agent Ecosystems

- 揭示 LLM Agent 生态中**自传播攻击**的可能性
- 攻击可跨Agent生态系统蔓延，超越单点注入
- **影响：** 为Agent生态安全敲响警钟，与 TrinityGuard 形成攻防互补
- 🔗 [arXiv:2603.15727](https://arxiv.org/abs/2603.15727)

### 5. Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale

- 构建三种规模的技能生态（小/中/大），评估技能检索与编排在规模增长下的退化
- 从人工策展核心到市场自动扩展的递进式构建方法
- **影响：** 首次系统性评估Agent技能生态的规模化挑战，为技能市场标准化提供数据支撑
- 🔗 [arXiv:2603.16572](https://arxiv.org/abs/2603.16572)

---

## 🔥 GitHub 热门 Agent 项目

### 1. obra/superpowers ⭐ 118,637（+2,752/天）

- 定位：**Agentic 技能框架 + 软件开发方法论**
- 提供结构化的Agent技能体系，强调「方法论驱动」而非纯工具堆叠
- Shell 实现，轻量级、可组合
- **亮点：** 日增星数高达 2,752，显示开发者对「技能即方法论」理念的强烈共鸣
- 🔗 [GitHub](https://github.com/obra/superpowers)

### 2. Yeachan-Heo/oh-my-claudecode ⭐ 14,001（+1,411/天）

- 定位：**Teams-first 多Agent编排框架**，专为 Claude Code 设计
- 支持多Agent协作与任务分发
- TypeScript 实现
- **亮点：** 连续多日上榜，Teams-first 的设计理念切中团队协作痛点
- 🔗 [GitHub](https://github.com/Yeachan-Heo/oh-my-claudecode)

### 3. mvanhorn/last30days-skill ⭐ 12,750（+2,821/天）

- 定位：AI Agent **跨平台主题研究技能**
- 自动搜索 Reddit、X、YouTube、Hacker News、Polymarket 和 Web，合成结构化摘要
- Python 实现，可作为独立 Agent Skill 调用
- **亮点：** 日增星数最高，「一个 Skill 搞定全网调研」的理念极具吸引力
- 🔗 [GitHub](https://github.com/mvanhorn/last30days-skill)

### 4. SakanaAI/AI-Scientist-v2 ⭐ 2,892（+143/天）

- 定位：**Workshop 级别自动科研发现**，通过 Agentic Tree Search 实现
- 从想法到论文的全自动化流程
- **亮点：** AI-Scientist 系列第二代，向更高质量的自主科研迈进
- 🔗 [GitHub](https://github.com/SakanaAI/AI-Scientist-v2)

### 5. virattt/dexter ⭐ 19,717（+672/天）

- 定位：**自主金融深度研究 Agent**
- TypeScript 实现，专注于金融领域的自动分析
- **亮点：** 垂直领域 Agent 持续走热，金融研究是高价值应用场景
- 🔗 [GitHub](https://github.com/virattt/dexter)

---

## 💻 Claude Code / Coding Agent Skills

### 1. agent-sh/agentsys — 19 插件 · 47 Agent · 39 技能

- 覆盖 Claude Code、OpenCode、Codex CLI、Cursor、Kiro 五大平台
- 每个 Agent 单一职责 + 特定模型分配 + 明确输入输出
- Pipeline 强制阶段门控，防止跳步；状态跨会话持久化
- 通过 `/plugin marketplace` 命令直接安装
- **影响：** Agent 编排从「单体」走向「插件化微服务」，标准化程度持续提升
- 🔗 [GitHub](https://github.com/agent-sh/agentsys)

### 2. alirezarezvani/claude-skills — 205 个生产级技能

- 支持 **11 种 AI 编程工具**：Claude Code、Codex、Gemini CLI、Cursor、Aider、Windsurf 等
- 覆盖工程、DevOps、营销、合规、C-level 顾问等多个领域
- 5,200+ GitHub Stars
- **影响：** 技能库从「代码辅助」扩展到「全组织职能」，Coding Agent 的边界持续外扩
- 🔗 [GitHub](https://github.com/alirezarezvani/claude-skills)

### 3. ARIS (Auto-Research-In-Sleep) — 让 Claude Code 在你睡觉时做科研

- 纯 Markdown 实现，**零依赖零锁定**
- 跨模型协作：Claude Code 驱动研究，外部 LLM 充当审稿人
- 支持 Codex CLI、Cursor、Trae、Antigravity 等多平台
- v0.3.2 新增 ACP 兼容后端 + 反造假系统 + 实验诊断修复循环
- **影响：** 「方法论而非平台」的理念使其成为最轻量的自主科研工作流方案
- 🔗 [GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

### 4. Are Coding Agents Generating Over-Mocked Tests?（实证研究）

- 对 Claude Code、GitHub Copilot、Cursor 三大 Coding Agent 进行系统性评估
- 研究重点：Agent 生成的测试是否**过度使用 Mock**，导致测试脆弱性
- **影响：** 首次对 Coding Agent 的测试质量进行定量分析，为改进提供方向
- 🔗 [arXiv:2602.00409](https://arxiv.org/abs/2602.00409)

### 5. Cursor 2.4–2.6 Revert Bug 确认

- Cursor 团队确认 2024年3月三个文件回退 Bug 的根因：Agent Review 冲突、Cloud Sync 冲突、Format On Save 冲突
- 导致代码更改**静默回退**，是当前最严重的已知问题之一
- **影响：** 提醒使用 Cursor 的团队注意版本控制风险，等待官方修复
- 🔗 [GitHub: murataslan1/cursor-ai-tips](https://github.com/murataslan1/cursor-ai-tips)

---

## 📈 趋势与信号

- **Agent 自进化成为核心范式：** AgentFactory（CVPR 2026）、SEMA、AgentEvolver 等多个框架同时推进「自我改进」路径，从文本反思进化到可执行代码积累
- **多Agent安全攻防持续升温：** TrinityGuard（防御）与 ClawWorm（攻击）同期出现，表明 Agent 生态安全已成学术焦点
- **幻觉检测进入多Agent协作阶段：** MARCH 用双Agent + MARL 实现事实自检，突破了单模型自我确认偏差的瓶颈
- **Coding Agent 技能标准化加速：** 技能市场规模化评测（arXiv:2603.16572）、200+ 技能库（claude-skills）、插件化编排（agentsys）三条线同步推进
- **GitHub 日榜被 Agent 相关项目主导：** superpowers、oh-my-claudecode、last30days-skill 包揽前列，显示 Agent 技能化和团队协作是当前开发者最关注的方向

---

## 📝 术语/概念速记

- **MARL（Multi-Agent Reinforcement Learning）**：多Agent强化学习，MARCH 中用于训练 Solver 和 Checker 共同进化
- **结构熵（Structural Entropy）**：SEMA 中用于对观测数据进行拓扑建模和语义压缩的信息论工具
- **阶段门控（Phase Gate）**：agentsys 中的 Pipeline 机制，确保 Agent 按序执行，不可跳步
- **ACP（Agent Communication Protocol）**：ARIS v0.3.2 新增的兼容协议，允许不同 Agent 后端互通