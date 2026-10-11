---
title: "1. 背景与目标"
description: "使用 Claude Code（Ducc）进行需求开发实践后的一些心得"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\使用 Claude Code（Ducc）进行需求开发实践后的一些心得.md"
---
使用 Claude Code（Ducc）进行需求开发实践后的一些心得

#### 🧑‍🏫 案例作者：[@常鑫鹏](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、研发全流程、运维
#### 🔧 使用工具：Ducc
#### 📒 案例概要：如何使用ducc进行一次完整的需求开发，以及集成skills和Harness Engineering搭建到Ai Coding的技巧、实践与心得
# 1. 背景与目标
很多团队都在用 AI Coding 工具做研发提效，但把 AI Coding 放进公司老项目、多仓项目、复杂链路项目后，很快会发现一个现实问题：

AI 会写代码，不代表它真的懂你的项目。

它可能改对一个函数，却看不清整条调用链；可能生成一个 patch，却不知道会不会误伤上下游；可能知道某个类是做什么的，却说不清它在业务流程里到底扮演什么角色。

老项目里真正难的，从来不是"怎么让 AI 多写一点代码"，而是怎么把项目环境搭到足够清晰，让 AI 不只是会写，而是真的能稳定地参与交付。

这也是 OpenAI 在 Harness Engineering 中强调的方向：当 agent 越来越像主要执行者，工程师的工作会从"亲手写每一行代码"转向"设计环境、明确意图、建立反馈闭环"，让 agent 在一个更可靠的系统里工作。OpenAI 后来不再依赖大而全的单文件说明，而是转向"短 AGENTS.md + 结构化 docs/ 知识库"的方式。

本文以公司里的 Ducc（Claude Code 场内版）为 AI Coding 工具，结合 UGC 一次新增需求开发实践，把实践的过程遇到的想法、坑抽象成几个个问题：

1. 想让 AI Coding 工具完整做完一次需求开发，前面到底要准备什么？
2. 怎样让它生成出来的代码更可控、更完整，也更健壮？
3. 怎样把业务知识、设计规范、编码特性沉淀下来，变成下一次还能继续复用的资产？
4. 除了 CLAUDE.md 之外，如何结合Skill、Hooks等Claude Code的关键能力 和 Harness Engineering，把老项目逐步搭成一个真正适合 agent 持续工作的环境？

# 2. 为什么选择 Ducc，而不是 Zulu
选择 Ducc，不是因为它"绝对最好"，而是因为它更适合做深入、持续、可工程化的实践。

对老项目需求开发来说，Ducc 的几个优势比较实际：

* 模式选择更多，适合不同开发阶段切换
* 与 Claude Code 的交互方式基本一致，外部社区经验更容易迁移
* 定制空间更大，可以配 hooks、skills、MCP，逐步沉淀成团队自己的 AI Coding 工作流
* 更适合从"会写代码的助手"演进到"可持续驯化的开发代理环境"

Anthropic 官方对 Claude Code 的定位是它是一个 agentic coding tool，能够读代码库、改文件、跑命令，并与开发工具集成来完成工程任务。真正影响效果上限的，往往不是模型是否"更聪明一点"，而是你有没有把环境搭好。

# 3. 核心理念：老项目里，真正难的不是编码，而是上下文、流程和结构
在老项目里做新增需求，常见痛点并不新鲜：

* 代码历史复杂、隐含约束多
* 测试不齐全、验证成本高
* 多仓依赖链长，一个改动可能牵动一串逻辑或者服务
* 真正决定实现方式的信息，散落在 Wiki、IM、历史提交和老同学脑子里

所以，Claude Code / Ducc 想在老项目里稳定发挥，不能只靠"让它多看点代码"，而是起码要先解决四类问题。

### 3.1 固化项目基线认知
这里Claude Code官方文章中推荐使用CLAUDE.md。

CLAUDE.md 管的是：这个仓库怎么跑、怎么测、有哪些坑、哪些规则不能违反。

Anthropic 官方最佳实践指出，CLAUDE.md 是 Claude Code 会在每次会话开始时读取的特殊文件，适合放那些模型无法仅凭代码推断出来的内容，比如 Bash 命令、风格约束、工作流规则、项目独有架构决策、环境变量怪癖和常见坑。因为这个文件每个会话都会加载，所以只放"广泛适用、低频变化"的内容。

### 3.2  固化工程方法论
个人推荐Superpowers或者类似的开源或者自己创建的SKILL

