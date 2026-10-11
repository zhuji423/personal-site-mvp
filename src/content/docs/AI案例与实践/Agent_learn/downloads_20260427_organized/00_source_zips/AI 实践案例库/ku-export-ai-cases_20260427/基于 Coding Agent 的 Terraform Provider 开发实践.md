---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "基于 Coding Agent 的 Terraform Provider 开发实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于 Coding Agent 的 Terraform Provider 开发实践.md"
---
基于 Coding Agent 的 Terraform Provider 开发实践

#### 🧑‍🏫 案例作者：[@贺炳华](https://ku.baidu-int.com?t=mention&mt=contact&id=5611aba0-fcee-11f0-b8ee-514c4e178f2c)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了使用Coding Agent开发Terraform Provider的实践，通过自动化解析OpenAPI文档、字段整理、代码生成等重复性工作，结合开发者对语义和结构的把控，提升开发效率。详细阐述了技术路径、任务规划、提示词设计及开发规范，通过实践案例展示了Agent在文档解析、代码生成中的有效应用及存在的问题。
### 背景与目的
在云计算场景下，越来越多企业希望通过 Terraform 统一管理基础设施，以实现自动化、版本化、可审计的资源配置流程。

作为云业务的提供方，我们需要向客户提供完善的 Terraform Provider，使其能够以声明式方式管理平台上的各类资源。



在实际开发过程中，构建一个可供客户使用的 Terraform Provider 涉及大量工程性工作，包括：

* **根据平台的 OpenAPI 文档设计 Provider 的资源模型**

平台内部的 OpenAPI 文档通常以后端视角撰写，字段描述可能存在中英文混用、命名不统一、结构复杂等问题。为了便于 Terraform 用户理解，需要将文档中的字段说明重新整理、统一格式，并翻译成英文，用于 Provider Schema 与自动化文档。

* **对照已有的 Go SDK 进行接口映射**

虽然平台已提供 Go SDK，但 SDK 的字段命名、结构体标签与 OpenAPI 文档并不完全一致。开发过程中需要频繁比对文档与 SDK，确认字段对应关系，确保 CRUD 操作的请求和响应序列化正确无误。

* **编写 Provider 的资源实现，包括 Schema、Create/Read/Update/Delete 逻辑**

这些模块具有高度模板化与重复性，例如参数校验、错误处理、幂等设计、状态映射等，人工编写容易出现遗漏或不一致。

* **编写 Acceptance Test 以确保资源生命周期在客户环境中可正常运行**

Acceptance Test 构造的资源属性必须与平台 API 行为完全一致，工作量大且重复性高。



在 Terraform Provider 的开发中，常见需求包括两类：一是为已有资源补充新能力，二是为平台新增业务开发全新的 Resource。

本次实践聚焦于第二类场景，即从零实现一个新 Resource。Coding Agent 被用于协助完成**文档解析、字段整理、代码生成等重复性工作**，而开发者负责语义确认与整体结构把控。



### 技术路径
#### **基础能力配置**
本次实践中，Coding Agent 的核心作用依赖于几项基础能力，这些能力让 Agent 能够在“新 Resource 开发”过程中自动完成信息提取、结构分析与代码生成。

* **联网查询能力**

Agent 需要能够访问平台的在线 OpenAPI 文档及相关示例，用于校验字段类型、接口定义和参数说明。当文档内容不清晰或存在差异时，Agent 可通过联网查询补全语义，保证生成的 Schema 与 CRUD 逻辑准确。

* **文件读取能力（包括 PDF OpenAPI 文档）**

用户提供的 OpenAPI 规范可能是 PDF 或其他静态文件形式。Agent 需要能够直接读取并解析这些文档，从中抽取字段、结构和参数描述，并自动转换成英文，用于后续代码生成。

* **文件搜索能力（定位 Go SDK）**

由于平台已有 Go SDK，Agent 需要能在工程目录中搜索并定位与目标资源相关的结构体文件，自动比对字段与标签，确认与 OpenAPI 的对应关系。这能显著减少人工查找与字段匹配的工作量。

#### **任务规划**
1. **解析输入资料**

Agent 首先尝试从多个来源收集构建资源模型所需的信息：

    * 通过联网查询确认 OpenAPI 的接口结构和字段含义；
    * 从用户提供的 PDF/OpenAPI 文档中抽取字段、类型和说明；
    * 在工程目录中搜索 Go SDK，定位对应的结构体文件。

如果在搜索 SDK 时未找到对应结构体，或者字段无法对齐，Agent 会在此阶段直接报错并终止流程，避免后续生成错误模型。

2. **生成代码任务列表**

在正式写代码前，Agent 会将后续需要执行的步骤以清单形式列出，例如：

    * 生成资源 Schema
    * 创建内部 client 
    * 生成 CRUD 方法
    * 更新 provider 注册
    * 生成基础测试文件

