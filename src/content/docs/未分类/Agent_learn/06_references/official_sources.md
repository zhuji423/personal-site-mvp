---
title: "官方资料本地摘要"
description: "这页把几个最容易被写旧的外部资料压缩成本地笔记。适合在开始学习前先过一遍。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\06_references\\official_sources.md"
---
# 官方资料本地摘要

> 这页把几个最容易被写旧的外部资料压缩成本地笔记。适合在开始学习前先过一遍。

---

## 1. Docker Docs

来源：

- https://docs.docker.com/engine/containers/resource_constraints/

关键结论：

- `--memory-swap` 只有在同时设置了 `--memory` 时才有意义。
- 如果只设置 `--memory` 而不设置 `--memory-swap`，在宿主机支持 swap 的前提下，容器总的 memory+swap 通常约为 `2 x memory`。
- `--oom-kill-disable` 只有配合 `--memory` 使用才相对安全。

你读文档时重点看：

- hard limit vs soft limit
- `--memory` / `--memory-swap` / `--memory-reservation`
- OOM 行为和风险

---

## 2. SWE-bench 官方数据页

来源：

- https://www.swebench.com/SWE-bench/guides/datasets/

当前要记住的数字：

| 数据集 | 规模 |
|--------|------|
| Full | 2,294 |
| Lite | 534 |
| Verified | 500 |

学习建议：

- 日常快速实验先看 Lite。
- 对外汇报和高质量比较优先看 Verified。
- 要讲系统吞吐或大规模评测成本时再看 Full。

---

## 3. OpenRLHF 官方 README

来源：

- https://github.com/OpenRLHF/OpenRLHF

当前更准确的技术栈描述：

- Ray：分布式调度
- vLLM：高吞吐 rollout generation
- DeepSpeed：高效训练
- HuggingFace Transformers：模型接口与兼容层

不要再写成：

- “OpenRLHF = Megatron-LM + vLLM”

更适合的讲法是：

- “OpenRLHF 基于 Ray + vLLM + DeepSpeed + HF，重点在 RLHF 的分布式 orchestration 和高吞吐采样。”

---

## 4. HLE Nature 论文

来源：

- https://www.nature.com/articles/s41586-025-09962-4

当前要记住的事实：

- 论文发表于 **2026-01-28**
- HLE 是 **closed-ended academic benchmark**
- 公开题目规模是 **2,500**
- 题型是 **multiple-choice + exact-match short answer**
- 不是“开放式 essay + 专家主观评分”的 benchmark

---

## 5. 这些资料怎么用

推荐顺序：

1. 先看这页，建立当前事实基线。
2. 再看各周 `resources.md`，知道去哪读原始资料。
3. 最后回到 `00_core_concepts/`，把知识重新挂到“并发 / 复现 / 自动判分”主线上。
