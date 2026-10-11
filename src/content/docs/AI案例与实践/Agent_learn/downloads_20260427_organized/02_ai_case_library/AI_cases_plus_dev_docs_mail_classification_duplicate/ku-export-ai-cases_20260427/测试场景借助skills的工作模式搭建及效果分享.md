---
title: "**先瞄准，再开枪（明确目标）**"
description: "测试场景借助skills的工作模式搭建及效果分享"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\测试场景借助skills的工作模式搭建及效果分享.md"
---
测试场景借助skills的工作模式搭建及效果分享

#### 🧑‍🏫 案例作者：[@程亚琳](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：测试、工作流自动化
#### 🔧 使用工具：Ducc
#### 📒 案例概要：根据知识库文档链接生成接口测试用例并执行
[文档目录]
# **先瞄准，再开枪（明确目标）**
**要干什么？**

**要怎么干？**

**需要准备什么？**

我要对接口进行测试

【任务】根据知识库文档链接生成接口测试用例并执行

我想让skills帮我干

[任务]1、解析知识库链接；2、根据知识库内容生成测试用例

我需要两个skill

[任务]1、生成解析知识库链接的skill；2、生成根据知识库内容生成测试用例的skill

# **工欲善其事，必先利其器（借助工具）**
先安装好用的skills，有了好的工具，接下来的活能够事半功倍

[https://github.com/anthropics/skills/blob/main/README.md](https://github.com/anthropics/skills/blob/main/README.md)

![](/personal-site-mvp/img/doc-placeholder.svg "")
[https://github.com/obra/superpowers/blob/main/README.md](https://github.com/obra/superpowers/blob/main/README.md)

![](/personal-site-mvp/img/doc-placeholder.svg "")
# **先造骨架，再填血肉（创建skill）**
## 1、生成解析知识库链接的skill，baidu-ku-content
在数字员工项目中，写过解析知识库链接的脚本和能力，借助已有的工具，将已有的能力封装为独立的工具+skill

![已有能力的封装](/personal-site-mvp/img/doc-placeholder.svg "已有能力的封装")
![已有能力构建的skill](/personal-site-mvp/img/doc-placeholder.svg "已有能力构建的skill")
![使用方式说明](/personal-site-mvp/img/doc-placeholder.svg "使用方式说明")
![直接输入知识库链接，完成解析](/personal-site-mvp/img/doc-placeholder.svg "直接输入知识库链接，完成解析")
![skill生成完成，分享及复用方式](/personal-site-mvp/img/doc-placeholder.svg "skill生成完成，分享及复用方式")
![baidu-ku-content 结构](/personal-site-mvp/img/doc-placeholder.svg "baidu-ku-content 结构")
baidu-ku-content 已提交至skills广场，按需安装使用：[https://console.cloud.baidu-int.com/onetool/space/4451/skills/252](https://console.cloud.baidu-int.com/onetool/space/4451/skills/252)



## 2、生成根据知识库内容生成测试用例的skill，api-test-case-generator
从无到有，直接提要求生成skill

![自动调起skill工具superpowers:brainstorming](/personal-site-mvp/img/doc-placeholder.svg "自动调起skill工具superpowers:brainstorming")
![确认过程的交互](/personal-site-mvp/img/doc-placeholder.svg "确认过程的交互")


![自动调起skill工具superpowers: writing-skills)](/personal-site-mvp/img/doc-placeholder.svg "自动调起skill工具superpowers: writing-skills)")
![skill创建完成及说明](/personal-site-mvp/img/doc-placeholder.svg "skill创建完成及说明")


![自动调起skill工具example-skills:skill-creator](/personal-site-mvp/img/doc-placeholder.svg "自动调起skill工具example-skills:skill-creator")
![确认过程的交互](/personal-site-mvp/img/doc-placeholder.svg "确认过程的交互")
![确认过程的交互](/personal-site-mvp/img/doc-placeholder.svg "确认过程的交互")
![检索到相关的skill](/personal-site-mvp/img/doc-placeholder.svg "检索到相关的skill")


## 3、使用方式（组合拳开干）
直接抛链接

![直接使用](/personal-site-mvp/img/doc-placeholder.svg "直接使用")
![输入知识库文档链接，开始任务](/personal-site-mvp/img/doc-placeholder.svg "输入知识库文档链接，开始任务")
![生成测试用例完成](/personal-site-mvp/img/doc-placeholder.svg "生成测试用例完成")
![执行用例](/personal-site-mvp/img/doc-placeholder.svg "执行用例")


## 4、用例更新（惊喜功能）
抛链接询问文档变更是否需要调整用例

![接口文档变更对比及用例更新](/personal-site-mvp/img/doc-placeholder.svg "接口文档变更对比及用例更新")
![用例更新后自动执行并给出调整部分](/personal-site-mvp/img/doc-placeholder.svg "用例更新后自动执行并给出调整部分")
# **复盘**
## **好的经验（可复用的方法论）**
1. **确定作用范围：**

    * 项目级工具推荐使用项目级skill

2. **明确需求，不求一步到位**：

    * 根据需求逐步拆解，逐步实现，过程中有走偏的情况及时提出要求改正

3. **借助官方工具**：

    * 推荐安装本文提到的工具（选择其中一个也OK）

## **反模式（需避免的坑）**
1. **skill的触发稳定性不足**

    * 基础的skill工具如果有范围重叠的部分，会随机进行使用。如果没有按照预期触发工具，建议指定skill进行使用

2. **不建议长时间死磕一个任务**

    * 长时间没有生成结果，或存在任务中断，建议重新另起一个终端

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
