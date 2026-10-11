---
title: "ITP迁移接口文档"
description: "接口路径: /tree/node/itpMigrate 请求方法: POST 接口功能: 将ITP（Interface Test Platform）平台的测试用例数据迁移到QAMate平台"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\core-migrate\\ITP_MIGRATE_DOCUMENTATION.md"
---
# ITP迁移接口文档

## 接口概述

**接口路径**: `/tree/node/itpMigrate`  
**请求方法**: POST  
**接口功能**: 将ITP（Interface Test Platform）平台的测试用例数据迁移到QAMate平台

### 请求参数

```json
{
  "itpProductId": "ITP产品ID",
  "itpGroupId": "ITP测试组ID",
  "moduleId": "目标模块ID"
}
```

---

## 整体流程图

```
┌─────────────────────┐
│   接收迁移请求      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ TreeNodeController.itpMigrate   │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│     ItpManager.migrate          │
└──────────┬──────────────────────┘
           │
           ├─────────────┬─────────────┬─────────────┐
           ▼             ▼             ▼             │
    ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
    │查询ITP   │  │查询ITP   │  │查询标签映射  │   │
    │测试组    │  │标签      │  │关系          │   │
    └─────┬────┘  └─────┬────┘  └───────┬──────┘   │
          │             │               │           │
          └─────────────┴───────────────┘           │
                        │                           │
                        ▼                           │
              ┌──────────────────┐                  │
              │创建QAMate标签    │                  │
              └────────┬─────────┘                  │
                       │                            │
                       ▼                            │
              ┌──────────────────┐                  │
              │获取QAMate测试组  │                  │
              └────────┬─────────┘                  │
                       │                            │
                       ▼                            │
              ┌──────────────────┐                  │
              │遍历ITP测试组     │◄─────────────────┘
              └────────┬─────────┘
                       │
       ┌───────────────┼───────────────┬─────────────────┐
       ▼               ▼               ▼                 ▼
  ┌─────────┐   ┌──────────┐   ┌──────────┐   ┌──────────────┐
  │创建树   │   │提取Host  │   │提取全局  │   │迁移测试节点  │
  │节点     │   │配置      │   │变量      │   │              │
  └────┬────┘   └────┬─────┘   └────┬─────┘   └──────┬───────┘
       │             │              │                 │
       └─────────────┴──────────────┴─────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │创建迁移日志      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │创建环境配置      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │更新树节点关系    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   迁移完成       │
                    └──────────────────┘
```

---

## 核心文件及功能说明

### 1. TreeNodeController.java

**文件路径**: `/src/main/java/com/baidu/qamate/core/controller/TreeNodeController.java`

**职责**: 
- 接收HTTP请求
- 解析请求参数
- 调用业务逻辑层

**关键代码**:
```java
@PostMapping("/itpMigrate")
public Response<?> itpMigrate(@RequestBody JSONObject body) throws Exception {
    Integer itpProductId = body.getInteger("itpProductId");
    Integer itpGroupId = body.getInteger("itpGroupId");
    Integer moduleId = body.getInteger("moduleId");
    itpManager.migrate(itpProductId, itpGroupId, moduleId);
    return Response.success(null);
}
```

---

### 2. ItpManager.java

**文件路径**: `/src/main/java/com/baidu/qamate/core/migrate/itp/ItpManager.java`

**职责**: 
- 核心迁移逻辑协调器
- 数据转换与映射
- 环境配置创建

#### 主要方法说明

##### 2.1 migrate()

**功能**: 主迁移流程入口

**流程图**:
```
开始迁移
   │
   ▼
查询ITP测试组数据
   │
   ▼
查询ITP标签数据
   │
   ▼
建立标签映射关系
   │
   ▼
获取QAMate测试组
   │
   ▼
初始化环境配置集合
   │
   ▼
遍历测试组 ──────┐
   │             │
   ▼             │
创建树节点TreeNode│
   │             │
   ▼             │
提取Host配置     │
   │             │
   ▼             │
提取全局变量     │
   │             │
   ▼             │
调用migrateNode  │
迁移用例         │
   │             │
   ▼             │
是否还有测试组? ─┘
   │ 否
   ▼
创建线下环境
   │
   ▼
创建线上环境
   │
   ▼
更新树节点关系
   │
   ▼
保存迁移日志
   │
   ▼
迁移完成
```

