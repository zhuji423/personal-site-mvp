---
title: "query-comment — 查询文档评论"
description: "查询指定文档的评论信息。默认同时查询底部评论和划线评论，输出格式化文本。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\query_comment.md"
---
# query-comment — 查询文档评论

查询指定文档的评论信息。默认同时查询底部评论和划线评论，输出格式化文本。

## CLI 用法

```bash
python3 scripts/ku_operator.py query-comment --doc-id <文档ID> [--type all|bottom|side] [--page N] [--page-size N] [--raw-json]
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--type` | 否 | 评论类型：`all`=全部（默认）, `bottom`=底部评论, `side`=划线评论 |
| `--page` | 否 | 页码，默认 1 |
| `--page-size` | 否 | 每页条数，默认 100 |
| `--raw-json` | 否 | 输出原始 JSON（不做格式化） |

## 输出说明

默认输出格式化文本，包含评论摘要和分区展示：

```
文档 D5JiZRULjdEJHR 评论（底部 2 条，划线 1 条）

## 底部评论（2 条）

1. 王哲 (wangzhe12) · 2026-03-20 10:00
   这是一条评论

2. 张三 (zhangsan) · 2026-03-20 11:00
   这是另一条评论
   └─ 李四 (lisi) · 2026-03-20 11:05
      这是一条回复

## 划线评论（1 条）

1. 王哲 (wangzhe12) · 2026-03-20 12:00
   引用: "被标注的文字"
   └─ 张三 (zhangsan) · 2026-03-20 12:05
      针对标注的回复
```

传 `--raw-json` 时输出原始 API 响应 JSON。

## 使用示例

### 查询全部评论（默认）

```bash
python3 scripts/ku_operator.py query-comment \
  --doc-id D5JiZRULjdEJHR
```

### 只查底部评论

```bash
python3 scripts/ku_operator.py query-comment \
  --doc-id D5JiZRULjdEJHR \
  --type bottom
```

### 只查划线评论

```bash
python3 scripts/ku_operator.py query-comment \
  --doc-id D5JiZRULjdEJHR \
  --type side
```

### 输出原始 JSON

```bash
python3 scripts/ku_operator.py query-comment \
  --doc-id D5JiZRULjdEJHR \
  --raw-json
```
