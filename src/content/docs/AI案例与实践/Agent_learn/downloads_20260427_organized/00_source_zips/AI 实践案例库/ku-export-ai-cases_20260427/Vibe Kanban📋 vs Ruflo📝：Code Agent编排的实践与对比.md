---
title: "RuFlo(claude-flow) 工作流程规则"
description: "Vibe Kanban📋 vs Ruflo📝：Code Agent编排的实践与对比"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Vibe Kanban📋 vs Ruflo📝：Code Agent编排的实践与对比.md"
---
Vibe Kanban📋 vs Ruflo📝：Code Agent编排的实践与对比

#### 🧑‍🏫 案例作者：[@戴贝奇](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)[@v_王佳腾](https://ku.baidu-int.com?t=mention&mt=contact&id=3096b170-3a21-11f1-8584-ad27b5ee9e0f)[@张金龙](https://ku.baidu-int.com?t=mention&mt=contact&id=32e3aeb0-3a21-11f1-8584-ad27b5ee9e0f)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Claude、Ducc、iCafe、iCode
#### 📒 案例概要：近期组内尝试使用两种不同的 AI 协作方式——Vibe Kanban 和 Ruflo重构一个纯后端项目bgw-proxy。这篇文章旨在对比这两种方式在体验上的优缺点，为后续工作提供思路。
[文档目录]
## 0. 核心成果
⏰ **开发效率**：单次任务从手动多窗口切换至单窗口操作，整体提效约 80%

👷 **人工介入**：从全程 10+ 次手动窗口切换、状态追踪减少为 3 次关键审核点（设计、拆分、代码），从被动跟进度变为主动把质量关

📋 **任务管理**：Vibe Kanban从之前的人工记录 ai会话变为 Kanban记录——任务状态、负责人、阻塞关系一目了然，历史决策翻卡片就能找到。

📝 **上下文保持**：Ruflo 多 agent 共享上下文，多任务协调不需要人工传递

🤝 **协作效率**：Vibe Kanban独立 workspace 隔离 + 阻塞关系明确，协作时不用互相等

## 概述
近期组内尝试使用两种不同的 AI 协作方式——Vibe Kanban 和 Ruflo重构一个纯后端项目bgw-proxy。这篇文章旨在对比这两种方式在体验上的优缺点，为后续工作提供思路。



## 用 Code Agent 开发到底“痛”在哪
日常用 code agent 干活，最折腾的是这几个问题：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d760343caf7c4e2a9c54fd9f6264d63d&docGuid=qNj6dnNgcG7iln "")
#### 任务繁多易混乱管理
第一个是任务一多就容易乱。你开了三个任务，每个得生成代码、写单测、审核、提交，窗口切来切去，哪个干完了、哪个卡住了、哪个等审核，全靠脑子记或者其他方式记录，一走神就容易漏掉什么。

#### 任务切换上下文易断档
第二个是上下文断档。一个任务干完了，换下一个任务，前面干了啥、讨论了啥，下个任务不知道。特别是任务之间有依赖的时候，下一个任务得接上一个任务的输出，上下文断了就得重新讲一遍，浪费时间。

#### 审核节点把控麻烦
第三个是审核节点不好把控。生成代码完要看看对不对，通过才提代码，测试完了还得再看一次。每个审核点都要你手动切窗口、找对应的对话，任务多了根本管不过来。

#### 并行执行窗口存在局限
第四个是并行执行不方便。你有个大任务，拆成几个小任务理论上能一起跑，但共享相同文件，任务之间又没有沟通，越改越乱。

根因还是 Code Agent的编排管理问题。我们调研了两种方式，一种是将各个独立的任务窗口综合成一个看板综合管理，一种是由一个 agent 管理编排所有的 agent ，所有工作只依赖一个窗口。

## 这两种工具是干嘛的
**Vibe Kanban**的核心是任务看板加独立工作空间。你把任务拆成卡片放在看板上，每个卡片有自己的状态和负责人。关键点是每个任务跑在独立的工作空间里，互不干扰——就像每个人有自己的工位，干完了再合并到主仓库，在面对多个任务多 Code Agent 执行时，可通过统一的可视化看板界面，实现任务规划、执行编排、配置管理等。详细说明指路：[Vibe Kanban 使用调研](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/CuU6IyQRw33_0x?t=mention&mt=doc&dt=doc)

![ Vibe Kanban 的组成](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a535444daa024d2da2f805845145c9fe&docGuid=qNj6dnNgcG7iln " Vibe Kanban 的组成")
![workspace 使用 git Worktree 使多个对话隔离代码分支和文件](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dbc29c6b3d6a46029dabe85151d84d0b&docGuid=qNj6dnNgcG7iln "workspace 使用 git Worktree 使多个对话隔离代码分支和文件")
**Ruflo**的核心是多 agent 协作编排，主要还是依托Claude Code，以 **MCP Server** 的形式为 Claude Code 提供多 Agent 协调、任务管理、记忆存储等能力。它不是一个独立运行的开发框架，而是一个**附加在 Claude Code 上的元信息管理层，**后续提到的**Ruflo**也是指** Ruflo 和 Claude Code的 Agent Team 结合**。它有个 Swarm 的概念，就是多个 agent 一起协作的蜂群。你只需要给一个总的提示词，规定好系统设计、拆分任务、开发、测试这几个流程，每个流程设置个审批节点就行。Ruflo 会自动安排任务顺序，agent 之间还会互相通讯，共享同一个项目目录和记忆系统，全程在一个窗口进行工作。详细说明指路：[RuFlo 编排调研](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/y6qXt8iXxFl4gF?t=mention&mt=doc&dt=doc)

![多个agent 间信息共享](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c6e85faa62c348898865634b3a0016c7&docGuid=qNj6dnNgcG7iln "多个agent 间信息共享")
两种工具不是竞品，更多的是利用 Code Agent 开发的两种思路

## 使用Vibe Kanban 的重构流程
### **4.1 设计阶段**
```
flowchart LR
    classDef start fill:#2d7d46,stroke:#1a5a2f,stroke-width:2,color:#fff
    classDef process fill:#3498db,stroke:#2980b9,stroke-width:2,color:#fff
    classDef decision fill:#f39c12,stroke:#e67e22,stroke-width:2,color:#fff
    classDef finish fill:#e74c3c,stroke:#c0392b,stroke-width:2,color:#fff
    
    START([开始]):::start --> P1[issue001:分析原代码和 Rule]:::process
    P1 --> P2[生成设计文档和测试用例]:::process
    P2 --> R{人工审核}:::decision
    R -->|不通过| P2
    R -->|通过| P3[创建 issue002拆分任务卡片]:::process
    P3 --> FINISH([完成]):::finish
```
创建issue001分析原代码和Rule生成设计文档和测试用例，并创建拆分任务 issue02

