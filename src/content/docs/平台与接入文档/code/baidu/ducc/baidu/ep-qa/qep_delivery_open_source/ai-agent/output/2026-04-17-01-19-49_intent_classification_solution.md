---
title: "意图识别的困境与解决方案"
description: "文档生成时间：2026-04-17 01:19:49 核心问题：意图识别本身不能排队，否则失去意义"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-01-19-49_intent_classification_solution.md"
---
# 意图识别的困境与解决方案

> 文档生成时间：2026-04-17 01:19:49
> 核心问题：意图识别本身不能排队，否则失去意义

---

## 问题描述

### 核心矛盾

```python
# 场景：用户追问进度
用户: "刚才那个问题怎么样了？"

# 错误的处理流程 ❌
1. 收到消息
2. 需要判断意图（是查询进度？还是新问题？）
3. 发给正在工作的 Claude：
   await claude.query("请判断这条消息的意图: '刚才那个问题怎么样了？'")
4. ⚠️ 消息进入 stdin 队列
5. ⚠️ 等待前面的任务完成（可能还要等5分钟）
6. ❌ Claude 返回："这是查询进度"
7. ❌ 再返回进度给用户（此时用户已经等了5分钟）

# 结果：完全失去了"立即返回"的意义！
```

### 问题根源

**意图识别如果依赖正在工作的 Claude，就会进入队列，无法实现即时响应**

---

## 解决方案对比

### 方案1：纯关键词匹配（推荐）

**原理**：基于正则表达式和关键词快速判断

```python
import re
from enum import Enum

class MessageIntent(Enum):
    QUERY_STATUS = "query_status"
    NEW_TASK = "new_task"
    CONTEXT_FOLLOWUP = "context_followup"
    INTERRUPT = "interrupt"

def classify_intent_fast(
    message: str,
    session_status: str,  # "running" | "idle" | "closed"
    has_history: bool
) -> MessageIntent:
    """
    快速意图识别（<1ms，不依赖 LLM）

    Args:
        message: 用户消息
        session_status: 当前 Session 状态
        has_history: 是否有历史对话

    Returns:
        MessageIntent
    """
    msg_lower = message.lower()

    # 规则1：中断指令（最高优先级）
    interrupt_patterns = [
        r'停止', r'取消', r'别.*了', r'不用.*了', r'算了'
    ]
    for pattern in interrupt_patterns:
        if re.search(pattern, msg_lower):
            return MessageIntent.INTERRUPT

    # 规则2：明确的进度查询（高优先级）
    status_patterns = [
        r'怎么样了', r'查得.*如何', r'进度',
        r'跑.*完.*吗', r'好.*了.*吗', r'完成.*吗',
        r'还.*在.*跑', r'查到.*吗', r'结果.*了.*吗',
        r'弄.*怎么样', r'搞.*定.*吗'
    ]
    for pattern in status_patterns:
        if re.search(pattern, msg_lower):
            return MessageIntent.QUERY_STATUS

    # 规则3：如果当前没有运行任务，且没有历史
    if session_status != "running" and not has_history:
        return MessageIntent.NEW_TASK

    # 规则4：如果当前有运行任务
    if session_status == "running":
        # 4.1 检查是否包含新任务的明确指示
        new_task_indicators = [
            r'http[s]?://',  # 包含链接
            r'帮我.*查', r'帮我.*排查', r'再.*帮',
            r'另一个', r'新的', r'再.*看看'
        ]

        has_new_task_indicator = any(
            re.search(pattern, message)
            for pattern in new_task_indicators
        )

        # 4.2 检查是否引用当前任务
        reference_patterns = [
            r'刚才', r'之前', r'刚刚', r'上面',
            r'这个', r'那个', r'它', r'他'
        ]

        has_reference = any(
            re.search(pattern, msg_lower)
            for pattern in reference_patterns
        )

        # 判断逻辑
        if has_new_task_indicator and not has_reference:
            # "帮我再查另一个链接" → 新任务
            return MessageIntent.NEW_TASK
        elif has_reference or not has_new_task_indicator:
            # "刚才那个为什么报错" → 上下文追问
            return MessageIntent.CONTEXT_FOLLOWUP
        else:
            # 模糊情况，默认为上下文追问（保守策略）
            return MessageIntent.CONTEXT_FOLLOWUP

    # 规则5：任务已完成，有历史
    if session_status == "idle" and has_history:
        # 检查是否是新任务
        new_task_keywords = ['帮我', '再', '另一个', 'http']
        if any(kw in message for kw in new_task_keywords):
            return MessageIntent.NEW_TASK
        else:
            # 默认为追问之前的结果
            return MessageIntent.CONTEXT_FOLLOWUP

    # 默认：新任务
    return MessageIntent.NEW_TASK


# 使用示例
intent = classify_intent_fast(
    message="刚才那个问题怎么样了？",
    session_status="running",
    has_history=True
)
# 返回: MessageIntent.QUERY_STATUS
# 耗时: <1ms ✅
```

