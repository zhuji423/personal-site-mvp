---
title: "代码库接口路由知识"
description: "当前分析步骤：接口粗筛与推荐"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\api_recommendation.md"
---
# 代码库接口路由知识

```markdown
{{api_rules}}
```

# 可用的MCP工具列表
```
{{mcp_configs}}
```

# 任务目标

当前分析步骤：**接口粗筛与推荐**

- **目标**：基于需求的理解和解析、结合初步圈定的接口集合等信息，采用**api-recommendation** skill 定位目标需求相关的候选接口集合。
- **结果存储路径**：`.lumos/{{icafe_id}}/candidate_apis.json`。

# 历史高度关联需求及其关联变更接口

{{linked_icafes}}

# 当前目标需求

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

- 分析的需求点：

```markdown
{{story_descs}}
```

- 拆解的 Sevrer 功能点：

```markdown
{{feature_descs}}
```

# 初步圈定的接口集合

```json
{{candidate_apis}}
```

# 反思与修复

- 每个步骤的输出需完全符合对应 skill 的结构约束。
- 输出结果必须为严格符合 JSON 标准且可直接由解析器解析的文本，字符串中的双引号需正确转义以避免解析错误。
- 在输出前应**自检与修正**，确保结构完整、字段正确、内容合理后再生成最终结果。
