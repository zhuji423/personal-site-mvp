---
title: "Batching 策略"
description: "核心问题：推理服务怎么把大量请求高效地塞进 GPU，既尽量提高吞吐，又不把延迟拖得太夸张？"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\03_week3_inference_claude_code\\inference\\batching_strategies.md"
---
# Batching 策略

> **核心问题**：推理服务怎么把大量请求高效地塞进 GPU，既尽量提高吞吐，又不把延迟拖得太夸张？

在 LLM 推理系统中，单次请求的 GPU 利用率通常只有个位数百分比。为了把 GPU 吃满，最直接的手段就是 batching —— 把多个请求打包在一起并行处理。但"怎么打包"这件事，从最朴素到最精细，经历了三代演进。

---

## 1. Static Batching（静态批处理）

> **Static Batching**: 把请求凑成一批一起处理，等整批完成后再处理下一批

### 1.1 工作流程

```
请求到达 → 攒满 batch_size 条 → 整批发送 GPU → 等待全部生成完成 → 处理下一批
```

Static batching 的调度逻辑非常简单：设定一个固定的 batch size，等凑够了就发车。整个过程像一辆公交车，必须坐满（或等到截止时间）才出发，中途不上下客。

```python
# Static Batching 伪代码
def static_batch_serving(requests, batch_size):
    batches = [requests[i:i+batch_size] for i in range(0, len(requests), batch_size)]
    for batch in batches:
        # 整批同时进入 prefill + decode，所有请求全部生成完毕才释放
        outputs = model.generate(batch)
        return_outputs(outputs)
```

### 1.2 Head-of-Line Blocking 问题

Static batching 最致命的问题是 **head-of-line blocking**：一个 batch 里只要有一个请求特别长，其他短请求都得跟着等。

| 情况 | 后果 |
|------|------|
| batch 里混入一个生成长度 2048 的请求 | 所有生成 32 token 的短请求一起白等 |
| batch 尚未凑满 | GPU 空转，新到的请求只能排队 |
| batch 刚发车又有新请求到达 | 必须等当前整批跑完 |

### 1.3 时间线示意

```
时间 →
请求 A: [======prefill======][====decode====]                          ↘ 完成时间 = 100%
请求 B: [======prefill======][=decode=]     <--- 等A解码完才返回       ↗ 完成时间 = 100%
请求 C:                 [======prefill======][====decode====]  ↘ 实际本可以更早完成
                         ↑ batch 2 等待 batch 1 结束才开始
```

### 1.4 唯一适用场景

- 输入输出长度非常接近（如批量翻译、批量摘要）
- 离线批处理，吞吐优先，对延迟完全不敏感
- 简单的评估基准测试

---

## 2. Dynamic Batching（动态批处理）

> **Dynamic Batching**: 在请求到达时动态组合成 batch，不等固定窗口

### 2.1 工作流程

```
请求到达 → 等待时间窗口 / 凑满 batch_size → 动态组合成 batch → GPU 处理 → 返回结果
```

Dynamic batching 引入了两个关键参数来决定"何时发车"：
- **max_batch_size**：batch 最大容量
- **wait_timeout**：最长等待时间（如 50ms）

只要满足其中一个条件（凑满 or 超时），就立即发车。

```python
# Dynamic Batching 伪代码
def dynamic_batch_serving(request_queue, max_batch_size, wait_timeout):
    while True:
        batch = []
        deadline = now() + wait_timeout

        while len(batch) < max_batch_size and now() < deadline:
            req = request_queue.poll(timeout=deadline - now())
            if req:
                batch.append(req)

        if batch:
            outputs = model.generate(batch)
            return_outputs(outputs)
```

### 2.2 相比 Static 的改进

| 维度 | Static Batching | Dynamic Batching |
|------|-----------------|------------------|
| 发车时机 | 固定凑满 batch_size | 凑满 or 超时，先到先得 |
| GPU 空转 | 严重（等凑满） | 较轻（有超时兜底） |
| 流量适配 | 差（固定节奏） | 较好（自适应流量波动） |
| 实现复杂度 | 极低 | 中等 |

