---
title: "九、备注"
description: "Agent Engineering实战"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Agent Engineering实战.md"
---
Agent Engineering实战

#### 🧑‍🏫 案例作者：[@彭宇豪](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：项目管理
#### 🔧 使用工具：Comate
#### 📒 案例概要：Agent Engineering实践：基于Zulu构建上下文工程体系，含规则/技能分层、知识库、七步工作流及六层评估体系。
> **前言**
> AI Coding 已不再是新奇的概念验证，而是正在快速演变为可落地的工程实践。尽管大模型的能力边界仍在持续拓展，当前面临的上下文受限、幻觉控制、质量波动等问题终将被更先进的技术所消解，但在这一技术跃迁的窗口期，系统性地探索工程化方法论、沉淀可复用的最佳实践、构建人机协作的标准流程，恰恰是最大化释放 AI 生产力的关键。本方案正是基于 clouddisk-lifeactivity 项目的技术栈与业务场景，对当前阶段 AI 辅助开发进行体系化梳理与规范化定义，以期为团队的持续交付提供可执行、可追踪、可优化的工程蓝图。
---

## 一、背景与问题
### 1.1 现状
个人在 AI 辅助开发时遇到以下问题：

* 使用方法相对碎片化、个人技巧相对分散；
* 没有一个项目级的评估标准，没有一个可参照的实践；

### 1.2 核心需求
有一个**稳定可复现的工程化实践**，能够：

1. 让 AI 充分理解项目上下文（规范、模式、踩坑）
2. 有标准化的开发流程可以遵循
3. 有可量化的质量评估体系
4. 实践可以持续沉淀和迭代

### 1.3 风险认知
> 当前面临的各种问题可能随着 AI 的迭代，都不再是数据。我们做的工程化实践可能也只是一个阶段性的中间产物。
设计原则：**保持灵活，避免过度工程化，关注当下可落地的核心价值**。

---

## 二、工具选型
原则：

> 1. 上下文尽可能精简；
> 2. 构建完善的评分体系；
> 3. 需要人工对阶段性目标进行确认；
> 4. 有自行迭代的机制；
> 5. 可模板化，可稳定复现。
> 
### 2.1 方案对比
|维度|Zulu|Ducc |
|-|-|-|
|CLI 支持|支持 CLI，可做深度上下文注入|支持|
|插件/MCP 支持|支持各种插件和 MCP 配置|支持|
|内部模型接入|原生接入百度内部模型，无合规风险|封装外部模型，存在合规限制|
|内网集成|与内部系统（Ducc、知识库、iCafe）深度集成|有限|
|工程化配置|Rules/Skills 完整体系|支持|
|团队共享配置|MCP 配置可通过项目仓库共享|配置共享受限|
|结论|**选用**|备选|

### 2.2 选型结论
**基于 Zulu，结合 Anthropic 黑客马拉松冠军实践和上下文工程方法论，构建工程化体系。**

选择 Zulu 的核心原因：

* **合规优先**：原生对接百度内部模型，无外部数据泄露风险
* **生态集成**：与 iCafe、知识库、Ducc 等内部系统无缝联动
* **CLI + 插件全支持**：与 Ducc 具备同等的工程化能力，且配置可在团队内共享

##### 方案总结：
**核心设计理念**：

1. **上下文工程** - 精心选择和注入相关的代码、文档、规范，比写复杂的 Prompt 更有效
2. **人工阶段性确认** - 将 AI 协作拆解为可观测、可验收的关键节点，把端到端黑盒生成转变为**风险可控、质量可预期的渐进式交付过程**。

|优点维度|具体优势|说明|
|-|-|-|
|**合规安全**|原生内部模型接入|原生对接百度内部模型，无外部数据泄露风险，满足企业合规要求|
|**生态集成**|与内部系统无缝联动|集成 iCafe、知识库、Ducc 等内部系统MCP，打通研发工作流|
|**架构设计**|两层架构精简高效|Rules（定义"是什么"）+ Skills（提供"怎么做"），Token 消耗低，渐进式披露|
|**Token 优化**|上下文压缩|go-coding-standard 精简为 ~70 行核心规则，编辑时从 ~2500 tokens 降至 ~300，节省 88%|
|**质量保障**|L0-L5 六层评估体系|覆盖需求理解、方案设计、基础合规、能力输出、代码质量、业务价值全链路|
|**失败恢复**|自动化诊断修复|代码生成编译失败、质量评估不通过、测试失败时自动诊断并回退修复|
|**知识沉淀**|持续迭代机制|自动沉淀踩坑记录（pitfalls.md）、可复用模式（patterns.md）、功能归档|
|**开发流程**|7 步结构化工作流|从 TODO→需求解析→方案设计→代码生成→质量评估→单测→归档，标准化全流程|
|**灵活适配**|触发词语义匹配|Skills 通过 description 字段触发词实现语义匹配，适配 IDE 对话框交互模式|

