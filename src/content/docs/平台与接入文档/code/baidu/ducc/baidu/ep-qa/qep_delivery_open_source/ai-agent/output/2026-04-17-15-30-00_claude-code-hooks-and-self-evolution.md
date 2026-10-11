---
title: "Claude Code Hooks 与自我进化机制深度解析"
description: "讨论时间: 2026-04-17 主题: Claude Code 内部机制、Hooks 系统、自我进化功能设计"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-15-30-00_claude-code-hooks-and-self-evolution.md"
---
# Claude Code Hooks 与自我进化机制深度解析

> 讨论时间: 2026-04-17
> 主题: Claude Code 内部机制、Hooks 系统、自我进化功能设计

---

## 1. Claude SDK 的 Client 与 Query 区别

### query() - 简单一次性调用

```python
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

async for message in query(
    prompt="解释这个代码库",
    options=ClaudeAgentOptions(allowed_tools=["Read", "Glob", "Grep"])
):
    if isinstance(message, ResultMessage):
        print(message.result)
```

**特点**: 简单直接，返回异步迭代器，适合快速使用场景。

### ClaudeSDKClient - 完整控制

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async with ClaudeSDKClient(options=options) as client:
    await client.query("解释这个代码库")
    async for message in client.receive_response():
        # 处理消息
```

**特点**:
- 支持 **自定义工具**（通过 SDK MCP servers）
- 支持 **中断执行**（`client.interrupt()`）
- 资源自动清理（context manager）
- 更细粒度的控制

### 选择建议

| 场景 | 推荐 |
|------|------|
| 简单任务、快速原型 | `query()` |
| 需要自定义工具 | `ClaudeSDKClient` |
| 需要中断/暂停能力 | `ClaudeSDKClient` |
| 复杂生命周期管理 | `ClaudeSDKClient` |

---

## 2. Hooks 系统详解

### Hook 的本质

Hook 就是在特定事件触发时运行的代码：

```
[事件发生] → [Claude Code 调用你的脚本] → [你的代码处理] → [返回结果]
```

### Hook 类型

| Hook | 触发时机 | 用途 |
|------|---------|------|
| `SessionStart` | 会话开始 | 加载上下文、检测项目 |
| `UserPromptSubmit` | 用户发送消息后 | Prompt 审查、添加上下文 |
| `PreToolUse` | 工具执行前 | 拦截/修改/阻止工具 |
| `PostToolUse` | 工具执行后 | 记录、监控、自动格式化 |
| `Stop` | 响应结束 | 总结、保存状态 |
| `SessionEnd` | 会话结束 | 清理、统计 |

### Hook 的输入输出协议

```
stdin  → JSON（hook input，包含 transcript_path, session_id 等）
stdout → JSON（hook output，控制是否继续等）
```

**任何能读 stdin、写 stdout 的语言都可以写 Hook**：

```json
// Node.js
{"command": "node scripts/my-hook.js"}

// Python
{"command": "python3 scripts/my-hook.py"}

// Bash
{"command": "bash scripts/my-hook.sh"}
```

### Hook Input 结构 (BaseHookInput)

```python
class BaseHookInput(TypedDict):
    session_id: str        # 会话 ID
    transcript_path: str   # 完整对话记录文件路径
    cwd: str              # 当前工作目录
    permission_mode: str   # 权限模式
```

### Hook Output 结构 (SyncHookJSONOutput)

```python
class SyncHookJSONOutput(TypedDict):
    continue_: bool          # False = 阻止继续
    stopReason: str          # 停止原因
    decision: Literal["block"]  # 阻止决策
    systemMessage: str       # 显示给用户的警告
    reason: str              # 反馈给 Claude 的原因
    hookSpecificOutput: dict # 特定 hook 的输出
