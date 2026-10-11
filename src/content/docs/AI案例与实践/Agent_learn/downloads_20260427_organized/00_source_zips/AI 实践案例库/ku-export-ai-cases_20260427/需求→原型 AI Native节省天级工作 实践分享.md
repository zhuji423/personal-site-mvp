---
title: "实践案例介绍"
description: "需求→原型 AI Native节省天级工作 实践分享"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\需求→原型 AI Native节省天级工作 实践分享.md"
---
需求→原型 AI Native节省天级工作 实践分享

#### 🧑‍🏫 案例作者：[@张尧](https://ku.baidu-int.com?t=mention&mt=contact&id=20bbedb0-fce6-11f0-aa72-c7218fa65fa0)
#### 🎬 案例场景：设计
#### 🔧 使用工具：V0
#### 📒 案例概要：本文分享了TPG工程效能部在AI IDE探索中的实践经验，提出了“人机协同，而非完全自动化”的方向。通过AI工具快速实现产品原型设计，将原本需要数天的工作缩短至数小时，显著提升了工作效率。文章详细介绍了实践案例、操作步骤及提效效果，展示了AI在需求到原型转化中的巨大价值。
# 实践案例介绍
## 新方向的背景
8月份当时市面上很多AI coding产品，比如Trae、Codebuddy等竞品，都发布了从需求到代码全部自动化完成的功能——**人更少的参与**。但通过对很多用户的访谈我们意识到：在真实的工程场景里，**“完全自动化”并不是最优解**。于是我们提出了一个不同的方向：

> **“人机协同，而非完全自动化。”——人更多的参与**
由AI把控流程，让人深度参与其中。工程师在AI生成、规划、修改的每个环节，都可以随时介入、批注、调整，真正实现人和AI的协作创作。

我们团队内部也经过5轮的脑暴，因为缺少一个可以讨论的可视化产品形态，大家对始终没有办法把各自的想法进行对齐。

我们讨论后，确定了需要包含的六个核心模块：

* **Chat：**核心流程体现与用户交互的主阵地
* **TodoList**：AI自动拆解任务，支持主任务和子任务两层结构；
* **View**：网页预览模块，支持实时批注；
* **Code**：代码编辑器，文件树+多标签页；
* **Terminal**：命令行界面，命令执行可视化；
* **Doc**：文档编辑器，支持需求、方案模板。

要想把这么多模块组合在一起，并且有好的用户体验，听起来是件很复杂的事情。

## 实际效果
**原先的方法（预估）**

**AI新的方法**

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
输入：

{我的核心主张和参考输入}我要生成一个aiIDE产品界面，具备以下特征……

{模块介绍}模块1-模块6的介绍……

{模块关系、层级逻辑}模块1是核心主模块，统领其他5个模块……

{补充细节和再次强调主张}整个流程中，用户还可以……

输出：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2018bfc1497c47698f75dfebd153a2dc&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bd2f42ec0c07401a996094fb6461b0e1&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=80cd60feed1b4caca9a3040850541814&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d4199e08fc724df2bc6149b23a8f8dc2&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ba05e31fbaec414fa5e6a0198a2b9d12&docGuid=fVpbvz8JR_jV3X "")
### 第二步：不断补充功能并试错，找到最优方案（v2-v15）
输入：

加一个首页并调整用户交互流程

扩展历史会话功能

提供具体case数据（看起来更真实）

增加新建会话输入框

输出：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a700731bc6ab44a0a7363076e5548ec9&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc119b0c95d6467893f55c1f29cab44c&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=98fdac9cacd74e75893477adcdba9f91&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=35e61ca2249e4d83bc61293ad776bd1f&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9d174d36d63f407db144d0d1f762a3f5&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f3c33d79b42642e799e1043713518a29&docGuid=fVpbvz8JR_jV3X "")
### 第三步：细节打磨优化（v16-v24）
输入：

放大新建会话输入框

不展示已完成任务

补充「常用上下文功能」

……



输出：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e72fa2a821bd4e5784e14edee456e77b&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=78742f8930c445faa5fdb9732f2aacc0&docGuid=fVpbvz8JR_jV3X "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=23ca4f28a7c84a8aa42c87d92c268ce2&docGuid=fVpbvz8JR_jV3X "")


实践案例：[https://v0.app/chat/aiide-product-design-bSgBpiE0f1Z?utm_source=450235118-5500&utm_medium=referral&utm_campaign=share_chat&ref=74M6CS](https://v0.app/chat/aiide-product-design-bSgBpiE0f1Z?utm_source=450235118-5500&utm_medium=referral&utm_campaign=share_chat&ref=74M6CS)

# 再分享一个小案例
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


# 整体个人总结
## 适合的场景
* 非常适合的场景
    * 0→1且比较复杂的Case，可以让AI帮你攒出第一个版本，再继续修改
    * 1→N且相对比较简单的Case
        * 例如加一个新模块、点击弹窗、移动端适配等


* 一般适合的场景
    * 1→N且需要基于现有产品界面和交互进行功能的增删、交互优化
        * 可能先要将当前的交互告诉模型，模型才能先知道你现在是什么样，新的功能加在哪里



## 提效效果
|**方式/提效点**|**沟通效率**|**决策质量**|**开发成本**|**创新空间**|
|-|-|-|-|-|
|传统方式|开5次会，每次2小时，还有理解偏差|基于想象和静态图做决策|开发后发现问题，返工成本高|受限于画图能力，很多想法无法表达|
|AI方式|边看边改，实时对齐，2-3小时完成|基于真实可交互的原型做决策|原型阶段就发现问题，修改成本低|任何想法都能快速验证，大胆尝试更多可能性|

## 我的方法
大体分为三步：

* 第一步：快速实现核心框架
* 第二步：不断补充功能并试错，找到最优方案
* 第三步：细节打磨优化

tips：模型虽然提高了效率让我们“偷了懒”，但不代表思考也可以“偷懒”。反而需要PM更加想清楚为什么做这个功能，对用户的价值在哪，并前置的切身感受功能对用户是否友好，怎么能更好。才能更高效的指引模型、不被模型带跑偏。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
