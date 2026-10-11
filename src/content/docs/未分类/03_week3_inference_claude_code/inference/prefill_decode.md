---
title: "Prefill vs Decode：LLM 推理的两个阶段"
description: "核心问题：为什么同一块 GPU，处理不同类型的请求时性能差距巨大？为什么长 prompt 场景下首字延迟很高？为什么模型越大、batch 越大时 decode 阶段反而越容易拖后腿？答案都藏在 prefill 和 decode 这两个阶段的"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\03_week3_inference_claude_code\\inference\\prefill_decode.md"
---
# Prefill vs Decode：LLM 推理的两个阶段

> **核心问题**：为什么同一块 GPU，处理不同类型的请求时性能差距巨大？为什么长 prompt 场景下首字延迟很高？为什么模型越大、batch 越大时 decode 阶段反而越容易拖后腿？答案都藏在 prefill 和 decode 这两个阶段的本质差异中。

---

## 1. LLM 推理的完整流程

一条 LLM 请求的完整生命周期分为两个截然不同的阶段：

```
用户输入 tokens ──────────────────────────────────────────────────────┐
                                                                    │
  [Prefill 阶段]  一次性并行处理全部输入 ──→ 生成 KV Cache            │
                                                                    │
  [Decode 阶段]   逐个生成输出 token ──→ 每步读取 KV Cache ──→ 输出   │
```

这两个阶段在计算模式、资源瓶颈、优化方向上完全不同，理解这种差异是推理系统优化的前提。

---

## 2. Prefill 阶段详解

### 2.1 什么是 Prefill

> **Prefill**: 推理的第一阶段，将输入 token 序列一次性并行计算，生成 KV Cache

Prefill 阶段的核心任务是：把用户发送的所有输入 token（system prompt + 用户消息 + 历史对话等）一次性送入模型，并行完成所有 Transformer 层的前向传播计算。

具体过程：

1. **Embedding**: 将输入的 N 个 token 转为 N 个向量，shape 为 `(N, d_model)`
2. **逐层前向传播**: 经过 L 层 Transformer，每层包含 Self-Attention 和 FFN
3. **Attention 计算**: 对 N 个 token 做完整的 self-attention，每个 token 都要 attend to 所有 token
4. **生成 KV Cache**: 将每层的 Key 和 Value 矩阵保存下来，供 decode 阶段复用
5. **产出 logits**: 取最后一个 token 的 hidden state，经过 LM head 输出词表概率分布

关键特征：所有输入 token 是**并行处理**的，GPU 的一次 forward pass 就能完成全部计算。

### 2.2 KV Cache 的生成

> **KV Cache**: Transformer Attention 层中缓存的 Key 和 Value 矩阵，避免 decode 阶段重复计算历史 token

在 Prefill 结束后，每层 Attention 都会保存两个矩阵：

| 缓存项 | Shape | 说明 |
|--------|-------|------|
| Key Cache | `(num_layers, num_heads, N, head_dim)` | N 个输入 token 的 Key 投影 |
| Value Cache | `(num_layers, num_heads, N, head_dim)` | N 个输入 token 的 Value 投影 |

例如，对于 Llama-3-70B（80 层、64 头、head_dim=128），处理 4096 个输入 token 的 KV Cache 大小为：

```
2 × 80 × 64 × 4096 × 128 × 2 bytes (fp16) = 8 GB
```

这意味着仅输入 4096 个 token，KV Cache 就占用了 8 GB 显存。这就是长上下文推理时显存容易爆的原因。

### 2.3 Prefill 为什么是 Compute-Bound

> **Compute-Bound**: 计算受限，任务性能由 GPU 的算力（FLOPS）决定，而非显存带宽

Prefill 阶段的计算特性决定了它是 compute-bound：

#### Attention 的 O(n²) 复杂度

标准 Self-Attention 的核心计算是 Q、K 矩阵相乘：

```
Attention(Q, K, V) = softmax(Q · K^T / sqrt(d_k)) · V
```

- Q 的 shape: `(N, d_k)`
- K^T 的 shape: `(d_k, N)`
- Q · K^T 的结果 shape: `(N, N)` -- **这是一个 N×N 的注意力分数矩阵**

当输入长度 N = 4096 时，仅 Q·K^T 这一步就需要 `2 × N × N × d_k = 2 × 4096 × 4096 × 128 ≈ 4.3G` 次 FLOPs。

