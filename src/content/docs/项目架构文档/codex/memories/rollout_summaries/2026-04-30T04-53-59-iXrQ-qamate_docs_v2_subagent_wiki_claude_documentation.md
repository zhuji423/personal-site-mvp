---
title: "基于 Claude team/subagent 完成 `wiki_claude` 四份系统文档，并按修正范围只展开 Core 的 apismartmgt"
description: "Rollout context: 用户要求按照 /Users/zhujim4pro/.claude/plans/reflective-cuddling-firefly.md 分析当前相关代码库，并明确希望启用 Claude 的 subage"
date: "2026-05-05"
category: "项目架构文档"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-30T04-53-59-iXrQ-qamate_docs_v2_subagent_wiki_claude_documentation.md"
---
thread_id: 019ddcbc-9380-79e0-9424-adcf7486da5a
updated_at: 2026-04-30T06:00:57+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/30/rollout-2026-04-30T12-53-59-019ddcbc-9380-79e0-9424-adcf7486da5a.jsonl
cwd: /Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code
git_branch: kirin_batowl

# 基于 Claude team/subagent 完成 `wiki_claude` 四份系统文档，并按修正范围只展开 Core 的 apismartmgt

Rollout context: 用户要求按照 `/Users/zhuji_m4pro/.claude/plans/reflective-cuddling-firefly.md` 分析当前相关代码库，并明确希望启用 Claude 的 subagent 机制来实施计划。过程中先做只读扫描，确认计划范围、现有文档、真实代码路径和跨服务链路；后来按 `qamate-docs-v2` team 里的 writer prompts 分工执行，最终产出 4 份 Markdown 文档，全部位于 `/Users/zhuji_m4pro/code/baidu/qamate-strategy/apismart-code/wiki_claude/`。

## Task 1: 识别计划范围并确认可执行边界

Outcome: success

Preference signals:
- 用户先要求“帮我实施一下”，后又明确说“我希望你能够 ... 按照这个计划去分析一下当前的所有代码库” -> 后续类似任务应先做计划/范围核对，再进入写作或改动，而不是默认直接改文件。
- 用户又补充“/subagents 帮我启用subagent 去实施上面的计划 ... 具体的agent 按照 Claude 的 subagent 去实习” -> 说明他们接受并偏好通过 Claude team/subagent 分工来执行大范围文档/分析任务。

Key steps:
- 读取 `/Users/zhuji_m4pro/.claude/plans/reflective-cuddling-firefly.md`，发现它是“系统文档化与架构分析 - 实施计划”，目标是 4 份 Markdown Wiki 文档，且 Core 范围后来修正为只分析 `apismartmgt`。
- 先用 `rg`、`find`、`nl -ba` 核对真实代码路径，纠正计划里一些漂移路径：例如 `FeignConfig.java` 真实位置在 `core/apismartmgt/manager/FeignConfig.java`，executor 的 Runner 在 `runner/impl`，dispatch 的调度线程在 `scheduler/thread`。
- 识别出 `qamate-docs-v2` team 的 3 个 writer subagent：`arch-writer`、`topo-writer`、`manual-writer`，并确认 `team-lead` 无 prompt。

Failures and how to do differently:
- 计划里多处路径已过时或拼写漂移，不能直接信任计划文本；必须先用 `rg --files` / `rg -n` / `nl -ba` 反查真实路径和行号。
- 一开始对范围有冲突（前后两版计划混在一起），后来通过“Core 只展开 apismartmgt，其余模块照常”的修正范围解决；以后遇到类似计划冲突，先冻结边界再分工。

Reusable knowledge:
- `qamate-docs-v2` team 的 writer prompt 直接保存在 `/Users/zhuji_m4pro/.claude/teams/qamate-docs-v2/config.json` 的 `members[1..3].prompt`。
- 真正的执行记录在 `/Users/zhuji_m4pro/.claude/projects/-Users-zhuji-m4pro-code-baidu-qamate-strategy-apismart-code/76982603-9441-4753-8fa1-cb5393666c82.jsonl` 和对应 `subagents/` 目录。

References:
- [1] `qamate-docs-v2` team config: `members[1].prompt`=`arch-writer`, `members[2].prompt`=`topo-writer`, `members[3].prompt`=`manual-writer`
- [2] 计划修正后的核心边界：Core 只展开 `baidu/qamate-server/core/src/main/java/com/baidu/qamate/core/apismartmgt/**`
- [3] 真实路径反查结果：executor Runner 在 `baidu/qamate-server/apiExecutor/executor-server/src/main/java/com/baidu/qamate/server/runner/impl/`，dispatch 调度线程在 `.../scheduler/thread/`

## Task 2: 使用 Claude subagent 实施三份主文档并补总索引

Outcome: success

