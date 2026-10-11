---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "你写的 Skill，及格了吗？"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\你写的 Skill，及格了吗？.md"
---
你写的 Skill，及格了吗？

#### 🧑‍🏫 案例作者：[@孙兴博](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：评估
#### 🔧 使用工具：dodo
#### 📒 案例概要：Skill 评估框架通过 8 个维度量化打分（支持多模型交叉评估），帮助判断 Skill 质量、指导改进与横向对比。
## 0. 为什么需要一把尺子？
![](/personal-site-mvp/img/doc-placeholder.svg "")
Skill 是 Agent 能力的最小封装单元，它把领域知识、工作流程和工具集成打包成一个即插即用的模块，让通用 Agent 秒变领域专家。

现在所有人都在写 Skill、分享 Skill，但面临的问题是：

* **👷 你写的那个 Skill，真的够好吗？**
* **🛜 网络上获取的 Skill 选哪一个更好？**



**能跑**和**好用**之间隔着十万八千里。

一个 Skill，description 写得太宽泛了，很可能 Agent 根本不会触发它；工作流缺少分支逻辑，可能碰到稍复杂的输入就翻车；明明需要附带脚本却硬塞在 Markdown 里，每次执行都重写一遍相同的代码。更麻烦的是，这些问题写的时候不一定能看出来，只有真正使用的时候才会暴露（也有可能不会暴露）。



基于此设定了一套 **8 个维度的量化评估框架**并实现了一个评估 Skill，从元数据质量、执行引导、领域知识密度到工作流完整性等，逐项打分、加权汇总，最终给出 Skill 的 S/A/B/C/D 等级评定。它能帮你审视自己的 Skill：哪里还有短板、该怎么改；也能横向对比多个 Skill：谁设计得更好、好在哪里。



审视自己的作品，它是**改进路线图**；对比他人的作品，它是**选型决策工具**。

## **8 个维度，把"感觉"变成"分数"**
![](/personal-site-mvp/img/doc-placeholder.svg "")
我们要评估一个 Skill 的好坏，不能只靠感觉，必须要有一套可量化的标准。



### 1.1. 8 个评估维度分布在 **Skill 生命周期的三个阶段中**
下面的 8 个维度分布在一个 Skill 从被**发现**到被**执行**完成的完整生命周期，分成三个评估阶段：



#### 第一阶段：能不能被找到
一个 Skill 装好之后，Agent 在每次对话中只会读到它的 name 和 description。如果这几十个字写得不好，Skill 就根本不会被触发，后面写得再好也没用了。

**D1. 元数据质量** 评估的就是这个**第一印象**。description 是否精准地描述了功能？是否包含了用户可能使用的关键词？最好的 description 甚至会写明**不该在什么场景触发**，防止误触发。

这是唯一一个决定 Skill 生死的维度。其他维度影响的是"好不好用"，D1 决定的是"有没有机会被用到"。



#### 第二阶段：用起来顺不顺
Agent 决定触发后，会加载 SKILL.md 的完整内容。这时候考验的是：Agent 能不能顺畅地把任务执行完？

这一阶段有四个维度：

* **D2. 执行引导清晰度：**Agent 加载了 Skill，但面对用户的具体输入，它知道该走哪条路吗？什么情况需要追问用户？什么情况该直接执行？什么操作不该做？好的 Skill 像一本清晰的操作手册，而不是一堆信息的堆砌；
* **D4. 工作流完整性**：如果说 D2 是**每一步怎么走**，D4 就是**整条路是否走得通**。流程是否端到端？步骤之间的衔接是否顺畅？碰到异常（API 超时、文件下载失败）有没有处理方案？
* **D5. 输入输出清晰度**：用户给什么、最终得到什么？这听起来是基本功，但很多 Skill 只写了中间步骤，用户第一次看完全不知道整个流程的起点和终点是什么；
* **D6. 资源利用**：该用脚本的地方是不是用了脚本？该放参考文档的地方是不是放了？还是把所有东西都塞在一个巨大的 SKILL.md 里？好的资源结构遵循**渐进式披露**（SKILL.md 保持精简，详细内容按需加载）；



#### 第三阶段：值不值得存在
最后，跳出执行细节，从更高的视角审视这个 Skill 本身。

