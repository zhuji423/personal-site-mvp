---
title: "一、设计哲学"
description: "Context Engineer再进阶——Harness Engineer"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Context Engineer再进阶——Harness Engineer.md"
---
Context Engineer再进阶——Harness Engineer

#### 🧑‍🏫 案例作者：[@彭宇豪](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Comate、Ducc
#### 📒 案例概要：个人在AI Coding实践时，与Harness Engineering理论碰撞产生的思想火花。
> 前言：
> 如今，AI Coding 已经从一个新鲜话题逐渐演变为行业共识，如何让 AI 持续、可靠地生成高质量代码，成为各个团队探索的核心命题。深入实践后大家逐渐发现，这本质上是软件工程在新时代的延伸——传统工程解决的是"人如何可靠地编写代码"，AI 时代这一命题并未改变，变化的只是执行主体从"人"迁移到了"AI Agent"。这里以clouddisk-lifeactivity 项目的技术栈与业务场景为载体，对 AI 辅助开发展开体系化梳理，致力于构建一套可执行、可追踪、可持续优化的工程实践体系。
> 而实践证明，卓越的上下文工程，关键不在于"提供多少信息"，而在于"如何有序地组织信息供给"来保障 AI Agent 在长周期任务中的执行稳定性。这一探索方向，与 Harness Engineering 的若干核心理念高度契合。本文既是对既有实践的系统性沉淀，也是历经大量理论碰撞与真实验证后，逐步凝练而成的思考结晶。
**核心理念**：上下文工程（Context Engineering）—— 精心选择和注入相关的代码、文档、规范，比写复杂的 Prompt 更有效。

**已验证的实践**：

    * 两层架构（Rules + Skills）
    * 人工阶段性确认，将 AI 协作拆解为可观测的关键节点
    * L0-L4 过程质量评估体系

**预计交付形式**：

一个**整合完整开发实践的工具包插件**，以**工作流**为核心，通过人工阶段性对齐实现目标制定与结果验收，提升AI生成准确率。workflow全闭环设计减少返工，兼容Comate与Ducc。

---

# 一、设计哲学
在深入技术细节之前，先明确当前实践设计Workflow的五大原则：

### 1.1 上下文压缩
> **问题是 context 会满，而不是模型记不住。**
主 Agent 的 context window(上下文窗口) 是有限资源。压缩的本质是"让模型看到更少但更精的信息"：

|压缩维度|实现|效果|
|-|-|-|
|历史对话|context-manager 摘要化|清理冗余轮次|
|知识库|索引 + 按需加载|只加载相关片段|
|代码库|Explore SubAgent 按需检索|不预加载全量代码|

### 1.2 人工阶段性目标制定与结果验收
> **AI 负责执行，人负责目标和验收。**
7 步工作流中，人在三个关键节点介入：

```
需求解析后 → Checkpoint 1 → 确认"要做什么"（目标制定）
方案设计后 → Checkpoint 2 → 确认"怎么做"（方向确认）
代码生成后 → Checkpoint 3 → 确认"做对了吗"（结果验收）
```
Checkpoints 不仅是验收点，也是**目标制定点**——每一步的人工确认都在重新校准下一步的目标。

### 1.3 人工确定边界
> **边界由人定义，AI 在边界内自由发挥。**
Architectural Constraints 的核心是不变量，而不变量必须由人划定（这也是为何我在Workflow中加入了“致死量”的人工确认环节）：

|边界类型|人工定义|AI 自由发挥|
|-|-|-|
|安全边界|"SQL 禁止字符串拼接"|选择 ORM 库、参数绑定方式|
|架构边界|"路由前缀必须符合规范"|具体的 handler 实现|
|契约边界|"接口响应必须包装"|内部逻辑结构|

**错误做法（微观管理）**：规定"必须用 GORM 库"——连实现细节都被规定，AI 没有自由度。

**正确做法（不变量约束）**：规定"禁止字符串拼接 SQL"——**AI 可以选择任何安全的实现方式**。

### 1.4 文档知识库再压缩
> **静态文档压缩为索引，动态信息记录为即时上下文。**
知识分层策略的本质是把"全量知识"压缩为"按需加载的索引"：

```
flowchart LR
    Full[全量知识库 约10000 tokens] --> |提炼不变量| Rules[静态上下文 约500 tokens]
    Full --> |建立索引| Index[SKILL.md 索引 约450 tokens]
    Full --> |按需检索| Instant[即时上下文 约500 tokens/次]

    Rules --> Agent[主 Agent Context]
    Index --> Agent
    Instant --> Agent

    style Full fill:#ffebee
    style Agent fill:#e8f5e9
```
**即时上下文**：Explore/docs-reader 按需检索得到的精炼信息，区别于静态上下文（常驻加载）和动态上下文（session 摘要）。

### 1.5 批判性思维
> **不懂的问题要抛出来，不能臆测。**
当遇到以下情况，AI 必须**主动暂停并请求人工确认**：

|情况|正确行为|错误行为|
|-|-|-|
|需求有歧义|抛出问题，列出可能的理解|选择一个理解继续执行|
|上下文不足|明确说明缺少什么信息|假设或猜测缺失信息|
|多种方案可选|列出方案及优劣，请求选择|自行选择一个方案|
|规则冲突|报告冲突，请求澄清|选择一条规则遵循|

批判性思维是防止 AI "自信地做错事"的关键机制。

---

## 二、从 Context 到 Harness：实践的自然演进
### 2.1 实践驱动：问题先于概念
Harness Engineering 并非一个全新的颠覆性理论。回顾在 `clouddisk-lifeactivity` 项目的实践轨迹：

