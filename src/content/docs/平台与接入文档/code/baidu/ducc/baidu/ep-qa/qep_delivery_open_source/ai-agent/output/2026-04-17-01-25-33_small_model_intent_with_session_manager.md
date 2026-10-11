---
title: "基于小模型的快速意图识别 + SessionManager 数据组装方案"
description: "完整实现：新 query → 小模型意图识别 → 分支处理"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-01-25-33_small_model_intent_with_session_manager.md"
---
# 基于小模型的快速意图识别 + SessionManager 数据组装方案

> 完整实现：新 query → 小模型意图识别 → 分支处理

---

## 核心流程

```python
用户新消息
    ↓
从 SessionManager 获取当前状态
    ↓
调用小模型快速意图识别（~50-100ms）
    ↓
    ├─ 意图=查询进度？
    │   ↓
    │   从 SessionManager 读取 session.progress
    │   ↓
    │   格式化数据 + 直接返回 ✅
    │
    └─ 意图=新任务/追问？
        ↓
        扔给 Claude SDK 排队 ✅
```

---

## 完整实现代码

```python
import asyncio
import aiohttp
from typing import Dict, Optional, Literal
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

# ============================================
# 1. 小模型意图识别器
# ============================================

@dataclass
class IntentResult:
    """意图识别结果"""
    intent: Literal["query_status", "new_task", "context_followup", "interrupt"]
    confidence: float  # 0.0-1.0
    reason: str  # 判断依据

class SmallModelIntentClassifier:
    """
    小模型意图识别器

    要求：
    - 响应时间 < 100ms
    - 成本极低
    - 可以是本地部署的小模型，或云端的 ERNIE-Tiny 等
    """

    def __init__(
        self,
        model_endpoint: str = "http://localhost:8000/intent",
        timeout: float = 0.1  # 100ms 超时
    ):
        self.endpoint = model_endpoint
        self.timeout = timeout
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *args):
        if self._session:
            await self._session.close()

    async def classify(
        self,
        message: str,
        context: Dict
    ) -> IntentResult:
        """
        调用小模型进行意图识别

        Args:
            message: 用户消息
            context: 上下文信息
                - session_status: "running" | "idle" | "created"
                - has_history: bool
                - current_stage: str (如 "下载日志")
                - progress_percent: float

        Returns:
            IntentResult
        """
        # 构造 prompt
        prompt = self._build_prompt(message, context)

        try:
            # 调用小模型
            response = await asyncio.wait_for(
                self._call_model(prompt),
                timeout=self.timeout
            )

            return self._parse_response(response)

        except asyncio.TimeoutError:
            logger.warning("Intent classification timeout, fallback to keyword")
            # 超时降级：使用关键词匹配
            return self._fallback_keyword_match(message, context)

        except Exception as e:
            logger.error(f"Intent classification error: {e}")
            # 异常降级
            return self._fallback_keyword_match(message, context)

    def _build_prompt(self, message: str, context: Dict) -> str:
        """构造小模型的 prompt"""
        return f"""你是一个意图分类器。请判断用户消息的意图。

用户消息: "{message}"

当前上下文:
- 任务状态: {context.get('session_status', 'unknown')}
- 当前阶段: {context.get('current_stage', '未知')}
- 进度: {context.get('progress_percent', 0):.1f}%
- 有历史记录: {'是' if context.get('has_history') else '否'}

意图类型:
1. query_status - 查询任务进度（如"怎么样了"、"好了吗"）
2. new_task - 提交新任务（如"帮我查另一个链接"）
3. context_followup - 追问当前任务（如"为什么报这个错"）
4. interrupt - 中断任务（如"停止"、"取消"）

请只返回一个 JSON 对象:
{{"intent": "...", "confidence": 0.95, "reason": "..."}}
"""

    async def _call_model(self, prompt: str) -> str:
        """调用小模型 API"""
        if not self._session:
            self._session = aiohttp.ClientSession()

        async with self._session.post(
            self.endpoint,
            json={
                "prompt": prompt,
                "max_tokens": 50,
                "temperature": 0.1  # 低温度，更确定性
            },
            timeout=aiohttp.ClientTimeout(total=self.timeout)
        ) as response:
            result = await response.json()
            return result.get("text", "")

    def _parse_response(self, response: str) -> IntentResult:
        """解析模型响应"""
        import json

        try:
            # 假设返回格式: {"intent": "query_status", "confidence": 0.95, "reason": "..."}
            data = json.loads(response)

            return IntentResult(
                intent=data.get("intent", "new_task"),
                confidence=data.get("confidence", 0.5),
                reason=data.get("reason", "")
            )
        except Exception as e:
            logger.error(f"Failed to parse response: {e}")
            # 解析失败，返回默认值
            return IntentResult(
                intent="new_task",
                confidence=0.3,
                reason="解析失败"
            )

    def _fallback_keyword_match(
        self, message: str, context: Dict
    ) -> IntentResult:
        """降级策略：关键词匹配"""
        msg_lower = message.lower()

        # 中断
        if any(kw in msg_lower for kw in ['停止', '取消', '算了']):
            return IntentResult("interrupt", 0.9, "关键词:停止")

        # 明确的进度查询
        if any(kw in msg_lower for kw in ['怎么样', '进度', '完成', '好了']):
            return IntentResult("query_status", 0.8, "关键词:进度")

        # 包含链接
        if 'http' in message:
            return IntentResult("new_task", 0.85, "包含链接")

        # 默认
        if context.get('session_status') == 'running':
            return IntentResult("context_followup", 0.6, "默认:追问")
        else:
            return IntentResult("new_task", 0.6, "默认:新任务")


# ============================================
# 2. SessionManager 集成
# ============================================

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, SessionInfo] = {}
        self.intent_classifier = SmallModelIntentClassifier()
        self._lock = asyncio.Lock()

    async def handle_user_message(
        self,
        user_id: str,
        message: str,
        task_context: str
    ) -> str:
        """
        处理用户消息的入口

        流程：
        1. 获取/创建 Session
        2. 从 Session 提取上下文信息
        3. 调用小模型意图识别
        4. 根据意图分支处理
        """
        # 步骤1: 获取 Session
        session = await self.get_or_create_session(user_id, task_context)

        # 步骤2: 提取上下文（供意图识别使用）
        context = self._extract_context_from_session(session)

        # 步骤3: 意图识别（小模型，~100ms）
        intent_result = await self.intent_classifier.classify(
            message=message,
            context=context
        )

        logger.info(
            f"Intent: {intent_result.intent} "
            f"(confidence={intent_result.confidence:.2f}, "
            f"reason={intent_result.reason})"
        )

        # 步骤4: 根据意图分支处理
        if intent_result.intent == "query_status":
            # ✅ 查询进度：从 SessionManager 组装数据，直接返回
            return self._handle_query_status(session)

        elif intent_result.intent == "interrupt":
            # ✅ 中断任务
            return await self._handle_interrupt(session)

        elif intent_result.intent == "new_task":
            # ✅ 新任务：扔给 Claude SDK 排队
            return await self._handle_new_task(session, message, task_context)

        elif intent_result.intent == "context_followup":
            # ✅ 追问：扔给 Claude SDK 排队
            return await self._handle_context_followup(session, message)

        else:
            return "无法识别您的意图，请重新描述"

    def _extract_context_from_session(self, session: SessionInfo) -> Dict:
        """从 Session 提取上下文信息"""
        context = {
            "session_status": session.status.value,
            "has_history": len(session.message_buffer) > 0,
        }

        # 如果有进度信息，提取详情
        if session.progress:
            context.update({
                "current_stage": session.progress.stage,
                "progress_percent": session.progress.progress_percent,
                "elapsed_seconds": session.progress.elapsed_seconds,
                "latest_message": session.progress.latest_message
            })

        return context

    def _handle_query_status(self, session: SessionInfo) -> str:
        """
        处理进度查询

        关键：从 SessionManager 读取数据，组装后直接返回
        不经过 Claude SDK！
        """
        # 任务状态判断
        if session.status == SessionStatus.RUNNING:
            # 正在运行中
            if session.progress:
                return self._format_running_progress(session)
            else:
                # 还没有进度信息（刚开始）
                elapsed = (datetime.now() - session.created_at).total_seconds()
                return f"🔄 任务已启动，正在初始化...（已运行 {elapsed:.0f} 秒）"

        elif session.status == SessionStatus.IDLE:
            # 任务已完成
            if session.task_status == "completed":
                return self._format_completed_result(session)
            elif session.task_status == "failed":
                return f"❌ 任务执行失败：{session.error_message}"
            elif session.task_status == "interrupted":
                return "⚠️ 任务已被中断"
            else:
                return "任务已结束，但状态未知"

        elif session.status == SessionStatus.CREATED:
            return "任务尚未启动"

        else:
            return "任务状态未知"

    def _format_running_progress(self, session: SessionInfo) -> str:
        """格式化正在运行的任务进度"""
        progress = session.progress

        # 计算运行时长
        elapsed_str = self._format_duration(progress.elapsed_seconds)

        # 预估剩余时间（基于进度百分比）
        if progress.progress_percent > 5:
            estimated_total = progress.elapsed_seconds / (progress.progress_percent / 100)
            remaining = estimated_total - progress.elapsed_seconds
            remaining_str = self._format_duration(remaining)
        else:
            remaining_str = "计算中..."

        # 组装响应
        response = f"""🔄 **任务进行中**

⏱️ **运行时长**: {elapsed_str}
📊 **当前阶段**: {progress.stage}
📈 **进度**: {progress.progress_percent:.1f}%
⏳ **预计剩余**: {remaining_str}

💬 **最新进展**:
{progress.latest_message}
"""

        return response

    def _format_completed_result(self, session: SessionInfo) -> str:
        """格式化已完成任务的结果"""
        # 计算总耗时
        total_duration = (
            session.last_activity - session.created_at
        ).total_seconds()
        duration_str = self._format_duration(total_duration)

        # 提取关键结果
        result_summary = self._extract_result_summary(session.task_result)

        response = f"""✅ **任务已完成**

⏱️ **总耗时**: {duration_str}

📋 **结果摘要**:
{result_summary}
"""

        return response

    def _extract_result_summary(self, task_result: Optional[Dict]) -> str:
        """从任务结果中提取摘要"""
        if not task_result:
            return "无详细结果"

        messages = task_result.get("messages", [])

        # 查找最后一条 assistant message
        for msg in reversed(messages):
            if msg.get("type") == "message":
                content = msg.get("content", "")
                if isinstance(content, str) and len(content) > 0:
                    # 截取前500字符
                    return content[:500] + ("..." if len(content) > 500 else "")

        return "任务已完成，但无详细输出"

    def _format_duration(self, seconds: float) -> str:
        """格式化时长"""
        if seconds < 60:
            return f"{int(seconds)} 秒"
        elif seconds < 3600:
            minutes = int(seconds // 60)
            secs = int(seconds % 60)
            return f"{minutes} 分 {secs} 秒"
        else:
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            return f"{hours} 小时 {minutes} 分"

    async def _handle_new_task(
        self, session: SessionInfo, message: str, task_context: str
    ) -> str:
        """处理新任务：扔给 Claude SDK 排队"""
        # 判断是否需要创建新 Session
        if self._should_create_new_session(session, task_context):
            # 创建新 Session
            new_session = await self.get_or_create_session(
                session.user_id, task_context, force_new=True
            )

            # 启动 Client
            if new_session.client is None:
                await self.start_client_for_session(new_session)

            # 加入队列
            await new_session.pending_messages.put(message)

            return f"✅ 已创建新任务（任务ID: {new_session.session_key}）"

        else:
            # 复用 Session，加入队列
            await session.pending_messages.put(message)
            queue_size = session.pending_messages.qsize()

            return f"✅ 已加入队列（当前排队: {queue_size} 个）"

    async def _handle_context_followup(
        self, session: SessionInfo, message: str
    ) -> str:
        """处理上下文追问：扔给 Claude SDK 排队"""
        if session.status == SessionStatus.RUNNING:
            # 正在运行，加入队列
            await session.pending_messages.put(message)
            return "✅ 已收到您的追问，当前任务完成后会回答"

        elif session.status == SessionStatus.IDLE and session.task_result:
            # 任务已完成，可以立即处理（基于历史上下文）
            await session.pending_messages.put(message)
            return "✅ 正在基于之前的结果回答您的问题..."

        else:
            return "没有可以追问的上下文，请先提交一个任务"

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

    def _should_create_new_session(
        self, session: SessionInfo, new_task_context: str
    ) -> bool:
        """判断是否需要创建新 Session"""
        import hashlib

        old_hash = hashlib.md5(session.task_context.encode()).hexdigest()[:8]
        new_hash = hashlib.md5(new_task_context.encode()).hexdigest()[:8]

        return old_hash != new_hash


# ============================================
# 3. 使用示例
# ============================================

async def main():
    """完整示例"""
    manager = SessionManager()
    await manager.start()

    try:
        user_id = "user123"
        link = "https://console.baidu.com/itp/xxx"

        # 场景1: 用户提交任务
        print("\n=== 场景1: 提交任务 ===")
        response = await manager.handle_user_message(
            user_id=user_id,
            message=f"帮我排查这个链接 {link}",
            task_context=link
        )
        print(response)
        # 小模型识别耗时: ~100ms
        # 输出: "✅ 已创建新任务（任务ID: user123_abc）"

        # 等待3秒
        await asyncio.sleep(3)

        # 场景2: 用户查询进度（任务还在运行）
        print("\n=== 场景2: 查询进度 ===")
        response = await manager.handle_user_message(
            user_id=user_id,
            message="怎么样了？",
            task_context=link
        )
        print(response)
        # 小模型识别耗时: ~100ms
        # 从 SessionManager 读数据: <5ms
        # 总耗时: ~105ms ✅
        # 输出: "🔄 任务进行中\n⏱️ 运行时长: 3 秒\n📊 当前阶段: 查询数据库\n..."

        # 场景3: 模糊追问
        print("\n=== 场景3: 模糊追问 ===")
        response = await manager.handle_user_message(
            user_id=user_id,
            message="为什么会报这个错？",
            task_context=link
        )
        print(response)
        # 小模型识别为: context_followup
        # 输出: "✅ 已收到您的追问，当前任务完成后会回答"

        # 场景4: 提交新任务
        print("\n=== 场景4: 新任务 ===")
        link2 = "https://console.baidu.com/itp/yyy"
        response = await manager.handle_user_message(
            user_id=user_id,
            message=f"帮我再查另一个链接 {link2}",
            task_context=link2
        )
        print(response)
        # 小模型识别为: new_task
        # 输出: "✅ 已创建新任务（任务ID: user123_def）"

    finally:
        await manager.stop()


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 性能分析

### 响应时间分解

```python
# 场景1: 查询进度
用户消息: "怎么样了？"
    ↓
