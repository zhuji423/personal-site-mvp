---
title: "Agent记忆与规划评测升温，时间推理与多模态few-shot基准推进，Codin"
description: "**一句话总览**：今天的信号很集中，Agent 侧继续围绕**记忆、规划与可评测性**加速细化，基础模型侧则出现**时间推理、多模态 few-shot 与几何表征 probing**三条主线，开发工具侧的重点落在 **Claude Code 的上下文治理、记忆管理与插件稳定性**。"
date: "2026-03-21"
category: "每日日报"
---

# 20260321 Agent记忆与规划评测升温，时间推理与多模态few-shot基准推进，Coding Agent上下文治理增强

Owner: AI论文抓取器
Last edited time: 2026年3月21日 10:58

<aside>
🗞️

**一句话总览**：今天的信号很集中，Agent 侧继续围绕**记忆、规划与可评测性**加速细化，基础模型侧则出现**时间推理、多模态 few-shot 与几何表征 probing**三条主线，开发工具侧的重点落在 **Claude Code 的上下文治理、记忆管理与插件稳定性**。

</aside>

<aside>
⚠️

部分条目是本轮过去 24 小时检索中最值得关注的高相关结果，**并不全部是当天首次发布**。对发布时间无法完全确认的条目，以下按“值得跟踪”而非“今日首发”处理。

</aside>

### 🧠 CV / NLP 大模型基础论文

#### 1. What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?

- 提出 **MultiTempBench**，聚焦日期计算、时区转换、时间关系抽取三类时间推理任务
- 覆盖英语、德语、中文、阿拉伯语、豪萨语，以及公历、回历、农历等不同日历体系
- 引入 **mDFR** 指标，用来量化时间表示被切碎后对推理质量的影响
- 结论指向：时间推理瓶颈不只是 tokenization，本质上还与模型内部时间表征质量有关

**影响/为什么重要**：这类工作把“LLM 时间推理不稳定”从经验问题推进到**可测量、可诊断**的问题，对多语种日程助手、规划系统、知识更新任务都很关键。

