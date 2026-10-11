---
title: "注册 Marketplace"
description: "多 Skills 组织、共享与 Plugin 设计"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\多 Skills 组织、共享与 Plugin 设计.md"
---
多 Skills 组织、共享与 Plugin 设计

#### 🧑‍🏫 案例作者：[@闫世锋](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：其他、通用
#### 🔧 使用工具：Claude
#### 📒 案例概要：本文档核心阐述如何通过Plugin系统解决多Skills管理中的三大痛点：共享资源失控、引用关系脆弱和分发成本高。Plugin通过集中管理共享文档、声明式依赖和统一路径（如）实现高效共享与可靠引用。同时，文档定义了高质量Skill的五个标准：功能流程化、触发精准、能自适配、边界清晰、案例充分。Plugin的组件（Hooks、MCP Server、Agent、LSP Server）进一步赋能Skill，使其具备自动触发、调用外部工具、异步处理和深度代码分析等高级能力，从而提升整体效能。
Skills 数量少的时候，放在 `.claude/skills/` 下没有问题。但超过 5 个之后，三类问题会同时出现：

**共享资源失控**：`testing-anti-patterns.md` 被四个 Skill 引用，改一处要同步四次。格式化脚本被复制粘贴进每个 Skill 目录，版本开始分叉。

**引用关系脆弱**：Skill A 依赖 Skill B 的某个文档，用了 `@../skill-b/reference.md` 这种相对路径。目录一重组，全断。

**分发成本高**：13 个 Skill 想给团队用，要手动复制 13 个目录，还要确保依赖关系没搞错。更新一个文件，通知所有人手动替换。

Plugin 系统同时解决这三个问题。

---

## Plugin 解决的核心问题：共享与引用
### 问题 1：多个 Skill 共用同一份文档
没有 Plugin 时：

```
skill-a/
├── SKILL.md
└── testing-standards.md   ← 副本 1

skill-b/
├── SKILL.md
└── testing-standards.md   ← 副本 2（已经和副本 1 不同步）

skill-c/
├── SKILL.md
└── testing-standards.md   ← 副本 3
```
有了 Plugin，共享文档放根目录，所有 Skill 通过 `${CLAUDE_PLUGIN_ROOT}` 引用：

```
my-plugin/
├── docs/
│   └── testing-standards.md   ← 唯一来源
├── scripts/
│   └── validate.sh             ← 唯一来源
└── skills/
    ├── skill-a/SKILL.md        ← 引用 ${CLAUDE_PLUGIN_ROOT}/docs/testing-standards.md
    ├── skill-b/SKILL.md        ← 同上
    └── skill-c/SKILL.md        ← 同上
```
改一次，所有 Skill 同步生效。

### 问题 2：Skill 之间的依赖声明
跨 Skill 引用有两种正确方式：

**方式 A：声明依赖关系（推荐）**

```
<!-- executing-plans/SKILL.md -->

**Required workflow skills:**
- **my-plugin:brainstorming** - REQUIRED: 执行计划前必须先完成设计
- **my-plugin:using-git-worktrees** - REQUIRED: 创建隔离工作区后再开始
```
这是声明式约束，不是建议。Claude 读到 `REQUIRED` 标记时会强制调用对应 Skill。

**方式 B：在计划文件中内嵌调用指令**

```
<!-- docs/plans/2026-03-01-login-design.md -->

> **For Claude:** REQUIRED SUB-SKILL: Use my-plugin:executing-plans to implement this plan task-by-task.
```
当 Claude 读取该计划文件时，自动触发 `executing-plans` Skill。