---

## 三、架构设计
### 3.1 两层能力定位
```
┌─────────────────────────────────────────────────────────┐
│ Rules - 定义"是什么"和"应该怎样"          始终/按需生效  │
│ ├── always/：security、project-guide                     │
│ ├── auto/：go-coding-standard（编辑 .go 文件时加载）     │
│ └── requested/：requirement-guide                        │
└─────────────────────────────────────────────────────────┘
          ↓ 约束
┌─────────────────────────────────────────────────────────┐
│ Skills - 提供"怎么做"的可复用能力           按需加载     │
│ ├── code-review/：代码审查能力                           │
│ ├── unit-test/：单测生成能力                             │
│ ├── evaluation/：L0-L5 评估检查清单                      │
│ ├── project/：功能知识归档能力                           │
│ ├── dev-workflow/：结构化开发工作流（6步）                │
│ ├── optimize-flow/：流程优化与复盘                       │
│ └── experience-depositor/：踩坑与经验沉淀                │
└─────────────────────────────────────────────────────────┘
```
* **维度** → Rules / Skills
* **本质** → 轻量级行为约束 / 可复用能力文件夹
* **教 AI** → 遵守什么规则 / 怎么做
* **Token 消耗** → 低（简短规则） / 节省（渐进式披露）

### 3.2 目录结构
```
.comate/
├── rules/
│   ├── always/             # alwaysApply=true，注入系统 Prompt
│   │   ├── project-guide/RULE.md        # 项目概览/路由前缀/响应包装/模块路径
│   │   └── security/RULE.md             # 权限/输入校验/防注入
│   ├── auto/               # alwaysApply=false + globs，文件匹配时加载
│   │   └── go-coding-standard/RULE.md   # 核心硬规则（~70行，编辑 .go 文件时触发）
│   └── requested/          # 按需加载，语义匹配触发
│       └── requirement-guide/RULE.md    # 需求理解检查清单
│
├── skills/
│   ├── code-review/
│   │   ├── SKILL.md                     # 触发词："review"/"帮我看看代码"/"代码审查"
│   │   └── references/
│   │       ├── security-checklist.md
│   │       └── performance-patterns.md
│   ├── unit-test/
│   │   ├── SKILL.md                     # 触发词："写测试"/"生成单测"/"帮我测一下"
│   │   └── references/
│   │       └── mock-patterns.md         # gomonkey 使用模式
│   ├── evaluation/
│   │   └── SKILL.md                     # L0-L5 评估检查清单
│   ├── project/
│   │   ├── SKILL.md                     # 触发词："归档"/"保存功能"/"沉淀一下"
│   │   └── [功能名].md                  # 已归档功能文档
│   ├── dev-workflow/
│   │   └── SKILL.md                     # 触发词："开发"/"实现"/"帮我写"/"做一个"
│   ├── optimize-flow/
│   │   └── SKILL.md                     # 触发词："优化流程"/"复盘一下"
│   └── experience-depositor/
│       └── SKILL.md                     # 触发词："记住这个坑"/"记下来"
│
├── references/             # 全局知识库（核心上下文）
│   ├── patterns.md         # 可复用代码模式（发奖/分布式锁/缓存等）
│   ├── pitfalls.md         # 踩坑记录（CRITICAL/WARN/TIP 分级）
│   ├── database-cache.md   # Redis/MySQL 实例说明和 Key 命名规范
│   └── go-coding-detail.md # Go 编码详细规范+代码示例（~280行，按需查阅）
│
└── tmp/                    # 工作流临时文档（任务完成后清理）
    ├── REQUIREMENT_*.md
    └── DESIGN_*.md
```
### 3.3 知识分层策略
```
┌─────────────────────────────────────────────────────┐
│              上下文注入优先级                         │
│                                                     │
│  L1: Always Rules（每次必带）                        │
│      → security / project-guide                     │
│  L1.5: Auto Rules（文件匹配时加载）                  │
│      → go-coding-standard (globs: **/*.go)          │
│                                                     │
│  L2: 任务相关知识（按需加载）                         │
│      → references/patterns.md                       │
│      → references/pitfalls.md                       │
│                                                     │
│  L3: 技能专属参考（Skill 触发时加载）                 │
│      → skills/*/references/                         │
│                                                     │
│  L4: 临时工作文档（任务周期内）                       │
│      → tmp/REQUIREMENT_*.md                         │
│      → tmp/DESIGN_*.md                              │
└─────────────────────────────────────────────────────┘
```
---

