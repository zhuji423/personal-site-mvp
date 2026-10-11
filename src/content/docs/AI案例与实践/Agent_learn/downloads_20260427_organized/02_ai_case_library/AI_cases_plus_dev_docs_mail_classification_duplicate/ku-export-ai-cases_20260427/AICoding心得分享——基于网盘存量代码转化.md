---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "AICoding心得分享——基于网盘存量代码转化"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AICoding心得分享——基于网盘存量代码转化.md"
---
AICoding心得分享——基于网盘存量代码转化

#### 🧑‍🏫 案例作者：[@徐敬磊](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Ducc、Claude
#### 📒 案例概要：分享 Skill、SubAgent、Agent Team 三项 AI 技术的应用心得
> 复杂工程场景下，AI 不是一个"问一句答一句"的黑盒，而是一套需要被精心设计的技术体系。本文以网盘 Android 存量代码转 KMP 项目为实践载体，分享 Skill、SubAgent、Agent Team 三项 AI 技术的应用心得——它们分别回答"怎么稳定执行"、"怎么调度不失控"、"怎么协作提效"三个层次的问题，组合起来，构成一套从原子执行到并行协作的完整方案。
---

## 一、Skill——将 AI 的执行能力标准化固化
### 1.1 从"每次重新理解"到"按规范稳定输出"：Skill 是什么
[Claude Code Skills](https://code.claude.com/docs/zh-CN/skills)

在实际使用 AI 的过程中，一个常见的困扰是：让 AI 执行同一类任务，不同对话中的表现可能差异很大。这不是模型能力波动，而是因为 AI 每次执行都在"重新理解"任务意图——上下文不同，理解就不同，输出自然不稳定。

Skill 要解决的就是这个问题：**把 AI 完成某类任务的方式固化为可复用的执行规范**。

Skill 是一种无状态、单一职责的执行单元，通过 `SKILL.md` 文件定义 AI 执行任务的方式——包括触发条件、执行步骤、完成标准、参考模板。Skill 本身没有对话历史和记忆，它只做一件事：被调用时，按照预定义的规范稳定执行。

Skill 与 Agent 在使用中是**执行者与编排者**的关系：Agent 决定做什么、以什么顺序做，Skill 决定怎么做。这种分离让"策略"和"执行"解耦，Agent 可以灵活组合不同 Skill，Skill 本身无需关心上下文调度。

|**维度**|**Agent**|**Skill**|
|-|-|-|
|定位|编排者，决定做什么、以什么顺序做|执行者，按照规范完成具体任务|
|记忆|有 Memory（对话历史、配置信息）|无 Memory，每次调用独立执行|
|调用关系|调用 Skill|被 Agent 调用|
|定义位置|`.claude/agents/*.md`|`.claude/skills/*/SKILL.md`|

Skill 支持三个层级的定义，覆盖从项目到用户到插件的完整复用链路：

|**层级**|**路径**|**作用范围**|**定位**|
|-|-|-|-|
|项目级|`.claude/skills/<name>/SKILL.md`|当前项目内复用|项目专属的执行规范|
|用户级|`~/.claude/skills/<name>/SKILL.md`|跨项目复用|个人通用的执行习惯|
|插件级|`<plugin-dir>/skills/<name>/SKILL.md`|插件生态提供|平台级的通用能力|

### 1.2 约束行为而非描述意图：Skill 怎么写
写 Skill 最常见的误区是只写"做什么"不写"怎么做"。只告诉 AI 目标不约束过程，不同上下文中的输出差异会很大。

一个好的 Skill，应该让任何 Agent 在任何上下文中调用它，都能得到稳定一致的输出。以下是实践中总结的编写规范：

|**要求**|**说明**|**为什么重要**|
|-|-|-|
|单一职责|每个 Skill 只做一件事|职责清晰才能稳定执行，混合多种逻辑会导致 AI 行为不可预测|
|描述清晰|description 说清楚触发场景和适用边界|Agent 需要根据描述判断是否调用，描述模糊会导致误调用或漏调用|
|模板与示例|提供可复用的代码模板和输入输出示例|有模板参考时，AI 的输出质量显著高于纯指令驱动|
|检查清单|用 Checklist 明确每一步的完成标准|防止 AI 在多步骤执行中跳过关键环节|
|分层参考|通用规则放 SKILL.md，细节和边缘情况放 references/|避免单文件过长导致 AI 注意力分散|

其中，**检查清单（Checklist）** 是实践中最有效的约束手段。AI 在多步骤执行中容易跳过某些环节——不是不会做，而是在步骤序列中遗漏。Checklist 相当于逐项打勾的执行凭证，每完成一步核对一步，遗漏率大幅下降。

### 1.3 职责分离才能自我纠错：Skill 的实战价值
**案例：页面代码提取中的力度控制**

在网盘存量代码转化中，页面代码的提取力度是最核心的难题。力度是一个光谱：一端是只提取表面文件，依赖链路断裂，后续编译失败；另一端是过度提取无关文件，提取包膨胀，转化负担加重。人工提取尚且难以平衡，AI 更容易在两个极端之间摇摆。

如果将提取和校验写在同一个 Skill 里，AI 会陷入"自己 review 自己"的困局——提取完之后自己校验自己，天然倾向于确认结果无误。这与代码 review 中作者自我审查容易放过问题同理，**审查者和执行者需要视角分离**。

我们的做法是将提取环节拆分为三个独立 Skill，形成 `extractor → validator → fixer` 的三层自修复链路：

[流程图]
* **extractor**：首次提取，以 import 语句为入口扫描依赖关系，生成初始提取包
* **validator**：校验提取结果，检查链路完整性。它的视角与 extractor 天然不同——extractor 关注"该提取什么"，validator 关注"还缺什么"
* **fixer**：根据 validator 的反馈定向补充遗漏文件，形成闭环

三层拆分的核心价值在于**职责分离产生的自我纠错能力**。validator 不受 extractor 的思维惯性影响，能独立审视结果的完整性；fixer 无需重新理解整个提取逻辑，只需针对 validator 指出的缺口定向修复。这种"提取-校验-修复"的闭环，在单个 Skill 内部无法稳定实现——审查者和执行者必须分离。

另一个重要收益是**问题定位精准**。出现遗漏时，可以精确定位是 extractor 的提取规则不够全面、validator 的校验逻辑有盲区、还是 fixer 的修复策略不够灵活，定向调整即可，无需在一个庞大的 Skill 中排查。

---

## 二、SubAgent——以上下文隔离对抗信息过载
### 2.1 上下文膨胀是复杂任务的必然瓶颈：SubAgent 是什么
[Claude Code SubAgent](https://code.claude.com/docs/zh-CN/sub-agents)

AI 在一次对话中能保持的信息量是有上限的。当上下文不断增长超过限制时，系统会自动压缩：早期加载的文件细节被模糊化，文件之间的引用关系变得不确定，AI 开始生成不存在的方法或类，这就是**幻觉（Hallucination）**的典型来源。

在 KMP 转化这样的复杂工程中，上下文膨胀几乎是必然的——一个页面的转化涉及模块配置、资源文件、UI 布局、业务逻辑，动辄几十个文件。如果在 MainAgent 的同一个 Session 中处理所有步骤，到了后期，前期加载的文件信息已经被压缩，AI 丧失了对关键依赖的记忆。

SubAgent 正是为解决这个问题而设计的。它是由 MainAgent 创建的独立调度器，拥有**完全独立的对话上下文**。MainAgent 将任务分发给 SubAgent 后，SubAgent 在自己的上下文中完成工作，不会污染 MainAgent 的上下文，也不受 MainAgent 上下文压缩的影响。

运行关系为 `MainAgent → SubAgent → Skills`：

* **SubAgent** 作为调度器，决定调用哪些 Skill、以什么顺序调用
* **Skills** 作为执行者，按照规范完成具体任务
* SubAgent 运行结束时，将关键信息写入 **memory** 记录，供后续环节参考

与直接在 MainAgent 中调用 Skill 相比，SubAgent 的核心优势在于**上下文隔离**：

|**维度**|**SubAgent + Skill**|**直接调用**|
|-|-|-|
|上下文管理|独立上下文，互不干扰|主 Session 上下文持续膨胀，触发压缩|
|复用性|Skill 可跨 SubAgent 复用|逻辑内联在主对话中，难以复用|
|可维护性|Skill 单一职责，独立测试|逻辑耦合在主流程中，改动影响面大|
|调试难度|各环节可独立验证，问题定位精准|问题混在主上下文中，定位困难|
|适用场景|复杂多步骤任务|简单一次性任务|

### 2.2 Agent-Memory 机制：隔离上下文，但不割裂信息
上下文隔离解决了膨胀问题，但带来了一个必须解决的问题：**SubAgent 之间如何传递信息**？如果每个 SubAgent 都是信息孤岛，后续步骤无法获知前序步骤的产出，工作无法衔接。

Agent-Memory 机制就是在"隔离"与"衔接"之间找到平衡。

它的做法是：将关键信息从对话上下文中**提炼出来**，存储为结构化的 memory 文件，放在 `.claude/agent-memory/` 目录下。这些文件不是对话历史的复制，而是经过提炼的**关键产出摘要**——只保留后续步骤必需的信息，丢弃对话中的冗余细节。

工作流程：

* SubAgent A 完成工作后，将关键信息写入 memory 文件
* SubAgent B 启动时，读取 memory 文件，获取 A 的核心产出
* B 在自己的独立上下文中工作，但拥有 A 的关键信息作为输入

**案例：资源转化与 UI 转化的 Memory 传递**

在 KMP 转化流程中，资源转化（strings.xml、colors.xml 等）和 UI 转化是两个先后步骤。UI 代码中大量引用资源 ID，转化时必须知道这些 ID 在 KMP 侧的映射关系。如果 UI 转化的 SubAgent 缺少资源映射信息，它可能凭空推测映射关系，这正是幻觉的典型触发场景。

通过 Agent-Memory，资源转化的 SubAgent 完成后将资源 ID 映射表写入 memory 文件，UI 转化的 SubAgent 启动时读取这份映射表，在自己的上下文中准确完成转化，无需推测也无需重复劳动。

这一机制的设计哲学可以概括为：**对话上下文可以隔离，但关键信息必须流转**。Memory 文件不是"前面说了什么"的记录，而是"后面需要什么"的提炼——从对话历史中萃取结构化知识，而非原始信息的搬运。

### 2.3 串行调度串联依赖步骤：SubAgent 怎么用
SubAgent 的使用模式是**串行调度**：每个步骤由一个 SubAgent 负责，步骤之间通过 Memory 传递信息，确保有依赖关系的步骤按正确顺序执行。

**案例：KMP 转化流程的 SubAgent 调度**

KMP 转化是一个典型的多步骤串行流程——模块生成、资源转化、UI 转化、业务代码转化，后一步依赖前一步的产出。每个步骤交给一个 SubAgent，步骤之间通过 Memory 传递关键信息。每个 SubAgent 内部又遵循 `converter → validator → fixer` 的三层模式：

* **converter**：执行首次转化
* **validator**：校验转化结果，检查语法正确性、依赖完整性
* **fixer**：根据 validator 反馈修复问题

前序 SubAgent 的产出通过 Memory 传递给后续 SubAgent，例如：

* 模块生成的 SubAgent 产出模块结构和配置信息，后续 SubAgent 据此确定代码放置路径
* 资源转化的 SubAgent 产出资源映射表，UI 转化的 SubAgent 据此处理资源引用

这种方案的实际价值：

* **上下文可控**：每个步骤的上下文独立且精简，不会因文件过多触发压缩导致幻觉
* **增量可行**：不必一次性转化整个页面，可以分批次转化、多次补充，降低单次执行复杂度
* **依赖明确**：每个步骤的输入输出通过 Memory 显式定义，信息流转有据可查，而非依赖 AI 的隐式记忆

---

## 三、Agent Team——以专业分工实现并行协作
### 3.1 串行模式的天花板在于效率与记忆的双重瓶颈：Agent Team 是什么
[Claude Code Agent Team](https://code.claude.com/docs/zh-CN/agent-teams)

当任务复杂度进一步上升——比如一个页面的代码提取需要同时处理 UI、布局、业务逻辑、资源四种类型的文件——SubAgent 的串行模式也会遇到瓶颈：

* **上下文仍然会膨胀**：即使每个 SubAgent 只处理一个步骤，单个步骤内也可能涉及大量文件
* **串行效率低**：四种类型的文件提取并无强依赖，串行执行浪费时间
* **记忆衰减加剧**：流程越长，早期步骤的信息在后续步骤中越容易丢失

Agent Team 要解决的就是"多类型任务并行处理"的问题。它是一种多 Agent 并行协作框架，由 Team Lead 创建团队、生成多个 Teammates，各 Teammate 在独立上下文中并行处理不同任务。

|**组件**|**角色**|**定位**|
|-|-|-|
|Team Lead|创建团队、协调工作的主会话|团队管理者|
|Teammates|各自处理分配任务的独立实例|团队成员|
|Task List|Teammates 认领和完成的共享工作项列表|共享任务看板|
|Mailbox|Teammates 之间通信的消息系统|跨成员通信通道|

![](/personal-site-mvp/img/doc-placeholder.svg "")
与 SubAgent 的核心区别在于**协作模式**：

|**维度**|**Agent Team**|**SubAgents**|
|-|-|-|
|定位|Team Lead 创建，多 Teammates 协作|MainAgent 创建，作为独立调度器|
|通信方式|Teammates 之间通过 Mailbox 实时通信|SubAgent 之间通过 Memory 文件异步传递|
|任务来源|共享 Task List，Teammates 自行认领|MainAgent 直接分发|
|上下文共享|各 Teammate 完全独立上下文|SubAgent 独立上下文，可继承 MainAgent 信息|
|并行能力|原生支持多 Teammates 并行|串行调度，不可通信的并行|
|协作灵活性|高（Teammates 可通过 Mailbox 自行协调）|中（按固定顺序执行，缺乏运行时协调）|
|适用场景|多类型任务并行处理|有依赖关系的多步骤串行流程|

简要区分：SubAgent 是"流水线"，上一个工位完成传给下一个；Agent Team 是"项目组"，多人各负责一块，有交集的地方通过 Mailbox 协调。

### 3.2 Agent Team 怎么搭
搭建 Agent Team 需要三个关键决策：**Teammates 怎么定义、任务怎么分发、信息怎么流转**。

**前置条件**：

1. 在 `/Users/用户名/Library/Application Support/Comate/User/settings.json` 中启用实验特性：

```
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```
2. 使用可分屏命令行（如  [iTerm2](https://iterm2.com/)），便于同时观察多个 Teammates 的运行状态

> **注意**：SubAgent 不能作为调起 Agent Team 的对象，必须在 Main Agent 直接创建 Team。团队配置存储在 `~/.claude/teams/{team-name}/config.json`，不支持项目级私有配置，项目目录中的 `.claude/teams/` 下的文件不会被识别为团队配置。
**Teammates 的定义原则**：按文件类型或职责域划分，每个 Teammate 专注一类工作。划分粒度太粗会失去并行意义，太细则 Teammate 间协调开销超过收益。

**任务分发与协调机制**：

* Team Lead 创建 Task List，将任务拆分为独立工作项
* Teammates 从 Task List 中自行认领任务，而非被动等待分配
* Teammates 之间通过 Mailbox 互通信息，处理跨职责的依赖

### 3.3 四路并行提取，以专业分工对抗复杂度：Agent Team 的实战价值
**案例：页面代码提取中的 Agent Team 协作**

页面提取是 Agent Team 最典型的应用场景。一个页面的代码涉及四种类型的文件：UI 组件、布局文件、业务逻辑、资源文件。这四类文件的提取逻辑各不相同，但彼此之间没有强依赖——布局提取不需要等 UI 提取完成，资源提取也不需要等业务逻辑提取完成。

如果让单一 Agent 串行处理，问题有三：

* 四类文件混在一个上下文中，上下文快速膨胀触发压缩，最早提取的文件细节丢失
* Agent 在处理完 UI 和布局后，到处理业务逻辑时可能已经遗忘 UI 中引用了哪些业务类
* 耗时是四类提取时间的串行累加

我们将提取工作拆分为四个专业 Teammates 并行执行：

[流程图]
|**Teammate**|**职责**|**提取内容**|**专业关注点**|
|-|-|-|-|
|`ui-extraction-agent`|UI 层组件提取|Activity、Fragment、自定义 View、ViewModel|生命周期、View 层次结构|
|`layout-extraction-agent`|布局文件提取|XML 布局、include 引用、fragment 标签|布局嵌套关系、动态加载的布局|
|`business-code-extraction-agent`|业务逻辑提取|Repository、Service、API、DataModel|调用链路完整性、接口契约|
|`resource-extraction-agent`|资源文件提取|strings.xml、colors.xml、drawable|资源引用关系、资源命名规范|

四个 Teammates 各自维护独立上下文，只关注自己负责的文件类型，上下文精简且聚焦。通过 Mailbox 互通依赖信息——例如 UI 提取 Agent 发现代码中动态创建了 Dialog，通过 Mailbox 通知布局提取 Agent 补充提取该 Dialog 的布局文件；业务逻辑提取 Agent 发现 API 调用涉及字符串资源，通知资源提取 Agent 补充提取。

四路并行直接解决三个问题：

* **上下文可控**：每个 Teammate 只处理一类文件，上下文体积可控，不会触发压缩
* **提取深度更优**：每个 Teammate 专注一类提取逻辑，对该类型的依赖模式理解更深（如布局中的 include 引用、业务代码中的接口契约），提取质量高于"什么都做"的通用 Agent
* **执行效率提升**：四路并行，总耗时近似取最长路径，而非四段串行累加

---

## 四、三项技术的组合选型——从原子执行到并行协作的分层方案
三项技术不是互斥的替代关系，而是解决不同层次问题的互补方案。在网盘 KMP 转化项目中，我们按"执行-调度-协作"三层组合使用：

|**层次**|**技术**|**解决什么问题**|**在项目中的角色**|**定位**|
|-|-|-|-|-|
|执行层|**Skill**|怎么稳定执行|所有具体任务的执行单元|原子执行规范|
|调度层|**SubAgent**|怎么串行调度、隔离上下文|转化阶段的串行流程调度|独立调度器|
|协作层|**Agent Team**|怎么并行协作、专业分工|提取阶段的多类型并行处理|并行协作框架|

整体协作关系：

* **提取阶段**：使用 Agent Team 四路并行提取页面代码，各 Teammate 内部调用 Skill 执行具体提取、校验、修复任务
* **转化阶段**：使用 SubAgent 串联 converter → validator → fixer 流程，SubAgent 之间通过 Agent-Memory 传递关键产出，各 SubAgent 内部同样调用 Skill 执行

[流程图]
选型的核心判断依据是**任务之间的依赖关系**：

* 任务之间无强依赖、可并行 → **Agent Team**
* 任务之间有依赖、需串行 → **SubAgent**
* 具体执行动作 → **Skill**

**最终落地的架构理念**：Skill 保证单点执行的稳定，SubAgent 保证串行流程的上下文可控，Agent Team 保证并行任务的高效协作。三者叠加，构成一套从原子执行到团队协作的完整 AI 工程化方案。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
