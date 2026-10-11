---
title: "Hook 与 SessionInfo 的数据流关系"
description: "核心问题：Hook 更新的对象是否与 Claude SDK 绑定？"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-01-30-15_hook_session_relationship.md"
---
# Hook 与 SessionInfo 的数据流关系

> 核心问题：Hook 更新的对象是否与 Claude SDK 绑定？

---

## TL;DR

**SessionInfo 是你的 Python 进程中的普通对象，不属于 Claude SDK，可以随意访问！** ✅

---

## 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                  你的 Python 进程                             │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │        SessionManager（你的代码）                    │    │
│  │                                                      │    │
│  │  sessions = {                                        │    │
│  │    "user123_abc": SessionInfo(...)  ← 普通Python对象  │    │
│  │  }                                                   │    │
│  └───────────┬──────────────────────────────────────────┘    │
│              │                                              │
│              │ 可以随时读写                                  │
│              │                                              │
│  ┌───────────▼──────────────────────────────────────────┐    │
│  │     你的业务代码                                       │    │
│  │  - handle_user_message()                            │    │
│  │  - get_progress_summary()                           │    │
│  │  - 任何其他函数都可以直接访问 sessions               │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐    │
│  │    ClaudeSDKClient（SDK代码）                         │    │
│  │                                                        │    │
│  │  - 持有一个 transport（到CLI的连接）                   │    │
│  │  - 不持有、不管理 SessionInfo                         │    │
│  └───────────┬────────────────────────────────────────────┘    │
│              │                                              │
│              │ stdin/stdout                                │
│              ↓                                              │
└──────────────┼──────────────────────────────────────────────┘
               │
               ↓
┌──────────────────────────────────────────────────────────────┐
│          Claude CLI 子进程（独立进程）                         │
│                                                              │
│  - 读取 stdin                                                │
│  - 执行工具（Bash, Read, ...）                               │
│  - 触发 Hook（回调到你的 Python 进程）                        │
│  - 写入 stdout                                               │
└──────────────────────────────────────────────────────────────┘

Hook 执行流程：
┌─────────────────────────────────────────────────────────────┐
│ Claude CLI 调用工具（如 Bash）                                │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────────────────┐
│ CLI 通过 stdout 发送事件给 SDK:                               │
│ {"type": "tool_result", "tool": "Bash", ...}                │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────────────────┐
│ SDK 内部识别到 PostToolUse 事件                               │
│ 调用你注册的 Hook 回调函数                                     │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────────────────────────┐
│ 你的 Hook 函数（在你的 Python 进程中执行）:                    │
│                                                              │
│ async def progress_tracking_hook(hook_input, ...):          │
│     session.update_progress_from_tool(...)  ← 直接访问对象    │
│                                                              │
│ ✅ 这是普通的 Python 函数调用！                               │
│ ✅ session 是你的对象，不是 SDK 的！                          │
└──────────────────────────────────────────────────────────────┘
```

---

## 关键事实

### 1. SessionInfo 的归属

```python
# 你的代码
class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, SessionInfo] = {}  # ← 这是你的字典
        #                  ↑
        #                  完全归你所有，不属于 SDK

# SessionInfo 就是一个普通的 dataclass
@dataclass
class SessionInfo:
    session_key: str
    progress: Optional[TaskProgress] = None
    # ... 其他字段

# 这和下面的普通对象没有任何区别：
user_data = {"name": "Alice", "age": 30}
```

**结论**：SessionInfo 是你的普通 Python 对象，和 list、dict 没有本质区别 ✅

---

### 2. Hook 的执行位置

```python
# Hook 是在【你的 Python 进程】中执行的回调函数
async def progress_tracking_hook(
    hook_input: PostToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext
) -> HookJSONOutput:
    # ✅ 这段代码运行在你的 Python 进程中
    # ✅ 可以访问你进程中的任何对象

    # 访问全局变量
    global_session_manager.sessions[session_key].update_progress(...)

    # 访问通过闭包捕获的变量
    session.update_progress(...)  # session 是外部作用域的变量

    # 写文件
    with open("/tmp/progress.log", "a") as f:
        f.write(...)

    # 发送网络请求
    await http_client.post(...)

    # 任何你想做的事情！

    return {"hookEventName": "PostToolUse"}