* 从预加载全部规范到 Rules + Skills 两层架构
* 从一次性生成到 7 步结构化工作流，人工在关键节点验收
* 从单 Agent 包揽一切到探索 SubAgent 职责拆分

这些改进正是**在实践中持续遇到真实问题，逐步演化出的解决方案**。当我们发现"给 AI 什么信息"已经优化到瓶颈，自然开始关注"如何组织信息的供给方式"。

**Harness 是上下文工程在实践深化的自然延伸**。

### 2.2 Agent 退化的数学约束
为什么需要检查点机制？因为 LLM 在长期任务中存在结构性约束：

|问题|说明|
|-|-|
|**局部优化 vs 全局一致**|LLM 每次生成时，它优化的是局部概率最优，而非全局逻辑一致|
|**误差不可逆积累**|随着任务推进，误差会像滚雪球一样不断放大|
|**信息传递损耗**|每次需求翻译都是一次信息损耗，约束在传递中不断被稀释|

LLM 本质是一个 $P(next_token | context)$ 的条件概率模型。它在每一步都选择概率最高的 token，但这些"局部最优"串联起来，并不保证"全局最优"或"全局一致"。这就像贪婪算法——每步选最优，整体未必最优。这些不是可以通过更好的 Prompt 或更多的上下文彻底解决的技术问题，而是**数学上的固有限制**。承认这一点，才能理解为什么必须在架构层面引入 Checkpoint，而非持续在单点优化。

### 2.3 Context Engineering vs Harness Engineering
|维度|Context Engineering|Harness Engineering|
|-|-|-|
|**核心问题**|给 AI 什么信息|如何让 AI 稳定产出|
|**关注点**|信息供给|约束与验收|
|**关键机制**|RAG 按需检索|不变量|
|**关系**|基础能力|在基础之上的稳定性保障|

没有良好的上下文工程，Harness 无从谈起；仅有上下文工程而没有 Harness，长期任务的稳定性难以保证。两者相辅相成。

---

## 三、Harness 三大支柱实践落地
> OpenAI 定义的 Harness Engineering 由三大支柱构成：Context Engineering、Architectural Constraints、Entropy Management。我们的实践也是基于此展开。
### 3.1 三大支柱映射
```
flowchart LR
    subgraph CE[Context Engineering 信息供给]
        rules[rules/ 静态上下文]
        skills[skills/ 指南文档]
        knowledge[knowledge/ 动态知识]
        explore[Explore/docs-reader 即时上下文]
    end

    subgraph AC[Architectural Constraints 行为边界]
        security[security 安全不变量]
        constraints[constraints 架构不变量]
        linter[linter 自动拦截]
        review[code-review 人工审查]
    end

    subgraph EM[Entropy Management 熵管理]
        cm[context-manager 对话层]
        qe[quality-evaluator 代码库层]
        ka[knowledge-archiver 知识沉淀]
        test[测试验证]
    end
```
|支柱|核心问题|我们的实践|
|-|-|-|
|**Context Engineering**|Agent 需要什么信息？|rules/ + skills/ 提供静态上下文，knowledge/ 提供动态知识，Explore/docs-reader 按需检索即时上下文|
|**Architectural Constraints**|Agent 能做什么？边界是什么？|security + constraints 定义不变量，linter + code-review 执行约束|
|**Entropy Management**|如何防止对话上下文和业务系统腐化？|context-manager 管理对话层熵增，quality-evaluator + knowledge-archiver 管理代码库层熵增，测试验证|

### 3.2 目录结构
```
.comate/
├── rules/                    # Context Engineering：静态上下文
│   ├── always/               # 常驻上下文（安全红线 + 关键约束 + 索引）
│   │   ├── security/         # Architectural Constraints：安全不变量
│   │   ├── constraints/      # Architectural Constraints：架构不变量
│   │   ├── skill-index/      # Context Engineering：能力索引
│   │   └── workflow-priority/
│   ├── auto/                 # 按文件匹配加载
│   └── requested/            # 按需加载
│
├── skills/                   # Context Engineering + Tool
│   ├── dev-workflow/         # 开发流程
│   │   ├── SKILL.md          # 索引（~450 tokens）
│   │   └── step/             # 详细步骤（按需加载）
│   ├── coding-guide/         # 开发指南
│   ├── code-review/          # Entropy Management：代码审查
│   ├── unit-test/            # Entropy Management：测试验证
│   ├── knowledge/            # Context Engineering：知识库
│   │   ├── SKILL.md          # 入口
│   │   ├── INDEX.md          # 索引
│   │   ├── patterns/         # 可复用模式
│   │   ├── pitfalls/         # 踩坑记录
│   │   └── projects/         # 功能归档
│   ├── context-manager/      # Entropy Management：对话压缩
│   └── README.md
│
├── agents/                   # Tool + SubAgent
│   ├── code-explorer.md
│   ├── docs-reader.md
│   ├── quality-evaluator.md  # Entropy Management
│   ├── test-generator.md     # Entropy Management
│   └── knowledge-archiver.md
│
└── context/                  # Entropy Management：会话摘要
    └── session_*.md
```
### 3.3 知识分层策略
```
flowchart LR
    L1[L1 Always<br />安全红线] --> L2[L2 Auto<br />编码规范] --> L3[L3 Task<br />相关模式] --> L4[L4 Skill<br />专属参考] --> L5[L5 Temp<br />临时文档]

    style L1 fill:#e1f5fe
    style L2 fill:#e8f5e9
    style L3 fill:#fff3e0
    style L4 fill:#f3e5f5
    style L5 fill:#fce4ec
```
**Token 优化**：`go-coding-standard` 从 ~2500 tokens 降至 ~300，节省 88%。

