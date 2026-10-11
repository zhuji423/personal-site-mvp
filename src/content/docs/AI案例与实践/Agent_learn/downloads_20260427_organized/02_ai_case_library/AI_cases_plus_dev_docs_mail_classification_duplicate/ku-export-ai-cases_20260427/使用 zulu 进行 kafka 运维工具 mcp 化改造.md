---
title: "背景"
description: "使用 zulu 进行 kafka 运维工具 mcp 化改造"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\使用 zulu 进行 kafka 运维工具 mcp 化改造.md"
---
使用 zulu 进行 kafka 运维工具 mcp 化改造

#### 🧑‍🏫 案例作者：[@刘桐仁](https://ku.baidu-int.com?t=mention&mt=contact&id=92d8dd20-fced-11f0-8ced-db2849cb58ff)
#### 🎬 案例场景：运维
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了使用zulu工具对Kafka运维工具进行MCP化改造的过程，通过拆分开发流程为多个步骤，利用AI辅助编码，逐步实现工具的MCP化。改造后的工具支持自然语言查询集群信息，提升运维效率。同时，总结了开发过程中的经验教训，包括知识添加备注、重命名对话历史标题等改进建议。
# 背景
## 工具 MCP 化的动机
在 2022 年接手 Kafka 集群的运维工作时，基于遇到的一些问题，造了一个 CLI（命令行界面）工具。关于这款工具的具体细节，可以参考[kafka 运维](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/SCIE54A-T7/yntf5y5LN9/F13pekA9RS89XB#anchor-07a45db0-a934-11ee-b4df-1b8da7ef8c4e?t=mention&mt=doc&dt=doc)文档中的`pandora-kafka-cli`部分，下面举几个典型场景：

1. **快速定位实例**：通过指定Broker ID，快速获取与之对应的 Pandora 实例信息，从而能够直接使用 Pandora API 对这些实例执行所需操作。
2. **监控集群健康**：获取集群中所有存在不同步副本的 Topic 列表，这一功能对于评估集群压力状况及定位问题 Broker 很有帮助。

然而，传统的 CLI 工具需要记忆很多执行参数 ，且必须在终端环境中运行，这无疑增加了使用门槛。随着大模型技术的发展，我们如今可以借助其 function call 的能力，以口语化的方式调用工具，同时，统一的 MCP 协议为工具接口提供了标准化的定义，极大地简化了调用流程。将这款 Kafka 运维工具进行 MCP 化改造，不仅能够实现通过自然语言查询集群信息的便捷性，还为开发专用的智能 Agent 提供了基础，这些 Agent 能够自动化地分析集群状态，进一步提升运维效率和智能化水平。

## 使用 ai 来辅助改造的原因
1. 人工编码需要先去学习 MCP 协议以及 sdk 的使用，然后需要梳理存量工具的业务逻辑（22 年写的代码，已经忘的差不多了），比较费时间
2. 之前没有使用 ai 辅助编码整个项目的经验，想以这个小项目为契机熟悉整个流程，且项目产出可以直接在日常运维工作中使用
3. 值周的时候，因为经常有人来处理问题，编码思路老是被打断。而 ai 辅助编程时，只需要将实现思路发给 ai ，后续均由 ai 完成，ai 编码期间可以来处理值周问题
4. ~~参加搜索研发 AICoding 赛~~

# 开发流程设计
由于 MCP 是今年新出现的概念，官方的 Golang SDK 发布的时间更晚，所以大模型对其基本没有知识储备，所以我将开发流程拆分为了以下几步：

1. 由于 zulu 使用的模型（不清楚背景具体的模型信息）没有 mcp 的知识，先下载 [Golang SDK](https://github.com/modelcontextprotocol/go-sdk) 让它来学习，并输出文档
2. 基于它输出的文档，让 zulu 写一个简单的 mcp server demo 。这个 server 没有复杂的业务逻辑，主要用来验证 sdk 的功能
3. 让 zulu 梳理 kafka 运维工具的代码，并输出文档
4. 让 zulu 基于输出的文档以及原始代码，对工具的各个功能进行 MCP 化改造

为了避免上下文爆炸和提升精度，当前基于上述四个大步骤共拆分了 13 个指令：

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 效果验证
均符合预期

## broker 
|场景|prompt|执行效果|
|-|-|-|
|获取集群指定 brokerid 对应 pandora 实例信息|列出 kafka build 集群 brokerid 为 10 的详细信息|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|根据 ip 查询指定集群 broker 信息|查询  kafka hbe 集群 ip  xxxx/xxxx/xxxx ... 对应的 broker 信息|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|分析集群中无 broker 的 pandora 实例信息|kafka trace 集群预期有 20 个实例，查询没有 brokerid 的 pandora 实例信息|![](/personal-site-mvp/img/doc-placeholder.svg "")|

## topic
|场景|prompt|执行效果|
|-|-|-|
|分析集群指定 topic 的 partition 的信息|查询  kafka hbe 集群 topic xxxxxxx 的 26 号副本的状态|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|分析集群 topic 分片丢主的问题|确认 kafka trace 集群中存在丢主的 topic 分片的信息，并按照 brokerid 进行归类|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|分析集群 topic 分片副本的问题|查询 kafka njjs 集群中存在未同步的 topic 分片的信息，对于存在未同步数据的 brokerid，统计其未同步分片的数量|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|



# prompt 及代码变更
注：前四步的变跟忘记 commit 了

cr: [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/base...latest/.gitignore?t=mention&mt=doc&dt=sdk)

## step 1 学习 golang mcp sdk
[https://console.cloud.baidu-int.com/comatestack/share/2580?token=3f4c3fce](https://console.cloud.baidu-int.com/comatestack/share/2580?token=3f4c3fce)

```
# 背景

我们需要为使用 Golang 开发一个 MCP server ，首要的目标是学习如何使用 github.com/modelcontextprotocol/go-sdk 来进行开发

# 需求

1. 这个 sdk 已经下载到本地目录 mcp-go-sdk-main/ 中了 ，你需要通过这个 sdk 了解什么是 mcp 以及如何使用这个 sdk 的 api 来开发 mcp server
2. 将你学习到的内容输出到 mcp-go-sdk-learning/doc/ 目录下的文件中，可以拆分多个文件，内容需要精炼，因为这个文档后续会被使用来进行代码开发的参考
```
|生成文档目录截图|部分文档内容截图|zulu 部分执行记录|
|-|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|

## step 2 使用 sdk 编写 mcp server demo
[https://console.cloud.baidu-int.com/comatestack/share/2581?token=2dc42c24](https://console.cloud.baidu-int.com/comatestack/share/2581?token=2dc42c24)

```
# 背景

我们需要为使用 Golang 开发一个 MCP server，需要使用官方的 golang sdk github.com/modelcontextprotocol/go-sdk 来进行开发

# 需求

1. 对于这个 sdk 的使用细节，已经在目录 mcp-go-sdk-learning/doc 中的各个文件里进行了总结，你需要先学习这些文件
2. 在 mcp-go-sdk-learning/ 目录下初始化 golang module 环境，并根据你在 step1 中所学的知识，编写一个简易的 mcp server ，代码写在 mcp-go-sdk-learning/demo-server 中，这个服务的要求如下：
    - 可以列出 server 部署环境下指定目录中的文件列表
    - 根据给出的文件路径，生成 ftp 下载链接，样例为 wget ftp://work:work@yq01-build-rd2.yq01.baidu.com/home/work/nohup.out ，其中 yq01-build-rd2.yq01.baidu.com 为 mcp server 部署的机器 host 名称，/home/work/nohup.out 为输入的文件路径
3. 对于 step2 中 server 的关键功能，请编写对应的单元测试进行验证
```
|生成的文件|文件样例|
|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|

但是发现存在问题，zulu 来回改了好几轮都没改对。我发现是它 step1 中生成的文档中没有相关接口的信息。让 zulu 重新学习 sdk ，然后改正错误

## step 3 重新学习 sdk 然后修正错误
[https://console.cloud.baidu-int.com/comatestack/share/2582?token=8870f3db](https://console.cloud.baidu-int.com/comatestack/share/2582?token=8870f3db)

```
# 背景

我们需要为使用 Golang 开发一个 MCP server，需要使用官方的 golang sdk github.com/modelcontextprotocol/go-sdk 来进行开发

# 需求

目前已经在目录 mcp-go-sdk-learning/demo-server 下完成了样例的编码，存在编译报错的问题：
go build .
# demo-server
./main.go:31:17: undefined: mcp.UnmarshalParams
./main.go:63:17: undefined: mcp.UnmarshalParams

你需要结合着报错信息，重新学习目录 mcp-go-sdk-main/ 下的 sdk ，更新 mcp-go-sdk-learning/doc 下的文档，然后对编译报错的问题进行修正
```
|zulu 部分输出|
|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|

此时编译不报错了，但是发现它的 server 实现为 stdin ，我们需要启动一个远程服务，不过也是我的需求没说清楚，打回重写

## step 4 mcp server 支持远程连接及问题排查
### step 4.1 初版代码实现
[https://console.cloud.baidu-int.com/comatestack/share/2583?token=50b78972](https://console.cloud.baidu-int.com/comatestack/share/2583?token=50b78972)

```
# 背景

我们需要为使用 Golang 开发一个 MCP server，需要使用官方的 golang sdk github.com/modelcontextprotocol/go-sdk 来进行开发

# 需求

目前已经在目录 mcp-go-sdk-learning/demo-server 下完成了样例的编码，但是其中使用的 stdin 模式，这个不符合我的需求。我希望这个 mcp server 可以给远程的 mcp client 访问，你需要对 demo-server 进行重构：

1. 重新学习目录 mcp-go-sdk-main/ 下的 sdk ，了解如何编写供远程 client 访问的 mcp server，并更新 mcp-go-sdk-learning/doc 下的文档
2. 重构 demo-server ，使得其支持 stdin 和 server 两种模式，通过命令行参数控制使用的 server 类型
```
|zulu 部分输出|执行报错|
|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|

前几个变更对应的 cr 为 v1 ：[评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/base...1/.gitignore?t=mention&mt=doc&dt=sdk)

![](/personal-site-mvp/img/doc-placeholder.svg "")
### step 4.2 执行报错问题修复
```
执行时报错：panic: AddTool "list-files": missing input schema

goroutine 1 [running]:
github.com/modelcontextprotocol/go-sdk/mcp.(*Server).AddTool(0xc0001e7830?, 0x7af320?, 0xc00019ad01?)
        /home/disk1/nizhenyang/env/go/golib/pkg/mod/github.com/modelcontextprotocol/go-sdk@v0.3.1/mcp/server.go:167 +0x235
main.registerTools(0xc0001be180)
        /home/disk7/nizhenyang/dev/baidu_aladdin_kafka/baidu/aladdin/kafka/tool/mcp-go-sdk-learning/demo-server/main.go:46 +0x5f
main.main()
        /home/disk7/nizhenyang/dev/baidu_aladdin_kafka/baidu/aladdin/kafka/tool/mcp-go-sdk-learning/demo-server/main.go:32 +0x145



重新学习目录 mcp-go-sdk-main/ 下的 sdk 来解决这个问题，完成错误修复后，更新 mcp-go-sdk-learning/doc 下的文档
```
|zulu 部分输出|server 可以正常启动|cherry studio 也可以连上|
|-|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|

但是无工具可用，需要继续排查问题：

![](/personal-site-mvp/img/doc-placeholder.svg "")
### step 4.3 mcp server 无工具可用排查
[https://console.cloud.baidu-int.com/comatestack/share/2584?token=34b24d92](https://console.cloud.baidu-int.com/comatestack/share/2584?token=34b24d92)

```
在使用远程 client 访问时，发现它无法找到可以使用的工具，请结合 sdk 源码进行排查，确认是 server 端实现存在问题，还是远程 client 有问题。如果是前者，对代码进行修复并更新文档，如果是后者，请给出本地验证的手段
```
后续又进行了多轮排查，但是 zulu 依旧查不出结果，由于内容较多，这里就不详细列出了，最后代码对应为 v6 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/1...6/.gitignore?t=mention&mt=doc&dt=sdk)。需要人工介入处理。

### step 4.4 人工介入排查
zulu 在初始化 server 的时候，配置了 `KeepAlive`参数：

![](/personal-site-mvp/img/doc-placeholder.svg "")
根据源码中的定义，它是用来保活的，也即如果每次 ping 超过了这个时间，server 就主动断开了连接

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
那么问题来了，这里的类型是 time.Durtaion 类型，值为 30 ，也即 30 纳秒 .... 这明显有问题。给 zulu 一点提示，让他自己做修改吧

```
这里执行的还是存在问题。不要通过调整测试脚本来解决这个问题。重点关注  mcp.NewServer 初始化时的 mcp.ServerOptions 里的 KeepAlive 参数的定义和类型，通过修改这个值来解决这个问题
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
这次改对了：

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
至此 demo server 生成完毕，对应 v7 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/6...7/tool/mcp-go-sdk-learning/demo-server/main.go?t=mention&mt=doc&dt=sdk)

## step 5 分析 kafka cli 工具
### step 5.1 梳理业务逻辑
[https://console.cloud.baidu-int.com/comatestack/share/2585?token=91c6f2a4](https://console.cloud.baidu-int.com/comatestack/share/2585?token=91c6f2a4)

```
# 背景

我们将一个 golang 编写的 kafka 运维工具进行重构 ，需要明确这个运维工具的业务逻辑

# 需求

kafka 运维工具所在的目录为 pandora-kafka-tool/ , 你需要全面分析其中的代码和文档，分析其业务逻辑，并整理为文档输出至  pandora-kafka-tool/doc 下 , 文档中需要注明相关业务逻辑和代码文件的映射关系
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
对应 v8 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/7...8/tool/pandora-kafka-tool/doc/design.md?t=mention&mt=doc&dt=sdk)

### step 5.2 生成改造计划
[https://console.cloud.baidu-int.com/comatestack/share/2586?token=fe861011](https://console.cloud.baidu-int.com/comatestack/share/2586?token=fe861011)

```
# 背景

我们将一个 golang 编写的 kafka 运维工具进行重构，将其改造为 mcp server 供外部调用

# 需求

1. 仔细阅读目录 mcp-go-sdk-learning/doc/ 下的 mcp sdk 文档和目录 mcp-go-sdk-learning/demo-server 下的 demo server 样例 ，了解 mcp server 的开发流程
2. 仔细阅读目录 pandora-kafka-tool/doc/ 下的 kafka 运维工具文档，了解需要改造工具的业务逻辑。如果有不明确的地方，可以阅读 pandora-kafka-tool/ 中的 golang 代码进行进一步确认。
3. 制定具体的改造计划，主要包含如下内容，结合实际需求补充其它的项目
    - 将运维工具的哪个功能重构为 mcp server 的哪个工具，工具的描述和出参分别是什么
    - server 启动时需要哪些配置信息
4. 将改造计划输出至 mcp-kafka/doc 目录下，可以拆分为多个文件
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
对应 v9 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/8...9/tool/mcp-kafka/doc/README.md?t=mention&mt=doc&dt=sdk)

## step 6 kafka cli 工具 mcp 化改造
### step 6.1 第一轮编码
[https://console.cloud.baidu-int.com/comatestack/share/2587?token=32622996](https://console.cloud.baidu-int.com/comatestack/share/2587?token=32622996)

```
# 背景

我们将一个 golang 编写的 kafka 运维工具进行重构，将其改造为 mcp server 供外部调用

# 需求

1. 仔细阅读目录 mcp-kafka/doc/ 下的改造文档，了解改造的具体需求
2. 仔细阅读目录 mcp-go-sdk-learning/doc/ 下的 mcp sdk 文档和目录 mcp-go-sdk-learning/demo-server 下的 demo server 样例 ，了解 mcp server 的开发流程
3. 在目录 mcp-kafka/ 下使用 go module 进行初始化
3. 根据改造文档的内容，将 pandora-kafka-tool/ 中 kafka 运维工具相关的业务逻辑改造为 mcp server

# 代码实现要求

1. 各个业务逻辑需要封装为独立的函数，和 mcp server 的架构逻辑解耦，这边便于未来新业务逻辑的新增
2. 各个业务逻辑需要编写单元测试验证其正确性
3. mcp server 的返回值需要尽量地精简，冗余的信息需要输出至日志中
4. 对于 mcp server 收到的请求内容及响应，需要将其输出至日志文件中，便于后期进行问题排查
```
在处理依赖及编译阶段，陷入了死循环。这里终止了任务，由人工介入来处理

![](/personal-site-mvp/img/doc-placeholder.svg "")
代码对应 v10 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/9...10/tool/mcp-kafka/README.md?t=mention&mt=doc&dt=sdk)

### step 6.2 人工调整编译依赖问题
[https://console.cloud.baidu-int.com/comatestack/share/2589?token=f59c7ee8](https://console.cloud.baidu-int.com/comatestack/share/2589?token=f59c7ee8)

代码对应 v11 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/10...11/tool/mcp-kafka/go.mod?t=mention&mt=doc&dt=sdk)

### step 6.3 其它编译问题修复
[https://console.cloud.baidu-int.com/comatestack/share/2590?token=82d7ff82](https://console.cloud.baidu-int.com/comatestack/share/2590?token=82d7ff82)

[https://console.cloud.baidu-int.com/comatestack/share/2592?token=15f1f4ba](https://console.cloud.baidu-int.com/comatestack/share/2592?token=15f1f4ba)

第一、二次。部分问题涉及 sdk ，无法自主修改

```
在编译目录 mcp-kafka/ 下的  go module 项目时存在一些报错，请根据编译报错信息来进行结果
```
第三次

```
在编译目录 mcp-kafka/ 下的  go module 项目时存在一些报错，请根据编译报错信息来进行结果。和 mcp 相关的报错，请参考 mcp-go-sdk-learning/doc 下的文档、mcp-go-sdk-learning/demo 下的样例程序以及 mcp sdk 的源码 mcp-go-sdk-main
```
第三次修复中，由于 `mcp-kafka-server/zk`和 `github.com/go-zookeeper/zk`的包名重复，导致其中一个 undefine 的问题一直无法修正，人工介入进行了处理。

![](/personal-site-mvp/img/doc-placeholder.svg "")
最终代码对应对应 v12 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/11...12/tool/mcp-kafka/config/config.go?t=mention&mt=doc&dt=sdk)

启动与工具注册看着没问题

![](/personal-site-mvp/img/doc-placeholder.svg "")
但是调用的时候出现问题

![](/personal-site-mvp/img/doc-placeholder.svg "")
### step 6.4 执行报错问题排查
此时正好我有时间了，就人工来对问题进行了排查：

发现 zulu 在迁移代码的时候修改了 Children 和 Get 的代码逻辑，修改为了使用异步模式，但是未等待返回，导致无法获取到 zk 上注册的 kafka 信息。根因是因为 step 6.3 中 zulu 在导 zk 包的时候出现错误，官方的 zk 包和模块 zk 包重名了。

![](/personal-site-mvp/img/doc-placeholder.svg "")
并且对于部分数据结构的 struct 定义，抄原来的代码也抄不对

![](/personal-site-mvp/img/doc-placeholder.svg "")
修正的代码为 v13 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/12...13/tool/mcp-kafka/zk/conn.go?t=mention&mt=doc&dt=sdk)

### step 6.5 mcp server 响应数据格式修正
[https://console.cloud.baidu-int.com/comatestack/share/2593?token=21c9d943](https://console.cloud.baidu-int.com/comatestack/share/2593?token=21c9d943)

mcp 返回的数据需要为 object ，不能为 array，让 zulu 进行调整

![](/personal-site-mvp/img/doc-placeholder.svg "")
```
# 背景
当前已经将目录 pandora-kafka-tool/ 下的 kafka 运维工具改造为了初版的 mcp server ，存放在目录 mcp-kafka/ 中，但是存在数据格式的问题，需要你来进行修正

# 需求

1. 阅读目录 mcp-go-sdk-learning/doc 下的 mcp sdk 文档和目录 mcp-go-sdk-learning/demo-server 下的 mcp server 样例，了解 mcp server 开发流程
2. 阅读目录 mcp-kafka/doc 下的 kafka mcp server 文档，了解当前现状
3. 将目录 mcp-kafka/ 中的 kafka mcp server 所有工具的返回值修改为 object 格式，原格式存在 array 的类型，这不符合 mcp 的规范。在对 tool 进行修改后，更新 mcp-kafka/doc 下的文档
```
追加1

```
请确认是否全部的工具的数据返回格式都进行了修改？
```
追加2（正好上下文中有所有工具的信息，这里就一并让它改了）

```
修改所有工具的代码实现，在提取输入参数时进行数据存在性校验，如果数据不存在，则打印日志并返回错误。
```
对应代码变更 v14 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/13...14/tool/mcp-kafka/doc/broker_tools.md?t=mention&mt=doc&dt=sdk)

测试 broker 接口，看着没啥问题

![](/personal-site-mvp/img/doc-placeholder.svg "")
## step7 新需求开发
### step 7.1 新增查询单个 topic 信息的接口
[https://console.cloud.baidu-int.com/comatestack/share/2594?token=88f9b094](https://console.cloud.baidu-int.com/comatestack/share/2594?token=88f9b094)

```
# 背景
当前已经将目录 pandora-kafka-tool/ 下的 kafka 运维工具改造为了初版的 mcp server ，存放在目录 mcp-kafka/ 中，现在需要新增查看单个 topic 信息的工具

# 需求

1. 阅读目录 mcp-go-sdk-learning/doc 下的 mcp sdk 文档和目录 mcp-go-sdk-learning/demo-server 下的 mcp server 样例，了解 mcp server 开发流程
2. 阅读目录 mcp-kafka/doc 下的 kafka mcp server 文档，了解当前现状
3. 在 mcp-kafka/ 下开发新的工具，它的工具是可以查询指定集群的指定 topic 的信息。开发模式和其它的工具保持一致。
4. 完成代码开发后，完成 mcp-kafka/doc 下的文档，并编写单元测试进行功能性验证
```
远程测试文件生成在了根目录，追加 prompt

```
按照 golang 规范，生成的单元测试文件需要和原文件在同一个目录层级中，请对单元测试文件进行调整，包括文件的位置和其中 import 的依赖信息
```
实现时为从 zk 路径上拉取指定的 topic，而是先拉取了全部的 topic 然后进行过滤，效率太低，打回修改

```
在获取单个 topic 信息时，直接从 zk 对应的路径上直接获取即可，不要获取全量的 topic 信息然后进行过滤，效率太低。按照上述要求进行调整
```
对应代码版本为 v15 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/14...15/tool/mcp-kafka/doc/topic_tools.md?t=mention&mt=doc&dt=sdk)验证没问题

![](/personal-site-mvp/img/doc-placeholder.svg "")
### step 7.2 补全所有函数的注释和单元测试
[https://console.cloud.baidu-int.com/comatestack/share/2595?token=d860167c](https://console.cloud.baidu-int.com/comatestack/share/2595?token=d860167c)

原 step 中的 prompt 存在缺陷，模型在编写代码时并没有生成单元测试，这里让他单独生成一下

```
# 背景
当前已经将目录 pandora-kafka-tool/ 下的 kafka 运维工具改造为了初版的 mcp server ，存放在目录 mcp-kafka/ 中。由于编码不规范，大量代码缺少注释和单元测试，我们需要将其补全

# 需求
1. 阅读目录 mcp-go-sdk-learning/doc 下的 mcp sdk 文档和目录 mcp-go-sdk-learning/demo-server 下的 mcp server 样例，了解 mcp server 的背景信息和开发流程
2. 阅读目录 mcp-kafka/doc 下的 kafka mcp server 文档，了解当前现状
3. 为 mcp-kafka/ 目录中的 golang module 项目中的文件添加注释，包含：
    - 函数定义
    - 结构体定义
    - 代码逻辑中的关键步骤
4. 为 mcp-kafka/ 目录中的 golang module 项目中的文件添加单元测试，单元测试文件需要与被测试函数所在的文件位于同一个目录中
```
追加 prompt

```
运行单元测试进行验证
```
代码版本对应 v16 [评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/15...16/tool/mcp-kafka/config.go?t=mention&mt=doc&dt=sdk) 

# 总结
## 开发总结
虽然上面的步骤比较多，但是我这边主要是先花最多五六分钟写 prompt ，然后就丢给 zulu 去写代码了。zulu 写代码时我就可以去处理值周的业务问题了，所以整体来说没花太多的时间。时间范围为 09/01 下午 - 09/02 上午。在 zulu 生成代码期间处理了至少 5 个业务咨询和线上故障排查的值周事务。

在使用大模型进行编码时，最好在 prompt 里加上：

1. 需要为关键步骤及函数签名/struct增加注释
2. 每一个函数都需要配套上单元测试，并在实现后运行单元测试进行验证

## 一些问题
* zulu 在循环解决问题时，希望可以支持人工介入。例如插入一些 prompt 进行提醒，或者补充一些漏掉的背景知识。
* 希望可以支持对知识添加备注，例如 `xxx dir : 存储 api 文档和样例`，方便管理。目前是人工写在 user prompt 中。
* 希望可以支持重命名对话历史的标题，或者自动总结生成标题，也是方便管理。
* 会小概率生成非预期字符，需要人工 review + 单测兜底：[评审：search-aladdin-offline-809 kafka 运维工具 mcp 改造](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/aladdin/kafka/reviews/117904453/files/18...latest/tool/mcp-kafka/config/config.go?t=mention&mt=doc&dt=sdk)

![](/personal-site-mvp/img/doc-placeholder.svg "")


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
