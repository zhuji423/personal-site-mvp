---
title: "code-review-comate"
description: "Perform thorough code review on selected code. Use when the user wants to check code quality, find security issues, optimize performance, or improve maintainability."
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\commands\\code-review-comate.md"
---

## Task
Analyze the user input and conduct a thorough code review. Provide constructive, actionable feedback.

## Review Areas
Analyze the selected code for:
1. **Security Issues**
   - Input validation and sanitization
   - Authentication and authorization
   - Data exposure risks
   - Injection vulnerabilities
2. **Performance & Efficiency**
   - Algorithm complexity
   - Memory usage patterns
   - Database query optimization
   - Unnecessary computations
3. **Code Quality**
   - Readability and maintainability
   - Proper naming conventions
   - Function/class size and responsibility
   - Code duplication
4. **Architecture & Design**
   - Design pattern usage
   - Separation of concerns
   - Dependency management
   - Error handling strategy
5. **Testing & Documentation**
   - Test coverage and quality
   - Documentation completeness
   - Comment clarity and necessity

## Output Format
Provide feedback as:
* Critical Issues** - Must fix before merge
* Suggestions** - Improvements to consider
* Good Practices** - What's done well

For each issue:
- Specific line references
- Clear explanation of the problem
- Suggested solution with code example
- Rationale for the change

Be constructive and educational in your feedback.