整个 Attention 层（含 Q·K^T、softmax、attention·V）的 FLOPs 大约为 `4 × N² × d_k`。

#### FFN 的矩阵乘法

每层的 FFN 包含两个线性变换：

```
FFN(x) = W2 · GELU(W1 · x + b1) + b2
```

- `W1 · x`: shape `(d_ff, d_model) × (d_model,)` -- 需要 `2 × d_ff × d_model` FLOPs
- `W2 · h`: shape `(d_model, d_ff) × (d_ff,)` -- 需要 `2 × d_model × d_ff` FLOPs

对于 70B 模型（`d_ff = 28672`），每层 FFN 对每个 token 需要 `2 × 28672 × 8192 × 2 ≈ 940M` FLOPs，N 个 token 则乘以 N。

#### 算术强度（Arithmetic Intensity）分析

> **Arithmetic Intensity**: 每 Byte 显存传输对应的浮点运算次数，单位为 FLOPs/Byte

Prefill 阶段的算术强度很高：

| 计算步骤 | 数据搬运量 | 计算量 | 算术强度 |
|----------|-----------|--------|---------|
| Attention Q·K^T | 2N × d_k (Q) + 2N × d_k (K) = 4N × d_k bytes | 2N² × d_k FLOPs | N/2 |
| FFN W1·x | 2d_ff × d_model bytes (权重) | 2d_ff × d_model FLOPs | 1 |
| FFN W2·h | 2d_model × d_ff bytes (权重) | 2d_model × d_ff FLOPs | 1 |

以 N = 4096, d_k = 128 为例，Attention Q·K^T 的算术强度约为 `4096/2 = 2048 FLOPs/Byte`。

而 A100 GPU 的显存带宽约为 2 TB/s，理论算力为 312 TFLOPS (fp16)，对应的平衡点算术强度为 `312T / 2T = 156 FLOPs/Byte`。2048 >> 156，远超平衡点，说明计算资源是瓶颈，显存带宽不是。

**结论**：Prefill 阶段，GPU 的算力被大量矩阵运算充分吃满，计算时间远大于数据搬运时间，因此是 compute-bound。

#### GPU 利用率高的原因

GPU 的架构天然适合 Prefill 的工作模式：

- **大规模并行**：GPU 拥有数千个 CUDA 核心，可以同时处理 N 个 token 的计算
- **矩阵运算优化**：Tensor Core 专为矩阵乘法设计，Prefill 中的大量 GEMM 操作可以高效利用
- **高算术强度**：数据复用率高，每个权重被多个 token 共享使用
- **计算密集**：FLOPs 总量大，足以让所有计算单元保持忙碌

在实际测试中，Prefill 阶段的 GPU 利用率（MFU，Model FLOPs Utilization）通常可以达到 40%-60%，而 Decode 阶段往往只有 1%-5%。

### 2.4 Prefill 的优化策略

| 策略 | 原理 | 效果 |
|------|------|------|
| Flash Attention | 分块计算 attention，减少 HBM 读写 | 减少 HBM 访问 5-20x |
| Flash Attention 2/3 | 更好的 warp 调度和并行化 | MFU 提升至 50-72% |
| Prefix Caching | 缓存共享前缀的 KV，跳过重复 prefill | 共享 system prompt 时 TTFT 大幅下降 |
| Paged Attention (vLLM) | 虚拟内存管理 KV Cache，减少碎片 | 显存利用率提升 2-4x |
| 多请求 batch prefill | 多个请求一起做 prefill | 提升 GPU 利用率 |

---

## 3. Decode 阶段详解

### 3.1 什么是 Decode

> **Decode**: 推理的第二阶段，逐个生成输出 token，每步读取 KV Cache

Decode 阶段从 Prefill 产出的 KV Cache 开始，每次生成一个新 token：

1. 取上一步生成的 token，做 embedding 得到一个向量 `(1, d_model)`
2. 经过 L 层 Transformer 前向传播
3. 在每层 Attention 中，用当前 token 的 Q 去和 KV Cache 中所有历史 token 的 K、V 做 attention
4. 取最后一层的输出，经 LM head 得到下一个 token 的概率分布
5. 用采样策略（greedy / top-k / top-p / temperature）选出下一个 token
6. 将新 token 的 K、V 追加到 KV Cache 中
7. 回到第 1 步，循环直到生成 EOS 或达到最大长度