Superpowers 管的是：这次需求应该按什么节奏推进，而不是拿到一句话需求就直接开写。

Superpowers 官方 README 把它定位成一个 agentic skills framework & software development methodology。它不是简单的快捷指令合集，而是一套让 AI 遵循现代软件工程流程的方法框架。README 里的基础工作流：先 brainstorming，再 writing-plans，然后进入执行、review 和后续闭环。

### 3.3 补足结构化代码理解
这里推荐GitNexus，**为代理上下文构建神经系统。**

> **Building nervous system for agent context.**
> Indexes any codebase into a knowledge graph — every dependency, call chain, cluster, and execution flow — then exposes it through smart tools so AI agents never miss code.
GitNexus 管的是：代码到底挂在哪条流程上、改这里会影响谁、哪些模块表面相关但其实不在同一条主链路上。

按照 GitNexus 官方 README，它的 CLI + MCP 模式会为仓库建立本地知识图谱，并暴露 query、context、impact、detect_changes、rename、cypher 等能力，支持多仓注册、自动生成 AGENTS.md / CLAUDE.md、安装 skills，以及为 Claude Code 注册 hooks。它的 Web UI 适合快速探索，但复杂项目更推荐 CLI + MCP。CLI+MCP的模式非常适合DUCC

### 3.4 用 Harness Engineering 把这些层织成系统
Harness Engineering：为Agent搭建一个合适的稳定的可持续运行的环境。

Harness Engineering 管的是：别让这些东西只是零散技巧，而要把它们编织成一个 agent 能长期稳定工作的工程系统。

OpenAI 的核心观点：在 agent-first 的世界里，真正有效的做法不是"不断换 prompt"，而是把上下文、工具、约束、评测和反馈闭环做成环境。对于 workflow 级问题，OpenAI 还建议使用可复现评测、trace grading 和 datasets 来持续迭代 agent 质量。

用一句话概括这四层分工：

CLAUDE.md 管规则，Superpowers 管流程，GitNexus 管结构，Harness 管系统。

## 4. 准备工作
### 4.1 安装与进入 Ducc
这部分比较直接：

* 安装 comate。目前在公司网络环境下，安装完 comate 后通常会自动安装 Ducc
* 拉取业务相关代码仓库到一个 workspace 下。多仓协同会顺滑很多，尤其适合后续跨仓需求分析、结构查询和多仓改动

这一步看起来像普通准备，但实际上很关键。一旦进入多仓协同场景，AI Coding 的效果很大程度上取决于：它是不是处在一个完整、连续、可跨仓检索的工作空间里。

### 4.2 在每个仓库生成 CLAUDE.md
重要：每个仓库都建议生成 CLAUDE.md，且后续要持续精化。

Anthropic 官方最佳实践强调，CLAUDE.md 用来放 Claude 猜不到的命令、风格和规则，而 /init 的价值在于：它会分析代码库结构、识别构建系统和测试框架，生成一个可以持续精化的 starter 文件，而不是让用户从空白文档胡写。

方法一：IDE 插件方式（推荐）

1. 进入需要生成 CLAUDE.md 的仓库
2. 右上角 Ducc 图标 → 打开交互窗口
3. 输入 /init 回车
4. 允许写入后生成 CLAUDE.md

方法二：终端 CLI 方式

1. 终端进入项目目录
2. 执行 ducc 进入交互界面
3. 输入 /init 回车
4. 流程与插件方式一致

### 4.3 在复杂老项目里，同时把 GitNexus 装上
如果项目有这些特征：

* 仓库大
* 目录深
* 调用链长
* 模块间耦合明显
* 新需求经常牵出历史链路
* 经常需要回答"这个改动到底会影响谁"

那我会建议在 CLAUDE.md 之外，再加上一层 GitNexus。

官方推荐的快速开始方式：

```
npx gitnexus analyze
npx gitnexus setup
```
analyze 会索引代码库、安装 agent skills、注册 Claude Code hooks，并创建上下文文件；setup 用来给编辑器配置全局 MCP。对于多仓 workspace，建议每个仓库都执行一次 analyze，然后统一执行一次 setup。GitNexus 的设计是每个仓库存索引到 .gitnexus/，再通过 ~/.gitnexus/registry.json 做全局注册，一个 MCP server 就能服务多个仓库。

### 4.4 准备好与本次任务相关的详细上下文
Claude Code / Ducc 想真正做完一个需求，不能只知道一句需求描述。它最好还能看到：

