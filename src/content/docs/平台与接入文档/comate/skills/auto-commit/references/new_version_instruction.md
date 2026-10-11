---
title: "新版本 IDE 交互指南"
description: "本文档适用于新版本 IDE（IDE 名称占位符已替换、插件版本 ≥ 4.1.0）的交互方式。"
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\auto-commit\\references\\new_version_instruction.md"
---
# 新版本 IDE 交互指南

本文档适用于**新版本 IDE**（IDE 名称占位符已替换、插件版本 ≥ 4.1.0）的交互方式。

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

## 步骤 1：获取 iCafe 数据（新版本命令）

使用 SKILL.md 步骤 1 中定义的命令模板，**加 `__silent:` 前缀**执行。

---

## 步骤 2：获取 git diff（新版本命令）

使用 SKILL.md 步骤 2 中定义的命令模板，**加 `__silent:` 前缀**执行。

---

## 步骤 4：展示卡片选择（交互式 UI）

调用 `run_command` 展示卡片选择/新建 UI，**禁止在调用前输出任何文字**：

```
run_command(command="__interactive:icafe-cards <payload JSON>")
```

payload 构造方法 — 用 `result` 中的字段和匹配结果拼接 JSON：
```python
import json
payload = json.dumps({
    "cards": result["cards"],        # 已按匹配度排序
    "spacePrefix": result["space_prefix"],
    "spaceId": result["space_id"],
    "spaceName": result["space_name"],
    "availableSpaces": result["available_spaces"],
    "viewMode": viewMode,  # "list" 或 "create"
    "defaults": {
        "title": result["defaults"]["title"],
        "typeId": result["defaults"]["type_id"],
        "spaceId": result["space_id"]
    }
})
command = f"__interactive:icafe-cards {payload}"
```

完整示例 command 值：
```
__interactive:icafe-cards {"cards":[{"sequence":"200","title":"修复登录问题","type":"Bug","status":"开发中"}],"spacePrefix":"dkx","spaceId":12345,"spaceName":"测试空间","viewMode":"list","availableSpaces":[{"id":12345,"prefix":"dkx","name":"测试空间","types":[{"id":"5009","name":"Bug"},{"id":"5007","name":"Story"}]}],"defaults":{"title":"修复登录验证码刷新问题","typeId":"5009","spaceId":12345}}
```

---

## 步骤 5：处理用户操作（新版本 IDE）

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

## 步骤 8：展示提交确认（交互式 UI）

调用 `run_command` 展示提交确认 UI：

```
run_command(command="__interactive:git-commit <payload JSON>")
```

Agent 仅对 **`hasChanges: true` 的 workspace** 执行 `git branch -vv` + `git branch -r --sort=-committerdate`（使用 `__silent:` 前缀）。**无变更的 workspace 跳过分支查询，`currentBranch` 和 `remoteBranches` 使用空值。** 多 workspace 时，不同 workspace 的分支查询命令必须在同一次响应中并行发出。然后构造 payload：

**⚠️ 重要：`workspaces` 数组必须包含环境上下文 `Workspace Path` 中列出的所有 workspace，不可遗漏。** 即使某个 workspace 没有变更（`hasChanges: false`），也必须包含在数组中。

payload 结构（多 workspace 格式）：
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
        },
        {
            "workspace": "/path/to/shared-utils",
            "repoName": "shared-utils",
            "currentBranch": "",
            "remoteBranches": [],
            "hasChanges": false,
            "diffSummary": null
        }
    ]
}
```

**构造规则：**
- `commitMessage`：基于 diff 和绑定卡片生成的 commit message（格式 `"<spacePrefix>-<sequence> <brief_description>"`）
- `boundCard`：步骤 5 中选定的卡片信息
- `workspaces`：对每个 workspace 目录，使用步骤 2 中构建的 `workspace_diffs` 数据：
  - `workspace`：绝对路径
  - `repoName`：路径的最后一段
  - `currentBranch`：有变更时从 `git branch -vv` 解析当前分支名，无变更时为空字符串
  - `remoteBranches`：有变更时从 `git branch -r` 解析远程分支列表；无变更时为空数组。解析规则：
    1. 跳过包含 `->` 的行（如 `origin/HEAD -> origin/master`，这是 HEAD 指针，不是分支）
    2. 对每一行 trim 后去掉 `origin/` 前缀，得到分支名
    3. 从 `git branch -vv` 输出中解析当前分支的远程追踪分支名，将匹配的分支标记为 `isCurrent: true`，其余为 `false`
    4. 最多取 10 个分支（当前追踪分支必须包含在内），按最近活跃排序
  - `hasChanges`：该 workspace 是否有变更（`workspace_diffs[path].has_changes`）
  - `diffSummary`：有变更时为 `workspace_diffs[path]` 中的 `changed_files` + `stat_summary`，无变更时为 `null`

**顶层不再有旧的 `currentBranch`/`remoteBranches`/`diffSummary` 字段。**

完整示例 command 值：
```
__interactive:git-commit {"commitMessage":"dkx-200 修复登录验证码刷新问题","boundCard":{"sequence":"200","title":"修复登录问题","type":"Bug","status":"开发中","spacePrefix":"dkx"},"workspaces":[{"workspace":"/home/user/frontend-app","repoName":"frontend-app","currentBranch":"feature/login-fix","remoteBranches":[{"name":"feature/login-fix","isCurrent":true},{"name":"main","isCurrent":false}],"hasChanges":true,"diffSummary":{"changed_files":[{"file":"src/login.ts","insertions":15,"deletions":3}],"stat_summary":"1 file, +15, -3"}}]}
```

用户操作后，tool output 返回 JSON：
- 确认提交：`{"action": "submit", "repos": [{"workspace": "...", "commitMessage": "...", "branch": "..."}]}`
- 取消提交：`{"action": "cancel"}`

---

## 步骤 9：执行提交（新版本 IDE）

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
- 执行 `git push origin HEAD:refs/for/<branch>` 推送到远程
- 多仓库时逐个执行，每个仓库独立处理

**如果是 action === "cancel"：**
- 输出"已取消提交"
