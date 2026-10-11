---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "Notex: 厂内可用的 Google NotebookLM 平替产品"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Notex 厂内可用的 Google NotebookLM 平替产品.md"
---
Notex: 厂内可用的 Google NotebookLM 平替产品

#### 🧑‍🏫 案例作者：[@晁岳攀](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：办公、通用
#### 🔧 使用工具：Onetool、Nano Banana、Gemini、Ducc、知识库、NotebookLM
#### 📒 案例概要：Notex是我厂内部的NotebookLM的一个平替产品，可以实现资料的智能化分析和挖掘，提供信息图、幻灯片、深度分析等功能
## 概述
NotebookLM 是谷歌的一个 20%时间的开发的实验项目发展起来的谷歌产品，是目前谷歌 AI 产品在炎手可热口碑爆裂的产品之一，是和 nano banana 一样深受大家好评的谷歌产品。



NotebookLM 是一款强大的 AI 笔记工具，一键上传资料，NotebookLM 就能迅速阅读并整理好，并且可以生成信息图、幻灯片、播客、视频等多种分析资料，同时你也可以通过 Chat 的方式和它进行交互和资料挖掘。



产品的确是好，但是毕竟还是人家的产品，尤其在国内，想使用它还是比较麻烦的。同时这个产品适合谷歌的其他产品绑定的，比如 LLM、比如 Google Docs、youtube，它都是围绕的谷歌的产品而做。另外，出于安全的考虑，大厂也不会把自己私密的文档放到 NotebookLM 中去分析。



所以，有了希望能够在厂内部署私有『NotebookLM』的需求。Notex 应运而生，可以部署在厂内，它可以结合知识库的文档，分析私有的数据而不担心泄密，同时也可以实现 NotebookLM 丰富的功能和强大的能力。



厂内 notex 地址： [https://notex.weiyun.baidu.com/](https://notex.weiyun.baidu.com/)



首先让我们回顾 NotebookLM 的历史，看看谷歌高层如何独具慧眼，发掘并发展 NotebookLM 这一产品的。



## NotebookLM 历史
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fb2b54219a1f468dbbaaee66e7efe738&docGuid=lHSbPCzZuCIlqS "")
### 缘起：20% 时间里的“小火苗”
NotebookLM 的传奇始于 Google Labs 团队内部一个名为 **Project Tailwind** 的原型。最初，它只是资深产品经理Raiza Martin利用谷歌的‘20%时间’机制（该机制鼓励员工探索个人兴趣）开发的试验品，旨在解决知识碎片化时代的痛点：让用户上传文档、PDF 甚至视频，由 AI 提炼要点。

Google Labs 负责人 Josh Woodward 对这个创意一眼相中。为了打破大公司内部的官僚壁垒，他采取了一系列“非常规”举措。他邀请了从未在任何公司任职的科技作家史蒂文·约翰逊（Steven Johnson）担任‘创作总监’，让写作者的直觉与工程师的算法发生碰撞。

### 破局：Discord 里的“草莽气”
在 Woodward 的支持下，团队展现出极强的初创色彩。他们拒绝了传统的内部封闭测试，而是直奔开发者云集的 **Discord** 社区。面对高管“为什么要用第三方聊天软件”的质疑，Woodward 留下一句简洁有力的 **“Let them cook（让他们放手去做）”**。

这种接地气的开发模式让 NotebookLM 迅速迭代。到 2024 年底，该社区成员已突破 20 万。Woodward 甚至在内部设立了“Block”工单系统，专门解决算力审批等资源障碍，确保这支小团队能以硅谷初创公司的速度奔跑。

### 进化：从 Project Tailwind 到 Gemini 驱动
2023 年 5 月的 Google I/O 大会上，Project Tailwind 正式更名为 **NotebookLM**（LM 意为语言模型）。Woodward 在台上展示了它最核心的灵魂：**“基于来源的 AI（Source-grounding）”**——AI 提供的每一个答案都会标注原文出处，彻底解决了幻觉问题。

