---
title: "设置环境变量"
description: "Agent运维实战——云审计事件分析"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Agent运维实战——云审计事件分析.md"
---
Agent运维实战——云审计事件分析

#### 🧑‍🏫 案例作者：[@刘雪超](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：运维
#### 🔧 使用工具：Ducc、Comate
#### 📒 案例概要：云审计值班Agent整合查询与调试技能，通过自然语言交互提升事件排查效率，支持端到端诊断与脚本调试。
## 0.背景
### 云审计系统简介
云审计(Baidu CloudTrail, 简称 BCT)是一项云上的审计服务，通过记录用户对云资源的关键操作行为，支持对云账户进行合规性检查、操作审核和事件回溯。

BCT提供通过云管理控制台、部分已接入服务API调用的操作记录查询，并支持将这些关键的用户活动长期存储到BOS中，以支持企业和机构的合规审计、事件追溯等。

云审计是一个流式数据处理系统，通过实时消费 console-hub 和 api-gateway 网关的 access 日志，获取各产品线的用户请求原始数据。系统基于配置平台中各产品线预先定义的接口配置规则，对原始日志进行解析、转换和标准化处理，最终产出结构化的审计事件。



目前系统每日处理原始日志**百亿**+，生成审计事件 **15 亿**，已接入产品线 100+，覆盖处理接口 3000+，完整记录所有用户的审计事件，确保操作可追溯、可审计。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=10a8479b223e4f83848f1b68a9dfcd6c&docGuid=t6EbkKV0pDRglL "")
结构化事件结果示例

```
{
  "eventType": "console",
  "eventSource": "iam",
  "eventName": "CreateUser",
  "eventTimeInMilliseconds": 1775195866000,
  "eventTime": "2026-04-03T05:57:46Z",
  "userIdentity": {
    "iamDomainId": "eb40xxxxxxxxx7788",
    "iamUserId": "196befxxxxxxxxx10811bc",
    "loginUserId": "",
    "userDisplayName": "xxxxxxxxx",
    "userName": "xxxxxxxxx"
  },
  "userIpAddress": "220.181.3.xxx",
  "userAgent": "Mozilla/5.0xxxxxxxxx,
  "requestId": "b24b2226-9167-41dc-9108-4d14ee7e8dd0",
  "resources": [
    {
      "resourceType": "resource-User",
      "resourceName": "05615xxxxxxxxx6b79"
    }
  ],
  "errorCode": "200",
  "operationMethod": "控制台",
  "originRequestParameters": {
    "query": {
      "locale": [
        "zh-cn"
      ]
    },
    "body": "{... ...}"
  },
  "originResponse": {
    ... ...
    }
  },
  "success": true
}
```
### 方案
云审计系统每日处理原始日志百亿+，需要完整记录所有用户的审计事件。随着业务快速发展，客户对云审计的诉求与日俱增，越来越多的产品线需要接入云审计。然而，接入产品的 RD 往往不熟悉 JS 脚本编写和配置平台操作，遇到问题时需要云审计研发人员随时支持协助定位，人工排查耗时长、效率低。

云审计值班 Agent 将分散的查询能力整合起来，通过自然语言交互，帮助值班人员快速定位审计事件问题，显著提升值班效率。

|**待解决问题**|**解决思路**|
|-|-|
|**1. 问题查询效率低，响应速度慢**• 需要在多个系统间切换• 手动拼接查询条件• 人工排查耗时长，影响值班效率|整合如下skill, 通过自然语言交互直接调用 API，秒级返回结果`cloud-audit`（查询云审计事件，支持按时间范围、用户、资源、操作类型搜索）和`bls-query`（查询 BLS 日志，支持按 RequestID、用户ID、自定义条件查询）`js-debug` 执行 JS 代码、捕获执行错误、返回解析结果、支持变量注入。|
|**2. 问题定位链路长**• 需要从原始日志查起• 需判断日志缺失/解析失败/规则配置问题• 缺乏统一排查工具|使用 `audit-check` 技能（检查审计事件是否存在、验证 API 事件解析结果， 分析js脚本）进行端到端诊断：先检查审计事件 → 不存在则自动查询 BLS 原始日志 → 分析日志内容给出明确原因|
|**3. 专业知识门槛高**• 需熟悉云审计事件结构• 需了解各产品线接口配置规则• 新人上手成本高|自然语言交互界面，无需学习 BLS 语法和 API 调用方式；Agent 自动解析用户输入并生成正确查询；内置值班知识库，新人快速上手|

