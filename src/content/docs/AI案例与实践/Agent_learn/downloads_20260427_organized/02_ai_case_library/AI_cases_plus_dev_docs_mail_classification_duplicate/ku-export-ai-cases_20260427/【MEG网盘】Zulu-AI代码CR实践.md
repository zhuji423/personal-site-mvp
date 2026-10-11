---
title: "背景"
description: "【MEG网盘】Zulu-AI代码CR实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\【MEG网盘】Zulu-AI代码CR实践.md"
---
【MEG网盘】Zulu-AI代码CR实践

#### 🧑‍🏫 案例作者：[@袁辉辉](https://ku.baidu-int.com?t=mention&mt=contact&id=f957b330-fce5-11f0-8070-5f6b046ade2d)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了Zulu-AI在MEG网盘中的代码CR实践，强调其能自动分析代码规范、逻辑问题，提供修改建议，助力提升代码质量和规范性。通过示例展示了Zulu在检测潜在问题、自动修复及合规性检查方面的能力，凸显其随时响应、全面扫描及学习型助手的优势，有效解放人力，让开发者专注于更有价值的架构设计和深度讨论。
# 背景
*前景提要：若没安装或未使用Zulu先参考 *[Zulu-让研发效率飞起🚀 🚀 🚀](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/8MCddZCpuH/yu9spOzG0p/fIkjO5OkRe4FvI?t=mention&mt=doc&dt=doc)**

**网盘Q3目标：Zulu月度使用渗透率 ****> 50%**

随着大模型对代码语义理解能力的提升，AI 审查代码的准确性与智能化程度大幅提升，作为一个优秀的编码智能体Zulu可以自行分析本次提交内容，在给别人推送CR前自己可**对提交内容做个整体的代码审查和评分。**

**✅ 规范及逻辑发现：分析开发提交代码，提前发现潜在逻辑问题与规范风险**

**✅ 问题 Bug 分析定位：通过语义理解定位潜在问题代码行，缩短排查路径**

**✅ 建议和优化改进：提供清晰解释和改进建议助你精进编码技艺。**

# 准备
准备一份针对自身编程语言且符合本团队最佳实践的rules, 这里以 [zulu mdr规范文件【草稿】](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/8MCddZCpuH/0UrS1BO6Qk/vYZGDUKQp2C4Dc?t=mention&mt=doc&dt=doc)为例（Zulu也兼容Cursor的rules），增加规则。

当然，若没有规则，也可完成对代码的规范和逻辑的检查，只是效果会差一些。

![项目规范文档](/personal-site-mvp/img/doc-placeholder.svg "项目规范文档")
![规则增加](/personal-site-mvp/img/doc-placeholder.svg "规则增加")


# 代码审查示例
在大家commit本次修改代码后，可根据以下query给Zulu提问题，提前进行代码CR。

这里先抛示例结论：**Zulu基本能找出本次修改内容的规范、逻辑问题，大家多多试用对代码规范性和BUG率都有很大裨益。小伙伴们快快用起来🎉🎉🎉**

|**问题类型**|**代码修改及提交**|**Query及调用**|**过程及效果**|**效果说明**|
|-|-|-|-|-|
|代码违反最佳实践|删除了swiper.vue 的一个key，这不符合规范，可能引发bug![](/personal-site-mvp/img/doc-placeholder.svg "")|根据规则对git diff 修改的内容审查合规性|![](/personal-site-mvp/img/doc-placeholder.svg "")|能找出问题并自动修复⭐⭐⭐⭐⭐|
||删除了swiper.vue 的一个key，这不符合规范，可能引发bug![](/personal-site-mvp/img/doc-placeholder.svg "")|根据规则对git diff 修改的内容进行打分|[附件]![](/personal-site-mvp/img/doc-placeholder.svg "")|能找出问题并自动修复，但试图加不必要的单测⭐⭐⭐⭐|
||针对单个文件tab_card.vue检查合规性| 检查下这个文件的代码是否合规#tab_card.vue |![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|能找出问题，但没按照规范评分⭐⭐⭐⭐|
||针对单个文件tab_card.vue，把整个规范文件拷贝进去检查合规性|基于下面规范审查文件 #tab_card.vue |![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|按照规范进行评分，并且给出建议和审查结论，很赞⭐⭐⭐⭐⭐|
|代码逻辑有问题|修改writer.ts的isEmpty方法，制造漏洞![](/personal-site-mvp/img/doc-placeholder.svg "")|根据规则对git diff 修改的内容审查合规性|![](/personal-site-mvp/img/doc-placeholder.svg "")|能找出错误并修改⭐⭐⭐⭐⭐|
||修改writer.ts的isEmpty方法，制造漏洞，本次不加规则![](/personal-site-mvp/img/doc-placeholder.svg "")|对git diff 修改的内容审查合规性|![](/personal-site-mvp/img/doc-placeholder.svg "")|能准确找出错误⭐⭐⭐⭐|

# Zulu CR代码优势
* **随时响应：** 提交代码前或后，只要你想，Zulu 随时服务，再不用等小伙伴。
* **全面扫描：** 覆盖逻辑错误、潜在崩溃、安全风险、性能问题、代码异味、风格规范... 比人眼更细致、更稳定。
* **学习型助手：** 不只是指出问题，更提供清晰解释和改进建议，助你精进编码技艺。
* **解放人力：** 让你从繁重的低级错误审查中解脱，专注于更有价值的架构设计和深度讨论。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
