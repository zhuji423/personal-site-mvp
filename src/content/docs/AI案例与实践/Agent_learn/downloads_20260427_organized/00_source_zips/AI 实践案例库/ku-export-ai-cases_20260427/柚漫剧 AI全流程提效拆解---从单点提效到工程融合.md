---
title: "+"
description: "柚漫剧 AI全流程提效拆解---从单点提效到工程融合"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\柚漫剧 AI全流程提效拆解---从单点提效到工程融合.md"
---
柚漫剧 AI全流程提效拆解---从单点提效到工程融合

#### 🧑‍🏫 案例作者：[@王珠卉](https://ku.baidu-int.com?t=mention&mt=contact&id=591eb9d0-2d9c-11f1-b278-41f01e7e457f)[@易旻](https://ku.baidu-int.com?t=mention&mt=contact&id=5c786c20-2d9c-11f1-b278-41f01e7e457f)[@赵龙](https://ku.baidu-int.com?t=mention&mt=contact&id=5e7a0880-2d9c-11f1-b278-41f01e7e457f)[@柴延晨](https://ku.baidu-int.com?t=mention&mt=contact&id=607b56c0-2d9c-11f1-b278-41f01e7e457f)[@张莹](https://ku.baidu-int.com?t=mention&mt=contact&id=62ba7150-2d9c-11f1-b278-41f01e7e457f)
#### 🎬 案例分类：研发全流程
#### 🔧 使用工具：Figma、Comate
#### 📒 案例概要：柚漫剧团队深度拆解其如何通过构建Prompt友好型PRD、设计即代码、AI Coding基建与AI Agent测试等核心能力，打通“需求-设计-开发-测试”全链路智能闭环的实战经验。
### 一、PMO[@王珠卉](https://ku.baidu-int.com?t=mention&mt=contact&id=592b8580-1c4d-11f1-bcb8-7d5effba2a1a)
### 背景&目标
以柚漫剧APP为锚点，开启AI赋能全链路的深度实验。通过打通‘需求-设计-开发-测试’的智能提效闭环，实现从“人力驱动”向“AI驱动”的范式跃迁，为产研模式升级提供实战样本。

### 全流程落地总述
### 📋需求方案阶段
### 🎨 交互视觉阶段
### 💻 功能开发阶段
### 🧪 测试上线阶段
**标准化与结构化**

**设计即代码（Design to Code）**

**从“工具引入”到“工程融合”**

**Agent 架构将 AIQA 融入全生命周期**

* **Prompt友好型PRD：**采用结构化模块，定义**AI友好的撰写规范**
* **需求智能预审辅助：** AI成为**纠错员**，扫描逻辑闭环，识别边界条件缺失
* **快速原型**：Figma Make等AI工具，生成高保真产品demo
* **原型接力与调优:** 承接PM的AI生成原型进行专业调整
* **Library + Token JSON + Guidelines:** 融入设计规范,提升AI生成质量
* **设计即代码(Design to Code):** 在规则框架内调优，最终设计天然符合技术架构
* **任务先行-单点提效：**编码（Zulu / Coding Agent）、F2C、AI CR、 AI 单测
* **弥补“知识差”-Rules & MCP：**将框架生命周期、组件用法、Lint 规范结构化，解决“跨端调用”的黑盒问题。
* **从Copilot 到"AI Agent" ：**QA 的转型为 Agent 的“调教者”与“策略监督者”，构建主 Agent+数字员工+六大专业 Agent模式
* **测试左移**：实现“全流程 AI 化”，利用 AI 深入研发阶段，在代码进入测试环境前消除隐患。

### **🏗️ 核心基建支撑：全链路的“心脏”**
* **规范工程：**定义 AI 听得懂的命名规范、代码风格、需求模板。
* **知识工程：**利用 **RAG**技术，将企业内部沉淀的陈旧文档转化为AI可用的活跃知识。
* **工具层：**统一的 AI-IDE 环境，确保所有开发者使用的模型底座和 Prompt 库是一致的。

### 二、产品[@程杜新](https://ku.baidu-int.com?t=mention&mt=contact&id=6d01a580-1c4d-11f1-bcb8-7d5effba2a1a)[@易旻](https://ku.baidu-int.com?t=mention&mt=contact&id=a4549560-2da0-11f1-8d47-f1f56575bf88)
**AI 赋能产品经理从单点提效到全流程串联的实践与思考**

### 需求方案阶段
* **需求文档总是要包括从外到内的各个模块信息，每一模块我们都有尝试利用AI提效**

