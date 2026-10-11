---
title: "一、构建产设研协作新范式：大厂UE如何把AI Coding快速融入日常workflow"
description: "AI Coding 超级速成——直通设计工程师的秘籍✨"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\AI Coding 超级速成——直通设计工程师的秘籍✨.md"
---
AI Coding 超级速成——直通设计工程师的秘籍✨

#### 🧑‍🏫 案例作者：[@周嘉诚](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)[@钱秋婷](https://ku.baidu-int.com?t=mention&mt=contact&id=QK1zaYf0)
#### 🎬 案例分类：设计、开发
#### 🔧 使用工具：Gemini
#### 📒 案例概要：聚焦Google Gemini 3，结合PC & WISE端真实项目实践，从真实案例系统拆解AI Coding如何介入设计工作流，并与研发高效协同，推动项目在研发资源有限、排期紧张的情况下，帮助设计方案实现高还原度、高效率落地。此外系统介绍vibe coding 2026年初最新关键词skills能力，把AI上下文/开源工具封装成SOP手册，内化AI能力，实现专家级标准化流程闭环。

## 本期内容由 **整页 UE **[@钱秋婷](https://ku.baidu-int.com?t=mention&mt=contact&id=QK1zaYf0) 与 **创新搜索 UE **[@周嘉诚](https://ku.baidu-int.com?t=mention&mt=contact&id=MOtugPli) 共同编写。
本次分享源自已落地的真实项目。在项目推进过程中，我们需要在较短周期内完成可交互动效视觉效果的实现与交付。



在整页项目 **AI API 官网** 中，UE 引入 **Gemini 3 AI Coding**，通过自然语言生成可运行的动效代码，实现设计意图的即时验证与快速迭代，显著缩短了从构想到 Web 端落地的路径。

**在妙笔创作器项目**中，UE 应用 **Gemini 3 AI Coding **，通过自然语言生成可运行的动效代码，实现设计稿高度还原，大幅提升研发效能，在 iOS/Android 双端成功落地。

尽管面向不同终端，我们逐渐沉淀出一套共通的方法：**用 AI 缩短设计与实现之间的距离，以可运行代码作为沟通媒介而非门槛**。



## 显著收益
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bd3e32996ad947c7b8cf66c1909c1b00&docGuid=tx780KqnKrSeO8 "")
**实现质量近乎完美**

设计师在开发工具中部署代码后，可在**真机预览**提前走查修正，从源头确保设计还原度接近**100%**。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ed4995d1c98e46e39e3e3d62f462ec09&docGuid=tx780KqnKrSeO8 "")
**研发效能大幅提升**

研发动效耗时从3–4天缩短至1–2小时，提升**97%**。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=54d24abaeba84889abd214d221b8ffeb&docGuid=tx780KqnKrSeO8 "")
**人力与沟通成本显著降低**

减少多轮交付与走查，走查成本趋近于**0。**



本次分享将从 Web 端与Wise 端两个真实项目出发，介绍 AI Coding 辅助下的动效落地工作流，并沉淀成团队AI能力内化，积累可复用方法论与经验。

# 一、构建产设研协作新范式：大厂UE如何把AI Coding快速融入日常workflow
> 在vibe coding交付代码之后，我也在思考：设计与研发如何在项目中找到自己的定位和节奏，利用自己擅长的部分驱动项目，在AI新时代，既要扩展自己的设计角色能力，拓宽技术边界，也要明确自己的职能范围，不做重复和实际反而会扩大工作量的事情。
###### **在项目中设计师应该用AI Coding 做什么？或者不做什么？**
Cursor 的head of design说的“Focus on what designers good at and let the agent do the rest ” ，利用AI做设计师擅长的部分。

##### 用AI coding前置探索设计方案，
##### **总结落地性&不确定性**
##### **打破静态原型的壁垒，让用户测试可交互的原型，**
##### **增强沟通与审稿效率**
##### **通过直接调整更细节的动态效果和可交互动效，提高设计品**
##### **质，**把原本更感性的视觉效果参数化，达到落地还原
* 动效实现复杂度、跨端适配风险
* 通过技术扩展提升设计想象力，在设计阶段探索多模态/多样化方案



💡**设计师前置判断与收敛。**

* 通过真实交互，验证并跑通体验
* 让产品、研发、业务、评审在同一交互语境下讨论问题
* 审稿从「看稿」变成「用稿」



**💡提升跨角色沟通效率与决策质量。**

* **before：**用AE/视频交付动效，研发实现不了❌，
* **After：**用AI coding像素级设计源头掌控 100%视觉还原可交互动效✅，参数化和技术调整对视觉落地效果更可控。



**💡将设计从「视觉稿」升级为「工程化体验形态」**

# 二、落地关键项目：研发协同方式 与 AI Coding 实践案例拆解
## 2.1 重构设计研发协作链路-复杂视觉动效全套提案：Web 实现工作流（从 0 到交付）[@钱秋婷](https://ku.baidu-int.com?t=mention&mt=contact&id=e44485a0-e7b8-11f0-b828-0d2fa0669f28)
在项目中制作轻量化动效时，我选择了google gemini3的AI google studio作为快速验证与推动上线的工具。

![为什么不用figma make？figma make因为是beta环境，依然容易卡崩，而且不适合做复杂动效，更适合做体验原型，对于前端环境的兼容性不强，还是会有难以落地的风险](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=97313cc3927b42b5ad12deaf7bce4e66&docGuid=3Pz3oSRjmWPM1D "为什么不用figma make？figma make因为是beta环境，依然容易卡崩，而且不适合做复杂动效，更适合做体验原型，对于前端环境的兼容性不强，还是会有难以落地的风险")