**关键步骤**:
1. 查询ITP测试组列表
2. 创建QAMate标签映射
3. 为每个测试组创建树节点
4. 提取并创建服务器配置
5. 提取并创建参数配置
6. 调用`migrateNode()`迁移具体用例
7. 创建线上/线下环境
8. 保存迁移日志

---

##### 2.2 migrateNode()

**功能**: 迁移测试节点及步骤

**流程图**:
```
                    开始迁移节点
                         │
                         ▼
                  查询所有测试节点
                         │
                         ▼
                   分类测试节点
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    用例节点      Setup/Teardown节点   禁用节点
        │                │                │
        ▼                ▼                ▼
  创建CaseNode实体   创建Hook节点    标记禁用信息
        │                │                │
        ▼                ▼                │
  批量保存CaseNode   关联父节点           │
        │                │                │
        ▼                │                │
   创建CaseDetail       │                │
        │                │                │
        ▼                │                │
  构建节点层级关系      │                │
        │                │                │
        ▼                │                │
  更新childrenIds       │                │
        │                │                │
        └────────────────┴────────────────┘
                         │
                         ▼
                  创建节点步骤Step
                         │
                         ▼
              更新detail的stepIndex
                         │
                         ▼
                   保存迁移日志
                         │
                         ▼
                  节点迁移完成
```

**关键步骤**:
1. 查询所有测试节点（用例、Setup、Teardown）
2. 创建CaseNode实体并保存
3. 创建CaseDetail关联信息
4. 构建父子节点关系
5. 处理Setup/Teardown（Hook节点）
6. 处理禁用节点
7. 调用`createNodeStep()`创建测试步骤

---

##### 2.3 createNodeStep()

**功能**: 创建HTTP和SQL测试步骤

**流程图**:
```
                     开始创建步骤
                          │
                          ▼
                  判断节点类型
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
    HTTP步骤(type=4)               SQL步骤(type=5)
          │                               │
          ▼                               ▼
   调用genHttpStepInfo            调用genSQLStepInfo
          │                               │
          ▼                               ▼
    解析URL和Path                  迁移数据库配置
          │                               │
          ▼                               ▼
     转换请求参数                    转换SQL语句
          │                               │
          ▼                               ▼
      转换请求头                     转换变量提取
          │                               │
          ▼                               ▼
       转换Body                     创建线上SQL步骤
          │                               │
          ▼                               ▼
       转换断言                     创建线下SQL步骤
          │                               │
          ▼                               │
   创建HTTP步骤实体                       │
          │                               │
          └───────────────┬───────────────┘
                          ▼
                    批量保存步骤
                          │
                          ▼
                   步骤创建完成
```

**关键步骤**:
1. 遍历HTTP/SQL节点
2. 对于HTTP节点：
   - 解析请求接口URL
   - 转换请求参数和Header
   - 转换Body（支持form-data、json、xml等）
   - 转换断言规则
3. 对于SQL节点：
   - 迁移数据库配置
   - 分别创建线上和线下步骤
4. 批量保存步骤实体

---

##### 2.4 genHttpStepInfo()

**功能**: 生成HTTP步骤的配置信息

**流程图**:
```
                开始生成HTTP配置
                        │
                        ▼
                    解析URL
                        │
                        ▼
            是否包含服务器变量?
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
        提取服务器ID          使用默认服务器
            │                       │
            └───────────┬───────────┘
                        ▼
                    转换Path
                        │
                        ▼
                  替换变量引用
                        │
                        ▼
              转换请求参数Params
                        │
                        ▼
               转换请求头Header
                        │
                        ▼
                解析Body类型
                        │
        ┌───────┬───────┼───────┬───────┐
        ▼       ▼       ▼       ▼       ▼
    bodyType=1  =9     =2      =5    其他
        │       │       │       │       │
        ▼       ▼       ▼       ▼       ▼
    form-data  url-  raw-json raw-xml none
               encoded
        │       │       │       │       │
        └───────┴───────┴───────┴───────┘
                        │
                        ▼
                  转换断言配置
                        │
                        ├─> assertText断言
                        ├─> assertJson断言
                        └─> assertJsonSchema断言
                        │
                        ▼
              设置超时和重定向
                        │
                        ▼
                 生成JSON字符串
                        │
                        ▼
                    返回配置
```

