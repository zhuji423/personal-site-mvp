---
title: "**大纲**"
description: "Coding Agent在日常开发中的应用"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Coding Agent在日常开发中的应用.md"
---
Coding Agent在日常开发中的应用

#### 🧑‍🏫 案例作者：[@张立理](https://ku.baidu-int.com?t=mention&mt=contact&id=976d4540-fce0-11f0-a06a-57ba2daee414)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文由前端架构师张立理分享Coding Agent（含Zulu）在日常开发中的应用实践。内容涵盖Agent能力边界界定、Query与Rule的使用技巧（如大规模任务的Plan&Act、超长上下文Summary），并通过异步迭代器工具库案例详解Rules编写规范（含Should/Not约束）。最后展望了多智能体协同解放人力、语义编码及计划循环等未来趋势。
Coding Agen话题正在厂内被热烈地讨论着，本期特邀【前端架构师-张立理】从开发者视角出发，结合实际开发场景与案例，探讨如何高效利用Coding Agent提升开发效率，分享实践与技巧。相信能给各位同学带来一些新的思路与启发，快来看看吧～

**课程链接：**[Coding Agent在我日常开发中的应用](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55368?isFromPc=1&reportLog=true?t=mention&mt=doc&dt=sdk)

# **大纲**
#### [一、Coding Agent & Zulu内部揭秘](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/r1nLoPXfl6WVyP?block_id=docyg-33802b70-4b50-11f0-8da4-07f1ec6566a1&type=card)
#### [二、Agent能力与边界](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/r1nLoPXfl6WVyP?block_id=docyg-de6b82a0-4b50-11f0-8da4-07f1ec6566a1&type=card)
#### [三、Query与Rule的使用实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/r1nLoPXfl6WVyP?block_id=docyg-e7dad2f1-4b50-11f0-8da4-07f1ec6566a1&type=card)
#### [四、多智能体协同的未来展望](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/r1nLoPXfl6WVyP?block_id=docyg-f0383e11-4b50-11f0-8da4-07f1ec6566a1&type=card)
# 一、Coding Agent&Zulu内部揭秘
# Coding Agent & Zulu
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 使用工具自动化地完成任务


![](/personal-site-mvp/img/doc-placeholder.svg "")




![](/personal-site-mvp/img/doc-placeholder.svg "")
## Zulu内部的重要工具
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 全模型的图像多模
![](/personal-site-mvp/img/doc-placeholder.svg "")
## Zulu所没有的……
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 二、Agent能力与边界
# Find the Boundary
## 与大模型协同,找到任务边界
![](/personal-site-mvp/img/doc-placeholder.svg "")
---

## 代码定位与分析
[附件]
[附件]
## 线上日志分析解决
[附件]
## 参考已有逻辑实现新业务
[附件]
## 进行重复工作
[附件]
# 三、Query与Rule的使用实践
## Query&Rule
## Query—每一个需求的起点


![](/personal-site-mvp/img/doc-placeholder.svg "")
## 提供更丰富的实时信息
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 提供行动大纲 - Act As Planned
参考 #actor.ts ，为 #couple, #henshin, #ringRing, #standalone中的各个role的实现做以下修改：

1. 按照`provideToolSet`方法把字符串部分提到外面去作为tools变量

2. 修改`provideToolSet`使用提出去的变量

3. 增加`toolFactory`成员，在构造函数中注册tools

4. 增加`provideToolImplement`方法，使用`this.toolFactory` 有部分role的实现中有自定义的非字符串形式的tool，这部分保留下来，事后我会做手动修改



## 大规模任务 - Plan & Act
我需要完成以下任务：XXXX

现在请分析整个项目，帮我**生成一个修改计划**，并拆解为多个可验证的小任务。先不要进行代码的修改，生成一个plan.md放置在项目根目录，文件内使用markdown的待办格式标记每一个子任务

现在开始根据plan.md**自上而下依次完成**还处在未完成状态的子任务，完成后在plan.md中将该任务为已完成状态，并开始下一个子任务

你一次**最多完成10个子任务**，完成后中止，我将对完成情况进行检查



## 超长上下文 - Summary To New
对上面的任务过程做一个总结，你需要按照以下要求来组织内容：

1. 对任务的具体要求进行摘要，描述任务的目标和大致的要求
2. 提供任务推进和完成的过程和线索，以任务分析、拆解的角度提供有效且压缩的信息
3. 如果当前的任务并没有被彻底地完成，在以上信息之后提供一个后续待办事项，较详实地罗列需要进行的工作和每一项工作明确的完成目标
4. 特别地，你需要输出一个列表，详细地罗列以下信息：

    * 你读取的每一个文件，以及该文件内容的简要描述
    * 你编辑的每一个文件，编辑的目的和内容的简单总结
    * 你执行的每一个命令，该命令是否成功和命令输出的摘要



## Rules - 人、项目、AI的桥梁


![](/personal-site-mvp/img/doc-placeholder.svg "")


## 看一个实例
![](/personal-site-mvp/img/doc-placeholder.svg "")


