---
title: "业务背景与问题痛点"
description: "AI 驱动开发：从 Prompt 到 Product"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI 驱动开发：从 Prompt 到 Product.md"
---
AI 驱动开发：从 Prompt 到 Product

#### 🧑‍🏫 案例作者：[@高雅典](https://ku.baidu-int.com?t=mention&mt=contact&id=75decdb0-fced-11f0-a35d-e5f584c78fff)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Cursor（不限制）
#### 📒 案例概要：本文介绍了通过自然语言Prompt重构开发生命周期，实现AI原生研发范式。以 AI 原生网关产品为例，前端由产品经理使用 Prompt 开发，后端由 AI 辅助研发，显著提升开发效率。AI赋能后，1周完成传统团队30天的工作量，展示了自然语言即代码的未来趋势。
**本文档视频讲解：**[AI驱动开发：从Prompt到Product](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/55443?isFromPc=1&reportLog=true?t=mention&mt=doc&dt=sdk)

# 业务背景与问题痛点
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
1️⃣

**"深夜 10 点，会议室灯光惨白。**
PM 指着屏幕上的原型图第 18 版：“这个搜索框，能不能再调一下交互？”
RD 猛地合上笔记本：“这需求根本做不完！明天又要通宵！”
—— 直到我们发现了【**开发者的魔法咒语】：Prompt。**"

2️⃣

**"现在，一切变得不同 ——**
PM 只需要用自然语言输入：“做一个支持模糊搜索的列表页，并且支持多选移除...”
AI 瞬间响应：**前端自动生成 React 代码，后端构建 API，甚至考虑了边界情况！**
RD 检查代码后震惊：‘这 API 居然自带 Swagger 文档和 JWT 鉴权？比我手写的还规范！’"

3️⃣

**"这不仅是‘低代码’，而是‘自然语言即代码’的革命。**

我们训练 AI ‘啃’了真实项目代码和前后端开发规范，让它理解：

* 列表页 = 分页查询 + 按关键字排序 + Table 组件
* 搜索 = Search 组件 + 模糊匹配/精准匹配
* 多选移除 = 复选框 + Checkbox 组件 + 记录ID...   **AI 不再只是补全代码，而是真正‘理解’业务逻辑。**"

4️⃣

**"上线后，PM 用一句 Prompt：‘新增一列关联状态，需要实时查询集群的关联状态’**
**1 小时后，完整功能已部署到生产环境 —— **而传统团队至少需要一周。
现在，PM 和 RD 终于可以一起准时下班，喝着咖啡说：‘下次需求会，能不能让 AI 也来参加？’"

# 项目方案/解决方案
**我们做了一件被认为不可能的事！**

