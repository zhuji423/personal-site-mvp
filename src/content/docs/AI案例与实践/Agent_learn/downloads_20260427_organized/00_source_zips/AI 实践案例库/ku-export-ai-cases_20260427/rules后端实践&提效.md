---
title: "数据库访问规范"
description: "rules后端实践&提效"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\rules后端实践&提效.md"
---
rules后端实践&提效

#### 🧑‍🏫 案例作者：[@杨志强](https://ku.baidu-int.com?t=mention&mt=contact&id=1d938160-fce2-11f0-853d-c78d9d89ed7f)[@赵艳东](https://ku.baidu-int.com?t=mention&mt=contact&id=1fa6d100-fce2-11f0-853d-c78d9d89ed7f)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文总结了通过rules提升后端研发效率的实践。通过制定基础rules，如数据库访问规范和HTTP控制器开发规范，促进团队研发风格统一。利用rules联动iapi MCP开发，实现一键全项目注释，便于新人接入。同时，针对历史代码下线进行通知处理。rules的应用不仅沉淀了团队核心资产，还有效约束AI行为，减少模型幻觉偏差，提高研发效率。
## **一、目标：**
每个RD的研发风格不同，通过rules促进已有GDP规范，项目组研发规范落地，促进风格统一。

最终目的：**沉淀可重复使用的rules，提升研发效率。**

## 二、生成基础rules
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5b736b2c88b54763b3040590c207a0af&docGuid=l7CgWuftXAHfsO "")
生成基础的配置rules

数据层规则：

```
---
globs: model/dao/**,library/resource/*.go
description: 数据库访问规范
---

# 数据库访问规范

## 数据库连接管理
- 数据库连接统一在 [library/resource/gorm.go](mdr:library/resource/gorm.go) 管理
- 每个业务域有独立的数据库连接
- CP业务使用 [resource.Gorm().CpBiz](mdr:model/dao/cpbiz/db.go)
- WK业务使用 [resource.Gorm().WKBiz](mdr:model/dao/wkbiz/db.go)

## DAO层规范
- 每个子包必须有 `db.go` 文件提供数据库连接
- 实体文件命名: `[entity_name].go`
- 测试文件命名: `[entity_name]_test.go`
- 使用 gormadapter.GormDB 类型

## 事务管理
- 事务处理需考虑事务边界和异常处理
- 遵循数据库操作的最佳实践
```
controller层规则：

```
---
globs: httpserver/controller/**/*.go
description: HTTP控制器开发规范
---

# HTTP控制器开发规范

## 控制器架构模式
- 控制器文件组织在功能模块下：[/httpserver/controller/](mdr:httpserver/controller/)
- 使用 `ghttp.HandlerFunc` 作为处理器类型
- 采用 MService 服务调用模式

## 通用封装模式
- 必须使用 [util.NewMSLogPushFrame](mdr:library/util/util.go) 封装处理器
- 使用 [msserver.NewMSHTTPJSONExecutorNewer](mdr:model/mservice/scpbiz/) 进行 JSON 处理
- 每个控制器方法委托给对应的 MService 层

## 代码示例
```go
// 标准控制器模式
return util.NewMSLogPushFrame(
    msserver.NewMSHTTPJSONExecutorNewer(
        func(ctx context.Context, req RequestType) (*ResponseType, error) {
            return service.Method(ctx, req)
        },
    ),
)
```
```
## 三、指导rules不断自我完善所有rules文件
以单测的rules为例：

```
---
description: 
globs: 
alwaysApply: false
---
# 单元测试规范

## 文件命名

- 测试文件与被测文件同名，后缀加`_test`

- 测试文件与被测文件同目录

## 包命名

- 测试使用被测文件相同的包名（非`_test`后缀）

## 测试结构

1. **测试函数命名**：
```go
func TestType_Method(t *testing.T)  // 测试类型方法
func TestFunction(t *testing.T)     // 测试独立函数
```
```
```
---
description: 
globs: 
alwaysApply: false
---
# 单元测试规范

## 文件命名

- 测试文件与被测文件同名，后缀加`_test`

- 测试文件与被测文件同目录

## 包命名

- 测试使用被测文件相同的包名（非`_test`后缀）

## 测试结构

1. **测试函数命名**：
```go
func TestType_Method(t *testing.T)  // 测试类型方法
func TestFunction(t *testing.T)     // 测试独立函数
```

## 测试依赖
- 必须使用`github.com/agiledragon/gomonkey/v2`进行mock
- 必须使用项目日志组件`resource.LoggerService()`
- 必须使用项目错误处理`wkerror`

## 测试用例设计
1. **基本结构**：
```go
func TestFunction(t *testing.T) {
    ctx := context.Background()
    ctx = logit.WithContext(ctx)
    patch := gomonkey.NewPatches()
    defer patch.Reset()

    testCases := []struct {
        name        string
        param       InputType
        mockfunc    func()
        expectErr   bool
    }{
        // 测试用例
    }

    for _, tc := range testCases {
        t.Run(tc.name, func(t *testing.T) {
            tc.mockfunc()
            // 调用被测函数并验证
        })
    }
}

