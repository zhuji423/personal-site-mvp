---
title: "可用的MCP工具列表"
description: "上一步候选接口定位结果已存储至：.lumos/{{icafeid}}/candidateapis.json，详情如下："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\api_design.md"
---
# 可用的MCP工具列表
```
{{mcp_configs}}
```

# 任务描述

上一步候选接口定位结果已存储至：`.lumos/{{icafe_id}}/candidate_apis.json`，详情如下：

```json
{{candidate_apis}}
```

当前分析步骤：**接口精筛与变更设计**

- **目标**：基于历史对话分析以及分析的候选接口集合，采用**api-design** skill 分析每个目标接口的核心逻辑及依赖，进行功能点到接口的关系挂载进行精筛，最终完成接口粒度的变更设计；
- **结果存储路径**：`.lumos/{{icafe_id}}/api_design.json`。

# 反思与修复

- 校验输出的合理性与准确性，确保接口挂载与功能点对应正确。
- 确保接口变更设计遵循“优先复用、最小改动”原则。
- 保证变更设计无遗漏，功能点的验收标准得到完整覆盖。
- 输出必须为严格符合 JSON 标准的文本，可直接解析。
- **若字符串中存在字符引用，请使用转义后的双引号\"**.
- 输出字段名称、层级、类型与预定义结构一致，不得遗漏、拼写错误或新增未定义字段。
- 若发现接口挂载错误、结构不符或格式解析失败，应及时修正并重新生成结果。