**优点**：
- ✅ 极快（<1ms）
- ✅ 零成本
- ✅ 准确率 80-85%（足够应对大部分场景）
- ✅ 可维护（规则清晰）

**缺点**：
- ⚠️ 边界情况可能误判
- ⚠️ 需要持续维护规则

---

### 方案2：小模型分类器（备选）

**原理**：使用快速的小模型做意图分类（不是完整推理）

```python
import asyncio
from typing import Dict

# 假设使用百度的 ERNIE-Tiny 或本地模型
class FastIntentClassifier:
    """快速意图分类器（使用小模型）"""

    def __init__(self, model_endpoint: str = "http://localhost:8000/classify"):
        self.endpoint = model_endpoint
        self.cache: Dict[str, MessageIntent] = {}  # 简单缓存

    async def classify(
        self,
        message: str,
        context: Dict
    ) -> MessageIntent:
        """
        使用小模型分类意图

        预期响应时间: ~100ms
        """
        # 检查缓存
        cache_key = f"{message}_{context.get('session_status')}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        # 构造分类请求
        prompt = self._build_classification_prompt(message, context)

        # 调用小模型（非 Claude）
        try:
            response = await self._call_small_model(prompt)
            intent = self._parse_response(response)

            # 缓存结果
            self.cache[cache_key] = intent

            return intent
        except Exception as e:
            # 降级到关键词匹配
            return classify_intent_fast(
                message,
                context.get("session_status", "idle"),
                context.get("has_history", False)
            )

    def _build_classification_prompt(self, message: str, context: Dict) -> str:
        """构造分类 prompt（针对小模型优化）"""
        return f"""意图分类任务：
用户消息: "{message}"
当前状态: {context.get('session_status')}
历史记录: {'有' if context.get('has_history') else '无'}

请返回以下之一：
- query_status (查询进度)
- new_task (新任务)
- context_followup (追问)
- interrupt (中断)

只返回一个单词，不要解释。
"""

    async def _call_small_model(self, prompt: str) -> str:
        """调用小模型 API"""
        import aiohttp

        async with aiohttp.ClientSession() as session:
            async with session.post(
                self.endpoint,
                json={"prompt": prompt, "max_tokens": 10},
                timeout=aiohttp.ClientTimeout(total=0.5)  # 500ms 超时
            ) as response:
                result = await response.json()
                return result["text"]

    def _parse_response(self, response: str) -> MessageIntent:
        """解析模型响应"""
        response_lower = response.strip().lower()

        if "query_status" in response_lower:
            return MessageIntent.QUERY_STATUS
        elif "new_task" in response_lower:
            return MessageIntent.NEW_TASK
        elif "interrupt" in response_lower:
            return MessageIntent.INTERRUPT
        else:
            return MessageIntent.CONTEXT_FOLLOWUP


# 使用示例
classifier = FastIntentClassifier()

intent = await classifier.classify(
    message="刚才那个问题怎么样了？",
    context={
        "session_status": "running",
        "has_history": True
    }
)
# 返回: MessageIntent.QUERY_STATUS
# 耗时: ~100ms ✅（比关键词慢，但仍然可接受）
```

**优点**：
- ✅ 比关键词更准确（90%+）
- ✅ 成本低（小模型便宜）
- ✅ 仍然很快（~100ms）

**缺点**：
- ⚠️ 需要部署额外服务
- ⚠️ 比关键词慢
- ⚠️ 有网络依赖

---

