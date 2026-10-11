---
title: "一、背景"
description: "基于Harness Engineering的商家智能体前端代码生成实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\基于Harness Engineering的商家智能体前端代码生成实践.md"
---
基于Harness Engineering的商家智能体前端代码生成实践

#### 🧑‍🏫 案例作者：[@韩露](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Ducc、Figma、Comate、知识库
#### 📒 案例概要：基于Harness Engineering方法论，商家智能体前端团队通过知识工程、多Agent协作与仿真平台搭建业务harness agent，解决UI、逻辑与工程约束，提升代码可用性与研发效率。
# 一、背景
在商家智能体的前端研发流程中，整体的工作主要分为以下4个部分。

详设（40%）

开发（50%）

代码自测（5%）

代码CR（5%）

其中代码开发是研发流程中工作占比最高的部分。前期调研的过程中发现，当前的模型能力在单一约束的场景下，代码生成效果基本符合预期。

但是在商家智能体这样成熟的业务场景下（70万行存量组件代码），代码的生成的可用性存在多维度的限制条件：

**约束1（UI层）**：不同于vibe coding 的自由样式生成，商家智能体的的UI 层效果，需要和UE 产出的Figma稿中的样式对齐。

**约束2（逻辑层）**: 不同与全新的业务场景，商家智能体大量的代码的功能要在理解存量逻辑的基础上进行迭代升级。

**约束3（工程范式）**：存量的代码库中，为了方便代码的维护和测试，存在大量的设计范式以及业务无关的环境工程型代码，AI coding 生成的代码需要进行此类规范进行理解。

由于以上三个条件的约束，导致在商家智能体的业务场景下， 直接使用AI coding生成的代码可用性较差。

||场景1: 仅约束功能|场景2: 仅约束UI|场景3: 约束功能 + 约束UI + 约束工程范式|
|-|-|-|-|
|示例|我要生成一个用于计算24 点的页面|figma链接为xx，实现这个页面。|在gt-merchant-header 组件的功能基础上（约束功能）参考新的UI 效果，figma链接为xx（约束UI），按照已有的卡片体系规范升级该组件（约束工程范式）|
|效果图|![](/personal-site-mvp/img/doc-placeholder.svg "")|![figma 设计稿](/personal-site-mvp/img/doc-placeholder.svg "figma 设计稿")![AI 生成](/personal-site-mvp/img/doc-placeholder.svg "AI 生成")|![旧组件](/personal-site-mvp/img/doc-placeholder.svg "旧组件")![新需求要求的组件](/personal-site-mvp/img/doc-placeholder.svg "新需求要求的组件")![效果1](/personal-site-mvp/img/doc-placeholder.svg "效果1")![效果2](/personal-site-mvp/img/doc-placeholder.svg "效果2")![效果3](/personal-site-mvp/img/doc-placeholder.svg "效果3")|
|可用性|🌟🌟🌟🌟🌟|🌟🌟🌟🌟|🌟|

本次期望通过系统性的工程能力建设，提升AI coding 在商家智能体业务场景下代码生成的可用性。同时探索全流程的AI解决方案，以提升研发整体的效率。

# 二、收益
[附件]
基于AI Coding的工程化体系建设，解决三重约束问题，提升整体研发效率；

当前团队AI 生成代码的占比88%，简单需求开发时间从1-2pd缩短至2-4h，复杂需求至少节约30%人力；

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 三、主要工作
## 3.1 方案调研
项目的目标是**在三重约束下高效生成生产环境下可用的代码**。我们调研了厂内以及业界流行的 Figma 稿转 UI 代码的方案，主要有以下三种：

