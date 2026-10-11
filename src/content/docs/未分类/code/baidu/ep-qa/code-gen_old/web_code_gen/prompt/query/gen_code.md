---
title: "关联知识库:"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\query\\gen_code.md"
---
# 关联知识库:
<context>
\n---------------------\n{{context}}\n---------------------\n
</context>

# 任务描述：
解析 Query，识别核心信息，并拆解为检索任务，以便获取相关知识 **辅助 Query 解答**。

## Step 1 - 思考分析：
1. 识别 Query 中的核心实体、关系及意图 
   - 确定目标对象（函数、类、变量等）。
   - 明确**需求类型**（代码变更（新增/修改/重构）、代码理解（问答/示例））。
   - 判断是否涉及 跨层影响：
     * 方法/接口签名变更 → 影响调用方。
     * 数据结构或 API 变更 → 影响依赖服务、数据库交互。
     * 业务逻辑封装或拆分 → 可能影响多个层级。
2. 确保拆解的是“检索任务”，而非 Query 本身的执行步骤
   - 仅拆解出检索所需的信息，避免扩展。
3. 优化检索策略：
   - 代码变更类
     - 新增类/方法/字段 → 检索相关依赖项（如已有接口、调用方）。
     - 修改现有代码 → 需同时检索：
       - 目标代码的定义（确保改动位置正确）。
       - **仅当在方法签名（入参/出参数量）发生变更时，需检索该方法的所有调用位置**，确保正确修改调用代码。
       - 目标参数的获取方式。
       - 特别注意：**涉及接口修改时，需解析并检索需求涉及到的关联接口层实现检索**（如：MVC模式下GDP框架接口实现包含Router、Controller、Service、DAO、RPC第三方下游服务toml配置&调用、核心业务逻辑方法定义、相关请求/响应体等结构体定义等。）
   - 代码理解类 → 侧重现有实现、API 文档或代码库中的示例。 
     - **涉及到接口实现时，需考虑完整接口跨层实现检索**（如：MVC模式下GDP框架接口完整实现需检索Router、Controller、Service、DAO、RPC第三方下游服务toml配置&调用、核心业务逻辑方法定义、相关请求/响应体等结构体定义等。）
4. 判断 Query 是否需要拆解：
   - 简单 Query → 直接检索，无需拆解。
   - 复杂 Query → 拆解为独立的检索任务，但**避免过度拆分**，确保任务独立、无重复。

## Step 2 - 行动拆解：
基于分析结果，拆解最多 **{{max_split_count}}** 个独立的检索任务，满足以下要求：
- Context与Query无关时，忽略Context
- 仅关注Query涉及的信息，不进行扩展或假设
- 可独立检索，不依赖其他任务
- **仅当方法签名（入参/出参数量）变更时，需检索方法所有调用位置**，否则不检索调用方。
- **必须形成明确的检索关键词**

# 检索任务拆解示例
## 示例1
- 输入Query示例："给出调用第三方下游接口的示例"
- 响应示例：
```json
{
    "thoughts": "需要检索代码库中所有调用下游第三方接口相关的实现以供参考，下游接口数据获取通常与特定关键词ral、ghttp、call等相关。",
    "sub_queries": ["调用第三方下游接口的所有实现（ral/ghttp/call等）"]
}
```
## 示例2
- 输入Query示例："将TestFunc中元素遍历逻辑封装成公共方法，并给方法增加TestAddParam参数，且当参数TestExistParam值为0时直接返回。"
- 响应示例：
```json
{
    "thoughts": "需要检索TestFunc方法的具体实现、TestExistParam的获取方式，由于TestFunc定义增加了入参TestAddParam，所以还需要检索TestAddParam的获取、所有TestFunc被调用的位置。",
    "sub_queries": ["TestFunc方法具体实现", "参数TestExistParam的获取方式", "参数TestAddParam的获取方式", "所有调用TestFunc的位置"]
}
```

## 示例3：接口修改
- 输入Query示例：`接口路径：test/testTask\n修改逻辑：增加的TestParam通过TestFunc方法赋值并组装至返回结果中。\n接口入参：不变\n接口出参：{"TestParam": string # 新增字段\n"TestID": string}。`
- 结合目标语言规范&需求理解，拆解需求涉及到的关联接口层检索任务（若未指定或无法解析目标语言，默认参考MVC模式的GDP框架），拆解示例如下：
```json
{
    "thoughts": "要修改test/testTask接口出参，需要检索接口响应体定义以及业务逻辑中响应体的组装逻辑，还需要检索TestFunc方法定义用于新增参数赋值。",
    "sub_queries": ["test/testTask接口核心业务逻辑", "test/testTask接口响应体定义", "TestFunc方法定义"]
}
```

## 示例4：接口实现问答
- 输入Query示例：`给出test/testTask接口各层的实现。`
- 结合目标语言规范，需拆解完整关联接口层的检索任务（若未指定或无法解析目标语言，默认参考MVC模式的GDP框架），拆解示例如下：
```json
{
    "thoughts": "需要检索test/testTask接口在各层的具体实现，包括Router、Controller、Service、DAO、RPC第三方下游服务toml配置&调用、业务核心逻辑方法定义、相关请求/响应体等结构体定义等，下游接口数据获取通常与特定关键词ral、ghttp、call等相关。",
    "sub_queries": ["test/testTask接口Router层实现", "test/testTask接口Controller层实现", "test/testTask接口Service层实现", "test/testTask接口DAO层实现", "test/testTask接口第三方下游服务toml配置", "test/testTask接口RPC第三方下游服务调用（ral/ghttp/call等）", "test/testTask接口核心业务逻辑方法定义", "test/testTask接口请求体、响应体等结构体定义"]
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
\n---------------------\n{{query}}\n---------------------\n