---
title: "必读论文清单"
description: "本清单按照推荐阅读顺序排列，每篇论文包含核心贡献、与岗位的关联、关键概念解释。"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\02_week2_rl_verification\\papers\\paper_list.md"
---
# 必读论文清单

> 本清单按照推荐阅读顺序排列，每篇论文包含核心贡献、与岗位的关联、关键概念解释。

---

## 1. PPO: Proximal Policy Optimization Algorithms

**标题**: Proximal Policy Optimization Algorithms
**作者**: John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov
**年份**: 2017
**链接**: https://arxiv.org/abs/1707.06347

### 核心贡献

提出了 PPO 算法，一种简单但高效的策略优化方法。通过 clipped surrogate objective 限制了每次策略更新的幅度，实现了与 TRPO（Trust Region Policy Optimization）相近的训练稳定性，但实现复杂度大幅降低。PPO 迅速成为 RL 领域最广泛使用的策略梯度算法。

### 为什么读这篇

- **面试必问**：PPO 是 RL 训练大模型（RLHF）的基础算法，不理解 PPO 就无法理解 RLHF
- **Agent Infra 工程视角**：PPO 的训练循环（rollout → advantage → update）是所有 RL 训练框架（verl、OpenRLHF、TRL）的核心
- **工程实现的关键**：clip 机制、GAE 计算、Actor-Critic 架构都是工程实现的关键决策点

### 关键概念

> **Surrogate Objective (代理目标)**：不直接优化真正的目标函数（因为太难），而是优化一个近似的、更容易计算的目标函数。

> **Trust Region (信任域)**：限制策略更新的范围，确保新策略不会偏离旧策略太远。TRPO 用 KL 约束显式实现，PPO 用 clip 隐式实现。

> **Clipped Surrogate Objective**：PPO 的核心公式，通过限制 ratio = pi_new/pi_old 在 [1-epsilon, 1+epsilon] 范围内来约束更新幅度。

### 核心公式

```python
# PPO 的核心公式
ratio = pi_new(a|s) / pi_old(a|s)
clipped_ratio = clip(ratio, 1 - epsilon, 1 + epsilon)
L_CLIP = min(ratio * A, clipped_ratio * A)

# epsilon 通常设为 0.1 ~ 0.2
# A 是 advantage function
```

---

## 2. GRPO: Group Relative Policy Optimization (DeepSeek-Math)

**标题**: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
**作者**: Zhihong Shao et al. (DeepSeek)
**年份**: 2024
**链接**: https://arxiv.org/abs/2402.03300

### 核心贡献

提出了 GRPO（Group Relative Policy Optimization），一种不需要 Critic 网络的 RL 算法。核心思想是对同一个问题生成一组回答，用组内相对排名代替 Critic 的价值估计来计算 Advantage。在 DeepSeekMath 中，使用 GRPO 在数学推理任务上取得了显著提升。

### 为什么读这篇

- **代码 RL 训练的主流选择**：DeepSeek-Coder、Kimi-K2 等都采用了 GRPO 或其变体
- **理解 GRPO 为什么适合代码任务**：代码任务有明确的验证标准（测试通过/失败），组内相对排名天然有效
- **工程简化**：省掉 Critic 意味着节省 50% 显存，对 Agent Infra 工程师来说是重要的架构决策

### 关键概念

> **Group Relative Policy Optimization**：对同一问题生成 G 个回答，用组内均值作为 baseline、标准差做归一化来计算 Advantage，从而省掉 Critic 网络。

> **Rejection Sampling**：一种简单的 RL 方法，从多个回答中选择最好的，直接用最好的回答做 SFT。GRPO 可以看作是 rejection sampling 的「梯度版本」。

### 核心公式

```python
# GRPO 的 Advantage 计算
# 对同一 prompt 的 G 个回答：
rewards = [r1, r2, ..., rG]
A_i = (r_i - mean(rewards)) / std(rewards)

# 不需要 Critic！
# 没有 V(s) 的估计
# 显存减少约 50%
```