这个优化的本质是"不变量提炼"：把 2500 tokens 的完整规范，压缩为 ~70 行核心约束（禁止项 + 必须项），详细示例移至Skill中按需加载。

### 3.4 7 步结构化工作流
```
flowchart TD
    A[需求输入] --> B[Step1 TODO] --> C[Step2 需求解析] --> D[Step3 方案设计] --> E[Step4 代码生成] --> F[Step5 质量评估] --> G[Step6 单测] --> H[Step7 自动沉淀]

    C -.->|Checkpoint| C1[人工确认]
    D -.->|Checkpoint| D1[人工确认]
    E -.->|Checkpoint| E1[人工确认]

    style A fill:#e3f2fd
    style H fill:#c8e6c9
```
### 3.5 L0-L4 过程质量评估体系
> L0-L4 是**任务内可评估**的过程质量指标，由 `evaluation` skill 覆盖。L5 业务收益是**周期性外部指标**，需上线后数周才可观察，不纳入单次任务评估。
|层级|维度|MVP|达标|优秀|说明|
|-|-|-|-|-|-|
|L0|需求理解|≥60%|≥75%|≥80%|任务内评估 ✅|
|L1|方案设计|≥70%|≥80%|≥85%|任务内评估 ✅|
|L2|规范遵循|≥60%|≥80%|≥85%|任务内评估 ✅|
|L3|能力执行|≥75%|≥85%|≥90%|任务内评估 ✅（工作流/SubAgent 是否正确触发）|
|L4|代码质量|≥70%|≥85%|≥90%|任务内评估 ✅|
|L5|业务收益|≥30%|≥40%|≥50%|周期性指标 ⏱️（不在 evaluation skill 范围）|

**L2（规范遵循）是工程化的核心保障**：它直接对应约束层的有效性。L2 达标，意味着不变量未被击穿；L2 低于 MVP，说明 Rules 定义有问题或约束力不足。

---

## 四、三大支柱详解
> Harness Engineering 的核心理念：**限制解决方案空间，反而增加 Agent 的生产力和可靠性。**
### 4.1 Context Engineering：精准供弹
**核心问题**：Agent 需要什么信息？

**三种上下文**：

|类型|说明|实现|加载时机|
|-|-|-|-|
|**静态上下文**|项目规范、安全红线、能力索引|rules/always + skills/SKILL.md|永远加载|
|**动态上下文**|会话摘要、历史决策|context/session_*.md|新对话开始时|
|**即时上下文**|按需检索的代码片段、文档内容|Explore/docs-reader SubAgent|执行过程中按需加载|

```
flowchart TD
    Agent[主 Agent]

    Static[静态上下文<br />rules + skills 索引] --> |永远加载| Agent
    Dynamic[动态上下文<br />session 摘要] --> |新对话加载| Agent
    Instant[即时上下文<br />Explore 检索结果] --> |按需加载| Agent

    Agent --> Task[执行任务]

    style Static fill:#e1f5fe
    style Dynamic fill:#fff3e0
    style Instant fill:#f3e5f5
```
**静态上下文**：

|内容|实现|
|-|-|
|项目规范|rules/always/security + constraints|
|能力索引|rules/always/skill-index|
|开发指南|skills/coding-guide|
|知识库|skills/knowledge/patterns + pitfalls|

**动态上下文**：

|内容|实现|
|-|-|
|会话摘要|context/session_*.md|
|任务临时文档|.comate/tmp/|

**分层加载策略**：

|层级|内容|Token|加载方式|
|-|-|-|-|
|L0 元规则|安全红线 + 关键约束|~500|永远加载|
|L1 索引|skill-index + SKILL.md|~500|永远加载|
|L2 详情|step/ + patterns/|2000-3000|按需加载|

### 4.2 Architectural Constraints：不变量约束
**核心问题**：Agent 行为边界是什么？

**边界由人工定义**：

不变量约束的前提是**边界必须由人划定**——AI 在边界内自由发挥，但边界本身不能由 AI 决定。

```
人工职责：定义边界（禁止什么、必须符合什么）
AI 职责：在边界内选择最优实现
```
**什么是不变量？**

绝对不能违反的边界，是维持全局一致性的锚点：

|类别|不变量|验证方式|
|-|-|-|
|安全|SQL 禁止字符串拼接|linter|
|安全|敏感信息禁止入日志|linter + 扫描|
|安全|权限必须校验 UID|代码审查|
|架构|路由前缀必须符合规范|自动化检查|
|契约|接口响应必须包装|linter|

**不变量 vs 微观管理**：

|维度|不变量（正确）|微观管理（错误）|
|-|-|-|
|形式|"禁止 X" / "必须符合 Y"|"必须用 Z 库"|
|AI 自由度|高（方式可选，边界不可破）|低（连实现细节都被规定）|
|维护成本|低（规则稳定）|高（库升级就要更新规则）|

**约束执行**：

|机制|实现|
|-|-|
|确定性 Linter|rules/auto/go-coding-standard|
|人工审查|skills/code-review|
|质量评估|agents/quality-evaluator|

### 4.3 Entropy Management：熵管理
**核心问题**：AI 生成的代码库会积累熵，如何防止系统腐化？

**熵的表现**：

|问题|说明|
|-|-|
|文档脱节|文档与现实不同步|
|命名偏离|命名约定逐渐走样|
|死代码|废弃代码堆积|
|对话退化|长对话中 Agent 注意力分散|

**范围说明**：