* **D3. 领域知识密度**：这是 Skill 存在的根本理由。如果 Skill 里的内容，通用 Agent 不靠它也能做到，那它就没必要存在。好的 Skill 内嵌了难以获取的专业知识：私有 API 的调用方式、内部系统的数据模型、行业特定的最佳实践。
* **D7. 写作质量**：SKILL.md 本质上是写给另一个 AI 看的技术文档。结构是否清晰？有没有冗余？Agent 能否快速扫读并抓到关键信息？
* **D8. 范围与聚焦**：一个 Skill 应该做好一件事，而不是试图包揽一切。过宽的 Skill 什么都做不好，过窄的 Skill 不值得封装。



### 1.2. 权重与评级
并非所有维度同等重要。我们按**对 Skill 实际效果的影响程度**分配权重：

|维度|维度总分|权重|作用|
|-|-|-|-|
|D1. 元数据质量|10|15%|不被触发 = 不存在|
|D2. 执行引导清晰度|10|15%|触发后能否正确决策|
|D3. 领域知识密度|10|15%|Skill 存在的核心理由|
|D4. 工作流完整性|10|15%|能否端到端跑通|
|D5. 输入输出清晰度|10|10%|辅助理解，非决定性|
|D6. 资源利用|10|10%|并非所有 Skill 都需要|
|D7. 写作质量|10|10%|影响效率，不影响能力|
|D8. 范围与聚焦|10|10%|设计原则层面的考量|

每个维度具体的评分方式这里不赘述，有兴趣的同学可以从[附录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/GN8tFVJbUNkx2J?block_id=docyg-f04cf5c6-33c7-11f1-bade-7ffb0416ee86)下载 Skill 查看。



加权求和后，总分映射为五个等级：

|最终得分|评定等级|一句话评语|
|-|-|-|
|9.0 - 10|S|标杆级，可作为范例参考|
|7.5 - 8.9|A|生产可用，只需小幅打磨|
|6.0 - 7.4|B|能用，但有明显短板|
|4.0 - 5.9|C|需要大改|
|0 - 3.9|D|建议推倒重来|



接下来，我们用这套框架实际评估一个 Skill，看看分数背后的含义。

## **拿自己开刀：一个真实的 Skill 评估**
光看评分标准还是比较抽象，这里先拿一个真实的 Skill 跑一遍评估。



下面参与评估的这个 Skill 是我在[从手忙脚乱到一键丝滑——小龙虾/dodo Skill 集成公网 IP 用量推送实录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/M41Mm3wC2t3V-Y?t=mention&mt=doc&dt=doc)实例中真实开发并已投入使用的：

![](/personal-site-mvp/img/doc-placeholder.svg "")
****

评估得出的具体问题与建议摘录如下：

> **问题与建议**
> D1. 元数据质量 (3/10)：description 过于简略，缺少触发条件
> * 影响：Agent 无法自动识别何时应触发此 Skill
> * 建议：扩展 description，包含触发关键词和功能概述
> 
> D7. 写作质量 (7/10)：存在重复内容
> * 影响：文档冗余，影响可读性
> * 建议：删除重复的 SQL 示例（第 333-347 行），保留一处即可；合并重复的说明段落
> 
> 
> **总体评价**
> ip-bill 是一个功能完整、执行清晰的 Skill，适合自动化处理公网 IP 出账流程。主要优势在于：
> * 工作流设计严谨，包含连通性检查和错误处理
> * 领域知识丰富，API、数据库、BOS 等各环节都有详细说明
> * 资源组织合理，脚本、参考文档、示例文件齐全
> 
> 主要改进空间在于**元数据描述**和**文档精简**。增强 description 中的触发条件描述，有助于 Agent 自动识别使用场景。
## 选谁好？两个同类 Skill 的正面对决
这里从 dodo 的可用 Skill 列表中随便选取了两个功能相近的 Skill 进行评估对比：

* Skill A：workos-weekly
* Skill B：subordinate-weekly-report



详细评估结果摘录如下：

![](/personal-site-mvp/img/doc-placeholder.svg "")


