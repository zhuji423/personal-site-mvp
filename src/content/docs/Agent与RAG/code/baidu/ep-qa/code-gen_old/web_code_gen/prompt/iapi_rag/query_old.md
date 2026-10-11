---
title: "输出格式："
description: "你的任务是分析接口生成任务，识别核心信息，并拆解为代码检索任务，以便获取相关代码上下文辅助接口生成："
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\iapi_rag\\query_old.md"
---
你的任务是分析接口生成任务，识别核心信息，并拆解为代码检索任务，以便获取相关代码上下文辅助接口生成：

拆解最多 `4` 个独立的检索任务，满足以下要求：
- 仅关注接口逻辑涉及的信息，不进行扩展或假设
- 可独立检索，不依赖其他任务
- 必须形成明确的检索关键词

# 输出格式：
```json
{
    "thoughts": "思考过程（注意要言简意赅）",
    "sub_queries": ["检索子任务列表"]
}
```

下面我们来看几个例子：
用户的需求：接口路径：/student/getInfoById
回答：
```json
{
    "thoughts": "参考同路径/student下接口的实现，通过id获取学生信息",
    "sub_queries": ["路由/student路径下已注册的接口", "通过id获取学生信息"]
}
```

用户的需求：接口路径：/generateMonthlyReport，接口描述：将每一天的价格数据聚合生成月度报表（参考模板）并发邮件给xx
回答：
```json
{
    "thoughts": "参考已有接口的实现，涉及报表生成逻辑",
    "sub_queries": ["已注册的接口示例", "获取每天价格数据", "月度报表模板的处理", "发送邮件的实现"]
}
```

用户的需求：接口路径：/s/d/notification/sendBulk
回答：
```json
{
    "thoughts": "逻辑空缺，参考同路径/s/d/notificatio下接口的实现",
    "sub_queries": ["路由/s/d/notificatio路径下注册的接口"]
}
```

现在让我们开始一个新的任务:
下面是用户的需求：
{{query}}