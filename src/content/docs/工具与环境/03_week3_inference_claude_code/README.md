---
title: "Week 3: 推理引擎与 Claude Code 架构"
description: "本周定位：理解 LLM 推理的性能瓶颈和优化手段，并深入理解 Claude Code 的工程架构。Agent Infra 工程师的核心工作之一就是让模型推理「又快又省」。"
date: "2026-04-20"
category: "工具与环境"
source: "D:\\mac_m4\\Agent_learn\\03_week3_inference_claude_code\\README.md"
---
# Week 3: 推理引擎与 Claude Code 架构

> **本周定位**：理解 LLM 推理的性能瓶颈和优化手段，并深入理解 Claude Code 的工程架构。Agent Infra 工程师的核心工作之一就是让模型推理「又快又省」。

---

## 本周目标

学完本周内容后，你应该能够：

1. **讲清 Prefill vs Decode 的性能差异**：为什么 decode 是 memory-bound，怎么优化
2. **理解 KV Cache 的原理和内存占用**：能手算一个模型的 KV Cache 大小
3. **对比各种 Batching 策略**：Static → Dynamic → Continuous → Prefix Caching
4. **画出 Claude Code 的架构图**：理解 REPL、Tool Registry、Context Manager 的角色
5. **解释 SubAgent 的进程模型**：独立进程、独立上下文、并行执行

### 核心思维模型

LLM 推理的本质可以压缩成三句话：

- 输入 token 经过 Embedding 和多层 Transformer，最终得到下一个 token 的概率分布。
- 推理优化的目标是让这些矩阵乘法跑得更快，同时占用更少显存。
- 推理引擎本质上是一个精心设计的矩阵乘法调度器。

---

## 学习路径

1. Day 1-2: [inference/prefill_decode.md](inference/prefill_decode.md) 和 [inference/kv_cache.md](inference/kv_cache.md)，先把 Prefill / Decode 与 KV Cache 的底层机制讲清。
2. Day 3-4: [inference/batching_strategies.md](inference/batching_strategies.md)，理解 Static / Dynamic / Continuous 等调度策略。
3. Day 5-7: 依次阅读 [claude_code/architecture.md](claude_code/architecture.md)、[claude_code/task_tool_subagent.md](claude_code/task_tool_subagent.md)、[claude_code/hooks_lifecycle.md](claude_code/hooks_lifecycle.md)、[claude_code/context_compaction.md](claude_code/context_compaction.md)，把 Claude Code 的整体架构串起来。

---

## 必读框架源码

### vLLM

| 路径 | 作用 |
|------|------|
| `vllm/core/scheduler.py` | 请求调度 |
| `vllm/core/block_manager.py` | KV Cache 块管理 |
| `vllm/attention/paged_attention.py` | PagedAttention 实现 |
| `vllm/worker/worker.py` | Worker 主循环 |
| `vllm/engine/llm_engine.py` | LLM 引擎入口 |
| `benchmarks/` | 性能基准测试 |
| `examples/` | 使用示例 |

### SGLang

| 路径 | 作用 |
|------|------|
| `sglang/srt/layers/radix_attention.py` | RadixAttention 实现 |
| `sglang/srt/server.py` | 服务器入口 |
| `sglang/srt/scheduler.py` | 调度器 |
| `sglang/backend/runtime.py` | 运行时 |

---

## 产出要求

1. **性能分析报告**：选择一个模型（如 Llama 7B），计算其在不同 context length 下的 KV Cache 大小、Prefill/Decode 的理论吞吐量
2. **架构图**：手绘 Claude Code 的架构图，标注每个组件的职责
3. **优化方案**：给定一个推理场景（如 100 并发请求、平均 4K 输入 512 输出），给出你的推理引擎配置建议

---

## 与其他章节的关联

- **Week 2 (RL)**：RL 训练中的 rollout 生成就是推理 → 参见 [../02_week2_rl_verification/README.md](../02_week2_rl_verification/README.md)
- **Week 4 (Eval)**：推理引擎的性能直接影响评估的吞吐量和成本 → 参见 [../04_week4_eval_deep_research/README.md](../04_week4_eval_deep_research/README.md)

---

## 面试高频问题

### Q1: LLM 推理的主要瓶颈是什么？

**A**: LLM 推理有两个截然不同的阶段，各有不同的瓶颈：

1. **Prefill 阶段（compute-bound）**：一次性处理所有输入 token，矩阵乘法的计算量大，GPU 计算单元利用率高
2. **Decode 阶段（memory-bound）**：每步只生成一个 token，矩阵很小，但需要从 HBM 读取整个 KV Cache，GPU 计算单元大量闲置

Decode 阶段是实际部署中的主要瓶颈，因为大部分请求的 decode 时间远超 prefill 时间。各种推理优化（KV Cache 优化、Continuous Batching、Speculative Decoding）都是针对 decode 阶段的。

### Q2: 你觉得 vLLM 和 SGLang 各有什么优势？

**A**:

**vLLM**:
- PagedAttention 是开创性的工作，解决了 KV Cache 的内存碎片问题
- 生态最成熟，社区最大
- Continuous Batching 支持最好

**SGLang**:
- RadixAttention 是 Prefix Caching 的最佳实现，通过 Radix Tree 共享 KV Cache
- 在多轮对话和 Agent 场景下，Prefix Caching 带来的加速非常显著
- 编程接口更灵活（支持复杂的 Agent 逻辑）

选择建议：如果是标准推理服务，vLLM 更稳定；如果涉及大量 Agent 场景（共享 system prompt），SGLang 的 Prefix Caching 优势更大。

### Q3: Claude Code 为什么选择当前这种架构？和 LangChain 有什么区别？

**A**: Claude Code 的架构核心设计原则是「简洁、可靠、可扩展」：

1. **简洁**：REPL 主循环 + Tool Registry，没有过度抽象
2. **可靠**：权限系统、错误恢复、上下文管理都是内建的
3. **可扩展**：通过 Hook 和 Skill 机制扩展，不修改核心逻辑

与 LangChain 的区别：
- LangChain 是一个通用的 LLM 应用框架，支持各种 Agent 模式、Memory、Chain
- Claude Code 是一个专业的编程助手，专注于代码生成、工具调用、文件操作
- Claude Code 的架构更专注、更深层优化（如上下文压缩、并行 SubAgent），而 LangChain 更通用但更浅层

本质上，Claude Code 选择的是「深度优化一个场景」而非「支持所有场景」的架构哲学。

---

## 详细学习笔记

- [Prefill vs Decode 瓶颈](inference/prefill_decode.md)
- [KV Cache 原理](inference/kv_cache.md)
- [Batching 策略](inference/batching_strategies.md)
- [Claude Code 架构](claude_code/architecture.md)
- [Task Tool (SubAgent)](claude_code/task_tool_subagent.md)
- [Hook 生命周期](claude_code/hooks_lifecycle.md)
- [Context 压缩策略](claude_code/context_compaction.md)
