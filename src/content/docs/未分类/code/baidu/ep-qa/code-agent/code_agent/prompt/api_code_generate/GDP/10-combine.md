---
title: "service层检索知识"
description: "当前代码库{{repo}} 当前为接口生成任务最后一步：完成service层功能代码生成。 参考历史router、controller、types、业务逻辑代码等生成代码，理解各层的调用链路逻辑，生成service层相关代码。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\prompt\\api_code_generate\\GDP\\10-combine.md"
---
当前代码库{{repo}}
当前为接口生成任务最后一步：完成service层功能代码生成。
参考历史router、controller、types、业务逻辑代码等生成代码，理解各层的调用链路逻辑，生成service层相关代码。

注意：所有判断和生成逻辑必须基于当前项目实际结构、自定义封装与已有实现。

1. 判断并校验接口controller、service等层初始化入口及方法是否已完整实现。
- 检查接口{{uri}}对应controller、service等层初始化入口及用户描述功能是否已实现，且能够和上下游方法形成完整调用链路。
- 若用户描述功能已实现且调用链路完整，则说明已实现即可，格式如下：
* 说明：service层入口、结构体等定义以及controller层链路均完整实现。

2. 生成service层功能代码（若controller、service等层入口及用户描述功能未实现 或 用户描述功能函数已实现但需要修改数据获取、处理等逻辑）
- 若controller、service层用户描述功能未实现或已实现但需要调整数据获取、处理等逻辑，则请参考历史任务中router层、controller、service、types层请求体&结构体实现代码、检索上下文中的代码风格与结构，按照系统要求自动生成代码；
- 生成代码应与已有风格保持一致，尽可能复用已有模式与写法。
- 注意新增/修改代码严格按照系统要求[* 步骤描述\n* 文件路径: ``\n```SEARCH/REPLACE block```] 的格式输出。


# service层检索知识
{{search_context}}

# 已完成任务代码生成结果
{{done_tasks}}

# 目标完整需求描述
{{full_requirement}}