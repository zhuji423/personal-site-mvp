---
title: "从 Ducc 插件市场拉取"
description: "AI辅助编程插件——“Harness Joding”介绍"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI辅助编程插件——“Harness Joding”介绍.md"
---
AI辅助编程插件——“Harness Joding”介绍

#### 🧑‍🏫 案例作者：[@彭宇豪](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Ducc、Comate
#### 📒 案例概要：AI辅助编程插件，用检查点、上下文隔离和人在关键节点验收，让 AI 辅助开发更可控、更工程化。且同时兼容Ducc和Comate生态，可通过Ducc 插件市场安装。
> **harness**：遵守 Harness Engineering 的实践理念——用检查点、上下文隔离和人在关键节点验收，让 AI 辅助开发更可控、更工程化。
> **joding**：jo 是 9 的谐音，意为 **99 度 Coding**，差一步到百度。AI 能完成大部分研发工作，最后一公里的质量判断和上线决策由人来把关。
> **版本：1.3.6**
---

## 设计哲学
```
flowchart TD
    Root[Harness Joding]
    Root --> 核心理念
    Root --> 方法论融合

    核心理念 --> 检查点机制
    核心理念 --> 上下文隔离
    核心理念 --> 职责分层
    核心理念 --> 知识沉淀

    检查点机制 --> CE1[关键节点人工验收]
    检查点机制 --> CE2[避免AI盲目执行]

    上下文隔离 --> CI1[SubAgent独立上下文]
    上下文隔离 --> CI2[并行调用节省Token]
    上下文隔离 --> CI3[会话复用避免重复分析]

    职责分层 --> RL1[AI负责执行]
    职责分层 --> RL2[人负责决策]

    知识沉淀 --> KP1[Spec/模式/踩坑/归档四分类]
    知识沉淀 --> KP2[索引式按需加载]
    知识沉淀 --> KP3[项目根目录 docs/ 与 .comate 分离]

    方法论融合 --> Harness_Engineering
    方法论融合 --> SDD_RIPER

    Harness_Engineering --> HE1[Sensors检测自纠正]
    Harness_Engineering --> HE2[上下文隔离工程化]

    SDD_RIPER --> SR1[文档前馈提升首次成功率]
    SDD_RIPER --> SR2[结构化状态机约束执行]

    style Root fill:#e3f2fd,stroke:#1976d2
    style 核心理念 fill:#c8e6c9,stroke:#388e3c
    style 方法论融合 fill:#c8e6c9,stroke:#388e3c
    style 检查点机制 fill:#fff9c4,stroke:#f9a825
    style 上下文隔离 fill:#fff9c4,stroke:#f9a825
    style 职责分层 fill:#fff9c4,stroke:#f9a825
    style 知识沉淀 fill:#fff9c4,stroke:#f9a825
    style Harness_Engineering fill:#e1bee7,stroke:#7b1fa2
    style SDD_RIPER fill:#e1bee7,stroke:#7b1fa2
```
Harness Joding 融合了 Harness Engineering 与 SDD-RIPER 两种方法论的优势：

|维度|Harness Engineering 取|SDD-RIPER 取|
|-|-|-|
|质量保障|Computational Sensors 思路——结构化自检清单、落盘验证|Spec 前馈思路——需求文档与技术方案先于代码|
|上下文管理|SubAgent 隔离 + 并行 + 会话复用|知识持久化，跨会话可恢复；docs/ 与框架分离，升级不丢|
|执行约束|检查点机制，关键节点人工确认|RIPER 式分阶段推进，三档执行模式|

---

## 快速开始
```
flowchart TD
    Start([开始]) --> A[安装插件]
    A --> B[项目初始化]
    B --> C[填写业务配置]
    C --> D[开始使用]
    D --> End([完成])

    A --> A1[ducc marketplace install]
    B --> B1[/joding init/]
    C --> C1[架构约束]
    C --> C2[安全红线]
    C --> C3[编码规范]
    D --> D1[自然语言触发]

    style Start fill:#e8f5e9,stroke:#4caf50
    style End fill:#e8f5e9,stroke:#4caf50
    style A fill:#e3f2fd,stroke:#1976d2
    style B fill:#e3f2fd,stroke:#1976d2
    style C fill:#fff3e0,stroke:#f57c00
    style D fill:#f3e5f5,stroke:#7b1fa2
```
### 第一步：安装插件
```
# 从 Ducc 插件市场拉取
ducc marketplace install harness-joding

# 安装指定版本
ducc marketplace install harness-joding@1.3.6
```
### 第二步：项目初始化
启动 Ducc 或 Comate，在对话框中输入：