|**环节**|**提效心得**|**图例**|****|
|-|-|-|-|
|① 市场动态行情&信息**信息输入 AI 化：从“看不完”到“抓重点”**|**日常问题：**市场信息太多、太散、太快，人工追踪效率低，难沉淀成持续输入。**AI解决什么：**把行业关键词、竞品关键词、内容关键词做成定时抓取 Bot，自动搜集、分类、归纳、生成日报。**案例：**比如我们要做一个内容画风专项；现在 AI 可以先把“画风趋势、用户讨论、竞品动作、行业变化”按类整理好，帮助我们更快判断：什么值得跟，什么不值得跟。|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=431e8b71c05c4009930c030019b56c84&docGuid=KnPV0yzB3Az4qy "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fab93b487e874816bb87a94188a055a5&docGuid=KnPV0yzB3Az4qy "")|这个环节的核心价值在于：**AI帮我们解决了‘从0到60分’的信息收集与处理工作**。我们不需要再花大量时间去做重复性的信息整理，而是可以直接站在AI给的基础上，去做深度的、判断性的工作。**目前局限性**：AI目前无法完全替代深度体验，尤其是竞品的交互流程细节。所以我目前使用场景是“AI做前置整理 + 人做深度分析”|
|② 竞品深度信息动态：**竞品洞察 AI 化：从“冗杂信息”到“结构化拆解”**|**日常问题：**深度信息获取成本高，访谈、录音、回听、整理很耗时，细节还容易丢。**AI解决什么：**用 NotebookLLM 这类工具，把访谈录音、长文档、评测材料快速转成结构化洞察。**案例：**在针对漫剧竞品调研过程中，以前 1 个多小时访谈只是开始，后面还要回听、摘重点、写纪要；现在 AI 能先把“功能逻辑、交互细节、用户反馈、可借鉴点和不适合借鉴点”拆出来，极大缩短从信息到洞察的时间。|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dd863f4fbad04686b8aa0aa91e59a601&docGuid=KnPV0yzB3Az4qy "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c86950c9bd4040dbb258c4da3293dd2e&docGuid=KnPV0yzB3Az4qy "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a7cd65405c54407aa790a7e630e57dd2&docGuid=KnPV0yzB3Az4qy "")||
|③ 定义端内问题点与收益**问题定位 AI 化：从“人肉”到“自动识别异常模式”**|**日常问题：**用户行为数据量大，人工看 session 非常耗时，容易漏掉真正的问题点，或者样本过少。**AI解决什么：**PM先定义业务逻辑和异常标准，再让 AI 自动做 session 分类、路径标注和问题归因。**案例：**比如留存链路分析，以前要 PM 一条条看 session、标用户每一步操作；现在只要先定义清楚什么叫异常，AI 就能批量识别异常路径，并输出报告：例如“用户在发布环节流失率最高”，帮助团队把问题点直接收敛到关键节点。|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fde0413f276f457aae4747c9fcf78271&docGuid=KnPV0yzB3Az4qy "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2ef3464ff9f240c69802625e8e19e03d&docGuid=KnPV0yzB3Az4qy "")||
|④ 按模块撰写产品方案**方案产出 AI 化：从“空白文档”到“可用初稿”**|**日常问题：**写需求文档耗时，尤其是从 0 到 1 起草时，容易遗漏流程、边界和验收口径。**AI解决什么：**把需求目标、功能范围、关键约束输入给 AI，快速生成 PRD 初稿，并转写为设计、研发可理解的表达。**案例：**比如做“发布器功能”，只要把核心需求说清楚：支持模块、功能点、交互逻辑，AI 就能先输出功能描述、交互流程、边界条件和验收标准，帮助 PM 从“开始写”变成“开始修改”。|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4219368901c245d6a508d398ca82bf00&docGuid=KnPV0yzB3Az4qy "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3774887952c94935abf2004c56f367dc&docGuid=KnPV0yzB3Az4qy "")|这个环节的核心价值在于：**AI帮我们建立了一个‘可行需求’的标准化模板**。它不是一个自动写需求的工具，而是一个帮助我们确保需求质量的协作者。好的产品需求到底需要哪些维度？AI可以帮我们定义出来，并且在每一次撰写时提醒我们**前提条件**：AI辅助撰写的前提是输入足够清晰。如果输入模糊，AI输出也会模糊。所以PM需要先想清楚自己要什么。|
|⑤ 智能Review 查漏补缺**Review AI 化：从“写完等Leader看”到“上线前再过一遍风险”**|**日常问题：**需求写完后，最怕遗漏边界条件、异常流程和逻辑矛盾，问题往往在评审后或开发中才暴露。**AI解决什么：**把 PRD 输入 AI，自动做结构化 Review，输出问题清单和补充项建议。**案例：**比如一个发布器功能，主流程写完了，但 AI 可能会提醒：背景、收益不清楚、超字数怎么提示、审核状态如何回显。这类问题如果LR前没补齐，后面就会反复返工。甚至技术评审时被Q的死死的|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ec30758005c4440ab335ac80983b0cc7&docGuid=PyTQ6godwus6we "")||

### 交互视觉阶段
##### 2.1 原型设计阶段：产品与设计的协同，快速搭建demo原型
* 我们在做创作发布器’这个功能时，尝试了一种新的协同方式：**产品和设计共同定义一个‘需求范式’，然后基于这个范式，AI可以辅助快速生成原型草稿**。
    * **范式的重要性**：AI辅助生成的前提是有一个清晰的范式。这个范式需要产品和设计一起定义，是团队协作的基础。

* **传统方式：**原型设计这个环节，传统上产品和设计中间需要大量的沟通对齐。尤其是复杂交互流程，经常出现‘我理解的和你理解的不一样’的情况。
    * **沟通成本高**：一个复杂交互可能要来回确认好几轮。有时候产品内部需求改了一版，产品原型没同步更新，协同方不知道具体改动点。
    * **效率瓶颈**：产品从需求完成到设计样图发给UIUE优化，再拿到可用的原型图，中间有较长等待时间，少则3天多则1周。


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6bd43b6dee464a08be92f2e78a0e95f5&docGuid=KnPV0yzB3Az4qy "")
* **AI赋能：**通过之前定好的prompt撰写规则，把指令输入给Figma Make，可以快速产出直接可用的60分毛坯房，再结合产品功能上线后，预期的用户使用路径，以对话的形式表述明晰用户操作步骤，利用AI可以完成多页面深度的交互流程；把原本要花1-2天的原型设计压缩到1-2个小时。
* **逻辑自检：**过程中我作为PM不仅自己重新梳理产品逻辑，在使用链路上验证用户操作便利性，同时可以快速把demo样式发给UIUE，进入下一步操作

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cce2e15ce94c43618827f81d9a77cdfb&docGuid=KnPV0yzB3Az4qy "")


[附件]
### AI在产品经理工作流中经验总结
* **我认为思路比结果更重要**，AI 不是替代产品经理做判断，而是把产品经理最耗时、最重复、最容易漏的工作，系统化提效。AI帮我们做好信息输入、深度拆解、问题定位、方案生成、风险兜底

### 三、设计[@赵龙](https://ku.baidu-int.com?t=mention&mt=contact&id=75083e10-1c4d-11f1-bcb8-7d5effba2a1a)
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4b8cbe5519144163a3145805ad5e81cd&docGuid=KnPV0yzB3Az4qy "")
### 1. 向上游赋能：设计师作为“需求架构师”
设计师不再被动接收碎片化、模糊的需求，而是主动为 PM 提供标准化的模版及工具，通过AI辅助需求澄清，确保“源头高质量”。

###### **提效原型生成 · Prompt组件模板**
通过预设一套包含组件基础功能、交互逻辑的 **Prompt 撰写及组件模版，**PM 只需输入业务核心逻辑，即可利用模版快速拼搭生成原型





![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ec73c2088e5b4348b61db367af8891b2&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=73f2ff78ca31414ca5f0638c1542d786&docGuid=qk4Y6eAyzgjykh "")
###### **Prompt友好 · 需求撰写新模板**
通过prompt撰写规则，反推需求模板，提取需求中的关键词，与prompt词模版比对查缺补漏，结合交互表述明晰需求撰写**结构化/标准化要求**，提供单页面0-1、单页面1-2、多页面流程3种常见类型需求撰写模板，以填空形式帮助梳理产品逻辑，生成内容完整、逻辑严密的需求文档，提升撰写及后续链路阅读友好性

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d86c11d6f11a4f719f7d79c7b0cbb227&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c56def9791bc4c4e9487f7a4b5414596&docGuid=qk4Y6eAyzgjykh "")
#### 实践案例： 
### 需求MRD新范式
## 01
#### 提供模版，联合PMO融入icafe需求规范
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ca03bf37b72a45e5bc92bc79b79899d0&docGuid=qk4Y6eAyzgjykh "")
![icafe模版](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=77b848f49e814160a8688e7d33e791af&docGuid=qk4Y6eAyzgjykh "icafe模版")
## 02
#### PM按模版撰写需求
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3da295098a5e47b3b86aaa3c1e601fa3&docGuid=qk4Y6eAyzgjykh "")
![PM撰写](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a17cb0d8b60948fead623c4e25207ffd&docGuid=qk4Y6eAyzgjykh "PM撰写")
## 03
#### 根据内容生成产品demo
![PM产出产品原型](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f41b18a0c7f3400abe44dc29ae79cc35&docGuid=qk4Y6eAyzgjykh "PM产出产品原型")
![PM产出产品原型](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=15351b7131d34cf09292299c04a9e350&docGuid=qk4Y6eAyzgjykh "PM产出产品原型")




