---
title: "背景信息"
description: "根据步骤需要读取以下文件内容："
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\task_design.md"
---
# 背景信息

根据步骤需要读取以下文件内容：

- 需求详情文件：`.lumos/{{icafe_id}}/requirement.md`
- 上一步功能点接口设计方案已存储至：`.lumos/{{icafe_id}}/api_design.json`

# 可用的MCP工具列表
```
{{mcp_configs}}
```

# 当前分析步骤：**功能点代码实现任务设计**

- **目标**：从功能点视角出发，结合候选接口定位结果和接口设计方案，采用 **task-design** skill 设计实际需要在代码层面完成的变更任务。每个功能点需给出清晰、可执行、可追踪的代码实现任务描述。

- **结果存储路径**：`.lumos/{{icafe_id}}/task_design.json`。

# 反思与修复

- 校验需求的验收标准是否已完整覆盖，**逻辑链路是否完整可追溯**。
- **当前代码库目标影响接口分析准确，代码变更任务设计无遗漏**。
- **严格对比实现与功能点验收标准等细节差异，是否都映射转换为对应的变更任务**。
- 变更任务设计是否遵循最小改动原则，对已有实现考虑复用优先。
- 输出字段名称、层级、类型与预定义结构一致，不得遗漏、拼写错误或新增未定义字段。
- 输出结果必须为严格符合 JSON 标准且可直接由解析器解析的文本，字符串中的双引号需正确转义以避免解析错误。

# 输出格式校验
- **进行自我校验 → 修复问题 → 给出最终可直接解析的 JSON 输出**
- **输出必须与以下 JSON 字段名称、层级、数据类型全部一致。**
```json
[
  {
    "featureId": "功能点ID",
    // 通用变更任务&非接口内部逻辑变更任务，如：第三方下游服务封装、MySQL表等存储设计等可公共使用的能力，自动化脚本、配置等内部任务，没有则为空列表
    "internalTasks": [
      {
        "objectName": "操作对象，如：配置项、下游接口、脚本名等",
        "taskType": "任务类型枚举（将存储设计区别出来），MySQL | Redis | GCP | AMIS | OTHER",
        "summary": "配置说明、内部逻辑或通用能力变更概述",
        // 任务关联或影响到的接口，实在没有则为空列表
        "linkedApis": [
          {
            "uri": "关联接口uri",
            "changeType": "枚举：NEW｜MODIFY"
          }
        ],
        "structChanges": [
          {
            "objectName": "数据结构名称",
            "structSchema": "JSONC格式的数据结构、建表语句等数据对象调整等变更/影响说明",
            "codeChange": "schema变更对应的结构体代码实现，如代码中结构体定义的变更（如有）"
          }
        ],
        "todoCodeList": [
          {
            "filePath": "代码路径",
            "changeDesc": "文件级变更描述",
            "tasks": [
              {
                "funcName": "函数名或结构体名",
                "taskDesc": "核心逻辑变更任务说明/受影响的逻辑说明，非代码行级别实现说明"
              }
            ]
          }
        ]
      }
    ],
    // 接口类变更任务，没有则为空列表
    "apiTasks": [
      {
        "uri": "接口路径",
        "changeType": "枚举值，NEW ｜ MODIFY",
        "method": "接口调用方式，如 GET / POST / PUT / DELETE等",
        "relation": "CORE | PARTIAL",
        "summary": "接口变更概述，例如：支持未登录领取奖励；调整任务完成逻辑。",
        "paramChanges": {
          "requestSchema": "string, JSONC格式请求参数变更",
          "responseSchema": "string, JSONC格式响应参数变更"
        },
        "todoCodeList": [
          // 变更任务详情，格式同上
        ]
      }
    ]
  }
]
```