### 2.3 仍然存在的问题

Dynamic batching 虽然比 static 灵活，但 batch 边界依然存在：

1. **batch 内部的拖累**：长请求和短请求仍然混在一起，短请求被长请求拖住
2. **batch 之间的间隙**：一个 batch 中某些请求先完成了，但槽位不会立即释放给新请求
3. **padding 浪费**：为了对齐张量，短序列需要 padding 到 batch 内最长序列的长度

---

## 3. Continuous Batching（vLLM / Orca）

> **Continuous Batching**: iteration 级别调度，有请求完成立即塞新请求，无需等待整批

### 3.1 核心思想

Continuous batching（也叫 iteration-level scheduling 或 in-flight batching）彻底打破了 batch 的边界。它不是以"一批"为单位调度，而是以"每一个 iteration"为单位：每个 decode step 结束后，检查哪些请求已经完成，释放它们的槽位，立即从队列里取新请求填入。

```
传统 batching:  [====batch 1 (全部完成)====] [====batch 2 (全部完成)====]
Continuous:     [req1][req2][req3]...
                ↑ req1 完成后立即塞入 req4，不等 req2/req3
```

### 3.2 时间线 ASCII 图

假设 batch 有 3 个槽位，请求 A/B/C 同时开始：

```
时间 →
         Iteration 1       Iteration 2       Iteration 3       Iteration 4
Slot 1: [A: decode tok1] [A: decode tok2] [A: decode tok3] [D: decode tok1]
Slot 2: [B: decode tok1] [B: decode tok2] [B: decode tok3] [E: decode tok1]
Slot 3: [C: decode tok1] [C: decode tok2] [D: decode tok1] [E: decode tok2]
                                    ↑                ↑                ↑
                               C 在 iter2 完成    B 在 iter3 完成   D 完成
                               D 立即填入槽位3    E 立即填入槽位3   F 立即填入

关键观察：
- Iteration 1: A, B, C 三个请求并行解码
- Iteration 2: C 生成完毕（只生成了 2 个 token），D 立即从等待队列填入 Slot 3
- Iteration 3: B 生成完毕（生成了 3 个 token），E 立即填入 Slot 3
- Iteration 4: A 仍在生成（需要 4+ token），D 完成，F 立即填入
- 没有任何 iteration 是"等一批结束"，GPU 始终满载
```

### 3.3 关键实现

```python
# Continuous Batching 伪代码
def continuous_batch_serving(request_queue, max_batch_slots):
    running = []  # 当前正在运行的请求

    while True:
        # 1. 执行一个 decode step（只对正在运行的请求）
        if running:
            model.forward(running)

        # 2. 收集已完成的请求，释放槽位
        finished = [r for r in running if r.is_finished()]
        for r in finished:
            running.remove(r)
            return_output(r)

        # 3. 立即从队列中取新请求填入空槽位
        free_slots = max_batch_slots - len(running)
        for _ in range(free_slots):
            req = request_queue.dequeue()
            if req:
                # 新请求先做 prefill，然后加入 running batch
                model.prefill(req)
                running.append(req)
            else:
                break
```

### 3.4 优势

| 优势 | 说明 |
|------|------|
| GPU 利用率更高 | batch 间几乎没有空洞，GPU 持续满载 |
| 对短请求更友好 | 短请求完成即返回，不必等长请求 |
| 吞吐更稳 | 更接近流式服务，尾部延迟更可控 |
| TTFT 更可预测 | prefill 可以在任意 iteration 插入 |

### 3.5 代表实现

- **vLLM**: 基于 PagedAttention，实现了 continuous batching + 自动内存管理
- **Orca (Microsoft)**: 首次提出 iteration-level scheduling 的论文
- **TGI (HuggingFace)**: 基于 FIFO 的连续批处理推理服务
- **SGLang**: RadixAttention 前缀缓存 + continuous batching 结合

