---
title: "copy-doc — 复制文档"
description: "在指定目录复制出一篇文档的副本。支持跨知识库复制和自定义新标题。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\copy_doc.md"
---
# copy-doc — 复制文档

在指定目录复制出一篇文档的副本。支持跨知识库复制和自定义新标题。

## CLI 用法

```bash
python3 scripts/ku_operator.py copy-doc --doc-id <源文档ID> [--to-repo-guid <目标知识库ID>] [--to-parent-guid <目标父目录ID>] [--new-title "新标题"]
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 待复制的源文档 ID |
| `--to-repo-guid` | 否 | 目标知识库 ID，不传则复制到源文档所在知识库 |
| `--to-parent-guid` | 否 | 目标父目录 ID。不传则与源文档同级；`00000000000000` 表示知识库根目录；不能复制到源文档的下级目录 |
| `--new-title` | 否 | 新文档标题，不传则为原标题 + "的复制" |

## 前置条件

- 数字员工需有源文档的**管理员**权限
- 数字员工需有目标位置的**创建**权限
- 操作者用户名自动从环境变量 `COMATE_USERNAME` 读取

## 输出说明

返回 JSON 格式结果，关键字段：
- `docInfo.docGuid` — 新文档 ID
- `docInfo.url` — 新文档访问 URL
- `docInfo.name` — 新文档标题

## 使用示例

### 在同知识库同目录复制文档

```bash
python3 scripts/ku_operator.py copy-doc \
  --doc-id OQAehZAod_HVHC
```

### 复制到指定知识库根目录并自定义标题

```bash
python3 scripts/ku_operator.py copy-doc \
  --doc-id OQAehZAod_HVHC \
  --to-repo-guid B8wSneaLSC \
  --to-parent-guid 00000000000000 \
  --new-title "接口说明-副本"
```
