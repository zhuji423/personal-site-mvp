---
title: "stdout/stdin：进程间通信的管道"
description: "从操作系统基础到 Claude SDK 的完整原理"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-01-45-23_stdin_stdout_explained.md"
---
# stdout/stdin：进程间通信的管道

> 从操作系统基础到 Claude SDK 的完整原理

---

## TL;DR

**stdout** = 标准输出流 = 进程的"嘴巴"（用来说话）
**stdin** = 标准输入流 = 进程的"耳朵"（用来听）

CLI 通过 stdout "说出" JSON 消息，SDK 通过 stdin "听到" 这些消息。

---

## 一、什么是 stdin/stdout？（操作系统基础）

### 类比：电话通话

```
你（Python进程）              朋友（CLI子进程）
    ↓                              ↓
   话筒（stdout）                 耳朵（stdin）
   耳朵（stdin）                  话筒（stdout）
    ↓                              ↓
   你说话 ──────→ 朋友听到
   你听到 ←────── 朋友说话
```

### 每个进程都有 3 个标准流

```python
import sys

# 任何 Python 进程都有这 3 个：
sys.stdin   # 标准输入（从哪里读数据）
sys.stdout  # 标准输出（往哪里写数据）
sys.stderr  # 标准错误（错误信息输出）
```

**默认情况**（在终端运行）：
```python
# 当你运行 python script.py
sys.stdin  → 键盘输入
sys.stdout → 屏幕显示
sys.stderr → 屏幕显示（红色）

# 示例
print("Hello")  # 等价于 sys.stdout.write("Hello\n")
# "Hello" 会显示在屏幕上
```

---

## 二、父子进程的 stdin/stdout 连接

### 场景：Python 启动一个子进程

```python
import subprocess

# Python（父进程）启动一个子进程
process = subprocess.Popen(
    ["python", "child.py"],
    stdin=subprocess.PIPE,   # 👈 创建管道
    stdout=subprocess.PIPE,  # 👈 创建管道
    stderr=subprocess.PIPE
)
```

**发生了什么？**

```
┌──────────────────────────────────────────────────────────────┐
│               Python 父进程（你的代码）                        │
│                                                               │
│  process.stdin  ──→ [管道] ──→ 子进程的 sys.stdin             │
│  process.stdout ←── [管道] ←── 子进程的 sys.stdout            │
└──────────────────────────────────────────────────────────────┘

管道（Pipe）= 连接两个进程的"水管"
```

**通信示例**：

```python
# 父进程（你的 Python 代码）
process = subprocess.Popen(
    ["python", "-c", "import sys; print(sys.stdin.read())"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)

# 父进程写入数据到子进程的 stdin
process.stdin.write(b"Hello from parent\n")
process.stdin.flush()

# 父进程从子进程的 stdout 读取数据
output = process.stdout.read()
print(output)  # b"Hello from parent\n"
```

**数据流**：
```
父进程: process.stdin.write("Hello")
    ↓ 通过管道
子进程: sys.stdin.read() → "Hello"
子进程: print("World")
    ↓ 通过管道
父进程: process.stdout.read() → "World"
```

---

## 三、Claude CLI 的 stdin/stdout 通信

### SDK 如何启动 CLI

```python
# SDK 内部代码（简化版）
import anyio
from anyio.streams.file import FileWriteStream, FileReadStream

# 启动 CLI 子进程
process = await anyio.open_process(
    ["claude", "--sdk-mode"],  # CLI 命令
    stdin=anyio.subprocess.PIPE,   # 创建 stdin 管道
    stdout=anyio.subprocess.PIPE,  # 创建 stdout 管道
    stderr=anyio.subprocess.PIPE
)

# 现在可以通过管道通信：
# - 写入 process.stdin → CLI 的 stdin
# - 读取 process.stdout → CLI 的 stdout
```

### 完整通信图