> [!WARNING]
> 不要用 `@../other-skill/SKILL.md` 跨目录引用。路径依赖一旦目录重组就会断掉。跨 Skill 依赖只用 `plugin-name:skill-name` 的命名空间方式声明。
### 问题 3：共享脚本的归属规则
```
my-plugin/
├── scripts/                      ← 被 2 个及以上 Skill 使用 → 放这里
│   ├── format.sh
│   └── validate.py
└── skills/
    ├── skill-a/
    │   ├── SKILL.md
    │   └── skill-a-only.sh       ← 只有 skill-a 用 → 放 Skill 自己目录
    └── skill-b/
        └── SKILL.md
```
在 Skill 内引用共享脚本，用环境变量，不要硬编码路径：

```
<!-- skills/code-review/SKILL.md -->
审查完成后格式化代码（将 <target-file> 替换为实际文件路径）：
${CLAUDE_PLUGIN_ROOT}/scripts/format.sh <target-file>
```
```
<!-- skills/test-generator/SKILL.md -->
生成测试后格式化（将 <target-file> 替换为实际文件路径）：
${CLAUDE_PLUGIN_ROOT}/scripts/format.sh <target-file>
```
> [!NOTE]
> `${CLAUDE_PLUGIN_ROOT}` 是 Claude Code 注入的环境变量，指向 Plugin 根目录的绝对路径，无论安装在哪里都正确。Skill 内的 `<target-file>` 是占位符，Claude 执行时会根据当前任务上下文替换为实际文件路径。如果是 Hook 场景，用 `$ARGUMENTS`——Hook 触发时系统自动注入触发事件的文件路径参数。
---

## Plugin 结构全景
```
enterprise-plugin/
├── .claude-plugin/
│   └── plugin.json              ← 唯一必须的元信息
│
├── skills/                      ← Skills（新格式）
│   ├── brainstorming/
│   │   └── SKILL.md
│   ├── systematic-debugging/
│   │   ├── SKILL.md
│   │   ├── root-cause-tracing.md
│   │   ├── defense-in-depth.md
│   │   └── find-polluter.sh
│   └── test-driven-development/
│       ├── SKILL.md
│       └── testing-anti-patterns.md
│
├── agents/                      ← Subagents
│   ├── security-reviewer.md
│   └── performance-tester.md
│
├── hooks/                       ← 自动化钩子（重点）
│   └── hooks.json
│
├── scripts/                     ← 共享脚本
│   ├── format.sh
│   └── validate.py
│
├── docs/                        ← 共享文档
│   └── coding-standards.md
│
└── README.md
```
> [!WARNING]
> `skills/`、`agents/`、`hooks/` 必须在 **Plugin 根目录**，不能放进 `.claude-plugin/` 里。`.claude-plugin/` 只存放 `plugin.json`。
### plugin.json
```
{
  "name": "my-toolkit",
  "description": "团队开发工作流工具箱",
  "version": "1.0.0",
  "author": {
    "name": "Team Name",
    "email": "team@example.com"
  },
  "license": "MIT",
  "keywords": ["tdd", "debugging", "review"]
}
```
`name` 字段成为命名空间。这里是 `my-toolkit`，调用时是 `/my-toolkit:code-review`。

---

## 什么是好的 Skill
一个 Skill 质量的五个维度：

---

### 标准 1：功能丰富，把任务流程化
一个 Skill 对应一类完整任务，不是一个步骤。用户调用它，得到的是从输入到输出的完整路径，而不是"你还需要再做几件事"。

**差的设计**：`code-review` Skill 只说"检查代码质量"，用户调用后拿到一堆建议，还要自己决定怎么输出、存在哪里、格式是什么。

**好的设计**：`code-review` Skill 覆盖完整流程：

```
## Checklist

为每项创建 TodoWrite 任务，按顺序完成：

1. **读取目标文件** — 理解上下文、语言、框架
2. **执行审查** — 安全漏洞、性能问题、代码质量三个维度
3. **按 @template.md 填写报告** — 格式统一，包含文件行号
4. **执行 @scripts/validate.sh** — 验证报告格式完整性
5. **输出结论** — 通过 / 需要修改，列出必改项
```
流程化的 Skill 把"一类任务"的最佳实践固化下来，用户不需要每次重新决策执行路径。复杂任务拆成有序步骤，通过 Checklist + TodoWrite 强制执行，不允许跳过。