### 2.设计师的核心深耕：从“生产”转向“效果精修”
当 PM使用AI 完成 60 分的“毛坯房”后，设计师将精力集中在最具溢价的专业领域：**效果调优**。

* **原型接力与调优：**设计师承接PM通过AI 生成的原型进行专业调整，由于使用同一套原型，可减少大量重复搭建的时间，使得设计师能够专注于交互/视觉的深度打磨，使产品达到90分的可用“精装房”

#### 实践案例：
### 基于Figma Make的原型接力
## 01
#### Figma Make复制原型文件
![复制文件](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=46bead3975ae41debfe586cc2513bb1d&docGuid=qk4Y6eAyzgjykh "复制文件")
![产品原型](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ba78d1e34a404cd4a6e5539de5b64431&docGuid=qk4Y6eAyzgjykh "产品原型")
![产品原型](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=35be2face62145039515522290c882b6&docGuid=qk4Y6eAyzgjykh "产品原型")
## 02
#### 导出设计稿/优化沟通
![导出设计稿](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0bd60cbc909749d181035a836da13a7c&docGuid=qk4Y6eAyzgjykh "导出设计稿")
![优化沟通](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ee6f5b31f2704a3c914215ed6aa0091c&docGuid=qk4Y6eAyzgjykh "优化沟通")




## 03
#### 完成原型界面及交互流程优化
![设计优化](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc3731760fb04ec1a2221b004e014c55&docGuid=qk4Y6eAyzgjykh "设计优化")
![设计优化](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d2cb2cdd50be44a7bf5a15d795dafa89&docGuid=qk4Y6eAyzgjykh "设计优化")




### 提升DEMO输出质量
### library
###### **功能的集合体、组件及方法（相当于冰箱）**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5cf60eb54c2549998355e83c8323ce5f&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=73c53ea299764e308260305ea61893f0&docGuid=qk4Y6eAyzgjykh "")
# +
### token json + Guidelines
###### token是规范（佐料），Guidelines是**rules规则（相当于菜谱）**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dd33ff2109744541968d25fac5403356&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bc3f4897a99346b087c8ce3647d6d13a&docGuid=qk4Y6eAyzgjykh "")
# =
### 符合规范的界面
###### **做好一道标准口味的菜**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=287302da9c2a4b98acf673eea8da43c7&docGuid=qk4Y6eAyzgjykh "")
#### 通过AI生成组件拼搭界面（现炒菜）
原先是需要学习烹饪技巧（详细prompt来生成界面），学习成本高，出品不稳定；现在可以将菜谱写进机器中，让机器人现炒，厨师只需输入简答指令即可

#### 通过library融入设计规范
[附件]
可直接添加已有的设计library，但目前AI会根据自己的理解进行token识别并命名，不方便设研之间进行沟通

#### 场域组件库
需先将组件库进行发布，最好按照研发的实现方式进行布局

![单场域组件库-手百主feedUI kit](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=56ebf10afb064f28a53616aed29649d6&docGuid=CsxOJr-QcT6TTc "单场域组件库-手百主feedUI kit")


#### 通过导出 token json + Guidelines 融入设计规范（推荐）
[附件]
包含完整的设计token信息和约定好的的命名

#### json导出
用插件导出已有token到json文件，并在figma make中添加json文件

![导入变量](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a8f4cd45e93043fdb0d388316a5a75a3&docGuid=qk4Y6eAyzgjykh "导入变量")
![导出到文件夹](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=63dd86efdb9a4213b16f272929c646e8&docGuid=qk4Y6eAyzgjykh "导出到文件夹")
![生成文件](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0b028258c2d84a60b550ab3505a5b61d&docGuid=qk4Y6eAyzgjykh "生成文件")
#### guidelines撰写
撰写规则可将设计规范主要内容交给deepseek，把内容润色成合理的guidelines描述  

```
 **忽略theme.css的设计规范，所有组件的设计规范基于design.json**

# 字号
单列标题用subtitle-lg，用户名文字用subtitle-xs，按钮字号用caption-lg，来源信息用caption-md，标签文字用caption-sm，内容用标题展示最多两行

# 字体加粗
标题用regular

# 圆角
标签用rounded-xxs，图片用rounded-md，卡片用rounded-lg，按钮用rounded-full

# 间距
标签内部用space-6xs，卡片内信息上下间距用space-xl，卡片内信息左右间距用space-xl，文字与图片间距用space-md

# 颜色
标题用text，来源和辅助信息用text-slim

# 图片
单图大图比例16:9，三图的图片比例3:2，三图只有第一张左边和第二张右边加圆角
```
```
请基于以下设计规范，使用 `design.json` 中的设计令牌（Design Tokens）来定义组件样式，并完全忽略 `theme.css` 中的任何现有规则。

### 设计依据与整体要求
*   **唯一设计源**：所有组件的样式定义必须严格基于 `design.json` 文件中的令牌值。
*   **组件类型**：请假设这些规范应用于一个“卡片”组件及其内部元素。

### 具体样式规范
请将以下设计描述映射到 `design.json` 中对应的令牌：

1.  **文字与排版**
    *   **字号**：
        *   卡片主标题：使用 `subtitle-lg`。
        *   用户名：使用 `subtitle`。
        *   按钮内文字：使用 `caption-lg`。
        *   信息来源/辅助文字：使用 `caption-md`。
        *   标签内文字：使用 `caption-sm`。
        *   主要内容正文：使用标题样式展示，并限制最多显示两行。
    *   **字重**：主标题的字重为 `regular`（常规，不加粗）。
    *   **颜色**：
        *   标题：使用 `text` 颜色。
        *   来源、时间等辅助信息：使用 `text-slim` 颜色。
        *   分割线：使用`divider` 颜色。

2.  **圆角**
    *   标签：使用 `rounded-xxs`。
    *   图片：使用 `rounded-md`。
    *   卡片容器：使用 `rounded-lg`。
    *   按钮：使用 `rounded-full`（完全圆形或胶囊形状）。

3.  **间距**
    *   标签内部（文字与边框之间）：使用 `space-6xs`。
    *   卡片内部，上下区域之间的间距：使用 `space-xl`。
    *   卡片内部，左右两侧的内边距：使用 `space-xl`。
    *   文字内容与图片之间的水平间距：使用 `space-md`。
    *   信息来源/辅助文字之间间距：使用 `space-md`。
    *   三图图片间距：使用 `space-4xs`。
    *   分割线距离页面边缘间距：使用 `space-xl`。

4.  **图片布局**
    *   **单图大图模式**：图片宽高比为 **16:9**。
    *   **左文右图模式**：图片宽高比为 **3:2**。
    *   **三图并列模式**：
        *   图片宽高比为 **3:2**。
        *   仅对第一张图片的**左上角、左下角**和第三张图片的**右上角、右下角**应用圆角（`rounded-md`），其余图片边角保持直角。

### 输出要求
请根据以上规范，生成相应的样式实现方案或配置代码，确保所有值均引用自 `design.json`。
```
### library（弱）+  token json + Guidelines（强）
未来趋势