```
┌─────────────────────────────────────────────────────────────┐
│            Python 进程（SDK）                                 │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  await process.stdin.write(                           │  │
│  │      '{"type": "user", "message": "帮我排查链接"}\n'   │  │
│  │  )                                                    │  │
│  └────────────────┬──────────────────────────────────────┘  │
│                   │                                         │
│                   │ stdin 管道（JSON 消息）                  │
│                   ↓                                         │
└───────────────────┼─────────────────────────────────────────┘
                    │
┌───────────────────┼─────────────────────────────────────────┐
│                   ↓                                         │
│            Claude CLI 子进程                                 │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  line = sys.stdin.readline()                          │  │
│  │  message = json.loads(line)                           │  │
│  │  # {"type": "user", "message": "帮我排查链接"}         │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  处理消息...                                           │  │
│  │  Claude 决定调用 Bash 工具                             │  │
│  │  执行: mysql -e "select * from tasks"                 │  │
│  │  获得结果: "trace_id=abc123"                           │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  检测到有 PostToolUse Hook，发送事件：                 │  │
│  │                                                        │  │
│  │  sys.stdout.write(json.dumps({                        │  │
│  │      "type": "hook_callback",                         │  │
│  │      "hook_event": "PostToolUse",                     │  │
│  │      "tool_name": "Bash",                             │  │
│  │      "tool_input": {"command": "..."},                │  │
│  │      "tool_response": "trace_id=abc123"               │  │
│  │  }) + "\n")                                           │  │
│  │  sys.stdout.flush()  # 立即发送                       │  │
│  └────────────────┬──────────────────────────────────────┘  │
│                   │                                         │
│                   │ stdout 管道（JSON 消息）                 │
│                   ↓                                         │
└───────────────────┼─────────────────────────────────────────┘
                    │
┌───────────────────┼─────────────────────────────────────────┐
│                   ↓                                         │
│            Python 进程（SDK）                                 │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  line = await process.stdout.readline()               │  │
│  │  message = json.loads(line)                           │  │
│  │  # {                                                  │  │
│  │  #   "type": "hook_callback",                         │  │
│  │  #   "hook_event": "PostToolUse",                     │  │
│  │  #   ...                                              │  │
│  │  # }                                                  │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  识别到 Hook 事件，调用用户的回调函数：                 │  │
│  │                                                        │  │
│  │  for hook_func in self.hooks["PostToolUse"]:          │  │
│  │      await hook_func(hook_input=message)              │  │
│  └───────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## 四、回答你的问题

### Q1: stdout 是什么？

**A**: stdout（标准输出）是每个进程都有的"输出通道"。

```python
# 在终端运行
print("Hello")  # 输出到 stdout → 显示在屏幕

# 在子进程中
sys.stdout.write("Hello\n")  # 输出到 stdout → 父进程可以读取
```

**类比**：
- stdout = 进程的"嘴巴"
- stdin = 进程的"耳朵"

---

### Q2: 为什么 CLI 会发消息到 stdout？

**A**: 因为 SDK 启动 CLI 时，把 CLI 的 stdout 连接到了一个管道，SDK 可以从这个管道读取数据。

```python
# SDK 启动 CLI
process = await anyio.open_process(
    ["claude"],
    stdout=PIPE  # 👈 创建管道，连接 CLI 的 stdout 到 SDK
)

# CLI 写入 stdout
sys.stdout.write("Hello\n")  # CLI 内部代码

# SDK 从管道读取
line = await process.stdout.readline()  # SDK 读到 "Hello\n"
```

**为什么用 stdout？**
- 这是操作系统标准的进程间通信方式
- 简单、可靠、跨平台

---

### Q3: 那个 JSON 是 CLI 的输出吗？

**A**: 是的！CLI 把 JSON 写到 stdout，SDK 从 stdout 读取。

```python
# CLI 内部（伪代码）
def on_tool_complete(tool_name, tool_input, tool_response):
    """工具执行完成后"""

    # 检测到有 PostToolUse Hook
    if has_posttooluse_hook():
        # 构造 JSON 消息
        message = {
            "type": "hook_callback",
            "hook_event": "PostToolUse",
            "tool_name": tool_name,
            "tool_input": tool_input,
            "tool_response": tool_response,
            "callback_id": generate_id()
        }

        # 👉 写入 stdout（发送给 SDK）
        sys.stdout.write(json.dumps(message) + "\n")
        sys.stdout.flush()  # 立即发送，不缓冲