## 四、核心定义
### 4.1 Always Rules + Auto Rules 规范
#### go-coding-standard：Go 编码规范（Auto - 编辑 .go 文件时加载）
来源：[百度 Go 编码规范 v1.3](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/a1zD7CMpKX/AD4lVjdO8PfAC6)

> v2.0 变更：精简为 ~70 行核心硬规则，详细示例移至 `references/go-coding-detail.md`（~280 行），按需加载。
#### security：安全规范
* 所有接口必须校验 uid 归属（防越权）
* 禁止 SQL 拼接，使用 `db.DBHandler2` 参数化查询
* 禁止在日志中打印 token、手机号等敏感信息

### 4.2 全局知识库（references/）
#### patterns.md — 可复用模式库
当前已沉淀 4 个核心模式：

* **统一发奖入口** → `prize.SendPrizeCommon()` — 所有发奖必须走统一入口
* **分布式锁** → `utils.RedisLock()` + defer 解锁，防并发重复执行
* **SetNX 幂等标记** → 接口幂等标记，TTL = 业务允许重试间隔
* **缓存读穿写回** → 先读 Redis，miss 时读 DB 并回填，写时同时更新

#### pitfalls.md — 踩坑记录（分级管理）
* **CRITICAL / C1** → 并发场景必须加分布式锁，不能只依赖 DB 唯一索引
* **CRITICAL / C2** → `failGids` 判断用 `len() > 0`，不能用 `!= nil`
* **CRITICAL / C3** → uid 归属校验缺失会导致越权问题
* **WARN / W1** → gomonkey patch 私有方法需 `-gcflags="-l"`
* **WARN / W2** → 奖品配置读取需检查 nil，避免 panic
* **WARN / W3** → patch 使用完必须 Reset，否则污染其他测试

### 4.3 dev-workflow 工作流（7步结构化开发）


```
用户输入需求（纯文字 / ku链接 / URL）
     ↓
Step 1: 创建 TODO 清单
  → 使用 ask_user_question 询问用户是否创建
  → 用户选择后执行，等待确认再继续
     ↓
Step 2: 需求解析
  → 加载 requirement-guide
  → 使用 ask_user_question 批量澄清模糊项
  → 输出 REQUIREMENT_*.md
  → 等待用户确认再继续
     ↓
Step 3: 方案设计
  → 加载 patterns.md + pitfalls.md
  → 探索 componentization/ 可复用组件
  → 输出 DESIGN_*.md（含关键决策表）
  → 等待用户确认再继续
     ↓
Step 4: 代码生成
  → 逐文件生成，自检三项规范
  → 路由变更单独列出提示人工添加
  → 编译失败时自动诊断并修复
  → 等待用户确认再继续
     ↓
Step 5: 质量评估（加载 evaluation skill）
  → L1 方案设计检查（6项）
  → L4 代码质量检查（5项）
  → 负向指标扫描（幻觉/冲突/返工风险）
  → 结论为 ❌ 时自动回到 Step 4
  → 等待用户确认再继续
     ↓
Step 6: 单测生成（加载 unit-test skill）
  → 参考 action/uinfo/uinfo_test.go
  → 参考 service/componentization/buysendprizes_test.go
  → 测试失败时自动诊断并修复
  → 等待用户确认再继续
     ↓
Step 7: 自动沉淀（加载 project skill）
  → 7a: 自动识别 → 用户确认后写入 patterns.md / pitfalls.md
  → 7b: 功能归档（用户确认后创建）
     ↓
清理 .comate/tmp/ 临时文件（询问用户后执行）
```
预期效果：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aaa5f93c409e4867b12967cfd4bf2a7a&docGuid=Hbfm-w1U5nGH4o "")
### 4.4 单测规范
```
// Mock 库：github.com/agiledragon/gomonkey/v2
// 断言库：github.com/smartystreets/goconvey/convey

func TestXxx(t *testing.T) {
    Convey("描述", t, func() {
        // 公有方法 Mock
        patch := gomonkey.ApplyMethod(
            reflect.TypeOf(&SomeStruct{}), "PublicMethod",
            func(_ *SomeStruct, ...) (...) { return mockResult },
        )
        defer patch.Reset()

        // 私有方法 Mock（需要 -gcflags="-l"）
        patch2 := gomonkey.ApplyPrivateMethod(...)
        defer patch2.Reset()

        result, err := target.DoSomething()
        So(err, ShouldBeNil)
        So(result, ShouldEqual, expected)
    })
}

// 运行命令（私有方法 Mock 必须加 gcflags）
// go test -gcflags="-l" ./action/xxx/...
```
---