```
/joding init
```
一行命令，完成所有初始化工作。安装脚本基于 Shell 实现，三端兼容（Windows Git Bash/WSL、macOS、Linux），效果确定可控。

**初始化完成后，项目结构如下：**

```
your-project/
├── CLAUDE.md                    ← Agent 加载入口
├── docs/                        ← 知识库（项目根目录）
│   ├── INDEX.md                 ← 索引文件
│   ├── spec/                    ← 方案文档
│   ├── patterns/                ← 设计模式
│   ├── pitfalls/                ← 踩坑记录
│   └── projects/                ← 功能归档
├── harness-joding.README.md     ← 插件说明
└── .comate/
    ├── rules/                   ← 路由触发规则
    ├── skills/                  ← 11个技能
    ├── agents/                  ← 6个 SubAgent
    ├── context/                 ← 会话摘要与进度记录（运行时生成）
    └── tmp/                     ← 临时文件（不入库）
```
### 第三步：填写业务配置（必做）
初始化后，需要填写以下业务特定文件：

|文件|说明|示例内容|
|-|-|-|
|`skills/coding-guide/constraints.md`|架构约束|路由规范、响应格式、模块划分|
|`skills/coding-guide/security.md`|安全红线|权限校验、输入验证规范|
|`rules/auto/go-coding-standard/RULE.md`|编码规范|Go 语言特定规范（可扩展其他语言）|
|`skills/coding-guide/SKILL.md`|开发指南|技术栈、日志、监控、数据库、缓存|
|`skills/code-review/references/`|审查规则|安全检查清单、性能模式|
|`docs/`|知识库|spec/方案、patterns/模式、pitfalls/踩坑、projects/归档|

**这些文件在安装时提供了结构模板，填入项目实际内容即可（也可让 AI 代劳）。**

### 升级（保留业务配置）
```
# 拉取新版本
ducc marketplace install harness-joding
```
然后在 Ducc 中执行：

```
/joding update
```
**升级策略保护清单**——以下文件永远不会被覆盖：

```
✓ 业务架构约束 (coding-guide/constraints.md)
✓ 业务安全红线 (coding-guide/security.md)
✓ 业务编码规范 (rules/auto/)
✓ 业务知识库 (docs/ 下全部内容：spec/patterns/pitfalls/projects)
✓ 业务定制审查规则 (code-review/references/)
✓ 业务定制开发指南 (coding-guide/SKILL.md)
✓ 长上下文记忆 (context/session_*)
✓ 开发进度记录 (context/PROGRESS_*)
✓ CR处理记录 (context/CR_*)
✓ 运行时临时文件 (tmp/)
```
---

## 双工作流体系
Harness Joding 提供两大核心工作流，覆盖研发全生命周期：

