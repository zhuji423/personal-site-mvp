---
title: "memory_summary"
description: "The user works on a local macOS/zsh machine under /Users/zhujim4pro and repeatedly uses Codex/Claude-style agents for re"
date: "2026-05-02"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\memory_summary.md"
---
## User Profile

The user works on a local macOS/zsh machine under `/Users/zhuji_m4pro` and repeatedly uses Codex/Claude-style agents for repo orientation, documentation generation, dashboard/runtime forensics, local workspace organization, Bilibili note generation, SSH/IDE setup, and mentor-style coding/tutoring. Recurring working areas include `/Users/zhuji_m4pro/Agent_learn`, `/Users/zhuji_m4pro/Downloads/core-migrate_ori`, `/Users/zhuji_m4pro/code/LLM_from_scrach`, and Baidu Java repos around `/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code`.

They usually ask in Chinese and prefer answers that are direct, evidence-backed, and operational. Good answers for this user usually include exact paths, commands, config fields, rollout handles, and clear validation. They often correct shallow summaries, metadata-only outputs, or answers that stay conceptual for too long.

Their collaboration style is conditional and worth respecting. If they say "不要修改", they want inspection and a plan first. If they say "开始修改", they want execution without repeated micro-confirmations. If they ask for mentor mode or learning-mode-like behavior, they want scaffold-first teaching with user-owned core logic rather than a completed solution. In tutoring contexts, they may impose a strict first-mention teaching format and expect it to persist through the conversation.

They also care about durable workflows that reduce future friction: organized workspaces, shared asset roots, passwordless SSH, cwd-driven watchers, restartable batch jobs, and documentation or analytics outputs that are easy to navigate later. For larger documentation jobs, they are comfortable with a coordinator plus subagent/team workflow as long as scope is verified first and the outputs stay evidence-based.

## User preferences

- Default to Chinese when the user asks in Chinese, unless they switch language.
- For direct local lookup questions, answer path-first and concise, with a plain existence confirmation.
- When the user says "不要修改", inspect broadly and give a problem list or plan before editing.
- When the user says "开始修改", proceed with the agreed scope instead of re-asking small decisions.
- When the user sends "继续" after interruption, inspect partial state and resume from the furthest completed step instead of restarting.
- For repo/config questions where they ask for "快速回答", lead with the conclusion and put evidence paths or fields immediately after it.
- When the user asks to understand a codebase "按照这个计划去分析", verify scope and real code paths before writing docs or making changes.
- For large documentation jobs, if the user asks to use subagents/Claude team style, default to a coordinator + specialized writer pattern.
- When they ask for practical Codex usage help, give shortcut-, flag-, or command-oriented answers rather than a generic overview.
- When they ask a direct CLI capability question like monthly usage availability, answer that yes/no capability first before expanding.
- When they ask about restoring Codex model settings, inspect `~/.codex/config.toml` first and undo pinned model or migration overrides rather than hand-tuning one setting.
- When they ask about Codex Cloud, explain local-vs-cloud first, then separate web/app Cloud threads, CLI `codex cloud`, environment binding, and deploy/hosting.
- If the UI shows `Env: none` or they say submission does nothing, treat environment selection/binding as the first debugging step.
- When they say they only know Python basics or have shallow backend understanding, explain Java/Maven/backend concepts from first principles and with analogies.
- For backend tutoring, on first mention of a concept use the requested `正面 / 反面 / 反事实 / 合` structure when that rule has been set in the conversation.
- For backend tutoring, prefer everyday analogies over backend jargon and keep scope tiny when the time budget is only `1-2小时`.
- When they ask for mentor mode or Claude learning-mode-like behavior, do not jump straight to the full solution; leave design-shaping or core logic to the user.
- For mentor-mode review, prefer a quiet background coach that auto-detects project files, polls every 5 seconds, and only speaks when the user is stuck or blocked.
- For small Java learning demos, isolate the exercise in a child directory; if they say "之前的删掉", remove the earlier variant before rebuilding.
- For Bilibili lecture-note PDFs, never accept metadata-only output; default to Whisper transcripts, keyframes, and transcript/frame-grounded writing.
- For Bilibili runs, use authenticated access when cookies/headers are provided or `HTTP 412` appears, and report per-video outputs plus degradation notes.
- For Bilibili collection requests like "下面所有的分p视频", check both `pages[]` and `ugc_season` or related collection metadata.
- For local workspace organization, the user prefers stable top-level structure over ad hoc nesting.
- In `Agent_learn`, if they set a shared asset rule, follow it exactly: image assets for the learning-record workflow belong under `downloads_20260427_organized/_remote_images`.
- When turning pasted internal table data into a tool, prefer a direct one-shot CSV + runnable command path over an abstract framework.
- If they correct an internal endpoint after showing the real curl, trust the pasted curl over inferred path fragments.
- When they ask for "完整的请求信息", print method, URL, headers, body, and a curl-like rendering, redacting secrets unless they explicitly ask to see them.
- When they want a cookie or credential-like operator input reused locally, prefer a hidden local file or readback wrapper, never raw secret storage in memory artifacts.
- For SSH/IDE setup, configure the durable IDE workflow and prefer passwordless SSH key auth over saving passwords.
- For Claude session/subagent forensics, default to timeline + hook map + flow + file locations, and include line numbers or retrieval handles when possible.
- When they ask unfamiliar runtime terms like `sidechain local_agent worker`, define the plain-language meaning first and then the protocol details.
- For dashboard/session-detail work, default to raw + derived exhaustive views when they ask for "所有字段" or "所有的tool use".