原始 Böckeler 框架中的 Entropy Management 特指**对代码库本身的垃圾回收**——由专用 cleanup Agent 定期扫描文档漂移、架构约束违规、过时规范，在代码库层面对抗熵增。我们的实践覆盖了其中的**代码质量**和**知识沉淀**维度，同时将**对话上下文退化**（context window 内的信息稀释）也纳入了熵管理范畴。两者都是真实问题，但层次不同：

|层次|问题|当前实践|
|-|-|-|
|**对话层熵增**|长对话中约束被稀释、Agent 注意力分散|context-manager 对话压缩 ✅|
|**代码库层熵增**|文档漂移、命名偏离、废弃代码堆积|quality-evaluator + knowledge-archiver ✅|
|**Harness 自身熵增**|Rules/Skills 文件过时矛盾（原始定义的核心）|code-review 人工审查 ⚠️ 部分覆盖|

**熵管理机制**：

|机制|实现|说明|
|-|-|-|
|**对话压缩**|context-manager|长对话摘要化，清空上下文|
|**质量评估**|quality-evaluator|评估代码质量，发现问题|
|**测试验证**|unit-test + go test|确保代码可运行|
|**知识沉淀**|knowledge-archiver|识别模式，归档踩坑|

**执行流程**：

```
开发任务 → Checkpoint 验收 → 质量评估 → 测试验证 → 知识沉淀
                ↓
           发现问题 → 回滚修复
```
---

## 五、工程化的本质：保证下限，而非追求上限
> **用强力的 模型 生成准确的内容不算什么，用普通的 模型 生成稳定、准确的内容才是工程化。**
### 5.1 成熟度的量化
不是看"最好的情况下能做多好"，而是看"最坏的情况下能保证多不坏"：

```
成熟度 = 下限稳定性 / 上限天花板

依赖强力模型：上限 95 分，下限 40 分，成熟度 = 0.42
Harness 系统：上限 90 分，下限 80 分，成熟度 = 0.89
```
**L0-L4 评估体系与下限的关系**：

|评估层级|保证的下限|对应的 Harness 机制|
|-|-|-|
|L0 需求理解|方向不偏（MVP ≥60%）|Checkpoint 1 人工确认|
|L1 方案设计|架构不错（MVP ≥70%）|Checkpoint 2 人工确认|
|L2 规范遵循|约束不破（MVP ≥60%）|Rules 不变量 + linter|
|L3 能力执行|工具不空转（MVP ≥75%）|Skills 成功触发|
|L4 代码质量|代码可用（MVP ≥70%）|Checkpoint 3 + go test|

**L2 是下限的核心保障**：L2 低于 MVP，意味着约束层失效，不变量被击穿——这时必须停下来修复 Rules，而不是让 AI 继续往后执行。

### 5.2 为什么"大家都可以用"
|维度|依赖强力模型|Harness 工程化|
|-|-|-|
|**成本**|高（顶级模型贵 5-10 倍）|低（普通模型即可）|
|**稳定性**|低（模型升级可能改变行为）|高（系统约束保证稳定）|
|**可复现**|差（相同 prompt 可能不同结果）|好（约束系统保证一致性）|
|**可迁移**|差（换模型需重新调优）|强（约束系统模型无关）|
|**团队协作**|难（依赖个人调 prompt 技巧）|易（Rules/Skills 是团队共享资产）|

**Harness 如何提升下限**：

|机制|作用|效果|
|-|-|-|
|**检查点**|人在关键节点纠正方向|防止偏离目标太远|
|**不变量**|linter 自动拦截违规|防止输出不可用的代码|
|**模式库**|复用经过验证的方案|避免每次从零思考|
|**知识分层**|精准上下文而非全量灌输|减少无关信息干扰|

**思想实验**：假设明天最强模型下线，只能用能力只有 60% 的模型——依赖强力模型的团队项目瘫痪，而 Harness 工程化的团队通过约束 + 检查点弥补模型能力不足，依然可以稳定交付 80 分的代码。**这才是工程化的价值**：不依赖个别超级个体（无论是人还是模型），通过系统化设计保证稳定产出。

---

## 六、快速适配指南（任意项目 30 分钟启动）
本套实践的通用核心只需最小配置，项目特定内容会随开发自动积累。

### 6.1 最小可用配置（MVP）
```
.comate/
├── rules/always/
│   ├── security/RULE.md         # ✅ 可复用：安全红线（UID校验/SQL禁拼/敏感信息）
│   ├── constraints/RULE.md      # ✏️ 需定制：关键约束（路由前缀/响应格式）
│   ├── skill-index/RULE.md      # ✅ 可复用：Skills 全局索引
│   └── workflow-priority/RULE.md # ✅ 可复用：工作流优先级
├── rules/auto/
│   └── [lang]-coding-standard/RULE.md  # ✏️ 需裁剪：换语言只需替换规范文件
├── skills/
│   ├── dev-workflow/            # ✅ 可直接复用：7步工作流
│   │   ├── SKILL.md             # 流程骨架 + 步骤索引（64 行）
│   │   └── step/                # 详细步骤文档
│   ├── coding-guide/            # ✏️ 需定制：开发规范详解
│   ├── code-review/             # ✅ 可直接复用：语言无关的审查框架
│   ├── unit-test/               # ✅ 可直接复用：Mock+断言规范需适配语言
│   ├── knowledge/               # ✅ 可直接复用：知识库统一入口
│   │   ├── SKILL.md             # 索引入口
│   │   ├── patterns/            # 空目录，开发中自动积累
│   │   ├── pitfalls/            # 空目录，开发中自动积累
│   │   └── projects/            # 空目录，开发中自动积累
│   ├── context-manager/         # ✅ 可直接复用：上下文管理
│   └── README.md                # Skills 详细说明
└── agents/                      # ✅ 可直接复用：SubAgent
    ├── code-explorer.md
    ├── docs-reader.md
    ├── quality-evaluator.md
    ├── test-generator.md
    └── knowledge-archiver.md
```
**启动步骤**：

