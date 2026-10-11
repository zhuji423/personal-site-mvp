---
title: "分享主题"
description: "基于 Figma，如何更好实现原型图到生产级产品上线"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\基于 Figma，如何更好实现原型图到生产级产品上线.md"
---
基于 Figma，如何更好实现原型图到生产级产品上线

#### 🧑‍🏫 案例作者：[@高雅典](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：需求、设计、研发全流程、通用
#### 🔧 使用工具：Figma、Comate、Cursor
#### 📒 案例概要：本文档分享了基于 Figma 实现原型图到生产级产品上线的经验。核心是构建 AI 友好的 Figma 工程：使用 Auto Layout 对应前端布局，建立 Design Tokens 统一变量，管理组件状态。PM 角色转向定义系统状态和业务逻辑，利用 AI 生成代码和原型；UE 则聚焦设计资产沉淀，确保 Figma 组件与代码库 1:1 映射，从而借助 AI 工具加速设计到代码的转换，直接生成生产级代码。
# 分享主题
1. **作为 PM，我做了什么事情？给我带来了什么收益？**
2. **基于 Figma，如何更好实现原型图到生产级产品上线  **
3. **AI 时代，PM/UE 的工作发生了哪些变化**

# 背景
[AI 驱动开发：从 Prompt 到 Product](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/P4b3XJtQBgl-ua?t=mention&mt=doc&dt=doc)

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


**定义了全新的流程范式，AI Coding 实现了生产级产品的上线，所有代码全部为 AI 生成。**

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 如何实现
## 作为 PM 我做了什么？
1. 深入投入整个研发流，探索各个环节使用 AI 的可能性
2. 写** AI 友好 **的 PRD（prompt），**AI Coding** 生成生产级别代码

![传统 PRD](/personal-site-mvp/img/doc-placeholder.svg "传统 PRD")
![AI 友好的 PRD](/personal-site-mvp/img/doc-placeholder.svg "AI 友好的 PRD")
3. 团队全面转型 Figma，联合 UE 使用 Figma 协同设计** AI 友好 **的设计稿

## Figma 介绍
**Figma = Sketch（UI 设计）+ InVision（原型设计） + Zeplin（标注）+** **Dropbox（云端同步）+ Abstract（版本历史）+ Craft-Freehand（实时讨论） +** **Liveshare（实时分享）+ Team Library （团队组件库）+ Web API（第三方接入）+ …**

### 优点
1. **团队协作友好。**在 Figma 里，设计和协作可以是同时进行的，任何人都可以在设计图的任何地方添加评论， 你可以在评论中 **@其他人 **或将评论标记为已解决。

![](/personal-site-mvp/img/doc-placeholder.svg "")
2. **AI 友好。**插件生态丰富，有非常多的 MCP 工具、插件可以提供设计稿转 Coding、一键还原页面为 Figma 的能力，官方提供的 Figma MCP 达到了极高的前端还原度。
3. **团队 Library。**可以跨项目共享和更新 Component、Style。

### 缺点
1. 价格略贵（其他缺点都可以忽略）

# 我们如何使用 Figma 改进工作流
## 基础：构建 AI 友好的 Figma 工程
要让 AI 或自动化工具读懂设计，Figma 文件本身必须具备高度的结构化。

1. UE 沉淀设计资产

![UE 组件资产](/personal-site-mvp/img/doc-placeholder.svg "UE 组件资产")
2. **全面应用 Auto Layout（自动布局）：** 这是从设计到代码的最关键一步。Auto Layout 在逻辑上与前端的 Flexbox 布局完全对应。没有 Auto Layout 的设计稿只是静态图片，而应用了 Auto Layout 的设计稿则是具备空间逻辑的“准代码”。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


3. **构建统一的 Design Tokens（设计变量）：** 不要使用硬编码的颜色（如 `#FF0000`），而是使用语义化的 Tokens（如 `Color-Primary-Brand`）。这使得 AI 可以在代码库中直接映射这些变量，无论是在构建 IaaS 控制台还是复杂的 Agent 编排界面，都能保证全局样式的瞬间同步。

![](/personal-site-mvp/img/doc-placeholder.svg "")


4. **组件与状态管理：** 为 UI 元素建立完善的 Component Properties（变体、布尔值、文本属性）。在 Figma 中模拟组件的真实状态（Hover、Disabled、Loading），**确保需要保证代码库里的组件名能和代码库中对应上**。

![](/personal-site-mvp/img/doc-placeholder.svg "")


5. **结构化设计稿：**保证一个完整的交互模块在一个组里（被一个父节点统一管理），后面给 AI 的时候就是给这个模块的链接

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 提效：利用 AI 加速原型图/设计稿生成
目前，我们的产品交付越来越倾向于直观地知道结果，而不是通过冗长的文档进行传递。打通 Figma 到生产代码的路径，可以借助以下方案：

1. **对于从 0 到 1 的项目（没有任何历史包袱，不需要和现有业务融合）：**利用 AI 快速生产原型图，比如 Figma make、Builder、Gemini 等，梳理业务逻辑后直接生成初版可交互的页面。
2. **对于存量产品：**如果直接使用 AI 画原型图，会和我的现有业务完全不沾边，无法无缝融入到现有的产品功能中，UE 同学可能需要进行较大重构。
    1. 解决方案：
        1. 找 RD 同学要代码仓库拉到本地，只有前端代码仓库即可
        2. 打开 AI IDE，直接让 AI 通读代码，基于代码整理当前的交互流程和功能逻辑，生成一份 **md 文档（产品现状）**
        3. PM 同学关注业务流程和功能逻辑，利用 AI 生成**需求 md（主要聚焦业务逻辑和功能目标）**
        4. 然后再使用这份 md 文档+需求 md，在已有代码库的基础之上直接让 AI 修改代码，这样就得到了一个可运行可交互和现有产品逻辑完全兼容的原型
        5. 使用 code 转 Figma 工具，推送到 Figma
        6. UE 同学介入，基于初版 Figma 继续修改....
        7. Figma 转 code，直接上生产





## 升级：AI 时代 PM 与 UE 的角色演进
当 Figma 原型/其他 AI 工具可以直接输出代码片段或高保真交互时，PM 和用户体验设计师 UE 的工作正在发生重塑。

* **PM 的精力转移：** 从撰写事无巨细、解释每个按钮逻辑的“重型 PRD”，转向**定义系统状态、数据流向和验收标准**。PM 应该更多地思考业务逻辑，思考如何利用 AI 将产品逻辑、业务逻辑沉淀，并可以利用 AI 工具进行演示和对齐，减少信息损耗。
* **UE 的重心转移：** UE 应该更多地思考如何利用 AI 沉淀设计资产、设计规范。UE 需要更深入地理解前端组件库（如 Ant Design 或特定的云服务设计体系），确保在 Figma 中构建的组件库与代码仓库中的组件库保持 1:1 的映射关系。同时，也需要学习如何为 AI 提供更好的视觉提示，以获得更优质的代码输出。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
