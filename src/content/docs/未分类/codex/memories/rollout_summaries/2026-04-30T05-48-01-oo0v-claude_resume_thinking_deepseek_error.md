---
title: "Claude Code 续聊报错排查：thinking 历史回传失败，且 DeepSeek 兼容接口模型名不匹配"
description: "Rollout context: 用户在 /Users/zhujim4pro/Downloads/core-migrateori 里问“帮我分析一下claude 怎么了继续”，并贴出报错：API Error: 400 {\"error\":{\""
date: "2026-05-05"
category: "未分类"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-30T05-48-01-oo0v-claude_resume_thinking_deepseek_error.md"
---
thread_id: 019ddcee-0bcc-7d82-bd13-9447e719901f
updated_at: 2026-04-30T07:34:00+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/30/rollout-2026-04-30T13-48-01-019ddcee-0bcc-7d82-bd13-9447e719901f.jsonl
cwd: /Users/zhuji_m4pro/Downloads/core-migrate_ori
git_branch: product_migrate

# Claude Code 续聊报错排查：thinking 历史回传失败，且 DeepSeek 兼容接口模型名不匹配

Rollout context: 用户在 `/Users/zhuji_m4pro/Downloads/core-migrate_ori` 里问“帮我分析一下claude 怎么了继续”，并贴出报错：`API Error: 400 {"error":{"message":"The \\`content[].thinking\\` in the thinking mode must be passed back to the API."...}}`。后续排查重点放在本机 Claude/Claude Code 配置、最近会话日志和任务状态文件上。

## Task 1: 分析 Claude 继续/恢复时报错

Outcome: success

Preference signals:
- 用户直接给出错误并问“帮我分析一下 claude 怎么了继续” -> 说明在类似故障排查里，用户希望先定位原因、再给出可执行恢复方案，而不是泛泛解释。
- 用户随后继续追问“继续” -> 暗示他们希望把问题放到“恢复当前中断任务”的语境里处理，而不是只停留在错误表面。

Key steps:
- 先用本机记忆/日志索引快速定位到 Claude 相关的 session 和 history，而不是盲查整个仓库。
- 读取 `~/.claude/settings.json`，确认当前走的是 DeepSeek 的 Anthropic 兼容接口：`ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic`，并且模型变量里配置了 `deepseek-v4-pro` / `deepseek-v4-flash`。
- 在最近的会话 JSONL 里看到：
  - `thinkingMetadata.maxThinkingTokens=31999`
  - 续聊后先出现模型名不被接口接受的错误：`The supported API model names are deepseek-v4-pro or deepseek-v4-flash, but you passed DeepSeek-V3.2.`
  - 随后又出现本次核心报错：`The \`content[].thinking\` in the thinking mode must be passed back to the API.`
- 同时读取 `~/.claude/tasks/76982603-9441-4753-8fa1-cb5393666c82/*.json`，确认当前 `wiki_claude` 相关任务仍是 `in_progress`，说明更合理的恢复方式是新会话继续任务，而不是强行复用损坏的 resume 历史。

Failures and how to do differently:
- 这类故障不是单纯“Claude 坏了”，而是“resume 的旧 thinking 历史 + 当前 API/模型配置”组合出了问题。未来遇到类似错误，应优先检查：
  1) 是否存在模型名不匹配；
  2) 是否启用了 thinking；
  3) 是否在恢复旧会话而不是新开会话。
- 不要直接建议用户继续复用同一个损坏的 resume 链路；先让用户用新会话接管当前任务状态文件更稳。

Reusable knowledge:
- 在这套环境里，Claude Code 走的是 DeepSeek 兼容 Anthropic 接口：`ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic`。
- 该接口只接受 `deepseek-v4-pro` 或 `deepseek-v4-flash`；日志里出现 `DeepSeek-V3.2` 时会触发 400 invalid_request_error。
- thinking 模式下，续聊/恢复时必须把 `content[].thinking` 原样回传，否则会报：`The \`content[].thinking\` in the thinking mode must be passed back to the API.`
- 相关任务状态文件在 `~/.claude/tasks/76982603-9441-4753-8fa1-cb5393666c82/`，可用来判断是否应该“新会话继续未完成任务”，而不是只看当前对话是否还能 resume。

References:
- `~/.claude/settings.json`：`ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic`、`ANTHROPIC_MODEL=deepseek-v4-pro`、`ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash`
- 最近会话 JSONL：`/Users/zhuji_m4pro/.claude/projects/-Users-zhuji-m4pro-code-baidu-qamate-strategy-apismart-code/76982603-9441-4753-8fa1-cb5393666c82.jsonl`
- 关键错误串：`The supported API model names are deepseek-v4-pro or deepseek-v4-flash, but you passed DeepSeek-V3.2.`
- 关键错误串：`The \`content[].thinking\` in the thinking mode must be passed back to the API.`
- 任务文件：`/Users/zhuji_m4pro/.claude/tasks/76982603-9441-4753-8fa1-cb5393666c82/{1..5}.json`

## Task 1: 回答用户“Claude 怎么了，继续”并给恢复建议

Outcome: success

Preference signals:
- 用户的问题是中文、且很直接地要“分析一下 claude 怎么了继续” -> 这类场景适合用中文给出结论、原因链和具体修复命令，而不是只给英文术语解释。

Key steps:
- 输出了结论：这次不是 Claude 单点故障，而是“Claude Code + DeepSeek 兼容 API + resume 历史”链路不一致。
- 建议了两条恢复路线：
  1) 先检查并修正环境变量/模型名；
  2) 不要继续 resume 损坏的旧 session，改为新会话读取任务文件和输出目录继续。
- 还提醒如果 thinking 相关报错持续出现，可以把 `MAX_THINKING_TOKENS` 临时改成 `0` 再重启。

Failures and how to do differently:
- 这次排查里使用了比较多的本机记忆和日志索引；未来若用户只想要“当前报错原因”，可以先短结论后再补证据，减少第一轮展开。

Reusable knowledge:
- 对于这种 400 错误，若日志同时出现模型名错误和 thinking 回传错误，优先判断为“恢复链路/配置问题”，而不是网络或鉴权失败。

References:
- 用户原始错误：`API Error: 400 {"error":{"message":"The \`content[].thinking\` in the thinking mode must be passed back to the API."...}}`
- 建议检查命令：`env | rg 'ANTHROPIC|CLAUDE|THINKING|DEEPSEEK'`
- 建议新开会话而不是 resume 的方式：`cd /Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code && claude`