![AI coding使用软件/IDE全集全家桶](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8733018409574f37b0f3c6bbb11bfa82&docGuid=3Pz3oSRjmWPM1D "AI coding使用软件/IDE全集全家桶")
#### 🔮第一阶段：简单介绍Google Gemini3
### **在Google AI Stuido build**环境下使用 Gemini 3
1.打开[https://aistudio.google.com/](https://aistudio.google.com/)，进入vibe coding工作台

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9c3361ac24724feab4e3d7bd49529dda&docGuid=1Rj1jmk1U7F4Ex "")
2.在对话框描述想要的效果

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a28485f291a94848bf023322f2866667&docGuid=1Rj1jmk1U7F4Ex "")
3.多轮对话输出

[附件]
这是很经典的左边对话右边预览的工作台界面，相信用过claude等其他的vibe coding都不陌生。简单介绍一下它的更多功能。

![部署到github上，开源项目](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=20020f1a154c4303850653e20e884552&docGuid=1Rj1jmk1U7F4Ex "部署到github上，开源项目")
![预览代码，可以手动修改代码直接微调数值](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c0c165bdc9d844fdb5e1029a1be3cf41&docGuid=1Rj1jmk1U7F4Ex "预览代码，可以手动修改代码直接微调数值")
![下载这个包，然后就可以交付研发](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=92eee5dfcaa84c63a685a28469382346&docGuid=1Rj1jmk1U7F4Ex "下载这个包，然后就可以交付研发")


#### 🔮第二阶段：和前端聊一聊交付
#### 这一步主要是为了规范框架和技术栈内容，能够让前端拿到我们的代码可以直接使用，避免因为技术栈等各种原因不同造成返工成本二次重写或重新封装，因此尽早与前端进行一次“交付对齐”，目的是**在开发正式开始前，把工程框架、渲染方式、样式体系与关键能力一次性对齐**。该步骤的输出是：明确技术栈、页面结构与复用方式，并同步交付规范与验收口径。


在网页项目中，**React 和 Vue 是当前最主流的两类前端框架**。在我几次和不同项目的不同前端对接代码交付的经验来看，具体框架需要具体沟通。

### **React**
### **Vue**
React 是一种以“组件”为核心的前端框架，强调模块拆分与参数驱动。

**在实际网页项目中的特点：**

* 常用于官网、营销页、ToB 产品、长期维护的 Web 项目
* 组件边界清晰，适合将动效、背景、交互封装成独立模块
* 更强调“复用”和“扩展”，一个动效可以在多个页面反复使用

**Vue** 同样是以组件为核心的前端框架，但更强调**结构、样式和交互的一体化表达**。

**在实际网页项目中的特点：**

* 常用于业务系统、中台、工具型产品、偏应用型页面
* 上手直观，页面结构和设计稿对应关系强
* 适合快速还原设计方案并推进业务落地



上面是一个简单的科普，其实设计师要做的操作很简单。

比如我和前端沟通之后接收到的信息是：

**1.前端框架使用nextjs react SSG实现**

* Next.js 是建立在 React 之上的一个框架，用来解决：页面结构、路由跳转、性能与发布方式
* React 是一种以“组件”为核心的前端框架，强调模块拆分与参数驱动。
* SSG（静态生成）：页面提前生成好

**2.样式使用tailwind**

* Tailwind 是一种直接在结构里写样式的方式，作为规范化UI库，可以直接在AI引入。

那就把这两条在一开始vibe coding的时候作为**强调指令**即可，这样确保我们的coding完全能使用，而且如果再次修改，视觉效果很有可能大打折扣。

![其实前端也会用到gemini3搭建框架，所以前期沟通好非常必要，在之前我就遇到过前端用的是vue组件，因此不改react框架](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7dda9520659d46079b5fc12106cdbde0&docGuid=1Rj1jmk1U7F4Ex "其实前端也会用到gemini3搭建框架，所以前期沟通好非常必要，在之前我就遇到过前端用的是vue组件，因此不改react框架")


作为置顶指令，接下来AI输出的所有代码都会遵循此规范。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=774eb2a455c2487d863fad37440a7722&docGuid=1Rj1jmk1U7F4Ex "")


**规范对接：因为做的是网站全套动效，因此前置沟通时，与研发提前明确动效区域与规范，整理成知识库文档对接。**

这里放一个知识库模版

[AI Coding 动效 / 研发 × 设计 协作交付说明规范](https://ku.baidu-int.com/d/T-_AsLQ8ayjPFv?t=mention&mt=doc&dt=doc)



#### 🔮第三阶段：多次prompt调优
**分成设计种类拆解动效，同种交互类型/视觉种类可以应用一套参数化底层逻辑，根据页面动效类型分成以下五类动效。**

|**首页多层交互动效**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0f7b6cfce5194901961cd29ac9524514&docGuid=3Pz3oSRjmWPM1D "")|
|-|-|
|**流光引导视觉动线**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d0c3ae541089439aacdb1ad44e67f024&docGuid=3Pz3oSRjmWPM1D "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=558443a2f2344937b758c5f6d5c4ccb1&docGuid=3Pz3oSRjmWPM1D "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=97fcadc40a1a40cc949e2935a6068954&docGuid=3Pz3oSRjmWPM1D "")|
|**物理引擎掉落趣味玩法**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3ad10b20dd8546088ca18d5ac001517c&docGuid=3Pz3oSRjmWPM1D "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c80534ccf2994f55b65c62e89361f1dd&docGuid=3Pz3oSRjmWPM1D "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f9a725a2388444eb81140bbc49fffe88&docGuid=3Pz3oSRjmWPM1D "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a036a3892899424c91bd89dcd937faee&docGuid=3Pz3oSRjmWPM1D "")|
|**数据微动效流动感**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=86418c2393dc4942a99e1e83473f864f&docGuid=3Pz3oSRjmWPM1D "")|
|**反差色光强化品牌感知**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2cbdd40e6b6b4aa7b019f54790caf825&docGuid=3Pz3oSRjmWPM1D "")|

