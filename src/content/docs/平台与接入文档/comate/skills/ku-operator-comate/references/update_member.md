---
title: "update-member — 更新文档成员角色"
description: "更新文档中已有成员的角色。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\update_member.md"
---
# update-member — 更新文档成员角色

更新文档中已有成员的角色。

## CLI 用法

```bash
python3 scripts/ku_operator.py update-member --doc-id <文档ID> --username <用户名> --role <新角色>
```

## 参数表

| 参数 | 必填 | 说明 |
|------|------|------|
| `--doc-id` | 是 | 文档 ID |
| `--username` | 是 | 用户名（单个） |
| `--role` | 是 | 新角色，可选 `DocReader` / `DocEditor`（或 `DocMember`） / `DocAdmin`。`DocEditor` 会自动映射为 API 实际值 `DocMember` |

## 输出说明

返回 JSON 格式结果，操作成功时返回 JSON 中不包含 `error` 字段。

## 使用示例

### 将成员升级为编辑者

```bash
python3 scripts/ku_operator.py update-member \
  --doc-id OQAehZAod_HVHC \
  --username zhangsan \
  --role DocEditor
```

### 将成员降级为只读

```bash
python3 scripts/ku_operator.py update-member \
  --doc-id OQAehZAod_HVHC \
  --username zhangsan \
  --role DocReader
```
