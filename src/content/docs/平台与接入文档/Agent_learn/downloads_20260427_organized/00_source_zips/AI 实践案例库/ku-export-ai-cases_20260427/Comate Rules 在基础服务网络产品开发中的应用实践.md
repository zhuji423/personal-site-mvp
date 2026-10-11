---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "Comate Rules 在基础服务网络产品开发中的应用实践"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Comate Rules 在基础服务网络产品开发中的应用实践.md"
---
Comate Rules 在基础服务网络产品开发中的应用实践

#### 🧑‍🏫 案例作者：[@孙兴博](https://ku.baidu-int.com?t=mention&mt=contact&id=70a20050-fce9-11f0-a652-7374b50bbb3c)
#### 🎬 案例场景：运维
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了Comate Rules在基础服务网络产品开发中的应用，通过灵活配置Rules，解决了重复性开发任务的效率与规范问题。结合MCP工具与Zulu平台，实现了知识库的即时调用与高效开发。应用后，接口与数据处理器开发效率显著提升，开发时间大幅缩短，同时保证了代码质量与风格一致性，为项目开发提效探索了新路径。
## 0. 背景介绍
项目开发中，框架搭建、接口与应用架构搭建、数据库模型生成等重复性繁琐工作，往往占用大量时间且易产生不规范问题。随着 AI Coding 技术日趋成熟，如何借助 AI 提升开发效率、实现项目开发的规范化与高效化，已成为团队关注的核心议题。



基础服务平台项目中，不仅对开发规范性要求极高，还需快速完成基础模块搭建以聚焦核心故障定位逻辑的研发。而 Comate Rules 具备灵活的规则配置能力，可精准适配标准化开发场景，恰好能解决这类重复性工作的效率与规范痛点。为此，我们在故障定位这个子项目开发中尝试引入 Comate Rules，专门攻克重复性、标准化开发任务，为项目提效探索新路径。



另外常规 AI 开发多依赖人机对话模式，AI 需先理解用户需求再完成开发，但这种方式对 Prompt 的精准度要求极高。实际场景中，复杂需求往往难以通过单一 Prompt 完整、准确传递，而我们的核心诉求是让 AI 严格按照既定设计落地开发。为此，我们可借助知识库提前沉淀完整设计成果，在 Comate Zulu 平台中通过 MCP 工具直接调取知识库内容，让 Zulu 全面掌握所有需求细节。后续与人机交互时，我们仅需提供设计文档，即可让 Zulu 按规范高效完成开发工作。





## Comate 配置与交互
### 1.1. 配置 Rules 
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0d0d9ca8700249e38eae07ccd2115d04&docGuid=Mr-eyTNav9MqN2 "")


按需编写项目的 Rules，在本次实践中，使用[故障定位项目 Rules](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/Mr-eyTNav9MqN2?block_id=docyg-3bc87270-c516-11f0-9e9f-33df471cd304) 作为整个项目的 Rules。



### 1.2. 配置 MCP 工具
在 Comate MCP 市场中安装知识库开放接口 MCP 工具并设置 AK/SK，主要用于我们的设计文档内容的获取，作为需求提供给 Zulu。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ee9ec6b7a7d438d9408e7a2319bf1b2&docGuid=P-oE35-gJeJucB "")
当然也可以扩展更多其他 MCP 工具获取私有化数据等等。



### 1.3. 开发过程中与 Zulu 的交互过程
与 Zulu 的整体交互过程十分简单：

[流程图]




## 应用场景
我们所涉后端项目，开发核心主要分为接口开发与数据处理器开发两大模块。其中，接口按实际使用场景划分为控制台接口、内部接口及开放接口三类；异步数据处理流程、数据同步等特定业务逻辑，则被封装为一个个独立的数据处理器。本次 Comate Rules 的应用实践，正是聚焦于这两类核心模块的开发过程。



这里为整个项目定义了一个大而全的 Rules，详细的说明了项目架构与规范要求。



