---
title: "引言"
description: "解放双手：自动化完成手机应用操作-以地图竞对CASE线上效果分析为例"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\解放双手：自动化完成手机应用操作-以地图竞对CASE线上效果分析为例.md"
---
解放双手：自动化完成手机应用操作-以地图竞对CASE线上效果分析为例

#### 🧑‍🏫 案例作者：[@王成龙](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：数据分析、工作流自动化、开发、评估
#### 🔧 使用工具：其他、Ducc
#### 📒 案例概要：对话式手机GUI操作，解放线下自己对手机繁琐的操作，通过多模型协作实现竞对分析App操作的自动化，完成截图留存、结论产出。
# 引言
多模态大模型能力的提升，GUI的自动化操作容易通过Prompt实现，相关应用也不断出现（千问点奶茶、红手指Operator）。

针对地图数据效果的竞对分析和评估，从依赖手动操作App、针对性自动化操作App截图，完全可以通过一句Prompt实现泛化的自动化操作，因此我们实现了“对话式手机GUI操作”，用来解放CASE分析、竞对评估的各种手机操作。

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 技术实现方案
技术上通过对Agent效果多次迭代，最终形成通用大模型+专用GUI操作大模型多模型协作的技术方案

[流程图]
在实现过程中，技术上主要使用的解决方案：

1. 任务步骤过多时gui模型分析能力、记忆能力无法满足要求：通过多模型协作解决。
2. 手机集群(办公网)与应用服务(IDC机房)之间网络通讯。
3. adb操作适配：使用ducc和comake，结合开源代码完成。
4. Agent开发：通过Langgraph完成
5. 图文聊天前端：chainlit

# 后续工作计划
**如流数字员工**：监控case群消息，自动进行竞对case分析。

**数据分析**：针对关键竞对界面效果，进行文档化沉淀。

**手机集群运维：**完善操作次数分析统计，监控和保障可用性。





# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
