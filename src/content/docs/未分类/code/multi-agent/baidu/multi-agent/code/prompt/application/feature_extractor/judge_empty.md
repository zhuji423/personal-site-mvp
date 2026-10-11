---
title: "任务目标"
description: "{{extradocs}}"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\feature_extractor\\judge_empty.md"
---
# 任务目标
判断输入的第三方信息和需求详情有没有实际内容。

# 任务要求
这些第三方信息和需求详情在之后的环节会被用于需求澄清，但在那之前需要你先判断其有没有实际内容。
如果这些信息为空，或是根据EARS语法没有实际内容能提取出用户story和验收标准，则输出0；否则输出1。

# 输入信息

## 补充第三方信息

{{extra_docs}}

## 需求详情

- 需求标题：`{{title}}`
- 需求内容：

```markdown
{{content}}
```

# 输出格式

- 严格遵守以下 JSON 格式输出，禁止输出额外解释
- 注意字符串内引用使用单引号，避免 JSON 无法解析
- 若无任何有效内容，输出 `[]`，**但前提是需确保已逐行扫描确认无遗漏**

```json
{
  "flag": 1/0 // 1表示不为空，0表示为空
}
```