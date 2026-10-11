---
title: "目标"
description: "- 需求 ID：{{icafeid}} - 需求标题：{{title}} - 需求原文："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\strategy\\api_collect.md"
---
# 目标
基于当前代码库内容：
1. 分析梳理仓库中所有的api接口，和接口对应的业务功能
2. 分析梳理所有的api接口中，与本次需求相关的接口，并给出理由

# 输入信息
本次的需求内容：

- 需求 ID：{{icafe_id}}
- 需求标题：{{title}}
- 需求原文：

```markdown
{{content}}
```

- 补充的第三方文档：

```markdown
{{extra_info}}
```


# 输出与存储

```json
{
  "all": {
    "/video/external/wechatOfficier/subscribeReward": "业务功能1"
  },
  "candidate": {
    "/video/external/wechatOfficier/subscribeReward": "候选接口理由1"
  }
}
```

其中：
- `all`表示所有接口及对应业务功能
- `candidate`表示与本次需求相关的候选接口及相关性理由


# 反思与修复
- 输出必须为严格符合 JSON 标准的文本，可直接解析。
- **若字符串中存在字符引用，请使用转义后的双引号\"**.
- 输出字段名称、层级、类型与预定义结构一致，不得遗漏、拼写错误或新增未定义字段。
