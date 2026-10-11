---
title: "Week 2 资源链接汇总"
description: "- GitHub: https://github.com/volcengine/verl - 定位: 大规模分布式 RL 训练框架，基于 Ray - 特点: 对 GPU 集群利用率优化较好，支持 PPO、GRPO、DPO"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\02_week2_rl_verification\\resources.md"
---
# Week 2 资源链接汇总

---

## RL 训练框架

### 1. verl (字节跳动)

- **GitHub**: https://github.com/volcengine/verl
- **定位**: 大规模分布式 RL 训练框架，基于 Ray
- **特点**: 对 GPU 集群利用率优化较好，支持 PPO、GRPO、DPO

**关键文件说明**:

| 路径 | 作用 |
|------|------|
| `verl/trainer/ppo/core_algos/compute_advantage.py` | GAE 计算 |
| `verl/trainer/ppo/core_algos/ppo_policy_loss.py` | PPO clip loss |
| `verl/trainer/ppo/core_algos/kl_divergence.py` | KL 散度计算 |
| `verl/trainer/ppo/ray_trainer.py` | 分布式训练主循环 |
| `verl/trainer/grpo/ray_trainer.py` | GRPO 训练逻辑 |
| `verl/workers/actor.py` | Actor 策略模型 |
| `verl/workers/critic.py` | Critic 价值模型 |
| `verl/workers/rollout.py` | Rollout 生成 |
| `verl/models/model.py` | 模型封装 |
| `verl/utils/reward.py` | Reward 计算 |
| `verl/utils/tokenizer.py` | Tokenizer 封装 |

**推荐阅读顺序**:
1. `verl/trainer/ppo/ray_trainer.py` — 理解完整的训练循环
2. `verl/trainer/ppo/core_algos/compute_advantage.py` — 理解 GAE
3. `verl/workers/rollout.py` — 理解 rollout 生成
4. `verl/workers/actor.py` — 理解 Actor 的推理逻辑

### 2. OpenRLHF

- **GitHub**: https://github.com/OpenRLHF/OpenRLHF
- **定位**: 生产级 RLHF 训练框架，基于 Ray + vLLM + DeepSpeed + HuggingFace Transformers
- **特点**: 代码结构清晰、支持多种算法、社区活跃
- **本地摘要**: 参见 [../06_references/official_sources.md](../06_references/official_sources.md)

**关键文件说明**:

| 路径 | 作用 |
|------|------|
| `openrlhf/trainer/ppo_trainer.py` | PPO 训练主循环 |
| `openrlhf/trainer/grpo_trainer.py` | GRPO 训练 |
| `openrlhf/trainer/dpo_trainer.py` | DPO 训练 |
| `openrlhf/trainer/reward_trainer.py` | Reward Model 训练 |
| `openrlhf/models/actor.py` | Actor 模型 |
| `openrlhf/models/critic.py` | Critic 模型 |
| `openrlhf/models/reward_model.py` | Reward Model |
| `openrlhf/datasets/sft_dataset.py` | SFT 数据集 |
| `openrlhf/datasets/rl_dataset.py` | RL 数据集 |
| `openrlhf/utils/deepspeed.py` | DeepSpeed 集成 |
| `openrlhf/utils/blending.py` | 数据混合策略 |

**推荐阅读顺序**:
1. `openrlhf/trainer/ppo_trainer.py` — 完整的 PPO 训练流程
2. `openrlhf/trainer/ppo_trainer.py#generate` — rollout 生成
3. `openrlhf/trainer/ppo_trainer.py#train_minibatch` — PPO 更新
4. `openrlhf/models/actor.py` — Actor 模型的封装

### 3. TRL (HuggingFace)

- **GitHub**: https://github.com/huggingface/trl
- **文档**: https://huggingface.co/docs/trl/
- **定位**: HuggingFace 生态的 RL 训练库，最易上手
- **特点**: 与 HF 模型/数据集无缝集成，适合原型验证

**关键文件说明**:

