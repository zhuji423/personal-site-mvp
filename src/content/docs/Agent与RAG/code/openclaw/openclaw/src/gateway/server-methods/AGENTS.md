---
title: "Gateway Server Methods Notes"
description: "- Pi session transcripts are a parentId chain/DAG; never append Pi type: \"message\" entries via raw JSONL writes missing "
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\src\\gateway\\server-methods\\AGENTS.md"
---
# Gateway Server Methods Notes

- Pi session transcripts are a `parentId` chain/DAG; never append Pi `type: "message"` entries via raw JSONL writes (missing `parentId` can sever the leaf path and break compaction/history). Always write transcript messages via `SessionManager.appendMessage(...)` (or a wrapper that uses it).
