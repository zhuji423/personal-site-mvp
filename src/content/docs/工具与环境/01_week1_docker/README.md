---
title: "Week 1: Docker 容器化基建"
description: "能手写 Dockerfile，能用 compose 起 16 个服务并发跑任务，能白板讲清 namespace / cgroups。"
date: "2026-04-20"
category: "工具与环境"
source: "D:\\mac_m4\\Agent_learn\\01_week1_docker\\README.md"
---
# Week 1: Docker 容器化基建

> 最高优先级周

## 目标

能手写 Dockerfile，能用 compose 起 16 个服务并发跑任务，能白板讲清 namespace / cgroups。

## 任务清单

### 必做动手任务
- [ ] 写一个「并发起 16 个 Python worker、每个 worker 跑一个任务、主进程收集 reward」的 demo
- [ ] 用 `docker-compose up --scale worker=16` 或 Python `docker` SDK 实现
- [ ] 测试 Copy-on-Write 共享 volume 的效果

### 必读
- [ ] [Docker overview](https://docs.docker.com/get-started/overview/) 核心概念章节
- [ ] 《Docker 从入门到实践》namespace / cgroups 章节（只看原理，不抄命令）
- [ ] 精读 SWE-bench evaluation harness 源码（`princeton-nlp/SWE-bench`）

### SWE-bench 源码重点
- 每个 instance 怎么起独立 Docker
- 怎么控制并发数
- 怎么自动判分并回收结果

## 产出

- [ ] 能给面试官白板画一张「16 Docker 并发验证 rollout 的调度图」
- [ ] 能讲清 `pid / net / mnt / uts / ipc / user` 六大 namespace 的作用

## 文件导航

| 文件 | 内容 |
|------|------|
| [concepts/namespace_cgroups.md](concepts/namespace_cgroups.md) | namespace 六大类 + cgroups 原理 |
| [concepts/image_layers_cow.md](concepts/image_layers_cow.md) | 镜像分层 + Copy-on-Write |
| [concepts/container_orchestration.md](concepts/container_orchestration.md) | 容器编排与调度设计 |
| [tasks/concurrent_workers.md](tasks/concurrent_workers.md) | 动手任务：16 个并发 worker demo |
| [resources.md](resources.md) | 必读资源链接 |
