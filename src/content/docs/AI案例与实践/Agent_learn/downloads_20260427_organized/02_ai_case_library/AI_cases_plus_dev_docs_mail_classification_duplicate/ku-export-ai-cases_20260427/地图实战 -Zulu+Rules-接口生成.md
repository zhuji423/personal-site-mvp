---
title: "一、rules是什么"
description: "地图实战 -Zulu+Rules-接口生成"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\地图实战 -Zulu+Rules-接口生成.md"
---
地图实战 -Zulu+Rules-接口生成

#### 🧑‍🏫 案例作者：[@陈鑫玉](https://ku.baidu-int.com?t=mention&mt=contact&id=0fb42560-fce5-11f0-8c3d-c928e2e4d24f)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了在地图打车业务中，如何利用AI和爱速搭平台实现前端页面代码的一键生成。通过AI工具自动生成代码，提高了开发效率，减少了人工编写代码的工作量。文章详细描述了实现过程、技术路径及最佳实践，展示了AI在前端开发领域的巨大潜力。
# 一、rules是什么
## 1.1解决什么问题
目的：对抗LLM的核心局限，缺乏交互间的持久记忆（大模型对话窗口的上下文不会共享）

这个局限会导致的问题：

* 失忆导致输出不一致
* 需要反复重申指令
* 上下文不足时，AI助手会表现出幻觉

AI幻觉可能导致的问题：

* 推荐与项目技术栈不符的库
* 生产违反既定架构约定的代码

## 1.2rules做了什么
将项目的上下文稳定进行持久化，每次AI在生成代码时，都会将rule带到prompt中，让开发者集中精力在当前任务逻辑上，而不是每次都重新解释基础设定

带来的好处

* 提供AI回答的准确性和相关性
* 保证代码风格和架构的一致性
* 极大提升编码效率

# 二、在comate中的rule的使用
## 2.1触发入口
在comate页面点击这个点点点图表，在点击Rules菜单，进入rules管理面板

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.2管理面板
在管理面板能够对当前项目的中的rules进行管理，有新建、修改、删除能力

![](/personal-site-mvp/img/doc-placeholder.svg "")
也可以直接在当前代码库中以查看文件的方式进行管理，目录为:当前项目根路径/.comate/rules/

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.3命名Rules
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.4选择生效范围
![](/personal-site-mvp/img/doc-placeholder.svg "")
|生效范围|解释|对应配置|
|-|-|-|
|手动使用|需要手动使用#提及才能生效|description: globs: alwaysApply: false|
|指定文件生效|指定对应的文件才会生效，可以支持模糊匹配来限制文件类型|description: globs: *.goalwaysApply: false|
|始终生效|会自动对所以生产的代码生效|description: globs: alwaysApply: true|

## 2.5编写rules
### 2.5.1手动编写
可以按照写prompt的方式编写rules，rules文件的内容通常覆盖以下场景

* 业务领域知识
* 架构与模块
* 模块详情
* 配置管理
* 外部依赖
* 构建与开发命令
* 开发模式
* 开发环境搭建
* 编码规范
* 约束
* 特定开发流程

### 2.5.2通过LLM辅助生成rule
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
对话框输入 "/" 后选择规则生成标签，可以让LLM来辅助生成rule

## 
# 三、最佳实践
## 3.1简单接口代码生成
目标：一次对话让AI生成一个简单的查询数据库接口

### 3.1.1 rules
这里展示gomis服务当前的rules结构做为参考



├── base # 基本规则（全局）

│   ├── 01-project-structure.mdr # 项目结构和架构

│   └── 02-framework-initialization.mdr # DP2框架基础、应用初始化和项目结构指南

├── biz # 业务规则（局部）

│   ├── 01-business-logic.mdr # 业务逻辑模式

│   ├── 02-domain-models.mdr # 领域模型结构

│   └── 03-data-layer-architecture.mdr # 数据层架构

├── develop # 开发规则（指定）

│   └── api.mdr # API开发规范

