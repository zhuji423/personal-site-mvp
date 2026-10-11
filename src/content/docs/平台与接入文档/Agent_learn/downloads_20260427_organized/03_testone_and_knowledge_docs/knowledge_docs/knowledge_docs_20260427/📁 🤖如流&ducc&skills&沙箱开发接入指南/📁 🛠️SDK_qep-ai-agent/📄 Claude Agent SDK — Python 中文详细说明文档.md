---
title: "Claude Agent SDK — Python 中文详细说明文档"
description: "Claude Agent SDK — Python 中文详细说明文档"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🤖如流&ducc&skills&沙箱开发接入指南\\📁 🛠️SDK_qep-ai-agent\\📄 Claude Agent SDK — Python 中文详细说明文档.md"
---
Claude Agent SDK — Python 中文详细说明文档

# Claude Agent SDK — Python 中文详细说明文档
> 基于官方文档整理，适用于 `claude-agent-sdk` Python 包。
---

## 目录
1. [安装](#安装)
2. [核心概念：query() vs ClaudeSDKClient](#核心概念)
3. [函数参考](#函数参考)

    * [query()](#query)
    * [tool() 装饰器](#tool-装饰器)
    * [create_sdk_mcp_server()](#create_sdk_mcp_server)
    * [list_sessions()](#list_sessions)
    * [get_session_messages()](#get_session_messages)

4. [类参考](#类参考)

    * [ClaudeSDKClient](#claudesdkclient)

5. [配置类型](#配置类型)

    * [ClaudeAgentOptions](#claudeagentoptions)
    * [SettingSource](#settingsource)
    * [ThinkingConfig](#thinkingconfig)

6. [消息类型](#消息类型)
7. [错误类型](#错误类型)
8. [Hook 系统](#hook-系统)
9. [权限系统](#权限系统)
10. [沙箱配置](#沙箱配置)
11. [MCP 服务器配置](#mcp-服务器配置)
12. [内置工具 I/O 参考](#内置工具-io-参考)
13. [完整示例](#完整示例)

---

## 安装
```
pip install claude-agent-sdk
```
---

## 核心概念
SDK 提供两种使用方式，适用于不同场景：

|特性|`query()`|`ClaudeSDKClient`|
|-|-|-|
|会话|每次新建独立会话|复用同一会话|
|对话|单次问答交换|多轮对话，保持上下文|
|连接管理|自动管理|手动控制生命周期|
|流式输入|支持|支持|
|中断任务|不支持|支持|
|Hooks|支持|支持|
|自定义工具|支持|支持|
|继续历史对话|不支持|支持|
|**适用场景**|一次性、独立任务|持续对话、交互式应用|

**选择原则：**

* 如果你只需要「问一个问题拿到答案」，用 `query()`。
* 如果你需要「多轮对话」或「任务中途打断」，用 `ClaudeSDKClient`。

---

## 函数参考
### `query()`
每次调用创建一个新的独立会话，返回异步迭代器，逐条产出消息。

```
async def query(
    *,
    prompt: str | AsyncIterable[dict[str, Any]],
    options: ClaudeAgentOptions | None = None,
    transport: Transport | None = None
) -> AsyncIterator[Message]
```
**参数说明：**

|参数|类型|说明|
|-|-|-|
|`prompt`|`str` 或异步迭代器|用户输入，可以是字符串或流式消息序列|
|`options`|`ClaudeAgentOptions`|可选，配置模型、工具、权限等行为|
|`transport`|`Transport`|可选，自定义传输层（一般不需要）|

**基础示例：**

```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are an expert Python developer",
        permission_mode="acceptEdits",
        cwd="/home/user/project",
    )
    async for message in query(prompt="帮我创建一个 Python Web 服务器", options=options):
        print(message)

asyncio.run(main())
```
---

### `tool()` 装饰器
将一个异步函数注册为 MCP 工具，支持类型安全的输入 Schema 定义。

```
def tool(
    name: str,
    description: str,
    input_schema: type | dict[str, Any],
    annotations: ToolAnnotations | None = None
) -> Callable[..., SdkMcpTool[Any]]
```
**参数说明：**

|参数|类型|说明|
|-|-|-|
|`name`|`str`|工具名称（Claude 调用时使用）|
|`description`|`str`|工具描述（帮助模型理解何时使用）|
|`input_schema`|`dict`|输入参数的 Schema 定义|
|`annotations`|`ToolAnnotations`|可选的额外注解|

**两种 Schema 定义方式：**

```
# 方式一：简单类型映射（推荐，更简洁）
{"text": str, "count": int, "enabled": bool}

# 方式二：标准 JSON Schema 格式（支持复杂验证）
{
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "count": {"type": "integer", "minimum": 0},
    },
    "required": ["text"],
}
```
**示例：**

```
from claude_agent_sdk import tool
from typing import Any

@tool("greet", "向用户打招呼", {"name": str})
async def greet(args: dict[str, Any]) -> dict[str, Any]:
    return {
        "content": [{"type": "text", "text": f"你好，{args['name']}！"}]
    }
```
> **注意：** 工具函数返回值必须遵循 MCP 内容格式：`{"content": [{"type": "text", "text": "..."}]}`
---

### `create_sdk_mcp_server()`
创建一个在当前 Python 进程内运行的 MCP 服务器，无需额外进程或网络连接。

```
def create_sdk_mcp_server(
    name: str,
    version: str = "1.0.0",
    tools: list[SdkMcpTool[Any]] | None = None
) -> McpSdkServerConfig
```
**参数说明：**

|参数|类型|说明|
|-|-|-|
|`name`|`str`|服务器名称|
|`version`|`str`|服务器版本，默认 `"1.0.0"`|
|`tools`|`list`|注册到服务器的工具列表|

**示例：**

```
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions, query

@tool("add", "将两个数相加", {"a": float, "b": float})
async def add(args):
    result = args["a"] + args["b"]
    return {"content": [{"type": "text", "text": f"结果：{result}"}]}

@tool("multiply", "将两个数相乘", {"a": float, "b": float})
async def multiply(args):
    result = args["a"] * args["b"]
    return {"content": [{"type": "text", "text": f"结果：{result}"}]}

# 创建计算器服务器
calculator = create_sdk_mcp_server(
    name="calculator",
    version="2.0.0",
    tools=[add, multiply],
)

# 将服务器注册到 options
options = ClaudeAgentOptions(
    mcp_servers={"calc": calculator},
    allowed_tools=["mcp__calc__add", "mcp__calc__multiply"],
)
```
> **工具命名规则：** 使用 `mcp__{服务器名}__{工具名}` 格式引用工具。
---

### `list_sessions()`
同步方法，列出历史会话信息。

```
def list_sessions(
    directory: str | None = None,
    limit: int | None = None,
    include_worktrees: bool = True
) -> list[SDKSessionInfo]
```
**参数说明：**

|参数|类型|说明|
|-|-|-|
|`directory`|`str`|指定项目目录，`None` 表示全局|
|`limit`|`int`|最多返回的会话数量|
|`include_worktrees`|`bool`|是否包含 Git worktree 会话|

`SDKSessionInfo`** 字段说明：**

|字段|类型|说明|
|-|-|-|
|`session_id`|`str`|唯一会话标识符|
|`summary`|`str`|会话显示标题|
|`last_modified`|`int`|最后修改时间（毫秒时间戳）|
|`file_size`|`int`|会话文件大小（字节）|
|`custom_title`|`str | None`|用户自定义标题|
|`first_prompt`|`str | None`|会话中第一个用户提示|
|`git_branch`|`str | None`|对应的 Git 分支|
|`cwd`|`str | None`|会话工作目录|

**示例：**

```
from claude_agent_sdk import list_sessions

# 列出某项目最近 10 个会话
sessions = list_sessions(directory="/path/to/project", limit=10)
for session in sessions:
    print(f"[{session.session_id}] {session.summary}")
    if session.git_branch:
        print(f"  分支：{session.git_branch}")
```
---

### `get_session_messages()`
同步方法，获取指定历史会话的消息列表。

```
def get_session_messages(
    session_id: str,
    directory: str | None = None,
    limit: int | None = None,
    offset: int = 0
) -> list[SessionMessage]
```
**参数说明：**

|参数|类型|说明|
|-|-|-|
|`session_id`|`str`|目标会话 ID|
|`directory`|`str`|项目目录（可选）|
|`limit`|`int`|最多返回的消息数|
|`offset`|`int`|跳过前 N 条消息，用于分页|

**示例：**

```
from claude_agent_sdk import list_sessions, get_session_messages

# 获取最新会话的前 20 条消息
sessions = list_sessions(limit=1)
if sessions:
    messages = get_session_messages(sessions[0].session_id, limit=20)
    for msg in messages:
        print(msg)
```
---

## 类参考
### `ClaudeSDKClient`
维持跨多次交换的会话状态，适用于需要上下文连续性的场景。

```
class ClaudeSDKClient:
    def __init__(
        self,
        options: ClaudeAgentOptions | None = None,
        transport: Transport | None = None
    )
```
**方法列表：**

|方法|说明|
|-|-|
|`connect(prompt)`|建立连接，可选初始提示|
|`query(prompt, session_id)`|发送提示，`session_id` 默认 `"default"`|
|`receive_messages()`|接收所有消息（异步迭代器）|
|`receive_response()`|接收当前轮次的响应（异步迭代器）|
|`interrupt()`|中断当前正在执行的任务|
|`set_permission_mode(mode)`|动态修改权限模式|
|`set_model(model)`|动态切换模型|
|`rewind_files(user_message_id)`|回滚到指定消息时的文件状态|
|`get_mcp_status()`|获取所有 MCP 服务器状态|
|`add_mcp_server(name, config)`|动态添加 MCP 服务器|
|`remove_mcp_server(name)`|动态移除 MCP 服务器|
|`get_server_info()`|获取服务器信息|
|`disconnect()`|断开连接，释放资源|

**推荐用法（上下文管理器）：**

```
async with ClaudeSDKClient() as client:
    await client.query("你好，Claude")
    async for message in client.receive_response():
        print(message)
```
> **警告：** 迭代消息时不要用 `break` 提前退出，可能导致 asyncio 资源清理问题。
**多轮对话示例：**

```
import asyncio
from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, TextBlock

async def main():
    async with ClaudeSDKClient() as client:
        # 第一轮
        await client.query("法国的首都是哪里？")
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Claude: {block.text}")

        # 第二轮 — 会话保留上下文，可以追问
        await client.query("那个城市的人口是多少？")
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Claude: {block.text}")

asyncio.run(main())
```
**中断任务示例：**

```
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(permission_mode="acceptEdits")
    async with ClaudeSDKClient(options=options) as client:
        await client.query("从 1 慢慢数到 100")

        # 等待 2 秒后中断
        await asyncio.sleep(2)
        await client.interrupt()
        print("任务已中断！")

        # 发送新任务
        await client.query("算了，只说一声你好就好")
        async for message in client.receive_response():
            print(message)

asyncio.run(main())
```
**流式输入示例：**

```
import asyncio
from claude_agent_sdk import ClaudeSDKClient

async def message_stream():
    yield {"type": "user", "message": {"role": "user", "content": "分析以下数据："}}
    await asyncio.sleep(0.5)
    yield {"type": "user", "message": {"role": "user", "content": "温度：25°C，湿度：60%"}}

async def main():
    async with ClaudeSDKClient() as client:
        await client.query(message_stream())
        async for message in client.receive_response():
            print(message)

asyncio.run(main())
```
---

## 配置类型
### `ClaudeAgentOptions`
控制 Claude Agent 行为的核心配置类。

```
@dataclass
class ClaudeAgentOptions:
    tools: list[str] | ToolsPreset | None = None
    allowed_tools: list[str] = []
    disallowed_tools: list[str] = []
    system_prompt: str | SystemPromptPreset | None = None
    mcp_servers: dict[str, McpServerConfig] | str | Path = {}
    permission_mode: PermissionMode | None = None
    continue_conversation: bool = False
    resume: str | None = None
    max_turns: int | None = None
    max_budget_usd: float | None = None
    model: str | None = None
    fallback_model: str | None = None
    betas: list[SdkBeta] = []
    output_format: dict[str, Any] | None = None
    cwd: str | Path | None = None
    can_use_tool: CanUseTool | None = None
    hooks: dict[HookEvent, list[HookMatcher]] | None = None
    enable_file_checkpointing: bool = False
    thinking: ThinkingConfig | None = None
    effort: Literal["low", "medium", "high", "max"] | None = None
    sandbox: SandboxSettings | None = None
    setting_sources: list[SettingSource] | None = None
    plugins: list[SdkPluginConfig] = []
```
**关键字段详解：**

|字段|类型|说明|
|-|-|-|
|`allowed_tools`|`list[str]`|自动批准使用的工具（不影响其他工具的请求）|
|`disallowed_tools`|`list[str]`|始终拒绝的工具（优先级最高，覆盖 allowed）|
|`permission_mode`|`str`|权限模式（见下表）|
|`system_prompt`|`str`|系统提示，设定 Claude 角色和行为规范|
|`cwd`|`str | Path`|工作目录|
|`max_turns`|`int`|最大对话轮次限制|
|`max_budget_usd`|`float`|最大消耗预算（美元）|
|`model`|`str`|指定使用的模型 ID|
|`enable_file_checkpointing`|`bool`|启用文件变更追踪，支持 `rewind_files()` 回滚|
|`setting_sources`|`list`|从文件系统加载哪些配置源|
|`resume`|`str`|继续指定的历史会话 ID|

`permission_mode`** 可选值：**

|值|说明|
|-|-|
|`"default"`|敏感操作需要用户确认|
|`"acceptEdits"`|自动接受文件编辑，其他操作仍需确认|
|`"plan"`|仅规划，不执行实际操作|
|`"bypassPermissions"`|跳过所有权限检查（谨慎使用）|

---

### `SettingSource`
控制从文件系统加载哪些配置文件。

```
SettingSource = Literal["user", "project", "local"]
```
|值|描述|对应文件路径|
|-|-|-|
|`"user"`|全局用户配置|`~/.claude/settings.json`|
|`"project"`|项目共享配置（提交到 Git）|`.claude/settings.json`|
|`"local"`|本地项目配置（不提交到 Git）|`.claude/settings.local.json`|

> **注意：** 默认值 `None` 时不加载任何文件系统配置，SDK 运行在完全隔离模式。
**加载项目 CLAUDE.md 文件的配置方式：**

```
options = ClaudeAgentOptions(
    system_prompt={"type": "preset", "preset": "claude_code"},
    setting_sources=["project"],  # 必须包含 "project" 才能加载 CLAUDE.md
)
```
---

### `ThinkingConfig`
配置 Claude 的「扩展思考」功能，让模型在回答前进行更深层的推理。

```
# 三种配置方式：

# 1. 自适应模式：Claude 自主决定是否需要深度思考
thinking = {"type": "adaptive"}

# 2. 启用模式：指定思考使用的 token 预算
thinking = {"type": "enabled", "budget_tokens": 8000}

# 3. 禁用模式：关闭扩展思考
thinking = {"type": "disabled"}
```
**示例：**

```
options = ClaudeAgentOptions(
    thinking={"type": "enabled", "budget_tokens": 16000},
    model="claude-opus-4-6",
)
```
---

### `SdkBeta`
启用测试版功能。

```
SdkBeta = Literal["context-1m-2025-08-07"]
```
`"context-1m-2025-08-07"`：为 Claude Sonnet 4.5/4 启用 **100 万 token** 的超大上下文窗口。

```
options = ClaudeAgentOptions(
    betas=["context-1m-2025-08-07"],
    model="claude-sonnet-4-6",
)
```
---

## 消息类型
所有从 `query()` 或 `receive_response()` 产出的消息均属于以下联合类型：

```
Message = UserMessage | AssistantMessage | SystemMessage | ResultMessage | StreamEvent
```
### `AssistantMessage`
Claude 的响应消息。

```
@dataclass
class AssistantMessage:
    content: list[ContentBlock]           # 内容块列表
    model: str                            # 使用的模型
    parent_tool_use_id: str | None = None # 父工具调用 ID（子 Agent 场景）
    error: AssistantMessageError | None = None  # 错误信息（如有）
```
**内容块类型：**

```
ContentBlock = TextBlock | ThinkingBlock | ToolUseBlock | ToolResultBlock
```
|类型|字段|说明|
|-|-|-|
|`TextBlock`|`text: str`|普通文本回复|
|`ThinkingBlock`|`thinking: str`, `signature: str`|扩展思考内容|
|`ToolUseBlock`|`id: str`, `name: str`, `input: dict`|工具调用|
|`ToolResultBlock`|`tool_use_id: str`, `content`, `is_error: bool`|工具结果|

### `ResultMessage`
会话结束时产出的汇总信息。

```
@dataclass
class ResultMessage:
    subtype: str                    # 结果类型
    duration_ms: int                # 总耗时（毫秒）
    duration_api_ms: int            # API 调用耗时（毫秒）
    is_error: bool                  # 是否发生错误
    num_turns: int                  # 对话轮次数
    session_id: str                 # 会话 ID
    total_cost_usd: float | None    # 总费用（美元）
    usage: dict[str, Any] | None    # Token 用量明细
    result: str | None              # 最终结果文本
    structured_output: Any          # 结构化输出
```
`usage`** 字段包含：**

* `input_tokens`：输入 token 数
* `output_tokens`：输出 token 数
* `cache_read_tokens`：缓存命中读取的 token 数
* `cache_write_tokens`：写入缓存的 token 数

**遍历消息示例：**

```
from claude_agent_sdk import query, AssistantMessage, ResultMessage, TextBlock, ThinkingBlock

async for message in query(prompt="解释量子计算"):
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, ThinkingBlock):
                print(f"[思考中] {block.thinking[:100]}...")
            elif isinstance(block, TextBlock):
                print(f"[回复] {block.text}")
    elif isinstance(message, ResultMessage):
        print(f"\n--- 会话结束 ---")
        print(f"总轮次：{message.num_turns}")
        print(f"总费用：${message.total_cost_usd:.4f}")
        if message.usage:
            print(f"输入 token：{message.usage.get('input_tokens', 0)}")
            print(f"输出 token：{message.usage.get('output_tokens', 0)}")
```
---

## 错误类型
```
ClaudeSDKError              # 所有 SDK 异常的基类
├── CLIConnectionError      # 连接 CLI 进程失败
│   └── CLINotFoundError    # 找不到 Claude Code CLI
├── ProcessError            # 进程非正常退出（含 exit_code 和 stderr）
└── CLIJSONDecodeError      # JSON 解析失败（含出错的 line 和 original_error）
```
**完整错误处理示例：**

```
from claude_agent_sdk import (
    query,
    CLINotFoundError,
    CLIConnectionError,
    ProcessError,
    CLIJSONDecodeError,
    ClaudeSDKError,
)

async def safe_query(prompt: str):
    try:
        async for message in query(prompt=prompt):
            print(message)
    except CLINotFoundError:
        print("错误：未找到 Claude Code CLI，请先安装并配置")
    except CLIConnectionError as e:
        print(f"连接失败：{e}")
    except ProcessError as e:
        print(f"进程异常退出，退出码：{e.exit_code}")
        print(f"标准错误输出：{e.stderr}")
    except CLIJSONDecodeError as e:
        print(f"JSON 解析失败，问题行：{e.line}")
        print(f"原始错误：{e.original_error}")
    except ClaudeSDKError as e:
        print(f"SDK 未知错误：{e}")
```
---

## Hook 系统
Hook 允许你在 Claude 执行特定事件时注入自定义逻辑，例如在工具调用前进行安全检查。

### 事件类型 (`HookEvent`)
```
HookEvent = Literal[
    "PreToolUse",          # 工具执行前（可阻止或修改输入）
    "PostToolUse",         # 工具执行成功后
    "PostToolUseFailure",  # 工具执行失败后
    "UserPromptSubmit",    # 用户提交提示时
    "Stop",                # Claude 停止执行时
    "SubagentStop",        # 子 Agent 停止时
    "PreCompact",          # 消息压缩（上下文裁剪）前
    "Notification",        # 通知事件
    "SubagentStart",       # 子 Agent 启动时
    "PermissionRequest",   # 权限决策请求时
]
```
### `HookMatcher`
定义事件匹配规则和对应的处理函数。

```
@dataclass
class HookMatcher:
    matcher: str | None = None      # 工具名匹配模式（如 "Bash"，"Write|Edit"）
    hooks: list[HookCallback] = []  # 处理函数列表
    timeout: float | None = None    # 超时时间（秒），默认 60 秒
```
### Hook 回调函数签名
```
async def my_hook(
    input_data: dict,      # 事件输入数据（含工具名、工具参数等）
    tool_use_id: str,      # 当前工具调用 ID
    context: dict          # 上下文信息
) -> dict:                 # 返回 Hook 输出
    ...
```
### Hook 输出格式
**同步 Hook 输出：**

```
{
    "continue_": bool,           # False 表示终止执行（注意有下划线）
    "suppressOutput": bool,      # True 则隐藏 hook 的 stdout
    "decision": "block",         # 阻止当前操作
    "systemMessage": str,        # 向用户显示的警告信息
    "reason": str,               # 给 Claude 的反馈原因
    "hookSpecificOutput": {      # Hook 特定的结构化输出
        "hookEventName": "PreToolUse",
        # 权限决策（仅 PreToolUse / PermissionRequest）
        "permissionDecision": "allow" | "deny" | "ask",
        "permissionDecisionReason": str,
        # 修改工具输入
        "updatedInput": dict,
        # 额外上下文（给 Claude）
        "additionalContext": str,
    }
}
```
**异步 Hook 输出（用于长耗时操作）：**

```
{
    "async_": True,            # 标记为异步（注意有下划线）
    "asyncTimeout": int,       # 最长等待时间（毫秒）
}
```
### 安全检查 Hook 完整示例
```
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

# 危险命令拦截
async def validate_bash_command(input_data, tool_use_id, context):
    if input_data.get("tool_name") == "Bash":
        command = input_data.get("tool_input", {}).get("command", "")

        # 拦截危险命令
        dangerous_patterns = ["rm -rf /", "dd if=", "> /dev/sda"]
        for pattern in dangerous_patterns:
            if pattern in command:
                return {
                    "hookSpecificOutput": {
                        "hookEventName": "PreToolUse",
                        "permissionDecision": "deny",
                        "permissionDecisionReason": f"危险命令已被拦截：{pattern}",
                    }
                }
    return {}

# 审计日志 Hook
async def audit_log(input_data, tool_use_id, context):
    tool_name = input_data.get("tool_name", "unknown")
    print(f"[审计] 工具调用：{tool_name} | ID：{tool_use_id}")
    return {}

options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            HookMatcher(
                matcher="Bash",
                hooks=[validate_bash_command],
                timeout=10,
            ),
            HookMatcher(
                matcher=None,  # None 表示匹配所有工具
                hooks=[audit_log],
            ),
        ],
    }
)

async for message in query(prompt="列出当前目录文件", options=options):
    print(message)
```
---

## 权限系统
### `CanUseTool` 回调
比 Hook 更简洁的权限控制方式，直接决定工具是否可以使用。

```
# 类型签名
CanUseTool = Callable[
    [str, dict[str, Any], ToolPermissionContext],
    Awaitable[PermissionResult]
]

# 允许结果
@dataclass
class PermissionResultAllow:
    behavior: Literal["allow"] = "allow"
    updated_input: dict[str, Any] | None = None  # 可选：修改工具输入

# 拒绝结果
@dataclass
class PermissionResultDeny:
    behavior: Literal["deny"] = "deny"
    message: str = ""          # 向用户显示的原因
    interrupt: bool = False    # 是否同时中断整个任务
```
**自定义权限控制示例：**

```
from claude_agent_sdk import (
    query, ClaudeAgentOptions,
    PermissionResultAllow, PermissionResultDeny
)

async def custom_permission(tool_name: str, input_data: dict, context) -> dict:
    # 禁止写入系统目录
    if tool_name == "Write":
        file_path = input_data.get("file_path", "")
        if file_path.startswith("/system/") or file_path.startswith("/etc/"):
            return PermissionResultDeny(
                message=f"不允许写入系统目录：{file_path}"
            )

    # 将配置文件写入重定向到沙箱目录
    if tool_name in ["Write", "Edit"]:
        file_path = input_data.get("file_path", "")
        if "config" in file_path and not file_path.startswith("./sandbox/"):
            safe_path = f"./sandbox/{file_path.lstrip('/')}"
            print(f"[安全] 重定向写入：{file_path} -> {safe_path}")
            return PermissionResultAllow(
                updated_input={**input_data, "file_path": safe_path}
            )

    return PermissionResultAllow(updated_input=input_data)

options = ClaudeAgentOptions(
    can_use_tool=custom_permission,
    permission_mode="acceptEdits",
)
```
---

## 沙箱配置
沙箱提供系统级隔离，防止 Claude 执行危险操作。

### `SandboxSettings`
```
class SandboxSettings(TypedDict, total=False):
    enabled: bool                          # 启用沙箱隔离
    autoAllowBashIfSandboxed: bool         # 沙箱模式下自动批准 bash 命令
    excludedCommands: list[str]            # 始终绕过沙箱的命令（如 ["docker", "git"]）
    allowUnsandboxedCommands: bool         # 允许模型请求在沙箱外执行
    network: SandboxNetworkConfig          # 网络访问配置
    ignoreViolations: SandboxIgnoreViolations
    enableWeakerNestedSandbox: bool
```
### `SandboxNetworkConfig`
```
class SandboxNetworkConfig(TypedDict, total=False):
    allowLocalBinding: bool           # 允许绑定本地端口（如启动 Web 服务器）
    allowUnixSockets: list[str]       # 允许访问指定的 Unix socket 路径
    allowAllUnixSockets: bool         # 允许访问所有 Unix socket
    httpProxyPort: int                # HTTP 代理端口
    socksProxyPort: int               # SOCKS 代理端口
```
> **安全警告：** 若在 `allowUnixSockets` 中包含 `/var/run/docker.sock`，将等同于授予模型完整的宿主机访问权限，请谨慎使用。
**沙箱使用示例：**

```
from claude_agent_sdk import query, ClaudeAgentOptions

sandbox_settings = {
    "enabled": True,
    "autoAllowBashIfSandboxed": True,
    "network": {
        "allowLocalBinding": True,   # 允许绑定端口（运行测试服务器）
    },
    "excludedCommands": ["git"],     # git 命令绕过沙箱
}

options = ClaudeAgentOptions(
    sandbox=sandbox_settings,
    permission_mode="acceptEdits",
)

async for message in query(
    prompt="构建并测试我的项目",
    options=options,
):
    print(message)
```
---

## MCP 服务器配置
除了 SDK 内置服务器，还可以连接外部 MCP 服务器。

### 三种连接类型
**stdio 类型（本地子进程）：**

```
from claude_agent_sdk import ClaudeAgentOptions

options = ClaudeAgentOptions(
    mcp_servers={
        "my_tool": {
            "type": "stdio",          # 可省略（向后兼容）
            "command": "python",
            "args": ["-m", "my_mcp_server"],
            "env": {"API_KEY": "xxx"},
        }
    }
)
```
**SSE 类型（服务端发送事件）：**

```
options = ClaudeAgentOptions(
    mcp_servers={
        "remote_tool": {
            "type": "sse",
            "url": "https://my-server.example.com/mcp",
            "headers": {"Authorization": "Bearer token123"},
        }
    }
)
```
**HTTP 类型：**

```
options = ClaudeAgentOptions(
    mcp_servers={
        "api_tool": {
            "type": "http",
            "url": "https://my-server.example.com/mcp",
            "headers": {"X-API-Key": "secret"},
        }
    }
)
```
---

## 内置工具 I/O 参考
Claude 内置以下工具，可通过 `allowed_tools` / `disallowed_tools` 控制使用权限。

|工具|关键输入字段|关键输出字段|
|-|-|-|
|`Bash`|`command`, `timeout`, `run_in_background`|`output`, `exitCode`, `killed`, `shellId`|
|`Read`|`file_path`, `offset`, `limit`|`content`, `total_lines`|
|`Write`|`file_path`, `content`|`message`, `bytes_written`|
|`Edit`|`file_path`, `old_string`, `new_string`, `replace_all`|`message`, `replacements`|
|`Glob`|`pattern`, `path`|`matches`, `count`|
|`Grep`|`pattern`, `path`, `glob`, `output_mode`|`matches`, `total_matches`|
|`WebFetch`|`url`, `prompt`|`response`, `status_code`|
|`WebSearch`|`query`, `allowed_domains`, `blocked_domains`|`results`, `total_results`|
|`Agent`|`description`, `prompt`, `subagent_type`|`result`, `usage`, `duration_ms`|
|`BashOutput`|`bash_id`, `filter`|`output`, `status`, `exitCode`|
|`KillBash`|`shell_id`|`message`, `shell_id`|

**限制工具使用示例：**

```
options = ClaudeAgentOptions(
    # 自动批准文件读写，无需用户确认
    allowed_tools=["Read", "Write", "Edit", "Glob", "Grep"],
    # 禁止联网操作
    disallowed_tools=["WebFetch", "WebSearch"],
)
```
---

## 完整示例
### 示例一：自定义工具 + 多轮对话
```
import asyncio
from claude_agent_sdk import (
    ClaudeSDKClient, ClaudeAgentOptions,
    tool, create_sdk_mcp_server,
    AssistantMessage, TextBlock, ResultMessage,
)

@tool("calculate", "执行数学计算", {"expression": str})
async def calculate(args):
    try:
        # 使用受限的 eval（生产环境请使用更安全的数学解析库）
        result = eval(args["expression"], {"__builtins__": {}})
        return {"content": [{"type": "text", "text": f"计算结果：{result}"}]}
    except Exception as e:
        return {"content": [{"type": "text", "text": f"计算出错：{e}"}]}

async def main():
    # 创建内置 MCP 服务器
    my_server = create_sdk_mcp_server("utilities", tools=[calculate])

    options = ClaudeAgentOptions(
        mcp_servers={"utils": my_server},
        allowed_tools=["mcp__utils__calculate"],
        system_prompt="你是一个数学助手，擅长使用 calculate 工具解答数学问题。",
    )

    async with ClaudeSDKClient(options=options) as client:
        questions = [
            "123 乘以 456 等于多少？",
            "那个结果再加上 789 呢？",
        ]

        for question in questions:
            print(f"\n用户：{question}")
            await client.query(question)

            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"Claude：{block.text}")
                elif isinstance(message, ResultMessage):
                    if message.total_cost_usd:
                        print(f"[费用：${message.total_cost_usd:.4f}]")

asyncio.run(main())
```
### 示例二：带安全 Hook 的代码执行
```
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

# 安全 Hook：检查并记录所有 Bash 命令
async def security_hook(input_data, tool_use_id, context):
    tool_name = input_data.get("tool_name", "")

    if tool_name == "Bash":
        command = input_data.get("tool_input", {}).get("command", "")
        print(f"[安全检查] 即将执行：{command}")

        # 拦截删除操作
        if any(danger in command for danger in ["rm -rf", "rm -f /", "mkfs"]):
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "包含破坏性命令，已拦截",
                }
            }

        # 对可疑命令要求用户确认
        if "sudo" in command:
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "ask",
                    "permissionDecisionReason": "命令包含 sudo，需要确认",
                }
            }

    return {}

async def main():
    options = ClaudeAgentOptions(
        permission_mode="acceptEdits",
        allowed_tools=["Read", "Glob"],  # 读操作自动批准
        hooks={
            "PreToolUse": [
                HookMatcher(matcher="Bash", hooks=[security_hook], timeout=30),
            ],
        },
    )

    async for message in query(
        prompt="分析当前目录结构，然后用 echo 命令输出分析摘要",
        options=options,
    ):
        print(message)

asyncio.run(main())
```
### 示例三：历史会话管理
```
from claude_agent_sdk import list_sessions, get_session_messages
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
import asyncio

def show_recent_sessions(project_dir: str, n: int = 5):
    """展示最近的会话列表"""
    sessions = list_sessions(directory=project_dir, limit=n)
    print(f"最近 {len(sessions)} 个会话：")
    for i, session in enumerate(sessions, 1):
        print(f"  {i}. [{session.session_id[:8]}...] {session.summary}")
        if session.git_branch:
            print(f"     分支：{session.git_branch}")
    return sessions

async def continue_session(session_id: str):
    """继续历史会话"""
    options = ClaudeAgentOptions(
        resume=session_id,
        permission_mode="acceptEdits",
    )
    async with ClaudeSDKClient(options=options) as client:
        await client.query("继续我们上次的工作，从哪里停下的？")
        async for message in client.receive_response():
            print(message)

# 使用示例
sessions = show_recent_sessions("/path/to/my/project")
if sessions:
    asyncio.run(continue_session(sessions[0].session_id))
```
---

## 常见问题
**Q：**`query()`** 和 **`ClaudeSDKClient.query()`** 有什么区别？**

`query()` 顶级函数每次调用创建新会话，适合独立任务。`ClaudeSDKClient.query()` 在同一客户端会话中发送请求，Claude 能记住之前的对话内容。

**Q：为什么不能在接收消息时用 **`break`**？**

`ClaudeSDKClient` 的消息迭代器持有底层 asyncio 资源，提前退出会导致资源未正确清理，可能引发警告或内存泄漏。如需提前停止，应使用 `await client.interrupt()`。

**Q：**`allowed_tools`** 和 **`disallowed_tools`** 的优先级？**

`disallowed_tools` 优先级高于 `allowed_tools`，即一个工具同时出现在两个列表中时，以拒绝为准。

**Q：如何控制 token 费用？**

使用 `max_budget_usd` 参数设置预算上限，通过 `ResultMessage.total_cost_usd` 监控实际消耗。也可以用 `max_turns` 限制对话轮次。

**Q：SDK 沙箱和 **`permission_mode="bypassPermissions"`** 有什么区别？**

沙箱是系统级隔离（OS 层面限制），`bypassPermissions` 只是跳过 SDK 的权限确认逻辑，不提供真正的系统隔离。生产环境推荐使用沙箱而非绕过权限。
