---
title: "PM日常工作中的AI提效工具及工作流"
description: "用AI重构工作流：PM提效实战"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\用AI重构工作流：PM提效实战.md"
---
用AI重构工作流：PM提效实战

#### 🧑‍🏫 案例作者：[@李奕博](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：信息洞察、项目管理、任务管理、数据分析、设计、需求、工作流自动化
#### 🔧 使用工具：dodo、NotebookLM、Gemini、Claude、Comate
#### 📒 案例概要：本案例展示了PM如何通过AI工具实现工作流的全链路重构。利用NotebookLM深挖洞察、Figma快捷出图、Claude Code跨越技术鸿沟及dodo沉淀内部知识。
# PM日常工作中的AI提效工具及工作流
|PM工作流程||可使用AI工具|度厂内部工具|工作流|
|-|-|-|-|-|
|市场洞察与机会发现|用户研究|用户访谈转化为结构化数据：[Notebooklm](https://notebooklm.google.com/)、[飞书妙记](https://ocnni2g6u5sk.feishu.cn/minutes/home)|[百度](https://www.baidu.com/)+[文心一言](https://yiyan.baidu.com/?utmSource=pinzhuan)|访谈录音→ NotebookLM整理 → 结构化用户洞察|
||竞品分析|各类大模型：ChatGPT，[Gemini](https://gemini.google.com/)，[claude](https://claude.ai/login)，deepseek，豆包，千问……[Notebooklm](https://notebooklm.google.com/)||用大模型搜索竞品 → 抓URL → [Notebooklm](https://notebooklm.google.com/)分析 → 输出结构化对比表|
||行业趋势|行情调研：[Chatgpt DeepResearch](https://chat.openai.com/?model=text-davinci-002-render-sha)各类大模型：ChatGPT，[Gemini](https://gemini.google.com/)，[claude](https://claude.ai/login)，deepseek，豆包，千问……||1.直接使用[Chatgpt DeepResearch](https://chat.openai.com/?model=text-davinci-002-render-sha)，输入*搜集翻译软件的行业背景及当前市场占有率等相关商业数据，进行行业趋势的预测*，即可返回调研报告|
||模型能力可行性评估|工具：[OpenRouter](https://openrouter.ai/)评估：Evals / LangSmith|百度智能云|构建测试集 → 多模型跑结果 → 对比 cost / latency / 准确率|
|产品规划与定义|需求管理|各类大模型openclaw|Dodo (看板/项目管理)|需求录入 → AI自动分类（RICE）→ 优先级排序|
||功能设计与 PRD|各类大模型：ChatGPT，[Gemini](https://gemini.google.com/)，[claude](https://claude.ai/login)，deepseek，豆包，千问……**claude code：处理结构化任务，拆需求，理解技术逻辑，梳理系统边界，生成可沟通原型页面**|文心一言|对话式梳理需求（与AI对话完善逻辑框架） → 自动生成PRD → 人工校正|
||原型设计|[Figma make](https://www.figma.com/make/),[mastergo](https://mastergo.com/files/home)，墨刀AI，axure AI，sketch|-|描述页面 → 自动生成UI → 快速迭代|
||Prompt 开发与调优|各类大模型：ChatGPT、Claude、Gemini……调试：Playground；评估：LangSmith|百度智能云、DODO|大模型生成Prompt →百度智能云 A/B测试  → 持续优化也可以直接使用claudecode，在本地创建md文件，通过不断测试完成调优可以使用dodo完成测试效果的分析|
||快速 Demo 搭建|Claude CodeIDE：cursor、codex、trae、codebuddy……低代码平台：coze、dify、n8nGoogle AI Studio等|Comate、Ducc、秒哒|PRD → 自然语言 → 生成Demo → 本地运行|
||数据分析|各类大模型vibing coding工具claude code|Comate、dodo、ducc|输入分析目标 → 自动生成SQL/Python脚本 → 输出结论|
|项目跟进与研发协同|需求评审与同步|-|-||
||技术协同与配置|**Claude Code**, Cursor|**DUCC**|利用 Claude Code读取代码库 → 分析逻辑 → 执行修改也可通过 DUCC进行读取 |
||进度与风险管理|-|-||
|数据复盘与迭代优化|数据回溯|各类大模型|dodo|分析用户行为 → 找问题 → 输出优化建议|

表格中是我整理的PM全流程工作中AI工具是如何帮助提效，但内容比较多，就不进行详细分享。

总体来说，AI提效的工具主要是这5类：

第一类是**通用/多模态大模型**，这些工具具备极强的文本理解、生成和逻辑推理能力，可以帮我们完成竞品分析、行业趋势调研、文档撰写等一系列工作；

第二类是**结构化数据**的工具，帮助我们把大量杂乱的信息进行结构化，典型的如 **NotebookLM；**

第三类便是各种**低代码、原型设计**的工具。我们可以通过自然语言，实现原型界面的设计，甚至可以搭建自动化工作流；

第四类是**代码协调工具**，我最常使用的便是**Claude Code**，此外还包括 Cursor、Trae、Codebuddy 等 IDE，度厂内部的便是Ducc和Comate；

第五类我认为是我们的**AI助手**，Openclaw、Hermes Agent以及我们的dodo。因为dodo连接着我们的内部资料以及如流文档，所以对于AI助手，我比较偏向使用dodo，他能够更好的贴合我的工作场景。

最后我从上述工具中挑选几个我常使用的AI提效工具来介绍：**NotebookLM、figma AI（Make）、Claude Code和Dodo**。它们解决的问题各有侧重，组合在一起，覆盖了从「资料整理→原型验证→技术沟通→内部协作」的全链路。

这篇文章不对工具做完整介绍，只记录我实际使用下来最有体感的一些场景。

---

## 一、NotebookLM —— 把散落的资料变成可对话的知识库
**解决什么问题：**

PM每天要处理大量分散的资料——用户访谈记录、行业报告、会议纪要、需求文档，散落在如流文档、邮件和各种文件夹里。NotebookLM解决的是「怎么快速从这些资料里提取我需要的信息」。

**核心逻辑：**

我的理解是NotebookLM是一种**“开箱即用”的 RAG系统，**它的知识边界完全由你划定——**你上传什么，它就只基于什么回答**。它不会胡编乱造，不会有时效性问题，非常适合处理内部敏感资料。

**我的高频使用场景：**

* **整理用户访谈记录**：上传一段时间内的访谈文本，让它提炼高频需求、用户痛点和原话引用
* **横向对比行业报告**：上传多篇报告，让它做结构化对比，比自己一篇篇读快很多
* **从会议纪要中提取行动项**：上传一份超长纪要，让它列出「核心结论 + 行动项 + 待跟进问题」
* **基于资料库模拟预演**：写完一个方案后，让它扮演用户或开发，预判可能被质疑的问题

**一个具体的感受：**

以“百度翻译竞品分析”为例，这套工作流彻底重塑了我的调研效率：

**1.情报索引：** 首先利用大模型（如 ChatGPT/Gemini）的知识面，快速扫描并锁定核心竞品，精准获取其官网 URL 及最新动态。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e0b26ea7d16548eead931f2ed493604c&docGuid=e6u5JzsiUedZ2a "")
**2.知识沉淀：** 将这些 URL 一键注入 NotebookLM。系统会自动对网页进行“吞噬”与消化，在左侧信源区完成结构化摘要，瞬间建立起一个专属的竞品情报站。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=19711948fed64c899f57760dce290c3b&docGuid=e6u5JzsiUedZ2a "")
**3.下指令：**我们在对话框中输入自己的指令：核心功能对比表/深度挖掘优劣势/目标用户画像分析/商业模式与定价调研……一份质量极高、严谨且**所有结论均可溯源**的结构化分析报告，真正实现了“调研即输出”。

以下是一些自己使用过程的prompt及产出内容

|需求|prompt|
|-|-|
|核心功能对比表|请基于提供的资料，对比百度翻译、DeepL 和有道翻译在‘翻译模式’（如同传、拍照、文档）、‘支持语种数量’和‘特色 AI 功能’三个维度的差异，并整理成表格。|
|深度挖掘优劣势|根据用户评价和产品介绍，分析 DeepL 相比百度翻译的核心竞争优势在哪里？百度翻译在哪些本地化功能上做得更好？|
|目标用户画像分析|这几个竞品分别针对的是什么样的人群？（例如：学术研究者、商务出差人士、学生还是开发者？）请从资料中找到依据。|
|商业模式与定价调研|梳理各竞品的付费会员体系。哪些功能是免费的，哪些需要订阅？它们的定价策略有什么不同？|

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=986c701054584744a82d47e11deeb29d&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0e705564bc5149818d3cd5bd2682409a&docGuid=e6u5JzsiUedZ2a "")
---

## 二、figma AI（Make）—— 用自然语言快速搭原型
**解决什么问题：**

PM经常遇到「脑子里有一个交互想法，自己用figma画又太慢」的情况。figma Make把原型制作的门槛大幅降低。

**核心能力：**

用自然语言描述需求，直接生成界面框架。

**我的使用场景：**

* **快速验证交互概念**：想确认某个流程是否合理时，让AI生成一版原型，大家「有东西可看」再讨论，比空对空描述高效很多
* **向开发描述需求时配合使用**：开发经常说「这个交互我看不太懂」，一张AI生成的原型图比一段文字描述清晰很多

**一个真实的感受：**

以前做一个复杂的交互验证，画一个较为完整的原型，最快也要半天。现在5分钟出初稿，后续只需要微调。**它在「快速验证想法」这个环节做得足够好。**

but！figma的make功能很容易卡死，所以我推荐使用MasterGo这也是我们之前测试下来效果较好的一个国产软件，速度快，且较为稳定，用来画原型足以。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6bc8db6fd6884f10bc9d1149dc1c736d&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=efbb0cceffc140bebf2ec68c89ae953f&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f81abcfc0bba4324bdb8cc0adbe7a2cb&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fb764be10dea4db2b0cfcf7aa4db3c36&docGuid=e6u5JzsiUedZ2a "")


---

## 三、Claude Code —— 帮我和技术团队高效协作
**解决什么问题：**

PM经常遇到「需要理解技术实现，但找开发问又怕打扰对方」的场景。Claude Code让我可以自己去代码库里探索，降低了「技术沟通」的摩擦。

**核心能力：**

与普通大模型只能“纸上谈兵”不同，Claude Code 拥有**实际执行与验证的能力**。它能直接操作本地文件、调用终端命令、搭建多 Agent 系统并实现任务并行处理。它不只是在“回复指令”，而是在“交付结果”。

**我的高频使用场景：**从基础交互到复杂工程

* **文本对话：**不仅是聊需求，而是基于当前代码上下文进行对话。它能直接指出某段逻辑在哪个文件的哪一行。
* **闭环式的 Prompt 工程自动化**：这是我最近最常用的功能。我通过在本地创建文件夹，并与cc进行对话，它能自动完成：**生成初版 Prompt → 批量产出测试 Case → 实际运行测试 → 输出对比文档 → 分析结果并自动调优 Prompt**。这一套全自动的“实验-反馈”链路，比手动调试快了数倍。
* **端到端的数据分析与清洗**：面对杂乱的原始日志或数据文件，我只需描述目标。它会自动编写 Python 脚本、在本地环境运行清洗程序，并直接输出分析结论。我不需要懂脚本怎么写，只需要看结果。
* **深度理解代码并生成 Demo**：这是最体现 cc 价值的场景。通过深度读取现有项目逻辑，它能帮我快速搭建出一个可运行的功能 Demo。在需求评审前，我可以先自己探路，判断实现路径是否合理。

**它帮我解决的问题：**

通过它，我可以先自主完成 80% 的探索工作，将模糊的疑虑转化为清晰的技术命题，再与开发进行精准对标。这不仅释放了开发的精力，更让 PM 在技术决策中从“旁听者”变成了“深度参与者”，沟通效率与专业威信得到了质的飞跃。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=188981c17f794f5fa26b93786bb443f8&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7a7b78532aaa4a0ca886fbcf1e5304fe&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2979c349bb7340c5964beeed95e69845&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b690d7fd842d4b2eba18d8b56c59b238&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a0b4cc7ecfe843f89c31256dc6acc756&docGuid=e6u5JzsiUedZ2a "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=42fdc4f6fdd64208905760d9eb3187bf&docGuid=e6u5JzsiUedZ2a "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4d1bd67bebcc4d3b99b88a29c117078a&docGuid=e6u5JzsiUedZ2a "")


---

## 四、Dodo —— 连接内部资料的即时助手
**解决什么问题：**

日常工作中有很多即时性的问题，比如「上次那个需求评审的结论是什么」「Q2 OKR进展到哪里了」，这类问题问通用AI得不到答案，但Dodo连接着内部资料库，可以直接回答。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5e285654485b48f19c75a7f7b6f1d599&docGuid=jXYado60Zxjihj "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2bac75266a6449f79158360d77b34486&docGuid=e6u5JzsiUedZ2a "")
**为什么我更倾向用Dodo而不是通用大模型：**

||Dodo|通用大模型|
|-|-|-|
|内部资料查询|✅|❌|
|如流文档访问|✅|❌|
|联网最新信息|一般|✅|
|创意发散和写作|一般|✅|

**使用场景：**

* 查如流文档里某个功能的历史讨论
* 问某个需求上次评审的结论
* 查询组内OKR和项目进展
* 定时任务每天早上发布竞对的更新
* 将群Q&A直接沉淀到知识库
* 用dodo来画可交互原型
* 用PRD/iCafe卡片来写changelog

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fc34c10d0a9c4dacaed961ef1e97c6cd&docGuid=jXYado60Zxjihj "")
![cc进行测试效果分析](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=332f22011d64468b96d093f669339ac7&docGuid=e6u5JzsiUedZ2a "cc进行测试效果分析")
![dodo进行测试效果分析](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=de3e86a162fe46f1bc9a41c93e060265&docGuid=e6u5JzsiUedZ2a "dodo进行测试效果分析")
![dodo生成的翻译软件原型](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b4621586b9204421b664cde5e3ca2b4b&docGuid=e6u5JzsiUedZ2a "dodo生成的翻译软件原型")
![dodo将网页版原型改为app](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=04e574df56734c4c9fc7f0826b720d97&docGuid=jXYado60Zxjihj "dodo将网页版原型改为app")
![对话dodo，要求生成竞品对比文档](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fb210b6aa96c47169887783e0320f19c&docGuid=jXYado60Zxjihj "对话dodo，要求生成竞品对比文档")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=973a1356e3ff407ca4e21df89cf8acc4&docGuid=jXYado60Zxjihj "")
dodo生成的竞品对比文档：[百度翻译App竞品对标分析](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/4RXBU2nBRw/0kYXAlOvBFahei?t=mention&mt=doc&dt=doc)