├── framework # 框架规则（局部）

│   ├── 01-gdp2-basics.mdr # GDP2框架基础

│   ├── 02-gorm-database.mdr # GORM数据库操作

│   ├── 03-http-api.mdr # HTTP API模式

│   ├── 04-dao-generation.mdr # DAO代码生成

│   ├── 05-application-initialization.mdr # 应用初始化

│   └── 06-cronjob-implementation.mdr # 定时任务实现

├── language # 语言规则（局部）

│   ├── 01-go-standards.mdr # Go编码标准

│   ├── 02-logging.mdr # 日志记录规范

│   ├── 03-test.mdr # 单元测试规范

│   ├── 04-review.mdr # 代码审查标准

│   └── 05-error-handling.mdr # 错误处理规范

└── library # 库规则（局部）

    ├── 01-utils-usage.mdr # 工具包使用

    ├── 02-constant-definition.mdr # 常量定义

    ├── 03-resource-management.mdr # 资源管理

    └── 04-types-definition.mdr # 类型定义



### 3.1.2生成接口
先指定api开发专用rules，再写prompt



prompt如下，给出接口文档地址，并给出接口逻辑，让AI完成代码之后进行测试

```
你是一个GO语言开发大师，现在需要根据接口文档开发一个接口
iapi接口文档： https://iapi.baidu-int.com/web/project/364583/apis/api-4786264
接口逻辑：根据条件分页查询talos_activity_card表的数据
表结构：表结构在script/sql/activity/talos_activity_card.sql
测试数据：id=5,card_type=2,status=1,creater=chenxinyu10,page=1,per_page=10
需要完成工作：完成接口开发、启动服务、使用测试数据验证接口是否可用
```


### 3.1.3rules编写总结
rules生成流程

1. 使用AI辅助生成rules，直接让AI读取一个模块代码，基于现有代码逻辑生成rules
2. 对生成的rules进行修剪，ai生成的rules不一定符合实际应用规范，一般需要人工修剪一下
3. 持续对rules进行维护，rules并不是生成一次之后就不用修改的，在项目持续迭代的过程中，也需要对rules进行迭代



rules编辑最大的挑战

如何平衡rules数量和上下文大小，rules太多会导致上下文超长AI罢工，rules太少会导致规范描述不清晰AI自由发挥

将rules分为三个部分：

|rules类型|描述规则|生效范围|
|-|-|-|
|需求rules|这个需求的代码链路，相当于预估rules路由，说明这个需求大概要用到那些局部rules功能|指定生效|
|全局rules|所有代码都需要遵守的规则|全局生效|
|局部rules|功能模块的rules，列如：日志rules，数据库rules|特定目录生效|

通过需求rules将局部rules串起来，既能精简rules又能规范AI编码



## 3.2php代码迁移探索
目前团队存在大量的php代码需要迁移到go上，人工手动进行迁移工作量非常大，使用AI来辅助迁移可以大幅提升迁移效率

### 3.2.1操作流程
[流程图]
AI生成代码图谱prompt

```
你是一个PHP语言开发大师，现在需要梳理接口代码逻辑
marketing/actions/sale/Detail.php 生成这个文件的代码图谱
1.列出controller、service、dao层逻辑
2.列出request和response字段
```
生成迁移代码prompt 的 prompt

```
根据代码图谱，生成一个把代码迁移到gomarketing 服务中的prompt
1.读取gomarketing服务的rule，在gomarketing/.comate/rule中
2.使用下面的prompt为模板
```
# PHP 转 Go 接口迁移规则

## 任务目标
将 PHP 接口 `marketing/actions/sale/Detail.php` 迁移至 Go 项目 `gomarketing` 中，接口地址为 `gomarketing/api/activity/goods/sale/detail`。

## 核心规则

### 1. 规则遵循
- 严格遵守 `.comate` 基础规则和 PHP 转 Go 规则
- 遵循 `gomarketing` 项目的目录结构和编码规范

