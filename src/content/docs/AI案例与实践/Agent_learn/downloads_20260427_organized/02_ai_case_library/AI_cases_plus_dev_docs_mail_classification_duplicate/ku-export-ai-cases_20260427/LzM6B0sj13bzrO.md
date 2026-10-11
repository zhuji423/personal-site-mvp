---
title: "Ducc 使用实践指南"
description: "资源摘要 图片: 发现 3 个，成功下载 3 个 ✓ /home/gem/workspace/.ark/output/ku-export-ai-cases20260427/assets/LzM6B0sj13bzrO/image001.png"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\LzM6B0sj13bzrO.md"
---

[资源摘要]
  图片: 发现 3 个，成功下载 3 个
    ✓ /home/gem/workspace/.ark/output/ku-export-ai-cases_20260427/assets/LzM6B0sj13bzrO/image_001.png (118.3KB, image/png)
    ✓ /home/gem/workspace/.ark/output/ku-export-ai-cases_20260427/assets/LzM6B0sj13bzrO/image_002.png (217.4KB, image/png)
    ✓ /home/gem/workspace/.ark/output/ku-export-ai-cases_20260427/assets/LzM6B0sj13bzrO/image_003.png (155.5KB, image/png)
Ducc (Claude Code) 使用实践指南

#### 🧑‍🏫 案例作者：[@陈冬雨](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、研发全流程、运维、测试、设计、需求
#### 🔧 使用工具：Ducc、Claude
#### 📒 案例概要：Ducc是百度基于Claude Code的研发Agent，支持代码生成、Bug修复等任务，提供CLAUDE.md规则、Skills技能和子代理等核心组件。
# Ducc 使用实践指南
## 一、简介
Ducc（达克）是百度面向命令行开发场景打造的研发 Agent。它基于 Claude Code 的能力，与百度内部研发体系深度融合，为开发者提供开箱即用的智能研发工具。Ducc 支持代码生成、Bug 修复、代码审查、项目重构等常见研发任务，同时兼容 Claude Code 的开放能力（命令、工具、Plugin、Rules、Skills 等），方便团队和个人高效定制专属 Coding Agent。

---

