---
title: "交互指南"
description: "本文档描述 auto-commit skill 中 UI 交互和数据提交的具体操作方式。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\auto-commit-comate\\references\\interaction_instruction.md"
---
# 交互指南

本文档描述 auto-commit skill 中 UI 交互和数据提交的具体操作方式。

---

## 全局规则

**⚠️ 全局静默要求：整个流程中 Agent 仅通过 `__interactive:` UI 组件与用户交互。除步骤 9 的最终结果文字外，Agent 禁止向用户输出任何文字内容，包括但不限于：**
- **过渡性话语**：如 "Now I have the data"、"Let me perform matching"、"让我分析一下"
- **内部分析过程**：如 "Card 26: xxx - Score: 95"、"Matching analysis:"、匹配评分细节
- **状态说明**：如 "has_good_match: true"、"Cards sorted by score"
- **JSON 数据或代码片段**

**Agent 应在内部完成所有思考后，直接调用对应的 `run_command`，不在工具调用之间输出任何文字。**

**⚠️ 重要：所有 `run_command` 调用（`__interactive:` 除外）必须加 `__silent:` 前缀。唯一例外是步骤 9 的 git commit 命令，需要展示提交结果给用户。**

**⚠️ 禁止额外命令：Agent 不得在流程步骤之外自行执行任何 shell 命令（如 `git status`、`ls` 等）。iCafe 数据由步骤 1 的 Python 脚本获取，git diff 由步骤 2 中 Agent 按规定命令获取。**

**⚠️ 工作目录规则：Skill 执行时的工作目录可能不是用户项目目录。当命令需要在用户项目目录下执行时（如 git 操作、Python 脚本），必须在命令中加 `cd <用户项目目录> &&` 切换目录。但 `__silent:` 或 `__interactive:` 前缀必须始终在命令最开头。**

**⚠️ 多 Workspace 规则：用户可能打开了多个代码库（multi-root workspace）。环境上下文中的 `Workspace Path` 会列出所有 workspace 路径。在步骤 2 和步骤 8 中，Agent 必须对每个 workspace 分别执行 git 命令，不可只处理第一个 workspace 后忽略其余的。**

正确格式：
```
__silent: cd /path/to/project && git add .
__interactive:icafe-cards {...}
```

错误格式（禁止）：
```
cd /path/to/project && __silent: git add .
cd /path/to/project && __interactive:icafe-cards {...}
```

---

## 步骤 1：获取 iCafe 数据

使用 SKILL.md 步骤 1 中定义的命令模板执行。

---

## 步骤 2：获取 git diff

使用 SKILL.md 步骤 2 中定义的命令模板执行。

---

## 步骤 4：展示卡片选择

### 4a. 构造并通过脚本验证 payload

**⚠️ 不需要手动转换 snake_case/camelCase，不需要拼 JSON，不需要传文件路径。** 脚本自动读取步骤 1 留下的缓存文件，Agent 只需传入简单的 CLI 参数。

```bash
__silent: python3 <skill_directory>/scripts/build_icafe_cards_payload.py --view-mode list --default-title "优化 xxx 相关功能"
```

参数说明：
- `--view-mode`（必填）：`list` 或 `create`，由步骤 3 确定
- `--default-title`（必填）：Agent 根据 diff 语义生成的推荐标题
- `--cards`（可选）：排序后的 cards JSON 数组，不传则使用 result 中的原始顺序
- `--result-file`（可选）：默认读取 `/tmp/__comate_icafe_result.json`（步骤 1 自动写入）

**脚本自动从缓存文件读取所有数据并完成 snake_case → camelCase 转换，Agent 不需要手动处理任何字段名。**

### 4b. 解析脚本输出并调用 UI

**如果脚本返回 `{"valid": true, "payload": {...}}`：**

**⚠️ 必须提取 `payload` 字段的值（内层 JSON），使用 `run_command` 工具调用 UI，禁止将 payload 作为文本输出给用户。**

例如脚本返回：
```json
{"valid": true, "payload": {"cards": [...], "spacePrefix": "dkx", ...}}
```
则调用：
```
run_command(command="__interactive:icafe-cards {\"cards\": [...], \"spacePrefix\": \"dkx\", ...}")
```
**禁止**（作为文本输出或传入错误数据）：
```
__interactive:icafe-cards {"valid": true, "payload": {"cards": [...], ...}}
```

**如果脚本返回 `{"valid": false, "errors": [...]}`：**

根据 `errors` 中的具体描述修正数据，重新调用脚本（最多重试 1 次）。如果重试后仍返回 `valid: false`，或脚本返回 `{"error": "..."}`，则**降级为文本交互**（见下方降级格式）。

---

## 步骤 5：处理用户操作

UI 组件返回 JSON，可能的 action 值：