关键特征：每一步**只处理 1 个 token**，但要和**所有历史 token** 做注意力计算。

### 3.2 Decode 为什么是 Memory-Bound

> **Memory-Bound**: 显存受限，任务性能由 GPU 的显存带宽（GB/s）决定，而非算力

#### 逐 token 计算导致的低算术强度

Decode 每步只处理 1 个 token，但需要读取之前所有 N 个 token 的 KV Cache：

```
当前步的 attention:
  Q: shape (1, d_k)     -- 只有 1 个 query
  K: shape (N, d_k)     -- 要读取 N 个历史 key
  V: shape (N, d_k)     -- 要读取 N 个历史 value
```

分析算术强度：

| 计算步骤 | 数据搬运量 | 计算量 | 算术强度 |
|----------|-----------|--------|---------|
| Q·K^T | 2d_k (Q) + 2N·d_k (K from HBM) ≈ 2N·d_k bytes | 2N × d_k FLOPs | 1 |
| Attn·V | 2N (weights) + 2N·d_k (V from HBM) ≈ 2N·d_k bytes | 2N × d_k FLOPs | 1 |

算术强度约为 1 FLOP/Byte，远低于 A100 的平衡点 156 FLOPs/Byte。

这意味着 GPU 每完成 1 次 FLOP 运算，就要等待 1 Byte 的数据从 HBM 传输过来。计算单元在大部分时间处于空闲状态，等数据"喂"过来。

#### 直观类比

可以把 GPU 想象成一个庞大的工厂（成千上万的工人），显存相当于远处的仓库：

- **Prefill** = 工厂接到一张大订单，把大量原材料一次性运到工厂，所有工人同时开工，流水线满负荷运转
- **Decode** = 工厂每秒钟只生产 1 个零件，但每次都要派人去仓库翻遍所有历史记录（KV Cache）来确认规格，工人大部分时间在等仓库数据

#### 显存带宽的瓶颈

以 A100 (80GB) 为例：

```
显存带宽:        ~2 TB/s (2,000 GB/s)
理论算力 (fp16): ~312 TFLOPS

Decode 单步的数据需求（70B 模型, 4096 token 上下文）:
  - 模型权重读取:  2 × 70B × 2 bytes = 280 GB (每层都要读一次)
  - KV Cache 读取: 2 × 80 × 2 × 64 × 4096 × 128 × 2 bytes = 8 GB
  - 总数据搬运量:  ~288 GB

  最低耗时 = 288 GB / 2,000 GB/s = 144 ms

Decode 单步的计算量:
  - Attention: ~2 × 4096 × 128 = 1M FLOPs (每个head)
  - FFN: ~2 × 28672 × 8192 × 2 = 940M FLOPs
  - 总计算量(80层): ~75G FLOPs
  - 计算耗时 = 75G / 312T = 0.24 ms

  实际耗时 >> 计算耗时, 说明 GPU 大部分时间在等数据
```

从这个计算可以看出，Decode 单步的计算只需要 0.24 ms，但数据搬运需要 144 ms。计算能力严重浪费，瓶颈完全在显存带宽上。

#### KV Cache 读取是 Decode 的最大开销

在 Decode 阶段，每一步的数据搬运构成如下（70B 模型）：

| 数据来源 | 大小 | 说明 |
|----------|------|------|
| 模型权重 | ~140 GB | 所有层的 Wq, Wk, Wv, Wo, W1, W2 等 |
| KV Cache (seq=4096) | ~8 GB | 随序列长度线性增长 |
| 激活值 | ~1 GB | 中间计算结果 |
| **合计** | **~149 GB** | |

随着对话轮次增加，KV Cache 越来越大，Decode 每步需要读取的 KV Cache 也在持续增长，导致 ITL（Inter-Token Latency）逐渐恶化。

### 3.3 Decode 的优化策略