## 设计思路
```
graph TB
    User[用户] --> Input[输入问题]
    Input --> TopSkill[值班问题分析Skill]

    TopSkill -->|调度| BLSQuery[BLS Query]
    TopSkill -->|调度| CloudAudit[Cloud Audit]
    TopSkill -->|调度| ResourceCode[Resource Code]
    TopSkill -->|调度| Debug[JS Debug]
    TopSkill -.->|待扩展| OtherSkills[其他 Skills...]

    BLSQuery --> BLS[(BLS日志集)]
    CloudAudit --> CA[(云审计服务)]
    ResourceCode --> Code[(源代码)]
    Debug --> Node[(js执行服务)]

    BLS & CA & Code & Node --> TopSkill
    TopSkill --> Output[分析报告]
    Output --> User
```
```
prompt  
实现一个云审计值班机器人，他的主要作用是代替一些常规问题的查询工作。值班人在值班过程中，常常查询阅读的信息有
    1. bls日志集，其中有云审计服务的源数据和业务日志。 
    2.云审计数据，通过调用接口查询事件配置以及生成出来的事件。
    3. 云审计源代码，阅读源代码以判断分析一些数据为什么不符合预期。
使用agent实现这个功能的思路是，
    1. bls-query skill 让agent可以通过请求id, 时间段，账户等信息，查询云审计收到的源数据以及在处理这个事件过程中产生的业务日志。 
    2. cloud-audit skill ,让agent可以通过调接口的方式查询某个事件在云审计平台配置的解析规则，以及查询云审计解析事件产生的事件，来判断是否解析成功，解析出什么数据了。
    3. resourcecode skill ，这个skill可以让agent读到云审计服务的源代码，辅助判断对源数据的处理过程。
    4。js-debug skill, 这个skill 让agent可以调用js脚本执行器，可以对拿到的源数据再次进行消费模拟，以得到一些中间结果，辅助判断问题。
基于这4个skill, 最后顶层skill, 描述值班问题的输入，什么时候该调用哪个skill, 如何分析问题，并给出一些值班例子。

bls-query skill - 查询BLS日志集（云审计源数据和业务日志）
cloud-audit skill - 调用接口查询事件配置和生成的事件
resourcecode skill - 阅读云审计服务源代码 (会造成上下文太大，废弃)
js-debug skill - 模拟消费源数据
顶层skill - 整合上述skill，描述值班问题输入、调用逻辑和分析方法
```


## 基础查询能力
### bls skill-日志查询能力
bls-query 封装 BLS SDK 提供 CLI 工具，无需登录控制台即可秒级返回结果。内置预设查询方法，自动处理凭证优先级和日志集映射，降低使用门槛。

核心查询能力：按用户ID查询、查询错误日志、按RequestID查询、按RequestID+URL查询、自定义SQL查询。

