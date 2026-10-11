---
title: "实践简介"
description: "Zulu零基础搭建Electron客户端框架实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Zulu零基础搭建Electron客户端框架实践.md"
---
Zulu零基础搭建Electron客户端框架实践

#### 🧑‍🏫 案例作者：[@杨青霖](https://ku.baidu-int.com?t=mention&mt=contact&id=5c8c46a0-fce6-11f0-b1eb-8788d1659a23)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了零经验开发者利用zulu编码助手，从零开始搭建Electron客户端框架的实践。通过与zulu讨论技术栈、明确需求、逐步实施，成功完成了项目初始化、依赖安装、CSS集成等关键步骤，搭建起跨平台应用基础框架。展示了AI助手在快速上手新技术、提高开发效率方面的价值。
# 实践简介
本实践由青霖贡献，旨在解决旧版语音录音工具（Python+PyQt）维护困难且无法跨平台的问题。业务目标是利用现代技术栈，开发一款全新的、集干声录音与自动标注功能于一体的桌面应用。核心挑战在于贡献人对目标技术栈 Electron 毫无经验，因此决定全程借助编码助手 zulu 来完成从零到一的探索和搭建。

实践中，贡献人首先与 zulu 进行了充分的技术方案讨论，最终确定采用 electron-vite 方案。随后，在 zulu 的引导下，逐步完成了项目初始化、安装依赖、集成 Tailwind CSS 等关键步骤，成功搭建起了一个可运行的跨平台应用基础框架。此案例不仅展示了如何借助 AI 助手快速上手全新技术领域，还总结了宝贵的“先讨论后行动”、“明确需求”、“避免模糊指令”等人机协作经验，证明了即使是零基础开发者，也能通过有效的 AI 交互高效完成项目启动。

# 关键词
* Coding Agent / zulu
* Electron
* 零经验开发
* 跨平台桌面应用
* 技术栈选型
* 项目脚手架
* 人机协作



# 具体实施
## 背景信息
语音终端需要一个辅助业务方录音的工具，之前的工具使用python + pyqt实现，维护困难，无法跨平台编译打包。同时之前有一个网页版的“声速录”自动标注工具，经过多方考虑，本次使用electron技术栈，实现干声录音和自动标注功能。 

因为没有electron的使用经历，后续将会全程使用zulu完成所有需求。



**什么是electron**

Electron 是一个开源框架，它允许你使用前端Web技术（HTML, CSS, JavaScript）来构建跨平台的桌面应用程序。

简单来说，它将 Chromium 浏览器（用于渲染界面）和 Node.js（用于访问本地文件和系统功能）打包在一起，让你能像开发网站一样轻松地开发功能强大的桌面软件。

开发者只需编写一套代码，就能打包成在 Windows、macOS 和 Linux 上都能运行的应用。许多知名软件，如 Visual Studio Code、Slack、Discord 等，都是用 Electron 构建的。



## 整体流程
### 因为对electron没有使用经验，所以我们可以先跟zulu讨论相关技术栈实践。
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
> 这里我们先明确要求它不要写任何代码，因为在整体路线定下来之前就开始写的话，就很容易弄得一地鸡毛。


### 又因为我们有vue的使用经验，所以看起来electron vite 会更适合我们使用。
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
> 为了避免zulu擅自行动，我们继续要求 “仅讨论”


### 开始要求创建初始项目
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
> 创建完成了，并且运行起来了


### 我们继续根据建议 安装tailwindcss
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")


> 至此electron的基础运行框架就搭建起来了




### 实际最后业务成果
所有代码由AI生成， 0人工。



![带有完整的模板渲染机制](/personal-site-mvp/img/doc-placeholder.svg "带有完整的模板渲染机制")
![声学校准机制](/personal-site-mvp/img/doc-placeholder.svg "声学校准机制")




# 复盘
## 模式：（好的经验）


**截止2025年11月17号，建议使用GLM-4.6 MAX模式**

![](/personal-site-mvp/img/doc-placeholder.svg "")


**先讨论，确认方向之后再让zulu行动 （善用“仅讨论”）**



**让AI行动前先想明白自己想要的是什么（方向、效果）**



**忘记“一句话xxxx”这种宣传，有AI你可以少写代码，但是不能少说话。AI不能直接读取你的大脑。变成一个话唠，你不能跟AI比谁话少。**



## 反模式（不要这么做）


**不要模糊的提问。告诉AI你需求的相关信息，尽可能详细。**



**不要不经确认就直接让AI执行危险操作（删除、执行bash、执行代码）**



**谨慎在没有git托管的项目中使用AI**

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
