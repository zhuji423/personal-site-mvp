---
title: "iCafe 卡片查询 IQL 完整参考"
description: "所有请求需要 x-ac-Authorization header。Token 获取优先级："
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\auto-commit-comate\\references\\query_reference.md"
---
# iCafe 卡片查询 IQL 完整参考

## API 端点

### 条件查询卡片

```
GET {base_url}/api/spaces/{space_id}/cards?iql={iql_expression}
```

**请求参数：**

| 参数 | 位置 | 类型 | 必填 | 说明 |
|------|------|------|------|------|
| space_id | path | string | 是 | 空间 ID |
| iql | query | string | 是 | IQL 查询表达式 |
| page | query | int | 否 | 页码 |
| showDetail | query | flag | 否 | 显示详情（传空字符串即可） |
| showAssociations | query | flag | 否 | 显示关联信息 |
| isDesc | query | flag | 否 | 降序排列 |
| order | query | string | 否 | 排序字段 |
| showChildren | query | flag | 否 | 显示子卡片 |
| maxRecords | query | int | 否 | 最大返回数 |
| showOkr | query | flag | 否 | 显示 OKR |
| showAccumulate | query | flag | 否 | 显示累计信息 |

**响应示例：**

```json
{
  "cards": [
    {
      "id": "12345",
      "sequence": "628",
      "title": "示例卡片",
      "type": "Bug",
      "status": "新建",
      "assignee": "dongkexin01",
      "priority": "P1-High",
      "createdAt": "2025-01-15 10:30:00",
      "updatedAt": "2025-01-16 14:20:00"
    }
  ],
  "total": 1,
  "page": 1,
  "pageSize": 20
}
```

### 获取单张卡片

```
GET {base_url}/api/spaces/{space_id}/cards/{card_id}
```

### 查询最近访问空间

```
GET {base_url}/api/v2/space/latest?currentUser={user_id}
```

### 获取空间计划

```
GET {base_url}/api/v2/space/{space_id}/plans
```

## IQL 查询语法完整参考

### 运算符

| 运算符 | 含义 | 适用类型 | 示例 |
|--------|------|----------|------|
| `=` | 等于 | 所有类型 | `类型 = Bug` |
| `!=` | 不等于 | 所有类型 | `状态 != 已完成` |
| `>` | 大于 | 日期、数字、流程状态 | `创建时间 > "2025-01-01"` |
| `<` | 小于 | 日期、数字、流程状态 | `优先级数值 < 3` |
| `>=` | 大于等于 | 流程状态、数字 | `流程状态 >= 开发中` |
| `<=` | 小于等于 | 流程状态、数字 | `流程状态 <= 开发中` |
| `in ()` | 在列表中 | 人员、类型、状态、标签等 | `类型 in (Bug, Story)` |
| `not in ()` | 不在列表中 | 人员、类型、状态、标签等 | `状态 not in (已完成, 已关闭)` |
| `is empty` | 为空 | 所有类型 | `负责人 is empty` |
| `is not empty` | 不为空 | 所有类型 | `截止日期 is not empty` |
| `~` | 包含（模糊匹配） | 标题、文本、关键字、URL | `标题 ~ 登录` |
| `!~` | 不包含 | 标题、文本 | `标题 !~ 测试` |
| `AND` | 逻辑与 | 连接多个条件 | `类型 = Bug AND 状态 = 新建` |
| `OR` | 逻辑或 | 连接多个条件 | `类型 = Bug OR 类型 = Story` |
| `()` | 分组 | 控制优先级 | `(类型 = Bug OR 类型 = Story) AND 负责人 = currentUser` |

### 字段参考

| 字段名 | 类型 | 说明 |
|--------|------|------|
| 类型 | 枚举 | Bug, Story, Task, Epic 等 |
| 负责人 | 人员 | 用户 ID，如 "dongkexin01" |
| 创建人 | 人员 | 用户 ID |
| 流程状态 | 状态枚举 | 新建, 待开发, 开发中, 进行中, 已完成 等 |
| 优先级 | 枚举 | P0-Urgent, P1-High, P2-Medium, P3-Low 等 |
| 创建时间 | 日期 | 格式 "YYYY-MM-DD" 或 "YYYY-MM-DD HH:mm:ss" |
| 更新时间 | 日期 | 格式同上 |
| 截止日期 | 日期 | 格式同上 |
| 标题 | 文本 | 卡片标题 |
| 关键字 | 文本 | 全文搜索关键字 |
| Label | 标签 | 卡片标签 |
| 所属计划 | 树 | 需要完整路径，如 "测试/测试1" |

### 常用查询模式

#### 按类型查询

```
类型 = Bug
类型 in (Bug, Story, Task)
类型 != Epic
```

#### 按人员查询

```
负责人 = currentUser
负责人 = dongkexin01
创建人 = v_liuxiang
负责人 in (user1, user2, user3)
负责人 is empty
```

#### 按状态查询

```
流程状态 = 新建
流程状态 in (新建, 开发中, 待开发, 进行中)
流程状态 <= 开发中
流程状态 != 已完成
```

#### 按时间查询

```
创建时间 > "2025-01-01"
创建时间 > "2025-01-01 00:00:00" AND 创建时间 < "2025-06-30 23:59:59"
更新时间 > "2025-03-01"
```

#### 按内容查询

```
标题 ~ 登录
标题 !~ 测试
关键字 ~ 性能优化
```

#### 组合查询

```
类型 = Bug AND 负责人 = currentUser AND 流程状态 != 已完成
(类型 = Bug OR 类型 = Story) AND 优先级 = P1-High
创建人 = dongkexin01 AND 创建时间 > "2025-01-01" AND 流程状态 in (新建, 开发中)
```

## 认证说明

所有请求需要 `x-ac-Authorization` header。Token 获取优先级：

1. 环境变量 `COMATE_AUTH_TOKEN`
2. 文件 `~/.comate/login`

## 错误码

| HTTP 状态码 | 说明 |
|-------------|------|
| 200 | 成功 |
| 400 | 请求参数错误（如 IQL 语法错误） |
| 401 | 认证失败（token 无效或过期） |
| 403 | 无权限访问该空间 |
| 404 | 空间或卡片不存在 |
| 500 | 服务端错误 |