---

## 3. SWE-RL / SWE-Gym: RL for Coding Agents

**标题 1**: SWE-Gym: A Reinforcement Learning Environment for Software Engineering
**标题 2**: SWE-RL: Advancing LLM Reasoning for Software Engineering
**作者**: Meng et al. / Yang et al.
**年份**: 2024
**链接**: https://arxiv.org/abs/2410.04927 / https://github.com/SWE-Gym/SWE-Gym

### 核心贡献

构建了第一个专门用于 RL 训练代码 Agent 的环境和 benchmark。SWE-Gym 从真实 GitHub issue 中提取任务，提供了标准化的环境（Docker sandbox）和评估方式。SWE-RL 使用这个环境对 LLaMA 模型进行 RL 训练，展示了 RL 训练能显著提升模型在真实软件工程任务上的表现。

### 为什么读这篇

- **直接对口岗位**：Agent Infra 工程师的工作核心就是构建这样的 RL 训练环境
- **Verifier 设计参考**：SWE-Gym 的 Verifier 设计（运行测试、检查 git diff）是最典型的工程实践
- **真实世界的 RL 训练 pipeline**：从 rollout 生成到 reward 计算，展示了完整的工程实现
- **Docker 在 RL 训练中的应用**：展示了如何用容器做安全的代码验证

### 关键概念

> **SWE-Gym**：一个 RL 训练环境，将 GitHub issue 转化为 RL 任务。每个任务包括：问题描述、代码仓库、测试用例、评估脚本。

> **Solve Rate**：模型成功解决 SWE-bench 任务的比例。是衡量 coding agent 能力的核心指标。

> **Action Space (动作空间)**：Agent 在 SWE-Gym 中可以执行的动作集合，包括编辑文件、运行命令、搜索代码等。

### 工程亮点

```
SWE-Gym 的关键设计决策：

  1. 任务来源: 真实 GitHub issue（不是合成数据）
  2. 环境隔离: Docker 容器（安全 + 可复现）
  3. 评估方式: 运行原有测试套件（客观、可靠）
  4. Reward 设计: binary（测试全部通过 = 1，否则 = 0）
  5. 难度分级: Easy / Medium / Hard（基于需要修改的文件数量）
```

---

## 4. Kimi-Researcher / WebDancer: Agentic RL for Deep Research

**标题**: WebDancer: Agent Reinforcement Learning with Large Language Models
**作者**: Shengnan Guo et al. (Moonshot AI)
**年份**: 2025
**链接**: https://arxiv.org/abs/2501.10928

### 核心贡献

提出了一种用于训练深度研究 Agent（deep research agent）的 RL 方法。核心思想是将 Agent 的搜索-阅读-总结过程建模为一个 RL 问题，reward 信号来自最终答案的质量（通过独立的验证模型评估）。WebDancer 展示了 RL 训练可以使 Agent 学到更高效的搜索策略和信息整合能力。

### 为什么读这篇

- **Agent RL 训练的前沿方向**：不止是代码任务，RL 训练也可以提升 Agent 在信息检索、多步推理等场景的能力
- **非代码任务的 Verifier 设计**：展示了如何用 reward model 评估 Agent 的最终输出质量
- **多步决策的 RL 训练**：Agent 需要做多步决策（搜什么、读什么、什么时候停止），比代码生成更复杂

### 关键概念

> **Agentic RL**：将 Agent 的完整决策过程（搜索、阅读、总结）作为 RL 的轨迹进行训练。每个工具调用都是一个 action，每步的观测是工具返回的结果。

> **Deep Research Agent**：一个能够自主搜索、阅读多篇文章、综合信息来回答复杂问题的 Agent。与简单的搜索-回答不同，它需要多轮搜索和多步推理。

> **Terminal Reward**：只在 Agent 完成任务时才给 reward，中间步骤没有即时 reward。需要用 GAE 或 Monte Carlo 方法将最终 reward 分配到每一步。