> [!TIP]
> 判断 Skill 功能是否足够完整：用户调用后，在不追加任何提示的情况下，AI 能否独立完成该任务并产出预期结果？如果用户还需要补充说明"然后你还要做 X"，说明 Skill 覆盖不够。
---

### 标准 2：触发时机精准，需要时出现，不需要时不干扰
Skill 的 `description` 字段决定 AI 在什么情况下自动调用它。写得太宽泛，Skill 会被误触发；写得太窄，用户需要时 Skill 不出现。

**触发过宽（差）**：

```
---
name: data-validate
description: 用于数据处理
---
```
"数据处理"太模糊，用户问任何跟数据相关的问题都可能触发它，包括不该触发的场景。

**触发过窄（差）**：

```
---
name: data-validate
description: 仅用于验证 JSON Schema 格式是否符合 draft-07 规范
---
```
场景太具体，用户说"帮我校验一下这个数据结构"时，AI 可能判断不匹配而跳过。

**精准触发（好）**：

```
---
name: data-validate
description: 当用户需要校验数据格式、检查字段完整性、验证数据是否符合预期结构时使用。
适用：JSON/CSV/表格数据的结构校验、字段类型检查、必填项验证。
不适用：数据转换、数据清洗、业务逻辑校验。
---
```
触发条件描述用户的**意图**，不是技术实现。把适用场景和不适用场景都写清楚，AI 能准确判断该不该调用。

> [!NOTE]
> 在 `using-superpowers` 或类似的入口 Skill 里，可以声明"1% 原则"：只要有 1% 的概率某个 Skill 适用，就必须调用它去检查。这把触发阈值调低，避免 AI 因为"感觉不需要"而跳过有价值的 Skill。
---

### 标准 3：有学习能力，能自适配
好的 Skill 不是死板的脚本，而是能根据上下文调整执行策略。这体现在两个层面：

**层面 A：根据项目上下文自适配**

Skill 在执行前主动探索环境，而不是假设一切都是固定的：

```
## 执行前

1. 读取 `CLAUDE.md` 或 `README.md`，了解项目技术栈和规范
2. 检查是否存在 `docs/plans/` 目录，判断是否有进行中的任务
3. 读取近 5 次 git commit，理解当前开发方向

根据探索结果，调整后续步骤的侧重点。
```
**层面 B：支持显式覆盖，允许用户修正**

Skill 声明哪些规则是 Strict（不可跳过），哪些是 Flexible（可根据上下文调整）：

```
## Skill 类型

**Strict 部分**（必须执行，不允许跳过）：
- 执行前必须读取项目规范文件
- 输出必须包含文件路径和行号

**Flexible 部分**（可根据项目上下文调整）：
- 报告的详细程度
- 审查维度的优先级排序
```
用户可以在调用时追加"这次只关注安全漏洞"，Skill 的 Flexible 部分响应这个指令，Strict 部分不受影响。

---

### 标准 4：边界清晰，能做什么不能做什么都写明
能力边界模糊的 Skill 有两个后果：AI 在该用时不调用，或在不该用时乱用。

每个 Skill 都应该在 frontmatter 或开头明确声明边界：

```
---
name: api-test-generator
description: 根据接口定义生成测试用例，覆盖正常流程、边界值和异常场景
---

## 适用范围

**能做：**
- 根据 OpenAPI/Swagger 文档生成测试用例
- 覆盖正常输入、边界值、必填项缺失、类型错误等场景
- 生成可直接运行的测试代码（pytest / Jest / JUnit）

**不做：**
- 执行测试（只生成代码，不运行）
- 分析已有测试的覆盖率
- 生成 UI 测试或 E2E 测试

**前置条件：**
- 需要接口定义文件（OpenAPI YAML/JSON 或接口描述文档）
- 如果没有接口文档，先用 brainstorming Skill 梳理接口设计
```
边界清晰的 Skill 还能引导用户到正确的工具：