### library：解析能力提升（强）
## +
### Guidelines：回归规则属性（平衡）


### 3. 向下游交付：实现“无需走查”的代码集成
研发不再是被动接收图纸，而是通过前置干预，让设计产出即为最终方案，交付给研发的是已经过设计校验、符合底层代码规则的“逻辑成品”。实现了从设计到实现的像素级自动化还原。

* **RD 提供前置约束：** 研发为 PM 和设计师提供**前置的代码约束 Prompt**（包括组件库规范、布局规则、性能基准）
* **设计即代码（Design to Code）：** 设计师在研发设定的规则框架内进行调优，产出的最终设计方案天然符合技术架构。

#### 实践案例：
### 动效/交互交付：Figma Make+前置部署
**1-N柚漫剧官网升级：**在已有H5官网的基础上通过AI进行动效升级，帮助研发侧整体提效60%（双端6pd → 2pd）

#### 原静态官网
![原静态官网](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4d8f8e304fb94887b74cf13dd84d2103&docGuid=qk4Y6eAyzgjykh "原静态官网")
#### 动效赋能及适配
![动效赋能](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b9fd4661499f4143ac4b242267872081&docGuid=qk4Y6eAyzgjykh "动效赋能")
![移动端适配](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=90b44702b4c148338f01b307561acdd2&docGuid=qk4Y6eAyzgjykh "移动端适配")
#### 研发侧工作：明确技术基准，提供约束prompt
## **01**
# 前期：技术栈&页面框架锁定
> 一个直觉上的疑问是：既然是 UE 用 Figma Make 生成代码，FE 等生成完再介入验收不就行了？
核心原因：**两个角色对"结构"的关注点和变更成本不同**（代码架构的变更成本远高于设计稿）

设计工具中增删页面、调整布局是相对轻量的操作；但在代码层面，页面数量、切换方式、状态管理方案等架构决策一旦落地，后续调整的级联影响很大——新增一个页面可能动摇之前所有页面的代码结构。

因此，FE 在生成前就需要介入，做好两件事：

1. **锁定技术栈和架构约束**；
2. **输出通用技术 Prompt 模板；**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e350dc7c1f03470dbeea229289de5628&docGuid=KnPV0yzB3Az4qy "")


**通用技术 Prompt 模板：**

```
### 精密视口与高度适配 (Engineered Viewport Logic)

* **PC 优先架构：** 以 **1440px** 为核心设计基准。默认样式即为 PC 端，通过 `max-width` 断点向下兼容。
* **动态高度计算 (Dynamic Calc)：** \* **禁止**使用 `100vh` 或 `100%` 处理全屏容器。
  * **实现方案：** 必须通过计算逻辑（如监听 `resize` 结合 `requestAnimationFrame` 或使用现代 CSS 变量注入）动态更新 `--vh` 单位。
  * **公式应用：** 容器高度应通过 `calc(var(--vh, 1vh) * 100)` 实现，确保在移动端动态工具栏伸缩时，布局能进行精密重绘或保持稳定，避免内容被遮挡或溢出。
* **比例锁定：** 核心展示组件优先使用 `aspect-ratio` 配合 `calc()` 进行自适应缩放，而非硬编码高度。
* **存量优化：** 会影响整体高度内容区域, 检查并优化不符合要求的100vh
```
```
### 动效性能与 DOM 生命周期 (State-Driven Lifecycle)

* **非视口静默策略 (Off-screen Silencing)：**
  * **目标：** 不在当前视口内的元素，其计算逻辑（如 JS 循环、Canvas 渲染、高频计时器）必须**彻底挂起**。
  * **DOM 优化：** 在不破坏进场/退场动画连贯性的前提下，利用**状态驱动渲染**（State-driven rendering）。当元素处于“非活跃且无过渡动画”状态时，尽可能将其从 DOM 树中移除，以减轻内存压力和浏览器的层合成负担。
* **动效解耦：** 动效实现需与业务逻辑解耦，支持“动画预判”。通过组件的生命周期钩子（如 `useEffect` 销毁函数或 `cancelAnimationFrame`）**确保没有任何无效的后台计算在静止页面上运行。确保不影响现有的动效及显示效果**
```


## **02**
# 后期：代码验收&工程化处理
UE 交付生成代码后，FE 的工作集中在：

* **代码清洗**：移除 Figma Make 生成的冗余 Context、未使用的工具函数和依赖（如 @radix-ui/react-slot、lucide-react 等非必要引入）；
* **适配修正**：修复 PC 端遮挡、移动端异形屏兼容、极端屏幕比例下的布局异常；
* **性能调优**：补充 useEffect 清理函数防止内存泄漏、优化大图加载策略；
* **功能补齐**：下载按钮、底部政策文案等业务逻辑，直接复用已有代码接入。

其中，部分重复性的适配修改（如跨断点样式调整）借助 Zulu 完成，人工只需确定方案，具体的重复修改交给 AI 执行。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4374cd9bb0dc4ef284c6efe8dc507d2c&docGuid=KnPV0yzB3Az4qy "")
## 
#### 设计侧工作：将设计稿导入，通过prompt生成效果
## **01**
# 整理设计稿
###### 按照动效实现的方式将设计稿图层分好，方便后续导出和生成


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b09b8c85e003413b9a5b00c55cb00a8e&docGuid=qk4Y6eAyzgjykh "")