### 核心挑战

```
Agentic RL 面临的挑战：

  1. 信用分配问题 (Credit Assignment)
     最终 reward 是 0.8，但 Agent 做了 10 步决策
     哪些步骤是好的？哪些是多余的？

  2. 稀疏奖励 (Sparse Reward)
     大部分步骤没有即时反馈
     Agent 如何学到好的搜索策略？

  3. 长轨迹 (Long Trajectory)
     一个研究任务可能涉及 20+ 次搜索
     轨迹很长，训练不稳定

  4. 评估困难
     研究类任务的答案不唯一
     需要可靠的 reward model
```

---

## 5. OpenRLHF: 一个易于使用的 RLHF 框架

**标题**: OpenRLHF: An Easy-to-use, Scalable and High-performance RLHF Framework
**作者**: Huayi Zou et al.
**年份**: 2024
**链接**: https://github.com/OpenRLHF/OpenRLHF

### 核心贡献

构建了一个生产级的 RLHF 训练框架，支持 PPO、DPO、GRPO 等多种算法。根据 OpenRLHF 官方 README，当前更准确的描述是：它基于 **Ray + vLLM + DeepSpeed + HuggingFace Transformers** 构建，在分布式训练和推理方面做了深度优化。OpenRLHF 的设计哲学是「简单易用 + 高性能」，代码结构清晰，适合作为学习 RL 训练工程的起点。

### 为什么读这篇

- **工程实现的最佳参考**：比学术论文更贴近实际工程，展示了生产级 RL 训练框架的设计决策
- **代码结构清晰**：比 verl 更容易理解，适合入门
- **覆盖多种算法**：PPO、DPO、GRPO 的实现在同一个框架中，方便对比学习
- **分布式训练实践**：展示了如何用 Ray 做调度、用 DeepSpeed 做高效训练、用 vLLM 做高吞吐 rollout 的工程细节

### 关键概念

> **Ray**：分布式调度框架。OpenRLHF 用它来拆分 Actor、Reward、Reference、Critic 等角色，并在多 GPU / 多节点上协调这些组件。

> **DeepSpeed**：高效训练基础设施。OpenRLHF 用 ZeRO-3、AutoTP 等能力降低显存占用、支持大模型训练。

> **vLLM**：高性能推理引擎。OpenRLHF 用它加速 rollout 生成，因为 RLHF 训练的大头通常是 sample generation。

> **HuggingFace Transformers**：模型接口层。OpenRLHF 直接兼容 HF 模型权重、Tokenizer 和训练工作流。

### 代码导读

**PPO 训练流程**

| 位置 | 作用 |
|------|------|
| `openrlhf/trainer/ppo_trainer.py#generate` | 生成 rollout |
| `openrlhf/trainer/ppo_trainer.py#compute_rewards` | 计算 reward |
| `openrlhf/trainer/ppo_trainer.py#compute_advantage` | 计算 advantage（GAE） |
| `openrlhf/trainer/ppo_trainer.py#train_minibatch` | 执行 PPO clip update |
| `openrlhf/trainer/ppo_trainer.py#train_epoch` | 多轮训练迭代 |

**GRPO 训练流程**

| 位置 | 作用 |
|------|------|
| `openrlhf/trainer/grpo_trainer.py#generate` | 生成 `G` 个 rollout |
| `openrlhf/trainer/grpo_trainer.py#compute_rewards` | 计算 reward |
| `openrlhf/trainer/grpo_trainer.py#compute_advantage` | 做组内归一化 |
| `openrlhf/trainer/grpo_trainer.py#train_minibatch` | 执行 PPO clip update |

---

## 推荐阅读顺序

1. PPO 原始论文：理解 RL 训练的算法基础。
2. GRPO / DeepSeek-Math：理解代码 RL 训练的主流算法。
3. SWE-Gym：理解代码 RL 训练的工程实践。
4. WebDancer：如果你对 research agent 感兴趣，用来补前沿方向。
5. OpenRLHF：最后回到代码，理解这些算法是怎么落进工程实现里的。

