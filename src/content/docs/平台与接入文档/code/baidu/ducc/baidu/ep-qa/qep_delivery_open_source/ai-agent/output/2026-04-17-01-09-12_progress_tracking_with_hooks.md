---
title: "Claude Agent 实时进度跟踪方案：基于 Hook 的零成本实现"
description: "文档生成时间：2026-04-17 01:09:12 主题：如何在不开启额外 LLM 的情况下，实时维护任务进度"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\ducc\\baidu\\ep-qa\\qep_delivery_open_source\\ai-agent\\output\\2026-04-17-01-09-12_progress_tracking_with_hooks.md"
---
# Claude Agent 实时进度跟踪方案：基于 Hook 的零成本实现

> 文档生成时间：2026-04-17 01:09:12
> 主题：如何在不开启额外 LLM 的情况下，实时维护任务进度

---

## 目录

1. [问题背景](#问题背景)
2. [方案对比与选型](#方案对比与选型)
3. [核心方案：Hook + 工具调用推断](#核心方案hook--工具调用推断)
4. [完整实现代码](#完整实现代码)
5. [核心难点与解决方案](#核心难点与解决方案)
6. [生产环境注意事项](#生产环境注意事项)
7. [面试回答模板](#面试回答模板)

---

## 问题背景

### 用户场景

```
T0:  用户: "帮我排查这个链接的问题"
     Agent: "收到！正在排查..."
     → Claude 开始工作（预计需要5-10分钟）

T3:  用户: "查得怎么样了？"
     期望: "🔄 正在分析日志，当前进度 60%"
     ❌ 错误: "📌 已标记，完成后通知你" (敷衍回复)
```

### 技术挑战

**问题**：如何实时维护 `SessionInfo.progress`？

```python
@dataclass
class SessionInfo:
    progress: Optional[TaskProgress] = None  # 👈 这个字段怎么更新？

@dataclass
class TaskProgress:
    stage: str              # "查询数据库" / "分析日志" 等
    progress_percent: float # 0-100
    elapsed_seconds: float
    latest_message: str
```

**错误方案**：开一个新的 LLM 去"监控"主任务
```python
# ❌ 错误方案
async def monitor_progress(session):
    while session.task_status == "running":
        # 每10秒调用一次 LLM 去分析当前进度
        summary = await another_llm.query(
            f"分析任务 {session.resume_id} 的当前进度"
        )
        session.progress = parse_summary(summary)
        await asyncio.sleep(10)
```

**问题**：
- 💰 成本高（每10秒一次 LLM 调用）
- 🐢 延迟（LLM 响应需要时间）
- 🤔 不准确（另一个 LLM 无法真正知道主任务在做什么）

---

## 方案对比与选型

| 方案 | 数据来源 | 实时性 | 准确性 | 成本 | 复杂度 | 推荐度 |
|------|---------|--------|--------|------|-------|-------|
| **Hook拦截** | PostToolUse事件 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 零 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **流式解析** | Claude文本输出 | ⭐⭐⭐⭐ | ⭐⭐⭐ | 零 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Prompt模板** | 让Claude自报进度 | ⭐⭐⭐ | ⭐⭐ | 零 | ⭐ | ⭐⭐ |
| ~~监控LLM~~ | 另一个LLM | ⭐⭐ | ⭐⭐ | 高 | ⭐⭐⭐⭐⭐ | ❌ |

---

## 核心方案：Hook + 工具调用推断

### 方案原理

Claude 执行任务时，会调用各种工具：
```
用户任务："帮我排查链接问题"
    ↓
Claude 的工作流程：
    ├─ Bash: mysql -e "select trace_id from tasks where..."
    ├─ Bash: curl https://log.baidu.com/xxx.log -o /tmp/xxx.log
    ├─ Read: /tmp/xxx.log
    ├─ Grep: "ERROR" in /tmp/xxx.log
    ├─ Read: /path/to/service/handler.py
    └─ Write: /tmp/report.md
```

**关键洞察**：
- ✅ 每次工具调用，**PostToolUse Hook 会被自动触发**
- ✅ Hook 回调能拿到：`tool_name`, `tool_input`, `tool_response`
- ✅ 从这些信息可以**推断当前阶段**

```python
Hook 捕获到：
    tool_name = "Bash"
    tool_input = {"command": "mysql -e 'select ...'"}
    ↓
推断：
    阶段 = "查询数据库"
    进度 = 25%
    ↓
更新：
    session.progress = TaskProgress(
        stage="查询数据库",
        progress_percent=25.0,
        latest_message="执行SQL查询获取trace_id"
    )
```

### 架构图

```
┌─────────────────────────────────────────────────┐
│              User Query                          │
│   "帮我排查这个链接 https://xxx"                  │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│         ClaudeSDKClient                          │
│  - session_id: "user123_abc"                     │
│  - hooks: {PostToolUse: [progress_hook]}         │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│           Claude CLI Process                     │
│                                                  │
│  Claude 生成计划 → 调用工具                       │
└─────────────────┬───────────────────────────────┘
                  ↓
        ┌─────────┴──────────┐
        ↓                    ↓
   Tool: Bash          Tool: Read
   (查数据库)          (读日志)
        ↓                    ↓
   PostToolUse         PostToolUse
   Hook 触发           Hook 触发
        ↓                    ↓
   ┌─────────────────────────────┐
   │   progress_tracking_hook     │
   │  - 分析工具调用               │
   │  - 推断阶段和进度             │
   │  - 更新 session.progress      │
   └─────────────┬───────────────┘
                 ↓
   ┌─────────────────────────────┐
   │     SessionInfo.progress     │
   │  stage: "查询数据库"          │
   │  progress_percent: 25.0      │
   │  latest_message: "..."       │
   └─────────────┬───────────────┘
                 ↓
   用户查询进度时：
   直接读取 session.progress
   立即返回（不调用LLM）
```

---

## 完整实现代码

### 1. 进度推断器（核心逻辑）

```python
from typing import Dict, Tuple, List
from dataclasses import dataclass
import re
import logging

logger = logging.getLogger(__name__)

@dataclass
class StageDefinition:
    """阶段定义"""
    name: str               # 阶段名称
    progress_percent: float # 进度百分比
    tool_patterns: List[Dict[str, str]]  # 匹配模式

class ProgressInferencer:
    """从工具调用中推断任务进度"""

    # 预定义的阶段（可根据业务自定义）
    STAGES = [
        StageDefinition(
            name="准备阶段",
            progress_percent=5.0,
            tool_patterns=[
                {"tool": "Read", "pattern": ".*config.*"},
                {"tool": "Glob", "pattern": ".*"},
            ]
        ),
        StageDefinition(
            name="查询数据库",
            progress_percent=25.0,
            tool_patterns=[
                {"tool": "Bash", "pattern": ".*(mysql|psql|select).*"},
                {"tool": "Skill", "pattern": ".*database-helper.*"},
            ]
        ),
        StageDefinition(
            name="下载日志",
            progress_percent=45.0,
            tool_patterns=[
                {"tool": "Bash", "pattern": ".*(curl|wget|scp).*\\.log.*"},
            ]
        ),
        StageDefinition(
            name="分析日志",
            progress_percent=65.0,
            tool_patterns=[
                {"tool": "Read", "pattern": ".*\\.log$"},
                {"tool": "Grep", "pattern": ".*(ERROR|WARN|Exception).*"},
            ]
        ),
        StageDefinition(
            name="分析代码",
            progress_percent=75.0,
            tool_patterns=[
                {"tool": "Read", "pattern": ".*\\.(py|java|go|js|ts)$"},
                {"tool": "Grep", "pattern": ".*class|function|def.*"},
            ]
        ),
        StageDefinition(
            name="生成报告",
            progress_percent=90.0,
            tool_patterns=[
                {"tool": "Write", "pattern": ".*(output|report|summary).*"},
            ]
        ),
    ]

    def __init__(self):
        self.tool_call_history: List[Dict] = []
        self.current_stage_index = 0
        self.max_progress = 0.0

    def infer_progress(
        self,
        tool_name: str,
        tool_input: Dict,
        tool_response: str
    ) -> Tuple[str, float, str]:
        """
        从工具调用推断进度

        Returns:
            (stage_name, progress_percent, message)
        """
        # 记录工具调用历史
        self.tool_call_history.append({
            "tool": tool_name,
            "input": tool_input,
            "response": tool_response[:200]  # 只保存前200字符
        })

        # 1. 基于工具调用次数的保底进度
        call_count_progress = min(len(self.tool_call_history) * 8, 95)

        # 2. 基于阶段匹配的推断进度
        matched_stage = self._match_stage(tool_name, tool_input)

        if matched_stage:
            stage_name = matched_stage.name
            stage_progress = matched_stage.progress_percent
        else:
            # 未匹配到预定义阶段，使用通用描述
            stage_name = self._generate_generic_stage(tool_name)
            stage_progress = call_count_progress

        # 3. 取最大值（避免进度倒退）
        final_progress = max(
            self.max_progress,
            call_count_progress,
            stage_progress
        )
        self.max_progress = final_progress

        # 4. 生成简短消息
        message = self._generate_message(tool_name, tool_input, tool_response)

        logger.info(
            f"Progress inferred: {stage_name} ({final_progress:.1f}%) - {message}"
        )

        return stage_name, final_progress, message

    def _match_stage(
        self,
        tool_name: str,
        tool_input: Dict
    ) -> StageDefinition | None:
        """匹配预定义的阶段"""

        # 遍历所有阶段（从当前阶段开始，避免倒退）
        for i in range(self.current_stage_index, len(self.STAGES)):
            stage = self.STAGES[i]

            # 检查该阶段的所有匹配模式
            for pattern_def in stage.tool_patterns:
                if pattern_def["tool"] != tool_name:
                    continue

                # 构造匹配字符串（从 tool_input 中提取关键字段）
                match_string = self._extract_match_string(tool_name, tool_input)

                # 正则匹配
                if re.search(pattern_def["pattern"], match_string, re.IGNORECASE):
                    # 匹配成功，更新当前阶段索引
                    self.current_stage_index = i
                    return stage

        return None

    def _extract_match_string(self, tool_name: str, tool_input: Dict) -> str:
        """从 tool_input 提取用于匹配的字符串"""
        if tool_name == "Bash":
            return tool_input.get("command", "")
        elif tool_name in ["Read", "Write", "Edit"]:
            return tool_input.get("file_path", "")
        elif tool_name == "Grep":
            return tool_input.get("pattern", "")
        elif tool_name == "Skill":
            return tool_input.get("skill", "")
        else:
            return str(tool_input)

    def _generate_generic_stage(self, tool_name: str) -> str:
        """生成通用的阶段描述"""
        stage_map = {
            "Bash": "执行命令",
            "Read": "读取文件",
            "Write": "写入文件",
            "Edit": "编辑文件",
            "Grep": "搜索内容",
            "Glob": "查找文件",
            "Skill": "调用技能",
        }
        return stage_map.get(tool_name, f"执行 {tool_name}")

    def _generate_message(
        self,
        tool_name: str,
        tool_input: Dict,
        tool_response: str
    ) -> str:
        """生成简短的进展消息"""
        if tool_name == "Bash":
            cmd = tool_input.get("command", "")
            # 截取前60字符
            return f"执行: {cmd[:60]}..." if len(cmd) > 60 else f"执行: {cmd}"

        elif tool_name == "Read":
            path = tool_input.get("file_path", "")
            filename = path.split("/")[-1] if "/" in path else path
            return f"读取: {filename}"

        elif tool_name == "Write":
            path = tool_input.get("file_path", "")
            filename = path.split("/")[-1] if "/" in path else path
            return f"写入: {filename}"

        elif tool_name == "Grep":
            pattern = tool_input.get("pattern", "")
            return f"搜索: {pattern}"

        elif tool_name == "Skill":
            skill = tool_input.get("skill", "")
            return f"调用技能: {skill}"

        else:
            return f"执行 {tool_name}"
```

---

### 2. 集成到 SessionInfo

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class TaskProgress:
    """任务进度信息"""
    stage: str
    progress_percent: float
    elapsed_seconds: float
    latest_message: str
    updated_at: datetime = field(default_factory=datetime.now)

@dataclass
class SessionInfo:
    """Session 元信息"""
    session_key: str
    user_id: str
    task_context: str
    resume_id: str

    # ... 其他字段 ...

    # 进度跟踪
    progress: Optional[TaskProgress] = None
    progress_inferencer: ProgressInferencer = field(
        default_factory=ProgressInferencer
    )

    created_at: datetime = field(default_factory=datetime.now)
    last_activity: datetime = field(default_factory=datetime.now)

    def update_progress_from_tool(
        self,
        tool_name: str,
        tool_input: Dict,
        tool_response: str
    ):
        """从工具调用更新进度"""
        stage, progress_percent, message = self.progress_inferencer.infer_progress(
            tool_name, tool_input, tool_response
        )

        elapsed = (datetime.now() - self.created_at).total_seconds()

        self.progress = TaskProgress(
            stage=stage,
            progress_percent=progress_percent,
            elapsed_seconds=elapsed,
            latest_message=message
        )

        self.last_activity = datetime.now()

    def get_progress_summary(self) -> str:
        """获取进度摘要（用于返回给用户）"""
        if not self.progress:
            elapsed = (datetime.now() - self.created_at).total_seconds()
            return f"任务已运行 {self._format_duration(elapsed)}"

        elapsed_str = self._format_duration(self.progress.elapsed_seconds)

        summary = f"🔄 任务进行中（已运行 {elapsed_str}）\n"
        summary += f"📊 当前阶段：{self.progress.stage}\n"
        summary += f"⏱️ 进度：{self.progress.progress_percent:.1f}%"

        if self.progress.latest_message:
            summary += f"\n💬 {self.progress.latest_message}"

        return summary

    def _format_duration(self, seconds: float) -> str:
        """格式化时长"""
        if seconds < 60:
            return f"{int(seconds)} 秒"
        elif seconds < 3600:
            return f"{seconds / 60:.1f} 分钟"
        else:
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            return f"{hours} 小时 {minutes} 分钟"
```

---

### 3. 配置 Hook

```python
from claude_agent_sdk import ClaudeAgentOptions, HookMatcher
from claude_agent_sdk.types import PostToolUseHookInput, HookContext, HookJSONOutput

def create_options_with_progress_tracking(
    resume_id: str,
    session: SessionInfo
) -> ClaudeAgentOptions:
    """创建带进度跟踪 Hook 的 Options"""

    async def progress_tracking_hook(
        hook_input: PostToolUseHookInput,
        tool_use_id: str | None,
        context: HookContext
    ) -> HookJSONOutput:
        """PostToolUse Hook：实时更新进度"""

        tool_name = hook_input["tool_name"]
        tool_input = hook_input["tool_input"]
        tool_response = hook_input.get("tool_response", "")

        try:
            # 更新进度（同步操作，很快）
            session.update_progress_from_tool(
                tool_name,
                tool_input,
                str(tool_response)
            )

            logger.debug(
                f"[{session.session_key}] Progress: "
                f"{session.progress.stage} ({session.progress.progress_percent:.1f}%)"
            )

        except Exception as e:
            logger.error(f"Failed to update progress: {e}")

        # 返回空响应（不影响 Claude 的工作流）
        return {
            "hookEventName": "PostToolUse"
        }

    return ClaudeAgentOptions(
        permission_mode='acceptEdits',
        resume=resume_id,
        setting_sources=["user", "project"],
        allowed_tools=["Read", "Write", "Edit", "Grep", "Glob", "Bash", "Skill"],
        cwd="/workspace",
        cli_path="/path/to/claude",

        # 👇 关键：配置 PostToolUse Hook
        hooks={
            "PostToolUse": [
                HookMatcher(
                    matcher=None,  # 匹配所有工具
                    hooks=[progress_tracking_hook],
                    timeout=5.0  # Hook 执行超时（避免阻塞）
                )
            ]
        }
    )
```

---

### 4. SessionManager 集成

```python
class SessionManager:
    # ... 之前的代码 ...

    async def start_client_for_session(
        self,
        session: SessionInfo,
        cwd: str = "/workspace"
    ) -> Any:
        """为 Session 启动 Claude Client（带进度跟踪）"""
        from claude_agent_sdk import ClaudeSDKClient

        async with self._lock:
            if session.client is not None:
                return session.client

            # 创建带 Hook 的 Options
            options = create_options_with_progress_tracking(
                session.resume_id,
                session
            )

            client = ClaudeSDKClient(options=options)
            await client.connect()

            session.client = client
            session.status = SessionStatus.RUNNING
            session.update_activity()

            logger.info(f"Started client with progress tracking: {session.session_key}")
            return client
```

---

## 核心难点与解决方案

### 难点 1：如何从工具调用推断阶段？

**问题**：工具调用的信息有限，如何准确判断当前阶段？

```python
# 示例：只知道调用了 Bash 工具
tool_name = "Bash"
tool_input = {"command": "curl https://log.baidu.com/xxx.log"}

# 如何推断这是"下载日志"阶段，而不是其他？
```

**解决方案：多层匹配策略**

```python
# 策略1：正则模式匹配
if re.search(r"(curl|wget).*\.log", command):
    stage = "下载日志"

# 策略2：文件路径特征
if ".log" in file_path:
    stage = "分析日志"

# 策略3：关键词组合
if "mysql" in command and "select" in command:
    stage = "查询数据库"

# 策略4：工具调用序列
# 如果之前调用过 database-helper，现在调用 curl *.log
# 大概率是"查完数据库后下载日志"
```

**权衡**：
- ✅ 简单、快速、零成本
- ⚠️ 无法100%准确
- ✅ 对于大部分场景足够了（用户关心的是"大致在做什么"）

---

### 难点 2：进度百分比如何计算？

**问题**：不同任务的时长差异很大，如何估算进度？

```python
# 任务A：查日志，5分钟完成
# 任务B：深度分析代码，30分钟完成

# 同样调用了3个工具，进度应该是多少？
```

**解决方案：混合策略**

```python
def calculate_progress():
    # 策略1：基于工具调用次数（保底）
    call_count_progress = min(call_count * 10, 95)

    # 策略2：基于阶段映射（启发式）
    stage_progress = STAGE_MAP.get(current_stage, 50.0)

    # 策略3：基于时间（可选）
    # 如果历史数据显示类似任务平均8分钟
    # 当前已运行4分钟 → 50%
    time_progress = (elapsed / estimated_total) * 100

    # 取最大值（避免倒退）
    return max(call_count_progress, stage_progress, time_progress)
```

**权衡**：
- ✅ 百分比不需要绝对准确
- ✅ 用户关心的是"还要等多久"，而不是"精确到小数点"
- ✅ 进度不倒退（用户体验好）

---

### 难点 3：Hook 执行失败会影响主任务吗？

**问题**：如果 `progress_tracking_hook` 内部抛异常，Claude 会挂掉吗？

**答案**：不会，但需要正确处理

```python
async def progress_tracking_hook(hook_input, tool_use_id, context):
    try:
        # 你的逻辑
        session.update_progress_from_tool(...)
    except Exception as e:
        # ⚠️ 必须捕获异常，不能让它传播出去
        logger.error(f"Hook failed: {e}")
        # 继续返回，不影响 Claude

    return {"hookEventName": "PostToolUse"}
```

**最佳实践**：
```python
# 1. 设置 timeout（避免 Hook 卡住）
HookMatcher(
    matcher=None,
    hooks=[progress_tracking_hook],
    timeout=5.0  # 5秒超时
)

# 2. Hook 内部所有操作都要 try-except
# 3. 避免在 Hook 中执行耗时操作（如网络请求）
```

---

### 难点 4：并发安全问题

**问题**：多个工具可能并发调用，Hook 会并发触发吗？

**答案**：不会，Claude CLI 是单线程的

```python
# Claude 的工作流程是顺序的：
Tool 1 → PostToolUse Hook 1 → Tool 2 → PostToolUse Hook 2 → ...

# 所以不需要担心并发问题
session.progress_inferencer.infer_progress(...)  # 不需要加锁
```

**但是**：如果你的应用层是多线程的（如 Flask），需要注意：

```python
# ❌ 错误：多个线程同时访问同一个 session
thread1: session.update_progress_from_tool(...)
thread2: status = session.get_progress_summary()

# ✅ 正确：加锁保护
class SessionInfo:
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    async def update_progress_from_tool(self, ...):
        async with self._lock:
            # 更新逻辑
```

---

### 难点 5：如何处理长时间没有工具调用的情况？

**问题**：Claude 可能在"思考"（generating text），此时没有工具调用

```python
# 用户查询进度，但 Claude 正在生成长文本回复
# 最后一次工具调用是 5 分钟前
# 进度停在 60%，但实际任务还在进行
```

**解决方案：基于时间的保底更新**

```python
def get_progress_summary(self) -> str:
    if not self.progress:
        return "任务已运行 ..."

    # 检查进度更新时间
    time_since_last_update = (
        datetime.now() - self.progress.updated_at
    ).total_seconds()

    if time_since_last_update > 60:
        # 超过1分钟没更新，说明可能在"思考"
        # 基于时间缓慢增加进度（但不超过95%）
        elapsed_ratio = self.progress.elapsed_seconds / (10 * 60)  # 假设10分钟完成
        time_based_progress = min(elapsed_ratio * 100, 95)

        if time_based_progress > self.progress.progress_percent:
            self.progress.progress_percent = time_based_progress
            self.progress.stage = "分析中"

    return f"🔄 任务进行中 ..."
```

---

### 难点 6：不同业务场景的阶段定义不同

**问题**：排查任务 vs 代码生成任务，阶段完全不同

```python
# 排查任务
stages = ["查数据库", "下载日志", "分析日志", "定位问题"]

# 代码生成任务
stages = ["分析需求", "设计架构", "生成代码", "编写测试"]
```

**解决方案：可配置的阶段定义**

```python
class ProgressInferencer:
    def __init__(self, task_type: str = "default"):
        if task_type == "troubleshoot":
            self.STAGES = TROUBLESHOOT_STAGES
        elif task_type == "code_generation":
            self.STAGES = CODE_GEN_STAGES
        else:
            self.STAGES = DEFAULT_STAGES

# 使用时
session.progress_inferencer = ProgressInferencer(task_type="troubleshoot")
```

或者动态检测：

```python
def detect_task_type(user_message: str) -> str:
    if "排查" in user_message or "链接" in user_message:
        return "troubleshoot"
    elif "帮我写" in user_message or "生成代码" in user_message:
        return "code_generation"
    else:
        return "default"
```

---

## 生产环境注意事项

### 1. Hook 性能优化

```python
async def progress_tracking_hook(hook_input, tool_use_id, context):
    # ✅ 使用异步日志（不阻塞）
    logger.debug(...)  # 而不是 print()

    # ✅ 避免复杂计算
    # 推断逻辑应该在 O(1) 或 O(log n) 时间内完成

    # ✅ 避免 I/O 操作
    # 不要在 Hook 里读写文件、发送网络请求

    # ✅ 设置 timeout
    # 在 HookMatcher 配置中设置合理的超时时间
```

### 2. 内存管理

```python
class ProgressInferencer:
    def __init__(self, max_history: int = 100):
        self.tool_call_history = []
        self.max_history = max_history

    def infer_progress(self, ...):
        self.tool_call_history.append(...)

        # ✅ 限制历史记录大小
        if len(self.tool_call_history) > self.max_history:
            self.tool_call_history = self.tool_call_history[-self.max_history:]
```

### 3. 日志级别

```python
# 生产环境建议：
logger.setLevel(logging.INFO)  # 不要用 DEBUG

# Hook 内部：
logger.debug(...)  # 详细信息（开发时用）
logger.info(...)   # 关键进度更新
logger.warning(...) # Hook 执行慢
logger.error(...)  # Hook 失败
```

### 4. 监控指标

```python
class ProgressInferencer:
    def __init__(self):
        self.metrics = {
            "total_tools": 0,
            "matched_stages": 0,
            "hook_errors": 0,
            "avg_hook_duration_ms": 0.0
        }

    def infer_progress(self, ...):
        start = time.time()

        try:
            # ... 推断逻辑 ...
            self.metrics["total_tools"] += 1
            if matched_stage:
                self.metrics["matched_stages"] += 1
        except Exception as e:
            self.metrics["hook_errors"] += 1
            raise
        finally:
            duration_ms = (time.time() - start) * 1000
            self.metrics["avg_hook_duration_ms"] = (
                self.metrics["avg_hook_duration_ms"] * 0.9 + duration_ms * 0.1
            )
```

---

## 面试回答模板

### 问题："怎么实时维护 SessionInfo.progress？需要开另一个 LLM 监控吗？"

### 完整回答（5分钟版）

**第一步：否定错误方案**

> "不需要开另一个 LLM！那样成本太高，而且不准确。"

**第二步：说明核心思路**

> "我的方案利用了 Claude SDK 的 **PostToolUse Hook 机制**。
>
> Claude 执行任务时会调用各种工具——比如 Bash 执行 SQL 查询、Read 读取日志文件、Grep 搜索错误信息。每次工具调用完成后，**PostToolUse Hook 会自动触发**，我在这个 Hook 里分析工具的名称、参数、输出，从中推断当前所处的阶段和进度。"

**第三步：举具体例子**

> "举个例子：
> ```
> Hook 捕获到：
>   tool_name = "Bash"
>   tool_input = {"command": "mysql -e 'select trace_id from...'"}
>
> 我的逻辑：
>   - 检测到 "mysql" + "select" 关键词
>   - 推断：当前阶段 = "查询数据库"
>   - 映射：进度 = 25%
>   - 更新：session.progress = TaskProgress(stage="查询数据库", progress=25%)
>
> 下一次 Hook：
>   tool_name = "Bash"
>   tool_input = {"command": "curl https://log.baidu.com/xxx.log"}
>
> 推断：
>   - 检测到 "curl" + ".log"
>   - 阶段 = "下载日志"，进度 = 45%
> ```
>
> 用户这时候查询进度，我直接从 `session.progress` 读取，立即返回'正在下载日志，进度45%'。"

**第四步：说明优势**

> "这个方案的优势：
> 1. **零成本**：Hook 是被动触发的，不需要额外调用 LLM
> 2. **实时性**：工具调用时立即更新，延迟几乎为零
> 3. **准确性**：虽然是启发式推断，但对于大部分场景足够准确
> 4. **不影响主任务**：Hook 执行很快（毫秒级），且有异常保护"

**第五步：谈难点和权衡**

> "当然也有一些难点：
>
> **难点1**：如何从工具调用推断阶段？
> - 解决：预定义阶段 + 正则匹配 + 工具序列分析
> - 权衡：不需要100%准确，用户关心的是'大致在做什么'
>
> **难点2**：进度百分比如何计算？
> - 解决：混合策略（工具调用次数 + 阶段映射 + 时间估算）
> - 保证进度不倒退（用户体验好）
>
> **难点3**：长时间没有工具调用怎么办？
> - 解决：基于时间的保底更新，避免进度"卡住"
>
> **难点4**：不同任务的阶段定义不同
> - 解决：可配置的阶段定义，或动态检测任务类型"

**第六步：对比其他方案**

> "也考虑过其他方案：
> - **Prompt 方案**：让 Claude 自己返回模板回复（'正在处理中～'）
>   - 问题：不是真实进度，用户会察觉是在敷衍
> - **流式解析**：解析 Claude 的文本输出
>   - 问题：准确性更差，Claude 的输出格式不稳定
> - **单独监控进程**：另一个 LLM 定期查询
>   - 问题：成本高、延迟大、不准确
>
> 综合考虑，Hook 方案是最优解。"

**第七步：总结**

> "所以总结来说，我的方案是：
> 1. **数据来源**：PostToolUse Hook（零成本）
> 2. **推断逻辑**：工具名称 + 参数 + 调用序列 → 阶段和进度
> 3. **存储**：SessionInfo.progress（内存）
> 4. **查询**：用户追问时直接返回，不调用 LLM
>
> 这是一个工程化、可落地、零额外成本的方案。"

---

## 总结

### 核心方案

```
PostToolUse Hook（被动触发，零成本）
    ↓
分析工具调用（tool_name + tool_input + tool_response）
    ↓
启发式推断（正则匹配 + 阶段映射 + 序列分析）
    ↓
更新 SessionInfo.progress（内存操作，毫秒级）
    ↓
用户查询时直接返回（不调用 LLM）
```

### 关键优势

| 维度 | 优势 |
|------|------|
| **成本** | 零额外成本（Hook 是内置机制） |
| **实时性** | 毫秒级更新（工具调用时触发） |
| **准确性** | 70-80%（足够应对生产场景） |
| **复杂度** | 中等（需要阶段定义和匹配逻辑） |
| **可维护性** | 高（阶段定义可配置） |

### 核心难点

1. 从工具调用推断阶段（正则匹配 + 启发式规则）
2. 进度百分比计算（混合策略 + 不倒退）
3. Hook 异常处理（不影响主任务）
4. 长时间无工具调用（基于时间的保底更新）
5. 不同业务场景（可配置的阶段定义）

---

**文档版本**：v1.0
**适用SDK版本**：claude-agent-sdk >= 0.0.20
**维护者**：Ducc AI Team
**最后更新**：2026-04-17