## **02**
# 框架搭建
###### 将设计稿发送并描述第一页的效果，同时输入前端约束条件，把基础框架搭建好，后续将AI生成的组件替换为设计稿效果，推荐逐页搭建的方式，避免一次性全部生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d7316ef2f6b64968b9a11b9966a78fb0&docGuid=qk4Y6eAyzgjykh "")
```
帮我生成一个如图所示的官网界面，背景的漫画从下至上无限滚动，同时按以下要求做优化：
### 精密视口与高度适配 (Engineered Viewport Logic)

* **PC 优先架构：** 以 **1440px** 为核心设计基准。默认样式即为 PC 端，通过 `max-width` 断点向下兼容。
* **动态高度计算 (Dynamic Calc)：** \* **禁止**使用 `100vh` 或 `100%` 处理全屏容器。
  * **实现方案：** 必须通过计算逻辑（如监听 `resize` 结合 `requestAnimationFrame` 或使用现代 CSS 变量注入）动态更新 `--vh` 单位。
  * **公式应用：** 容器高度应通过 `calc(var(--vh, 1vh) * 100)` 实现，确保在移动端动态工具栏伸缩时，布局能进行精密重绘或保持稳定，避免内容被遮挡或溢出。
* **比例锁定：** 核心展示组件优先使用 `aspect-ratio` 配合 `calc()` 进行自适应缩放，而非硬编码高度。
* **存量优化：** 会影响整体高度内容区域, 检查并优化不符合要求的100vh
### 动效性能与 DOM 生命周期 (State-Driven Lifecycle)

* **非视口静默策略 (Off-screen Silencing)：**
  * **目标：** 不在当前视口内的元素，其计算逻辑（如 JS 循环、Canvas 渲染、高频计时器）必须**彻底挂起**。
  * **DOM 优化：** 在不破坏进场/退场动画连贯性的前提下，利用**状态驱动渲染**（State-driven rendering）。当元素处于“非活跃且无过渡动画”状态时，尽可能将其从 DOM 树中移除，以减轻内存压力和浏览器的层合成负担。
* **动效解耦：** 动效实现需与业务逻辑解耦，支持“动画预判”。通过组件的生命周期钩子（如 `useEffect` 销毁函数或 `cancelAnimationFrame`）**确保没有任何无效的后台计算在静止页面上运行。确保不影响现有的动效及显示效果**
```
## **03**
# 设计稿导入及效果生成
#### 方式一：切图导入 
与常规实现方式类似，通过切图实现各个页面的效果，将切图上传后替换至相应位置，适合静态的、不规则的并且带有特殊效果的元素使用，可以保证还原设计稿效果。例如LOGO图片等

*注意性能要求，切图不要太大

*注意上传时最好做好命名，避免使用模糊的描述，方便后续调整时能够精确定位，推荐根据元素作用, 特征, 位置命名(取1个或多个)如右上角遮罩, 就可以叫rightTopMask

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=792d22e2802d484b804304b0def0e699&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=de0c4754e8594554b2abb0ce2163c497&docGuid=qk4Y6eAyzgjykh "")


#### 方式二：设计稿导入
直接复制frame导入，由于这种方法AI会根据设计稿重新用代码绘制样式，容易丢失细节，因此适合较为简单的、需要变形的元素使用。例如页面左下角的指示器

*还是注意性能要求，设计稿不要太大太复杂，可以将复杂部分导出切图





![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ff1ca65f5ba4c4c84190ba437c9b3f5&docGuid=KnPV0yzB3Az4qy "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=54b7171dee4b4801bf57da4ddcc34d99&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f2939c60627d4940b064c2208177dd4d&docGuid=qk4Y6eAyzgjykh "")


## **04**
# 效果微调
#### 方式一：prompt调整 
无需代码基础，通过自然语言方式通过prompt微调，耗时较长，可以调整一些较为复杂的效果

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=729c3e5fdec04f1da758a3807f8732ed&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fe63161e63d6455db01f831f7d6c8d3c&docGuid=qk4Y6eAyzgjykh "")


#### 方式二：代码调整 
需要一些代码基础，通过直接到代码中调整参数，耗时较少，适合调节一些简单的例如位置、间距、透明度、动效时长等参数

以下提供一些常用的调参方法，遇到看不懂的也可以将代码复制下来给AI或询问研发同学

* 快捷栏：figma生成的组件提供了快捷栏直接调整基础样式，也可进入源代码修改

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1010ff311eea420283da8e545fa37edb&docGuid=qk4Y6eAyzgjykh "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=87f2077155294fe9ba656be4ffe4b761&docGuid=qk4Y6eAyzgjykh "")
* 一些切图被包含在组件中，或多层结构不容易被选中，则需要进入该图片所在组件找到该图片对应代码进行调整

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5a577f82858548d6abd589e0d361010b&docGuid=b_txIXlFA0X5F7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bdb825874b8d4f2fa3e7386b0cd7f0a8&docGuid=qk4Y6eAyzgjykh "")


### 视觉交付：配合 Agent 解析设计
UI完成后协同研发用F2C技术，AI 转设计稿为代码，从现有H5\Talos再拓展端能力，联调校准以优化 F2C、降人工成本[Figma2Code结合compose示例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/qALG60a_V0/05net839a_VudY?t=mention&mt=doc&dt=doc)；协同QA同学调优chacha智能走查工具能力，缩减人为对照验收成本。

##### 通过规范约束设计语义，保障输入的设计稿信息可信
* AutoLayout规范
* 图层分组规范
* 属性使用规范等

##### 约束代码生成流程与规范，支持业务私有知识
* 为F2CAgent配置额外的业务rules
* 生成代码
* 最后研发同学完成review和精修代码

##### 植入走查工具，在QA环节前完成样式校准
* 匹配设计稿标准
* 校准问题识别标准
* 制定验收评分标准

![文字/透明度色值使用规范](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=da8ccffeb1f24d86bd719b931e2d8320&docGuid=fSmzFjtNm5wrBs "文字/透明度色值使用规范")
![图层结构/分组规范](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f097996eba6e40b88265d5dc8aeba8a2&docGuid=fSmzFjtNm5wrBs "图层结构/分组规范")
![输入figma链接](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=44db22be9bd14cc7ae701b65a7c65d74&docGuid=t6mGwlvDgNnlkt "输入figma链接")
![F2C生成内容](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=977557d688c246d49a1a876973b577cc&docGuid=t6mGwlvDgNnlkt "F2C生成内容")
![F2C转化代码](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9c42d71ec7904c8f874d82222d6a8d1b&docGuid=qk4Y6eAyzgjykh "F2C转化代码")
![chacha走查工具](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9941f16595e942e980cde5ed62df0f9a&docGuid=KnPV0yzB3Az4qy "chacha走查工具")


### 四、研发[@柴延晨](https://ku.baidu-int.com?t=mention&mt=contact&id=b5854aa0-1c57-11f1-a0e0-31a14fc93899)
### 漫剧研发侧 AI Coding 落地实践：从单点提效到基建驱动
> 本文从研发视角出发，分享漫剧团队在 AI Coding 落地过程中的实际经验。核心观点：AI 工具本身不难用起来，难的是让它在真实工程环境中持续产出可用代码——这背后需要 Rules、MCP 等基建能力的支撑。同时，我们也看到了"代码作为产研协作中间态"的趋势可能。
---

### 一、背景：AI 工具全面接入
2025 年Q4开始，漫剧研发团队陆续接入了 Zulu（AI 辅助编码）、F2C（设计稿转代码）、AI CR（智能代码审查）、AI 单测等一系列 AI 工具。从渗透率看，团队很快做到了"人人都在用"。

接下来的问题自然就变成了：**用起来之后，效果到底怎么样？**

在持续推进的过程中，我们发现仅靠工具本身还不够——AI 对我们的自研框架、端能力接口一无所知，每次生成都需要人工反复纠正。这促使我们开始投入 Rules、MCP 等基建能力，让 AI 真正理解我们的工程上下文。而当基建逐步成熟后，我们还在漫剧官网项目上做了一次多角色协同的尝试——UE 使用 Figma Make 直接生成代码，研发在此基础上做工程化处理，**代码本身成为了产研协作的中间态**。