## General Tips

- Known local config/memory root: `/Users/zhuji_m4pro/.codex`; re-check with `ls -ld` if existence matters.
- Recurring workspaces: `/Users/zhuji_m4pro/Agent_learn`, `/Users/zhuji_m4pro/Downloads/core-migrate_ori`, `/Users/zhuji_m4pro/code/LLM_from_scrach`, and Baidu repos around `/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code`.
- For Baidu documentation plans, assume path drift until `rg --files`, `rg -n`, and `nl -ba` confirm the real code paths.
- For the newer `wiki_claude` workflow, the validated Core scope was `apismartmgt`, not all of `core`.
- For Claude resume failures on this machine, distinguish three branches early: model-name mismatch, thinking-history replay failure, and auth/network issues.
- If Claude resume errors mention both `DeepSeek-V3.2` and `content[].thinking`, treat it as a broken resume/config chain and inspect `~/.claude/settings.json` plus `~/.claude/tasks/...` before advising a restart.
- For quick Java repo orientation, inspect `pom.xml` fields like `<java.version>`, `<maven.compiler.source>`, and `<maven.compiler.target>` before broader scans.
- For local Codex config restore or model questions, check live CLI help and `~/.codex/config.toml` directly; older command/model details are time-sensitive.
- If a Codex CLI question is about capabilities such as usage/quota, `codex --help` and related `--help` pages are faster evidence than general searching.
- In `core-migrate_ori`, repo-local mentor tooling is the reliable path; writes into global `~/.codex/skills` may fail with `Operation not permitted`.
- For tiny Java exercises there, prefer `javac` validation over repo Maven compile when `.m2` or resolver permissions fail.
- For Bilibili-to-PDF work, preflight network/auth, Whisper model availability or TLS, and PDF engine availability before promising final PDFs.
- In `Agent_learn` learning-record localization, go straight to the shared `_remote_images` root instead of creating temporary asset trees.
- The internal ITP batch runner lives under `tools/itp_batch/`; direct Python invocation from the real directory is safer than assuming a server wrapper path.
- On server coaching tasks, check `pwd` and `ls` before giving path-sensitive commands; heredoc and prompt-copy mistakes are common.
- For Claude dashboard or session forensics, prefer filesystem- and JSONL-backed evidence over assistant-authored summaries.

## What's in Memory

### /Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code

#### 2026-04-30

- `wiki_claude` documentation via Claude team/subagents: reflective-cuddling-firefly, qamate-docs-v2, wiki_claude, apismartmgt, arch-writer, topo-writer, manual-writer, DOCUMENTATION_INDEX.md
  - desc: Covers plan-driven system documentation for the Baidu QAMate repos from `cwd=/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code`: verifying real code paths, narrowing Core scope to `apismartmgt`, splitting the work across Claude writer agents, and validating the final four-doc `wiki_claude/` output set.
  - learnings: Do not trust the plan paths blindly. Re-derive real paths first, constrain each subagent to one target Markdown file, and keep the coordinator responsible for `DOCUMENTATION_INDEX.md`, reading order, and sensitivity checks.