---

## 4. 三种 Batching 策略对比

| 维度 | Static Batching | Dynamic Batching | Continuous Batching |
|------|-----------------|------------------|---------------------|
| 调度粒度 | batch 级别 | batch 级别 | iteration 级别 |
| 请求完成处理 | 等整批完成 | 等整批完成 | 完成即释放槽位 |
| GPU 利用率 | 低（batch 间空洞大） | 中（有超时等待） | 高（持续满载） |
| 短请求延迟 | 差（被长请求拖住） | 中（稍有改善） | 优（完成即返回） |
| 实现复杂度 | 低 | 中 | 高（需精细的内存和槽位管理） |
| 适用场景 | 离线批处理 | 一般在线服务 | 高并发在线推理 |

---

## 5. Prefix Caching 在 Batching 中的价值

> **Prefix Caching**: 缓存已计算过的 KV Cache 前缀，后续请求若共享相同前缀则直接复用，跳过重复 prefill

### 5.1 为什么 Prefix Caching 与 Batching 息息相关

在 batching 场景下，Prefix Caching 的价值被成倍放大。想象一个 batch 里有 32 个请求，它们都使用相同的 2000 token system prompt：

- **没有 Prefix Caching**：每个请求都要独立做 2000 token 的 prefill，batch 内重复计算 32 次
- **有 Prefix Caching**：只在第一次为这 2000 token 计算 KV Cache，后续 31 个请求直接复用

```
无 Prefix Caching:
  Req1: [system_prompt(2000 tok)][user_input] → 全部 prefill
  Req2: [system_prompt(2000 tok)][user_input] → 全部 prefill  ← 重复！
  Req3: [system_prompt(2000 tok)][user_input] → 全部 prefill  ← 重复！
  ...

有 Prefix Caching:
  Req1: [system_prompt(2000 tok)][user_input] → prefill 全部，缓存前缀
  Req2: [cached ✓][user_input] → 只 prefill user_input 部分
  Req3: [cached ✓][user_input] → 只 prefill user_input 部分
  ...
```

### 5.2 共享前缀的存储结构

```
RadixAttention Tree（SGLang 方案）:

                [system_prompt]
               /       |        \
        [tool_a]   [tool_b]   [tool_c]     ← 共享 system prompt 前缀
           |          |          |
      [user_q1]  [user_q2]  [user_q3]     ← 各自不同的用户输入
```

RadixAttention 使用基数树（radix tree）存储 KV Cache，自动发现和复用公共前缀，不限于完全匹配——部分前缀也可以共享。

### 5.3 Prefix Caching 在各场景下的价值

| 场景 | 共享前缀长度 | 价值 |
|------|-------------|------|
| 相同 system prompt | 中（数百~数千 token） | 高——几乎所有 LLM 服务都有 system prompt |
| 相同工具 schema | 高（数千 token） | 极高——function calling 场景 schema 可达数万 token |
| Agent 多轮对话 | 高（历史上下文） | 极高——每轮都重复历史对话 |
| 多路 best-of-n / tree search | 极高（几乎完全共享） | 核心——tree search 能跑起来的前提 |
| Coding agent 共享模板 | 中高（代码框架） | 高——大量文件共享 import、boilerplate |

### 5.4 与 Batching 的协同效应

Prefix Caching 和 Continuous Batching 是天然搭档：

1. **减少 prefill 时间** → 请求更快进入 decode 阶段
2. **节省显存** → 相同前缀只存一份 KV Cache → 同样显存可以塞更多请求
3. **提升 batch 吞吐** → prefill 阶段缩短，更多 iteration 用于并行 decode
4. **降低 TTFT** → 对首 token 延迟敏感的应用直接受益

---

## 6. Speculative Decoding（推测解码）