本文将围绕**单点提效、基建驱动、协作模式变化**三条线展开，分享我们的实际经验。

****

---

### 二、单点提效：先让每个环节跑起来
我们先在各个研发环节把 AI 用起来，看看哪些场景能直接见效，哪些还有问题。

**技术调研**

**UI/交互实现**

**业务逻辑实现**

**单元测试/自测**

**测试/上线**

* AI辅助技术调研
* AI生成demo
* F2C
* figma make
* 业务模块代码生成
* AI 辅助CR
* AI 补充单元测试
* bug辅助定位&修复



#### 2.1 AI 辅助编码（Zulu / Coding Agent）
日常编码中，Zulu 和 Coding Agent 是使用频率最高的工具，主要覆盖：

* **样式拼装与重复逻辑**：布局代码、工具函数等标准化程度高的任务，AI 生成效率明显高于手写；
* **代码补全与上下文续写**：在已有代码结构中续写逻辑，采纳率较高；
* **辅助排查与重构建议**：对已有代码提出优化方向，作为"第二双眼睛"使用。

实际体感是：AI 辅助编码在"有明确上下文、标准化程度高"的任务上效果好，但在涉及业务逻辑判断、跨模块依赖的场景下，仍然需要人工主导。

#### 2.2 F2C（设计稿转代码）
F2C 能力主要用于将设计稿直接转换为前端样式代码，减少传统的标注-切图-还原流程。

我们在实践中发现：

* 对于**结构清晰、模块独立**的页面或组件，F2C 的还原度较高，可以直接采用或少量调整；
* 对于**精细化视觉还原**，F2C 的效果优于纯文本 Prompt 描述的方式；
* 但对于**复杂布局和多状态组件**，生成结果往往需要较大幅度的人工修正。

在实际使用中，我们发现 F2C 的生成质量不只取决于工具本身的能力，还高度依赖两个输入条件：一是上下文 Rules 的完善程度，二是设计稿本身的规范程度——图层结构、AutoLayout 使用、分组命名等是否清晰，直接影响生成代码的可读性和可维护性。为此，研发侧和 UE 侧协同制定了一套 F2C 设计规范，从源头提升生成质量。

关键经验是：**F2C 适合按模块使用，不适合整页一次性生成。** 标注好模块边界再逐个处理，效果远好于"一把梭"。

#### 2.3 AI CR（智能代码审查）
在 commit 和 CR 阶段引入 AI SA + AI CR，针对 Android、iOS、Go 等方向做问题召回。初期存在误报率较高的问题，QA 团队针对标记的问题进行了分析，按不同语言进行了针对性优化，有效率持续提升。

AI CR 更详细的实践经验将在 QA 方向的分享中展开，这里不做赘述。

#### 2.4 AI 单测
前端新增业务模块接入了 AI 单测流程，重点覆盖复杂分支、异常链路与回归路径。对于减少手工漏测、提升分支覆盖率有明显帮助，新增模块的平均行覆盖率稳定在较高水平。

这里同样遇到了自研框架带来的挑战：TalosPro 的组件结构和生命周期与主流框架不同，AI 默认生成的单测代码在 mock 方式、组件挂载、事件模拟等方面都存在偏差。因此，我们同样需要通过 Rules 来补充 TalosPro 的测试规范，让 AI 生成的单测能够正确运行。同时，单测也是我们后续 Skills 建设的首个落地场景（详见 3.3 节）。



#### 2.5 小结
单点提效的价值在于**见效快、推进阻力小**，能让团队建立起对 AI 工具的基本信任。

但在这个过程中，一个规律性的问题也逐渐浮现：**同样的纠正，我们在反复做。** AI 不认识自研框架 TalosPro，每次生成的组件写法都要手动改；端能力的调用方式它查不到，每次都要人工补；编码规范和项目约定它不知道，每次都要逐条修正。工具本身的能力没问题，但它对"我们的工程"一无所知——每次对话都像从零开始教一个新人。

这促使我们反过来想：**既然每次纠正的内容都差不多，为什么不把这些规则直接告诉 AI，让它从一开始就按我们的方式来？**



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e2f0427bfd43476ab885c53ea4ee6f5d&docGuid=oY7zvJPx3W2MlF "")


---

### 三、基建驱动：让 AI 理解"我们的工程"
上面那个问题的本质是：**AI 不理解我们的技术栈和工程约束**。这不是工具的问题，而是信息没有以 AI 可消费的方式组织起来。

我们在三个方向上做了基建投入：Rules、MCP 工具和 Skills。



#### 3.1 Rules：教 AI 认识自研框架
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=645767b19c574fa1bcb9efdfe63a7c50&docGuid=oY7zvJPx3W2MlF "")
漫剧前端在跨端开发中使用的是 TalosPro——一个自研跨端框架。这个框架在公开的模型训练数据和互联网资料中几乎没有任何信息，AI 对它一无所知。

这意味着，如果不额外做些什么，AI 在涉及 TalosPro 的场景下生成的代码基本不可用——语法不对、API 不存在、组件用法错误。

**解决方案是 Rules（规则文件）。** 我们把 TalosPro 的框架概念、组件用法、API 约定、编码规范等信息，结构化地写入 Rules 文件，让 Coding Agent 在生成代码时能够读取和遵循这些规则。

这个过程本身也是一个不断迭代的过程：

* 最初是把常见的纠错经验写成规则，解决最高频的生成错误；
* 随后逐步补充框架的核心概念、组件生命周期、状态管理方式等；
* 最终形成一套相对完整的 Rules 体系，新成员也可以通过 Rules 快速理解框架约束。

目前，我们围绕 TalosPro 建设的 Rules 体系已覆盖 25 个规则文件，整体目录如下：

```
.comate/rules/
├── start.mdr                      # 入口调度（强制三步流程）
│
│  ── 基础规则（必读） ──
├── app.mdr                        # 项目结构与入口规范
├── syntax.mdr                     # San 组件语法与标签白名单
├── style-normal.mdr               # 样式属性白名单与 Flex 布局
├── best-practices.mdr             # 横向滚动、四宫格等布局实践
│
│  ── 组件 & 能力专项规则（按需加载） ──
├── component-img.mdr              # 图片组件
├── component-list.mdr             # 列表组件
├── component-swiper.mdr           # 滑动容器组件
├── component-video.mdr            # 视频组件
├── component-pag.mdr              # PAG 动效组件
├── component-refresh.mdr          # 下拉刷新组件
├── api.mdr                        # BOM / DOM / 路由 / 全局 API
├── jsnative.mdr                   # 端能力调用（fetch / callNative / scheme）
├── animation.mdr                  # CSS 动画（transition / animation）
│
│  ── 工程专项规则 ──
├── config.mdr                     # 项目配置文件规范
├── cli.mdr                        # CLI 创建项目
├── test.mdr                       # 单元测试规范（vitest）
├── cr.mdr                         # AI Code Review 评审规则
│
│  ── 迁移规则（Talos → TalosPro） ──
├── talos2pro.mdr                  # 迁移总控流程
├── talospro-project-structure.mdr # 入口与项目结构迁移
├── talospro-api-migration.mdr     # API 替换规则
├── talospro-component-rules.mdr   # 组件标签迁移
├── talospro-style-rules.mdr       # 样式迁移
├── talospro-lib-structure.mdr     # 组件库迁移
└── talospro-opt-rules.mdr         # 目录结构优化
```
按职责分为四类：