#### 2026-04-28

- Three-repo Java version scan, `pom.xml` explanation, and local Mermaid architecture doc: apismart-code, qamate-server, inner-os, itp, pom.xml, requirements.txt, ARCHITECTURE_OVERVIEW.md, Mermaid, QAMateCoreClient
  - desc: Covers fast orientation across the three Baidu repos near this checkout: Java-version detection, Python-friendly explanation of `pom.xml`, and a local `ARCHITECTURE_OVERVIEW.md` deliverable with Mermaid diagrams.
  - learnings: Lead with the answer, then cite `pom.xml` evidence. The durable split was `core=Java 21`, `apiExecutor=Java 17`, and most of `itp=Java 8`, with the architecture output written locally instead of only explained in chat.

### /Users/zhuji_m4pro/Downloads/core-migrate_ori

#### 2026-04-30

- Claude resume recovery and thinking-mode 400 diagnosis: claude code, resume, continue, content[].thinking, ANTHROPIC_BASE_URL, deepseek-v4-pro, DeepSeek-V3.2, ~/.claude/tasks
  - desc: Covers diagnosing Claude/Claude Code continue-resume failures from `cwd=/Users/zhuji_m4pro/Downloads/core-migrate_ori`, especially the combination of DeepSeek Anthropic-compatible model mismatch and thinking-history replay failure.
  - learnings: If logs mention both unsupported DeepSeek model names and `content[].thinking`, treat it as broken resume state plus config mismatch. Recovery is usually "new session + re-read task files", not endless retries on the same broken resume chain.

### /Users/zhuji_m4pro/Agent_learn

#### 2026-04-28

- Learning-record archive organization, markdown image localization, and shared `_remote_images` rule: downloads_20260427_organized, 08-周洁学习记录, _remote_images, agents.md, gzip -t, tar -tzf, rte.weiyun.baidu.com
  - desc: Covers organizing downloaded learning-record exports inside `cwd=/Users/zhuji_m4pro/Agent_learn`, extracting safely, localizing markdown images, and enforcing the shared asset-root rule under `downloads_20260427_organized/_remote_images`.
  - learnings: Integrate into the existing organized tree, not a sibling folder. Some remote image URLs fail because `docGuid` is missing, and some exported `.bin` files are JSON errors rather than real images.

- Internal ITP batch runner from pasted table data: tools/itp_batch, health_itp_nodes.csv, batch_itp_nodes.py, run_health_itp_batch.sh, itpMigrate, --print-cookie, request logging
  - desc: Covers building and operating a one-shot internal batch tool in `cwd=/Users/zhuji_m4pro/Agent_learn`: turning pasted rows into a CSV, posting to the corrected `itpMigrate` endpoint, persisting Cookie input locally, and making request logs operator-friendly.
  - learnings: Trust the raw pasted curl for the endpoint, print full structured request info, and prefer direct `python3 batch_itp_nodes.py run ...` from the actual server directory over brittle wrapper assumptions.

- One-day backend tutoring for a front-end learner: Node Express, 正面, 反面, 反事实, 合, 日常类比, GET /api/hello, POST /api/login, 1-2小时
  - desc: Covers a time-boxed backend-learning plan from `cwd=/Users/zhuji_m4pro/Agent_learn` for a user who finds backend obscure and wants first-principles explanations plus a strict first-mention teaching format.
  - learnings: Ask for stack, goal, time, and code depth first. With this user, keep the lesson to a tiny Express demo and explain new concepts with `正面 / 反面 / 反事实 / 合` plus everyday analogies.

### /Users/zhuji_m4pro/code/LLM_from_scrach

#### 2026-04-24