## What - 代码库和各名词是干啥的
这是一个工具库，提供一系列的工具类来对async-iterable类型进行操作，可以将异步迭代器封装成和**普通数组类似的形态**，并使用各种方法对迭代器中的数据进行遍历、过滤、映射。

代码库的核心有3部分：

* 一个AsyncIteratorController类能进行异步迭代器的读写控制
* 一个over函数对异步数据源进行封装，变成AsyncIteratorController
* 一些factory函数将事件、定时器等不同源转为异步迭代器

本代码库中的**常见概念**：

* operator：也叫运算符、函数，指挂载在over函数上的一个运算符，处理一个输入与输出都是AsyncIterator类型的逻辑



## Where - 关键的代码在哪里
项目的**主要结构**：

* src/controller.ts：实现AsyncIteratorController类，一个可以手动写入数据的异步迭代器
* src/helper/index.ts：实现over函数把异步迭代器转为OverAsyncIterator对象，可以向数组一样操作
* src/helper/operators/*：每一个文件包含一个over函数上的方法
* src/factory/*：每个文件处理一种数据源转为异步迭代器
* src/index.ts：最终导出用户可用到的函数和类



## How - 常见场景怎么写代码
当需要添加一个异步迭代器上的处理函数时，需要**按以下步骤**：

1. 在src/helper/operators下新建对应的文件，在文件中实现一个输入和输出都是AsyncIterable类型的函数，注意泛型
2. 在src/helper/operators/__tests__下补充单元测试，确保100%分支覆盖率
3. 在src/helper/index.ts中引入新的函数，并在类型定义和具体实现中都加上该函数
4. 在src/helper/__tests__/index.test.ts下，补充被over封装后的单元测试
5. 在src/index.ts下，导出且**仅导出**新的函数使用到的类型，**不要**导出函数本身

你可以**参考**src/helper/operators下的其它函数**作为一个模板**来实现新的处理函数，需要注意**完全符合函数的输入输出类型**，在over函数下完可用



## Should - 正向控制生成行为
在本代码库中编写代码，需要严格遵守以下要求：

* 各操作函数**不是**数组的方法，**永远不要**引入lodash、rambda、rxjs等三方库，本项目不基于任何三方库实现
* 所有代码均由TypeSript编写，类型必须正确且最大限度地严格
* 任意代码变更都必须有相应的单元测试，单元测试放置在源码文件同级目录的__tests__子目录下，与源码文件同名，后缀为.test.ts
* 使用细粒度的文件和函数拆分，函数不超过100行，文件不超过200行，但如果当前文件已经超过这些行数限制，你需要保持现状，**不要**对它们进行拆分
* 在完成一次实现后，必须：

	- 使用npm run build**确保构建通过**

	- 使用npm run test**确保单测通过**，且**分支覆盖率必须大于95%**



## Not - 反向约束错误行为
额外地，你需要关注以下行为：

* 在当前项目的情境下，操作函数如map、group等****不是**数组上的方法**，**不等同lodash、ramda等库**，它们都运作在异步迭代器（AsyncIterable）类型上
* ****不要****在src/index.ts中导出具体的操作函数，它们统一通过over函数被使用
* 代码库的单元测试全部使用vitest框架进行，****测试框架不是jest****，在编写单元测试时，你需要使用import来引入test、expect等函数
* **不允许**通过删除当前已经存在的测试用例来让单元测试通过，****不得**修改vitest.config.ts和tsconfig.json文件**

# 四、多智能体协同的未来展望
# Multi-Agent
## 多角色的关键——解放
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 多角色协作完成需求
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 语义性编码-成本可控的高质量代码生成
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 计划循环-通过拆解提升任务完成度
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 检阅管控——工程完整前提下确保高质量
![](/personal-site-mvp/img/doc-placeholder.svg "")
[附件]
# 有奖互动
即日起至**9月19日18:00**，在评论区留言，任选下方2个问题回复：

####  1.你有哪些AI Coding技巧？
####  2.你对AI Coding看法或期待是什么？
我们将挑选5个走心评论，特别送上【BIT蛇年小熊或国潮小马摆件盲盒】～

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 本期获奖公示
恭喜[@贾舒瑞](https://ku.baidu-int.com?t=mention&mt=contact&id=f6062d00-9544-11f0-8779-377dcb67db40)[@何银磊](https://ku.baidu-int.com?t=mention&mt=contact&id=0662ddb0-9545-11f0-8779-377dcb67db40)[@员佳音](https://ku.baidu-int.com?t=mention&mt=contact&id=2e7d96f0-9545-11f0-8779-377dcb67db40)[@黄兰](https://ku.baidu-int.com?t=mention&mt=contact&id=43858030-9545-11f0-8779-377dcb67db40)[@胡雅洁](https://ku.baidu-int.com?t=mention&mt=contact&id=4d43dae0-9545-11f0-8779-377dcb67db40)在本期评论中获奖，

请联系[@李思晗](https://ku.baidu-int.com?t=mention&mt=contact&id=536e8780-9545-11f0-8779-377dcb67db40)领取奖品（非科技园工区伙伴可邮寄）~❤️

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
