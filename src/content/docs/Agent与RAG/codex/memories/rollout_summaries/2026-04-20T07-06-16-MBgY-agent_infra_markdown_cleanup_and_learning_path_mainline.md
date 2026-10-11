---
title: "先审查再改写：修复学习路线 Markdown 的断链、事实偏差和图表渲染，并提炼一条贯穿 Week 0-5 的主线"
description: "Rollout context: 工作区在 /Users/zhujim4pro/Agentlearn。用户先要求“检查所有 md 文件是否有问题，找出问题并给计划，不要修改”，随后又明确“开始修改”；最后又要求把当前每一周内容整理成一条能穿"
date: "2026-05-05"
category: "Agent与RAG"
source: "F:\\百度工作\\07_codex_cloud_data_sensitive\\.codex\\memories\\rollout_summaries\\2026-04-20T07-06-16-MBgY-agent_infra_markdown_cleanup_and_learning_path_mainline.md"
---
thread_id: 019da9b6-1972-7761-9138-d8cd8a15e7f0
updated_at: 2026-04-20T08:56:22+00:00
rollout_path: /Users/zhuji_m4pro/.codex/sessions/2026/04/20/rollout-2026-04-20T15-06-16-019da9b6-1972-7761-9138-d8cd8a15e7f0.jsonl
cwd: /Users/zhuji_m4pro/Agent_learn

# 先审查再改写：修复学习路线 Markdown 的断链、事实偏差和图表渲染，并提炼一条贯穿 Week 0-5 的主线

Rollout context: 工作区在 `/Users/zhuji_m4pro/Agent_learn`。用户先要求“检查所有 md 文件是否有问题，找出问题并给计划，不要修改”，随后又明确“开始修改”；最后又要求把当前每一周内容整理成一条能穿起来的主线。整个过程没有 Git 仓库可用，修改是在工作区直接完成并通过扫描回归验证。

## Task 1: 审查并整改全仓 Markdown（结构、事实、图表格式）

Outcome: success

Preference signals:
- 用户先说“帮我检查一下这个文件下面的所有md文件…给我一个计划，不要修改” -> 说明这类任务他希望先看到问题清单和整改计划，再决定是否动文件，适合先审查后改写。
- 用户补充“里面的图表md格式都有问题，都需要修改的，让我学习的内容你也应该爬到本地让我看” -> 说明他不只关心内容正确性，也关心 Markdown 渲染可读性和本地可学习性；后续应默认检查图表渲染、目录结构和本地资料落地。
- 用户直接说“开始修改” -> 说明在给出计划后，他会接受按计划落地修改，不需要反复确认每一处小改动。

Key steps:
- 先做全仓枚举和相对链接检查，确认不是只看某几个文件，而是整个学习路线仓库。
- 用脚本校验内部链接、缺失引用、未闭合 code fence，确认问题主要集中在断链、事实过时、和大量 ASCII 框图/目录树的 Markdown 可读性。
- 把入口文档和资源页里的树状目录、代码块式目录树改成 Markdown 表格和条目列表。
- 将 Week 4 里最重的结构图、流程图、对比图改成 Mermaid flowchart 或 Markdown 表格，尤其是 `five_layer_optimization.md`、`architecture_comparison.md`、`gaia_browsecomp.md`。
- 顺手修正了 Week 2 里 OpenRLHF 的过时技术栈表述；把它从“Megatron-LM + vLLM”更新为更接近官方 README 的“Ray + vLLM + DeepSpeed + HuggingFace Transformers”。
- 校验通过后再确认：全仓相对链接无 broken link、fence 配对正常、box-drawing 字符残留扫描无命中。

Failures and how to do differently:
- 一开始把“图表难读”当成主要问题，后面扫描后发现真正的大头是“代码块里的终端风格框图”而不是普通表格；后续如果再遇到类似仓库，应该先做全仓字符扫描和链接扫描，再决定改造重点。
- 有些文件最初只改了入口和资源页，后来发现 Week 4 的两个重文档（`architecture_comparison.md`、`five_layer_optimization.md`）才是最需要系统性重构的地方；后续类似任务应优先处理“信息密度最高且最常被阅读”的长文档。
- 用户明确要求“不要修改”后才给计划，说明如果先行动会触发不必要的返工；后续同类任务应先给计划，再执行。