**变量转换规则**:
- `${config.XXX}` → `{{groupId-XXX}}`
- `${XXX}` → `{{groupId-XXX}}`
- `${/path/to/value}` → `{{value}}`
- `${&object.field}` → `{{field}}`

---

##### 2.5 genSQLStepInfo()

**功能**: 生成SQL步骤的配置信息

**流程图**:
```
        开始生成SQL配置
                │
                ▼
           解析SQL语句
                │
                ▼
         提取数据库名称
                │
                ▼
           isOnline?
                │
        ┌───────┴───────┐
        ▼               ▼
   迁移线上数据库   迁移线下数据库
        │               │
        └───────┬───────┘
                ▼
       调用migrateItpDB
                │
                ▼
          设置数据库ID
                │
                ▼
           设置SQL语句
                │
                ▼
        生成变量提取配置
                │
                ▼
        生成后置操作配置
                │
                ▼
         生成JSON字符串
                │
                ▼
            返回配置
```

---

##### 2.6 migrateItpDB()

**功能**: 迁移ITP数据库配置

**流程图**:
```
         开始迁移数据库
                │
                ▼
       从SQL提取数据库名
                │
                ▼
       查询ITP数据库配置
                │
                ▼
          是否已迁移?
                │
        ┌───────┴────────┐
        ▼                ▼
   返回已迁移的ID    解析数据库地址
        ▲                │
        │                ▼
        │          构建数据库配置
        │                │
        │                ▼
        │            解密密码
        │                │
        │                ▼
        │         判断环境类型
        │                │
        │        ┌───────┴────────┐
        │        ▼                ▼
        │   创建线下数据库    创建线上数据库
        │        │                │
        │        └───────┬────────┘
        │                ▼
        │        调用createDb API
        │                │
        │                ▼
        │          缓存数据库ID
        │                │
        └────────────────┘
                │
                ▼
          返回数据库ID
```

---

##### 2.7 createModuleServer()

**功能**: 创建模块服务器配置

**流程图**:
```
       开始创建服务器
              │
              ▼
         解析地址列表
              │
              ▼
         遍历地址 ◄─────┐
              │         │
              ▼         │
        是否已存在?      │
              │         │
      ┌───────┴────────┐│
      ▼                ▼│
  复用已有服务器  创建新服务器实体
      │                │
      │                ▼
      │           保存服务器
      │                │
      │                ▼
      │       生成EnvDetailServerVo
      │                │
      │                ▼
      │         添加到映射表
      │                │
      └────────┬───────┘
               ▼
        构建服务器映射
               │
               ▼
        是否还有地址? ───┘
               │ 否
               ▼
        返回服务器映射
```

---

##### 2.8 createModuleParams()

**功能**: 创建模块参数配置

**流程图**:
```
       开始创建参数
            │
            ▼
     解析全局变量JSON
            │
            ▼
     解析线上变量JSON
            │
            ▼
       遍历参数 ◄────────┐
            │            │
            ▼            │
      是否已存在?         │
            │            │
      ┌─────┴─────┐      │
      ▼           ▼      │
    跳过    创建参数实体   │
      │           │      │
      │           ▼      │
      │       保存参数    │
      │           │      │
      │           ▼      │
      │   生成线下ParamInfoVo
      │           │      │
      │           ▼      │
      │   是否有线上配置? │
      │           │      │
      │     ┌─────┴─────┐│
      │     ▼           ▼│
      │ 生成线上     添加到│
      │ ParamInfoVo  映射表│
      │     │           ││
      │     └─────┬─────┘│
      │           │      │
      └───────────┤      │
                  ▼      │
          是否还有参数? ──┘
                  │ 否
                  ▼
           返回参数映射
```