## 二、常用指令
> 指令参考：[https://code.claude.com/docs/zh-CN/cli-reference](https://code.claude.com/docs/zh-CN/cli-reference)
### 2.1 基础启动
|命令|说明|
|-|-|
|`claude`|启动交互模式（默认）|
|`claude "描述任务"`|一次性执行命令，不进入交互模式|
|`claude --continue`|恢复并继续**上一次**的会话|
|`claude --resume`|从历史会话列表中选择并恢复|

### 2.2 交互指令
|命令|说明|
|-|-|
|`/init`|初始化项目，生成 `CLAUDE.md` 配置文件|
|`/permissions`|查看或重置工具的授权状态|
|`/clear`|清空当前会话上下文（保留配置，类似重置记忆）|
|`/compact`|压缩上下文（节省 Token，保留核心信息）|
|`/resume`|在交互模式内恢复其他会话|

### 2.3 上下文与文件
|操作|说明|
|-|-|
|`@filename`|引用指定文件加入上下文|
|`@folder/`|引用整个目录加入上下文|
|`# <context>`|添加上下文标记（引导 AI 注意特定范围）|
|`Ctrl + V`|粘贴截图（macOS 终端中通常需用 Ctrl+V 而非 Cmd+V）|

### 2.4 自定义命令
|命令|说明|
|-|-|
|`/project:command-name`|执行**项目级**自定义命令（定义在项目的配置中）|
|`/user:command-name`|执行**用户级**自定义命令（定义在全局配置中）|

### 2.5 切换模型
```
ducc config model auto                  # auto 为国产任意模型，由后台视资源情况调度
ducc config model glm-4.7               # 前提是当前代码库支持外部模型
ducc config model MiniMax-M2-Stable
ducc config model 'Claude sonnet 4.5'
ducc config model 'Claude Opus 4.5'
ducc config model 'Claude Haiku 4.5'
```
### 2.6 进阶命令详解
#### /powerup — 互动教学模式
`/powerup` 会启动一个交互式引导，帮助你快速了解 Ducc 的核心功能和使用方法，适合新手入门。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### /compact — 压缩上下文
`/compact` 会将会话历史压缩成一份精简摘要，你可以通过参数告诉它重点保留哪些内容。

**基本用法：**

```
/compact                                                  # 直接压缩
/compact focus on the auth module and current test failures  # 指定保留重点
/compact 保留我们关于数据库 schema 的决定和当前进度            # 中文指定重点
```
**替代方案：**

有些工程师倾向于避免 `/compact`，认为自动压缩不够透明可控。他们的做法是：

* **简单任务**：`/clear` + 自定义 `/catchup` 命令，让 Ducc 读取 git branch 里的变更文件
* **复杂任务**：让 Ducc 先把计划和进度写进一个 `.md` 文件，再 `/clear`，新会话读这个文件继续——即「Document & Clear」模式

|场景|推荐做法|
|-|-|
|任务中途 context 快满|`/compact 保留 XX 进度`|
|任务完成，切换新任务|`/clear`|
|大型复杂任务|Document & Clear 模式更可靠|

#### /context — 查看上下文消耗
`/context` 是一个上下文检查工具，显示当前会话各组成部分的 token 消耗，帮助你做精准的上下文优化决策。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**配合使用建议：**

* **到 70-80%** → 手动 `/compact`，比等自动触发效果好（context 到 80% 会触发自动 compact，此时可能遗漏重点）
* **切换新任务** → `/clear`，彻底清空对话历史（CLAUDE.md 仍然保留）
* **想保留部分上下文** → `/compact focus on XXX`，告诉它重点保留什么

#### /insights — 使用分析报告
`/insights` 会读取你过去一个月的使用历史，分析你的使用模式，生成一份交互式 HTML 报告（保存在 `~/.claude/usage-data/report.html`），完全本地运行，数据不上传。

**报告包含四个核心板块：**

1. **使用统计** — 会话数、token 消耗、最常用工具、时间分布
2. **摩擦点分析** — 找出痛点并分类，每个摩擦点附上真实会话中的具体例子
3. **CLAUDE.md 建议** — 把你反复说的指令提取出来，生成可直接复制粘贴的 CLAUDE.md 规则

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### /btw — 旁路询问
在任务进行中随时可以用 `/btw` 提问，主任务继续跑不会被打断，问答结束后 overlay 消失，内容不写进主会话历史。

```
/btw 你的问题
/btw What does the calculate_metrics function return?
/btw 这个项目用的是哪个测试框架？
```
**核心特性：**

* **任务进行中可用** — Ducc 还在处理响应时就能问，不打断主任务
* **无工具访问** — 只能基于当前 context 回答，不能读文件、跑命令
* **单轮问答** — 没有追问，需要来回对话就用普通 prompt
* **低成本** — 复用父会话的 prompt cache，额外开销极小

> `/btw` 是 subagent 的反面：它能看到你的完整会话但没有工具；subagent 有完整工具但从空 context 开始。用 `/btw` 问 Ducc 已经知道的事，用 subagent 去探索新的东西。
---

## 三、Ducc 核心组件
### 3.1 CLAUDE.md（Rules）
> 详细文档：[https://code.claude.com/docs/zh-CN/memory](https://code.claude.com/docs/zh-CN/memory)
CLAUDE.md 是 Ducc 的"记忆文件"，核心作用包括：对齐编码风格、提供架构上下文、常用命令速查、减少幻觉。建议保持精简并持续维护。

**配置层级：**

|层级|配置文件位置|说明|是否提交 Git|
|-|-|-|-|
|Global（全局级）|`~/.claude/CLAUDE.md`|个人通用习惯，如"总是用中文回复"|—|
|Project（项目级）|`./CLAUDE.md`|团队共享的项目规范，包含架构、技术栈、代码风格|是|
|Local（本地级）|`./CLAUDE.local.md`|个人在该项目中的私有设置|否（加到 `.gitignore`）|

**CLAUDE.md 示例：**

```
# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## 项目概述
Benchmark-verification 是一个对 GPU 压测进行任务编排和结果展示的验收平台。

**技术栈**: Go 1.24+ | Gin 1.10 | GORM v1.25 | Viper | Swagger | Logrus | Prometheus

## 常用开发命令

# 环境配置
go env -w GOPROXY=https://goproxy.cn,direct

# 构建和运行
make build        # 编译项目到 output/benchmark-verification/
make run          # 编译并运行（使用 dev 环境）

# 测试
make test         # 运行所有测试（含 race 检测）
go test -v ./internal/dao/...  # 运行特定包的测试

## 架构模式

Router层 (internal/route/)   → 路由定义、中间件链
Handler层 (internal/handler/) → HTTP 请求处理、参数校验
Domain层 (internal/domain/)   → 核心业务逻辑、业务规则
DAO层 (internal/dao/)         → 数据访问、复杂查询
Model层 (internal/model/)     → 数据模型（db/requests/responses）

## 开发契约
- **错误码分层**: 1-9 基础状态码 | 200xx 通用业务错误 | 201xx 数据库错误 | 202xx 第三方调用错误
- **日志规范**: 结构化 JSON 格式，四级体系（DEBUG/INFO/WARN/ERROR），RequestID 串联链路
- **API 响应格式**: 统一 `{code, data, msg, requestId, currentTime}` 结构
- **命名规范**: 包命名小写，`x` 前缀表示扩展封装；API 端点 `/api/v1/` + 复数名词
```
**Ducc 如何使用 CLAUDE.md?**

当你运行 `claude` 命令时，Ducc 会自动扫描并加载 CLAUDE.md 作为高优先级上下文。例如：你说"帮我修个 Bug"，它会根据你定义的错误处理规范来写代码；你说"跑一下测试"，它会查阅常用命令部分，知道应该运行 `make test` 而不是 `npm test`。

**大型项目的 CLAUDE.md 组织方式：**

> 参考：[https://code.claude.com/docs/zh-CN/memory#使用-claude/rules/-组织规则](https://code.claude.com/docs/zh-CN/memory#使用-claude/rules/-组织规则)
对于大型项目，建议使用 `.claude/rules/` 目录将规则按主题拆分为多个文件，Ducc 会根据上下文自动加载相关规则。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 3.2 Skills
Skills 是 Ducc 的可扩展技能模块，允许你为 Ducc 添加特定领域的专业知识和工作流。

#### skill-creator（创建技能）
用于创建自定义 Skill 的脚手架工具。

* 安装方式：[https://skills.sh/anthropics/skills/skill-creator](https://skills.sh/anthropics/skills/skill-creator)

#### claude-md-management（CLAUDE.md 管理）
* 安装方式：[https://claude.com/plugins/claude-md-management](https://claude.com/plugins/claude-md-management)

这个技能集包含两个子技能：

|子技能|触发方式|功能|
|-|-|-|
|`revise-claude-md`|`/revise-claude-md` 命令|回顾本次会话 → 提取新知识 → 追加到 CLAUDE.md|
|`claude-md-improver`|自动触发|扫描所有 CLAUDE.md 文件 → 评分报告（A-F）→ 针对性改进|

* **revise-claude-md** 适合刚结束一段工作时，固化本次经验
* **claude-md-improver** 适合 CLAUDE.md 长期未维护时，做一次整体优化

#### ku-doc-manage（知识库文档管理）
百度如流知识库的文档操作技能，基于知识库 OpenAPI 开发，提供 14 个核心 API，覆盖文档的完整生命周期。

* 安装方式：`ducc skill install ku-doc-manage`

**核心功能：**

|功能类别|能力|
|-|-|
|文档管理|查询内容、创建文档（支持直接传入 md 文件）、编辑正文、复制文档、上传附件|
|权限管理|查询权限、添加/更新成员、修改公开范围|
|互动数据|查询评论、查询浏览记录|

**典型用法：** 直接给 Ducc 一个知识库 URL，它就能读取文档内容、创建新文档、或将本地 Markdown 文件同步到知识库。

#### brainstorming（头脑风暴）
来自 Superpowers 插件的设计前置技能。在动手写任何代码之前，通过结构化的对话帮你把想法变成完整的设计方案。

* 安装方式：随 Superpowers 插件自动安装

**工作流程：**

1. **探索项目上下文** — 检查文件、文档、最近的提交
2. **逐个提问澄清需求** — 一次只问一个问题，偏好选择题
3. **提出 2-3 种方案** — 附带权衡分析和推荐理由
4. **分段展示设计** — 覆盖架构、组件、数据流、错误处理、测试，逐段确认
5. **输出设计文档** — 保存为 spec 文件并提交 Git
6. **衔接实施** — 自动调用 writing-plans 技能生成实施计划

**核心原则：** 无论项目看起来多简单，都必须先产出设计方案并获得用户确认，才能进入编码阶段——"看似简单"的项目往往是未经审视的假设浪费最多工作量的地方。

### 3.3 子代理（Sub-agents）
子代理是 Ducc 处理复杂任务时自动拆分出的独立工作单元。每个子代理拥有完整的工具访问权限，但从空 context 开始。Ducc 会在需要并行处理多个独立任务时自动启用子代理，比如同时搜索多个文件、并行运行测试等。

### 3.4 Plugins
Plugins 是 Ducc 中最高级别的扩展机制，用于将命令、代理、Skills、Hook、MCP 等能力打包、版本化、共享和分发。

#### LSP Plugins
> 参考：[https://zhuanlan.zhihu.com/p/1993283855554192045](https://zhuanlan.zhihu.com/p/1993283855554192045)
LSP（Language Server Protocol）插件为 Ducc 补上了语言服务器协议支持，使其具备 IDE 常见的代码理解能力，如跳转到定义、查找引用以及实时诊断。

**安装 LSP 插件：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
**本地安装语言服务器（以 Go 为例）：**

```
go install golang.org/x/tools/gopls@latest
gopls version
```
> 如果提示 "command not found"，说明 Go bin 目录没有添加到 `PATH` 中。
**使用效果：** 大模型不需要大量搜索即可定位目标函数，速度更快且节省 token。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 
### 3.5 MCP（Model Context Protocol）
MCP 是一个开放协议，允许 Ducc 连接外部工具和数据源。通过 MCP，你可以让 Ducc 访问数据库、调用内部 API、操作第三方服务等。

**常见 MCP 使用场景：**

* 连接 Notion、GitHub 等外部服务
* 接入内部工具链（如知识库、发布系统）
* 自定义数据查询和操作

**配置方式：** MCP 有两种接入方式——本地进程和远程 HTTP。

方式一：本地进程模式（适用于大多数 MCP Server）

在项目目录的 `.mcp.json` 中配置：

```
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-xxx"],
      "env": {}
    }
  }
}
```
方式二：远程 HTTP 模式（适用于云端 MCP 服务）

```
{
  "mcpServers": {
    "server-name": {
      "type": "http",
      "url": "https://example.com/mcp"
    }
  }
}
```
**实战示例：接入 Notion MCP**

Notion 官方提供了远程 MCP 服务，接入后 Ducc 可以直接搜索、读取、创建和编辑你的 Notion 页面。

1. 安装 Notion Plugin：

```
claude plugin marketplace add https://github.com/anthropics/notion-mcp-plugin
claude plugin install notion-workspace-plugin@notion-plugin-marketplace
```
安装完成后，Plugin 会自动在 `.mcp.json` 中写入以下配置：

```
{
  "mcpServers": {
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    }
  }
}
```
2. 首次使用时会弹出 Notion OAuth 授权页面，授权后即可在 Ducc 中直接操作 Notion。
3. 在 `settings.json` 中启用 Plugin：

```
{
  "enabledPlugins": {
    "notion-workspace-plugin@notion-plugin-marketplace": true
  }
}
```
**使用效果：** 你可以直接对 Ducc 说"搜索 Notion 中关于 XXX 的文档"、"在 Notion 里创建一个任务页面"等，Ducc 会通过 MCP 协议自动完成操作。

---

## 四、Workflow 推荐
以下是社区中两个广受好评的 Ducc / Claude Code 工作流框架：

### 4.1 Superpowers
> 项目地址：[https://github.com/obra/superpowers](https://github.com/obra/superpowers)
Superpowers 是一套 Claude Code Skills 集合，涵盖了从计划编写、代码审查、TDD 开发到分支管理的完整研发工作流。它强调"先计划再编码"，通过结构化的 Skill 串联，帮助开发者在复杂项目中保持高质量的输出。

**核心 Skill 包括：** 写计划（writing-plans）、执行计划（executing-plans）、TDD 开发（test-driven-development）、代码审查（requesting-code-review）、分支收尾（finishing-a-development-branch）等。

### 4.2 gstack
> 项目地址：[https://github.com/garrytan/gstack](https://github.com/garrytan/gstack)
gstack 提供了一个快速的无头浏览器环境，用于 QA 测试和站点验证。它支持页面导航、元素交互、状态验证、截图对比、响应式布局测试等功能，让 Ducc 能够"看到"并操作网页。

---

## 五、使用技巧
### 5.1 MCP 工具延迟加载
默认情况下所有 MCP 工具会在会话启动时全部预加载，这会占用 context 空间。启用延迟加载后，工具描述不占用 context，Ducc 仅在需要时才动态加载相关工具。

**配置方式：** 通过环境变量 `ENABLE_TOOL_SEARCH` 控制：

|值|行为|
|-|-|
|不设置|使用官方 API 时开启，第三方 Base URL 时关闭|
|`true`|强制开启|
|`auto`|超过 context 10% 时自动激活|
|`auto:<N>`|自定义阈值，如 `auto:5` 表示超过 5% 激活|
|`false`|强制关闭，全部预加载|

写入 `~/.claude/settings.json` 持久化：

```
{
  "env": {
    "ENABLE_TOOL_SEARCH": "auto"
  }
}
```
### 5.2 理解 Prompt Cache — 省钱的关键
> 原文：[Cache is All You Need](https://x.com/MinLiBuilds/status/2041178722230030384)
每次你在 Ducc 里敲一句话，背后都在消耗 token。理解缓存机制，可以让同样的套餐多撑 **3-5 倍**。

**核心原理：KV Cache**

大模型生成文本时使用 Transformer 注意力机制。其中历史 token 的 Key 和 Value（KV）算完就固定了，可以缓存复用。新 token 只需计算自己的 Query，然后查已有的 KV，这就是 KV Cache。模型越大，缓存带来的加速越显著。

**Ducc 的缓存架构**

Ducc 每次 API 调用会发送一个精心拼接的多层结构：

```
┌─────────────────────────────────────────────┐
│ system（系统提示词，~20K tokens）              │
│   静态指令（行为规则等）  → 全局缓存（全球共享）  │
│   动态内容（CLAUDE.md 等）→ 组织级缓存          │
├─────────────────────────────────────────────┤
│ tools（工具 schema，session 内冻结）           │
├─────────────────────────────────────────────┤
│ messages（对话历史）                           │
│   最后一条消息上放 cache_control 标记           │
└─────────────────────────────────────────────┘
```
缓存是**前缀匹配**的：只要从头开始的 token 序列一致，就能复用。缓存 TTL 默认 5 分钟，Pro/Max 用户扩展到 1 小时。

**费用对比**

假设系统提示词 20K tokens，对话 10 轮：

* **一个 session 持续对话**：1 次全价 + 9 次 1/10 = **1.9 份**
* **每次开新 session**：10 次全价 = **10 份**
* 差了 **5 倍**

**省钱操作清单**

|操作|缓存影响|建议|
|-|-|-|
|连续对话|前缀不变，增量缓存|一个 session 持续对话|
|`/btw`|共享 session 缓存|用 `/btw` 而非开新会话提问|
|开新 session|冷缓存，~20K 全价重算|非必要不开新 session|
|改 CLAUDE.md|该层之后的缓存全部失效|配好就别动，别在工作中途整理|
|加减 MCP 工具|工具 schema 变化 = 缓存断裂|session 前配好，禁用不用的 MCP|
|切换模型|完全失效|按阶段切，别频繁切|
|`/compact`|消息历史变化 = 断裂|对话 >100K 时再用|
|发呆超过 TTL|缓存过期|1h 内说句话保活|

### 5.3 上下文会话管理
> 原文：[使用 Claude Code：会话管理与 100 万上下文](https://x.com/dotey/status/2044563867355754900)
100 万 token 的上下文窗口是一把双刃剑：它让 Ducc 能处理更长更复杂的任务，但也带来了**上下文衰减**（Context Rot）——随着上下文越来越长，模型注意力被分散，早期无关内容会干扰当前任务。

**五种上下文管理操作**

当 Ducc 完成一轮回答后，你有五种选择：

|操作|说明|适用场景|
|-|-|-|
|**继续**|在同一会话里直接发送下一条消息|任务连贯，上下文仍然相关|
|**回溯** `/rewind` 或双击 Esc|退回到之前某条消息，从那里重新开始|纠正错误方向，比追加指令更高效|
|**清空** `/clear`|开启全新会话，手动带上核心要点|切换到全新任务|
|**压缩** `/compact`|让模型总结当前对话，用摘要替换历史|上下文快满，但任务未完成|
|**子代理**|委派给拥有独立上下文的子 Agent|预知会产生大量"阅后即焚"的中间结果|

**经验法则：新任务 = 新会话**

当你开始一项新任务时，应该开启新会话。但如果前后任务有关联（如写完功能后写文档），保留上下文比重新让 Ducc 读一遍文件更快更省。

**善用回溯（Rewind）**

回溯是最容易被忽略但最实用的操作。当 Ducc 走了弯路时，与其在对话里追加"这招不管用，换个方法"，不如回溯到它还没动手的时刻，带上经验教训重新指示。这样上下文里不会残留失败的尝试，Ducc 表现更好。

**压缩 vs 清空**

* `/compact`：有损压缩，由 Ducc 决定保留什么。好处是省心，可以通过参数引导重点（如 `/compact 将重点放在 auth 模块重构上`）
* `/clear`：手动写下核心要点后彻底重启。更费劲，但上下文 100% 是你认为相关的精华

> 压缩"翻车"通常发生在模型无法预测你下一步方向时。建议在切换任务方向前，主动带上"接下来要做什么"执行 `/compact`，而非等自动触发。
**子代理的使用判断**

灵魂拷问：**以后我还需要看这些工具运行的详细输出吗？** 如果只需要最终结论，就交给子代理——它会在独立上下文里完成工作，只把结果带回来。

---

## 六、参考资料
**官方文档：**

* [常见工作流程](https://code.claude.com/docs/zh-CN/common-workflows)

**最佳实践：**

* [Claude Code 最佳实践](https://www.claude-cn.org/posts/Claude-code-best-practices.html)
* [Anthropic 黑客马拉松冠军经验](https://github.com/affaan-m/everything-claude-code)

**深度阅读：**

* [Cache is All You Need](https://x.com/MinLiBuilds/status/2041178722230030384) — Prompt Cache 原理与省钱技巧
* [上下文会话管理](https://x.com/dotey/status/2044563867355754900) — 100 万上下文窗口的管理之道
* [为什么你的"AI 优先"战略可能大错特错](https://mp.weixin.qq.com/s/RYKuHiQewwJ8p9zyBrAIzQ?poc_token=HGV432mjLZE9W2gbh1boIDnaTxTNYtc92ijyzv8V) — AI 研发策略思考
* [如何使用skills](https://x.com/trq212/status/2033949937936085378)
* [如何让 AI Agent 在多轮、长时间的编码任务中保持高效](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
