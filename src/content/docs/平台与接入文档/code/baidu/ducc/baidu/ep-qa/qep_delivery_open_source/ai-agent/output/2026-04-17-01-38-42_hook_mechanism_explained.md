---
title: "Hook 机制深度解析：从原理到实战"
description: "面试必备：PostToolUse Hook 如何将工具信息传递给 SessionManager"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-01-38-42_hook_mechanism_explained.md"
---
# Hook 机制深度解析：从原理到实战

> 面试必备：PostToolUse Hook 如何将工具信息传递给 SessionManager

---

## TL;DR

**Hook 本质**：就是普通的**回调函数**（Callback），和 JavaScript 的 `addEventListener` 一模一样！

```javascript
// JavaScript 的回调（你肯定熟悉）
button.addEventListener('click', function(event) {
    console.log('按钮被点击了', event.target);
});

// Claude SDK 的 Hook（一样的原理）
options = ClaudeAgentOptions(
    hooks={
        "PostToolUse": [
            HookMatcher(hooks=[my_callback_function])
        ]
    }
)
```

---

## 一、Hook 机制的本质（用类比理解）

### 类比1：餐厅的服务铃

```
你（顾客）在餐厅吃饭：
    ↓
服务员（Claude CLI）在厨房做菜
    ↓
每做好一道菜，服务员就按一下服务铃 🔔
    ↓
你听到铃声，知道菜好了
    ↓
你可以记录："第3道菜，用时15分钟"
```

**对应关系**：
- 服务员 = Claude CLI（执行工具）
- 按铃 = 触发 Hook
- 你听到铃声 = Hook 回调函数被执行
- 你记录 = 更新 SessionManager

### 类比2：外卖订单的推送通知

```
你点了外卖：
    ↓
骑手（Claude CLI）接单、取餐、配送
    ↓
每个关键节点，系统给你发推送：
    - "商家已接单" 📱
    - "骑手已取餐" 📱
    - "骑手配送中" 📱
    ↓
你的手机收到推送，更新订单状态
```

**对应关系**：
- 骑手 = Claude CLI
- 推送通知 = Hook 事件
- 你的手机 = SessionManager
- 更新状态 = session.update_progress()

---

## 二、Hook 机制的完整流程（逐步讲解）

### 步骤1：你注册 Hook（告诉 SDK 你要监听）

```python
# 你的代码
async def my_hook_function(hook_input, tool_use_id, context):
    """这是你的回调函数"""
    print(f"工具 {hook_input['tool_name']} 执行完了！")

    # 可以访问你的任何对象
    session_manager.update_something(...)

    return {"hookEventName": "PostToolUse"}

# 把回调函数"注册"到 SDK
options = ClaudeAgentOptions(
    hooks={
        "PostToolUse": [
            HookMatcher(
                matcher=None,  # 匹配所有工具
                hooks=[my_hook_function]  # 👈 你的回调函数
            )
        ]
    }
)

client = ClaudeSDKClient(options=options)
await client.connect()
```

**这一步做了什么？**
- SDK 内部保存了你的函数引用：`self.hooks = {"PostToolUse": [my_hook_function]}`
- 就像 `button.addEventListener('click', my_function)` 一样

---

### 步骤2：Claude 执行工具

```python
# 用户发送消息
await client.query("帮我排查这个链接")

# Claude 生成计划，决定调用工具
# 比如：先调用 Bash 工具执行 SQL 查询
```

**CLI 进程内部发生了什么？**

```
Claude CLI 子进程：
    ↓
1. 收到用户消息 "帮我排查链接"
    ↓
2. Claude 思考，决定调用 Bash 工具
    ↓
3. 执行: bash -c "mysql -e 'select * from tasks'"
    ↓
4. 获得结果: "trace_id=abc123"
    ↓
5. 👉 检测到有 PostToolUse Hook 注册
    ↓
6. 通过 stdout 发送事件给 SDK:
   {
     "type": "hook_callback",
     "hook_event": "PostToolUse",
     "tool_name": "Bash",
     "tool_input": {"command": "mysql -e ..."},
     "tool_response": "trace_id=abc123",
     "callback_id": "hook-123"
   }
```