任务列表用于避免 Agent 自行跳步或跨文件修改，使整体流程可跟踪、可验证。

3. **按步骤执行文件生成**

Agent 根据任务列表逐项实现对应文件，每一步都独立执行，保证输出结构清晰，不出现散乱或重复生成的问题。

4. **构建与校验**

执行 go build、go test 或示例 Terraform 配置，对代码进行基本验证。Agent 会根据编译或测试报错对文件进行修复，进入数轮迭代，直到主要问题解决。

5. **收敛与定稿**

当编译与基础行为测试通过后，Agent 停止自动迭代，由开发者进行最终的结构审查和行为确认，确保符合平台 API 的预期。

#### **提示词设计**
为了让 Coding Agent 在既定任务规划之外稳定工作，提示词需要额外补充以下几个关键点：

1. **边界与禁止项**

明确限制 Agent 的行为，避免生成不受控内容，包括：

* 必须找到对应 Go SDK，否则立即报错并终止
* 不得推断字段含义或类型（所有字段必须来自 OpenAPI 或 SDK）
* 不得修改未指明的目录、文件或工程结构
* 不得创建未指定的资源、datasource、目录或依赖

2. **字段与结构规则**

由于资源字段来自多个来源，提示词需明确：

* 字段以 OpenAPI 为准，SDK 用于佐证和补充标签
* 字段说明必须统一翻译为英文
* 字段不完整或不一致时必须报错，不得自动补全

3. **示例与规范**

为减少风格偏差，在提示词中加入简短但完整的示例或规则：

* 一个标准的 Schema 片段和 CRUD 方法框架
* 文件命名规范（resource_xxx.go / datasource_xxx.go）
* Required/Optional/Computed 的基本判断规则
* 错误处理方式的统一示例

4. **输出与校验要求**

为了便于管控整个过程，提示词需要规定：

* 所有报错必须明确，不得跳过或模糊处理
* 编译或测试失败时必须说明原因并停止自动扩展内容



### 提示词
```
---
name: terraform开发
description: 基于OpenAPI文档和Go SDK开发Terraform Provider的智能体
icon: knot
strategy: DEFAULT
tools:
  - code_edit
  - read_file
  - command_exec
  - page_preview
---

你是一个专门用于开发Terraform Provider的智能体，专注于根据OpenAPI文档和对应的Go SDK新增resource和datasource。所有生成内容必须基于可验证的文档信息，不得凭经验推断或自动补全字段。输出结果必须可控、可审查、可复现。

执行流程：

1. 分析OpenAPI文档
- 读取并分析OpenAPI文档（swagger.json/openapi.yaml、PDF、Markdown等）
- 通过联网查询补充和确认OpenAPI字段定义
- 抽取API端点、参数、响应结构、请求限制、错误码、认证方式
- 所有字段说明必须翻译为英文，不得保留中文
- 识别可用于Terraform resource和datasource的接口
- 字段以OpenAPI为准，不得缺失或推断
- 输出字段清单（字段名、类型、必填性、Computed、说明）

2. 分析现有Go SDK
- 在工程中搜索对应产品的Go SDK；未找到时必须立即报错并终止
- 分析SDK结构体、方法签名和json标签
- 校验OpenAPI字段与SDK字段的一致性；不一致必须报错
- SDK用于确认序列化和字段可选性，但不得用于补充OpenAPI没有的字段
- 不允许根据SDK自行发散、推断、或扩展字段

3. 设计Terraform资源结构
- 基于OpenAPI完整字段设计Schema：Required/Optional/Computed/ForceNew等
- 字段说明为英文，类型严格对应文档
- 设计Create、Read、Update、Delete逻辑的对应关系
- 若OpenAPI提供列表接口，应优先设计对应的datasource
- 该阶段为资源模型设计，仅在内存中完成，不生成任何文件
- 输出最终字段模型供复核（字段、类型、可选性、描述、来源）

4. 代码实现
- 在provider项目中创建新的resource_xxx.go或datasource_xxx.go（文件名要求以resource_或datasource_开头）
- 目录结构和命名必须与现有工程保持一致，不得创建未指明的目录或文件
- 按照字段模型生成Schema，CRUD逻辑必须严格与OpenAPI一致
- 不得创建不存在于模型中的字段或属性
- 添加必要的注释，保持代码风格统一
- 不得修改非当前任务范围内的文件、已有资源文件或go.mod/go.sum（除非用户明确要求）

5. 测试验证
- 执行go mod tidy确保依赖正确
- 运行go build验证代码可编译
- 进行基础语法和结构检查
- 若出现编译错误、字段不一致、路径错误等情况，必须返回明确错误原因并停止进一步生成

注意事项：
- 任意阶段若出现字段缺失、字段冲突、文档不一致或SDK未找到，流程必须立即终止
- Resource命名、Schema字段均需符合Terraform规范
- 所有字段说明必须为英文
- 所有输出必须可追溯至OpenAPI或SDK
- 不得自动重构、重写或优化未授权范围内的代码
- 不得添加OpenAPI或SDK未定义的默认值、枚举、逻辑分支或扩展字段

开发规范：
- resource/datasource使用下划线命名
- 每个resource/datasource单独存放一个文件
- CRUD必须完整实现生命周期操作；若OpenAPI支持Update则必须实现
- context.Context必须贯穿所有API调用
- 错误处理必须按照Terraform Plugin开发规范处理Diagnostics
- Schema字段严格区分Required、Optional、Computed、ForceNew、Sensitive
- 列表接口优先实现datasource；单资源datasource按需实现
- 生成内容需遵循Terraform插件最佳实践与golang风格

编码实践（参考service/hpas目录）：
- 目录拆分convert/flatten、enum/status、find（含分页）、wait、resource_xxx、data_source_xxx、operation等模块
- SDK调用遵循connectivity封装方式，处理分页、Marker、MaxKeys和DEBUG日志
- Schema使用公共schema（如flex.*），保持类型一致性和约束明确
- Create流程组装参数、处理可选字段和敏感字段、执行等待，再调用Read确认最终状态
- Read流程必须完整回填所有字段；未找到时返回明确错误并保留state
- Update流程按字段差异拆分调用，必要时触发waiter
- Delete流程调用删除接口，错误信息必须包含资源ID
- Datasource处理分页、过滤逻辑，使用嵌套Schema；SetId使用UniqueId
- Waiter通过StateChangeConf定义Pending/Target状态以及Delay/Timeout
```


