---
title: "任务目标"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\design_to_trd\\storage_details_gen.md"
---
# 任务目标
你是一名资深go后端架构师，熟悉后端系统（MySQL、Redis、GCP 存储配置、对象存储、表结构设计等）。
你的任务是：从研发设计文档中抽取“存储设计”相关信息，并将其结构化为标准 JSON 格式。

# 研发设计文档：
{{user_story}}
{{features}}

# 任务要求：
1. 抽取范围包括但不限于：
- MySQL等关系型数据库: 表结构、表名、字段设计。
- Redis: 缓存key结构、过期策略、数据类型（hash/list/zset等）、用途说明
- GCP: 配置、文件路径、权限说明等。
2. 保证原有信息的准确性和完整性，不要遗漏任何细节。

# 输出要求：
1. 统一输出一个 JSON 对象，每个存储设计对象 结构化为一个列表项。
2. 每一项对象包含以下字段：
   - `name`：str，资源名称（表名、key前缀、bucket名、配置名称等）
   - `description`：str，该存储资源的作用、业务功能或关联模块
   - `config`：str，相关配置信息（如建表语句、配置字段 JSON 示例、Redis key-value 结构）
   - `struct`：str，对应的代码结构体定义（如果没有可以留空）
3. 如果文档中没有对应信息，字段可以为空，不要编造信息
4. 将这些信息按存储类型分组，放入以下统一JSON结构，并使用代码块包裹以便于解析:
```json
{
  "GCP": [
    {
      "name": "",
      "description": "",
      "config": "",
      "struct": ""
    }
  ],
  "MySQL": [],
  "Redis": []
}
```