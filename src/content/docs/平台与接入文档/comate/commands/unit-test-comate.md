---
title: "unit-test-comate"
description: "Generate comprehensive unit tests for selected functions. Use when the user wants to create test cases, validate behavior, test edge cases, or improve test coverage."
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\commands\\unit-test-comate.md"
---

## Task
Analyze the user-selected function/method and generate focused unit tests that thoroughly validate its behavior.

## Test Generation Strategy
1. **Core Functionality Tests**
   - Test the main purpose/expected behavior
   - Verify return values with typical inputs
   - Test with realistic data scenarios
2. **Input Validation Tests**
   - Test with invalid input types
   - Test with null/undefined values
   - Test with empty strings/arrays/objects
   - Test boundary values (min/max, zero, negative numbers)
3. **Error Handling Tests**
   - Test expected exceptions are thrown
   - Verify error messages are meaningful
   - Test graceful handling of edge cases
4. **Side Effects Tests** (if applicable)
   - Verify external calls are made correctly
   - Test state changes
   - Validate interactions with dependencies

## Test Structure Requirements
- Use existing project testing framework and patterns
- Follow AAA pattern: Arrange, Act, Assert
- Write descriptive test names that explain the scenario
- Group related tests in describe/context blocks
- Mock external dependencies cleanly

## Guidelines
- Generate 5-8 focused test cases covering the most important scenarios
- Include realistic test data, not just simple examples
- Add comments for complex test setup or assertions
- Ensure tests are independent and can run in any order
- Focus on testing behavior, not implementation details

Create tests that give confidence the function works correctly and help catch regressions.