|维度|Figma Make + Code Connect|Figma2Code Skill（厂内）|Claude Code + 工程体系（业界）|
|-|-|-|-|
|核心定位|提示词驱动的 AI 原型设计工具，同时生成设计与代码![](/personal-site-mvp/img/doc-placeholder.svg "")|IDE 内置的 Figma 转代码智能体，专注代码生成|终端 AI 编程助手，通过 MCP 协议接入 Figma 数据|
|使用方式|Figma 生态内，通过自然语言描述生成|Comate AI IDE 内，选中设计稿元素一键发送|终端 Claude Code + Figma MCP 配置|
|代码框架|React + Tailwind CSS|支持多种框架（以 Vue 为主）|项目现有技术栈，由 AI 根据上下文生成|
|约束实现的可能方式|研发侧沉淀原子组件库基于code connect 能力二次转换，构建专属设计系统设计侧：使用专属设计系统，基于figma make对话产出设计稿和代码研发侧：基于产出的react代码转换为vue代码|研发侧：准备组件使用文档：整理维护组件知识文档到.comate/components目录下，包括组件的引入与使用等关键信息。设计侧遵循组件标记规范：已有Figma设计组件：规范设计组件命名，与研发组件对应无Figma设计组件：使用图层标记组件研发侧：使用F2C skill在comate中生成代码|基于Claude Code 的 可扩展架构，做深度的项目适配|

上述三种方式都能通过AI Coding生成代码。

**项目初期**我们选定方案一，探索 Figma Make 代码生成方案，因为 UI 数据源头产自设计侧，如果设计侧能够在产出 Figma 稿的同时产出研发可用的代码，则能够提高设计与开发之间的协同效率，确保设计一致性和组件复用性，从而极大提高研发和UE效率。然而在调研阶段我们发现，基于 Code Connect 生成的原子组件设计系统，在 Figma Make 系统中稳定性很差甚至无法使用——生成的代码没有按照预期使用我们提供的原子组件库，因此放弃了该方案。

**方案二**则需要较大的人工介入：研发需要升级维护组件信息，设计侧每次产出 Figma 稿都需要手动进行标注。这种方式比较适合当前基于ONE-UI组件库建设的多个B端平台，保证跨平台体验一致性和效率提升的最大化；

**最终**我们选择第三种方案：**以Harness Engineering为方法论，基于Code Agent （ducc）搭建一套完整的harness工程，帮助我们更加高效、稳定地生成可用的代码**。

**Harness Engineering（驾驭工程）**

![](/personal-site-mvp/img/doc-placeholder.svg "")
**核心思想**：AI Agent 的瓶颈不在于模型本身，而在于你为它构建的"环境"。其核心不是优化 AI 模型，而是优化模型运行的"环境"。

有实验表明，仅优化harness不改变底层模型，Code Agent在Terminal Bench 2.0基准测试中得分从52.8%提升值66.5%~

一个完备的 Harness Engineering 体系通常包含五大核心维度：

* **约束机制**：设定明确的边界和规则，防止 AI 的行为超出预定范围。
* **复杂代码库管理**：确保 AI 能够理解并高效操作大型、结构复杂的代码库。
* **可观测性**：全程记录 Agent 的行动与决策，确保所有行为都有据可查。
* **多 Agent 协作**：设计并协调多个智能体分工合作，共同完成复杂的任务。
* **自我修复**：构建自动检测和修复机制，让系统在出现小故障时能自动恢复。

## 3.2 方案设计
基于上述Harness Engineering 体系定义，我们通过**知识工程体系****（约束机制 + 代码管理）****+ 多 Agent 协作 + 仿真平台****（自我修复）**，完成整个Harness 的搭建。

其中，**知识工程体系与多 Agent 协作解决逻辑约束和工程范式约束问题，仿真平台解决 UI 约束问题**。

[流程图]
## 3.2 知识工程体系
**定义**：知识工程体系是一个将人类知识转化为机器可处理形式的系统化工程，旨在构建一个能够存储、管理和应用知识的智能系统。

**作用**：为 AI 准备的"知识引擎"和"导航地图"，让 AI 的行为有据可依。