### 方案3：混合方案（推荐用于复杂场景）

**原理**：关键词 + 小模型，兼顾速度和准确性

```python
class HybridIntentClassifier:
    """混合意图识别器"""

    def __init__(self):
        self.fast_classifier = FastIntentClassifier()

    async def classify(
        self,
        message: str,
        session_status: str,
        has_history: bool
    ) -> MessageIntent:
        """
        混合策略：
        1. 先用关键词快速判断（<1ms）
        2. 如果置信度高，直接返回
        3. 如果置信度低，用小模型确认（~100ms）
        """
        # 第一步：关键词快速分类
        intent, confidence = self._classify_with_confidence(
            message, session_status, has_history
        )

        # 如果置信度高，直接返回
        if confidence >= 0.9:
            return intent

        # 置信度低，用小模型确认
        try:
            intent = await asyncio.wait_for(
                self.fast_classifier.classify(
                    message,
                    {
                        "session_status": session_status,
                        "has_history": has_history
                    }
                ),
                timeout=0.2  # 200ms 超时
            )
        except asyncio.TimeoutError:
            # 超时，使用关键词结果
            pass

        return intent

    def _classify_with_confidence(
        self, message: str, session_status: str, has_history: bool
    ) -> tuple[MessageIntent, float]:
        """
        关键词分类 + 置信度评估

        Returns:
            (intent, confidence)  # confidence: 0.0-1.0
        """
        msg_lower = message.lower()

        # 高置信度场景

        # 1. 明确的进度查询关键词
        strong_status_keywords = ['怎么样了', '进度', '完成了吗', '好了吗']
        if any(kw in msg_lower for kw in strong_status_keywords):
            return MessageIntent.QUERY_STATUS, 0.95

        # 2. 明确的中断指令
        if any(kw in msg_lower for kw in ['停止', '取消', '算了']):
            return MessageIntent.INTERRUPT, 0.99

        # 3. 包含新链接
        if 'http' in message:
            return MessageIntent.NEW_TASK, 0.9

        # 中等置信度场景

        # 4. 模糊的查询
        weak_status_keywords = ['怎么', '如何', '什么']
        if any(kw in msg_lower for kw in weak_status_keywords):
            if session_status == "running":
                return MessageIntent.QUERY_STATUS, 0.7  # 低置信度

        # 5. 默认情况
        intent = classify_intent_fast(message, session_status, has_history)
        return intent, 0.6  # 低置信度
```

---

## SessionManager 集成

### 完整流程

```python
class SessionManager:
    def __init__(self):
        # 使用混合分类器
        self.intent_classifier = HybridIntentClassifier()

    async def handle_message(
        self,
        user_id: str,
        message: str,
        task_context: str
    ) -> str:
        """
        处理用户消息（带意图识别）

        关键：意图识别在应用层完成，不依赖正在工作的 Claude
        """
        # 1. 获取或创建 Session
        session = await self.get_or_create_session(user_id, task_context)

        # 2. 【应用层】快速意图识别（不排队！）
        intent = await self.intent_classifier.classify(
            message=message,
            session_status=session.status.value,
            has_history=bool(session.message_buffer)
        )

        logger.info(
            f"Intent classified: {intent} "
            f"(session={session.session_key}, status={session.status})"
        )

        # 3. 根据意图路由
        if intent == MessageIntent.QUERY_STATUS:
            # ✅ 查询进度：直接返回，不发给 Claude
            return self._handle_status_query(session)

        elif intent == MessageIntent.INTERRUPT:
            # ✅ 中断：调用 interrupt()
            return await self._handle_interrupt(session)

        elif intent == MessageIntent.NEW_TASK:
            # ✅ 新任务：创建新 Session 或加入队列
            return await self._handle_new_task(session, message, task_context)

        elif intent == MessageIntent.CONTEXT_FOLLOWUP:
            # ✅ 上下文追问：加入队列（发给 Claude）
            return await self._handle_context_followup(session, message)

    def _handle_status_query(self, session: SessionInfo) -> str:
        """处理进度查询（应用层直接返回）"""
        if session.status == SessionStatus.RUNNING:
            # 任务运行中，返回实时进度
            return session.get_progress_summary()

        elif session.status == SessionStatus.IDLE:
            # 任务已完成
            if session.task_result:
                return f"✅ 任务已完成！\n\n{self._format_result(session.task_result)}"
            else:
                return "任务已完成，但没有结果记录"

        else:
            return "当前没有正在运行的任务"

    async def _handle_new_task(
        self, session: SessionInfo, message: str, task_context: str
    ) -> str:
        """处理新任务"""
        # 判断是否应该创建新 Session
        if self._should_create_new_session(session, task_context):
            # 创建新 Session
            new_session = await self.get_or_create_session(
                session.user_id,
                task_context,
                force_new=True
            )

            # 启动 Client（如果尚未启动）
            if new_session.client is None:
                await self.start_client_for_session(new_session)

            # 加入队列
            await new_session.pending_messages.put(message)

            return f"✅ 已创建新任务（ID: {new_session.session_key}）"

        else:
            # 复用当前 Session，加入队列
            await session.pending_messages.put(message)
            queue_size = session.pending_messages.qsize()

            return f"✅ 已加入队列（当前排队数: {queue_size}）"

    def _should_create_new_session(
        self, session: SessionInfo, new_task_context: str
    ) -> bool:
        """判断是否应该创建新 Session"""
        import hashlib

        old_hash = hashlib.md5(session.task_context.encode()).hexdigest()[:8]
        new_hash = hashlib.md5(new_task_context.encode()).hexdigest()[:8]

        return old_hash != new_hash
```