---

### 步骤3：SDK 收到事件，触发你的 Hook

```python
# SDK 内部代码（简化版）
class Query:
    def __init__(self, hooks):
        self.hooks = hooks  # 保存你注册的回调函数

    async def handle_message(self, message):
        """处理 CLI 发来的消息"""

        if message["type"] == "hook_callback":
            # 👉 收到 Hook 事件！

            # 提取信息
            hook_event = message["hook_event"]  # "PostToolUse"
            hook_input = {
                "tool_name": message["tool_name"],
                "tool_input": message["tool_input"],
                "tool_response": message["tool_response"]
            }

            # 👉 调用你注册的回调函数
            if hook_event in self.hooks:
                for hook_func in self.hooks[hook_event]:
                    # 🔥 关键：就是普通的函数调用！
                    result = await hook_func(
                        hook_input=hook_input,
                        tool_use_id=message.get("tool_use_id"),
                        context={}
                    )

            # 把结果发回 CLI
            await self.send_to_cli({
                "type": "hook_response",
                "callback_id": message["callback_id"],
                "result": result
            })
```

**关键点**：
- SDK 只是个"中间人"
- 收到 CLI 的通知 → 调用你的函数 → 把结果返回 CLI
- **你的函数在你的 Python 进程中执行！**

---

### 步骤4：你的 Hook 函数执行（访问 SessionManager）

```python
# 你的 Hook 函数
async def my_hook_function(hook_input, tool_use_id, context):
    # hook_input = {
    #     "tool_name": "Bash",
    #     "tool_input": {"command": "mysql -e ..."},
    #     "tool_response": "trace_id=abc123"
    # }

    # 👉 这里可以访问你的任何对象！
    # 因为这是在你的 Python 进程中执行的

    session = session_manager.get_session("user123")
    session.update_progress_from_tool(
        tool_name=hook_input["tool_name"],
        tool_input=hook_input["tool_input"],
        tool_response=hook_input["tool_response"]
    )

    # 完成
    return {"hookEventName": "PostToolUse"}
```

**为什么能访问 SessionManager？**
- Hook 函数就是普通的 Python 函数
- 和你的其他代码在同一个进程
- 当然可以访问任何对象！

---

## 三、完整数据流图（重要！）