### 2. 关键规范
- **规则索引**： 使用规则索引 gomarketing/.comate/rules/RULES_INDEX.md。对应的模块选择对应的规则
- **数据转换**: 使用 `library/utils/conv` 包，禁止直接使用 `strconv`
- **错误处理**: 错误变量用单数形式（`ErrorXXX`），使用 `library/errno` 包
- **HTTP API**: 遵循 `gomarketing/.comate/rules/framework/03-http-api.mdr` 规范
- **PHP转GO 规范**:遵循`.comate/rules/transfer`
- **复用原则**:优先复用已经存在的代码

### 3. 兼容性要求
- 保持业务逻辑、参数校验、异常处理与原 PHP 一致
- 错误码和返回格式完全兼容

## 目录结构与文件路径
### 关键文件路径
- **请求类型**: `library/types/request/goods/sale_detail.go`
- **响应类型**: `library/types/response/goods/sale_detail.go`
- **业务逻辑**: `model/service/goods/sale_detail.go`
- **控制器**: `httpserver/controller/activity/goods/sale_detail.go`
- **路由**: `httpserver/routers/activity.go`
- **数据库访问**: `model/dao/db/ycunion/goods/goodsorder/goods_order_info.go`

## 输出要求
1. 完整的代码实现（包含所有层级）
2. Service 层的单元测试（特别是 `GetSaleDetail` 方法）
3. 规则适配说明（简要说明如何遵循项目规范）
4. 不用生成单侧，直接用go run main.go 启动服务进行验证
```

```


# 四、其他rules相关学习资源
rules社区

[https://console.cloud.baidu-int.com/aitools/rules](https://console.cloud.baidu-int.com/aitools/rules)

###### **Rules实践落地相关学习资源：**
* Rules占比报表说明：[Rules占比报表使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/G7oz65Tuh-/lsXqa6fmsFwg8F?t=mention&mt=doc&dt=doc)
* Rules社区与自动生成工具说明：[Rules管理&社区使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/iw_M6wfv-D3CHw?t=mention&mt=doc&dt=doc)
* 学习资源：
    * **课程：**[AI Coding项目 上下文规则（Rules）](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56520?isFromPc=1?t=mention&mt=doc&dt=sdk)
    * **课程：**[Coding Agent With Rules](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56651?isFromPc=1?t=mention&mt=doc&dt=sdk)
    * **实践：**[内化AI能力实战：用Rules玩转电商场景研发提效](http://learn.baidu.com/review.html?reviewId=19154?t=mention&mt=doc&dt=sdk)
    * **实践：**[网盘Server Coding Agent 将需求转换成工程化交付的代码 ​](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56518?activityId=8747?t=mention&mt=doc&dt=sdk)
    * **实践：**[Comate国际化Rule设定](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/RN8tHqy0od/zVNNKcBqJrxLNJ?t=mention&mt=doc&dt=doc)
    * **实践：**[【ACG系统部】光传输控制器结合Zulu编码案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/G7oz65Tuh-/cAV7nuPs-J2lS9?t=mention&mt=doc&dt=doc)
    * **实践：**[AI-Coding rule分享](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/h6hJSY6ZpD/j06pVdjlL6HA7Z?t=mention&mt=doc&dt=doc)
    * **实践：**[全局顶层规约rule](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/mcV1ZM02Cz/-Ir1pBr-FMBpsG?t=mention&mt=doc&dt=doc)

* 申请工作坊：可以联系yanzhijie01、hemu01，或者提报到支持里[TSC执行网络CodingAgent落地场景与计划](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/G7oz65Tuh-/3523ba923d8841?t=mention&mt=doc&dt=sheet)
    * 以往工作坊：[网盘AI Coding实战工坊](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/zf7rq2G1GdJCwf?t=mention&mt=doc&dt=doc)[文库AI Coding实战工坊](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/uj0WupU7whVZ7F?t=mention&mt=doc&dt=doc)[商业&输入法&国际化实战工作坊](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/CRn6rpelFzX6il?t=mention&mt=doc&dt=doc)


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
