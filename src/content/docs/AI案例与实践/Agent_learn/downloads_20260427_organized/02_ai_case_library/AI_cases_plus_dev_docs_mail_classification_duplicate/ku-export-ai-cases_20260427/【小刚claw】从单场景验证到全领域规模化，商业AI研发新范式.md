---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "【小刚claw】从单场景验证到全领域规模化，商业AI研发新范式"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\【小刚claw】从单场景验证到全领域规模化，商业AI研发新范式.md"
---
【小刚claw】从单场景验证到全领域规模化，商业AI研发新范式

#### 🧑‍🏫 案例作者：[@田树一](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：小刚
#### 📒 案例概要：小刚claw是端到端商业AI研发产品，通过知识资产化与反馈自动化，在复杂业务场景中实现规模化提效，覆盖风控等全领域研发流程。
[嵌入应用]
![未收藏](/personal-site-mvp/img/doc-placeholder.svg "未收藏")
![已收藏](/personal-site-mvp/img/doc-placeholder.svg "已收藏")
**🎧 本文已由AI生成播客版**

🖥PC端：可点击上方播放器直接收听

📱移动端：点击收藏按钮，小助手提醒稍后收听（移动端体验更好哦）

（点击打开[我的播客助手](https://applink-infoflow.baidu.com/share/contact/open/?token=14axitZXw8OkBlufrght73M3PI-J3S3XHIMUmy4GVd8?t=mention&mt=doc&dt=sdk)单聊界面，获取收听提醒~）

👉 反馈入口：有任何建议或问题，欢迎提交[“我的播客”许愿池](https://ku.baidu-int.com/share/shrGZMZBT3dkFMG7WSNfn/fombLZKG1lvVko9oPn?t=mention&mt=doc&dt=datasheet)

👉 天使用户群（12593817）：欢迎加入，一起共创优化我的播客

## 一、前言：从AICoding的困境谈起
AICoding能大幅提升研发效能，已逐渐成为业界共识。然而，随着我们在复杂业务场景中不断深入使用，我们发现AIcoding的引入导致：

* **节省时间有限**：面对复杂的工业级场景，AICoding的成功率有限*，真正能够节省的研发时间远低于预期；
* **引入新负担**：每个人prompt的能力不一，AI生成的代码质量参差不齐，Code Review时长增加，测试难度也随之上升。

更根本的问题是：大商业有众多业务线和复杂场景，如果每个场景都依靠case-by-case的prompt调优、手工设计AI流程，成本极高且无法规模化复制。

为此，我们打造了**小刚claw**（以下简称小刚）：一款具备规模化能力、适应复杂业务场景、能够端到端提效的商业智能化研发产品。通过精心设计的harness使得小刚即使在复杂业务场景下依然具备一击即中、端到端交付的能力，并通过知识资产化+反馈自动化使得小刚大规模推广到商业各主要研发场景，持续支撑商业全场景智能化研发转型。

> SWE-Bench Mobile: Can Large Language Model Agents Develop Industry-Level Mobile Applications? 中指出复杂的工业级场景下AICoding成功率仅20%
## 二、小试牛刀：商业风控端到端提效
### 背景：人力瓶颈与需求积压
商业风控是典型的高需求密度业务。25年Q4，风控场景共有MRD需求130个，受限于人力，实际排入开发的仅有34个，大量需求长期积压，严重制约业务迭代速度。

### 成果：端到端重构研发范式
26年Q1，我们将小刚引入商业风控场景，对研发范式进行了根本性重构。与传统AICoding只覆盖"代码编写"这一环节不同，小刚实现了研发链路的端到端覆盖：用户提供给小刚MRD，**小刚包揽设计、开发、编译、测试等工作，产出CR以及相应的设计/测试报告**，用户只需专注于评审验收。新范式将人从重复性的开发工作中解放出来，专注于更高价值的设计判断和质量把关。


> 小刚完成率包括100%AI生成和修改量<20%&修改时间<10min的生成。
## 三、大商业：从单场景验证到全领域规模化
商业风控的成功只是小刚的"小试牛刀"。在大部分业务场景还在prompt tuning、或case-by-case设计流程的时候，大商业在小刚牵引下已经在规模化地知识资产化、反馈自动化，以支撑大商业全场景智能化研发范式转型。

* 知识资产化：将各业务团队的代码库、配置规范、专家经验、历史经验，系统性地转化为相对静态的层级化知识以及相对动态的套路/Skills，作为harness的一部分提升小刚效果。
* 反馈自动化：每次任务执行结束后，自动进行任务回溯优化套路效果，合并和下线低效/相似套路，同时修正知识错误，补充知识盲区，形成"越用越好"的自进化飞轮。

> 当前已经积累了 180+ 套路、80+% 高频迭代模块知识（[https://eniac.baidu-int.com/](https://eniac.baidu-int.com/)）。
此外，我们精心打磨的旗舰Skills覆盖端到端的研发流程：

|阶段|需求理解|开发|流水线|联调|
|-|-|-|-|-|
|Skill|mrd2point|小刚/扫地僧/史帕克|安稳稳|AIQA|

目前，小刚已覆盖以下大商业业务场景，提供需求研发、联调测试、数据分析、运维支持四大方向核心能力：


![知识资产化](/personal-site-mvp/img/doc-placeholder.svg "知识资产化")
![反馈自动化](/personal-site-mvp/img/doc-placeholder.svg "反馈自动化")


## 四、小刚架构：端到端、可进化的智能研发Harness

## 附录：小刚视频
[附件]
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
