---
title: "controller层检索知识"
description: "当前代码库{{repo}} 当前为接口controller层控制代码生成任务。 请参考以下已检索到的 controller 层相关代码（见下方 controller层检索知识），根据用户提供的目标接口路径 {{uri}}，完成控制器是否已存"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\prompt\\api_code_generate\\GDP\\4-controller.md"
---
当前代码库{{repo}}
当前为接口controller层控制代码生成任务。
请参考以下已检索到的 controller 层相关代码（见下方 controller层检索知识），根据用户提供的目标接口路径 {{uri}}，完成控制器是否已存在的判断与代码生成任务：

1. 判断接口控制器入口及方法是否已实现
- 检查目标路径 {{uri}} 是否已完成控制器入口及方法的实现；
- 若已实现，则按以下格式输出接口控制器已实现入口及方法代码，格式如下：
* 说明：接口{{uri}}控制器已实现，{简短实现说明}。
* 文件路径：`{文件路径}`
```go
{接口{{uri}}相关控制器实现}
```

2. 生成控制器代码（如未实现）：
- 如果未检测到 {{uri}} 的控制器入口及方法的实现代码，请参考历史任务中router层、types层请求体&结构体实现代码、检索上下文中的代码风格与结构，按照系统要求自动生成 controller 层对应的接口控制器初始化、方法实现代码；
- 生成代码应与已有风格保持一致，尽可能复用已有模式与写法。
- 注意新增/修改代码严格按照系统要求[* 步骤描述\n* 文件路径: ``\n```SEARCH/REPLACE block```] 的格式输出。

# controller层检索知识
{{search_context}}

# 已完成任务生成结果参考
{{done_tasks}}

# 目标接口路径：`{{uri}}`