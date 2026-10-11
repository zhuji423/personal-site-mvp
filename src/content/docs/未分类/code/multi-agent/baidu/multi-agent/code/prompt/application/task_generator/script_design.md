---
title: "任务目标"
description: "基于输入的用户故事描述，提炼出可独立开发、上线、验证的功能点。 每个功能点需体现清晰的系统行为或接口改动方向，且可映射到具体研发任务。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\script_design.md"
---
# 任务目标

基于输入的用户故事描述，提炼出**可独立开发、上线、验证的功能点**。
每个功能点需体现清晰的系统行为或接口改动方向，且可映射到具体研发任务。

# 任务要求

- 内容应仅来源于输入的用户故事描述。
- 允许提炼与重组表达，但禁止臆测、补充或生成原文未出现的新信息。
- **应完整保留需求中的关键细节**。

# 输入数据

- 目标代码库：{{repo}}
- 用户故事描述：
  {{story_descs}}

# 输出格式

- 请严格遵守以下输出格式

```json
[
  {
    "idTag": "格式：功能点{N}，示例：功能点1",
    "featureName": "功能点名称（<=10字）",
    "featureDesc": "功能点概述（<=30字）",
    "linkedStories": ["挂载的需求点标签，示例：需求点1"],
    "todoContent": "markdown格式的待完成的任务详情"
  }
]
```