进入 2024 年，NotebookLM 迎来了跨越式的发展：

* **底层重构：** 2024 年 6 月，NotebookLM 正式接入了 **Gemini 1.5 Pro** 模型。得益于该模型长达 **200 万 token** 的超长上下文窗口，用户能够一次性向 AI 输入数十万字的研报、数小时的会议录音，或是数百页的课本内容。
* **多模态突破：** 它不再仅仅处理文字，而是进化成了一个全能助手，支持 Google Docs、PDF、文本文件、Google Slides、网页链接，甚至包括 **YouTube 视频和音频文件**。

### 引爆：Audio Overview 的“出圈”时刻
真正让 NotebookLM 在 2024 年下半年红遍全球的，是其创新的 **Audio Overview（音频综述）** 功能。

用户只需一键，AI 就能将枯燥的文档转化为一段**极其自然的“双人对话播客”**。两个 AI 主持人将模仿真人，插科打诨、互相纠正，并深入浅出地探讨文档内容。这种极具情绪价值和陪伴感的交互方式，让 NotebookLM 瞬间从生产力工具变为社交媒体上的爆款，被用户誉为“谷歌近年来最令人惊艳的产品”。

### 现状：科研与创作的“第二大脑”
如今，NotebookLM 已从一个默默无闻的实验室项目，成长为谷歌 AI 版图中最具口碑的应用之一。它不仅证明了 Woodward 识人用人的独到，更验证了在大型科技公司内部，小团队通过深度社区互动与快速迭代，依然能创造出改变规则的产品。

## Notex 的历史
[notex](https://github.com/smallnest/notex) 本来是我的另外一个开源的智能体开发框架 [langgraphgo](https://github.com/smallnest/langgraphgo) 的 showcase 项目，用来展示 langgraphgo 的快速智能体开发的能力。



langgraphgo 是 langgraph 的 Go 语言版本，提供了 70+的开发示例，但是我觉得还不够，因为我想要一个『非 demo』的项目，能够充分展示 langgragphgo 能力的产品级的产品。我是 NotebookLM 的深度用户，所以我想开发一个类似产品。



虽然 NotebookLM 是谷歌非开源的项目，但是从它的产品特性分析，它背后的技术和实现方案从实现难度上不会太困难，并且也适合模块化的逐步实现。



得益于最近 vibe coding 能力的快速发展，我使用 claude code + GLM 4.7, 利用数周的业务时间和周末时光，快速建立起 notex 的初始版本。



安全与企业效率平台部门在 AI 内化和 AI 工具的开发，在陈洋总的大力支持下，在宗帅、王超等多位同学的大力支持下，我们将 notex 迁移到厂内，并结合厂内的同学的痛点，集成了厂内 SSO 身份认证， 可以导入知识库，录音转录资料，类似 Manus 内置 20 个左右对话场景，包含 10 左右的 transfomer 等功能，方便厂内同学使用 NotebookLM 类似的功能。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f929752eee614790ac8d54a75df5c0cb&docGuid=lHSbPCzZuCIlqS "")
## Notex 介绍
本质上，notex 是谷歌 NotebookLM 平替，最初它也是模仿 NotebookLM 的功能和 UI 实现的，这也减少了大家对 notex 的陌生感，实现了开箱即用的效果。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bd7277baef2248bd8d4ad6637b3cbe46&docGuid=lHSbPCzZuCIlqS "")


当你访问首页的时候，自动会使用公司的 Auth 进行身份认证。如果你还没有登录，可以点击右上角的登录按钮进行登录。



最上面一栏显示大家分享的优秀的笔记本，你可以欣赏别人生成的笔记本的效果。



最下面是你的私有的笔记本列表。



你还没有笔记本，创建一个吧。点击 

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e170064aae3e451882480882cc2c0082&docGuid=lHSbPCzZuCIlqS "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ca0a91306d204aeebb60c4478436ace9&docGuid=lHSbPCzZuCIlqS "")


