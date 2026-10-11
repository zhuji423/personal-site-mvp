---
title: "health"
description: "Fetch health from the running Gateway."
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\cli\\health.md"
summary: "CLI reference for `openclaw health` (gateway health endpoint via RPC)"
---

# `openclaw health`

Fetch health from the running Gateway.

```bash
openclaw health
openclaw health --json
openclaw health --verbose
```

Notes:

- `--verbose` runs live probes and prints per-account timings when multiple accounts are configured.
- Output includes per-agent session stores when multiple agents are configured.
