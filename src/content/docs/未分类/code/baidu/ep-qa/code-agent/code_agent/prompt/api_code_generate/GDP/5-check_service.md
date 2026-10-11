---
title: "service层相关检索知识"
description: "当前代码库{{repo}} 当前为生成过程中的中间任务：检查并判断service层初始化入口及方法是否已实现。 请参考以下已检索到的 service 层及其相关代码（见下方 service层相关检索知识），结合历史已完成的任务代码，完成业务"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\prompt\\api_code_generate\\GDP\\5-check_service.md"
---
当前代码库{{repo}}
当前为生成过程中的中间任务：检查并判断service层初始化入口及方法是否已实现。
请参考以下已检索到的 service 层及其相关代码（见下方 service层相关检索知识），结合历史已完成的任务代码，完成业务逻辑部分的代码生成：

1. 判断并校验接口service层初始化入口及方法是否已实现。
- 检查接口{{uri}}对应service层初始化入口及方法是否已完整实现。
- 若已实现，则按以下格式输出接口service层初始化入口及方法已实现代码，格式如下：
* 说明：接口{{uri}}对应service层已实现，{简短实现逻辑总结}。
* 文件路径：`{文件路径}`
```go
{接口{{uri}}相关service实现}
```

2. 若service层入口及方法定义未实现，需要在下一步中参考引入更多的知识去生成完整的service层代码，给出service层未实现说明即可，示例如下：
* 说明：尚未检索到接口{{uri}}对应service层实现，需参照更多的检索知识进行生成。

# service层相关检索知识
{{search_context}}

# 已完成任务生成结果参考
{{done_tasks}}