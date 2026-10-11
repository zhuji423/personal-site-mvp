---
title: "Hook 生命周期详解"
description: "核心问题: Claude Code 在执行任务的过程中，什么时候允许你插入自定义逻辑？这些逻辑如何参与质量检查、自动化流程和 RL 训练中的 reward 采集？"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\03_week3_inference_claude_code\\claude_code\\hooks_lifecycle.md"
---
# Hook 生命周期详解

> **核心问题**: Claude Code 在执行任务的过程中，什么时候允许你插入自定义逻辑？这些逻辑如何参与质量检查、自动化流程和 RL 训练中的 reward 采集？

---

## 1. Hook 定义

> **Hook（钩子）**: 在系统生命周期的某个确定性节点自动触发的可扩展回调函数。它允许用户在不修改核心代码的前提下，在特定时机注入自定义逻辑。

Hook 的本质是"控制反转"（Inversion of Control）——系统定义好触发点，用户填写回调逻辑。这和 Git Hook、Web Framework 的 Middleware、Kubernetes 的 Admission Controller 是同一类设计模式。

在 Claude Code 中，Hook 的核心价值包括：

- **质量检查**：在工具执行前后插入验证逻辑
- **自动化**：工具执行后自动格式化代码、运行 lint
- **指标采集**：收集每次工具执行的耗时、结果、错误率
- **Reward 收集**：在 RL 训练中采集 reward signal
- **安全审计**：记录所有对文件系统和 Shell 的操作

---

## 2. 四种 Hook 类型详解

### 2.1 PreToolUse — 工具执行前钩子

> **PreToolUse**: 在工具被实际执行之前触发的钩子。它可以检查、修改甚至拦截工具调用。

**触发时机**：模型输出了 `tool_use` 块，参数校验通过，权限检查通过，即将调用工具函数之前。

**接收参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `tool_name` | string | 即将执行的工具名称（如 `Bash`、`Edit`） |
| `tool_input` | object | 工具调用的参数（如文件路径、命令内容） |
| `session_id` | string | 当前会话标识 |
| `context` | object | 当前上下文摘要（非完整 context） |

**典型使用场景**：

1. **参数校验与拦截**：阻止对敏感文件的修改操作

```json
{
  "hook_type": "PreToolUse",
  "matcher": { "tool_name": "Edit" },
  "script": "check_protected_files.sh",
  "description": "检查是否尝试编辑受保护的文件"
}
```

2. **命令安全检查**：阻止危险的 Shell 命令

```json
{
  "hook_type": "PreToolUse",
  "matcher": { "tool_name": "Bash" },
  "script": "validate_command.sh",
  "description": "验证 Bash 命令是否安全"
}
```

3. **参数修改**：在执行前规范化工具参数（如自动补充路径前缀）

**返回值语义**：

| 返回值 | 含义 |
|--------|------|
| 无输出 / exit 0 | 允许工具继续执行 |
| 输出修改后的参数 JSON | 用修改后的参数替换原始参数 |
| 输出错误信息 / exit 非 0 | 拦截工具调用，错误信息反馈给模型 |

### 2.2 PostToolUse — 工具执行后钩子

> **PostToolUse**: 在工具执行完成后触发的钩子。它可以检查执行结果、执行附加操作、采集指标。

**触发时机**：工具函数执行完毕，结果已经生成，即将将结果写回 Context Window 之前。

**接收参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `tool_name` | string | 已执行的工具名称 |
| `tool_input` | object | 工具调用的原始参数 |
| `tool_output` | string | 工具执行的结果 |
| `duration_ms` | number | 执行耗时（毫秒） |
| `exit_code` | number | 退出码（Bash 工具） |
| `error` | string | 错误信息（如果执行失败） |

**典型使用场景**：

1. **自动格式化**：代码修改后自动运行 formatter

