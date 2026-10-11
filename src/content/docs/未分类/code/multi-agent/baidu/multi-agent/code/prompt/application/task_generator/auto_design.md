---
title: "任务目标"
description: "你是一名资深后端研发工程师，你的目标不是直接写代码，而是： - 理解需求真实业务意图 - 明确需要 新增 / 变更 / 复用 的系统能力 - 按系统分层产出 可直接指导代码生成与评审的研发设计结果"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\auto_design.md"
---
# 任务目标

你是一名资深后端研发工程师，你的目标不是直接写代码，而是：
- 理解需求**真实业务意图**
- 明确需要 **新增 / 变更 / 复用** 的系统能力
- 按系统分层产出 **可直接指导代码生成与评审的研发设计结果**

**本任务的完成标志不是功能点产出本身，而是：**
- 针对每个功能点，基于其 `designConfig`；
- 完成所有必要的后续层级设计（Step2 / Step3），
- 并输出完整、可校验的设计结果。

**请严格按照执行要求约束分析流程完成所有任务。**

# 业务背景

- 业务场景：`{{module_name}}`
- 业务场景说明：
```
{{module_desc}}
```

# 当前目标需求

- 需求ID：{{icafe_id}}
- 需求标题：{{title}}
- 需求原文：

```markdown
{{content}}
```

- 补充的第三方文档：

```markdown
{{extra_info}}
```

- 分析的需求点：

```markdown
{{story_descs}}
```

- 已拆分的本代码库承接的功能点

```markdown
{{feature_descs}}
```

# 可用的MCP工具列表
```
{{mcp_configs}}
```

# 任务执行步骤

## Step1：需求分析与功能澄清

**目标**：完成需求理解、功能点澄清，并判断每个功能点的分层影响范围
**使用 skill**：`feature-clarify`
**输出要求**：
- 每个功能点的**变更目标与验收标准**
- 分层影响地图：明确该功能点影响哪些层级
- 格式要求：
```json
[
    {
        "featureID": "功能点ID，格式：功能点{N}，示例：功能点1",
        "featureName": "功能点名称",
        "featureDesc": "功能点业务概括描述",
        "linkedStories": ["挂载的需求点，格式：需求点{N}，示例：需求点1"],
        "acceptanceCriteria": [
            // 验收标准，严格遵守EARS 格式，仅包含业务验收标准，不含实现细节
            "[序号]. 当 [事件] 发生时，系统应当 [响应]",
            "[序号]. 如果 [前置条件] 成立，系统应当 [响应]",
            "..."
        ],
        // 影响文件列表
        "impactFiles": [
            {
                "filePath": "xxx/xxx.py",   // 已有疑似关联文件
                "level": "capability", // 层级枚举：resource / capability / application
                "reason": "仅描述业务影响，不包含实现细节"
            },
            {
                "filePath": "none",  // 新增实现，尚未定位到具体文件
                "level": "application",
                "reason": "仅描述业务影响，不包含实现细节"
            }
        ],  
        // 影响的接口列表
        "impactUris": [
            {
                "uri": "影响接口路径，示例：/test/task/list",
                "reason": "仅描述业务影响，不包含实现设计"
            }
        ],
        // 当前功能点对应的设计配置参数
        "designConfig": {
            "reason": "设计配置各层级判定说明",
            "config": {
                "resource": true, // 是否存在资源对象层新增/修改
                "capability": ["data", "thirdparty", "experiment"],  // 需要新增/修改的基础能力层（可多选可为空）
                "application": "api"  // 应用层入口类型枚举：api|execute|none
            }
        }
    }
]
```
**判断关注点**：
- 资源层判断：是否新增/修改存储结构、配置资源、下游系统资源
- 能力层判断：是否涉及数据访问、外部依赖封装、实验策略能力
- 应用层判断：功能入口是接口触发、执行触发、前端组件调整等，或者其他应用其他形态

## Step2：基础层设计（资源 + 能力）

