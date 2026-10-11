---
title: "Bootstrap Extra Files Hook"
description: "Inject additional workspace bootstrap files via glob/path patterns"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\src\\hooks\\bundled\\bootstrap-extra-files\\HOOK.md"
name: "bootstrap-extra-files"
homepage: "https://docs.openclaw.ai/automation/hooks#bootstrap-extra-files"
---

# Bootstrap Extra Files Hook

Loads additional bootstrap files into `Project Context` during `agent:bootstrap`.

## Why

Use this when your workspace has multiple context roots (for example monorepos) and
you want to include extra `AGENTS.md`/`TOOLS.md`-class files without changing the
workspace root.

## Configuration

```json
{
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "bootstrap-extra-files": {
          "enabled": true,
          "paths": ["packages/*/AGENTS.md", "packages/*/TOOLS.md"]
        }
      }
    }
  }
}
```

## Options

- `paths` (string[]): preferred list of glob/path patterns.
- `patterns` (string[]): alias of `paths`.
- `files` (string[]): alias of `paths`.

All paths are resolved from the workspace and must stay inside it (including realpath checks).
Only recognized bootstrap basenames are loaded (`AGENTS.md`, `SOUL.md`, `TOOLS.md`,
`IDENTITY.md`, `USER.md`, `HEARTBEAT.md`, `BOOTSTRAP.md`, `MEMORY.md`, `memory.md`).