```
核心功能
基于百度云 BLS 服务查询线上用户操作日志

查询方法
Query()    通用日志查询    日志集、查询语句、时间范围、返回条数
QueryUserLogs()    查询指定用户操作日志    日志集、用户ID、时间范围
QueryByRequestID()    根据请求ID查询日志    日志集、请求ID、时间范围

查询语法支持
SQL 语法: select * from log limit 10
混合语法: match error \| select * limit 10
Match 语法: match 'requestId' limit 10

日志集映射
cloud-trail-stream-origin → cloud-trail (project)

调用方式
BAIDU_ACCESS_KEY_ID=ak BAIDU_SECRET_ACCESS_KEY=sk ./bin/bls-query query --project cloud-trail-sandbox --logstore cloud-trail-stream-api_sandbox --query "select * limit 10"
```
### bct skill-云审计服务信息查询能力
cloud-audit 封装百度云 SDK 提供 CLI 工具，无需进入云审计控制台即可查询审计事件/配置。支持多种过滤条件（RequestID、事件名称、时间范围等），自动处理环境变量凭证。提供 hestia profile 查询和测试功能，方便排查解析规则问题。

核心查询能力：查询审计事件、按 RequestID 查询、按事件名称查询、获取 hestia profile 信息、测试 profile。

|文件|作用|关键点|
|-|-|-|
|**SKILL.md**|技能元数据|定义技能名称、描述、环境变量要求、使用文档|
|**client.go**|Go 客户端|使用百度云 SDK 处理签名和 HTTP 请求|
|**main.go**|CLI 工具|解析命令行参数，调用客户端，格式化输出|
|**scripts/cloud-audit**|入口脚本|检查环境变量，自动编译，调用二进制|

```
认证方式： 使用百度云 SDK (github.com/baidubce/bce-sdk-go)，自动处理签名
client, err := bce.NewBceClientWithAkSk(ak, sk, endpoint)
请求结构： 根据实际 API 响应调整了数据结构

# 设置环境变量
export BAIDU_ACCESS_KEY_ID=your-ak
export BAIDU_SECRET_ACCESS_KEY=your-sk

查询方法
方法    功能    参数
Query()    通用事件查询    DomainID、过滤条件、时间范围、页大小
QueryByRequestID()    根据请求ID查询事件    DomainID、请求ID、时间范围
QueryByEventName()    根据事件名称查询    DomainID、事件名称、时间范围
配置查询方法
方法    功能    说明
GetProfile()    获取 Profile 配置    独立函数，通过 profileId 查询解析规则
TestProfile()    测试 Profile 解析    独立函数，用源数据测试解析结果

# 直接使用
./bin/cloud-audit query --domainId xxx --pageSize 10

# 或通过 skill 脚本
./.comate/skills/cloud-audit/scripts/cloud-audit query --domainId xxx
```
### js-debug skill-脚本调试能力
js-debug 基于 Node.js 提供 JS 代码执行器，支持实时执行 JS 代码并返回结果。针对云审计场景，产品 RD 在配置平台编写的 JS 解析脚本可能出现语法错误或逻辑错误，导致审计事件无法正常解析。该 skill 可以接收 JS 配置代码和测试数据，执行后返回解析结果或错误信息，帮助快速定位脚本问题。 

核心执行能力：执行 JS 代码、捕获执行错误、返回解析结果、支持变量注入。

```
核心功能 
基于 Node.js 执行用户提供的 JS 代码，用于调试解析脚本

执行方法
Execute()    通用 JS 执行    JS 代码字符串、输入数据对象、注入变量
ValidateScript()    脚本语法检查    JS 代码字符串

执行环境
运行时： Node.js
超时控制： 默认 5 秒，防止死循环
错误捕获： 捕获语法错误、运行时错误、超时错误

调用方式

直接执行 JS 代码
./bin/js-debug execute --code "'

通过 skill 脚本
./.comate/skills/js-debug/scripts/js-debug execute --code "..." --input "..."
```
## 端到端排查能力
audit-check 整合以上skill，提供端到端诊断能力。根据用户描述场景调用对应能力分析数据，根据结果给出明确原因和排查建议（日志缺失/解析失败/规则问题）。

核心查询能力：检查审计事件是否存在、查询 API 事件解析结果、获取并测试 profile配置、JS 脚本调试与优化。

```
audit-check核心功能
云审计值班检查工具，协助值班人员快速定位审计事件问题

命令    功能    必需参数
check    检查审计事件是否存在    --requestId, --domainId
api    查询API事件解析结果    --requestId, --url
debug    JS脚本调试    --requestId, --url, [--timePoint]
```


