---
title: "OpenClaw docs i18n assets"
description: "This folder stores generated and config files for documentation translations."
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\.i18n\\README.md"
---
# OpenClaw docs i18n assets

This folder stores **generated** and **config** files for documentation translations.

## Files

- `glossary.<lang>.json` — preferred term mappings (used in prompt guidance).
- `<lang>.tm.jsonl` — translation memory (cache) keyed by workflow + model + text hash.

## Glossary format

`glossary.<lang>.json` is an array of entries:

```json
{
  "source": "troubleshooting",
  "target": "故障排除",
  "ignore_case": true,
  "whole_word": false
}
```

Fields:

- `source`: English (or source) phrase to prefer.
- `target`: preferred translation output.

## Notes

- Glossary entries are passed to the model as **prompt guidance** (no deterministic rewrites).
- The translation memory is updated by `scripts/docs-i18n`.
