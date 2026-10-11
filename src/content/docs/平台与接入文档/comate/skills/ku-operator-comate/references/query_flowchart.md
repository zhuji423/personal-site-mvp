---
title: "query-flowchart — 查询流程图"
description: "查询文档中嵌入的流程图数据。支持自动发现文档中的所有流程图，无需提前知道流程图 ID。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\query_flowchart.md"
---
# query-flowchart — 查询流程图

查询文档中嵌入的流程图数据。支持自动发现文档中的所有流程图，无需提前知道流程图 ID。

## CLI 用法

```bash
# 自动发现文档中所有流程图并查询（推荐）
python3 scripts/ku_operator.py query-flowchart --doc-id <文档ID>

# 指定流程图 ID 查询
python3 scripts/ku_operator.py query-flowchart --doc-id <文档ID> --flowchart-id <流程图ID>

# 保存到文件
python3 scripts/ku_operator.py query-flowchart --doc-id <文档ID> --output out.xml
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--flowchart-id` | 否 | 流程图 ID。不传时自动调用 queryContent 从文档正文中发现所有 `type=diagram` 的节点并逐一查询 |
| `--output` | 否 | 输出文件路径。多个流程图时自动添加序号后缀（如 `out_1.xml`、`out_2.xml`） |

## 自动发现机制

当 `--flowchart-id` 未指定时，脚本会：

1. 调用 `queryContent` API 获取文档正文的 block 列表
2. 筛选 `type=diagram` 的 block，提取其 `id` 字段作为流程图 ID
3. 逐一调用 `queryFlowchart` API 查询每个流程图的数据
4. 输出 agent 友好的结构化结果

## 输出说明

输出包含以下信息：

- **流程图元信息**：文档 ID、流程图 ID、格式
- **节点列表**：每个节点的 ID、形状类型（菱形=判断、矩形=处理、椭圆=开始/结束等）、文字内容
- **连线列表**：每条连线的源节点、目标节点、标签
- **原始 XML**：mxGraph 格式的完整流程图数据

## 使用示例

### 自动发现并查询所有流程图（推荐）

```bash
python3 scripts/ku_operator.py query-flowchart \
  --doc-id D5JiZRULjdEJHR
```

输出示例：
```
## 流程图 #1
- 文档 ID: D5JiZRULjdEJHR
- 流程图 ID: 5282101654e6424c9c6d8e483c856afc
- 格式: mxGraph XML

### 节点 (2 个)
  - [2] diamond (判断): 条件判断
  - [3] process (处理): 执行任务
### 连线 (1 个)
  - [4] 2 → 3 (是)

### 原始 XML
...
```

### 指定流程图 ID 查询

```bash
python3 scripts/ku_operator.py query-flowchart \
  --doc-id D5JiZRULjdEJHR \
  --flowchart-id 5282101654e6424c9c6d8e483c856afc
```

### 保存到文件

```bash
python3 scripts/ku_operator.py query-flowchart \
  --doc-id D5JiZRULjdEJHR \
  --output flowchart.xml
```
