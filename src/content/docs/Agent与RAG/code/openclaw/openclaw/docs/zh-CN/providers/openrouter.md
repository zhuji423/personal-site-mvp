---
title: "OpenRouter"
description: "OpenRouter 提供了一个统一 API，通过单一端点和 API 密钥将请求路由到多种模型。它兼容 OpenAI，因此大多数 OpenAI SDK 只需切换 base URL 即可使用。"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\zh-CN\\providers\\openrouter.md"
summary: "使用 OpenRouter 的统一 API 在 OpenClaw 中访问多种模型"
---

# OpenRouter

OpenRouter 提供了一个**统一 API**，通过单一端点和 API 密钥将请求路由到多种模型。它兼容 OpenAI，因此大多数 OpenAI SDK 只需切换 base URL 即可使用。

## CLI 设置

```bash
openclaw onboard --auth-choice apiKey --token-provider openrouter --token "$OPENROUTER_API_KEY"
```

## 配置片段

```json5
{
  env: { OPENROUTER_API_KEY: "sk-or-..." },
  agents: {
    defaults: {
      model: { primary: "openrouter/anthropic/claude-sonnet-4-5" },
    },
  },
}
```

## 注意事项

- 模型引用格式为 `openrouter/<provider>/<model>`。
- 更多模型/提供商选项，请参阅[模型提供商](/concepts/model-providers)。
- OpenRouter 底层使用 Bearer 令牌和你的 API 密钥进行认证。