> **Speculative Decoding**: 用小模型快速 draft N 个 token，大模型并行验证，accept/reject

### 6.1 核心思想

LLM 的 decode 阶段是自回归的——每生成一个 token 都要依赖前一个 token，GPU 并行度极低。Speculative Decoding 的巧妙之处在于：用一个小模型（draft model）快速猜 N 个 token，然后用大模型（target model）一次性并行验证这 N 个 token。猜对了就采纳，猜错了就从第一个错误的位置开始用大模型重新生成。

```
关键洞察：
- decode 阶段串行生成 token 是性能瓶颈
- 小模型生成速度快（参数少），但质量可能不高
- 大模型可以一次 forward 验证多个 token（因为输入已知）
- 如果 draft 质量不错，大部分 token 能被接受 → 减少大模型 forward 次数
```

### 6.2 流程图

```
Step 1: Draft 阶段（小模型，串行生成 K 个 token）
──────────────────────────────────────────────
  输入: "The capital of France is"
  Draft Model → "Paris" → "a" → "beautiful" → "city"
  生成 K=4 个 draft token: [Paris, a, beautiful, city]

Step 2: Verify 阶段（大模型，一次 forward 并行验证）
──────────────────────────────────────────────────
  输入: "The capital of France is Paris a beautiful city"
  大模型对每个位置计算概率，与 draft token 对比：
    P(Paris | ...) = 0.95  → draft 概率 0.90 → accept ✓
    P(a     | ...) = 0.02  → draft 概率 0.01 → reject ✗ ← 停在这里
    （后面 beautiful, city 不需要验证）

Step 3: 修正阶段
────────────────
  从第一个 reject 位置开始，用大模型重新采样：
  "The capital of France is Paris, the most visited..."
  新 token 替换 reject 之后的所有 draft token

最终结果:
  保留: [Paris]        ← 来自 draft model，被验证通过
  修正: [, the most visited...] ← 来自 target model
  效果: 大模型只做了一次 forward，但输出了多个 token
```

### 6.3 数学原理

验证过程使用一次大模型 forward 即可完成。关键在于：对每个 draft token t_i，只需要检查大模型在给定相同前缀下给 t_i 分配的概率是否足够高。具体地：

- 对每个 draft token t_i，采样一个随机数 u ~ Uniform(0, 1)
- 如果 u < min(1, P_target(t_i) / P_draft(t_i))，则 accept
- 否则 reject t_i 及之后的所有 draft token，从位置 i 开始用大模型重新采样

这保证了验证后生成的分布与大模型原始分布完全一致（**分布不变性定理**），即 speculative decoding 不会改变生成质量。

### 6.4 何时有用

| 条件 | 说明 |
|------|------|
| draft model 与 target model 分布相似 | 接受率高，加速效果明显 |
| 生成阶段较长（长文本生成） | decode 步数多，有更多加速空间 |
| 大模型推理本身是瓶颈 | GPU 利用率未饱和时效果好 |
| 大 batch 场景 | 大模型已经接近满载时，额外 draft 成本相对可接受 |

典型的有效组合：
- Llama 70B（target）+ Llama 7B（draft）
- GPT-4 级别模型 + GPT-3.5 级别模型作为 draft
- 同一模型的量化版本作为 draft（如 FP16 target + INT4 draft）

### 6.5 何时没用

| 条件 | 说明 |
|------|------|
| draft model 质量太差 | 接受率低，频繁 reject，反而更慢 |
| 短文本生成（如分类、问答） | decode 步数太少，验证开销抵消收益 |
| 大模型 GPU 已经 100% 满载 | draft forward 会挤占大模型的计算资源 |
| 对延迟极其敏感 | draft 阶段本身会增加首 token 延迟 |
| target model 本身很快（小模型） | 加速比空间有限，不值得引入复杂度 |

### 6.6 变体扩展

