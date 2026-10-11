---
title: "logs"
description: "Tail Gateway file logs over RPC works in remote mode."
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\cli\\logs.md"
summary: "CLI reference for `openclaw logs` (tail gateway logs via RPC)"
---

# `openclaw logs`

Tail Gateway file logs over RPC (works in remote mode).

Related:

- Logging overview: [Logging](/logging)

## Examples

```bash
openclaw logs
openclaw logs --follow
openclaw logs --json
openclaw logs --limit 500
openclaw logs --local-time
openclaw logs --follow --local-time
```

Use `--local-time` to render timestamps in your local timezone.
