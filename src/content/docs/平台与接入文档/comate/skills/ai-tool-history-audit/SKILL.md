---
title: "AI Tool History Audit"
description: "Audit and analyze the user's AI coding tool usage history across multiple tools (Codex, Claude Code, Comate, Ducc, Trae, Cursor, etc.). Summarize what tasks were done in each period, identify pitfalls and recurring issues, analyze root causes, and provide improvement suggestions. Trigger when the user asks to review their AI tool history, summarize past work, analyze mistakes/pitfalls across tools, or wants a retrospective of their AI-assisted development workflow."
date: "2026-02-27"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ai-tool-history-audit\\SKILL.md"
name: "ai-tool-history-audit"
---

# AI Tool History Audit

## Intent

Use this skill to perform a comprehensive retrospective analysis of the user's AI coding tool usage. The goal is to extract actionable insights from historical data: what was done, what went wrong, why, and how to improve.

> **语言偏好**：默认使用中文输出分析报告；如果用户用英文提问则用英文。

## Workflow

### Phase 0: Scope — Ask for Time Range

**在开始任何扫描之前**，先用 `AskUserQuestion` 询问用户想要审计的时间范围。

提供以下选项：
- **最近 1 周**（推荐，适合写周报）
- **最近 2 周**
- **最近 1 个月**
- **全部历史**

获得时间范围后，在后续所有 Phase 中仅提取该时间窗口内的数据（根据 timestamp / ctime / mtime 过滤）。这样可以大幅减少扫描量，加快报告生成速度，并让输出更聚焦。

> 如果用户在调用 skill 时已经指定了时间范围（如"最近一周"、"上个月"），则跳过此步骤，直接使用用户指定的范围。

### Phase 1: Discovery — Locate History Sources

Scan the user's home directory for known AI tool data directories. Use the Explore agent for each tool **in parallel** to maximize efficiency. **Only scan data within the time range established in Phase 0.**

**Known locations to check:**

| Tool | Primary Paths | Key Files |
|---|---|---|
| Codex | `~/.codex/` | `history.jsonl`, `config.toml`, `conversations/`, `archive/` |
| Claude Code | `~/.claude/` | `history.jsonl`, `projects/`, `todos/`, `stats-cache.json`, `skills/` |
| Comate/Ducc | `~/.comate/`, `~/.comate-engine/store/`, `~/.baidu-cc/` | `comate_chat_sessions`, `codeWrittenMetric.json`, `log/error_report_*` |
| Trae | `~/.trae/`, `~/.trae-cn/`, `~/.trae-aicc/` | Session logs under `logs/` |
| Cursor | `~/.cursor/` | Conversation history, settings |
| Windsurf | `~/.windsurf/`, `~/.codeium/` | Chat logs, configuration |

For each tool directory found:
1. List top-level structure (`ls -la`)
2. Identify history/session files by size and modification date
3. Note total file count, date range, and disk usage
4. Skip tools with no meaningful history

**Output**: A tool inventory table listing each discovered tool, its data path, session count, date range, and disk footprint.

### Phase 2: Extraction — Read and Parse History

For each tool with meaningful history, read the key files to extract:

1. **Task Content**: What the user asked the AI to do (user prompts, session titles)
2. **Timestamps**: When each task was performed (file ctime/mtime, embedded timestamps)
3. **Errors & Failures**: Any error messages, crashes, failed operations
4. **Configuration**: Models used, MCP servers, plugins, API endpoints
5. **Project Contexts**: Which workspace/project directories were active

**Parsing strategies per tool:**

- **Codex `history.jsonl`**: Each line is a JSON object with `prompt` and `session_id`. Read all lines to get the full prompt history. Cross-reference with `conversations/{session_id}.jsonl` for details.
- **Claude Code `history.jsonl`**: Similar JSONL format. Also read `projects/*/sessions-index.jsonl` and `stats-cache.json` for aggregated stats. The `todos/` directory (one file per session) reveals task planning patterns.
- **Comate `comate_chat_sessions`**: Large JSON file listing all sessions with `title`, `ctime`, `mtime`, `workspaceDir`, `model` fields. Read the first portion (it can be hundreds of MB). Also check `codeWrittenMetric.json` for code generation stats and `log/error_report_*` for crashes.
- **Trae**: Read log files under `logs/` for session summaries.

**Important**: Some files are very large (100MB+). Read only the first 500-2000 lines, or use structured queries (grep for titles, timestamps, error keywords) instead of full reads.

**Output**: Per-tool raw extraction with task lists, timestamps, error logs, and config snapshots.

### Phase 3: Timeline Synthesis — Build the Chronological Narrative

Merge extractions from all tools into a unified timeline:

1. **Sort all tasks by date** across all tools
2. **Group into phases** by identifying natural clusters:
   - Look for project/topic shifts (different workspace directories)
   - Look for time gaps (>1 week of inactivity)
   - Look for tool switches (same task migrated between tools)
3. **For each phase**, document:
   - Date range
   - Primary tool(s) used
   - Main tasks/projects
   - Key outputs/deliverables
4. **Cross-reference overlaps**: Identify cases where the same task appeared in multiple tools (indicates context loss and re-explanation overhead)

**Output**: A phased timeline table with columns: Phase, Date Range, Tools, Tasks, Notes.

### Phase 3.5: Project Consolidation — Group by Project

将时间线中的任务**按项目（workspace/目录）重新归类**，而非按工具或日期。这是周报的核心视角。

