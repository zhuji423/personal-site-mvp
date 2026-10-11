---
title: "add-member — 添加文档成员"
description: "为指定文档添加一个或多个成员，并设置其角色。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\add_member.md"
---
# add-member — 添加文档成员

为指定文档添加一个或多个成员，并设置其角色。

## CLI 用法

```bash
python3 scripts/ku_operator.py add-member --doc-id <文档ID> --usernames <用户名列表> [--role <角色>]
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--usernames` | 是 | 用户名，多个用逗号分隔（如 `user1,user2`） |
| `--role` | 否 | 角色，可选 `DocReader` / `DocEditor`（或 `DocMember`） / `DocAdmin`，默认 `DocReader`。`DocEditor` 会自动映射为 API 实际值 `DocMember` |

## 输出说明

返回 JSON 格式结果，操作成功时返回 JSON 中不包含 `error` 字段。

## 使用示例

### 添加单个只读成员

```bash
python3 scripts/ku_operator.py add-member \
  --doc-id OQAehZAod_HVHC \
  --usernames zhangsan
```

### 添加多个编辑成员

```bash
python3 scripts/ku_operator.py add-member \
  --doc-id OQAehZAod_HVHC \
  --usernames zhangsan,lisi,wangwu \
  --role DocEditor
```

### 添加管理员

```bash
python3 scripts/ku_operator.py add-member \
  --doc-id OQAehZAod_HVHC \
  --usernames admin_user \
  --role DocAdmin
```