```

---

## 3. transcript_path 详解

### 文件位置

```
~/.claude/projects/{project-hash}/{session-id}.jsonl
```

### 文件格式

JSONL 格式，每行一条记录。

### 记录类型

#### 1. 用户消息 (`type: "user"`)

```json
{
  "type": "user",
  "message": {
    "role": "user",
    "content": "用户问了什么"
  },
  "uuid": "58de6278-...",
  "timestamp": "2026-04-17T06:33:48.300Z",
  "sessionId": "19f2d39e-..."
}
```

#### 2. Assistant Thinking (`type: "assistant"`)

```json
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{
      "type": "thinking",
      "thinking": "我在想..."
    }]
  }
}
```

#### 3. 工具调用 (`type: "assistant"`)

```json
{
  "type": "assistant",
  "message": {
    "content": [{
      "type": "tool_use",
      "name": "Bash",
      "input": {"command": "ls -la"}
    }],
    "stop_reason": "tool_use"
  }
}
```

#### 4. 工具结果 (`type: "user"`)

```json
{
  "type": "user",
  "message": {
    "content": [{
      "type": "tool_result",
      "tool_use_id": "toolu_...",
      "content": "工具输出内容"
    }]
  }
}
```

---

## 4. Everything-Claude-Code 的自我进化系统

### 核心概念：Instinct（本能）

不是学习完整技能，而是学习**原子化的小行为**：

```yaml
---
id: prefer-functional-style
trigger: "when writing new functions"
confidence: 0.7
domain: "code-style"
scope: project
---

# Prefer Functional Style

## Action
Use functional patterns over classes when appropriate.

## Evidence
- Observed 5 instances of functional pattern preference
```

### 整体流程

```
Session Activity (对话)
      │
      │ PreToolUse/PostToolUse Hooks (observe.sh)
      │ 100% 可靠捕获每个工具调用
      ▼
observations.jsonl (按项目隔离)
~/.claude/homunculus/projects/<hash>/observations.jsonl
      │
      │ Observer Agent (后台 Haiku 分析)
      │ 每 5 分钟或每 20 条观察触发
      ▼
Instincts (原子化学习结果)
~/.claude/homunculus/projects/<hash>/instincts/personal/
      │
      │ /evolve 命令聚类
      ▼
Evolved Artifacts
  - skills/   → 完整技能
  - commands/ → 快捷命令
  - agents/   → 专用 Agent
```

### 模式检测

| 模式类型 | 例子 | 生成的 Instinct |
|---------|------|----------------|
| 用户纠正 | "不要用 X，用 Y" | "When doing X, prefer Y" |
| 错误修复 | 报错后的修复步骤 | "When encountering error X, try Y" |
| 重复工作流 | Grep → Read → Edit | "When modifying code, search first" |
| 工具偏好 | 总是用 Grep | "Use Grep tool instead of bash grep" |

### 置信度系统

```
观察次数 → 初始置信度
1-2 次   → 0.3 (tentative)
3-5 次   → 0.5 (moderate)
6-10 次  → 0.7 (strong)
11+ 次   → 0.85 (very strong)

置信度变化：
+0.05  每次确认观察
-0.1   每次矛盾观察
-0.02  每周无观察（衰减）
```

### 作用域隔离

| 项目级 (project) | 全局 (global) |
|-----------------|--------------|
| React hooks 偏好 | 输入验证 |
| Django 模式 | Grep before Edit |
| 测试文件放 __tests__/ | Git 提交规范 |

---

## 5. 自定义自我进化方案

### 简化版实现思路

只用 **Stop hook + transcript_path**，提取完整排查路径：

```python
#!/usr/bin/env python3
# hooks/extract-path.py

import sys
import json
from pathlib import Path
from datetime import datetime

def extract_path(transcript_lines):
    path = {
        "user_question": None,
        "thinking_steps": [],
        "tool_chain": [],
        "conclusion": None
    }

    for line in transcript_lines:
        record = json.loads(line)
        msg = record.get("message", {})
        content = msg.get("content")

        # 提取用户问题
        if record["type"] == "user" and isinstance(content, str):
            path["user_question"] = content

        # 提取 thinking
        if record["type"] == "assistant" and isinstance(content, list):
            for block in content:
                if block.get("type") == "thinking":
                    path["thinking_steps"].append(block["thinking"])
                elif block.get("type") == "tool_use":
                    path["tool_chain"].append({
                        "tool": block["name"],
                        "input": block["input"]
                    })
                elif block.get("type") == "text":
                    path["conclusion"] = block.get("text")

    return path

def main():
    input_data = json.loads(sys.stdin.read())
    transcript_path = input_data.get("transcript_path")
    session_id = input_data.get("session_id")

    if transcript_path and Path(transcript_path).exists():
        lines = Path(transcript_path).read_text().strip().split('\n')
        path = extract_path(lines)

        # 保存到每日文件
        today = datetime.now().strftime("%Y-%m-%d")
        output_file = Path.home() / ".claude" / "paths" / f"{today}.jsonl"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "a") as f:
            f.write(json.dumps({
                "session_id": session_id,
                "timestamp": datetime.now().isoformat(),
                **path
            }, ensure_ascii=False) + "\n")

    print(json.dumps(input_data))