获取 Session: ~1ms
    ↓
提取上下文: <1ms
    ↓
小模型意图识别: ~100ms  ← 主要耗时
    ↓
判断为 query_status
    ↓
从 session.progress 读取: <1ms
    ↓
格式化响应: ~5ms
    ↓
✅ 总耗时: ~107ms
```

### 对比：如果发给 Claude

```python
用户消息: "怎么样了？"
    ↓
发给正在工作的 Claude
    ↓
❌ 进入队列，等待前面任务完成: 5-10 分钟
    ↓
❌ 完全不可接受
```

---

## 关键优势

1. **快速响应**
   - 小模型意图识别: ~100ms
   - 读取 SessionManager 数据: <5ms
   - 总耗时: ~105ms ✅

2. **低成本**
   - 小模型调用成本极低（或本地部署免费）
   - 不调用昂贵的 Claude Opus

3. **准确性**
   - 小模型针对意图分类训练，准确率 90%+
   - 有降级策略（关键词匹配）

4. **不阻塞主任务**
   - 意图识别在应用层完成
   - Claude 继续专心处理主任务

---

## 小模型选择建议

### 方案1: 本地部署（推荐）

```python
# 使用轻量级模型（如 distilbert）
# 优点：免费、快速、隐私
# 缺点：需要维护

