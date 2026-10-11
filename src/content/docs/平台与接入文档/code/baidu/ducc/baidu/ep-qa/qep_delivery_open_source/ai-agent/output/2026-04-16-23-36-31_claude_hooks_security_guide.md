---
title: "你的逻辑"
description: "Claude Agent SDK Hooks 安全拦截完整指南"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-16-23-36-31_claude_hooks_security_guide.md"
---
[# Claude Agent SDK Hooks 安全拦截完整指南

> 文档生成时间：2026-04-16 23:36:31
> 主题：使用 PreToolUse 和 PostToolUse Hooks 拦截不安全操作

---

## 目录

1. [核心概念](#核心概念)
2. [Hooks 能力矩阵](#hooks-能力矩阵)
3. [PreToolUse 安全拦截示例](#pretooluse-安全拦截示例)
4. [PostToolUse 审计日志示例](#posttooluse-审计日志示例)
5. [组合使用多层防护](#组合使用多层防护)
6. [实际效果演示](#实际效果演示)
7. [最佳实践总结](#最佳实践总结)

---

## 核心概念

### ✅ Hooks 可以做什么？

**PreToolUse Hook** 的能力：
- ✅ 在工具执行**之前**拦截
- ✅ 检查工具参数是否安全
- ✅ 返回 `permissionDecision: "deny"` 来阻止执行
- ✅ 修改工具输入参数（`updatedInput`）
- ✅ 提供自定义的拒绝原因

**PostToolUse Hook** 的能力：
- ✅ 在工具执行**之后**检查结果
- ✅ 添加额外的上下文信息（`additionalContext`）
- ✅ 记录审计日志
- ✅ 增强工具输出内容

### Hook 函数签名

```python
from claude_agent_sdk.types import (
    HookInput,           # 输入数据（PreToolUseHookInput | PostToolUseHookInput | ...）
    HookContext,         # Hook上下文（包含signal等）
    HookJSONOutput       # 返回值类型
)

async def my_hook_callback(
    hook_input: HookInput,      # 强类型的输入数据
    tool_use_id: str | None,    # 工具调用ID
    context: HookContext        # 上下文信息
) -> HookJSONOutput:            # 返回控制指令
    # 你的逻辑
    pass
```

---

## Hooks 能力矩阵

| 特性 | PreToolUse | PostToolUse |
|------|-----------|-------------|
| **执行时机** | 工具执行前 | 工具执行后 |
| **可以阻止执行** | ✅ 可以（`permissionDecision: "deny"`） | ❌ 不能（已执行） |
| **可以修改输入** | ✅ `updatedInput` | ❌ 无法修改已执行的操作 |
| **可以添加上下文** | ❌ 不支持 | ✅ `additionalContext` |
| **典型用途** | 安全拦截、参数校验、输入脱敏 | 审计日志、结果增强、合规检查 |

---

## PreToolUse 安全拦截示例

### 场景1：阻止危险的 Bash 命令 💣

拦截可能导致系统损坏的命令（如 `rm -rf /`、`DROP DATABASE` 等）。

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher
from claude_agent_sdk.types import PreToolUseHookInput, HookContext, HookJSONOutput

async def security_check_before_bash(
    hook_input: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """在执行Bash命令前进行安全检查"""

    # 获取要执行的命令
    command = hook_input["tool_input"].get("command", "")

    # 危险命令黑名单
    dangerous_patterns = [
        "rm -rf /",           # 删除根目录
        "rm -rf ~",           # 删除home目录
        "DROP DATABASE",      # 删除数据库
        "DROP TABLE",         # 删除表
        "sudo rm",            # 带sudo的删除
        "mkfs",               # 格式化磁盘
        ":(){:|:&};:",        # fork炸弹
        "dd if=/dev/zero",    # 磁盘破坏
        "chmod 777 /",        # 危险权限修改
        "chown root:root /",  # 危险所有权修改
    ]

    # 检查是否包含危险命令
    for pattern in dangerous_patterns:
        if pattern.lower() in command.lower():
            # 🚨 拦截！返回deny
            return {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",  # 👈 阻止执行
                "permissionDecisionReason": f"❌ 检测到危险命令: {pattern}",
                "continue_": True,  # 继续会话，但不执行此工具
                "decision": "block",
                "systemMessage": f"🛡️ 安全策略阻止了危险命令的执行",
                "reason": f"命令包含危险模式 '{pattern}'，已被安全策略拦截"
            }

    # ✅ 安全，允许执行
    return {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow"
    }

# 配置hooks
options = ClaudeAgentOptions(
    permission_mode='acceptEdits',
    hooks={
        "PreToolUse": [
            HookMatcher(
                matcher="Bash",  # 只拦截Bash工具
                hooks=[security_check_before_bash],
                timeout=10.0  # 10秒超时
            )
        ]
    }
)

client = ClaudeSDKClient(options=options)
```

---

### 场景2：限制文件写入路径 📁

只允许写入到指定的白名单目录，防止误操作覆盖重要文件。

```python
async def check_file_write_path(
    hook_input: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """只允许写入到指定的安全目录"""

    file_path = hook_input["tool_input"].get("file_path", "")

    # 白名单：只允许这些目录
    allowed_dirs = [
        "/tmp/",
        "/workspace/",
        "/home/user/safe_zone/",
        "/var/app/output/"
    ]

    # 黑名单：绝对不允许的路径
    forbidden_paths = [
        "/etc/",
        "/usr/bin/",
        "/boot/",
        "~/.ssh/",
        "~/.bashrc",
        "~/.zshrc"
    ]

    # 检查黑名单
    for forbidden in forbidden_paths:
        if file_path.startswith(forbidden):
            return {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": f"禁止写入系统关键路径: {forbidden}",
                "systemMessage": f"🚫 禁止修改系统关键文件: {file_path}"
            }

    # 检查白名单
    is_safe = any(file_path.startswith(safe_dir) for safe_dir in allowed_dirs)

    if not is_safe:
        return {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"路径 {file_path} 不在允许的目录内",
            "systemMessage": f"🚫 只能写入到以下目录: {', '.join(allowed_dirs)}"
        }

    return {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow"
    }

# 配置：拦截Write和Edit工具
options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            HookMatcher(
                matcher="Write|Edit",  # 👈 使用正则匹配多个工具
                hooks=[check_file_write_path]
            )
        ]
    }
)
```

---

### 场景3：自动脱敏敏感信息 🔐

检测并修改包含硬编码密钥的命令，自动替换为环境变量引用。

```python
async def sanitize_sensitive_data(
    hook_input: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """自动脱敏敏感信息"""

    command = hook_input["tool_input"].get("command", "")

    # 检测是否包含API密钥
    import re

    # 匹配模式：api_key=xxx, token="xxx", password: "xxx"
    sensitive_patterns = [
        r'(api[_-]?key)\s*[=:]\s*["\']?([a-zA-Z0-9_\-]{20,})["\']?',
        r'(token)\s*[=:]\s*["\']?([a-zA-Z0-9_\-]{20,})["\']?',
        r'(password)\s*[=:]\s*["\']?([^\s"\']{8,})["\']?',
        r'(secret)\s*[=:]\s*["\']?([a-zA-Z0-9_\-]{20,})["\']?',
    ]

    has_sensitive = False
    sanitized_command = command

    for pattern in sensitive_patterns:
        match = re.search(pattern, sanitized_command, re.IGNORECASE)
        if match:
            has_sensitive = True
            key_name = match.group(1)
            # 替换为环境变量引用
            sanitized_command = re.sub(
                pattern,
                rf'{key_name}="${{{key_name.upper()}}}"',
                sanitized_command,
                flags=re.IGNORECASE
            )

    if has_sensitive:
        return {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "updatedInput": {  # 👈 修改输入参数
                **hook_input["tool_input"],
                "command": sanitized_command
            },
            "reason": "⚠️ 检测到硬编码密钥，已自动替换为环境变量引用"
        }

    return {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow"
    }
```

---

### 场景4：防止大文件写入 💾

限制单次写入文件的大小，防止磁盘空间耗尽。

```python
async def check_file_size_limit(
    hook_input: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """限制文件写入大小"""

    content = hook_input["tool_input"].get("content", "")
    file_path = hook_input["tool_input"].get("file_path", "")

    # 计算内容大小（字节）
    content_size = len(content.encode('utf-8'))
    max_size = 10 * 1024 * 1024  # 10MB

    if content_size > max_size:
        size_mb = content_size / (1024 * 1024)
        return {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"文件大小 {size_mb:.2f}MB 超过限制 10MB",
            "systemMessage": f"🚫 单次写入文件不能超过 10MB（当前: {size_mb:.2f}MB）"
        }

    return {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow"
    }

# 配置
options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            HookMatcher(
                matcher="Write",
                hooks=[check_file_size_limit]
            )
        ]
    }
)
```

---

## PostToolUse 审计日志示例

### 场景5：完整审计日志记录 📝

记录所有工具调用的详细信息，用于合规审计和问题追溯。

```python
from claude_agent_sdk.types import PostToolUseHookInput
import json
from datetime import datetime
from pathlib import Path

async def audit_log_after_tool(
    hook_input: PostToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """记录所有工具调用的审计日志"""

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "session_id": hook_input["session_id"],
        "tool_name": hook_input["tool_name"],
        "tool_use_id": tool_use_id,
        "cwd": hook_input["cwd"],
        "transcript_path": hook_input["transcript_path"],
        "input": hook_input["tool_input"],
        "response_preview": str(hook_input["tool_response"])[:500],  # 只记录前500字符
        "response_size": len(str(hook_input["tool_response"]))
    }

    # 确保日志目录存在
    log_dir = Path("/var/log/claude_audit")
    log_dir.mkdir(parents=True, exist_ok=True)

    # 按日期分文件记录
    log_file = log_dir / f"audit_{datetime.now().strftime('%Y-%m-%d')}.jsonl"

    # 追加写入
    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    # 添加上下文信息（会显示给Claude）
    return {
        "hookEventName": "PostToolUse",
        "additionalContext": f"✅ 操作已记录到审计日志（ID: {tool_use_id}）"
    }

# 配置：监控所有工具
options = ClaudeAgentOptions(
    hooks={
        "PostToolUse": [
            HookMatcher(
                matcher=None,  # 👈 None表示匹配所有工具
                hooks=[audit_log_after_tool]
            )
        ]
    }
)
```

---

### 场景6：执行时间监控 ⏱️

记录工具执行时间，发现性能瓶颈。

```python
import time

# 使用全局字典存储开始时间（实际应用中用更好的状态管理）
_tool_start_times = {}

async def record_tool_start(
    hook_input: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """PreToolUse: 记录开始时间"""
    if tool_use_id:
        _tool_start_times[tool_use_id] = time.time()

    return {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow"
    }

async def record_tool_duration(
    hook_input: PostToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """PostToolUse: 计算执行时间"""

    if tool_use_id and tool_use_id in _tool_start_times:
        start_time = _tool_start_times.pop(tool_use_id)
        duration = time.time() - start_time

        # 如果执行时间过长，记录警告
        if duration > 30:  # 超过30秒
            warning = f"⚠️ 工具 {hook_input['tool_name']} 执行时间过长: {duration:.2f}秒"
            print(warning)

            return {
                "hookEventName": "PostToolUse",
                "additionalContext": warning
            }

    return {
        "hookEventName": "PostToolUse"
    }

# 配置：同时使用Pre和Post来测量时间
options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            HookMatcher(matcher=None, hooks=[record_tool_start])
        ],
        "PostToolUse": [
            HookMatcher(matcher=None, hooks=[record_tool_duration])
        ]
    }
)
```

---

## 组合使用多层防护

### 完整的企业级安全配置 🛡️

结合多个hooks实现深度防御策略。

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher

# 组合所有安全策略
options = ClaudeAgentOptions(
    permission_mode='acceptEdits',
    resume="my-session-id",
    setting_sources=["user", "project"],
    allowed_tools=["Read", "Write", "Edit", "Grep", "Glob", "Bash", "Skill"],
    cwd="/workspace",

    hooks={
        # ========== PreToolUse：执行前拦截 ==========
        "PreToolUse": [
            # 1. Bash命令安全检查
            HookMatcher(
                matcher="Bash",
                hooks=[
                    security_check_before_bash,    # 危险命令黑名单
                    sanitize_sensitive_data,       # 敏感信息脱敏
                    record_tool_start              # 记录开始时间
                ],
                timeout=10.0
            ),

            # 2. 文件写入路径限制
            HookMatcher(
                matcher="Write|Edit",
                hooks=[
                    check_file_write_path,         # 路径白名单
                    check_file_size_limit,         # 大小限制
                    record_tool_start
                ],
                timeout=5.0
            ),

            # 3. 所有工具的通用检查
            HookMatcher(
                matcher=None,  # 匹配所有工具
                hooks=[record_tool_start]
            )
        ],

        # ========== PostToolUse：执行后审计 ==========
        "PostToolUse": [
            HookMatcher(
                matcher=None,  # 匹配所有工具
                hooks=[
                    audit_log_after_tool,          # 完整审计日志
                    record_tool_duration           # 性能监控
                ]
            )
        ]
    }
)

client = ClaudeSDKClient(options=options)
```

---

## 实际效果演示

### 场景A：用户让Claude执行危险命令

**用户输入**：
```
请执行命令：rm -rf /important_data
```

**执行流程**：
1. ✅ Claude生成Bash工具调用
2. ✅ **PreToolUse hook触发** → `security_check_before_bash` 执行
3. 🚨 检测到危险模式 `"rm -rf"`
4. ❌ 返回 `permissionDecision: "deny"`
5. ❌ **工具不会执行**
6. 📢 Claude收到反馈："命令包含危险模式 'rm -rf /'，已被安全策略拦截"
7. 💬 Claude告诉用户："抱歉，这个命令被安全策略阻止了，因为它可能导致数据丢失"

---

### 场景B：用户让Claude写入系统文件

**用户输入**：
```
请修改 /etc/hosts 文件
```

**执行流程**：
1. ✅ Claude生成Edit工具调用：`file_path="/etc/hosts"`
2. ✅ **PreToolUse hook触发** → `check_file_write_path` 执行
3. 🚨 检测到路径在黑名单中（`/etc/`）
4. ❌ 返回 `permissionDecision: "deny"`
5. ❌ **工具不会执行**
6. 💬 Claude告诉用户："无法修改 /etc/hosts，这是系统关键文件，被安全策略保护"

---

### 场景C：自动脱敏硬编码密钥

**用户输入**：
```
请执行：curl -H "api_key: sk-1234567890abcdef" https://api.example.com
```

**执行流程**：
1. ✅ Claude生成Bash工具调用
2. ✅ **PreToolUse hook触发** → `sanitize_sensitive_data` 执行
3. 🔍 检测到硬编码API密钥
4. ✏️ 自动修改为：`curl -H "api_key: ${API_KEY}" https://api.example.com`
5. ✅ 返回 `permissionDecision: "allow"` + `updatedInput`
6. ✅ 执行修改后的安全命令
7. 📢 Claude收到提示："检测到硬编码密钥，已自动替换为环境变量引用"
8. 💬 Claude告诉用户："我已将硬编码的密钥替换为环境变量 $API_KEY，请确保该变量已设置"

---

## 最佳实践总结

### 1. 分层防御策略 🏰

```
第一层：PreToolUse - 参数校验和黑名单拦截
第二层：PreToolUse - 输入脱敏和修正
第三层：Permission System - 用户权限控制
第四层：PostToolUse - 审计日志和合规检查
```

### 2. Hooks 优先级规则

- 同一个 `HookMatcher` 中的多个 hooks **按顺序执行**
- 任何一个 hook 返回 `deny` 就会终止执行
- 第一个返回 `updatedInput` 的修改会生效

### 3. 性能考虑 ⚡

- **设置合理的 timeout**（建议 5-10 秒）
- **避免在 hooks 中执行耗时操作**（如大文件读写、网络请求）
- **使用异步 I/O**（日志写入用 `aiofiles`）
- **matcher 尽量具体**（不要所有工具都拦截，除非必要）

### 4. 安全配置清单 ✅

对于生产环境，建议配置：

- [ ] Bash工具：危险命令黑名单拦截
- [ ] Write/Edit工具：路径白名单限制
- [ ] 所有工具：硬编码密钥检测和脱敏
- [ ] 所有工具：完整审计日志记录
- [ ] 所有工具：执行时间监控
- [ ] 文件操作：大小限制（防止磁盘耗尽）
- [ ] 网络请求：域名白名单（如果使用WebFetch）

### 5. 调试技巧 🔧

```python
async def debug_hook(
    hook_input: HookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """调试用hook：打印所有参数"""
    import json
    print(f"=== Hook Debug ===")
    print(f"Event: {hook_input.get('hook_event_name')}")
    print(f"Tool: {hook_input.get('tool_name')}")
    print(f"Input: {json.dumps(hook_input.get('tool_input'), indent=2)}")
    print(f"Tool Use ID: {tool_use_id}")
    print("==================")

    # 允许继续
    return {
        "hookEventName": hook_input["hook_event_name"],
        "permissionDecision": "allow" if "PreToolUse" in hook_input.get("hook_event_name", "") else None
    }
```

### 6. 错误处理

```python
async def safe_hook_wrapper(
    hook_input: HookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    """带错误处理的hook包装器"""
    try:
        # 你的实际逻辑
        return await your_actual_hook(hook_input, tool_use_id, context)
    except Exception as e:
        # 出错时默认拒绝（安全优先）
        print(f"Hook执行出错: {e}")
        return {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"Hook执行异常: {str(e)}"
        }
```

---

## 附录：完整类型定义参考

### PreToolUseHookInput

```python
class PreToolUseHookInput(TypedDict):
    hook_event_name: Literal["PreToolUse"]
    session_id: str
    transcript_path: str
    cwd: str
    permission_mode: NotRequired[str]
    tool_name: str          # 工具名称（如 "Bash", "Write"）
    tool_input: dict[str, Any]  # 工具参数
```

### PreToolUseHookSpecificOutput

```python
class PreToolUseHookSpecificOutput(TypedDict):
    hookEventName: Literal["PreToolUse"]
    permissionDecision: NotRequired[Literal["allow", "deny", "ask"]]  # 核心决策
    permissionDecisionReason: NotRequired[str]  # 决策原因
    updatedInput: NotRequired[dict[str, Any]]   # 修改后的输入参数
```

### PostToolUseHookInput

```python
class PostToolUseHookInput(TypedDict):
    hook_event_name: Literal["PostToolUse"]
    session_id: str
    transcript_path: str
    cwd: str
    permission_mode: NotRequired[str]
    tool_name: str
    tool_input: dict[str, Any]
    tool_response: Any      # 工具执行结果
```

### PostToolUseHookSpecificOutput

```python
class PostToolUseHookSpecificOutput(TypedDict):
    hookEventName: Literal["PostToolUse"]
    additionalContext: NotRequired[str]  # 添加给Claude的上下文信息
```

---

## 参考资源

- [Claude Agent SDK 官方文档](https://docs.anthropic.com/en/docs/claude-code)
- [Hooks 完整文档](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [安全最佳实践](https://docs.anthropic.com/en/docs/claude-code/security)

---

**文档版本**：v1.0
**适用SDK版本**：claude-agent-sdk >= 0.0.20
**维护者**：Ducc AI Team
**最后更新**：2026-04-16
]()