## Mock规范
1. **RAL调用mock**：
```go
patch.ApplyFunc(ral.RAL, func(ctx context.Context, name interface{}, req ral.Request, resp ral.Response, opts ...ral.ROption) error {
    // 模拟成功或失败
})
```

2. **日志mock**：
```go
patch.ApplyFunc(resource.LoggerService, func() logit.Logger {
    return logit.NewSimple(os.Stderr)
})
```
## 四、使用rules联动 iapi MCP开发
#### comate添加iapi的MCP；
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=531039aafee54a2a80669397e49c39c9&docGuid=l7CgWuftXAHfsO "")
1. 配置iapi的MCP的用户名及token，用户名即百度邮箱前缀，iapi_token 根据iapi配置

![图1](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=28075eaf53a84caa806fd5ead2d6589e&docGuid=L801Vrle9oiWIh "图1")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=af85388fae7d4f6794f19d55ac61535f&docGuid=l7CgWuftXAHfsO "")


IAPI：[https://iapi.baidu-int.com/web/project/362812/apis/api-4764198](https://iapi.baidu-int.com/web/project/362812/apis/api-4764198)

ZULU：[https://console.cloud.baidu-int.com/comatestack/share/3305](https://console.cloud.baidu-int.com/comatestack/share/3305)

## 五、新人查看代码  全注释rules
一键全项目注释，新人接入0阻塞

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f804992f9044c34b5413040db2518c8&docGuid=uU6kzPti3W26Eq "")
## 六、历史代码下线
无用代码下线，通知下线处理操作

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e709ba56d87b419789a372d6a7667616&docGuid=uU6kzPti3W26Eq "")
## 七、总结
#### 一、Rules 的核心优势
1、沉淀团队核心资产：将代码库中的研发范式、知识固化下来，过去，团队积累的研发经验只能依赖文档传递，吸收效率低；而借助rules，实现高效共享与即时落地。无需在每个任务中从零分析，直接基于既有经验输出结果。

2、rules 能有效约束AI行为，减少模型幻觉偏差，提升在实际工作中的可用性。

#### 二、以上需要完成的rules才能实现（需投入一定时间打磨）
1、建立完整运营流程：使用 Rules 并非简单编写规则文件，更需要一套流程发挥最大价值，生成基础rule只是一个开始，后续需要不断的完善，优化，完善后才能发挥作用，工欲行其事 必先利其器。

2、研发众多，大家都共同书写rules，文件会很多很多，rules的标准有待完善。



|代码库|语言|负责人|需求|备注||
|-|-|-|-|-|-|
|baidu/wenku-go/gcustomer|go|杨志强|1、生成代码规范规则2、生成项目规则3、MCP接入|[https://console.cloud.baidu-int.com/comatestack/share/3305](https://console.cloud.baidu-int.com/comatestack/share/3305)各种MCP的完善，能推动rules更好的应用||
|baidu/wenku-go/doc|go|赵艳东|生成单测|[https://console.cloud.baidu-int.com/comatestack/share/3312](https://console.cloud.baidu-int.com/comatestack/share/3312)[https://console.cloud.baidu-int.com/comatestack/share/3318](https://console.cloud.baidu-int.com/comatestack/share/3318)总结以往单测文件，生成单测文件规则根据新的rules规则，为新接口生成单测文件生成过程中会根据生成的结果多次与模型进行沟通，进行调试||
|baidu/wenku/nd-tfwap-aigc-client|vue|申浩玉|options api升级composition api|[https://console.cloud.baidu-int.com/comatestack/share/3308?token=906d918a](https://console.cloud.baidu-int.com/comatestack/share/3308?token=906d918a)针对某一个指定文件进行升级修改把特定的地方改成业务特定的方式生成规则应用到别的文件，发现问题，再修改，更新规则||
|baidu/wenku-go/canvas-to-b|go|李连胜|查看文件内容并且分析其功能|[https://console.cloud.baidu-int.com/comatestack/share/3319](https://console.cloud.baidu-int.com/comatestack/share/3319)有些时候需要快速对陌生的文件或者函数阅读，利用AI可以大大节省时间||
|baidu/wenku/ppt-editor-canvas|vue|陈琦|替换指定内容|评审：[wk-web-55166 ](https://console.cloud.baidu-int.com/devops/icode/myreview/changes/c/baidu/wenku/ppt-editor-canvas/+/118837295)判断有指定内容的文件根据替换规则，替换为新的内容替换后，检查内容要过是否正确||
|baidu/wenku/ioswenku|iOS|于传峰|查找端能力|先在plist配置文件中查找再通过方法名查找输出action名字，参数，方法逻辑描述及功能概要||

badcase

|||问题描述|
|-|-|-|
|工具类|Comate for Xcode|无法创建规则官网下载的3.2.1版本无法创建规则|
|||会话无法分享会话分享后在zulu会话广场看不到，我的作品中也没有|
|会话||返回内容和要求不匹配根据描述查找对应方法，返回的内容非预期，让其重新查找后还是返回同样的结果|

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