## 五、评估体系（L0-L5）
### 5.1 六层评估总览
```
L0 需求理解 ──→ L1 方案设计 ──→ L2 基础合规 ──→ L3 能力输出 ──→ L4 代码质量 ──→ L5 业务价值
   需求准确率      技术选型         Rules 覆盖      Skills 成功     代码通过率      开发提效
```
注：**MVP**** **即** ****Minimum Viable Practice****，****最低可行标准**

* **L0 需求理解** → 需求理解准确性 / MVP ≥60% / 达标 ≥75% / 优秀 ≥80% / 每次生成后人工（10s）
* **L1 方案设计** → 方案设计合理性 / MVP ≥70% / 达标 ≥80% / 优秀 ≥85% / 每次生成后人工（10s）
* **L2 基础合规** → Rules 规范遵循 / MVP ≥60% / 达标 ≥80% / 优秀 ≥85% / code-review 后人工
* **L3 能力输出** → Skills 执行效果 / MVP ≥75% / 达标 ≥85% / 优秀 ≥90% / 每周统计
* **L4 代码质量** → 生成代码质量 / MVP ≥70% / 达标 ≥85% / 优秀 ≥90% / go test + 人工
* **L5 业务价值** → 实际业务收益 / MVP ≥30% / 达标 ≥40% / 优秀 ≥50% / 每月统计

### 5.2 负向指标（发现问题根源）
* **幻觉率** → 编造不存在的 API/函数 / 警告值 <10% / 严重值 <5%
* **规则冲突次数** → 多规则给出矛盾指导 / 警告值 <5% / 严重值 <2%
* **Token 浪费率** → 未使用的 references Token / 警告值 <30% / 严重值 <20%
* **返工率** → 需要返工的任务占比 / 警告值 <15% / 严重值 <10%

### 5.3 评估记录方式
使用飞书表格，每次 AI 生成后约 10 秒完成记录：

|日期|任务|L0 需求|L1 方案|L2 合规|L4 质量|返工|备注|
|-|-|-|-|-|-|-|-|
|03-16|新增 API|7/10|6/10|8/10|9/10|否|需求边界不清晰|
|03-17|优化性能|6/10|7/10|7/10|8/10|是|方案需调整|

**评分标准**：1-3（不合格需返工）| 4-5（不合格可部分用）| 6-7（及格 MVP）| 8-9（良好达标）| 10（优秀）

### 5.4 分阶段目标
```
Phase 1（Rules 基础建设）
  L0: ≥ 60%, L2: ≥ 60%
        ↓
Phase 2a（核心开发技能）
  L0: ≥ 60%, L1: ≥ 70%, L2: ≥ 70%, L3: ≥ 75%, L4: ≥ 70%
        ↓
Phase 2b（评估反馈技能）
  L0: ≥ 70%, L1: ≥ 75%, L2: ≥ 75%, L3: ≥ 80%, L4: ≥ 75%, L5: ≥ 30%
        ↓
Phase 3（持续优化）
  全面达标：L0: ≥ 75%, L1: ≥ 80%, L2: ≥ 80%, L3: ≥ 85%, L4: ≥ 85%, L5: ≥ 40%
        ↓
持续优化（优秀）
  L0: ≥ 80%, L1: ≥ 85%, L2: ≥ 85%, L3: ≥ 90%, L4: ≥ 90%, L5: ≥ 50%
```
---

## 六、持续优化机制
### 6.1 反馈闭环
```
每次 AI 生成
     ↓
人工评估（约10秒）→ 记录到如流知识库表格
     ↓
每周汇总（约30分钟）→ 分析共性问题
     ↓
优化 Rules / Skills / references
     ↓
下次生成质量提升
     ↓
每月全面评估（约2小时）→ 生成改进计划
```
### 6.2 知识沉淀机制
**自动沉淀**（dev-workflow Step 6 自动执行）：

* 发现可复用模式 → 追加到 `references/patterns.md`
* 发现踩坑 → 追加到 `references/pitfalls.md`（CRITICAL/WARN/TIP 分级）

**功能归档**（用户确认后执行）：

* 重要功能实现 → 创建 `.comate/skills/project/[功能名].md`
* 更新 SKILL.md 中的功能索引

**规则迭代**：

* 每周评估数据 → 识别 AI 频繁犯的错误 → 补充/更新 Rules
* 负向指标触发 → 检查 references 是否冗余 → 精简 Token 消耗

