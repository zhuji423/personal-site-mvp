---
title: "Claude Code Go — 设计方案"
description: "Claude Code Go语言重现"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Claude Code Go语言重现.md"
---
Claude Code Go语言重现

#### 🧑‍🏫 案例作者：[@杨桐](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Claude
#### 📒 案例概要：Claude Code Go语言重现项目，设计AI终端CLI工具，支持流式对话、工具调用、权限控制和TUI界面。
# Claude Code Go — 设计方案
> 基于原 TypeScript 版本 [claude-code](../claude-code/) 的 Golang 重实现。
---





[https://github.com/atom-yt/claude-code-go](https://github.com/atom-yt/claude-code-go)



## 一、项目概述
Claude Code 是一个 AI 驱动的终端 CLI 工具，核心能力：

* 与 Claude API 进行流式对话
* 通过工具（Tool）调用执行本地操作（读写文件、运行命令、搜索等）
* 支持多轮 Agent 循环（工具调用 → 结果反馈 → 继续推理）
* 支持 MCP（Model Context Protocol）服务器扩展
* Hooks 系统（pre/post tool call 等生命周期拦截）
* 权限控制（每个工具调用都需权限检查）
* 会话持久化与恢复
* 斜杠命令（/help, /clear, /compact 等）

---

## 二、原版架构分析
### 2.1 整体架构
```
User Input
    │
    ▼
CLI Parser (Commander.js)
    │
    ▼
┌─────────────────────────────────┐
│          Agent Loop             │
│  query.ts (1729 lines)          │
│                                 │
│  1. Build messages              │
│  2. Stream API call             │
│  3. Parse stream events         │
│  4. Execute tool calls          │
│  5. Collect tool results        │
│  6. Loop until done             │
└─────────────────────────────────┘
    │               │
    ▼               ▼
Claude API      Tool Executor
(Anthropic)     (45+ tools)
    │               │
    ▼               ▼
Stream Events   Tool Results
(SSE/HTTP)      (file/bash/web...)
    │
    ▼
Ink React TUI (Terminal UI)
```
### 2.2 核心模块
|模块|TS 实现|职责|
|-|-|-|
|CLI 入口|`entrypoints/cli.tsx`|启动、参数解析|
|Agent 主循环|`query.ts`|流式 API 调用、工具调度|
|工具系统|`tools/`, `Tool.ts`|45+ 内置工具定义与注册|
|权限系统|`utils/permissions/`|Allow/Deny/Ask 规则匹配|
|Hooks 系统|`utils/hooks.ts`|生命周期拦截执行|
|MCP 集成|`services/mcp/`|MCP 协议客户端|
|配置管理|`utils/settings/`|JSON 配置、MDM、合并|
|会话管理|`state/AppStateStore.ts`|全局状态、会话持久化|
|TUI 渲染|`ink/`, `components/`|React + Ink 终端渲染|
|命令系统|`commands/`|100+ 斜杠命令|

### 2.3 Agent 循环核心流程
```
┌──────────────────────────────────────────┐
│              query() generator            │
│                                          │
│  messages = prepareMessages()            │
│                                          │
│  loop:                                   │
│    response = streamAPI(messages)        │
│    for event in response.stream:         │
│      if text_delta: yield text event     │
│      if tool_use:                        │
│        result = executeTool(tool, args)  │
│        messages.append(tool_result)      │
│    if stop_reason != 'tool_use': break   │
│                                          │
│  yield stop event                        │
└──────────────────────────────────────────┘
```
---

## 三、Go 版本设计
### 3.1 设计原则
1. **忠实核心逻辑**：忠实还原 Agent 循环、工具系统、权限系统、Hooks 等核心逻辑
2. **Go 惯用模式**：用 channel + goroutine 替代 AsyncGenerator，用 interface 替代 TypeScript 的 type union
3. **模块化边界清晰**：每个包只暴露必要接口，内部实现可替换
4. **可测试性优先**：核心业务逻辑与 I/O 分离，便于单元测试
5. **渐进式实现**：先实现 MVP（基础对话 + 核心工具），再扩展高级特性

### 3.2 目录结构
```
claude-code-go/
├── cmd/
│   └── claude/
│       └── main.go              # CLI 入口
├── internal/
│   ├── agent/
│   │   ├── agent.go             # Agent 主循环
│   │   ├── stream.go            # 流式处理
│   │   └── context.go           # ToolUseContext 定义
│   ├── api/
│   │   ├── client.go            # Anthropic API 客户端
│   │   ├── types.go             # API 消息类型
│   │   └── stream.go            # SSE 流式解析
│   ├── tools/
│   │   ├── registry.go          # 工具注册表
│   │   ├── tool.go              # Tool 接口定义
│   │   ├── bash/                # Bash 工具
│   │   ├── read/                # 文件读取
│   │   ├── write/               # 文件写入
│   │   ├── edit/                # 文件编辑
│   │   ├── glob/                # 文件搜索
│   │   ├── grep/                # 内容搜索
│   │   ├── webfetch/            # HTTP 请求
│   │   └── ...                  # 其他工具
│   ├── permissions/
│   │   ├── checker.go           # 权限检查
│   │   ├── rules.go             # 规则匹配
│   │   └── types.go             # 权限类型
│   ├── hooks/
│   │   ├── executor.go          # Hook 执行器
│   │   ├── types.go             # Hook 类型
│   │   └── runner.go            # 各类 Hook 运行
│   ├── mcp/
│   │   ├── client.go            # MCP 客户端
│   │   ├── stdio.go             # stdio transport
│   │   ├── sse.go               # SSE transport
│   │   └── types.go             # MCP 协议类型
│   ├── config/
│   │   ├── settings.go          # 配置加载
│   │   ├── types.go             # 配置类型
│   │   └── merge.go             # 配置合并
│   ├── session/
│   │   ├── store.go             # 会话存储
│   │   ├── persist.go           # 持久化
│   │   └── types.go             # 会话类型
│   ├── messages/
│   │   ├── types.go             # 消息类型
│   │   ├── normalize.go         # 消息规范化
│   │   └── compact.go           # 历史压缩
│   ├── commands/
│   │   ├── registry.go          # 命令注册
│   │   ├── command.go           # Command 接口
│   │   ├── help.go              # /help
│   │   ├── clear.go             # /clear
│   │   ├── compact.go           # /compact
│   │   └── ...                  # 其他命令
│   └── tui/
│       ├── app.go               # TUI 主界面
│       ├── input.go             # 输入处理
│       ├── render.go            # 输出渲染
│       └── style.go             # 样式定义
├── pkg/
│   └── anthropic/               # 可复用的 Anthropic SDK
│       ├── client.go
│       ├── messages.go
│       └── stream.go
├── go.mod
├── go.sum
├── DESIGN.md                    # 本文件
└── PLAN.md                      # 开发计划
```
### 3.3 核心接口设计
#### Tool 接口
```
// internal/tools/tool.go

type ToolResult struct {
    Data     any
    Messages []Message
    Error    error
}

type ToolUseContext struct {
    Messages    []Message
    AppState    *AppState
    Tools       []Tool
    Commands    []Command
    Permissions *PermissionContext
    MCPClients  []MCPClient
    CWD         string
    // OnProgress callback
    OnProgress  func(data any)
}

type Tool interface {
    Name() string
    Description(input map[string]any) string
    InputSchema() map[string]any   // JSON Schema
    Call(ctx context.Context, input map[string]any, tctx *ToolUseContext) (ToolResult, error)
    IsReadOnly() bool
    IsConcurrencySafe() bool
}
```
#### Agent 主循环
```
// internal/agent/agent.go

type StreamEvent struct {
    Type    string // "text", "tool_use", "tool_result", "stop", "error"
    Text    string
    Tool    *ToolUse
    Result  *ToolResult
    Error   error
}

type Agent struct {
    client    *api.Client
    tools     []tools.Tool
    commands  []commands.Command
    config    *config.Settings
    hooks     *hooks.Executor
    perms     *permissions.Checker
}

// Query 执行一次 Agent 查询，通过 channel 流式返回事件
func (a *Agent) Query(ctx context.Context, messages []Message) <-chan StreamEvent {
    ch := make(chan StreamEvent)
    go a.run(ctx, messages, ch)
    return ch
}

func (a *Agent) run(ctx context.Context, messages []Message, ch chan<- StreamEvent) {
    defer close(ch)
    for {
        // 1. 调用 API
        stream := a.client.StreamMessages(ctx, messages, a.buildToolSpecs())

        // 2. 处理流式事件
        var toolUses []ToolUse
        for event := range stream {
            switch event.Type {
            case "text_delta":
                ch <- StreamEvent{Type: "text", Text: event.Text}
            case "tool_use":
                toolUses = append(toolUses, event.ToolUse)
            }
        }

        // 3. 如果没有工具调用则退出
        if len(toolUses) == 0 {
            ch <- StreamEvent{Type: "stop"}
            return
        }

        // 4. 执行工具（可并发）
        results := a.executeTools(ctx, toolUses)

        // 5. 追加工具结果到消息
        messages = append(messages, buildToolResultMessage(results))
    }
}
```
#### 权限系统
```
// internal/permissions/checker.go

type PermissionMode string
const (
    ModeDefault  PermissionMode = "default"
    ModeTrustAll PermissionMode = "trust-all"
    ModeManual   PermissionMode = "manual"
)

type Rule struct {
    Tool    string // e.g. "Bash", "Write"
    Path    string // file path pattern
    Command string // shell command pattern
}

type Checker struct {
    Mode      PermissionMode
    AllowRules []Rule
    DenyRules  []Rule
    AskRules   []Rule
    // AskFn 由 TUI 实现，用于向用户询问
    AskFn     func(ctx context.Context, req AskRequest) (bool, error)
}

type Decision struct {
    Allowed bool
    Reason  string
}

func (c *Checker) Check(ctx context.Context, toolName string, input map[string]any) (Decision, error)
```
#### Hooks 系统
```
// internal/hooks/types.go

type HookEvent string
const (
    HookPreToolCall  HookEvent = "pre_tool_call"
    HookPostToolCall HookEvent = "post_tool_call"
    HookSessionStart HookEvent = "session_start"
    HookStop         HookEvent = "stop"
    // ...
)

type HookCommand struct {
    Type    string // "command", "http", "prompt"
    Command string // shell command
    URL     string // for http type
    Prompt  string // for prompt type
    Timeout int    // seconds
}

type HookMatcher struct {
    Matcher string       // e.g. "Write", "Read(*.ts)"
    Hooks   []HookCommand
}

type HookInput struct {
    Event     HookEvent
    ToolName  string
    ToolInput map[string]any
    SessionID string
}

type HookResult struct {
    Decision string // "allow", "deny", "continue"
    Reason   string
    Output   string
}
```
#### 配置类型
```
// internal/config/types.go

type Settings struct {
    Model              string
    MaxTokens          int
    APIKey             string
    APIBaseURL         string
    Permissions        PermissionsConfig
    Hooks              map[string][]HookMatcher
    MCPServers         map[string]MCPServerConfig
    EnvironmentVars    map[string]string
    // ...
}

type MCPServerConfig struct {
    Type    string            // "stdio", "sse", "http"
    Command string            // for stdio
    Args    []string          // for stdio
    URL     string            // for sse/http
    Env     map[string]string
    Headers map[string]string
}
```
### 3.4 流式处理设计
Go 使用 channel 替代 TypeScript 的 AsyncGenerator：

```
// internal/api/stream.go

type APIEvent struct {
    Type    string
    // text_delta
    Text    string
    // tool_use
    ToolUse *ToolUse
    // message_stop
    StopReason string
    // error
    Error  error
    Usage  *Usage
}

// StreamMessages 返回事件 channel
func (c *Client) StreamMessages(
    ctx context.Context,
    req MessagesRequest,
) <-chan APIEvent {
    ch := make(chan APIEvent, 32)
    go c.streamSSE(ctx, req, ch)
    return ch
}
```
### 3.5 TUI 设计
使用 [bubbletea](https://github.com/charmbracelet/bubbletea) 构建终端 UI：

```
┌─────────────────────────────────┐
│  Claude Code (Go)               │
│─────────────────────────────────│
│  [conversation history]         │
│  User: explain this file        │
│  Claude: [streaming response]   │
│  > Reading file.go...           │
│  > Running bash...              │
│─────────────────────────────────│
│  Input: █                       │
│  [Ctrl+C: exit] [Enter: send]   │
└─────────────────────────────────┘
```
* `bubbletea` 处理事件循环和键盘输入
* `lipgloss` 处理样式和颜色
* `glamour` 渲染 Markdown 输出

### 3.6 并发模型
```
Main Goroutine (TUI)
    │
    ├── Agent Goroutine
    │       │
    │       ├── API Stream Goroutine
    │       │
    │       └── Tool Executor Pool
    │               ├── Tool 1 Goroutine
    │               ├── Tool 2 Goroutine
    │               └── ...
    │
    └── Hook Goroutine Pool
```
* Agent 循环运行在独立 goroutine
* 并发安全工具（`isConcurrencySafe`）并行执行
* Hooks 异步执行，不阻塞主流程
* 通过 `context.Context` 传播取消信号

---

## 四、技术选型
|功能|选型|说明|
|-|-|-|
|CLI 参数解析|[cobra](https://github.com/spf13/cobra)|成熟的 Go CLI 框架|
|TUI 框架|[bubbletea](https://github.com/charmbracelet/bubbletea)|Elm 架构的终端 UI|
|终端样式|[lipgloss](https://github.com/charmbracelet/lipgloss)|终端颜色和布局|
|Markdown 渲染|[glamour](https://github.com/charmbracelet/glamour)|终端 Markdown 渲染|
|JSON Schema 验证|[jsonschema](https://github.com/santhosh-tekuri/jsonschema)|JSON Schema 校验|
|HTTP 客户端|标准库 `net/http`|支持 SSE 流式|
|配置文件|[viper](https://github.com/spf13/viper)|多层配置合并|
|日志|[slog](https://pkg.go.dev/log/slog)|Go 1.21 标准库|
|测试|`testing` + [testify](https://github.com/stretchr/testify)|标准测试框架|
|MCP 协议|自实现|基于官方 spec|

---

## 五、MVP 范围
第一版（MVP）聚焦核心能力，不追求功能完整性：

### 包含
- [x] Claude API 流式调用（SSE）
- [x] 基础消息对话循环
- [x] Agent 工具调用循环
- [x] 核心工具：Bash、Read、Write、Edit、Glob、Grep
- [x] 基础权限系统（allow/deny/ask）
- [x] JSON 配置加载（`~/.claude/settings.json`）
- [x] 基础 TUI（输入框 + 输出区域）
- [x] 会话历史显示

### 不包含（后续版本）
* MCP 服务器集成
* Hooks 系统
* 斜杠命令系统
* 会话持久化与恢复
* 自动历史压缩（compact）
* WebSearch/WebFetch 工具
* 多 Agent 协调

---

## 六、与原版主要差异
|方面|TypeScript 版|Go 版|
|-|-|-|
|异步模型|AsyncGenerator|channel + goroutine|
|UI 框架|React + Ink|bubbletea|
|Schema 校验|Zod|jsonschema|
|状态管理|Zustand-like store|结构体 + mutex|
|类型系统|丰富的 Union Type|interface|
|构建工具|Bun|go build|
|包管理|npm|go modules|

---

## 七、关键技术挑战
1. **SSE 流式解析**：Anthropic API 返回 SSE 格式，需正确解析 `data:` 前缀、事件类型、JSON body
2. **工具并发执行**：标记为 `ConcurrencySafe` 的工具应并发执行，需协调结果收集
3. **权限 DSL 匹配**：`"Bash(git *)"` 这类规则需要解析和匹配
4. **流式 TUI 更新**：API 流式输出需实时更新终端，不能等全部完成
5. **上下文取消**：用户 Ctrl+C 需要中断正在执行的工具和 API 请求
6. **错误边界**：工具执行失败不应崩溃整个 agent 循环

# Claude Code Go — MVP版本开发计划
> 分阶段实现 Go 版本的 Claude Code CLI 工具。
---

## 阶段划分总览
```
Phase 1: 基础骨架 (1-2周)
    ↓
Phase 2: API 客户端 + Agent 循环 (1-2周)
    ↓
Phase 3: 核心工具集 (2周)
    ↓
Phase 4: 权限系统 + 配置 (1周)
    ↓
Phase 5: TUI 完善 (1周)
    ↓
Phase 6: Hooks + MCP (2-3周)
    ↓
Phase 7: 命令系统 + 会话持久化 (1-2周)
    ↓
Phase 8: 测试 + 打磨 (持续)
```
---

## Phase 1：项目骨架
**目标**：建立项目结构，能编译运行，打印 hello world。

### 任务
- [ ] **1.1** 初始化 Go module

```
go mod init github.com/baidu/claude-code-go
```
- [ ] **1.2** 引入基础依赖

    * `github.com/spf13/cobra` — CLI 框架
    * `github.com/charmbracelet/bubbletea` — TUI
    * `github.com/charmbracelet/lipgloss` — 样式
    * `github.com/charmbracelet/glamour` — Markdown 渲染

- [ ] **1.3** 实现 `cmd/claude/main.go`

    * `cobra` 根命令：`claude [flags] [prompt]`
    * 子命令：`claude resume`、`claude version`
    * 全局 flag：`--model`、`--api-key`、`--verbose`

- [ ] **1.4** 实现空壳 TUI（`internal/tui/`）

    * `bubbletea` 基础 Model/View/Update
    * 可输入文本并回显
    * Ctrl+C 退出

- [ ] **1.5** 项目目录结构按 DESIGN.md 创建

**验收标准**：`go build ./cmd/claude && ./claude` 可以启动 TUI，输入文字可以回显，Ctrl+C 退出。

---

## Phase 2：Anthropic API 客户端 + Agent 基础循环
**目标**：能和 Claude API 进行基础流式对话，看到实时输出。

### 任务
- [ ] **2.1** 实现 API 消息类型（`internal/api/types.go`）

    * `Message`、`ContentBlock`、`ToolUse`、`ToolResult`
    * `MessagesRequest`、`MessagesResponse`
    * `Usage`、`StopReason`

- [ ] **2.2** 实现 SSE 流式客户端（`internal/api/stream.go`）

    * HTTP POST 到 `https://api.anthropic.com/v1/messages`
    * 解析 SSE：`data: {...}` 格式
    * 处理事件类型：
        * `message_start`
        * `content_block_start` / `content_block_delta` / `content_block_stop`
        * `message_delta` / `message_stop`
        * `error`

    * 返回 `<-chan APIEvent` channel

- [ ] **2.3** 实现基础 Agent 循环（`internal/agent/agent.go`）

    * 接收用户 message
    * 调用 API，收集流式输出
    * 返回 `<-chan StreamEvent`（目前只支持文本，无工具调用）

- [ ] **2.4** 将 Agent 接入 TUI

    * 用户按 Enter 发送消息
    * Agent 流式响应实时显示
    * 显示 "thinking..." 状态

- [ ] **2.5** 配置基础加载

    * 从环境变量读取 `ANTHROPIC_API_KEY`
    * 从 `~/.claude/settings.json` 读取 `model` 配置

**验收标准**：`./claude "hello"` 或交互模式输入消息，能看到 Claude 的流式回复。

---

## Phase 3：核心工具系统
**目标**：Claude 能通过工具调用执行文件和命令操作。

### 任务
- [ ] **3.1** 定义 Tool 接口（`internal/tools/tool.go`）

```
type Tool interface {
    Name() string
    Description(input map[string]any) string
    InputSchema() map[string]any
    Call(ctx context.Context, input map[string]any, tctx *ToolUseContext) (ToolResult, error)
    IsReadOnly() bool
    IsConcurrencySafe() bool
}
```
- [ ] **3.2** 实现工具注册表（`internal/tools/registry.go`）

    * `Register(tool Tool)`
    * `GetAll() []Tool`
    * `GetByName(name string) (Tool, bool)`
    * `ToAPISpecs() []ToolSpec`（供 API 调用时传递）

- [ ] **3.3** 实现 `Read` 工具（`internal/tools/read/`）

    * 读取文件内容
    * 支持行范围（offset/limit）
    * 大文件截断提示
    * 返回带行号的内容

- [ ] **3.4** 实现 `Write` 工具（`internal/tools/write/`）

    * 写入/创建文件
    * 支持创建父目录
    * 权限检查（需要 write 权限）

- [ ] **3.5** 实现 `Edit` 工具（`internal/tools/edit/`）

    * 精确字符串替换（`old_string` → `new_string`）
    * `replace_all` 选项
    * 唯一性检查（防止错误替换）

- [ ] **3.6** 实现 `Bash` 工具（`internal/tools/bash/`）

    * 执行 shell 命令
    * 超时控制（默认 120s）
    * 捕获 stdout/stderr
    * 工作目录跟随

- [ ] **3.7** 实现 `Glob` 工具（`internal/tools/glob/`）

    * 文件名模式匹配（`**/*.go` 等）
    * 按修改时间排序
    * 结果数量限制

- [ ] **3.8** 实现 `Grep` 工具（`internal/tools/grep/`）

    * 基于 ripgrep 或标准库
    * 支持正则表达式
    * 文件类型过滤（`--type`）
    * 上下文行（`-C`）
    * 输出模式：files/content/count

- [ ] **3.9** 将工具调用接入 Agent 循环

    * 解析 API 响应中的 `tool_use` 事件
    * 根据 tool name 找到 tool 并执行
    * 将 `tool_result` 追加到消息历史
    * 继续调用 API（循环）

- [ ] **3.10** TUI 中显示工具调用状态

    * "Running bash: git status..."
    * 工具结果折叠显示

**验收标准**：`./claude "list all .go files and show me main.go"` 能自动调用 Glob + Read 工具完成任务。

---

## Phase 4：权限系统 + 配置管理
**目标**：完善权限控制，防止未授权操作。

### 任务
- [ ] **4.1** 实现权限类型（`internal/permissions/types.go`）

    * `PermissionMode`：default / trust-all / manual
    * `Rule`：tool、path、command 匹配
    * `Decision`：allowed/denied + reason

- [ ] **4.2** 实现规则匹配器（`internal/permissions/rules.go`）

    * 解析 `"Bash(git *)"` 格式的规则
    * 路径 glob 匹配（`*.ts`、`src/**`）
    * 命令前缀匹配

- [ ] **4.3** 实现权限检查器（`internal/permissions/checker.go`）

    * 按优先级：deny > allow > ask
    * `trust-all` 模式跳过检查
    * 向 TUI 发起询问（Ask 模式）

- [ ] **4.4** 完善配置加载（`internal/config/settings.go`）

    * 加载 `~/.claude/settings.json`
    * 加载项目级 `.claude/settings.json`（当前目录向上查找）
    * 合并策略（项目覆盖用户）
    * 环境变量覆盖
    * CLI flag 最高优先级

- [ ] **4.5** 配置文件 JSON Schema 定义

    * 权限配置：`permissions.allow/deny/ask`
    * 模型配置：`model`
    * 环境变量注入：`env`

- [ ] **4.6** 在 Agent 循环中集成权限检查

    * 每次工具调用前调用 `checker.Check()`
    * 拒绝时返回错误给 Claude（不执行工具）
    * Ask 时暂停等待用户确认

**验收标准**：配置 `deny: [{tool: "Bash"}]` 后，Bash 工具调用被拒绝；trust-all 模式下所有工具自动通过。

---

## Phase 5：TUI 完善
**目标**：提供完整的终端交互体验。

### 任务
- [ ] **5.1** 多行输入支持

    * `Enter` 发送，`Shift+Enter` 换行
    * 或可配置的提交快捷键

- [ ] **5.2** 对话历史滚动

    * 鼠标滚轮 / 键盘滚动
    * 自动滚动到最新消息
    * 历史消息折叠

- [ ] **5.3** 工具调用可视化

    * 工具名称 + 参数摘要
    * 执行状态（进行中/完成/失败）
    * 结果折叠展开

- [ ] **5.4** Markdown 渲染

    * 使用 `glamour` 渲染 Claude 的 Markdown 回复
    * 代码块语法高亮
    * 链接处理

- [ ] **5.5** 状态栏

    * 当前模型
    * token 用量
    * 当前工作目录

- [ ] **5.6** 键盘快捷键

    * `Ctrl+C`：取消当前请求或退出
    * `Ctrl+L`：清屏
    * `↑/↓`：历史输入导航

- [ ] **5.7** 流式输出动画

    * 打字效果（光标闪烁）
    * 思考中的旋转动画

**验收标准**：TUI 体验流畅，支持长对话滚动、Markdown 渲染、工具状态显示。

---

## Phase 6：Hooks 系统
**目标**：支持生命周期拦截，允许用户自定义行为。

### 任务
- [ ] **6.1** 实现 Hook 类型（`internal/hooks/types.go`）

    * 事件：`session_start`、`pre_tool_call`、`post_tool_call`、`stop`
    * 命令类型：`command`（shell）、`http`（HTTP POST）

- [ ] **6.2** 实现 Shell Hook 执行器

    * 执行 shell 命令，传入 JSON 环境变量
    * 超时控制
    * 捕获 stdout 作为 hook 输出

- [ ] **6.3** 实现 HTTP Hook 执行器

    * POST JSON 到指定 URL
    * 支持自定义 headers
    * 解析响应决策（allow/deny）

- [ ] **6.4** 实现 Hook 匹配器

    * 按 tool name 匹配 `matcher` 字段
    * 支持通配符

- [ ] **6.5** 在 Agent 循环中触发 Hooks

    * `pre_tool_call`：工具执行前，可拦截（deny）
    * `post_tool_call`：工具执行后，可修改结果
    * `session_start`：会话开始时
    * `stop`：Agent 停止时

- [ ] **6.6** 从配置加载 Hooks

```
{
  "hooks": {
    "pre_tool_call": [
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "echo $TOOL_INPUT" }] }
    ]
  }
}
```
**验收标准**：配置 pre_tool_call hook 后，每次工具调用前 shell 命令被执行。

---

## Phase 7：MCP 客户端集成
**目标**：支持 MCP 服务器，扩展工具能力。

### 任务
- [ ] **7.1** 实现 MCP 协议类型（`internal/mcp/types.go`）

    * `initialize` / `tools/list` / `tools/call`
    * `resources/list` / `resources/read`
    * JSON-RPC 2.0 消息格式

- [ ] **7.2** 实现 stdio transport（`internal/mcp/stdio.go`）

    * 启动子进程
    * 通过 stdin/stdout 进行 JSON-RPC 通信
    * 进程生命周期管理

- [ ] **7.3** 实现 SSE transport（`internal/mcp/sse.go`）

    * HTTP SSE 连接
    * 支持 HTTP headers 认证

- [ ] **7.4** 实现 MCP 客户端（`internal/mcp/client.go`）

    * `Connect()` 建立连接
    * `ListTools()` 获取工具列表
    * `CallTool(name, input)` 执行工具
    * 将 MCP tools 转换为 `Tool` 接口

- [ ] **7.5** 在启动时加载 MCP 服务器

    * 从配置 `mcpServers` 读取
    * 并发连接所有服务器
    * 注册 MCP 工具到 registry（前缀 `mcp__<server>__`）

- [ ] **7.6** 处理 MCP 工具调用

    * 通过对应 MCP 客户端执行
    * 错误处理和超时

**验收标准**：配置 MCP server 后，MCP 工具出现在 Claude 可用工具列表中，可被调用。

---

## Phase 8：斜杠命令 + 会话持久化
**目标**：支持内置命令和会话恢复。

### 任务
- [ ] **8.1** 实现命令接口（`internal/commands/command.go`）

```
type Command interface {
    Name() string
    Description() string
    Execute(ctx context.Context, args []string, tctx *ToolUseContext) error
}
```
- [ ] **8.2** 实现内置命令

    * `/help` — 显示帮助
    * `/clear` — 清空对话历史
    * `/compact` — 压缩历史（摘要）
    * `/model <name>` — 切换模型
    * `/verbose` — 切换详细模式
    * `/cost` — 显示 token 用量和费用

- [ ] **8.3** TUI 中解析斜杠命令

    * 输入以 `/` 开头时识别为命令
    * 命令补全提示

- [ ] **8.4** 会话持久化（`internal/session/persist.go`）

    * 保存对话历史到 `~/.claude/sessions/<id>.json`
    * 记录 session ID、时间戳、模型、cost
    * 保存 AppState

- [ ] **8.5** 会话恢复（`claude resume`）

    * 列出最近会话
    * 加载选定会话的消息历史
    * 继续对话

- [ ] **8.6** 历史压缩（`/compact`）

    * 调用 Claude API 生成历史摘要
    * 用摘要替换旧消息
    * 保留最近 N 条消息

**验收标准**：`/clear` 清空历史；`claude resume` 恢复上次对话。

---

## Phase 9：测试与打磨
**目标**：确保稳定性，完善文档。

### 任务
- [ ] **9.1** API 客户端单元测试

    * SSE 解析测试
    * 错误处理测试
    * Mock HTTP server

- [ ] **9.2** 工具单元测试

    * 各工具 happy path 测试
    * 边界条件（大文件、权限拒绝等）

- [ ] **9.3** 权限系统测试

    * 规则匹配测试
    * 各种模式下的决策测试

- [ ] **9.4** Agent 循环集成测试

    * Mock API 返回工具调用
    * 验证工具被正确执行和结果被正确传递

- [ ] **9.5** 性能优化

    * 启动时间优化
    * 大消息历史处理
    * 并发工具执行

- [ ] **9.6** 文档完善

    * README.md
    * 安装说明
    * 配置参考
    * 工具列表

- [ ] **9.7** 构建和发布

    * Makefile
    * 多平台交叉编译（darwin/linux/windows）
    * GitHub Actions CI

---

## 里程碑
|里程碑|目标|预计完成|
|-|-|-|
|M1|Phase 1+2 完成：基础对话可用|Week 3|
|M2|Phase 3+4 完成：工具调用 + 权限控制|Week 6|
|M3|Phase 5 完成：TUI 体验完善|Week 7|
|M4|Phase 6+7 完成：Hooks + MCP|Week 10|
|M5|Phase 8+9 完成：完整功能 + 稳定|Week 12|

---

## 技术债务和风险
|风险|说明|缓解方案|
|-|-|-|
|SSE 解析兼容性|Anthropic API SSE 格式可能变化|充分测试，参考官方 SDK|
|bubbletea 学习曲线|Elm 架构对 Go 开发者较陌生|从简单示例开始|
|并发工具执行|并发执行可能引发竞态|仔细设计锁和 channel|
|MCP 协议合规性|MCP spec 还在演进|参考官方 TypeScript SDK|
|权限 DSL 复杂性|原版规则语法复杂|先实现简化版，逐步完善|

---

## 开发规范
### 代码规范
* `gofmt` 格式化
* `golint` + `staticcheck` 静态检查
* 错误必须处理（不得 `_` 忽略关键错误）
* 公开接口必须有文档注释

### Git 规范
* feature 分支开发
* commit message：`feat:`, `fix:`, `refactor:`, `test:`, `docs:`
* PR 前通过所有测试

### 测试规范
* 核心逻辑覆盖率 > 80%
* 集成测试使用 mock API server
* 工具测试使用临时目录

# 使用codex分析claude-code-go 当前MVP版本对比其他产品功能分析和改进
> 对比对象：
> * `../claude-code`
> * `../hermes-agent`
> * `../OpenHarness`
> * 当前仓库 `claude-code-go`
> 
## 1. 结论先行
`claude-code-go` 现在更像一个“可用的单机版 agent loop + TUI 原型”，而不是一个成熟的 agent harness。

它已经具备这些核心基础：

* 流式多轮 agent loop
* 基础工具系统
* 权限检查与 hooks
* session 持久化
* MCP stdio 工具接入
* skills 扫描
* slash commands
* 基础 auto-compact / auto-dream 雏形

但和 `claude-code`、`hermes-agent`、`OpenHarness` 对比，当前短板不是“工具数量少”这么简单，而是下面几个更关键的问题：

1. 很多能力已经有“tool 壳子”或“目录雏形”，但没有打通成完整产品闭环。
2. 系统提示词、上下文注入、计划模式、任务管理、记忆系统都还偏浅，缺少稳定的 runtime contract。
3. 安全与执行边界仍较粗糙，尤其是 bash/path/web/mcp 侧。
4. 缺少 coordinator / subagent / background task 这一层，导致复杂任务扩展性明显弱于另外三个项目。
5. 目前最应该优先补的是“架构完成度”，不是继续横向加更多工具。

建议把未来 1-2 个版本的目标定义为：

* 先把 `claude-code-go` 做成一个扎实的本地单 agent harness
* 再引入受控的 plan/task/subagent 能力
* 最后再考虑插件生态、消息网关、多终端平台等外围扩张

---

## 2. 四个项目的定位差异
### 2.1 claude-code
定位是成熟的生产级 coding agent CLI。

强项：

* 工具体系完整，且不是简单堆工具，而是围绕工作流组织
* 有 plan mode、worktree、agent tool、task、LSP、MCP resource、plugin、remote/CCR 等完整运行时
* 安全与权限规则做得很细，尤其是 bash/path/sandbox
* TUI、命令、服务层、状态层边界清晰

对 `claude-code-go` 的启发：

* 不是补“更多命令”，而是补“运行时层”
* 先补 prompt/context orchestration、task lifecycle、tool execution governance

### 2.2 hermes-agent
定位是长期运行、跨平台、多环境、多技能、多记忆的 personal agent。

强项：

* messaging gateway 与长期运行能力强
* memory / skill / profile / model routing / environment backend 很完整
* 明显偏“agent platform”，不只是本地 coding CLI

对 `claude-code-go` 的启发：

* 记忆、技能、环境抽象值得借鉴
* 但 messaging/gateway/voice 不应成为当前阶段优先级

### 2.3 OpenHarness
定位是开源 agent harness 基础设施，强调可组合架构和 swarm。

强项：

* 模块边界清晰：engine / prompts / permissions / swarm / plugins / memory / channels
* 对 coordinator、task、plugin、auth/provider、channel 支撑比较系统
* 很适合作为“中间态架构”参考

对 `claude-code-go` 的启发：

* 最值得借鉴的是架构分层方式
* 先把 runtime 与 service 层拆清楚，再继续长功能

### 2.4 claude-code-go
定位目前是：

* Go 重写版本地 coding agent CLI
* 已有可运行体验
* 但系统层还偏薄，许多高级能力处在“半实现”状态

---

## 3. 当前 claude-code-go 的真实状态
下面这个判断基于代码而不是 README。

### 3.1 已经比较扎实的部分
* `internal/agent/agent.go`
    * agent loop 已能完成文本流式输出、tool_use 收集、权限检查、hooks、串并行工具执行、tool_result 回注

* `internal/api/`
    * 同时支持 Anthropic 风格和 OpenAI-compatible 风格的流式客户端

* `internal/tui/`
    * 基础 TUI 可用，包含 markdown 渲染、滚动、输入历史、autocomplete、状态栏

* `internal/permissions/`
    * allow / deny / ask 三层规则已成型

* `internal/hooks/`
    * shell / HTTP hooks 能工作

* `internal/session/`
    * session 落盘和恢复已经够用

* `internal/mcp/`
    * stdio MCP tools 已能注册进本地 registry


### 3.2 已实现但明显偏“原型”的部分
* `EnterPlanMode` / `ExitPlanMode`
    * 现在只是返回提示文本，没有真实 plan-mode 状态机

* `AskUserQuestion`
    * 现在只会格式化问题，不会真的驱动交互问答闭环

* `TodoWrite` / `Task*`
    * 都是进程内全局内存结构，不是持久任务系统，也没有 subagent/runtime 集成

* auto-compact
    * 现在本质是裁剪历史，不是高质量摘要压缩

* auto-dream
    * 触发条件、锁、prompt 有了，但记忆抽取/写回仍比较脆

* skills
    * 已支持扫描和注入，但还没有 skill workflow、依赖装载、插件化技能组合


### 3.3 明显缺失或薄弱的部分
* 没有稳定的 prompt builder / context builder
* 没有 `CLAUDE.md` / `AGENTS.md` / 项目上下文注入主链路
* 没有真正的 coordinator / subagent / background worker runtime
* 没有 sandbox abstraction
* MCP 只做到 stdio tool bridge，缺 resource/auth/http/reconnect
* provider 体系仍是硬编码 map，扩展性弱
* 安全策略没有细化到 destructive command、敏感路径、URL guard、path normalization 等层次
* session / memory 没有搜索、索引、摘要、回放能力
* plugin 目前没有真正的 runtime/plugin contract

---

## 4. 对标后的核心优化方向
## 4.1 优化方向一：先把“上下文系统”做完整
这是当前最值得优先补的设计层。

### 当前问题
`claude-code-go` 现在把大部分能力放在：

* model config
* tools
* slash commands
* TUI

但真正决定 agent 上限的是上下文装配能力，当前这里明显不够：

* 没有统一 system prompt builder
* 没有环境上下文、项目上下文、用户规则、技能上下文的分层注入
* 没有像 `claude-code` / `OpenHarness` 那样的 prompt/context service

### 对标参考
* `claude-code/services/*Prompt*`, `services/compact`, `services/toolUseSummary`
* `OpenHarness/src/openharness/prompts/*`
* `hermes-agent/agent/prompt_builder.py`

### 建议设计
引入独立的上下文装配层：

* `internal/prompt/system.go`
* `internal/prompt/context.go`
* `internal/prompt/project.go`
* `internal/prompt/environment.go`
* `internal/prompt/skills.go`

明确每次请求的上下文组成：

1. base system prompt
2. project instructions
3. runtime mode instructions
4. tool policy / permission hints
5. loaded skills
6. memory snippets
7. conversation history

### 直接收益
* 后续 plan mode、compact、dream、task、subagent 都有统一挂载点
* 可以把“功能”变成“模式”，而不是继续堆 command/tool

---

## 4.2 优化方向二：把 plan / task / subagent 从原型做成运行时
这是和另外三个项目差距最大的地方。

### 当前问题
当前仓库已经有：

* `EnterPlanMode`
* `ExitPlanMode`
* `TodoWrite`
* `TaskCreate/Update/List/...`

但它们还没有形成完整执行链：

* plan mode 没有独立状态
* task 没有 durable storage
* task 和 tool execution 没有调度关系
* 没有真正的 subagent spawn / wait / stop 机制

### 对标参考
* `claude-code/tasks/*`
* `claude-code/tools/AgentTool/*`
* `OpenHarness/src/openharness/swarm/*`
* `OpenHarness/src/openharness/tasks/*`
* `hermes-agent/tools/delegate_tool.py`

### 建议设计
优先做“轻量版”，不要一步学 Hermes 那种全平台代理系统。

建议路线：

1. 先做 plan session

    * 进入 plan mode 后，切换 prompt profile
    * 限制允许工具
    * 产出 plan artifact
    * 用户批准后再进入 implement mode

2. 再做 durable task store

    * 任务落盘到 session scope 或 workspace scope
    * task 状态与会话关联
    * TUI 能显示 current task / background task

3. 最后做本地 subagent runtime

    * 先支持 subprocess / goroutine worker 即可
    * 明确只允许只读 explorer 和有限写 worker 两类

### 直接收益
* 复杂任务不再全塞进单轮上下文
* 可以开始追平 `OpenHarness`/`claude-code` 的 coordinator 设计

---

## 4.3 优化方向三：重做 compact / memory，使其从“裁剪”升级为“压缩系统”
### 当前问题
当前 compact 主要是：

* 保留最近若干消息
* 删除旧消息

这不是严格意义上的 compact，更接近“截断”。

当前 dream 也存在类似问题：

* 有锁和阈值
* 有 consolidation prompt
* 但缺少稳定的 memory schema、索引、冲突合并策略

### 对标参考
* `claude-code/services/compact/*`
* `claude-code/services/autoDream/*`
* `claude-code/services/SessionMemory/*`
* `OpenHarness/src/openharness/memory/*`
* `hermes-agent/agent/memory_manager.py`

### 建议设计
把 compact 分为三层：

* micro-compact: 针对本轮或短段历史
* session-compact: 提取 session summary + open loops + pending tasks
* memory extract: 从 session summary 里抽 durable memory

memory 需要至少有三类对象：

* session summary
* project memory
* user/workspace memory

### 直接收益
* 长对话能力会明显提升
* dream 才真正有价值，不会只是“让模型再读一遍自己说过的话”

---

## 4.4 优化方向四：把权限与安全从“规则匹配”升级为“执行治理”
### 当前问题
当前权限系统有基础规则，但还远不够稳：

* `isReadOnlyTool()` 只硬编码了 `Read/Glob/Grep`
* `Bash` 没有 destructive command 语义层
* 文件路径没有更完整的 normalize / sensitive-path / workspace boundary 校验
* `WebFetch` / `WebSearch` 安全策略偏弱
* MCP 没有 server-level trust / capability gating

### 对标参考
* `claude-code/tools/BashTool/*`
* `claude-code/utils/sandbox/*`
* `OpenHarness/src/openharness/utils/network_guard.py`
* `OpenHarness/src/openharness/sandbox/*`
* `hermes-agent/tools/path_security.py`

### 建议设计
把安全层拆成三类：

* policy layer
    * allow/deny/ask

* validation layer
    * path normalization
    * command semantics
    * URL validation
    * sensitive path guard

* execution layer
    * sandbox backend
    * timeout
    * output truncation
    * provenance logging


优先补这些点：

* Bash command classifier
* 路径边界检查
* Web URL allow/deny rules
* MCP server trust level

### 直接收益
* 这是把 `claude-code-go` 从 demo 提升到“能放心跑”的关键

---

## 4.5 优化方向五：把 MCP 从“可调用工具桥”升级为“完整扩展协议层”
### 当前问题
现在 MCP 主要能力是：

* 连接 stdio server
* 列工具
* 注册为本地 tool

这离成熟实现还有明显差距：

* 没有 HTTP/SSE transport
* 没有 resource 读取
* 没有 auth / reconnect / health
* 没有按 server 分类显示与权限控制

### 对标参考
* `claude-code/services/mcp/*`
* `claude-code/tools/ListMcpResourcesTool/*`
* `claude-code/tools/ReadMcpResourceTool/*`
* `OpenHarness/src/openharness/mcp/*`

### 建议设计
先补最有价值的 3 件事：

1. `list_mcp_resources`
2. `read_mcp_resource`
3. HTTP transport + reconnect

之后再补：

* MCP auth
* tool/resource capability filtering
* TUI 中 server 状态展示

### 直接收益
* MCP 才会从“可用”变成“平台能力”

---

## 4.6 优化方向六：重构 provider 层，避免继续硬编码
### 当前问题
当前 provider 体系虽然支持多 provider，但总体还是：

* hardcoded provider map
* API key / base URL 映射零散
* 模型能力没有统一元数据

这会导致：

* provider 越多，分支越多
* 模型能力差异无法被 runtime 感知

### 对标参考
* `OpenHarness/src/openharness/api/provider.py`
* `OpenHarness/src/openharness/api/registry.py`
* `hermes-agent/agent/model_metadata.py`
* `hermes-agent/agent/smart_model_routing.py`

### 建议设计
引入 provider registry：

* provider id
* protocol
* auth env keys
* default base URL
* default model
* capability flags
    * tools
    * reasoning
    * image input
    * prompt caching
    * max context


### 直接收益
* `/model`、config、prompt builder、token estimation 都能复用同一份元数据

---

## 4.7 优化方向七：补齐 project instructions / memory files / skills 的主链路
### 当前问题
这个点被三个对标项目都证明非常重要，但 `claude-code-go` 现在还没真正打通。

缺口包括：

* 没有稳定发现并注入 `CLAUDE.md` / `AGENTS.md`
* skill 只是“扫描和返回内容”
* 记忆文件没有和 prompt builder 绑定

### 对标参考
* `OpenHarness/src/openharness/prompts/claudemd.py`
* `claude-code/skills/*`
* `hermes-agent/agent/skill_utils.py`

### 建议设计
在 prompt build 阶段明确注入顺序：

1. workspace instructions
2. active skill instructions
3. memory snippets
4. user prompt

同时给 skills 增加最少的运行时约束：

* source
* trigger
* dependencies
* load mode
* visibility

### 直接收益
* 用户会立刻感受到“项目懂我了”，这是体验跃迁点

---

## 4.8 优化方向八：把 TUI 从“能用”做成“适合长任务”
### 当前问题
当前 TUI 基础够用，但长任务体验仍弱于另外几个项目：

* tool output 展示较轻
* ask / background event / auto-compact / auto-dream 与 UI 状态没有完全同步设计
* 任务、计划、session、MCP、permissions 没有统一的侧边信息视图

### 对标参考
* `claude-code/components/*`
* `OpenHarness` React/Ink TUI
* `hermes-agent` 的 curses/TUI 与 gateway status 组织方式

### 建议设计
不用一开始就做大 UI 重构，先补下面这些：

* tool result collapse/expand
* current mode indicator
* pending task indicator
* current session / plan file / memory status
* MCP server status
* permission prompt modal 化

### 直接收益
* 更适合长时间 coding session
* 也为 subagent/background task 提前铺路

---

## 5. 从三个对标项目各自应该学什么
## 5.1 应该向 claude-code 学
* plan mode / worktree / task / agent tool 的运行时整合方式
* bash/path/sandbox 的安全治理深度
* compact / dream / session memory 的服务层拆分
* MCP resource 与 plugin 的系统化设计

## 5.2 应该向 OpenHarness 学
* engine / prompts / permissions / swarm / plugins 的模块边界
* provider/auth/channel/plugin 的注册式架构
* 作为开源 harness 的“中台层”组织方式

## 5.3 应该向 hermes-agent 学
* 长期记忆、技能沉淀、环境抽象、模型元数据
* 多平台运行的能力边界设计

## 5.4 当前阶段不建议优先学什么
下面这些很强，但不适合作为当前 1-2 个版本的优先项：

* Hermes 的 messaging gateway / voice / social platform
* OpenHarness 的 channels 全家桶
* Claude Code 的远程容器、云端规划、团队同步

原因很简单：

* `claude-code-go` 现在最缺的不是外沿能力，而是本地 runtime 的厚度

---

## 6. 推荐的目标架构
建议把当前结构往下面这个方向演进：

```
cmd/
  claude/

internal/
  app/            # 顶层装配
  agent/          # 单 agent loop
  prompt/         # system/context/project/skills/memory builder
  runtime/        # mode/task/subagent lifecycle
  tools/          # builtin tools
  permissions/    # policy + validation
  sandbox/        # local sandbox backends
  hooks/          # lifecycle hooks
  mcp/            # tools/resources/auth/transports
  memory/         # session summary + durable memory
  sessions/       # persistence/search/index
  providers/      # provider registry + model metadata
  plugins/        # plugin loader / contracts
  tui/            # presentation layer only
```
关键原则：

* `tui` 只负责交互，不承载核心业务决策
* `agent` 只负责 loop，不承担所有 runtime 状态
* `prompt`、`runtime`、`memory`、`providers` 必须从 `tui` 中分离出来

---

## 7. 分阶段实施建议
## Phase 1：补架构地基
目标：

* 先解决“功能有了，但没有统一主链路”的问题

建议项：

* 引入 prompt/context builder
* 注入 `CLAUDE.md` / `AGENTS.md` / skills / memory
* provider registry 化
* 将 auto-compact、auto-dream 从 TUI 状态里拆出 service

验收标准：

* 每次请求都能稳定打印一份可解释的 assembled context 结构

## Phase 2：补执行运行时
目标：

* 把 plan/task 变成真正可依赖的能力

建议项：

* real plan mode
* durable task store
* task-aware TUI
* limited local subagent runtime

验收标准：

* 一个复杂任务能拆解、批准、执行、跟踪，而不是全靠单轮上下文硬撑

## Phase 3：补安全与扩展
目标：

* 让系统更稳、更可扩展

建议项：

* bash/path/url guard
* sandbox abstraction
* MCP resources + HTTP transport
* plugin contract

验收标准：

* 对外扩展和安全控制都有清晰边界

## Phase 4：补产品化体验
目标：

* 把“工程上能跑”升级为“长期使用舒服”

建议项：

* tool/result 视图增强
* session search
* compact/memory 可视化
* plan/task/subagent 状态视图

验收标准：

* 连续工作数小时仍然可控

---

## 8. 建议优先级
### P0：必须先做
* prompt/context builder
* project instructions 注入
* compact/memory 服务化
* provider registry
* 安全校验补强

### P1：很值得紧接着做
* real plan mode
* durable task system
* 轻量 subagent runtime
* MCP resources / HTTP transport

### P2：做完会明显加分
* plugin contract
* session search / indexing
* richer TUI panels
* 模型能力感知与智能路由

### P3：先不要急
* messaging gateway
* voice
* 多平台社交集成
* 远程容器和云端 orchestration

---

## 9. 一个更务实的版本目标
如果只给 `claude-code-go` 规划两个里程碑，我建议是：

### v0.2
目标是“成为一个扎实的单机 coding harness”

范围：

* prompt builder
* `CLAUDE.md`/`AGENTS.md` 注入
* provider registry
* 真 compact
* memory 提取最小闭环
* 安全治理第一版

### v0.3
目标是“成为一个可规划、可拆解的本地 agent”

范围：

* real plan mode
* durable task store
* local subagent runtime
* MCP resources
* TUI 任务/模式/权限增强

---

## 10. 最后判断
如果把三个对标项目当作参考系：

* 对 `claude-code`，`claude-code-go` 当前差在“运行时深度”和“安全治理深度”
* 对 `OpenHarness`，差在“架构完整度”和“扩展层设计”
* 对 `hermes-agent`，差在“长期记忆/技能/环境抽象”

但从投入产出比看，`claude-code-go` 现在最有价值的方向不是追求大而全，而是：

* 先把本地 coding agent 的 runtime 厚起来
* 把半实现能力打通
* 把上下文、安全、记忆、计划四个核心层补齐

只要这四层补起来，`claude-code-go` 就会从“Go 版复刻项目”变成“有自己工程优势的 agent harness”。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