if __name__ == "__main__":
    main()
```

### Hook 配置

```json
{
  "hooks": {
    "Stop": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/hooks/extract-path.py"
      }],
      "description": "从 transcript 提取排查路径"
    }]
  }
}
```

---

## 6. Claude Code 消息处理机制

### 中断 vs 排队

| Claude 状态 | 你按 Enter | 结果 |
|------------|-----------|------|
| **Streaming 文本** | 可中断 | 立即处理新消息 |
| **执行工具中** | 不可中断 | 消息排队，等工具完成 |
| **等待你输入** | - | 直接处理 |

### 流程图

```
┌─────────────────────────────────────────────────────────────┐
│                   Claude 响应阶段                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Thinking/Streaming] ←── 可中断 ←── 你的 Enter            │
│         │                                                   │
│         ▼                                                   │
│  [Tool Execution]     ←── 不可中断，消息排队等待            │
│    - Bash 命令                                              │
│    - 文件读写                                               │
│    - API 调用                                               │
│         │                                                   │
│         ▼                                                   │
│  [Tool Result]                                              │
│         │                                                   │
│         ▼                                                   │
│  [继续 Thinking/Streaming] ←── 可中断                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### SDK 实现

```python
# 中断方法
async def interrupt(self) -> None:
    await self._send_control_request({"subtype": "interrupt"})

# 消息队列
self._message_send, self._message_receive = anyio.create_memory_object_stream(
    max_buffer_size=100  # 最大 100 条消息
)
```

---

## 7. UserPromptSubmit Hook 做 Prompt 审查

### 实现方案

#### 方案 1：规则检查（免费、快速）

```python
#!/usr/bin/env python3
import sys
import json
import re

BLOCKED_PATTERNS = [
    r"删除.*数据库",
    r"rm\s+-rf",
    r"DROP\s+TABLE",
]

def check_prompt(prompt: str) -> tuple[bool, str]:
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return False, f"匹配到敏感模式: {pattern}"
    return True, ""

def main():
    input_data = json.loads(sys.stdin.read())
    prompt = input_data.get("prompt", "")

    allowed, reason = check_prompt(prompt)

    if not allowed:
        output = {
            "continue": False,
            "decision": "block",
            "stopReason": f"Prompt 被拒绝: {reason}",
            "systemMessage": f"⚠️ {reason}"
        }
    else:
        output = {"continue": True}

    print(json.dumps(output))

if __name__ == "__main__":
    main()
```

#### 方案 2：小模型审查（Haiku）

```python
def check_with_haiku(prompt: str) -> dict:
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"]},
        json={
            "model": "claude-haiku-4-5",
            "max_tokens": 100,
            "messages": [{
                "role": "user",
                "content": f"判断是否合规，回复 JSON: {prompt}"
            }]
        }
    )
    return json.loads(response.json()["content"][0]["text"])
```

### 模型选择建议

| 方案 | 优点 | 缺点 |
|-----|------|------|
| 规则检查 | 免费、快速、无延迟 | 不够智能 |
| Haiku 模型 | 便宜、够智能 | 有延迟 (~0.5s) |
| 同一个 Claude | 最智能 | 太贵、没必要 |

**推荐**: 规则 + Haiku 组合

---

## 8. 关键文件路径

| 文件/目录 | 用途 |
|----------|------|
| `~/.claude/settings.json` | 全局配置 |
| `~/.claude/projects/{hash}/` | 项目级数据 |
| `~/.claude/projects/{hash}/{session}.jsonl` | 会话 transcript |
| `~/.claude/homunculus/` | 自我进化数据 |
| `~/.claude/plugins/` | 已安装插件 |

---

## 总结

1. **Hooks 是核心扩展点** - 可以在各个阶段介入 Claude 的执行流程
2. **transcript_path 是金矿** - 包含完整对话历史，可用于学习和分析
3. **自我进化有多种实现** - ECC 的 instinct 系统是一种成熟方案
4. **Prompt 审查可行** - 用 UserPromptSubmit hook + 规则/小模型
5. **消息处理有两种模式** - Streaming 可中断，工具执行需等待
