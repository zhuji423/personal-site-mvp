---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "开局一个文档，我该怎么办？——以 Ducc 为核心，全流程智能落地应用"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\开局一个文档，我该怎么办？——以 Ducc 为核心，全流程智能落地应用.md"
---
开局一个文档，我该怎么办？——以 Ducc 为核心，全流程智能落地应用

#### 🧑‍🏫 案例作者：[@王堃](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：研发全流程
#### 🔧 使用工具：Ducc、Claude、Figma、iCafe、其他
#### 📒 案例概要：AI全流程辅助软件开发，从需求到代码、测试、管理，大幅提升效率。


[文档目录]
## 概述
一个人，一份需求文档，如何用 AI 在极短时间内实现完整功能的落地？本文将不仅仅停留在前后端代码的生成的优化方案，而是聚焦于整个软件的开发流程，从需求文档、PRD、文档、前后端代码、测试以及项目管理，全方位借助 AI 能力进行整个研发流程的还原，并分享我的实战思考与心得。



**关键字：Ducc，Claude Code，Zule，Visily，Figma，Skills，Mcp，Rules，Agent Team；**

## 痛点
**原有开发流程：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aaa1945f73084dee824b4f83c744928d&docGuid=fLrlF3HC0xKyed "")


**主要痛点：**

* **角色缺失**：我只是一个后端研发同学，我根本不会什么 PRD 、前端、原型图；
* **时间问题**：时间紧张，没有过多人力和时间放到这个简单的小项目中；
* **缺少需求梳理**：缺乏产品经理对需求进行梳理；
* **测试覆盖不全面：**QA 测试和测试用例编写占用 QA 时间，有可能遗漏case；
* **项目管理重复性工作过多：**项目管理繁琐，简单重复性的创建 icafe 卡片。

## 关键收益
|编号|关键步骤|人工时间|AI生成|备注|
|-|-|-|-|-|
|1|PRD生成|1-2天|**10分钟**||
|2|原型图|1天|**5分钟**|完全由AI生成|
|3|API文档|1天|**10分钟左右**|完全由AI生成|
|4|前端代码|5天|**共1天**|完全由AI生成|
|5|后端代码|3天||99% 由 AI 生成|
|6|测试|1天||完全由AI生成|
|7|ICafe卡片建立|30-40分钟|**10分钟**|虽然这部分内容在消耗时间上提升不算很多，但是能够让工程师在这个方面上不需要去投入任何精力和时间，尤其是大量卡片需要建立时，会让人觉得烦躁|



整个代码的生成过程，并不是不需要人工介入，在某些地方仍需要人工干预，但 99% 的任务都是由 AI 完成，甚至前后端代码在夜里完成，实现 AI 帮我打黑工。开局一个需求文档，后面全靠各种 AI 帮我来打工。原本需要产品经理、前端、后端、测试等多角色需要工作一周多的工作量，在AI的帮助下一天完成。

## 需求生成
整个需求开始开始，手中的资料只有一个数据库设计表，如果直接丢给 AI 去生成页面和代码，AI 将难以理解表与表的对应关系，因此前期需要在需求文档中提供数据库 E-R 图以便于 AI 助手更好的理解我们的需求。（需求文档整体耗时大概在30分钟，其中包含E-R生成时间）。需求文档如下。

[6. BSP 权限管理系统后台需求梳理](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/gEbfgwxlHm/sPyNicPkJad4wh?t=mention&mt=doc&dt=doc)



