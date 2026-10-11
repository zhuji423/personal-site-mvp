---
title: "Mentor Mode"
description: "Build an interactive mentoring workflow where Codex scaffolds architecture and non-critical plumbing, the user implements core logic in marked code blocks, and each save triggers automated local review feedback. Use when the user asks for learning mode, pair-programming mode, user-owned core coding, real-time review on save, or hook-like coding supervision."
date: "2026-04-23"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\skills\\mentor-mode\\SKILL.md"
name: "mentor-mode"
---

# Mentor Mode

Use this skill to run an interactive "you write the core logic, I supervise quality" workflow.

## Enforce Ownership Contract

1. Identify the exact files to change.
2. Mark ownership explicitly:
`[MENTOR_USER_CORE_START <block-id>]` and `[MENTOR_USER_CORE_END <block-id>]` for user-owned core logic.
3. Keep scaffold, integration, and validation code owned by Codex.
4. Do not edit user-owned core blocks unless the user explicitly asks.

Marker example:

```java
// [MENTOR_USER_CORE_START auth-header-injection]
// TODO(user): implement mapping from login cookie to request global variable
// [MENTOR_USER_CORE_END auth-header-injection]
```

## Execution Flow

1. Create scaffold code and insert user-core markers.
2. Ask the user to implement one small core block at a time (5-10 meaningful lines).
3. Start local watcher:

```bash
python3 skills/mentor-mode/scripts/mentor_loop.py \
  --path src/main/java \
  --include "*.java" \
  --cmd "./mvn-compile.sh" \
  --cmd "python3 skills/mentor-mode/scripts/core_block_status.py --path src/main/java --include '*.java' --require-done"
```

4. After each save, read watcher feedback and provide:
- blocker issues (compile/runtime failures)
- correctness risks (logic/regression)
- one focused next action for the user

## Feedback Format

Use this compact format:

1. `Critical`: must fix before moving forward.
2. `Risk`: likely regression or weak assumption.
3. `Next step`: smallest concrete code change.

Keep advice specific to changed files and marker blocks.

## Tooling

- `scripts/mentor_loop.py`: save-triggered watcher + command runner + core-block progress checks.
- `scripts/core_block_status.py`: inspect user-core marker blocks and fail when unfinished.

## Guardrails

1. Prefer one user block at a time; avoid parallel unfinished core blocks.
2. Keep each user block narrowly scoped to design-significant logic.
3. When checks fail, explain root cause before proposing code.
4. When checks pass, still surface one improvement suggestion.