```
┌─────────────────────────────────────────────────────────────────┐
│                    你的 Python 进程                               │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  1. 你的代码：注册 Hook                                    │   │
│  │                                                           │   │
│  │  async def my_hook(hook_input, ...):                      │   │
│  │      session.update_progress(...)                         │   │
│  │                                                           │   │
│  │  options = ClaudeAgentOptions(                            │   │
│  │      hooks={"PostToolUse": [my_hook]}                     │   │
│  │  )                                                        │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   ↓                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  2. SDK 保存你的 Hook 函数                                 │   │
│  │                                                           │   │
│  │  self.hooks = {                                           │   │
│  │      "PostToolUse": [my_hook]  ← 函数引用                 │   │
│  │  }                                                        │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   │ stdin: "帮我排查链接"                        │
│                   ↓                                              │
└───────────────────┼──────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│              Claude CLI 子进程（独立进程）                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  3. Claude 决定调用 Bash 工具                              │   │
│  │                                                           │   │
│  │  Tool: Bash                                               │   │
│  │  Input: {"command": "mysql -e 'select...'"}              │   │
│  │  ↓                                                        │   │
│  │  执行命令...                                               │   │
│  │  ↓                                                        │   │
│  │  Output: "trace_id=abc123"                                │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   │ 检测到有 PostToolUse Hook                    │
│                   ↓                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  4. CLI 发送 Hook 事件到 stdout                            │   │
│  │                                                           │   │
│  │  stdout.write(json.dumps({                                │   │
│  │      "type": "hook_callback",                             │   │
│  │      "hook_event": "PostToolUse",                         │   │
│  │      "tool_name": "Bash",                                 │   │
│  │      "tool_input": {"command": "..."},                    │   │
│  │      "tool_response": "trace_id=abc123",                  │   │
│  │      "callback_id": "hook-123"                            │   │
│  │  }))                                                      │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
└───────────────────┼──────────────────────────────────────────────┘
                    │
                    │ stdout（JSON 事件）
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│                    你的 Python 进程                               │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  5. SDK 从 stdout 读到 Hook 事件                           │   │
│  │                                                           │   │
│  │  message = json.loads(stdout_line)                        │   │
│  │  # {                                                      │   │
│  │  #   "type": "hook_callback",                             │   │
│  │  #   "hook_event": "PostToolUse",                         │   │
│  │  #   ...                                                  │   │
│  │  # }                                                      │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   ↓                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  6. SDK 调用你注册的 Hook 函数                             │   │
│  │                                                           │   │
│  │  for hook_func in self.hooks["PostToolUse"]:              │   │
│  │      result = await hook_func(                            │   │
│  │          hook_input={...},                                │   │
│  │          tool_use_id=None,                                │   │
│  │          context={}                                       │   │
│  │      )                                                    │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   ↓                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  7. 你的 Hook 函数执行（在你的进程中！）                    │   │
│  │                                                           │   │
│  │  async def my_hook(hook_input, ...):                      │   │
│  │      # 可以访问你的任何对象                                │   │
│  │      session = session_manager.get_session("user123")     │   │
│  │      session.update_progress_from_tool(                   │   │
│  │          tool_name="Bash",                                │   │
│  │          tool_input={...},                                │   │
│  │          tool_response="trace_id=abc123"                  │   │
│  │      )                                                    │   │
│  │      return {"hookEventName": "PostToolUse"}              │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   ↓                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  8. SessionManager 更新进度                                │   │
│  │                                                           │   │
│  │  session.progress = TaskProgress(                         │   │
│  │      stage="查询数据库",                                   │   │
│  │      progress_percent=25.0,                               │   │
│  │      latest_message="执行SQL查询"                          │   │
│  │  )                                                        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  9. 用户查询进度（任何时候都可以）                          │   │
│  │                                                           │   │
│  │  progress = session.progress  ← 直接读取！                │   │
│  │  return f"当前进度: {progress.progress_percent}%"          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 四、Hook 如何访问 SessionManager？（3种方式）

### 方式1：通过闭包捕获（推荐）

```python
class SessionManager:
    def start_client_for_session(self, session: SessionInfo):
        """为 Session 启动 Client"""

        # 👉 定义 Hook 函数（在这个方法内部）
        async def progress_hook(hook_input, tool_use_id, context):
            # ✅ 通过闭包访问外部的 session 变量
            session.update_progress_from_tool(
                tool_name=hook_input["tool_name"],
                tool_input=hook_input["tool_input"],
                tool_response=hook_input["tool_response"]
            )
            return {"hookEventName": "PostToolUse"}

        # 创建 Options（包含 Hook）
        options = ClaudeAgentOptions(
            hooks={
                "PostToolUse": [
                    HookMatcher(hooks=[progress_hook])  # 👈 传入闭包
                ]
            }
        )

        # 启动 Client
        client = ClaudeSDKClient(options=options)
        await client.connect()
        session.client = client
```

**原理**：
```python
# 闭包的例子（简化）
def outer(session):
    def inner():
        session.value = 123  # ✅ 可以访问外部变量
    return inner

f = outer(my_session)
f()  # 执行时，inner 能访问 my_session
```

---

### 方式2：通过全局变量

```python
# 全局 SessionManager
global_manager = SessionManager()

