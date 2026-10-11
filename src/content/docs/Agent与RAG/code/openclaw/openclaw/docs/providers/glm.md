---
title: "GLM Models"
description: "GLM is a model family not a company available through the Z.AI platform. In OpenClaw, GLM models are accessed via the za"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\providers\\glm.md"
summary: "GLM model family overview + how to use it in OpenClaw"
---

# GLM models

GLM is a **model family** (not a company) available through the Z.AI platform. In OpenClaw, GLM
models are accessed via the `zai` provider and model IDs like `zai/glm-5`.

## CLI setup

```bash
openclaw onboard --auth-choice zai-api-key
```

## Config snippet

```json5
{
  env: { ZAI_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "zai/glm-5" } } },
}
```

## Notes

- GLM versions and availability can change; check Z.AI's docs for the latest.
- Example model IDs include `glm-5`, `glm-4.7`, and `glm-4.6`.
- For provider details, see [/providers/zai](/providers/zai).