---

##### 2.9 createEnv()

**功能**: 创建环境配置

**流程图**:
```
       开始创建环境
            │
            ▼
  检查是否已存在同名环境
            │
            ▼
        是否存在?
            │
      ┌─────┴─────┐
      ▼           ▼
   直接返回   创建环境实体
                  │
                  ▼
            设置环境名称
                  │
                  ▼
             设置模块ID
                  │
                  ▼
       设置OS类型为服务端
                  │
                  ▼
         构建环境配置JSON
                  │
                  ├─> 添加服务器列表
                  │
                  └─> 添加参数列表
                  │
                  ▼
            保存环境实体
                  │
                  ▼
           环境创建完成
```

---

## 数据模型关系图

### ITP数据模型
```
ITP_TEST_GROUP (测试组)
    │
    ├──> ITP_TEST_NODE (测试节点) [1对多]
    │       │
    │       └──> ITP_TEST_STEP (测试步骤) [1对多]
    │               │
    │               └──> ITP_DATABASE (数据库配置) [多对1]
    │
    └──> ITP_TAG_MAP (标签映射) [1对多]
            │
            └──> ITP_TAG (标签) [多对1]
```

### QAMate数据模型
```
QAMATE_MODULE (模块)
    │
    ├──> QAMATE_TREE_NODE (树节点) [1对多]
    │       │
    │       └──> QAMATE_CASE_NODE (用例节点) [1对多]
    │               │
    │               └──> QAMATE_CASE_DETAIL (用例详情) [1对1]
    │                       │
    │                       └──> QAMATE_CASE_STEP (用例步骤) [1对多]
    │
    ├──> QAMATE_SERVER (服务器) [1对多]
    │
    ├──> QAMATE_PARAMS (参数) [1对多]
    │
    ├──> QAMATE_ENV (环境) [1对多]
    │
    └──> QAMATE_TAG (标签) [1对多]
```

### 迁移映射关系
```
ITP_TEST_GROUP ───────────> QAMATE_TREE_NODE
       │                           │
       ▼                           ▼
ITP_TEST_NODE ────────────> QAMATE_CASE_NODE
       │                           │
       ▼                           ▼
ITP_TEST_STEP ────────────> QAMATE_CASE_STEP
       │
       ▼
ITP_TAG ──────────────────> QAMATE_TAG
       │
       ▼
ITP_DATABASE ─────────────> QAMATE_DB_CONFIG
```

---

## 关键实体说明

### ITP侧实体

| 实体 | 说明 |
|-----|------|
| TbTestGroupEntity | ITP测试组，包含用例集合 |
| TbTestNodeEntity | ITP测试节点，包含用例/步骤 |
| TbDataMigrationOperationEntity | ITP操作数据，包含HTTP/SQL步骤信息 |
| TbTagEntity | ITP标签 |
| TbTagMapEntity | ITP标签映射关系 |
| TbDatabaseEntity | ITP数据库配置 |

### QAMate侧实体

| 实体 | 说明 |
|-----|------|
| TreeNodeEntity | 树节点，组织用例结构 |
| CaseNodeEntity | 用例节点，表示单个用例 |
| CaseNodeDetailEntity | 用例详情，关联OS类型 |
| CaseNodeStepEntity | 用例步骤，包含具体操作 |
| ServerEntity | 服务器配置 |
| ParamsEntity | 参数配置 |
| EnvEntity | 环境配置 |
| TagEntity | 标签 |

---

## 步骤类型映射

### ITP节点类型

| Type | 说明 |
|------|------|
| 0 | ROOT节点 |
| 1 | Suite（测试套件） |
| 2 | Case（测试用例） |
| 3 | Step（步骤容器） |
| 4 | HTTP步骤 |
| 5 | SQL步骤 |
| 6 | Setup（前置操作） |
| 7 | Teardown（后置操作） |

### QAMate步骤类型

| StepType | 说明 |
|----------|------|
| 1001 | HTTP接口步骤 |
| 1101 | SQL数据库步骤 |

---

## 数据转换规则

### 1. URL转换规则

