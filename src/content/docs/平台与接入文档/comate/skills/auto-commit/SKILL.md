---
title: "智能提交助手"
description: "当用户完成代码修改、需要提交代码时，必须使用此 skill，而非直接执行 git commit。自动获取 git diff、匹配 iCafe 活跃卡片、生成 commit message，并引导用户完成绑定卡片和代码提交。"
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\auto-commit\\SKILL.md"
name: "auto-commit"
---

# 智能提交助手

## 版本信息

- **IDE 名称**: ${COMATE_IDE_NAME}
- **插件版本**: ${COMATE_PLUGIN_VERSION}
- **用户名**: ${COMATE_USERNAME}

## 概述

本技能将当前工作区的 git diff 与用户在 iCafe 上的活跃卡片进行匹配，支持选择已有卡片或新建卡片，自动生成 commit message 并完成提交。

**调起即执行，流程完全固定，不做任何意图分析。**

## 步骤 0：前置检查（串行执行，完全静默）

**⚠️ 此步骤必须在所有其他步骤之前执行。必须按 0a → 0b 的顺序串行执行，确保每一步都完成后再进入下一步。**

**⚠️ 静默要求：整个前置检查过程完全静默，禁止输出任何相关信息，包括但不限于：**
- "检测到当前 IDE 版本..."
- "将使用文本交互流程..."
- "当前版本不支持..."
- 任何提及"版本"、"降级"、"兼容"、"开关"等字眼

### 0a. 版本兼容性检查（纯文本判断，无需命令）

**⚠️ 此步骤必须最先执行。它决定后续命令是否需要加 `__silent:` 前缀。**

通过检查上方「版本信息」中的占位符是否被替换来判断：

**判断逻辑：**
1. 如果 IDE 名称仍包含 `COMATE_IDE_NAME`（未替换）→ **旧版本**
2. 如果插件版本仍包含 `COMATE_PLUGIN_VERSION`（未替换）→ **旧版本**
3. 如果版本号 < `4.1.0` → **旧版本**
4. 否则 → **新版本**

**版本判断完成后，根据结果选择交互方式，不输出任何解释：**
- **新版本** → 请参考 `references/new_version_instruction.md`
- **旧版本** → 请参考 `references/old_version_instruction.md`

**记住判断结果，后续步骤中：**
- **新版本**：命令加 `__silent:` 前缀
- **旧版本**：命令不加 `__silent:` 前缀

**继续执行 0b。**

### 0b. 开关检查 + Python 检测（并行执行）

**⚠️ 必须在 0a 完成后执行此步骤，不可跳过。两条命令无依赖，Agent 必须在同一次响应中并行发出。**

**说明：开关检查读取用户本地配置（`~/.comate/settings.json` 中的 `enableSmartCommit`），是用户个人的开关偏好。步骤 1 中的 `result.disabled` 是服务端/空间级别的开关，两者独立，互不替代。**

#### 命令 1：开关检查（纯 shell，无外部依赖）

Agent 根据环境上下文中的操作系统信息选择对应命令（**新版本加 `__silent:` 前缀，旧版本不加**）：

**macOS / Linux：**
```
[__silent: ]cat ~/.comate/settings.json 2>/dev/null || echo "{}"
```

**Windows（cmd）：**
```
[__silent: ]type "%USERPROFILE%\.comate\settings.json" 2>NUL || echo {}
```

Agent 解析输出的 JSON，检查 `enableSmartCommit` 字段：
- 如果 `enableSmartCommit` 为 `false` → **立即结束 skill，不再输出任何内容，不再执行任何后续步骤**
- 如果 `enableSmartCommit` 为 `true`、字段不存在、或命令输出为 `{}`（文件不存在）→ 默认开启，继续

#### 命令 2：Python 可用性检测

与命令 1 **并行**发出（**新版本加 `__silent:` 前缀，旧版本不加**）：

**macOS / Linux：**
```
[__silent: ]python3 --version 2>/dev/null || python --version 2>/dev/null
```

**Windows（cmd）：**
```
[__silent: ]python --version 2>NUL || python3 --version 2>NUL || py -3 --version 2>NUL
```