```
flowchart LR
    UserInput[用户输入] -->|包含关键词| Intent{意图识别}

    Intent -->|开发/实现/接口| DevWF[dev-workflow]
    Intent -->|CR/审查意见/处理反馈| CRWF[cr-workflow]
    Intent -->|review/排查| Review[code-review]
    Intent -->|测试/单测| Test[unit-test]
    Intent -->|记住/沉淀/spec/查方案| Docs[docs]
    Intent -->|记录/回顾| Memory[memory]

    style UserInput fill:#e3f2fd,stroke:#1976d2
    style Intent fill:#fff3e0,stroke:#f57c00
    style DevWF fill:#e8f5e9,stroke:#4caf50
    style CRWF fill:#e8f5e9,stroke:#4caf50
    style Review fill:#e8f5e9,stroke:#4caf50
    style Test fill:#e8f5e9,stroke:#4caf50
    style Docs fill:#f3e5f5,stroke:#7b1fa2
    style Memory fill:#fce4ec,stroke:#e91e63
```
### dev-workflow：7 步研发工作流
```
flowchart TB
    subgraph DevWF[dev-workflow 7步研发流程]
        direction TB
        S1[Step 1: 创建 TODO]
        S2[Step 2: 需求解析]
        S3[Step 3: 方案设计]
        S4[Step 4: 代码生成]
        S5[Step 5: 质量评估]
        S6[Step 6: 单元测试]
        S7[Step 7: 知识归档]

        S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7
    end

    style S1 fill:#e8f5e9,stroke:#4caf50
    style S2 fill:#e8f5e9,stroke:#4caf50
    style S3 fill:#e8f5e9,stroke:#4caf50
    style S4 fill:#e3f2fd,stroke:#2196f3
    style S5 fill:#fff3e0,stroke:#ff9800
    style S6 fill:#fff3e0,stroke:#ff9800
    style S7 fill:#fce4ec,stroke:#e91e63
```
|步骤|阶段|输出|SubAgent 协作|
|-|-|-|-|
|Step 1|设计期|TODO 列表（落盘验证）|—|
|Step 2|设计期|需求文档 REQUIREMENT_*.md|docs-reader|
|Step 3|设计期|技术方案 DESIGN_*.md|code-explorer ∥ docs|
|Step 4|编码期|代码实现|—|
|Step 5|质量期|质量评估 QUALITY_*.md|quality-evaluator|
|Step 6|质量期|单元测试|test-generator|
|Step 7|沉淀期|知识归档 + 进度记录|knowledge-archiver|

**三档执行模式**，适配不同场景：

|模式|确认节点|过程文档|适用场景|
|-|-|-|-|
|逐步确认|每步确认|完整输出|重要需求、首次使用|
|自动执行|仅关键节点|完整输出|日常开发|
|快速生成|无确认|跳过|小改动、紧急修复|

### cr-workflow：4 步 CR 意见处理流
```
flowchart TB
    subgraph CRWF[cr-workflow 4步CR处理流程]
        direction TB
        C1[Step 1: 上下文准备]
        C2[Step 2: CR 分析]
        C3[Step 3: 改动执行]
        C4[Step 4: CR 总结]

        C1 --> C2 --> C3 --> C4
    end

    style C1 fill:#e8f5e9,stroke:#4caf50
    style C2 fill:#e3f2fd,stroke:#2196f3
    style C3 fill:#fff3e0,stroke:#ff9800
    style C4 fill:#fce4ec,stroke:#e91e63
```
|步骤|做什么|SubAgent 协作|
|-|-|-|
|Step 1|收集 CR 意见，加载全部中间产物（REQUIREMENT/DESIGN/QUALITY）与进度记录|—|
|Step 2|逐条分析 CR 意见，定位代码，评估影响，P0/P1/P2 优先级排序；默认假定需更新设计文档和单测|cr-helper|
|Step 3|按优先级执行改动：设计文档 → 实现代码 → 单元测试（三者默认执行，Step 2 明确否时才跳过）|—|
|Step 4|生成 CR 记录，检查 docs/spec/ 一致性，更新进度，生成 commit 模板|—|

CR 意见处理是 dev-workflow 之后的常见场景，cr-workflow 与之共享上下文（自动加载 `.comate/tmp/` 中的全部中间产物——REQUIREMENT/DESIGN/QUALITY——以及 `.comate/context/` 中的进度记录），形成完整的 **开发 → CR 反馈 → 修复** 闭环。改动默认同步设计文档和单测，跳过时必须在分析中注明理由。

---

## 自然语言触发
安装完成后，无需记忆复杂命令，用自然语言即可触发各项能力：

```
# 触发 dev-workflow 7 步流程
"帮我实现一个发奖接口"
"新增游戏中心积分查询 API"
"优化这个缓存策略"

# 触发 cr-workflow 4 步流程
"处理一下 CR 意见"
"reviewer 说的这个问题帮我改一下"

# 触发 code-review
"review 一下这段代码"
"帮我排查安全问题"

# 触发 unit-test
"给这个 service 写单测"

# 知识沉淀
"记住这个坑：发奖必须判断 failGids"
"沉淀这个模式：幂等性检查"
"记录这个方案：缓存穿透防护设计"     # 写入 docs/spec/

# 长上下文记忆
"我做了什么"           # 查看当前进度
"继续上次"             # 加载最近的进度记录

# 上下文管理
"整理上下文"           # 压缩会话
"上下文太长了"         # 归档并清空
```
---