```
## 超出范围时

- 需要执行测试 → 使用 `my-plugin:run-tests`
- 需要分析覆盖率 → 使用 `my-plugin:coverage-analysis`
- 没有接口文档 → 先调用 `my-plugin:brainstorming`
```
---

### 标准 5：使用案例充分，覆盖典型场景
文档写得再好，不如几个具体例子直接。使用案例至少覆盖三类场景：

**典型场景**（最常见的用法）：

```
## 示例 1：审查新增功能代码

用户：帮我审查 src/auth/login.py 的代码

预期执行路径：
1. 读取 login.py
2. 检查 SQL 注入、密码明文存储、Session 管理三个安全维度
3. 输出报告到当前目录 code-review-YYYY-MM-DD.md
```
**边界场景**（输入不完整或有歧义时的处理）：

```
## 示例 2：用户没有指定文件

用户：帮我做代码审查

预期行为：
不要猜测，提问：
"请告诉我要审查哪个文件或目录？是整个 PR 还是某个具体文件？"
```
**拒绝场景**（超出边界时的行为）：

```
## 示例 3：用户要求执行测试

用户：帮我审查代码并跑一下测试

预期行为：
完成代码审查后说明：
"代码审查已完成。运行测试不在本 Skill 范围内，请使用 my-plugin:run-tests。"
```
案例写法参考 `examples/` 目录，把真实输入、预期输出、边界处理都覆盖到：

```
my-skill/
├── SKILL.md
└── examples/
    ├── typical-case.md      ← 典型用法
    ├── edge-case.md         ← 边界输入
    └── out-of-scope.md      ← 超出范围的处理
```
---

### 五个标准的关系
|标准|解决的问题|主要体现在|
|-|-|-|
|功能完整|Skill 能独立完成一类任务|Checklist、流程化步骤|
|精准触发|该用时出现，不该用时不打扰|frontmatter description|
|自适配|不同项目/上下文下都能正确执行|执行前探索、Strict/Flexible 声明|
|边界清晰|AI 和用户都清楚能做什么|适用范围、超出范围引导|
|案例充分|降低误用，提供参考|examples/ 目录|

这五个标准没有优先级之分，缺少任何一个都会导致 Skill 在实际使用中出现问题。功能完整但触发时机差，用户找不到它；边界清晰但没有案例，用户不知道怎么用；案例多但不自适配，换个项目就失效。

---

## Plugin 如何让 Skill 变得更好
单个 Skill 本质上是一份 Markdown 文档。它能做的事情取决于 AI 的理解和执行——没有外部工具，没有自动触发，没有跨任务状态。

Plugin 的各个组件给 Skill 套上了一层能力外壳，让同一份 Skill 文档在 Plugin 环境下表现出完全不同的能力上限。

### Hooks：把触发时机从手动变成自动
Skill 默认需要显式调用，Hook 把 Skill 相关逻辑绑定到系统事件，不再依赖任何人主动触发：

|Skill 能力|没有 Hook|有 Hook|
|-|-|-|
|代码格式化|用户每次提醒"记得格式化"|`PostToolUse(Write|Edit)` 自动执行|
|上下文恢复|用户每次重新交代背景|`SessionStart` 自动检查未完成任务|
|关键决策存档|对话压缩后丢失|`PreCompact` 自动保存到文件|
|安全检查|偶尔跑偶尔忘|`PostToolUse` 每次写文件后必跑|

**对五个标准的提升**：精准触发（标准 2）从依赖 description 判断，升级为事件驱动的确定性触发。