* 使用三个不同的 codeagent 完成，**选取测试用例覆盖最全、设计文档和原代码库功能最一致的结果**
* [系统设计文档模板](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/6Xy2I1RUADz-9N)和[接口文档模版](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/vllLCsOX4wnk2T?source=137)格式存放在 rules 中，设计产出严格遵守模版格式
    * 系统设计文档章节划分：0.修订记录、1.概述、2.整体设计、3.模块设计、4.数据模型、5.接口列表。
    * 接口设计文档章节划分：0.修订记录、1.概述、2.请求数据、3.响应数据、4.错误码。

* 生成前会搭建 rules 中提前打包的脚手架，自动检查编译，检查后通过 skill [icode](https://console.cloud.baidu-int.com/onetool/skills/2057)提交至 icode，提交 icode 时会使用 skill [icafe](https://console.cloud.baidu-int.com/onetool/skills/2082)同步创建 icafe卡片 到指定空间中。
* 文档审核标准
    * 一个 API 一个设计文档，接口设计文档中不包含过多业务逻辑说明。
    * 系统设计覆盖所有功能，接口数量与设计文档一致。
    * 系统设计和接口设计文档风格、格式、示例代码，要符合 Rule中模板定义。
    * 测试用例文档覆盖所有核心功能。

* 这一步中 Rules 的使用就开始十分重要，他会作为后面开发任务的详细指导，尽量编写完善的 Rules，另外如果Rules 中有脚手架先搭建脚手架再进行设计生成指导会更加准确。

![创建设计任务卡片，并且启用了三个不同的 Code Agent](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=033694aca1344dc6a9ccbabdb0ab7811&docGuid=qNj6dnNgcG7iln "创建设计任务卡片，并且启用了三个不同的 Code Agent")


### **4.2 任务拆分阶段**
```
flowchart LR
    classDef start fill:#2d7d46,stroke:#1a5a2f,stroke-width:2,color:#fff
    classDef process fill:#3498db,stroke:#2980b9,stroke-width:2,color:#fff
    classDef decision fill:#f39c12,stroke:#e67e22,stroke-width:2,color:#fff
    classDef finish fill:#9b59b6,stroke:#8e44ad,stroke-width:2,color:#fff
    
    START([开始]):::start --> P1[issue002:拆分独立任务]:::process
    P1 --> R1{人工审核}:::decision
    R1 -->|不通过| P1
    R1 -->|通过| P2[创建任务issue003:\n 搭建项目结构\nissue004: 配置模块\nissue005: 日志模块\n。。。。。。。]:::process
    P2 --> FINISH([结束]):::finish
```
自动生成issue002根据设计文档、代码库和 Rule 拆分出任务列表

* 使用三个不同的 codeagent 完成，**选取拆分最合理，后续合并代码可能冲突更小的结果**。
* 卡片拆分要求：
    * 必须描述清楚职责且让任务卡片只做自己的事情，不要让和其他任务冲突，描述中要给对应的卡片，必须为task 卡片，并且强调必须遵守 rules 规定和设计文档、编译通过、单测覆盖度超 80%、且全部通过。特别提示无论如何不允许调用真实的 bgw 集群接口操作 vs或者其他外部接口，单测和测试都需要 mock 接口。
    * 任务实现时间平均，每个任务预估执行时间不超过 2 小时
    * 人工审核通过，审核中要着重检查任务的依赖关系是否合理，这关乎了后续提交代码冲突的概率，比如常量的定义没有完成就执行了后续任务，那么每个后续任务可能会都创建这个常量的定义，造成了冲突的可能

* iCafe创建原则
    * 使用 icafe skill
    * 每个任务对应一个 icafe story
    * 每个story 下包含一个子卡片，类型为 task
    * icafe中描述信息要记录任务的详细内容


![设计任务自动生成拆分任务->拆分任务生成开发任务、设置阻塞关系](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d7701892d40b4a328d6860af7a80e76a&docGuid=qNj6dnNgcG7iln "设计任务自动生成拆分任务->拆分任务生成开发任务、设置阻塞关系")


### **4.3 开发阶段**
```
flowchart LR
    classDef start fill:#2d7d46,stroke:#1a5a2f,stroke-width:2,color:#fff
    classDef process fill:#3498db,stroke:#2980b9,stroke-width:2,color:#fff
    classDef decision fill:#f39c12,stroke:#e67e22,stroke-width:2,color:#fff
    classDef finish fill:#9b59b6,stroke:#8e44ad,stroke-width:2,color:#fff
    
    START([开始]):::start --> P1[issue003:搭建任务项目结构]:::process
    P1 --> R1{人工审核}:::decision
    R1 -->|不通过| P1
    R1 -->|通过| P2[issue004：常量定义]:::process
    R1 -->|通过| p3[issue005：model层代码编写]:::process
    R1 -->|通过| p4[issue006：client层代码编写 ]:::process
    p3 --> R2{人工审核}:::decision
    P2 --> R2{人工审核}:::decision
    p4 --> R2{人工审核}:::decision
    R2 --> p5[issue006：VSAdd API编写]:::process
    R2 --> p6[issue007：VSDel API编写]:::process
    R2 --> p7[issue008：VSUpdate API编写]:::process
    R2 --> p8[issue009： 回调处理器编写]:::process
    p5 --> R3{人工审核}:::decision
    p6 --> R3{人工审核}:::decision
    p7 --> R3{人工审核}:::decision
    p8 --> R3{人工审核}:::decision
    R3 --> P9[执行完整集成测试]:::process
    P9 --> R4{测试通过?}:::decision
    R4 -->|失败| P10[修复后重新测试]:::process
    P10 --> P9
    R4 -->|通过| P11[产出测试报告]:::report
    P11 --> R5{人工最终审核}:::decision
    R5 -->|不通过| P11
    R5 -->|通过| FINISH([完成]):::finish
```
每个任务是一个独立的 issue，根据设计文档、原代码库和 Rule 生成代码和单测，审核通过后提交到代码库，之后执行集成测试issue，根据代码、设计文档和测试用例进行集成测试，同样审核通过提交代码。因为所有任务都是独立的，集成测试就显得比较重要，除了测试功能，也可以检查出整体在风格、规范等的一致性，这样在一定程度上，解决了上下文不共享的问题。

* 单任务完成标准：
    * 人工审核通过，对比设计文档无遗漏的功能点，是否符合 Rule 规范
    * 单测覆盖度达到 80% 以上


![开发任务在 icode 上审核并冲突处理](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=08e909a3ed324bf2b48323cbf5bbd22c&docGuid=qNj6dnNgcG7iln "开发任务在 icode 上审核并冲突处理")
## 使用Ruflo 的重构流程


ruflo通过一次提示词规定按照系统设计、拆分任务、开发、测试这几个流程，并在每个流程设立审核节点

### **5.1 设计阶段**
由code Agent 分析原代码和Rule生成设计文档和测试用例，产出后进行人工审核

```
flowchart LR
    classDef start fill:#2d7d46,stroke:#1a5a2f,stroke-width:2,color:#fff
    classDef process fill:#3498db,stroke:#2980b9,stroke-width:2,color:#fff
    classDef decision fill:#f39c12,stroke:#e67e22,stroke-width:2,color:#fff
    classDef finish fill:#e74c3c,stroke:#c0392b,stroke-width:2,color:#fff
    
    START([开始]):::start --> P1[分析原代码和 Rule]:::process
    P1 --> P2[生成设计文档和测试用例]:::process
    P2 --> R{人工审核}:::decision
    R -->|不通过| P2
    R -->|通过| FINISH([完成]):::finish
```


### **5.2 任务拆分阶段**
```
flowchart LR
    classDef start fill:#2d7d46,stroke:#1a5a2f,stroke-width:2,color:#fff
    classDef process fill:#3498db,stroke:#2980b9,stroke-width:2,color:#fff
    classDef decision fill:#f39c12,stroke:#e67e22,stroke-width:2,color:#fff
    classDef finish fill:#9b59b6,stroke:#8e44ad,stroke-width:2,color:#fff
    classDef icafe fill:#1abc9c,stroke:#16a085,stroke-width:2,color:#fff
    
    START([开始]):::start --> P1[拆分独立任务]:::process
    P1 --> R1{人工审核}:::decision
    R1 -->|不通过| P1
    R1 -->|通过| P2[询问 icafe 空间地址]:::icafe
    P2 --> P3[创建 icafe 卡片]:::icafe
    P3 --> FINISH([回填卡片 ID]):::finish
```
由 code Agent 决定拆分任务，人工审核通过后提交至 icafe

    1. icafe MCP 提交卡片
    2. 将创建的 icafe 卡片 ID 回填到 task-list.md 中，用于后续阶段同步更新卡片状态



### **5.3 开发阶段**
```
flowchart LR
    classDef start fill:#2d7d46,stroke:#1a5a2f,stroke-width:2,color:#fff
    classDef process fill:#3498db,stroke:#2980b9,stroke-width:2,color:#fff
    classDef decision fill:#f39c12,stroke:#e67e22,stroke-width:2,color:#fff
    classDef ruflo fill:#e67e22,stroke:#d35400,stroke-width:2,color:#fff
    classDef finish fill:#9b59b6,stroke:#8e44ad,stroke-width:2,color:#fff
    
    START([开始]):::start --> P1[RuFlo spawn Agent]:::ruflo
    P1 --> R1{人工审核<br/>任务分配方案}:::decision
    R1 -->|不通过| P1
    R1 -->|通过| P2[开始开发]:::process
    P2 --> P3[编码 + 单测 + 提交]:::process
    P3 --> R2{人工审核}:::decision
    R2 -->|不通过| P3
    R2 -->|通过| P4[更新状态为待测试]:::process
    P4 --> R3{还有任务?}:::decision
    R3 -->|是| P2
    R3 -->|否| FINISH([产出存入 RuFlo]):::finish
```
1. 由code Agent 编排任务并处理，使用 RuFlo spawn 专业 Agent 并行处理独立任务
    1. 每个任务的状态流转：


        * 开始开发时：同步更新 task-list.md 和 icafe 卡片状态为"开发中"
        * 编码和单测完成后提交代码，暂停等待人工审核
        * 人工审核通过后：同步更新 task-list.md 和 icafe 卡片状态为"待测试"

    2. 每个阶段的关键产出存入 RuFlo 记忆系统，跨阶段/跨会话时优先从记忆中检索上下文

```
flowchart LR
    classDef start fill:#2d7d46,stroke:#1a5a2f,stroke-width:2,color:#fff
    classDef process fill:#3498db,stroke:#2980b9,stroke-width:2,color:#fff
    classDef decision fill:#f39c12,stroke:#e67e22,stroke-width:2,color:#fff
    classDef finish fill:#e74c3c,stroke:#c0392b,stroke-width:2,color:#fff
    classDef report fill:#1abc9c,stroke:#16a085,stroke-width:2,color:#fff
    
    START([开始]):::start --> P1[执行完整集成测试]:::process
    P1 --> R1{测试通过?}:::decision
    R1 -->|失败| P2[修复后重新测试]:::process
    P2 --> P1
    R1 -->|通过| P3[更新 icafe 卡片状态]:::report
    P3 --> P4[产出测试报告]:::report
    P4 --> R2{人工最终审核}:::decision
    R2 -->|不通过| P1
    R2 -->|通过| FINISH([完成]):::finish
```
由code Agent 结合测试用例文档进行测试，产出后进行人工审核

## 最终结果
#### 系统设计
生成[系统设计文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/nBIAsAEv8dG8Wp)，包含整体设计、模块设计、数据模型设计、API 设计

* [1. 系统设计文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/nBIAsAEv8dG8Wp?source=137?t=mention&mt=doc&dt=doc)

生成接口文档：

* [1. 添加 VS](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/aAdV9LzSrkqEM3?source=137?t=mention&mt=doc&dt=doc)
* [2. 删除 VS](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/agloHPvPwInd5g?source=137?t=mention&mt=doc&dt=doc)
* [3. 修改 VS](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/y3-AafoPyk65r9?source=137?t=mention&mt=doc&dt=doc)
* [4.TTM 配置](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/XC1GlFyGitg2hu?source=137?t=mention&mt=doc&dt=doc)

生成测试用例文档：

* [3. BGW Proxy 测试用例文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/Xa05s1Ibuy/FOc05Mdi0JwPhG?source=137?t=mention&mt=doc&dt=doc)

#### 开发
对比设计文档，无遗漏的功能点，符合 Rule 规范，产出内容：[文件页：baidu/bs-ai/study-vibekanban  *develop](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bs-ai/study-vibekanban/tree/develop?t=mention&mt=doc&dt=sdk)

代码库统计汇总：

|统计项|数量|
|-|-|
|文件总数|151|
|Go 文件数|86|
|代码总行数|约 10,133 行|
|提交次数|44 次|

#### 测试
测试统计汇总：

|统计项|数量|
|-|-|
|总测试包数|7|
|有测试的包数|5|
|无测试的包数|2 (health, metrics)|
|总测试用例数|160|
|通过测试数|157|
|跳过测试数|3|
|失败测试数|0|
|平均覆盖率|91.12%|
|最高覆盖率|95.8% (load_ttm, callback)|
|最低覆盖率|84.4% (bgw_vs_delete)|
|回调相关测试|65 (callback 38 + API 27)|

测试模块统计汇总：

|模块|状态|覆盖率|测试数|通过|失败|跳过|
|-|-|-|-|-|-|-|
|bgw_vs_delete|✅ PASS|84.4%|42|42|0|0|
|vs_add|✅ PASS|92.5%|37|34|0|3|
|vs_modify|✅ PASS|87.1%|31|31|0|0|
|load_ttm|✅ PASS|95.8%|12|12|0|0|
|callback|✅ PASS|95.8%|38|38|0|0|
|health|✅ PASS|0.0%|-|-|-|-|
|metrics|✅ PASS|0.0%|-|-|-|-|
|**汇总**|||**160**|**157**|**0**|**3**|

* **通过率**: 100% (157 通过 / 3 跳过)
* **平均覆盖率**: 91.12% 

## 两种方式的体验对比
![核心区别对比](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1d68817198514666a574fd3d91d7375a&docGuid=qNj6dnNgcG7iln "核心区别对比")
### 7.1 人工参与
### **Vibe Kanban**
### **Ruflo**
Vibe Kanban面向一个窗口，在任务卡片上进行查看和审批。对比原始的人工编排效率要高，不用自己切来切去盯着每个任务。省去了人工去频繁切换窗口的时间。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e5e46a06916e475580ebb71387faa9fa&docGuid=qNj6dnNgcG7iln "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=03779825c5b442d6be26e10fe70bf04c&docGuid=qNj6dnNgcG7iln "")




不过 Vibe Kanban 有个问题——创建多个任务后，不会自己按照依赖关系跑起来。需要手动按阻塞关系一个一个推，或者专门创建一个任务通过 MCP 接口查询任务状态去推进任务。这块既然可以设置阻塞、依赖关系，如果有自动化执行的功能会更方便些。

Ruflo 也同样面向一个窗口，任务由Code Agent 编排，当需要审批时候阻塞流程，再由人工进行审批。

Ruflo 的编排逻辑内化为 ClaudeCode 的系统能力，首先需要通过生成 `flow.md` 规则文件，向 ClaudeCode 明确整套工作流程，使其能够按照指定流程开展开发工作。
但在实际开发过程中，仍需要多次进行人工干预。原因在于：虽然工作流程由 ClaudeCode 自动执行，但实际体验中发现，它往往会根据任务规模与内容自行规划执行节奏，而非严格遵循规则中定义的流程步骤。
例如，规则中指定设计文档应由 Ruflo 提供的架构师 Agent 完成，ClaudeCode 却可能直接自行开展项目重构，此时就需要及时中断并修正任务，后续开发中也需要持续关注、随时纠偏。

此外，还偶发完全不遵循 `rule` 流程的情况：比如规则明确要求先提出方案并经人工审核，再创建任务列表，但 ClaudeCode 有时会直接完成全部任务创建；甚至出现不使用 Ruflo Task，转而使用自身内置 todos 能力的情况。
即便在规则中明确要求强制使用 Ruflo 编排能力，并指定由专业 Agent 承担对应工作，ClaudeCode 依然更倾向于直接解决问题，而非严格按流程执行。

### 7.2 Prompt 的不同
### **Vibe Kanban**
### **Ruflo**
Vibe Kanban 需要指明任务执行阶段，说明下一步要生成哪些任务，用哪个 agent，在哪个代码库和分支。下面为设计任务时编排的提示词，因为设计任务为起始任务，后续的任务都有他指导生成，所以有关任务执行阶段的提示词以创建任务的形式都写在了这里，提示词包含了如何生成拆分任务和拆分任务如何拆分并生成开发任务和测试任务。

```
创建 vibe kanban issue,以下为 issue 信息：
项目：当前项目
标题：design002 - 任务拆分
描述：
```javascript
你正在执行一个重构百度项目BGW Proxy的重构阶段的任务拆分阶段，使用 go 重构原来的 Python 项目。
## 你的任务
1. 仔细阅读设计文档，理解项目架构和模块划分
2. 识别所有需要实现的功能模块和技术模块
3. 将项目拆分为可执行的任务列表
4. 确定任务之间的依赖关系
5. 估算每个任务的工作量
6. 使用 mcp根据拆解的任务在 iCafe中创建卡片，创建卡片必须调用icafe-card-assistant这个 skill,同时为 bgw_proxy项目创建issue,issue和 iCafe 卡片必须一一对应
7. 遵守代码库中 rules 规定
8. 在拆分任务完成需要我确定再创建 icafe 卡片和 issue
 
#### issue 的规定
- 项目:为当前项目
- 标题:格式为：develop00x - xxx（注意卡片不用这个格式，卡片格式还是参考 skill 中的规定）
- 描述:必须描述清楚他的职责且让他只做自己的事情，不要让他和其他任务冲突，描述中要给他对应的卡片，注意是 task 卡片，并且强调必须遵守 rules 规定和设计文档、编译通过、单测覆盖度超 80%、且全部通过。特别提示无论如何不允许调用真实的 bgw 集群接口操作 vs或者其他外部接口，单测和测试都需要 mock 接口。最后提示将此百度项目提交代码到icode，要绑定此任务 icafe 的 task 卡片。
## 任务拆分原则
### 粒度控制
- 每个任务预计完成时间：2-4 小时
- 保证写一个 api为 一个任务
- 调用 外部 api 可以进行任务合并
- 保证一个处理器一个任务
- 要先创建项目框架
### 依赖管理
- 明确任务之间的阻塞关系（blocking）
- 确保依赖任务先完成
- 尽量减少阻塞依赖，提高并行度
## 验收标准
- 任务列表完整，覆盖所有模块
- 依赖关系正确，无循环依赖
- 任务粒度合理（2-4 小时）
```
```
Ruflo的 prompt 与 vibe Kanban 雷同，但是因为是为 ClaudeCode 引入了 ruflo 的思想，所以需要指定相关的 rule 文件，指明工作流程。

但是目前柑橘 Ruflo V3 还是 alpha 阶段，自己生成的 CLAUDE.md 说明并不多，所以我这里补充了很多 Ruflo 的 MCP 的相关接口，其实感觉除了流程外，这些应该是 Ruflo 自己生成的，但是目前并没有强制要求 ClaudeCode 必须使用 Ruflo 的能力。

rule:

```
# RuFlo(claude-flow) 工作流程规则

## 核心职责划分
- **RuFlo MCP**：负责任务跟踪、Agent 管理、集群协调、状态同步
- **Claude Code**：
  - **阶段一**：与 `system-architect` 协作完成系统设计
  - **阶段二～阶段四**：仅负责任务编排，包括 Spawn Agent、调用 MCP 工具、更新任务状态，**不得自行读取代码文件、搜索代码内容或做分析工作**
- **Spawn 出来的 Subagent（阶段二～阶段四）**：负责所有实际工作，包括读代码、做分析、写文档、编码、Review 等

**【强制禁止（阶段二～阶段四）】Claude Code 主 agent 禁止自行执行任何代码分析、文件读取、代码搜索等操作。所有分析工作必须交给 Spawn 出来的专业 Agent 完成。阶段一除外。**

## 阶段编排策略
| 阶段 | 编排方式 | Agent 类型 | 说明 |
|------|---------|-----------|------|
| 阶段一 | 系统设计 | `system-architect` | 分析原代码库，阅读 Rule 规范，产出架构/功能/接口/测试用例文档 |
| 阶段二 | 单 Agent Spawn | `planner` | 任务拆分，不需要集群 |
| 阶段三 | **Swarm 集群** | `coder`, `reviewer`, `tester`, `hierarchical-coordinator` | 复杂开发任务，需要集群并行 |
| 阶段四 | 复用阶段三集群 | `tester`, `test-long-runner`, `coder` | 集成测试，复用无需重建 |

### Swarm 集群（仅阶段三、四）
阶段三开始时**初始化一次 Swarm 集群**，阶段四复用：

1. **阶段三开始时初始化**：
   - 调用 `swarm init` MCP 工具：`topology=hierarchical`, `max-agents=8`, `strategy=specialized`
   - 使用 `hierarchical` 拓扑结构
   - 最大 8 个 agent 用于紧密协作

2. **阶段四复用**：直接使用，无需重新初始化

### Agent 池（60+ 预定义类型）
RuFlo 提供丰富的预定义 Agent 类型，包括但不限于：
- 核心开发：`coder`、`reviewer`、`tester`、`planner`、`researcher`
- 架构设计：`security-architect`、`performance-engineer`、`ddd-domain-expert`
- 集群协调：`hierarchical-coordinator`、`mesh-coordinator`、`adaptive-coordinator`
- 代码质量：`security-auditor`、`code-review-swarm`

**根据任务需要自行分析选择合适的 Agent 类型**。

### Subagent 启动方式（两种工具，缺一不可）
Claude Code 必须同时使用两类工具才能让 Subagent 真正工作：

1. **RuFlo MCP `agent spawn`**（注册 agent 到系统）
2. **Claude Code `delegate_subtask` 工具**（真正启动 agent 执行任务）

**缺一不可**：`agent spawn` 只注册不启动，`delegate_subtask` 才让 agent 真正跑起来。

**正确调用示例**（阶段二/三 spawn coder）：
```
使用 delegate_subtask 工具：
- agent_type: coder
- description: 你是专业的 Golang 开发工程师。请完成以下任务：...（填写具体任务描述）
- run_in_background: true
```

### Swarm 编排规则
- **所有操作必须并发执行**：在单条消息中批量 spawn 所有需要的 Agent
- **必须使用 `run_in_background: true`**：所有 Agent Task 调用必须后台运行
- **Spawn 后停止**：不要持续检查状态，等待 Agent 结果返回
- **【强制】Subagent 生命周期管理**：
  - Subagent 在完成**整个任务流程**前**不得被销毁**，包括：编码 → 单测 → Review → 修复（如有）→ 再次 Review 直至通过
  - **禁止完成开发编码后就销毁 agent**，因为可能出现 Review 问题需要原 agent 修复
  - 只有在任务最终完成（代码提交 icode、人工审核通过）后才能释放 agent
- **【强制】Agent 与 Task 的对应关系**：
  - **一个 Task 必须对应一个专属的 Subagent**，该 agent 全权负责此 Task直至完成
  - 创建 Task 时，通过 `task_assign` MCP 工具分配负责此 Task 的 agent_id
  - **禁止多个 Task 共用一个 agent**，也**禁止一个 Task 中途更换 agent**
  - 出现 Review 问题需要修复时，**必须由该 Task 对应的原 agent 修复**，不得转让给其他 agent
- **子 Agent 必须更新状态**：Spawn 的子 Agent 在工作时必须通过 `task update` MCP 工具更新自身的任务状态，包括：
  - **task 状态**：`status=in_progress`（开始）、`status=completed`（完成）
  - **worker 状态**：通过 `agent update` MCP 工具更新 worker 的运行状态（`idle`、`busy`、`error`）
  - **metadata**：记录进度、踩坑经验等

### 记忆系统集成
- **每个阶段完成后**：通过 MCP 接口将关键产出存入记忆系统
  - 调用 `memory store` MCP 工具：`key=<阶段名>-摘要`, `value=<关键内容>`, `namespace=project`
- **进入新阶段时**：通过 MCP 接口检索记忆系统获取上下文
  - 调用 `memory search` MCP 工具：`query=<阶段名 context>`
- **【新增】Task 级别 Checkpoint 机制**：防止长时间运行导致上下文压缩而跑偏
  - **开始 Task 前**：调用 `session_save` MCP 工具保存当前会话快照，同时调用 `memory store` 存入任务上下文（Task 名称、当前进度、待解决问题、已完成代码路径、踩坑记录），`key` 格式为 `checkpoint-<task-id>-<步骤名>`
  - **每个关键步骤完成后**：必须立即调用 `memory store` 更新 Checkpoint，记录当前进度和待处理项（不要等到 Task 结束才存）
  - **检测到上下文可能丢失时（如响应开始偏离主题）**：主动调用 `memory retrieve` 检索 `checkpoint-<task-id>` 恢复上下文
  - **Task 恢复时**：必须先调用 `session_restore` 或 `memory search` 恢复 Checkpoint，确保从断点继续而非从头开始
  - **核心原则**：RuFlo 的 Session 和 Memory 作为外部持久层，Claude Code 上下文作为运行时层，两者互补；RuFlo 中存的是结构化的「任务快照」，Claude Code 内存的是当前的「对话上下文」

## 工作流程

```mermaid
flowchart TD
    START([一次提示词启动]) --> P1[阶段一：系统设计]

    subgraph 阶段一：系统设计
        P1 --> P1_1[分析原代码和 Rule]
        P1_1 --> P1_2[生成设计文档和测试用例]
        P1_2 --> R1{人工审核}
    end

    R1 -->|不通过| P1_2
    R1 -->|通过| P2[阶段二：拆分任务]

    subgraph 阶段二：拆分任务
        P2 --> P2_1[拆分独立任务]
        P2_1 --> R2{人工审核}
        R2 -->|不通过| P2_1
        R2 -->|通过| P2_2[询问用户 icafe 空间地址]
        P2_2 --> P2_3[创建 icafe 卡片<br/>多个 Story + 对应 Task]
        P2_3 --> P2_4[回填卡片 ID 到 task-list.md]
    end

    P2_4 --> P3[阶段三：任务开发]

    subgraph 阶段三：任务开发
        P3 --> P3_1[RuFlo spawn Agent<br/>并行处理独立任务]
        P3_1 --> R3_0{人工审核<br/>任务分配方案}
        R3_0 -->|不通过| P3_1
        R3_0 -->|通过| P3_2[开始开发：更新状态为开发中<br/>同步 task-list.md + icafe]
        P3_2 --> P3_3[编码 + 单测 + 提交代码]
        P3_3 --> R3{人工审核}
        R3 -->|不通过| P3_3
        R3 -->|通过| P3_4[更新状态为待测试<br/>同步 task-list.md + icafe]
        P3_4 --> P3_5{还有任务?}
        P3_5 -->|是| P3_2
        P3_5 -->|否| P3_6[产出存入 RuFlo 记忆系统]
    end

    P3_6 --> P4[阶段四：集成测试]

    subgraph 阶段四：集成测试
        P4 --> P4_1[执行完整集成测试]
        P4_1 --> P4_2{测试通过?}
        P4_2 -->|失败| P4_3[修复后重新测试]
        P4_3 --> P4_1
        P4_2 -->|通过| P4_4[更新 icafe 卡片状态为测试通过]
        P4_4 --> P4_5[产出测试报告]
        P4_5 --> R4{人工最终审核}
    end

    R4 -->|不通过| P4_1
    R4 -->|通过| END([流程完成])
```

## MCP 工具速查
**【强制】所有操作必须通过 MCP 接口调用，不得使用本地命令行**：

| MCP 工具 | 用途 | 关键参数 |
|---------|------|---------|
| `hive-mind init` | **【强制】初始化 Hive-Mind 集群** | `topology`, `queenId` |
| `hive-mind spawn` | **【强制】创建 workers 并自动加入集群** | `count`, `role`, `agentType`, `prefix` |
| `swarm init` | 初始化 Swarm 集群 | `topology=hierarchical`, `max-agents=8`, `strategy=specialized` |
| `agent spawn` | 注册 agent 到 RuFlo 系统（仅注册，不启动工作） | `agentType`, `agentId` |
| `agent start` | 启动已注册的 agent | `agent_id` |
| `agent update` | **【强制】更新 worker 状态** | `agent_id`, `status`（`idle`、`busy`、`error`） |
| `task create` | **【强制】创建任务** | `type`, `description`, `priority`, `assignTo` |
| `task update` | **【强制】更新任务状态** | `task_id`, `status`, `progress`, `assignTo` |
| `task assign` | **【强制】分配 Task 给 Agent** | `task_id`, `agentIds` |
| `task list` | 列出所有任务 | `status`, `assignedTo`（可选） |
| `session_save` | **【强制】Task 开始前保存会话快照** | `session_id`, `metadata` |
| `session_restore` | **【强制】Task 恢复时还原会话** | `session_id` |
| `session_list` | 列出已有会话 | - |
| `memory store` | **【强制】存入 Checkpoint（Task 级别）** | `key=checkpoint-<task-id>-<步骤>`, `value`, `namespace` |
| `memory retrieve` | **【强制】恢复 Checkpoint** | `key`, `namespace` |
| `memory search` | 检索记忆（语义搜索） | `query`, `namespace`, `limit` |

**【重要】`delegate_subtask` 工具**：这是 Claude Code 调用 Subagent 执行实际工作的唯一方式，必须在每次 Spawn Agent 时使用，`agent_type` 指定 Agent 类型，`description` 填写详细任务描述，`run_in_background: true`。不要只用 MCP `agent spawn`，那是只注册不工作的。

## 约束
* **【强制】每个 `[阶段X完成]` 后必须停止，输出完整状态报告，等待人工回复"继续"后方可进入下一阶段**
* **【强制】所有 ruflo 操作必须使用 MCP 接口（`task create`、`task update`、`agent update` 等），禁止使用本地命令行（如 `claude-flow task create` 等）**
* **【强制】任务状态变更时，必须同时更新 RuFlo Task 和 icafe 卡片两处状态，不得只更新一处**
* **【强制】代码完成后必须推送到 icode 远程仓库，禁止只提交到本地**
* **【强制】Task 级别的 Checkpoint 机制**：每个 Task 在开始时必须 `session_save` + `memory store`；在每个关键步骤（编码完成、Review 修复后、提交前）必须更新 Checkpoint；Task 恢复时必须先 `memory retrieve` 恢复上下文，不得在上下文丢失后继续裸奔
* 如果人工审核反馈需要修改，在当前阶段内迭代修改，不跳过
* 严格遵守文件组织规范：src → 源码，tests → 测试，docs → 文档
* **【强制禁止（阶段二～阶段四）】Claude Code 主 agent 不得自行读取代码文件、搜索代码内容、做代码分析。所有分析工作必须交给 Spawn 的 Agent 完成。阶段一除外。**
* **必须使用 delegate_subtask 工具 spawn Agent**，不得仅使用 MCP
* **必须使用 `run_in_background: true`** 进行后台并发执行

## 工具要求
本项目已通过 `ruflo init` 初始化，开发过程中**必须使用 RuFlo（claude-flow） 的完整编排能力**：

1. **多 Agent 协作**：通过 `delegate_subtask` 工具 spawn 专业 Agent（`coder`、`reviewer`、`tester`、`planner`、`system-architect`）并行处理独立任务，而非逐个串行执行
2. **Swarm 集群**：仅阶段三需要初始化一次，阶段四直接复用
3. **记忆持久化**：每个阶段的关键产出存入 RuFlo 记忆系统；进入新阶段或会话恢复时，优先从记忆中检索前序上下文
4. **【强制】`delegate_subtask` 工具是启动 Subagent 工作的唯一方式**，必须在每次需要 Agent 干活时调用，提供详细的 `description`（任务要求）和正确的 `agent_type`（Agent 类型），`run_in_background: true`

```
prompt：

```
# bgw-proxy 重构任务

## 背景
重构 bgw-proxy 项目，将现有代码按照设计文档和 Rule 规范进行重写，确保功能与原 Python 开发的功能一样完整、测试覆盖达标。

## 项目配置
- **原代码库路径**：`/root/codes/bgw-proxy`
- **Rule 规范路径**：`./.claude/rules/*.mdr`
- **icafe 空间**：`study-ai`
- **所属计划**：`ruflo`
- **卡片负责人**：`v_wangjiateng`

## 任务要求

### 阶段一：系统设计
1. 阅读原代码库：`/root/codes/bgw-proxy`，理解现有功能和架构
2. 阅读项目 Rule 规范：`./.claude/rules/*.mdr`
3. 生成设计文档（中文），写入 `docs/` 目录：
   - 架构文档：整体架构、模块划分、技术选型、架构决策
   - 功能文档：功能模块描述、业务流程、数据流图
   - 接口文档：API 定义、请求/响应结构、错误码
   - 测试用例文档：测试策略、测试分层、测试用例
4. **完成后暂停，等待人工审核确认**

### 阶段二：拆分任务
1. 分析设计文档，拆分独立开发任务
2. 要求：
   - 每个任务预估不超过 1 小时
   - 任务依赖关系明确
   - 任务粒度均匀
3. **输出任务拆分方案，等待人工确认**
4. 确认后创建 icafe 卡片并同步到 RuFlo Task

### 阶段三：任务开发
1. 初始化 Swarm 集群并行开发
2. 每个任务要求：
   - 代码写入当前项目目录（Golang 风格）
   - 单测使用 `_test.go` 风格，与被测文件同目录
   - 编译通过，单测全部 pass
   - 符合 Rule 规范
3. 代码需推送到 icode 进行人工审核
4. **全部完成后暂停，等待人工审核确认**

### 阶段四：集成测试
1. 执行完整集成测试
2. 产出测试报告，写入 `docs/test-report.md`
3. **完成后暂停，等待人工最终审核**

## 完成标准
- 架构/功能/接口文档覆盖所有功能
- 开发无功能遗漏，编译通过，单测覆盖率 ≥ 80%
- 代码风格符合 Rule 规范
- 所有集成测试用例通过

---

**工作流程详细规则参考**：`@14-ruflo-workflow.md`

```
Vibe Kanban规定生成什么任务的行为和Ruflo设置审批节点其实作用是一样，都是规定任务介入的时机。

### 7.3 上下文共享
### **Vibe Kanban**
### **Ruflo**
Vibe Kanban 每个任务上下文是隔开的。每个任务可以启动不同的会话处理，好处是基本不会遇到 Token 溢出压缩的问题，坏处是每个任务都要从头读一遍设计文档和当前代码，有点重复劳动。但可以通过为 code agent配置上下文记忆插件缓解，如果解决了上下文共享的问题加上合理的任务拆分，独立的工作空间会让任务生成的更加稳定。



Ruflo 所有 agent 共享同一个上下文，也是同一个项目目录，内存是共用的。好处是信息流动顺畅，坏处是任务太复杂也会遇到上下文压缩。实际用下来会遇到上下文压缩导致，Claude 不使用 Ruflo 等情况，这种导致实际的效果会打折扣。同样可以通过为 code agent配置上下文记忆插件缓解上下文紧张的问题。

### 7.4 多任务提交代码冲突
### **Vibe Kanban**
### **Ruflo**
Vibe Kanban 的设计是每个任务跑在独立的工作空间里，就像多人协作一样——虽然阻塞关系规定了谁先谁后，但大家改的是不同的文件副本，最后合并时难免有冲突，不过其实让 agent 自己查看评审状态自行解决就好。

此次在开发任务中同样出现了代码冲突问题，删除 VS接口和创建 VS 接口的在公共路由注册文件定义时出现了冲突，后续通过 agent 自行解决冲突

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6a0471632a644ce8c1ebcd5b3e41d32&docGuid=qNj6dnNgcG7iln "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c854a21ae5b045ac8430c92a5ba31d9d&docGuid=qNj6dnNgcG7iln "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a4748a4a4e9444e7a1f2f0c8facb5403&docGuid=qNj6dnNgcG7iln "")




ruflo 不会出现代码冲突的问题，因为在规划任务时会根据任务的依赖关系合理的创建任务执行流程，并不会发生代码冲突，提交代码因为有人工干预 所以一次也只会提交一个 commit，而且并不是独立工作空间，是在同一个项目内操作

如下是任务规划：

```
gantt
      title BGW-Proxy 重构项目 - 并行执行时间线
      dateFormat X
      axisFormat %Hh

      section Story 1
      S1-T01 初始化项目      :s1_01, 0, 0.5h
      S1-T02~05 常量定义    :s1_par1, after s1_01, 0.5h
      S1-T06 配置管理       :s1_06, after s1_01, 0.75h
      S1-T07~09 数据模型    :s1_par2, after s1_06, 1h
      S1-T10~12 基础设施完成 :s1_end, after s1_par2, 1.5h

      section Story 2
      S2-T01~08 Parser串行   :s2_all, after s1_par2, 7.5h

      section Story 3
      S3-T01~02 Repository   :s3_01, after s1_end, 1.25h
      S3-T03 Service添加     :s3_03, after s3_01, 1h
      S3-T04~06 Service并行  :s3_par1, after s3_03, 2h
      S3-T07~10 Handler并行  :s3_par2, after s3_par1, 2.5h

      section Story 4
      S4-T01~04 TTM串行      :s4_all, after s1_par2, 3.5h

      section Story 5
      S5-T01 回调框架        :s5_01, after s1_par2, 1h
      S5-T02~03 处理器并行   :s5_par1, after s5_01, 1h
      S5-T04 重试机制        :s5_04, after s5_par1, 0.75h
      S5-T05~09 功能并行     :s5_par2, after s5_04, 3.75h

      section Story 6
      S6-T01~04 Mock串行     :s6_serial, 0, 3h
      S6-T05~06 Mock并行     :s6_par, after s6_serial, 2h

      section Story 7
      S7-T01~03 日志串行     :s7_all, 0, 2.25h

      section Story 8
      S8-T01~05 测试部署     :s8_all, after s3_par2 s4_all s5_par2, 4.5h
```
```
flowchart TB
      classDef critical fill:#ffcdd2,stroke:#c62828,stroke-width:3px,color:#000
      classDef parallel fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px,color:#000
      classDef serial fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
      classDef milestone fill:#fff9c4,stroke:#f9a825,stroke-width:3px,color:#000

      START((开始)):::milestone

      subgraph S1[Story 1: 基础设施搭建]
          direction TB
          S1T01[S1-T01: 初始化 Go 项目结构]:::critical
          S1T02[S1-T02: 通用错误码]:::parallel
          S1T03[S1-T03: BGW 常量]:::parallel
          S1T04[S1-T04: 回调常量]:::parallel
          S1T05[S1-T05: TTM 常量]:::parallel
          S1T06[S1-T06: 配置管理模块]:::critical
          S1T07[S1-T07: VS/RS 结构体]:::parallel
          S1T08[S1-T08: TTM 结构体]:::parallel
          S1T09[S1-T09: 回调任务结构体]:::parallel
          S1T10[S1-T10: 统一响应结构]:::serial
          S1T11[S1-T11: 数据库初始化]:::critical
          S1T12[S1-T12: HTTP Client]:::serial
      end

      START --> S1T01
      S1T01 --> S1T02 & S1T03 & S1T04 & S1T05
      S1T01 --> S1T06
      S1T06 --> S1T07 & S1T08 & S1T09
      S1T09 --> S1T10
      S1T07 --> S1T11
      S1T11 --> S1T12

      subgraph S2[Story 2: Parser 模块]
          direction TB
          S2T01[S2-T01: RSParser-基础]:::serial
          S2T02[S2-T02: RSParser-ID生成]:::serial
          S2T03[S2-T03: RSParser-rs_mode]:::serial
          S2T04[S2-T04: RSListParser]:::serial
          S2T05[S2-T05: ConfigParser-基础]:::serial
          S2T06[S2-T06: ConfigParser-overlay]:::serial
          S2T07[S2-T07: AddVS-underlay]:::serial
          S2T08[S2-T08: AddVS-overlay]:::serial
      end

      S2T01 --> S2T02 --> S2T03 --> S2T04 --> S2T05 --> S2T06 --> S2T07 --> S2T08

      subgraph S3[Story 3: VS 管理]
          direction TB
          S3T01[S3-T01: Repository 接口]:::critical
          S3T02[S3-T02: SQLite 实现]:::critical
          S3T03[S3-T03: Service-添加]:::critical
          S3T04[S3-T04: Service-删除]:::parallel
          S3T05[S3-T05: Service-更新]:::parallel
          S3T06[S3-T06: Service-验证]:::parallel
          S3T07[S3-T07: Handler-添加]:::parallel
          S3T08[S3-T08: Handler-删除]:::parallel
          S3T09[S3-T09: Handler-更新]:::parallel
          S3T10[S3-T10: ID 生成器]:::parallel
      end

      S3T01 --> S3T02 --> S3T03
      S3T03 --> S3T04 & S3T05 & S3T06
      S3T06 --> S3T07 & S3T08 & S3T09 & S3T10

      subgraph S4[Story 4: TTM 加载]
          direction TB
          S4T01[S4-T01: 配置解析器]:::serial
          S4T02[S4-T02: 文件加载器]:::serial
          S4T03[S4-T03: 缓存管理]:::serial
          S4T04[S4-T04: 更新机制]:::serial
      end

      S4T01 --> S4T02 --> S4T03 --> S4T04

      subgraph S5[Story 5: 异步回调]
          direction TB
          S5T01[S5-T01: 回调框架]:::serial
          S5T02[S5-T02: HTTP 处理器]:::parallel
          S5T03[S5-T03: MQ 处理器]:::parallel
          S5T04[S5-T04: 重试机制]:::serial
          S5T05[S5-T05: 状态追踪]:::parallel
          S5T06[S5-T06: 并发控制]:::parallel
          S5T07[S5-T07: 超时管理]:::parallel
          S5T08[S5-T08: 自定义扩展]:::parallel
          S5T09[S5-T09: 监控指标]:::parallel
      end

      S5T01 --> S5T02 & S5T03
      S5T02 & S5T03 --> S5T04
      S5T04 --> S5T05 & S5T06 & S5T07 & S5T08 & S5T09

      subgraph S6[Story 6: Mock 控制器]
          direction TB
          S6T01[S6-T01: 配置管理]:::serial
          S6T02[S6-T02: 规则引擎]:::serial
          S6T03[S6-T03: 响应生成器]:::serial
          S6T04[S6-T04: 状态管理]:::serial
          S6T05[S6-T05: 调试接口]:::parallel
          S6T06[S6-T06: 统计功能]:::parallel
      end

      S6T01 --> S6T02 --> S6T03 --> S6T04
      S6T04 --> S6T05 & S6T06

      subgraph S7[Story 7: 日志系统]
          direction TB
          S7T01[S7-T01: 日志框架]:::serial
          S7T02[S7-T02: 请求日志中间件]:::serial
          S7T03[S7-T03: 审计日志]:::serial
      end

      S7T01 --> S7T02 --> S7T03

      subgraph S8[Story 8: 集成测试]
          direction TB
          S8T01[S8-T01: 单元测试]:::critical
          S8T02[S8-T02: 集成测试]:::serial
          S8T03[S8-T03: 性能测试]:::serial
          S8T04[S8-T04: CI/CD]:::serial
          S8T05[S8-T05: 部署文档]:::serial
      end

      S8T01 --> S8T02 --> S8T03 --> S8T04 --> S8T05

      END((完成)):::milestone
      S8T05 --> END

      S1T07 -.->|数据模型| S2T01
      S1T11 -.->|数据库| S3T01
      S2T08 -.->|Parser| S3T03
      S1T08 -.->|TTM模型| S4T01
      S1T09 -.->|回调模型| S5T01
      S3T06 -.->|VS模块| S8T01
```
### 7.5 生成速度和Token 消耗
### **Vibe Kanban**
|阶段|任务|任务执行时间（分钟）|阶段执行时间（分钟）|任务 token 消耗（k）|阶段 token 消耗（k）|
|-|-|-|-|-|-|
|设计阶段|分析原项目|15|50|45|107|
||部署脚手架|8||23||
||生成设计文档|13||37||
||生成测试用例|13||22||
|拆分任务阶段|读取设计文档进行分析和规划|10|100|8|108|
||创建 iCafe 卡片|30||40||
||创建 Issues|20||20||
||创建依赖关系|10||20||
||修改 Issues|20||20||
|开发阶段|接口开发|平均45（读取文档消耗和拆分阶段几乎相同，主要还是编写代码）| 200|平均 80（读取文档消耗和拆分阶段几乎相同，主要还是编写代码）|320|
||处理器开发|60|60|61|61|

### **Ruflo**
|阶段|任务|任务执行时间（分钟）|阶段执行时间|任务 token 消耗|阶段 token 消耗|
|-|-|-|-|-|-|
|设计阶段|部署脚手架| 5|29|35|111K|
||分析原项目|5||20||
||生成设计文档+测试用例|15.7||56||
|拆分任务阶段|生成任务规划|11|30|55|75K|
||创建 task+icafe|35||20||
|开发阶段|功能开发（30 个子任务）| 355 平均 11.8|475|平均114k  |3.42M|
||集成测试|120 平均 14.6||平均103k|929k|

### 7.6 Code Agent配置体验对比
### **Vibe Kanban**
### **Ruflo**
Vibe Kanban 不需要通过另外配置和 Code Agent 互联互通，他会自动调用 Code Agent的 Cli，并通过 Web 页面统一管理Code Agent 的 mcp和运行参数配置，还可以设置预设配置，每次生成任务的时候可以自己选用哪个 agent（Claude Code、Codex、Gemini、AMP、Cursor、Copilot、OpenCode、QWen Code、DUCC 等 11 种）和哪个配置。

配置 Code Agent MCP 服务器

![阿哥](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bb5362edbe014985b691533f82567436&docGuid=qNj6dnNgcG7iln "阿哥")
配置 Code Agent  执行参数

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=276b27b2a419472fa590cd52a27ccdac&docGuid=qNj6dnNgcG7iln "")
Ruflo 提供初始化命令 `ruflo init`，会在项目中自动生成 CLAUDE.md、./.claude、./.claude-flow、.mcp.json 等 ClaudeCode 相关文件。



其中核心结构包括：



* `./.claude/agents`：内置 60+ 个 Ruflo 预定义 Agent
* `./.claude/helpers/`：存放预设的工具函数文件
* `./.claude/settings.json`：已注册 Ruflo 钩子函数，并导入了多种预定义 skill 和 command
* `.mcp.json`：已完成 Ruflo MCP 的注册配置



整体配置非常简单，一行命令即可完成初始化；



唯一需要自行编写的，是工作流里的规则（rule）定义。

## 总结与展望
### 8.1. 总结
两种方式都不是完美的，但相比人工编排要效率高。Vibe Kanban 的优势是任务拆分清晰、每个任务独立运行、互不干扰，适合任务边界明确、可以并行干的项目。Ruflo 的优势是多 agent 自动编排、共享上下文、自动安排顺序，适合子任务之间依赖多、需要密协配合的场景。

### 8.2. 展望
![Vibe Kanban 和 Ruflo相结合](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=69f292d3fdc9449f842e2ddd8019122f&docGuid=qNj6dnNgcG7iln "Vibe Kanban 和 Ruflo相结合")
Vibe Kanban 和 Ruflo 各有优势，正如之前说的，他们不是竞品，将两种工具结合起来可能是个更好的方案。

用 Vibe Kanban 做任务管理和跟踪，用 Ruflo 做具体任务的执行。进度跟踪、团队协作用等看板，单个复杂任务的执行、多 agent 协调用 Ruflo 的 swarm 能力。将任务拆解成尽可能独立的任务创建在看板上，用看板管理 Ruflo，这样的拆解也就解决了上下文压缩的问题，且 Ruflo 的上下文记忆功能也解决了多个任务间上下文共享问题，不用每次都重新读取设计文档等参考信息，而靠 Ruflo 的能力也能更快速的解决单个任务，这也是 vibe kanban 可以调用 agent 的这一和其他看板能力不同的体现。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
