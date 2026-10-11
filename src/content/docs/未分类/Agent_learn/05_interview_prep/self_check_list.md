---
title: "自检清单"
description: "- 我能解释 rollout / harness / verifier / reward 的区别。 - 我能用一句话说明 Agent Infra 工程师和应用工程师的差别。 - 我能讲清楚为什么“并发、复现、自动判分”是主线。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\05_interview_prep\\self_check_list.md"
---
# 自检清单

---

## 1. 核心概念

- 我能解释 `rollout / harness / verifier / reward` 的区别。
- 我能用一句话说明 Agent Infra 工程师和应用工程师的差别。
- 我能讲清楚为什么“并发、复现、自动判分”是主线。

## 2. Docker 与执行环境

- 我能说明 namespace 和 cgroups 分别解决什么问题。
- 我能解释为什么 warm pool 能显著提升吞吐。
- 我能说清楚 Copy-on-Write 和环境复用的关系。

## 3. RL 与 verifier

- 我能完整讲出 `rollout -> reward -> update`。
- 我能解释 PPO 和 GRPO 的关键差异。
- 我能说明 verifier 出错会带来什么系统性后果。

## 4. 推理与调度

- 我能解释 prefill / decode 的不同瓶颈。
- 我能说明 KV cache 为什么是 decode 阶段的核心资产。
- 我能给出一个 batching / scheduling 的基本优化思路。

## 5. Eval 与 benchmark

- 我能解释 SWE-bench、HLE、GAIA 各自测什么。
- 我能说明为什么不同 benchmark 需要不同 infra。
- 我能说出评测系统里最值得优先优化的环节。

## 6. 项目表达

- 我有没有把项目讲成系统，而不是功能列表？
- 我有没有给出具体的工程指标？
- 我有没有明确说出瓶颈、权衡和收益？
