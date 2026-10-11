---
title: "背景"
description: "AI-SOC Rules 实战分享"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\AI-SOC Rules 实战分享.md"
---
AI-SOC Rules 实战分享

#### 🧑‍🏫 案例作者：[@王贺军](https://ku.baidu-int.com?t=mention&mt=contact&id=b1a143f0-fced-11f0-b173-81b0b0bcf94e)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了AI-Coding在SOC系统中的应用，通过沉淀项目规范为Rules，提升团队需求交付效率和质量。实战案例包括Error日志治理改造和LLM Server消费者逻辑重构，展示了如何通过AI-Coding-Agent实现繁琐编码任务的自动化，提高开发效率。同时，强调了规则的重要性，确保生成代码符合标准，降低维护成本。
**本文档视频讲解：**[AI-SOC Rules 实战分享](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56879?activityId=8747?t=mention&mt=doc&dt=sdk)

# 背景
* 于组织，**AI-Coding**是**AI内化**的重要手段之一
* 于团队，SOC已经沉淀了一些Rules[Rules 沉淀](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/TV-qnpj85H/zzcTImQ1NG/xthfol-_RDgo1S?t=mention&mt=doc&dt=doc)，需借助AI-Coding提升团队需求交付效率和质量，推动项目更快地迭代
* 于个人，积极拥抱AI，提升开发效率，释放更多精力去做更有挑战的事，如聚焦架构、聚焦业务等

# Rules介绍
通过巧妙使用AI-Coding-Agent提供的Rules，沉淀项目规范，包括但不限于：编码规范、项目架构、技术栈、注意事项、开发流程等等，用来尽量的约束大模型不确定性的行为，保证生成符合我们标准的代码。

更多rules介绍见：[2026研发提效目标推进思路（for SO&BPIT）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/H4gIgyYDqo/vtfPMnSOENOMHt?t=mention&mt=doc&dt=doc)



# 实战


## 实战一：繁琐且耗费精力的编码场景
### 背景：SOC系统Error日志治理
* 线上告警策略简单，只要有Error日志，就会触发告警，大部分告警非严重问题，不需要RD第一时间跟进，容易淹没重要告警
* 告警内容以Message字符串为主，难以有效聚合，无法统计同一Error的量级，无法配置同比类告警策略

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=28ba9d13d3bd46a8ade104bb23544cd9&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5ef4bc87189948fba1bcef79f74f0c9d&docGuid=1JNvSH1K3E-SfD "")
* 已经设计出统一的告警治理技术方案，错误分级（Error/Warning）、错误信息携带error_code、error_code先注册后使用、Metric自动采集、监控大盘搭建
* 推进RDs进行存量告警治理，但**改造范围之广，耗费精力之多**，且经常因高优先级支持业务需求开发，Error改造**进度十分缓慢**
* [自定义error及log打印](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/TV-qnpj85H/zzcTImQ1NG/n7YrmBLb3Qj-aI?t=mention&mt=doc&dt=doc)
* [存量业务自定义Error改造（2025 Q4）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/TV-qnpj85H/zzcTImQ1NG/vOJdYvAVCzPkr0?t=mention&mt=doc&dt=doc)

### 任务
* 借助AI-Coding-Agent进行Error日志治理改造工作，推进治理速度，提升告警质量和可观测性

### 动作
1. 沉淀**日志规范、自定义错误日志规范** Rules ，见[Rules 沉淀](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/TV-qnpj85H/zzcTImQ1NG/xthfol-_RDgo1S?t=mention&mt=doc&dt=doc)**【人】**
2. 针对本次要做的任务，按人的改造路径，书写一个改造指南Rule，Rule里关联上日志规范Rule、自定义错误日志规范Rule**【人】**

```
---
description: CustomError分层改造指南，根据代码不同层级去改造旧代码，包含错误码选择(注册)、错误定义、错误日志输出等
globs: **/*.go
alwaysApply: false
---

# CustomError分层改造指南
#### 前置原则（重要！！！）
**1、myerrors.NewCustomError 使用 ErrCodeType前，一定要判断 error_list.go中有无注册，如果没有注册，一定要在合适位置注册，否则会panic**

**2、先判断代码属于哪一层级，再使用对用层级改造规范**

**3、改造过程要遵循 [自定义错误规范](mdr:.docs/custom_error.md)和[日志规范](.docs/log.md)**

## 背景
- 线上存在大量的使用 resource.LoggerLogic.Error 方式打印error日志，缺少error_code，无法有效针对错误进行聚合统计
- 使用者没有关注错误属于error类别 还是 warning类别，直接使用error类别进行打印，导致线上大量无效告警

## 目标
- 按照本文档规范，对error日志进行改造

## 分层改造规范

> 无论哪一层都要先查看有没有导入包`myerrors "icode.baidu.com/baidu/sec-llm/sec-smart-chat/pkg/util/errors"`，没有则需要先导入

### 1. API层改造 (`api/servers/httpserver/controller/**/*.go`)

**参考示例**: [update_level.go](mdr:api/servers/httpserver/controller/soc/alert/update_level.go)

```go
// 标准改造模式
func UpdateLevel(ctx context.Context, req ghttp.Request) ghttp.Response {
    var reqData UpdateLevelReq
    err := httpx.Parse(req.HTTPRequest(), &reqData)
    if err != nil {
        //生成自定义error对象
        merr := myerrors.NewCustomError(myerrors.WarnParamParse, err.Error())

        //调用OutputLog方法打印日志
        merr.OutputLog(ctx, resource.LoggerLogic)

        //返回时使用error_code和 error_msg
        return ghttp.NewJSONResponse(http.StatusOK, types.NewHTTPResponse(merr.GetErrCode(), merr.Error(), nil))
    }

    // 参数校验
    if reqData.ID == nil && reqData.Identifier == nil {
        merr := myerrors.NewCustomError(myerrors.WarnParamVerify, "请填入告警id")
        return ghttp.NewJSONResponse(http.StatusOK, types.NewHTTPResponse(merr.GetErrCode(), merr.Error(), nil))
    }

    // 业务调用
    resp, merr := alert.UpdateLevel(ctx, &socpb.UpdateAlertLevelReq{...})
    if merr != nil {
        return ghttp.NewJSONResponse(http.StatusOK, types.NewHTTPResponse(merr.GetErrCode(), merr.Error(), nil))
    }

    return ghttp.NewJSONResponse(http.StatusOK, types.NewOKHTTPResponse(ret))
}
```

### 2. RPC调用层改造 (`api/model/service/**/*.go`)

**参考示例**: [update_level.go](mdr:api/model/service/soc/alert/update_level.go)

```go
// 标准RPC调用模式
func UpdateLevel(ctx context.Context, req *socpb.UpdateAlertLevelReq) (*socpb.UpdateAlertLevelResp, *myerrors.CustomError) {
    resp, err := resource.SOCRPC.Request(ctx, &socpb.UpdateAlertLevelResp{},
        pbrpc.NewRequest(socpb.ServiceName, socpb.UpdateAlertLevelMethod, req, nil))

    //使用 PBRPCCustomError方法提取自定义error
    if merr := myerrors.PBRPCCustomError(err, resp); merr != nil {
        merr.OutputLog(ctx, resource.LoggerLogic)
        return nil, merr
    }
    ret, ok := resp.Data().(*socpb.UpdateAlertLevelResp)
    if !ok {
        return nil, myerrors.NewCustomError(myerrors.ErrRPCRespParse, "UpdateAlertLevelResp Parse Error")
    }
    return ret, nil
}
```

### 3. RPC定义层改造 (各个RPC服务中`{module}/servers/pbserver/**/*.go`)

**参考示例**: [alert_update_level.go](mdr:soc/servers/pbserver/soc/alert_update_level.go)

```go
// 标准RPC接口定义模式
func (s *Service) UpdateAlertLevel(ctx context.Context, req pbrpc.Request) (pbrpc.Response, error) {
    reqBody := &socpb.UpdateAlertLevelReq{}
    err := req.Bind(reqBody)
    if err != nil {
        merr := myerrors.NewCustomError(myerrors.ErrParamParse, err.Error())
        merr.OutputLog(ctx, resource.LoggerLogic)
        return pbrpc.NewResponse(nil, nil, 
            pbrpc.ErrorCodeSetter(merr.ErrCode), 
            pbrpc.ErrorTextSetter(merr.ErrMsg)), nil
    }

    // 业务逻辑调用
    resp, merr := alert.UpdateAlertLevel(ctx, &alert.UpdateAlertLevelReq{...})
    if merr != nil {
        merr.OutputLog(ctx, resource.LoggerLogic)
        return pbrpc.NewResponse(nil, nil,
            pbrpc.ErrorCodeSetter(merr.ErrCode),
            pbrpc.ErrorTextSetter(merr.ErrMsg)), nil
    }

    return pbrpc.NewResponse(ret, nil), nil
}
```

### 4. 业务逻辑层改造 (各个RPC服务中`{module}/model/service/**/*.go`)

**参考示例**: [update_level.go](mdr:soc/model/service/alert/update_level.go)

```go
// 标准业务逻辑层方法定义模式
func UpdateAlertLevel(ctx context.Context, req *UpdateAlertLevelReq) (*UpdateAlertLevelResp, *myerrors.CustomError) {
    var err error
    alert := req.AlertInfo
    if alert == nil {
        alert, err = GetRootAlert(ctx, req.AlertID)
        if err != nil {
            merr := myerrors.NewCustomError(myerrors.ErrMysql, err.Error())
            return nil, merr
        }
    }
    rootID := alert.ID
    if alert.SimilarRootID != 0 {
        rootID = alert.SimilarRootID
        alert, err = GetRootAlert(ctx, alert.SimilarRootID)
        if err != nil {
            merr := myerrors.NewCustomError(myerrors.ErrMysql, err.Error())
            return nil, merr
        }
    }
    if alert.Status != int32(socpb.AlertStatus_ALERT_STATUS_NOT_REVIEW) {
        merr := myerrors.NewCustomError(myerrors.WarnAlertInvalidOperate, "当前告警已处置，不可调整等级")
        return nil, merr
    }

    err = resource.MySQLClient.Transaction(func(tx *query.Query) error {
        if err := tx.SocAlertAll.WithContext(ctx).UpdateLevel(updateList, req.Level, req.Owner, req.Manual); err != nil {
            resource.LoggerLogic.Error(ctx, err.Error())
            return err
        }
        return nil
    })
    if err != nil {
        merr := myerrors.NewCustomError(myerrors.ErrMysql, err.Error())
        return nil, merr
    }

    return ret, nil
}
```

> 业务逻辑层代码较多，且可能调用很多别的方法，或者被别的方法调用，这一层改造要检查完整的调用链，防止漏改。改造区分上三层，使用通用改造方法


## 改造检查清单
- 是否导入包: `myerrors "icode.baidu.com/baidu/sec-llm/sec-smart-chat/pkg/util/errors"`
- 创建 或者 复用 error_code，使用 `NewCustomError` 创建业务错误
- 调用 `OutputLog` 输出错误日志
- 函数签名从 `error` 改为 `*myerrors.CustomError`（
    - 前提是本函数所有return的 error都改造成 *myerrors.CustomError
    - 需要检查调用方接收error。需要万分注意，具体case参照 [自定义错误规范](mdr:.docs/custom_error.md) 中 ##特别注意 这一部分
- 使用 `PBRPCCustomError` 处理RPC返回错误
```
3. 使用**Spec模式**Comate Agent，输入简单提示词，触发任务执行 

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d57157ee7e4e43549d82dae47238350a&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e2a156e126114689ac46d7ca8a2e6b10&docGuid=1JNvSH1K3E-SfD "")
    1. 首先，它会**检查 Rule，理解需求 以及 查看必要代码**，输出一个需求文档**【Agent】**，我们只需要检阅一下此文档，看有无明显错误，如果有则纠正，没有则继续 **【人】**
        1. 如下，我纠正了一个错误，error_list中已经注册了通用的json解析错误码，直接复用即可 （**纠正更前置**）


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=333a67e097c64c64898a307c57a19b7e&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b4e2468559274df8ad9007f2bd92fec2&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fd4f233ccd7d451fa121fcd7cb900260&docGuid=1JNvSH1K3E-SfD "")