1. 复制通用 Skills（dev-workflow/code-review/unit-test/knowledge/context-manager）
2. 填写 constraints/RULE.md（路由前缀 + 响应格式 + 模块划分）
3. 填写 coding-guide/SKILL.md（技术栈 + 日志规范 + 数据库使用）
4. 替换编码规范文件（Go → Java/Python/TS 只需换一个文件）

### 6.2 项目特定 vs 通用
|组件|类型|适配成本|
|-|-|-|
|`security/RULE.md`|可复用|直接使用|
|`constraints/RULE.md`|项目特定|~30分钟|
|`skill-index/RULE.md`|可复用|直接使用|
|`dev-workflow/`|可复用|直接使用|
|`coding-guide/SKILL.md`|项目特定|~1小时|
|`code-review/SKILL.md`|可复用|直接使用|
|`knowledge/`|可复用|直接使用|
|`context-manager/`|可复用|直接使用|
|`agents/`|可复用|直接使用|
|`L0-L4 评估体系`|可复用|直接使用|
|`[lang]-coding-standard/RULE.md`|语言特定|~2小时（提炼不变量）|
|`knowledge/patterns/`|项目积累|开发中自动生成|
|`knowledge/pitfalls/`|项目积累|开发中自动生成|
|`context/`|会话积累|对话中自动生成|

---

## 七、工程化实践详解
> **演进过程**：从单点优化到系统化 Harness，逐步覆盖三大支柱。
---

## 7.1 上下文管理（Context Manager）
> **核心问题**：长对话中 Agent 必然退化，需要检查点机制进行上下文压缩。
### 设计思想
**Agent 退化的数学约束**：

|问题|说明|
|-|-|
|信息过载|长对话中，关键约束被稀释|
|误差积累|每轮对话的误差会滚雪球|
|注意力分散|模型"忘记"早期的重要信息|

**解决方案**：

```
长对话 → 摘要化 → 清空 → 新对话（带摘要上下文）
```
### context-manager Skill
**触发条件（****硬编码于 Skill 逻辑中****）**：

|条件|默认值|说明|
|-|-|-|
|对话轮次|20 轮|超过则自动提示整理|
|Token 消耗|50000|超过则自动提示整理|
|用户手动触发|"整理上下文"、"压缩对话" 等关键词||

**执行流程**：

```
检测触发 → 分析对话 → 生成摘要 → 用户确认 → 清空上下文
                              ↑
                        Harness 检查点
```
**摘要内容**：

```
# 会话摘要 - [时间]

## 已完成任务
- [任务名称]：[关键决策]

## 待处理事项
- [ ] [事项]

## 关键上下文
- [需记住的信息]
```
### 与 Harness Engineering 的对应
|Harness 原则|context-manager 实现|
|-|-|
|**检查点机制**|对话过长时主动提示，在关键节点整理|
|**上下文隔离**|清空当前上下文，避免累积退化|
|**人在关键节点验收**|生成摘要后需用户确认才清空|
|**信息传递优化**|摘要保留关键信息，丢弃冗余|

### 使用示例
```
系统：对话已进行 25 轮，建议整理上下文。是否现在整理？
选项：
  - 整理并清空
  - 仅保存摘要
  - 稍后再说
```
### 目录结构
```
.comate/
├── context/                 # 上下文摘要存储
│   ├── README.md
│   └── session_*.md
├── skills/
│   ├── context-manager/     # 上下文管理
│   ├── knowledge/           # 知识库
│   └── ...
```
---

## 7.2 SubAgent 架构
> **核心问题**：主 Agent 上下文膨胀，需要职责拆分和上下文隔离。
### 目录结构
```
.comate/agents/
├── README.md              # 架构说明
├── code-explorer.md       # 代码探索（只读，返回摘要）
├── docs-reader.md         # 文档读取（只读，返回摘要）
├── quality-evaluator.md   # 质量评估（独立执行，返回报告）
├── test-generator.md      # 单测生成（独立执行，返回测试代码）
└── knowledge-archiver.md  # 知识归档（独立执行，返回沉淀建议）
```
### 设计原则
|原则|说明|
|-|-|
|**主 Agent 轻量**|主 Agent 只负责核心决策和用户交互|
|**SubAgent 隔离**|SubAgent 独立执行，返回摘要，不污染主上下文|
|**质量不可妥协**|质量敏感任务（代码生成）必须由主 Agent 执行|
|**结果可验证**|SubAgent 返回结果必须可验证|

### 主 Agent 职责边界
**主 Agent 做三件事，不做记忆**：

|职责|说明|
|-|-|
|**任务分解**|把模糊需求拆成具体子任务，决定先后顺序|
|**路由**|根据上下文判断每步调用哪个 SubAgent|
|**综合**|合并多个 SubAgent 结果，解决矛盾和冗余|

> 主 Agent 不应该"做事"，只应该"调度"。SubAgent 只知道自己那一块，主 Agent 看全局。
```
flowchart TD
    User[用户需求] --> Main[主 Agent]

    Main --> |分解| Tasks[子任务列表]
    Main --> |路由| Route{调用哪个 SubAgent?}

    Route --> |读代码| Explore[code-explorer]
    Route --> |读文档| Docs[docs-reader]
    Route --> |质量评估| QA[quality-evaluator]
    Route --> |生成单测| Test[test-generator]
    Route --> |知识归档| Archive[knowledge-archiver]

    Explore --> |返回摘要| Main
    Docs --> |返回摘要| Main
    QA --> |返回报告| Main
    Test --> |返回测试代码| Main
    Archive --> |返回沉淀建议| Main

    Main --> |综合| Result[最终输出]

    style Main fill:#e1f5fe
    style Result fill:#c8e6c9
```
**为什么代码生成（Step 4）不下放**：