用`自然语言`替代`代码`，用`Prompt`重构`开发生命周期`，打造了首个**完全由 AI 原生范式驱动的云上产品**。

   我们结合 Cursor 颠覆传统开发模式，探索出一条 AI 原生研发范式，使用 AI 开发新范式打造了一款基于云原生的、高扩展、高可用的云上托管网关产品：AI 原生网关，产品面向 Agent/MCP/AI 推理场景/传统容器服务/微服务精心设计。

   **产品前端完全由产品经理使用 Prompt 进行开发，后端由研发使用 AI 辅助进行开发**，在规定好生成范式和前后端开发规则后，AI 能够自动生成生产级、符合业务逻辑的代码，毫不夸张地说，AI 赋能后 1 周完成了传统团队 30 天的工作量。这就是 OpenAI 预言的未来：自然语言即代码的时代已经到来！**  **产品体验地址：[https://console.bce.baidu.com/aigw](https://console.bce.baidu.com/aigw)。

**我们做了一件被认为不可能的事！**

用`自然语言`替代`代码`，用`Prompt`重构`开发生命周期`，打造了首个**完全由 AI 原生范式驱动的云上产品**。

   我们结合 Cursor 颠覆传统开发模式，探索出一条 AI 原生研发范式，使用 AI 开发新范式打造了一款基于云原生的、高扩展、高可用的云上托管网关产品：云原生网关，产品面向 Kubernetes AI 推理场景/传统容器服务/微服务精心设计。

   **产品前端完全由产品经理使用 Prompt 进行开发，后端由研发使用 AI 辅助进行开发**，在规定好生成范式和前后端开发规则后，AI 能够自动生成生产级、符合业务逻辑的代码，毫不夸张地说，AI 赋能后 1 周完成了传统团队 30 天的工作量。这就是 OpenAI 预言的未来：自然语言即代码的时代已经到来！**  **产品体验地址：[https://console.bce.baidu.com/aigw](https://console.bce.baidu.com/aigw)。

# 一、AI 开发新范式 1.0
## AI 开发模式 vs 传统开发模式
**传统开发模式：**

1. 产品设计 - 产品 PRD
2. 需求评审
3. UE 设计 & UE 评审
4. 前端技术方案
5. 后端技术方案
6. 后端开发
7. 前端开发
    1. 业务逻辑
    2. 交互界面

8. 灰度环境联调
9. QA 回归测试
10. UE 走查页面
11. showcase
12. 问题修复
13. 部署上线

**AI 开发模式：**

1. 产品设计 - 产品 PRD
2. 需求评审
3. UE 设计 & UE 评审（PM 和UE同时使用 Figma 进行设计，设计交付效率提升）
4. 前端技术方案
5. 后端技术方案
6. PM 输出接口需求文档
7. RD 将接口需求文档投给 AI，由 AI 输出接口文档
8. PM 和 RD 双方 Review 接口文档
9. 将确认后的接口文档上传至前后端代码库
10. 前后端以确认后的接口文档为标准进行 Prompt 开发
11. PM 输出页面交互 Prompt（需要包含交互指令、需要调用的接口的接口文档）
12. 后端基于接口文档用自然语言指挥 AI 开发
13. 前端基于Figma链接 + 页面交互 Prompt 指挥 AI 开发
    1. 业务逻辑
    2. 交互界面

14. 灰度环境联调



*熟练后基本可达到一段 Prompt 实现一个页面*

1. RD 使用 AI 生成测试用例
2. QA 回归测试
3. UE 走查页面
4. showcase
5. 问题修复，将问题用自然语言描述给 AI
6. 部署上线



## AI 开发工作流
### 2.1. 前端预备知识
** ****  Q1: 什么是组件？**

* 组件 = HTML+CSS+Javascript 封装，可以理解成一个能被直接拿去搭建不同页面的积木。调用时只需要使用组件名并指定其属性值即可使用，不需要自己使用代码开发。

![](/personal-site-mvp/img/doc-placeholder.svg "")


![按钮（Button）](/personal-site-mvp/img/doc-placeholder.svg "按钮（Button）")
![搜索框+刷新按钮（Search+Refresh Button）](/personal-site-mvp/img/doc-placeholder.svg "搜索框+刷新按钮（Search+Refresh Button）")
![弹窗+表单（Modal+Form）](/personal-site-mvp/img/doc-placeholder.svg "弹窗+表单（Modal+Form）")
** ****  Q2: 为什么要用组件？**

* 1. 能保证 UI 样式的一致性
* 2. 提高开发效率：避免重复造轮子

** ****  Q3: 什么是组件库？**

* 就是不同组件的集合，目前有很多开源的组件库，比如 antd、element 等，不同组件库的区别基本可以归类为 1. 支持的前端技术栈可能不一样（Vue or React） 2. 组件的设计风格不一样  3. 组件丰富度不一样。

![支持的前端技术栈](/personal-site-mvp/img/doc-placeholder.svg "支持的前端技术栈")
![设计风格](/personal-site-mvp/img/doc-placeholder.svg "设计风格")
* 百度云上用的组件库非开源，包括 acud、sui（acud：[https://acud.now.baidu-int.com/components/radio](https://acud.now.baidu-int.com/components/radio) sui：[https://console-center.cdn.bcebos.com/bce-plat-static/sui/doc/index.html#/doc/intro/intro](https://console-center.cdn.bcebos.com/bce-plat-static/sui/doc/index.html#/doc/intro/intro)）

** ****  Q4: 前端的一些触发事件包括哪些？**

* 可以分成 2 类（每类中仅列举常用的触发事件）：
    * 1. 鼠标事件：点击事件、鼠标移入事件、鼠标焦点离开某个区域
    * 2. 键盘事件：键盘输入时监听


** ****  Q5: 怎么在控制台查看前端样式？**

打开Chrome浏览器，右键->点击检查，点击右上角红框圈出来的地方，放到某一个样式上就能看见这个样式的布局，在右侧【样式】中能看见具体的样式代码

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
** ****  Q6: 前端怎么调试？**

1. 方式1: 可以在代码中加入 console.log()，写上你需要打印的内容，就能在控制台中输出，查看的方式为：右键->点击检查，点击右上角控制台 Tab
2. 方式2: 点击网络查看接口请求和响应是否符合预期

![方式1](/personal-site-mvp/img/doc-placeholder.svg "方式1")
![方式2](/personal-site-mvp/img/doc-placeholder.svg "方式2")
### 2.2. 前置准备
在使用 AI 开发之前，需要准备一系列 markdown 格式的文档，用于约束 AI 开发。

**Why Markdown？** AI 需要一份读得懂的文档，而 markdown 本身就是**格式化的、结构化**的，不管是人还是 AI 都能够读懂

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


#### 2.2.1. 全局规则
这部分内容需要放在全局 Rules 中，每次向 AI 发送 Prompt 都需要让 AI 读取这部分内容

1. **前端组件库的使用说明**（比如云上用的比较多的 acud、sui 等，每个组件对应的自然语言是什么、经常用到的组件以及组件的属性字段有哪些...都需要梳理清楚，例如列表：Table，按钮：Button，刷新：Refresh，空状态：Empty... PS：不同的前端组件库组件名不一定相同） **—— 后续我们发现直接使用 Figma 设计稿的链接，使用组件搭建页面，AI 就能够读取到对应的组件名（参见开发新范式 2.0）**
2. **前端代码生成规范**（比如文件结构、命名规范、样式处理、全局样式规范...）
3. **后端代码生成规范**
4. **接口规范**（比如后端接口响应结构需要符合云上的结构、List 接口需要支持分页、请求失败的响应结构...）

![](/personal-site-mvp/img/doc-placeholder.svg "")
![前端组件属性说明](/personal-site-mvp/img/doc-placeholder.svg "前端组件属性说明")
![前端代码规范](/personal-site-mvp/img/doc-placeholder.svg "前端代码规范")
#### 2.2.2. 业务逻辑
在规定好全局规范后，就可以开始进入 AI 开发的阶段啦！这里需要准备和业务逻辑相关的文档

**  AI 研发新范式几个重要的标准  **

1. **接口需求文档：**由 PM 产出，需包含以下内容：1. 页面需要哪些接口 2. 每个接口的请求和响应是什么 3. 错误信息返回格式，保证接口需求文档中每个字段和页面上的字段能对上
2. **接口文档：**由 RD 基于接口需求文档结合 AI 生成，RD 首先需要 review 一遍各个字段名称是否合适、是否符合接口需求文档，RD review 后再拉上 PM 二次 review
3. **页面交互 Prompt：**由 PM 产出，需包含以下内容：1. 现状描述   2. 需求描述  3. 页面交互与样式  4. 页面与接口对应关系  5. 可维护性  6.接口文档  7. 遵守原则*（可根据自身业务进行调整）*
4. **AI 整体约束：**全局 Rules，用于约束 AI 生成代码的规范，包含 1. 前端代码规范 2. 后端代码规范  3. 前端组件使用规范 4. 接口文档规范



![接口需求文档示例](/personal-site-mvp/img/doc-placeholder.svg "接口需求文档示例")
![接口文档示例](/personal-site-mvp/img/doc-placeholder.svg "接口文档示例")
![前端页面交互 Prompt 示例](/personal-site-mvp/img/doc-placeholder.svg "前端页面交互 Prompt 示例")
### 2.3. AI 开发
首先演示一个比较简单的功能实现流程：实例列表支持局部编辑

[附件]


以下是完整的页面生成 Prompt：

```
1. 现状描述：目前在实例列表页面中展示了当前地域中的所有实例，在列表操作列中有一个删除操作。当鼠标移入实例列表中某一行时，实例 ID 和接入地址中内网、公网后面会出现一个复制的图标，点击之后支持复制对应内容。
2. 需求描述：现在，我期望保留原有复制功能和逻辑不变，当鼠标移入实例列表中某一行时，实例名称和描述对应的内容右侧会出现一个编辑的图标（<OutlinedEditingSquare />），点击编辑图标之后可以对对应的内容进行编辑。当用户编辑完成后，就调用更新实例接口，接口字段和格式和接口文档保持一致，我会在第 3 点中描述页面交互以及和页面接口对应的关系。
3. 页面交互与样式&页面和接口的对应关系：当用户点击实例名称右侧的编辑图标后，在当前编辑图标上方出现一个 Popover 气泡卡片，卡片包含 1 个输入框，左下角为确定和取消按钮，首先需要在输入框内回显当前网关实例的名称，用户支持编辑，在输入框下方有一行提示文案：“必须以字母或者中文开头，支持大小写字母、中文、数字以及-/.特殊字符“，并且输入框长度限制 64，在输入的过程中需要判断实例名称是否符合规则，如果不符合需要输入框置红，并且在输入框下方提示不合法的原因；仅合法实例名称可点击确定按钮。点击确定按钮后调用更新实例接口，将输入框内的实例名称传给接口，若更新成功则右上角 toast 提示：实例名称编辑成功。当用户点击描述内容右侧的编辑图标后，在当前编辑图标上侧出现一个Popover 气泡卡片，卡片包含 1 个输入框，左下角为确定和取消按钮，同样首先在输入框回显原有的描述内容，支持编辑，编辑完成后点击确定调用更新实例接口，若更新成功则右上角 toast 提示：实例描述编辑成功。
4. 可维护性：尽量不要修改存量代码，如果实在需要修改请写上注释并保留原代码注释掉即可，另外，在你认为比较重要的操作节点时使用 console. log 输出关键信息以方便后期前后端联调。
5. 接口文档：参见附件
6. 遵守原则：尽量不要自动生成我没有提到的交互逻辑，比如在本次 prompt 中我只希望你修改实例列表中编辑实例名称和描述的逻辑，所以你不应该再自动修改其他页面。
```


接下来演示一个完整的功能模块：消费者管理，总共会涉及 7 个接口，5 个页面，**仅用于简单演示基于我们的研发新范式使用 AI 驱动研发的能力，后续功能上线需要详细的测试和 review**

[附件]


# 二、AI 开发新范式 2.0
**随着团队使用开发新范式的逐渐深入，我们也在多个方面进行了提升，最值得展开深入分享的是和 UE 团队的深入合作，解决了在新范式 1.0 中我们遇到的以下问题：**

1. PM 不再需要写动辄 2000 字的前端交互 prompt 用以约束页面样式的生成。结合 UE 团队提供的标准设计资产，**使用 Figma 以搭建组件的方式设计页面** —— 产出原型图

![UE 组件资产](/personal-site-mvp/img/doc-placeholder.svg "UE 组件资产")
![使用 Figma，AI 能够直接读取到组件名称，提高准确性](/personal-site-mvp/img/doc-placeholder.svg "使用 Figma，AI 能够直接读取到组件名称，提高准确性")
 

![1.0 的前端 prompt](/personal-site-mvp/img/doc-placeholder.svg "1.0 的前端 prompt")
![2.0 的前端 prompt ](/personal-site-mvp/img/doc-placeholder.svg "2.0 的前端 prompt ")
2. 在第一步基础上，我们已经得到了一份包含前端标准组件信息的原型图设计稿。大部份情况下后续 UE 同学可以直接在这份设计稿的基础上进行调整，不用再从 0 到 1 进行设计。**PS：这里需要感谢 红利、舒羽、金风几位 UE 同学给我们提供详细的帮助～**

![](/personal-site-mvp/img/doc-placeholder.svg "")
3. 使用 Figma 提供的官方 MCP，在任何 AI Coding 编辑器中都能够准确无误的读取到设计稿中对应的组件信息。我们需要做的就是 **1. 配置 Figma MCP 2. 复制设计稿的链接 3. 加入到前端交互 prompt 中喂给 AI ****（为什么可以读到？因为设计稿本身就是由组件搭建的，自带了组件的元信息，这一步解决的是我们必须要指定组件名称的过程，但是这一步能成功的前提是前端代码库中已经安装了对应的组件库，这样 AI 从设计稿中读到这个组件，例如：这个组件叫 Search，只有前端代码里已经安装过，才能在代码中 import Search 成功）**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
4. 最后我们可以看一下设计稿和最终生成的效果对比：

![Figma 设计稿](/personal-site-mvp/img/doc-placeholder.svg "Figma 设计稿")
![生成效果](/personal-site-mvp/img/doc-placeholder.svg "生成效果")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")




# 评估指标
根据需求的复杂度拆分成 A、B、C 三类，分类统计从需求评审到功能上线的完整时长

![](/personal-site-mvp/img/doc-placeholder.svg "")
### A 级**（高复杂度）**：全新页面，全新功能 ***（从 开发->******前后端******上线 平均 14d） ***
* **定义**：涉及全新页面搭建，或涉及复杂交互与后端多接口联调的从 0 到 1 的功能。
* **周期 **：开发至上线约 **14** 个工作日。

1. AI 可观测

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
2. MCP 服务

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### B 级**（中复杂度）**：在已有页面基础上加入全新功能模块 ***（从 开发->前后端上线 平均 5d） -  传统模式大概约 3周～4周***
* **定义**：在现有页面架构下，新增独立的功能区块、弹窗或复杂的组件级更新。
* **周期**：开发至上线约 **5** 个工作日。



1. AI 模型路由 + Token 限流

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### C 级（低复杂度）：已有页面，新增 1-2 个字段 ***（从 开发->前后端上线 平均 1d） - 传统模式约 7d***
* **定义**：不改变页面结构，仅涉及字段增减、文案调整、样式优化或简单逻辑修正。
* **周期**：开发至上线约 **1** 个工作日。

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 落地成果与业务价值
用`自然语言`替代`代码`，用`Prompt`重构`开发生命周期`，打造了首个**完全由 AI 原生范式驱动的云上产品 —— AI 原生网关**。

   我们结合 Cursor 颠覆传统开发模式，探索出一条 AI 原生研发范式，使用 AI 开发新范式打造了一款基于云原生的、高扩展、高可用的云上托管网关产品：AI 原生网关，产品面向 Agent/MCP/AI 推理场景/传统容器服务/微服务精心设计。

   **产品前端完全由产品经理使用 Prompt 进行开发，后端由研发使用 AI 辅助进行开发**，在规定好生成范式和前后端开发规则后，AI 能够自动生成生产级、符合业务逻辑的代码，毫不夸张地说，AI 赋能后 1 周完成了传统团队 30 天的工作量。这就是 OpenAI 预言的未来：自然语言即代码的时代已经到来！**  **产品体验地址：[https://console.bce.baidu.com/aigw](https://console.bce.baidu.com/aigw)。

### 产品介绍：AI 原生网关
![](/personal-site-mvp/img/doc-placeholder.svg "")
### **What**
**AI 原生网关（AI Gateway）**是基于云原生的、高扩展、高可用的云上托管网关服务，是面向 Kubernetes AI 推理场景/传统容器服务/微服务设计的云原生网关，通过零侵入式服务代理与多策略流量调度，为企业提供生产级高效接入与调度能力。

### **Why**
**多层网关架构导致资源浪费与性能损耗：**传统架构中，企业常采用流量网关、微服务网关和安全网关的独立三层架构，导致资源重复消耗、性能逐层衰减，且运维复杂度高；

**动态服务治理能力不足：**传统网关（如 Nginx）依赖静态配置，无法适应云原生环境中服务实例动态扩缩、IP 频繁变更等场景，导致配置更新延迟和业务中断风险；

**安全与合规的分散管理：**传统方案中安全策略（如认证、鉴权）分散在多个网关或服务中，导致管理碎片化、防护链路冗余，且难以满足数据隐私法规;

**多源 AI 服务难以管理：**各种商业和自建模型促进业务发展，然而企业应用 AI 时面临集成、稳定性、安全性、管理复杂性等挑战。

### **How**
提供**无侵入式托管网关服务**，实现 K8S 自有模型服务/容器服务代理及流量调度，支持网关实例管理、推理服务管理、路由管理、消费者管理，支持配置多种负载均衡算法、认证鉴权策略、流量调度策略，解决客户多层网关部署繁琐、运维耗时、动态服务治理能力不足等问题。



作为云原生产品体系的核心拼图，成功从 0 到 1 打造了面向 Kubernetes AI 推理、容器服务及微服务场景的下一代智能网关。产品深度整合 CCE 容器引擎，无缝承接百舸开发机与 AI 推理流量，填补了企业在云原生流量治理中的关键需求。

> 以下视频展示网关线上 console：
[附件]
## 附录：全局规则
**我们所有使用的全局规则如下：**

[附件]
[附件]
[附件]
[附件]
[附件]
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