```
flowchart TD
    Start([开始]) --> Parse[解析参数<br/>requestId, domainId, timePoint]
    Parse --> Validate{参数完整?}
    Validate -->|否| Error[返回错误]
    Validate -->|是| QueryAudit[查询云审计事件<br/>cloud-audit skill]

    QueryAudit --> AuditFound{找到事件?}
    AuditFound -->|是| OutputEvent[输出: 事件已找到]
    AuditFound -->|否| QueryBLS[查询 BLS 源数据<br/>bls-query skill]

    OutputEvent --> End([结束])

    QueryBLS --> BLSFound{找到源数据?}
    BLSFound -->|是| OutputSource[输出: 源数据已找到<br/>建议检查 Profile/业务日志]
    BLSFound -->|否| OutputNone[输出: 事件未收到<br/>建议检查信息/网关]

    OutputSource --> End
    OutputNone --> End
```


```
flowchart TD
    Start([开始]) --> Parse[解析参数<br/>requestId, url, timePoint]
    Parse --> Validate{参数完整?}
    Validate -->|否| Error[返回错误]
    Validate -->|是| QueryBLS[查询 BLS 源数据<br/>bls-query skill]

    QueryBLS --> BLSFound{找到源数据?}
    BLSFound -->|否| Error
    BLSFound -->|是| ParseMsg[解析 receive_msg<br/>Base64 解码]

    ParseMsg --> Convert[转换为云审计事件格式]
    Convert --> HasEvents{有事件?}

    HasEvents -->|否| Output[输出: count=0]
    HasEvents -->|是| GetProfile[查询 Profile 配置<br/>cloud-audit skill]

    GetProfile --> ProfileFound{找到 Profile?}
    ProfileFound -->|否| SetProfileError[设置 profileError]
    ProfileFound -->|是| TestProfile[调用 TestProfile<br/>cloud-audit skill]

    TestProfile --> TestSuccess{测试成功?}
    TestSuccess -->|否| SetTestError[设置 testProfileError]
    TestSuccess -->|是| SetTestResult[设置 testProfile]

    SetProfileError --> Output
    SetTestError --> Output
    SetTestResult --> Output

    Output --> End([结束])
```


```
flowchart TD
    Start([开始]) --> Parse[解析参数<br/>requestId, url, timePoint]
    Parse --> Validate{参数完整?}
    Validate -->|否| Error[返回错误]
    Validate -->|是| GetProfile[获取 Profile 配置与 JS 脚本<br/>cloud-audit skill]

    GetProfile --> ProfileFound{Profile 存在?}
    ProfileFound -->|否| OutputNoProfile[输出: Profile 不存在<br/>建议配置解析规则]
    ProfileFound -->|是| QueryBLS[查询 BLS 源数据<br/>bls-query skill]

    OutputNoProfile --> End([结束])

    QueryBLS --> BLSFound{找到源数据?}
    BLSFound -->|否| OutputNone[输出: 未找到源数据<br/>建议检查信息/网关]
    BLSFound -->|是| ParseMsg[解析 receive_msg<br/>提取事件详情]

    OutputNone --> End

    ParseMsg --> PrepareInput[准备执行输入<br/>JS 脚本 + 源数据]
    PrepareInput --> ExecuteJS[执行 JS 脚本<br/>js-debug skill]

    ExecuteJS --> JSError{执行成功?}
    JSError -->|是| OutputSuccess[输出: 解析成功<br/>返回解析结果]
    JSError -->|否| AnalyzeError[分析错误信息<br/>定位问题原因]

    OutputSuccess --> End

    AnalyzeError --> ModifyJS[修改 JS 脚本<br/>增加调试信息]
    ModifyJS --> ReExecute[重新执行优化后的 JS<br/>js-debug skill]

    ReExecute --> ReCheck{执行成功?}
    ReCheck -->|是| OutputFixed[输出: 修复成功<br/>返回正确代码建议]
    ReCheck -->|否| AnalyzeError

    OutputFixed --> End

```


