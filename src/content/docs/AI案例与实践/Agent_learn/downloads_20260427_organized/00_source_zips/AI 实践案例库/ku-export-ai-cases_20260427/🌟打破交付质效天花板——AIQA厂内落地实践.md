---
title: "核心内容速览"
description: "🌟打破交付质效天花板——AIQA厂内落地实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\🌟打破交付质效天花板——AIQA厂内落地实践.md"
---
🌟打破交付质效天花板——AIQA厂内落地实践

#### 🧑‍🏫 案例作者：AI原生研发圆桌会
#### 🎬 案例场景：测试
#### 🔧 使用工具：数字员工
#### 📒 案例概要：本文探讨了AIQA在研发质效提升中的应用，通过AI原生研发圆桌会分享了AIQA的下一代交付模式设想，即以AIQA为核心的交付过程。AIQA作为智能体，具备业务理解、测试专长和自动化执行能力，可替代真人完成需求分析、测试执行等任务。文中还介绍了AIQA在商业需求端到端交付、搜索前端自动化测试等场景的实践案例，展现了AIQA在提升交付质效方面的巨大潜力。
**导语：**

为加速AI原生研发新范式在研发团队的落地，今年在TSC的牵引下，BIT联合EE推出【AI原生研发圆桌会】，旨在聚焦AI原生研发场景，组织厂内有相关实践和交流需求的同学，围绕业务实践落地中面临的关键问题和挑战，过程中积累的经验/踩过的坑...展开深度的讨论与交流，促进跨业务间经验的流转与复用。

欢迎大家关注本期AIQA主题圆桌会的干货内容，并在评论区一同探讨交流！

# 核心内容速览
大模型技术的飞速发展给传统质效工具建设提供了更多的想象空间，更为改变现有交付模式，提升交付质效天花板创造了更多可能。本期圆桌会聚焦AIQA主题，线上&线下28位一线专家，围绕实际工作场景与实践落地经验进行了深入探讨。现在，让我们一起回顾这场精彩的思想碰撞！

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=caa2265bbb444b16aadb34948304987e&docGuid=Lx-UGL0HrgEBeO "")
现场分享视频请点击👉[面向未来的下一代交付模式](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55415?activityId=8747?t=mention&mt=doc&dt=sdk)[有方测试助手](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55416?activityId=8747?t=mention&mt=doc&dt=sdk)

[语音数字员工阿童木建设及落地](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55417?activityId=8747?t=mention&mt=doc&dt=sdk)[【智研师】助力研发项目迭代效率提升](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55418?activityId=8747?t=mention&mt=doc&dt=sdk)

更多Coding Agent分享内容请点击👉[Coding Agent实践专区](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/special-detail/8747)

🎁欢迎参与文章结尾关于AIQA的**有奖互动**，说出你的想法与经验~

# 实践分享详情


#  主题1  面向未来的下一代交付模式——刘道伟
## 1.什么是下一代交付模式
### 1.1 下一代交付模式设想
在软件交付的发展过程中，我们经历了由全面的**手工测试(第一代)到自动化测试及部分智能化（第二代）**的过程，在23年也逐步开始引入"无人值守"概念，但是当前的无人值守依然是由自动化的工具+质量度的分析报告的模式组成，这种模式下更多的是把原本自主测试的需求转换到无人值守，对于研发感知上这种需求并没有经过QA跟进，可能会跟免测等同。

当OpenAI的o1/o3、DeepSeek R1等新一代模型不断突破复杂推理的极限——从跨领域知识整合到结构化思维构建，甚至开始动摇人类"快思考"（直觉判断）的认知边界时，一个更具颠覆性的命题正在浮现：**基于大模型的智能体（AI Agent）是否有希望演变为人类在认知行为过程中的另一种数字孪生？** **如果Agent具备足够的交付领域知识和工具执行能力，是否可让AIQA来替代真人来满足交付过程中各类工作。**

在AIQA可实现的前提下，**下一代的交付模式应该是打造****以AIQA为核心的交付过程，提供的是AIQA的服务，通过给需求和任务分配一个AIQA，给每个RD和QA真人提供一个AIQA助力。**

[流程图]


### 1.2 如何理解AIQA
在新的交付模式中，AIQA不是一个虚拟的概念，是一个**实实在在的Agent**，**依托EE的数字员工的机制**，AIQA也会有具体的身份，对AIQA的能力也有更一些基本的要求

