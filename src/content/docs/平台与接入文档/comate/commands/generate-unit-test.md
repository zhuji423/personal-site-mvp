---
title: ".generate-unit-test"
description: "请根据提供的被测方法（或类）信息，为目标方法（或类）编写完整可运行的单元测试代码。并严格遵循以下要求："
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\commands\\.generate-unit-test.md"
---
请根据提供的被测方法（或类）信息，为目标方法（或类）编写完整可运行的单元测试代码。并严格遵循以下要求：

通用要求：

- 当用户输入只有选中代码块时，只对代码块所在的方法写单测代码。
- 当用户输入有多个方法（或类）信息时，请为每个方法都生出单测。
- 单元测试代码必须完整可运行，不能是简单示例，每个测试方法必须有完整的代码实现。
- 测试覆盖率必须尽可能达到 100%，要求：
  - 覆盖所有正常输入场景
  - 覆盖边界值（最小值 / 最大值 / 特殊值）
  - 覆盖所有条件分支（if / else / switch / try-catch / 循环 / 返回路径）
  - 覆盖异常输入和错误处理逻辑（包括抛出异常或返回错误的情况）
  - 每条代码路径都必须至少有一个对 应的测试用例
- 禁止使用通配符导入：所有导入语句中不得包含通配符 *。
- 如果是断言类（如 JUnit 的 Assertions），必须显式写出每个需要的静态方法导入，例如：
  import static org.junit.jupiter.api.Assertions.assertEquals;
  import static org.junit.jupiter.api.Assertions.assertThrows;
  import static org.junit.jupiter.api.Assertions.assertTrue;
- 如果模型生成了包含 * 的导入语句，视为错误输出，必须重写代码 ，直到所有 import 均为显式导入。

各语言要求：

- Go：使用 `gotests` 生成单元测试；采用集成测试方式，对需要的资源做必要的准备；
- Java：使用 `junit5` 生成单元测试；要求严格使用 JDK 23 语法，确保用例在 JDK 23 环境中可以正常运行；不能调用 private 的属性和方法；
- Python：使用 `pytest` 生成单元测试；每个测试 case 必须完整实现，并包含有效断言；
- Kotlin：每个测试 case 必须有断言
- JavaScript：使用 `Jest` 生成单元测试，每个测试 case 必须完整可运行，并包含断言
