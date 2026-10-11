---
title: "Claude Agent SDK Session 生命周期管理方案"
description: "文档生成时间：2026-04-17 00:35:12 主题：生产环境中的长任务 Session 管理与多用户隔离策略"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-00-35-12_session_lifecycle_management.md"
---
# Claude Agent SDK Session 生命周期管理方案

> 文档生成时间：2026-04-17 00:35:12
> 主题：生产环境中的长任务 Session 管理与多用户隔离策略

---

## 目录

1. [问题场景](#问题场景)
2. [Claude CLI 的并发模型](#claude-cli-的并发模型)
3. [核心挑战分析](#核心挑战分析)
4. [Session 生命周期管理方案](#session-生命周期管理方案)
5. [完整实现代码](#完整实现代码)
6. [面试回答模板](#面试回答模板)
7. [生产环境最佳实践](#生产环境最佳实践)

---

## 问题场景

### 典型场景 A：长任务追问

```
用户A: "帮我排查这个链接的问题 https://console.baidu.com/itp/xxx"
 ↓ Agent 开始排查（预计需要 5 分钟）
    - 查询数据库获取 trace_id
    - 下载日志文件分析
    - 查询相关代码库定位问题
 ↓ 3 分钟后，用户去忙别的事情了
 ↓ 又过了 10 分钟
用户A: "刚才那个问题查得怎么样了？"

【核心问题】：
1. 第二条消息如何知道是在问"刚才那个任务"？
2. 如果是同一个 session，会不会打断正在运行的排查？
3. 如果是新 session，怎么获取之前的排查进度？
```

### 典型场景 B：多用户并发

```
[群聊中]
用户A: "@Agent 帮我排查 https://link1"
用户B: "@Agent 帮我排查 https://link2"

【核心问题】：
1. 如何隔离两个用户的上下文？
2. 如何保证 A 的排查结果不会混到 B 的回复里？
3. 两个任务能否并行执行？
```

---

## Claude CLI 的并发模型

### 关键发现 🔍

通过源码分析 `ClaudeSDKClient` 和 `Query` 类，我们发现：

#### 1. 一个 Client = 一个 CLI 子进程

```python
# client.py:130-134
self._transport = SubprocessCLITransport(
    prompt=actual_prompt,
    options=options,
)
await self._transport.connect()  # 👈 spawn 一个新的 CLI 子进程
```

**结论**：
- ✅ 每次 `connect()` 都会启动一个独立的 CLI 子进程
- ✅ 一个 Client 对象对应一个子进程
- ❌ 不同 Client 之间无法共享内存状态

---

#### 2. 一个进程内支持多个 session_id

```python
# client.py:180-208
async def query(self, prompt: str, session_id: str = "default"):
    message = {
        "type": "user",
        "message": {"role": "user", "content": prompt},
        "session_id": session_id,  # 👈 在同一个 CLI 进程内区分多个对话分支
    }
    await self._transport.write(json.dumps(message) + "\n")
```

**结论**：
- ✅ 一个 CLI 进程内可以管理多个 `session_id`
- ✅ 不同 `session_id` 的消息会被路由到不同的对话上下文
- ⚠️ 但所有 session 共享一个 CLI 进程的 stdin/stdout 通道

---

#### 3. CLI 是**单线程顺序处理**的

```python
# query.py:564-567
async for message in stream:
    if self._closed:
        break
    await self.transport.write(json.dumps(message) + "\n")  # 👈 顺序写入 stdin
```

```python
# query.py:591-600
async def receive_messages(self) -> AsyncIterator[dict[str, Any]]:
    """从 stdout 顺序读取消息"""
    async for message in self._message_receive:  # 👈 顺序读取
        if message.get("type") == "end":
            break
        yield message
```

**结论**：
- ❌ CLI **不支持真正的并发处理**
- ✅ 所有消息都是**顺序处理**的（FIFO 队列）
- ⚠️ 新消息**不会打断**正在执行的任务，而是排队等待

---

#### 4. interrupt() 的作用

```python
# client.py:210-214
async def interrupt(self) -> None:
    """Send interrupt signal (only works with streaming mode)."""
    await self._query.interrupt()
```

**作用**：
- ✅ 发送中断信号，让 Claude **停止当前正在生成的响应**
- ✅ 类似于用户按 Ctrl+C
- ❌ **不会清空队列中的其他消息**

---

## 核心挑战分析

### 挑战 1：长任务期间用户追问会怎样？

**情况A：使用同一个 Client 实例**

```python
client = ClaudeSDKClient(ClaudeAgentOptions(resume="task-123"))
await client.connect()

# 第一条消息：开始排查
await client.query("帮我排查这个链接", session_id="default")

# 3分钟后，第二条消息：追问进度
await client.query("刚才那个问题怎么样了？", session_id="default")
```

**会发生什么？**
1. ✅ 第二条消息进入 stdin 队列
2. ⏳ Claude **先完成第一个任务**（或者处理到某个断点）
3. ⏳ 然后才开始处理第二条消息
4. ❌ 用户可能需要等待第一个任务完全结束

**问题**：
- 用户想问"进度"，但得等任务完成才能问
- 用户体验差

---

**情况B：使用不同的 Client 实例**

```python
# 任务1：长时间运行
client1 = ClaudeSDKClient(ClaudeAgentOptions(resume="task-123"))
await client1.connect()
await client1.query("帮我排查这个链接", session_id="default")
# ... client1 还在运行中

# 任务2：追问进度（新进程）
client2 = ClaudeSDKClient(ClaudeAgentOptions(resume="task-123"))  # 👈 恢复同一个 session
await client2.connect()
await client2.query("刚才那个问题怎么样了？", session_id="default")
```

**会发生什么？**
1. ❌ `client2.connect()` 会报错：**Session 正在被其他进程使用**
2. ❌ 或者，client2 拿到的是 task-123 的旧状态（磁盘上的），看不到 client1 正在做的事情

**问题**：
- `resume` 机制是为了**跨进程恢复**，不是为了**同时访问**
- 无法实现"查看正在运行的任务"

---

### 挑战 2：多用户并发隔离

**错误做法：共享一个 Client**

```python
# 全局共享
shared_client = ClaudeSDKClient()
await shared_client.connect()

# 用户A的请求
await shared_client.query("排查 link1", session_id="user-A")

# 用户B的请求（会被排队）
await shared_client.query("排查 link2", session_id="user-B")  # ⏳ 需要等A完成
```

**问题**：
- 所有用户共享一个 CLI 进程
- 无法并行处理
- 响应速度慢

---

**正确做法：每个用户独立 Client**

```python
# 用户A
client_a = ClaudeSDKClient(ClaudeAgentOptions(resume="session-A"))
await client_a.connect()
await client_a.query("排查 link1")

# 用户B（并行）
client_b = ClaudeSDKClient(ClaudeAgentOptions(resume="session-B"))
await client_b.connect()
await client_b.query("排查 link2")
```

**优势**：
- ✅ 两个独立的 CLI 进程
- ✅ 真正的并行执行
- ✅ 上下文完全隔离

---

## Session 生命周期管理方案

### 方案架构

```
┌─────────────────────────────────────────────────────────────┐
│                     SessionManager                          │
│  - 管理所有活跃的 Client 实例                                 │
│  - 负责 Session 的创建、复用、清理                            │
│  - 提供任务状态查询接口                                        │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
   ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
   │ Session │         │ Session │         │ Session │
   │  user-A │         │  user-B │         │  user-C │
   │  task-1 │         │  task-2 │         │  task-3 │
   └─────────┘         └─────────┘         └─────────┘
        │                   │                   │
   ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
   │ Client  │         │ Client  │         │ Client  │
   │ Instance│         │ Instance│         │ Instance│
   └─────────┘         └─────────┘         └─────────┘
        │                   │                   │
   ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
   │ CLI子进程│         │ CLI子进程│         │ CLI子进程│
   └─────────┘         └─────────┘         └─────────┘
```

---

### 核心设计决策

#### 1. Session Key 设计

```python
def generate_session_key(user_id: str, task_context: str) -> str:
    """
    生成唯一的 session 标识

    Args:
        user_id: 用户ID（如IM用户名、群ID+用户名）
        task_context: 任务上下文（如链接URL的hash、关键词）

    Returns:
        session_key: 如 "user123_trace456" 或 "groupA_user123_link789"
    """
    return f"{user_id}_{hash(task_context) % 10000}"
```

**策略**：
- ✅ 同一个用户 + 同一个任务上下文 → 复用 session
- ✅ 不同用户 → 不同 session（隔离）
- ✅ 同一用户但不同任务 → 不同 session（避免混淆）

---

#### 2. Session 生命周期状态机

```
   ┌──────────┐
   │  CREATED │  ← 新建，尚未启动 Client
   └────┬─────┘
        │ start_session()
        ▼
   ┌──────────┐
   │  RUNNING │  ← Client 正在处理任务
   └────┬─────┘
        │ (任务完成或超时)
        ▼
   ┌──────────┐
   │   IDLE   │  ← 任务完成，但 Client 仍然存活（可复用）
   └────┬─────┘
        │ (超时或主动清理)
        ▼
   ┌──────────┐
   │  CLOSED  │  ← Client 已关闭，Session 已清理
   └──────────┘
```

---

#### 3. 超时清理策略

```python
SESSION_IDLE_TIMEOUT = 600  # 10分钟无活动后清理
SESSION_MAX_LIFETIME = 3600  # 1小时后强制清理
```

**场景**：
- 用户发起任务后长时间无响应 → 10分钟后自动清理
- 避免内存泄漏 → 最长1小时强制回收

---

## 完整实现代码

### 1. SessionInfo 数据结构

```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any
import asyncio

class SessionStatus(Enum):
    CREATED = "created"
    RUNNING = "running"
    IDLE = "idle"
    CLOSED = "closed"

@dataclass
class SessionInfo:
    """Session 元信息"""
    session_key: str
    user_id: str
    task_context: str
    resume_id: str  # 对应 ClaudeAgentOptions 的 resume 参数

    client: Optional[Any] = None  # ClaudeSDKClient 实例
    status: SessionStatus = SessionStatus.CREATED

    created_at: datetime = field(default_factory=datetime.now)
    last_activity: datetime = field(default_factory=datetime.now)

    # 任务状态
    task_status: str = "pending"  # pending | running | completed | failed
    task_result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None

    # 消息缓冲区（用于异步收集响应）
    message_buffer: list = field(default_factory=list)
    response_complete: asyncio.Event = field(default_factory=asyncio.Event)

    def update_activity(self):
        """更新最后活动时间"""
        self.last_activity = datetime.now()

    def is_expired(self, idle_timeout: int = 600, max_lifetime: int = 3600) -> bool:
        """检查 Session 是否过期"""
        now = datetime.now()
        idle_seconds = (now - self.last_activity).total_seconds()
        lifetime_seconds = (now - self.created_at).total_seconds()

        return idle_seconds > idle_timeout or lifetime_seconds > max_lifetime
```

---

### 2. SessionManager 核心类

```python
import asyncio
from typing import Dict, Optional, Callable
from contextlib import asynccontextmanager
import hashlib
import logging

logger = logging.getLogger(__name__)

class SessionManager:
    """Session 生命周期管理器"""

    def __init__(
        self,
        idle_timeout: int = 600,  # 10分钟
        max_lifetime: int = 3600,  # 1小时
        cleanup_interval: int = 60  # 1分钟检查一次
    ):
        self.sessions: Dict[str, SessionInfo] = {}
        self.idle_timeout = idle_timeout
        self.max_lifetime = max_lifetime
        self.cleanup_interval = cleanup_interval

        self._lock = asyncio.Lock()
        self._cleanup_task: Optional[asyncio.Task] = None
        self._running = False

    async def start(self):
        """启动管理器（包括后台清理任务）"""
        self._running = True
        self._cleanup_task = asyncio.create_task(self._cleanup_loop())
        logger.info("SessionManager started")

    async def stop(self):
        """停止管理器并清理所有 Session"""
        self._running = False
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass

        # 关闭所有活跃的 Session
        async with self._lock:
            for session_key in list(self.sessions.keys()):
                await self._close_session(session_key)

        logger.info("SessionManager stopped")

    def generate_session_key(self, user_id: str, task_context: str) -> str:
        """生成 Session Key"""
        # 对 task_context 取 hash 避免 key 过长
        context_hash = hashlib.md5(task_context.encode()).hexdigest()[:8]
        return f"{user_id}_{context_hash}"

    async def get_or_create_session(
        self,
        user_id: str,
        task_context: str,
        force_new: bool = False
    ) -> SessionInfo:
        """获取或创建 Session

        Args:
            user_id: 用户ID
            task_context: 任务上下文（如链接、关键词）
            force_new: 是否强制创建新 Session（不复用）

        Returns:
            SessionInfo
        """
        session_key = self.generate_session_key(user_id, task_context)

        async with self._lock:
            # 检查是否已存在
            if not force_new and session_key in self.sessions:
                session = self.sessions[session_key]

                # 如果 Session 还活着，复用
                if session.status != SessionStatus.CLOSED:
                    session.update_activity()
                    logger.info(f"Reusing existing session: {session_key}")
                    return session
                else:
                    # 已关闭的 Session，删除并重建
                    del self.sessions[session_key]

            # 创建新 Session
            resume_id = f"session_{session_key}_{int(datetime.now().timestamp())}"

            session = SessionInfo(
                session_key=session_key,
                user_id=user_id,
                task_context=task_context,
                resume_id=resume_id
            )

            self.sessions[session_key] = session
            logger.info(f"Created new session: {session_key} (resume_id={resume_id})")
            return session

    async def start_client_for_session(
        self,
        session: SessionInfo,
        options_factory: Callable[[str], Any]  # 接收 resume_id，返回 ClaudeAgentOptions
    ) -> Any:
        """为 Session 启动 Claude Client

        Args:
            session: SessionInfo 对象
            options_factory: 用于创建 ClaudeAgentOptions 的工厂函数

        Returns:
            ClaudeSDKClient 实例
        """
        from claude_agent_sdk import ClaudeSDKClient

        async with self._lock:
            if session.client is not None:
                # 已有 Client，直接返回
                return session.client

            # 创建新 Client
            options = options_factory(session.resume_id)
            client = ClaudeSDKClient(options=options)
            await client.connect()

            session.client = client
            session.status = SessionStatus.RUNNING
            session.update_activity()

            logger.info(f"Started client for session: {session.session_key}")
            return client

    async def execute_task(
        self,
        session: SessionInfo,
        prompt: str,
        timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        """在指定 Session 中执行任务

        Args:
            session: SessionInfo 对象
            prompt: 用户问题
            timeout: 超时时间（秒）

        Returns:
            任务结果字典
        """
        if session.client is None:
            raise ValueError("Client not started. Call start_client_for_session first.")

        session.status = SessionStatus.RUNNING
        session.task_status = "running"
        session.message_buffer.clear()
        session.response_complete.clear()
        session.update_activity()

        try:
            # 发送消息
            await session.client.query(prompt, session_id="default")

            # 收集响应
            async def collect_messages():
                async for msg in session.client.receive_messages():
                    session.message_buffer.append(msg)
                    session.update_activity()

                    # 检查是否完成
                    if msg.get("type") == "result":
                        session.response_complete.set()
                        break

            # 启动收集任务
            collect_task = asyncio.create_task(collect_messages())

            # 等待完成或超时
            if timeout:
                await asyncio.wait_for(
                    session.response_complete.wait(),
                    timeout=timeout
                )
            else:
                await session.response_complete.wait()

            # 提取结果
            result = {
                "status": "success",
                "messages": session.message_buffer,
                "session_key": session.session_key
            }

            session.task_status = "completed"
            session.task_result = result
            session.status = SessionStatus.IDLE

            logger.info(f"Task completed for session: {session.session_key}")
            return result

        except asyncio.TimeoutError:
            session.task_status = "timeout"
            session.error_message = f"Task timeout after {timeout}s"
            session.status = SessionStatus.IDLE

            logger.warning(f"Task timeout for session: {session.session_key}")
            return {
                "status": "timeout",
                "error": session.error_message,
                "partial_messages": session.message_buffer
            }

        except Exception as e:
            session.task_status = "failed"
            session.error_message = str(e)
            session.status = SessionStatus.IDLE

            logger.error(f"Task failed for session {session.session_key}: {e}")
            return {
                "status": "error",
                "error": str(e)
            }

    async def get_task_status(self, session_key: str) -> Optional[Dict[str, Any]]:
        """查询任务状态

        用于用户追问"刚才那个任务怎么样了"
        """
        async with self._lock:
            session = self.sessions.get(session_key)
            if not session:
                return None

            return {
                "session_key": session_key,
                "status": session.task_status,
                "result": session.task_result,
                "error": session.error_message,
                "last_activity": session.last_activity.isoformat()
            }

    async def interrupt_session(self, session_key: str) -> bool:
        """中断正在运行的 Session"""
        async with self._lock:
            session = self.sessions.get(session_key)
            if not session or not session.client:
                return False

            try:
                await session.client.interrupt()
                session.task_status = "interrupted"
                session.status = SessionStatus.IDLE
                logger.info(f"Interrupted session: {session_key}")
                return True
            except Exception as e:
                logger.error(f"Failed to interrupt session {session_key}: {e}")
                return False

    async def _close_session(self, session_key: str):
        """关闭并清理 Session"""
        session = self.sessions.get(session_key)
        if not session:
            return

        try:
            if session.client:
                await session.client.disconnect()
            session.status = SessionStatus.CLOSED
            del self.sessions[session_key]
            logger.info(f"Closed session: {session_key}")
        except Exception as e:
            logger.error(f"Error closing session {session_key}: {e}")

    async def _cleanup_loop(self):
        """后台清理过期 Session"""
        while self._running:
            try:
                await asyncio.sleep(self.cleanup_interval)

                async with self._lock:
                    expired_keys = [
                        key for key, session in self.sessions.items()
                        if session.is_expired(self.idle_timeout, self.max_lifetime)
                    ]

                    for key in expired_keys:
                        logger.info(f"Cleaning up expired session: {key}")
                        await self._close_session(key)

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in cleanup loop: {e}")
```

---

### 3. 使用示例：处理用户请求

```python
from claude_agent_sdk import ClaudeAgentOptions

# 全局 SessionManager 实例
session_manager = SessionManager(idle_timeout=600, max_lifetime=3600)

async def handle_user_query(user_id: str, message: str, task_context: str):
    """
    处理用户请求的核心逻辑

    Args:
        user_id: 用户ID（如IM用户名）
        message: 用户消息
        task_context: 任务上下文（如链接URL）
    """
    # 1. 检查是否是追问
    is_followup = any(keyword in message for keyword in ["怎么样了", "进度", "查得如何"])

    if is_followup:
        # 追问场景：查询已有 Session 的状态
        session_key = session_manager.generate_session_key(user_id, task_context)
        status = await session_manager.get_task_status(session_key)

        if status:
            if status["status"] == "running":
                return f"任务还在进行中，已经运行了 {calculate_duration(status['last_activity'])} 分钟"
            elif status["status"] == "completed":
                return format_result(status["result"])
            elif status["status"] == "failed":
                return f"任务执行失败: {status['error']}"
        else:
            return "没有找到相关的任务记录"

    else:
        # 新任务：创建或复用 Session
        session = await session_manager.get_or_create_session(
            user_id=user_id,
            task_context=task_context,
            force_new=False  # 允许复用
        )

        # 启动 Client（如果尚未启动）
        if session.client is None:
            def create_options(resume_id: str):
                return ClaudeAgentOptions(
                    permission_mode='acceptEdits',
                    resume=resume_id,
                    setting_sources=["user", "project"],
                    allowed_tools=["Read", "Write", "Edit", "Grep", "Glob", "Bash", "Skill"],
                    cwd="/workspace",
                    cli_path="/path/to/ducc"
                )

            await session_manager.start_client_for_session(session, create_options)

        # 执行任务（异步）
        # 注意：这里不要 await，让任务在后台运行
        asyncio.create_task(
            session_manager.execute_task(session, message, timeout=600)
        )

        return f"收到！正在为你排查，任务ID: {session.session_key}"

# 启动管理器
async def main():
    await session_manager.start()

    try:
        # 模拟用户请求
        user_id = "user123"
        link = "https://console.baidu.com/itp/xxx"

        # 第一次请求
        response1 = await handle_user_query(
            user_id=user_id,
            message=f"帮我排查这个链接 {link}",
            task_context=link
        )
        print(response1)  # "收到！正在为你排查..."

        # 等待一会儿
        await asyncio.sleep(180)  # 3分钟后

        # 追问进度
        response2 = await handle_user_query(
            user_id=user_id,
            message="刚才那个问题查得怎么样了？",
            task_context=link  # 👈 必须传相同的 task_context 才能找到对应 session
        )
        print(response2)  # "任务还在进行中..." 或 "已完成：..."

    finally:
        await session_manager.stop()

# 运行
asyncio.run(main())
```

---

### 4. 多用户并发示例

```python
async def handle_multi_user_scenario():
    """模拟群聊中多用户并发请求"""
    await session_manager.start()

    try:
        # 用户A和用户B同时发起请求
        tasks = [
            handle_user_query(
                user_id="userA",
                message="帮我排查 https://link1",
                task_context="https://link1"
            ),
            handle_user_query(
                user_id="userB",
                message="帮我排查 https://link2",
                task_context="https://link2"
            )
        ]

        # 并发执行
        responses = await asyncio.gather(*tasks)

        print(f"用户A: {responses[0]}")  # 任务ID: userA_abc123
        print(f"用户B: {responses[1]}")  # 任务ID: userB_def456

        # ✅ 两个任务在独立的 CLI 进程中并行执行
        # ✅ 上下文完全隔离

    finally:
        await session_manager.stop()
```

---

## 面试回答模板

### 问题："Task 级记忆不就是 Claude Code 内部的对话上下文吗？你做了什么？"

### 参考回答

**第一步：承认事实**
> "对，Task 级的对话上下文底层确实是 Claude Code 的 `session_id` 和 `resume` 机制在管理。Claude CLI 内部维护了完整的 conversation history。"

**第二步：强调上层封装**
> "但我们在上层做了 **Session 生命周期的封装和管理策略**——具体来说就是：
> 1. **什么时候创建新 session**：根据用户ID和任务上下文生成唯一的 session_key
> 2. **什么时候复用已有 session**：同一个用户追问同一个任务时，复用之前的 session
> 3. **什么时候判定任务结束并清理**：设置 idle timeout（10分钟）和 max lifetime（1小时）
> 4. **如何隔离多用户**：每个用户分配独立的 ClaudeSDKClient 实例和 CLI 子进程"

**第三步：举具体例子（场景A）**
> "举个例子，用户在 IM 群里发了一个链接让我排查，Agent 开始查日志、查数据库，这可能需要 5 分钟。用户去忙别的了，过了半小时回来追问'刚才那个问题查得怎么样了'——**这时候我需要判断这条消息属于哪个 session**。
>
> 我的设计是：
> - 根据 `user_id` + `task_context`（链接的 hash）生成唯一的 `session_key`
> - 第二次追问时，通过相同的 `session_key` 找到之前的 `SessionInfo` 对象
> - 如果任务还在运行中（status = RUNNING），返回进度信息
> - 如果任务已完成（status = IDLE），返回缓存的结果"

**第四步：举具体例子（场景B）**
> "再比如，同一个群里 A 和 B 同时在问不同的问题，我需要做**上下文隔离**，不能把 A 的排查结果混到 B 的回答里。
>
> 我的设计是：
> - 为每个用户创建独立的 `ClaudeSDKClient` 实例
> - 每个 Client 对应一个独立的 CLI 子进程
> - 两个进程之间完全隔离，可以并行执行
> - 通过 `SessionManager` 统一管理这些 Client 实例的生命周期"

**第五步：总结技术价值**
> "所以总结来说，Claude Code SDK 提供了底层的对话上下文管理能力，但**Session 的创建策略、复用逻辑、超时清理、多用户隔离、任务状态查询**这些**生产环境的实际需求**是需要我们在上层自己设计和实现的。这就是我在这个模块做的核心工作。"

---

## 生产环境最佳实践

### 1. Session Key 设计原则

```python
# ❌ 错误：只用 user_id
session_key = user_id  # 同一个用户的所有任务都在同一个 session，会混淆

# ✅ 正确：user_id + task_context
session_key = f"{user_id}_{hash(task_context)}"  # 不同任务隔离

# ✅ 更好：加上时间戳（避免旧任务影响新任务）
session_key = f"{user_id}_{hash(task_context)}_{timestamp_bucket}"
```

---

### 2. 超时策略

| 场景 | Idle Timeout | Max Lifetime | 原因 |
|------|-------------|-------------|------|
| 快速问答 | 5分钟 | 30分钟 | 用户期望快速响应 |
| 深度排查 | 10分钟 | 1小时 | 任务可能较长 |
| 后台任务 | 30分钟 | 4小时 | 允许长时间运行 |

---

### 3. 并发限制

```python
class SessionManager:
    def __init__(self, max_concurrent_sessions: int = 10):
        self.max_concurrent_sessions = max_concurrent_sessions
        self.semaphore = asyncio.Semaphore(max_concurrent_sessions)

    async def start_client_for_session(self, session, options_factory):
        # 限制并发数
        async with self.semaphore:
            # ... 启动 Client
            pass
```

**原因**：
- 每个 Client = 一个 CLI 子进程
- 过多子进程会导致系统资源耗尽
- 建议限制在 10-50 个并发

---

### 4. 错误重试策略

```python
async def execute_task_with_retry(
    self,
    session: SessionInfo,
    prompt: str,
    max_retries: int = 3
):
    """带重试的任务执行"""
    for attempt in range(max_retries):
        try:
            return await self.execute_task(session, prompt)
        except Exception as e:
            if attempt < max_retries - 1:
                logger.warning(f"Task failed (attempt {attempt+1}/{max_retries}): {e}")
                await asyncio.sleep(2 ** attempt)  # 指数退避
            else:
                raise
```

---

### 5. 监控指标

```python
class SessionManager:
    def get_metrics(self) -> Dict[str, Any]:
        """获取监控指标"""
        return {
            "total_sessions": len(self.sessions),
            "running_sessions": sum(
                1 for s in self.sessions.values()
                if s.status == SessionStatus.RUNNING
            ),
            "idle_sessions": sum(
                1 for s in self.sessions.values()
                if s.status == SessionStatus.IDLE
            ),
            "average_task_duration": self._calculate_avg_duration(),
            "success_rate": self._calculate_success_rate()
        }
```

---

## 总结

### 核心要点

1. **Claude CLI 的并发模型**：
   - 一个 Client = 一个 CLI 子进程
   - 一个进程内支持多个 session_id
   - 消息是顺序处理的，不支持真并发

2. **Session 生命周期管理**：
   - 通过 `SessionManager` 统一管理所有 Client 实例
   - 根据 user_id + task_context 生成唯一的 session_key
   - 支持 Session 复用、超时清理、状态查询

3. **多用户隔离**：
   - 每个用户独立的 Client 实例和 CLI 子进程
   - 真正的并行执行
   - 完全的上下文隔离

4. **长任务追问**：
   - 任务在后台运行（asyncio.create_task）
   - 通过 session_key 查询任务状态
   - 返回进度信息或缓存结果

---

**文档版本**：v1.0
**适用SDK版本**：claude-agent-sdk >= 0.0.20
**维护者**：Ducc AI Team
**最后更新**：2026-04-17