**ITP格式**:
```
${ITP_HOST_0}/api/endpoint
```

**QAMate格式**:
```
serverId: 对应的服务器ID
path: /api/endpoint
```

### 2. 变量引用转换

| ITP格式 | QAMate格式 | 说明 |
|---------|------------|------|
| `${config.VAR}` | `{{groupId-VAR}}` | 配置变量 |
| `${VAR}` | `{{groupId-VAR}}` | 全局变量 |
| `${/path/to/value}` | `{{value}}` | JSON路径引用 |
| `${&object.field}` | `{{field}}` | 对象字段引用 |

### 3. 断言转换

| ITP比较类型 | QAMate类型码 | 说明 |
|------------|-------------|------|
| `in` | 1 | 包含 |
| `//` | 2 | 正则匹配 |
| `==` | 3 | 等于 |
| `>` | 4 | 大于 |
| `<` | 5 | 小于 |
| `>=` | 6 | 大于等于 |
| `<=` | 7 | 小于等于 |
| `!=` | 8 | 不等于 |

### 4. Body类型转换

| ITP bodyType | QAMate type | 说明 |
|--------------|-------------|------|
| 1 | 2 | form-data |
| 9 | 3 | x-www-form-urlencoded |
| 2 | 4 | raw-json |
| 5 | 5 | raw-xml |

---

## 依赖服务说明

### 核心Service层

| Service | 功能 |
|---------|------|
| TreeNodeService | 树节点管理 |
| CaseNodeService | 用例节点管理 |
| CaseNodeDetailService | 用例详情管理 |
| CaseNodeStepService | 用例步骤管理 |
| GroupService | 测试组管理 |
| ServerService | 服务器管理 |
| ParamsService | 参数管理 |
| EnvService | 环境管理 |
| TagService | 标签管理 |

### ITP数据查询Service

| Service | 功能 |
|---------|------|
| TbTestGroupService | 查询ITP测试组 |
| TbTestNodeService | 查询ITP测试节点 |
| TbDataMigrationOperationService | 查询ITP操作数据 |
| TbTagService | 查询ITP标签 |
| TbTagMapService | 查询ITP标签映射 |
| TbDataBaseService | 查询ITP数据库配置 |
| ItpMigrateLogService | 迁移日志管理 |

---

## 完整调用链路图

```
客户端                TreeNodeController      ItpManager              ITP数据服务         QAMate数据服务      外部API
  │                          │                    │                        │                    │              │
  │ POST /tree/node/itpMigrate                    │                        │                    │              │
  ├─────────────────────────>│                    │                        │                    │              │
  │                          │                    │                        │                    │              │
  │                          │ migrate(...)       │                        │                    │              │
  │                          ├───────────────────>│                        │                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 查询测试组              │                    │              │
  │                          │                    ├───────────────────────>│                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │<─ 返回测试组列表 ──────┤                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 查询标签                │                    │              │
  │                          │                    ├───────────────────────>│                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │<─ 返回标签列表 ────────┤                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建标签                │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │                        │                    │              │
  │                          │                    │<─ 返回标签映射 ────────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 获取目标测试组          │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │                        │                    │              │
  │                          │                    │<─ 返回测试组信息 ──────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │【循环：遍历每个ITP测试组】                   │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建TreeNode            │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │<─ 返回TreeNode ID ─────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建Server配置          │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │<─ 返回Server ID ───────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建Params配置          │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │<─ 返回Params ID ───────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │ migrateNode()          │                    │              │
  │                          │                    │────┐                   │                    │              │
  │                          │                    │<───┘                   │                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 查询测试节点            │                    │              │
  │                          │                    ├───────────────────────>│                    │              │
  │                          │                    │<─ 返回节点列表 ────────┤                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │【循环：遍历测试节点】   │                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建CaseNode            │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │<─ 返回CaseNode ID ─────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建CaseDetail          │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │<─ 返回Detail ID ───────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │【循环：遍历HTTP/SQL步骤】                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ genHttpStepInfo()      │                    │              │
  │                          │                    │ 或 genSQLStepInfo()    │                    │              │
  │                          │                    │────┐                   │                    │              │
  │                          │                    │<───┘                   │                    │              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建数据库配置(SQL步骤) │                    │              │
  │                          │                    ├────────────────────────────────────────────────────────────>│
  │                          │                    │<─ 返回数据库ID ────────────────────────────────────────────┤
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建CaseStep            │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │<─ 返回Step ID ─────────────────────────────┤              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 更新节点关系            │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建线下环境            │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 创建线上环境            │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │                        │                    │              │
  │                          │                    │ 保存迁移日志            │                    │              │
  │                          │                    ├────────────────────────────────────────────>│              │
  │                          │                    │                        │                    │              │
  │                          │<─ 迁移完成 ────────┤                        │                    │              │
  │                          │                    │                        │                    │              │
  │<─ 返回成功响应 ──────────┤                    │                        │                    │              │
  │                          │                    │                        │                    │              │
```