```

```python
# SDK 内部（伪代码）
async def read_messages_from_cli():
    """持续读取 CLI 的输出"""

    while True:
        # 👉 从 stdout 读取一行
        line = await process.stdout.readline()

        if not line:
            break  # CLI 关闭了 stdout

        # 解析 JSON
        message = json.loads(line)

        # 处理不同类型的消息
        if message["type"] == "hook_callback":
            # 触发 Hook
            await handle_hook_callback(message)
        elif message["type"] == "message":
            # Claude 的文本响应
            yield message
        # ... 其他类型
```

---

## 五、为什么用 JSON？

### 因为需要结构化数据

```python
# ❌ 如果 CLI 直接输出文本
sys.stdout.write("工具Bash执行完成，结果是trace_id=abc123\n")

# SDK 收到后需要解析：
# "工具名是什么？Bash？还是其他？"
# "结果是什么？trace_id=abc123？还是整句话？"
# 太难解析了！

# ✅ 使用 JSON（结构化数据）
sys.stdout.write(json.dumps({
    "type": "hook_callback",
    "tool_name": "Bash",
    "tool_response": "trace_id=abc123"
}) + "\n")

# SDK 收到后直接解析：
message = json.loads(line)
tool_name = message["tool_name"]  # "Bash" ✅
tool_response = message["tool_response"]  # "trace_id=abc123" ✅
```

---

## 六、混合内容的处理

### CLI 的 stdout 可能包含多种内容

```python
# CLI 的输出流（stdout）可能包含：

1. Claude 的文本响应（给用户看的）
   "正在查询数据库..."

2. Hook 事件（给 SDK 的）
   {"type": "hook_callback", ...}

3. 工具调用结果（给 SDK 的）
   {"type": "tool_result", ...}

4. 错误信息（如果用 stderr 就不会混在一起）
   "Error: connection timeout"
```

**如何区分？**

方法1：按行读取，每行是一个 JSON
```python
async for line in process.stdout:
    try:
        message = json.loads(line)
        # 结构化消息
        if message["type"] == "hook_callback":
            ...
    except json.JSONDecodeError:
        # 不是 JSON，是纯文本
        print(line)  # 显示给用户
```

方法2：使用特殊前缀
```python
# CLI 输出
sys.stdout.write("TEXT: 正在查询数据库...\n")
sys.stdout.write("JSON: {\"type\": \"hook_callback\", ...}\n")

# SDK 读取
if line.startswith("TEXT:"):
    text = line[5:]  # 纯文本
elif line.startswith("JSON:"):
    message = json.loads(line[5:])  # JSON
```

方法3：使用不同的流（最干净）
```python
# 文本输出到 stdout
sys.stdout.write("正在查询数据库...\n")

# JSON 输出到 stderr（或专门的文件描述符）
sys.stderr.write(json.dumps({...}) + "\n")

# SDK 分别读取
text_line = await process.stdout.readline()  # 文本
json_line = await process.stderr.readline()  # JSON
```

---

## 七、完整示例：父子进程通信

### 子进程（child.py）

```python
#!/usr/bin/env python3
import sys
import json
import time

def main():
    # 从 stdin 读取消息
    for line in sys.stdin:
        message = json.loads(line)

        # 模拟工具执行
        if message["type"] == "execute_tool":
            tool_name = message["tool_name"]

            # 执行工具...
            time.sleep(1)
            result = f"Result of {tool_name}"

            # 发送 Hook 事件到 stdout
            hook_event = {
                "type": "hook_callback",
                "hook_event": "PostToolUse",
                "tool_name": tool_name,
                "tool_response": result
            }

            sys.stdout.write(json.dumps(hook_event) + "\n")
            sys.stdout.flush()  # 立即发送