| 策略 | 原理 | 效果 |
|------|------|------|
| KV Cache 量化 (GPTQ/AWQ) | 将 KV Cache 从 fp16 量化到 int8/int4 | 显存带宽需求降低 2-4x |
| Continuous Batching | 动态组合不同阶段的请求，提高 GPU 利用率 | 吞吐提升 2-3x |
| Speculative Decoding | 用小模型预测多个候选 token，大模型一次验证 | 减少 decode 步数 2-3x |
| Paged Attention | 分页管理 KV Cache，减少碎片浪费 | 显存利用率提升 2-4x |
| Tensor Parallelism | 将模型切分到多张 GPU | 减少单卡权重和 KV 读取量 |
| 修改注意力实现 | 使用 Flash-Decoding 等分块注意力实现 | 提升 decode 阶段 MFU |

---

## 4. Prefill vs Decode 全面对比

| 维度 | Prefill | Decode |
|------|---------|--------|
| **处理模式** | 一次性并行处理所有输入 token | 逐个串行生成输出 token |
| **每步输入量** | N 个 token（N 可能很大） | 1 个 token |
| **计算复杂度** | O(N² · d) per layer (attention) + O(N · d²) per layer (FFN) | O(N · d) per layer (attention) + O(d²) per layer (FFN) |
| **瓶颈类型** | Compute-Bound（算力受限） | Memory-Bound（显存带宽受限） |
| **GPU 利用率 (MFU)** | 40%-72% | 1%-5% |
| **延迟决定因素** | 输入序列长度 N、模型规模 | 输出序列长度、batch size、KV Cache 大小 |
| **典型显存压力** | 激活值存储（大 batch 时） | KV Cache 持续增长 |
| **优化方向** | 更高效算子（Flash Attention）、Prefix Caching、减少输入长度 | KV Cache 量化、Speculative Decoding、Continuous Batching |

**核心洞察**：Prefill 和 Decode 的瓶颈本质不同，因此优化方向也完全不同。用优化 Prefill 的方法去优化 Decode（或者反过来），往往收效甚微。

---

## 5. Throughput vs Latency Trade-off

> **Throughput**: 吞吐量，单位时间内系统处理的 token 总数或完成的请求数
> **Latency**: 延迟，单个请求从开始到完成的总耗时

### 5.1 两个维度的核心指标

在 LLM 推理场景中，吞吐和延迟分别由不同指标衡量：

**吞吐相关指标：**

| 指标 | 定义 | 关注方 |
|------|------|--------|
| Token Throughput | 每秒生成的 token 总数 | 服务提供方、成本控制 |
| Request Throughput | 每秒完成的请求数 | 服务容量规划 |

**延迟相关指标：**

> **TTFT (Time to First Token)**: 从请求开始到输出第一个 token 的延迟，主要取决于 Prefill 阶段的耗时

> **ITL (Inter-Token Latency)**: 相邻两个输出 token 之间的时间间隔，主要取决于 Decode 阶段的速度

> **TPOT (Time Per Output Token)**: 每生成一个输出 token 的平均耗时，与 ITL 含义相近

```
请求发出  │──────── TTFT ────────│─ITL─│─ITL─│─ITL─│── ... ──│
          │  Prefill 阶段  │  Decode 阶段（逐个 token）  │
          ↓                 ↓
        首 token          第2个  第3个  第4个 ...
```

### 5.2 Trade-off 的本质矛盾

吞吐和延迟之间天然存在矛盾，根源在于 batching：

| 策略 | 对 Throughput 的影响 | 对 Latency 的影响 |
|------|---------------------|-------------------|
| 增大 batch size | 提升（GPU 利用率更高） | 恶化（排队等待 + 单请求变慢） |
| 减小 batch size | 降低（GPU 空闲更多） | 改善（无需等待，单请求更快） |
| 多个请求拼 prefill | 提升 Prefill 吞吐 | 单请求 TTFT 变长 |
| 多个请求拼 decode | 提升 Decode 吞吐 | 单请求 ITL 变长 |

### 5.3 不同场景的偏好

| 应用场景 | 首要指标 | 次要指标 | 典型配置 |
|----------|---------|---------|---------|
| 交互式 Chat / Agent | **TTFT < 1s**, ITL < 100ms | Throughput | 小 batch、低并发 |
| 代码生成 (Copilot) | **TTFT < 500ms** | ITL（补全速度） | 小 batch、单请求优先 |
| 批量翻译 / 摘要 | **Throughput** | Latency（可接受分钟级） | 大 batch、高并发 |
| 离线数据处理 | **Throughput** | 几乎不限 | 最大 batch |
| 实时语音对话 | **TTFT < 200ms**, ITL < 50ms | Throughput | 极小 batch、模型量化 |

