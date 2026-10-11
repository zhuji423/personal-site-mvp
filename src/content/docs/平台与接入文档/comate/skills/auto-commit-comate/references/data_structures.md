---
title: "数据结构与 Payload 构造参考"
description: "本文档包含 auto-commit skill 各步骤中涉及的数据结构定义和 payload 构造规则。Agent 在需要构建具体数据时参考此文档。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\auto-commit-comate\\references\\data_structures.md"
---
# 数据结构与 Payload 构造参考

本文档包含 auto-commit skill 各步骤中涉及的数据结构定义和 payload 构造规则。Agent 在需要构建具体数据时参考此文档。

---

## 步骤 1：match_card_cli.py 返回值（result 对象）

| 字段 | 说明 |
|------|------|
| cards | 简化卡片列表：sequence, title, type, status |
| space_prefix | 空间前缀（如 "dkx"） |
| space_id | 空间数字 ID |
| space_name | 空间名称 |
| final_iql | 实际执行的完整 IQL |
| available_types | 可绑定卡片类型列表：[{id, name}, ...] |
| available_spaces | 可访问空间列表：[{id, prefix, name, types}, ...] |
| defaults | 默认表单值：{title, type_id, type_name, space_id} |
| disabled | 服务端/空间级别开关，为 True 时立即结束 skill |

---

## 步骤 2：git_diff_cli.py 输出格式

每个 workspace 执行 `git_diff_cli.py` 后输出的 JSON：

```json
{
    "workspace": "/path/to/project",
    "changed_files": [
        {"file": "src/App.tsx", "insertions": 76, "deletions": 66}
    ],
    "untracked_files": ["src/NewFile.tsx"],
    "stat_summary": "2 files, +106, -66",
    "has_changes": true,
    "diff_content": "<tracked diff + untracked diff>",
    "truncated": false
}
```

### Agent 构建的数据结构

#### workspace_diffs（按 workspace 独立存储）

```
workspace_diffs = {
    "<workspace_path>": {
        "changed_files": [...],   // 脚本输出的 changed_files
        "stat_summary": "...",
        "has_changes": true/false
    }
}
```

#### diff_summary（合并后用于语义匹配）

```
diff_summary = {
    "changed_files": [...],      # 所有 workspace 的文件路径（多 workspace 时加标识）
    "stat_summary": "...",       # 合并统计
    "diff_content": "...",       # 各 workspace diff_content 拼接，超 500 行截断
    "truncated": true/false
}
```

合并规则：各 workspace 的 `diff_content` 按 workspace 分段拼接，总计超 500 行截断。所有 `has_changes` 为 false 时，`diff_summary` 设为 `null`。

---

## 统一缓存文件

路径：`/tmp/__comate_auto_commit_cache.json`

结构：
```json
{
  "icafe_result": { /* match_card_cli.py 完整输出 */ },
  "git_diffs": {
    "/path/to/workspace1": { /* git_diff_cli.py 完整输出 */ },
    "/path/to/workspace2": { /* git_diff_cli.py 完整输出 */ }
  }
}
```

写入时机：
- `icafe_result`：步骤 1 由 `match_card_cli.py` 写入
- `git_diffs[workspace]`：步骤 2 由 `git_diff_cli.py` 对每个 workspace 写入

清理时机：步骤 9 执行完成后由 Agent 清理（`rm -f /tmp/__comate_auto_commit_cache.json`）。

---

## Payload Builder 脚本

Agent 在构造 `__interactive:` payload 时，**禁止自行拼接 JSON**，必须通过以下脚本验证并生成。脚本会对输入数据进行结构校验，返回验证结果。

### 通用用法

```bash
__silent: python3 <skill_directory>/scripts/<script_name>.py --json '<camelCase 数据 JSON>'
```

### 输出格式

- 验证通过：`{"valid": true, "payload": {...}}`
- 验证失败：`{"valid": false, "errors": ["具体错误描述", ...]}`
- 系统错误：`{"error": "..."}`

### 处理流程

1. Agent 构造 camelCase 数据
2. 调用 builder 脚本传入数据
3. 解析脚本输出：
   - `valid: true` → 用 `payload` 调用 `__interactive:` UI
   - `valid: false` → 根据 `errors` 修正数据，重新调用脚本（最多重试 1 次）
   - 重试仍失败或 `error` → 降级为文本交互（参考 interaction_instruction.md 中降级格式）

---

### build_icafe_cards_payload.py（步骤 4）

**作用**：从缓存文件读取原始数据，自动完成 snake_case → camelCase 转换并验证，输出 `__interactive:icafe-cards` 的 payload。

**用法**（最简形式）：
```bash
python3 build_icafe_cards_payload.py --view-mode list --default-title "优化 xxx 相关功能"
```

脚本自动读取 `/tmp/__comate_icafe_result.json`（由 `match_card_cli.py` 在步骤 1 自动写入）。

**Agent 不需要手动转换任何字段名，不需要拼 JSON，不需要传文件路径。** 只需传入 2 个必填参数（`--view-mode`、`--default-title`）和 1 个可选参数（`--cards`，排序后的卡片列表）。

**验证规则**：
- `cards` 为数组，每项含 `sequence/title/type/status`
- `viewMode` 为 `"list"` 或 `"create"`
- `availableSpaces` 每项含 `id/prefix/name/types`，`types` 每项含 `id/name`
- `defaults` 含 `title(string)/typeId(string)/typeName(string)/spaceId(int)`

---

### build_git_commit_payload.py（步骤 8）

**作用**：验证并输出 `__interactive:git-commit` 的 payload。

**用法**：脚本自动从统一缓存读取 diff 数据，执行 git branch 获取分支信息，Agent 只需传入 commit message 和绑定卡片：
```bash
python3 build_git_commit_payload.py --cache --commit-message "<message>" --bound-card '<card JSON 或 null>'
```
- `--commit-message`（必填）：commit message
- `--bound-card`（必填）：选定卡片 JSON 对象，无卡片传字符串 `'null'`

**输出 payload 结构**：

```json
{
    "commitMessage": "dkx-200 修复登录问题",
    "boundCard": {"sequence": "200", "title": "修复登录问题", "type": "Bug", "status": "开发中", "spacePrefix": "dkx"},
    "workspaces": [
        {
            "workspace": "/path/to/frontend-app",
            "repoName": "frontend-app",
            "currentBranch": "feature/xxx",
            "remoteBranches": [{"name": "feature/xxx", "isCurrent": true}, {"name": "main", "isCurrent": false}],
            "hasChanges": true,
            "diffSummary": {
                "changed_files": [{"file": "src/App.tsx", "insertions": 76, "deletions": 66}],
                "stat_summary": "2 files, +100, -78"
            }
        }
    ]
}
```

**验证规则**（脚本内部自动保证，Agent 无需关心）：
- 顶层包含 `commitMessage`, `boundCard`, `workspaces`
- `boundCard` 为 `null` 或包含 `sequence/title/type/status/spacePrefix` 的对象
- 每个 workspace 自动填充 `workspace/repoName/currentBranch/remoteBranches/hasChanges/diffSummary`
- `diffSummary` 内部的 `changed_files` 和 `stat_summary` 保持 snake_case（与 git_diff_cli.py 输出一致）

### 用户操作返回

- 确认：`{"action": "submit", "repos": [{"workspace": "...", "commitMessage": "...", "branch": "..."}]}`
- 取消：`{"action": "cancel"}`
