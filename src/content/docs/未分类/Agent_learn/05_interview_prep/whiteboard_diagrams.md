---
title: "白板图清单"
description: "目标：面试时优先画能体现 infra 思维的图，不画纯产品流程图。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\05_interview_prep\\whiteboard_diagrams.md"
---
# 白板图清单

> 目标：面试时优先画能体现 infra 思维的图，不画纯产品流程图。

---

## 1. Agent 基础闭环

```mermaid
flowchart LR
    A[Policy / Model] --> B[Rollout]
    B --> C[Environment / Sandbox]
    C --> D[Verifier / Judge]
    D --> E[Reward / Score]
    E --> F[Update or Ranking]
```

适用场景：

- 讲 RL / verifier
- 讲评测系统
- 讲 agent execution loop

---

## 2. Docker 验证环境

```mermaid
flowchart TD
    A[Task Queue] --> B[Scheduler]
    B --> C[Warm Container Pool]
    C --> D[Checkout / Apply Patch]
    D --> E[Run Tests]
    E --> F[Collect Logs and Results]
```

适用场景：

- 讲 SWE-bench
- 讲 rollout 验证
- 讲并发执行环境

---

## 3. Deep Research 五层图

```mermaid
flowchart TD
    A[I/O Cache] --> B[Scheduler]
    B --> C[Inference Engine]
    C --> D[Algorithm / Search]
    D --> E[Environment Reuse]
```

适用场景：

- 讲 deep research 优化
- 讲端到端性能分析

---

## 4. 推理吞吐图

```mermaid
flowchart LR
    A[Incoming Requests] --> B[Batching / Scheduling]
    B --> C[Prefill]
    C --> D[KV Cache]
    D --> E[Decode]
    E --> F[Responses]
```

适用场景：

- 讲 vLLM / continuous batching
- 讲 inference bottleneck

---

## 5. 评测 Pipeline

```mermaid
flowchart LR
    A[Benchmark Dataset] --> B[Dispatcher]
    B --> C[Execution Sandbox]
    C --> D[Judge]
    D --> E[Metrics Aggregator]
```

适用场景：

- 讲 benchmark infra
- 讲自动判分和报告生成
