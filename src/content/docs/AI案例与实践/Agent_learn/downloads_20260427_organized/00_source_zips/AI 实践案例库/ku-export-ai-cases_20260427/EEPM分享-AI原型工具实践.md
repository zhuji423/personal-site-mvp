---
title: "引言"
description: "EEPM分享-AI原型工具实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\EEPM分享-AI原型工具实践.md"
---
EEPM分享-AI原型工具实践

#### 🧑‍🏫 案例作者：[@陈琦洁](https://ku.baidu-int.com?t=mention&mt=contact&id=06fa5780-fce7-11f0-b317-9930ce5a4471)
#### 🎬 案例场景：设计
#### 🔧 使用工具：V0
#### 📒 案例概要：本文分享了EE PM团队在AI原型工具实践中的阶段性总结，通过AI工具在需求梳理、原型设计、PRD编写及评审协同等场景中显著提效。AI工具帮助团队快速生成原型和文档，减少重复性工作，使PM有更多时间进行需求分析和设计思考。文章详细介绍了各场景的提效案例及AI工具的使用效果。
# 引言
从25年8月，EE PM团队就开始探索AI工具生成原型的实践，这和总监会上提出的 “3 prototypes” 要求刚好契合。

到9月，EE部门提出了移山计划[25Q4 移山计划](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/Hb6OQz5Jc7/OKJ5Rq7CXnQIei?t=mention&mt=doc&dt=doc)，推动全员深度践行 “Agentic 工作模式”—— 这项计划不仅覆盖 PM 团队，也联动各研发同学共同参与。为聚焦实践落地，PM团队就此正式成立两个专项小组： “AI原型实践小组”、 “PM AI Coding 实践小组”

今天我先分享下AI原型实践的阶段性总结：过去这段时间我们团队**10**个PM，累计上百个实际需求用到了AI工具画原型。实践中我们明显感受到，AI 工具能为产品全流程工作带来显著提效，尤其在交互流程复杂、功能体量较大的 feature 中，优势更为突出。接下来，为大家展开详细介绍具体提效的场景、需求等

# 什么场景可以提效
产品日常工作链路很长，主要由PM主导的 “从需求开始 —> 需求进开发”期间，其实每个工作场景都会有所提效：

[流程图]


以下是一些案例：

|**提效场景**|**AI介入前**|**AI介入后**|
|-|-|-|
|**需求梳理**|产品改版，搜集竞品进行分析，并梳理流程，预估耗时1-2天|AI快速收集资料，生成竞品分析与初步流程Demo，**可以节省1天**|
|**自己画原型**|PM手动画复杂原型，耗时2-3天|通过V0等工具自动生成原型，**由原2-3天缩短为2-3小时**|
|**PRD编写提效**|PM需基于原型手动撰写PRD，编写PRD约需要1天，人工编写原型和文档可能有差异|借助AI生成的内容，自动补充描述，由**1天缩短为半天**完成文档，整体文档结构、细节更完整及清晰，保证原型&文字一致性|
|**PRD评审协同提效**|传统评审依赖静态图文，沟通效率低，评审耗时至少1H|AI生成Demo直观展示交互细节，由**1小时缩短为半小时**对齐需求协同提效：UE&RD理解需求更快，需求交互细节更好，文字无法表达的可以通过DEMO表达评审时间更少 |
|**UE协同提效**|有些平台如CNAP，PM承担交互设计工作，一些需求需要设计，耗时1-2天|CNAP所有需求没有进交互，利用AI生成设计仅需2-3小时，**减少了交互参与+评审 2天***（建议： 需要交互规范&视觉规范作为知识输入，可以不用UE交互）*|