```json
{
  "hook_type": "PostToolUse",
  "matcher": { "tool_name": ["Write", "Edit"] },
  "script": "auto_format.sh",
  "description": "文件修改后自动运行 prettier 和 eslint --fix"
}
```

2. **结果记录与指标采集**：记录每次工具调用的元数据

```json
{
  "hook_type": "PostToolUse",
  "matcher": { "tool_name": "*" },
  "script": "collect_metrics.py",
  "description": "收集工具执行指标写入日志"
}
```

3. **Reward Signal 采集**：在 RL 训练中收集每步的反馈

```json
{
  "hook_type": "PostToolUse",
  "matcher": { "tool_name": ["Bash"] },
  "script": "collect_reward.py",
  "description": "分析命令执行结果，计算局部 reward"
}
```

4. **错误检测**：工具执行失败时的自动诊断

```json
{
  "hook_type": "PostToolUse",
  "matcher": { "tool_name": "Bash" },
  "condition": "exit_code != 0",
  "script": "diagnose_error.sh",
  "description": "命令失败时自动分析错误原因"
}
```

### 2.3 Notification — 通知钩子

> **Notification**: 在特定事件发生时触发异步通知的钩子。它不会阻塞主流程，仅用于发送消息。

**触发时机**：任务完成、长时间运行、错误发生等需要通知用户的时刻。

**接收参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `event_type` | string | 事件类型（如 `task_complete`、`error`） |
| `message` | string | 通知消息内容 |
| `session_id` | string | 当前会话标识 |
| `timestamp` | string | 事件发生时间 |

**典型使用场景**：

1. **任务完成通知**：长时间任务结束后通知用户

```json
{
  "hook_type": "Notification",
  "event": "task_complete",
  "script": "notify_slack.sh",
  "description": "任务完成后发送 Slack 通知"
}
```

2. **错误告警**：严重错误发生时立即通知

```json
{
  "hook_type": "Notification",
  "event": "error",
  "script": "notify_pagerduty.sh",
  "description": "严重错误时触发 PagerDuty 告警"
}
```

**关键特性**：Notification Hook 是异步执行的，不会阻塞主 Agent 的消息循环。即使通知发送失败，也不影响 Agent 继续工作。

### 2.4 Stop — 停止钩子

> **Stop**: 在 Agent 任务停止时触发的钩子。用于最终清理、汇总报告和持久化结果。

**触发时机**：Agent 的 Message Loop 正常结束（模型输出最终回复）或异常终止（用户中断、超时）时。

**接收参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| `stop_reason` | string | 停止原因（`end_turn` / `user_cancel` / `timeout`） |
| `total_tool_calls` | number | 本次任务执行的工具调用总数 |
| `total_duration_ms` | number | 本次任务的总耗时 |
| `files_modified` | list[string] | 被修改的文件列表 |
| `final_summary` | string | Agent 的最终输出摘要 |

**典型使用场景**：

1. **最终清理**：删除临时文件、关闭连接

```json
{
  "hook_type": "Stop",
  "script": "cleanup.sh",
  "description": "任务结束后清理临时文件和缓存"
}
```

2. **汇总报告**：生成任务执行的完整日志

```json
{
  "hook_type": "Stop",
  "script": "generate_report.py",
  "description": "生成任务执行报告，包含所有工具调用和修改"
}
```

3. **最终 Reward 计算**：在 RL 训练中计算整条轨迹的总 reward

```json
{
  "hook_type": "Stop",
  "script": "compute_final_reward.py",
  "description": "基于完整轨迹计算最终 reward，写入训练数据"
}
```

---

## 3. 生命周期时间线图

一次完整的 Claude Code 任务执行过程中，所有 Hook 的触发时间线如下：