### 主要工作
#### 问题
在项目初期，面对代码量达到30w+的商家智能体业务，最核心的问题是**我们应该构造一个什么样的环境，让Code Agent能够按我们的要求产出我们想要的代码？**

在知识工程下，哪些知识该沉淀，该怎么沉淀，后续怎么维护和优化，以及怎么做好业务知识隔离，都是待解决的问题；

没有人确切知道AI Agent在这样一个复杂业务中会表现如何，会遇到什么瓶颈，在这种高不确定性环境下，作为一个探索性的项目，传统的“先参考成熟实践”思路并不完全适用；

#### 解决方案
**先启动、快试错、积累认知。**从真实的需求出发，探索出最佳实践；

![产品卡增加下载按钮需求示意](/personal-site-mvp/img/doc-placeholder.svg "产品卡增加下载按钮需求示意")
|问题|缺乏的知识类型|
|-|-|
|不知道可以复用已有的下载组件，而是重新实现一遍|业务知识|
|没有参考现有产品卡下挂组件的逻辑，而是重新实现一遍流程|业务知识+研发技能|
|产品消息卡在UI验证环节不知道如何作为一条消息展现|研发技能|
|样式整体错乱，直接从figma中读取px而不是参考代码规范使用@rpx414|研发规范|
|代码实现忽略了详设文档中的核心代码|研发规范|
|新建的组件名称不符合命名规范|项目级知识|



![](/personal-site-mvp/img/doc-placeholder.svg "")


基于上述分析和规范，我们整理总结并沉淀了：

**项目级知识CLAUDE.md**：项目级知识的入口，写入项目特定的指令、编码规范或架构约束，同时编写商家智能体的知识地图导航入口，与其他业务做好隔离

**研发规范 Rules**：沉淀 7 个通用规范 Rules，包括样式单位换算、UI 匹配判定（高/中/低优先级）、代码编辑规范、测试迭代策略等，作为强制性约束。

**业务知识 Docs**：建立结构化 Docs 目录，包括组件映射表、前端详设模板、字段映射表等，支持模型按需检索。

**开发技能 Skills**：沉淀 18 个业务 Skills，按职责分类：

* 组件定位类：mbot-structure-analyzer（组件查找、依赖分析、引用链追踪）
* 开发指导类：mbot-card-system-guide（卡片四层架构）、mbot-download-component-guide（下载组件）、mbot-message-system-guide（消息系统）
* 测试生成类：mbot-mock-message-generator、mbot-bigjson-generator、mbot-test-step-generator
* 验证类：mbot-style-diff-checker、mbot-test-executor

![](/personal-site-mvp/img/doc-placeholder.svg "")
基于分层知识建设，CLUADE.md全局统筹、Rules 层强制约束、Docs 层按需检索、Skills 层封装能力，解决 AI 知识匮乏的同时保证大模型合理的token消耗;

详细的探索细节可以参考团队沉淀的经验文档。[ducc协作方式下的文档设计经验分享](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/6XZN2Ew1Dm/zI4pTxl9oe/esyRlbzeVepSJd?t=mention&mt=doc&dt=doc)

**流程优化Tips**

* 编排器通过 triggers 字段实现场景自动检测：如检测到"卡片"关键词自动触发卡片系统 Skill，检测到"下载"触发下载组件 Skill，保证 Skill 稳定触发。
* 阶段输出结构化产物写入本地缓存（figmaCode、详设内容），后续阶段按需读取，提升流程稳定性的同时避免长上下文压缩导致关键信息丢失。

##### 哪些知识需要沉淀？
很多开发者知道大模型存在业务知识匮乏导致产生幻觉的问题，但面对复杂的业务场景，哪些知识需要沉淀、哪些不需要沉淀，往往难以把握。整体可以参考以下思路：

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 如何沉淀、如何优化？
###### 沉淀
**主动沉淀**：人工判断某部分知识较复杂，沉淀有助于 AI 理解整个业务和代码结构；先让 AI 基于核心业务进行梳理，人工 check 之后让其沉淀为知识。

