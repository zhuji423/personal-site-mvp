---
title: "Agent Bootstrapping"
description: "Bootstrapping is the first‑run ritual that prepares an agent workspace and collects identity details. It happens after o"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\docs\\start\\bootstrapping.md"
summary: "Agent bootstrapping ritual that seeds the workspace and identity files"
sidebarTitle: "Bootstrapping"
---

# Agent Bootstrapping

Bootstrapping is the **first‑run** ritual that prepares an agent workspace and
collects identity details. It happens after onboarding, when the agent starts
for the first time.

## What bootstrapping does

On the first agent run, OpenClaw bootstraps the workspace (default
`~/.openclaw/workspace`):

- Seeds `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.
- Runs a short Q&A ritual (one question at a time).
- Writes identity + preferences to `IDENTITY.md`, `USER.md`, `SOUL.md`.
- Removes `BOOTSTRAP.md` when finished so it only runs once.

## Where it runs

Bootstrapping always runs on the **gateway host**. If the macOS app connects to
a remote Gateway, the workspace and bootstrapping files live on that remote
machine.

<Note>
When the Gateway runs on another machine, edit workspace files on the gateway
host (for example, `user@gateway-host:~/.openclaw/workspace`).
</Note>

## Related docs

- macOS app onboarding: [Onboarding](/start/onboarding)
- Workspace layout: [Agent workspace](/concepts/agent-workspace)
