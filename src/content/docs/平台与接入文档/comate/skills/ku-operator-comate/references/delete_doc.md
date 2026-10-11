---
title: "delete-doc — 删除文档"
description: "删除指定的知识库文档。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\delete_doc.md"
---
# delete-doc — 删除文档

删除指定的知识库文档。

## CLI 用法

```bash
python3 scripts/ku_operator.py delete-doc --doc-id <文档ID>
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 要删除的文档 ID |

## 输出说明

返回 JSON 格式结果，关键字段：
- `docGuid` — 被删除文档的 ID
- 操作成功时返回 JSON 中不包含 `error` 字段

> 操作者用户名自动从环境变量 `COMATE_USERNAME` 读取，无需手动传入。
>
> **注意**：删除操作不可恢复，执行前请确认目标文档无误。

## 使用示例

```bash
python3 scripts/ku_operator.py delete-doc --doc-id ABC123
```
