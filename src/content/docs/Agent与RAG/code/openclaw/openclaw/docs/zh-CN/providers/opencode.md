---
title: "OpenCode Zen"
description: "OpenCode Zen 是由 OpenCode 团队推荐的一组精选模型列表，适用于编程智能体。它是一个可选的托管模型访问路径，使用 API 密钥和 opencode 提供商。Zen 目前处于测试阶段。"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\zh-CN\\providers\\opencode.md"
summary: "在 OpenClaw 中使用 OpenCode Zen（精选模型）"
---

# OpenCode Zen

OpenCode Zen 是由 OpenCode 团队推荐的一组**精选模型列表**，适用于编程智能体。它是一个可选的托管模型访问路径，使用 API 密钥和 `opencode` 提供商。Zen 目前处于测试阶段。

## CLI 设置

```bash
openclaw onboard --auth-choice opencode-zen
# 或非交互式
openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
```

## 配置片段

```json5
{
  env: { OPENCODE_API_KEY: "sk-..." },
  agents: { defaults: { model: { primary: "opencode/claude-opus-4-5" } } },
}
```

## 注意事项

- 也支持 `OPENCODE_ZEN_API_KEY`。
- 你需要登录 Zen，添加账单信息，然后复制你的 API 密钥。
- OpenCode Zen 按请求计费；详情请查看 OpenCode 控制台。