在这里我总结我自己的web端prompt调优工作流，能够几次就出比较好的还原效果。下面就拿一个比较复杂的动效模块做说明，这个模块涉及背景、不同区域触发不同交互动效。



### **1.复杂动效-拆流程-分层写动效说明**
### **2.把视觉逻辑构成参数化实现指令**
不仅交给AI，也可以交给研发。

我会分成几层去写，尽量按照前端写的逻辑去拆分动效为几个模块，写的越详细后期调整和走查成本越小。

```
# ❌尽量不要用视觉纯感性语言来说明动效/视觉效果，比如（我想要纯科技风的未来感线性动效/炫光动效，AI理解会丑得超乎你的想象）
# ✅带上具体动效构思+静态页面关键帧1-2张描述，复杂动效将逻辑按照前端逻辑拆分，参数后期都可以调整
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=73ce5fac899240c2b2c3296d4f7706d5&docGuid=1Rj1jmk1U7F4Ex "")
先和chatgpt5/gemini3讨论复杂动效实现方式，并进行参数化拆解，下面这段prompt为我总结的参数化指令。先和AI讨论动效的实现方式，优化自然语言动效指令。在生成之前，尽量明确设计意图，可以避免浪费token，而且AI不会越用越傻。

```

你是前端动画和可视化专家，熟悉 HTML/CSS/JS/Canvas/WebGL/Three.js 动效开发。  
请根据下面提供的自然语言动效描述，生成一个**完整的参数化 prompt 指令**，用于 Google AI Studio / Gemini Build 生成可执行的动效代码。  

要求：

1. **动效实现方式分析**：
   - 对动效描述进行分析，判断最适合的实现方式：CSS 动画、Canvas 2D、WebGL 或 Three.js。
   - 给出选择理由，例如性能、可复用性、移动端流畅度、复杂度。

2. **参数化拆解**：
   - 将动效拆解成可调整参数：
     - 动效类型（effectType）
     - 颜色或渐变（color / gradientColors）
     - 尺寸 / 线条宽度（size / scale）
     - 动画速度（speed / duration）
     - 循环方式（loopType，如 repeat / alternate / once）
     - 透明度（opacity）
     - 方向（direction，如 horizontal / vertical / radial / random）
     - 其他可参数化特性（density / 数量，rotation / 旋转，spread / 散射等）
   - 给出每个参数默认值和可调整范围

3. **生成自然语言 prompt 指令**：
   - 输出自然语言格式的参数化 prompt 指令
   - 每个参数都明确标注，可直接修改生成不同效果
   - prompt 指令中应包含：
     - 动效类型
     - 参数列表及默认值
     - 建议实现方式
     - 运行环境（网页 / 移动端 WebView / 其他）

4. **示例结构**：
   - 首先分析动效特点并推荐实现方式
   - 然后输出完整参数化 prompt 指令
   - 每个参数标注默认值与用途
   - 指令可直接发给 AI Studio / Gemini Build 生成代码

自然语言动效描述：
“{这里填你的自然语言动效描述}”

请根据以上要求生成优化后的**完整参数化 prompt 指令**，并附实现方式分析与推荐。

