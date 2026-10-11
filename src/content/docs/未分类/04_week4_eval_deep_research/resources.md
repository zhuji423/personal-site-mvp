---
title: "Week 4: 资源链接汇总"
description: "本文件汇总 Week 4 学习涉及的所有资源链接，包括论文、代码仓库、技术博客和学习资料。"
date: "2026-04-20"
category: "未分类"
source: "D:\\mac_m4\\Agent_learn\\04_week4_eval_deep_research\\resources.md"
---
# Week 4: 资源链接汇总

> 本文件汇总 Week 4 学习涉及的所有资源链接，包括论文、代码仓库、技术博客和学习资料。

> 本地摘要入口：
> - [papers.md](../06_references/papers.md)
> - [official_sources.md](../06_references/official_sources.md)

---

## Benchmark 相关

### SWE-bench

| 资源 | 链接 | 说明 |
|------|------|------|
| SWE-bench 官方仓库 | https://github.com/princeton-nlp/SWE-bench | 数据集、评测脚本、Docker 方案 |
| SWE-bench 论文 | https://arxiv.org/abs/2310.06770 | Jimenez et al., 2024 |
| SWE-bench 官方排行榜 | https://www.swebench.com/ | 实时更新的模型排名 |
| SWE-bench Lite 介绍 | https://openai.com/index/introducing-swe-bench-verified/ | OpenAI 的筛选方案 |
| SWE-bench Verified | https://www.swebench.com/verified.html | 人工验证版本 |

### HLE

| 资源 | 链接 | 说明 |
|------|------|------|
| HLE 项目主页 | https://humans-last-exam.github.io/ | 题目介绍和评测结果 |
| HLE Nature 论文 | https://www.nature.com/articles/s41586-025-09962-4 | 官方论文，2026-01-28 发表于 Nature |
| HLE 数据集 | https://huggingface.co/datasets/cais/hle | HuggingFace 数据集 |

### GAIA

| 资源 | 链接 | 说明 |
|------|------|------|
| GAIA 论文 | https://arxiv.org/abs/2311.12983 | Mialon et al., 2023 |
| GAIA 数据集 | https://huggingface.co/datasets/gaia-benchmark/GAIA | HuggingFace 数据集 |
| GAIA 排行榜 | https://huggingface.co/spaces/gaia-benchmark/leaderboard | 实时排名 |

### BrowseComp

| 资源 | 链接 | 说明 |
|------|------|------|
| BrowseComp 论文 | https://arxiv.org/abs/2404.12936 | Cohan et al., 2024 |
| BrowseComp 官网 | https://browsecomp.github.io/ | 任务介绍和评测方案 |
| BrowseComp 数据集 | https://github.com/web-arena-x/browse_comp | 数据和评测脚本 |

---

## Deep Research 相关

### OpenAI Deep Research

| 资源 | 链接 | 说明 |
|------|------|------|
| OpenAI 官方博客 | https://openai.com/index/deep-research/ | Deep Research 功能介绍 |
| 技术分析文章 | https://blog.langchain.dev/deep-research/ | LangChain 的架构分析 |

### Perplexity

| 资源 | 链接 | 说明 |
|------|------|------|
| Perplexity 官方博客 | https://blog.perplexity.ai/ | 搜索架构介绍 |
| Perplexity 技术博客 | https://www.perplexity.ai/technology | 技术细节 |

### 开源实现

| 资源 | 链接 | 说明 |
|------|------|------|
| GPT-Researcher | https://github.com/assafelovic/gpt-researcher | 最流行的开源实现 |
| Jina DeepSearch | https://github.com/jina-ai/reader | Jina AI 的阅读器 + 搜索 |
| DeepResearch (开源) | https://github.com/langchain-ai/deep-research | LangChain 实现 |

### 学术研究

| 资源 | 链接 | 说明 |
|------|------|------|
| Kimi-Researcher 论文 | https://arxiv.org/abs/2502.04723 | Agent 搜索增强 |
| WebDancer 论文 | https://arxiv.org/abs/2405.01906 | Web 浏览 Agent RL 训练 |

---

## 推理引擎相关

→ 参见 [../03_week3_inference_claude_code/](../03_week3_inference_claude_code/README.md) 了解推理引擎基础

| 资源 | 链接 | 说明 |
|------|------|------|
| vLLM GitHub | https://github.com/vllm-project/vllm | PagedAttention 实现 |
| vLLM 技术博客 | https://blog.vllm.ai/ | 技术细节 |
| SGLang GitHub | https://github.com/sgl-project/sglang | RadixAttention 实现 |
| SGLang 技术博客 | https://blog.sglang.ai/ | 技术细节 |
| Orca 论文 (Continuous Batching) | https://arxiv.org/abs/2309.14509 | 连续批处理 |
| Speculative Decoding 论文 | https://arxiv.org/abs/2302.01318 | 投机解码 |

---

## RL 训练相关

→ 参见 [../02_week2_rl_verification/](../02_week2_rl_verification/README.md) 了解 RL 基础

| 资源 | 链接 | 说明 |
|------|------|------|
| verl GitHub | https://github.com/volcengine/verl | 字节跳动的 RL 框架 |
| OpenRLHF GitHub | https://github.com/OpenRLHF/OpenRLHF | 开源 RL 训练框架 |
| TRL GitHub | https://github.com/huggingface/trl | HuggingFace 的 RL 框架 |
| GRPO 论文 (DeepSeek-Math) | https://arxiv.org/abs/2402.03300 | GRPO 算法 |

---

## Docker 相关

→ 参见 [../01_week1_docker/](../01_week1_docker/README.md) 了解 Docker 基础

| 资源 | 链接 | 说明 |
|------|------|------|
| Docker 官方文档 | https://docs.docker.com/ | 容器化基础 |
| Docker Compose 文档 | https://docs.docker.com/compose/ | 多容器编排 |
| Playwright Docker | https://github.com/microsoft/playwright/tree/main/utils/docker | 浏览器自动化容器 |

---

## 学习路径推荐

### Day 1-2: Benchmark 深度解析

1. 通读 SWE-bench 论文 (2310.06770)
2. 浏览 SWE-bench 官方仓库的代码结构
3. 通读 HLE 论文 (2501.14715)
4. 通读 GAIA 论文 (2311.12983)
5. 浏览 BrowseComp 数据和评测脚本

### Day 3-4: Deep Research 架构

1. 阅读 OpenAI Deep Research 博客
2. 克隆 GPT-Researcher，阅读核心代码
3. 阅读 Kimi-Researcher 论文
4. 对比不同架构的差异
5. 阅读 five_layer_optimization.md（本仓库）

### Day 5: 综合应用

1. 思考如何用 Docker + RL infra 搭建评测系统
2. 设计 Deep Research 五层优化方案
3. 尝试运行 GPT-Researcher

### Day 6-7: 面试准备

1. 阅读 project_reframing.md（项目重讲）
2. 练习白板图（whiteboard_diagrams.md）
3. 自检清单（self_check_list.md）