---

## 特殊处理说明

### 1. Hook节点处理

Setup和Teardown节点（type=6,7）会被转换为QAMate的Hook节点：
- Setup → hookType=1（前置）
- Teardown → hookType=2（后置）

### 2. 禁用节点处理

ITP中status=1的节点会被标记为禁用，在attr字段中添加：
```json
{
  "disabledInfo": {
    "status": true,
    "type": 1,
    "message": "禁用"
  }
}
```

### 3. 数据库密码解密

ITP数据库密码使用`ITPDecryptUtil.decrypt()`进行解密后再迁移。

### 4. 时间戳转换

ITP使用毫秒级时间戳，QAMate使用秒级时间戳，需要转换：
```java
millis / 1000
```

---

## 错误处理

### 主要异常场景

1. **ITP数据不存在**: 查询不到对应的测试组或节点
2. **数据库迁移失败**: 无法提取数据库名称或创建失败
3. **API调用失败**: 创建数据库、Hook等外部API调用失败
4. **数据格式错误**: JSON解析失败、格式不匹配等

### 日志记录

所有关键步骤都有日志记录，包括：
- 迁移开始/结束
- 节点创建
- 步骤转换
- API调用结果
- 异常信息

---

## 性能优化点

1. **批量保存**: 使用`saveBatch()`批量保存实体，减少数据库交互
2. **映射缓存**: 使用Map缓存标签、服务器、参数等映射关系
3. **数据库缓存**: `itpDbMap`缓存已迁移的数据库配置，避免重复创建

---

## 配置说明

### 外部API地址

```java
BASE_ENV = "https://qamate.baidu-int.com"
pioneerURL = BASE_ENV + "/core/module/db/create"
pioneerHookURL = BASE_ENV + "/core/case/node/hook/create"
pioneerCaseUpdateURL = BASE_ENV + "/core/case/node/update"
```

### API Token

```java
QAMate-Token: super-9a796933bf024ebfa0420dce6f864a51
```

---

## 使用示例

### 请求示例

```bash
curl -X POST http://localhost:8080/tree/node/itpMigrate \
  -H "Content-Type: application/json" \
  -d '{
    "itpProductId": 123,
    "itpGroupId": 456,
    "moduleId": 789
  }'
```

### 响应示例

```json
{
  "code": 0,
  "message": "success",
  "data": null
}
```

---

## 迁移日志

迁移完成后会在`itp_migrate_log`表中记录：

| 字段 | 说明 |
|------|------|
| module_id | 模块ID |
| case_type | 类型（1=TreeNode, 2=CaseNode） |
| old_value | ITP侧ID |
| new_value | QAMate侧ID |
| create_time | 创建时间 |

---

## 总结

该接口实现了从ITP到QAMate的完整测试用例迁移，包括：

✅ 测试组和用例结构迁移  
✅ HTTP接口测试步骤迁移  
✅ SQL数据库测试步骤迁移  
✅ 服务器配置迁移  
✅ 参数配置迁移  
✅ 环境配置创建  
✅ 标签关系迁移  
✅ Setup/Teardown处理  
✅ 断言规则转换  
✅ 变量引用转换  
✅ 迁移日志记录  

整个迁移过程自动化程度高，数据转换规则清晰，具有良好的可维护性和扩展性。