> **各自优劣势**
> **workos-weekly 更强的方面：**
> * 领域知识密度更高（OKR 关系、活跃空间、洞察分析等）
> * 资源利用更丰富（references、examples、CHANGELOG）
> * 工作流更复杂（9 步端到端流程）
> 
> **subordinate-weekly-report 更强的方面：**
> * 元数据质量更高（场景路由表更清晰）
> * 输入输出清晰度更高（每个 action 都有完整的输入输出示例）
> * 场景覆盖更全面（6 种 action 覆盖多种查询场景）
> 
> **subordinate-weekly-report 更弱的方面：**
> * 领域知识密度较低（专业概念较少）
> * 资源利用不足（参考资料较少）
> 
> 
> **经验总结**
> **两个 Skill 做得好的地方：**
> * 都有明确的触发条件和反向排除条件
> * 都有清晰的执行引导和错误处理
> * 都聚焦于单一场景，边界清晰
> * 写作质量都很高，结构清晰易读
> 
> 
> **可借鉴的经验：**
> * workos-weekly 的 HARD-GATE 设计值得借鉴，能明确强制规则
> * subordinate-weekly-report 的场景路由表设计优秀，能快速匹配用户意图
> * 两个 Skill 都有详细的命令示例和输出示例，降低了 Agent 的理解成本
> 
## 一个模型就够了？多模型交叉验证
![](/personal-site-mvp/img/doc-placeholder.svg "")
前面的评估案例中，分数评定由一个模型完成。这就像一场考试只有一个阅卷老师，他可能偏严，也可能偏松，我们却无从判断。

实测中很明显的看到，**不同模型对同一个 Skill 的评分存在些许差异**。例如用 GLM-5.1 评估某 Skill，得到 7.8 / A，换成 Claude Opus 4.6 评估则为 6.5 / B。分数差了一个等级，但两个模型指出的核心问题却是趋同的。

这说明单模型评分的**绝对值**不够可靠，但不同模型之间的**共识**是有价值的。

基于这个观察，我又给本 skill-evaluator 增加了**多模型交叉验证**机制：让多个模型独立评估、互相质疑、最终再由主模型完成仲裁，把一家之言升级为专家评审团。



### 4.1. 评估流程
```
flowchart TD
    subgraph phase1["🔍 第一阶段：独立评估 — 互不可见"]
        direction LR
        A["🤖 模型 A<br/>打分 + 证据"]
        B["🤖 模型 B<br/>打分 + 证据"]
        C["🤖 模型 C<br/>打分 + 证据"]
    end

    A & B & C --> MIX((" "))

    subgraph phase2["🔄 第二阶段：交叉互审 — 分差≥2分必须质疑"]
        direction LR
        RA["A 审查 B、C<br/>引用证据质疑<br/>自我修正"]
        RB["B 审查 A、C<br/>引用证据质疑<br/>自我修正"]
        RC["C 审查 A、B<br/>引用证据质疑<br/>自我修正"]
    end

    MIX --> RA & RB & RC

    RA & RB & RC --> ARB

    subgraph phase3["⚖️ 第三阶段：仲裁综合"]
        ARB["主模型（仲裁者）<br/>汇总全部评估 + 互审结果<br/>逐维度三级共识裁定"]
    end

    ARB --> REPORT(["📋 最终评估报告<br/>每个维度标注共识度"])

    style phase1 fill:#E8F5E9,stroke:#66BB6A,stroke-width:2px,color:#2E7D32
    style phase2 fill:#E3F2FD,stroke:#42A5F5,stroke-width:2px,color:#1565C0
    style phase3 fill:#FFF3E0,stroke:#FFA726,stroke-width:2px,color:#E65100
    style A fill:#C8E6C9,stroke:#43A047,color:#1B5E20
    style B fill:#C8E6C9,stroke:#43A047,color:#1B5E20
    style C fill:#C8E6C9,stroke:#43A047,color:#1B5E20
    style RA fill:#BBDEFB,stroke:#1E88E5,color:#0D47A1
    style RB fill:#BBDEFB,stroke:#1E88E5,color:#0D47A1
    style RC fill:#BBDEFB,stroke:#1E88E5,color:#0D47A1
    style ARB fill:#FFE0B2,stroke:#FB8C00,color:#BF360C
    style REPORT fill:#F3E5F5,stroke:#AB47BC,stroke-width:2px,color:#6A1B9A
    style MIX fill:#FAFAFA,stroke:#BDBDBD,stroke-width:1px
```


**第一阶段：独立评估**。

多个模型各自按 8 维度标准独立打分。



**第二阶段：交叉互审**。

所有独立评估完成后，每个模型会看到其他模型的评分。它们需要找出与自己**分差 ≥ 2 分**的维度，明确指出对方哪里评得不合理，并且必须引用 Skill 中的具体内容作为证据。例如：你 D3 给了 8 分，但这个 Skill 的领域知识只覆盖了 API 调用方式，缺少数据模型和决策逻辑的描述（见第 45-60 行），7 分以上要求要有丰富的专家知识，我认为 6 分更合理。