- 如果命令**成功**（返回版本号，如 `Python 3.x.x`）→ 记住**输出中实际成功的那个命令名**（`python3`、`python` 或 `py -3`），后续步骤中所有 `python3` 必须替换为该命令名
- 如果**全部失败** → 标记 `python_available = false`。后续步骤 1 直接进入"iCafe 获取失败降级"流程，步骤 2 中 `git_diff_cli.py` 也无法执行，Agent 应直接执行 git 命令获取 diff 信息

#### 跨平台说明

Agent 根据环境上下文的操作系统信息判断当前平台。同时需注意：
- **macOS / Linux**：shell 命令中使用 `2>/dev/null` 抑制错误
- **Windows（cmd）**：使用 `2>NUL` 抑制错误，路径使用 `%USERPROFILE%`，`cd` 跨盘符需用 `cd /d`
- 后续步骤中所有 `cd <path> && <command>` 在 Windows 上应改为 `cd /d <path> && <command>`

---

## 步骤 1：获取 iCafe 数据

通过 `run_command` 执行以下命令获取 iCafe 卡片数据。**新版本加 `__silent:` 前缀，旧版本不加。**

```bash
[__silent: ]python3 <skill_directory>/scripts/match_card_cli.py --username "${COMATE_USERNAME}"
```

脚本内部通过 `os.environ.get("COMATE_USERNAME")` 读取用户名（跨平台兼容），`${COMATE_USERNAME}` 由 Agent 构建命令时替换为实际值。

从 stdout 输出的 JSON 解析为 `result` 对象。

**⚠️ 开关检查（服务端/空间级别）：** 解析 `result` 后，**首先**检查 `result.get("disabled")` 是否为 `True`。如果是，**必须立即结束 skill，不再执行任何后续步骤，不输出任何内容**。此开关与步骤 0a 的本地用户偏好开关独立，由服务端控制。

### iCafe 获取失败降级

**如果步骤 1 的命令执行失败（脚本报错、超时、返回非 JSON 等），Agent 不应中断流程，而是进入"无卡片模式"：**
1. 标记 `icafe_failed = true`
2. 步骤 2 正常执行（获取 git diff 和 commit style 不依赖 iCafe）
3. **跳过步骤 3（语义匹配）、步骤 4（卡片选择）、步骤 5（处理用户操作）、步骤 6（存储卡片 ID）**
4. 直接进入步骤 7，基于 diff 内容和 `commit_style` 生成 commit message（不带卡片 ID 前缀）
5. 步骤 8 展示提交确认时，`boundCard` 为 `null`，commit message 中不包含卡片信息

`find_matching_card()` 内部自动完成用户获取、空间检测、卡片查询等工作，返回结构化数据。**不再获取 git diff，diff 由 Agent 在步骤 2 中自行获取。**

**⚠️ 并行执行：步骤 1 和步骤 2 之间无依赖关系。Agent 必须在同一次响应中同时发出步骤 1 的 iCafe 命令、步骤 2 的所有 git diff 命令（每个 workspace 一条）以及步骤 2 的 git log 命令，由客户端并行执行。** 多 workspace 时，不同 workspace 的 git 命令也一起并行发出。例如 2 个 workspace = 1（iCafe）+ 2（git diff）+ 1（git log）= 4 条并行 `run_command`。

## 步骤 2：获取 git diff（支持多 workspace）

**⚠️ 多 Workspace 必须逐一执行：** Agent 必须从环境上下文的 `Workspace Path` 中读取**所有**路径。`Workspace Path` 的格式为：
```
Workspace Path:
- /path/to/repo1
- /path/to/repo2
```
Agent 必须对列表中的**每一个路径**分别执行下方的命令。**即使只有部分 workspace 有变更，也必须对所有 workspace 都执行一次**，以确定每个仓库是否有变更。禁止只对第一个 workspace 执行后就跳过其余的。

### 命令格式

对每个 workspace 执行（**新版本加 `__silent:` 前缀，旧版本不加**）：

```bash
[__silent: ]python3 <skill_directory>/scripts/git_diff_cli.py --workspace <workspace_path>
```

