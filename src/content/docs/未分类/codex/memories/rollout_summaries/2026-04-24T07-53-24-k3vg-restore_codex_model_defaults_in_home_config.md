---
title: "Restored Codex model settings in `~/.codex/config.toml`"
description: "Rollout context: The user wanted the Codex model selection list/configuration “restored to original/default behavior” af"
date: "2026-05-05"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-24T07-53-24-k3vg-restore_codex_model_defaults_in_home_config.md"
---
thread_id: 019dbe7a-b0c7-7d30-acf8-163604b0484e
updated_at: 2026-04-24T10:27:13+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/24/rollout-2026-04-24T15-53-24-019dbe7a-b0c7-7d30-acf8-163604b0484e.jsonl
cwd: /Users/zhuji_m4pro/code/LLM_from_scrach
git_branch: main

# Restored Codex model settings in `~/.codex/config.toml`

Rollout context: The user wanted the Codex model selection list/configuration “restored to original/default behavior” after seeing a narrowed set of models (`gpt-5.4`, `gpt-5.4-mini`, `gpt-5.3-codex`, `gpt-5.2`) in the UI. The meaningful work happened in `~/.codex/config.toml` under the home directory, not inside the repo at `/Users/zhuji_m4pro/code/LLM_from_scrach`.

## Task 1: Restore Codex model config to defaults

Outcome: success

Preference signals:

- When the user saw a reduced model list, they asked to “帮我将 `.codex` 里面的设置模型都还原” -> future agents should treat `~/.codex/config.toml` as the likely place to restore model-selection behavior when the user says the model choices look narrowed or pinned.
- The user explicitly wanted the current fixed model set removed rather than adjusted one-by-one -> when restoring defaults, remove the pinned config entries instead of only editing a single model name.

Key steps:

- Located the active Codex config at `~/.codex/config.toml` after searching `~/.codex` for model-related settings.
- Confirmed the file contained `model = "gpt-5.4"`, `review_model = "gpt-5.4-mini"`, `model_reasoning_effort = "medium"`, and a migration rule mapping `"gpt-5.3-codex" = "gpt-5.4"`.
- Removed those model-specific lines, then re-read the file to confirm only the general settings and project trust entries remained.

Failures and how to do differently:

- The first broad search through `~/.codex` produced a very noisy result set, including cached artifacts and session logs. For this kind of task, jump quickly to `~/.codex/config.toml` after confirming it exists.
- The `perl -0pi` edit required escalated permissions because the target was outside the workspace. Future similar edits to `~/.codex` should expect escalation.

Reusable knowledge:

- `~/.codex/config.toml` is the authoritative place for the local Codex model selection and reasoning-effort defaults in this environment.
- The file can contain both a pinned model (`model`, `review_model`, `model_reasoning_effort`) and a migration override under `[notice.model_migrations]`; removing those entries restores more default behavior without affecting unrelated trust or feature settings.
- After the edit, the remaining config was:
  - `model_provider = "OpenAI"`
  - `disable_response_storage = true`
  - `network_access = "enabled"`
  - `windows_wsl_setup_acknowledged = true`
  - `[model_providers.OpenAI]` with `wire_api = "responses"`
  - per-project `trust_level` entries
  - `[features] memories = true`

References:

- [1] `~/.codex/config.toml` before edit contained:
  - `model = "gpt-5.4"`
  - `review_model = "gpt-5.4-mini"`
  - `model_reasoning_effort = "medium"`
  - `[notice.model_migrations]` with `"gpt-5.3-codex" = "gpt-5.4"`
- [2] After edit, `sed -n '1,120p' ~/.codex/config.toml` showed those lines removed and only general settings/trust entries left.
- [3] The user’s requested restoration target was the `.codex` config model settings, not the repo files.