---

## 性能对比

| 方案 | 首次响应时间 | 准确率 | 成本 | 复杂度 |
|------|------------|--------|------|-------|
| **发给工作中的Claude** | 5-10分钟 ❌ | 99% | 中 | 低 |
| **纯关键词** | <1ms ✅ | 80-85% | 零 | 中 |
| **小模型** | ~100ms ✅ | 90-95% | 极低 | 中 |
| **混合方案** | 1-100ms ✅ | 85-95% | 极低 | 高 |

---

## 实际运行示例

```python
async def example():
    manager = SessionManager()
    await manager.start()

    user_id = "user123"
    link = "https://console.baidu.com/itp/xxx"

    # T0: 开始任务
    response1 = await manager.handle_message(
        user_id, f"帮我排查 {link}", link
    )
    print(f"[T0] {response1}")
    # 输出: "✅ 已创建新任务"
    # 意图识别耗时: <1ms ✅

    # T3: 追问进度（任务还在运行）
    response2 = await manager.handle_message(
        user_id, "怎么样了？", link
    )
    print(f"[T3] {response2}")
    # 输出: "🔄 任务进行中（已运行 3 分钟）\n📊 当前阶段：下载日志\n⏱️ 进度：45.0%"
    # 意图识别耗时: <1ms ✅
    # 总响应时间: <5ms ✅（不排队！）

    # T5: 模糊追问
    response3 = await manager.handle_message(
        user_id, "为什么会这样？", link
    )
    print(f"[T5] {response3}")
    # 输出: "✅ 已加入队列"
    # 意图识别: 先关键词（置信度低）→ 小模型确认（100ms）
    # 判断为 CONTEXT_FOLLOWUP，加入队列
```

---

## 核心要点总结

### ✅ 正确的架构

```
用户消息
    ↓
【应用层】意图识别（关键词/小模型）← 不排队！
    ↓
    ├─ QUERY_STATUS → 直接返回 session.progress（<5ms）
    ├─ INTERRUPT → 调用 client.interrupt()
    ├─ NEW_TASK → 创建新Session 或加入队列
    └─ CONTEXT_FOLLOWUP → 加入队列（发给Claude）
```

### ❌ 错误的架构

```
用户消息
    ↓
发给正在工作的 Claude："请判断这条消息的意图"
    ↓
❌ 进入 stdin 队列
    ↓
❌ 等待前面的任务完成（5-10分钟）
    ↓
❌ 失去意义
```

### 关键原则

1. **意图识别必须在应用层完成**
2. **不能依赖正在工作的 Claude**
3. **优先使用关键词匹配（快速、零成本）**
4. **必要时使用小模型（准确性更高）**
5. **降级策略：小模型失败时回退到关键词**

---

**文档版本**：v1.0
**最后更新**：2026-04-17
