---
title: "Changelog"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\Swabble\\CHANGELOG.md"
---
# Changelog

## 0.2.0 — 2025-12-23

### Highlights
- Added `SwabbleKit` (multi-platform wake-word gate utilities with segment-aware gap detection).
- Swabble package now supports iOS + macOS consumers; CLI remains macOS 26-only.

### Changes
- CLI wake-word matching/stripping routed through `SwabbleKit` helpers.
- Speech pipeline types now explicitly gated to macOS 26 / iOS 26 availability.
