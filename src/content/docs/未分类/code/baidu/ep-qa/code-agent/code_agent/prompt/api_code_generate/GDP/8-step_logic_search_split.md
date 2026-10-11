---
title: "检索任务拆解示例"
description: "当前为生成过程中的的中间任务：为待实现数据获取任务进行对应的检索任务拆解。 深入理解目标任务，提取关键检索关键词，并拆解出最多 {{maxsplitcount}} 个必要的检索任务，目的是据此检索知识为目标数据获取任务提供有效实现参考。 请"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\prompt\\api_code_generate\\GDP\\8-step_logic_search_split.md"
---
当前为生成过程中的的中间任务：为待实现数据获取任务进行对应的检索任务拆解。
深入理解目标任务，提取关键检索关键词，并拆解出最多 {{max_split_count}} 个必要的检索任务，目的是据此检索知识为目标数据获取任务提供有效实现参考。
请遵循以下要求：
- 每个检索任务需明确指向具体的检索关键词；
- 针对配置文件、常量定义、结构体定义、代码实现等内容，应分拆为独立的检索任务；
- 避免冗余：不重复为同一对象生成多个检索任务。

# 检索任务拆解示例
* 注意参考示例保证重点关键词的保留；
## 示例1：mysql数据库数据操作
- 输入示例：`从test_table表中获取测试数据。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含test_table表、测试数据获取。",
    "sub_queries": ["test_table表.toml请求配置", "test_table表对象定义或初始化（mysql.Client/*gorm_adapter.GormDB/init/db/sql）", "从test_table表获取测试数据逻辑实现"]
}
```
## 示例2：redis缓存数据操作
- 输入示例：`调用TestRedis对象删除数据。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含TestRedis对象、删除数据。",
    "sub_queries": ["TestRedis对象.toml请求配置", "TestRedis对象定义或初始化（redis.Client/init）", "通过TestRedis对象删除数据逻辑实现"]
}
```
## 示例3：gcp配置数据操作
- 输入示例：`采用TestGCPStruct结构配置通过TestGCPKey、TestGCPID获取GCP配置。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含TestGCPKey、TestGCPID配置，TestGCPStruct结构体、GCP数据获取。",
    "sub_queries": ["TestGCPStruct结构体定义", "TestGCPKey、TestGCPID配置常量定义", "采用TestGCPStruct结构配置通过TestGCPKey、TestGCPID获取GCP配置的实现"]
}
```
## 示例4：下游服务数据操作
- 输入示例：`调用test_service下游服务获取数据。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含test_service服务、下游服务数据获取，其中下游接口数据获取通常与特定关键词ral、ghttp、call等相关。",
    "sub_queries": ["test_service服务.toml请求配置", "test_service下游服务名、path常量定义", "test_service下游服务数据获取实现（ral/ghttp/call等）"]
}
```

# 输出格式
```json
{
    "thoughts": "核心检索关键词提取思考过程（注意言简意赅）",
    "sub_queries": ["检索子任务列表"]
}
```

# 目标数据获取任务
```
{{task}}
```