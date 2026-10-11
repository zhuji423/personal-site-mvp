---
title: "核心内容速览"
description: "🌟Coding Agent实践：业务与平台的双向奔赴"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\🌟Coding Agent实践：业务与平台的双向奔赴.md"
---
🌟Coding Agent实践：业务与平台的双向奔赴

#### 🧑‍🏫 案例作者：AI原生研发圆桌会
#### 🎬 案例场景：开发
#### 🔧 使用工具：Onetool，Comate，Cursor
#### 📒 案例概要：本文分享了Coding Agent在业务与平台中的实践应用，通过AI原生研发圆桌会探讨了AI Coding与MCP的未来发展趋势。介绍了MCP在降低开发适配成本、提升协同效率及丰富中长尾工具生态方面的价值，同时指出了MCP服务使用中的关键问题，如工具稀缺性、质量参差不齐等。还展示了MCP工具链如何解决开发成本高、工具选择难等问题，促进AI研发提效的落地应用。
**导语：**

为加速AI原生研发新范式在研发团队的落地，今年在TSC的牵引下，BIT联合EE推出【AI原生研发圆桌会】，旨在聚焦AI原生研发场景，组织厂内有相关实践和交流需求的同学，围绕业务实践落地中面临的关键问题和挑战，过程中积累的经验/踩过的坑...展开深度的讨论与交流，促进跨业务间经验的流转与复用。

欢迎大家关注本期Coding Agent主题圆桌会的干货内容，并在评论区一同探讨交流！

# 核心内容速览
Coding Agent的高频使用，为我们的研发场景和效率带来了更多的可能，本期圆桌会聚焦『AI Coding』与『MCP』，线上&线下20位一线专家，围绕实际工作场景与对 AI Coding未来发展趋势的判断进行了深入探讨。现在，让我们一起回顾这场精彩的思想碰撞！

![](/personal-site-mvp/img/doc-placeholder.svg "")


现场分享视频请点击👉[研发数字员工 + MCP插件中心工具链介绍](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55371?activityId=8747?t=mention&mt=doc&dt=sdk)[AI 研发业界趋势及MEG应用现状](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55372?activityId=8747?t=mention&mt=doc&dt=sdk)

更多Coding Agent分享内容请点击👉[Coding Agent实践专区](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/special-detail/8747)

🎁欢迎参与文章结尾关于Coding Agent的有奖互动，说出你的想法与经验~

# 实践分享详情


#  主题1  MCP插件中心工具链介绍——颜志杰
## 1、背景
**现状**

* **业界共识**：**共识很重要**，MCP有成为LLM与外部数据源和工具间通信的标准协议的趋势，有类似"http协议"的感受，协议目前不完美，但是大家认可才是最重要的，其它的都可以不断完善
* **百度拥抱**：各业务正积极拥抱和探索MCP，当前有影响力的MCP应用还在探索中



**MCP协议处于早期：有较多工程化工具链诉求，但只有业界共识，这些问题都会在发展中解决**

* **协议不断发展变化、官方工程化语言支持不够**：比如官方没有golang/C++ SDK，0326对remote mcp调用支持OAuth认证，对于开发者来说需要适配
* **新增MCPServer常驻进程带来的开发和运维成本**：
    * 即使是一个简单的API查询、一个简单的脚本调用，也需要开发一个服务程序；如果把视角放到宿主机，则会出现N个mcp server进程，无论资源成本还是管理都是一个问题（如何启停、如何升级更新）
    * 由于每个mcp server独立进程带来相当一部分重复开发工作：不仅仅是该服务有可能API服务已经提供，还有比如认证、session维护、流控、可观测等功能设计

* **Token爆炸带来成本压力和较多工具选择成功率：**
    * **当前MCP缺乏对Tools的筛选操作设计**：Mcp Host一般是遍历mcp server提供的toollist，统一组装放入Prompt里面供模型选择，随着工具增多会极大增加**token长度以及带来工具描述如果不到位**，模型调用的效果将难以保障，比如github mcp server有26个工具，消耗3-4k的token