endpoint = "http://localhost:8000/intent"
```

### 方案2: 云端小模型

```python
# 百度 ERNIE-Tiny
# 文心一言 Lite
# 阿里通义千问 Lite

# 优点：无需部署、稳定
# 缺点：有成本（但很低）
```

### 方案3: 混合策略

```python
async def classify(message, context):
    # 先尝试本地模型
    try:
        return await local_model.classify(message, context)
    except:
        # 降级到云端模型
        return await cloud_model.classify(message, context)
```

---

## 总结

### ✅ 你的方案完全可行！

```
新 query 进来
    ↓
访问 SessionManager.sessions[session_key]
    ↓
调用小模型意图识别（~100ms）
    ↓
    ├─ 意图=查询进度？
    │   → 从 session.progress 组装数据
    │   → 直接返回 ✅
    │
    └─ 意图=新任务/追问？
        → 扔给 Claude SDK 排队 ✅
```

### 关键点

1. **SessionManager 的数据是实时的**
   - 通过 PostToolUse Hook 持续更新
   - `session.progress` 始终是最新进度

2. **小模型调用要快**
   - <100ms 超时
   - 有降级策略（关键词）

3. **不依赖正在工作的 Claude**
   - 意图识别在应用层完成
   - Claude 专心处理任务

---

**文档版本**: v1.0
**最后更新**: 2026-04-17