1. **识别项目**：根据 workspace 目录、session 标题关键词、任务主题，将所有会话归入具体项目。同一项目可能跨多个工具。
2. **合并跨工具信息**：同一项目在 Claude Code / Codex / Comate 中的会话合并到一起，避免同一件事在不同工具的段落中重复出现。
3. **提取每个项目的**：
   - 具体做了什么（任务列表，足够写周报的颗粒度）
   - 产出了什么（文件、报告、skill、配置变更、代码修复）
   - 遇到了什么问题、如何解决的
   - 涉及哪些模型/技术栈
4. **注意区分相似但不同的项目**：例如"模型评测框架开发"（改框架代码/checker/config）和"benchmark 数据分析"（用框架跑出的结果做归因分析）是两个项目，不要混在一起。

**Output**: Per-project task breakdown with deliverables, issues, and outcomes.

### Phase 4: Pitfall Identification — Find What Went Wrong

Systematically scan for issues in these categories:

| Category | What to Look For |
|---|---|
| **Config/Setup Issues** | Auth failures, token errors, MCP registration failures, env detection failures |
| **Tool Stability** | Crashes, corrupted files, connection drops, temp file race conditions |
| **Network/Infra** | DNS failures, unreachable services, VPN issues, timeout errors |
| **AI-Generated Code Bugs** | IndentationError, type errors, import failures post-generation |
| **Workflow Inefficiency** | Same task in multiple tools, repeated sessions on same topic, oil-monkey-script-4-versions pattern |
| **Context Loss** | Re-explaining the same requirement to a new tool, orphaned sessions |
| **Resource Bloat** | Single sessions >50MB, total disk >1GB per tool, 900+ todo files |

For each pitfall found:
1. **Describe the symptom** (what happened)
2. **Quantify the cost** (how many sessions/hours were spent)
3. **Identify the root cause** (why it happened)
4. **Classify**: Config issue / Tool bug / User workflow / Infrastructure / AI limitation

**Output**: A numbered pitfall list with Symptom, Cost, Root Cause, Classification.

### Phase 5: Improvement Recommendations

Generate actionable suggestions organized by impact:

1. **High Impact** (eliminates recurring time sinks):
   - Unified MCP config management
   - Tool specialization (assign each task type to one primary tool)
   - Pre-flight network/env checks before starting work

2. **Medium Impact** (reduces friction):
   - Personal work log for cross-tool context preservation
   - Session size limits and periodic cleanup
   - Dotfiles repo for AI tool config backup

3. **Low Impact** (nice-to-have):
   - Skill/automation creation for repeated patterns
   - Analytics dashboard for personal productivity

For each recommendation:
- State the **problem** it addresses (reference the pitfall number)
- Describe the **concrete action** (not vague advice)
- Provide an **example** if applicable (a script, a config snippet, a file structure)

### Phase 6: Report Assembly

根据用户需求输出不同格式的报告。

#### 格式 A：完整审计报告（默认）

适用于全量审计或回顾。包含以下 section：

1. **工具概览** — Tool inventory table
2. **时间线** — Phased timeline of work
3. **重点项目** — Per-project detailed breakdown（来自 Phase 3.5）
4. **踩坑记录** — Pitfall list with root causes
5. **改进建议** — Recommendations by impact tier
6. **数据总览** — Summary statistics table (sessions, messages, disk, models, etc.)

#### 格式 B：周报模式

适用于用户写周报。当时间范围为 1 周或 2 周时，**默认使用此格式**。特征：

1. **按项目组织**，每个项目用**一段话**描述本周进展
2. 段落内容应包含：做了什么 → 关键发现/产出 → 解决了什么问题
3. **不要按工具拆分**：同一项目在不同工具中的工作合并到一段话里
4. **语气简洁专业**：适合直接粘贴到周报中，不需要二次编辑
5. **避免内容混淆**：相似但独立的项目必须严格分开（如"框架开发"vs"数据分析"）

周报格式示例：

```
# 周报（YYYY.MM.DD — YYYY.MM.DD）

## 一、项目名称 A

本周完成了 XXX，具体包括 A、B、C。发现了 XXX 问题，根因是 XXX，已通过 XXX 方式修复。产出了 XXX 报告/文件/skill。

## 二、项目名称 B

...
```

> 先输出周报格式，如果用户需要更详细的展开（如某个项目的具体任务列表、踩坑记录等），再按需补充。

## Key Heuristics

- **"4-version oil-monkey pattern"**: When 3+ sessions exist with nearly identical titles (e.g., "油猴脚本批量下载 v1/v2/v3/v4"), this indicates iterative failure without adequate error diagnosis between attempts. Flag as workflow issue.
- **"Cross-tool echo"**: When the same task title appears in 2+ tools within a short time window, the user lost context switching tools. Flag as context loss.
- **"Giant session smell"**: Any single session file >50MB suggests the conversation ran too long without checkpointing. Flag as resource bloat.
- **"Auth storm"**: Clusters of auth/token errors at the start of a tool's history indicate incomplete initial setup. Flag as onboarding issue.
- **"Config corruption cluster"**: Multiple `.corrupted.*` or `.backup.*` files indicate write contention. Flag as tool stability issue.

## Iteration

Keep improving this skill by:
1. Adding new AI tool paths as they emerge (e.g., Gemini CLI, Amazon Q, GitHub Copilot Workspace)
2. Recording new pitfall patterns discovered during audits
3. Updating parsing strategies when tool history formats change
4. Adding reference files for tool-specific deep-dive analysis if needed
