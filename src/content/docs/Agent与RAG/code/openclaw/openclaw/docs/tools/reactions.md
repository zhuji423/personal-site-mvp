---
title: "Reactions"
description: "Shared reaction semantics across channels:"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\tools\\reactions.md"
summary: "Reaction semantics shared across channels"
---

# Reaction tooling

Shared reaction semantics across channels:

- `emoji` is required when adding a reaction.
- `emoji=""` removes the bot's reaction(s) when supported.
- `remove: true` removes the specified emoji when supported (requires `emoji`).

Channel notes:

- **Discord/Slack**: empty `emoji` removes all of the bot's reactions on the message; `remove: true` removes just that emoji.
- **Google Chat**: empty `emoji` removes the app's reactions on the message; `remove: true` removes just that emoji.
- **Telegram**: empty `emoji` removes the bot's reactions; `remove: true` also removes reactions but still requires a non-empty `emoji` for tool validation.
- **WhatsApp**: empty `emoji` removes the bot reaction; `remove: true` maps to empty emoji (still requires `emoji`).
- **Zalo Personal (`zalouser`)**: requires non-empty `emoji`; `remove: true` removes that specific emoji reaction.
- **Signal**: inbound reaction notifications emit system events when `channels.signal.reactionNotifications` is enabled.
