---
title: "用例场景覆盖分析策略 (Case Analysis Strategy)"
description: "CaseAnalysisStrategy 是一个用于分析测试用例覆盖情况和冗余检测的策略类。该模块主要功能是分析API接口的测试用例，计算核心参数覆盖情况，并识别冗余的测试用例。"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\01_code\\code\\life_cycle\\README_lifecycle.md"
---
# 用例场景覆盖分析策略 (Case Analysis Strategy)

## 概述

`CaseAnalysisStrategy` 是一个用于分析测试用例覆盖情况和冗余检测的策略类。该模块主要功能是分析API接口的测试用例，计算核心参数覆盖情况，并识别冗余的测试用例。

## 核心处理流程

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              完整处理流程                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Step 1: ITP用例检索                                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 在ITP内检索产品线用例，获取 uri → 关联用例集合 的映射Map           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  Step 2: 知识库查询                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 遍历Step1获取的Map，使用接口uri检索业务知识库                        │   │
│  │ → 获取接口知识 → 确认核心参数                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  Step 3: 用例覆盖计算                                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 遍历关联用例，为每个用例计算：                                       │   │
│  │ → 解析用例参数(query/params/body)                                   │   │
│  │ → 匹配核心参数                                                      │   │
│  │ → 生成该用例覆盖的核心字段详情                                       │   │
│  │ → 存储到Map[node_id → cov_kv]                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  Step 4: 冗余检测                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 遍历Step3获取的Map，计算该用例在整体关联用例内是否存在冗余：          │   │
│  │ → 查找是否存在其他用例的核心参数覆盖完全包含当前用例的覆盖参数        │   │
│  │ → 若存在，进一步比较断言信息                                         │   │
│  │ → 根据结果打标(is_redundancy)                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  Step 5: 结果整合                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ 整合计算结果并返回：                                                 │   │
│  │ → API级别: 覆盖KV列表、未覆盖KV列表、冗余用例数                      │   │
│  │ → 用例级别: 覆盖KV、是否冗余、冗余来源信息                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 详细功能说明

### 1. ITP用例检索 (Step 1)
- 根据产品线信息查询关联的测试用例集合
- 构建 `uri → [case_list]` 的映射关系
- 支持通过一级/二级产品线查询关联的测试产品

### 2. 知识库查询 (Step 2)
- 从业务知识库获取接口的核心参数定义
- 核心参数包含参数名、参数位置、枚举值范围
- 核心参数标识：`x-itp-core-param` 或 `xitpCoreParam`

### 3. 用例覆盖计算 (Step 3)
- 解析用例的请求参数：
  - Query参数
  - FormData参数
  - JSON Body参数(支持嵌套结构)
- 将用例参数值与核心参数枚举值匹配
- 生成该用例覆盖的核心KV详情

### 4. 冗余检测 (Step 4)
**冗余判断条件：**
- 条件A：存在其他用例的核心参数覆盖 **完全包含** 当前用例的覆盖参数
- 条件B：断言信息完全一致(或当前用例无断言)

**断言比较维度：**
- 期望响应断言 (assert_expect)
- 期望响应Map断言 (assert_expect_map)
- 非期望响应Map断言 (assert_unexpect_map)
- SQL断言 (assert_sql)
- Header断言 (assert_header)
- JSON Schema断言 (assert_expect_json_schema)

### 5. 用例运行数据统计
- 获取近30天用例运行次数
- 统计成功运行次数

## 类结构

```
CaseAnalysisStrategy(Strategy)
├── 初始化参数
│   ├── product_level1: 一级业务方向
│   ├── product_level2: 二级业务方向
│   ├── kirin_task_id: Kirin任务ID
│   └── kirin_env: 环境配置
│
├── 主要方法
│   ├── execute(): 执行策略入口
│   ├── api_analysis(): API用例分析(从度量平台获取数据)
│   ├── api_analysis_new(): API用例分析(直接传入参数)
│   ├── case_analysis(): 单个用例分析
│   └── is_redundancy(): 冗余检测
│
└── 辅助方法
    ├── get_api_infos_by_product(): 获取API信息
    ├── get_knowledge_by_uri(): 获取接口知识
    ├── get_qamate_productid(): 获取产品线ID
    ├── get_case_kv_infos(): 获取用例KV信息
    ├── get_core_infos(): 提取核心字段信息
    └── var_replace(): 变量替换处理
```

