---
title: "health"
description: "从运行中的 Gateway 网关获取健康状态。"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\zh-CN\\cli\\health.md"
summary: "`openclaw health` 的 CLI 参考（通过 RPC 获取 Gateway 网关健康端点）"
---

# `openclaw health`

从运行中的 Gateway 网关获取健康状态。

```bash
openclaw health
openclaw health --json
openclaw health --verbose
```

注意：

- `--verbose` 运行实时探测，并在配置了多个账户时打印每个账户的耗时。
- 当配置了多个智能体时，输出包括每个智能体的会话存储。