代码生成需要综合前几步的全部上下文（需求 + 方案 + 现有代码结构），主 Agent 已持有这些信息，将其下放给 SubAgent 需要重新传递大量上下文，反而增加损耗。判断标准：

|上下文边界|质量敏感度|推荐|
|-|-|-|
|清晰、可隔离|低|SubAgent 执行|
|需要全局感知|高|主 Agent 执行|

```
flowchart LR
    subgraph 方案A[方案 A: 主 Agent 写代码 ✅]
        A1[主 Agent 持有全部上下文] --> A2[直接写代码]
        A2 --> A3[完成]
    end

    subgraph 方案B[方案 B: 下放给 SubAgent ❌]
        B1[主 Agent 上下文] --> B2[传递大量上下文给 SubAgent]
        B2 --> B3[SubAgent 写代码]
        B3 --> B4[返回结果]
        B4 --> B5[主 Agent 验证]
    end

    style 方案A fill:#e8f5e9
    style 方案B fill:#ffebee
```
**TodoWrite 的定位**：

TodoWrite 是主 Agent 的**注意力辅助工具**，解决的是 context window 内的注意力不足问题，而非跨 context 的状态持久化：

|工具|解决的问题|适用场景|
|-|-|-|
|**TodoWrite**|模型注意力不足，容易遗漏步骤|当前实践（单 context）|
|**Task Tool**|跨 context window 的状态共享与真并行|多 context、长任务|

三个减负机制协同作用，尽可能延长主 Agent 的有效工作范围：

```
flowchart TD
    Problem[主 Agent Context 压力来源]

    Problem --> |历史对话积累| P1[对话层熵增]
    Problem --> |全量代码库信息| P2[信息过载]
    Problem --> |评估/单测细节| P3[任务间干扰]

    P1 --> |解决方案| S1[context-manager<br />文本压缩]
    P2 --> |解决方案| S2[Explore/docs-reader<br />按需检索]
    P3 --> |解决方案| S3[SubAgent 隔离<br />独立上下文]

    S1 --> Result[主 Agent Context 有效工作范围延长]
    S2 --> Result
    S3 --> Result

    style Problem fill:#ffebee
    style Result fill:#e8f5e9
```
```
文本压缩（context-manager）  → 清理历史对话积累
按需检索（Explore SubAgent） → 主 Agent 只看精炼信息
SubAgent 隔离               → 评估/单测不污染写代码上下文
```
### 任务下放评估
|步骤|上下文消耗|质量敏感|下放建议|集成状态|
|-|-|-|-|-|
|Step 1 TODO|小|低|❌ 不下放（需用户交互）|—|
|Step 2 需求解析|中|高|⚠️ 部分下放（docs-reader）|✅ 已集成|
|Step 3 方案设计|大|高|⚠️ 部分下放（code-explorer）|✅ 已集成|
|Step 4 代码生成|大|极高|❌ 不下放（核心任务）|—|
|Step 5 质量评估|中|中|✅ quality-evaluator|✅ 已集成|
|Step 6 单测生成|中|中|✅ test-generator|✅ 已集成|
|Step 7 归档沉淀|中|低|✅ knowledge-archiver|✅ 已集成|

### 调用方式
**显式调用**：

```
Use the code-explorer agent to find reusable prize-sending components.
```
**delegate_subtask 工具**：

```
{
  "agent_type": "Explore",
  "description": "探索发奖组件",
  "query": "查找 service/prize/ 目录下与发奖相关的可复用组件"
}
```
### 上下文收益
|场景|无 SubAgent|有 SubAgent|节省|
|-|-|-|-|
|需求解析|2000 tokens|500 tokens|75%|
|方案设计|3000 tokens|800 tokens|73%|
|质量评估|1500 tokens|600 tokens|60%|
|单测生成|2000 tokens|1000 tokens|50%|
|**总计**|**8500 tokens**|**2900 tokens**|**66%**|

### 与 Harness Engineering 的对应
|Harness 原则|SubAgent 架构实现|
|-|-|
|**职责隔离**|主 Agent 决策 / SubAgent 执行|
|**上下文隔离**|SubAgent 独立上下文，返回摘要|
|**检查点验收**|SubAgent 结果需主 Agent 验证|
|**下限保障**|质量敏感任务由主 Agent 执行|