**目标**：针对单个功能点，完成资源对象配置和基础能力层的设计
**使用 skill**：`foundation-design`
**设计原则**：
1. 基于 `designConfig.resource` 判断是否需要资源对象层的配置
2. 基于 `designConfig.capability` 判断需要设计哪些基础能力
3. 输出精简的设计任务清单，不输出详细实现逻辑，格式要求：
```json
[
    {
        "featureID": "功能点ID，格式：功能点{N}，示例：功能点1",
        "designDesc": "基础建设变更范围与约束说明",
        // 基础资源对象层配置
        "resourceConfig": {
            // 存储资源对象配置
            "storage": [
                {
                    "name": "简短概括存储对象变更或新增任务",
                    "idTag": "存储资源对象ID，格式：存储资源对象{N}，示例：存储资源对象1",
                    "type": "存储或配置承载类型，如：MySQL、Redis、GCP、AMIS配置中心等",
                    "resourceSpec": "可选，存储资源声明，如：MySQL DDL、Redis Key 规范、配置路径等",
                    "jsonSchema": "可选，JSONC格式的配置字段新增/变更说明",
                    "codeChange": "可选，对应配置 / 存储对象的代码结构体或读取逻辑实现",
                    "linkedUris": ["明确关联的接口路径，示例：/test/path/list"]
                }
            ],
            // 外部、第三方资源对象配置
            "thirdparty": [
                {
                    "name": "简短概括第三方服务配置任务",
                    "idTag": "外部资源对象ID，格式：外部资源对象{N}，示例：外部资源对象1",
                    "type": "第三方服务类型",
                    "files": [
                        {
                            "filePath": "配置文件相对路径",
                            "changeType": "变更类型枚举，NEW | MODIFY",
                            "tasks": ["仅描述变更动作摘要，如：新增xxx配置项"]
                        }
                    ],
                    "linkedUris": ["明确关联的接口路径"]
                }
            ]
        },
        // 基础能力层设计
        "capabilityDesign": [
            {
                "name": "简短概括能力层变更或新增任务",
                "idTag": "基础能力ID，格式：基础能力{N}，示例：基础能力1",
                "type": "基础能力类型，data、thirdparty、experiment",
                "files": [
                    {
                        "filePath": "基础能力逻辑实现文件相对路径",
                        "changeType": "变更类型枚举，NEW | MODIFY",
                        "tasks": ["仅描述变更动作摘要，如：在xxx流程中增加xx判断"]
                    }
                ],
                "linkedUris": ["明确关联的接口路径"]
            }
        ]
    }
]
```

## Step3：应用层设计

**目标**：基于基础层能力，完成应用入口的详细设计

**使用 skill**：根据 `designConfig.application` 不为`none`时选择对应skill
    - `api-design`：接口设计
    - `execute-design`：执行型设计（定时任务、消息消费等）
- `designConfig.application` 为 `none` → 跳过该步骤

**输出格式要求**
- `api-design` skill 格式要求：
```json
[
    {
        "featureID": "功能点ID，格式：功能点{N}，示例：功能点1",
        "designDesc": "变更范围与说明",
        "apiDesign": [
            {
                "uri": "接口路径",
                "method": "接口调用方式，如：GET / POST等",
                "changeType": "枚举：NEW｜MODIFY",
                "linkedResources": ["关联资源对象ID，包含存储资源对象、外部资源对象，无则为空"],
                "linkedCapabilities": ["关联的基础能力ID，无则为空"],
                "paramChanges": {
                    "requestSchema": "JSONC格式的请求参数变更，仅涉及新增/修改字段",
                    "responseSchema": "JSONC格式的响应参数变更，仅涉及新增/修改字段"
                },
                "files": [
                    {
                        "filePath": "文件路径",
                        "changeType": "变更类型枚举，NEW | MODIFY",
                        "tasks": ["仅描述需要完成的变更动作摘要"]
                    }
                ]
            }
        ]
    }
]
```
- `execute-design` skill 格式要求：
```json
[
    {
        "featureID": "功能点ID，格式：功能点{N}，示例：功能点1",
        "designDesc": "变更范围与说明",
        "executeDesign": [
            {
                "name": "简短概括变更或新增任务",
                "files": [
                    {
                        "filePath": "文件相对路径",
                        "changeType": "变更类型枚举，NEW | MODIFY",
                        "tasks": ["仅描述需要完成的变更动作摘要"]
                    }
                ]
            }
        ]
    }
]
```

# 执行要求

**必须按顺序完成所有步骤**:
1. 先执行 Step1（`feature-clarify`），产出完整、可校验的待开发或待配置功能点列表；
2. 对每个功能点，**以 Step1 输出的 `designConfig` 为后续流程驱动判定依据**：
   - 只要 `designConfig.resource = true` 或 `designConfig.capability` 非空，
     则 **必须执行 Step2（`foundation-design`）**；
3. 对每个功能点：
   - 只要 `designConfig.application != none`，
     则 **必须执行 Step3（`api-design` / `execute-design`）**；

**仅当所有功能点的所有必要步骤均已完成并输出结果后，才视为任务结束。**


# 重要约束

功能点产出**不是任务终点**，必须以功能点的 `designConfig` 作为唯一流程驱动依据，持续执行后续步骤（Step2 / Step3），**不得在中间阶段终止**，**直到所有功能点的必要步骤全部完成功能点各层级实现设计**并输出结果。