```

**结论**：Hook 就是普通的 Python 异步函数，可以做任何事 ✅

---

### 3. 并发访问示例

```python
# 线程1: Hook 更新数据
async def progress_tracking_hook(hook_input, tool_use_id, context):
    session.progress = TaskProgress(
        stage="查询数据库",
        progress_percent=25.0
    )
    # ✅ 更新完成

# 线程2: 用户查询进度（同时进行）
async def handle_user_query():
    progress = session.progress  # ✅ 直接读取，不需要等 Hook
    return f"当前进度：{progress.progress_percent}%"

# ✅ 两者可以并发执行，因为都是在同一个 Python 进程中
```

**注意**：如果有并发写入的风险，加锁：

```python
@dataclass
class SessionInfo:
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def update_progress(self, ...):
        async with self._lock:
            self.progress = TaskProgress(...)
```

但通常不需要，因为：
- Hook 的触发是**顺序的**（CLI 是单线程的）
- 读操作不需要锁

---

## 代码验证

### 完整示例：多处访问同一个 SessionInfo

```python
import asyncio
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class SessionInfo:
    session_key: str
    progress_value: float = 0.0

# 全局 Session 存储
sessions = {}

# ===== 场景1: Hook 更新 =====
async def progress_tracking_hook(session: SessionInfo):
    """Hook 回调：更新进度"""
    print(f"[Hook] 更新进度: {session.session_key}")
    session.progress_value = 50.0
    print(f"[Hook] 更新后: {session.progress_value}%")

# ===== 场景2: 业务代码读取 =====
async def get_progress(session_key: str) -> float:
    """业务代码：读取进度"""
    session = sessions[session_key]
    print(f"[Business] 读取进度: {session.progress_value}%")
    return session.progress_value

# ===== 场景3: 其他代码修改 =====
def update_from_elsewhere(session_key: str, value: float):
    """任何代码都可以修改"""
    session = sessions[session_key]
    session.progress_value = value
    print(f"[Other] 修改进度为: {value}%")

# ===== 测试 =====
async def main():
    # 创建 Session
    session = SessionInfo(session_key="test-123")
    sessions["test-123"] = session

    print("初始值:", session.progress_value)  # 0.0

    # 模拟 Hook 更新
    await progress_tracking_hook(session)
    print("Hook 后:", session.progress_value)  # 50.0

    # 业务代码读取
    progress = await get_progress("test-123")
    print("读取到:", progress)  # 50.0

    # 其他代码修改
    update_from_elsewhere("test-123", 75.0)
    print("修改后:", session.progress_value)  # 75.0

    # ✅ 所有代码都在操作同一个对象！

asyncio.run(main())

# 输出：
# 初始值: 0.0
# [Hook] 更新进度: test-123
# [Hook] 更新后: 50.0%
# Hook 后: 50.0
# [Business] 读取进度: 50.0%
# 读取到: 50.0
# [Other] 修改进度为: 75.0%
# 修改后: 75.0
```

---

## Hook 函数的"魔法"在哪里？

**其实没有魔法！** Hook 只是：

```python
# SDK 内部（简化版）
class Query:
    def __init__(self, hooks: Dict[str, List[Callable]]):
        self.hooks = hooks  # 保存你传入的函数

    async def handle_tool_result(self, tool_name, tool_input, tool_response):
        # 工具执行完成后，触发 Hook

        if "PostToolUse" in self.hooks:
            for hook_func in self.hooks["PostToolUse"]:
                # ✅ 就是普通的函数调用！
                result = await hook_func(
                    hook_input={
                        "tool_name": tool_name,
                        "tool_input": tool_input,
                        "tool_response": tool_response
                    },
                    tool_use_id=None,
                    context={}
                )
```

**本质**：SDK 只是在合适的时机调用你传入的函数，仅此而已！

---

## 实际使用模式

### 模式1: 通过闭包捕获 Session

```python
def create_hook_for_session(session: SessionInfo):
    """为特定 Session 创建 Hook（通过闭包）"""

    async def hook(hook_input, tool_use_id, context):
        # ✅ session 被闭包捕获，可以直接访问
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