```
---
description: 
globs: 
alwaysApply: true
---
## 项目概述

这是一个用于网络故障定位的微服务项目，提供了一系列用于处理网络故障定位/巡检/系统日志操作的API接口及数据处理器。


## 项目架构

项目采用模块化设计，主要分为以下几个核心部分：

1. **配置文件** (`src/location/config/*`)
   - 存储项目依赖的配置数据
   - 通过`src/location/internal/pkg/config/`下的全局变量读取并使用（在项目启动时完成配置加载）

2. **应用** (`src/location/internal/apps/*`)
   - `src/location/internal/apps/apis`: API接口应用
      - `src/location/internal/apps/apis/console/*`: 控制台接口（`apis`每一个目录对应一个API，`middleware`为中间件，`routes`为接口路由注册组件，`services`为各接口的通用处理逻辑）
      - `src/location/internal/apps/apis/open/*`: 开放接口（`apis`每一个目录对应一个API，`middleware`为中间件，`routes`为接口路由注册组件，`services`为各接口的通用处理逻辑）
      - `src/location/internal/apps/apis/mcp/*`: MCP接口
   - 其他目录每一个代表一个处理器应用（cron、daemon、command）

3. **依赖组件** (`src/location/internal/pkg/*`)
   - `src/location/internal/pkg/components/client/*`: 每个目录代表一个第三方API请求客户端
   - `src/location/internal/pkg/components/snowflake`: 雪花算法服务，项目中主要用于生成资源的唯一标识
   - `src/location/internal/pkg/components/config`: 配置组件，用于加载、更新配置内容
   - `src/location/internal/pkg/components/constants/*`: 常量定义
   - `src/location/internal/pkg/components/di`: 依赖注入组件，用于MySQL、Redis、RabbitMQ等等服务实例的获取
   - `src/location/internal/pkg/models/*`: 数据模型定义；每一个目录代表一个DB实例的模型数据；queue目录为消息队列模型实例；


## 代码结构说明

### 1. 配置文件

配置文件为TOML格式，分为：
   - `components`: 组件类，如数据库、Redis的服务链接配置等
   - `datamap`: 数据字典类，如错误码信息映射等
   - `params`: 其他参数类，如第三方服务客户端配置、Redis的键名配置、RabbitMQ的队列名配置等
每一分类的目录内每一个文件代表一个细分的配置项分类

### 2. API

每一大类API目录内的每一个子目录代表一个具体的API功能，具体包括：
    - `api.go`: API路由、中间件等定义
    - `data.go`: API的请求/响应数据定义，以及请求数据的校验规则定义
    - `form.go`: 请求数据的绑定操作封装
    - `query.go`: 数据查询操作的封装
    - `saver.go`: 数据存储操作的封装
    - `service.go`: 具体业务逻辑

### 3. 处理器

每个处理器目录下可能包含
    - `data/*`: 数据结构定义
    - `processors/*`: 具体处理器实例
    - `services/*`: 处理器执行的业务逻辑流
    - `utils/*`: 处理器依赖的通用工具
    - `app.go`: 处理器的入口定义
    - `executor.go`: 处理器的

### 4. 数据模型

数据模型目录下每一个子目录对应了一个`di`中的数据库实例，子目录中的每一个文件代表一个数据表的ORM定义，其中需要定义：
    - 数据结构
    - 实现TableName方法
    - 实现新建实例函数
具体可以`src/location/internal/pkg/models/probe/probe_main.go`为参考

### 5. 依赖组件实例

`di`注入了所有服务依赖的组件（MySQL、Redis等）；在业务代码的实现中只要考虑具体的实例用法即可，例如：
    - 启动数据库事务: `_ = di.DB().Transaction(func(tx *gorm.DB) error {/*业务逻辑...*/return nil})`；数据库实例可能有多个，例如`di.DBCMDB()` `di.DBMetric()`
    - 操作Redis: `di.Redis().HGetAll(context.Background(), "key").Result()`
    - 操作RabbitMQ: 可参考`src/location/internal/apps/apis/console/apis/probe/launch/service.go`中`sendToMQ`方法的实现方式


## 开发指南

### 1. 基本开发流程

1. 如需新增接口，需在对应的接口分类目录下创建子目录，并创建对应的go代码文件
2. 如需新增处理器，需在应用目录内创建对应的子目录及其下级结构，根据处理器类型参考其他相似的处理器实现来生成相关源码文件

### 2. 扩展开发指南（基本示例）

1. **添加新的控制台接口**
   - 在 `src/location/internal/apps/apis/console/apis`目录下创建新目录，例如一个主机列表查询接口，这里命名为`host_list`
   - 在 `src/location/internal/apps/apis/console/apis/host_list`目录下创建`api.go` `data.go` `form.go` `service.go` 等文件
   - 实现业务逻辑，格式参考其他同类接口
   - 在 `src/location/internal/apps/apis/console/apis/routes/register.go`中注册本次新增加的接口路由（在providers方法中新增一行对应新增的接口）

2. **添加新的处理器**
   - 在 `src/location/internal/apps` 目录下创建应用代码目录
   - 定义 `data`、`processors`、`services`等目录及源代码文件，定义`app.go`、`executor.go`应用入口文件 
   - 实现操应用业务逻辑
   - 在 `src/location/internal/apps/bootstrap.go` 中注册应用

## 代码风格指南

1. **类型定义**
   - 对于每个函数、结构、字段都需要增加简洁易懂的注释
   - 对于接口实现，代码结构及代码风格严格参考`src/location/internal/apps/apis/console/apis/probe/launch/*`
   - 对于处理器实现，代码结构及代码风格严格参考`src/location/internal/apps/probe/*`
   - 如果需要新增模型定义，严格参考`src/location/internal/pkg/models/location/probe/probe_main.go`的实现形式

2. **错误处理**
   - 统一使用`icode.baidu.com/baidu/bs-platform/common-go/apperror`处理错误
   - 在异步操作中正确处理错误传播

3. **命名规范**
   - 使用驼峰命名法
   - 专有名词全大写
   - 方法/函数名清晰表达其用途

## 注意事项

1. 所有的异步操作都应该正确处理错误情况
2. 注意内存泄漏，特别是在处理事件监听器时
3. 在实现新功能时，确保与现有的接口保持一致
4. 保持代码的可测试性，避免副作用
5. 文档注释要清晰完整，包含参数说明和使用示例

```


### 2.1. 接口开发
在我们的项目代码中，一个具体接口定义为一个目录实体，其中包括：

* `api.go`：声明请求请求路径、请求方法、注册中间件等
* `data.go`：声明请求/响应数据结构
* `form.go`：声明请求数据的绑定与验证方式
* `query.go`：这个接口中是数据查询模块，其他的接口中也可能是其他操作
* `service.go`：核心业务逻辑，完成处理并组装响应数据



另外在实现完成以上代码后，需要将接口路由添加到`routes/register.go`路由容器中。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f9ad18874ab0490489552b4c78730b9e&docGuid=Mr-eyTNav9MqN2 "")


下面我们就以[查询拨测点](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/41FsefhkDo/w-e7jN9XXGjx9Z)这个开放接口为例，看一下使用 Comate Rules 前后的开发效率的体感对比。



#### 2.1.1. 传统开发方式
在不使用 AI 时，我们开发一个接口大致的过程为：

[流程图]


在传统流程中，对于一个简单的接口来说，完成整个开发过程可能也需要大概一个小时的时间。



#### 2.1.2. 使用 Comate Rules 
使用 Zulu 时的开发过程大致简化为：

[流程图]


大概 5 分钟左右即大致实现完成了一个接口的整体逻辑，我们可以根据生成情况微调代码，或者调整 Rules 矫正预期效果，开发效率得到了极大提升。



[附件]


### 2.2. 数据处理器开发
与接口类似，一个数据处理器基本包括：

* data 目录：可能包含诸多数据结构声明
* processors 目录：处理器实体，可以理解为控制层
* services 目录：定义业务逻辑
* utils 目录：工具函数
* `executor.go`：执行器，负责整个处理器的逻辑调度
* `app.go`：处理器的定义与注册实体



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a8b858a250b241b8a5dd52e04faead73&docGuid=Mr-eyTNav9MqN2 "")


以一个简单的[处理器程序](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/6231Y5uehZ/RrtdyXeXBaZUcL)为例，看一下使用 Comate Rules 前后的开发效率的体感对比。



#### 2.2.1. 传统开发方式
在不使用 AI 时，我们处理器大致的过程为：

[流程图]


过程中可能还涉及到配置文件的调整，整体开发流程较长，耗时较久。



#### 2.2.1. 使用 Comate Rules 
[流程图]


与接口开发一样进化为三步即可完成，由于处理器的项目规范比接口负责，所以整体生成速度要比接口慢一些，这里就不放置录屏视频了，整体交互流程也与接口开发是一致的。 Zulu 能够按照项目规范准确的生成应用框架，并按设计文档完成数据结构定义和业务逻辑实现，并且能准确的修改相关文件，例如处理器应用注入到`bootstrap.go`、在配置文件中增加队列名配置等，以及为我们生成当前不存在的数据库模型定义（但是这个我们并不需要，数据库模型的生成在 [2.3](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/Mr-eyTNav9MqN2?block_id=docyg-de264771-c50e-11f0-9e9f-33df471cd304) 节有更标准化的实现）。

我们可以按需调整或重新生成代码：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fc230f7d3c8f457ab7483b04ef6ed798&docGuid=Mr-eyTNav9MqN2 "")


### 2.3. 数据库模型代码生成
另一个比较繁琐的工作就是数据库模型的创建与调整，以往数据表的设计都是维护在代码仓库中的，需要人工对照这设计完成代码模型的转换，比较耗时也。有了 Comate Rules 后，我们就可以像代码开发一样，将设计维护在知识库文档中，这里以[会话模型](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/6231Y5uehZ/uljkfljuEB0-GV)为例，初步编写了一个简单的 Rules 为模型代码的生成指定参考，并说明文档中数据表的结构定义。



```
---
description: 
globs: 
alwaysApply: true
---

## 背景
项目中的 M与SQL 数据表定义在知识库文档的表格中。在开发中，我们需要将其转换为项目代码中针对与 gorm 的模型代码定义。


## 知识库文档表结构
表格固定具有 8 列数据，分别为：
1. 行序号
2. 字段释义
3. 字段名
4. 类型
5. 长度
6. 是否允许为 NULL
7. 默认值
8. 备注


## 模型代码生成
- 严格参考`src/location/internal/pkg/models/probe/probe_main.go`的范式将文档内容转换为 Golang 模型代码
```


直接将文档提供给 Zulu：

[附件]


可以看到第一次生成的模型代码的实例化函数不符合预期（可能是由于 Rules 写的比较简单），经过我们对话提醒后，Zulu 能够准确的参考规范更正不符合预期的代码，整个过程大概不到 3 分钟，十分高效。





## 引入 AI Coding 后的工作重心转移
引入 AI Coding 前，团队的研发精力主要分散在系统设计与代码实现两大核心环节。由于需同时兼顾设计构思与具体编码落地，精力被大幅分摊，难以做到两头兼顾。实际开发中，部分需求的细节往往不会完整体现在设计文档中，而是依赖开发人员在编码过程中凭经验灵活把控。这种模式不仅导致设计逻辑缺乏完整留痕，形成 “隐性知识” 沉淀不足的问题，还会给团队新人理解项目架构、核心逻辑带来阻碍，同时在项目交接时因信息不完整产生较高的沟通成本与上手门槛。



引入 AI Coding 后，代码实现环节可基本交由 AI 高效完成，这一转变让团队得以将绝大部分精力聚焦于系统设计本身。我们能够投入更多时间打磨设计方案，尽可能完善、细化设计文档的每一个细节 —— 既明确核心业务逻辑、接口定义、数据流转规则，也补充异常场景处理、兼容性要求等关键信息。这样一来，一方面能为 AI 提供精准、全面的开发依据，引导其输出更贴合需求的规范代码；另一方面也为团队沉淀了体系化、可复用的系统知识库，让项目核心逻辑、设计思路实现显性化留存，不仅降低了新人上手与项目交接的成本，也为后续项目迭代、扩展奠定了坚实基础。





## 总结
Comate Zulu 结合 Rules 方案的落地，极大简化了故障定位项目的整体开发流程，为接口与数据处理器开发带来了显著改变。对于接口开发（涵盖控制台接口、内部接口、开放接口）而言，从接口定义、参数校验、返回格式标准化到基础逻辑搭建，这些重复性强、规则固定的工作均能由 AI 高效完成；而数据处理器开发中，数据接收、格式转换、异步任务调度、日志打印等标准化模块，也无需人工重复编码。



前文所提及的仅为单个接口或处理器的开发示例，在实际研发场景中，一次业务需求往往涉及更庞大的开发量 —— 可能包含十几个甚至几十个接口的设计与实现，再搭配若干个独立数据处理器以支撑异步流程、数据同步等核心逻辑。尤其是面对这类工作量密集的需求时，AI 替代人工完成重复性标准化工作的优势更为突出：不仅大幅减少了手动编码的时间成本，还规避了人工操作可能出现的格式不统一、参数遗漏等问题，让开发效率的提升变得直观可感，团队得以更快推进需求落地。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