### 5.4 实际工程中的调度策略

现代推理引擎（vLLM, TGI, TensorRT-LLM）通过以下方式平衡 trade-off：

```
                    ┌──────────────────────────┐
                    │     请求队列 (Queue)       │
                    └──────────┬───────────────┘
                               │
                    ┌──────────▼───────────────┐
                    │   Continuous Batching     │  ← 动态调整 batch
                    │   调度器 (Scheduler)      │     大小和组合
                    └──────────┬───────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼──────┐ ┌──────▼────────┐ ┌────▼──────────┐
     │ Prefill 请求  │ │ Decode 请求   │ │ Prefill+Decode│
     │ (新到达)      │ │ (正在生成)    │ │ (混合执行)    │
     └───────────────┘ └───────────────┘ └───────────────┘
```

- **Continuous Batching**: 在一个 batch 中混合不同阶段的请求，新请求进来可以立即加入当前 batch 的 prefill 位置
- **Iteration-level Scheduling**: 每个 iteration 重新决定 batch 的组成，请求完成后立即释放 slot
- **Sliding Window**: 限制 attention 窗口大小，减少 decode 阶段的 KV Cache 读取量

---

## 6. Chunked Prefill 方案

> **Chunked Prefill**: 将长输入 token 序列分块处理，每个 chunk 的 prefill 和 decode 交替执行，降低单次 prefill 的显存峰值和延迟

### 6.1 问题背景

标准 Prefill 要求一次性处理所有输入 token。对于超长输入（如 100K+ token 的长文档），这带来几个问题：

1. **显存峰值极高**: 大 N 导致 Attention 的 `(N, N)` 矩阵占用大量显存
2. **TTFT 过长**: 用户要等整个 Prefill 完成才能看到第一个 token
3. **GPU 利用率不均**: 长 Prefill 占用大量时间，decode 请求被饿死

### 6.2 Chunked Prefill 的思路

将长度为 N 的输入分成 C 个 chunk，每个 chunk 大小为 `N/C`：

```
标准 Prefill:
  Token 1..N ──→ [一次全部处理] ──→ KV Cache (全部 N 个) ──→ Decode

Chunked Prefill:
  Token 1..(N/C)      ──→ [Prefill Chunk 1] ──→ KV Cache (N/C 个)
  Token (N/C+1)..(2N/C) ──→ [Prefill Chunk 2] ──→ KV Cache (2N/C 个)
  ...
  Token ((C-1)N/C+1)..N  ──→ [Prefill Chunk C] ──→ KV Cache (N 个) ──→ Decode
```

### 6.3 Chunked Prefill 的优势

| 优势 | 说明 |
|------|------|
| 降低显存峰值 | Attention 矩阵从 (N, N) 降到 (N/C, N/C)，峰值显存降低约 C 倍 |
| 更好的 QoS | 每个 chunk 之间可以插入 decode 请求，减少 decode 请求的等待时间 |
| 支持更长上下文 | 在有限显存内处理更长的输入序列 |
| 更灵活的调度 | chunk 之间可以做 preemption（抢占）和 swap（换入换出） |

### 6.4 Chunked Prefill 的代价

| 代价 | 说明 |
|------|------|
| 计算开销增加 | 每个 chunk 都要和之前所有 chunk 的 KV 做 attention，总计算量略增 |
| TTFT 不变 | 首 token 仍需等所有 chunk 处理完才能开始 decode |
| 实现复杂度 | 调度器需要管理 chunk 粒度的生命周期 |
| 对短输入无收益 | 输入较短时 chunk 化反而增加开销 |

### 6.5 实际应用

Chunked Prefill 在 Sarathi 系统中被系统性地提出和使用，vLLM 也在较新版本中支持了类似机制。在长文档问答、代码仓库分析等场景中效果显著。

---

## 7. 实际场景 Prefill 耗时估算

### 7.1 Coding Agent 场景

以一个典型的 coding agent（如 Claude Code、Cursor）请求为例，分析其 Prefill 耗时：

**输入构成：**

| 组成部分 | Token 数量 | 说明 |
|----------|-----------|------|
| System Prompt | ~2,000 tokens | 角色、能力边界、安全策略等 |
| Tool Schema | ~500 tokens | 文件读写、终端执行等工具定义 |
| 对话历史 (5 轮) | ~3,000 tokens | 包含代码片段、文件内容引用 |
| 当前用户消息 | ~200 tokens | 当前的用户指令 |
| **合计** | **~5,700 tokens** | |

