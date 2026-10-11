---
title: "GRPO Training Guide"
description: "All code has been implemented and tested. The GRPO training script is ready for experiments."
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\cs336\\assignment1-basics\\reference\\Stanford-CS336-spring25\\assignment5-alignment\\GRPO_TRAINING_GUIDE.md"
---
# GRPO Training Guide

## 🎉 Status: Ready to Run!

All code has been implemented and tested. The GRPO training script is ready for experiments.

## ✅ Pre-flight Checklist

### 1. Core Components
- [x] `scripts/grpo_train_loop.py` - Main training loop
- [x] `tests/adapters.py` - All 10 adapter functions implemented
- [x] `cs336_alignment/drgrpo_grader.py` - Reward function
- [x] Data format standardized to `question`/`answer`

### 2. Data Files
- [x] MATH train: 7,500 examples
- [x] MATH test: 5,000 examples
- [x] Format conversion completed (backups created with `.backup` extension)

### 3. Dependencies
- [x] Virtual environment active at `.venv/`
- [x] All required packages installed (vLLM, transformers, torch, etc.)

## 🚀 Quick Start

### Test Run (10 steps, ~30 minutes on 2xH100)
```bash
.venv/bin/python scripts/grpo_train_loop.py \
    --n-grpo-steps 10 \
    --eval-steps 2 \
    --rollout-batch-size 64 \
    --train-batch-size 64 \
    --gradient-accumulation-steps 32 \
    --model-path /data/a5-alignment/models/Qwen2.5-Math-1.5B \
    --wandb-project cs336-grpo \
    --wandb-run-name test-run
```

### Full Training (200 steps, default hyperparameters)
```bash
.venv/bin/python scripts/grpo_train_loop.py \
    --model-path /data/a5-alignment/models/Qwen2.5-Math-1.5B \
    --wandb-project cs336-grpo \
    --wandb-run-name grpo-baseline
```

## 📊 Default Hyperparameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `n_grpo_steps` | 200 | Number of GRPO training steps |
| `learning_rate` | 1e-5 | AdamW learning rate |
| `rollout_batch_size` | 256 | Batch size for rollouts |
| `group_size` | 8 | Responses per question |
| `train_batch_size` | 256 | Training batch size |
| `gradient_accumulation_steps` | 128 | Gradient accumulation |
| `loss_type` | `"reinforce_with_baseline"` | Policy gradient loss |
| `use_std_normalization` | `True` | Normalize by group std |
| `eval_steps` | 5 | Evaluate every N steps |

## 🎛️ Key Configuration Options

### Loss Types
- `"no_baseline"` - Vanilla REINFORCE
- `"reinforce_with_baseline"` - REINFORCE with group baseline (recommended)
- `"grpo_clip"` - GRPO-Clip for off-policy training

### On-Policy vs Off-Policy
**On-Policy (default)**:
```bash
--epochs-per-rollout-batch 1 \
--train-batch-size 256
```

**Off-Policy**:
```bash
--epochs-per-rollout-batch 4 \
--train-batch-size 1024 \
--loss-type grpo_clip \
--cliprange 0.2
```

## 📁 Important Files

```
assignment5-alignment/
├── scripts/
│   ├── grpo_train_loop.py          # Main training script ⭐
│   └── convert_dataset_format.py   # Data format converter
├── tests/
│   └── adapters.py                 # Adapter implementations ⭐
├── cs336_alignment/
│   ├── drgrpo_grader.py           # Reward function
│   └── prompts/
│       └── r1_zero.prompt         # Default prompt template
└── data/
    └── math/
        ├── train.jsonl            # 7,500 training examples
        ├── test.jsonl             # 5,000 test examples
        ├── train.jsonl.backup     # Original format backup
        └── test.jsonl.backup      # Original format backup
```

## 🔧 Implemented Functions

All required adapter functions in `tests/adapters.py`:

1. ✅ `run_tokenize_prompt_and_output` - Tokenization with response mask
2. ✅ `run_compute_group_normalized_rewards` - Group-normalized advantages
3. ✅ `run_compute_entropy` - Per-token entropy
4. ✅ `run_get_response_log_probs` - Log probabilities from model
5. ✅ `run_compute_naive_policy_gradient_loss` - Vanilla policy gradient
6. ✅ `run_compute_grpo_clip_loss` - GRPO-Clip loss
7. ✅ `run_compute_policy_gradient_loss` - Loss dispatcher
8. ✅ `run_masked_mean` - Masked averaging
9. ✅ `run_masked_normalize` - Masked normalization
10. ✅ `run_grpo_microbatch_train_step` - Microbatch training step

## 💡 Usage Tips

### 1. View All Options
```bash
.venv/bin/python scripts/grpo_train_loop.py --help
```

### 2. GPU Requirements
- **Minimum**: 2 GPUs (1 for training, 1 for vLLM)
- **Recommended**: 2x H100 80GB

### 3. Data Paths
Training data paths can be customized:
```bash
--data-path ./data/math/train.jsonl \
--val-data-path ./data/math/test.jsonl
```

### 4. Checkpointing
Models are saved:
- Every 10 steps: `./checkpoints/grpo/checkpoint_step_N/`
- Final model: `./checkpoints/grpo/final_model/`

Customize save directory:
```bash
--save-dir /path/to/checkpoints
```

### 5. WandB Logging
The script automatically logs to WandB:
- Training metrics: loss, grad_norm, entropy, rewards
- Evaluation metrics: accuracy, format_reward, answer_reward

Customize project and run name:
```bash
--wandb-project my-project \
--wandb-run-name my-experiment
```

## 🐛 Troubleshooting

### Import Errors
If you get `ModuleNotFoundError`, make sure to use the virtual environment:
```bash
.venv/bin/python scripts/grpo_train_loop.py ...
```

### Data Format Issues
If you get key errors, verify data format:
```bash
head -1 data/math/train.jsonl | python -m json.tool
```
Should show `"question"` and `"answer"` keys.

To restore original format:
```bash
mv data/math/train.jsonl.backup data/math/train.jsonl
```

### Model Not Found
The model path should be on the cluster:
```
/data/a5-alignment/models/Qwen2.5-Math-1.5B
```

## 📚 Algorithm Reference

The implementation follows **Algorithm 3 (GRPO)** from the assignment PDF:

1. **Rollout Phase**: Generate `group_size` responses per question using vLLM
2. **Reward Computation**: Compute group-normalized advantages
3. **Training Phase**: Update policy with policy gradient loss
4. **Evaluation**: Periodically evaluate on validation set

## 🎯 Next Steps

1. Run a small test to verify everything works
2. Tune hyperparameters (learning rate, batch sizes)
3. Experiment with different loss types
4. Try off-policy training
5. Compare to baselines (SFT, Expert Iteration)

Good luck with your experiments! 🚀