脚本输出 JSON，直接解析为该 workspace 的 diff 数据：
```json
{
    "workspace": "/path/to/project",
    "changed_files": [
        {"file": "src/App.tsx", "insertions": 76, "deletions": 66},
        {"file": "src/NewFile.tsx", "insertions": 30, "deletions": 0}
    ],
    "untracked_files": ["src/NewFile.tsx"],
    "stat_summary": "2 files, +106, -66",
    "has_changes": true,
    "diff_content": "<tracked diff + untracked diff>",
    "truncated": false
}
```

### 获取历史 commit message 风格

**与 git diff 并行执行。** 对**第一个** workspace 执行以下命令获取最近的 commit message 记录（**新版本加 `__silent:` 前缀，旧版本不加**）：

```bash
[__silent: ]cd <第一个workspace_path> && git log --oneline -n 20
```

Agent 从输出中提取最近 20 条 commit message，分析其格式特征（包括但不限于）：
- **前缀格式**：是否使用卡片 ID 前缀（如 `dkx-200`）、Conventional Commits 前缀（如 `feat:`, `fix:`）、或其他自定义前缀
- **语言**：commit message 使用中文还是英文
- **描述风格**：简短描述 vs 详细描述、使用动词开头 vs 名词短语
- **分隔符**：前缀与描述之间使用空格、冒号还是其他分隔符

将分析结果记为 `commit_style`，供步骤 3 生成 `recommended_commit_message` 时参考。**不输出任何内容。**

### 构建数据结构

Agent 从各 workspace 的 JSON 输出构建两级数据结构，**不输出任何内容**：

#### 1) `workspace_diffs` — 按 workspace 独立存储

直接使用脚本输出的 `changed_files`、`stat_summary`、`has_changes` 字段：

```
workspace_diffs = {
    "<workspace_path>": {
        "changed_files": [...],   // 脚本输出的 changed_files
        "stat_summary": "...",    // 脚本输出的 stat_summary
        "has_changes": true/false // 脚本输出的 has_changes
    }
}
```

#### 2) `diff_summary` — 合并后用于步骤 3 语义匹配

```
diff_summary = {
    "changed_files": [...],      # 所有 workspace 的变更文件路径字符串列表（含 workspace 标识）
    "stat_summary": "...",       # 合并后的统计摘要
    "diff_content": "...",       # 各 workspace 的 diff_content 拼接，超过 500 行截断
    "truncated": true/false
}
```

**合并规则：**
1. `changed_files`：所有 workspace 的文件路径，多 workspace 时加 workspace 标识
2. `diff_content`：各 workspace 的 `diff_content` 按 workspace 分段拼接，总计超过 500 行则截断
3. 多 workspace 时，`stat_summary` 为各 workspace 统计的汇总

**如果所有 workspace 均无变更（所有 `has_changes` 为 false），`diff_summary` 设为 `null`。**

### 无变更提前退出

**如果 `diff_summary` 为 `null`（即所有 workspace 均无变更），Agent 必须立即输出以下提示并结束 skill，不再执行步骤 3-9：**

```
ℹ️ 当前工作区没有检测到代码变更，无需提交。

你可以先修改代码，之后再使用 /auto-commit 提交。
```

**新版本和旧版本均直接输出上述文本（不走 `__interactive` UI），输出后立即结束，禁止继续执行后续步骤。**

---

同时，Agent 内部基于 diff 内容生成 `defaults.title`（建卡默认标题）：取前 3 个变更文件名，生成格式为 `"优化 xxx, yyy 相关功能"`。将生成的标题写入 `result["defaults"]["title"]`。

Agent 内部分析 git diff 内容，总结代码变更的语义（修改了哪些模块、变更目的、涉及的业务领域），**不输出任何内容**，仅用于后续生成 commit message。

## 步骤 3：语义匹配（内部完成，禁止输出）

在展示 UI 或文本**之前**，Agent 需要在内部（不输出）完成语义匹配：
**注意：执行到此步骤时，`diff_summary` 一定不为 `null`（无变更已在步骤 2 提前退出）。**

