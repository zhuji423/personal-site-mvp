---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "AI coding 新范式：Harness Engineering 下的 BSP 实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI coding 新范式：Harness Engineering 下的 BSP 实践.md"
---
AI coding 新范式：Harness Engineering 下的 BSP 实践

#### 🧑‍🏫 案例作者：[@杨轶男](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：项目管理、开发、测试、研发全流程
#### 🔧 使用工具：iCode、Comate、Codex、Ducc
#### 📒 案例概要：Harness Engineering 是通过系统化工程环境设计，让AI Agent规范稳定交付代码的工程范式。
## 背景：
当用 Claude Code 或者 Cursor，写一个稍微有点复杂的项目。

前半段可能顺风顺水，模型表现得让人觉得，AI马上就要碾压式地取代我了。

然后，到了某个时间点，它开始犯一些奇怪的错误。

忘了之前做过的决定。

甚至直接说"已完成"，但功能跑起来完全不对。

于是，人类工程师开始怀疑，是自己 Prompt 写得差？还是模型本来就不够强？

但其实，问题的关键在于，模型没有记忆，但任务有连续性。

而 Harness Engineering 提供了一种解决方案。





## Harness Engineering 是什么
* AI 领域 又双叒 有新概念了：**Harness Engineering**

> OpenAI 在 2026 年 2 月发布了 Codex 工程范式 复盘文章，该文章公开团队为期 5 个月的极限工程实验成果，OpenAI 官方拆解 Harness 如何支撑交付，这篇文章的重点**不是 AI 写了多少代码**，而是**怎么让 Agent 稳定干活、怎样把软件工程环境改造成适合 Agent 工作的系统。**完整阐述了“人类掌舵、Agent 执行”的 Coding 范式，定义了 Harness Engineering 在 AI Coding 的方法论。
> 
> Harness Engineering（驾驭工程）是 2026 年 AI 工程化领域最火爆的新范式，标志着软件工程从"人类写代码"向"人类设计AI工作系统"的根本转变。OpenAI、Anthropic、腾讯等巨头已开始正式采用这一术语。


**标题：Harness Engineering: Leveraging Codex in an Agent-First World**

**           驾驭工程：在智能体优先的世界中释放 Codex 的潜力**

发布时间：2026-02-11，作者：Ryan Lopopolo