```
# NotifyWorkflowRun CustomError 改造需求文档

## 需求场景
对 `notifyserver/model/service/run_notify_workflow.go` 文件进行 CustomError 改造，将现有的错误处理逻辑替换为标准化的自定义错误处理机制。

## 架构技术方案
### 代码层级识别
- **文件路径**: `notifyserver/model/service/run_notify_workflow.go`
- **所属层级**: 业务逻辑层（第4层）
- **改造类型**: 业务逻辑层改造

### 错误码规划
基于 `pkg/util/errors/error_list.go` 中的现有错误码，主要使用以下类别：
- **数据库错误**: `ErrMysql` (101), `WarnMysql` (102)
- **RPC服务错误**: `ErrRPCServer` (11)
- **业务逻辑错误**: `ErrBusinessLogic` (1201), `WarnBusinessLogic` (1202)
- **通知相关错误**: `ErrSendMsg` (71001), `WarnTemplateQuery` (90010)
- **参数相关错误**: `ErrParamParse` (1001), `WarnParamParse` (1002)
- **EAC相关错误**: `ErrEacGetUserResource` (305), `WarnEacGetUserResource` (306)

## 影响文件
### 主要修改文件
- `notifyserver/model/service/run_notify_workflow.go` (2664行)
  - 修改函数签名：返回值改为 `(*Type, *myerrors.CustomError)`
  - 替换所有错误创建和返回逻辑
  - 添加错误日志输出

### 可能影响的调用文件
需要检查以下文件的调用兼容性：
- `notifyserver/servers/pbserver/notifyserverpb/service.go` (RPC定义层)
- `api/model/service/notify/*.go` (RPC调用层，如存在)
- `api/servers/httpserver/controller/notify/*.go` (API层，如存在)

## 实现细节

### 核心函数改造清单

#### 1. Start 函数 (第85行)
```go
// 当前签名
func (s *NotifyWorkflowRun) Start(ctx context.Context, reqBody *notifyserverpb.StartNotifyWorkflowReq) (resp notifyserverpb.StartNotifyWorkflowResp, err error)

// 改造后签名
func (s *NotifyWorkflowRun) Start(ctx context.Context, reqBody *notifyserverpb.StartNotifyWorkflowReq) (resp notifyserverpb.StartNotifyWorkflowResp, merr *myerrors.CustomError)
```

#### 2. RunNextNode 函数 (第435行)
```go
// 当前签名
func (s *NotifyWorkflowRun) RunNextNode(ctx context.Context, req *notifyserverpb.RunNextWorkflowNodeReq) error

// 改造后签名
func (s *NotifyWorkflowRun) RunNextNode(ctx context.Context, req *notifyserverpb.RunNextWorkflowNodeReq) *myerrors.CustomError
```

#### 3. End 函数 (第620行)
```go
// 当前签名
func (s *NotifyWorkflowRun) End(ctx context.Context, endReq *notifyserverpb.EndNotifyWorkflowReq) error

// 改造后签名
func (s *NotifyWorkflowRun) End(ctx context.Context, endReq *notifyserverpb.EndNotifyWorkflowReq) *myerrors.CustomError
```

#### 4. ModifyCard 函数 (第1080行)
```go
// 当前签名
func (s *NotifyWorkflowRun) ModifyCard(ctx context.Context, req *notifyserverpb.ModifyNotifyCardReq) error

// 改造后签名
func (s *NotifyWorkflowRun) ModifyCard(ctx context.Context, req *notifyserverpb.ModifyNotifyCardReq) *myerrors.CustomError
```

#### 5. BuildNewMsgAndSend 函数 (第1250行)
```go
// 当前签名
func (s *NotifyWorkflowRun) BuildNewMsgAndSend(ctx context.Context, req *notifyserverpb.BuildNewMsgAndSendReq) error

// 改造后签名
func (s *NotifyWorkflowRun) BuildNewMsgAndSend(ctx context.Context, req *notifyserverpb.BuildNewMsgAndSendReq) *myerrors.CustomError
```

### 错误处理改造示例

#### 数据库操作错误
```go
// 改造前
info, errA := resource.MySQLClient.Notify.WithContext(ctx).GetByRelationIDAndLevel(reqBody.Id, consts.NotifyTypeAlert, reqBody.Level)
if errA != nil {
    merr := myerrors.NewCustomError(myerrors.ErrMysql, errA.Error())
    merr.OutputLog(ctx, resource.LoggerLogic)
    return notifyserverpb.StartNotifyWorkflowResp{}, merr
}

// 改造后（保持一致，已经是标准用法）
info, errA := resource.MySQLClient.Notify.WithContext(ctx).GetByRelationIDAndLevel(reqBody.Id, consts.NotifyTypeAlert, reqBody.Level)
if errA != nil {
    merr := myerrors.NewCustomError(myerrors.ErrMysql, errA.Error())
    merr.OutputLog(ctx, resource.LoggerLogic)
    return notifyserverpb.StartNotifyWorkflowResp{}, merr
}
```

#### 业务逻辑错误
```go
// 改造前
if s.TicketData == nil {
    merr := myerrors.NewCustomError(myerrors.WarnTemplateQuery, "ticket data is nil")
    merr.OutputLog(ctx, resource.LoggerLogic)
    return notifyserverpb.StartNotifyWorkflowResp{}, merr
}

// 改造后（保持一致，已经是标准用法）
if s.TicketData == nil {
    merr := myerrors.NewCustomError(myerrors.WarnTemplateQuery, "ticket data is nil")
    merr.OutputLog(ctx, resource.LoggerLogic)
    return notifyserverpb.StartNotifyWorkflowResp{}, merr
}
```

#### 简单错误返回
```go
// 改造前
if err != nil {
    resource.LoggerLogic.Warning(ctx, fmt.Sprintf("transaction error: %v", err))
    return
}

// 改造后
if err != nil {
    merr := myerrors.NewCustomError(myerrors.ErrMysql, fmt.Sprintf("transaction error: %v", err))
    merr.OutputLog(ctx, resource.LoggerLogic)
    return notifyserverpb.StartNotifyWorkflowResp{}, merr
}
```

#### RPC调用错误
```go
// 改造前
resp, err := resource.InfoFlowRPC.Request(ctx, &infoflowpb.PushCardResp{},
    pbrpc.NewRequest(infoflowpb.ServiceName, infoflowpb.PushCardMethod, notifyReq, nil))
if err = myerrors.PBRPCError(err, resp); err != nil {
    resource.LoggerLogic.Warning(ctx, fmt.Sprintf("info flow notify failed, error: %v", err))
    return err
}

// 改造后
resp, err := resource.InfoFlowRPC.Request(ctx, &infoflowpb.PushCardResp{},
    pbrpc.NewRequest(infoflowpb.ServiceName, infoflowpb.PushCardMethod, notifyReq, nil))
if err = myerrors.PBRPCError(err, resp); err != nil {
    merr := myerrors.NewCustomError(myerrors.ErrRPCServer, fmt.Sprintf("info flow notify failed, error: %v", err))
    merr.OutputLog(ctx, resource.LoggerLogic)
    return merr
}
```

## 边界条件与异常处理

### 1. 空指针检查
```go
// 改造前
if s.Alert == nil {
    return
}

// 改造后
if s.Alert == nil {
    merr := myerrors.NewCustomError(myerrors.ErrRecordNotFound, "alert data is nil")
    merr.OutputLog(ctx, resource.LoggerLogic)
    return notifyserverpb.StartNotifyWorkflowResp{}, merr
}
```

### 2. 数组越界检查
```go
// 改造前
if len(receivers) == 0 {
    if s.NotifyType == consts.NotifyTypeTicket {
        return notifyserverpb.StartNotifyWorkflowResp{}, nil
    }
    merr := myerrors.NewCustomError(myerrors.WarnTemplateQuery, "no receiver found")
    merr.OutputLog(ctx, resource.LoggerLogic)
    return notifyserverpb.StartNotifyWorkflowResp{}, merr
}

// 改造后（保持一致，已经是标准用法）
```

### 3. JSON解析错误
```go
// 改造前
err = json.Unmarshal([]byte(messageInfo.InfoflowMessage), &notifyAlertInfo)
if err != nil {
    resource.LoggerLogic.Error(ctx, fmt.Sprintf("reBuildInfo json unmarshal notifyAlertInfo failed, error: %v", err))
    return "", 0, err
}

// 改造后
err = json.Unmarshal([]byte(messageInfo.InfoflowMessage), &notifyAlertInfo)
if err != nil {
    merr := myerrors.NewCustomError(myerrors.ErrJSONUnmarshal, fmt.Sprintf("reBuildInfo json unmarshal notifyAlertInfo failed, error: %v", err))
    merr.OutputLog(ctx, resource.LoggerLogic)
    return "", 0, merr
}
```

## 数据流动路径

### 1. 通知工作流启动流程
```
StartNotifyWorkflowReq -> Start() -> 数据库查询 -> 工作流配置 -> 消息构建 -> 通知发送
```

### 2. 下一节点执行流程
```
RunNextWorkflowNodeReq -> RunNextNode() -> 节点查询 -> 接收者获取 -> 消息重建 -> 通知发送
```

### 3. 工作流结束流程
```
EndNotifyWorkflowReq -> End() -> 节点状态更新 -> 卡片修改 -> 缓存更新
```

## 预期成果

### 1. 函数签名标准化
- 所有主要函数返回值统一为 `(*Type, *myerrors.CustomError)`
- 保持与现有 CustomError 框架的一致性

### 2. 错误处理标准化
- 所有错误使用 `myerrors.NewCustomError` 创建
- 所有错误调用 `OutputLog` 方法输出日志
- 使用合适的错误码分类

### 3. 调用链兼容性
- 确保上层调用者能够正确处理新的返回类型
- 保持 RPC 接口兼容性

### 4. 错误信息丰富化
- 错误信息包含足够的上下文信息
- 便于问题定位和调试

## 验证标准

### 1. 编译验证
```bash
cd notifyserver && CC=/usr/bin/gcc CXX=/usr/bin/g++ go build -o ../bin/notify
```

### 2. 功能验证
- 通知工作流启动功能正常
- 节点流转功能正常
- 工作流结束功能正常
- 卡片修改功能正常

### 3. 错误处理验证
- 各种异常情况能够正确返回 CustomError
- 错误日志输出格式正确
- 错误码分类合理
```
```
# notifyserver服务error改造需求文档

## 需求概述
对notifyserver/model/service目录下的5个Go文件进行CustomError改造，统一错误处理规范，提升系统错误处理能力。

## 需求场景
当前notifyserver服务的错误处理不统一，部分地方直接使用标准error，部分地方使用fmt.Sprintf格式化错误信息，缺乏统一的错误码和错误处理机制。需要按照CustomError规范进行改造。

## 架构技术方案
按照CustomError改造规范，对业务逻辑层进行改造：
1. 导入myerrors包
2. 函数返回值改为(*YourResp, *myerrors.CustomError)
3. 使用合适的错误码
4. 所有错误调用OutputLog方法
5. 检查调用链完整性

## 影响文件
- notifyserver/model/service/alert_notify_info.go
- notifyserver/model/service/consume.go  
- notifyserver/model/service/get_robot_list.go
- notifyserver/model/service/incident_notify_info.go
- notifyserver/model/service/notify_info_base.go

## 实现细节

### 1. 错误码注册
需要在pkg/util/errors/error_list.go中注册Notify模块相关错误码：
- ErrNotifyConfigParse: 通知配置解析失败
- ErrNotifyNodeLock: 节点加锁失败
- ErrNotifyNodeUpdate: 节点更新失败

### 2. alert_notify_info.go改造要点
- buildNewMessageInfo方法中的JSON解析错误
- prepareVarInfo方法中的扩展信息解析错误
- 使用ErrJSONUnmarshal错误码

### 3. consume.go改造要点  
- InitConsumeConfig方法中的配置解析错误
- deal方法中的数据库操作错误
- 使用ErrNotifyConfigParse、ErrNotifyNodeLock、ErrNotifyNodeUpdate错误码

### 4. get_robot_list.go改造要点
- InitRobotTokenConfig方法中的配置解析错误
- GetRobotTokenConfig方法中的参数校验错误
- 使用ErrNotifyConfigParse错误码

### 5. incident_notify_info.go改造要点
- buildNewMessageInfo方法中的用户信息获取错误
- 使用ErrNotifyUserNotFound错误码

### 6. notify_info_base.go改造要点
- buildTips方法中的用户信息获取错误
- buildTimeCountDownStopInfo方法中的用户信息获取错误
- initUserInfo方法中的用户信息获取错误
- 使用ErrNotifyUserNotFound错误码

## 边界条件与异常处理
- JSON解析失败时的降级处理
- 用户信息获取失败时的日志记录
- 数据库操作失败时的重试机制
- 配置解析失败时的默认值设置

## 数据流动路径
1. 配置文件 → JSON解析 → 业务逻辑
2. 用户ID → 用户服务调用 → 用户信息
3. 节点状态 → 数据库操作 → 状态更新
4. 告警数据 → 消息构建 → 通知发送

## 预期成果
- 统一的错误处理机制
- 标准化的错误码体系
- 完整的错误日志记录
- 更好的错误追踪和调试能力
- 符合CustomError规范的代码质量
```


    2. 接下来，**【Agent】**会根据确认后的需求/技术文档，产出具体可执行的任务 Tasks ，我们需要再次check**【人】**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=601e7c22dbcc490fbaf65f27fd01b64f&docGuid=1JNvSH1K3E-SfD "")
```
# NotifyWorkflowRun CustomError 改造任务计划

## 任务1：分析现有错误处理和导入包检查
- 1.1: 检查当前文件是否已导入 `myerrors` 包，如未导入则添加导入语句
- 1.2: 分析现有错误处理模式，识别需要改造的错误类型
- 1.3: 检查现有错误码使用情况，确保复用已有错误码
- 1.4: 识别所有需要修改的函数签名和返回类型

## 任务2：改造核心业务函数 - Start函数
- 2.1: 修改 Start 函数签名为返回 `*myerrors.CustomError`
- 2.2: 改造数据库查询错误处理（GetByRelationIDAndLevel调用）
- 2.3: 改造业务逻辑错误处理（ticket data nil检查等）
- 2.4: 改造事务错误处理，确保所有错误都包装为CustomError
- 2.5: 改造工作流配置查找错误处理

## 任务3：改造核心业务函数 - RunNextNode函数
- 3.1: 修改 RunNextNode 函数签名为返回 `*myerrors.CustomError`
- 3.2: 改造通知记录查询错误处理
- 3.3: 改造工作流节点获取错误处理
- 3.4: 改造接收者获取错误处理
- 3.5: 改造数据库操作错误处理（创建notify_node）

## 任务4：改造核心业务函数 - End函数
- 4.1: 修改 End 函数签名为返回 `*myerrors.CustomError`
- 4.2: 改造节点信息查询错误处理（getNodeInfoByNodeID/Relation）
- 4.3: 改造事务错误处理（更新节点和通知状态）
- 4.4: 改造用户权限校验错误处理
- 4.5: 改造卡片修改相关错误处理

## 任务5：改造辅助业务函数 - ModifyCard和BuildNewMsgAndSend
- 5.1: 修改 ModifyCard 函数签名为返回 `*myerrors.CustomError`
- 5.2: 改造 ModifyCard 中的数据库查询和消息构建错误处理
- 5.3: 修改 BuildNewMsgAndSend 函数签名为返回 `*myerrors.CustomError`
- 5.4: 改造 BuildNewMsgAndSend 中的JSON解析和RPC调用错误处理

## 任务6：改造通知发送相关函数
- 6.1: 改造 notifyToReceiver 函数中的各种通知渠道错误处理
- 6.2: 改造 notifyByInfoflow 函数中的RPC调用错误处理
- 6.3: 改造 notifyByCellPhone 函数中的电话通知错误处理
- 6.4: 改造 notifyByEmail 函数中的邮件发送错误处理
- 6.5: 改造 modifyCardToReceiver 函数中的卡片修改错误处理

## 任务7：改造数据初始化和构建函数
- 7.1: 改造 initAlert/initIncident/initVulnerablity 函数中的RPC调用错误处理
- 7.2: 改造 buildInfo/reBuildInfo 函数中的JSON解析错误处理
- 7.3: 改造 supplyOriginInfo 函数中的JSON反序列化错误处理
- 7.4: 改造各种build*ModifyInfo函数中的错误处理

## 任务8：改造工具函数和辅助方法
- 8.1: 改造 getReceiver/buildReceiversV2 函数中的用户查询错误处理
- 8.2: 改造 saveNodeExtraInfo/parseNodeExtraInfo 函数中的JSON处理错误
- 8.3: 改造 checkEndStatus/setEndStatus 函数中的Redis操作错误处理
- 8.4: 改造 findWorkflow 函数中的工作流查找错误处理

## 任务9：验证和测试
- 9.1: 编译验证确保所有修改语法正确
- 9.2: 检查函数调用链兼容性，确保上层调用正确处理新返回类型
- 9.3: 验证错误码使用正确性，确保所有错误都有合适的错误码
- 9.4: 测试主要业务流程，确保功能正常工作

## 任务10：文档更新和清理
- 10.1: 更新相关注释，说明新的错误处理机制
- 10.2: 清理不再使用的错误处理代码
- 10.3: 确保所有错误日志输出格式统一
- 10.4: 验证改造完成度，确保无遗漏的错误处理点
```
    3. 第三步，**【Agent】**按照任务规划，进行代码改造。**【人】**只需要在改造完之后，**耐心地做一下CodeReview**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=116cd29339a04928a98fa8e035375f48&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc83c852874a4118b56253bd16cda932&docGuid=1JNvSH1K3E-SfD "")


**【Agent】**改造完成后，申请执行编译任务（需要人来审核**【人】**），Agent发现问题，并自觉修复**【Agent】**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=740a07f925ad4418ac9cbf5368c264f9&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d0e2e6120b0445ad9e2ffe0028c65fcb&docGuid=1JNvSH1K3E-SfD "")
自觉修复后再次编译，编译通过**【Agent】**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3428c4491fab4b88a511819ef879ff57&docGuid=1JNvSH1K3E-SfD "")
    4. 最终，改造完成，输出总结**【Agent】**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d913a3a79b544021b3ea69de739f3d1d&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fedac6037a7140e39db747537efbfaaa&docGuid=1JNvSH1K3E-SfD "")
4. 对Agent产出的结果不太放心，进行**手动编译，编译通过****【人】**
5. 后续**发布到test环境，充分自测后方可上线****【人】**



**技巧**

* 在任务执行过程中，有两次申请编译，需要人来确认，编译非危险操作，我不想每次都要手动确认，改成自动执行即可，修改如下：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9593a061115947d1a72b7711f27b0a7a&docGuid=1JNvSH1K3E-SfD "")
* 相较于Chat Mode的自由模式，用了Spec Mode后，**Agent跑偏次数降低**，且更能**清晰把控每个关键步骤，及时纠偏**



### 结果
*  [评审：2024-3-11-2460](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/sec-llm/sec-smart-chat/reviews/119096622/files/base...latest/notifyserver/model/service/run_notify_workflow.go?t=mention&mt=doc&dt=sdk)
* 2个小时完成notifyserver模块的error改造工作 ，效率提升7倍

## 实战二：有技术挑战的代码重构场景
### 背景
LLM Server 是SOC大模型服务基座，作为SOC微服务架构中的核心底层服务，主要负责接入和管理多个大模型服务（如文心千帆、GPT、千问、DeepSeek等），屏蔽不同模型提供商的接入细节，为上层应用提供统一的大模型调用接口。

LLM Server 采用**生产者-消费者架构模式**，通过Kafka消息队列实现异步解耦。

消费者逻辑存在以下问题：

1. 消息拉取策略缺陷，容易饿死低优先级队列
2. Context使用不当，大量使用根ctx进行DB/Redis操作，缺乏超时控制，存在连接泄漏风险
3. 事务处理逻辑混乱
4. 代码冗余，可读性差、维护性差

[SOC微服务架构（集成工作流引擎）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/TV-qnpj85H/zzcTImQ1NG/vUWFWITVMrHoDo?t=mention&mt=doc&dt=doc)

### 任务
尝试使用AI-Agent-Coding，进行LLM消费者逻辑重构，以解决上述问题

### 动作
人改造的思路：先要了解这个服务架构、职责、功能、编码规范；其次梳理要解决的问题，针对问题制定技术方案；方案评审通过后，进行Coding工作

为了让AI复刻人的决策思路，做了如下动作

1. 书写一版 LLMServer的服务介绍文档（Rule）**【人】**
2. 交给大模型，让其完善此服务介绍文档

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a8a6d1dd0c124660bf0c3a1472d815f0&docGuid=1JNvSH1K3E-SfD "")
3. 针对模型完善后的服务介绍文档，删繁就简，得到完整的LLMServer服务介绍文档**【人】**
    1. 如LLMServer主要接口就是 异步提交任务/获取任务结果两个接口，其余接口都是由于历史包袱存在的无用接口
    2. 其他废话删除


```
---
description: 
globs: 
alwaysApply: false
---
# LLM Server 完整介绍文档

## 📋 概述

LLM Server 是一个基于Go语言开发的大模型服务基座，作为sec-smart-chat项目的核心组件，主要负责接入和管理多个大模型服务（如文心千帆、GPT、千问、DeepSeek等），为上层应用提供统一的大模型调用接口，屏蔽不同模型提供商的接入细节。

## 🏗️ 架构设计

### 整体架构
LLM Server 采用**生产者-消费者架构模式**，通过Kafka消息队列实现异步解耦：

```
[客户端请求] → [HTTP接口（API服务）] → [RPC接口 (LLMServer)] → [写入DB] → [任务投递到Kafka] → [消费者处理] → [大模型API] → [结果返回]  → [更新DB]
```

### 核心组件
- **RPC服务层**：提供统一的gRPC接口
- **消息队列**：Kafka实现任务异步处理
- **消费者集群**：多消费者并发处理任务
- **令牌桶限流**：控制各模型的调用频率
- **数据库层**：MySQL存储任务和结果

## 🚀 核心功能

### 1. 多模型统一接入
支持多种大模型提供商：
- **文心千帆**：ERNIE-Bot系列模型
- **OpenAI GPT**：GPT-3.5、GPT-4系列
- **阿里千问**：Qwen系列模型
- **DeepSeek**：DeepSeek-V3等模型

### 2. 异步任务处理
- **Job-Task模式**：一个Job包含多个Task，支持批量处理
- **Kafka队列**：按模型类型分队列，提高处理效率
- **并发消费**：多消费者实例，支持水平扩展

### 3. 智能限流控制
- **令牌桶算法**：为每个模型配置独立的限流策略
- **动态配置**：支持运行时调整限流参数
- **降级处理**：Redis故障时的降级策略

### 4. 结果回调机制
- **Webhook支持**：任务完成后自动回调通知
- **状态跟踪**：完整的任务生命周期管理
- **结果聚合**：多任务结果统一返回

## 📁 项目结构

```
llmserver/
├── bootstrap/              # 启动初始化
│   ├── bootstrap.go        # 主初始化逻辑
│   └── shutdown.go         # 优雅关闭
├── cmd/                    # 构建脚本
├── conf/                   # 配置文件
│   ├── app.toml           # 应用主配置
│   ├── kafka.toml         # Kafka配置
│   └── servicer/          # 服务发现配置
├── library/                # 核心库
│   ├── model/             # 模型定义
│   ├── resource/          # 资源管理
│   ├── status/            # 状态定义
│   └── types/             # 类型定义
├── model/                  # 数据层
│   ├── dao/               # 数据访问对象
│   │   ├── cache/         # Redis缓存
│   │   ├── dml/           # 数据操作
│   │   └── orm/           # ORM生成代码
│   └── service/           # 业务服务
│       ├── kafkaserver/   # Kafka消费者
│       ├── llm/           # 大模型调用
│       └── tokenbucket/   # 令牌桶限流
├── servers/                # 服务层
│   └── pbserver/          # gRPC服务
│       ├── desc/          # Protocol Buffers定义
│       └── llmserver/     # 接口实现
└── main.go                # 程序入口
```

## 🔧 核心接口

### 1. 异步任务接口(除了下面接口，其余接口逻辑都不需要关心)
```protobuf
// 提交异步任务
rpc PostLlmJobV2(PostLlmJobReqV2) returns (PostLlmJobResp);


// 获取任务结果
rpc GetLlmResult(GetLlmResultReq) returns (LlmResp);

```

## 🗄️ 数据库设计

### llm_job_info 表
存储大模型任务组信息：
```sql
CREATE TABLE `llm_job_info` (
    `id` bigint NOT NULL COMMENT '雪花ID，job_id',
    `model` varchar(64) NOT NULL DEFAULT '' COMMENT '模型',
    `business_type` int(11) NOT NULL DEFAULT '0' COMMENT '业务类型',
    `priority` int(11) NOT NULL DEFAULT '0' COMMENT '任务优先级',
    `task_count` int(11) NOT NULL DEFAULT '0' COMMENT '任务个数',
    `webhook` varchar(1024) NOT NULL DEFAULT '' COMMENT 'webhook地址',
    `job_info` text NOT NULL COMMENT '一组大模型请求任务（json）',
    `job_status` smallint NOT NULL DEFAULT '0' COMMENT '任务状态',
    `job_result` text NOT NULL COMMENT '大模型请求结果（json）',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `idx_ctime` (`ctime`)
);
```

### llm_task_info 表
存储单个任务详情：
```sql
CREATE TABLE `llm_task_info` (
    `id` bigint NOT NULL COMMENT '雪花ID，task_id',
    `job_id` bigint unsigned NOT NULL DEFAULT '0' COMMENT 'job_id',
    `task_idx` smallint unsigned NOT NULL DEFAULT '0' COMMENT '任务序列号',
    `task_info` text NOT NULL COMMENT '大模型请求任务（json）',
    `task_status` smallint NOT NULL DEFAULT '0' COMMENT '任务状态',
    `task_result` text NOT NULL COMMENT '大模型请求结果（json）',
    `model` varchar(64) NOT NULL DEFAULT '' COMMENT '模型',
    `pull_time` TIMESTAMP NOT NULL DEFAULT '1970-01-01 08:00:01' COMMENT '拉取时间',
    `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `mtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `idx_ctime` (`ctime`),
    UNIQUE KEY `idx_job_task` (`job_id`, `task_idx`)
);
```

## 🔄 任务处理流程

### 1. 任务提交流程
1. API服务调用`PostLlmJobV2`接口提交任务
2. 服务器验证参数并生成JobID
3. 将Job信息写入`llm_job_info`表
4. 将每个Task写入`llm_task_info`表
5. 根据模型类型将Task投递到对应Kafka队列

### 2. 任务消费流程
1. 消费者从Kafka队列拉取Task
2. 验证Task有效性（检查Job和Task是否存在）
3. 获取令牌桶令牌（限流控制）
4. 调用对应的大模型API
5. 更新Task状态和结果
6. 检查Job是否完成，如完成则更新Job状态
7. 如果配置了Webhook，发送回调通知

### 3. 状态管理
- **Job状态**：0-创建，1-运行中，2-全部成功，3-部分成功，4-全部失败
- **Task状态**：0-创建，1-运行中，2-成功，3-失败
```
4. 人以Rule形式书写一版任务（简单需求文档）**【人】**

```
---
description: 
globs: 
alwaysApply: false
---
## 当前问题
    - 消费者逻辑(LlmTaskConsumer)代码有些乱，主要体现在
        a. LlmTaskConsumer 代码冗余，可读性、维护性差
        b. 拉取消息有点粗暴，容易一直消费p0的任务，饿死p1 和 p2 队列
        c. 对db、redis的操作，一直用根ctx，这个ctx没有超时时间，存在连接泄露风险
        d. 事务处理逻辑混乱
## 任务
    - 请你结合这些问题，重构一下 LlmTaskConsumer方法
```
5. 结合LLMServer服务介绍文档 和 需求文档，给到Agent，让它产生更为完整的需求文档**【Agent】**，人工review修改后得到最终的需求文档**【人】**
    1. **目的：让Agent发现人未轻易发现的问题，补齐需求文档**


```
---
description: 
globs: 
alwaysApply: false
---
## 当前问题分析

基于对llmserver代码的深入分析，消费者逻辑(LlmTaskConsumer)存在以下核心问题：

### 🔴 严重问题

#### 1. 消息拉取策略缺陷 (问题b)
**问题描述**：
- 采用优先级拉取策略：p0(500ms) → p1(300ms) → p2(200ms)
- 容易导致p0队列持续消费，p1和p2队列饿死
- 缺乏负载均衡和公平调度机制

**影响**：
- 高优先级队列积压时，低优先级任务无法及时处理
- 系统整体吞吐量下降
- 任务处理延迟不均衡

#### 2. Context使用不当 (问题c)
**问题描述**：
- 大量使用根ctx进行DB/Redis操作
- 缺乏超时控制，可能导致连接泄漏
- 异步goroutine中context传递混乱

**风险**：
- 数据库连接池耗尽
- Redis连接长时间占用
- 系统资源泄漏

#### 3. 事务处理逻辑混乱 (问题d)
**问题描述**：
- 事务边界不清晰
- 部分操作在事务外，部分在事务内
- 错误处理和回滚机制不完善

**风险**：
- 数据一致性问题
- 并发冲突
- 错误恢复困难

### 🟡 设计问题

#### 4. 方法过于冗余 (问题a)
**问题描述**：
- LlmTaskConsumer方法超过200行
- 职责不单一，包含消息拉取、处理、状态更新等多重逻辑
- 代码可读性和维护性差

#### 5. 错误处理不统一
**问题描述**：
- 错误日志格式不一致
- 缺乏统一的错误分类和处理策略
- 部分错误只记录日志，不进行重试或回滚

#### 6. 并发安全问题
**问题描述**：
- 多个goroutine同时操作Redis计数器
- 缺乏原子性保证
- 可能出现计数不准确的情况

### 🟢 性能问题

#### 7. 资源利用不合理
**问题描述**：
- 同时维护3个Kafka消费者连接
- 长时间运行goroutine可能泄漏
- 数据库查询未优化

#### 8. 批处理能力缺失
**问题描述**：
- 单条消息处理，无批量优化
- 数据库操作频繁，未充分利用批处理
- 网络调用效率低下

## 🔧 重构建议

### 1. 消息拉取策略重构
```go
// 建议采用轮询+权重策略
type MessagePuller struct {
    consumers []*kafka.Consumer
    weights   []int
    current   int
}

func (mp *MessagePuller) PullMessage(ctx context.Context) (*kafka.Message, error) {
    // 实现加权轮询算法
    // 考虑队列长度、处理时间等因素
}
```

### 2. Context管理优化
```go
// 为不同操作设置合适的超时时间
func (c *Consumer) processTask(ctx context.Context, task *LlmKafkaTask) error {
    // DB操作超时
    dbCtx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()
    
    // LLM调用超时
    llmCtx, cancel := context.WithTimeout(ctx, 30*time.Second)
    defer cancel()
    
    // Redis操作超时
    redisCtx, cancel := context.WithTimeout(ctx, 2*time.Second)
    defer cancel()
}
```

### 3. 事务边界清晰化
```go
func (c *Consumer) updateTaskStatus(ctx context.Context, taskID int64, status int32, result string) error {
    return resource.MySQLClient.Transaction(func(tx *query.Query) error {
        // 所有相关操作在同一事务中
        if err := tx.LlmTaskInfo.WithContext(ctx).SetTaskStatusAndTaskResultByID(taskID, status, result); err != nil {
            return err
        }
        
        // 检查并更新Job状态
        if err := c.updateJobStatusIfNeeded(ctx, tx, taskID); err != nil {
            return err
        }
        
        return nil
    })
}
```

### 4. 方法拆分重构
```go
// 主方法只负责协调
func LlmTaskConsumer(ctx context.Context, kafkaConf kafka.ConfigMap, bucket tokenbucket.LuaTokenBucket, topics []string, idx int, model string) {
    puller := NewMessagePuller(kafkaConf, topics)
    processor := NewTaskProcessor(bucket, model)
    
    for {
        select {
        case <-ctx.Done():
            return
        default:
            msg := puller.PullMessage(ctx)
            if msg != nil {
                processor.ProcessAsync(ctx, msg)
            }
        }
    }
}

// 消息拉取器
type MessagePuller struct {
    // 拉取逻辑
}

// 任务处理器
type TaskProcessor struct {
    // 处理逻辑
}
```

### 5. 统一错误处理
```go
// 使用自定义错误类型
func (c *Consumer) handleProcessError(ctx context.Context, err error, task *LlmKafkaTask) {
    var customErr *myerrors.CustomError
    if errors.As(err, &customErr) {
        customErr.OutputLog(ctx, resource.LoggerLogic)
    } else {
        merr := myerrors.NewCustomError(myerrors.ErrTaskProcess, err.Error())
        merr.OutputLog(ctx, resource.LoggerLogic)
    }
    
    // 根据错误类型决定是否重试
    if c.shouldRetry(err) {
        c.retryTask(ctx, task)
    }
}
```

### 6. 批处理优化
```go
// 批量处理任务
func (c *Consumer) processBatch(ctx context.Context, tasks []*LlmKafkaTask) error {
    // 批量获取令牌
    if err := c.acquireTokensBatch(ctx, len(tasks)); err != nil {
        return err
    }
    
    // 并发处理
    results := make(chan TaskResult, len(tasks))
    for _, task := range tasks {
        go c.processSingleTask(ctx, task, results)
    }
    
    // 收集结果并批量更新
    return c.updateResultsBatch(ctx, results)
}
```

## 📋 重构优先级

### 🔥 P0 - 立即修复
1. **Context超时问题** - 防止资源泄漏
2. **事务边界问题** - 保证数据一致性
3. **消息拉取策略** - 解决队列饿死问题

### 🟡 P1 - 短期优化
1. **方法拆分** - 提高代码可维护性
2. **错误处理统一** - 改善监控和告警
3. **并发安全** - 防止数据竞争

### 🟢 P2 - 长期优化
1. **批处理能力** - 提升性能
2. **监控指标完善** - 运维可观测性
3. **配置动态化** - 提升灵活性

## 🎯 重构目标

1. **可靠性**：消除资源泄漏，保证数据一致性
2. **性能**：提升吞吐量，降低延迟
3. **可维护性**：代码结构清晰，职责单一
4. **可观测性**：完善监控，便于运维
5. **可扩展性**：支持新模型和新功能

```


6. 新建对话，触发代码重构任务 

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fac39ef727cb4d91b9ad192a352887f7&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac21e6ddcc7a42b38f4fbdad0fd9e7f9&docGuid=1JNvSH1K3E-SfD "")
7. Agent完成任务后，主动告知其进行编译 ：**可优化点：完成任何代码改造任务后，都要执行编译，放置在一直生效的Rule中**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e89c409d8d8d4ad69cb7b2da2ca23923&docGuid=1JNvSH1K3E-SfD "")
8. 接下来就是不断的编译、发现错误、修正错误，人可以去干别的事了

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3c0e7b8a7955481397f52e17bd0a4124&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fa4cb9a22b5f42838c2b10c008dccae4&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b13596a4b0014e9abf5fd39ae09f3405&docGuid=1JNvSH1K3E-SfD "")
后续插曲...

9. 等了10min+，发现Agent还没修完，查看错误陷入循环了中断后继续执行，还是不行
    1. 分析：上下文太长了，影响Agent思考与决策
    2. **解决方案：重开一个会话，如下**


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e068201c44c2473d8b56b23b58bc063d&docGuid=1JNvSH1K3E-SfD "")
最终完成修复，编译通过

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e0a2ef768f244fd7ad8f649359e78057&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f7900a361b664b6fa5dfa56f5225cb27&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1f61c513b9514337876226cdf46e7a82&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0973019f4977404db5cc6020afc96b2a&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=63e9f7080e6440988a7be88b702a47a3&docGuid=1JNvSH1K3E-SfD "")


### 结果
* 完成重构开发任务，人效提升：由2d的开发工作量，不到0.5d完成，人效**提升3倍**
* [代码Diff](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/sec-llm/sec-smart-chat/merge/63f117dbb98bfaf733755e8f7e951e600749e8ed...b30c8c22416c1996ec606501d62f2adf1cea5a1f/llmserver/model/service/kafkaserver/consumer.go)

## 实战三：复杂需求类
### 背景
[[AISOC-RD-monitor-13] 【BUG】【告警模块】告警列表筛选告警标签存在漏召/多召情况](https://console.cloud.baidu-int.com/devops/icafe/issue/AISOC-RD-monitor-13/show?source=drawer-header?t=mention&mt=doc&dt=sdk)

筛选时间跨度较大，存在不符合预期结果

![](https://newicafe.baidu.com/rest/v5/attachment/file/stream/25732751 "")


### 任务
优先级提到最高，火速解决问题

### 动作
1. 产生技术方案rules并触发任务执行 **【人】**

```
---
description: 告警列表标签筛选Bug fix
globs: 
alwaysApply: false
---

## 背景

### 功能描述
    告警列表页支持丰富的查询功能，包括告警来源、负责人、告警标签、关键字筛选等。

### 接口和代码链路
- 查询接口如下：https://usoc.baidu-int.com/api/soc/alert/get-alert-list?page_no=1&page_size=20&sources=&levels=%5B0%5D&tags=%5B3%2C4%2C6%5D&invert_tags=1
- 代码路径
    - 先走到http服务API模块
        - api/servers/httpserver/registers/soc.go
        ```go 
        alertRouter.HandleFunc(http.MethodGet, "/get-alert-list", alert.GetAlertList)
        ```
        - api/servers/httpserver/controller/soc/alert/getalertlist.go  GetAlertList方法
        - api/model/service/soc/alert/getalertlist.go  GetAlertList 方法

    - 再RPC请求到RPC服务SOC模块 
        - soc/servers/pbserver/soc/register.go
        ```go 
            ss.RegisterHandler(socpb.ServiceName, socpb.GetAlertListMethod, i(pbrpc.AutoHandler(s.GetAlertList)))

        ```
        - soc/servers/pbserver/soc/getalertlist.go
        ```go
            func (s *Service) GetAlertList(ctx context.Context, req pbrpc.Request) (pbrpc.Response, error) {...}
        ```
        - soc/model/service/alert/getalertlist.go
        ```go
            func GetAlertList(ctx context.Context, in *GetAlertListReq) (*LongQueryTaskInfo, int64, []int64, []*AlertList, error) { ... }
        ```
### 查询技术实现
- 基本查询都从alert的 ES Index中获取。
- 特殊逻辑：
    - 冷热存储：查询时间跨度在180天之内，走热索引查询；跨度在180天之外，走全量索引离线查询
    - 涉及到标签（tags）查询：优先从mysql tag关联表里根据tags召回告警ID列表（alert_id_list），再用作关联从ES召回
- 涉及到的存储
    - MYSQL: 
        - 告警热表：soc/model/dao/sql/soc_alert.sql; 
        - 告警全表：soc/model/dao/sql/soc_alert_all.sql； 
        - 告警标签关联表：soc/model/dao/sql/soc_alert_tag_conn.sql
    - ES:(soc/conf_online/es.toml)
        - 告警热表： alert
        - 告警全表: alert_all 
        
    - MYSQL到ES数据同步：自动由同步组件进行，黑盒形式，无需关心

### 问题：告警列表筛选告警标签存在漏召/多召情况

有两个表：告警表、告警tag关联表
  a. 优先根据筛选标签去mysql tag表中召回 alert_id_list
  b. 再组装其他查询语句 +  id in alert_id_list从 alert ES Index中召回告警数据
ES会限制传入的 alert_id_list数量 （10000个），所以 a中最多召回1万个alert_id。
  a. 如果是正向筛选标签（包含），则会出现漏召
  b. 如果是反向筛选标签（不包含），则会出现多召

### 解决方案：统一从alert Index中查询，弃用tag关联表,alert表
- alert 表增加 JSON类型的tags字段，存储tags数组，如 [1,3,5]，由于自动同步组件，所以相关联的alert index也会增加 tags字段，字段的类型大致如下
    ```json
    "tags" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
    ```
- 所有涉及到对 soc_alert_tag_conn表数据的增删改逻辑，都改为对alert.tags字段的变更
- 涉及到标签的查询逻辑，也都改为对alert.tags的查询
- 另外针对存量的soc_alert_tag_conn 数据，也要写一个方法迁移过来
---
description: 告警列表标签筛选Bug fix
globs: 
alwaysApply: false
---

## 背景

### 功能描述
    告警列表页支持丰富的查询功能，包括告警来源、负责人、告警标签、关键字筛选等。

### 接口和代码链路
- 查询接口如下：https://usoc.baidu-int.com/api/soc/alert/get-alert-list?page_no=1&page_size=20&sources=&levels=%5B0%5D&tags=%5B3%2C4%2C6%5D&invert_tags=1
- 代码路径
    - 先走到http服务API模块
        - api/servers/httpserver/registers/soc.go
        ```go 
        alertRouter.HandleFunc(http.MethodGet, "/get-alert-list", alert.GetAlertList)
        ```
        - api/servers/httpserver/controller/soc/alert/getalertlist.go  GetAlertList方法
        - api/model/service/soc/alert/getalertlist.go  GetAlertList 方法

    - 再RPC请求到RPC服务SOC模块 
        - soc/servers/pbserver/soc/register.go
        ```go 
            ss.RegisterHandler(socpb.ServiceName, socpb.GetAlertListMethod, i(pbrpc.AutoHandler(s.GetAlertList)))

        ```
        - soc/servers/pbserver/soc/getalertlist.go
        ```go
            func (s *Service) GetAlertList(ctx context.Context, req pbrpc.Request) (pbrpc.Response, error) {...}
        ```
        - soc/model/service/alert/getalertlist.go
        ```go
            func GetAlertList(ctx context.Context, in *GetAlertListReq) (*LongQueryTaskInfo, int64, []int64, []*AlertList, error) { ... }
        ```
### 查询技术实现
- 基本查询都从alert的 ES Index中获取。
- 特殊逻辑：
    - 冷热存储：查询时间跨度在180天之内，走热索引查询；跨度在180天之外，走全量索引离线查询
    - 涉及到标签（tags）查询：优先从mysql tag关联表里根据tags召回告警ID列表（alert_id_list），再用作关联从ES召回
- 涉及到的存储
    - MYSQL: 
        - 告警热表：soc/model/dao/sql/soc_alert.sql; 
        - 告警全表：soc/model/dao/sql/soc_alert_all.sql； 
        - 告警标签关联表：soc/model/dao/sql/soc_alert_tag_conn.sql
    - ES:(soc/conf_online/es.toml)
        - 告警热表： alert
        - 告警全表: alert_all 
        
    - MYSQL到ES数据同步：自动由同步组件进行，黑盒形式，无需关心

### 问题：告警列表筛选告警标签存在漏召/多召情况

有两个表：告警表、告警tag关联表
  a. 优先根据筛选标签去mysql tag表中召回 alert_id_list
  b. 再组装其他查询语句 +  id in alert_id_list从 alert ES Index中召回告警数据
ES会限制传入的 alert_id_list数量 （10000个），所以 a中最多召回1万个alert_id。
  a. 如果是正向筛选标签（包含），则会出现漏召
  b. 如果是反向筛选标签（不包含），则会出现多召

### 解决方案：统一从alert Index中查询，弃用tag关联表,alert表
- alert 表增加 JSON类型的tags字段，存储tags数组，如 [1,3,5]，由于自动同步组件，所以相关联的alert index也会增加 tags字段，字段的类型大致如下
    ```json
    "tags" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
    ```
- 所有涉及到对 soc_alert_tag_conn表数据的增删改逻辑，都改为对alert.tags字段的变更
- 涉及到标签的查询逻辑，也都改为对alert.tags的查询
- 另外针对存量的soc_alert_tag_conn 数据，也要写一个方法迁移过来
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f38ddc6141cc4d1da44c0f9d1cfae916&docGuid=1JNvSH1K3E-SfD "")
2. Agent生成详细技术方案文档，进行适当调整**【人】**

```
# 告警列表标签筛选Bug修复需求文档

## 需求背景

### 问题描述
告警列表页支持丰富的查询功能，包括告警来源、负责人、告警标签、关键字筛选等。当前标签筛选存在漏召/多召情况：

1. **正向筛选标签（包含）**：会出现漏召
2. **反向筛选标签（不包含）**：会出现多召

### 问题根因
当前实现使用两个表：告警表、告警tag关联表
- 优先根据筛选标签去mysql tag表中召回 alert_id_list
- 再组装其他查询语句 + id in alert_id_list从 alert ES Index中召回告警数据
- ES会限制传入的 alert_id_list数量（10000个），所以最多召回1万个alert_id

## 解决方案

### 核心思路
统一从alert Index中查询，弃用tag关联表，改为使用alert表的tags字段。

### 技术方案

#### 1. 数据库结构变更
- alert 表增加 JSON类型的tags字段，存储tags数组，如 [1,3,5]
- 由于自动同步组件，相关联的alert index也会增加 tags字段
- ES字段类型：
```json
"tags" : {
  "type" : "text",
  "fields" : {
    "keyword" : {
      "type" : "keyword",
      "ignore_above" : 256
    }
  }
}
```

#### 2. 业务逻辑变更
- 所有涉及到对 soc_alert_tag_conn表数据的增删改逻辑，都改为对alert.tags字段的变更
- 涉及到标签的查询逻辑，也都改为对alert.tags的查询
- 针对存量的soc_alert_tag_conn 数据，写迁移方法

## 影响文件分析

### 需要修改的核心文件

#### 1. 查询逻辑文件
- `soc/model/service/alert/getalertlist.go` - 主要查询逻辑
- `soc/model/service/alert/get_alert_list_es.go` - ES查询逻辑

#### 2. 标签管理文件
- `soc/model/service/alert/update_alerts_tag.go` - 标签更新逻辑
- `soc/model/service/alert/getalerttags.go` - 标签获取逻辑
- `soc/model/service/alert/tag.go` - 标签工具函数

#### 3. 数据库文件
- `soc/model/dao/sql/soc_alert.sql` - 热表结构
- `soc/model/dao/sql/soc_alert_all.sql` - 全量表结构

#### 4. ORM层文件
- `soc/model/dao/orm/soc_alert.go` - 告警ORM模型
- `soc/model/dao/orm/soc_alert_all.go` - 全量告警ORM模型
- `soc/model/dao/query/soc_alert.go` - 告警查询方法
- `soc/model/dao/query/soc_alert_all.go` - 全量告警查询方法

### 接口层文件（无需修改）
- `api/servers/httpserver/controller/soc/alert/getalertlist.go` - HTTP接口层
- `api/model/service/soc/alert/getalertlist.go` - RPC调用层
- `soc/servers/pbserver/soc/getalertlist.go` - RPC接口层

## 实现细节

### 1. 数据库字段添加
在soc_alert和soc_alert_all表中添加tags字段：
```sql
ALTER TABLE soc_alert ADD COLUMN tags JSON COMMENT '告警标签数组';
ALTER TABLE soc_alert_all ADD COLUMN tags JSON COMMENT '告警标签数组';
```
数据表定义修改完后，到 `soc/model/dao` 下，执行go run main.go 生成gen.go相关代码
### 2. ES查询逻辑改造
- 移除`getAlertIDListByTag`函数中对soc_alert_tag_conn表的查询
- 改为直接在ES查询中使用tags字段进行terms查询
- 支持正向和反向筛选

### 3. 标签更新逻辑改造
- 更新标签时直接修改alert.tags字段
- 移除对soc_alert_tag_conn表的操作
- 保持相似告警的标签同步逻辑

### 4. 数据迁移脚本
- 编写迁移脚本，将soc_alert_tag_conn中的存量数据迁移到alert.tags字段
- 支持增量迁移和全量迁移

## 边界条件与异常处理

### 1. 数据一致性
- 确保迁移过程中数据不丢失
- 处理迁移过程中的并发问题
- 支持回滚机制

### 2. 性能考虑
- ES查询性能优化
- 大数据量迁移的性能问题
- 避免影响线上服务

### 3. 兼容性
- 确保新旧逻辑平滑切换
- 支持灰度发布
- 向后兼容现有API

## 预期成果

1. **修复Bug**：彻底解决标签筛选的漏召/多召问题
2. **性能提升**：减少数据库查询次数，提升查询效率
3. **架构简化**：简化数据模型，减少表关联复杂度
4. **维护性**：降低系统复杂度，便于后续维护

## 风险评估

### 高风险项
- 数据迁移过程中的数据一致性
- 线上服务的稳定性影响

### 中风险项
- ES字段映射变更
- 大量存量数据的迁移性能

### 低风险项
- 代码逻辑变更
- 单元测试覆盖

## 测试策略

### 1. 单元测试
- 标签查询逻辑测试
- 标签更新逻辑测试
- 边界条件测试

### 2. 集成测试
- 端到端功能测试
- 性能压力测试
- 数据一致性测试

### 3. 灰度测试
- 小流量验证
- 监控指标观察
- 回滚预案验证
```
3. Agent生成任务计划**【Agent】**

```
# 告警列表标签筛选Bug修复任务规划

## 阶段1：数据库结构变更和代码生成

- [x] 任务1：修改数据库表结构，添加tags字段
    - 1.1: 在soc_alert.sql中添加tags JSON字段
    - 1.2: 在soc_alert_all.sql中添加tags JSON字段
    - 1.3: 执行go run main.go生成ORM代码

- [x] 任务2：验证ORM代码生成
    - 2.1: 检查生成的soc_alert.go中的Tags字段
    - 2.2: 检查生成的soc_alert_all.go中的Tags字段
    - 2.3: 检查生成的query文件中的相关方法

## 阶段2：数据迁移脚本开发

- [x] 任务3：开发数据迁移脚本
    - 3.1: 创建迁移脚本文件migrate_tags.go
    - 3.2: 实现从soc_alert_tag_conn表读取数据逻辑
    - 3.3: 实现数据转换和写入alert.tags字段逻辑
    - 3.4: 添加批量处理和错误处理机制

## 阶段3：查询逻辑改造

- [x] 任务5：改造ES查询逻辑
    - 5.1: 修改get_alert_list_es.go中的getAlertListByES函数
    - 5.2: 移除对soc_alert_tag_conn表的查询依赖
    - 5.3: 实现基于alert.tags字段的ES查询
    - 5.4: 支持正向和反向标签筛选

- [x] 任务6：改造全量查询逻辑
    - 6.1: 修改getAlertAllIDsByES函数
    - 6.2: 统一热表和全量表的查询逻辑
    - 6.3: 移除getAlertIDListByTagFromES函数

## 阶段4：标签管理逻辑改造

- [x] 任务7：改造标签更新逻辑
    - 7.1: 修改update_alerts_tag.go中的UpdateAlertsTags函数
    - 7.2: 移除对soc_alert_tag_conn表的操作
    - 7.3: 实现直接更新alert.tags字段逻辑
    - 7.4: 保持相似告警标签同步机制

- [x] 任务8：改造标签获取逻辑
    - 8.1: 修改getalerttags.go中的GetAlertTags函数
    - 8.2: 从alert.tags字段读取标签信息
    - 8.3: 移除对soc_alert_tag_conn表的依赖

- [x] 任务9：改造辅助函数
    - 9.1: 修改getalertlist.go中的GetTagsByAlertIDs函数
    - 9.2: 移除对soc_alert_tag_conn表的查询
    - 9.3: 从alert.tags字段解析标签信息

## 阶段5：测试和验证

- [ ] 任务10：单元测试
    - 10.1: 编写标签查询逻辑单元测试
    - 10.2: 编写标签更新逻辑单元测试
    - 10.3: 编写边界条件测试用例

## 阶段6：清理和优化

- [ ] 任务13：代码清理
    - 13.1: 移除不再使用的soc_alert_tag_conn相关代码
    - 13.2: 清理导入的未使用包
    - 13.3: 代码注释和文档更新

- [ ] 任务14：性能优化
    - 14.1: ES查询性能优化
    - 14.2: 数据库查询优化
    - 14.3: 内存使用优化
```
4. Agent执行任务**【Agent】**
5. 人进行代码review、改造**【人】**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f55dc8e5212a4d46beafe9cf8562b9bb&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=39086fa454f34e759ee77718ac119b8e&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=febc875720a1447c956c9d60e6480dee&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=44851ed8ba3042ebb5d5accd099fd17c&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fad209d005494b62845cab3bbc168232&docGuid=1JNvSH1K3E-SfD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=05e8655ffb644187b7938a351fc710cb&docGuid=1JNvSH1K3E-SfD "")
6. 人对其他地方的标签逻辑进行改造**【人】**
7. 心理路程：让AI全包（50%工作）->我指导，AI干（20%工作）->算了，剩下的我来干吧（30%工作）



### 结果
* AI完成简单功能、人做复杂功能的完成下，成功完成需求提测；**Agent贡献代码60%，人贡献代码40%**
* [代码DIFF](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/sec-llm/sec-smart-chat/merge/63f117dbb98bfaf733755e8f7e951e600749e8ed...335e9d7b6eb6a88e0148b886c29e5e8a933e4d5b/soc/model/service/alert/getalerttags.go)
* AI能够把简单的逻辑开发完成，复杂度高的逻辑仍需人去主导实现，AI在面对**复杂度高**的需求时，任重道远，需要将其拆解成多个子任务

# 总结
1. 对于Agent
    1. Agent在 **繁琐重复的任务 **和 **有技术挑战的任务（在较小的领域范围内） **上均有所建树，面对**复杂度高**的需求时，任重道远
    2. 上下文窗口是有限的，rules不要太繁琐、规则不要冗余（我们项目仍需精简优化规则）

2. 对于人
    1. 敢于尝试，避免浅尝辄止
        1. 先从繁琐但简单的需求开始
        2. 执行更复杂需求时，可以进行拆解，分而治之
        3. 当在一个复杂的上下文背景下，发现他糊涂了，果断让它**进行总结，新开会话**，重新执行一个新的任务

    2. 保持耐心
        1. 介绍项目背景、编码规范、服务架构等
        2. 出了错误也要耐心辅导

    3. 有责任心
        1. 要对Agent产生的代码负责，**严格Review**他的技术方案、代码



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
