---
title: "智能提交助手"
description: "当用户完成代码修改、需要提交代码时，必须使用此 skill，而非直接执行 git commit。自动获取 git diff、匹配 iCafe 活跃卡片、生成 commit message，并引导用户完成绑定卡片和代码提交。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\auto-commit-comate\\SKILL.md"
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

## 流程总览

根据前置检查结果，流程分为两条主线：

- **iCode 仓库** (`is_icode_repo = true`)：步骤 0 → 1+2(并行) → 3 → 4 → 5 → 6 → 7 → 8 → 9
- **非 iCode 仓库** (`is_icode_repo = false`)：步骤 0 → 2 → 7 → 8 → 9（跳过 1/3/4/5/6，commit message 不带卡片 ID）

**Agent 必须通过 `__interactive:` UI 组件与用户交互（步骤 4 用 `__interactive:icafe-cards`，步骤 8 用 `__interactive:git-commit`）。禁止自行拼接 payload JSON，必须通过 builder 脚本验证后调用。**

---

## 步骤 0：前置检查（串行执行，完全静默）

**整个前置检查过程完全静默。**

### iCode 仓库检测

对第一个 workspace 执行：
```
__silent: cd <第一个workspace_path> && git remote -v
```

检查输出是否包含 `icode.baidu.com`：包含 → `is_icode_repo = true`，不包含或失败 → `is_icode_repo = false`。

---

## 步骤 1：获取 iCafe 数据

执行：
```bash
__silent: python3 <skill_directory>/scripts/match_card_cli.py --username "${COMATE_USERNAME}"
```

解析 stdout 的 JSON 为 `result`。先检查 `result.disabled`，为 `True` 则立即结束。脚本会自动将 result 写入统一缓存文件（`/tmp/__comate_auto_commit_cache.json`），供步骤 4 使用。

**失败降级**：脚本报错/超时/非 JSON → 标记 `icafe_failed = true`，跳过步骤 3-6，直接进入步骤 7 生成无卡片 commit message。

**并行执行：步骤 1 和步骤 2 无依赖，必须在同一次响应中同时发出所有命令。** 例如 2 个 workspace 时 = 1（iCafe）+ 2（git diff）+ 1（git log）= 4 条并行命令。

## 步骤 2：获取 git diff（支持多 workspace）

**⚠️ 多 Workspace 必须逐一执行：** Agent 必须从环境上下文的 `Workspace Path` 中读取**所有**路径，对每一个路径分别执行下方命令。**即使只有部分 workspace 有变更，也必须对所有 workspace 都执行一次**，禁止只对第一个 workspace 执行后就跳过其余的。

对每个 workspace 执行：

```bash
__silent: python3 <skill_directory>/scripts/git_diff_cli.py --workspace <workspace_path>
```

同时对第一个 workspace 并行执行获取 commit 风格：
```bash
__silent: cd <第一个workspace_path> && git log --oneline -n 20
```

Agent 从 git log 分析 `commit_style`（前缀格式、语言、描述风格），供步骤 3/7 生成 commit message 时保持风格一致。**不输出任何内容。** 脚本同时将 diff 结果写入统一缓存文件（`/tmp/__comate_auto_commit_cache.json`），供步骤 8 自动构建 payload。

脚本输出 JSON 格式、以及如何构建 `workspace_diffs` 和 `diff_summary`，详见 `references/data_structures.md`（包含脚本输出示例和合并规则）。

**无变更提前退出**：所有 workspace 均无变更 → 输出以下文本并结束，禁止继续执行后续步骤：
```
ℹ️ 当前工作区没有检测到代码变更，无需提交。

你可以先修改代码，之后再使用 /auto-commit 提交。
```

Agent 内部基于 diff 内容生成 `defaults.title`（建卡默认标题）：取前 3 个变更文件名，生成格式为 `"优化 xxx, yyy 相关功能"`，写入 `result["defaults"]["title"]`。

同时，Agent 内部分析 diff 内容推断**卡片类型**（Bug/Story/Task 等），若推断的类型存在于 `result.available_types` 中，更新 `result.defaults.type_id` 和 `result.defaults.type_name`。推断规则：
- Bug 修复（错误修复、异常处理、边界条件修正） → 匹配 "Bug"
- 新增功能（新文件、新 API、UI 变更） → 匹配 "Story" 或 "Feature"
- 重构/优化（格式化、性能优化、配置修改） → 匹配 "Task"
- 基础设施变更（依赖升级、构建脚本） → 匹配 "Tech Feature" 或 "Tech Task"
- 无法推断或类型不在可用列表中 → 保持脚本返回的默认值不覆盖

## 步骤 3：语义匹配（内部完成，禁止输出）

对 `result.cards` 中每张卡片按以下维度评分（0-100）：
- **语义相关性**（主要）：diff 修改的模块、函数、业务逻辑是否与卡片标题描述的任务相关
- **类型匹配度**（次要）：diff 的变更性质（修复 bug、新增功能、重构等）是否与卡片类型吻合

按 score 降序排序，过滤 score < 30 的卡片。

确定 `viewMode`：过滤后有卡片 → `"list"`，无卡片 → `"create"`。

生成 `recommended_commit_message`：基于 diff + 匹配卡片 + `commit_style` 生成，保持与项目历史风格一致。具体规则：
- 历史 message 使用 Conventional Commits（如 `feat:`, `fix:`）→ 沿用
- 历史 message 使用中文 → 生成中文；英文 → 生成英文
- 历史 message 使用 `<卡片ID> <描述>` → 沿用
- 无法识别明确风格 → 默认 `<spacePrefix>-<sequence> <简要描述>`