> **详细内容：**
> 1. 需求思路梳理：产品改版场景下，需求思路梳理是核心前置环节。团队需先广泛搜集行业内主流竞品及创新型产品，从功能布局、用户流程、交互体验、视觉风格等多维度开展对比分析，同时结合自身产品定位与业务目标，梳理出改版的核心方向、功能优先级及关键业务流程。该环节需投入大量时间进行信息搜集、整理与分析，常规预估耗时 1-2 天，且流程梳理的完整性直接影响后续原型设计与开发落地的准确性
> 2. 原型设计：原型设计是产品工作的核心环节之一，尤其针对多模块联动、交互逻辑复杂的中大型需求，PM 需手动搭建页面框架、设计交互流程、配置组件关联。复杂原型的绘制过程需反复调整细节（如页面布局优化、交互逻辑校验），不仅耗时费力，还需确保各页面风格统一、流程连贯，常规手动绘制耗时 2-3 天，且容易因人工操作出现细节遗漏
> 3. PRD 编写：手动撰写易出错且耗时，PRD 作为需求落地的核心文档，需基于原型完整呈现功能说明、交互规则、业务逻辑、异常场景等关键信息。传统模式下，PM 需手动对照原型逐模块撰写文档，不仅耗时约 1 天，还可能因人工同步不及时，出现 PRD 描述与原型设计不一致的问题（如字段名称偏差、交互逻辑遗漏），进而增加后续评审与开发的沟通成本。
> 4. PRD 评审协同：静态沟通效率低下，PRD 评审环节需协调开发、测试、设计等多角色参与，传统评审依赖静态图文文档进行沟通。由于静态内容无法直观呈现交互流程与功能逻辑，评审过程中易出现理解偏差，需 PM 反复解释说明，导致评审沟通效率低下，单次评审耗时至少 1 小时，复杂需求的评审甚至需要多次沟通才能达成共识。
> 5. UE 协同：AI工具能基于需求描述自动补全完整的交互逻辑，包括页面间的联动关系、操作触发的反馈机制、边界场景的处理规则等，生成的原型不仅包含页面布局，更自带连贯的交互流程。对于多数常规需求（如表单提交、列表筛选、数据详情查看等），AI 生成的交互逻辑已足够完整，无需额外进入专业交互设计环节；即使是中复杂需求，也仅需在 AI 输出的基础上进行少量调整，即可满足使用要求，减少很多交互设计时间
> 


# 哪类需求适合AI
在实践中，可以感受到：AI画原型并不是“输入一句话就能出图”，而是一个需要反复思考与调整的过程：

* 思考与需求转译：使用者需要先将需求梳理清楚，转化为AI能理解的描述（例如功能逻辑、信息层级、页面结构等）。这一步要求PM要表达清楚，有时候甚至需要详细描述，否则AI容易生成偏题结果
* prompt输入与生成等待：用户需多轮输入Prompt，不断尝试不同表述方式，等待AI生成原型。通常在2~3轮调整后，结果才逐步接近预期
* 结果审查与人工修正：生成后往往需要手动调整布局、命名、交互细节，AI更像是“原型起稿助手”，不是“一键完成工具”

**结合数据统计，团队成员大概一个月有40%左右的需求，适合用到AI原型工具，总结来看，AI原型工具和需求适配情况如下：**

**适合的需求：**

* 中大型Feature：交互逻辑较复杂的流程型需求，AI能自动生成完整的界面结构和交互逻辑，减少人工搭框架和布局的时间
* 新增页面、功能类需求：只要需求输出完整，AI可快速搭建整体框架，相较于在原有系统上调整，效果更优
* 内部评审、方向探索类需求：需要快速产出低保真原型用于讨论或头脑风暴，AI能快速提供参考版本

**不适合的需求：**

* 简单或局部修改类需求：典型场景有 截图替换、文案修改、样式微调、元素位置调整等。这类需求本身逻辑简单、改动范围小，通常人工操作几分钟即可完成。如果交由AI来处理，虽然看似“自动化”，但实际上需要额外投入时间进行说明和沟通——包括撰写Prompt、等待生成结果、再进行反复修正与比对。由于AI生成往往是“重新生成整块界面”，可能导致页面结构或样式被不必要地重构，甚至带来新的问题，最终仍需人工干预。在这类微型任务中，AI的生成周期（输入+等待+调整）反而比人工直接操作更长，整体效率反而下降



#  怎么算是好用的AI工具
按照以下维度进行对比，综合来看V0、Lovable表现最佳

总结来说，好用的AI工具可以不需要耗时很长、人工大量调整，就可以实现目标需求

* **功能完整性**：是否能覆盖原型设计的核心需求
* **交互逻辑**：是否符合用户使用习惯，比如页面跳转逻辑是否清晰、核心流程是否顺畅，无需大量手动调整就能满足基础使用场景
* **视觉样式：**设计美观度、和需求的匹配程度，比如整体风格是否统一、布局是否混乱，生成的视觉效果是否符合规范
* **生成速度**：生成效率情况，从输入需求描述（或上传草图）到生成完整原型的总耗时，是否能快速响应需求，单页面生成时间是否在可接受范围

*单个维度：5分满分，0-1完全不可用，2-3部分可用，4-5基本都可用；综合评分：单个维度评分加和  / 总维度数*

|**工具**|**功能完整性**|**交互逻辑**|**视觉样式**|**生成速度**|**综合评分**|**总结**|
|-|-|-|-|-|-|-|
|**V0 **|4|4.67|4|4|4.17|各项表现不错，给出参考的情况下，视觉设计OK，另外还**支持直接在页面上编辑**，比较方便|
|**Lovable **|4.33|3.67|3.67|3|3.66|对参考案例复用能力强， 0→1、**1→N 原型生成表现都还可以**|
|**Figma AI**|3.67|3.67|3|3.33|3.42|各方面表现比较平均，比较适合 0→1需求的原型设计，对复杂功能、1→N的需求处理能力一般|
|**Bolt.new**|3.67|2.67|2.67|2.33|2.83|生成速度与视觉设计均能力较弱，不太适合|