---

## 面试高频问题

### Q1: 你觉得哪篇论文对 Agent Infra 工程师最重要？为什么？

**A**: 我认为 SWE-Gym 最为重要，因为：

1. 它将 RL 训练从「学术问题」变成了「工程问题」：展示了如何构建完整的 RL 训练 pipeline，从任务定义到 reward 计算到评估
2. Verifier 设计是它的核心贡献：Docker 沙箱、测试运行、评估脚本，这些都是 Agent Infra 工程师的日常工作
3. 它代表了业界趋势：用 RL 训练 coding agent 已经成为主流方向（OpenAI、DeepSeek、Anthropic 都在做）

PPO 论文虽然基础，但它更多是算法层面的。SWE-Gym 是「如何把算法落地到工程」的最佳范例。

### Q2: DeepSeek-Math 中的 GRPO 和传统 PPO 最大的区别是什么？

**A**: 最大的区别是 **Advantage 的计算方式**：

- PPO 需要一个额外的 Critic 网络来估计 V(s)，然后用 GAE 计算 Advantage = R - V(s)
- GRPO 不需要 Critic，对同一问题生成 G 个回答，用组内相对排名计算 Advantage = (r - mean) / std

这个区别带来的工程影响：
1. **显存减少**：省掉 Critic 网络，可以用更大的 batch size
2. **训练更稳定**：不依赖 Critic 的训练质量
3. **实现更简单**：不需要维护 Actor-Critic 的同步

特别适合代码/数学任务，因为这些任务有明确、可靠的 reward signal（测试通过/失败），不需要 Critic 做额外的价值估计。

### Q3: SWE-Gym 的 reward 设计为什么只用 binary reward？不觉得太粗糙了吗？

**A**: SWE-Gym 选择 binary reward（测试全部通过 = 1，否则 = 0）是经过深思熟虑的：

**支持 binary reward 的理由**：
1. **可靠性**：binary reward 最不容易被 gaming。如果用连续 reward，模型可能学会"通过大部分测试"但不完全正确的策略
2. **简洁性**：binary reward 不需要调参（没有权重），实现最简单
3. **GRPO 的适配**：GRPO 用组内相对排名，即使 reward 是 binary，组内也有方差（部分回答通过、部分不通过）

**binary reward 的局限**：
1. 信号粗糙，无法区分"差一点就对了"和"完全错误"
2. 对接近正确但不完美的回答没有额外的学习信号

**实际做法**：可以先用 binary reward 训练，后期加入 continuous reward（如代码覆盖率、风格分数）做精细调优。

### Q4: WebDancer 论文中提到的 Agentic RL 和代码 RL 训练有什么本质区别？

**A**: 核心区别在于**轨迹的结构和 reward 的分配**：

| 维度 | 代码 RL | Agentic RL (Research) |
|------|---------|----------------------|
| 轨迹结构 | 生成代码 → 运行 → 结果 | 搜索 → 阅读 → 总结 → 搜索 → ... |
| 步骤数 | 少（通常 1 次生成） | 多（10-30 步） |
| reward 时机 | 生成后立即获得 | 任务完成后才获得（terminal reward） |
| 信用分配 | 容易（reward 直接对应生成的代码） | 困难（reward 需要分配到多个步骤） |
| 动作空间 | 离散（token 生成） | 混合（token + 工具调用） |

Agentic RL 的关键挑战是**信用分配**：最终 reward 是好的，但 Agent 的 20 步操作中，哪些步骤是关键的好步骤？哪些是多余的？这需要 GAE 等方法来将最终 reward 合理地分配到每一步。

→ 参见 [../concepts/ppo_grpo.md](../concepts/ppo_grpo.md) 了解 PPO/GRPO 算法细节
→ 参见 [../concepts/rollout_reward_update.md](../concepts/rollout_reward_update.md) 了解完整数据流
→ 参见 [../resources.md](../resources.md) 了解框架代码导读