* 需求背景与验收标准
* 涉及的上下游系统
* 第三方 API 文档
* 数据库 DDL
* 历史相似需求
* 关键链路说明
* 业务术语解释
* 风险点和边界条件

我的建议一直很直接：把这些内容整理成规范 Markdown，直接放进 workspace。

因为对 agent 来说，看不见的知识就等于不存在。OpenAI 的文章本质上也是这个意思：工程师要把 agent 缺失的信息前置到环境里，而不是期待模型自己脑补。

### 4.5 先敲定一份技术方案，再让 AI 编码
作为 RD，我们都清楚：一次需求开发里，编码本身往往不是占用时间最多的环节。真正决定上线质量、稳定性和后续维护成本的，通常是最开始的技术方案，以及中间的 trade-off。

在 AI Coding 里，我更推荐这三种思路中的第三种：

* 自己已经非常了解需求和历史代码，先写详细方案，再让 AI 按方案执行
* 把需求和上下游信息交给 AI，让它先产出方案
* 先定大方向，再和 AI 一起把细节 trade-off 一点点磨出来

这一层最适合和 Superpowers + GitNexus 组合使用：

* 先用 brainstorming 做需求澄清和方案推演
* 再让 GitNexus 做结构化摸底和影响面分析
* 然后用 writing-plans 输出实施计划

这样生成出来的方案，通常比"一句需求直接问怎么做"要稳得多。

## 5. 为什么需要 CLAUDE.md
### 5.1 CLAUDE.md 的本质作用
CLAUDE.md 最大的价值，不是"放很多知识"，而是让 agent 在每次会话开始时，先拥有一份正确的项目基线认知。

它适合放：

* Claude 无法从代码直接推断出来的 Bash 命令
* 代码风格与工作流规则
* 测试命令、推荐 runner、常见失败修复方式
* 项目独有架构决策、环境变量怪癖、常见坑

Anthropic 的最佳实践对这一点讲得很清楚。

### 5.2 /init 为什么重要
/init 的价值在于：它不是让你从空白开始胡写，而是先理解仓库，再生成一个 starter 版本。对老项目来说，这特别重要，因为老项目最麻烦的就是各种"默认大家都知道，实际上新人和 AI 都不知道"的隐含事实。

### 5.3 CLAUDE.md 写作准则
建议包含：

* Claude 猜不到的命令 / 入口
* 与默认不同的代码风格与提交规范
* 测试指令、推荐 runner、常见失败修复方式
* 项目架构关键决策、隐含约束
* 环境变量 / 开发机怪癖
* "不显而易见"的坑

建议排除：

* Claude 读代码就能得到的信息
* 大段 API 文档原文
* 经常变化的内容
* 冗长教程、逐文件介绍代码库

### 5.4 @ 引用与多层 CLAUDE.md
Anthropic 官方也建议用引用方式把 CLAUDE.md 做成入口，例如引用 README、架构文档、依赖文件，而不是把所有东西直接堆进去。多层 CLAUDE.md 也适合 monorepo 或多目录工程。

### 5.5 保持 CLAUDE.md 的实时性
每次需求完成并上线后，都建议回头检查：

* 这次踩过的坑
* 这次补过的命令
* 这次确认过的架构约束

是不是值得补回 CLAUDE.md。但要注意，不是所有东西都适合写进去。更复杂、更低频、流程型的知识，更适合放到 skills、hooks 或 docs/ 中。

### 5.6 CLAUDE.md 不是百科全书，而是入口
这点很重要。OpenAI 在 Harness Engineering 里已经踩过这个坑了：大而全的单文件会快速过时、上下文负担重、重点不突出。所以后来转向"短 AGENTS.md + 结构化 docs/"的做法。这个经验对 CLAUDE.md 同样适用。



一句话总结：CLAUDE.md 不是知识库，它是导航页。

## 6. 推荐的目录结构与协同方式
### 6.1 单个项目
单项目至少建议有：

* ./CLAUDE.md
* ./ARCHITECTURE.md
* 与本次需求相关的上下文文档
* docs/exec-plans/
* docs/references/

如果结构复杂，额外加上 GitNexus 索引。

### 6.2 多老项目、多仓库
目标是：在一个 workspace 里同时改多个仓库时，规则不冲突、上下文不混乱、流程可复用、结构可查询。

更推荐这种模式：