| action | 含义 | 处理方式 |
|--------|------|----------|
| `select` | 选择已有卡片 | 保存 `card` 中的卡片信息，继续步骤 7 |
| `recognize` | 链接或卡片 ID 识别 | 调用 `recognize_card_cli.py` 获取卡片详情，继续步骤 7 |
| `create` | 新建卡片 | 调用 `create_card_cli.py` 创建卡片，继续步骤 7 |
| `skip` | 跳过 | 输出"已跳过卡片绑定和代码提交。"，**结束 skill** |
| `do_not_show_again` | 不再提示 | 输出"已关闭推荐卡片提示。"，**结束 skill** |

**recognize 处理：**
```
__silent: cd <用户项目目录> && python3 <skill_directory>/scripts/recognize_card_cli.py --link "<用户返回的link>"
```

**create 处理：**

使用 SKILL.md 步骤 5 中定义的「创建卡片命令模板」，**加 `__silent:` 前缀**执行。

---

## 步骤 8：展示提交确认

### 8a. 构造并通过脚本验证 payload

**推荐：使用缓存模式**（脚本自动从缓存读取 diff、执行 git branch 获取分支信息）：

```bash
__silent: python3 <skill_directory>/scripts/build_git_commit_payload.py --cache --commit-message "<commitMessage>" --bound-card '<boundCard JSON 或 null>'
```

参数说明：
- `--commit-message`（必填）：iCode 仓库格式 `"<spacePrefix>-<sequence> <描述>"`；非 iCode 仓库不带卡片 ID
- `--bound-card`（必填）：步骤 5 选定的卡片对象 JSON，无卡片时传字符串 `'null'`

**⚠️ 所有命令必须带 `__silent:` 前缀（`__interactive:` 除外）。**

### 8b. 解析脚本输出并调用 UI

**如果脚本返回 `{"valid": true, "payload": {...}}`：**

**⚠️ 必须提取 `payload` 字段的值（内层 JSON），使用 `run_command` 工具调用 UI，禁止将 payload 作为文本输出给用户。**

例如脚本返回：
```json
{"valid": true, "payload": {"commitMessage": "dkx-200 fix", "boundCard": {...}, "workspaces": [...]}}
```
则调用：
```
run_command(command="__interactive:git-commit {\"commitMessage\": \"dkx-200 fix\", \"boundCard\": {...}, \"workspaces\": [...]}")
```
**禁止**（作为文本输出或传入错误数据）：
```
__interactive:git-commit {"valid": true, "payload": {"commitMessage": "dkx-200 fix", ...}}
```

**如果脚本返回 `{"valid": false, "errors": [...]}`：**

根据 `errors` 中的具体描述修正数据，重新调用脚本（最多重试 1 次）。如果重试后仍返回 `valid: false`，或脚本返回 `{"error": "..."}`，则**降级为文本交互**（见下方降级格式）。

用户操作后，tool output 返回 JSON：
- 确认提交：`{"action": "submit", "repos": [{"workspace": "...", "commitMessage": "...", "branch": "..."}]}`
- 取消提交：`{"action": "cancel"}`

---

## 步骤 9：执行提交

从 tool output 解析用户操作：

**如果是 action === "submit"：**

UI 返回的结果格式：
```json
{"action": "submit", "repos": [{"workspace": "/path/to/repo", "commitMessage": "dkx-200 修复...", "branch": "feature/xxx"}]}
```

Agent 收到后，对 `repos` 数组中的每个仓库自主决定执行方式：
- `cd` 到对应 workspace 目录
- 执行 `git add .`、`git commit -m "<commitMessage>"`（git commit 命令不使用 `__silent:`，展示提交结果给用户）
- 如果用户选择了特定分支且不是当前分支，先 `git checkout` 切换
- **推送方式根据仓库类型区分：**
  - 统一使用 `git push origin HEAD:refs/for/<branch>` 推送到 Gerrit 代码评审
- 多仓库时逐个执行，每个仓库独立处理

**如果是 action === "cancel"：**
- 输出"已取消提交"

---

## 降级文本交互格式

当 builder 脚本验证失败且重试仍失败，或脚本返回系统错误时，Agent 降级为纯文本交互。

### 步骤 4 降级（卡片选择）

```
请选择要绑定的 iCafe 卡片（回复编号）：

1. dkx-200 修复登录问题 [Bug] [开发中]
2. dkx-198 新增导出功能 [Story] [待开发]
3. dkx-195 优化查询性能 [Task] [进行中]

回复 N 选择对应卡片，或回复卡片链接/ID，或回复 "新建" 创建卡片，回复 "跳过" 跳过。
```

用户回复后，Agent 按步骤 5 的规则处理对应操作。

### 步骤 8 降级（提交确认）

```
📝 提交确认

Commit Message: dkx-200 修复登录问题
绑定卡片: dkx-200 修复登录问题 (Bug)

变更文件:
- frontend-app: 2 files, +100, -78
  - src/App.tsx (+76, -66)
  - src/utils.ts (+24, -12)

回复 "确认" 提交代码，回复 "取消" 放弃提交。
```

用户回复后，Agent 按步骤 9 的规则处理对应操作。