- Codex model restore, model naming, Cloud task launch, environment binding, and `deploy` meaning: ~/.codex/config.toml, gpt-5.5, gpt5.5, codex cloud, --env ENV_ID, Env: none, codex login status, deploy
  - desc: Covers restoring local Codex model-selection behavior and answering Cloud onboarding questions even though the conversational cwd was `cwd=/Users/zhuji_m4pro/code/LLM_from_scrach`. Search here first for `~/.codex/config.toml` restore requests, exact model-name wording, or `Env: none` Cloud debugging.
  - learnings: Restore by removing pinned model entries and migration overrides, use exact model spelling like `gpt-5.5`, and separate web/app Cloud threads from CLI `codex cloud` and from real deployment/hosting.

### Older Memory Topics

#### /Users/zhuji_m4pro/Downloads/core-migrate_ori

- Mentor-mode workflow, quiet background watcher, and Java lesson demos: mentor mode, claude 的 learning mode, MENTOR_USER_CORE, start_mentor.py, --poll-interval 5.0, javac, java-login-lesson
  - desc: Covers scaffold-first mentor mode, repo-local mentor tooling, quiet 5-second background watching, and tiny Java demo exercises in `cwd=/Users/zhuji_m4pro/Downloads/core-migrate_ori`. Use for mentor mode, save-triggered review, or supervised learning-demo work.

#### /Users/zhuji_m4pro/Agent_learn

- Bilibili note-generation workflow and quality batches: bilibili_notes, quality_batch_1, BILI_COOKIE, HTTP 412, transcript.srt, frames_manifest.json, note.pdf, ugc_season
  - desc: Covers the user's Bilibili-to-PDF workflow in `cwd=/Users/zhuji_m4pro/Agent_learn`, including Whisper-first notes, authenticated access, per-BV outputs, collection discovery, batch prompts, and organized final outputs.

- Claude Dashboard raw session detail, todos, tool analytics, and imagegen CLI: claude-dashboard, history.jsonl, /api/session/<session_id>, tool_use, tool_result, /api/tool-calls-by-project, NotebookEdit, imagegen, 401 invalid_api_key
  - desc: Covers dashboard feature work and Claude session/tool analytics rooted in `cwd=/Users/zhuji_m4pro/Agent_learn` with code changes in `/Users/zhuji_m4pro/claude-dashboard`. Use for raw session visibility, todo-count explanation, all-tools analytics, or imagegen CLI troubleshooting.

- Claude resumed-session and subagent protocol forensics: sessionId, SessionStart:resume, subagent, sidechain, local_agent, agentId, TaskOutput, queue-operation, PID
  - desc: Covers older Claude JSONL forensic work from `cwd=/Users/zhuji_m4pro/Agent_learn`: resumed-session flow, hook counts, subagent launch protocol, queue notifications, and durable retrieval handles.

- Markdown curriculum cleanup and Week 0-5 mainline: markdown, NO_BROKEN_REL_LINKS, NO_ODD_FENCES, Mermaid, 太散乱了, 主线, engineering loop
  - desc: Covers learning-material cleanup and curriculum reframing in `cwd=/Users/zhuji_m4pro/Agent_learn`, including rendering fixes, broken-link scans, and a single engineering mainline for Week 0-5 docs.

- SSH remote access and passwordless IDE login: ssh, ~/.ssh/config, Remote-SSH, seetacloud-westd, ssh-copy-id, SSH_KEY_LOGIN_OK
  - desc: Covers IDE-friendly remote access setup on this machine, including alias management, dedicated keys, and passwordless verification.

- Local environment/path and Codex usage basics: .codex, /Users/zhuji_m4pro/.codex, codex -a never, /plan, Shift+Tab, codex-cli 0.124.0, usage, quota
  - desc: Covers direct environment lookup plus practical Codex CLI usage questions from local shells, including `.codex` path lookup, approval flags, Plan mode switching, and the absence of a monthly usage/quota command in observed CLI help.

#### /Users/zhuji_m4pro

- Conservative `~/Downloads` cleanup: Downloads, top-level cleanup, 01_文档, 10_其他, find -maxdepth 1, moved 441 files
  - desc: Covers a safe home-directory cleanup strategy for `/Users/zhuji_m4pro/Downloads`: classify only top-level regular files into numbered folders and leave hidden files plus existing directories untouched unless the user asks for deeper cleanup.
