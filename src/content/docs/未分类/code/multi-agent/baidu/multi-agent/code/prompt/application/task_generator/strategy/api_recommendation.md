---
title: "当前目标需求"
description: "当前分析步骤：接口粗筛与推荐"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\strategy\\api_recommendation.md"
---
当前分析步骤：**接口粗筛与推荐**

- **目标**：基于需求的理解和解析、结合初步圈定的接口集合等信息
  - 如果给定的候选api只有一个，则直接锁定该api即可
  - 如果给定的候选api是空，则请自行梳理项目的所有接口，并根据功能相似性进行推荐
- **结果存储路径**：`.lumos/{{icafe_id}}/candidate_apis.json`。

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

- 拆解的 策略 功能点：

```markdown
{{feature_descs}}
```

# 初步圈定的接口集合

```json
{{candidate_apis}}
```

# 反思与修复
- 输出结果必须为严格符合 JSON 标准且可直接由解析器解析的文本，字符串中的双引号需正确转义以避免解析错误。
- 在输出前应**自检与修正**，确保结构完整、字段正确、内容合理后再生成最终结果。
