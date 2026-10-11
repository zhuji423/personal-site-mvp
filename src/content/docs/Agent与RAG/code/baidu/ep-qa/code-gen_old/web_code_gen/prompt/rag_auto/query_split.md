---
title: "任务目标"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_auto\\query_split.md"
---
# 任务目标
深入解析理解任务Query，识别接口逻辑描述中涉及的核心检索关键词，根据关键词拆解出必要的检索任务，以便获取知识**辅助基于Query的代码生成任务的解答**。
1. 深入思考理解Query，解析提取接口逻辑描述中需要进行知识检索的关键词。
2. 根据解析提取的关键词，结合MVC模式GDP框架背景知识，最多拆解出{{max_split_count}}个**必要**的检索任务，注意事项如下：
- 仅关注Query涉及的信息，不进行扩展或假设；
- 每个检索任务必须形成明确的检索关键词；
- 配置文件、常量定义、结构体定义、代码实现等不同目标任务需拆解成独立任务；
- 仅拆解必要的检索任务，**注意避免对同一对象的重复检索**；

# 检索任务拆解示例
* `...`表示内容省略，不影响检索任务拆解；
* 注意参考示例保证重点关键词的保留；
## 示例1：mysql数据库数据操作
- 输入示例：`接口路径：/testTask1\n调用方式：GET\n接口逻辑：从test_table表中获取测试数据并返回。\n接口入参：...\n接口出参：...。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含test_table表、测试数据获取，还要考虑/testTask1接口请求体、结构体是否已完成定义。",
    "sub_queries": ["/testTask1接口请求体&响应体定义", "test_table表结构定义&对象初始化（mysql/db/sql）", "从test_table表获取测试数据逻辑实现"]
}
```
## 示例2：redis缓存数据操作
- 输入示例：`接口路径：/testTask2\n调用方式：GET\n接口逻辑：调用TestRedis对象删除数据。\n接口入参：...\n接口出参：...。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含TestRedis对象、删除数据，还要考虑/testTask2接口请求&响应体是否已定义。",
    "sub_queries": ["/testTask2接口请求体&响应体定义", "TestRedis对象定义&初始化", "通过TestRedis对象删除数据逻辑实现"]
}
```
## 示例3：gcp配置数据操作
- 输入示例：`接口路径：/testTask3\n调用方式：POST\n接口逻辑：采用TestGCPStruct结构配置通过TestGCPKey、TestGCPID获取GCP配置。\n接口入参：...\n接口出参：...。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含TestGCPKey、TestGCPID配置，TestGCPStruct结构体、GCP数据获取，还需检索确认/testTask3接口请求体&响应体是否已定义。",
    "sub_queries": ["/testTask3接口请求体&响应体定义", "TestGCPStruct结构体定义", "TestGCPKey、TestGCPID配置常量定义", "采用TestGCPStruct结构配置通过TestGCPKey、TestGCPID获取GCP配置的实现"]
}
```
## 示例4：下游服务数据操作
- 输入示例：`接口路径：/testTask4\n调用方式：POST\n接口逻辑：调用test_service下游服务获取数据。\n接口入参：...\n接口出参：...。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含test_service服务、下游服务数据获取，其中下游接口数据获取通常与特定关键词ral、ghttp、call等相关，还要考虑/testTask4接口请求体&响应体是否已定义。",
    "sub_queries": ["/testTask4接口请求体&响应体定义", "test_service服务名常量定义", "test_service下游服务数据获取实现（ral/ghttp/call等）"]
}
```
## 示例5：iconf配置数据操作
- 输入示例：`接口路径：/testTask5\n调用方式：GET&POST\n接口逻辑：通过test_conf、test_param获取iconf配置。\n接口入参：...\n接口出参：...。`
- 输出示例：
```json
{
    "thoughts": "涉及到的检索关键信息包含test_conf&test_param参数、iconf配置数据获取，还需检索确认/testTask5接口请求体&响应体是否已定义。",
    "sub_queries": ["/testTask5接口请求体&响应体定义", "iconf常量参数定义", "iconf配置数据获取逻辑实现"]
}
```

# 输出格式
```json
{
    "thoughts": "核心检索关键词提取思考过程（注意言简意赅）",
    "sub_queries": ["检索子任务列表"]
}
```

# 目标输入
```
{{query}}
```