---
title: "is"
description: "Analyze GitHub issues (bugs or feature requests)"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\openclaw\\openclaw\\.pi\\prompts\\is.md"
---

Analyze GitHub issue(s): $ARGUMENTS

For each issue:

1. Read the issue in full, including all comments and linked issues/PRs.

2. **For bugs**:
   - Ignore any root cause analysis in the issue (likely wrong)
   - Read all related code files in full (no truncation)
   - Trace the code path and identify the actual root cause
   - Propose a fix

3. **For feature requests**:
   - Read all related code files in full (no truncation)
   - Propose the most concise implementation approach
   - List affected files and changes needed

Do NOT implement unless explicitly asked. Analyze and propose only.