创建完毕后就自动进入这个笔记本的工作区：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9edbb78e924d49a6abef0dd70820792d&docGuid=lHSbPCzZuCIlqS "")


### 导入资料源
首先你需要导入资料源，这是你的笔记本的资料。notex 会分析和索引这些资料，存储到 RAG 中。这些资料是你后续分析和会话的基础。



notex 支持从各种数据文件中抽取资料，比如 pdf 、docx、pptx、文本文件、网页、度厂的知识库、音频(播客、会议录音)等。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1560bc0ee401403fa49c41f1dfe1a4f7&docGuid=lHSbPCzZuCIlqS "")


比如我们导入采访刘震云的播客音频文件：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=66e54d6aa34f486bbe0ccbbaf3a4d95b&docGuid=lHSbPCzZuCIlqS "")


比如我们导入一个网页：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=46cc61cd22274b50afa5072decbd8830&docGuid=lHSbPCzZuCIlqS "")


这个例子中我们导入了播客定位音频、播客的网页版介绍、知识库的《咸的玩笑》的一个简单介绍、《咸的玩笑》电子书：在这个例子中，我们导入了以下内容：\n- 播客定位音频\n- 播客网页版1的介绍\n- 知识库中《咸的玩笑》的简单介绍\n- 《咸的玩笑》电子书

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=df07ffca9b0e4dcb86d3cf5456bd3684&docGuid=lHSbPCzZuCIlqS "")


点击资料卡片可以显示此资料的细节。

### Transformer
这些资料准备好后，我们就可以使用 transformer 对这些资料进行转换和分析。



比如我们可以生成摘要：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=30aca7f9bdc54ca98ccf0163f4b2be8b&docGuid=lHSbPCzZuCIlqS "")


比如为这些资料生成信息图：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=117ae3c6bc0c4ae98041a58ec82ae19b&docGuid=lHSbPCzZuCIlqS "")


比如生成幻灯片，你还可以下载此幻灯片的 pptx 文件：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=362e18192d534474ad368da3ef6b27dc&docGuid=lHSbPCzZuCIlqS "")


生成的笔记都可以在笔记列表中查看，点击笔记卡片可以查看此笔记的详细内容：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4d665bd86f9a47d092c2ba093ea315aa&docGuid=lHSbPCzZuCIlqS "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c32f23a726f64f3aab2d840cc40e4862&docGuid=lHSbPCzZuCIlqS "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fe798c46700a4442ad7472077eb949eb&docGuid=lHSbPCzZuCIlqS "")


### 会话
你还可以基于资料和 LLM 对话，挖掘更多的深层次的问题。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=37452db9867d4956a1a7a67874b6dcdb&docGuid=lHSbPCzZuCIlqS "")
这一块类似 NBotebookLM+Manus 的功能糅合体。

一开始是对内容的总结，并提出了三个有深度的问题，你可以点击问题询问 LLM。



你也可以在输入框中输入你自己的问题，和 LLM 交互。



提示词场景中还有 20 个内置的提示词，这是专家总结的 NotebookLM 最常用的提示词，我移植到了这里。比如我们使用『矛盾猎人』这个提示词，挖掘这些资料的矛盾之处：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d620c6d3011b4f1a98c97a397df6f815&docGuid=lHSbPCzZuCIlqS "")


最佳实践是你和LLM交互完某个方向的问题后，新开会话去讨论其他方向的问题，这样可以减少会话的上下文，减少Token的使用和LLM的幻觉。历史会话自动保存到会话历史中：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=07ef2266e95b41f1bd9a4cd99713fa90&docGuid=lHSbPCzZuCIlqS "")
### 总结
Notex 实现了NotebookLM大部分的功能，并且实现了自己特有的一些功能，使用上和NotebookLM类似，可以作为厂内的NotebookLM的平替产品使用。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