* 每个仓库一个轻量 CLAUDE.md
* 公共上下文和业务资产放进 docs/ 或共享目录
* 高频流程沉淀为 skills
* 必须发生的动作沉淀为 hooks
* 复杂仓库用 GitNexus 建索引和结构查询
* 关键需求和失败样本沉淀到 evals

如果把这套东西画成工作分工：

* CLAUDE.md：项目规则和入口
* Superpowers：过程编排和工程节奏
* GitNexus：代码结构理解和影响面分析
* hooks：关键动作自动化
* evals：质量闭环

## 7. 从 CLAUDE.md 走向 Harness Engineering
很多团队在引入 AI Coding 时，停在 CLAUDE.md + prompt + skills 这一步，就已经觉得够用了。但如果场景是老项目、多仓、链路长、验证重，那么只做到这里通常还不够。

一旦业务负责度变高涉及服务变多，迟早会遇到这些问题：

* AI 会写，但不一定会自己验证
* AI 会改，但不一定会先看影响面
* AI 这次能做成，下次换个会话又得重新摸索
* AI 成功或失败，团队说不清到底为什么

这时候，就应该把视角从"prompt engineering"切到 harness engineering。

 harness 简单点来说：它就是一整套让 agent 能稳定工作的工程环境。

在老项目里，我会把一个相对完整的 harness 拆成七层。

### 7.1 上下文层
解决的是：AI 知不知道自己在什么项目里干活。

包括：

* CLAUDE.md
* ARCHITECTURE.md
* 需求上下文
* 历史变更记录
* 活跃中的技术方案
* 上下游接口说明

### 7.2 流程层
解决的是：AI 知不知道应该按什么节奏推进。

这一层最适合由 Superpowers 承担。例如：

* brainstorming：先澄清问题、推演设计、识别 trade-off
* writing-plans：把需求转成分步骤实施计划
* executing-plans：按检查点推进实现
* requesting-code-review / receiving-code-review：把 review 前后动作结构化

它解决的不是"AI 会不会写"，而是"AI 会不会按正确的节奏写"。

### 7.3 结构层
解决的是：AI 能不能不只是搜到代码，还能看懂结构关系。

这一层更适合由 GitNexus 承担，因为它提供的是：

* 功能簇
* 执行流程
* 符号级 360 度上下文
* blast radius 分析
* diff 级影响分析
* 多仓统一索引和 MCP 接入

### 7.4 工具层
解决的是：AI 能不能真正动手干活。

包括：

* 文件检索与编辑
* build / test / lint
* git diff / git log
* 数据库 DDL / 测试数据生成
* 日志和链路查询
* GitNexus 的 query/context/impact/detect_changes

OpenAI 在 Harness Engineering 里提到，他们会把 UI、日志、指标、trace 都暴露给 agent，让它在隔离环境里自己查、自己跑、自己验证。

### 7.5 约束层
解决的是：AI 会不会乱来。

不要只靠 prompt 写"请谨慎修改"，而要尽量把规则做成机器能检查的东西，比如：

* 哪些目录不能改
* 哪些层不能跨层依赖
* 哪些改动必须补测试
* 哪些命令不能执行
* 哪些文件必须配套更新

### 7.6 观测层
解决的是：能不能看见 AI 做了什么、为什么成功、为什么失败。

至少要保留：

* 工具调用记录
* 开发日志
* 输出产物
* 测试结果
* diff
* 错误原因
* review 记录

### 7.7 评测层
这是最容易被忽略的一层。

很多团队对 AI Coding 的评估停留在"这次好像做成了"，但 OpenAI 明确建议要用可复现评测、trace grading 和 datasets 去持续迭代 agent 质量。

放到 AI Coding 场景里的一些启发是逐步沉淀成如下的内容：

* 给定需求上下文，是否能生成合理计划
* 给定历史代码，是否能找到正确改动点
* 给定 bug，是否能生成最小修复
* 给定 DDL，是否能生成可联调数据
* 给定 diff，是否能识别影响面和风险点

ducc是可以更换模型的，但是一个适合自己好用的AI Coding工具应该是：模型 + Context + Skills + hooks + toolchain + 验证流程，这整套 harness 到底稳不稳。

## 8. 演示 Demo：原生 PLAN 模式
下面这部分主要是想把原生 PLAN 模式真正拆成一条可执行路径。

### 8.1 需求说明与验收标准
以这次 UGC 需求为例：

* 业务背景：对 Meg 工单进行付费加严审核
* 验收标准：保证 Meg 工单命中风险类目后，在进行 MPF 批次加工平台灌入时有对应的风险提示

