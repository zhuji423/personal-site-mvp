---
title: "一、背景"
description: "“智研师”—智能PMO+的实践与成果"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\“智研师”—智能PMO+的实践与成果.md"
---
“智研师”—智能PMO+的实践与成果

#### 🧑‍🏫 案例作者：[@潘凯](https://ku.baidu-int.com?t=mention&mt=contact&id=f3ce8470-fcea-11f0-8191-25f9b46126e3)
#### 🎬 案例场景：测试
#### 🔧 使用工具：数字员工
#### 📒 案例概要：本文介绍了“智研师”作为智能PMO+的实践与成果，通过融合大模型与流程、数据、知识等多维能力，提升项目管理效能。智研师具备需求管理、流程管理、风险管理等能力，支持开箱即用和积木化赋能，已在多个业务线应用，显著提升效率。文章还探讨了未来智研师的发展方向。
# 一、背景
随着大模型技术迅猛发展，人工智能正驱动一场涵盖技术、组织与工作方式的全局变革。在此背景下，将AI能力深度融入现有DevOps体系，推动各角色向“智能体驱动”（Agentic Work）的工作模式演进，已成为提升整体研发效能的行业共识。

实现这一目标的关键路径，在于构建企业级、场景化的Agentic能力体系，并将其无缝嵌入研发工作流，逐步在关键研发环节中引入AI主导机制，从而全面提升智能研发体验。

当前，大模型技术正由点及面重塑DevOps平台的交互范式与流程，推动Agentic DevOps进入规模化应用的前夜。我们秉持“从小场景切入，以快速验证迭代”的思路，旨在将团队从重复、低价值的“连接性”工作中解放出来，回归思考、创造与深度协作的本源。

本文聚焦于项目管理领域的智能化转型，提出构建智能“增强型PMO”——一个不仅能够催办跟进，更能实质参与项目过程的数字员工。通过融合大模型与流程、数据、知识等多维能力，增强人、事、系统之间的连接与协同，最终实现复杂协作的智能化提效，打通从信息到行动的完整闭环。

# 二、探索思考
项目管理作为企业数字化转型的核心支柱，集成了计划、任务、进度、风险、协作与报告等关键职能，旨在为管理者提供全方位的支持。其核心价值主要体现在：

* **提升效率**：借助CI/CD与自动化流程，减少手动干预与重复劳动，加速任务执行。
* **增强透明度**：通过项目数据与信息共享，确保所有参与者能够及时掌握项目动态。
* **促进团队协作**：基于统一的协作平台，打破地域限制，强化成员间的沟通与协同。
* **辅助科学决策**：通过数据分析和可视化报告，为管理者提供深度洞察，支撑更合理的决策。

然而，随着项目规模与复杂度的持续攀升，传统项目管理模式在高效、精准与协同方面的瓶颈日益凸显：

* **跨角色、跨平台协作流程冗长**：项目需在产品、开发、测试、运维等多角色及多个独立系统间手动流转，导致信息同步滞后，流程阻塞频发
* **流程执行依赖人工，标准难以固化**：关键环节如提测、准出、上线等仍高度依赖人工触发与审批，既影响效率，也导致质量管控风险上升
* **任务状态更新与跟进滞后**：项目进度与风险依赖人工跟踪与汇报为主，管理成本高，且信息更新不及时易引发决策偏差与项目延误
* **数据孤岛阻碍全局视野**：各平台数据独立，缺乏有效拉通与聚合，管理者难以实时获取跨系统全景视图，制约资源协调与风险预判

随着并行项目与团队数量的增长，项目管理者正陷入“人肉调度”的困境，大量时间被消耗在催进度、收报告、对数据、排会议等事务性工作中。战略思考与高价值活动，如产能分析、流程改进与战略对齐，因此被严重挤压，导致组织级项目管理成熟度停滞。推动项目管理的智能化转型，不仅是一项趋势性选择，更是企业提升效能实现可持续发展的关键路径。



**聚焦项目管理任务中跨角色、跨平台任务的自动协作和流转问题，基于数字员工探索****项目管理Agentic变革，****我们的基本原则如下：**

* **交互形态从「指哪打哪」到「心有灵犀」：**
    * 从**被动执行**迈向**主动理解：**传统系统依赖用户逐步操作，而数字员工以“意图识别”为核心。用户只需提出目标（如“帮我发起提测”），系统即可自动理解、决策并执行全流程，实现复杂任务的“一语即达”。这不仅提升了工具能力，更重塑了人机协作模式
    * **简洁直观的交互界面**：面对流程复杂、意图模糊、信息冲突等现实挑战，友好的UI是AI能力落地的关键一环。数字员工应承担起理解、协调与纠偏的职责，通过结构化呈现结果数据，降低用户认知负荷，提升操作效率，让AI不仅具备能力，更贴近业务、善于协同——这是智能化真正赋能业务的重要跨越
    * **过程透明，反馈可见**：智能不应是黑盒，而应是可对话、可理解的伙伴。通过结构化数据展示与决策逻辑的透明化，用户可以清晰了解AI的“思考过程”与判断依据，并能便捷地对执行偏差进行干预与修正

