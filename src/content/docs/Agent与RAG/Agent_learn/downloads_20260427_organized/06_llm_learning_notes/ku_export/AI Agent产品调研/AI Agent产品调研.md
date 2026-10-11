---
title: "AI Agent产品调研"
description: "场内都有哪些大模型平台（model builder、app builder、agent builder的区别）："
date: "2026-04-28"
category: "Agent与RAG"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\AI Agent产品调研\\AI Agent产品调研.md"
---
# AI Agent产品调研
一、厂内（对外宣传统一model builder、app builder、agent builder）

场内都有哪些大模型平台（model builder、app builder、agent builder的区别）：

|  | ACG |  | MEG |
| --- | --- | --- | --- |
| 定位 | model builder | app builder | agent builder |
| 产品名称 | 千帆大模型平台 | AppBuilder | 文心智能体平台（之前叫灵境矩阵平台） |
| 关键定位 | 开发专属的大模型 | 开发专属的AI应用 | 利用自然语言开发智能体 |
| 区别（模型配置） | 不同版本文心大模型或开源大模型等 |  | 文心大模型4.0 |
| 区别（付费资源） | 调用模型付费 | c端用户生成应用需付费 | c端用户生成智能体免费 |

app-builder和灵境目前看上去功能还是挺像的，主要提供两种能力，一种是组件/插件能力，一种是agent能力；当前都是在不断丰富自己的组件/插件能力，然后重点迭代agent能力，目标是能让开发者比较快的复制已有的应用，或是通过选择已有的组件能力编排出新的应用。

modelbuilder-千帆大模型平台：提供一站式的大模型开发和应用服务。主要定位在开发专属的大模型，模型开发时不仅基于文心大模型，也可以基于开源大模型和其他生态合作伙伴例如百川大模型和智谱大模型。百度千帆 AppBuilder：基于大模型搭建 AI 原生应用的工作台。主要定位在开发专属的 AI 应用，应用开发时不仅基于文心大模型，也可以基于其他开源大模型等。文心 agent builder-文心智能体平台：基于文心大模型的智能体构建平台。主要定位在提供自然语言创建智能体的开发新范式，致力于解决行业关心的零成本智能体开发、分发和商业变现等核心问题。模型配置中，只能使用文心大模型 4.0。千帆平台之前使用介绍较多（API使用：、开源部署：、模型微调：），本文重点调研AppBuilder和文心智能体平台的agent使用。

AppBuilder任务背景：根据需求编写代码，执行代码，并根据执行的报错信息修复代码，得到最终符合需求的代码实现。需求：

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。示例 1：输入: “babad”输出: “bab”注意: “aba” 也是一个有效答案。示例 2：输入: “cbbd”输出: “bb”分析：至少需要工具组件代码执行器，代码修复。

1、创建工具组件目前支持的自定义组件：

![](/personal-site-mvp/img/doc-placeholder.svg)

执行代码的方式有2种，要么api，要么使用代码执行块

（1）api 不支持内网（如kirin）

内部的一些服务都有类似的限制，appbuilder无法使用内网api

![](/personal-site-mvp/img/doc-placeholder.svg)

![](/personal-site-mvp/img/doc-placeholder.svg)

（2）代码执行块 不支持os库或exec()

我们换一个场景单测生成：为函数生成单测入参

![](/personal-site-mvp/img/doc-placeholder.svg)

2、创建应用了解更多使用详情：这里的组件类似于coze中的工作流

发布后可以使用sdk进行调用

试用地址：https://appbuilder.baidu.com/s/T1lQoJ7A

总结：页面拖拽式创建agent，更适合快速构建rag或functioncall，简单的代码格式处理，稍微复杂的代码执行或内网的服务调用都是不支持的。

文心智能体平台和appbuilder同样的问题，也不能指定get接口的params，同时也没有代码解释器。

![](/personal-site-mvp/img/doc-placeholder.svg)

总结：适合简单场景的拖动快速构建。不适合代码修复。缺乏官方插件库，目前支持api和搜索，其他只能自己写插件。

二、厂外coze扣子平台（字节）了解更多使用详情：与上面两个agent的实验背景相同，需要写代码-执行代码-修复代码。

扣子有官方的代码执行器插件。(但不支持二次开发，如果要用在算子生成是走不通的)

工作流节点更加丰富，支持选择分支与代码处理。

模型选择更加多样，扣子除了文心，其他模型基本都支持，包括豆包、glm4、千问max、百川4、minimax6.5、月之暗面

![](/personal-site-mvp/img/doc-placeholder.svg)

![](/personal-site-mvp/img/doc-placeholder.svg)

![](/personal-site-mvp/img/doc-placeholder.svg)

发布后使用：

试用地址：https://www.coze.cn/store/bot/7386521255559594003

同时coze也是唯一一个支持多智能体的()，appbuilder和灵境只支持单智能体。

![](/personal-site-mvp/img/doc-placeholder.svg)

总结：coze有非常丰富的插件库，偏向B端创作者或专业开发者，而灵境偏向B端企业/机构。

其他参考：

其他GPTS（openai）https://chat.openai.com/

魔塔社区（阿里）https://modelscope.cn/my/overview

抖音豆包https://www.doubao.com/

快手Agentshttps://acg.baidu-int.com/article/3566

昆仑万维https://model-platform.tiangong.cn/