**反思沉淀**：在 AI 产出代码不符合预期的情况下，让其抽象出问题（避免过拟合），持续优化或沉淀为通用知识。当前项目沉淀的大部分知识，都是在 AI Coding 生成的代码不符合预期的情况下，通过与模型对话、让其反思总结而沉淀出来的。

###### 优化
**数据飞轮**：通过收集开发者的对话数据，基于 d2c-optimizer Skill 持续优化业务 Skill 的效果，建设流程优化的闭环能力。

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 如何评估 Skill 效果？
在知识沉淀和优化的过程中，大家常有的疑问是：怎么评估这次的升级是否提升了 AI 生成代码的稳定性？

Anthropic 为 Claude Code 设计了 Eval（评估）功能界面，用于量化测试和对比 Skill 的性能表现。其核心逻辑是将 With Skill（搭载技能）与 Without Skill（无技能基线）的运行结果进行严格的量化对比，可以直接量化地知道优化是否真的有效。

![](/personal-site-mvp/img/doc-placeholder.svg "")
不过这种方案也存在 token 消耗大、构造 caselist 成本高的问题。

当前我们更多还是基于具体业务场景人工评判当前 Skill 是否达到预期效果，快速迭代持续优化。

## 3.3 多 Agent 协作
大模型的本质是一个"无状态的、单步的概率模型"，而本项目基于 AI 自动生成可用的组件代码，是一个明显要求"有状态的、多步的精确逻辑"的长任务（50-70 步），两者之间存在根本性的冲突。这导致本项目除知识匮乏外，还面临以下几个主要问题：

1. **长任务执行过程中，错误的累积与传播，导致代码可用性无法保证。**
2. **上下文爆炸导致指令遵循性降低，目标漂移。**
3. **AI 的不可控输出导致难以融入标准研发流程，工程闭环缺失。**

基于上述问题，针对完整的 AI Coding 自动生成流程，我们设计了多 Agent 编码架构。

![](/personal-site-mvp/img/doc-placeholder.svg "")
判断用单Agent还是多Agent协作，核心是看任务的**复杂度**和**多样性**。一个简单原则是：**单Agent能胜任的任务，不要复杂化成多Agent系统**，后者会显著增加延迟、成本和调试难度。

主 Agent 仅保留协调与决策职责，5 个独立的子 Agent 调用相关 Skill、运用相关知识执行不同任务，这既避免了上下文超限导致的指令服从性下降，也防止早期关键目标被中间内容冲淡。

![](/personal-site-mvp/img/doc-placeholder.svg "")
同时，子 Agent 可以基于任务难度自行决定模型选择——比如知识文档提取、Figma 代码提取使用 Haiku，而代码编写则使用 Opus，进一步减少token消耗

在真实的业务开发上，我们聚焦核心场景，沉淀 常用的workflow编排方式 **Command → Agent (with skill) → Skill**，降低开发者的使用成本：

1. **指令 1：designToCode**：输入详设文档，产出业务可用代码。

![](/personal-site-mvp/img/doc-placeholder.svg "")
2. **指令 2：mrdToDesign**：输入 MRD，对需求进行澄清，产出详设文档。

![关键流程](/personal-site-mvp/img/doc-placeholder.svg "关键流程")


|需求示意|设计细节的人工校准过程|详设的结果示意|
|-|-|-|
|![产品卡增加下载按钮示例](/personal-site-mvp/img/doc-placeholder.svg "产品卡增加下载按钮示例")|![方案确定](/personal-site-mvp/img/doc-placeholder.svg "方案确定")![业务字段确定](/personal-site-mvp/img/doc-placeholder.svg "业务字段确定")|![详设内容](/personal-site-mvp/img/doc-placeholder.svg "详设内容")|