* **双模驱动，灵活赋能**：设计上兼顾“开箱即用”的便捷性与“模块化扩展”的灵活性。团队不仅能立即使用标准化功能，还可根据实际场景，自由接入与组合各类原子化能力，从而高效、平滑地完成项目管理智能化转型。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=52e48740232b4adc8115eeb0550be8c0&docGuid=Sgw9Zqcjhud2vd "")


# 三、关键方案
**基本思想**：以LLM为智能中枢，结合如流机器人与现有DevOps基础设施开放能力，融合流程、数据与知识等多维能力，实现跨角色、跨平台的项目管理任务的智能协作与自动流转，从而增强人、事、系统之间的连接与融合，推动信息与行动的高效闭环。

**交互升级：从「指哪打哪」到「心有灵犀」，**为实现从被动响应到主动理解的交互转变，构建三层智能处理机制：

* **感知与规划**：如流机器人分析用户会话，由规划子智能体（Plan subAgent）主动解析用户意图并决策任务类型，并借助结构化GUI交互界面，辅助用户快速澄清与确认任务目标
* **编排与委派**：基于集成的流程引擎、数据资产与记忆信息，将已识别的任务类型精准委派至具备相应能力的任务智能体（Task Agent）
* **执行与反馈**：机器人通过调用DevOps开放能力获取实时数据，结合上下文记忆与底层服务进行深度交互，并将执行结果清晰、结构化地反馈给用户

**能力构建：双模驱动，灵活赋能，**为满足不同团队与场景的需求，设计两种能力供给模式：

* **通用能力：**以『智研师』为核心，提供覆盖项目管理核心场景的「开箱即用」解决方案。同时，其所有能力均以API、MCP等标准化方式原子化输出，可供各业务线的数字员工便捷接入，快速实现项目管理智能化
* **业务自定义能力：**基于MCP平台，支持业务方自定义接入其特有的场景与能力，并可灵活通过单聊、群聊、气泡等多种渠道触发，助力各团队加速其个性化流程的智能化演进

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16bc5598ff62443cb9f527dd29b776aa&docGuid=AZy4QLLR5KtKU2 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fa7dd09b3cf94f47a76e59788e74a4ba&docGuid=2TItZnx2a7yF7- "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=542775e5e4124d14a976c78031d5ea69&docGuid=2TItZnx2a7yF7- "")
# 四、实践成果-从「开箱即用」到「积木化赋能」
**实践效果**：使用「智研师」能力的业务线包括：SEP-SWS/BCDP/HCM/工作流/知识库、SEP-安全、Aistudio、视觉、MEG健康等，覆盖330+群聊，年化预计节省 200+人天

## 4.1 智研师-开箱即用
### 4.1.1、能力概述
聚焦项目管理任务中跨角色、跨平台任务的自动协作和流转问题，**『**智研师』当前支持的能力如下:

**场景覆盖：**

* **需求管理：**支持需求卡片的智能创建、修改、查询等；并支持基于预设规则智能创建卡片，比如基于群级别的值班表自动分配卡片负责人等
* **流程管理：**支持提测、确认提测、准出、确认准出、一键准出等，并支持流程自动编排：基于业务属性自主识别并匹配项目流程类型，包括非免测流程L1、自动提测流程L2、自动提测 & 发起准出流程L3、全自动流程L4四大场景，进一步提升流程流转效率
* **风险管理**：支持项目迭代看板、智能创建待办等；项目迭代看板包括项目进度看板、状态分布等，支持群内自动识别 『艾特人+截止时间+事项』任务智能创建待办等

**触发渠道**：

* 基于**如流群聊、单聊**消息识别用户潜在任务并推荐操作
* 基于**如流气泡MENU、如流吊顶卡和侧边栏**触发操作
* 基于Comate Stack**数字员工工作台**操作