Reusable knowledge:
- Markdown 学习路线文档中，树状目录和大型结构图不适合长期放在 fenced code block 里；更稳妥的做法是：目录树改表格，流程图改 Mermaid，概念对比改表格，伪代码才保留 code block。
- Week 4 的 Deep Research / Benchmark 文档最容易堆积框图和大段结构说明，适合用 Mermaid flowchart 和分类表格替代 ASCII 框图。
- `OpenRLHF` 在当前文本里应按更接近官方 README 的技术栈描述，而不是旧的“Megatron-LM + vLLM”版本；这类框架说明容易过时，最好同步到官方来源。
- 经过回归脚本验证，本次工作区里没有 broken relative links，也没有未闭合的 fenced code blocks。

References:
- [1] 入口文档批量改写：`01_week1_docker/resources.md`, `02_week2_rl_verification/README.md`, `02_week2_rl_verification/resources.md`, `02_week2_rl_verification/papers/paper_list.md`, `03_week3_inference_claude_code/README.md`, `03_week3_inference_claude_code/resources.md`, `04_week4_eval_deep_research/README.md`
- [2] 图表/结构重构：`04_week4_eval_deep_research/benchmarks/gaia_browsecomp.md`, `04_week4_eval_deep_research/deep_research/architecture_comparison.md`, `04_week4_eval_deep_research/deep_research/five_layer_optimization.md`
- [3] 校验结果：全仓相对链接检查输出 `NO_BROKEN_REL_LINKS`，code fence 检查输出 `NO_ODD_FENCES`，box-drawing 字符扫描最终无命中
- [4] 用户原话：`“里面的图表md格式都有问题，都需要修改的，让我学习的内容你也应该爬到本地让我看”`

## Task 2: 提炼 Week 0-5 的主线并重排学习顺序

Outcome: success

Preference signals:
- 用户说“帮我整理一下当前每一周的内容，我觉得太散乱了，有没有一条主线能穿起来” -> 说明他希望学习路径不是并列堆叠，而是有一条贯穿始终的工程主线，后续输出应该优先给“总线索”和“每周在总线索里的位置”。
- 这也暗示他更偏好“问题 -> 机制 -> 工程闭环 -> 评测/面试表达”的结构化叙事，而不是按章节机械罗列。

Key steps:
- 把全路线概括为：把“一个 Agent 任务”做成“可运行、可训练、可加速、可评测、可讲清”的工程闭环。
- 将 Week 0 定位为岗位视角和工程视角的起点，Week 1 到 Week 4 依次对应“能跑起来 -> 能学会变好 -> 能跑得更快更省 -> 能量化比较”，Week 5 则是把闭环讲成面试故事。
- 给出建议的阅读顺序和每周入口路径，按“问题、答案、产出”串联，而不是散点浏览。

Failures and how to do differently:
- 用户觉得“太散乱”，说明单纯的周目录并不足以形成心智模型；以后如果再整理路线，应该默认输出一条中心命题和一张总览图，而不是只给目录摘要。
- Week 4 的内容跨度最大，包含 benchmark、infra、Deep Research 优化和面试表达；后续类似路线最好明确把它拆成“评测标准”和“系统优化”两层，不然读起来容易发散。

Reusable knowledge:
- 这套学习路线可以用一个统一主线串起来：`执行环境 -> 训练闭环 -> 推理优化 -> 评测闭环 -> 面试表达`。
- 每周的角色建议如下：
  - Week 0：定义岗位与工程视角
  - Week 1：隔离、复现、并发，让任务先稳定跑起来
  - Week 2：rollout -> reward -> update，让模型学会变好
  - Week 3：Prefill/Decode、KV Cache、batching、SubAgent，让系统跑得更快更省
  - Week 4：benchmark、pipeline、Deep Research 五层优化，让结果可量化可比较
  - Week 5：项目重讲、白板图、自检，把工程闭环讲清楚

References:
- [1] 用户原话：`“帮我整理一下当前每一周的内容，我觉得太散乱了，有没有一条主线能穿起来”`
- [2] 回答中给出的主线表述：`“把‘一个 Agent 任务’做成‘可运行、可训练、可加速、可评测、可讲清’的工程闭环”`
- [3] 建议的阅读入口：`00_core_concepts/position_overview.md`, `00_core_concepts/mindset.md`, `01_week1_docker/README.md`, `02_week2_rl_verification/README.md`, `03_week3_inference_claude_code/README.md`, `04_week4_eval_deep_research/README.md`, `05_interview_prep/project_reframing.md`