* 原文链接：[https://openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/) 默认会跳转：[https://openai.com/zh-Hans-CN/index/harness-engineering/](https://openai.com/zh-Hans-CN/index/harness-engineering/)

### **常见误读**
### **文章重点**
* 只看到 0 手写代码
* 只关心模型有多强
* 把它当成一次炫技
* 工程环境怎么改
* 规则和反馈怎么建
* Agent 怎么稳定交付



### 1.1. 金句摘抄
* 我们唯一真正稀缺的资源：人类的时间和注意力。
* **agent-first** 的世界里，工程师最重要的能力，正在从**编码能力**转向 **Harness Engineering**（驾驭 Agent 的工程能力）。



### 1.2. 背景与实验规模
OpenAI 的一支 3 人工程团队（后扩展至 7 人），用 **5 个月时间**、以**零行手写代码**的方式，构建并发布了一个有真实用户的内部 Beta 产品：

|指标|数据|
|-|-|
|代码规模|~100 万行（应用逻辑、基础设施、文档、工具）|
|PR 数量|~1,500 个，全部由 Codex 生成|
|人均日产出|**3.5 个 PR / 工程师 / 天**|
|工程师人数|3 人起，扩展到 7 人后吞吐仍在增加|
|构建时效|估算约为手写代码的 **1/10 时间**|

核心约束：**全程没有人类直接写代码**——所有代码、测试、CI 配置、文档、可观测性组件均由 Codex 生成。



### 1.3. AI Coding 范式的三阶段演进
|阶段|时间|名称|核心内容|
|-|-|-|-|
|第一阶段|2023–2024|**Prompt 工程**|学怎么"问"模型，Few-Shot、角色扮演等各种技巧|
|第二阶段|2025|**Context 工程**|光会写 Prompt 不够，你得设计模型"看到什么"。RAG、MCP、Memory、工具调用…|
|第三阶段|2026|**Harness 工程**|当 AI Agent 大规模进入生产，如何构建机制驾驭它？|

## Harness Engineering 为了让 AI 更规范稳定运行，他们做了哪些事？
*  单次 prompt 的质量并非关键，系统化的工程环境才是 Agent 稳定交付的基础。



### 2.1. 上下文工程：**如何让 AI 知道该做什么**
> **核心原则：给 Agent 一张地图，而不是一本千页手册。**
问题：最初尝试"一个大 AGENTS.md"的方式，结果失败——上下文被挤占、重要信息被忽略、文件迅速腐烂、无法机械校验。

最终方案：分层文档体系

* 一个约 **100 行**的简短 `AGENTS.md` 作为"导航地图"
* 指向 `docs/` 目录下更深层的设计规范、执行计划、领域约定
* Agent 按需获取信息，而不是一次性加载全部

```
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── db-schema.md
├── product-specs/
│   ├── index.md
│   ├── new-user-onboarding.md
│   └── ...
├── references/
│   ├── design-system-reference-llms.txt
│   ├── nixpacks-llms.txt
│   ├── uv-llms.txt
│   └── ...
├── DESIGN.md
├── FRONTEND.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
└── SECURITY.md
```
**关键原则**：

* **渐进式披露（Progressive Disclosure）**：Agent 从稳定的小入口出发，被教导去哪里找深层信息，而不是被一次性淹没。
* **任何 Agent 无法在上下文中访问到的知识，等同于不存在**。Slack 讨论、Google Docs 中的决策，对 Agent 来说和三个月后入职的新人一样——不可见。
* **计划是一等公民（Plans as first-class artifacts）**：小改动用轻量临时计划，复杂工作使用带进度和决策日志的执行计划，active/completed/tech-debt 全部版本化存入仓库。



### 2.2. 架构约束：**如何让 AI 不做错误的事**
> **核心原则：**用 Linter 代替 Prompt 说教
问题：文档写了规范，但 Agent 不一定遵守；人工 review 规范合规性成本太高。

解法：把规范变成机械约束，强制执行

* 每个业务域划分为**固定的分层结构**（Types → Config → Repo → Service → Runtime → UI），依赖方向严格单向
* 所有业务都会用到的公共能力（auth、connectors、telemetry、feature flags）通过**唯一的 Providers 接口**进入，其他路径一律禁止
* 所有规则通过**自定义 Linter****（Codex 自己写的）** 和**结构性测试**机械执行，而非依赖 Prompt 约定
* "Taste invariants"（品味不变量）：结构化日志、Schema/Type 命名规范、文件大小限制、平台可靠性要求——全部静态 lint 检查
* **Lint 的错误信息本身就是修复指引**，直接注入到 Agent 上下文，Agent 看到报错就知道怎么修

> 在人工主导的工程中，这些规则会让人觉得繁琐。但在 Agent 工程中，它们是**乘法器**：一旦编码，就同时作用于每一行代码。
这些约束通过自定义 Linter（静态代码分析工具）和结构性测试来机械地执行——而这些 Linter 本身也是由 Codex 生成的。



### 2.3. 可观测性接入 + 闭环反馈：让 AI 能"看见"应用的运行状态
> **核心原则：把人类的注意力留给真正重要的决策。**
问题：代码吞吐量增加后，瓶颈变成了人类 QA 容量——人看不过来。人工 review 成为瓶颈；每次都要人介入效率极低。

解法：把应用的 UI、日志、指标直接"接给" Codex 看，构建 Agent 自驱的完整闭环

|接入能力|技术方案|
|-|-|
|UI 验证|将 **Chrome DevTools Protocol** 接入 Agent 运行时，创建处理 DOM 快照、截图、导航的 Skills|
|应用隔离启动|应用按 **git worktree** 启动，每个变更拥有完全隔离的实例（含独立日志/指标）|
|日志查询|**LogQL**（Vector → Victoria Logs）|
|指标查询|**PromQL**（Vector → Victoria Metrics）|
|追踪查询|**TraceQL**（Vector → Victoria Traces）|

**效果**：Agent 可以执行如下任务而无需人类介入：

* 复现 bug、录制失败视频、实现修复、验证修复、录制成功视频、开 PR
* "确保服务启动在 800ms 以内"、"这四条关键用户旅程中没有 span 超过两秒"

单次 Codex 运行可在**人类睡觉时连续工作 6 小时以上**。

```
工程师给出任务描述
    ↓
Codex 执行，开 PR
    ↓
Codex 本地审查自己的变更
    ↓
向其他 Codex 实例（本地 + 云端）请求特定视角审查
    ↓
响应人类/Agent 反馈，循环迭代
    ↓
所有 Agent 审查者满意 → 合并
    ↓
（人类可以参与审查，但不是必须的）

```
这套流程被称为 **Ralph Wiggum Loop**（出自外部文章引用）。关键结果：**几乎所有 review 工作推向 Agent-to-Agent 处理**，人类注意力被保留给真正需要判断的决策。



**可观测性基础设施**的接入是另一个关键。Agent 被连接到日志、指标、链路追踪系统，以监控应用性能并在隔离环境中复现 Bug。OpenAI 甚至将 **Chrome DevTools Protocol** 接入 Agent 的运行时，让 Agent 可以截图、操作 DOM、自主导航应用界面，从而独立修复视觉 Bug。



### 2.4. 熵管理（Entropy Management）
> **核心原则：技术债要每日偿还，而不是让它积累成雪崩。**
完全的 Agent 自治会引入**熵**（Entropy）——系统的无序度。

AI Agent 会复现代码仓库中已存在的模式，哪怕是不好的模式。随着时间推移，代码库会悄悄漂离最初的架构设计，产生越来越多的"聪明但有害"的代码。

OpenAI 最初的应对方式是每周拿出 20% 的时间（通常是周五全天）清理“AI 残渣”。不出所料，那并不具备可扩展性。

**最终解决方案**：将黄金原则直接编码进仓库，并构建**自动化的持续清理流程**：

* 后台 Codex 任务定期扫描代码库，检测偏离"黄金标准"的地方
* 自动更新质量评分，开出针对性的重构 PR
* 大多数清理 PR 在**一分钟内**被审查和自动合并

技术债被当作"高利贷"每日偿还，不断地以小额贷款的方式偿还债务，总比让债务不断累积，再痛苦地一次解决要好得多。



## Harness Engineering 的本质
![](/personal-site-mvp/img/doc-placeholder.svg "")
OpenAI 的这次实践给出了一个清晰的结论：

> **"建软件依然需要纪律，但纪律体现在脚手架上，而不是代码上。"** *Building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code.*
让 Agent 运行得规范稳定的关键，不是更好的 Prompt，而是更好的**环境设计**——包括知识组织、架构约束、工具可观测性、反馈闭环和持续熵管理。



## BSP 项目结合 Harness Engineering  范式实践
### 4.1. 上下文工程（Context Engineering）
#### 4.1.1. `.comate/rules/` —— AI 专用的架构导航地图
**我们做了什么：**

项目根目录下存在 `.comate/rules/` 目录，包含两个规则文件：

* `default.mdr`：**项目全局开发契约**，约 100 行，涵盖：
    * 项目概览与核心技术栈
    * 模块架构与层次结构
    * 四层文件结构规范（`api.go` / `service.go` / `form.go` / `data.go`）
    * 统一错误处理、表单验证、响应封装模式
    * 命名与目录结构规范
    * 代码质量工具链配置

* `detection.mdr`：**开发框架搭建规则**，描述了脚手架下载、代码清理、Goland IDE 配置的完整 SOP 流程

**对照 Harness 范式：**

这正是 Harness 上下文工程中推荐的 **"AGENTS.md 模式"**——用一份简洁的规则文档作为"导航地图"，告诉 AI 这个项目的架构意图、代码模式和开发约定。不同之处在于我们用的是 `.mdr` 格式（Comate 的规则格式），但本质完全一致。

> **Harness 原话**：*"给 Agent 一张地图，而不是一本千页手册。"*
> **我们的实践**：`default.mdr` 恰好 100 行左右，精准覆盖 AI 最需要的约定，没有冗余。
---

#### 4.1.2. `.comate/specs/` —— 结构化的需求 Spec 体系
**我们做了什么：**[Spec使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/Hb6OQz5Jc7/vmavFXxkR55VvD?t=mention&mt=doc&dt=doc)

项目中建立了 `.comate/specs/` 目录，每个复杂功能都有独立的 Spec 子目录，包含：

* `doc.md`：详细需求文档（含架构方案、影响文件、实现细节、边界条件）
* `tasks.md`：可追踪的任务清单（`- [x]` 勾选式）
* `summary.md`（部分功能）：实现总结

已有的 Spec 案例：

* `sla_all_apis/`：BigNAT SLA All 和 DNS SLA All 接口
* `batch_query_optimization/`：批量查询优化
* `dns_cluster_network_flow_all/`：DNS 集群网络流量全量查询

**对照 Harness 范式：**

这对应 Harness 上下文工程的**"任务级上下文注入"**。每次让 AI 完成一个复杂功能时，不是直接给一句话需求，而是先准备好：

1. 架构方案（AI 知道该怎么做）
2. 影响文件清单（AI 知道该改哪里）
3. 实现细节（AI 知道具体模式）
4. 边界条件（AI 知道什么情况要特殊处理）

Spec 文档本身就是精心设计的 Context，把 AI 需要"看到的东西"提前准备好。

---

#### 4.1.3. DeepWiki —— 活的项目文档体
**我们做了什么：**

项目维护了完整的 DeepWiki 文档体系（15 篇），覆盖：

|文档|内容|
|-|-|
|`项目概述.md`|架构图、技术栈、核心模块|
|`BGW设备检测.md`|BGW 专项文档|
|`BIGNAT设备检测.md`|BigNAT 专项文档|
|`DNS设备检测.md`|DNS 专项文档|
|`SLA检测分析.md`|SLA 分析逻辑|
|`数据模型.md`|核心数据结构|
|`配置说明.md`|配置体系说明|
|`开放API.md`|API 接口文档|
|`Hawk集成.md` / `NSC集成.md` / `Yunti集成.md`|外部系统集成|

**对照 Harness 范式：**

DeepWiki 是 Harness 上下文工程中的**"唯一真相来源（Single Source of Truth）"**。当 AI 需要了解某个模块的背景知识，DeepWiki 是它应该读的地方，而不是扫描整个 codebase。

---

### 4.2. 架构约束（Architectural Constraints）
#### 4.2.1. 四层文件结构 —— 强制模式约束
**我们做了什么：**

每个 API 模块强制遵循四文件结构：

`/internal/apps/apis/open/apis/{module}/{feature}/
├── api.go      # 路由定义和 HTTP 处理器
├── service.go  # 核心业务逻辑
├── form.go     # 请求参数绑定和验证
└── data.go     # 数据模型定义
`

这个约束写进了 `default.mdr`（AI 规则）中，并通过历史代码和 Spec 文档（如 `sla_all_apis/doc.md` 中的"影响文件"列表）持续强化。

**对照 Harness 范式：**

这是 Harness 架构约束中最核心的实践——**通过结构性规则，让 AI 没有选择，只能按规范来**。AI 每次新建一个功能模块，自然就会生成四个文件，而不是自由发挥。

> **Harness 原话**：*"让规则成为 Agent 的反射动作，而不是事后审查。"*
---

#### 4.2.2. golangci-lint —— 代码质量的硬性门禁
**我们做了什么：**

项目配置了 `.golangci.yml`，启用了多个 linter：

|Linter|作用|
|-|-|
|`gofmt` + `goimports`|代码格式统一|
|`stylecheck` + `revive`|代码风格检查|
|`errcheck` + `errorlint`|错误处理规范|
|`govet`|静态分析|
|`gocyclo`|圈复杂度控制（≤30）|
|`lll`|行长度限制（≤160字符）|
|`gosimple`|代码简化建议|

这些检查通过 CI 流水线（`ci.yml` 中的 `check: reuse: TASK`）在每次提交时自动执行。

**对照 Harness 范式：**

Linter 是 Harness 约束层的核心工具。它不是建议，而是**门禁**——不符合规范的代码无法合入。更重要的是，linter 错误信息本身就是 AI 的修复指引。当 AI 生成的代码违反了圈复杂度限制，linter 会告诉它哪里复杂度超标，AI 可以据此自行重构，无需人工干预。

---

#### 4.2.3. 统一服务创建模式 —— 可预测的代码结构
**我们做了什么：**

所有 Service 遵循统一的构造和调用模式：

`// 标准 Service 构造函数
func NewService(ctx *gin.Context) *Service { ... }

// 标准业务入口
func (s *Service) Handle() error { ... }

// 链式处理方法（按顺序执行）
s.validateParams()
s.fetchData()
s.processData()
s.buildResponse()`

**对照 Harness 范式：**

统一模式让 AI 的输出高度可预测。AI 不会每次都"发明"一种新的 Service 写法，而是按照固定模板填充业务逻辑。这降低了代码审查成本，也让后续的熵管理更容易自动化。

---

#### 4.2.4. CI 流水线 —— 三环境构建约束
**我们做了什么：**

`ci.yml` 定义了三个独立 Profile：

```
build_sandbox  → make env-sandbox   # 沙盒环境
build_test     → make env-test      # 联调环境
build_prod     → make env-prod      # 生产环境
```
每个 Profile 都触发 `check: reuse: TASK`，自动执行代码质量检查。`Makefile` 支持完整的构建、测试、打包、清理流程，测试命令和覆盖率统计。

**对照 Harness 范式：**

CI 流水线是 Harness 约束层的**外部执行器**——即使 AI 生成的代码绕过了本地检查，CI 也会在代码合入前进行最终拦截。

---

### 4.3. 闭环反馈（Recursive Feedback Loop）—— 我们做对了哪些
#### 4.3.1. Spec + Tasks —— 任务驱动的反馈闭环
**我们做了什么：**

`.comate/specs/` 下的每个功能都有 `tasks.md`，记录了细粒度的子任务和完成状态。以 `sla_all_apis/tasks.md` 为例：

```
- [x] 任务1：创建 BigNAT SLA All 接口目录和基础文件结构
    - 1.1: 创建目录
    - 1.2: 创建 api.go
    - 1.3: 创建 data.go
    - 1.4: 创建 form.go
    - 1.5: 创建 service.go
- [x] 任务2：实现核心业务逻辑
    ...
- [x] 任务6：接口测试和验证
    - 6.1: 验证路由注册
    - 6.2: 测试功能
    - 6.3: 验证异常处理

```
**对照 Harness 范式：**

这是 Harness 闭环反馈中的**"检查点机制"**。AI 每完成一个子任务就更新状态，如果某个任务出错，可以回溯到最近的正确检查点重试，而不是从头开始。这也是评论区里有人提到的"checkpoint 机制"——防止 Agent 跑偏。

---

#### 4.3.2. iCode CR 流程 —— 人类在闭环中的角色
**我们做了什么：**

通过 iCode 的 Code Review 机制，所有 AI 生成的代码都经过人工审查才能合入。

**对照 Harness 范式：**

这对应 Harness 闭环中的**"人类在最终节点确认"**——大部分验证由 CI 和 Linter 自动完成，人类只在最关键的合入节点做最终判断，效率和质量兼顾。

---

### 4.4. 效率提升
|指标|数据|
|-|-|
|代码规模|+4.1K|
|人均日产出|**8 个 API接口需求 / 工程师 / 天**|
|构建时效|估算约为手写代码的 **1/10 时间**|

---

### 还可以加强的地方
1. **失败日志机制**：当 AI 生成的代码不符合预期时，将错误场景和修复方式回写到 `.comate/rules/` 中，让同类错误不再发生第二次
2. **自动化测试覆盖**：Makefile 中已有测试框架，可以为关键逻辑增加更多单元测试，让 CI 反馈更快
3. **Spec 模板化**：将 `.comate/specs/` 的文档格式固化成模板，减少每次写 Spec 的成本

Anthropic 也发布有相关思考-*参考资料*：

* 建立与 AI 协作的思维底层逻辑，掌握 4D 框架 [课程原视频](https://anthropic.skilljar.com/ai-fluency-framework-foundations)  [bilibili 熟肉](https://www.bilibili.com/video/BV13WcQzQEDx/?spm_id_from=333.1387.favlist.content.click&vd_source=a072108a8241ae7d9c7b1dda48aefa19)
* 将 4D 框架落地，把 AI 变成你特定领域的专家 [课程原视频](https://anthropic.skilljar.com/introduction-to-claude-cowork)



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
