---
title: "RAG知识库查询技能"
date: "2026-01-29"
category: "未分类"
source: "F:\\百度工作\\06_comate_aiide_config\\User\\History\\146f966d\\seiW.md"
---
# RAG知识库查询技能

## 技能描述
用于查询RAG知识库，获取ITP平台相关文档和解决方案。

## 知识库列表
| 知识库名称 | ID | 说明 |
|-----------|-----|------|
| faq | 134 | itp 常见问题知识库 |
| api_docs | 133 | itp接口文档列表 |
| product | 135 | itp产品介绍知识库 |
| page_feature | 136 | 页面相关功能介绍知识库 |
| best_practice | 137 | 最佳实践知识库（轮询/批量/延迟/diff场景） |
| advanced | 138 | 进阶功能知识库（扩展函数断言等） |

## 工具调用策略
1. 优先使用MCP工具获取平台实时数据和文档信息
2. 首先查询常见问题知识库(134)判断是否有解决方案
3. 根据问题类型选择对应知识库查询

## 使用方法

### 查询常见问题
```bash
python query_rag.py --action query_faq --query "计划一直不运行怎么办"