一下是生成需求文档 E-R 图的交互，在生成 E-R 图的时候，其实遇到了两个问题，第一个问题是 Ducc 更加习惯于生成 MD 格式的文档，即使我告诉他我要生成 E-R 图，但是对于人来说一张图片以 MD 格式进行表现显然是不符合我们的认知的，也不直观；第二个问题是它生成的生成图片质量问题，第一次生成图片过于挤，表于表之间重合，需要进行二次交互重新进行生成。整体从 python 工具的安装到图片的生成大概耗时在 15 分钟左右，虽然进行了多轮交互，但是从生成图片的时间上看，这个速度也是快于人工进行手动绘画。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a61410aa5088412fa94699432fb606de&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=03df92366b894eae954af33d7d387464&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=87579ab89eae482b96639e06f34d6d7b&docGuid=fLrlF3HC0xKyed "")
## PRD 文档生成
产品经理在软件开发的生命周期中，产品经理在其中扮演着重要的角色，一份好的 PRD 文档能够指导前端、后端以及测试同学进行软件的研发。在 PRD 文档中明确本次研发任务需要做什么、前端页面如何与用户进行交互。在生成 PRD 时，不要让 AI 自由发挥，而是给出 PRD 的模板，让其根据 PRD 模板生成相关文档，可以借助[流知识库 MCP](https://console.cloud.baidu-int.com/onetool/square/server/207) 能力和[知识库skills](https://console.cloud.baidu-int.com/onetool/skills/154) 对需求文档进行阅读和创建，提示词如下：

```
当前项目的需求在百度的知识库中，我已经给你配置了读取知识库的MCP能力，你可以通过知识库的MCP能力读取到该需求文档，需求文档地址为：https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/gEbfgwxlHm/sPyNicPkJad4wh，

你要仔细阅读需求文档，尤其是是数据库的E-R图，请参照 PRD文档规范，生成本次需求的PRD，并且在 PRD 文档中要给出前端页面是如何与用户进行交互的，交互的逻辑是什么

PRD文档规范地址为https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/RB2EPv7tDS/TEF7HK03Rk56BW，

生成的PRD文档放在本地的/Users/wangkun/Desktop/goProject/bsp-iam/docs下

并且上传到https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/gEbfgwxlHm/NFPVtTqp5tsfT_目录下一份，文档名称为 BSP 后台管理系统 PRD
```


到此已经完成 Ducc 和如流知识库的打通，生成的PRD文档以自动上传到知识库中：[7. BSP 权限管理系统后台 PRD 文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/gEbfgwxlHm/nJdqQ4DrssbEEG?t=mention&mt=doc&dt=doc)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3afc97ad4271479396dea43f09f34b10&docGuid=fLrlF3HC0xKyed "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9cf41e7665c6482cae974bb0ebe0563e&docGuid=fLrlF3HC0xKyed "")


## 原型图生成
在前期已经生成好了相关的 PRD 文档，但是对于我这样一个审美比较差的后端开发来说，存在几个比较大问题：

* **主观审美：**审美差，画出来的图很丑；
* **专业性：**非专业人员，软件用起来不顺手，不会操作；
* **时间消耗：**耗时过长，简单的页面也需要耗费天级别的时间完成;



经过调研目前厂内没有专业生成原型图的相关 AI Agent，这里使用一个厂外的原型图生成的工具 [visily](https://www.visily.ai/)，该工具支持时使用自然语言描述和图片方式生成设计稿，而且可以进行多轮对话，对设计稿进行修改。在此之前，我们已经有了产品的 PRD 文档，可以将 PRD 文档内容传递给它，让他给我们生成一份设计稿，这极大的节省了时间，本次生成大概只耗费了 5 分钟，具体交互如下：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f86f0bc11b954b348bb230c363338443&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=21212e3f14b44dcfa0594d5d9ac348b9&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f776a1268eac42ba86cd6c4db29a6f0e&docGuid=fLrlF3HC0xKyed "")


该工具支持导出 PDF、图片、Code（React、Vue和Html，并可以指定组建，但是收费）、导出到Figma（收费）等，生成的设计稿图片如下：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=891c7a767036484695c79dc6c316cefc&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c2b681fc1c0f418aa4dcf214934b2cbd&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dfae759a8e574f819dd501059a3e5ae3&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fda3e55a7d2446079aab43cfd6dcae32&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8aee674ac46d4ed8a301972f14a38cd0&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6aec29f9f4204aef9504cd1a7e92b372&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1b23009ae21c4b009aed10392efe5eb5&docGuid=fLrlF3HC0xKyed "")
## 前后端代码生成
### 7.1. 生成前端基础页面
在此之前，使用过几次 Ducc 的 Agent Team 的方式同时去生成一次性生成 API 接口文档、前端代码、后端代码和项目管理 ICafe 卡片，发现前端页面还原度并不是很好，经常出现前端页面与原型图还原度低，缺少交互部分等问题，点击页面经常报错，出现这个问题由以下几个方面导致的：

* 完整的 PRD 文档一次行传递给 [visily](https://www.visily.ai/) 的时候，它并不能根据 PRD 文档中的用户交互内容虽然已经写清楚了，但是有一部分原因是因为上下文太长，其不能很好的将 PRD 文档中交互的内容生成对应的原型图，只能生成少量的交互图；
* Ducc 对于根据图片生成前端代码的能力较弱，导致生成的前端页面质量不高；
* Ducc 的大量的任务进行处理的时候，可能会出现上下文的遗忘，记不住一开始给的 Prompt，做的任务过多，导致质量下降，需要很多轮人工干预；



解决方案：

* 既然以目前大模型的能力不能一把将任务全都完成，那就将任务拆解，将大任务拆解成小任务，将前端的基础代码生成，用 mock 数据代替真实数据，后续的任务就变成对接后端 API 用真实数据来代替 mock 数据即可；
* 既然大模型对于图片这种格式的原型图还原度比较低，那我就直接给他代码，这里通过 [visily](https://www.visily.ai/)  导入到 Figma（开了会员，动用了钞能力），Figma 官方提供了 skills 可以将原型图导出为代码，可以参考[使用Figma MCP还原前端设计稿](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/CIkDF2HdNp/BGGav_8G2q/ehwQ_SgGWcr-KE?t=mention&mt=doc&dt=doc)进行相关资源的和能力的配置，然后告诉大模型我们使用的技术栈，让他先读懂原型图的代码，在按照我们的需要的技术栈生成我们的代码就好了；
* 针对 [visily](https://www.visily.ai/) 生成的原型图缺少用户交互的问题，在生成了基础代码之后，完全可以使用自然语言的描述让 Ducc 帮我生成用户的交互。



针对于上述的几点优化，可以看一下前后生成的前端页面的对比效果

![原型图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dd1e122041534134a4295c8ac3594fff&docGuid=fLrlF3HC0xKyed "原型图")
              优化前生成的前端页面（经过了很多轮对话后的效果）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c76d6a96eaf64cc4ad5cdf3ec5814ad0&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=752b84377a344208ab57c38b19dcaa70&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7f7ab200b70441688bea4d878832f679&docGuid=fLrlF3HC0xKyed "")
                                       优化后生成的前端页面

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=715e4d0f04064fc9bcbc00d2ee0659af&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e4e0048fec8c4eb583740e99bec5569f&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c6a821f83bcf47d08600a91193ca7445&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c5d4ac67f788418eaceaf54b16184cea&docGuid=fLrlF3HC0xKyed "")


以下是生成前端基础代码与Ducc交互的一些过程，期间的页面也会出现一些小问题，比如图标大小，目录的缩进等问题，但是经过自然语言的交互，均能进行修正，且由原型图生成设计稿还原度在可接受的范围内，整个过程没有自动动手写一行代码，全部由 Ducc 和其他 AI 工具生成

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1e966b5d89894146be58fcf9f76a14c0&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6b3251aebf5b4647aaac5c44136ec2fa&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2e351f92530c40ea865f3960c0a68413&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6f2f7d10e0624878804124befabf1fc1&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ff9accd1b97d4858bab3caa5136df397&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=65ed7d647e3342bebc22d5662871842a&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=18b68acf1c854263bbcde97b16d5cbba&docGuid=fLrlF3HC0xKyed "")


### 7.2. 生成后端开发框架
同样在后端开发的时候，也遇到了前端相同的问题，在 Agent-Team 的方式下，在生成后端代码不符合现在团队的开发风格和开发规范，由于这次任务较大，因此即使在任务开始时，给了大模型足够多的 Prompt，在后续生成的代码依然不符合规范，没有达到理想的效果，而且在前期输入过多的 Prompt 一方面会不能将研发规范说全，会有遗漏；第二方面，大模型在这种比较长的任务中会对上下文遗忘，达不到效果。

那既然直接给出 Prompt 的方式对于从零到一的项目效果不好，那就可以将代码的开发框架生成好，再给出框架的说明文档，以及研发注意事项以及规范，大模型更擅长做的事情是读现有代码，完成之后的代码，这样大模型在生成后续的代码时，就有参照代码了，而不是胡乱进行发挥。

在日常的开发中，其实在小组内部已经沉淀了一套生成代码框架的 rules 和，在这里直接借助厂内 zulu 的能力，让其自己生成代码开发的脚手架，整体效果来看，符合预期，具体过程如下：

* 交互过程

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc3091aca95b477dab84297c20d87fb9&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=32b30f5a4d0e428c8f1c9d8fc3d227cf&docGuid=fLrlF3HC0xKyed "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=86cc8a5f145b467b81ed5e6c5c0ee583&docGuid=fLrlF3HC0xKyed "")


* 生成代码效果如下

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=78a14e83cca345509c902d1ab47e73b7&docGuid=fLrlF3HC0xKyed "")




