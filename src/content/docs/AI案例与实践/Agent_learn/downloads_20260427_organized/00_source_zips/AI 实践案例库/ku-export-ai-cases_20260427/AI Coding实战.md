---
title: "概念介绍"
description: "AI Coding实战"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\AI Coding实战.md"
---
AI Coding实战

#### 🧑‍🏫 案例作者：[@杨祖豪](https://ku.baidu-int.com?t=mention&mt=contact&id=6b007a80-fce1-11f0-8e5b-11b25ffca8aa)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了利用AI Coding进行项目实战的经验，涵盖了网盘企业版服务重构、API对接、异步协程重构、性能分析、耗时优化及视频冷热判断等多个案例。通过制定详细规则，利用AI Coding工具提升开发效率，实现自动化代码生成与优化。同时，介绍了Spec-Driven Development（SDD）方法论，强调以规格说明书为核心，通过AI或代码生成器转换成实现，提升软件工程的抽象层次。
### 网盘项目案例
|代码库|语言|负责人|需求|备注||
|-|-|-|-|-|-|
|baidu/netdisk/nd-enorgnization|go|王俊|需求背景介绍：为将网盘企业版老服务纳入 **Easy** 项目治理，现对存量代码进行梳理并分批重构迁移，主要包含：**服务注册、API 注册、实体（Entity）注册**。**第一阶段**聚焦数据库操作最重的核心服务：完成大规模业务领域模型的梳理与数据库/数据表的设计与注册；同时依据 **Easy** 新规范重构既有数据库访问封装并自动化生成标准实现。该阶段完成后，预计可覆盖整体重构工作量的 **约 40%**。|**实现子任务1：**扫描存量代码找出符合要求的已注册的数据库信息和使用的表信息，通过easy提供的mcp工具同步到easy平台中，在根据easy脚手架拉取新生成Entity和常规Dao封装代码：[https://console.cloud.baidu-int.com/comatestack/share/2956](https://console.cloud.baidu-int.com/comatestack/share/2956)平台效果：![存量代码注册实体](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=74342a44c56745359a47ce73f22f3301&docGuid=-0XgDbIeQsi4aX "存量代码注册实体")![同步到了平台](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=84f3b98746a2407983f948b0d4840a10&docGuid=-0XgDbIeQsi4aX "同步到了平台")![新生成的Entity和Dao](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=69609f9fe0be43f7a509f176faed8490&docGuid=-0XgDbIeQsi4aX "新生成的Entity和Dao")代码库review：[评审：netdisk-infrastructure-18646 [Story] 【插入】easy项目重构](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/netdisk/nd-enorgnization/reviews/118544627?t=mention&mt=doc&dt=sdk) 业务方已review 入库**实现子任务2**：根据存量历史代码分析学习，按照Easy新标准生成全新规则的Dao层封装代码，并自动实现新老对照，和编译检查：[https://console.cloud.baidu-int.com/comatestack/share/2993](https://console.cloud.baidu-int.com/comatestack/share/2993)代码库review：[评审：netdisk-infrastructure-18646 [Story] 【插入】easy项目重构](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/netdisk/nd-enorgnization/reviews/118557364/files/base...latest/easy/dao/overseas_info.go?t=mention&mt=doc&dt=sdk)![增量生成目标代码](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=615f1cb5d69f4e1c96b659df93f2a0fd&docGuid=-0XgDbIeQsi4aX "增量生成目标代码")![完成后给出代码清单review](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cbecc6bd891d4c96a80c4a81cbd37b5b&docGuid=-0XgDbIeQsi4aX "完成后给出代码清单review")**实现子任务3：**根据存量代码分析出API定义细节注册到easy平台中实现存量API重构设计部分的实现功能：[https://console.cloud.baidu-int.com/comatestack/share/2998](https://console.cloud.baidu-int.com/comatestack/share/2998)预览地址：[http://aswiki.baidu.com/preview?gid=1498&type=api&id=471](http://aswiki.baidu.com/preview?gid=1498&type=api&id=471)**规则内容：**[api重构规则](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/8Izmc57IYM/Z0PhmNnjN80iDV?t=mention&mt=doc&dt=doc)[DB注册规则](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/8Izmc57IYM/1NWKz3ikJLHlMu?t=mention&mt=doc&dt=doc)[新框架DB封装规则（参考easy）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/8Izmc57IYM/_BPZ4wxIwiQ1N1?t=mention&mt=doc&dt=doc)[老代码分析转新代码实现规则](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/8Izmc57IYM/3STUqcSHvxBCgo?t=mention&mt=doc&dt=doc)||
|baidu/netdisk/mcp-oriented-apis|go|杨祖豪|对接文库的 PPT 生成接口，将大模型的 sse 流模式的接口进行包装，提供给 toB 的开发者进行使用|[评审：netdisk-tob-19045 [Story] 【server】后端大纲生成 PPT 接口](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/netdisk/mcp-oriented-apis/reviews/118554228/files/base...latest/.comate/mcp.json?t=mention&mt=doc&dt=sdk)[https://mcp-ai-agent-web-netdisk.now.baidu-int.com/](https://mcp-ai-agent-web-netdisk.now.baidu-int.com/)任务拆解：[https://console.cloud.baidu-int.com/comatestack/share/2942?token=bab5f3cb](https://console.cloud.baidu-int.com/comatestack/share/2942?token=bab5f3cb)执行过程步骤：[https://console.cloud.baidu-int.com/comatestack/share/2943?token=0722e31f](https://console.cloud.baidu-int.com/comatestack/share/2943?token=0722e31f)[https://console.cloud.baidu-int.com/comatestack/share/2944?token=02f0ec0c](https://console.cloud.baidu-int.com/comatestack/share/2944?token=02f0ec0c)[https://console.cloud.baidu-int.com/comatestack/share/2945?token=b6a7c7a5](https://console.cloud.baidu-int.com/comatestack/share/2945?token=b6a7c7a5)[https://console.cloud.baidu-int.com/comatestack/share/2946?token=1eef61f0](https://console.cloud.baidu-int.com/comatestack/share/2946?token=1eef61f0)[https://console.cloud.baidu-int.com/comatestack/share/2947?token=8532589c](https://console.cloud.baidu-int.com/comatestack/share/2947?token=8532589c)||
|baidu/netdisk/nd-cloud-print|go|李勇|对项目中所有开启异步协程，但未捕获panic的代码进行重构，提升服务稳定性和可观测性。|[评审：netdisk-commercialization-20483 修复协程未捕获panic的问题](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/netdisk/nd-cloud-print/reviews/118563159/files/base...latest/.comate/rules/async-code.mdr?t=mention&mt=doc&dt=sdk)rules：见CR执行过程：[https://console.cloud.baidu-int.com/comatestack/share/2997?token=fe32e1ad](https://console.cloud.baidu-int.com/comatestack/share/2997?token=fe32e1ad)||
|baidu/netdisk/vastplayer|cpp|张頔|对项目中的函数加入性能分析模块统计耗时|[https://console.cloud.baidu-int.com/comatestack/share/2996](https://console.cloud.baidu-int.com/comatestack/share/2996)||
|baidu/netdisk/netdiskScan|go|方泓树|分析现有项目中的耗时优化点，建议，以及耗时分析辅助|初步分析|这个文件中包含多个函数，分析这些函数的逻辑，整理调用链路，分析可能存在的耗时优化点|
||||||根据第一步的调用链路，对每个函数提出一些耗时优化点|
||||||按照刚才提出的优化点，预估可以节约多少耗时|
|||||尝试改写|按照刚才说的优化方案，实现优化代码|
||||||解决这里改写的语法错误问题|
|||||后续处理|在每个函数合适的地方添加耗时日志，辅助后续的耗时分析|
|baidu/netdisk/nest-offline-videoworker|go|张安娜|对项目中所有使用到视频源文件的地方，加上冷视频的判断逻辑。|[https://console.cloud.baidu-int.com/comatestack/share/2994?token=507a028e](https://console.cloud.baidu-int.com/comatestack/share/2994?token=507a028e)[评审：netdisk-onlines-5933 [Story] [robot] 使用rules兼容冷视频](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/netdisk/nest-offline-videoworker/reviews/118549628/files/base...latest/.comate/rules/tape-cold.mdr?t=mention&mt=doc&dt=sdk)||

[附件]
[附件]
### 项目开发任务拆解与执行计划生成
|步骤|规则|创建人|备注|
|-|-|-|-|
|任务拆解|你现在是一个 **项目结构分析与任务计划生成助手**，具备 **架构师 + 项目经理 + 工程实施专家** 三重视角。
你需要从整体项目结构与代码逻辑中，自动生成一份具备「可执行、可追踪、可交付」的任务拆解计划文档。

---

## 🎯 执行目标

请分析我提供的项目文件（含 `.go`, `.py`, `.vue`, `.json` 等），
并基于文件逻辑、目录结构、潜在依赖与当前开发阶段，**自动生成完整的《项目开发任务拆解计划》**。

输出内容**必须以 Markdown 表格形式保存到：**

```
docs/project_task_plan.md
```

---

## 🧠 输出结构与格式要求

### 一、项目目标（SMART 原则）

> 将当前阶段目标转化为可衡量、可验证的 SMART 目标。

| 目标编号 | 目标描述 | 衡量指标 | 验收标准 |
| ---- | ---- | ---- | ---- |

**要求：**

* 包含技术性与产品性目标（性能、稳定性、用户体验）。

---

### 二、核心模块分解（按 DDD + SOLID 架构）

> 以领域驱动思维拆解模块，体现职责边界与依赖关系。

| 模块 | 子模块 | 主要功能 | 技术栈 | 优先级 | 所属层级(Domain/Application/Data/Interface) |
| -- | --- | ---- | --- | --- | --------------------------------------- |

**规则：**

* 领域层负责策略、模型与业务规则；
* 应用层负责任务编排、接口流；
* 数据层负责缓存、配置、模型存取；
* 接口层负责 HTTP、SSE、RPC 等通信。

---

### 三、可执行任务清单（WBS粒度）

> 输出可直接分配的任务项，要求每项具备明确产出、依赖与验收标准。

| 任务编号 | 所属模块 | 任务描述 | 依赖 | 产出物 | 验收标准 | 预估工时(人天) | 优先级 | 状态 |
| ---- | ---- | ---- | -- | --- | ---- | -------- | --- | --- |

**执行规范：**

1. 每个任务的粒度应为 1~3 天内可交付；
2. 任务描述应为“动作 + 对象 + 目标”，如“实现大纲流式断点续传逻辑”；
3. 验收标准必须可度量（例如：“接口返回码=200，延迟<1s”）；
4. 对涉及架构或文档的任务，产出物需为 `.md`、`.go`、`.py` 等文件。

---

## ⚙️ 输出逻辑控制规则

1. **禁止输出模糊描述**（如“优化代码质量”），必须转化为明确行动；
2. **每个文件至少对应1~3个可执行任务项**；
3. 若发现模块缺失、接口依赖未定义、策略层与服务层耦合，请自动生成 `[待确认边界项]`；
4. 若文件逻辑具备上下游关系（如 theme → outline → ppt），需体现任务依赖链；
5. 输出最终内容时：

   ```
   docs/project_task_plan.md
   ```

   结构完整且 Markdown 渲染正常；
6. 输出风格符合项目经理文档标准：结构化、可执行、可追踪。

---

## 🚀 输出步骤（AI执行顺序）

1. **扫描目录与文件命名模式**，识别模块类型；
2. **推断逻辑依赖与数据流向**（如主题 → 大纲 → PPT）；
3. **根据SOLID原则生成任务列表**；
4. **最终生成完整Markdown内容**并写入：

   ```
   docs/project_task_plan.md
   ```

---

## ✅ 输出质量标准

* 至少包含 ** > 5+ 可执行任务**；
* 每个任务均具备：产出物、依赖、验收标准；
* Markdown 格式正确，可直接渲染。|[@杨祖豪](https://ku.baidu-int.com?t=mention&mt=contact&id=na3pvqLt)||
|TodoList 执行|你现在是一个 **任务执行代理**，负责根据提供的任务清单逐条执行任务，并生成可运行的产出和状态更新。每次只处理 **一个任务编号**。

---

## 🧠 执行规则

1. **读取任务清单**

   * 从 `docs/project_task_plan.md` 中读取任务表格，表格包含字段：
     `任务编号 | 所属模块 | 任务描述 | 依赖 | 产出物 | 验收标准 | 预估工时(人天) | 优先级 | 状态`

2. **定位任务**

   * 根据用户提供的 **任务编号** 找到对应任务行。
   * 若任务状态为 `[x]`（已完成）或 `[skip]`（跳过），输出提示信息，并停止执行该任务。

3. **依赖检查**

   * 查看任务的 `依赖` 字段。
   * 若依赖任务未完成，提示依赖未满足，并将状态标记为 `[skip]`，不执行当前任务。

4. **任务分析与执行**

   * **分析目标**：明确任务要实现的功能和产出标准。
   * **执行逻辑**：

     * 若任务是生成代码：输出完整可运行代码，并附带注释和简单测试方法。
     * 若任务是文档或配置修改：输出具体修改内容和操作步骤。
     * 若任务是其他操作：提供可复现的执行流程和示例。
   * **产出结果**：确保结构清晰，可直接使用或复制。
   * **状态更新**：

     * `[x]` 完成：任务成功执行且产出有效。
     * `[fail]` 失败：执行中出现错误，附原因。
     * `[skip]` 跳过：依赖未满足或无需执行。

5. **输出格式（严格 JSON）**
   每次任务执行必须返回以下结构：

   - "任务编号": "T002",
   - "任务描述": "实现流式传输断线重连机制",
   - "依赖检查": "依赖任务T001已完成",
   - "执行过程": "逐步说明执行逻辑和分析",
   - "产出结果": "代码/文档/配置等可运行内容",
   - "状态更新": "[x]/[fail]/[skip]",
   - "备注": "必要时提供额外说明"

6. **安全与可靠性要求**

   * 所有生成的代码或配置必须可直接运行或验证。
   * 每次仅执行一个任务编号。
   * 对于依赖未满足或已完成的任务，明确标记 `[skip]` 并提示原因。|杨祖豪||

# 概念介绍
## 使用流程
Spec-Driven Development（SDD）是一种**以“规格说明书”而非“代码”作为开发过程核心资产**的软件方法论。

它把传统“先写代码再补文档”的流程完全颠倒：**先写一份可执行、可验证的规格（spec），再由 AI 或代码生成器把规格一次性地转换成实现、测试、文档与部署脚本**。

在 2024-2025 年，随着大模型与 Agent 工具的成熟，SDD 迅速从研究概念走向工程落地，被视为对“vibe coding（即兴提示词编程）”的一次制度化升级

### SDD 与“vibe coding”的系统性差异
|维度|Vibe Coding|Spec-Driven Development|
|-|-|-|
|输入|即兴 prompt|结构化规格 + 宪法|
|目标|快速原型|可维护、可验证的生产系统|
|验证|人工运行看结果|契约测试自动生成并跑通|
|可追溯|几乎为零|需求→规格→代码→部署全链路 ID|
|团队协同|难（上下文在私聊）|可评审、可分支、可合并的规格仓库|
|技术债|快速堆积|通过“重新生成”持续清零|

> 二者并非对立：可用 vibe coding 快速探索，再把稳定结论固化成 spec，进入 SDD 流程
### 企业级落地要点
1. **小步试点**选内部工具或边缘服务，先做到 Level 2“规格锚定”。
2. **把验收标准写进规格**性能预算、安全约束、合规条款都变成可执行断言，拒绝“口头标准”。
3. **Agent 编排**用 Spec Kit、AWS Kiro 等 agent 流水线，让“生成-测试-静态分析-部署”无人值守。
4. **双向反馈**线上异常与用户反馈自动提炼成规格修正案，进入下一迭代。
5. **治理与审计**规格仓库即审计证据：谁改了哪条需求、何时生成、何时部署，一键回溯。

---

### 一句话总结
> **Spec-Driven Development 让“写规格”成为工程师的核心工作，而“写代码”交给 AI 编译器；**
> 它把软件工程从“手工雕琢代码”提升到“高层意图驱动 + 自动化生成 + 持续验证”的新抽象层次——
> 这是自高级语言取代汇编之后，软件开发范式的又一次跃迁
## 相关资料
[easyship 总控指令设计文档 v.1.0](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/8MCddZCpuH/SX81HQH0s5/sS7NyZp8ktsc9w?t=mention&mt=doc&dt=doc)

[Easy项目规则](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/8MCddZCpuH/k73vwkNTP1/COh6K3_62G43if?t=mention&mt=doc&dt=doc)

[网盘AI Coding实战工坊](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/Iss3jiglGG/zf7rq2G1GdJCwf?t=mention&mt=doc&dt=doc)

[https://github.com/888888888881/spec-kit-chinese](https://github.com/888888888881/spec-kit-chinese)

[https://github.com/github/spec-kit/tree/main](https://github.com/github/spec-kit/tree/main)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