这类需求看起来不算特别大，但它有几个典型特点：

* 横跨多个仓库
* 牵涉历史链路
* 对命中条件、提示词展示位置、批次加工链路都有依赖
* 不是简单"加个字段"就能结束

这种需求，反而非常适合用来检验 AI Coding 的真实能力。

### 8.2 Workspace 展示
推荐在 workspace 中明确摆出几类资产：

* 参与改动的仓库
* 每个仓库的 CLAUDE.md
* 需求背景文档
* 验收标准文档
* 历史相似需求和关键改动记录
* API 文档 / DDL / 表结构
* 一份随时更新的开发日志

这一层的核心，不是"信息越多越好"，而是：给 AI 尽可能多的"结构化相关上下文"。

### 8.3 生成计划：原生 PLAN 模式
这一步的目标不是立刻改代码，而是生成一份 review 后觉得没问题的技术方案和实施计划。

推荐输入包括：

* 基本要求
* 验收标准
* 关键历史变更
* ToDo 项
* 关键文件
* 表结构 / 接口定义 / 风险链路说明

输出最好至少包含：

* 需求理解
* 涉及模块
* 核心设计思路
* 关键改动点
* 风险点
* 验证清单
* 实施顺序
* 待确认项

### 8.4 最终产物
原生 PLAN 模式下，我建议至少沉淀这些产物：

* 技术方案 Markdown
* 实施计划 Markdown
* 风险点清单
* 开发日志
* 验证清单

这样后面无论是自己 review，还是让 AI 继续执行，路径都会清晰很多。

### 8.5 执行单测
执行单测时，不要只写"跑单测"，而要工程化一点，明确要求AI Coding工具：

* 跑哪些测试
* 哪些测试是新增的
* 哪些回归点必须过
* 哪些失败是已知噪音，哪些失败必须修复

### 8.6 生成测试数据
这本来就是 AI Coding 的强项。

简单的方案是把 DDL、关键字段约束、业务判定规则放进 workspace，更好的方案是通过 MCP 或者工具的形式封装数据库访问，并将和业务相关的领域描述封装成SKILL，那么让 AI在生产测试数据进行联调时会加载SKILL，让ducc实现“Text-To-Sql-To-Test”的流程。

但建议多加一道约束：数据不是只要"能插入"就行，而是必须满足需求链路验证所需的最小充分条件。

## 9. 演示 Demo：PLAN + Skill + GitNexus 模式
相比原生 PLAN 模式，个人更推荐的：PLAN + Skill + GitNexus。

因为这三者解决的是三种不同问题：

* PLAN：把目标变清楚
* Skill（如 Superpowers）：把推进节奏和方法论变标准
* GitNexus：把代码结构和影响面看清楚

### 9.1 方案生成前：先用 Superpowers 拉齐思路
先触发 brainstorming（更推荐将brainstorming的思考流程替换成个人平时编写方案时的流程和方法论），不要一上来就让 AI 写代码。

这一阶段的目标是：澄清需求、补齐上下文缺口、识别 trade-off、形成可以 review 的设计方向。

很多需求最后做偏，不是实现阶段的问题，而是一开始就没有把问题定义清楚。brainstorming 最有价值的地方就在这。

### 9.2 方案落地时：用 writing-plans 固化实施步骤
当需求方向基本明确后，再让 AI 通过 writing-plans 生成实施计划。

这一层会让计划更像一份工程文档，而不是一段聊天式回答。我一般会要求它至少输出：涉及模块、改动点、风险点、验证点、开发顺序、待确认项。

### 9.3 开始实施前：让 GitNexus 补一轮结构分析
等 plan 出来以后，再让 agent 用 GitNexus 做一次结构化补充：

* query 找相关流程
* context 看关键类 / 函数上下游
* impact 判断改动范围
* detect_changes 预估后续结构影响
* 必要时生成结构图草稿

这一步的价值在于：防止 plan 只建立在"文字理解"上，而没有真正落到代码结构层面。

### 9.4 编码执行时：按计划小步推进
这时再进入：修改代码、补单测、生成测试数据、更新开发日志。

如果中间遇到调用链不清、影响面不明的地方，优先查 GitNexus，而不是靠模型脑补。

### 9.5 提交前：用 detect_changes + review skill 做收口
最后在提交前，我更建议再做两件事：

* 用 GitNexus 的 detect_changes 看这次 diff 实际影响了哪些流程
* 用 Superpowers 的 review 类 skill 做提交前自检或 review 响应