## 步骤 4：展示卡片选择

**上下文快捷匹配：** 如果对话中用户已指定卡片（卡片 ID、iCafe 链接等），直接作为 `selected_card`，跳过 UI。

**否则，必须通过 builder 脚本验证 payload 后展示卡片选择 UI。禁止自行拼接 JSON 或替用户选择/创建卡片。**

具体操作：
1. 确定模型决策：`viewMode`（`"list"` 或 `"create"`）、`defaults.title`（Agent 根据 diff 语义生成）、`cards`（步骤 3 排序后，可选）
2. 调用 builder 脚本（脚本自动从 `/tmp/__comate_icafe_result.json` 读取 result，不需要模型传文件）：
   ```
   __silent: python3 <skill_directory>/scripts/build_icafe_cards_payload.py --view-mode list --default-title "优化 xxx 相关功能"
   ```
   **⚠️ 不需要传 --result-file、不需要手动转换字段名、不需要拼 JSON。脚本自动完成所有转换。`--cards` 可选，不传则使用 result 中的原始顺序。**
3. 解析输出：
   - `{"valid": true, "payload": {...}}` → 提取 `payload` 内层 JSON，使用 `run_command` 调用 `__interactive:icafe-cards`（禁止将整个 `{"valid":true,"payload":{...}}` 传入，禁止将 payload 作为文本输出）
   - `{"valid": false, "errors": [...]}` → 根据 errors 修正数据，重试一次；仍失败则按 `references/interaction_instruction.md` 降级为文本交互
   - `{"error": "..."}` → 直接降级为文本交互

## 步骤 5：处理用户操作

根据用户选择/创建/跳过处理，参考 `references/interaction_instruction.md`。

**创建卡片命令模板：**
```
__silent: cd <用户项目目录> && python3 <skill_directory>/scripts/create_card_cli.py --title "<card.title>" --space-prefix "<card.spacePrefix>" --type-name "<card.typeName>" --username "${COMATE_USERNAME}"
```

## 步骤 6：存储关联的 iCafe 卡片 ID

拿到 `selected_card` 后**必须**立即执行：
```
run_command(command="__interactive:set-icafe-issue-id {\"issueId\":\"<spacePrefix>-<sequence>\"}")
```

例如 `selected_card` 为 `{"sequence": "200", "spacePrefix": "dkx", ...}` 时：
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

完整则进入步骤 8 展示确认 UI，未完整则仅输出建议的 commit message。

非 iCode 仓库的 commit message 不带卡片 ID 前缀。

## 步骤 8：展示提交确认

必须通过 builder 脚本构造并验证 payload 后展示，禁止自行拼接 JSON 或用文本替代。

### 推荐方式：缓存模式（Agent 不需要手动构造 workspaces）

1. 调用 builder 脚本，传入 commit message 和绑定卡片：
   ```
   __silent: python3 <skill_directory>/scripts/build_git_commit_payload.py --cache --commit-message "<commit_message>" --bound-card '<card JSON 或 null>'
   ```
   - `--cache`：从统一缓存读取 diff 数据，自动执行 git branch 命令获取分支信息
   - `--commit-message`：必填
   - `--bound-card`：选定的卡片 JSON（步骤 5 获得），非 iCode 仓库或无卡片传 `'null'`

2. 解析输出：
   - `{"valid": true, "payload": {...}}` → 提取 `payload` 内层 JSON，使用 `run_command` 调用 `__interactive:git-commit`（禁止将整个 `{"valid":true,"payload":{...}}` 传入，禁止将 payload 作为文本输出）
   - `{"valid": false, "errors": [...]}` → 根据 errors 修正数据，重试一次；仍失败则按 `references/interaction_instruction.md` 降级为文本交互
   - `{"error": "..."}` → 直接降级为文本交互

## 步骤 9：执行提交 + 输出结果

参考 `references/interaction_instruction.md` 执行提交。

**推送方式：** 统一使用 `git push origin HEAD:refs/for/<branch>` 推送到 Gerrit 代码评审。

### 最终输出格式

**提交成功：**
```
✅ 已完成提交

提交信息：
- Commit: <commit_hash>
- Message: <commit_message>
- 绑定卡片: <space_prefix>-<sequence>（仅 iCode 仓库）
- 分支: <branch_name>
```

**取消提交：**
```
⏸️ 提交已取消

建议 commit message 已准备好：
<commit_message>

绑定卡片：<space_prefix>-<sequence> (<card_title>)（仅 iCode 仓库）

你可以稍后使用 `git commit -m "<message>"` 手动提交
```

**判断不展示 UI（直接输出 message）：**
```
📝 Commit message 已准备好

建议 commit message：
<commit_message>

绑定卡片：<space_prefix>-<sequence> (<card_title>)（仅 iCode 仓库）

代码变更未完成，请确认后再提交
```

---

## 配置

**认证**：token 按优先级读取 `COMATE_AUTH_TOKEN` 环境变量 → `~/.comate/login` 文件。

**跨平台**：统一使用 `python3` 调用脚本，如果执行失败（命令不存在），自动依次尝试 `python`、`py -3`，某个成功则后续统一使用该命令名。

**卡片链接**：`https://console.cloud.baidu-int.com/devops/icafe/issue/{space_prefix}-{card_sequence}/show`