## 核心架构
### SubAgent 架构：6 Agent 并行协作
```
flowchart TD
    User([用户]) --> MainAgent[主 Agent]

    MainAgent -->|Step 2| DR[docs-reader]
    MainAgent -->|Step 3 并行| CE[code-explorer]
    MainAgent -->|Step 3 并行| DO[docs]
    MainAgent -->|Step 5| QE[quality-evaluator]
    MainAgent -->|Step 6| TG[test-generator]
    MainAgent -->|Step 7| KA[knowledge-archiver]
    MainAgent -->|CR Step 2| CR[cr-helper]

    MainAgent -->|返回结果| User

    style MainAgent fill:#e3f2fd,stroke:#1976d2
    style CE fill:#c8e6c9,stroke:#388e3c
    style DR fill:#c8e6c9,stroke:#388e3c
    style QE fill:#c8e6c9,stroke:#388e3c
    style TG fill:#c8e6c9,stroke:#388e3c
    style KA fill:#c8e6c9,stroke:#388e3c
    style CR fill:#c8e6c9,stroke:#388e3c
```
|SubAgent|职责|调用场景|特性|
|-|-|-|-|
|`code-explorer`|代码探索与检索|dev-workflow Step 3|与 docs 并行|
|`docs-reader`|文档读取与解析|dev-workflow Step 2|—|
|`quality-evaluator`|质量评估与打分|dev-workflow Step 5|会话复用（返工场景）|
|`test-generator`|测试用例生成|dev-workflow Step 6|会话复用（修复循环）|
|`knowledge-archiver`|知识归档与沉淀|dev-workflow Step 7|—|
|`cr-helper`|CR 意见定位与影响分析|cr-workflow Step 2|—|

**并行执行**：Step 3 的 code-explorer 与 docs 并行收集信息；自动/快速模式下 Step 5+6 质量评估与单测生成并行。

**会话复用**：quality-evaluator 和 test-generator 在返工修复场景可复用上一次会话，避免重复分析，Token 消耗预计减少 ~50%。

**上下文节省**：通过 SubAgent 隔离 + 并行调用，总 Token 从 8500 降至 ~2300，节省约 73%。

### 规则层：路由与触发
```
flowchart LR
    subgraph AlwaysRules[常驻规则（始终加载）]
        WP[workflow-priority<br/>priority: 1000]
        CP[cr-priority<br/>priority: 998]
        SI[skill-index<br/>技能索引]
    end

    subgraph AutoRules[自动规则（编辑时触发）]
        GO[go-coding-standard<br/>globs: **/*.go]
    end

    style AlwaysRules fill:#e3f2fd,stroke:#1976d2
    style AutoRules fill:#e8f5e9,stroke:#388e3c
    style WP fill:#bbdefb,stroke:#1976d2
    style CP fill:#bbdefb,stroke:#1976d2
    style SI fill:#bbdefb,stroke:#1976d2
    style GO fill:#c8e6c9,stroke:#388e3c
```
规则层职责单一化——**只管路由触发逻辑**，规范内容统一归 `skills/coding-guide/` 按需加载。常驻 Token 开销从 ~3600 降至 ~1600，节省 56%。

**CR 意图优先**：当用户输入同时匹配 dev-workflow 和 cr-workflow 触发词时，cr-workflow 优先触发。CR 意图检测覆盖模糊表述（如"按他说的改"、"根据建议调整"），歧义时禁止自行跳过 cr-workflow。

