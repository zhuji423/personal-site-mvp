---
title: "move-doc — 移动文档"
description: "移动文档到目标知识库的指定位置。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\move_doc.md"
---
# move-doc — 移动文档

移动文档到目标知识库的指定位置。

## CLI 用法

```bash
python3 scripts/ku_operator.py move-doc --doc-id <文档ID> --to-repo-guid <目标知识库ID>
python3 scripts/ku_operator.py move-doc --doc-id <文档ID> --to-repo-guid <目标知识库ID> --to-parent-guid <目标父目录ID>
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 要移动的文档 ID |
| `--to-repo-guid` | 是 | 目标知识库 ID |
| `--to-parent-guid` | 否 | 目标父目录 ID，不传则移动到根目录 |

## 输出说明

返回 JSON 格式结果，关键字段：
- `docGuid` — 被移动文档的 ID
- 操作成功时返回 JSON 中不包含 `error` 字段

> 操作者用户名自动从环境变量 `COMATE_USERNAME` 读取，无需手动传入。

## 使用示例

### 移动到知识库根目录

```bash
python3 scripts/ku_operator.py move-doc \
  --doc-id ABC123 \
  --to-repo-guid B8wSneaLSC
```

### 移动到指定目录下

```bash
python3 scripts/ku_operator.py move-doc \
  --doc-id ABC123 \
  --to-repo-guid B8wSneaLSC \
  --to-parent-guid XYZ789
```