![智研师名片](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=75311c2d5edd4e7985d92947b612091f&docGuid=Sgw9Zqcjhud2vd "智研师名片")
![单聊会话](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=44f69e09f20246128d3a407be3655ef9&docGuid=Sgw9Zqcjhud2vd "单聊会话")
![群里会话](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=af1c812796f94fd9a41ff9d3a1460908&docGuid=Sgw9Zqcjhud2vd "群里会话")
![气泡触发](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=79aadc4b714d42f4ba5ba19fa1489a3b&docGuid=Sgw9Zqcjhud2vd "气泡触发")
![吊顶卡&侧边栏](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=300f7906515146b5936e8abb30b551c9&docGuid=Sgw9Zqcjhud2vd "吊顶卡&侧边栏")
### **4.1.2、场景使用示例**
#### 4.1.2.1、需求管理
**基于纯文字、文字+图片**消息类型智能管理iCafe卡片，下面以Chat模式创建iCafe卡片为例。

|**创建卡片-Step-1**|**创建卡片-Step-2**|**创建卡片-Step-3**|
|-|-|-|
|**自动识别群消息中  “创建卡片”的诉求**默认显示5个字段信息，并智能填充信息，可自行修改 ![创建纯文本卡片](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8caae9a195d94a8c87e3871a7174608d&docGuid=Sgw9Zqcjhud2vd "创建纯文本卡片")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a23c58ce76b3415caeec73bdedc09663&docGuid=Sgw9Zqcjhud2vd "")|点击【展开】按钮后，显示卡片全部待填写信息填写内容后，点击创建|创建成功后，显示创建成功的卡片，点击可跳转到卡片链接，卡片内容包含群聊天记录点击复制，可复制卡片链接  [[BPIT-SWS-1084] 数据迁移总量错误，创建bug](https://console.cloud.baidu-int.com/devops/icafe/issue/BPIT-SWS-1084/show?t=mention&mt=doc&dt=sdk)|
|![创建卡片中带有图片](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ee27c411b114fd086a1c24371a8f9b9&docGuid=Sgw9Zqcjhud2vd "创建卡片中带有图片")|![未展开：默认展示关键参数](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=816820e12f51473580095fd0e2b67cf3&docGuid=Sgw9Zqcjhud2vd "未展开：默认展示关键参数")![展开：提示卡片必填项](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16e0ef034ea34e488c75db46debe4d72&docGuid=Sgw9Zqcjhud2vd "展开：提示卡片必填项")|![创建成功，显示已创建卡片链接](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=53d93d82d0d24e6cb1ce7755cbc93a3e&docGuid=Sgw9Zqcjhud2vd "创建成功，显示已创建卡片链接")![创建卡片详情-纯文本](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=67a3e638c71d4a9cb1d57ebec925c1c0&docGuid=ao0Lm62pM-VPir "创建卡片详情-纯文本")![创建卡片详情-文本+图片](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=80dc11fa914e471d91f6f5dc866a3f19&docGuid=ao0Lm62pM-VPir "创建卡片详情-文本+图片")|

#### 4.1.2.1、流程管理
支持提测、确认提测、准出、确认准出、一键准出等，并支持流程自动编排，下面以群聊Chat模式为例。

**群聊-发起提测&确认提测**

**群聊-发起准出&确认准出**

**操作截图**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c70f4129b98c4b8dacda272e39833657&docGuid=vO23KDip1kSXwv "")


**步骤描述**

**Step-1**

自动识别群消息中  “发起提测”的任务或点击气泡Menu

**Step-2**

推荐用户待提测的卡片

勾选本次要提测的story卡片，自动推荐模块列表、提测人员

**Step-3**

填写提测标题、提测人员、提测说明，点击【发起提测】按钮

**Step-4**

提测成功，卡片状态自动流转为 待测试

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5c12c6b82aaa419884911df0d238d61d&docGuid=ao0Lm62pM-VPir "")
**Step-5**

测试人员确认提测，卡片状态自动流转为 测试中

**操作截图**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=eeeddb19a6b84a26ad17c93f9a57f5dd&docGuid=vO23KDip1kSXwv "")
**步骤描述**

**Step-1**

自动识别群消息中包含  “准出”的任务或点击气泡Menu

**Step-2**

推荐准出任务，用户可勾选提测计划、选择提测人员。准出自动生成测试报告建设中

推荐策略：

* 当前用户近1个月，所有待准出的测试计划，自动推荐准出人员，可修改
* 勾选提测计划后，会显示包含的需求卡片和模块信息

**Step-3**

点击【发起准出】按钮，完成发起准出

**Step-4**

准出人员收到人人卡，点击【发起准出确认】按钮，完成准出确认

****

**免测需求可走**【一键准出 】，即 点击【一键准出】后，包含上述Step3和step4

#### 4.1.2.3、风险管理
支持项目迭代看板、智能创建待办等，下面以群聊Chat模式为例

**群聊-项目迭代看板**

**群聊-智能创建待办**

**操作截图**