```
时间 ─────────────────────────────────────────────────────────────────▶

用户输入消息
    │
    ▼
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│  第 1 轮 Message Loop:                                             │
│                                                                    │
│    模型返回 tool_use: Read(config.json)                             │
│         │                                                          │
│         ├─ [PreToolUse]  ← 参数校验：路径是否合法？                   │
│         │         │                                                  │
│         │    ┌────┴────┐                                             │
│         │    │ 执行 Read │                                           │
│         │    └────┬────┘                                             │
│         │         │                                                  │
│         ├─ [PostToolUse] ← 记录读取结果，采集 metrics               │
│         │                                                          │
│    模型返回 tool_use: Edit(config.json, ...)                        │
│         │                                                          │
│         ├─ [PreToolUse]  ← 检查是否受保护文件                        │
│         │         │                                                  │
│         │    ┌────┴────┐                                             │
│         │    │ 执行 Edit │                                           │
│         │    └────┬────┘                                             │
│         │         │                                                  │
│         ├─ [PostToolUse] ← 自动运行 prettier，记录修改               │
│         │                                                          │
│    模型返回 tool_use: Bash(npm test)                                │
│         │                                                          │
│         ├─ [PreToolUse]  ← 命令安全检查                              │
│         │         │                                                  │
│         │    ┌────┴────┐                                             │
│         │    │ 执行 Bash │                                           │
│         │    └────┬────┘                                             │
│         │         │                                                  │
│         ├─ [PostToolUse] ← 收集测试结果，计算局部 reward             │
│         │                                                          │
│    模型返回纯文本回复 → 任务结束                                      │
│                                                                    │
│  [Notification] ← 可选：通知用户任务已完成                            │
│                                                                    │
│  [Stop] ← 最终清理、汇总报告、计算最终 reward                        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 4. Hook 在基础设施中的价值

### 4.1 质量检查（Quality Gate）

Hook 可以作为代码质量的自动化守门人：

```
┌──────────────────────────────────────────────────┐
│            质量检查 Hook 链                        │
│                                                  │
│  PreToolUse:                                     │
│    ├─ Edit → 检查是否修改了测试文件但没有对应实现    │
│    ├─ Bash → 阻止 rm -rf 等危险命令               │
│    └─ Write → 检查文件路径是否在允许范围内          │
│                                                  │
│  PostToolUse:                                    │
│    ├─ Edit/Write → 自动运行 prettier              │
│    ├─ Edit/Write → 自动运行 eslint                │
│    ├─ Bash(test) → 解析测试结果，检查覆盖率        │
│    └─ Bash(build) → 检查构建是否成功              │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 4.2 Reward Signal 收集

> **Reward Signal（奖励信号）**: 在 RL 训练中，用于评估模型行为质量的反馈信号。好的行为获得正奖励，坏的行为获得负奖励。

Hook 是采集 Reward Signal 的天然观察点：

| Hook 类型 | 可采集的 Reward 信息 | 具体示例 |
|-----------|---------------------|----------|
| PreToolUse | 意图评估 | 模型选择编辑正确的文件？参数是否合理？ |
| PostToolUse | 执行结果 | 测试通过？Lint 无错误？修改后代码能编译？ |
| Stop | 任务完成度 | 任务是否完成？修改是否正确？是否有副作用？ |

采集流程：