> **详细内容：**
> * **V0：**整体上手很简单，支持上传截图和版本管理，可回溯或合并历史版本，便于迭代和场景区分。给出参考，实现效果还可以，生成原型遵循页面风格，交互逻辑完整性高。视觉表现稳定，层次清晰，能够满足日常原型展示和验证需求。但是生成速度受案例复杂度影响，复杂场景比预期略慢
> * **Lovable**：功能完整度高，支持复杂交互，对参考案例复用能力强，可快速完成 0→1 或 1→N 原型生成生成速度稳定，适合多轮迭代。但是局限：视觉样式偏基础，高保真或品牌化设计仍需人工优化；初轮复杂场景生成可能需微调，适合快速搭建可用原型和验证流程
> * **Figma AI**：适合快速生成功能完整、流程合理的原型，更适合0→1阶段的原型设计。不过视觉表现偏基础，需要人工优化才能满足完成对应需求，对复杂功能或多轮迭代中细节还原存在一定限制，而且对 1→N 案例参考复用能力有限，细节和内容可能未完全还原
> * **Bolt.new：**功能覆盖全面，但短板也很突出：生成速度慢、交互和视觉表现不佳，不适合对效率、交互体验或视觉效果有高要求的场景，整体体验更偏“技术验证”和“结构生成”，而非高保真原型设计
> 


# 实践总结
* **提效感受**：
    * AI Prototype工具：适合交互复杂、流程繁琐、涉及多方协同的大Feature，在需求思路梳理、原型绘制、PRD编写与评审协同方向比较大的提效（如原型时间原2-3天缩短为2-3小时），对产品工作提效帮助还是很大的
    * 不适合很简单的需求（比如截个图，框个框，换个文案 ），甚至和AI交互出图会降低效率

* **产品对比**：V0 和 Lovable 的综合表现最佳，在功能完整度、交互逻辑上优势明显，适合快速落地原型和团队迭代；其他工具可作为辅助使用，根据不同场景选择
* **后续方向启示：**

    1. AI能力融合到产品全流程仍需规范：未来可进一步探索交互规范&视觉规范作为rules输入，比每次应用生成参考rules，可以减少重复输入成本
    2. 团队可以沉淀AI使用习惯与方法论：prompt 质量决定最终产出的质量，如何精准描述需求（Prompt规范）、如何二次编辑生成结果、如何与现有设计体系结合，都可以探索沉淀方法团队内共享
    3. AI更适合作为“提效中枢”，而非“全流程替代者”：它能释放PM在绘制与对齐阶段的时间，使更多精力投入到需求本身的思考与产品策略设计中

# 实践案例介绍
## 实际效果
我的诉求

**原先的方法（预估）**

**AI原型**

我要做一个AI源生的研发IDE工具

具体的模块/能力有：

* 对话模块，用户核心交互和输出呈现
* 任务模块，展示规划分解后的详细任务清单
* 文档模块，沉淀模型输出的需求文档和技术文档
* 代码模块，人工/模型主要编码的工作区
* 终端模块，执行运行命令、展示运行结果信息
* 预览模块，展示前端工程代码运行后的预览效果

1. 消化并整理信息
2. 能力抽象成模块
3. 设计产品整体框架、用户大体使用流程
4. 搭建原型雏形
5. 补充核心功能
6. 优化细节



整体需要预估2-3天。

1. 把会议中讨论的内容，大概整理
2. 交给模型
3. 调整细节
4. 完成



2-3小时，完成最终v0.1带交互的原型

## 实际操作
### 第一步：快速实现核心框架（v1）
Query：

{我的核心主张和参考输入}我要生成一个aiIDE产品界面，具备以下特征……

{模块介绍}模块1-模块6的介绍……

{模块关系、层级逻辑}模块1是核心主模块，统领其他5个模块……

{补充细节和再次强调主张}整个流程中，用户还可以……

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2018bfc1497c47698f75dfebd153a2dc&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bd2f42ec0c07401a996094fb6461b0e1&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=80cd60feed1b4caca9a3040850541814&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d4199e08fc724df2bc6149b23a8f8dc2&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ba05e31fbaec414fa5e6a0198a2b9d12&docGuid=fVpbvz8JR_jV3X "")
### 第二步：不断补充功能并试错，找到最优方案（v2-v15）
感受界面后，我要调整我的需求：

我要增加一个首页，包含下面几个能力：

