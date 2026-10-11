---
title: "query-repo — 查询知识库目录"
description: "查询知识库的目录结构，以文本树形格式输出，支持分页。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\query_repo.md"
---
# query-repo — 查询知识库目录

查询知识库的目录结构，以文本树形格式输出，支持分页。

## CLI 用法

```bash
# 查询根目录（默认行为）
python3 scripts/ku_operator.py query-repo --repo-guid <知识库ID>

# 查询某个目录下的直接子文档
python3 scripts/ku_operator.py query-repo --repo-guid <知识库ID> --parent-doc-guid <父文档ID>

# 大目录翻页
python3 scripts/ku_operator.py query-repo --repo-guid <知识库ID> --page 2
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--repo-guid` | 是 | 知识库 ID |
| `--parent-doc-guid` | 否 | 父文档 ID，不传则默认查询**根目录**下的直接子文档 |
| `--page` | 否 | 页码，默认 1（每页固定 100 条） |

## 输出说明

以文本树形格式输出，示例：

```
知识库 Xw0t0FBvVy 根目录（共 3 项）：

📄 欢迎使用 (GgD6PTVjSmZEC3)
📁 浏览器相关 (gsrJkBZ6XlyGRl) [2 子文档]
📄 接口说明 (vtUh01DEnyYDA6)
```

- `📁` 表示有子文档（可通过其 docGuid 作为 `--parent-doc-guid` 进一步展开查看）
- `📄` 表示叶子文档
- 括号内为 `docGuid`，可直接用于后续的 `query-content`、`create-doc`、`move-doc` 等操作
- 当目录内容超过一页时，末尾会提示使用 `--page` 翻页

## 使用示例

### 查询根目录

```bash
python3 scripts/ku_operator.py query-repo --repo-guid Xw0t0FBvVy
```

### 展开子目录

```bash
python3 scripts/ku_operator.py query-repo \
  --repo-guid Xw0t0FBvVy \
  --parent-doc-guid gsrJkBZ6XlyGRl
```
