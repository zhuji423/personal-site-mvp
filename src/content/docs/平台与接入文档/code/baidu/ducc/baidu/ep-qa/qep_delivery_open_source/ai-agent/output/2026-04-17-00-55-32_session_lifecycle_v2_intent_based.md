---
title: "Claude Agent SDK Session 生命周期管理方案 v2.0"
description: "文档生成时间：2026-04-17 00:55:32 主题：基于意图识别的消息路由策略"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-00-55-32_session_lifecycle_v2_intent_based.md"
---
# Claude Agent SDK Session 生命周期管理方案 v2.0

> 文档生成时间：2026-04-17 00:55:32
> 主题：基于意图识别的消息路由策略

---

## 目录

1. [核心问题重述](#核心问题重述)
2. [意图识别机制](#意图识别机制)
3. [完整实现代码](#完整实现代码)
4. [实际运行示例](#实际运行示例)
5. [面试回答模板](#面试回答模板)

---

## 核心问题重述

### 场景1：用户追问进度（应该立即返回）

```
T0:  用户: "帮我排查这个链接 https://xxx"
     → Agent 调用 Claude，任务开始（预计10分钟）
     → Claude 开始查日志、查数据库...

T7:  用户: "刚才那个问题查得怎么样了？"
     → 期望行为：✅ 立即返回 "正在运行中，已执行7分钟，Claude正在分析日志..."
     → 错误行为：❌ 消息进入 Claude 的 stdin 队列，等任务1完成才能回复（用户再等3分钟）
```

**问题根源**：
- 追问进度是**查询操作**，不应该发给 Claude
- 应该直接从 `SessionManager` 获取当前状态

---

### 场景2：用户提交新任务（应该排队）

```
T0:  用户: "帮我排查链接1"
     → Agent 调用 Claude，任务1开始

T3:  用户: "帮我排查链接2"
     → 期望行为：✅ 任务2排队，等任务1完成后再执行
     → 错误行为：❌ 任务2立即开始（可能打断任务1，或者上下文混乱）
```

**问题根源**：
- 新任务是**执行操作**，应该发给 Claude
- 需要排队等待前一个任务完成

---

## 意图识别机制

### 消息分类

| 消息类型 | 示例 | 处理方式 | 是否发给Claude |
|---------|-----|---------|---------------|
| **查询进度** | "刚才那个问题怎么样了？"<br>"任务跑完了吗？"<br>"进度如何？" | 从SessionManager直接返回状态 | ❌ 否 |
| **新任务** | "帮我排查链接2"<br>"再帮我看看另一个问题" | 发给Claude，进入消息队列 | ✅ 是 |
| **上下文追问** | "刚才那个日志有什么问题？"<br>"为什么会报这个错？" | 发给Claude，基于之前的上下文回答 | ✅ 是 |
| **中断/取消** | "别查了"<br>"停止" | 调用 client.interrupt() | ⚠️ 发中断信号 |

---

### 意图识别实现

#### 方法1：关键词匹配（简单快速）

```python
class MessageIntent(Enum):
    """消息意图枚举"""
    QUERY_STATUS = "query_status"      # 查询进度
    NEW_TASK = "new_task"              # 新任务
    CONTEXT_FOLLOWUP = "context_followup"  # 上下文追问
    INTERRUPT = "interrupt"            # 中断

def classify_intent(message: str, has_running_task: bool) -> MessageIntent:
    """
    基于关键词的简单意图识别

    Args:
        message: 用户消息
        has_running_task: 当前是否有正在运行的任务

    Returns:
        MessageIntent
    """
    message_lower = message.lower()

    # 1. 中断意图（优先级最高）
    interrupt_keywords = ["停止", "取消", "别查了", "不用了", "算了"]
    if any(kw in message_lower for kw in interrupt_keywords):
        return MessageIntent.INTERRUPT

    # 2. 查询进度意图
    status_keywords = [
        "怎么样了", "查得如何", "进度", "跑完了吗",
        "好了吗", "完成了吗", "还在跑吗",
        "查到了吗", "有结果了吗"
    ]
    if any(kw in message_lower for kw in status_keywords):
        return MessageIntent.QUERY_STATUS

    # 3. 如果有正在运行的任务
    if has_running_task:
        # 检查是否是新任务（包含链接、明确的任务关键词）
        new_task_indicators = [
            "http://", "https://",  # 包含链接
            "帮我", "帮忙", "再",     # 明确的请求词
            "另一个", "这个", "那个"  # 指代新对象
        ]
        if any(ind in message for ind in new_task_indicators):
            # 进一步判断：是否在问"刚才那个"
            reference_to_current = ["刚才", "之前", "刚刚", "上面", "那个"]
            if any(ref in message for ref in reference_to_current):
                # "刚才那个链接为什么报错？" → 上下文追问
                return MessageIntent.CONTEXT_FOLLOWUP
            else:
                # "帮我再看看这个链接" → 新任务
                return MessageIntent.NEW_TASK
        else:
            # 没有明确的新任务指示，默认为上下文追问
            return MessageIntent.CONTEXT_FOLLOWUP
    else:
        # 没有正在运行的任务，默认为新任务
        return MessageIntent.NEW_TASK
```

---

#### 方法2：基于 LLM 的意图识别（更准确）

```python
async def classify_intent_with_llm(
    message: str,
    context: Dict[str, Any]
) -> MessageIntent:
    """
    使用 LLM 进行意图识别

    Args:
        message: 用户消息
        context: 上下文信息（当前任务状态、历史消息等）

    Returns:
        MessageIntent
    """
    prompt = f"""
你是一个意图识别专家。请判断以下用户消息的意图类型。

当前上下文：
- 是否有正在运行的任务：{context.get('has_running_task', False)}
- 当前任务描述：{context.get('current_task', 'N/A')}
- 历史消息数：{context.get('message_count', 0)}

用户消息：
"{message}"

请返回以下意图之一：
1. query_status - 查询任务进度（如"怎么样了"、"跑完了吗"）
2. new_task - 提交新任务（如"帮我排查另一个链接"）
3. context_followup - 基于当前任务的追问（如"为什么会报这个错"）
4. interrupt - 中断/取消（如"停止"、"别查了"）

只返回意图类型，不要有其他内容。
"""

    # 使用一个快速的小模型来做意图识别（不需要 Claude Opus）
    response = await call_small_llm(prompt)  # 比如用 haiku 或本地模型

    intent_str = response.strip().lower()
    return MessageIntent(intent_str)
```

---

## 完整实现代码

### 1. 增强的 SessionInfo

```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any, List
import asyncio

class SessionStatus(Enum):
    CREATED = "created"
    RUNNING = "running"
    IDLE = "idle"
    CLOSED = "closed"

@dataclass
class TaskProgress:
    """任务进度信息"""
    stage: str  # 当前阶段（如 "查询数据库"、"分析日志"）
    progress_percent: float  # 进度百分比（0-100）
    elapsed_seconds: float  # 已执行时间
    estimated_remaining: Optional[float] = None  # 预计剩余时间
    latest_message: Optional[str] = None  # 最新的进展消息

@dataclass
class SessionInfo:
    """Session 元信息"""
    session_key: str
    user_id: str
    task_context: str
    resume_id: str

    client: Optional[Any] = None
    status: SessionStatus = SessionStatus.CREATED

    created_at: datetime = field(default_factory=datetime.now)
    last_activity: datetime = field(default_factory=datetime.now)

    # 任务状态
    task_status: str = "pending"
    task_result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None

    # 任务进度（新增）
    progress: Optional[TaskProgress] = None

    # 消息缓冲区
    message_buffer: List[Any] = field(default_factory=list)
    response_complete: asyncio.Event = field(default_factory=asyncio.Event)

    # 消息队列（用于排队新任务）
    pending_messages: asyncio.Queue = field(default_factory=asyncio.Queue)

    def update_activity(self):
        """更新最后活动时间"""
        self.last_activity = datetime.now()

    def update_progress(
        self,
        stage: str,
        progress_percent: float,
        latest_message: Optional[str] = None
    ):
        """更新任务进度"""
        elapsed = (datetime.now() - self.created_at).total_seconds()

        self.progress = TaskProgress(
            stage=stage,
            progress_percent=progress_percent,
            elapsed_seconds=elapsed,
            latest_message=latest_message
        )
        self.update_activity()

    def get_progress_summary(self) -> str:
        """获取进度摘要（用于返回给用户）"""
        if not self.progress:
            return f"任务已运行 {self._format_duration()} 分钟"

        elapsed_str = self._format_duration()

        summary = f"🔄 任务进行中（已运行 {elapsed_str}）\n"
        summary += f"📊 当前阶段：{self.progress.stage}\n"
        summary += f"⏱️ 进度：{self.progress.progress_percent:.1f}%"

        if self.progress.latest_message:
            summary += f"\n💬 最新进展：{self.progress.latest_message}"

        return summary

    def _format_duration(self) -> str:
        """格式化执行时长"""
        elapsed = (datetime.now() - self.created_at).total_seconds()
        if elapsed < 60:
            return f"{int(elapsed)} 秒"
        else:
            return f"{elapsed / 60:.1f} 分钟"

    def is_expired(self, idle_timeout: int = 600, max_lifetime: int = 3600) -> bool:
        now = datetime.now()
        idle_seconds = (now - self.last_activity).total_seconds()
        lifetime_seconds = (now - self.created_at).total_seconds()
        return idle_seconds > idle_timeout or lifetime_seconds > max_lifetime
```

---

### 2. 增强的 SessionManager（支持意图路由）

```python
import asyncio
from typing import Dict, Optional, Callable
import hashlib
import logging

logger = logging.getLogger(__name__)

class SessionManager:
    """Session 生命周期管理器（增强版）"""

    def __init__(
        self,
        idle_timeout: int = 600,
        max_lifetime: int = 3600,
        cleanup_interval: int = 60
    ):
        self.sessions: Dict[str, SessionInfo] = {}
        self.idle_timeout = idle_timeout
        self.max_lifetime = max_lifetime
        self.cleanup_interval = cleanup_interval

        self._lock = asyncio.Lock()
        self._cleanup_task: Optional[asyncio.Task] = None
        self._running = False

    async def start(self):
        """启动管理器"""
        self._running = True
        self._cleanup_task = asyncio.create_task(self._cleanup_loop())
        logger.info("SessionManager started")

    async def stop(self):
        """停止管理器"""
        self._running = False
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass

        async with self._lock:
            for session_key in list(self.sessions.keys()):
                await self._close_session(session_key)

        logger.info("SessionManager stopped")

    def generate_session_key(self, user_id: str, task_context: str) -> str:
        """生成 Session Key"""
        context_hash = hashlib.md5(task_context.encode()).hexdigest()[:8]
        return f"{user_id}_{context_hash}"

    async def get_or_create_session(
        self,
        user_id: str,
        task_context: str,
        force_new: bool = False
    ) -> SessionInfo:
        """获取或创建 Session"""
        session_key = self.generate_session_key(user_id, task_context)

        async with self._lock:
            if not force_new and session_key in self.sessions:
                session = self.sessions[session_key]
                if session.status != SessionStatus.CLOSED:
                    session.update_activity()
                    logger.info(f"Reusing existing session: {session_key}")
                    return session
                else:
                    del self.sessions[session_key]

            resume_id = f"session_{session_key}_{int(datetime.now().timestamp())}"
            session = SessionInfo(
                session_key=session_key,
                user_id=user_id,
                task_context=task_context,
                resume_id=resume_id
            )

            self.sessions[session_key] = session
            logger.info(f"Created new session: {session_key}")
            return session

    async def start_client_for_session(
        self,
        session: SessionInfo,
        options_factory: Callable[[str], Any]
    ) -> Any:
        """为 Session 启动 Claude Client"""
        from claude_agent_sdk import ClaudeSDKClient

        async with self._lock:
            if session.client is not None:
                return session.client

            options = options_factory(session.resume_id)
            client = ClaudeSDKClient(options=options)
            await client.connect()

            session.client = client
            session.status = SessionStatus.RUNNING
            session.update_activity()

            # 启动后台任务：处理消息队列
            asyncio.create_task(self._process_message_queue(session))

            logger.info(f"Started client for session: {session.session_key}")
            return client

    async def _process_message_queue(self, session: SessionInfo):
        """后台任务：处理 Session 的消息队列"""
        while session.status != SessionStatus.CLOSED:
            try:
                # 从队列中取出消息
                message = await asyncio.wait_for(
                    session.pending_messages.get(),
                    timeout=1.0
                )

                # 执行任务
                logger.info(f"Processing queued message for {session.session_key}")
                await self._execute_task_internal(session, message)

            except asyncio.TimeoutError:
                # 队列为空，继续等待
                continue
            except Exception as e:
                logger.error(f"Error processing message queue: {e}")

    async def _execute_task_internal(
        self,
        session: SessionInfo,
        prompt: str
    ):
        """内部方法：实际执行任务"""
        if session.client is None:
            raise ValueError("Client not started")

        session.status = SessionStatus.RUNNING
        session.task_status = "running"
        session.message_buffer.clear()
        session.response_complete.clear()
        session.update_activity()

        try:
            # 发送消息
            await session.client.query(prompt, session_id="default")

            # 收集响应（带进度更新）
            async for msg in session.client.receive_messages():
                session.message_buffer.append(msg)
                session.update_activity()

                # 从消息中提取进度信息（如果有）
                await self._update_progress_from_message(session, msg)

                # 检查是否完成
                if msg.get("type") == "result":
                    session.response_complete.set()
                    break

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

        except Exception as e:
            session.task_status = "failed"
            session.error_message = str(e)
            session.status = SessionStatus.IDLE
            logger.error(f"Task failed for session {session.session_key}: {e}")

    async def _update_progress_from_message(self, session: SessionInfo, msg: Any):
        """从 Claude 的消息中提取进度信息"""
        # 这里需要根据实际的消息格式来解析
        # 示例：假设 Claude 返回的 text 中包含进度信息

        if msg.get("type") == "message":
            content = msg.get("content", "")
            if isinstance(content, str):
                # 简单的启发式规则（实际可以更复杂）
                if "查询数据库" in content:
                    session.update_progress("查询数据库", 20.0, content[:100])
                elif "分析日志" in content:
                    session.update_progress("分析日志", 50.0, content[:100])
                elif "定位问题" in content:
                    session.update_progress("定位问题", 80.0, content[:100])

    async def handle_message(
        self,
        user_id: str,
        message: str,
        task_context: str,
        intent_classifier: Optional[Callable] = None
    ) -> str:
        """
        处理用户消息的核心入口（支持意图识别）

        Args:
            user_id: 用户ID
            message: 用户消息
            task_context: 任务上下文
            intent_classifier: 可选的意图识别函数

        Returns:
            响应文本
        """
        # 1. 获取或创建 Session
        session = await self.get_or_create_session(user_id, task_context)

        # 2. 意图识别
        has_running_task = (session.status == SessionStatus.RUNNING)

        if intent_classifier:
            intent = await intent_classifier(message, {"has_running_task": has_running_task})
        else:
            intent = classify_intent(message, has_running_task)

        logger.info(f"Message intent: {intent} (session={session.session_key})")

        # 3. 根据意图路由
        if intent == MessageIntent.QUERY_STATUS:
            # 查询进度 → 直接返回，不发给 Claude
            return await self._handle_status_query(session)

        elif intent == MessageIntent.INTERRUPT:
            # 中断任务
            return await self._handle_interrupt(session)

        elif intent == MessageIntent.NEW_TASK:
            # 新任务 → 加入队列
            return await self._handle_new_task(session, message, task_context)

        elif intent == MessageIntent.CONTEXT_FOLLOWUP:
            # 上下文追问 → 加入队列
            return await self._handle_context_followup(session, message)

        else:
            return "无法识别您的意图，请重新描述"

    async def _handle_status_query(self, session: SessionInfo) -> str:
        """处理进度查询（不发给Claude）"""
        if session.status == SessionStatus.RUNNING:
            # 正在运行中
            return session.get_progress_summary()

        elif session.status == SessionStatus.IDLE:
            # 已完成
            if session.task_status == "completed":
                return f"✅ 任务已完成！\n\n结果：\n{self._format_result(session.task_result)}"
            elif session.task_status == "failed":
                return f"❌ 任务执行失败：{session.error_message}"

        else:
            return "当前没有正在运行的任务"

    async def _handle_interrupt(self, session: SessionInfo) -> str:
        """处理中断请求"""
        if session.client and session.status == SessionStatus.RUNNING:
            try:
                await session.client.interrupt()
                session.task_status = "interrupted"
                session.status = SessionStatus.IDLE
                return "✅ 任务已停止"
            except Exception as e:
                return f"❌ 停止失败：{str(e)}"
        else:
            return "当前没有正在运行的任务"

    async def _handle_new_task(
        self,
        session: SessionInfo,
        message: str,
        task_context: str
    ) -> str:
        """处理新任务（加入队列或创建新Session）"""
        # 判断：是否应该在当前 Session 中排队，还是创建新 Session
        # 策略：如果 task_context 相同，则排队；否则创建新 Session

        current_context_hash = hashlib.md5(session.task_context.encode()).hexdigest()[:8]
        new_context_hash = hashlib.md5(task_context.encode()).hexdigest()[:8]

        if current_context_hash == new_context_hash:
            # 相同上下文，加入队列
            await session.pending_messages.put(message)
            queue_size = session.pending_messages.qsize()
            return f"✅ 已收到新任务，当前排队数：{queue_size}"
        else:
            # 不同上下文，创建新 Session
            new_session = await self.get_or_create_session(
                session.user_id,
                task_context,
                force_new=True
            )
            await new_session.pending_messages.put(message)
            return f"✅ 已创建新任务（Session ID: {new_session.session_key}）"

    async def _handle_context_followup(self, session: SessionInfo, message: str) -> str:
        """处理上下文追问（基于当前任务的追问）"""
        if session.status == SessionStatus.RUNNING:
            # 正在运行中，加入队列
            await session.pending_messages.put(message)
            return "✅ 已收到您的追问，当前任务完成后会回答"

        elif session.status == SessionStatus.IDLE and session.task_result:
            # 任务已完成，可以立即发送（基于历史上下文）
            await session.pending_messages.put(message)
            return "✅ 正在基于之前的结果回答您的问题..."

        else:
            return "没有可以追问的上下文，请先提交一个任务"

    def _format_result(self, result: Optional[Dict[str, Any]]) -> str:
        """格式化任务结果"""
        if not result:
            return "无结果"

        # 提取关键信息（根据实际消息格式调整）
        messages = result.get("messages", [])

        # 找到最后一条文本消息
        for msg in reversed(messages):
            if msg.get("type") == "message" and "content" in msg:
                return str(msg["content"])[:500]  # 截取前500字符

        return "任务已完成，但无详细结果"

    async def _close_session(self, session_key: str):
        """关闭 Session"""
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

## 实际运行示例

### 示例1：用户追问进度（立即返回）

```python
async def example_status_query():
    """示例：用户追问进度"""
    manager = SessionManager()
    await manager.start()

    try:
        user_id = "user123"
        link = "https://console.baidu.com/itp/xxx"

        # T0: 第一次请求
        response1 = await manager.handle_message(
            user_id=user_id,
            message=f"帮我排查这个链接 {link}",
            task_context=link
        )
        print(f"[T0] {response1}")
        # 输出: "✅ 已收到新任务，当前排队数：1"

        # 模拟任务在后台运行
        await asyncio.sleep(7)  # 7秒后

        # T7: 追问进度
        response2 = await manager.handle_message(
            user_id=user_id,
            message="刚才那个问题查得怎么样了？",
            task_context=link  # 👈 相同的 task_context
        )
        print(f"[T7] {response2}")
        # 输出: "🔄 任务进行中（已运行 7.0 秒）
        #        📊 当前阶段：查询数据库
        #        ⏱️ 进度：20.0%"

        # 👆 注意：立即返回！不需要等待任务完成

    finally:
        await manager.stop()

# 运行
asyncio.run(example_status_query())
```

**关键点**：
- ✅ 第二条消息被识别为 `QUERY_STATUS`
- ✅ 直接从 `SessionInfo.progress` 读取状态
- ✅ **不发给 Claude**，立即返回

---

### 示例2：用户提交新任务（排队）

```python
async def example_new_task_queue():
    """示例：用户提交新任务"""
    manager = SessionManager()
    await manager.start()

    try:
        user_id = "user123"
        link1 = "https://console.baidu.com/itp/xxx"

        # T0: 第一个任务
        response1 = await manager.handle_message(
            user_id=user_id,
            message=f"帮我排查链接1 {link1}",
            task_context=link1
        )
        print(f"[T0] {response1}")
        # 输出: "✅ 已收到新任务..."

        # T3: 第二个任务
        link2 = "https://console.baidu.com/itp/yyy"
        response2 = await manager.handle_message(
            user_id=user_id,
            message=f"帮我排查链接2 {link2}",
            task_context=link2  # 👈 不同的 task_context
        )
        print(f"[T3] {response2}")
        # 输出: "✅ 已创建新任务（Session ID: user123_yyyy）"

        # 👆 注意：创建了新的 Session，与任务1并行执行

        # 如果是相同的 task_context
        response3 = await manager.handle_message(
            user_id=user_id,
            message="再帮我详细看看这个链接的其他问题",
            task_context=link1  # 👈 相同的 task_context
        )
        print(f"[T3+] {response3}")
        # 输出: "✅ 已收到新任务，当前排队数：1"

        # 👆 注意：加入 Session1 的队列，等任务1完成后执行

    finally:
        await manager.stop()
```

**关键点**：
- ✅ 不同 `task_context` → 创建新 Session（并行）
- ✅ 相同 `task_context` → 加入队列（串行）

---

## 面试回答模板

### 问题："用户追问进度时，你怎么保证立即返回，而不是排队等待？"

### 参考回答

**第一步：明确问题**
> "这是一个非常实际的生产问题。用户问'刚才那个任务怎么样了'，期望的是立即得到状态反馈，而不是排队等10分钟后才回复——那样用户体验就太差了。"

**第二步：分析根本原因**
> "Claude CLI 的消息处理是**顺序的**（FIFO 队列）。如果我把所有用户消息都直接发给 Claude，那么查询进度的消息也会排队，需要等前面的长任务执行完才能处理。
>
> 所以核心解决思路是：**区分查询操作和执行操作**——查询操作不应该发给 Claude，而是直接从应用层的状态管理器获取。"

**第三步：说明具体实现**
> "我的实现方案分三步：
>
> **1. 意图识别**
> - 对每条用户消息进行意图分类：查询进度 / 新任务 / 上下文追问 / 中断
> - 使用关键词匹配（如'怎么样了'、'进度'）快速识别
> - 也可以用小模型（如 Haiku）来做更准确的意图识别
>
> **2. 路由策略**
> - 如果是**查询进度**：直接从 `SessionInfo.progress` 读取状态，立即返回 → **不发给 Claude**
> - 如果是**新任务**：发给 Claude，进入消息队列
> - 如果是**上下文追问**：发给 Claude，基于历史上下文回答
>
> **3. 进度跟踪**
> - 在 `SessionInfo` 中维护 `TaskProgress` 对象
> - 包括：当前阶段、进度百分比、已运行时间、最新进展消息
> - 从 Claude 的流式输出中解析进度信息（如'正在查询数据库'→20%）"

**第四步：举实际例子**
> "举个例子：
> ```
> T0:  用户：'帮我排查这个链接'
>      → 意图识别：NEW_TASK
>      → 发给 Claude，任务开始（预计10分钟）
>
> T7:  用户：'刚才那个问题怎么样了？'
>      → 意图识别：QUERY_STATUS
>      → 不发给 Claude，直接返回：
>         '🔄 任务进行中（已运行7分钟）
>          📊 当前阶段：分析日志
>          ⏱️ 进度：50%'
> ```
> 关键是第二条消息**不进入 Claude 的 stdin 队列**，所以可以立即返回。"

**第五步：对比另一种场景**
> "相反，如果用户发的是**新任务**：
> ```
> T0:  用户：'帮我排查链接1'
>      → 任务1开始
>
> T3:  用户：'帮我排查链接2'
>      → 意图识别：NEW_TASK
>      → 判断 task_context：
>         - 如果是不同链接 → 创建新 Session（并行执行）
>         - 如果是同一链接的追加问题 → 加入队列（串行执行）
> ```
> 这样既保证了查询的即时性，又保证了任务的有序执行。"

**第六步：总结技术价值**
> "所以总结来说，我在 Session 管理层做的核心工作是：
> 1. **意图识别**：区分查询操作和执行操作
> 2. **智能路由**：查询操作走应用层，执行操作走 Claude
> 3. **进度跟踪**：实时解析 Claude 的输出，维护可查询的进度状态
> 4. **队列管理**：为每个 Session 维护独立的消息队列
>
> 这些都是 Claude SDK 本身不提供的，需要在应用层自己设计。"

---

## 关键技术点总结

| 维度 | Claude SDK 提供的 | 你需要做的 |
|------|------------------|----------|
| **消息路由** | 所有消息都进 stdin 队列 | ✅ 意图识别 + 智能路由 |
| **进度查询** | 不支持 | ✅ 解析流式输出 + 维护进度状态 |
| **任务队列** | 单队列（stdin） | ✅ 每个 Session 独立队列 |
| **并发控制** | 单进程顺序处理 | ✅ 多 Session 并行 + 单 Session 串行 |
| **超时清理** | 不支持 | ✅ 后台清理任务 |

---

**文档版本**：v2.0
**适用SDK版本**：claude-agent-sdk >= 0.0.20
**维护者**：Ducc AI Team
**最后更新**：2026-04-17