### 知识库：四分类索引式管理
```
flowchart LR
    subgraph KnowledgeBase["docs/"]
        direction TB
        SP["spec/"]
        P["patterns/"]
        I["pitfalls/"]
        R["projects/"]
    end

    SP_desc[方案文档与设计决策]
    P_desc[可复用的设计模式]
    I_desc[踩过的坑及解决方案]
    R_desc[功能归档与项目总结]

    SP -.-> SP_desc
    P -.-> P_desc
    I -.-> I_desc
    R -.-> R_desc

    IDX[INDEX.md<br/>索引文件] --> SP
    IDX --> P
    IDX --> I
    IDX --> R

    style KnowledgeBase fill:#f3e5f5,stroke:#7b1fa2
    style SP fill:#e1bee7,stroke:#7b1fa2
    style P fill:#e1bee7,stroke:#7b1fa2
    style I fill:#e1bee7,stroke:#7b1fa2
    style R fill:#e1bee7,stroke:#7b1fa2
    style IDX fill:#fff9c4,stroke:#f9a825
```
知识库位于项目根目录 `docs/`，与框架 `.comate/` 分离，升级时不受影响。通过 `INDEX.md` 索引按需加载，避免全量灌入上下文。沉淀来源：

* dev-workflow Step 7 自动询问是否记录（必须用户确认后才写入）
* 自然语言触发："记住这个坑"、"沉淀这个模式"、"记录这个方案"
* cr-workflow Step 4 检查 `docs/spec/` 与代码一致性，询问后同步更新

### 记忆机制：上下文压缩与进度恢复
```
flowchart TB
    subgraph AutoRecover[对话开始自动恢复]
        Scan["扫描 context/ 目录"]
        Scan -->|发现 PROGRESS_*.md| Ask[询问是否加载]
        Scan -->|发现 session_*.md| Ask
        Scan -->|无记录| Start[正常开始]
    end

    subgraph ContextManager[上下文管理 context-manager]
        Detect[检测对话长度]
        Detect -->|超过阈值| Compress[压缩归档]
        Detect -->|正常| Continue[继续对话]
        Compress --> Summary[生成摘要]
        Summary --> Store[存入 context/session_*.md]
    end

    subgraph Memory[记忆 memory]
        AutoAsk[Step 7 自动询问]
        Manual[手动触发 记录进度]
        AutoAsk --> Record[记录进度]
        Manual --> Record
        Record --> ProgressFile[context/PROGRESS_*.md]
    end

    AutoRecover -.-> Disk[".comate/context/"]
    ContextManager -.-> Disk
    Memory -.-> Disk

    style AutoRecover fill:#e8f5e9,stroke:#4caf50
    style ContextManager fill:#e3f2fd,stroke:#1976d2
    style Memory fill:#fce4ec,stroke:#e91e63
    style Disk fill:#f5f5f5,stroke:#616161
```
**三层记忆保障**：

1. **自动恢复**：新对话开始时自动扫描 `.comate/context/`，发现进度记录或会话摘要时询问是否加载——断点续传
2. **上下文压缩**：`context-manager` 自动检测对话长度，超过阈值时压缩归档，防止长对话退化
3. **进度记录**：dev-workflow Step 7 自动询问记录进度，生成 `PROGRESS_*.md`，包含任务状态、已完成工作、待办事项、关键决策、**中间产物引用**（REQUIREMENT/DESIGN/QUALITY 文件状态）

```
.comate/context/
├── session_20260401_143022.md    ← 会话压缩摘要（含中间产物引用）
├── PROGRESS_feature_x.md        ← 功能开发进度（含中间产物状态）
├── PROGRESS_bugfix_y.md         ← Bug 修复进度
└── CR_20260402_091511.md        ← CR 处理记录
```
---