## 数据流程图

```
输入参数
├── product_level1: 一级业务方向
├── product_level2: 二级业务方向
├── qamate_product_ids: 产品线ID列表
└── group_ids: 用例分组ID列表
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 1: ITP用例检索                                          │
│   query_case_ids_by_groupids_and_uri()                      │
│   输出: Map<uri, List[case_id]>                             │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 2: 知识库查询                                           │
│   get_knowledge_by_uri()                                    │
│   输出: 核心参数定义列表                                      │
│   [{key, enums, in}, ...]                                   │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 3: 用例覆盖计算                                         │
│   for each case:                                            │
│     case_analysis() → get_case_kv_infos()                   │
│     输出: Map<node_id, cov_kv>                              │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 4: 冗余检测                                             │
│   for each case:                                            │
│     is_redundancy(case_kv_infos, node_id, cov_kv)           │
│     输出: is_redundancy, redundancy_case_id                 │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│ Step 5: 结果整合                                             │
│   API级别 + 用例级别结果                                     │
└─────────────────────────────────────────────────────────────┘
```

## 关键概念

### KV信息格式
代码中使用统一的KV格式来标识参数:
- `queryK:keyName` - Query参数
- `formDataK:keyName` - FormData参数
- `jsonK:rootKey->subKey` - JSON Body参数
- `anyK:keyName` - 任意位置参数(通用)

### 冗余判断逻辑
用例被判定为冗余需满足:
1. **核心参数覆盖包含关系**: 存在其他用例的核心参数覆盖完全包含当前用例的覆盖参数
2. **断言一致**: 断言信息完全一致(或当前用例无断言)

### 变量处理
支持处理用例中的变量替换:
- `${config.varName}` - 全局配置变量
- `${__xxx}` - 扩展函数(替换为空)

## 使用示例

```python
from case_analysis_strategy import CaseAnalysisStrategy

# 初始化策略
strategy = CaseAnalysisStrategy(
    params={
        "product_level1": "电商",
        "product_level2": "直播电商"
    },
    kirin_task_id=0,
    kirin_env="prod"
)

# 方式一: 执行完整流程(从度量平台获取数据)
strategy.execute()
result = strategy.result

# 方式二: 直接分析指定API
result = strategy.api_analysis_new(
    uris=["/api/example"],
    qamate_product_ids=[30],
    group_ids=[2030]
)
```

## 输出数据结构

### API级别结果
```json
{
    "api_key": "/api/example",
    "cov_kv_infos": "已覆盖的KV列表(JSON)",
    "no_cov_kv_infos": "未覆盖的KV列表(JSON)",
    "cov_kv_count": 10,
    "no_cov_kv_count": 5,
    "redundancy_case_count": 2
}
```

### 用例级别结果
```json
{
    "node_id": 12345,
    "api_key": "/api/example",
    "cov_kv": "覆盖的KV(JSON)",
    "cov_kv_count": 8,
    "is_redundancy": 1,
    "redundancy_infos": "{\"super_case_id\": 67890}",
    "last_30_run_count": 15,
    "last_30_run_success_count": 14
}
```

## 依赖模块

- `config.env.load_env`: 环境配置加载
- `config.logger.logger`: 日志记录
- `strategy.strategy`: 策略基类
- `utils.http_util`: HTTP请求工具
- `utils.itp_util`: ITP平台数据查询
- `utils.qamate_util`: QAMate平台数据查询
- `utils.sign_util`: 签名工具

## 数据存储

分析结果会存储到数据库:
- `insert_test_node_cov_analysis()`: 插入新记录
- `update_test_node_cov_analysis()`: 更新已有记录

## 注意事项

1. 需要正确配置环境变量和数据库连接
2. 需要有访问度量平台和知识库的权限
3. 变量替换依赖全局配置信息
4. 支持HTTP和RPC(Stargate)两种协议类型
