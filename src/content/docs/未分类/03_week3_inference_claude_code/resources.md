---
title: "Week 3 资源链接汇总"
description: "- GitHub: https://github.com/vllm-project/vllm - 文档: https://docs.vllm.ai/ - 定位: 最流行的 LLM 推理引擎，PagedAttention 和 Continuo"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\03_week3_inference_claude_code\\resources.md"
---
# Week 3 资源链接汇总

---

## 推理引擎

### 1. vLLM

- **GitHub**: https://github.com/vllm-project/vllm
- **文档**: https://docs.vllm.ai/
- **定位**: 最流行的 LLM 推理引擎，PagedAttention 和 Continuous Batching 的开创者
- **特点**: 高吞吐量、低延迟、易于部署

**关键文件说明**:

| 路径 | 作用 |
|------|------|
| `vllm/core/scheduler.py` | 请求调度（continuous batching） |
| `vllm/core/block_manager.py` | KV Cache 块管理（PagedAttention） |
| `vllm/attention/paged_attention.py` | PagedAttention 核心实现 |
| `vllm/attention/selector.py` | Attention kernel 选择 |
| `vllm/worker/worker.py` | Worker 主循环 |
| `vllm/worker/model_runner.py` | 模型推理执行 |
| `vllm/engine/llm_engine.py` | LLM 引擎入口 |
| `vllm/engine/arg_utils.py` | 参数配置 |
| `vllm/entrypoints/openai/api_server.py` | OpenAI 兼容 API |
| `vllm/entrypoints/api_server.py` | 原生 API |
| `vllm/model_executor/model_loader.py` | 模型加载 |
| `benchmarks/latency.py` | 延迟测试 |
| `benchmarks/throughput.py` | 吞吐量测试 |
| `examples/offline_inference.py` | 离线推理示例 |
| `examples/api_client.py` | API 调用示例 |

**推荐阅读顺序**:
1. `vllm/engine/llm_engine.py` — 理解引擎的整体工作流程
2. `vllm/core/scheduler.py` — 理解 Continuous Batching 的调度逻辑
3. `vllm/core/block_manager.py` — 理解 PagedAttention 的块管理
4. `vllm/attention/paged_attention.py` — 理解 PagedAttention 的 CUDA kernel

**核心论文**:
- vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention (SOSP 2023)
  https://arxiv.org/abs/2309.06180

### 2. SGLang

- **GitHub**: https://github.com/sgl-project/sglang
- **文档**: https://docs.sglang.ai/
- **定位**: 面向 Agent 场景的推理引擎，Prefix Caching 最佳实现
- **特点**: RadixAttention、灵活的编程接口、高性能

**关键文件说明**:

| 路径 | 作用 |
|------|------|
| `sglang/srt/layers/radix_attention.py` | RadixAttention 实现 |
| `sglang/srt/models/model_runner.py` | 模型推理执行 |
| `sglang/srt/server.py` | 服务器入口 |
| `sglang/srt/scheduler.py` | 调度器 |
| `sglang/srt/mem_cache/memory_pool.py` | 内存池管理 |
| `sglang/backend/runtime.py` | 运行时 |
| `docs/backend/vllm_backend.md` | SGLang + vLLM 集成 |
| `examples/agent_example.py` | Agent 场景示例 |

**推荐阅读顺序**:
1. `sglang/srt/layers/radix_attention.py` — 理解 RadixAttention 的实现
2. `sglang/srt/server.py` — 理解服务器的工作流程
3. `sglang/srt/scheduler.py` — 理解调度逻辑
4. `sglang/srt/mem_cache/memory_pool.py` — 理解内存池管理

**核心论文**:
- SGLang: Efficient Execution of Structured Language Model Programs
  https://arxiv.org/abs/2312.11570

### 3. TensorRT-LLM

- **GitHub**: https://github.com/NVIDIA/TensorRT-LLM
- **文档**: https://nvidia.github.io/TensorRT-LLM/
- **定位**: NVIDIA 官方的高性能推理引擎，极致优化
- **特点**: 最快的推理速度（在 NVIDIA GPU 上）、支持各种量化方式

**关键文件说明**:

| 路径 | 作用 |
|------|------|
| `tensorrt_llm/models/` | 各模型实现 |
| `tensorrt_llm/runtime/model.py` | 模型运行时 |
| `tensorrt_llm/runtime/generation.py` | 生成逻辑 |
| `tensorrt_llm/layers/attention.py` | Attention 层优化 |
| `tensorrt_llm/quantization/quantize.py` | 量化工具 |
| `tensorrt_llm/quantization/fp8.py` | FP8 量化 |
| `benchmarks/` | 性能基准测试 |
| `examples/` | 使用示例 |

### 4. llama.cpp

- **GitHub**: https://github.com/ggerganov/llama.cpp
- **定位**: CPU 推理引擎，适合在消费级硬件上运行
- **特点**: GGUF 格式、CPU/GPU 混合推理、极低的资源需求
- **相关**: Ollama (https://github.com/ollama/ollama) 基于 llama.cpp 的易用封装

---

## Claude Code 相关资源

### Claude Code 官方文档

- **Claude Code 文档**: https://docs.anthropic.com/en/docs/claude-code
- **Claude Code Hooks**: https://docs.anthropic.com/en/docs/claude-code/hooks
- **Claude Code Settings**: https://docs.anthropic.com/en/docs/claude-code/settings

### Claude Code 相关技术分析

- **Anthropic Engineering Blog**: https://www.anthropic.com/engineering
- **Claude API 文档**: https://docs.anthropic.com/en/docs/about-claude/models

### 类似系统（对比参考）

- **Aider** (AI 编程助手): https://github.com/paul-gauthier/aider
- **Cursor** (AI IDE): https://cursor.sh/
- **Cline** (VS Code Agent): https://github.com/cline/cline

---

## 推理优化学习资源

### 入门级

1. **vLLM 官方文档的 "Architecture" 章节**
   - 链接: https://docs.vllm.ai/en/latest/design/architecture.html
   - 特点: 最清晰的 PagedAttention 和 Continuous Batching 解释

2. **LMSYS Org 的推理教程**
   - 链接: https://lmsys.org/blog/2024-01-17-anthropic-vllm/
   - 特点: 实际的推理引擎对比和性能分析

### 进阶级

3. **"The Paged Attention Paper" (vLLM)**
   - 链接: https://arxiv.org/abs/2309.06180
   - 特点: PagedAttention 的原始论文，必读

4. **"Orca: A Distributed Serving System for Transformer-Based Generative Models"**
   - 链接: https://arxiv.org/abs/2304.14128
   - 特点: Continuous Batching 的原始论文

5. **"SGLang: Efficient Execution of Structured Language Model Programs"**
   - 链接: https://arxiv.org/abs/2312.11570
   - 特点: RadixAttention 的原始论文

### 工程实践

6. **vLLM 的性能调优指南**
   - 链接: https://docs.vllm.ai/en/latest/serving/engine_args.html
   - 特点: 实际部署时的参数调优建议

7. **Triton Inference Server 文档**
   - 链接: https://docs.nvidia.com/deeplearning/triton-inference-server/
   - 特点: NVIDIA 的推理服务部署平台

---

## RL 训练资源 (Week 2 延伸)

### 推理引擎在 RL 训练中的应用

- **verl 使用 vLLM 做 rollout 生成**
  - 链接: https://github.com/volcengine/verl/tree/main/verl/workers/rollout
  - 特点: 展示了推理引擎如何集成到 RL 训练流程中

- **OpenRLHF 使用 vLLM 做 rollout**
  - 链接: https://github.com/OpenRLHF/OpenRLHF/blob/main/openrlhf/trainer/ppo_trainer.py
  - 特点: PPO 训练中的 vLLM 集成

---

## 工具和实用资源

### Token 计数器

- **tiktoken** (OpenAI): https://github.com/openai/tiktoken
- **Anthropic Tokenizer**: https://github.com/anthropics/anthropic-sdk-python

### 性能监控

- **NVIDIA Nsight Systems**: GPU 性能分析
- **PyTorch Profiler**: 训练和推理性能分析
- **torch.cuda.memory_summary()**: GPU 内存使用分析

### 推理成本计算器

- **Anthropic Pricing**: https://docs.anthropic.com/en/docs/about-claude/pricing
- **OpenAI Pricing**: https://openai.com/pricing

→ 参见 [../02_week2_rl_verification/resources.md](../02_week2_rl_verification/resources.md) 了解 RL 训练资源
→ 参见 [../README.md](../README.md) 了解整体学习路线