**简单说：Dodo是我们日常工作的私人助手，一切你想让别人帮你做的事，都可以先让dodo试一试**

---

# 写在最后：从“工具革命”到“逻辑重构”
这四款工具构成了我目前 AI 提效的四块拼图，它们各司其职，击穿了 PM 不同环节的痛点：

* **NotebookLM：** 实现从海量资料到核心洞察的**快速提炼**；
* **Figma Make：** 实现从抽象想法到具象原型的**敏捷验证**；
* **Claude Code：** 实现从业务逻辑到技术实现的**无缝对话**；
* **Dodo：** 实现从通用智能到业务场景的**深度对齐**。

它们并非简单的替代关系，而是通过全链路的组合，将 PM 从琐碎的执行中解放出来。

#### 站在 AI 时代的风口，关于 PM 未来的三点思考：
**1. 交互对象的演变：从“人机交互”到“Agent 协同”**

未来的产品可能不再仅仅服务于自然人。随着生态的开放和 CLI（命令行界面）的普及，我们会看到越来越多“给 Agent 使用的产品”。这意味着 PM 不仅要考虑人的视觉体验，更要考虑机器的逻辑读取效率，软件生态将通过 Agent 实现真正的深层打通。

**2. 核心竞争力的迁移：从“生产信息”到“高阶决策”**

当 AI 可以写 PRD、画原型、调代码时，PM 的价值将向两端延伸。一端是**独立思考的能力**，在算法给出的无数选项中，洞察那 1% 真正有价值的机会；另一端是**决策的质量，**未来 PM 的核心竞争力，不在于你操作 AI 有多熟练，而在于你能在复杂变量中，拍板决定产品走向何方。

**3. 责任的终点：AI 可以交付结果，但不能承担责任**

这是我认为 PM 存在的最底层逻辑。**AI 可以给出最优解，但它无法为失败“扛雷”。** 产品的成败、团队的士气、对业务目标的最终承诺，这些充满人性的重担永远由 PM 肩负。在 AI 时代，PM 不仅是“产品定义者”，更是“最终责任人”。



**PM 存在的必要性：独立思考、果敢决策、终极负责。**

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