* **更懂业务 **- 真人员工可能只熟悉自己日常接触的业务，而数字员工基于RAG能力，可以比任何一个人，甚至比团队所有人加起来更懂业务
* **更懂测试 **- 真人员工的测试经验来源于个人的日常学习积累，各个员工的水平参差不齐，数字员工可以学习历史上的各个项目的测试经验，并能够通过数据飞轮持续成长，能够实现每个数字员工都是一个质效领域的专家。
* **更能测试** - 真人员工很难掌握业务的全部的工具，而数字员工通过MCP能够看到各类工具，并且能够进行智能的选择工具，完成各项测试执行工作

AIQA也不是只有一个，而是一个**AIQA的矩阵，**可以按照业务划分（商业的、搜索的），也可以按照测试能力划分（擅长前端的、擅长服务端），或者按照支持的场景分（环境的、定位的）；这些Agent可以由各个业务自己构建。

* 在需求测试场景，对于AIQA可完成的**简单需求端到端交付**；既可以直接把icafe分配给一个适合的AIQA，AIQA接受需求后，自己去读MRD，分析需求，产出测试方案，自动的执行测试，提交bug，给出测试的结果。
* 在垂直场景，AIQA可以**作为真人的帮手完成任务**，比如完成一个环境搭建，数据构造等，不同于现在query+工作卡的模式，**AIQA的工作是以目标为导向的，可以自主思考规划和使用工具完成**。
* 在交互场景，AIQA也可以作为**真人的分身**，替代真人完成研发咨询、日常值周等交互的工作。

再扩展一下，不只是在交付场景，在质量的场景也可以通过这种模式来提供监控、定位等服务。

### 1.3 从传统到AIQA模式的转变
#### 1.3.1 从脚本工具到传统Agent到AIQA
***【从Agent看为目标负责】***

最初“它们”被称为测试脚本、测试工具，后来是平台化下的API+页面交互（中间有一些小进化是API+前端低代码平台），最近被称为Agent，接下来会是AIQA的一部分

[流程图]
|**不同时期的Agent**|**为“？”负责**|**举例**|**与人的交互**|**信息丰富度**|**任务复杂度**|
|-|-|-|-|-|-|
|常规Agent（大多）|执行|【交付场域】交付Agent：洞察、规划、执行、决策触发：进入阶段执行、人工触发执行为执行负责：确保执行的稳定性、准召率等|一轮单次*PS：多轮那是助手/机器人的事情*|“内心戏”多，就是不说*PS：依赖数据多、大模型交互，但是人不知道，也缺少落盘*|单个任务，可能也会拆少数异步任务，但难回收|
|AIQA的Agent|目标|【交付场域】AIQA的Agent：完成项目测试触发：项目进入开发首次触发、过程持续盯盘为目标负责：确保项目测完|多轮，直到目标达成|信息丰富，逻辑顺畅，沉淀落盘便于后续分析总结和知识挖掘|任务层级，可拆子任务来独立进行，父任务负责回收整合判断事件中心串联Agent与工具，形成丝滑闭环|

#### 1.3.2 从机器人到传统助手到AIQA
***【从助手看为目标负责】***

[流程图]
## 2.下一代交付模式的设计
### 2.1 整体设计
如下图所示：整体数字员工分为基础依赖（紫）、业务Agent（绿）、数字员工基建（橙）、交互入口（蓝）四个部分：

* 基础依赖：包含知识建设、工具建设（MCP）、模型建设三个部分，主要是给Agent提供知识供给、思考能力、使用各类工具的能力；
* 业务Agent：各个业务建设的Agent框架，业务可按需灵活使用不同架构的Agent，但是对于数字员工，Agent需要升级以具备复杂任务的拆解，任务执行的规划，任务的反思等能力，同时为了支持复杂的异步子任务，业务的Agent需要与任务系统和事件中心打通。
* 数字员工基建：包含任务中心、事件中心、数字员工基建部分，主要是为Agent提供复杂异步任务的创建、管理、触发等能力，并支持Agent拆分子任务给其它Agent（A2A）
* 交互入口：交互入口包含如流入口（助理、机器人、数字员工）、平台入口以及新增的工作台界面；如流入口中并非全部都需要数字员工，对于简单问答和简单的场景，还是直接通过如流快速返回即可，对于复杂场景的任务，可通过任务的方式触发数字员工执行；工作台是新增的数字员工交互界面，提供类似manus的交互方式。

[流程图]
### 2.2 Agent能力升级
**AIQA的Agent能力由不同业务按照场景进行建设，统一与AIQA的基建进行对接，因此对Agent的实现方案不进行强制的约束，业务可以按照自身的需求进行建设。****Agent的能力决定了AIQA的能力的上限，是未来AIQA发展的关键**