完整事件列表、Hook 类型和配置示例见 [HOOK参考](https://code.claude.com/docs/zh-CN/hooks)。

---

### MCP Server：给 Skill 接上外部工具
Skill 文档里能描述的操作，受限于 Claude Code 内置工具集。需要查数据库、调外部 API、读取专有格式文件时，Skill 本身无能为力。

Plugin 捆绑 MCP Server 后，Skill 可以直接调用这些能力：

```
// .mcp.json
{
  "mcpServers": {
    "db-query": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"]
    },
    "api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"]
    }
  }
}
```
```
<!-- skills/data-validate/SKILL.md -->

## 执行步骤

1. 用 db-query 工具查询目标表的 Schema 定义
2. 对比用户提供的数据结构与 Schema
3. 用 api-client 工具调用校验服务做业务规则验证
4. 输出校验报告
```
这个 Skill 单独存在时只能做静态分析；放进 Plugin 后，接上 MCP Server，能实时查库、调接口，做真正的动态校验。

**对五个标准的提升**：功能丰富（标准 1）从"AI 能力范围内"扩展到"任何可以用 MCP 封装的外部能力"。

---

### Agent：把复杂验证委托出去
Skill 执行到复杂的验证或分析步骤时，主流程会被阻塞。Plugin 的 Agent 组件允许把这些任务交给专门的子代理异步处理：

```
<!-- agents/security-reviewer.md -->
---
name: security-reviewer
description: 专注于代码安全审查，检测注入漏洞、认证缺陷、敏感信息泄露
---

你是一名安全专家。收到代码文件后，执行以下检查：
1. SQL/命令注入漏洞
2. 认证和授权绕过风险
3. 硬编码密钥和敏感信息
4. 不安全的依赖

输出结构化的安全报告，包含漏洞级别（Critical/High/Medium/Low）和修复建议。
```
```
<!-- skills/code-review/SKILL.md -->

## 步骤 3：安全审查

将目标文件交给 security-reviewer agent 执行安全检查。
等待结果后，合并进总审查报告。
```
`code-review` Skill 不需要自己内置安全知识，专职 Agent 处理这部分，主流程继续。多个 Skill 可以共享同一个 Agent。

也可以用 Hook 的 `agent` 类型，在特定事件后自动触发 Agent 验证：

```
"PostToolUse": [{
  "matcher": "Write",
  "hooks": [{
    "type": "agent",
    "command": "对刚写入的文件 $ARGUMENTS 执行安全检查，发现 Critical 级别问题立即阻断并报告"
  }]
}]
```
**对五个标准的提升**：自适配（标准 3）从单一 AI 判断，升级为专职子代理的深度分析；功能完整（标准 1）通过职责分离实现，主流程不膨胀。

---

### LSP Server：给 Skill 接上实时代码智能
Skill 在分析代码时，默认只能看到文件内容，看不到类型信息、引用关系、编译错误。Plugin 的 LSP Server 组件给 Skill 提供语言服务器级别的代码理解能力：

```
// .lsp.json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": { ".go": "go" }
  }
}
```
接入 LSP 后，Skill 执行过程中 Claude 能实时看到：

* **即时诊断**：每次写文件后立刻看到编译错误和 lint 警告
* **类型信息**：变量的实际类型，不需要猜
* **引用关系**：找到所有调用某个函数的位置
* **跳转定义**：追踪接口实现，理解继承关系

一个 `refactoring` Skill 如果没有 LSP，只能做文本替换；有了 LSP，能做真正的符号级重命名，不会遗漏跨文件引用。

**对五个标准的提升**：自适配（标准 3）从阅读代码文本，升级为理解代码语义。

---

### 共享资源：让 Skill 能力不随时间衰退
单个 Skill 如果把所有依赖内嵌在自己目录里，随着项目规范变化，各个 Skill 之间会逐渐不同步。Plugin 的共享资源层保证所有 Skill 始终引用同一份权威来源：

```
my-plugin/
├── docs/
│   ├── coding-standards.md      ← 所有 Skill 引用同一份规范
│   └── security-checklist.md    ← 安全审查 Skill 和 review Skill 共用
├── scripts/
│   ├── format.sh                ← 多个 Skill 的格式化脚本不再各自维护
│   └── validate-schema.py       ← 数据校验逻辑唯一来源
└── skills/
    ├── code-review/SKILL.md     ← 引用 ${CLAUDE_PLUGIN_ROOT}/docs/coding-standards.md
    ├── test-generator/SKILL.md  ← 引用同一份规范
    └── data-validate/SKILL.md   ← 引用 ${CLAUDE_PLUGIN_ROOT}/scripts/validate-schema.py
```
规范文件更新一次，所有 Skill 同步生效。这不只是工程便利，而是保证多个 Skill 在执行时依据的是一致的标准，不会出现 `code-review` 用旧规范、`test-generator` 用新规范的割裂。

**对五个标准的提升**：功能完整（标准 1）和边界清晰（标准 4）获得一致性保障；案例充分（标准 5）中的 examples 也可以放进共享目录，多个 Skill 复用。

---

### 能力叠加的效果
把上面几个组件叠加起来，一个原本只有 Markdown 文档的 Skill 会变成什么样：

```
原始 Skill（纯文档）
  → 接入 MCP Server    → 能调用外部工具和数据库
  → 接入 LSP Server    → 理解代码语义而非只读文本
  → 配置 Hooks         → 关键步骤自动触发，不依赖手动调用
  → 挂载 Agent         → 复杂子任务委托专职代理，主流程不膨胀
  → 共享资源层         → 引用的规范和脚本始终是最新版本
```
不是每个 Skill 都需要全部组件。一个简单的文档整理 Skill 可能只需要 Hooks；一个数据分析 Skill 可能需要 MCP + LSP；一个完整的开发工作流 Skill 可能用到全部。Plugin 的价值在于这些能力**按需组合**，而不是全部强制开启。

---

## Hooks 完整参考
### Hooks 配置
`hooks/hooks.json`：

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/save-context-snapshot.sh"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "prompt",
            "command": "检查当前项目是否有未完成的 docs/plans/ 计划文件，如果有，提示用户是否继续上次的工作"
          }
        ]
      }
    ]
  }
}
```
### 可用事件完整列表
|事件|触发时机|典型用途|
|-|-|-|
|`PreToolUse`|Claude 使用任何工具前|权限检查、前置验证|
|`PostToolUse`|工具成功执行后|格式化、lint、自动测试|
|`PostToolUseFailure`|工具执行失败后|错误记录、回滚|
|`SessionStart`|会话开始时|加载上下文、检查未完成任务|
|`SessionEnd`|会话结束时|保存状态、生成摘要|
|`PreCompact`|对话历史压缩前|保存关键决策记录|
|`UserPromptSubmit`|用户提交提示时|注入上下文、格式化输入|
|`SubagentStart`|Subagent 启动时|初始化子任务环境|
|`TaskCompleted`|任务标记完成时|验证、通知|

### Hook 类型
`command`：执行 shell 脚本

```
{
  "type": "command",
  "command": "${CLAUDE_PLUGIN_ROOT}/scripts/run-tests.sh"
}
```
`prompt`：让 Claude 评估上下文并响应（用 `$ARGUMENTS` 获取触发事件的参数）

```
{
  "type": "prompt",
  "command": "分析刚刚写入的文件 $ARGUMENTS，如果检测到安全风险（SQL 注入、硬编码密钥），立即警告"
}
```
`agent`：运行带工具的 Agentic 验证器，处理复杂校验任务

```
{
  "type": "agent",
  "command": "执行完整的代码审查流程，检查 $ARGUMENTS 是否符合团队编码标准"
}
```
### 用 Hooks 强化 Skill 调用的实际场景
**场景 1：每次写文件后自动格式化**

```
"PostToolUse": [
  {
    "matcher": "Write|Edit",
    "hooks": [{ "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh $ARGUMENTS" }]
  }
]
```
`code-review` Skill 里不再需要手动说"记得格式化"——Hook 自动处理。

**场景 2：会话开始时恢复上下文**

```
"SessionStart": [
  {
    "hooks": [{
      "type": "prompt",
      "command": "检查 docs/plans/ 目录下是否有状态为 in-progress 的计划文件，有则加载并告知用户当前进度"
    }]
  }
]
```
跨会话继续任务时，AI 自动恢复上次的工作状态，不需要用户手动交代背景。

**场景 3：压缩前保存决策记录**

```
"PreCompact": [
  {
    "hooks": [{
      "type": "command",
      "command": "${CLAUDE_PLUGIN_ROOT}/scripts/save-decisions.sh"
    }]
  }
]
```
长对话被压缩前，把关键架构决策写入文件，压缩后不丢失。

> [!NOTE]
> Hook 脚本必须有执行权限：`chmod +x scripts/format.sh`。脚本第一行必须有 shebang：`#!/bin/bash`。路径必须用 `${CLAUDE_PLUGIN_ROOT}`，不要硬编码绝对路径。
### 分发和安装
### Marketplace（推荐）
在 GitHub 建一个仓库，放 `marketplace.json`：