这样一来，整条链路就完整了：Superpowers 负责让 AI 按工程方法推进，GitNexus 负责让 AI 按代码结构理解推进。

## 10. 从优秀 skills 项目"抄作业"
建立业务专属和个人专属的 Skills，最好的起点不是闭门造车，而是直接从成熟项目里挑"可复用模式"。

Superpowers 是一个非常好的参照。它不是简单的快捷指令合集，而是一个强制 AI 遵循现代软件工程最佳实践的开发方法论框架。它的核心理念是：
过程重于猜测。

它的典型 skills 包括：

* brainstorming：苏格拉底式设计推演
* writing-plans：详细实现计划
* executing-plans：带检查点的执行
* dispatching-parallel-agents：并行子代理工作流
* requesting-code-review：提交前检查清单
* receiving-code-review：响应并处理 review 反馈
* using-git-worktrees：隔离工作分支和并行开发
* finishing-a-development-branch：决定合并、PR 或继续迭代

真正应该"抄"的，不只是 skill 名字，而是背后的方法论：把一次成功开发背后的过程，沉淀成 agent 下次还能继续执行的结构化资产。更取巧的方法是在它或者其他大家在日常工作中会用到的SKILL上进行二次修改，形成适合自己的SKILL

## 11. 将变更追加到 CLAUDE.md，但别停在这里
很多人做到这里就结束了：需求做完，顺手把新知识补进 CLAUDE.md。

这当然没问题，但更建议把这一步再拆开看。

### 哪些应该进 CLAUDE.md
* 新增的长期有效命令
* 仓库级稳定规则
* 新发现的通用坑
* 明确过的架构边界

### 哪些应该进 docs/
* 某一类需求的完整实现经验
* 某条业务链路的详细说明
* 系统之间的契约说明
* 设计决策与 trade-off 记录

### 哪些应该进 skill / hook
* 高频重复的工作流
* 必须触发的检查动作
* 提交前检查
* review 前 checklist

### 哪些应该交给 GitNexus
* 结构关系
* 符号上下文
* 功能簇
* 执行流程
* blast radius
* diff 级影响分析

### 哪些应该进 evals
* 这次 AI 明显做错的 case
* 人工兜底修正过的失败样本
* 容易回归的问题场景
* 易误判的边界条件

当这样分层之后，知识沉淀就不再只是"写给下次看一眼"，而是开始真正进入 harness 的反馈闭环。

## 12. 结语：AI Coding 的上限，不只在模型，也在为它搭的环境
在项目开发中用好 AI Coding，真正决定效果上限的，已经不只是模型本身了，而是有没有把环境搭好。

这个环境，不只是 IDE、插件、MCP 或几段 prompt，而是一整套 harness：

* 它让 agent 知道项目是什么
* 它让 agent 知道该先看什么、再做什么
* 它让 agent 有工具可用，而不是只能"提建议"
* 它让 agent 的行为有边界
* 它让结果可验证、可追踪、可复盘
* 它把失败继续喂回系统，形成改进飞轮

概况来说本次实践选择的几个工具组合的达到的效果：

CLAUDE.md 解决"AI 进场时别跑偏"，Superpowers 解决"AI 做事时别失序"，GitNexus 解决"AI 看代码时别只见树木不见森林"，而 Harness Engineering 负责把这几层真正编织成一套能长期运转的工程系统。



成熟的实践，不是"换一个更强的模型"就能自动得到，而是要一步一步把项目变成一个 agent 能理解、能执行、能验证、能持续成长的环境。

## 参考资料
* [OpenAI, Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering)。关于 agent-first 开发中"短 AGENTS.md + 结构化 docs/ + 工程化反馈闭环"的核心实践。
* Anthropic, [Best Practices for Claude Code](https://code.claude.com/docs/en/best-practices) 与 [Claude Code Overview](https://code.claude.com/docs/en/overview)。关于 Claude Code 的定位、CLAUDE.md 的最佳实践与工作方式。
* [obra/superpowers README](https://github.com/obra/superpowers)。关于 Superpowers 作为 agentic skills framework 与 software development methodology 的定位，以及 brainstorming、writing-plans 等流程型 skills。
* [GitNexus README](https://github.com/abhigyanpatwari/GitNexus/blob/main/README.md)。关于 CLI + MCP 的推荐方式、query/context/impact/detect_changes 等能力，以及多仓注册、hooks 和本地图谱索引。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