# Hook 函数
async def global_hook(hook_input, tool_use_id, context):
    # ✅ 访问全局变量
    session_id = hook_input["session_id"]
    session = global_manager.sessions[session_id]
    session.update_progress(...)
    return {"hookEventName": "PostToolUse"}

# 注册
options = ClaudeAgentOptions(
    hooks={"PostToolUse": [HookMatcher(hooks=[global_hook])]}
)
```

**优点**：简单
**缺点**：全局变量不优雅

---

### 方式3：通过工厂函数

```python
def create_hook_for_session(session: SessionInfo):
    """为特定 Session 创建 Hook 函数"""

    async def hook(hook_input, tool_use_id, context):
        # ✅ session 被闭包捕获
        session.update_progress(...)
        return {"hookEventName": "PostToolUse"}

    return hook

# 使用
session = SessionInfo(...)
hook_func = create_hook_for_session(session)

options = ClaudeAgentOptions(
    hooks={"PostToolUse": [HookMatcher(hooks=[hook_func])]}
)
```

---

## 五、完整可运行示例

```python
import asyncio
from dataclasses import dataclass, field
from typing import Optional, Dict
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher
from claude_agent_sdk.types import PostToolUseHookInput, HookContext, HookJSONOutput

@dataclass
class TaskProgress:
    stage: str
    progress: float
    message: str

@dataclass
class SessionInfo:
    session_key: str
    progress: Optional[TaskProgress] = None

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, SessionInfo] = {}

    async def start_session(self, session_key: str):
        """启动一个 Session（带 Hook）"""

        # 创建 Session
        session = SessionInfo(session_key=session_key)
        self.sessions[session_key] = session

        # 👉 关键：定义 Hook 函数（闭包）
        async def progress_tracking_hook(
            hook_input: PostToolUseHookInput,
            tool_use_id: str | None,
            context: HookContext
        ) -> HookJSONOutput:
            """这个函数会在工具执行后被调用"""

            print(f"[Hook] 工具 {hook_input['tool_name']} 执行完成")

            # ✅ 通过闭包访问 session
            tool_name = hook_input["tool_name"]

            # 简单的进度推断
            if tool_name == "Bash":
                stage = "执行命令"
                progress = 50.0
            elif tool_name == "Read":
                stage = "读取文件"
                progress = 70.0
            else:
                stage = f"执行{tool_name}"
                progress = 30.0

            # 更新 Session 的进度
            session.progress = TaskProgress(
                stage=stage,
                progress=progress,
                message=f"工具: {tool_name}"
            )

            print(f"[Hook] 进度已更新: {stage} {progress}%")

            return {"hookEventName": "PostToolUse"}

        # 创建 Options（包含 Hook）
        options = ClaudeAgentOptions(
            permission_mode='acceptEdits',
            hooks={
                "PostToolUse": [
                    HookMatcher(
                        matcher=None,  # 匹配所有工具
                        hooks=[progress_tracking_hook]  # 👈 传入 Hook
                    )
                ]
            }
        )

        # 启动 Client
        client = ClaudeSDKClient(options=options)
        await client.connect()

        session.client = client
        return session

    def get_progress(self, session_key: str) -> str:
        """获取进度（任何时候都可以调用）"""
        session = self.sessions.get(session_key)

        if not session or not session.progress:
            return "没有进度信息"

        p = session.progress
        return f"📊 {p.stage} - {p.progress}%\n💬 {p.message}"

# ===== 使用示例 =====
async def main():
    manager = SessionManager()

    # 启动 Session（Hook 已注册）
    session = await manager.start_session("user123")

    # 发送任务
    await session.client.query("帮我读取 /tmp/test.txt 文件")

    # 等待一会儿
    await asyncio.sleep(2)

    # 查询进度（任何时候都可以）
    progress = manager.get_progress("user123")
    print(f"\n用户查询进度:\n{progress}")

    # 输出示例:
    # [Hook] 工具 Read 执行完成
    # [Hook] 进度已更新: 读取文件 70%
    #
    # 用户查询进度:
    # 📊 读取文件 - 70%
    # 💬 工具: Read