### 7.2 计算过程

以 Llama-3-70B 为例，估算 Prefill 的计算量：

**单层计算量：**

```
Attention 部分:
  Q/K/V 投影:  3 × 2 × N × d_model × d_model = 3 × 2 × 5700 × 8192 × 8192 = 2.2T FLOPs
  Q·K^T:       2 × N² × d_head × num_heads = 2 × 5700² × 128 × 64 = 5.3T FLOPs
  Attn·V:      2 × N² × d_head × num_heads = 2 × 5700² × 128 × 64 = 5.3T FLOPs
  Output 投影: 2 × N × d_model × d_model = 2 × 5700 × 8192 × 8192 = 0.76T FLOPs
  小计:        ~13.6T FLOPs per layer

FFN 部分:
  W1·x:        2 × N × d_model × d_ff = 2 × 5700 × 8192 × 28672 = 2.7T FLOPs
  W2·h:        2 × N × d_ff × d_model = 2 × 5700 × 28672 × 8192 = 2.7T FLOPs
  小计:        ~5.4T FLOPs per layer

单层合计:      ~19T FLOPs
```

**全模型计算量：**

```
总 FLOPs = 80 layers × 19T = 1,520T FLOPs = 1.52 PFLOPs
```

**Prefill 耗时估算：**

```
假设 MFU (Model FLOPs Utilization) = 45%:
  实际有效算力 = 312 TFLOPS × 0.45 = 140.4 TFLOPS

  Prefill 耗时 = 1,520T / 140.4T = 10.8 秒

假设 MFU = 60% (Flash Attention 3 + 优化良好):
  实际有效算力 = 312 TFLOPS × 0.60 = 187.2 TFLOPS
  Prefill 耗时 = 1,520T / 187.2T = 8.1 秒
```

### 7.3 耗时分解

| 因素 | 影响 |
|------|------|
| Token 数量 | 每增加 1000 token，Prefill 耗时增加约 1.5-2 秒 |
| 模型规模 | 参数量翻倍，Prefill 耗时约翻倍 |
| GPU 型号 | A100 (312T) vs H100 (990T) 快约 3x |
| 优化水平 | MFU 从 30% 提升到 60%，耗时减半 |
| Batch Size | 多请求 batch prefill 有额外收益，但也有额外开销 |

### 7.4 优化建议

针对这种 coding agent 场景，减少 Prefill 耗时的实际手段：

1. **Prefix Caching**: System prompt 和 Tool Schema 对同一会话的所有请求相同，可以缓存 KV，跳过这部分 prefill
   - 缓存 2,500 tokens 后，只需 prefill ~3,200 tokens，耗时减少约 44%

2. **精简 System Prompt**: 在不影响功能的前提下压缩 system prompt
   - 从 2,000 tokens 压缩到 1,000 tokens，节省约 10% Prefill 耗时

3. **精简 Tool Schema**: 只发送当前任务需要的工具定义
   - 如果只需要 3 个工具而非全部 10 个，Schema 可从 500 降到 150 tokens

4. **上下文窗口管理**: 限制对话历史的长度
   - 使用滑动窗口或摘要策略，将历史控制在 2000 tokens 以内

---

## 8. 面试高频问题

### Q1: 为什么 Decode 阶段是 memory-bound，而 Prefill 是 compute-bound？

**A**: 根本区别在于每步处理的 token 数量不同。

Decode 每步只处理 1 个 token，需要做的浮点运算很少（约几十 G FLOPs），但必须从 HBM 读取所有历史 token 的 KV Cache 和全部模型权重（约 150-300 GB）。数据搬运量远大于计算量，算术强度约为 1 FLOP/Byte，远低于 GPU 的 compute-memory 平衡点。GPU 的计算单元大部分时间在等待数据从 HBM 传过来。

Prefill 一次性处理 N 个 token（N 通常上千），Attention 中 Q·K^T 产生 N×N 的矩阵，总 FLOPs 量级远高于数据搬运量。例如 N=4096 时，Attention 的算术强度可达 2000+ FLOP/Byte，远超 GPU 平衡点，此时计算能力成为瓶颈，GPU 算力被充分吃满。