**基础规则（必读）**——项目结构、San 组件语法、样式属性白名单、常见布局最佳实践，任何代码生成前都会加载。

**组件 & 能力专项规则（按需加载）**——覆盖 TalosPro 的 6 个内置组件（img / list / swiper / video / pagview / refresh）和 3 类能力（BOM-DOM-路由 / 端能力调用 / CSS 动画），每条规则包含属性表、事件表、注意事项和正反示例。

**工程专项规则**——项目配置、CLI 创建、单元测试（vitest）、AI Code Review 评审标准，保证 AI 在非编码环节也能对齐团队规范。

**迁移规则**——完整的 Talos → TalosPro 迁移链路（项目结构 / API 替换 / 组件标签 / 样式转换 / 目录优化），支撑存量项目的渐进式迁移。

所有规则通过一个入口调度文件（`start.mdr`）统一管理，按"先读基础规则 → 按场景匹配专项规则 → 再执行生成"的三步流程强制加载，确保 AI 每次生成代码前都带着完整的框架认知。



**核心启发：Rules 的建设不是"提前规划"出来的，而是被真实的痛点倒逼出来的。** 当 AI 在某个场景反复出错时，就是需要补充 Rules 的信号。

#### 3.2 MCP 工具：让 AI 查到端上的能力
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0fd17eed7c99481d955bbfce84e435dd&docGuid=oY7zvJPx3W2MlF "")
漫剧是一个跨端项目，前端经常需要调用客户端提供的端能力（如原生组件、系统接口等）。传统流程中，前端需要查阅端上的接口文档，或者直接找客户端同学确认。

为了让 AI 在编码时也能获取这些信息，客户端团队提供了对应的 MCP 工具——当 Coding Agent 在生成代码过程中需要调用端能力时，可以通过 MCP 工具直接查询可用接口、参数格式和调用方式。

这解决的是**跨角色信息不对称**的问题：以前前端要"问人"才能知道端上有什么能力、怎么调用，现在 AI 可以直接"问工具"。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=29a202a04bbc43a1bd991817077a67b5&docGuid=KnPV0yzB3Az4qy "")
#### 3.3 Skills：从"知道规则"到"会跑流程"
Rules 解决的是"AI 知不知道"的问题，但有些任务不只需要知识，还需要**固定的执行流程**——比如单测生成，需要先分析模块分支、再结合框架约束生成用例、最后补充到项目中，步骤是确定的，但每次手动引导 AI 走一遍成本不低。

最近，基于前期积累的 Rules，我们开始在业务中尝试 Skills 的建设。Skill 本质上是**可复用的任务流程封装**，把 Rules 中的知识和固定的操作步骤组合在一起，让 AI 能够自主完成一个完整任务，而不再需要人工逐步引导。

目前已经落地的典型场景是前端单测 Skill：给定一个业务模块，Skill 自动分析其分支和边界，结合 TalosPro 的测试 Rules 生成测试代码并补充到项目中。这将单测从"人工驱动 AI 逐步生成"升级为"Skill 驱动 AI 一键完成"。

如果说 Rules 是教 AI"认识我们的工程"，那 Skills 就是教 AI"按我们的方式做事"。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01d7458aaff14a72bc6dfd8f66ace84c&docGuid=KnPV0yzB3Az4qy "")
#### 3.4 基建的本质
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0fe4d56daf5b4b3eaba129cafd6ba08a&docGuid=oY7zvJPx3W2MlF "")
Rules、MCP 工具和 Skills 看起来是三个不同层面的事情，但它们解决的是同一类问题：**把团队内部的隐性知识和工作方式，转化为 AI 可消费的显性资产。**

* Rules 解决的是"AI 不认识我们的框架"；
* MCP 解决的是"AI 查不到我们的端能力"；
* Skills 解决的是"AI 不会按我们的流程做事"。

没有这些基建，AI 工具只能在通用场景中发挥作用；有了这些基建，AI 才能真正进入我们的工程上下文，生成贴合实际的代码。而当基建能力逐步成熟后，一个更值得关注的变化也随之出现。



---

### 四、协作模式展望：代码作为产研协作的中间态
在单点提效和基建能力都有了一定基础后，我们在漫剧官网项目上做了一次多角色协同的尝试——UE 使用 Figma Make 直接生成代码，FE 从技术视角全程参与（这部分协作细节已在 UE 侧的案例中分享）。

这次实践中最值得关注的变化是**协作中间态的改变**。传统产研流程中，PM 输出 PRD，UE 输出设计稿，研发再基于设计稿编码——每个环节的交付物形态不同，信息在转换中不断损耗。而在这次实践中，**代码本身成为了贯穿全流程的中间态**：UE 通过 Figma Make 直接产出可运行的代码，FE 在此基础上做工程化处理，而不再从零还原。

我们认为，这种"以代码为中间态"的协作模式，可能是未来产研合作的一个趋势方向——各角色不再各自交付不同形态的产物然后"翻译"，而是围绕同一份代码资产进行协作和迭代。

当然也必须承认边界：这套模式目前更适合**重交互、无历史包袱的新项目**。对于有历史包袱、技术栈复杂的存量项目，更现实的做法是拆分模块——UE 负责关键模块的动效代码输出，FE 根据耦合程度选择直接采用或作为参考输入给 Coding Agent 进行工程适配。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ab6ab1804b7433dbd3f2fcaddab88e3&docGuid=oY7zvJPx3W2MlF "")


---

### 五、经验总结
#### 经验一：基建是单点到系统的桥梁
AI 工具用起来不难，但要让它在你的工程中持续产出可用代码，必须投入基建——Rules 让 AI 理解你的框架，MCP 让 AI 查到你的能力接口，Skills 让 AI 按你的流程做事。这些基建不是提前规划的，而是被真实痛点倒逼出来的。

#### 经验二：先找"高闭环任务"建立信任
优先选择标准化程度高、反馈周期短的任务（如样式拼装、单测补齐、规范化 CR）形成 AI 闭环样板。让团队看到实际效果，再推进更复杂的场景。

#### 经验三：跨角色协同需要前置对齐架构
不同角色的思维方式不同。研发习惯自上而下设计架构，设计习惯自下而上打磨细节。在 AI 参与的多角色协同中，如果不在生成前对齐整体结构，后续的返工成本会很高。

#### 经验四：承认边界，分场景落地
AI Coding 不是万能的。重交互、无包袱的新项目适合整体生成流程；有历史包袱的存量项目更适合模块化、渐进式地引入 AI 能力。认清这一点，反而能让落地更扎实。

---