**原文链接**：[arXiv 2603.19017](https://arxiv.org/abs/2603.19017)

#### 2. FewMMBench: A Benchmark for Multimodal Few-Shot Learning

- 提出 **FewMMBench**，系统评估 MLLM 在 few-shot 条件下的能力边界
- 覆盖属性识别、时序推理等多种多模态理解任务
- 对 26 个开源 MLLM 进行 zero-shot、few-shot、CoT few-shot 对比
- 一个重要发现是：不少 instruction-tuned 模型在 zero-shot 很强，但加示例后收益有限，甚至会退化

**影响/为什么重要**：这对提示工程和 demo-based prompting 是直接提醒，说明多模态模型并非“示例越多越好”，后续需要更细的示例选择与上下文编排方法。

**原文链接**：[arXiv 2602.21854](https://arxiv.org/abs/2602.21854)

#### 3. Do Foundation Models Know Geometry? Probing Frozen Features for Continuous Physical Measurement

- 探查冻结视觉基础模型特征是否已经隐含几何理解能力
- 关注连续物理量测量，而不是只看分类或离散识别
- 核心问题从“能不能识别物体”转向“能不能理解空间与尺度”
- 属于视觉基础模型向 3D/物理世界可用性外推的重要 probing 路线

**影响/为什么重要**：如果基础模型内部已经蕴含可读出的几何信息，那么机器人、3D 感知、空间推理系统可以更多依赖 **feature probing + lightweight adaptation**，减少重训练成本。

**原文链接**：[arXiv 2603.06459](https://arxiv.org/abs/2603.06459)

### 🤖 Agent 相关论文

#### 1. MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution

- 针对 memory-augmented agents 把“构建、检索、使用”彼此割裂的问题提出新框架
- 用 **Meta-Thinker、Memory Manager、Query Reasoner** 等模块协同管理记忆循环
- 同时处理 forward path 的策略盲区与 backward path 的稀疏监督问题
- 方向上更像把 agent memory 从被动缓存升级为可调度、可自演化的系统

**影响/为什么重要**：这表明 Agent memory 的研究焦点正在从“加不加记忆”转向“**记忆循环是否有明确策略层**”，对长任务代理尤其关键。

**原文链接**：[arXiv 2603.18718](https://arxiv.org/abs/2603.18718)

#### 2. AI Planning Framework for LLM-Based Web Agents

- 基于 WebArena 分析 web agent 的规划质量，而不只看最终成功率
- 配套 794 条人工标注轨迹数据，可用于更细粒度地比对 agent 行为
- 对比 **Step-by-Step** 与 **Full-Plan-in-Advance** 两类规划范式
- 结果显示两类方法在成功率与技术指标上各有优势，说明评测维度不能单一

**影响/为什么重要**：Web agent 评测开始从黑箱式 end-to-end 成功率，转向**过程可解释指标**，这会直接影响后续 agent 架构选型。

**原文链接**：[arXiv 2603.12710](https://arxiv.org/abs/2603.12710)

#### 3. MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks

- 面向多轮、跨阶段、子任务互相依赖的 agent 场景构建记忆基准
- 覆盖网页导航、偏好约束规划、渐进式信息搜索、序列推理等任务
- 强调 agent 必须从早期行动与反馈中蒸馏经验，再用于后续决策
- 论文指出很多在长上下文 benchmark 上接近饱和的方法，在真正 agentic memory 场景下表现并不好

**影响/为什么重要**：这类结果说明“长上下文 ≠ 好记忆”，行业会更关注**跨会话经验提炼与调用**而不是单纯扩窗口。

**原文链接**：[arXiv 2602.16313](https://arxiv.org/abs/2602.16313)

#### 4. AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications

- 针对真实 agent 应用中的长程记忆问题设计评测集
- 强调 agent memory 的输入往往是持续产生的环境交互，而不是只来自人类对话
- 指出许多现有 memory system 因相似度检索的损耗而表现不足
- 配套提出更强调因果结构与工具增强检索的思路

**影响/为什么重要**：它把“记忆”从聊天上下文问题进一步推进到**应用级执行轨迹问题**，更贴近真实生产 Agent。

**原文链接**：[arXiv 2602.22769](https://arxiv.org/abs/2602.22769)

#### 5. DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints

- 关注多天旅行规划、多商品购物等长程任务
- 任务同时包含预算、时间等全局约束，以及主动信息收集需求
- 强调很多现有 benchmark 更偏局部推理，低估了全局优化难度
- 提供更接近真实世界 planning 的约束结构

**影响/为什么重要**：这代表 agent planning benchmark 正在从“局部步骤正确”转向“**全局约束最优**”，更适合评估实际可部署的规划代理。

**原文链接**：[arXiv 2601.18137](https://arxiv.org/abs/2601.18137)

### 🔥 GitHub 热门 Agent 项目

#### 1. jarrodwatts / claude-hud

- GitHub Trending 今日热度很高，约 **9.5k stars**，**今日新增约 1,068 stars**
- 是一个 Claude Code 插件，用来可视化 context usage、active tools、running agents 和 todo progress
- 强调 agent 运行状态的**可观测性**而不是只看最终输出
- 很适合复杂 coding agent 工作流调试

**影响/为什么重要**：可观测性开始成为 coding agent 的基础设施层，说明团队使用 agent 时越来越重视“看得见内部状态”。

**仓库链接**：[GitHub Trending / claude-hud](https://github.com/trending)

#### 2. langchain-ai / open-swe

- GitHub Trending 今日热门，约 **7.6k stars**，**今日新增约 635 stars**
- 定位是开源异步 coding agent
- 关键词是 **asynchronous**，意味着更适合长任务、排队执行与异步协作
- 与传统单轮 IDE 助手相比，更接近真正的软件执行代理

**影响/为什么重要**：开源社区正把 SWE agent 从 demo 推向更工程化的执行模型，异步化是一个明显信号。

**仓库链接**：[GitHub Trending / open-swe](https://github.com/trending)

#### 3. obra / superpowers

- GitHub Trending 今日极热，约 **101.5k stars**，**今日新增约 2,819 stars**
- 主打 **agentic skills framework** 与软件开发方法论
- 强调把“技能”当成可复用资产，而不是把 agent 只当一次性 prompt
- 更像是技能化、流程化的软件工程层

**影响/为什么重要**：这说明 agent 生态的重心正在从“模型能力”转向“**技能封装与团队复用**”。

**仓库链接**：[GitHub Trending / superpowers](https://github.com/trending)

#### 4. TauricResearch / TradingAgents

- GitHub Trending 今日仍然活跃，约 **34.1k stars**，**今日新增约 433 stars**
- 是一个多 Agent 金融交易框架
- 展示了多 Agent 在垂直行业中的具体落地方式
- 比通用框架更能体现 agent 在高约束环境中的执行范式

**影响/为什么重要**：垂直行业 agent 继续受到关注，说明市场开始关心“能在哪个行业先跑起来”，而不是泛泛讨论 Agent 概念。

**仓库链接**：[GitHub Trending / TradingAgents](https://github.com/trending)

### 💻 Claude Code / Coding Agent Skills

#### 1. Claude Code 2.1.74：上下文与记忆管理继续增强

- `/context` 新增更可执行的建议，可识别 context-heavy tools、memory bloat 与容量预警
- 新增 `autoMemoryDirectory`，允许配置自动记忆存储目录
- 修复流式 API buffer 未及时释放导致的内存泄漏问题
- 还修复了 managed policy、agent model 字段与 MCP OAuth 等多项稳定性问题

**影响/为什么重要**：这轮更新非常像“**把 coding agent 从能跑变成更能长期稳定跑**”，尤其适合长会话与多工具场景。

**原文链接**：[Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

#### 2. Claude Code 官方仓库：安装路径继续收敛到推荐方式

- 官方 README 明确写到 **npm 安装已弃用**
- 推荐安装方式转向 Homebrew、WinGet 等更稳定路径
- 继续强化终端、IDE 与 GitHub 三种入口的一致使用方式
- 插件体系仍被保留并作为功能扩展手段

**影响/为什么重要**：这代表 Claude Code 的交付方式更产品化，安装与升级路径正朝着更稳定、可控的方向收敛。

**原文链接**：[Claude Code README](https://github.com/anthropics/claude-code)

#### 3. ai-coding-tips：Hooks 与 allow/deny 清单成为最佳实践

- 总结了 Cursor、Claude Code 等工具中的 hooks 用法
- 推荐在自动运行模式下配置 allow/deny command lists
- 特别强调删除、下载、安装包、Git 高风险命令需要人工介入或限制
- 反映出 coding agent 的实践重点已从“怎么更强”延伸到“怎么更稳、更安全”

**影响/为什么重要**：对团队使用 coding agent 来说，**权限边界与生命周期钩子**会越来越像工程必备件，而不是高级玩法。

**原文链接**：[AI Coding Tips](https://github.com/yixin0829/ai-coding-tips)

#### 4. last30days-skill v2.9.5：研究型技能继续扩展到多社媒源

- 支持 Bluesky / AT Protocol 作为新增社会化信号源
- 新增 comparative mode，可直接做如“Cursor vs Windsurf”类并行研究
- 支持项目级 `.claude/last30days.env` 配置
- 每次运行可自动保存 briefing 到本地文档目录

**影响/为什么重要**：这类 skill 表明 coding agent 正在从“写代码”扩展到“**为开发者做持续研究与情报整合**”。

**原文链接**：[last30days-skill](https://github.com/mvanhorn/last30days-skill)

#### 5. awesome-agent-skills：跨工具技能层开始统一

- 收录 500+ agent skills，并强调可兼容 Claude Code、Codex、Cursor 等多个 harness
- 技能正在从单工具定制转向跨生态复用
- 这意味着 skill 本身正在成为新的分发单位
- 也说明开发者对“可迁移的 agent workflow 资产”需求正在上升

**影响/为什么重要**：如果技能层逐步标准化，不同 coding agent 之间的切换成本会明显下降，生态竞争将更多转向执行质量与集成体验。

**原文链接**：[awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)

### 趋势与信号

- **Agent 研究进入“记忆系统工程化”阶段**：MemMA、MemoryArena、AMA-Bench 都在说明，单靠长上下文已经不足以支撑可靠 Agent。
- **规划评测开始强调过程与全局约束**：Web agent 与 long-horizon planning benchmark 都在把注意力从结果分数转向过程质量与约束满足。
- **Coding Agent 的竞争点转向基础设施**：可观测性、hooks、权限边界、记忆目录、插件稳定性，正在成为日常生产使用的关键差异。
- **基础模型评测更关注“结构化能力”**：时间、few-shot 多模态学习、几何认知都在走向更细颗粒度的诊断框架。

### 术语 / 概念速记

- **mDFR**：用于度量时间信息碎片化对模型时间推理质量影响的指标。
- **Full-Plan-in-Advance**：先形成较完整计划再执行的 agent 规划范式，与逐步规划形成对照。
- **autoMemoryDirectory**：Claude Code 新增的自动记忆存储目录配置项，用于更明确地管理记忆落盘位置。
- **Agentic memory**：不是简单的长上下文，而是能从多轮行动、反馈与环境交互中提炼并重用经验的记忆系统。