## 3.4 仿真平台
区别于传统的 one-shot 的 AI Coding 体验，我们在完成代码编写之后引入了样式自动走查环节，保证最后产出的代码可以直接用于生产环境。

**核心思路**：建设基于 Playwright 的预览服务，将测试子 Agent 生成的测试数据集作为输入（包括页面信息、初始化数据信息、caselist 等内容），实现"代码修改 → 页面热更新 → caselist 执行 → 自动截图"的闭环，输入 Figma 截图和页面渲染截图，让模型有明确的 UI 代码成功标准。

在进行多模态视觉验证后，如果不通过，则启动自动修正循环：测试失败 → 分析根因（属性差异/视觉差异）→ 修复代码 → 等待刷新 → 重新测试验证，实现 UI 问题的自修复。

同时，仿真平台提供图片的叠化预览能力，方便开发者在提交代码之前进行二次效果确认，以保证最后代码生成的可行性。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
通过搭建可视化仿真平台，一方面通过修改后的页面截图作为 AI 自动化校验功能的基准输入，提升 AI 代码生成的可用性；另一方面方便人工在提交前进行样式确认，减少后续返工成本。

## 3.5 体验优化
在 AI 能力无法达到 100% 稳定的情况下，引入工程层面的优化，提升整体的研发体验。

### Checkpoint + 通知机制
在长任务的执行中，某一个步骤的产物如果不符合预期，都会导致最后生成代码的可用性降低。因此，我们针对核心环节建设关键检查点，对产出进行校验。

Hooks 通知机制解决的是另一个问题：开发过程中某个节点被卡住需要人工确认，但没有被感知到，导致任务一直停滞。通过 Hooks 能力引入消息通知，既实现了开发者的按需关注，又提升了整体任务的成功率。

![输入不符合要求及时通知](/personal-site-mvp/img/doc-placeholder.svg "输入不符合要求及时通知")
![mrd to 详设问题澄清](/personal-site-mvp/img/doc-placeholder.svg "mrd to 详设问题澄清")
### LUI 与 GUI 协同
建设前端可视化的结果展示，方便在 AI 多模态理解不足时进行人工介入。

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 四、心得总结
1. AI 代码生成最大的挑战不是模型能力，而是如何让产出可控、可预期、可量化、可优化。
    1. **Think Like Human**：除了前述的基础操作，核心思考的是人为什么能写好——有哪些知识是 Code Agent 无法在系统中获取的，这些知识就需要沉淀给 Agent。
    2. **建立可观察中间指标**：历史对话相当于 Spec 模式下的验收依据，所以在当前自动化流程中我们做了沉淀对话的功能，期望能够持续辅助优化全流程；而其中的对话轮次、人工介入率则能够定量证明代码生成的稳定性是否在稳步向前。

2. 现在开发者已经从"如何写好详设、如何写好代码、如何进行代码 review"演变成了"如何构建支撑 Code Agent 高效稳定工作的系统体系"。
3. 工程建设区分确定性和不确定性：模型结果是不确定的，过程产出是确定的，要区分开，不要互相影响。

# 五、后续规划
## 5.1 逻辑代码生成增强
当前以 UI 代码生成为主，逻辑代码生成能力有限。后续将探索更复杂的业务逻辑生成场景，主要发力方向是三个点：

1. 生成信息完备、质量更高的详设文档
2. 增强逻辑代码生成和校验的能力
3. 优化caselist和初始化数据生成，提升全链路的稳定性

## 5.2 场景串联
当前 MRD 生成详设文档和详设文档转代码两个环节是独立的。期望将 designToCode 指令与 mrdToDesign 指令进行合并，实现 mrdToCode 的探索，进一步提升研发效率。

## 5.3 开发体验提升
对关键节点的产物进行增强，实现关键节点可验收、可干预的能力，从而探索基于如流中 dodo 实现全链路的代码开发新场景。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