---

## 七、实施计划
* **Phase 1** → always Rules（2个）+ auto Rules（1个）+ requirement-guide + evaluation-guide + 知识库基础 / 10h
* **Phase 2a** → code-review + unit-test + 小范围试用 / 7h
* **Phase 2b** → evaluation 检查清单 + 评估记录表格建立 / 5h
* **Phase 3** → dev-workflow + optimize-flow Skills + requested 规则补充 + 持续优化 / 6h
* **总计** → 28h（建议预留20%缓冲 → 34h）

### 风险与应对
* **人工评估成本高** → 研发人员负担 → 简化流程
* **评估主观性强** → 结果不一致 → 明确评分标准，定期校准
* **AI 迭代使实践过时** → 实践需要更新 → 保持灵活，定期复盘淘汰过时内容
* **requirement-guide 效果不明确** → 需求理解仍不准确 → 人工验证 20+ 场景，迭代优化

---

## 八、当前项目实践快照
### 已实现（当前状态）
```
✅ .comate/rules/always/    - 2个规范（security/project-guide）
✅ .comate/rules/auto/      - 1个规范（go-coding-standard，~70行核心规则 + 280行详细参考）
✅ .comate/rules/requested/ - 1个（requirement-guide）
✅ .comate/skills/          - 7个（code-review/unit-test/evaluation/project/dev-workflow/optimize-flow/experience-depositor）
✅ .comate/references/      - patterns.md（4个模式）+ pitfalls.md（10条记录）+ database-cache.md + go-coding-detail.md
✅ 已归档功能               - skills/project/prize-send.md（发奖能力）
```
### 核心可复用组件清单
已在 `service/componentization/` 沉淀的通用组件（新功能开发前必查）：

* `combogroup/` — 拼团组合
* `membership/` — 会员
* `pointloot/` — 积分抽奖
* `lottery.go` — 抽奖
* `componentization_prize.go` — 组件化发奖
* `prize/send_prize_mgr_service.go` — 统一发奖入口 `SendPrizeCommon`

---

# 九、备注
### 9.1 方案迭代记录
> 本方案经过多轮审查和实际落地验证后持续完善：
#### 9.1.1. 架构演进：三层 → 两层
* **原方案：** 

采用 Rules → Skills → Commands 三层架构，其中 Commands 提供 `/dev`、`/review` 等 CLI 快捷入口。

* **问题**：

Commands 使用 `/command` 语法，该触发范式为 Claude Code CLI 设计。迁移到 Zulu（IDE 插件）后，用户通过对话框交互，不会主动输入 `/dev`。触发机制不可靠。

* **改进**：

将 Commands 逻辑下沉到 Skills，通过 `description` 字段的触发词实现语义匹配，适配 IDE 对话框模式。5 个 command 的迁移映射：

1. `/dev` (dev.md) → `skills/dev-workflow/SKILL.md`（新建）
2. `/review` (review.md) → `skills/code-review/SKILL.md`（合并）
3. `/test` (test.md) → `skills/unit-test/SKILL.md`（合并）
4. `/save` (save.md) → `skills/project/SKILL.md`（合并）
5. `/optimize-flow` (optimize-flow.md) → `skills/optimize-flow/SKILL.md`（新建）

删除 `commands/` 目录及全部 5 个文件。

#### 9.1.2. Token 优化：go-coding-standard 瘦身
**改进**：

* RULE.md 精简为 ~70 行核心硬规则（9条红线禁止事项 + 必须遵守条款）
* 详细说明和 Good/Bad 代码示例移到 `references/go-coding-detail.md`（~280 行），仅在 code-review 或主动查阅时加载
* **Token 节省：~88%**（每次 Go 文件编辑从 ~2500 → ~300 tokens）

#### 9.1.3. 冗余文件清理
* 删除 `CLAUDE.md`（根目录），有价值增量合并到 `project-guide/RULE.md`
* 消除 `.claude/` → `.comate/` 迁移后的残留路径引用

#### 9.1.4. 失败恢复机制增强
`dev-workflow` 六步工作流增加失败处理：

* Step 3（代码生成）：编译失败时自动诊断并修复
* Step 4（质量评估）：结论为 ❌ 时自动回退到 Step 3
* Step 5（单测生成）：测试失败时自动诊断并修复

#### 9.1.5. 开发流程Dev-WorkFlow优先级提高
新增Rule确保dev-workflow优先级最高。

### 9.2. 后期规划
### 9.2.1. Sub Agent
多子Agent各司其职，减少主Agent上下文。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