24年大部分都Agent都是workflow的，Manus出圈后自主规划的agent越来越火，但是业界对于两种方式也存在的巨大的争议。不过在交付的领域，对于agent的模式还是可以两者结合的，不是非此即彼。对于比较明确的flow，可以继续使用wokflow保障精准执行，但是为了能够适应更多的场景，也需要进行自主规划能力的升级。

**一个简单的自主规划的Agent实现方案如下：**

* 在**Agent内增加思考和计划的层级**，Agent能够根据需求和当前情况制定并更新计划，通过计划把洞察、规划、执行、决策这些Agent动态的编排起来。
* **交付过程中涉及到所有的动作都通过Tool的方式进行封装**，包含了测试的执行的部分，需要打通xstp、itp、QAMate等各个自动化的平台。Agent过程中遇到问题，需要能够自主进行思考及调用工具解决。
* **Multi-Agent的执行是接受委托后即开始，不区分具体的阶段，Agent自己根据需求和代码的情况判断当前阶段及需要执行什么操作**，如果遇到当前无法继续执行，如需求还没有提测或者需要等待RD下一步操作的情况，Agent需要能够通过如流tool 通知相应人员，并且挂起，等待事件中心激活后继续执行。

[流程图]


### 2.2 产品形态
结合当前的的交付产品的现状，AIQA在产品模式上主要会有两大类产品。

* **一个基于平台的AIQA：**以当前的交付平台（TestOne或其它）为入口，平台提供AIQA的接入能力，可以通过平台给需求分配AIQA，并能够展示AIQA的工作的过程。*注意：这种并不是原有平台替换掉，因为并非全部的需求都适合AIQA，是在当前的模式种新增一个AIQA的工作模式，这种AIQA的工作模式也可以分配到当前平台的各个环节中。*
* **一个是基于如流的AIQA：**以如流为载体，通过超级助理、服务号、机器人、虚拟账号提供的AIQA服务，可以在如流上通过对话满足用户的各个目标任务，和当前助手的区别是1）具备思考能力，不是简单的问答和工作卡 2）打通工作台，可以通过工作台完成复杂的任务

**AI-QA 工作台**是一种为**智能体（AI Agent）**而设计的集成化平台。它通过提供协作框架、交付工具链、资源管理，帮助各业务高效承接具备自主动态决策、任务规划执行和交互能力的AI Agent系统。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=98ffece60e084661b24ce76d3e836450&docGuid=KOTmFUIrSbqCmN "")
### 📎 **会话区：自然语言交互的核心入口**
---

* **功能定位**：
    * 会话区是用户与AI Agent交互的核心界面，用户通过**自然语言输入任务需求**，系统实时解析意图并生成任务执行计划。

* **交互方式**：
    * **动态反馈**：用户输入后，系统会即时显示任务拆解步骤，支持流式展示AIQA的思考过程&任务拆解。
    * **过程可见：**针对每一个具体任务，会调起获取AI Agent的历史会话记录&执行情况，AI Agent可独立工作，无需持续监督，过程可视化。


### 📎 **执行详情区：工具控制台**
---

* **功能定位**：
    * 是用户理解任务执行逻辑、干预流程和掌握细节的核心界面。目标是通过可视化、实时反馈和交互式操作，让用户对 AI Agent 的【思考-规划-执行】全流程实现**透明化控制**。

* **交互方式**：
    * **节点交互**：点击子任务节点，可查看详细工具执行过程，如环境、qamate等，支持点击工具卡片展开详细执行日志和响应结果。
    * **工具列表**：列出当前任务调用的所有工具，Testone工具组件可平滑展示，允许用户对失


## 3.业务落地案例
|商业AIQA需求端到端交付|搜索前端AIQA自动化UI测试|Feed值班新模式|
|-|-|-|
|[附件]|[附件]|[附件]|





# 主题2  有方测试助手—罗希
## 1.整体介绍
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=acd7828ad661430db3296696d442e080&docGuid=8GLtRqUotU8A9D "")
支持以对话交互形式的提测全流程智能测试。在各个环节调用各类测试工具、平台完成各项测试工作。



## 2. 现有能力
### 2.1 测试分析
测试分析会根据提测卡片当中绑定的代码提交，分析出相应的风险和测试意见，其中包含：