### 模式2: 通过全局管理器

```python
# 全局管理器
class GlobalSessionManager:
    sessions: Dict[str, SessionInfo] = {}

manager = GlobalSessionManager()

# Hook 访问全局管理器
async def hook(hook_input, tool_use_id, context):
    session_id = hook_input["session_id"]
    session = manager.sessions[session_id]  # ✅ 通过全局变量访问
    session.update_progress(...)
```

### 模式3: 通过自定义上下文（不推荐）

```python
# 虽然 Hook 的 context 参数理论上可以传递数据
# 但实际上 SDK 不支持自定义 context
# 所以还是用闭包或全局变量
```

---

## 常见误解

### ❌ 误解1: "SessionInfo 属于 Claude SDK"

```python
# 错误理解
# "SessionInfo 是 SDK 管理的，我不能直接访问"

# ✅ 正确理解
# SessionInfo 就是你的普通对象，和 SDK 无关
session = SessionInfo(...)
# 你想怎么用就怎么用
session.progress = ...
print(session.progress)
del session
```

### ❌ 误解2: "Hook 更新的数据存储在 CLI 进程中"

```python
# 错误理解
# "Hook 更新 session.progress，数据保存在 CLI 子进程"

# ✅ 正确理解
# Hook 在你的 Python 进程执行，更新的是你进程的内存
# CLI 子进程根本不知道 SessionInfo 的存在
```

### ❌ 误解3: "需要通过 SDK 读取 Hook 更新的数据"

```python
# 错误理解
# progress = await client.get_progress()  # 没有这个 API

# ✅ 正确理解
# 直接读取对象
progress = session.progress
```

---

## 进程间关系总结

```
┌────────────────────────────────────────────────────────────┐
│              你的 Python 进程（主进程）                       │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ SessionInfo (你的对象)                               │   │
│  │  - progress: TaskProgress                           │   │
│  │  - status: "running"                                │   │
│  │  - ...                                              │   │
│  └────────────┬─────────────────────────────────────────┘   │
│               │                                             │
│               │ 可以随时读写                                 │
│               │                                             │
│  ┌────────────▼─────────────────────────────────────────┐   │
│  │ 业务代码                                              │   │
│  │  - handle_user_message()                            │   │
│  │  - get_progress_summary()                           │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Hook 回调函数                                         │   │
│  │  - progress_tracking_hook()                         │   │
│  │  - 也是在这个进程中执行                              │   │
│  └────────────┬─────────────────────────────────────────┘   │
│               │                                             │
│  ┌────────────▼─────────────────────────────────────────┐   │
│  │ ClaudeSDKClient (SDK 代码)                           │   │
│  │  - 负责与 CLI 通信                                    │   │
│  │  - 触发 Hook 回调                                     │   │
│  └────────────┬─────────────────────────────────────────┘   │
│               │ stdin/stdout 通信                           │
└───────────────┼─────────────────────────────────────────────┘
                │
                ↓
┌───────────────────────────────────────────────────────────┐
│           Claude CLI 子进程（独立进程）                     │
│                                                            │
│  - 不知道 SessionInfo 的存在                               │
│  - 只负责执行工具和生成文本                                 │
│  - 通过 stdout 发送事件给 SDK                              │
└────────────────────────────────────────────────────────────┘
```

---

## 总结

### ✅ 你的理解完全正确！

1. **SessionInfo 是你的普通对象**
   - 存储在你的 Python 进程内存中
   - 和 Claude SDK 没有绑定关系
   - 可以随意访问、修改

2. **Hook 只是普通的回调函数**
   - 在你的 Python 进程中执行
   - SDK 在合适的时机调用它
   - 就像 addEventListener 的回调一样

3. **数据流向**
   ```
   CLI 执行工具
   → SDK 收到事件
   → SDK 调用你的 Hook 函数
   → Hook 更新 SessionInfo
   → 你的业务代码随时可以读取 SessionInfo
   ```

4. **没有魔法**
   - 一切都是普通的 Python 对象和函数调用
   - 没有跨进程共享内存
   - 没有特殊的绑定机制

---

**核心答案**: 是的，SessionInfo 完全归你所有，可以随意访问，不需要通过 SDK！✅