- **Medusa**: 不用独立 draft model，而是在 target model 上额外训练多个 prediction head，一次 forward 预测多个后续 token
- **Eagle**: draft model 不仅看 token 序列，还利用 target model 的隐藏状态，提高 draft 质量
- **Staged Speculative**: 多级 draft，从小到大逐级验证
- **Self-Speculative**: 用 target model 自身的 early exit（浅层输出）作为 draft

---

## 7. 面试高频问题

### Q1: Continuous Batching 和 Dynamic Batching 的本质区别是什么？

**A**: 两者的本质区别在于 **调度粒度** 和 **槽位管理方式**。

- **Dynamic Batching** 仍然是 batch 级别调度：凑够一批 → 整批送 GPU → 全部完成 → 下一批。batch 内的请求即使有先完成的，也不能释放槽位给新请求。
- **Continuous Batching** 是 iteration 级别调度：每一步 decode 结束后，立即检查哪些请求完成了，释放它们的槽位，从等待队列中取新请求填入。没有固定的 batch 边界。

打个比方：Dynamic Batching 像火车（到站才上下客），Continuous Batching 像公交车（有人下车就有人上车）。

### Q2: Prefix Caching 什么时候效果最好？和数据分布有什么关系？

**A**: Prefix Caching 效果最好需满足两个条件：

1. **共享前缀足够长**：如果共享前缀只有几十个 token，复用节省的时间微乎其微。最佳场景是共享数千 token 的 system prompt + tool schema。
2. **请求间重叠率高**：需要大量请求共享相同或相似的前缀。数据分布越"集中"（如同一应用、同一 system prompt），效果越好；数据分布越"分散"（如通用 API 接受任意 prompt），效果越差。

典型的最佳实践是：为每个应用/场景维护独立的推理端点，确保请求间有高比例的共享前缀。

### Q3: Speculative Decoding 为什么能保证生成质量不变？

**A**: 因为验证过程的拒绝采样机制（rejection sampling）保证了输出分布与大模型原始分布完全一致。

形式化地说：设大模型的目标分布为 p(x)，draft 模型的分布为 q(x)。验证时，对每个 draft token，以概率 min(1, p(x)/q(x)) 接受，否则从 p(x) 的修正分布中重新采样。可以证明，经过这个过程后，最终每个 token 的分布恰好等于 p(x)。

这意味着 speculative decoding 是一种"无损加速"——要么更快（draft 全对），要么保持原有速度（draft 全错回退），但永远不会降低生成质量。

### Q4: 如果你负责设计一个面向 coding agent 的推理服务，会怎么选型？

**A**: 我会采用 **Continuous Batching + Prefix Caching** 作为基线，谨慎评估 Speculative Decoding。

**为什么选 Continuous Batching**：
- Coding agent 请求长度差异极大（从单行补全到整个文件重构），head-of-line blocking 是大问题
- Agent 通常有严格的响应延迟要求（用户在等待）
- 现代框架（vLLM、SGLang）已经成熟，工程成本可控

**为什么必须加 Prefix Caching**：
- Coding agent 的大量请求共享长 system prompt（编码规范、项目上下文、工具定义）
- 多轮对话场景中，历史对话作为前缀被反复使用
- Agent 的 tree-of-thought / best-of-n 采样几乎完全依赖 prefix caching 才能跑起来

**为什么对 Speculative Decoding 持谨慎态度**：
- Coding 生成对准确性要求极高，draft model 的代码错误被拒绝是常态，accept 率可能偏低
- Agent 交互模式中，生成长度较短且频繁，decode 阶段本身的优化空间有限
- 工程复杂度显著增加（需要管理两套模型、额外的内存占用），ROI 不确定

**补充考量**：
- 如果是吞吐优先的批量代码生成（如大规模代码补全、测试生成），Speculative Decoding 更值得尝试
- 如果是交互式 Agent（如 Cursor、Copilot Chat），优先保证 TTFT 和首段响应速度，Prefix Caching 优先级更高