```
┌──────────────────────────────────────────────────────────────┐
│              Reward 采集流程                                   │
│                                                              │
│  PostToolUse 触发                                             │
│       │                                                      │
│       ▼                                                      │
│  collect_reward.py 执行                                       │
│       │                                                      │
│       ├─ 解析工具执行结果（测试输出、lint 结果、编译结果）        │
│       │                                                      │
│       ├─ 计算局部 reward:                                      │
│       │   r_step = f(测试通过数, lint错误数, 执行耗时)           │
│       │                                                      │
│       ├─ 写入 rollout 日志:                                    │
│       │   {state, action, reward, next_state}                 │
│       │                                                      │
│       └─ 累积到 episode buffer                                │
│                                                              │
│  Stop 触发                                                    │
│       │                                                      │
│       ▼                                                      │
│  compute_final_reward.py 执行                                 │
│       │                                                      │
│       ├─ 汇总所有局部 reward                                   │
│       ├─ 计算最终任务完成奖励                                   │
│       └─ 输出完整 episode 数据用于训练                          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 4.3 CI/CD 集成

Hook 还可以与 CI/CD 流水线深度集成：

- **Pre-commit 检查**：在 Stop Hook 中运行完整测试套件，验证所有修改
- **自动提交**：当所有检查通过后，自动生成 commit
- **PR 创建**：在 Stop Hook 中调用 `gh pr create`，自动创建 Pull Request
- **部署触发**：任务完成后触发部署流水线

---

## 5. settings.json 配置示例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": {
          "tool_name": "Edit"
        },
        "hooks": [
          {
            "type": "command",
            "command": "python3 /path/to/check_protected_files.py"
          }
        ]
      },
      {
        "matcher": {
          "tool_name": "Bash"
        },
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/validate_command.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": {
          "tool_name": ["Write", "Edit"]
        },
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write $TOOL_INPUT_FILE_PATH"
          },
          {
            "type": "command",
            "command": "npx eslint --fix $TOOL_INPUT_FILE_PATH"
          }
        ]
      },
      {
        "matcher": {
          "tool_name": "*"
        },
        "hooks": [
          {
            "type": "command",
            "command": "python3 /path/to/collect_metrics.py"
          }
        ]
      }
    ],
    "Notification": [
      {
        "event": "task_complete",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/notify.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 /path/to/generate_report.py"
          },
          {
            "type": "command",
            "command": "/path/to/cleanup.sh"
          }
        ]
      }
    ]
  }
}
```

配置结构说明：

- 每种 Hook 类型下可以注册多个 hook 回调
- `matcher` 定义了 hook 的触发条件（按工具名匹配）
- `*` 通配符表示匹配所有工具
- 多个 hook 按注册顺序依次执行

---

## 6. 错误处理

Hook 的错误处理是工程上最容易被忽视、也最容易出问题的部分。

### 6.1 错误处理策略

| Hook 类型 | Hook 脚本失败时的行为 | 设计理由 |
|-----------|---------------------|----------|
| **PreToolUse** | **拦截工具调用**，错误信息反馈给模型 | 安全优先，宁可误拦不可漏放 |
| **PostToolUse** | **记录错误但不阻塞**，工具结果正常写回 context | 避免后置检查拖慢主路径 |
| **Notification** | **静默失败**，不影响主流程 | 通知是辅助功能，不应干扰核心 |
| **Stop** | **记录错误但继续**，不影响任务终止 | 清理和报告是附加动作 |

### 6.2 错误处理的工程原则

1. **Fail-safe**：Hook 失败时的默认行为应该是最安全的选项。PreToolUse 失败 → 阻止执行（安全优先）；PostToolUse 失败 → 继续执行（不阻塞主路径）。

2. **隔离**：Hook 脚本运行在独立进程中，即使崩溃也不会影响主 Agent 的 Message Loop。

3. **超时保护**：每个 Hook 都应该有超时机制，防止慢 Hook 拖住整个系统。建议超时时间：
   - PreToolUse: 5 秒（需要快速响应）
   - PostToolUse: 30 秒（可能包含格式化等重操作）
   - Stop: 60 秒（生成报告可能较慢）

4. **结构化错误输出**：Hook 失败时应该输出结构化的错误信息，便于排查。推荐格式：