* 影响接口：本次代码提交影响的接口，以及接口的Method，param，body, response的定义
* 代码缺陷：可能存在的代码缺陷
* 测试设计：基于接口的一些关键的测试点用例设计
* 自动化代码示例：pytest框架的接口自动化代码示例

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5ca1e4b607ae4530b4122b4b9594dc31&docGuid=8GLtRqUotU8A9D "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4363671205f247f09079dde01f558b1f&docGuid=8GLtRqUotU8A9D "")


### 2.2 iPipe流水线执行
测试智能体可以根据提测需求所绑定的代码提交，推荐相关的ipipe流水线做相应的测试执行。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0e9a02e0cd5e49fe9f1d4c781217c304&docGuid=bKRfxabe06hUFu "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5ac4cbbec62548c08ffcf0719ea215e0&docGuid=bKRfxabe06hUFu "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4cfb2275502742719479b2968f8b35fd&docGuid=bKRfxabe06hUFu "")
### 2.3 webUI用例推荐&执行
测试智能体可以分析需求卡片关联的gitcase用例以及卡片的相关功能描述，从【有方平台】上推荐出相关性较高的自动化测试用例，并且询问用户是否需要执行，用户回复执行，自动触发相关执行。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ef5913073cb14ddc9a3bd6a2cae85717&docGuid=8GLtRqUotU8A9D "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=140f5ccb00404c31807871af43493275&docGuid=2-D0Hx1ufLh_6S "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=eb0f7cd1ca534f59bddc132a5373ede3&docGuid=2-D0Hx1ufLh_6S "")


### 2.4 API接口自动化用例推荐&执行
测试智能体代码分析完成之后会给出相应的测试接口。如果API自动化用例使用的是有方平台，可以在有方平台上的接口用例集合关联上icafe空间标识。在代码分析完成之后，智能体会从关联的测试集合筛选出自动化用例，用户回复执行，自动触发执行。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9b3af45838c34331acda39b454a8f6e3&docGuid=2-D0Hx1ufLh_6S "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f868db9ee184607aec8e4e3031b889c&docGuid=2-D0Hx1ufLh_6S "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=44a3287e08ad4a48942e2dbb30bc1949&docGuid=2-D0Hx1ufLh_6S "")


## 3. 使用入口
|**icafe平台触发**|**如流单聊**|**如流群聊机器人**|
|-|-|-|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3eed6540e3a14ebbbe708edfadce87c2&docGuid=8GLtRqUotU8A9D "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a55dabb81fb94769a75280c87643f585&docGuid=2-D0Hx1ufLh_6S "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6e94b56588954e8bb95feaa185206252&docGuid=2-D0Hx1ufLh_6S "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7aea005c4b2b45bb973a584d69ae610e&docGuid=2-D0Hx1ufLh_6S "")|



## 4.使用场景
##### QA测试
**功能说明：**通过如流机器人LUI对话形式，按需求卡片纬度触发智能体测试，辅助QA进行测试。

**使用流程：**如流搜索【有方测试助手】关注服务号，或者在群聊中添加【有方测试助手】机器人。以对话的形式发起提测，例如：请帮我测试一下 E2ETEST-3891 这个需求卡片。

**场景示例：**

                    1. 搜索并关注服务号             -->           2.发起测试分析

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a730b4b861e945268078ca2921b04769&docGuid=8GLtRqUotU8A9D "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2445def05efe4891b90a733e5350a69b&docGuid=bKRfxabe06hUFu "")
##### 研发提测
**功能说明：**通过icafe数字员工，根据卡片变更状态，RD可在icafe卡片上无感自动触发需求提测分析。

**使用流程：**在icafe需求卡片中的【测试人员】或者【QA负责人】字段，添加【有方测试助手】，当卡片状态扭转为【待测试】的时候，会自动触发提测分析，并且会通过有方测试助手服务号发送消息给提测RD已经抄送消息给其他测试人员。

**场景示例：**

                   1.卡片状态变更                  - -->            2.发送提测分析消息                      -->  3. 抄送提测消息给负责QA

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3eed6540e3a14ebbbe708edfadce87c2&docGuid=8GLtRqUotU8A9D "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3e283d5f47c54401ad5e9c8a1c787a46&docGuid=bKRfxabe06hUFu "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=87ee45dc90c743a0a55a19d214cfde5f&docGuid=8GLtRqUotU8A9D "")




[附件]




