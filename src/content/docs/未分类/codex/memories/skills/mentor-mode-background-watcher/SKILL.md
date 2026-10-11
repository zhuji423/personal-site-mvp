---
title: "Mentor Mode Background Watcher"
description: "User-specific mentor workflow for `core-migrate_ori`: scaffold-first teaching, user-owned `MENTOR_USER_CORE` blocks, cwd auto-detect, and a quiet 5-second background watcher."
date: "2026-04-24"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\skills\\mentor-mode-background-watcher\\SKILL.md"
name: "mentor-mode-background-watcher"
argument-hint: "[cwd-or-target-file]"
user-invocable: "false"
---

# Mentor Mode Background Watcher

## When To Use

Use this when the user asks for mentor mode, Claude learning-mode-like behavior, save-triggered review, or a quiet background coding coach in `/Users/zhuji_m4pro/Downloads/core-migrate_ori`.

Non-goals:
- Do not use this when the user wants a one-shot finished implementation.
- Do not immediately write the user-owned core logic.
- Do not promise a global install into `~/.codex/skills` if the environment cannot write there.

## Inputs And Context

Gather first:
1. Whether the user wants teaching mode, direct implementation, or both.
2. The current cwd and the target file or exercise directory.
3. Whether the code already contains `MENTOR_USER_CORE` markers.
4. Which validation path fits the exercise: `javac` for a small standalone Java file, or something else for other languages.
5. Whether the environment can write outside the workspace.

## Procedure

1. Treat "mentor mode" as scaffold-first behavior: explain the minimal design, keep the user involved, and leave the design-shaping code in a marker block.
2. If the repo already has `skills/mentor-mode`, inspect `SKILL.md`, `scripts/mentor_loop.py`, `scripts/core_block_status.py`, and `scripts/start_mentor.py` before editing.
3. Add or preserve `MENTOR_USER_CORE_START` / `MENTOR_USER_CORE_END` markers around the code the user should implement.
4. If the user wants background review, use the cwd-driven launcher: `python3 skills/mentor-mode/scripts/start_mentor.py`.
5. Validate the launcher with `python3 skills/mentor-mode/scripts/start_mentor.py --dry-run` and confirm it watches only the intended source files.
6. For the small Java learning exercises in this repo, prefer a `javac` command over Maven when the watched target is a small set of `.java` files.
7. Keep mentor output quiet by default; only escalate when the user is stalled, blocked, or the validation command fails.

## Efficiency Plan

- Search for `MENTOR_USER_CORE` first to find the real watched files quickly.
- Reuse the existing repo-local mentor skill instead of building another watcher flow from scratch.
- Use `--dry-run` before starting a long-lived watcher session.
- For Java exercises, compile only the touched file to a temp output directory instead of invoking the whole repo build.
- Stop early if the user actually wants a full implementation rather than mentor mode.

## Pitfalls And Fixes

- Symptom: user says some version of "谁叫你写完的". Cause: over-eager completion. Fix: switch back to teach-first pacing and leave the core block to the user.
- Symptom: watcher includes `SKILL.md`. Cause: marker regex matched documentation. Fix: filter auto-detect to source-like extensions.
- Symptom: global install into `~/.codex/skills` fails with `Operation not permitted`. Cause: workspace-only write access. Fix: keep the skill local and explain the limitation.
- Symptom: Maven compile fails with `resolver-status.properties (Operation not permitted)`. Cause: repo build path depends on blocked `~/.m2` writes. Fix: use `javac` for the small Java exercise.
- Symptom: mentor loop stops recognizing progress because `No core blocks found.` Cause: markers were removed. Fix: keep the ownership markers in place after the user implements the code.

## Verification Checklist

- The user’s request actually calls for teaching/mentor behavior rather than pure implementation.
- The target source file contains a valid `MENTOR_USER_CORE` block.
- `python3 skills/mentor-mode/scripts/start_mentor.py --dry-run` resolves the intended file set only.
- The chosen validation command works in this environment.
- The watcher runs in quiet mode and only emits on real stalls or failures.