```
{
  "name": "my-marketplace",
  "plugins": [
    {
      "name": "my-toolkit",
      "version": "1.0.0",
      "source": "https://github.com/yourname/my-toolkit"
    }
  ]
}
```
用户安装：

```
# 注册 Marketplace
/plugin marketplace add yourname/my-marketplace

# 安装 Plugin
claude plugin install my-toolkit@my-marketplace

# 更新
claude plugin update my-toolkit
```
### 安装范围
|范围|配置文件|适用场景|
|-|-|-|
|`user`（默认）|`~/.claude/settings.json`|个人所有项目可用|
|`project`|`.claude/settings.json`|通过 Git 共享给团队|
|`local`|`.claude/settings.local.json`|项目特定，gitignored|

```
# 安装到项目范围，团队克隆后自动可用
claude plugin install my-toolkit@my-marketplace --scope project
```
### 本地开发测试
```
# 加载本地 Plugin
claude --plugin-dir ./my-toolkit

# 同时加载多个
claude --plugin-dir ./my-toolkit --plugin-dir ./another-plugin
```
## 验证清单
创建完成后逐项检查：

**结构**

- [ ] `.claude-plugin/plugin.json` 存在，`name` 字段已填写
- [ ] `skills/`、`agents/`、`hooks/` 在 Plugin 根目录（不在 `.claude-plugin/` 内）
- [ ] 至少一个 `skills/xxx/SKILL.md` 存在，frontmatter 用 `---` 包围