并且，在审查完对方之后，每个模型还要做**自我修正**：看了对方的论据后，我是否要调整自己的分数？这一步迫使模型认真对待对方的质疑，而不是固执己见。



**第三阶段：仲裁综合**。

由主模型（仲裁者）汇总所有独立评估和交叉互审的结果，对每个维度做出最终裁决。



### 4.2. 三级共识机制
针对于每个评估维度，这里设计了一个三级共识机制，用于主模型执行仲裁：

|共识度|条件|处理方式|
|-|-|-|
|一致|所有模型分差 <= 1 分|几乎无争议，取平均值|
|多数|多数模型接近，个别偏离 >= 2 分|采纳多数意见，说明为什么偏离者不被采纳|
|仲裁|无明确多数，分歧严重|审查交叉互审中的论据，采纳证据最充分的评分|



在最终的评估报告中，每个维度都会标注共识度，让使用者能直接看出哪些分数是比较确定的，哪些是有争议的。

例如：

|维度|最终分数|共识度|仲裁说明|
|-|-|-|-|
|D1. 元数据质量|4/10|一致|三模型评分一致|
|D3. 领域知识密度|7/10|仲裁|Sonnet 和 GLM-5 给 8 分，MiniMax 给 5 分；交叉审查中 Sonnet 引用了 API 调用方式和数据模型的具体章节，论据更充分，采纳多数意见|
|D7. 写作质量|7/10|多数|Sonnet(7) 和 MiniMax(7) 一致，GLM-5(9) 偏高；GLM-5 未能给出足够的高分依据|

如果一个维度被标记为"仲裁"，说明这个维度的质量确实处于模糊地带，值得 Skill 作者重点关注。



### 4.3. 当多模型不被支持时
不是所有环境都支持多模型调用，为此在这里我设计了一个兜底方案：单模型多视角评估。

在这个方案中，单一模型扮演三个不同的评审角色，依据评审风格分为：

|视角类型|倾向|
|-|-|
|严格|重视规范性：元数据是否精确？边界条件是否处理？|
|务实|重视可用性：能跑吗？用户能上手吗？|
|专家|重视专业性：领域知识够深吗？设计够精炼吗？|

三个视角评完后同样进行交叉审查和仲裁。

虽然本质上还是一个模型，但通过角色分化强制引入多样性：严格派可能在 D4 给 5 分，务实派同一维度给 8 分，这种分歧是有意义的。

## 四种执行策略的自动路由
不同的 AI 工具能力不同。有的工具（如 Claude Code）支持通过 subagent 同时调用自家多个模型，dodo 也支持这种模式调用 Claude 的 Opus 4.6、Sonnet 4.6、Haiku 4.5 模型。但如果想融合更多其他第三方模型或自定义评估模型列表目前还没有原生支持。所以这里在 Skill 中集成了千帆平台的模型能力，对于上述 Claude 系列之外的模型则通过千帆的能力支持。



### 5.1. 四种策略
如果交叉验证只能在特定工具上跑，这个功能的适用范围就很窄。为了保证在各种 AI 工具及不同的触发场景中本 Skill 执行的兼容性，这里设计了四种执行策略：

|策略|场景|说明|
|-|-|-|
|A（subagent 并行）|所选模型是工具支持 subagent 可用模型|平台原生调多个模型，效果最好|
|B（API 并行）|所选模型均为工具 subagent 不支持的模型|通过千帆调用模型|
|A + B 混合|所选模型同时包含 A 与 B 策略中的两类|原生模型走 subagent，第三方模型走千帆|
|C 多视角兜底|用户要求多模型评估并指定了第三方模型，但选择跳过千帆配置时|退化为单模型评审，使用工具当前的模型（会在报告中给出说明）|



从使用者的视角，只需要提供参与评审的模型：指定主模型（仲裁模型）和交叉评审模型。

策略路由逻辑根据模型列表自动分类：

* 全是工具原生模型走 A；
* 全是第三方走 B，两者都有走 A + B；
* 如果运行中出了问题自动降级到策略 C；