# 主题3  语音数字员工阿童木建设及落地—丁广路
## 1 背景
**语音项目流程复杂、协作成本高，**如除工程测试，评测环节包含数据生产标注、质检、ASR 识别、唤醒效果评估等流程，涉及设备操作、脚本准备、日志分析等数十个环节，环节多，执行强度大，任务分布广，需要多方协同。**工具割裂、缺乏统一入口，**和项目测试相关的工具平台（冰夷、易水、撒哈拉、如流、知识库等）缺乏整合，执行链路分散、测试人员需频繁手动切换工具完成一次次任务或项目，效率低、智能性不足。**依赖经验驱动、人员负担重，**测试场景众多、标准不统一，新人难以上手，老员工承担大量重复性任务和知识口传，效率与稳定性易受影响。

**问题思考：**基于AI原生思维，如何实现简单或复杂能力使用的智能化，提升用户体验，减少操作步长，对于一些难于触达用户的长尾功能，是否也可以达到极致的项目快速测试交付体验。是否可以实现一句话/一张图理解、能够记忆、规划、执行并总结的智能化能力，来完成项目测试交付相关的任务，同时随着用户的使用，能越来越聪明。

[流程图]
## 2 产品目标
语音测试数字员工通过用户一段时间的使用记忆训练，逐步掌握每位语音QA的工作方向、经验和任务内容，能够根据员工的 prompt 自动推理并完成数据处理、项目测试、评测、流程控制（如需求、Bug卡片相关操作等）、业务知识问答等一站式语音测试任务，既具备“**测试专家**”的判断能力，又具备“**执行机器人**”的自动化能力。数据处理模块可实现智能化操作，并支持对外输出开放。

* 能像员工一样理解业务知识、测试流程和常见问题，精准答复相关咨询；
* 能像员工一样了解项目节奏，知道如何测试、生成报告及关键环节的确认机制；
* 能像员工一样掌握数据生产与质检方法，并能自动转换为适配不同业务需求的格式；
* 能像员工一样完成语音评测，明确所需步骤，结合业务要求进行评估与分析对比。

## 3 整体架构设计
[流程图]
* **入口层：**支持群聊（机器人）、单聊（公众号）多入口形式探索与唤起阿童木能力。
* **理解层：**支持自然语言、图片、文件等多模态输入的理解与解析，支持历史多轮上下文的引用理解。样例如下：

![图片理解](https://newicafe.baidu.com/rest/v5/attachment/file/stream/22266464 "图片理解")
![语言引用理解](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e23a8f31394b4b38b32345a8c0f7a1a2&docGuid=90PlhlmIMaB826 "语言引用理解")
![文件理解（基于ecloud）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9c403eb5d1ce4a70a0880457f2201782&docGuid=VoAxw-QJ7l_zfm "文件理解（基于ecloud）")
* **记忆：**记忆分级，支持短、中、长期记忆，支持 channel 群记忆，通过群组记忆差异，实现能力的个性化智能适配。
* **能力层：**
    * **规划执行：**
        * **Task任务：**支持定时触发、提问触发、外部接口触发等多种 Task 触发方式。样例如下：



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0adde4beee034e07811763a43c6506cb&docGuid=VoAxw-QJ7l_zfm "")
        * **动态规划：**支持多步骤任务动态规划与中途调整（如取消、新增等）。样例如下：

