---
title: "🎨 背景"
description: "Figma Make+Spec驱动的AI提效路径"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Figma Make+Spec驱动的AI提效路径.md"
---
Figma Make+Spec驱动的AI提效路径

#### 🧑‍🏫 案例作者：[@骆奕伶](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：全流程
#### 🔧 使用工具：Cursor、Figma
#### 📒 案例概要：成熟项目往往伴随历史包袱、性能与安全约束，以及严格的工程规范，这使得单纯依赖 prompt 驱动的即时 coding 难以直接落地到真实业务中。
本文就详细介绍了国际化团队如何将复杂项目实现PM—UE—RD的协同，让每个角色都真实的使用AI来进行串联式协作，实现更快更高效的流程化协作模式，同时我们自研了可视化的流程Spec Flow插件帮助大家从繁琐的终端指令中解脱出来
[规范驱动的AI自动化Coding全流程提效](https://ku.baidu-int.com/d/UCNVCF0ICymWoZ?t=mention&mt=doc&dt=doc)

# 🎨 背景
**在使用AI进行需求协同的探索过程中，我们遇到的问题：**

* **PM: **在需求模糊前期，重点在于方案探索和demo呈现，需要避免陷入bug修改和页面还原，专注于产品功能设计
* **UE: **使用Cursor+原代码交付的方式减少了验收成本，但也意味着同一个功能设计需要做出安卓&iOS需要两套代码，增加了成倍的代码工作，设计变成了一个“伪前端”，工作并没有消失
* **RD:**AI Coding显著提升了开发效率，但是通过prompt驱动的代码生成方式仍然无法快速产出符合预期和高质量的代码，AI的“随意发挥”也成了阻碍研发效率的卡点，研发仍需要花费大量时间去调通流程、补足功能点、修改bug......

# 🤔 为什么选择make
——决策旅程

**优势 **

![一次复杂键盘还原](/personal-site-mvp/img/doc-placeholder.svg "一次复杂键盘还原")
还原速度快难度低，接入常用模型claude和gemini3，pm和设计可以共用一套标准，在demo阶段快速补全想法

**问题 **

![原生代码](/personal-site-mvp/img/doc-placeholder.svg "原生代码")
html不等于原生代码格式，一开始我们认为仅适合用于UE和PM之间的想法沟通

**解决 **

![Openspec](/personal-site-mvp/img/doc-placeholder.svg "Openspec")
openspec指导AI进行代码生成能实现组织结构化协作。make产物=交互语义的翻译器，PM&UE&RD的工作流程实现了串联

![PM&UE专注于方案构建，提供标准化物料包，RD作为流程中的ownership角色，把控个角色的输出符合结构化标准](/personal-site-mvp/img/doc-placeholder.svg "PM&UE专注于方案构建，提供标准化物料包，RD作为流程中的ownership角色，把控个角色的输出符合结构化标准")


# ⬆️ 流程&效率提升点
**PM** -主要减少需求输出阶段反复修改沟通成本，使用figma make实现多种交互具像化快速决策，较原来提效30%。

**UE** -同一需求耗时测试： make 0.5-1小时  安卓 5小时 iOS2天，极大减少coding时间

**RD** -使用Cursor开发，相较于原来多轮AI对话的开发方式提效20%左右

# 🌍 实践路径
**make的使用非常简单，可以自行尝试或看简单使用指南：**

[Figma Make使用指南](https://ku.baidu-int.com/d/Ua_qDA6084PVqa?t=mention&mt=doc&dt=doc)；[Figma Make使用攻略](https://ku.baidu-int.com/d/qxMEALp5BxuW0U?t=mention&mt=doc&dt=doc)**建贞❤️名华**

## 1.原型生成&PRD构建
PM：[@何朝阳](https://ku.baidu-int.com?t=mention&mt=contact&id=7be0eab0-d801-11f0-9770-eb33cdfd6200)

### 发挥Figma make优势，将模糊需求具像化。
对于 PM 而言，过去主要依赖需求文档 + 简单原型图来对齐，而现在通过Figma Make快速生成可交互Demo，把想法直接落到交互和流程上，用“看得见的东西”对齐认知。

# **尝试多****种交互：**
* **简单交互：**基础框架构思好后让AI生成原型图喂给Figma make。也可以动手画简单的原型图给到Figma make。
* **复杂交互：**涉及多层级页面的交互逻辑，通常在prompt中给每个页面命名，注意阅读回复中提到的页面名称，善于使用AI能记住的名称输出的效果更稳定。一个页面完成后再设计下一个页面。通常是布局ok后再优化细节（比如颜色、选中态，预览图替换，loading特效等等）。多轮对话也可以帮助pm发现遗漏的逻辑，逐步完善。
* **竞品交互搬运**：直接给到竞品的截图，prompt明确指令参考部分，其余部分不变。

![AI生成原型图](/personal-site-mvp/img/doc-placeholder.svg "AI生成原型图")
![Figma make效果](/personal-site-mvp/img/doc-placeholder.svg "Figma make效果")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![全屏](/personal-site-mvp/img/doc-placeholder.svg "全屏")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![半屏](/personal-site-mvp/img/doc-placeholder.svg "半屏")
![竞品交互搬运](/personal-site-mvp/img/doc-placeholder.svg "竞品交互搬运")
[附件]
[附件]
# **学习AI能理解的方式写Prompt**
* **命名固定**：给每个页面/功能点命名；使用thinking/回复中的名称下指令；
* **运用“md式”表达**：交付中多次强调要markdown格式，观察发现md格式具有结构化特征，框架清晰，布局整齐，突出关键点。因此pm也可以学习这种方式编辑prompt。
* **用「角色 + 目标 + 约束」三件套**，稳定出结果。尤其是约束哪个部分做修改，哪个部分不变。eg如下：
    * *你是一个【XX 产品/设计角色】*
    * *目标是【解决什么问题 / 验证什么假设】*
    * *约束条件包括【平台 / 用户 / 使用场景 / 不要什么】*




![](/personal-site-mvp/img/doc-placeholder.svg "")


### 如何输出规范化的产物给到生产线？
完成Demo确认需求后基本完成一大半，给到符合规范的需求产物，才能使Demo优势最大化，简单来说让RD用得上。

# **完整PRD=交互PRD+补充****逻辑**
* 基于Demo总结出交互PRD。
* 交互涵盖不到的实现逻辑，例如弹窗、服务端侧、多语言文案、埋点等等。将这些补充逻辑完善到PRD中。
* 将交互PRD和补充逻辑做个汇总，直接在Figma make汇总也可使用Cursor。
    * 简单的文字逻辑补充直接在Figma make中进行即可。
    * 含有附件、表格、链接等信息更推荐使用Cursor。
    * 期间发生的改动点可直接对话修改。




![交互PRD](/personal-site-mvp/img/doc-placeholder.svg "交互PRD")
![整合](/personal-site-mvp/img/doc-placeholder.svg "整合")
# **擅用Cursor实现规范化**
* PRD交付依然是markdown格式，转一份常规格式作为留底。
* 把RD整理的[Cursor标准化需求文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/iki-aVkbF_/tseQDafprx/aYAFEkhZpGgu3Y?t=mention&mt=doc&dt=doc)链接丢给Cursor学习，并通过prompt要求输出参照标准的PRD。
* Cursor去除多余逻辑：PRD时常会参杂多余的逻辑，例如用户反馈页面优化需求demo中为了还原拉键的状态将键盘主界面的逻辑涵盖进去。
* 打包产物时注意区分交付对象，例如同一个需求要在多个渠道上线（IOS，主线GP，预装）会有细微的差别。因此Cursor生成PRD注意prompt有所倾向，打包命名注意区分。
* 常规化的输出交给Cursor：拆解出PRD常规化的内容，比如埋点要规范，多语言文案，都可以按照固定格式形成Rules。甚至流程图都可以交给Cursor实现。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![多语言文案翻译](/personal-site-mvp/img/doc-placeholder.svg "多语言文案翻译")
![流程图](/personal-site-mvp/img/doc-placeholder.svg "流程图")
**AI提效流程实践心得**

1. Figma make多轮对话中帮助pm发现遗漏的逻辑，以往写需求文档时常存在模糊的点得以改善。
2. 多种AI工具交替使用，把自己想象成Cursor选择趁手的工具。
3. 一定要多尝试，多跟UE、RD同学交流，不懂就问，遇到问题/bug甚至可以截图求助Cursor。

## 2.还原&交付
UE：[@韩建贞](https://ku.baidu-int.com?t=mention&mt=contact&id=a63b0ca0-d801-11f0-9770-eb33cdfd6200)

# **结构化设计稿**
视觉稿作为视觉标准，这一步让Make&figma MCP能够准确识别，减少对话轮次，注意在组件名称编写上与rd协同能够更加规范化。

文档：[设计稿交付Cursor前注意事项](https://ku.baidu-int.com/d/LTkildj6hau7tx?t=mention&mt=doc&dt=doc)

![去年已经有规范](/personal-site-mvp/img/doc-placeholder.svg "去年已经有规范")
# **Rules 构建**
与cursor一样，Make同样能够进行正常的rules编写；

* **产品定位** —— 这是一个什么产品
* **交互布局** —— 制定半屏特征，区域滚动的规则
* **常用描述** —— 特殊用语&组件指代
* **检查清单** —— AI工作指南，自动把关质量，防止遗漏
* **使用提醒** —— 首轮对话&长时间对话提醒避免遗忘



在需求前构建rules能够减少bug以及对话轮次

![](/personal-site-mvp/img/doc-placeholder.svg "")
![按照项目特性和自身习惯，结合coding中的问题不断完善](/personal-site-mvp/img/doc-placeholder.svg "按照项目特性和自身习惯，结合coding中的问题不断完善")


# **设计规范**
make可以直接将已有的规范进行记录，并支持实时纠正更新

* **组件添加 **—— 组件库会被编译为Globals&Guideline两个文档
* **Globals（全局变量）** —— 定义具体的颜色、字体、尺寸数值
* **Guideline（指南）** —— 定义何时&如何使用这些规则



在需求前可以先把规范添加上并手动调整，合理的设计规范能够在coding中直接生成合适的UI效果，**后续可以尝试先在make中生成设计稿，再转为figma进行留档**

![规范可发布到make中直接使用，选择后不可更改](/personal-site-mvp/img/doc-placeholder.svg "规范可发布到make中直接使用，选择后不可更改")
![无设计稿直出测试，布局规范未完成所以比较混乱，但是颜色已经是按照规范进行](/personal-site-mvp/img/doc-placeholder.svg "无设计稿直出测试，布局规范未完成所以比较混乱，但是颜色已经是按照规范进行")
# **版本管理**
便于在一个大的项目中区分不同需求，避免错误修改，记录变更

* Changlog —— 记录版本功能和变更
* Versions —— 版本概览，作为Changlog的快速导航
* Rules —— 增加版本管理和提取指南模块

![版本修改记录](/personal-site-mvp/img/doc-placeholder.svg "版本修改记录")
# **Demo完善与发布**
不需要完全标准化还原，make代码作为交互语言翻译器，设计可以在pm的make中继续完善，pm也可以在设计构建的框架中进行demo实现

# 0**1 **
##### 完善Demo
就PM的 demo讨论敲定最终交互方案，通过多轮次的对话把交互和视觉完善。

**快速调整：**指定区域快捷编辑样式/动效/布局

[附件]
![](/personal-site-mvp/img/doc-placeholder.svg "")
![pm 初版 demo⬇️](/personal-site-mvp/img/doc-placeholder.svg "pm 初版 demo⬇️")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![完善 demo](/personal-site-mvp/img/doc-placeholder.svg "完善 demo")
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 02** **
##### Make to design
make 能 1:1 转换为设计稿，微调归档即可



[附件]
![设计稿 vs make转设计稿](/personal-site-mvp/img/doc-placeholder.svg "设计稿 vs make转设计稿")
![make设计稿 有图层带自动布局](/personal-site-mvp/img/doc-placeholder.svg "make设计稿 有图层带自动布局")


0**3**

##### 输出&发布
切换 code 模式下载 ，导出总物料包（代码、切图等）；

点击publish可以进行发布，复制url，用手机打开后就是一个可交互的demo，实现体验的前置

![输出方式](/personal-site-mvp/img/doc-placeholder.svg "输出方式")
![体验录屏](/personal-site-mvp/img/doc-placeholder.svg "体验录屏")
![发布URL](/personal-site-mvp/img/doc-placeholder.svg "发布URL")






















### 最终物料包
【figma-设计标准】【make文件包-交互标准】【动态说明.md】【版本说明.md】【差异说明,md】

![切图](/personal-site-mvp/img/doc-placeholder.svg "切图")
![PRD](/personal-site-mvp/img/doc-placeholder.svg "PRD")
![make 总包](/personal-site-mvp/img/doc-placeholder.svg "make 总包")
![make 总包内容](/personal-site-mvp/img/doc-placeholder.svg "make 总包内容")


[附件]


### 其他用途
# 🌟 动效设计 🌟
0**1  **

**交互动效：**使用Figma Make串联入口页→功能页→结果页，实现按钮呼吸引导、页面切换动效等；

![对话添加](/personal-site-mvp/img/doc-placeholder.svg "对话添加")
![send 按钮呼吸效果](/personal-site-mvp/img/doc-placeholder.svg "send 按钮呼吸效果")
![页面交互](/personal-site-mvp/img/doc-placeholder.svg "页面交互")
02** **

**粒子特效：**用自然语言的形式向 AI描述可以不用太细节，先创建大致的框架观察与预期的效果方向是否相符

![初版构想](/personal-site-mvp/img/doc-placeholder.svg "初版构想")
![初步效果](/personal-site-mvp/img/doc-placeholder.svg "初步效果")
![细化修改](/personal-site-mvp/img/doc-placeholder.svg "细化修改")
# 🌟 小工具制作 🌟
01

**键盘皮肤生成平台：** 可快速根据描述生成键盘皮肤，辅助创意发散/批量处理皮肤工作 。



[附件]
[@刘镇](https://ku.baidu-int.com?t=mention&mt=contact&id=3c21c6c0-daf3-11f0-aff9-5db00c5cad20)

02

**彩蛋banner生成、审核工具：**解决彩蛋具有时效性 banner需快速设计的痛点，辅助设计师批量设计、审核等工作提效 。

[附件]
[@v_钟雅茜](https://ku.baidu-int.com?t=mention&mt=contact&id=fefb8550-daf3-11f0-aff9-5db00c5cad20)

03

**genmoji表情批量生成平台：**批量 genmoji生成、筛选、调色、抠图、一键打包，优化了单个表情生成，人工再介入的工作流程。

[附件]
[@v_孙庆琪](https://ku.baidu-int.com?t=mention&mt=contact&id=d7a613b0-dafa-11f0-aff9-5db00c5cad20)

## 3.Cursor AI Agent + Spec开发提效
RD[@梁智开](https://ku.baidu-int.com?t=mention&mt=contact&id=988c64f0-d801-11f0-9770-eb33cdfd6200)

## **在开发前就明确"做什么"、"怎么做"，具体的实施过程交给AI。**
## 1. 什么是 Spec
**Spec** 是一套规范驱动的开发流程（Specification Driven Development：规格驱动开发），它将需求、设计、实现和验收标准统一管理，确保：

* ✅ **需求对齐**：PM、UE、研发对需求理解一致
* ✅ **验收明确**：每个功能都有清晰的验收标准
* ✅ **变更可追溯**：所有变更都有记录，可Review
* ✅ **AI 可执行**：生成的规范可以直接指导 AI 生成代码

## 2. 为什么需要 Spec
**传统流程的问题**：需求理解不一致、验收标准模糊、变更难追溯

![](/personal-site-mvp/img/doc-placeholder.svg "")
```
flowchart LR
    subgraph 传统流程
        A[PM 写 PRD] --> B[UE 出设计稿]
        B --> C[研发看文档开发]
        C --> D[测试验收]
    end
    
    A -.-> A1[文档分散]
    B -.-> B1[设计稿分散]
    C -.-> C1[理解偏差]
    D -.-> D1[验收标准不明确]
    
    style A1 fill:#ffcccc
    style B1 fill:#ffcccc
    style C1 fill:#ffcccc
    style D1 fill:#ffcccc
```
**基于Spec的开发流程优势**：需求对齐、验收明确、变更可追溯、AI 可执行

```
flowchart LR
    subgraph Spec流程
        A[创建 Change Proposal] --> B[多方 Review]
        B --> C[审批通过]
        C --> D[AI 实现]
        D --> E[验证归档]
    end
    
    A -.-> A1[统一文档格式<br/>proposal.md<br/>design.md<br/>tasks.md<br/>spec.md]
    B -.-> B1[PM/UE/研发<br/>共同审批]
    C -.-> C1[多方检查<br/>才能开发]
    D -.-> D1[自动生成代码]
    E -.-> E1[验收]
    
    style A1 fill:#ccffcc
    style B1 fill:#ccffcc
    style C1 fill:#ccffcc
    style D1 fill:#ccffcc
    style E1 fill:#ccffcc
```
**2.1 **代码层面：

* 单个功能需求的主流程能做到开箱即用，通过一轮对话即可产出可跑通主流程的代码
* 所有代码都严格遵循规格说明，消除理解偏差
* 不同开发者实现相同规格，代码风格保持一致
* 业务层面：
    * 产品、开发、测试对需求的理解高度一致，减少了需求理解偏差导致的返工


**2.2 **可回溯的文档记录：

* 任何变更都先更新Spec规格，再通过Cursor等AI Coding工具进行实施
* 通过阅读规格说明就能快速理解功能
* 变更影响分析：
    * 修改规格时，清晰知道影响哪些代码模块
    * 依赖关系在规格中明确定义

* 代码可读性：
    * 代码结构清晰，层次分明，在定义规格时就明确代码的文件结构

* 业务漏斗打点逻辑定义完整

**2.3 团队协作效率提升**

* 跨团队协作时，**规格成为统一语言**，PM、RD、UE、QA各业务环节的同学都可以快速对齐需求逻辑和技术方案

## 3. Spec三阶段工作流
```
flowchart LR
    subgraph Stage1[阶段 1: 创建提案]
        A1[准备物料包]
        A2[AI 生成 OpenSpec]
        A3[PM/UE/研发 Review]
        A4[发起审批]
    end
    
    subgraph Stage2[阶段 2: 实施变更]
        B1[生成实施 Prompt]
        B2[AI 实现代码]
        B3[标记任务完成]
    end
    
    subgraph Stage3[阶段 3: 归档变更]
        C1[验证 Scenario]
        C2[执行归档]
        C3[更新 specs]
    end
    
    Stage1 -->|审批通过| Stage2
    Stage2 -->|任务完成| Stage3
    
    style Stage1 fill:#e6f3ff
    style Stage2 fill:#fff2e6
    style Stage3 fill:#e6ffe6
```
### 阶段 1: 创建变更提案
#### 步骤 1.1: 准备物料包
基于[前置流程效率提升](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/zSOwyRj1a8/wlwgjWCT8gvvpn?t=mention&mt=doc&dt=doc)规范，PM/UE 准备产品需求物料包，结构如下：

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 步骤 1.2: 在 Cursor 中让 AI 生成 OpenSpec规格文档
在 Cursor IDE 中输入简单的自然语言 Prompt：

```
@产品需求物料包——用户反馈 我想添加用户反馈功能，请创建 OpenSpec 提案。
```
AI Agent 会自动生成：

* `proposal.md` - 需求提案（从需求背景提取）
* `design.md` - 技术设计（根据项目架构生成）
* `tasks.md` - 任务清单（从页面/交互拆分）
* `specs/*/spec.md` - 验收标准（从交互逻辑生成 Scenarios）

#### 步骤 1.3: PM/UE/研发 Review 和完善
**基于AI+Openspec生成的文档，仍需要人工去审查和完善。**

**Review 检查清单**：

|文件|Review 重点|负责人|
|-|-|-|
|`proposal.md`|需求背景是否准确、变更内容是否完整|PM|
|`proposal.md`|Figma 链接是否正确、UI 要求是否明确|UE|
|`design.md`|技术方案是否合理、架构是否符合规范|研发|
|`tasks.md`|任务拆分是否合理、工作量评估|研发|
|`spec.md`|验收场景是否完整、覆盖所有交互|PM + 研发|

#### 步骤 1.4: 发起 Review
1. Spec文档关联各方审批人，发起 Review（文档对齐，会议沟通）
2. 收集审批意见
3. 更新审批状态为 `✅ Approved`

### 阶段 2: 实施变更
#### 步骤 2.1: 生成实施 Prompt
我们在项目中实现了可根据Spec规格文档内容生成coding prompt的脚本命令，通过脚本命令即可快速生成Cursor code prompt。

#### 步骤 2.2: 在 Cursor 中实施
**使用Plan模式效果更佳！**

在 Cursor IDE 中输入：

```
@openspec/changes/add-user-feedback/cursor_prompt.md 

请按照这个需求文档实施用户反馈功能。
1.强调figma链接：http://figma.....
2.补充点1
3.补充点2
```
**AI可能无法每次都精确读取到cursor_prompt中的figma链接，因此最好还是在prompt中加入figma链接强调大模型使用。**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 步骤 2.3: 标记任务完成
编辑 `tasks.md`，将完成的任务从 `[ ]` 改为 `[x]`：

```
- [x] 1.1 创建布局文件 ✅
- [x] 1.2 创建 ViewModel ✅
- [ ] 1.3 创建 Fragment
```
#### 步骤 2.4: 根据Spec文档里的Scenario场景用例自测
确认功能完善后方可提测

### 阶段 3: 归档变更
把相关的文档归档记录

# 📖 落地案例
通过引入 Spec 规范化开发流程，团队在 AI 辅助开发效率上获得显著提升。两位开发者都反馈**整体开发效率有明显提升**，同时建立了可复用、可推广的团队开发标准。

> 这个模式的优点在于规范了一套很好实践的流程，以前的ai coding大家可能都有各自的开发习惯，现在这一套流程是很好复用和推广的，比较利于团队统一开发节奏和一起共用经验
## 落地项目
|开发者|原方式代码开发耗时|新方式耗时|提效幅度|主要场景|
|-|-|-|-|-|
|用户反馈页面优化|2天|0.5天|**75%**|UI还原 + 逻辑实现|
|预装文生表情包需求|5天|4.5天|**10%**|整体方案设计 + 分模块实现|

### 用户反馈页面优化（容器页面需求）
* 快速实现UI和逻辑代码
* 产出的代码代码符合项目规范，可开箱即用

### 预装文生表情包需求（键盘需求）
* 提前设计好整体思路，AI 理解更全面
* 一次性生成整体代码结构
* ⚠️ 仍需分模块调整细节

## 核心优势总结
### 1. 代码质量提升
**一次性跑通率**：

* ✅ 代码可以一次性跑通
* ✅ 大体代码结构正确
* ✅ 符合项目架构规范

**验证结果**：

* 两位开发者均反馈"可以快速产出跑通的代码"
* 代码结构符合预期，无需大幅重构

### 2. 流程标准化
**统一开发节奏**：

* ✅ 规范化的开发流程，易于复用和推广
* ✅ 团队可以统一开发节奏
* ✅ 经验可以共享和沉淀
* ✅ 流程设计合理，无明显卡点

# ❓QA&总结
##### 🤔 **我们使用了make+spec的方式，那是不是不需要Cursor直出的协作方式了？**
—— 并不是，使用Make只是团队协的一种选择，它并不与跨角色使用 Cursor 协同相冲突，make+spec的方式能够解决复杂项目的 **协作稳定性**，在一些 **相对独立&体验导向 **的模块中，依然可以继续使用 Cursor 进行更贴近体验细节的协同探索。

两种方式并非互斥，而是针对不同问题分层使用，形成互补。



❤️ 围绕 Spec 的具体落地细节，我们也会在实践中持续优化，相关问题欢迎进一步讨论 ❤️



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
