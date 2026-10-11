---
title: "query-recent-view — 查询文档浏览记录"
description: "查询指定文档的最近浏览记录，输出格式化文本。可按时间范围过滤，支持分页。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\query_recent_view.md"
---
# query-recent-view — 查询文档浏览记录

查询指定文档的最近浏览记录，输出格式化文本。可按时间范围过滤，支持分页。

## CLI 用法

```bash
python3 scripts/ku_operator.py query-recent-view --doc-id <文档ID> [--begin-time TIME] [--end-time TIME] [--page N] [--page-size N] [--raw-json]
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--begin-time` | 否 | 起始时间，支持格式：`YYYY-MM-DD`、`YYYY-MM-DD HH:MM`、`YYYY-MM-DD HH:MM:SS` |
| `--end-time` | 否 | 结束时间，格式同上 |
| `--page` | 否 | 页码，默认 1 |
| `--page-size` | 否 | 每页条数，默认 100 |
| `--raw-json` | 否 | 输出原始 JSON（不做格式化） |

## 输出说明

默认输出格式化文本，包含浏览统计和记录列表：

```
文档 D5JiZRULjdEJHR 浏览记录（共 24 次，3 位访客）

- 王哲 (wangzhe12) · 2026-03-20 18:00
- 张三 (zhangsan) · 2026-03-20 17:30
- 李四 (lisi) · 2026-03-20 16:00
```

传 `--raw-json` 时输出原始 API 响应 JSON。

## 使用示例

### 查询最近浏览

```bash
python3 scripts/ku_operator.py query-recent-view \
  --doc-id D5JiZRULjdEJHR
```

### 按时间范围查询

```bash
python3 scripts/ku_operator.py query-recent-view \
  --doc-id D5JiZRULjdEJHR \
  --begin-time "2026-03-20" \
  --end-time "2026-03-21"
```

```bash
python3 scripts/ku_operator.py query-recent-view \
  --doc-id D5JiZRULjdEJHR \
  --begin-time "2026-03-20 09:00" \
  --end-time "2026-03-20 18:00"
```

### 输出原始 JSON

```bash
python3 scripts/ku_operator.py query-recent-view \
  --doc-id D5JiZRULjdEJHR \
  --raw-json
```