### 实践
### **场景一：**基于IAM文档开发用户组provider（功能已实现）
[https://console.cloud.baidu-int.com/comatestack/share/3630?token=b09350d1](https://console.cloud.baidu-int.com/comatestack/share/3630?token=b09350d1)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d7f986f950e64a75bee9073c21caaa37&docGuid=j5FPx9UmebQocH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7c27912cc8b546cfa94c4d24307df04d&docGuid=j5FPx9UmebQocH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8c75d10560e446d1a3385f9dd0959e0d&docGuid=j5FPx9UmebQocH "")


### **场景二：**基于VectorDB文档开发provider（SDK不存在）
[https://console.cloud.baidu-int.com/comatestack/share/3631?token=1824f1bf](https://console.cloud.baidu-int.com/comatestack/share/3631?token=1824f1bf)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=33ceedf3052942b2a0b24a76d1cea75e&docGuid=j5FPx9UmebQocH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0fa75c892a054d0db0e872d3e20f420c&docGuid=j5FPx9UmebQocH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b7c06211469c42128edec1e8d643c481&docGuid=j5FPx9UmebQocH "")


### **场景三：**基于GaiaDB文档开发provider（正常产出）
[https://console.cloud.baidu-int.com/comatestack/share/3635?token=0bf59f52](https://console.cloud.baidu-int.com/comatestack/share/3635?token=0bf59f52)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d8e9d32d2c2146889a27ca41004d71f8&docGuid=j5FPx9UmebQocH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ae3da23e573a406fbc0f4fb349195b84&docGuid=j5FPx9UmebQocH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=11239ea0ecda4259872289fef577f8e4&docGuid=j5FPx9UmebQocH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f79243d8ce04cc99ce8a031908e45fb&docGuid=j5FPx9UmebQocH "")




### 实践总结
#### Coding Agent 的有效点
* 能减少重复性工作（字段抽取、Schema 生成、CRUD 框架搭建）。
* 能在文档解析和中英文字段整理方面明显提高效率。
* 给出示例可以显著提升模型输出的稳定性。

#### 实际遇到的问题
* 不同模型遵守约束能力差异明显：即使要求“未找到 SDK 必须终止”，仍有模型继续生成错误代码。
* 输入过多导致判断错误：同时提供多个产品文档时，Agent 容易选错资源目标或搜索到错误的 SDK 文件。
* 路径与结构识别不稳定：工程层级复杂时，Agent 可能将 SDK 搜索到错误位置，造成后续逻辑全链路偏移。

（这些问题可部分通过补充约束、更明确的指令与小型示例来改善。）

#### 人工审核压力仍然存在
1. AI 生成的代码仍需人工 Review；随着生成量变大，审查过程容易疲劳。
2. 多轮迭代后，人工保持细节一致性的成本上升。
3. 这引出一个新的可能性：是否需要一个专门的“review agent”验证字段一致性、SDK 对齐、文件结构、命名规范等工程质量？

#### Agent 开发本身的矛盾
* Agent 需要持续迭代才能稳定输出。
* 但因 Agent 缩短了开发周期，业务排期也随之压缩，导致反而没有足够时间优化提示词与逻辑。
* 最终 Agent 很难达到“最优”，只能在“能用”和“可控”之间找到平衡。



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