- 如果 `result["cards"]` 非空：
  1. 根据 `diff_summary` 中的变更文件、diff 内容，对每张卡片进行语义匹配度评分（0-100 分）
     - **语义相关性**（主要）：diff 修改的模块、函数、业务逻辑是否与卡片标题描述的任务相关
     - **类型匹配度**（次要）：diff 的变更性质（修复 bug、新增功能、重构等）是否与卡片类型吻合
  2. 按 `score` 降序对 `result["cards"]` 重新排序
  3. **过滤低分卡片**：仅保留 score >= 30 的卡片，score < 30 的卡片从 `result["cards"]` 中移除
  4. 确定 `viewMode`：过滤后卡片非空 → `"list"`，过滤后卡片为空 → `"create"`
  5. **生成 `recommended_commit_message`**：基于 diff 内容和匹配卡片生成 commit message，**必须参考步骤 2 中获取的 `commit_style`（历史 commit message 风格）**，确保生成的 message 与项目历史提交风格保持一致。具体规则：
     - 如果历史 message 使用了特定的前缀格式（如 `feat:`, `fix:`, `chore:` 等 Conventional Commits 格式），生成的 message 也应使用相同格式
     - 如果历史 message 使用中文描述，生成的 message 也应使用中文；反之使用英文
     - 如果历史 message 使用 `<卡片ID> <描述>` 格式，则沿用该格式
     - 如果历史记录中无法识别出明确的风格模式，则使用默认格式 `<spacePrefix>-<sequence> <简要描述>`
  6. 记住 `recommended_commit_message` 供后续步骤使用
- 如果 `result["cards"]` 为空：`viewMode` 默认为 `"create"`

## 步骤 4：展示卡片选择

**上下文快捷匹配：** 如果当前对话上下文中用户已明确指定了卡片（如提到了卡片 ID "dkx-200"、iCafe 链接、或说"用上次的卡片"），Agent 可直接将该卡片作为 `selected_card`，跳过展示选择 UI，直接进入步骤 6。

**否则，必须展示卡片选择 UI，禁止自行替用户选择或创建卡片。**

根据版本使用对应的交互方式：
- **新版本**：请参考 `references/new_version_instruction.md`
- **旧版本**：请参考 `references/old_version_instruction.md`

## 步骤 5：处理用户操作

根据版本使用对应的处理方式：
- **新版本**：请参考 `references/new_version_instruction.md`
- **旧版本**：请参考 `references/old_version_instruction.md`

### 创建卡片命令模板

当用户操作需要新建卡片时（新版本 action=create，旧版本输入 "new"），使用以下命令（**新版本加 `__silent:` 前缀，旧版本不加**）：

```
[__silent: ]cd <用户项目目录> && python3 <skill_directory>/scripts/create_card_cli.py --title "<card.title>" --space-prefix "<card.spacePrefix>" --type-name "<card.typeName>" --username "${COMATE_USERNAME}"
```

## 步骤 6：存储关联的 iCafe 卡片 ID（必须执行）

在步骤 5 处理完用户操作、拿到 `selected_card` 后，**必须**立即调用 `run_command` 将卡片 ID 保存到会话中：

```
run_command(command="__interactive:set-icafe-issue-id {\"issueId\":\"<spacePrefix>-<sequence>\"}")
```

例如，如果 `selected_card` 是 `{"sequence": "200", "spacePrefix": "dkx", ...}`，则执行：

```
run_command(command='__interactive:set-icafe-issue-id {"issueId":"dkx-200"}')
```

## 步骤 7：判断是否展示提交确认

Agent 内部分析以下信号判断是否展示提交确认，**不输出任何内容**：

**展示的信号（满足任意一条）：**
- 当前对话中用户明确表示"完成了"、"可以提交"等意图
- git diff 的代码变更是完整的、可独立运行的
- 对话上下文表明任务已结束

**不展示（仅输出 message）：**
- 用户表示还有后续修改
- 代码变更不完整
- 对话上下文表明任务仍在进行

## 步骤 8：展示提交确认

根据版本使用对应的交互方式：
- **新版本**：请参考 `references/new_version_instruction.md`
- **旧版本**：请参考 `references/old_version_instruction.md`

## 步骤 9：执行提交 + 输出结果

根据版本使用对应的处理方式：
- **新版本**：请参考 `references/new_version_instruction.md`
- **旧版本**：请参考 `references/old_version_instruction.md`

### 最终输出格式

**提交成功：**
```
✅ 已完成提交

提交信息：
- Commit: <commit_hash>
- Message: <commit_message>
- 绑定卡片: <space_prefix>-<sequence>
- 分支: <branch_name>
```

