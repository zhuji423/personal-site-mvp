---
title: "query-user-info — 查询当前用户信息"
description: "查询当前登录用户的知识库信息，包括个人知识库 ID 和 URL。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\ku-operator-comate\\references\\query_user_info.md"
---
# query-user-info — 查询当前用户信息

查询当前登录用户的知识库信息，包括个人知识库 ID 和 URL。

## CLI 用法

```bash
python3 scripts/ku_operator.py query-user-info
```

## 参数表

无需任何参数，用户名自动从环境变量 `COMATE_USERNAME` 读取。

## 输出说明

以 JSON 格式输出当前用户的关键信息，示例：

```json
{
  "username": "wangzhe12",
  "nickname": "王哲",
  "email": "wangzhe12@baidu.com",
  "personalRepoGuid": "yxin2LKp-R",
  "personalRepoUrl": "https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/yxin2LKp-R"
}
```

返回结果关键字段：
- `personalRepoGuid` — 个人知识库 ID，可直接用于 `--repo-guid` 参数
- `personalRepoUrl` — 个人知识库 URL

## 使用示例

```bash
python3 scripts/ku_operator.py query-user-info
```