![任务编排及任务插入样例](https://newicafe.baidu.com/rest/v5/attachment/file/stream/22266563 "任务编排及任务插入样例")
        * **状态通知：**支持异步任务跟踪、失败重试、任务结果状态回传。

* **模型层：**集成大模型与小模型能力，支持自然语言问答、任务规划、语音识别等模型输入解析与调用。
* **Agent层：**将复杂语音测试场景模块化、标准化，支持灵活组合、自动调度与多流程协同，构建可插拔智能能力组件体系。

## **4 重点场景效果**
[流程图]
****

### **场景一：**工程（server/client）测试一站式
* **能力支持：**测试生命周期统一支持提测、提测确认、报告生成、准出核心通用流程能力，可通过iCafe id作为整个流程的输入以及传递，中途支持任务的变更，测试需求新增。
    * **全流程测试：**当前提测自测能力在IOT、度秘业务应用，可通过iCafe id作为整个流程的输入以及传递，提测，自测、提测确认、测试执行、准出等流程，若存在未关闭的 Bug，将无法准出。
    * **功能测试：**此类测试针对复杂重复测试执行场景，包含测试任务编排、报告生成等能力。当前功能编排测试能力在服务端解码器、ASR业务应用**。**部分样例如下：


### **全流程测试**
### **功能测试**


![终端项目一站式测试样例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cd3ced1e84f1401c938611a1d80dcae5&docGuid=5b05nWHeH529W9 "终端项目一站式测试样例")


![服务端编排样例](https://newicafe.baidu.com/rest/v5/attachment/file/stream/23008958 "服务端编排样例")


### **场景二：**声学评测一站式
* **能力支持：**支持产品、场景、数据选择任务、报告生成能力，当前落地语音IOT、车载等项目落地。样例如下：

![评测样例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=770d86b82157475a8b9b1b027647d53b&docGuid=90PlhlmIMaB826 "评测样例")
### **场景三：**数据生产一站式
* **能力支持：**语音数据标注、质检、信噪比检测、音频解交织、切分合并等能力，支持自由组合编排执行，结果报告生成。当前能力落地IOT、RTOS、度秘、tts等业务。部分样例如下：

![数据质检+标注闭环样例](https://newicafe.baidu.com/rest/v5/attachment/file/stream/23009336 "数据质检+标注闭环样例")
### **场景四：**流程控制一站式
* **能力支持：**支持创建卡片（需求、Bug）、修改卡片状态、查询/复制卡片等能力。60%以上的 Bug 均由阿童木自动创建。部分样例如下：

### **Bug创建/修改**
### **Bug状态变更**




![B需求记忆-需求创建Bug](https://newicafe.baidu.com/rest/v5/attachment/file/stream/23008876 "B需求记忆-需求创建Bug")
![Bug创建-内容追加](https://newicafe.baidu.com/rest/v5/attachment/file/stream/23008889 "Bug创建-内容追加")




![Bug状态变更](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ba2339baf5df40d899ec4627193a9988&docGuid=pqULRrpsRNxsJK "Bug状态变更")
## 样例效果：
[附件]
## 5 落地情况
阿童木整体接入原子能力88个，累计支撑项目超过150个，语音数据质检、标注等能力已建设完成并落地326批次，评测完成173次，60%以上的Bug创建及相关操作由“阿童木”自动完成。阿童木使用方面，建设以来累计主动对话执行PV 9686、UV 71，周平均PV 500+，UV 30+。部分场景落地详情数据如下：

|智能体落地|季度|累计（年）|落地业务|
|-|-|-|-|
|数据处理|136|326|ALL|
|server端工程测试|282|391|解码器、ASR|
|client端工程测试|332|564|IOT、车载、移动端|
|灌测（评测）|114|173|IOT、度秘|
|流程控制|627|1097|ALL|
|知识问答|66|129|移动端|
|定时任务|208|247|ALL|
|报告生成|30|62|IOT、移动端、RTOS|

## 6 后续规划
* **需求理解**：结合 iCafe、私域知识与会议纪要，自动完成精准的需求解析，为后续任务规划与用例生成提供高质量输入。
* **用例生成**：引入手工与自动化用例生成机制，丰富数字员工 Agent 的能力，支持按需调用的可插拔智能组件。
* **任务管理**：构建统一任务视图，支持从需求到执行的全流程展示。





# 主题4 【智研师】助力研发项目迭代效率提升—王杰
## 一、背景介绍
随着大模型技术的快速发展，人工智能正在推动一场深刻的变革，如何将人工智能和现有研发基础设施进行融合，向数字员工形态演进，进一步提升研发效率，成为我们的重点之一。BEPQA与EE联合探索建设新Devops数字员工-【智研师】，一期基于如流机器人+如流群+如流工作卡建设工作流程闭环。让业务协作从 “人工串联” 升级为 “智能流转”，实现效率与知识沉淀的双提升 。

## 
# 人类主导
---

AI为工具，检索增强生成

## 
# 人机协同
---

优势互补、实时协作

## 
AI主导

---

自助规划、工具链集成

**角色定位**：

研发项目管理过程中跨角色、跨平台的任务多，且流程长，期望解决项目管理任务的自动协作和流转问题，打造PMO+智能能力，提升研发项目迭代效率

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=262c676aec614ab59ab1117962a139ca&docGuid=7hNBKpCH3RXJlz "")
**可见范围：**

* TPGQA+EE （按照部门划分，如有需要联系wangjie66添加邮件组，白名单，公司的部门组织架构都可以 | [链接](https://work.baidu.com/new-work/static/main/process-start/7514)）

**能力建设：**

* 需求管理：创建卡片、查询卡片、修改卡片等等
* 流程管理：发起提测、确认提测、发起准出、一键准出、智能生成测试报告等等

**触发机制：**

* 基于群聊消息识别用户诉求推荐待发起操作
* 基于单聊(类似服务号)识别用户诉求推荐待发起操作

**未来规划：**

* 覆盖更多场景：批量创建卡片、查询卡片、修改卡片、基于卡片发起提测、执行自动化测试用例、智能生成测试报告
* 支持更多入口：扩展触发机制和入口（接入EE工作台等）
* 持续开放更多能力、赋能更多业务：持续开放原子能力场景，快速支撑业务集成和接入



## 二、方案设计
**设计理念**：

让系统像 “有经验的项目经理”，既能听懂业务需求（意图识别），又能合理分工（机器人协同），还能处理突发状况（异常闭环），依赖大模型+技术手段把 “复杂协作” 变成 “自动化智能流转” 。

**流程设计图：**

[块引用]



**数据演示图：**

[流程图]
## 三、基础能力
基建能力：基于如流会话+机器人+大模型+智能工作卡实现

渠道：如流会话服务号、如流群会话

消息类型：文本消息、卡片消息

### 3.1 用户入口
1. 群聊：项目组人群集中，基于监听如流对话内容，智能识别用户意图，一键操作完成
2. 单聊：个人独立完成，避免打扰其他用户
3. MENU：直接推荐可解决问题，推荐用户对话query；方便用户直观get到数字员工职能
4. 侧边栏：可以承载更多、更复杂的信息；支持自研交互样式和框架

|**单聊**|****|**群聊**|****||
|-|-|-|-|-|
|**Menu**|**发起会话**|**Menu**|**发起会话**|**群聊侧边栏(开发中)**|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1adc10e9ba4143899189b26092b72840&docGuid=TIFpdKg5s59yf3 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=882f8878a4e742368078be0beede4500&docGuid=TIFpdKg5s59yf3 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1daec0ff6e574998907216de504ff45c&docGuid=TIFpdKg5s59yf3 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=923a544972cc4d1fbb714af897751db8&docGuid=TIFpdKg5s59yf3 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c4442c05996946e0816c116ea7cac979&docGuid=TIFpdKg5s59yf3 "")|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d0131f73072f4db693c2f99628380818&docGuid=TIFpdKg5s59yf3 "")||![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=791c51ecef824aec8190fcf8cc0e61ba&docGuid=TIFpdKg5s59yf3 "")|||

### 3.2 重点场景介绍
|**创建卡片**|**发起提测**|**确认提测**|**发起准出**|**一键准出**|
|-|-|-|-|-|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4dd90f1d043f482ba730ccaef0b45b4d&docGuid=ivlQ2xR-cbw5SC "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=27471e3840a64465a7a97b4998ca9290&docGuid=ivlQ2xR-cbw5SC "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=47bcbe9eea4e4cbdbae5daef34ae1f35&docGuid=ivlQ2xR-cbw5SC "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=89ee70afc64c4b08b0c5e3658fc4d95f&docGuid=ivlQ2xR-cbw5SC "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=89ee70afc64c4b08b0c5e3658fc4d95f&docGuid=ivlQ2xR-cbw5SC "")|
|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9e421b2750284f08ab6eaca16795a5c2&docGuid=TIFpdKg5s59yf3 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fc15654b82164b8cac9b019a1e3d2689&docGuid=7hNBKpCH3RXJlz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ac10fca5b4648f0ab9a1bfbb22b4a86&docGuid=7hNBKpCH3RXJlz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=40178c964d28447b8dae2974d727f57d&docGuid=7hNBKpCH3RXJlz "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=05630870d16a453399755a09366345bb&docGuid=7hNBKpCH3RXJlz "")|

**演示视频**：包括卡片新建、提测、提测确认、准出四个场景

[附件]
## 四、业务赋能
**适应场景：**

* 业务无专属机器人
* 业务有专属机器人
* 业务有专属机器人 + 指定任务数据

|**ID**|**接入方式**|**功能模块**|**依赖原子能力**|**业务方提供信息**|**接入成本**|**是否推荐**|
|-|-|-|-|-|-|-|
|**接入方式1**|业务专属数字员工(机器人)[接入方式1：业务专属机器人接入](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/QeoNOBXZ4m/58inP_Etq6XPic?t=mention&mt=doc&dt=doc)|观察决策分析推荐交互执行与反馈|5个原子能力创建卡片发起提测确认提测发起准出一键准出|机器人身份+用户输入触发人  ~~+ 需求卡片  +模块信息 + 提测成员~~触发人 + 需求卡片~~  +模块信息 + 提测成员~~触发人 + 需求卡片 + 模块信息 + 提测成员|申请业务专属机器人开发用户识别模块|推荐|
|**接入方式2**|业务专属数字员工(机器人)+业务自建任务数据[接入方式2：业务自建任务数据](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/QeoNOBXZ4m/_VhjD9jOWV5o1o?t=mention&mt=doc&dt=doc)|观察决策分析推荐交互执行与反馈|5个原子能力创建卡片发起提测确认提测发起准出一键准出| 机器人身份+用户输入|申请业务专属机器人开发用户识别模块开发用户数据分析模块|推荐|
|**接入方式3**|业务专属数字员工(机器人)--不推荐|观察决策分析推荐交互执行与反馈|5个原子能力创建卡片发起提测确认提测发起准出一键准出|机器人身份+用户输入触发人 + 需求卡片 + 模块信息等测试计划信息|申请业务专属机器人开发用户识别模块|不推荐|

**已接入业务：**

|**业务名称**|**知识库**|**安全**|**飞桨**|
|-|-|-|-|
|**机器人名称**|KU质效助手|百灵鸟|阿瓦塔|
|**接入样式**|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6f21ff69d6fd4a25bdd92c22dc3394b6&docGuid=TIFpdKg5s59yf3 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=07f6f26872b7494f83db460544d56703&docGuid=TIFpdKg5s59yf3 "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=31bfb1c969af42f397cfc8163cb70dc0&docGuid=TIFpdKg5s59yf3 "")|

%3CmxGr

## 五、基于Comate插件的工作卡快速开发案例
随着业务迭代升级，工作卡的功能表现实现了从仅支持在 IM 场景进行简单消息推送，到支持基于链接识别的单元化知识、基于智能工作卡的 AI 应用插件，以及基于气泡卡的 AIGC 组件内容渲染等多种形式的跨越。同时，工作卡接入文档与流程也愈发复杂，给开发者带来了较高的接入门槛。

[工作卡ComateX智能工作卡插件模式开发说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/LTv_LxwFwXIbDB?t=mention&mt=doc&dt=doc)

**适用场景：**

1. 机器人回调接口开发
2. 服务号、机器人、新机器人等工作卡发送开发
3. 工作卡回调接口开发

![Comate-插件](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7f9855c79d7e459a844ebcc8be6c7c75&docGuid=7hNBKpCH3RXJlz "Comate-插件")
![Comate-指令列表](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f3f28571c7454a6cb4046dc95c698f4a&docGuid=LTv_LxwFwXIbDB "Comate-指令列表")
![流程讲解](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3529b19366ce4ba9a66688d8ad047a06&docGuid=TIFpdKg5s59yf3 "流程讲解")
![代码示例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=febd5b1ae0f14c5fadbe39dd54c16f6c&docGuid=TIFpdKg5s59yf3 "代码示例")
**演示视频**：包括生成可调试一键发卡demo

[附件]


# 有奖互动
即日起至**7月31日18:00**，在评论区留言，任选下方3个问题回复：

####  1.关于AIQA，聊一聊你所在业务下的实践和工具～
####  2.围绕AIQA，你还有哪些希望讨论的话题？
#### 3.AI辅助编码，你有过哪些神操作想安利给全世界？
我们将挑选5个走心评论，特别送上【BIT蛇年小熊 或 福禄摆件盲盒】～

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e3b5ad11cb2b40b7a55ea20dc3b06d68&docGuid=1W6db4h2eyP7QW "")
### 本期获奖公示
恭喜[@吴玥瑾](https://ku.baidu-int.com?t=mention&mt=contact&id=528ac880-6e88-11f0-9b09-a1808ae0651b)[@v_张景毅](https://ku.baidu-int.com?t=mention&mt=contact&id=8aa8c7d0-6e88-11f0-9b09-a1808ae0651b)[@陈坤](https://ku.baidu-int.com?t=mention&mt=contact&id=99f2f710-6e88-11f0-9b09-a1808ae0651b)[@邢广杰](https://ku.baidu-int.com?t=mention&mt=contact&id=a01e3ff0-6e88-11f0-9b09-a1808ae0651b)[@闫思奇](https://ku.baidu-int.com?t=mention&mt=contact&id=acb44bb0-6e88-11f0-9b09-a1808ae0651b)在本期评论中获奖，

请联系[@王粤佳](https://ku.baidu-int.com?t=mention&mt=contact&id=c2d67e90-6e88-11f0-9b09-a1808ae0651b)领取奖品（非科技园工区伙伴可邮寄）~❤️

# 推荐阅读
[🌟Coding Agent实践：业务与平台的双向奔赴](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/kcH3cHcakHm37t?t=mention&mt=doc&dt=doc)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