**取消提交：**
```
⏸️ 提交已取消

建议 commit message 已准备好：
<commit_message>

绑定卡片：<space_prefix>-<sequence> (<card_title>)

你可以稍后使用 `git commit -m "<message>"` 手动提交
```

**判断不展示 UI（直接输出 message）：**
```
📝 Commit message 已准备好

建议 commit message：
<commit_message>

绑定卡片：<space_prefix>-<sequence> (<card_title>)

代码变更未完成，请确认后再提交
```

旧版本 IDE 提交成功后额外提示：`如需推送到远程，请执行：git push`

---

## 返回值说明

### `find_matching_card()` 返回字典

| 字段 | 说明 |
|------|------|
| cards | 简化卡片列表：sequence, title, type, status |
| space_prefix | 空间前缀（如 "dkx"） |
| space_id | 空间数字 ID |
| space_name | 空间名称 |
| final_iql | 实际执行的完整 IQL |
| available_types | 可绑定卡片类型列表：[{id, name}, ...] |
| available_spaces | 可访问空间列表：[{id, prefix, name, types}, ...] |
| defaults | 默认表单值：{title, type_id, space_id}（title 由 Agent 在步骤 2 中生成） |

### `diff_summary`（Agent 在步骤 2 中构建）

| 字段 | 说明 |
|------|------|
| changed_files | 所有 workspace 的变更文件路径字符串列表（用于步骤 3 语义匹配） |
| stat_summary | 合并后的 git diff --stat 统计行 |
| diff_content | 合并后的 diff 全文（超过 500 行截断） |
| truncated | 是否被截断 |

### `workspace_diffs`（Agent 在步骤 2 中构建，用于步骤 8 构造 payload）

| 字段 | 说明 |
|------|------|
| \<workspace_path\>.changed_files | 该 workspace 的 `[{file, insertions, deletions}]` 列表 |
| \<workspace_path\>.stat_summary | 该 workspace 的统计摘要（如 "2 files, +100, -78"） |
| \<workspace_path\>.has_changes | 该 workspace 是否有变更 |

## 卡片链接

```
https://console.cloud.baidu-int.com/devops/icafe/issue/{space_prefix}-{card_sequence}/show
```

## 配置

### 认证

token 按优先级读取：
1. 环境变量 `COMATE_AUTH_TOKEN`
2. 文件 `~/.comate/login`

### 跨平台 Python 命令

本 skill 中所有 `python3` 命令在 Windows 上可能不可用。步骤 0a 会自动检测可用的 Python 命令名，后续步骤中的 `python3` 必须替换为检测到的命令名：
- **macOS / Linux**：通常为 `python3`
- **Windows**：通常为 `python` 或 `py -3`

### 跨平台 Shell 命令

本 skill 中涉及 `cd <path> && <command>` 的命令模板在 Windows 上需注意：
- **macOS / Linux**：`cd /path/to/project && git add .`
- **Windows（cmd）**：需使用 `cd /d <path>` 以支持跨盘符切换，如 `cd /d D:\project && git add .`
- Agent 执行命令时应根据环境上下文中的操作系统信息自动选择正确的 `cd` 写法。

### 资源

- **scripts/icafe/** — 核心实现包
  - `client.py` — ICafeQueryClient、常量、配置、API 客户端
  - `matching.py` — `find_matching_card()` 主入口、匹配逻辑
  - `farseer.py` — `get_binding_card_types()` 获取可绑定卡片类型
- **scripts/git_utils.py** — diff 摘要、用户获取、git log 提取
- **scripts/git_diff_cli.py** — git diff 摘要命令行工具（步骤 2）
- **scripts/match_card_cli.py** — 查询匹配卡片命令行工具（步骤 1）
- **scripts/create_card_cli.py** — 创建卡片命令行工具
- **scripts/recognize_card_cli.py** — 识别卡片命令行工具
- **scripts/compat.py** — 版本兼容性检测模块
- **scripts/logger.py** — 统一日志模块
- **references/query_reference.md** — IQL 语法参考
- **references/issue_type_mapping.json** — 卡片类型 ID 映射
- **references/new_version_instruction.md** — 新版本 IDE 交互指南
- **references/old_version_instruction.md** — 旧版本 IDE 交互指南