### 六、下一步方向
1. 持续完善 Rules 、skills体系，覆盖更多自研框架和业务规范；
2. 探索 Figma → Mermaid → 代码的链路，将交互信息结构化为中间态，提升生成的可控性；
3. 在 1~2 个有一定复杂度的业务模块上试点多角色协同，尝试，验证在非理想条件下以及其他工具的落地效果；

****

> **一句话总结：AI Coding 落地不是"用工具"的问题，而是"建基建"的问题。把团队的隐性知识变成 AI 可消费的显性资产，让代码成为产研协作的统一中间态——这不仅是当下的提效手段，也是未来研发协作方式演进的方向。**
### 五、测试[@张莹](https://ku.baidu-int.com?t=mention&mt=contact&id=87a12320-1c4d-11f1-bcb8-7d5effba2a1a)
#### 5.1 AI模式升级：从**Copilot 到"AI Agent" 的范式转移**
* 人从“执行者” → “监督者 / 调教者”：从用例生成、规划生成跨越到用例执行，实现从Copilot 到"AI Agent" 的范式转移，LLM成为具备"独立行动"能力的AIQA

###### **全链路智能化测试（持续升级）**
**交付新模式**：通过两大角色（主Agent + 数字员工-"度小智"）+ 六大专业Agent + 工具生态 + 交付工程记忆，从"人用工具"升级到"人机协同"

![AIQA 架构图](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a7ac31d5a73049d19554835c10aa4301&docGuid=qNDa0XBzrZnxZx "AIQA 架构图")
![主动感知+持续测试](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=38108a3530874578aaa673db578868cd&docGuid=qNDa0XBzrZnxZx "主动感知+持续测试")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a535ef79d83e4821b93bf37e9ed2557c&docGuid=qNDa0XBzrZnxZx "")
![全链路多Agent协同工作](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cd8e1da524c14ea8a710d8ade47ff15d&docGuid=qNDa0XBzrZnxZx "全链路多Agent协同工作")


###### **实践效果（以 v1.0 为例）**
**AIQA**：落地需求占比100%；根据提测内容分析判定、自动发送提测报告QA反馈正向，根据需求准出标准自动拦截未达标需求；支持如流侧边栏形式、便捷观测需求和版本维度风险

**智能测试**：打通端到端全流程链路、完成从需求生成到测试准出全AI化；其中客户端落地12个需求（用例生成占比74%-6253个、稳定自动化用例占比10%-846个），服务端打通ITP新需求接口自动化、落地4个需求（用例生成占比81%-2000个、稳定自动化用例占比2%-50个）

![自动发送提测报告](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6ed6a0bd5d024a8aac400d35c04b9448&docGuid=qNDa0XBzrZnxZx "自动发送提测报告")
![需求准出自动拦截](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0dfd8178729642ebbbc5a16156f2b7e0&docGuid=qNDa0XBzrZnxZx "需求准出自动拦截")
![需求](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=94d768da227545c8a213ba2ae2165295&docGuid=qNDa0XBzrZnxZx "需求")
![版本](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a64c6f287bac4269b06102112a524587&docGuid=qNDa0XBzrZnxZx "版本")
![case自动生成-8s](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b07ee723e5354776b86ff55a099f9f90&docGuid=qNDa0XBzrZnxZx "case自动生成-8s")
![case单步执行-1min](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0db87f1f4427430d8d8fc95477caf23e&docGuid=qNDa0XBzrZnxZx "case单步执行-1min")
![通过](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=711ada1609344ee296447dc80079ef74&docGuid=qNDa0XBzrZnxZx "通过")
![不通过](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f918d34b20ef4827957eed496990467c&docGuid=qNDa0XBzrZnxZx "不通过")
![自动断言](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=449495c8a46d45e7b2fcb5d078d9358a&docGuid=qNDa0XBzrZnxZx "自动断言")
![自动签章](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=335cfedd687d4175b25dbe68372683fd&docGuid=qNDa0XBzrZnxZx "自动签章")
![签章汇总](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a205f165664e4859bdc3b6878c23b114&docGuid=qNDa0XBzrZnxZx "签章汇总")
#### 5.2 AI助力测试左移
###### **  提测阶段：AICR（持续完善）**
* **Commit** 阶段：基于Agent + rules 引入 AISA 扫描能力、CR可提前发现静态代码风险，该能力在Comate IDE / VSCode / JetBrains三端上线供业务使用
* **CR** 阶段：引入小码哥智能评审，并融合小码哥+AISA 能力（重复内容小码哥自动收起）、用AI评估代码质量
* 有效率**提升**：支持多端多语言扫描、初期存在误报率较高的问题，针对误报问题分析后针对性优化、提升有效率
* **经验：**不同业务线的扫描规则应用效果不同，【ING】增加知识本和代码库CR规则打通的功能、支持工程级和个人级的CR规则配置

![Commit](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=085d4d4ad6da41198834c38333826080&docGuid=qNDa0XBzrZnxZx "Commit")
![CR](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=38bc56da9efb417a9ad436c367252eeb&docGuid=qNDa0XBzrZnxZx "CR")
![优化前](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f9e9d70c17cd49b6825893196616922b&docGuid=CsxOJr-QcT6TTc "优化前")
![优化后](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=00a9adc2807a41338b9ca04a0b433144&docGuid=CsxOJr-QcT6TTc "优化后")
###### ** 走查阶段： AI Checker茶茬（建设中）**
* **背景**：从项目交付流程中的走查阶段痛点出发，结合AI+算法+代码实现figma+图像对比前置召回UI问题、并按问题类别定制化校验策略以提升召回准确率，经验总结走查高频问题有文本/样式/布局等
* **一期**：打通智能走查全流程、实现可见固定文本+元素布局识别能力，目前[ web 抢先版](http://10.25.65.174:8080/ai-checker/) 内测中
* **ING**：支持可变内容的识别与走查、拓展样式/布局类的检测能力，通过OpenClaw实现知识与算法的自主进化，将能力渗透至设计/开发/测试阶段

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e63a496ed94b4b10b75289aaf610f2df&docGuid=qNDa0XBzrZnxZx "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4cf321564b9f405b8ab2d1759cfaf2f1&docGuid=qNDa0XBzrZnxZx "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=25d400a7d1424a45b8849e14a63fecca&docGuid=qNDa0XBzrZnxZx "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=efa294bd32d341f5b56c7e49f3a36643&docGuid=qNDa0XBzrZnxZx "")
#### 5.3 下一步方向
1、智能测试稳定性提升：分析执行失败数据大部分来源于环境搭建+数据模拟，基于 ducc 建设端到端全流程skill、支持通过配置灵活实现业务定制化环境一键搭建+测试数据模拟

2、有效率持续提升：AICR +智能走查，持续完善能力覆盖并持续提升准召率

> 一句话总结：AI改变了测试模式、模糊了角色概念，就像是修仙"小绿瓶"，让我们的每一步走的意料之外、情理之中，成为我们最好的伙伴！
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
