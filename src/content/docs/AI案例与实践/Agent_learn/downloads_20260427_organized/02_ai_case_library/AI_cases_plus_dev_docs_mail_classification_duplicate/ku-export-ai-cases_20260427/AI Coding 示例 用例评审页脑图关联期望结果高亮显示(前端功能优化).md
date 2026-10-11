---
title: "实践简介"
description: "AI Coding 示例: 用例评审页脑图关联期望结果高亮显示前端功能优化"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI Coding 示例 用例评审页脑图关联期望结果高亮显示(前端功能优化).md"
---
AI Coding 示例: 用例评审页脑图关联期望结果高亮显示(前端功能优化)

#### 🧑‍🏫 案例作者：[@王哲](https://ku.baidu-int.com?t=mention&mt=contact&id=e6b42a50-fce6-11f0-9b15-af290a0ba15f)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Cursor
#### 📒 案例概要：本文介绍了通过AI Coding实现前端功能优化的案例，针对用例评审页脑图关联期望结果高亮显示的需求，利用AI Coding自动修改代码，实现了期望结果换行显示及与测试步骤对应行的高亮关联，显著提升了开发效率与质量，展示了AI在前端开发中的高效应用。
# 实践简介
该案例是前端测试智能化项目中一个真实的、来源于用户反馈的一个小的前端需求。

我们基于 Coding Agent 彻底完成了相关的功能开发，不需要自行修改一行代码就可以由 Coding Agent 一次性搞定上线。

从这个案例可以看出，对于一些简单的小需求，只要我们能将需求 & 问题定义清楚，Coding Agent 大概率可以彻底搞定，我们只需要做一些测试和验证即可。

# 关键词
前端优化、独立功能实现

# 具体实施
## 需求来源
[[baidu-testmate-web-ui-aitester-319] 【端到端测试】对于脑图中每个测试点的展开预期结果可以高亮显示对应的测试步骤](https://console.cloud.baidu-int.com/devops/icafe/issue/baidu-testmate-web-ui-aitester-319/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)

## 示例任务
[https://ai-assistant-web-testmate.now.baidu-int.com/68e77ec50a594e42ac3ad838/e2e-prd-design-workflow](https://ai-assistant-web-testmate.now.baidu-int.com/68e77ec50a594e42ac3ad838/e2e-prd-design-workflow)

现象:

![](/personal-site-mvp/img/doc-placeholder.svg "")
测试步骤对应的行已经高亮展示了，但是预期结果有两个问题:

1. 没有换行
2. 对应的步骤2的期望结果没有高亮展示



## 基于 AI Coding 的问题分析 & 实现
基于关键词查询相关代码，通过 AI Coding 软件 Ask 相关实现原理。

比如: 基于【的步骤已高亮显示】查询对应代码:

![](/personal-site-mvp/img/doc-placeholder.svg "")
AI Coding Ask：

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
可以看到，关联的本质是测试步骤里是 List[Dict] 的格式，其中有一个 cover_point_ids 的字段。从来实现是高亮关联。



AI Coding Plan 方案设计:

Query:

> 现在，我希望期望结果字段(overall_expected_outcome) 也可以和测试步骤一样，可以换行显示，同时也可以按需高亮(期望结果可以对应到指定测试步骤上)
> 但是，现在期望结果本身是字符串格式
> 例如:
> "1. 注册页面成功加载。\n2. 注册页面UI元素正确展示：页面标题显示为【创建新账户】，用户名输入框显示且标记为必填，密码输入框显示且标记为必填，确认密码输入框显示且标记为必填。\n4. 系统提示用户名长度不足的错误信息(例如【用户名长度应为6-20个字符】)，错误提示在表单附近清晰展示。\n6. 系统提示密码长度不足的错误信息【密码长度至少6位】，错误提示在表单附近清晰展示。\n9. 系统提示两次密码不一致的错误信息【两次输入的密码不一致】，错误提示在表单附近清晰展示。\n13. 注册成功：账户在数据库中成功创建，用户输入的明文密码被加密后存储到数据库，数据库中存储的密码不是明文形式。\n14. 页面自动跳转到【登录账户】页面。\n15. 登录页面UI元素正确展示：页面标题显示为【登录账户】，用户名输入框显示且标记为必填，密码输入框显示且标记为必填。\n18. 登录失败：后端查询到用户存在，但输入密码加密后与数据库存储的加密密码匹配失败，系统提示错误信息【用户名或密码错误】，错误提示在表单附近清晰展示。\n21. 登录成功：后端查询数据库返回用户信息，输入密码加密后与数据库存储的加密密码匹配成功，后端生成并返回有效的用户会话信息。\n22. 页面自动跳转到首页PAGE_HOME。\n23. 首页上【退出登录】按钮正确显示。\n25. 退出登录流程执行成功：页面显示成功提示【已退出登录】且提示在页面明显位置展示，页面自动跳转回首页，用户会话已从系统中清除。"
> 期望结果是用换行分隔的，同时每一行的前面的序号对应的是测试步骤的编号。
> 帮我设计一下如何实现:
> 1. 换行
> 2. 对应的测试步骤如果高亮的话，期望结果对应行也高亮。
> 
![](/personal-site-mvp/img/doc-placeholder.svg "")
AI Coding 软件会进行一些 Plan，有时也会做一些默认性假设，如果假设不符合预期，你可以通过对话的方式进行纠错。

然后会产出一个标准的设计方案:

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
你可以阅读整个的设计方案，如果有问题，可以让它继续调整，如果没问题，直接确认即可。

![](/personal-site-mvp/img/doc-placeholder.svg "")
修改完成后，可以依此 Review 每个变更:

![](/personal-site-mvp/img/doc-placeholder.svg "")
等等。

没问题的话，可以直接采纳。



## 测试&效果验证
通过方案 & 代码的评审，可以在一定程度提升可靠性，但是最终的效果是需要靠测试来验证的。

你可以本地启动对应服务进行测试。

以本需求为例子：

![](/personal-site-mvp/img/doc-placeholder.svg "")
可以看到效果验证符合预期啦~

接下来可以看着和测试更多的一些场景，测试完成没问题就可以上线啦。



## 说明
在整个需求中，我实际仅负责找到了对应的相关代码。然后提出了需求并审阅了方案和代码并进行了测试。

实际上并未针对方案和代码进行任何的调整和修改，整个的功能就已经完成了开发。

这其实也充分说明了 AI Coding 对研发模式的影响和变化，可以让一个不太会前端功能开发的同学在 10 分钟内完成一个小的需求迭代开发，效果甚至超过了部分专业前端同学。

但是，需要重点说明的，这种模式对于测试的依赖性较强，需要发挥测试同学的优势进行完备测试验证来保证产品质量。

# 复盘
## 模式：（好的经验）
1. 先让 Agent 去 Plan，然后再修改代码，往往可以得到更好的结果，同时，也可以帮助我们好全的思考需求；
2. 基于关键词等方式快速检索到需要修改的文件位置或相关功能入口，可以大幅降低 Agent 任务思考的复杂度，提升代码生成效果；
3. 随着交给 Coding Agent 的工作越来越复杂，Coding Agent 耗时也会不断提升，甚至在一些非常复杂的场景中，可能耗时能达到20分钟以上，但是一旦信任养成、协同模式磨合好的话，你会发现你真的可以同时指挥好几个"人"来完成不同工作了，效率飞速提升。

## 反模式（不要这么做）
1. 问题定义不要太模糊，同时输入信息要给足，例如在上述场景中 overall_expected_outcome 的示例数据的提供对于模型理解相关功能的逻辑至关重要。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