| 路径 | 作用 |
|------|------|
| `trl/trainer/ppo_trainer.py` | PPO 训练 |
| `trl/trainer/grpo_trainer.py` | GRPO 训练 |
| `trl/trainer/dpo_trainer.py` | DPO 训练 |
| `trl/trainer/sft_trainer.py` | SFT 训练 |
| `trl/models/modeling_base.py` | 基础模型类 |
| `trl/models/reward_model.py` | Reward Model |
| `trl/core/ppo_function.py` | PPO 核心算法 |
| `trl/core/utils.py` | 工具函数 |
| `trl/environment/text_environment.py` | 文本生成环境 |

**推荐阅读顺序**:
1. `trl/trainer/ppo_trainer.py` — TRL 的 PPO 实现
2. `trl/core/ppo_function.py` — PPO 核心（loss 计算、advantage）
3. `trl/models/modeling_base.py` — 理解 TRL 如何封装 HF 模型

---

## 推荐的 RL 入门教程

### 入门级（零基础）

1. **Spinning Up in Deep RL** (OpenAI)
   - 链接: https://spinningup.openai.com/
   - 特点: 最友好的 RL 入门教程，有大量直觉解释和可视化
   - 重点阅读: Policy Gradient、PPO 章节

2. **David Silver's RL Course** (DeepMind)
   - 链接: https://www.davidsilver.uk/teaching/
   - 特点: RL 领域最经典的课程，理论深度足够
   - 重点: Lecture 3 (Model-Free Prediction)、Lecture 5 (Actor-Critic)

3. **Simple RL 算法实现**
   - 链接: https://github.com/cyoon1729/deep-rl-tutorial
   - 特点: 从零实现 DQN、PPO 等算法，代码简洁

### 进阶级（理解 RLHF）

4. **InstructGPT 论文** (OpenAI, 2022)
   - 链接: https://arxiv.org/abs/2203.02155
   - 特点: RLHF 方法论的开山之作，展示了完整的 SFT → RM → PPO 流程

5. **ChatGPT 技术报告** (OpenAI, 2023)
   - 链接: https://arxiv.org/abs/2303.08774
   - 特点: InstructGPT 的工程化实践，涉及大规模部署的工程细节

6. **A Survey on RLHF** (2023)
   - 链接: https://arxiv.org/abs/2309.00252
   - 特点: RLHF 领域的综述论文，覆盖了各种变体和方法

### 实战级（工程实现）

7. **OpenRLHF examples**
   - 链接: https://github.com/OpenRLHF/OpenRLHF/tree/main/examples
   - 特点: 包含 PPO、DPO、GRPO 的训练脚本，可以直接运行

8. **verl examples**
   - 链接: https://github.com/volcengine/verl/tree/main/examples
   - 特点: 包含在真实任务上的 RL 训练示例

---

## 论文链接汇总

| 论文 | 链接 |
|------|------|
| PPO (2017) | https://arxiv.org/abs/1707.06347 |
| DeepSeek-Math (GRPO) | https://arxiv.org/abs/2402.03300 |
| SWE-Gym | https://arxiv.org/abs/2410.04927 |
| SWE-RL | https://arxiv.org/abs/2502.12270 |
| WebDancer | https://arxiv.org/abs/2501.10928 |
| InstructGPT (RLHF) | https://arxiv.org/abs/2203.02155 |
| TRLS (TRL from Language Feedback) | https://arxiv.org/abs/2302.05215 |

---

## 推理引擎（Week 3 预习）

> 以下资源会在 Week 3 深入学习，这里提前列出供预习。

- **vLLM**: https://github.com/vllm-project/vllm — PagedAttention, Continuous Batching
- **SGLang**: https://github.com/sgl-project/sglang — RadixAttention, Prefix Caching
- **TensorRT-LLM**: https://github.com/NVIDIA/TensorRT-LLM — NVIDIA 的推理优化引擎

→ 参见 [../03_week3_inference_claude_code/README.md](../03_week3_inference_claude_code/README.md)
