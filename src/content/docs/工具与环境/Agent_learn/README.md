---
title: "Agent Infra 学习路线"
description: "目标岗位：Agent 基建 / Infra 工程师 核心定位：搭一个让「1 个模型 x N 个任务 x M 条轨迹」同时跑、同时验、同时回收 reward 的高吞吐 infra 时间预算：每天 3-4 小时，4 周冲刺"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\README.md"
---
# Agent Infra 学习路线

> 目标岗位：Agent 基建 / Infra 工程师
> 核心定位：搭一个让「1 个模型 x N 个任务 x M 条轨迹」同时跑、同时验、同时回收 reward 的高吞吐 infra
> 时间预算：每天 3-4 小时，4 周冲刺

## 世界观模型

```
模型生成 patch/action  -->  [可验证的隔离环境]  -->  pass / fail --> reward
      (Policy)               (Verifier)              (Reward Signal)
                                   |
                           这就是岗位核心工作
```

**Docker 只是载体**，明天换成 Firecracker、gVisor、WebAssembly runtime 都可以。重点是「大规模可并发、可复现、可自动化判分的 rollout 验证基础设施」。

## 岗位核心能力

| 能力 | 技术栈 |
|------|--------|
| 大规模并发验证 | 容器编排、调度、资源池化、K8s |
| 验证环境可复现 | 镜像管理、状态快照、CoW 缓存 |
| 验证闭环自动化 | Harness 框架、reward signal 自动产出 |
| 推理侧多线程/多分支 | 异步推理调度、SubAgent 通信 |

## 4 周学习路线

| 周 | 主题 | 目标 |
|----|------|------|
| 1 | Docker 容器化基建 | 手写 Dockerfile，起 16 个服务并发跑，白板讲清 namespace/cgroups |
| 2 | RL 验证环境 + Harness | 讲清 PPO/GRPO，理解 Verifier 在训练流程中的角色 |
| 3 | 推理引擎 + Claude Code | 讲清 Prefill/Decode 瓶颈，画出 Claude Code 完整架构图 |
| 4 | 评测 Pipeline + Deep Research | 回答「怎么搭评测 infra」，答好 Deep Research 加速题 |

## 学习策略

### 三个核心问题（遇到任何技术问题都问自己）

1. 这个东西怎么**并发**？
2. 这个东西怎么**复现 / 复用**？
3. 这个东西怎么**自动判分**？

### 视角转变

| 应用层视角 | 基建视角 |
|------------|----------|
| 双层记忆系统 | 轨迹压缩 + 跨 session memory module |
| Hook 机制做进度反馈 | Hook 层作为 reward signal 采集点 |
| Session 管理按渠道隔离 | 多租户 context 隔离 + 资源调度 |
| Skills 设计 | Tool registry + 能力路由 infra |
| 120→30 分钟提效 | 消除 context switching + 并行化验证链路 |

## 目录结构

```
00_core_concepts/       核心概念与世界观
01_week1_docker/        Week 1: Docker 容器化基建
02_week2_rl_verification/ Week 2: RL 验证环境 + Harness
03_week3_inference_claude_code/ Week 3: 推理引擎 + Claude Code
04_week4_eval_deep_research/ Week 4: 评测 Pipeline + Deep Research
05_interview_prep/      面试准备
06_references/          参考资料汇总
```
