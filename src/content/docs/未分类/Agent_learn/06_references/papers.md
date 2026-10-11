---
title: "本地论文摘要"
description: "这页不是论文原文替代品，而是本地速读摘要。目的是让你先在仓库里建立知识框架，再决定要不要去读原文。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\06_references\\papers.md"
---
# 本地论文摘要

> 这页不是论文原文替代品，而是本地速读摘要。目的是让你先在仓库里建立知识框架，再决定要不要去读原文。

---

## 1. PPO (2017)

- 原文: https://arxiv.org/abs/1707.06347
- 一句话: 用 clip 约束更新幅度，换取更稳定、更易实现的策略优化。
- 你要带走的点:
  - PPO 是 RLHF / RLVR 里最常见的基础算法之一。
  - 关键不是背公式，而是理解“为什么不能让策略一次更新太猛”。
  - 面试里通常会追问 clip、advantage、KL。

## 2. DeepSeekMath / GRPO (2024)

- 原文: https://arxiv.org/abs/2402.03300
- 一句话: 用组内相对比较替代 Critic，简化训练架构。
- 你要带走的点:
  - GRPO 很适合 reward 清晰的任务。
  - 少一个 Critic，意味着更省显存、更省系统复杂度。
  - 讲代码 RL 时，GRPO 是高频关键词。

## 3. SWE-Gym (2024)

- 原文: https://arxiv.org/abs/2410.04927
- 一句话: 把真实软件工程问题包装成一个可训练、可验证的 RL 环境。
- 你要带走的点:
  - 它更像环境设计论文，不只是算法论文。
  - Docker sandbox、测试执行、动作空间定义都值得看。

## 4. SWE-RL (2025)

- 原文: https://arxiv.org/abs/2502.12270
- 一句话: 展示如何在软件工程任务上用 RL 提升 agent 表现。
- 你要带走的点:
  - 适合把 benchmark、verifier、reward 和训练框架串起来看。
  - 读这篇时要重点看 reward 来自哪里、环境如何搭。

## 5. WebDancer (2025)

- 原文: https://arxiv.org/abs/2501.10928
- 一句话: 把多步搜索、阅读、总结建模成 agentic RL。
- 你要带走的点:
  - 长轨迹、稀疏奖励、信用分配是关键挑战。
  - 它和 Deep Research 场景非常贴近。

## 6. HLE Nature Paper (2026)

- 原文: https://www.nature.com/articles/s41586-025-09962-4
- 一句话: HLE 是一个 2,500 题的 closed-ended expert-level academic benchmark。
- 你要带走的点:
  - HLE 不是开放式主观评分 benchmark。
  - 题型是 multiple-choice + exact-match。
  - 它更适合讲 frontier evaluation，而不是直接等同于 open-ended research agent。
