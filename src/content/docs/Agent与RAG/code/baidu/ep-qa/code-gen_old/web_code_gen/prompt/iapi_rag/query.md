---
title: "任务描述："
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\iapi_rag\\query.md"
---
# 任务描述：
解析接口逻辑实现描述Query，识别核心信息，并拆解出Query业务逻辑部分涉及到的**必要**的检索任务，以便获取相关知识 **辅助基于Query的业务逻辑代码生成任务的解答**。

## Step 1 - 思考分析：
1. 识别 Query 中的核心实体、关系及意图，需检索业务逻辑关联代码实现，包括但不限于：
- 目标代码的定义。
- 存在变更的目标参数的获取方式。
- **仅当方法签名（入参/出参数量）发生变更时，需检索该方法的所有调用位置**，确保正确修改调用代码。
2. 确保拆解的是“检索任务”，而非 Query 本身的执行步骤。

## Step 2 - 检索任务拆解：
基于分析结果，最多拆解出 **{{max_split_count}}** 个独立的检索任务，满足以下要求：
- 仅关注Query涉及的信息，不进行扩展或假设，**禁止过度拆解**。
- 确保检索任务存在**必要性、独立性、无重复性**。
- **仅当方法签名（入参/出参数量）变更时，需检索方法所有调用位置**，否则不检索调用方。
- **必须形成明确的检索关键词**

# 检索任务拆解示例
## 示例1：
- 输入Query示例：`接口路径：test/testTask\n接口描述：从test_table表中获取数据并返回。\n接口入参：{"TestNewParam1": string, "TestNewParam2": string}\n接口出参：{"TestNewData": array}。`
- 结合目标语言规范&需求理解，拆解需求涉及到的关联接口层检索任务（若未指定或无法解析目标语言，默认参考MVC模式的GDP框架），拆解示例如下：
```json
{
    "thoughts": "需要检索目标接口的检索从test_table表获取数据逻辑作为参考，也需要了解表的字段。",
    "sub_queries": ["test/testTask接口请求体、响应体定义", "test_table表定义", "从test_table表获取数据的逻辑"]
}
```

## 示例2：
- 输入Query示例：`接口路径：test/testTask\n接口描述：给TestFunc方法增加TestAddParam参数，通过该参数调用下游服务test_service服务获取测试数据，并格式化后返回。\n接口入参：{"TestExistParam": string, "TestAddParam": string}\n接口出参：{"TestData": array # 新增测试数据字段\n"TestID": int}。`
- 结合目标语言规范&需求理解，拆解需求涉及到的关联接口层检索任务（若未指定或无法解析目标语言，默认参考MVC模式的GDP框架），拆解示例如下：
```json
{
    "thoughts": "需检索接口TestFunc方法定义，并检索test_service第三方下游服务调用逻辑的实现，接口出/入参数字段也有变更，因此也需要检索出入参数是否已存在，由于TestFunc函数入参有增加，因此还需要检索函数被调用的位置以方便后续处理函数签名变更带来的影响，其中下游接口数据获取通常与特定关键词ral、ghttp、call等相关。",
    "sub_queries": ["test/testTask接口请求体、响应体定义", "TestFunc方法定义", "第三方下游服务test_service调用逻辑实现（ral/ghttp/call等）", "所有TestFunc方法被调用的位置"]
}
```

# 输出格式：
```json
{
    "thoughts": "思考过程（注意要言简意赅）",
    "sub_queries": ["检索子任务列表"]
}
```

# 目标Query：
{{query}}