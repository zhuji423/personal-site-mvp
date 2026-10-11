---
title: ".function-comment"
description: "请为选中函数生成标准的中文函数注释。"
date: "2026-04-21"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\commands\\.function-comment.md"
---
请为选中函数生成标准的中文函数注释。

要求：

1. 根据代码语言自动选择对应的标准注释格式：

- Java/C#：使用JavaDoc格式 (/** ... _/)
- Python：使用Google风格docstring格式 (\"\"\" ... \"\"\")
- JavaScript/TypeScript：使用JSDoc格式 (/_* ... */)
- Go：使用godoc格式 (// ...)
- 其他语言：使用该语言最广泛接受的注释格式

2. 格式要求：

- 保持与函数定义相同的缩进级别
- 使用清晰的段落分隔
- 保持注释格式的一致性

3. 其他要求：

- 简洁明了，避免冗余，不需要todo list进行规划
- 只返回注释内容，不包含函数定义和函数体
- 使用工具直接将结果应用到源文件

示例输出（Python）：
`python
\"\"\"
函数功能描述

    Args:
        参数1: 说明
        参数2: 说明

    Returns:
        返回值说明
    \"\"\"

`

示例输出（Java）：
`java
/**

- 函数功能描述
-
- @param 参数1 说明
- @param 参数2 说明
- @return 返回值说明
  */
  `