```json
{
  "hook_type": "PreToolUse",
  "tool_name": "Bash",
  "error": "command_validation_failed",
  "message": "命令 'rm -rf /' 被安全规则拦截",
  "rule_id": "R001",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### 6.3 Hook 调试最佳实践

- 所有 Hook 的输入和输出都应该写入日志文件，便于回溯
- Hook 脚本的开发应该遵循"快速失败"原则，第一时间验证输入参数
- 使用环境变量传递配置（如日志路径、超时时间），而不是硬编码
- 在开发阶段可以单独测试 Hook 脚本，不依赖 Claude Code 的完整运行

---

## 7. Hook 与其他系统的对比

| 系统 | Hook 触发点 | 阻塞行为 | 典型用途 |
|------|------------|----------|----------|
| **Claude Code** | Agent 生命周期（工具调用前后、任务停止） | PreToolUse 可阻塞 | 质量检查、reward 采集 |
| **Git Hook** | 版本控制事件（pre-commit、pre-push） | 可阻塞 commit/push | 代码规范检查 |
| **Kubernetes Admission Controller** | API 请求（创建/更新资源） | 可阻塞请求 | 安全策略、资源配额 |
| **Express.js Middleware** | HTTP 请求生命周期 | 可阻塞请求 | 认证、日志、限流 |
| **Webpack Plugin** | 构建流程的各个阶段 | 可中断构建 | 代码转换、优化、注入 |

Claude Code 的 Hook 系统借鉴了这些成熟系统的设计思路，但针对 Agent 场景做了专门优化：触发点围绕工具调用而非请求/事件，支持结构化 JSON 通信而非纯文本，并且与 Context Window 紧密集成。

---

## 面试高频问题

### Q1: Claude Code 的 Hook 系统和 Git Hook 有什么本质区别？

**A**: 触发维度不同。Git Hook 面向版本控制事件（commit、push、checkout），Claude Code 的 Hook 面向 Agent 执行生命周期，特别是工具调用的前后。更关键的区别在于：Git Hook 通常只做"检查 → 通过或拒绝"，而 Claude Code 的 Hook 不仅能拦截（PreToolUse），还能修改参数（PreToolUse 返回修改后的 JSON）、采集结果（PostToolUse）和异步通知（Notification）。此外，Claude Code 的 Hook 天然支持 RL 训练的 reward 采集，这是 Git Hook 完全不具备的能力。

### Q2: 如果 PostToolUse 的 Hook 脚本执行很慢（比如 30 秒），会对系统产生什么影响？

**A**: 会直接影响用户体验，因为每次工具执行后都要等 Hook 完成。缓解策略有三个层面：（1）异步化——将非关键的 PostToolUse Hook 改为异步执行，只通过 Notification 通知结果；（2）超时保护——给每个 Hook 设置最大执行时间，超时后自动跳过；（3）选择性触发——只在关键工具调用（如 Write、Edit）上触发重 Hook，跳过低风险工具（如 Read、Grep）的重量级检查。核心原则是：重计算尽量后置或异步，高风险检查前置但快速。

### Q3: 如何用 Hook 系统来采集 RL 训练的 reward signal？具体怎么做？

**A**: 最常用的方案是在 PostToolUse 和 Stop 两个钩子上采集。PostToolUse Hook 在每次工具执行后触发，可以分析执行结果（如测试是否通过、编译是否成功、lint 是否有错误），计算局部 reward r_step，并将 (state, action, reward, next_state) 四元组写入 episode buffer。Stop Hook 在任务结束时触发，汇总所有局部 reward 计算最终 episode reward，并输出完整的轨迹数据用于训练。这样整个 Hook 系统就充当了一个轻量级的 Reward Collector。

### Q4: 多个 Hook 可以共享数据吗？如果可以，怎么做比较合理？

**A**: 可以共享，但必须通过显式机制而非隐式状态。推荐两种方式：（1）通过文件系统——前一个 Hook 将结果写入临时文件（路径通过环境变量传递），后一个 Hook 读取；（2）通过环境变量——主 Agent 在触发 Hook 时注入共享数据作为环境变量。不推荐的做法包括：共享全局变量（进程隔离后无法共享）、隐式约定文件路径（容易冲突和难以维护）。核心原则是：共享数据要显式声明、显式传递、显式清理。
