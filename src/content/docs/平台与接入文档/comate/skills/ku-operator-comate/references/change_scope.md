---
title: "change-scope — 修改文档公开范围"
description: "修改指定文档的公开/私密范围。需要环境变量 COMATEUSERNAME 作为操作者身份。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\change_scope.md"
---
# change-scope — 修改文档公开范围

修改指定文档的公开/私密范围。需要环境变量 `COMATE_USERNAME` 作为操作者身份。

## CLI 用法

```bash
python3 scripts/ku_operator.py change-scope --doc-id <文档ID> --scope <范围值>
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--scope` | 是 | 公开范围：`5`=公开可读, `6`=公开可编辑, `20`=私密 |

## 输出说明

返回 JSON 格式结果，包含操作状态。

## 使用示例

### 设为公开可读

```bash
python3 scripts/ku_operator.py change-scope \
  --doc-id OQAehZAod_HVHC \
  --scope 5
```

### 设为私密

```bash
python3 scripts/ku_operator.py change-scope \
  --doc-id OQAehZAod_HVHC \
  --scope 20
```
