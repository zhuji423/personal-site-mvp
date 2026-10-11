---
title: "query-content — 查询文档内容"
description: "查询知识库文档内容，自动转换为 Markdown 格式输出，并可自动下载文档中引用的图片和附件。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\query_content.md"
---
# query-content — 查询文档内容

查询知识库文档内容，自动转换为 Markdown 格式输出，并可自动下载文档中引用的图片和附件。

## CLI 用法

```bash
python3 scripts/ku_operator.py query-content --doc-id <文档ID>
python3 scripts/ku_operator.py query-content --url <文档URL>

# 禁用自动下载资源
python3 scripts/ku_operator.py query-content --doc-id <文档ID> --no-download-assets

# 指定资源保存目录
python3 scripts/ku_operator.py query-content --doc-id <文档ID> --save-assets-dir ./my_assets

# 输出原始 JSON（含 blockId，用于 edit-content 操作）
python3 scripts/ku_operator.py query-content --doc-id <文档ID> --raw-json
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 与 `--url` 二选一 | 文档 ID |
| `--url` | 与 `--doc-id` 二选一 | 文档 URL |
| `--save-assets-dir` | 否 | 图片/附件保存目录，默认 `./ku_assets` |
| `--no-download-assets` | 否 | 禁用自动下载图片/附件（默认会自动下载） |
| `--raw-json` | 否 | 输出原始 JSON block 结构（含 blockId），不转换为 Markdown |

## 输出说明

### 默认模式（Markdown 输出）

- 直接输出 **Markdown 格式** 的文档内容（通过内部 jsonToMd 服务自动转换），可直接阅读
- **自动资源下载**：脚本会自动提取 Markdown 中的远程图片和附件 URL，下载到本地 `{save-assets-dir}/{doc_id}/` 目录，并将 Markdown 中的远程 URL 替换为本地路径。下载摘要会输出到 stderr

> **重要**：读取文档后，请关注 stderr 中输出的资源下载摘要。如果文档包含图片，这些图片已下载到本地，在分析文档时应结合图片内容（使用 Read 工具读取图片文件）进行理解，不要忽略图片中的信息。

### --raw-json 模式

- 输出文档内容的 **原始 JSON block 数组**，每个 block 包含 `blockId`、`type` 等完整字段
- 不经过 jsonToMd 转换，不下载资源
- 主要用于获取 `blockId` 以配合 `edit-content` 命令进行精确编辑（如表格替换、定点插入/删除）

输出格式示例：

```json
[
  {
    "type": "heading",
    "level": 2,
    "blockId": "docyg-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "children": [{"text": "标题内容"}]
  },
  {
    "type": "paragraph",
    "blockId": "docyg-yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
    "children": [{"text": "段落内容"}]
  },
  {
    "type": "table",
    "blockId": "docyg-zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz",
    "data": {"headless": true, "width": [150, 150]},
    "children": [...]
  }
]
```

## 使用示例

### 通过 doc-id 查询

```bash
python3 scripts/ku_operator.py query-content --doc-id OQAehZAod_HVHC
```

### 通过完整 URL 查询

```bash
python3 scripts/ku_operator.py query-content \
  --url "https://ku.baidu-int.com/knowledge/HFVrC2hT9H/pKzYIZbmZx/B8wSneaLSC/OQAehZAod_HVHC"
```