## 2、面向厂内的AI应用开发MCP工具链解决哪几个问题
EE推出MCP插件的工具链（**平台地址**：[https://console.cloud.baidu-int.com/comatestack/mcp](https://console.cloud.baidu-int.com/comatestack/mcp)），主要解决以下问题：

**【生产者】降低MCP Server的开发成本**

1. 提供面向厂内的**Remote MCP Server网关代理服务**，包括：
    1. **基于iapi服务，****提供存量OPENAPI转化为MCP Server**： 用户无须开发和部署mcp server：本质上需要实现openapi的yaml和mcp的json rpc的协议互转，当前阿里higress已经开展
    2. **提供mcp server的代理服务**：无论是你自己开发的MCP Server，还是从开源下载的MCP Server，通过注册SSE服务地址，提供remote远程代理服务，并包含
        1. 提供统一鉴权服务（厂内基于uuap认证以及token认证方式）
        2. 流控、可观测、日志等（通用网关具备的能力）


2. **提供基于宿主机的Local MCP Server服务**：**让本机脚本执行调用低成本实现，**一些简单的脚本、命令行可以更加方便的让大模型调用，不需要开发mcp服务，通过Local MCP Server常驻进程拉取命令到宿主机-->托管执行-->命令返回等操作



【**消费者**】**AI应用开发可以更高效的使用MCP**

1. **MCP市场**：厂内面向AI应用开发的MCP分享、包括基础平台方提供的通用MCP（比如icafe、icode、ipipe等）、行业MCP、业务自定义MCP服务
2. **实现Agent订阅MCP Server工具服务：token爆炸我们先解决一部分，**实现Agent<->MCP Server配置在远程存取；Agent可以选择MCP Server的Tool列表，不一定是全部的toollist，消费者能筛选到Tool级别，不仅仅是MCP Server级别；比如你发现github的MCP有26个工具，只要过我们的proxy代理服务，可以实现tools自定义筛选，不用每次让模型都把所有的tool list发给大模型
3. **MCP服务SLA监控和Trace**：请求通过Remote MCP Proxy，当后端代理服务SLA有问题，可以进行告警和trace；以及提供基于应用的trace

## 3、MCP工具链的实现方案
MCP工具链实现框架

[流程图]
配置管理模块mcp-plugin-center：

* **Agent消费者管理**：包括Agent服务身份申请与认证，为Agent下发clientID、clientSecret
* **MCPServer生产者管理**：主要包括MCP服务注册，包括
    * 开发的mcp server注册，以及常见的开源的mcp服务管理
    * 配置openapi和mcp server的互转，实现存量OPENAPI和MCP协议转换的配置
    * 配置面向local mcp server的脚本、命令等

* **Agent和MCP的关联关系映射**：哪个Agent需要消费哪个MCP Server的Tools

MCP代理服务mcp-server-proxy：

* 基于配置实现协议互转的Runtime
* 认证方式的实现，非Agent服务认证，而是Agent服务里面传递的用户身份认证

本地MCP服务Local-mcp-server：

* 拉取远程配置的命令行或者脚本，并负责执行命令、获取命令返回给MCP Client
* 未来会考虑将部分MCP代理服务的功能下放到本机Agent端，实现通过本地Local-mcp-server代理远端mcp服务

#### 使用体验（OPENAPI转MCP、本机脚本转MCP）请参考：[MCP工具中心（Onetool平台）使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/U9Q0FnOjJOfXaW?t=mention&mt=doc&dt=doc)
点击[MCP工具中心用户群](https://applink-infoflow.baidu.com/share/contact/open/?token=ynF1n-zjFORhxXLsKF5arqx_ZUMw3oUu0AJduU50oMo?t=mention&mt=doc&dt=sdk) 一键加入，一起探讨MCP的落地应用吧~~



# 主题2  AI 研发业界趋势及MEG应用现状——黄佳鑫
## 一、AI 研发业界发展方向和趋势
#### **1.1 应用方向一：AI 辅助编程，Cursor为代表**
通过**IDE或命令行交互**的方式，成为程序员随身数字助手，支持上下文感知、交互问答、即时调试等

**产品：**

|产品|公司|定位|演示视频|
|-|-|-|-|
|CURSOR|Anysphere* *|一款 IDE AI 编程助手类产品，其定位是一种“基于 AI 的开发环境”，可以帮助开发者更高效地编写、调试和管理代码|[https://www.cursor.com/ja](https://www.cursor.com/ja)|
|WINDSURF|Codeium|首个具备智能体能力的集成开发环境（IDE）——并不仅止于此。Windsurf 编辑器是开发者与 AI 真正协同工作的场所，带来宛如魔法般流畅的编码体验。|[https://windsurf.com/editor](https://windsurf.com/editor)|
|Comate、zulu、通义灵码、Trae、CodeGeeX等|百度、阿里、字节等|IDE AI 编程助手类产品，向cursor看齐。  rule、mcp、agent能力、独立的模型训练。 **复杂工程感知、自动记忆感知、工具使用、行间建议预测**|[https://lingma.aliyun.com/?userCode=okjhlpr5](https://lingma.aliyun.com/?userCode=okjhlpr5)|
|**Claude Code  CLI**|Anthropic|agentic tool，通过命令行，基于claude，专注于代码生成、代码理解、代码调试和编程辅助的AI产品或功能。适合后台任务执行，支持vscode、ide的集成|[https://www.youtube.com/watch?v=AJpK3YTTKZ4](https://www.youtube.com/watch?v=AJpK3YTTKZ4)|
|**Codex  CLI**|OpenAI|lightweight coding agent，基于专门训练的模型codex-1，可编写功能、解答代码库相关问题、修复 bug 以及提交拉取请求以供审核等。支持后台任务运行|[https://www.youtube.com/watch?v=FUq9qRwrDrI](https://www.youtube.com/watch?v=FUq9qRwrDrI)[https://github.com/openai/codex](https://github.com/openai/codex)|

#### **1.2 应用方向二：智能体主导的研发模式****                **程序员在需要的时候才干预，并Review效果
软件研发将由智能体主导完成，从需求到部署全流程自动化，Devops全生命周期AI化。

|类型|代表产品|介绍图|
|-|-|-|
|多智能体协作开发框架、协作系统|AutoGen、AutoDev、MetaGPT、CodeFusion、DevOpsGPT|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|智能体端到端解决问题|GitHub Copilot Workspace、Jules、Swe-Agent、Ghostwriter、Devin|![](/personal-site-mvp/img/doc-placeholder.svg "")|

**案例：**解决GitHub上的Issue，创建PR ；    

|产品|公司|定位|演示视频|
|-|-|-|-|
|**GitHub Copilot Workspace**|Microsoft|GitHub 2024年推出的一种 **全新 AI 驱动的开发环境**，它将 Copilot 从“代码补全助手”扩展为一个可以理解任务上下文、规划开发步骤、并参与实现和测试的 **端到端智能编程助手**。它的设计目的是帮助开发者更快地完成从需求理解到功能落地的全过程。**issue->specification->plan->implemention，可调计划/设计**|创建workspace解决issue、可ide调试，提交pr，触发后续ci/cd流程[https://www.youtube.com/watch?v=L5Xny6yehUg](https://www.youtube.com/watch?v=L5Xny6yehUg)|
|**Claude Code SDK**|Anthropic|agentic tool，Claude Code + GitHub Actions，在 PR 上标记 Claude Code，即可回复审阅者的反馈、修复持续集成 (CI) 错误或修改代码。|官方的github claude code sdk demo，[https://www.youtube.com/watch?](https://www.youtube.com/watch?v=L_WFEgry87M)[v=L_WFEgry87M](https://www.youtube.com/watch?v=L_WFEgry87M)turing issue to actual pr[https://www.youtube.com/watch?v=yGU1gHHItDA](https://www.youtube.com/watch?v=yGU1gHHItDA)|
|**Swe-Agent + G****ithub**|Microsoft|SWE agents 深度与github结合，人在github自然的ai就issue问题交互， 同时支持将ai的pr再次pull到ide进行编辑，提升解决问题的效率![](/personal-site-mvp/img/doc-placeholder.svg "")|SWE agents coming to GitHub[https://www.youtube.com/watch?v=VWvV2-XwBMM](https://www.youtube.com/watch?v=VWvV2-XwBMM)SWE-AGENT接近devin[https://www.youtube.com/watch?v=9-JBHGlYEBI](https://www.youtube.com/watch?v=9-JBHGlYEBI)|

#### **1.3 其他创新：代码自主演化与软件系统自我优化**       
软件系统将通过AI进行进化式开发（演化、选择、迭代），代码将像生物体一样通过“变异-选择-适应”机制自动进化

**案例：**Google的AlphaEvolve 通过自演化的方式，解决了数学、计算机科学等能给出明确评价标准的任务

**可应用场景：**Bug/Issue等可验证的业务问题解决，通过进化算法，提升完成效果

## 二、MEG 研发效能现状，及AI提效已落地应用
#### **2.1 项目交付过程：研发交付周期占整个项目交付周期的20%～61.5%，开发周期占比10%～30.7%**
项目交付包含需求创建、研发交付和实验3个环节，研发交付又包含开发、测试和上线3个阶段

![](/personal-site-mvp/img/doc-placeholder.svg "")
以信息分发产研为例，各阶段的具体周期如下：

|阶段|周期(人天)|研发环节周期占比|
|-|-|-|
|需求创建|5|无需跟进实验**研发交付占比：8.0/13=61.5%，开发占比：4.0/13=30.7% **需跟进实验研发交付占比：8.0/40=20%，开发占比：4.0/40= 10%|
|研发交付-开发|4||
|研发交付-测试|2||
|研发交付-上线|2||
|实验|27||

#### **2.2 AI研发提效实践：IDE辅助编码**
**公司内部Comate辅助编码已全量推行一段时间，但从落地来看：****IDE辅助编码****，能够提升研发编码效率，但是对研发周期作用不大**

* 从 MEG 大盘数据看**：代码生成占比的提升，跟人均吞吐代码行上涨正相关，但研发周期未明显变化**

**具体原因：**

* 代码编写只占整个研发流程中的一个环节，**IDE辅助编码****并没有带来研发模式的整体变革**，对整体研发周期影响有限（研发周期还包括了需求信息对齐、代码设计、调试、测试、发布、部署等多环节）
* 辅助为主，人主导，难以界定影响粒度和稳定的提效比例，**无法干预研发排期**，同时，受限于传统工期认知，存在即使编码提效，但研发周期无变化

#### **2.3 AI研发提效实践：Code-Agent模式，端到端场景**
##### 2.3.1 需求及交付在贴吧研发场景的应用
**效果：**2024年，贴吧单版本人效平均提升8.9%，吞吐带来13.9%的提升。

|**新增场景**|**单Story实际提效比**|**周期扣减程度**|
|-|-|-|
|轻量级接口|30%~80%|1人天->0.5人天|
|端到端后台服务|50%~90%|3人天->1人天|
|算子类|30%~50%|1人天->0.5人天|
|微服务|10%～30%|1人天->0.75人天|

**方案：**为了使AI能实现业务级交付，通过人工整理分场景的开发规范和业务知识，基于Deepseek+RAG生成代码，在贴吧论证了方案的可行性

##### 2.3.2 迁移类场景实践
**效果：**在搜索和EP的实践，AI带来至少6倍的人效提升：

|**搜索结果卡片技术栈迁移**|||**EP EOS技术栈迁移**|||
|-|-|-|-|-|-|
|**AI准确率**|**人工(单次)**|**AI(单次)**|**AI准确率**|**人工(单次)**|**AI(单次)**|
|90 %|14人日|1人日|97.6%|20分钟|3分钟|

#### **2.4 AI研发提效面临的挑战**
##### **2.4.1 对复杂业务理解推理的问题**
* **百度内部业务相对复杂，AI缺乏业务理解，较难准确完成任务**，如下：

|具体需求|模型|预期效果|实际效果|总结|
|-|-|-|-|-|
|矩阵-存钱罐产品需求生成研发设计 [[ailite-29174] 【server】【非随】【极速版存钱罐】上滑引导功能实验](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-29174/show?source=drawer-header?t=mention&mt=doc&dt=sdk)|deepseek-r1|涉及2个模块，4个修改接口[【矩阵】【目标】研发设计文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/D-uBqusitG/htRvootW3UG1YW?t=mention&mt=doc&dt=doc)|deepseek：接口准确率1/4，召回1/4claude：接口准确率1/4，召回1/4[【矩阵】【生成】研发设计文档V0](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/D-uBqusitG/oj-0mlnUh45-5j?t=mention&mt=doc&dt=doc)|如果只将文档的内容输给大模型，模型无法评估要修改哪些接口，**因为缺失功能和接口代码的关系。同时人工梳理关系知识输入模型后，准确率和召回率1/4不高**![](/personal-site-mvp/img/doc-placeholder.svg "")|
||claude4.0||||
|商业平台产品需求生成研发设计[[CPD-275093] TP切换服务商](https://console.cloud.baidu-int.com/devops/icafe/issue/CPD-275093/show?t=mention&mt=doc&dt=sdk)|deepseek-v3|涉及1个模块，15个新增接口[【测试集】TP服务商](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/D-uBqusitG/L8D8TFF1nOn67I?t=mention&mt=doc&dt=doc)|接口准确率5/11，召回5/15[【5.30】托管需求生成设计初版效果](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/D-uBqusitG/A-q53KNmT4EJzS?t=mention&mt=doc&dt=doc)||
||claude4.0||接口准确率10/20，召回10/15[【claude】TP服务商](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/D-uBqusitG/e0UlsZMP7KvA1b?t=mention&mt=doc&dt=doc)||
|蝴蝶游戏进度上报-代码修改[[ailite-28729] 【Server】【游戏中心】蝴蝶游戏进度上报-新增活动条件标识](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-28729/show?from=page&source=icode-commit-message-others?t=mention&mt=doc&dt=sdk)|deepseek-v3|在正确位置修改代码|修改失败|成功率受限于 代码的复杂度，相关代码越多，功能点越接近，对模型上下文理解能力要求越高，模型越容易出错，不同模型的成功率0%～30%左右[矩阵自动BugFix](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/D-uBqusitG/VSQi5Nq1LdJrPF?t=mention&mt=doc&dt=doc)[claude代码修改场景评测](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/D-uBqusitG/AkAQpvDbTCw-YF?t=mention&mt=doc&dt=doc)|
||claude3.7|在正确位置修改代码|修改失败||
||claude4.0|在正确位置修改代码|修改成功||
|矩阵上滑红包引导优化的bug修复[[ailite-29174] 【server】【非随】【极速版存钱罐】上滑引导功能实验](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-29174/show?source=drawer-header?t=mention&mt=doc&dt=sdk)|deepseek-v3|在正确位置修复代码|修复失败||
||claude3.7||修复失败||
|视频竞赛按钮文案bug修复[[ailite-29179] 【非随】【极速版存钱罐】任务列表任务顺序修改](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-29179/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)|deepseek-v3|在正确位置修复代码|修复失败||
||claude3.7||修复成功||

##### **2.4.2 从编码阶段提效到赋能研发全流程**
* 为了全面提升研发周期效率，**AI应不仅限于编码环节**，而是覆盖整个研发生命周期。包括：产品需求、生成研发设计、生成研发代码，生成测试用例并完成测试验收，需求上线。
* **把控好需求质量是第一步：**关于需求质量应该有较完善的标准及要求，需求质量的好坏决定了在后续研发环节的还原度，当然需求产生本身也应与AI充分结合。
* **具备研发设计能力：**通过对于需求的理解，以及对于业务系统知识的沉淀，AI应具备拆解需求并生成研发设计的能力，有了设计才能够完成编码。
* 代码的实现与验证：根据需求提前规划测试点，不断的调整代码实现策略，最终达成高质量代码的交付。

##### **2.4.2 引入先进的智能体架构，完成研发范式的升级转型**
* 让AI像工程师一样工作。
* 具备感知、决策、行动和反思的能力，模型与交付工具相结合，实现工业界编码领域超级智能体。
* 新研发范式下，思考工程师与AI的未来协作方式。

## 三、AI研发提效的建设思路
#### **大方向：以全智能化为远期目标**
#### **研发交付全环节提效的落地**
* **知识体系建设：**构建“作业-知识-经验”的闭环AI知识工程体系，降低知识整理成本，并让AI可实现业务级交付应用
* **AI能力打造：**结合先进模型，打造全流程多个Agent助手，赋能研发各个环节
* **流程重塑：**从纯人工 到 人为主，AI为辅， 再到 AI为主，人为辅，有希望类似贴吧，带来研发周期明显变化

[流程图]
#### **研发交付端到端提效：智能体主导，程序员在需要的时候才干预，并Review效果**
初期可优先探索的场景

* **BugFix类，有明确的修改CR及Bug说明，由AI端到端自主修复和修复后验证**

![](/personal-site-mvp/img/doc-placeholder.svg "")
* **算子开发场景，有相对清晰的输入输出，开发模式有一定同质化，较适合由AI端到端完成。**

未来

* 工程师将更多聚焦于上层设计、架构决策和创新型问题解决，而非低层阶的编码实现。工程师定义问题或需求，验证Agent来确保代码符合业务目标。



## 四、Q3的计划与合作探讨
**与业务的合作：**

选择共建业务，探索全环节的AI赋能，攻克需求规范、需求生成设计、设计生成代码、代码自主测试能力。   

**与ee的合作：**

* ai数字员工，让AI拥有人一样的权限
* 辅助编码环节与zulu做协同，  0-1生成后，可以1-n跳到zulu再次编码
* zulu提供封装能力，可在容器独立运行



**如何让研发更愿意表达和使用，以助手的思路使用AI**



ai赋能的交付抛个砖：

[流程图]
# 有奖互动
即日起至**7月22日18:00**，在评论区留言，任选下方3个问题回复：

####  1.关于Coding Agent，聊一聊你所在业务下的实践和工具～
####  2.围绕Coding Agent，你还有哪些希望讨论的话题？
#### 3.AI辅助编码，你有过哪些神操作想安利给全世界？
我们将挑选10个走心评论，特别送上【BIT蛇年小熊 或 福禄摆件盲盒】～

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 本期获奖公示
##### 获奖名单
|**梁婕妤**|**孙健欣**|**张鑫宇**|**常闯**|**李大宇**|
|-|-|-|-|-|
|**张祖亮**|**罗晓霞**|**黎梓涛**|**陈品天**|**李颖霞**|

##### 奖品领取
恭喜获得【BIT蛇年小熊 或 福禄摆件盲盒】一个！

请联系[@王粤佳](https://ku.baidu-int.com?t=mention&mt=contact&id=9be944f0-65d9-11f0-9af5-3f2fea62abb4)领取奖品（非科技园工区伙伴可邮寄）~❤️

# 推荐阅读
[🌟打破交付质效天花板——AIQA厂内落地实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/Lx-UGL0HrgEBeO?t=mention&mt=doc&dt=doc)

[Coding Agent在日常开发中的应用](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/r1nLoPXfl6WVyP?t=mention&mt=doc&dt=doc)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