### 7.3. 项目代码生成
在现实中的软件开发工作中，各个职能的同学在一起进行交流，架构师根据 PRD 文档对整个系统和接口接行设计，前端同学根据系统设计和接口文档完成前端代码，后端同学也需要根据系统设计和接口文档完成后端代码，并且前后端同学进行交流完成代码的联调整，完成ICafe卡片的状态流转，测试同学完成对整个系统的测试工作，将相关的问题反馈了研发同学，几名不同角色的同学形成一个团队，团队之间的同学互相交流完成整个项目的研发工作。

### **传统开发团队**
### **Agent Team**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=20d902da401a48efbf61cdd57ace2908&docGuid=fLrlF3HC0xKyed "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0a2b637195ba4cb8acc1f6d5f3446099&docGuid=fLrlF3HC0xKyed "")
 使用 Ducc 的 Agent Team 方案来模拟人工的开发团队，Agent Team 的优势在于每个 Agent 都是一个独立运行的 Agent，对比 SubAgent 方案的优势在于每个 Agent Team 之间的成员可以自由的交互，消息不必通过Leader Agent 进行传递，这样极大限度的模拟了人工团队的开发模式，这样做有如下的好处：

* 多 Agent 并行工作，提高代码生成速度；
* 将一个大的软件研发任务，分散到不同的 Agent 上，让每个 Agent 只专注于做自己的事情，上下文友好；
* 多个 Agent 分工明确，统一配置[知识库 MCP](https://console.cloud.baidu-int.com/onetool/square/server/207)、[知识库 Skills](https://console.cloud.baidu-int.com/onetool/skills/154) 和 [ICafe Skills](https://console.cloud.baidu-int.com/onetool/skills/151) 打通产内软件研发流程周边工具，方便项目的管理；
* 可以针对不同角色的 Agent 出现的问题进行独立的交互，让 Agent 只注重自己的问题；
* 在建立团队的时候，同一个角色可以建立多个 Agent，充分利用 Agent 之间可以互相讨论互相纠正的能力（比如建立两个后端程序员，两个前端程序员，一个进行代码书写一个进行代码检查）；



生成代码的 Prompt 如下：

```
我需要一名系统设计负责人，它能根据知识库中的PRD文档https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/gEbfgwxlHm/nJdqQ4DrssbEEG完成系统的接口设计，

接口文档格式参考知识库中的https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/41FsefhkDo/5XoHBngk87X3QQ格式，接口数据会返回code(string类型)，message(string类型)，data(any类型)，当接口正常返回时，code的值为空字符串，否则为错误的状态码

每个接口是一个文档，生成的接口文档需要同时保存在/Users/wangkun/Desktop/goProject/bsp-iam/docs目录下并且给我上传到知识库的https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/41FsefhkDo/T4jY-Hyib4bppU目录下，操作知识库文档的skills我已经给你配置了，你可以用过其对知识库文档进行操作；

并且需要告知给前后端的研发同学接口文档在哪里，让其进行阅读并按照接口文档进行开发。

我还需要两个后端开发，基于接口文档和后端研发规范完成代码编写，研发规范文档位于/Users/wangkun/Desktop/goProject/bsp-iam/.comate/rules/default.mdr，

后端在进行代码开发时，必须遵守后端研发规范文档中的内容，接口样例位于/Users/wangkun/Desktop/goProject/bsp-iam/src/internal/apps/apis/apis中，你必须严格按照研发规范文档和接口样例生成接口代码，每个文件夹是一个接口，不允许多个接口写到一个文件中！

后端同学在开发过程中，我已经写了常用的框架中的函数是如何使用的，后端同学在进行写代码的时候必须对其进行参考，其位于/Users/wangkun/Desktop/goProject/bsp-iam/.comate/rules/backend.mdr中，你需要在开发过程中仔细阅读
`
数据库对应golang的model可参考/Users/wangkun/Desktop/goProject/bsp-iam/src/internal/pkg/models/iam中，每个文件是一张数据库的表，在代码中你如果想操作数据库，可以使用`New表名`的方式直接，如`NewLocationMainModel`就可以对`location_main`表进行操作

后端代码需要写入到/Users/wangkun/Desktop/goProject/bsp-iam/src目录中，这两名程序员一个人写，另一个去判断他写的对不对，是否符合规范，两名后端开发需要进行沟通完成代码书写，后端程序员写完一个接口需要上报给用户，用户会进行review用来发现其中的问题

我需要两名前端开发工程师，前端使用Vue3+elementui-plus的方案进行开发，网络请求工具请你使用axios进行请求，前端的页面大体已经完成，代码位于/Users/wangkun/Desktop/bsp-iam目录中，但是缺少和后端对接API接口，现在前端的数据都是假数据，前端同学需要根据后端的接口完成数据增删改查操作，

同时前端开发工程师也必须遵照接口文档对项目进行开发，前端工程师必须完成接口文档的全部接口，确保开发出的代码正确运行，两门前端工程师也是，一个人去写代码，写好了另一名前端工程师进行检查；

前后端工程师必须完成前后端项目的连调，确保每个接口都能访问通顺；

还需要一名测试工程师对功以及接口进行进行测试，测试工程师必须对前后端代码进行测试，输出详细的测试报告和测试功能点，测试报告也需要生成对应的文档，确保前后端所有接口均可以正常访问通，并且代码没有BUG，如果测试出现BUG请你联系对应的开发同学进行修正；

测试同学必须完成前后端联调整，确保前后端交互不会报错，必须输出测试文档。

我还需要一名做项目的人员，需要帮我去icafe中建立卡片，进行项目的管理，建立卡片的标准为每一个story卡片是一个测试人员可以独立测试的功能，每个story下可以有一个或者多个task卡片，比如一个接口就是一个story卡片，

这个卡片下面的task是完成这个接口要做的步骤，这次迭代的卡片需要放在ICafe的NP-SPRINT-BSP空间的"待优化卡片"中创建卡片，负责人为wangkun40，卡片内容同卡片标题,不要怕task的数量多，虽然数量多但是你也必须建立对应的task卡片,

我已经给你配置好操作ICafe的skills了，你可以进行调用；

整体功能和测试完成之后先不要销毁团队，需要等我来验收，我验收通过后才可以销毁团队。
```


虽然在上述提到了很多的优化和优势，但是在生成代码的过程中依然会存在一些问题，比如代码首次生成还是有报错等问题，需要二次人工介入进行提醒，但是相比之前的方案，有了很大的提升，**交互的次数明显变少，首次生成的代码质量有了大幅度提高**，本次代码生成工涉及到了 **26 个 API 接口**，前后端共生成了 **29836 行代码（11345 +18491），ICafe卡片 86 张，QA测试报告一份。**

![前端页面](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=90716ddd25a948cebcee0613b031acd7&docGuid=fLrlF3HC0xKyed "前端页面")
![前端代码](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=493ebe7c688840f089e9f5268acfc069&docGuid=fLrlF3HC0xKyed "前端代码")
![后端代码](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c8174db3399440179823ea29e2976a10&docGuid=fLrlF3HC0xKyed "后端代码")
![QA测试报告](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e3d05746f914426eaeb108887f8ca374&docGuid=fLrlF3HC0xKyed "QA测试报告")
![API接口文档](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ed0c674f409a492ba4653aadd33b043b&docGuid=fLrlF3HC0xKyed "API接口文档")
![ICafe卡片](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=184ded237acf42a2840a8c0dccb9a05d&docGuid=fLrlF3HC0xKyed "ICafe卡片")


*在此之前其实也试过其他的方案，结果都不尽如人意，比如将所有任务都交给一个Agent、原型图图片生成前端代码等等尝试，才总结出上述一套代码生成的方案。*

## 总结
在本次项目实战中，遇到了和很多问题，回顾整个过程，提炼出一套适用于代码开发全流程的经验：

* 做专业的事情，使用专业的 AI 工具会加省时省力；
* 不要让大模型从 0 到 1 的开发一个项目，尽最大限度给出大模型参考代码，远比给出 Prompt 更有效率，让大模型续写会更有效率；
* 让每个 Agent 只专注做自己一件事（比如使用 Claude 的 Agent Team 模式），不要让一个 Agent 既做前端又写后端；
* 将大任务分解为小任务，让大模型循序渐进的去完成每一项任务，而不是一口气完成全部工作内容；
* 不要让大模型进行多模态任务，它对于代码和自然语言的理解远高于对于图片的理解；
* 将代码研发规范和常用函数进行文档沉淀，让大模型在写代码的时候，先读文档，再写代码，避免其在不知道代码框架已经封装好了相关的函数；
* 注意在日常使用 AI Coding 时候的相关 Promot、mcp、skills、rules 的沉淀，将日常开发的经验封装为可执行、可传承、可迭代文档及技术资产。

## 展望
这次实践真正的意义不在于解决了什么样子的业务问题，而是让身处在 AI 时代的同学们清晰的认识到 AI 完全颠覆了原来的开发模式，它正在以极低的成本去解决一个团队需要做一周的事情，极大的解决了研发效率问题。以目前 AI 的能力还不能一把生成全部的研发流程，但是可以通过将任务进行拆解，运用多种 AI Agent 联合去完成一个大任务，这本身也是一种进步，以最小的时间和最高的效率来解决实际问题。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
