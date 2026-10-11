---
title: "query-permission — 查询文档权限"
description: "查询指定用户对某文档的权限信息。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\query_permission.md"
---
# query-permission — 查询文档权限

查询指定用户对某文档的权限信息。

## CLI 用法

```bash
python3 scripts/ku_operator.py query-permission --doc-id <文档ID> --usernames <用户名列表>
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--usernames` | 是 | 用户名，多个用逗号分隔（如 `user1,user2`） |

## 输出说明

返回 JSON 格式结果，包含每个用户对该文档的权限角色信息。

## 使用示例

### 查询单个用户权限

```bash
python3 scripts/ku_operator.py query-permission \
  --doc-id OQAehZAod_HVHC \
  --usernames zhangsan
```

### 查询多个用户权限

```bash
python3 scripts/ku_operator.py query-permission \
  --doc-id OQAehZAod_HVHC \
  --usernames zhangsan,lisi,wangwu
```
