---
title: "💗有奖互动💗"
description: "AI 数据建模：从 iCafe 到 iCode"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI 数据建模：从 iCafe 到 iCode.md"
---
AI 数据建模：从 iCafe 到 iCode

#### 🧑‍🏫 案例作者：[@郑宇宏](https://ku.baidu-int.com?t=mention&mt=contact&id=77b62e20-fcdf-11f0-b2c3-950f2260e2a9)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate，iCafe,  iCode
#### 📒 案例概要：本文聚焦AI数据建模从iCafe到iCode的自动化方案。针对LLM训练数据异构性问题，提出基于Code Agent的智能建模管线：通过iCafe需求卡片驱动，结合历史代码与Schema文件，自动生成Python转换代码。方案支持模块化复用（50%任务由存量代码解决）和Agent辅助设计（采样、代码生成），显著降低技术门槛，提升数据建模效率与标准化水平，实现从原始数据到结构化Schema的自动映射。
## 背景
在大规模预训练语言模型（LLM）的开发中，我们从广泛渠道采集的海量原始数据构成了模型学习的基石，然而这些原始数据通常形态各异、结构混乱且质量不均，涵盖了文本、代码等多种形态，无法直接被模型高效利用。数据建模环节正是在此背景下应运而生，其核心使命在于解决数据的异构性问题，通过将非结构化的原始数据严格遵循一套预先定义的标准Schema进行转换与映射，从而实现对数据的规范化、结构化和语义化重塑。这一过程不仅是简单的格式转换，更是深度整合数据治理与模型需求的关键步骤，它为后续一系列的数据质量控制（如清洗、去重、安全过滤）以及模型的高效学习与性能提升提供了不可或缺的、具有一致性的高质量数据基础。

## 现状
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 难点
然而，在当前的技术实践中，这一关键流程仍面临显著挑战。**现阶段的数据建模方法主要依赖于人工编写数据解析代码与映射规则**。这种高度手工作业模式存在诸多瓶颈：

* 首先，它需要投入大量的人力和时间成本，数据工程师需要为不同来源、不同格式的数据重复开发特定的解析脚本，效率低下且难以规模化。
* 其次，该方法难以应对复杂多变的数据场景，尤其在数据来源广泛、格式灵活多样的情况下，手动编写的规则难以穷举和覆盖所有样本变异，导致数据处理的覆盖率和泛化能力不足。
* 此外，随着数据源的不断扩充和Schema的迭代，大量定制化的代码还会带来沉重的维护负担和版本管理问题，最终成为制约数据生产效率和质量的关键瓶颈。

## 方案
因此，探索并构建自动化、智能化且可扩展的数据建模管线已成为提升预训练数据产线效能的核心议题。这要求我们从根本上革新现有方法，我们正致力于引入基于大模型的Code Agent解决方案，通过智能解析、自动生成映射逻辑与代码实现，将传统依赖人工编写的转换过程转变为高度自动化的智能处理流程。该方案能够自主理解原始数据结构、识别语义内容，并生成符合目标Schema的高质量转换代码，显著减少对人肉劳动的依赖，全面提升对海量多源数据的处理效率、覆盖范围与格式适应性，最终为训练更强大的模型提供坚实的数据基础。

### 模块化复用方案
![模块化复用方案](/personal-site-mvp/img/doc-placeholder.svg "模块化复用方案")
工程研发已构建Schema改造流水线，其中约50%的任务可由存量代码解决。对于复杂的数据结构改造需求，Agent能够自动生成个性化改造代码，并供生产研发进一步调整使用，支持50%的定制schema改造。

### Agent辅助方案
#### 辅助设计
[流程图]
#### 工作流
[流程图]
##### 卡片信息
```
---
description: 
globs: 
alwaysApply: true
---

获取icafe信息时，直接python3 get_icafe_info.py {icafe编号} 即可获取icafe卡片信息，可以重定向到本地文件
```
iCafe卡片操作API参考[获取单张卡片](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/NbX2gitgSF/cdae2324b4c643?t=mention&mt=doc&dt=doc)即可完成。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
基于上述脚本、规则可以获取执行iCafe卡片信息，包括「数据路径」、「数据场景」、「数据场景特殊信息」，成功将iCafe需求卡片的信息写到本地磁盘。

##### 采样数据
```
---
description: 
globs: 
alwaysApply: true
---
如果需要下载BOS数据，给定bos:/或者bos://开头的bos路径，使用bcecmd bos cp {bos_url} . 进行下载
```
添加上述bcecmd使用说明规则，指导Agent使用bcecmd进行采样数据

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 代码生成
现在已经包含

1. 任务描述信息（来自iCafe需求卡片各个字段信息）
2. 任务输入数据（通过bcecmd客户端采样BOS数据到本地磁盘）
3. 数据建模任务的目标Schema

接下来就需要让Agent通过参考历史任务、历史代码生成转换代码。配置如下规则

```
---
description: 
globs: 
alwaysApply: true
---
1、用户会提供iCafe编号信息，从当前项目下{iCafe编号}文件夹找到icafe.json的任务描述信息，{iCafe编号}/data则包含了任务输入数据
2、数据建模的Schema文件存放在当前项目的Schema/schema.txt，内部包含了Schema各字段以及相关语义描述
3、已经校验成功可用的历史代码存放在当前项目的src目录下，按照需求维度组织历史代码
4、生成的代码存放在{iCafe编号}/code，要求用Python完成
```


##### 1、接收用户输入Query
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 2、分析数据
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 3、生成代码
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 4、验收数据


![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 5、验收代码
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 总结
基于Agent构建了一套智能代码生成系统，以需求卡片和输入数据为驱动，通过Agent自动解析目标Schema文件，并结合历史生成的代码，实现从原始数据到标准化Schema数据的自动映射与转换。

该方案显著提升了数据建模的开发效率：

* **大幅降低技术门槛**：无需深厚的数据建模背景，研发人员可轻松上手，快速入门数据建模工作；
* **提升开发体验**：通过简洁直观的交互方式，开发者能够高效完成从基础到进阶的数据建模与代码开发任务；
* **推动流程标准化**：在减少人工编写代码的同时，保障输出代码符合规范，提升整体数据产出的质量和一致性。

这一方案不仅减轻了开发者的重复劳动，更在团队中实现了数据建模能力的普惠，让每一位研发同学都能无痛参与、高效贡献。

# 💗有奖互动💗
即日起至9月17日14:00，评论区留言互动：

###### 围绕AI数据建模，你遇到了哪些问题？有哪些好的实践经验
我们将挑选5个走心评论，特别送上**【打工小狗摆件】**～

![](/personal-site-mvp/img/doc-placeholder.svg "")
恭喜@[@朱雪儿](https://ku.baidu-int.com?t=mention&mt=contact&id=a05d5ea0-9391-11f0-9970-9d5d4652ae6f)[@金英](https://ku.baidu-int.com?t=mention&mt=contact&id=a6e657e0-9391-11f0-9970-9d5d4652ae6f)[@符琴](https://ku.baidu-int.com?t=mention&mt=contact&id=aa42f060-9391-11f0-9970-9d5d4652ae6f)[@丁丹](https://ku.baidu-int.com?t=mention&mt=contact&id=aef86220-9391-11f0-9970-9d5d4652ae6f)[@赵智聪](https://ku.baidu-int.com?t=mention&mt=contact&id=b4728370-9391-11f0-9970-9d5d4652ae6f)获奖~

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