* 新对话的输入框
* 多个同时在执行任务的面板
* 展示历史会话功能
* 提供具体case数据（看起来更真实）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a700731bc6ab44a0a7363076e5548ec9&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc119b0c95d6467893f55c1f29cab44c&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=98fdac9cacd74e75893477adcdba9f91&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=35e61ca2249e4d83bc61293ad776bd1f&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9d174d36d63f407db144d0d1f762a3f5&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f3c33d79b42642e799e1043713518a29&docGuid=fVpbvz8JR_jV3X "")
### 第三步：细节打磨优化（v16-v24）
优化细节：

* **小功能：**添加批注，让模型后续执行时作为参考
* **用起来不顺畅的：**放大新建会话输入框
* **信息过滤：**不展示已完成任务
* **体验优化：**增加「常用上下文」功能，便于用户快速添加知识

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e72fa2a821bd4e5784e14edee456e77b&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=78742f8930c445faa5fdb9732f2aacc0&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=23ca4f28a7c84a8aa42c87d92c268ce2&docGuid=fVpbvz8JR_jV3X "")
## 再分享一个小案例
因为要做网页代码问答的移动端适配工作，正在和研发讨论如何调整。总感觉我和研发同学没有相互理解各自的想法，而且因为在移动端的产品设计上经验不太多，所以感觉大家的方案都不太好。

于是直接用AI工具完成了这样一个讨论，本来估计还要再讨论半个小时，然后再花1个小时画出原型，现在几分钟解决了。

### **V1：搭核心架子**
输入：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f4d557efe204f58aaa0dda35e3ec1ca&docGuid=fVpbvz8JR_jV3X "")
基于这张现有页面，做移动端的适配

输出：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4e13292e9c7749b48a96e0118dd5f6de&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=26263973c65540ea96b617af622b2691&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9a9d4930d3e34564a95778d6f3a757b1&docGuid=fVpbvz8JR_jV3X "")
### **V2-V4：优化细节和交互**
把代码文件切换变得更适配移动端，结合用户使用场景，给出了自己的一些想法建议

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8da8ed1e7f9f4a1aaaf62752d10a862f&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9b7adbb0c6f34f8e8fd5fbfbe2a30092&docGuid=fVpbvz8JR_jV3X "")


调整细节、补充后续扩展功能位置

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=00eab10d295649bdb3a577cf5cc94613&docGuid=fVpbvz8JR_jV3X "")




## 1月14日最新案例
背景：EEPM团队觉得每周都要写Changlog很费精力，希望能基于卡片快速生成一份初版Changlog

效果：5分钟完成一个带交互原型+交互描述的简易PRD，快速和用户沟通确认雏形

做法：截图、截图、画个框，2句话。剩下交给模型

**原始Query**

**生成效果**

![语言描述](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b9f2ecd93422499fb1e454cb82f4b30f&docGuid=ZsIM2sXt_q4Sat "语言描述")
![原始截图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=86dbfafc9979486d8f880e9da9254523&docGuid=ZsIM2sXt_q4Sat "原始截图")
![批量操作的截图+红框](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=753902ad19274c70be03e61e03338f47&docGuid=ZsIM2sXt_q4Sat "批量操作的截图+红框")
[附件]


## 整体个人总结
### 适合的场景
* 非常适合的场景
    * 0→1且比较复杂的Case，可以让AI帮你攒出第一个版本，再继续修改
    * 1→N且相对比较简单的Case
        * 例如加一个新模块、点击弹窗、移动端适配等


* 一般适合的场景
    * 1→N且需要基于现有比较复杂的页面交互，进行全面改动
        * 需要先把当前的交互告诉模型，模型才能先知道你现在是什么样，该怎么改。 不如直接让它从零开始



### 提效效果
|**方式/提效点**|**个人效率/沟通效率**|**决策质量**|**开发成本**|**创新空间**|
|-|-|-|-|-|
|传统方式|Case1：6人参与的5次2小时会议Case2：30分钟左右|基于想象和静态图做决策|开发后发现问题，返工成本高|受限于画图能力，很多想法无法表达|
|AI方式|Case1：1人2-3小时完成Case2：10分钟|基于真实可交互的原型做决策|原型阶段就发现问题，修改成本低|任何想法都能快速验证，大胆尝试更多可能性|

### 我的方法
大体概括分为三步：

* 第一步：快速实现核心框架
* 第二步：不断补充功能并试错，找到最优方案
* 第三步：细节打磨优化

tips：模型虽然提高了效率让我们“偷了懒”，但不代表思考也可以“偷懒”。

* 交互体验前置到研发实现之前，让每个人都可以切身感受用户视角，从而对用户使用路径、交互体验进行修改

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