## 场景测试
### 场景1 事件存在确定
|**项目**|**内容**|
|-|-|
|场景描述|用户携带具体请求信息（如 RequestID、DomainID）询问审计事件是否存在，以及事件的相关详情。|
|场景应用|值班人员收到用户反馈，需要确认某个操作是否生成了审计事件。用户提供 RequestID 和 DomainID，值班人员使用 audit-check 快速确认。|
|使用的能力|audit-check check：端到端检查审计事件，首先调用 cloud-audit 查询云审计服务，如果找到事件，直接返回事件详情。|
|预期结果|系统返回审计事件已找到，显示事件来源为云审计服务。输出包含完整的事件信息，如事件 ID、事件名称、事件时间、请求 ID、用户身份、资源信息等，并提示找到的记录数量。|

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b017aea64d2a4f1ab40099813f274165&docGuid=t6EbkKV0pDRglL "")
### 场景2 事件不存在
|**项目**|**内容**|
|-|-|
|场景描述|用户携带具体请求信息（如 RequestID、DomainID）询问审计事件是否存在，以及事件的相关详情。|
|场景应用|值班人员收到用户反馈，需要确认某个操作是否生成了审计事件。用户提供 RequestID 和 DomainID，值班人员使用 audit-check 快速确认。|
|使用的能力|audit-check check：端到端检查审计事件，首先调用 cloud-audit 查询云审计服务，如果找到事件，直接返回事件详情。|
|预期结果|系统返回审计事件已找到，显示事件来源为云审计服务。输出包含完整的事件信息，如事件 ID、事件名称、事件时间、请求 ID、用户身份、资源信息等，并提示找到的记录数量。|

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f4664621043d4db5b0ac68af39b84bf9&docGuid=t6EbkKV0pDRglL "")
### 场景3 事件配置debug
|**项目**|**内容**|
|-|-|
|场景描述|产品线配置了接口解析规则（Hestia Profile）后，需要验证配置是否正确。用户提供接口 URL 和示例 RequestID，咨询相关配置。|
|场景应用|产品线开发人员配置新接口的解析规则后，需要测试规则是否能正确解析日志。值班人员使用 audit-check 的 api 命令进行验证。|
|使用的能力|audit-check api：API 事件解析验证，调用 bls-query 查询 BLS 日志（按 RequestID + URL 筛选），解析 @raw 字段中的 receive_msg，转换为云审计事件格式，获取 Profile 配置并测试解析结果。|
|预期结果|系统返回完整的解析验证信息，包括请求 ID、接口 URL、查询时间范围、找到的日志数量。输出解析出的事件信息、对应的 Profile 配置信息（Profile ID、接口路径、服务名称、状态、映射规则等）和 Profile 测试结果，帮助验证配置是否正确。|

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ff33c613aca44bffbc03d03741b9a177&docGuid=t6EbkKV0pDRglL "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=679f79adf9314d5b86f54473d10e4f64&docGuid=t6EbkKV0pDRglL "")
## 5.决策与协调能力
在增加相关的问题排查能力后，agent仍然缺乏对云审计值班业务的理解，不知道自己的角色定位、可用技能以及如何根据用户问题选择合适的排查方案，需要通过 rules 明确行为规范和业务逻辑。

**通过增加全局rules, 排查工具增加了以下能力：**

1. **角色定位能力**：明确自己是云审计值班机器人，准确理解业务场景和用户诉求
2. **智能技能选择能力**：根据用户问题类型自动选择合适的技能，优先使用 audit-check 进行端到端诊断
3. **对话引导能力**：主动问候用户并展示可用能力，引导用户提出具体问题
4. **标准化排查流程能力**：按照"理解问题→选择技能→执行查询→分析结果→给出建议"的标准流程进行排查
5. **技能协调能力**：audit-check 作为顶层协调技能，自动整合底层的能力，实现端到端诊断