asyncio.run(main())
```

---

## 六、面试问答 QA

### Q1: Hook 是怎么传递数据给 SessionManager 的？

**A**: Hook 就是普通的回调函数，通过闭包或全局变量访问 SessionManager。

```python
# 闭包方式（最常用）
def start_client(session):
    async def hook(hook_input, ...):
        session.update(...)  # 通过闭包访问

    options = ClaudeAgentOptions(hooks={"PostToolUse": [hook]})
```

---

### Q2: Hook 在哪个进程执行？

**A**: 在你的 Python 进程，不是在 CLI 子进程。

```
CLI 子进程: 执行工具 → 发送事件（stdout）
    ↓
你的进程: SDK 收到事件 → 调用你的 Hook 函数 ✅
```

---

### Q3: Hook 函数能做什么？

**A**: 任何事情！它就是普通的 Python 函数。

```python
async def hook(hook_input, ...):
    # 可以修改对象
    session.progress = ...

    # 可以写文件
    with open("/tmp/log.txt", "a") as f:
        f.write(...)

    # 可以发网络请求
    await http.post("https://api.example.com", ...)

    # 可以调用数据库
    await db.insert(...)
```

---

### Q4: 为什么不直接用 Claude 的返回值？

**A**: Claude 的返回值是给用户看的文本，不是结构化数据。

```
Claude 返回: "我已经查询了数据库，找到了trace_id..."
    ↓
需要 LLM 再解析？成本高、不准确

Hook 返回: {"tool_name": "Bash", "tool_response": "trace_id=abc123"}
    ↓
结构化数据，直接使用 ✅
```

---

### Q5: Hook 会阻塞 Claude 吗？

**A**: 会！但很短（毫秒级），所以不影响。

```python
CLI: 执行工具 → 等待 Hook 完成 → 继续
         ↓           (~5ms)
     触发 Hook
```

所以 Hook 要快：
- ✅ 更新内存对象
- ❌ 不要做耗时操作（网络请求、大文件读写）

---

## 七、核心要点总结（背下来）

### 1. Hook 本质
- 就是**回调函数**（Callback）
- 和 JavaScript 的 `addEventListener` 一样
- SDK 在合适的时机调用你的函数

### 2. 数据流
```
CLI 执行工具 → stdout 发事件 → SDK 收到 → 调用你的 Hook → 更新 SessionManager
```

### 3. 访问方式
- **闭包**（最推荐）
- 全局变量
- 工厂函数

### 4. 执行位置
- **你的 Python 进程**
- 不是 CLI 子进程
- 所以可以访问任何对象

### 5. 性能
- Hook 执行很快（毫秒级）
- 不影响 Claude 的正常工作
- 但不要在 Hook 里做耗时操作

---

## 八、面试最佳回答（30秒版）

**面试官**: "PostToolUse Hook 是怎么把工具信息传递给 SessionManager 的？"

**你**:
> "Hook 本质就是**回调函数**，和 JavaScript 的事件监听一样。
>
> 流程是：
> 1. 我在创建 `ClaudeAgentOptions` 时注册一个回调函数
> 2. Claude CLI 执行工具后，通过 stdout 发送事件给 SDK
> 3. SDK 收到事件，调用我注册的回调函数
> 4. 我的回调函数在**我的 Python 进程**中执行，可以访问任何对象
> 5. 我通过**闭包**访问 `session` 对象，调用 `session.update_progress()`
>
> 关键是 Hook 不在 CLI 子进程执行，而是在我的进程，所以能直接访问 SessionManager。"

---

**文档版本**: v1.0
**最后更新**: 2026-04-17
**面试准备**: ⭐⭐⭐⭐⭐