![创建项目](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7aa3487c066848a387b5484ccbe2152f&docGuid=mETAwgt99VPQ9P "创建项目")
![项目迭代看板](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d6c35358726f4f149f31c4a2cc170e71&docGuid=Sgw9Zqcjhud2vd "项目迭代看板")


**步骤描述**

**Step-1**

项目迭代吊顶卡点击[ + ]新建按钮，触发打开群聊侧边栏

**Step-2**

新建项目：

设置详情：项目名称、关联相关需求、BUG等卡片

关联卡片：按条件查询、iCafe链接查询(最多1000张)

**Step-3**

基于关联卡片自动绘制项目迭代看板

群成员可以基于吊顶卡查看项目列表，点击项目名称可以基于侧边栏展示项目详情及时感知项目进度和风险

****



**操作截图**

![创建待办](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01a727ba32bf49988a7fc6e2bdcc6040&docGuid=Sgw9Zqcjhud2vd "创建待办")


**步骤描述**

**Step-1**

监听群内会话内容

**Step-2**

识别命中：时间、任务、todo事项触发创建待办

**Step-3**

用户确认待办内容，点击确认即可完成待办



## 4.2 智研师-积木化赋能
**积木化赋能能力体现在两个层面：**

|**类型**|**适用场景**|
|-|-|
|**原子能力赋能**|业务想使用自己的数字员工/Agent，不想直接使用『智研师』数字员工|
|**业务自定义接入特性能力**|业务想使用『智研师』数字员工，但是除通用能力外，想接入业务自己自定义能力|

**具体介绍如下：**

* **原子能力赋能**：需求管理、流程管理等提供原子能力，业务特性数字员工最快可分钟级快速接入，赋能的数字员工包括：『阿瓦塔』『百灵鸟』『MEG-小智』『Ku质效助手』『HCM质量管理机器人』等。

**接入方案**

**适用场景：**业务想使用特性数字员工/Agent，不想直接使用『智研师』

**接入方式**：

* 方式1：复用编排与委派能力，包括任务推荐组装、执行反馈
* 方式2：复用任务数据组装和交互、执行反馈
* 方式3：仅复用任务执行（不推荐）

**接入手册**：[智研师-业务接入手册](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/AtKECXn-wv/5hAIZWVfHRU8pG?t=mention&mt=doc&dt=doc)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2dd92a7d36c94c47a348a27e9dc8c7ee&docGuid=Sgw9Zqcjhud2vd "")


**接入案例**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16cdecf1ee8143278b288c214f4b0499&docGuid=May1cJ20IrqaYd "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c37006f3db6f434da16bb8a9a2575db3&docGuid=May1cJ20IrqaYd "")
* **业务自定义接入特性能力**：支持业务以MCP工具中心为基础，单聊、群聊场景可自助接入业务特性能力。

**接入方案**

**适用场景：**业务想使用『智研师』，但是除通用能力外，想接入业务自己自定义能力

**接入步骤**：

* Step-1：业务开发特性能力，并在MCP市场**注册**MCP Server
* Step-2：「智研师」所在群聊，打开MCP**配置**侧边栏，添加对应的MCP Server
* Step-3：用户在群聊**发起任务**，命中调用对应的MCP能力

![业务特性能力接入方案](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0c6f1f99ef7f431fb1558da0c596df4a&docGuid=-f4Y2PfDUkc1HU "业务特性能力接入方案")
**接入案例**

![业务特性能力接入案例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6526d4b7fd5a4de0a965c6aa6c2117a8&docGuid=-f4Y2PfDUkc1HU "业务特性能力接入案例")


# 五、总结
数字员工不只是人类的“工具”，而是团队中一个可以“看得见、能干预、能推动”的智能成员。它提前介入问题，减少人为疏漏，让业务运转更加高效；它主动完成重复性、琐碎却关键的操作，让项目成员的专业力量得以专注于更具创造性和决策性的工作。本文聚焦于项目管理领域的智能化转型，介绍了构建智能“增强型PMO”-『智研师』的实践方案和实践成果。未来，随着技术的不断进步和应用场景的拓宽，项目管理的智能化水平将进一步提升，『智研师』也会持续聚焦项目管理领域，不断探索和创新，以AI重塑项目管理的未来之路，助力推动各角色向“智能体驱动”（Agentic Work）的工作模式演进。





# 附录：开启您的智能PMO+之旅
[智研师-用户使用手册](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/AtKECXn-wv/ao0Lm62pM-VPir?t=mention&mt=doc&dt=doc)

[智研师-业务接入手册](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/AtKECXn-wv/5hAIZWVfHRU8pG?t=mention&mt=doc&dt=doc)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