Preference signals:
- 用户明确要求“按 Claude 的 subagent 去实施” -> 后续大文档/多文档任务应优先分派为多个写作 agent，各自只改自己的目标文件。
- 用户接受“本地协调 + subagent 写作 + 最后补索引”的方式；这种 workflow 以后可以默认用于多文档、跨模块的整理任务。

Key steps:
- 创建 `wiki_claude/` 目录后，启动三个 writer subagent，分别只允许写自己的目标文件：
  - `arch-writer@qamate-docs-v2` → `wiki_claude/ARCHITECTURE_DEEP_DIVE.md`
  - `topo-writer@qamate-docs-v2` → `wiki_claude/SYSTEM_TOPOLOGY_AND_LIFECYCLE.md`
  - `manual-writer@qamate-docs-v2` → `wiki_claude/DEVELOPER_MAINTENANCE_MANUAL_FULL.md`
- 主控最后补写 `wiki_claude/DOCUMENTATION_INDEX.md`，把四份文档的用途、阅读顺序、问题到文档映射、风险和维护护栏串起来。
- 做了最后的只读验收：检查章节标题、Mermaid、正反合结构、敏感信息脱敏提示、文件大小和行数。

Failures and how to do differently:
- 有一次结构扫描命令因 shell 引号写法失败，但不影响产物；以后校验命令尽量用更简单的 `rg` 和单引号，减少 shell 转义错误。
- `git status` 显示仓库里原本就有大量未跟踪/修改项，所以后续交付时应重点说明“本轮新增集中在 `wiki_claude/`”，避免把历史噪音算成本轮改动。

Reusable knowledge:
- 最终新增了 4 个文档，合计约 1212 行、约 123KB：`ARCHITECTURE_DEEP_DIVE.md`、`SYSTEM_TOPOLOGY_AND_LIFECYCLE.md`、`DEVELOPER_MAINTENANCE_MANUAL_FULL.md`、`DOCUMENTATION_INDEX.md`。
- 三个 writer subagent 的完成状态都明确说明：只写自己的目标 Markdown 文件，未改业务代码。

References:
- [1] `wiki_claude/ARCHITECTURE_DEEP_DIVE.md`（约 28KB，276 行）
- [2] `wiki_claude/SYSTEM_TOPOLOGY_AND_LIFECYCLE.md`（约 37KB，361 行）
- [3] `wiki_claude/DEVELOPER_MAINTENANCE_MANUAL_FULL.md`（约 48KB，425 行）
- [4] `wiki_claude/DOCUMENTATION_INDEX.md`（约 9KB，150 行）
- [5] 关键验收：三份正文都包含 `Thinking Process`、Mermaid、正反合 + 反事实、源码路径与行号引用

## Task 3: 文档内容的稳定模式与可复用结论

Outcome: success

Preference signals:
- 用户在多轮里持续要求“按计划分析所有代码库”，并接受我先只读核对、后分工实施 -> 说明他们更关心证据型、可追溯的系统文档，而不是即时口头概述。
- 用户没有要求写成中文/英文切换或改写风格，且对“面向完全不懂后端”的叙述方式没有反对，说明后续类似任务可默认采用低门槛解释 + 证据引用的风格。

Reusable knowledge:
- 这次文档形成了稳定写法：每份文档都包含 `Thinking Process` 开篇、首次概念解释用“正面 / 反面 / 反事实 / 合 / 本系统中的实例”、并在后续用 `（见 §...）` 回指。
- Core 文档的正确范围是 `apismartmgt`，而不是整个 `core`；其他 Core 业务域只在确有跨服务依赖时作为背景或外部依赖出现。
- 文档中对敏感配置采用“只写位置、不复写值”的方式，特别是 `FeignConfig`、`application-dev.yml`、`application-prod.properties`、`DesCbcDecryptorUtil` 这些风险点。

Failures and how to do differently:
- 计划文本与真实代码路径存在偏差，说明后续此类系统文档任务必须先做路径核对，再写章节；不能把计划中的包名/路径直接当事实。
- 某些章节里出现了重复或较长的引用列表，后续若做二次迭代，可优先保留高价值引用、压缩重复表述，减少文档噪音。

References:
- `ARCHITECTURE_DEEP_DIVE.md` 的结构：全局架构图景、核心业务流向、隐性依赖与副作用、设计模式、TOP 风险
- `SYSTEM_TOPOLOGY_AND_LIFECYCLE.md` 的结构：全景拓扑、核心技术栈、目录地图、启动生命周期
- `DEVELOPER_MAINTENANCE_MANUAL_FULL.md` 的结构：全库知识索引、关键类定义表、配置项释义字典、复杂函数拆解、常见维护动作
- `DOCUMENTATION_INDEX.md` 的结构：产物清单、阅读顺序、问题映射、风险总览、维护护栏