if __name__ == "__main__":
    main()
```

### 父进程（parent.py）

```python
#!/usr/bin/env python3
import asyncio
import json

async def main():
    # 启动子进程
    process = await asyncio.create_subprocess_exec(
        "python", "child.py",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    # 发送消息给子进程
    request = {"type": "execute_tool", "tool_name": "Bash"}
    process.stdin.write((json.dumps(request) + "\n").encode())
    await process.stdin.drain()

    # 读取子进程的响应
    line = await process.stdout.readline()
    response = json.loads(line.decode())

    print("收到 Hook 事件:", response)
    # 输出: 收到 Hook 事件: {'type': 'hook_callback', 'hook_event': 'PostToolUse', ...}

    # 关闭
    process.stdin.close()
    await process.wait()

asyncio.run(main())
```

**运行效果**：
```
父进程: 发送 {"type": "execute_tool", "tool_name": "Bash"}
    ↓ stdin 管道
子进程: 收到消息，执行工具
子进程: 发送 {"type": "hook_callback", ...}
    ↓ stdout 管道
父进程: 收到 Hook 事件
父进程: 调用用户的 Hook 函数
```

---

## 八、关键概念总结

### 1. stdin/stdout 是什么？

```
stdin  = 标准输入 = 进程的"耳朵"（读数据）
stdout = 标准输出 = 进程的"嘴巴"（写数据）
stderr = 标准错误 = 进程的"警告喇叭"（错误信息）
```

### 2. 管道（Pipe）是什么？

```
管道 = 连接两个进程的"水管"
父进程写入 → 管道 → 子进程读取
子进程写入 → 管道 → 父进程读取
```

### 3. 为什么用 stdout？

```
1. 操作系统标准的进程间通信方式
2. 简单、可靠、跨平台
3. 不需要网络、不需要文件
```

### 4. JSON 的作用

```
结构化数据 → 易于解析
{
  "type": "hook_callback",
  "tool_name": "Bash",
  "tool_response": "..."
}

比纯文本好解析多了！
```

---

## 九、面试问答

### Q: stdout 是什么？

**A**: stdout 是每个进程的标准输出流，进程可以通过它输出数据。在父子进程中，父进程可以读取子进程的 stdout。

---

### Q: CLI 为什么要发消息到 stdout？

**A**: 因为 SDK 启动 CLI 时，把 CLI 的 stdout 连接到了一个管道。CLI 写入 stdout，SDK 就能从管道读取。这是标准的进程间通信方式。

---

### Q: 那个 JSON 是 CLI 的输出吗？

**A**: 是的。CLI 执行完工具后，把 Hook 事件序列化成 JSON，写入 stdout。SDK 从 stdout 读取这行 JSON，解析后触发用户的 Hook 函数。

---

### Q: 为什么用 JSON 而不是纯文本？

**A**: JSON 是结构化数据，包含明确的字段（type、tool_name、tool_response 等），易于解析。纯文本难以准确提取这些信息。

---

## 十、类比总结（记忆版）

```
Claude SDK 和 CLI 的关系 = 你和朋友打电话

SDK（你）           CLI（朋友）
   ↓                    ↓
 话筒（stdin）        耳朵（stdin）
 耳朵（stdout）       话筒（stdout）
   ↓                    ↓
你说话: {"type": "execute_tool"}
   ↓ 电话线（管道）
朋友听到，去做事
朋友说话: {"type": "hook_callback"}
   ↓ 电话线（管道）
你听到，触发 Hook
```

**核心**：
- stdin = 输入通道（听）
- stdout = 输出通道（说）
- 管道 = 连接两个进程的"电话线"
- JSON = 结构化的"对话内容"

---

**文档版本**: v1.0
**最后更新**: 2026-04-17
**面试准备**: ⭐⭐⭐⭐⭐