## 模板机制：框架升级与业务定制的平衡
```
flowchart TB
    subgraph Framework[框架层（随版本更新）]
        F1[workflow-priority]
        F2[cr-priority]
        F3[dev-workflow / cr-workflow]
        F4[agents]
        F5[evaluation / unit-test]
    end

    subgraph Business[业务层（永不覆盖）]
        B1[coding-guide/constraints.md]
        B2[coding-guide/security.md]
        B3["docs/ (spec/patterns/pitfalls/projects)"]
        B4[coding-guide/SKILL.md]
    end

    Framework -.-> Business

    style Framework fill:#e3f2fd,stroke:#1976d2
    style Business fill:#fff3e0,stroke:#f57c00
    style F1 fill:#bbdefb,stroke:#1976d2
    style F2 fill:#bbdefb,stroke:#1976d2
    style F3 fill:#bbdefb,stroke:#1976d2
    style F4 fill:#bbdefb,stroke:#1976d2
    style F5 fill:#bbdefb,stroke:#1976d2
    style B1 fill:#ffe0b2,stroke:#e65100
    style B2 fill:#ffe0b2,stroke:#e65100
    style B3 fill:#ffe0b2,stroke:#e65100
    style B4 fill:#ffe0b2,stroke:#e65100
```
`.template` 后缀的文件在 `init` 时变为真实文件，`update` 时永不覆盖。这是框架与业务的分界线。

**多语言支持**：内置 Go 编码规范作为示例，其他语言按需添加：

```
# 以 Python 为例
mkdir -p .comate/rules/auto/python-coding-standard
cp .comate/rules/auto/go-coding-standard/RULE.md \
   .comate/rules/auto/python-coding-standard/RULE.md
# 然后编辑 RULE.md，修改 globs 和规范内容
```
---

## 完整目录结构
```
harness-joding/
├── plugin.yaml              ← 插件元信息（市场注册）
├── CLAUDE.md.template       ← Agent 入口模板
├── install.sh               ← init/update 安装脚本
├── CHANGELOG.md
├── docs/                    ← 知识库（项目根目录，与 .comate 分离）
│   ├── INDEX.md             ← 两层索引（一级类别 + 二级文件列表）
│   ├── spec/                ← 方案文档（含 README.md 模板）
│   ├── patterns/            ← 设计模式（init 时创建）
│   ├── pitfalls/            ← 踩坑记录（init 时创建）
│   └── projects/            ← 功能归档（init 时创建）
└── .comate/
    ├── rules/
    │   ├── always/
    │   │   ├── workflow-priority/RULE.md   ← 研发意图路由（可更新）
    │   │   ├── cr-priority/RULE.md         ← CR 意图路由（可更新，优先于 dev-workflow）
    │   │   └── skill-index/RULE.md         ← 技能索引（可更新）
    │   └── auto/
    │       └── go-coding-standard/RULE.md.template ← 编码规范模板
    ├── skills/
    │   ├── dev-workflow/        ← 7 步研发流程（可更新）
    │   ├── cr-workflow/         ← 4 步 CR 处理流程（可更新）
    │   ├── code-review/         ← 5 维代码审查（references/ 不更新）
    │   ├── unit-test/           ← 单测生成（可更新）
    │   ├── docs/                ← 知识库入口（spec/patterns/pitfalls/projects 不更新）
    │   ├── coding-guide/        ← 开发指南（SKILL.md + 子文件不更新）
    │   ├── memory/              ← 进度记忆（可更新）
    │   ├── context-manager/     ← 上下文压缩（可更新）
    │   ├── evaluation/          ← L0→L4 质量评分（可更新）
    │   └── optimize-flow/       ← 工作流优化（可更新）
    ├── agents/                  ← 6 个 SubAgent（全部可更新）
    ├── context/                 ← 运行时生成（session_*/PROGRESS_*/CR_*）
    └── tmp/                     ← 临时文件（不入库）
```
---

## 推荐模型
**claude-sonnet-4-6**（强烈推荐）

弱模型在规则遵循层（尤其是 workflow-priority）存在失效风险。

---

## 总结
Harness Joding 的设计哲学是**"约定优于配置，沉淀优于重复"**：

1. **约定**：双工作流（dev-workflow + cr-workflow）覆盖研发全生命周期，开箱即用
2. **可定制**：业务差异通过模板机制优雅处理，规则层只管路由，规范内容按需加载
3. **可升级**：框架更新不影响业务配置，`/joding update` 一行搞定
4. **可沉淀**：知识库四分类（spec/模式/踩坑/归档）+ 索引式管理，让经验持续积累、按需复用
5. **可恢复**：记忆机制三重保障——自动恢复、上下文压缩、进度记录，断点续传不丢上下文

**真正简单的不是配置的数量，而是逻辑的清晰度。**

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