```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=485f774fdbce41979ae559cf3cd25be3&docGuid=1Rj1jmk1U7F4Ex "")
### **3.build实时预览效果与细微把控**
### **4.自我走查中（我自己改一下代码）**
输出指令后并放上关键帧预览图/想要的大概效果图，gemini3 build功能可以实时预览效果，一般按照上面的逻辑生成之后，几轮指令就可以达到想要的效果。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c3cf6d4c478c4152a862698e5c7c0aa6&docGuid=1Rj1jmk1U7F4Ex "")
右侧点击code可以看到完整代码，一般build会自动分好类别和命名，如果遇到圆角、透明度、颜色、位置等，我会自己看一下代码），这些都是比较好改的问题，改后的代码会直接映射在预览效果中。

当然，如果看不懂的问题依然是自然语言修复。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=737dfb663a31486f97409b70b1f0d58e&docGuid=1Rj1jmk1U7F4Ex "")
### **5.下载！交付！**
### **6.如果你想部署到本地，添加更多3D模型和材质，做游戏！**
到这一步，所有基本效果都已经完成，点击下载会得到一个完整的包。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f5d98b312ae74a969c8ffc77a562ccda&docGuid=1Rj1jmk1U7F4Ex "")
[附件]


gemini 3 build不支持直接上传你自己的3d模型内嵌到网页中，如果需要内置材质需要部署到本地自己链接。

开发一般会用vision studio code：[https://code.visualstudio.com/](https://code.visualstudio.com/)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=71dcf1129d004228843658a8fae9d749&docGuid=1Rj1jmk1U7F4Ex "")
如果你使用ide（cursor/claude/trae国际版），把包扔到ide里面跑环境，添加更多功能。

这是用gemini+tripo 3D制作的游戏demo，在ide环境中可以放置glb文件，并且输出到浏览器预览。tripo 3D的AI实践在我的上一篇分享中提到，可以绑定骨骼。[🍌技能nano banana进阶玩法——AI从2D界面延伸到多感官3D空间](https://ku.baidu-int.com/d/EHdz6Urqih_z7H?t=mention&mt=doc&dt=doc)

```
请从零编写一个完整的index.html文件，只用原生HTML+CSS+JavaScript,实现一个3D手势交互小游
戏。要求如下：
1.依赖使用<script>标签从CDN引入：Three.js(含 GLTFLoader)、GSAP、MediaPipe Hands、Camera Utils。
2.模型与背景
·使用GLTFLoader 加载model.glb,保留模型原有材质和纹理。
·使用暗色环境光+至少两个方向光，营造阴暗立体效果。
·使用background.png作为远处大平面背景，并根据窗口宽高比自适应铺满视野（类似CSS的background-size:
cover 效果)。
模型初始在远处略低位置，例如(0，-7，-25)。
1.手势控制逻辑(MediaPipe Hands)
通过MediaPipe Hands 识别单手手势，实现三个阶段：
。
阶段1：上升(ASCENDING)
o初始为IDLE;当检测到张开手掌时，从IDLE进入ASCENDING。
。在ASCENDING状态中，用手掌在画面中的y坐标控制模型的高度：手越高，模型越高，限制在合理范围（如y
从-7到15)。
阶段2：靠近并悬停(HOVERING_NEAR)
。当模型上升到接近最高高度时，如果检测到握拳：
·结束ASCENDING,使用GSAP让模型沿z轴快速移动到摄像机前方（如(0,0，-8）)，并轻微上下浮动。
阶段3：化为灰烬粒子(DISSOLVING)
o当处于HOVERING_NEAR时，如果再次检测到张开手掌：
◆隐藏原网格模型；
·基于模型顶点生成粒子系统(THREE.Points),粒子大小略有随机、数量较多；
·在着色器或更新逻辑中，让粒子随时间向外、向上发散，并逐渐透明，表现为“灰烬消散”；
动画结束后，将状态和模型重置回初始IDLE,可重复体验。
```
[附件]




---

## 2.2 说明
生成**Web/H5代码**，可以使用**2.1流程⬆️**。若生成**iOS/安卓端代码**，需要使用**2.3流程⬇️**。

#### 🤔为什么有这个区分？
↪︎ 因为端代码不能直接在网页预览，必须得在开发工具中部署代码才能看到效果。

#### 🤔为什么不能直接预览？
↪︎ 因为有架构隔离，微波炉里不能运行黑悟空。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=94d5038155ed4709b783fb96d2eda2c7&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9ce8dd1aa13442b7a1a27950ee4476e0&docGuid=tx780KqnKrSeO8 "")
#### 🤔是否可以H5代码转端代码？
↪︎ 可以互转，但不建议，会出现很多bug，堆积💩山代码，修复成本也不低，最好还是重新写一下



---

## 2.3 Wise 双端实现工作流（从 0 到交付）[@周嘉诚](https://ku.baidu-int.com?t=mention&mt=contact&id=574c3d50-e9fc-11f0-bd6f-cbbb1c7b6a8a)
设计稿：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6cb8ca18d6142d3abc39c856ada6597&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b0b635d13ef244319ec5e60ef4b4d403&docGuid=tx780KqnKrSeO8 "")
AI Coding效果：

[附件]
AI Coding效果（练习-参考优秀案例）：

[附件]
源码分享：

[附件]
推荐关注这个抖音博主，审美和动效思路都很好：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4b888c11cc9c4d68a84ba839fd5dd272&docGuid=tx780KqnKrSeO8 "")




![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1fa0618eab81458a8e60406c6a02b160&docGuid=tx780KqnKrSeO8 "")
#### 🔮第一阶段：组织Prompt 描述想要的效果
**步骤1：简单抽象一下大概效果**

↪︎ 我要做的是一个扇形横滑图片流（类似走马灯的效果），支持上传图片、删除图片

**步骤2：写清楚代码用在哪（iOS端、安卓端、H5）****重点****⚠️**

↪︎ 适用于iOS / Android端的代码。

**Tips：**这里和研发前置沟通一下，有没有一些额外限制。

下面这些特殊适配规则为百度APP端内特有，如果做端需求，最好在一开始就告诉AI这些限制条件，后期再调整稍微有点麻烦。

### **iOS**
1. 手百iOS端需要使用OC代码。不能用SwiftUl。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c25963e7e5e64e16bedcc7611568cdb6&docGuid=tx780KqnKrSeO8 "")
### **Android **
1. 手百Android端需要使用kotlin代码，不能用compose。
2. 手百Android代码 gradle 版本是7.4.2。  一般AI生成的代码版本的太高，需要降低。
3. 手百Android代码 手百已经支持minSdkVersion="21" 了  但是 极速版本应该还是 minSdkVersion="16"。因为两边复用代码，所以这块需要兼容极速版。
4. 图片加载和处理需要使用 fresco。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3a796c0d2a6e410dac2d2b5f6d1764e3&docGuid=tx780KqnKrSeO8 "")
**步骤3：用图片+文字 描述样式和交互**（也可以把设计图给AI，让他自己写Prompt）

* 布局：平铺、重叠、对称...
* 样式：尺寸、色值、描边、投影
* 交互：上传、删除、滑动等等动画效果

### **图片：罗列所有状态**
### **Prompt：描述**样式和交互
![图片1](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5669287a2d4040f3aeaf0e8671c6c967&docGuid=tx780KqnKrSeO8 "图片1")
![图片2](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b6ee002e6ce640fe955abdc9371e678c&docGuid=tx780KqnKrSeO8 "图片2")
![图片3](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=efd9f3f4006a4e9085c7ff7f12298da3&docGuid=tx780KqnKrSeO8 "图片3")
![图片4](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4b174d2d161f43f6a6438b6d91de0b2c&docGuid=tx780KqnKrSeO8 "图片4")
![图片5](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0edc46db40e84addbb77f58e0959d633&docGuid=tx780KqnKrSeO8 "图片5")
![图片6](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f8bcd8e9200541aba570bf8ea9a4bc74&docGuid=tx780KqnKrSeO8 "图片6")
**图片1** 是最初始的状态，叫做【上传按钮】，是84*84px，背景颜色#333333，加号图标大小18*18px，图标颜色#FFFFFF

**图片2** 是上传1张图片的状态，图片上传动画是一个丝滑的从无到有、从小变大、旋转6°，这个图片位置叫做【左1图片】，【上传按钮】位移旋转到右侧，与【左1图片】呈现对称的状态，

**图片3** 是上传2张图片的状态，最新的中间图片叫【C位】，层级最高，呈整体现重叠的扇形状态。【C位】上传动画是从中间开始从无到有、从小变大。同时【左1图片】和【上传按钮】的组件缩放88%

**图片4** 是上传3张图片的状态，最新的图片上传动画是从最右侧【上传按钮】的从无到有、从小变大，位移到中间，成为新的【C位】。同时旧【C位】位移缩放到左侧，成为【左1图片】。同时【左1图片】向左位移，旋转至12°，并再次缩放88%，图片上所有组件清除，变成纯色灰块，颜色#333333，仅作为表示左边还有图片。同理上传4-9张图片也是一样的效果，最多上传9张图片。

**图片5** 是上传3张图片后左滑的状态，此时【左1图片】位移、缩放到中间，成为新的【C位】。旧【C位】位移、缩放到右侧，成为【右1图片】，【上传按钮】向右位移，旋转至12°，并再次缩放88%，变成纯色灰块，颜色#333333，仅作为表示右边还有东西。

**图片6** 是传图片大于2张时，滑动到最左侧的效果，最左侧图片变成【C位】，在最中间

下面是图片上的组件：

【文字标签】图片左下角有个文字标签，字号12px，字色#FFFFFF，标签尺寸自适应，距离文字上下2px间距，左右3px间距，标签背景颜色#000000，50%透明度。

【删除按钮】右上角有个删除按钮，尺寸18*18px，背景颜色#000000，50%透明度。图标颜色#FFFFFF。

【图片外描边】有个1px的外描边，描边颜色#FFFFFF

【图片投影】有个投影，box-shadow: 0 1px 6px 2px rgba(0, 0, 0, 0.25); 所有图片都有这些组件

详细观察分析我给你的图片和文字，时间长点也没关系

**步骤4：上传准备好的图片和Prompt给AI，等他生成代码**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ec048773db694bb09638bcd721fa812d&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=970219539ebb40c599a8e7d073b13589&docGuid=tx780KqnKrSeO8 "")


#### 🔮第二阶段：把代码放到开发工具中运行
**步骤1：部署代码**

根据AI返回的代码，复制到**代码编辑器**，遇到不会的问题/代码报错就直接问AI，所有代码复制完后，用**电脑模拟器**或者**插数据线用手机****（推荐）**预览效果

![从新建文件开始](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=36a35889356e43ceb97b982ce1cc81e7&docGuid=tx780KqnKrSeO8 "从新建文件开始")
![根据AI给的流程操作](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4de24f4b349d4c44a011bae7f8c158ef&docGuid=tx780KqnKrSeO8 "根据AI给的流程操作")
![若代码报错截图给AI](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0d3688ca0e1140ce870060210e337363&docGuid=tx780KqnKrSeO8 "若代码报错截图给AI")
![代码复制完后，在这里预览（iOS）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9f63a9e0b31d466ab0ec7e7dddf4d53c&docGuid=tx780KqnKrSeO8 "代码复制完后，在这里预览（iOS）")
![代码复制完后，在这里预览效果（Android ）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01ec36a55619421cb11ff201d4f572f2&docGuid=tx780KqnKrSeO8 "代码复制完后，在这里预览效果（Android ）")
![代码复制完后，在这里预览效果（H5 ）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8cb483ad3a214c3d899d2076c41a9310&docGuid=tx780KqnKrSeO8 "代码复制完后，在这里预览效果（H5 ）")
### **iOS-Xcode**
![（App Store可下载）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d127d36b45d745798ea2ee0e47eea32a&docGuid=tx780KqnKrSeO8 "（App Store可下载）")
### **安卓-Android Studio**
![（官网下载）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ff7bca17d67a405d892e08a60593f362&docGuid=tx780KqnKrSeO8 "（官网下载）")
下载地址：[https://developer.android.google.cn/studio?hl=zh-cn](https://developer.android.google.cn/studio?hl=zh-cn)

### **H5-CodePen**
![网页端线上预览](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=156d61dfb4bc4f2f8944494adfdb2e66&docGuid=tx780KqnKrSeO8 "网页端线上预览")
网页端地址：[https://codepen.io/your-work](https://codepen.io/your-work)

第一第二阶段完整实现过程⬇️：

[附件]


#### 🔮第三阶段：反复调优细节
**步骤1：分析问题 按优先级列出来发给AI**

代码**初次生成**的效果往往不尽人意，我们要做的就是**告诉AI存在的问题**，**反复调优**。就相当于提前走查了，调好效果后，研发拿到代码基本不用改动

##### **首次生成效果**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4c96906f924b4783bae287d5bff6336b&docGuid=tx780KqnKrSeO8 "")
##### **分析问题 告诉AI**
我看到了效果，现在有很多严重的问题，请修复

1.现在图片看不到效果，是灰色的，请给我真实图片

2.我要求【C位】和【C位】旁边的两张图片即【左1】、【右1】是显示出来的，但【左1】并没有显示出来

3.关闭按钮是圆形的，尺寸16*16px，距离上边距3px，右边距3px

4.左1、C位、右1 的负间距是-15px，左灰块，左1和左灰块，右1和右灰块的负间距是-70px

5.上传按钮的图标显示不出来

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=45e2ae9048924405bb643b40072c7381&docGuid=tx780KqnKrSeO8 "")
##### **拿AI返回的新代码，替换掉旧代码**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c20eadc7a2cc4ebe81bec2c81ac3b3e9&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ceaaa917f0441f1bf5c48dd068534db&docGuid=tx780KqnKrSeO8 "")


##### **二次生成效果**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9dc3729d8f4246fd8edd5ac18d062b3a&docGuid=tx780KqnKrSeO8 "")
##### **分析问题 告诉AI**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1394919d358541deaa15a7ba0ed7036e&docGuid=tx780KqnKrSeO8 "")
![若多问题不好解决，可拎出来逐个问题解决](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8cb6f755242749f7bf8330982f2e0e0f&docGuid=tx780KqnKrSeO8 "若多问题不好解决，可拎出来逐个问题解决")
![如果遇到一直调不好的情况，重新来过是最好的，不要错上加错](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0ea79a33fca846cc81416950de6b8b8b&docGuid=tx780KqnKrSeO8 "如果遇到一直调不好的情况，重新来过是最好的，不要错上加错")
##### **拿AI返回的新代码，替换掉旧代码**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=017519e754ec4cf186c2e6d723838a5d&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ceaaa917f0441f1bf5c48dd068534db&docGuid=tx780KqnKrSeO8 "")


**步骤2：反复调优，直至完美，交付研发**

**N次**调优后，得到自己满意的效果，保存代码，交付研发。

##### **N次调优效果**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1077870dc943454ab2df62ed4c9bc1e0&docGuid=tx780KqnKrSeO8 "")
##### **保存代码，交付研发**
**iOS**：在最初新建文件的时候会有个源文件，直接把源文件交给研发就行。

![新建文件就有源文件了](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2202e9bb71774947b669f769853b9157&docGuid=tx780KqnKrSeO8 "新建文件就有源文件了")
![源文件](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=04ebede85ab748c68cd828cd160be21a&docGuid=tx780KqnKrSeO8 "源文件")
**Android**：需要在Android Studio导出一个压缩包，把压缩包交给研发就行。

![Android Studio-导出压缩包](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a4a7e73c550a4dc1b15e37a7b422872e&docGuid=tx780KqnKrSeO8 "Android Studio-导出压缩包")
![压缩包](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f092d91fff384ba8a3b385920d84b84f&docGuid=tx780KqnKrSeO8 "压缩包")
**研发反馈：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=baba493fc06d4910bfe76b2bef9a8b1b&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16413118dc514fdb92998918e9ba8c1d&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ceae69fc0f624fe58a732a4ef71d1468&docGuid=tx780KqnKrSeO8 "")


# 三、AI coding实用延展：视觉设计邪修工作流，coding自制视觉工具[@钱秋婷](https://ku.baidu-int.com?t=mention&mt=contact&id=d87a2810-e899-11f0-80f8-5dff23267869)
在推特上经常能看到各种大神分享自己的视觉风格转换器网页，在实际项目中，我们可以通过视觉处理工具来延展想象力，快速统一不同模块的视觉风格。



### **我想做粒子映射的Y2K像素风视觉风格**
### **在chatgpt整理prompt，选择技术栈**
### **到gemini 3 build跑网页工具**
### **快速部署上线**
在pin上找到一些参考图。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0fe6f47be45e40ad9a8f404607b1d2c3&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=282a040796554f12a033836b244949ea&docGuid=tx780KqnKrSeO8 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ef50e90f12694f02bb5db270b955a41f&docGuid=tx780KqnKrSeO8 "")
他告诉我基于像素分析的粒子映射算法，

可以把任何画面转化成彩色粒子流动的效果。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2d370a4cd916492ebbf69e80ca2ffdb8&docGuid=tx780KqnKrSeO8 "")


在这里我加了一点参数，链接了本地文件，在视觉效果的基础上加了光晕和粒子点的格式化捕捉

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f7b10171f800495f9b4673fb85880454&docGuid=tx780KqnKrSeO8 "")


轻量化工具选择netlify零配置上线。

![选择手动/github引入](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=12cc9be1497b4eb08f6be2f20dc836ee&docGuid=3Pz3oSRjmWPM1D "选择手动/github引入")
![放置资源包](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5861fddd00db4011b53f37857f1f7205&docGuid=3Pz3oSRjmWPM1D "放置资源包")
![实时查看上线后数据](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0f51a4955e924cdba8ed94eb6e7d7f60&docGuid=3Pz3oSRjmWPM1D "实时查看上线后数据")
### **成品**

## [https://friendly-horse-2275b8.netlify.app/](https://friendly-horse-2275b8.netlify.app/)
###### 已经部署到网页中，请体验，接下来我会结合coding制作更多视觉工具 to be continue...


[附件]
**点状生成工具**

[附件]


**ascii代码风格生成工具并应用到API官网项目中**

[附件]
**为我自己的个人网站首页做的视觉参数化城市坐标风格实验，支持音乐可视化**

# 四、AI coding最新关键词玩法省流版：三分钟告诉你-skills是什么？怎么玩？实践操作？ [@钱秋婷](https://ku.baidu-int.com?t=mention&mt=contact&id=e2a99040-fa01-11f0-9835-059b1bdc2e15)
最近有很多设计师都开始使用vibe coding来开发个人/团队赋能的各种工具，接下来我结合**2026年初爆火的vibe coding关键词：skills**，为大家以后的vibe coding真正赋能提效。

![全家桶再次展示](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8733018409574f37b0f3c6bbb11bfa82&docGuid=3Pz3oSRjmWPM1D "全家桶再次展示")
![Skill生态正在以数倍的速度持续扩张着](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bbcd12cc17714f638fa2fdf0bef3489a&docGuid=3Pz3oSRjmWPM1D "Skill生态正在以数倍的速度持续扩张着")
# **概念介绍：skills是什么？**
简单来说，‌Skills 就是给** AI 助手（Agent）用的“专业工具箱”或“SOP 手册”‌**。它把完成特定任务所需的知识、步骤、甚至代码脚本打包起来，让 AI 不再是靠猜，而是能像专业人士一样，稳定、高效地完成工作。它让你可以把别人踩过的坑、总结出的方法论，一键装进自己的工作流。不用重新学，直接用。

claude官方教程：[https://code.claude.com/docs/zh-CN/skills](https://code.claude.com/docs/zh-CN/skills)



一个典型的Skill由三部分组成：指令、代码和资源。

以一个制作PPT的Skill为例：指令就是告诉AI按什么步骤做，代码负责执行其中的固定生成文件逻辑，资源则包含设计标准——比如什么排版好看、什么结构更清晰。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=88cb6b03a5ba428c85d1f2e0aaf44904&docGuid=3Pz3oSRjmWPM1D "")


**♠️ skills vs prompt vs mcp**

 ‌Prompt（提示词）就像你去奶茶店点单‌：你告诉店员“要一杯芝芝莓莓，去冰五分糖”。店员（AI）根据经验帮你做好。这种方式灵活，但每次都要从头说，而且如果店员忘了步骤，做出来的可能就不对了。

Skills（技能）就像你成了店长，制定了标准操作流程（SOP）‌：你写了一份《芝芝莓莓制作手册》，详细规定了先加多少草莓、捣多少次、加多少糖和冰。AI 助手（店员）会严格按照手册操作，出品稳定，而且这份手册可以反复使用，不用每次都重新教。

mcp 就更简单了，mcp是搅拌机、奶油等各种工具，skill sop里面详细规范了：什么时候使用搅拌机、奶油要打发到多少比例，才能制作出一份标准的芝芝莓莓。



# **高效赋能：skills能解决目前AI coding的什么痛点？**
如果用过cursor，那么就可以简单类比：skills约等于cursor的rules，不过rules是一开始的规范部署，skills是封装好的sop支持随意调用。我们都知道，AI第一次生成效果最好，到后面会越用越傻，而且不断叠bug浪费token，skills就是在源头部署工程文件，AI只能按照此规范文件作为底层逻辑准则去工作。



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c9fb2746151b46f1b02fed91c409f149&docGuid=3Pz3oSRjmWPM1D "")
**‌告别AI上下文指令的“健忘”‌**

长对话中，AI 容易因为上下文窗口满了而忘记之前的指令。Skills 采用“渐进式披露”机制，只有在需要时才加载详细内容，大大节省了宝贵的上下文空间。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2e112990962643e5865343bf11da91b5&docGuid=3Pz3oSRjmWPM1D "")
** ‌可复用，不重复劳动‌**

一旦把一个复杂的工作流程封装成 Skills，就可以像使用工具一样反复调用，再也不用每次都从头开始口头交代。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=39ce59e6aa6b46e1b5ecdae8abe1ac41&docGuid=3Pz3oSRjmWPM1D "")
**  ‌专业稳定，减少出错‌**

Skills 不仅仅是文字说明，还可以包含 Python 脚本、模板文件等。AI 可以调用这些实际工具来执行任务，结果更精准可靠。



# **我们直接上手实践！安装专家写好的skills-以trae国际版为例**
### **github仓库中可用的skills**
[https://github.com/anthropics/skills](https://github.com/anthropics/skills)

[https://github.com/skills](https://github.com/skills)

[https://github.com/openai/skills](https://github.com/openai/skills)

 Vercel联合 Anthropic、Google、OpenAI、GitHub 等一众大佬，搞了一个叫Open Agent Skills 的生态系统。简单来说，就是把这些复杂的“专家经验”打包成了标准化的安装包。

****[这是一个官网链接](https://skills.sh)

![skills能力已经上了主流IDE软件中](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6e9168ff00df4b7798ef916e0ca4468e&docGuid=3Pz3oSRjmWPM1D "skills能力已经上了主流IDE软件中")
![把单点五子棋变成技能五子棋](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ccdaf028ae1245cb9e37ad1ed4c78b92&docGuid=3Pz3oSRjmWPM1D "把单点五子棋变成技能五子棋")
### **1.在github下载**
### **2.skill装入trae**
#### **3.在vibe coding时，AI帮我按需调用skills，减少token，同时满足我的核心诉求**
这是一个比较热门的skill，设计者的核心点主要是提供给不懂设计的个人开发者，在生成网页时避免AI味出现。

![找到你需要的skill，安装](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=46fd2a5bd0c74aa2b2df02df28f7f316&docGuid=3Pz3oSRjmWPM1D "找到你需要的skill，安装")
![在github下载](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ab86a9a52e364894bd208bb149875ac2&docGuid=3Pz3oSRjmWPM1D "在github下载")
![找到这个skill 解压重新压缩成zip](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8df614450e6542aa91c389548f870034&docGuid=3Pz3oSRjmWPM1D "找到这个skill 解压重新压缩成zip")
![在trae的设置里找到规则和技能](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2ada1f98053d4e1f921ee3d21cce612b&docGuid=3Pz3oSRjmWPM1D "在trae的设置里找到规则和技能")
![上传刚刚的压缩包](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=203ff79086614f109c72d84a66bf1389&docGuid=3Pz3oSRjmWPM1D "上传刚刚的压缩包")
![装好了之后就可以看到解析的skill](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d2ef4c6e83254a27a9aa08cc4114b0fc&docGuid=3Pz3oSRjmWPM1D "装好了之后就可以看到解析的skill")


![我在solo模式下随便说一个关于这个skill的诉求，这个skill是关于前端网页设计风格的，于是我说：“我要设计一个杂志风网页”](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=796b82f9469447ef83b94de30de6573e&docGuid=3Pz3oSRjmWPM1D "我在solo模式下随便说一个关于这个skill的诉求，这个skill是关于前端网页设计风格的，于是我说：“我要设计一个杂志风网页”")
![可以看到它自动已经调用了这个skill来组装我的网页风格诉求。](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2a56e465837345bea0160b6676336f45&docGuid=3Pz3oSRjmWPM1D "可以看到它自动已经调用了这个skill来组装我的网页风格诉求。")
[附件]
简单预览一下网页设计，虽然尚未完全达到成熟的视觉设计标准，但对于开发者而言，已经初步具备了可感知的设计审美与结构判断能力。

**这正是 skills 的价值所在：**通过复用专家级 SOP，将隐性的经验转化为可执行的流程，让非此背景的小白也能在标准化路径中，快速产出“看起来就对”的结果。

[附件]
这是我用另一个remotion skill来跑的全自动化代码生成视频，我只对它说了一句：“给我生成一个产品宣讲视频”，trae就自动给我连接API，让我选择风格，设计并实现视频渲染，并且最终在终端给我打包好发给我，还支持自定义编辑。





# **自己封装一个skills-以trae国际版为例**
**什么适合做成skills？**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7e528e109fd340408f843da5862865cd&docGuid=3Pz3oSRjmWPM1D "")


### **我把刚刚的动效交付落地工作流打包成为一个skill**
### **测试skill在IDE环境中，能否直接使用**
### **共享skill，上传到我自己的github，让团队可以直接打开我的完整工作流，不需要学习，安装skill就可以自然语言描述动效，并直接交付代码和标准文档给研发**
* **1.解析与生成指令：**分析您的自然语言描述，生成一份详细的参数化Prompt 指令，并保存为文件。
* **2.代码实现：**自动使用 Next.js+Tailwind CSS实现该动效。会根据需求自动选择最佳技术方案(CSS/Canvas/Three.js)。
* **3.Vibe Coding 标注：**这是最关键的一步。在生成的代码中，所有的参数(如速度、颜色、密度)都会附带详细的注释，说明调整该参数会如何改变视觉“氛围”(Vibe),方便设计师直接修改。
* **4.在完成网页设计后，自动给我发送一份格式化动效说明用来交付研发**，说明包括动效在页面中具体位置/适用范围，动效触发说明，demo视频演示，动效包 / 资源交付，性能与环境约束，形成标准化对接文档。

![指令输入](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4eabee465a8c4358bf78ffdc8891dcfe&docGuid=3Pz3oSRjmWPM1D "指令输入")
![可以看到输入我的指令后，AI已经为我打包生成了一个skill](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=54192b40d81e468bac06e7819a94cf97&docGuid=3Pz3oSRjmWPM1D "可以看到输入我的指令后，AI已经为我打包生成了一个skill")


标准1:能够生成符合我要求的视觉动效效果：赛博朋克故障文字效果。✅

[附件]
标准2:可以看到代码语言是根据我的规范要求来的，每一步都给我详细注释，方便我直接修改参数调整效果。✅

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0f67207f61054eada74013c7877a0f40&docGuid=3Pz3oSRjmWPM1D "")
标准3:我要求把自然语言按照要求生成prompt数学逻辑后，发送给我完整指令说明。✅

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16560c836cd443c0b986249532f63aec&docGuid=3Pz3oSRjmWPM1D "")
标准4:我要求给我生成一份文件，根据交付文档规范来，我会把文件用于研发对接交付文档。✅

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fdb2a04c8dc84c049d06d3b965f44541&docGuid=3Pz3oSRjmWPM1D "")
[附件]




# **skills在AI coding团队赋能的作用**
### **把个人经验也变成资产**
### **真正节省打工人的时间，让AI做打工人的全能助理**
### **效率与可靠性**
就像我封装的工作流一样，从「一次性成功」到「可复现能力」，大家也可以尝试skills的玩法，从使用别人的skills到自己封装skills，让专业经验可复用、可批量、保持一致性。

从做重复的事，到做有用的事，把时间从低价值的重复劳动中释放出来，用于更关键的判断与创造，AI就是数字化员工，比如让AI封装一个skill，让他帮我从爬取我关注的AI博主的每日每5条新鲜内容，总结不重复内容做成ppt发送到我的如流，我每天花五分钟时间就可以知道AI最新动态和竞品洞察。

将重复任务的流程、规范、脚本封装成可复用的模块，AI无需临时推理，可以直接调用标准操作程序。





# **感谢大家的聆听！✨💜**
也希望我们能在这个快速变化的时代里，在 AI 的加持下，一起做更有价值的事，共同进步。


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