### 参考资料
* [Claude Code SubAgent Best Practices](https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/)
* [Claude Code Survival Guide 2026](https://www.linkedin.com/pulse/claude-code-survival-guide-2026-skills-agents-mcp-servers-rob-foster-lq9we)

---

## 7.3 Skill 索引化
> **核心问题**：Skill 文件过长，每次加载消耗大量上下文。
### 索引化设计
**问题**：dev-workflow SKILL.md 从 358 行 → 64 行索引 + step 子目录

```
.comate/skills/dev-workflow/
├── SKILL.md           # 64 行：流程骨架 + 步骤索引
└── step/
    ├── 01-todo.md         # TODO 创建详情
    ├── 02-requirement.md  # 需求解析详情
    ├── 03-design.md       # 方案设计详情
    ├── 04-codegen.md      # 代码生成详情
    ├── 05-quality.md      # 质量评估详情
    ├── 06-unittest.md     # 单测生成详情
    └── 07-archive.md      # 归档沉淀详情
```
### 执行方式
|路径|Token 消耗|适用场景|
|-|-|-|
|主 Agent 只看索引|~450|信息量足够时|
|主 Agent 按需加载 step|~450 + 按需|需要详细指引时|

### 索引内容
SKILL.md 包含：

|内容|行数|作用|
|-|-|-|
|触发词 + 核心约束|~20|强制规则|
|步骤索引表|~15|流程骨架|
|入参处理|~10|URL 解析|
|执行模式说明|~10|逐步/自动|
|结束清理|~10|临时文件处理|

**关键**：索引表包含"步骤名 + 关键操作 + SubAgent"，主 Agent 可以直接驱动执行。

### 与 Harness 的对应
|Harness 原则|Skill 索引化实现|
|-|-|
|**精准供弹**|索引 + 按需加载详情|
|**轻量上下文**|主文件 ~450 tokens|
|**检查点验收**|step 文件定义每步的验收点|

---

## 7.4 Rules vs Skills 职责分离
> **核心问题**：混淆"约束"和"指南"，导致常驻规则膨胀。
### 分离原则
|维度|Rules（约束）|Skills（工具）|
|-|-|-|
|**内容**|"禁止 X" / "必须 Y"|"怎么做"|
|**加载**|常驻|按需|
|**长度**|精简（~50 行/文件）|详尽（~100 行/文件）|
|**例子**|"SQL 禁止字符串拼接"|"使用 ORM 参数绑定示例"|

### 本次重构
**重构前**：

```
rules/always/
├── project-guide/RULE.md   # 119 行：混杂约束 + 指南
└── security/RULE.md        # 33 行
```
**重构后**：

```
rules/always/
├── constraints/RULE.md     # 57 行：关键约束（路由/响应/模块）
├── security/RULE.md        # 32 行：安全红线
├── skill-index/RULE.md     # 76 行：Skills 索引
└── workflow-priority/RULE.md

skills/
└── coding-guide/SKILL.md   # 新增：开发指南（技术栈/日志/数据库）
```
### 收益
|指标|重构前|重构后|
|-|-|-|
|rules/always 总行数|152|225（新增索引）|
|常驻 Token（不含索引）|~1100|~630|
|职责清晰度|混杂|分离|
|新人 Onboarding|依赖口口相传|skills/README.md 自说明|

---

## 7.5 与 Anthropic Harness 的关系
> **两套 Harness 定义解决的问题不同，适用场景也不同。**
### Anthropic 的 Harness 关注点
Anthropic 在 *"Effective harnesses for long-running agents"*（2025-11）和 *"Harness design for long-running application development"*（2026-03）中定义的 Harness，专注于**跨多个 context window 的 Agent 自主工作**：

|组件|作用|
|-|-|
|**Initializer Agent**|第一个 context window 专用 prompt，建立环境（init.sh + 初始 git commit）|
|**claude-progress.txt**|跨 context window 的进度追踪文件，新 Agent 启动时快速恢复状态|
|**Feature List**|功能清单作为 ground truth，防止 Agent 过早标记"完成"|
|**Planner-Generator-Evaluator**|三 Agent 架构，职责分离|

### 为什么当前实践未覆盖这些模式
这是有意的设计选择，而非遗漏：

**1. ****任务粒度不同**

|维度|Anthropic 的场景|当前实践的场景|
|-|-|-|
|任务周期|数小时到数天，跨多个对话|单次需求迭代，通常在单次对话内完成|
|自动化程度|Agent 高度自主，减少人工介入|人工 Checkpoint 在关键节点介入|
|状态管理需求|需要持久化进度文件|人工确认本身承担了"状态校验"职责|

**2. ****人工 Checkpoint 替代了自主状态管理**

Anthropic 的 claude-progress.txt + Initializer Agent 解决的核心问题是：**Agent 在新 context window 如何快速恢复上下文**。在当前实践中，这个问题由**人工 Checkpoint** 承担——人在关键节点确认方向，本质上也是一次状态校验和重新对齐。

```
Anthropic 方案：Agent 自主 → 进度文件 → 新 Agent 恢复 → 继续执行
当前实践：Agent 执行 → 人工 Checkpoint → 确认方向 → 下一步
```
**3. ****弱模型的适配约束**

Anthropic 的多 Agent 自主链路对模型的规则遵循能力有较高要求（见第七章模型适配层）。对于弱模型，全自主的多 context window 链路可靠性不足——人工边界确认比依赖模型自我校验更稳定。

### 轻量替代的存在
当前实践并非完全没有跨对话状态管理，而是以更轻量的方式实现：

|Anthropic 方案|当前的轻量替代|差异|
|-|-|-|
|claude-progress.txt（结构化）|context/session_*.md（摘要式）|更依赖人工整理，结构化程度低|
|Feature List（原子化功能清单）|TODO list（任务粒度）|粒度不同，不是完全等价|
|Initializer Agent（专用 prompt）|人工重新描述需求|人工成本更高|

### 演进方向
两套方案不是非此即彼，而是对应不同成熟度阶段：

|阶段|适用场景|推荐方案|
|-|-|-|
|**当前**|弱/中模型 + 单次需求迭代|人工 Checkpoint + session_*.md|
|**进阶**|强模型 + 较长任务周期|引入 claude-progress.txt + Feature List|
|**自动化**|强模型 + 多日跨 context window 任务|完整 Anthropic Harness 模式|

> **核心原则**：人工确认是弱模型阶段的合理策略，而非对自动化的排斥。随着模型能力提升，逐步向 Anthropic 的自主 Harness 演进是自然路径。
---

## 八、模型适配层
> **关键发现**：不同模型对规则的遵循能力存在显著差异，这是工程化实践中必须考虑的因素。
### 8.1 模型差异的发现过程
在实践过程中，我们发现：

|现象|说明|
|-|-|
|规则文件正确|格式、内容、优先级设置都正确|
|但模型不遵循|新窗口对话中，规则不生效|

经过多轮验证，发现根本原因：**模型差异**。

### 8.2 模型能力分层
|模型层级|规则加载|规则理解|规则遵循|工程化成本|
|-|-|-|-|-|
|**强**（如 Claude 4.6）|自动|自然|稳定|低|
|**中**|自动|需简化格式|不稳定|中|
|**弱**|需显式触发|需简化|不稳定|高|

### 8.3 规则遵循的三个层次
```
层次 1：规则加载 —— 规则内容出现在 prompt 中
层次 2：规则理解 —— 模型理解规则含义
层次 3：规则遵循 —— 模型在行动中遵守规则
```
|层次|强模型|弱模型|
|-|-|-|
|1. 规则加载|✅ 自动|❌ 需显式触发|
|2. 规则理解|✅ 自然|⚠️ 需简化格式|
|3. 规则遵循|✅ 稳定|⚠️ 不稳定|

### 8.4 适配策略
**针对强模型**：

* 直接使用，规则自动生效
* 关注 L2（规范遵循）达标率

**针对弱模型**：

* 显式触发：对话开始时说"读取规则"
* 简化规则：核心约束 ≤ 50 行
* 增强检查：更多依赖 linter、代码审查

### 8.5 对 Harness 理论的补充
原有 Harness 理论假设规则可以被模型识别和遵循。实践中发现：

|假设|现实|
|-|-|
|规则自动加载|强模型可以，弱模型需要显式触发|
|模型在边界内自由发挥|需要模型先"看到"边界|
|通过检查点保证质量|检查点依赖正确的执行路径|

**补充原则**：

> **模型适配是 Harness 工程化的前提条件**
> 在选择工程化方案时，必须考虑模型对规则的遵循能力。
### 8.6 实践建议
1. **优先选择规则遵循能力强的模型**
2. **建立显式触发规则的工作习惯**（针对弱模型）
3. **通过 linter、代码审查等手段弥补规则遵循不足**
4. **不追求完美**：接受模型的固有限制，通过系统化手段弥补

---

## 九、总结
### 核心观点
1. **Harness Engineering 三大支柱**：Context Engineering（信息供给）、Architectural Constraints（行为边界）、Entropy Management（熵管理）
2. **限制解决方案空间反而增加生产力**：清晰的边界让 Agent 更快收敛到正确方案
3. **Agent 退化是数学约束**：需要架构层面的应对机制（Checkpoint、熵管理）
4. **不变量约束维持全局一致性**：划定边界（禁止 X/必须 Y），AI 在边界内自由发挥
5. **工程化保证下限，而非追求上限**：成熟度 = 下限稳定性/上限天花板
6. **实践先行，概念跟进**：SubAgent、索引化、熵管理都是先有问题驱动的实践
7. **模型适配是前提条件**：不同模型对规则的遵循能力不同

### 一句话总结
> **Harness = Context（信息供给）+ Constraints（行为边界）+ Entropy Management（熵管理）**
### 实践公式
```
Harness Engineering = 
    Context Engineering（静态 + 动态上下文，按需加载）
    + Architectural Constraints（不变量 + linter + 审查）
    + Entropy Management（对话压缩 + 质量评估 + 测试验证）
    + Checkpoint（人在关键节点验收）
    + Model Adaptation（模型适配）
```
**三大支柱与目录对应**：

|支柱|目录/组件|
|-|-|
|Context Engineering|rules/ + skills/ + knowledge/ + Explore/docs-reader（即时上下文）|
|Architectural Constraints|security + constraints（定义不变量）+ linter + code-review（执行约束）|
|Entropy Management|context-manager（对话层）+ quality-evaluator + knowledge-archiver（代码库层）+ 测试|

---

## 附录
### 理论基础
**理论来源（来源说明）**：

> 文档中"OpenAI 定义的三大支柱"实际上是 **Birgitta Böckeler（ThoughtWorks Distinguished Engineer）对 OpenAI Codex 实践的分析归纳**，发表于 Martin Fowler 博客（2026-02-17），并获 Martin Fowler 本人认可。OpenAI 原文标题为 *"Harness engineering: leveraging Codex in an agent-first world"*，三支柱框架是行业分析师的概念提炼，非 OpenAI 官方规范文档。
* OpenAI Codex 实践文章 (2026-02) — 记录 5 个月、100 万行代码、零人工编写的实践
* Birgitta Böckeler 归纳三大支柱：Context Engineering、Architectural Constraints、Entropy Management（"Garbage Collection"）
* Martin Fowler：*"Harness Engineering 是对 AI 使能软件开发关键部分的有价值框架"*
* 关键洞察：限制解决方案空间，反而增加 Agent 生产力

**Anthropic 的 Harness 定义**：

* Anthropic *"Effective harnesses for long-running agents"* (2025-11) — 专注于**跨多个 context window 的状态持久化**
* Anthropic *"Harness design for long-running application development"* (2026-03) — 多 context window 编排实践
* 核心模式：Initializer Agent → Coding Agents 链路 + claude-progress.txt 进度追踪 + Feature List Ground Truth

**社区实践**：

* Cursor "Towards self-driving codebases" (2026-02) — Planner-Worker 分离
* Vercel AGENTS.md 实证研究 — 被动上下文优于主动检索
* [Harness Engineering 深度解析](https://zhuanlan.zhihu.com/p/2014014859164026634) — Agent 退化不可避免

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