```
flowchart TD
    INPUT["用户选定模型列表"] --> CHECK{"模型分类"}

    CHECK -->|全部原生| SA["策略 A<br/>子代理并行"]
    CHECK -->|全部第三方| SB["策略 B<br/>API 并行"]
    CHECK -->|混合| SAB["策略 A+B<br/>混合并行"]


    SB -->|Token 不可用| SC["策略 C<br/>多视角兜底"]
    SAB -->|第三方部分失败| SA2["仅原生模型<br/>继续评估"]

    SA --> REPORT["评估报告"]
    SB --> REPORT
    SAB --> REPORT
    SC --> REPORT
    SA2 --> REPORT

    style INPUT fill:#E8F5E9,stroke:#66BB6A,color:#2E7D32
    style CHECK fill:#FFF3E0,stroke:#FFA726,color:#E65100
    style SA fill:#E3F2FD,stroke:#42A5F5,color:#1565C0
    style SB fill:#E3F2FD,stroke:#42A5F5,color:#1565C0
    style SAB fill:#E3F2FD,stroke:#42A5F5,color:#1565C0
    style SC fill:#F3E5F5,stroke:#AB47BC,color:#6A1B9A
    style SA2 fill:#E3F2FD,stroke:#42A5F5,color:#1565C0
    style REPORT fill:#E8F5E9,stroke:#66BB6A,color:#2E7D32
```
策略 B 依赖一个 Python 脚本来调用千帆 API。这个脚本只使用了 Python 标准库，不需要操心依赖之类的问题。脚本支持了多模型并行调用和自动重试。



### 5.2. 模型组合与实际效果
这里测试了几种模型组合的评审效果：

|模型类型|模型组合|效果|
|-|-|-|
|工具原生模型|Opus + Sonnet + Haiku|速度快，走策略 A，但模型之间的结果差异较小|
|混合多模型|Sonnet + ernie-5.0 + GLM-5.1|视角差异最大，分歧最有参考价值，走策略 A + B|
|纯第三方模型|ernie-5.0 + DeepSeek + GLM-5.1|与混合多模型类似，不依赖特定平台能力，走策略 B|



当前 Skill 中已默认配置了模型，主模型为：当前 Agent 自身设置的模型；交叉互评模型为：ernie-5.0、sonnet、glm-5.1、minimax-m2.5。

## **三堂会审：多模型评估实践**
上文中对我写的 ip-bill 这个 Skill 进行了单模型的评估，最终评估结果虽然有理有据，但是我们仍然无法确定其权威性，一家之言终归是片面的：这个模型的结果是偏严了还是偏松了？它指出的问题是最关键的还是恰好它注意到的？那些没被扣分的维度，是真的没问题，还是被这个模型忽略了？



用多模型交叉验证对 ip-bill 再评一次。这次由 ernie-5.0、sonnet 4.6、glm-5.1、minimax-m2.5 四个来自不同厂商的模型独立评估，互相质疑，最终由主模型 Claude Code Opus 4.6 仲裁出一份经过质证的结论。评估结果篇幅较长，这里我直接导出了一份报告文件：

[附件]
## 评完之后怎么改？
拿到评估结果和改进建议后，可以继续让 AI 助手代劳。本文为了演示方便，拆分成了评估 + 优化，懒得看结果的话可以让 AI 助手直接一步处理分析 + 优化（这里演示的是单模型评估后优化，多模型的操作也是类似的）。

![](/personal-site-mvp/img/doc-placeholder.svg "")


更多的用法实践可以自行扩展，例如多 Skill 的对比优化，互相学习其优点改进缺点等等，主要还是要依赖模型的分析能力。

## 写在最后
回到开头的两个问题：自己写的 Skill 够不够好？网上下载的选哪个？

现在你有了一套 8 维度的评估框架来回答它们，给 Skill 打分、找短板、做对比，把**感觉还行**变成**可量化的判断**。并且可以选择通过多模型交叉评估来避免单模型一言堂的造成的评估局限，但是多模型也会增大 Token 的消耗和 Skill 的运行时间，具体使用哪种方式来评估可以由使用者自由选择。



随着更多人写 Skill、分享 Skill，我们可能需要更完善的评估手段：自动化的静态检查工具、基于实际执行数据的动态评分、社区驱动的 Skill 评级体系。这些都值得探索。

这套评估框架只是一把尺子，也有一定的局限性，它度量的是 Skill 的**文档工程**质量，而非运行时的全部真相。

知道它能量什么、不能量什么，才能用好它。

## 附录
* [本 Skill 在 OneTool 平台上的地址](https://console.cloud.baidu-int.com/onetool/skills/2041)；

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