```
# IAM Duty Project Rules

This file contains project-specific rules and guidelines for the IAM Duty project.

## Role Definition

You are a **Cloud Audit Duty Bot** (云审计值班机器人). Your mission is to help users query cloud audit information and troubleshoot cloud audit issues using multiple skills.

## Cloud Audit System Overview

Cloud Audit (云审计) is a stream processing system that:
- Consumes source log information from various log stores
- Processes and transforms the logs in real-time
- Produces audit events as output
- Provides visibility into user operations and system changes

## Available Skills

At the start of each conversation, you must present the available skills and their capabilities to the user:

### 1. cloud-audit
- Query cloud audit events
- Search audit logs by time range, user, resource, or operation type
- Analyze audit event patterns

### 2. bls-query
- Query BLS (Baidu Log Service) logs
- Search logs by RequestID, UserID, or custom queries
- Query error logs and authentication failures
- Useful for root cause analysis

### 3. audit-check
- Perform audit rule checks
- Validate compliance with audit policies
- Check for missing or incomplete audit events

### 4. js-debug
- Execute JavaScript code and return results
- Test JS scripts with sample data
- Identify syntax and runtime errors in parsing logic

## Conversation Start Protocol

When a new conversation begins, you must:

1. Greet the user as the Cloud Audit Duty Bot
2. Display the available skills with a brief description of each
3. Ask the user what they need help with

Example greeting:
```
👋 你好！我是云审计值班机器人。

我可以帮助你查询云审计信息和排查问题，目前支持以下能力：

📊 cloud-audit - 查询云审计事件
🔍 bls-query - 查询 BLS 日志（按 RequestID、用户ID、错误等）
✅ audit-check - 审计规则检查和合规性验证
🔧 js-debug - JS 脚本调试与执行

请告诉我你需要什么帮助？
```

## Troubleshooting Workflow

When helping users troubleshoot issues:

1. **Understand the Problem** - Ask for relevant details (RequestID, time range, user, resource, etc.)
2. **Choose the Right Skill** - Select the appropriate skill based on the issue type
3. **Execute Query** - Run the query with proper parameters
4. **Analyze Results** - Interpret the results and identify the root cause
5. **Provide Clear Explanation** - Explain findings in simple terms
6. **Suggest Actions** - Recommend next steps if applicable

## Project Structure

- `cmd/` - Command-line applications
- `skills/` - Skill implementations
- `docs/` - Documentation
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=053fdd6931fb49848ab77926f2d18bc9&docGuid=t6EbkKV0pDRglL "")
```
**Use audit-check when:**
- User asks "有没有这条审计事件" (Is there this audit event?)
- User asks "为什么事件没有生成" (Why wasn't this event generated?)
- User asks "RequestID xxx 的事件在哪里" (Where is the event for RequestID xxx?)
- User asks "某个时间点的事件查询" (Query events at a specific time)
- User asks "API事件解析不准"、"解析出的事件" (API event parsing is inaccurate / parsed events)
- User mentions "查审计事件"、"查事件"、"审计值班" (Query audit events / Query events / Audit duty)
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c5469aed789942a3a4b59ed56330b5a7&docGuid=t6EbkKV0pDRglL "")
## 6.其他todo & 问题
|能力|要解决的问题|
|-|-|
|**相关文档问题解答能力**|用户经常询问云审计相关的配置、规则、最佳实践等问题，当前需要人工查阅文档。需要接入云审计文档知识库，支持自然语言问答，快速响应用户咨询。|

1. 在问题解决模式写死在代码里的情况下，通常大模型的发挥空间有限，但是写死解决路径又有利于特定问题被快速准确的解决，如何控制这个边界
2. 源代码的上下文占用太多，想到的解决方式是，1. 把关键处理的部分代码放到source-code-skill里. 2. 让agent总结文字版 ，放到source-code-skill里



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