**共享资源**

- [ ] 被多个 Skill 引用的文档放在 `docs/` 或根目录
- [ ] 共享脚本放在 `scripts/`
- [ ] 所有脚本路径用 `${CLAUDE_PLUGIN_ROOT}` 而非硬编码

**Hooks**

- [ ] Hook 脚本有执行权限（`chmod +x`）
- [ ] Hook 事件名称大小写正确（`PostToolUse` 不是 `postToolUse`）
- [ ] 使用了 `${CLAUDE_PLUGIN_ROOT}` 变量

**Skill 质量**

- [ ] SKILL.md 有 Checklist（步骤强制有序）
- [ ] 声明了 Skill 类型（Strict 或 Flexible）
- [ ] 跨 Skill 依赖用 `plugin-name:skill-name` 声明，没有用路径引用

**测试**

- [ ] `claude --plugin-dir . --debug` 能正常加载，无报错
- [ ] 主要 Skill 命令能调用



> [https://code.claude.com/docs/zh-CN/hooks](https://code.claude.com/docs/zh-CN/hooks)
> [https://code.claude.com/docs/zh-CN/plugins-reference](https://code.claude.com/docs/zh-CN/plugins-reference)
> [Skills 调用顺序实现机制](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/yGJxMCCQ-f/jCxoMp0ODWlHAI?t=mention&mt=doc&dt=doc)
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