---

### Q2: 如果让你优化一个在线 AI 助手的 TTFT（Time to First Token），你会从哪些方面入手？

**A**: TTFT 主要由 Prefill 阶段决定，优化思路从以下几个层面展开：

**第一层：减少 Prefill 计算量**
- 启用 Prefix Caching，缓存 system prompt 和 tool schema 的 KV，避免每次请求重复 prefill
- 精简 system prompt 和 tool schema 的 token 数量
- 限制对话历史长度，使用摘要或滑动窗口替代完整历史

**第二层：提升 Prefill 计算效率**
- 使用 Flash Attention 2/3，减少 HBM 读写，提升 MFU
- 确保使用优化的 kernel（如 TensorRT-LLM、vLLM 的自定义 CUDA kernel）
- 如果输入极长，考虑 Chunked Prefill 降低峰值显存

**第三层：调度层面优化**
- 限制 Prefill batch size，避免长输入请求被排在大 batch 后面等待
- 实现请求优先级，对交互式请求给予更高的调度优先级
- Prefill-Decode 分离部署，专用 GPU 处理 prefill

**第四层：硬件层面**
- 使用更快的 GPU（H100 > A100 > A10G）
- 增加 GPU 数量，使用 Tensor Parallelism 分摊 prefill 负载

---

### Q3: Continuous Batching 是什么？它如何改善 Throughput？

**A**: Continuous Batching（也叫 Iteration-level Scheduling 或 Inflight Batching）是一种动态调度策略。

传统 static batching 的问题是：一个 batch 中所有请求必须一起完成，如果某个请求先结束了，它的 slot 也要等到整个 batch 结束才能释放，GPU 算力被浪费。

Continuous Batching 在每个 iteration（即每个 decode 步骤）结束时重新评估 batch 的组成：
- 已经完成的请求立即释放 slot，新请求可以立即加入
- 新到达的请求可以在当前 iteration 的空闲 slot 中开始 prefill
- Prefill 和 Decode 可以在同一个 batch 中混合执行

效果：
- GPU 的 decode slot 利用率接近 100%（不再有空闲等待）
- 吞吐提升 2-3x，同时延迟不会明显恶化
- 是 vLLM、TGI 等现代推理框架的核心调度策略

---

### Q4: 模型参数量增大后，为什么 Decode 阶段的问题会越来越严重？有哪些缓解手段？

**A**: 模型参数量增大，Decode 阶段的 memory-bound 问题加剧，原因有两方面：

**第一，模型权重读取量增大。** Decode 每步都要读取完整的模型权重（每层的 Q/K/V/O 投影矩阵和 FFN 权重），参数量从 7B 增到 70B，权重读取量增加 10 倍，但每步的计算量只和序列长度相关，增长有限。这意味着算术强度进一步下降，GPU 计算单元更加空闲。

**第二，KV Cache 增大。** 更大的模型通常有更多的层和更大的隐藏维度，每个 token 的 KV Cache 占用更多空间。加上大模型往往支持更长的上下文窗口，KV Cache 总量更大，Decode 每步要读取的 KV 也更多。

**缓解手段：**

| 手段 | 原理 | 典型效果 |
|------|------|---------|
| KV Cache 量化 | 将 KV 从 fp16 量化到 int8/int4 | 带宽需求降低 2-4x |
| Speculative Decoding | 小模型预测，大模型一次验证多个 token | decode 步数减少 2-3x |
| Tensor Parallelism | 模型切分到多卡，每卡只读部分权重 | 单卡带宽压力降低 |
| Attention 背景下的模型量化 | 模型权重本身做 int8/int4 量化 | 权重读取量降低 2-4x |
| GQA (Grouped Query Attention) | 多个 Q head 共享 K/V head，减少 KV 总量 | KV Cache 减少到 1/4 或更少 |
| 降低精度计算 | 使用 fp8 或 int8 计算 | 带宽需求翻倍降低 |

其中 GQA 是架构层面的优化，Llama-2/3、Mistral 等现代模型均已采用。从 Llama-1 的 MHA（每个 Q head 对应一个 K/V head）到 Llama-2 的 GQA（8 个 Q head 共享 1 个 K/V head），KV Cache 量直接降为 1/8，对 Decode 阶段的改善非常显著。
