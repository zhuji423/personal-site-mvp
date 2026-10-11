---
title: "**实践简介**"
description: "skill助力检测引擎验证"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\skill助力检测引擎验证.md"
---
skill助力**检测引擎验证

#### 🧑‍🏫 案例作者：[@程亚琳](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：数据分析、测试
#### 🔧 使用工具：Ducc
#### 📒 案例概要：在**检测引擎验证工作中，检测引擎产出的文件为parque文件，parque不方便直接查看，且存在大量不需要关注的日志内容。本文将使用skill实现一个用于快速对比两个 Parquet 文件差异的自动
# **实践简介**
在盗刷检测引擎验证工作中，检测引擎产出的文件为parque文件，parque不方便直接查看，且存在大量不需要关注的日志内容。本文将使用skill实现一个用于快速对比两个 Parquet 文件差异的自动化工具，专门用于防盗刷盗刷检测引擎验证场景中的数据比对分析。



**案例贡献人：**程亚琳

**关键词：**Coding Agent、skill、项目级工具建设



# **具体实施**
#### skill是怎么来的？
```
请帮我创建一个当前项目级的skill，作用是在用户提问"当前结果为xx1.parque, 历史parque为xx2.parque，请帮我对比结果"，将用户提供的两个parquet文件使用trans_parquet2csv.py转为两个csv文件，如果文件名中包含geo则对比r     
  iskTag列的数据是否一致，如果不一致则输出基于历史版本缺少了什么多了什么。如果文件名中包含cdn则对比ip列的是否一致，如果不一致则输出基于历史版本多了哪些ip，少了哪些ip   
```
![按照需求生成一个skill脚本](/personal-site-mvp/img/doc-placeholder.svg "按照需求生成一个skill脚本")
![调用方式说明](/personal-site-mvp/img/doc-placeholder.svg "调用方式说明")
![安装依赖环境](/personal-site-mvp/img/doc-placeholder.svg "安装依赖环境")
#### 尝试调用skill（失败）
![geolog检测结果验证（一致时）](/personal-site-mvp/img/doc-placeholder.svg "geolog检测结果验证（一致时）")
![geolog检测结果验证（不一致时）](/personal-site-mvp/img/doc-placeholder.svg "geolog检测结果验证（不一致时）")


![cdnlog检测结果验证（一致时）](/personal-site-mvp/img/doc-placeholder.svg "cdnlog检测结果验证（一致时）")
![cdnlog检测结果验证（不一致时）](/personal-site-mvp/img/doc-placeholder.svg "cdnlog检测结果验证（不一致时）")


#### 优化skill
![将达到预期的实现过程保存到skill中](/personal-site-mvp/img/doc-placeholder.svg "将达到预期的实现过程保存到skill中")
![尝试重新调用提示未加载](/personal-site-mvp/img/doc-placeholder.svg "尝试重新调用提示未加载")


#### 如何加载skill？
![重启加载](/personal-site-mvp/img/doc-placeholder.svg "重启加载")
![skill 的格式需要放在 .claude/skills/<name>/SKILL.md 目录下，文件名必须是 SKILL.md](/personal-site-mvp/img/doc-placeholder.svg "skill 的格式需要放在 .claude/skills/<name>/SKILL.md 目录下，文件名必须是 SKILL.md")
#### 我的项目级skill：
![](/personal-site-mvp/img/doc-placeholder.svg "")


#### 为什么要用skill？
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![流程固定的场景，直接使用zulu询问，每次回答都需要重新生成code且结果偏离预期](/personal-site-mvp/img/doc-placeholder.svg "流程固定的场景，直接使用zulu询问，每次回答都需要重新生成code且结果偏离预期")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 使用skill的效果
![cdnlog检测对比](/personal-site-mvp/img/doc-placeholder.svg "cdnlog检测对比")
![cdnlog检测对比](/personal-site-mvp/img/doc-placeholder.svg "cdnlog检测对比")
![geolog检测对比](/personal-site-mvp/img/doc-placeholder.svg "geolog检测对比")
![geolog检测对比](/personal-site-mvp/img/doc-placeholder.svg "geolog检测对比")
结果清晰且无其他多余操作



#### skill分享给研发使用，应用于自测环节
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# **复盘**
## **好的经验（可复用的方法论）**
1. **确定作用范围：**

    * 项目级工具推荐使用项目级skill

2. **不求一步到位**：

    * 首次生成的skill可以根据结果进行过程优化。

3. **skill 的格式**：

    * 需要放在 .claude/skills/<name>/SKILL.md 目录下，文件名必须是 SKILL.md。

## **反模式（需避免的坑）**
1. **首次生成的skill不建议直接分享使用**

    * 首次生成的skill建议多使用正向和反向的case验证通过后再进行分享使用

  

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
