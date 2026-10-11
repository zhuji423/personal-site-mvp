---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "基于Comate/DuCC端到端Coding能力探索"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\基于ComateDuCC端到端Coding能力探索.md"
---
基于Comate/DuCC端到端Coding能力探索

#### 🧑‍🏫 案例作者：[@杨桐](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Claude、Comate、Ducc
#### 📒 案例概要：探索AI编程助手在软件开发全生命周期的端到端智能化提效，包括七大阶段、能力扩展与Harness工程系统。
## 概述
随着 AI 编程助手（如 ClaudeCode、Cursor等）能力的快速发展，正在探索如何将 AI Coding 能力**系统性地融入软件开发全生命周期**，从需求分析到开发落地实现面向项目的端到端的智能化提效。



```
┌─────────────────────────────────────────────────────────────┐
│                    端到端 AI Coding 愿景                      │
├─────────────────────────────────────────────────────────────┤
│  🎯 提升研发效率：减少重复性工作，加速开发交付周期              │
│  🎯 保障代码质量：通过 AI 辅助测试、Review，提升代码健壮性      │
│  🎯 降低上手门槛：新人快速理解代码，缩短学习曲线                │
│  🎯 沉淀最佳实践：形成可复用的脚手架、Rules、工作流             │
└─────────────────────────────────────────────────────────────┘
```


基于软件开发的 **7 大核心阶段**，逐步探索 AI 能力的落地场景：

```
需求分析 → 系统设计 → 编码实现 → 软件测试 → 部署上线 → 运行维护 → 运营分析
   │          │          │          │          │          │          │
   ▼          ▼          ▼          ▼          ▼          ▼          ▼
 Spec文档   Design文档  Task拆解   单测/E2E   流水线     重构优化   数据分析
 需求定义   架构设计    代码实现   覆盖率     自动化     日志监控   脚本生成
   └──────────────┬──────────────┘
                  │
           Spec 闭环
```


## 端到端试点
|**阶段名称**|**目标**|**试点内容**|
|-|-|-|
|**需求分析**​|与客户或利益相关者深入沟通，明确软件需要实现的功能、性能要求及约束条件，并形成规范的需求文档。|明确的功能feature需求  ⭐ 成熟通过spec模式，可以从Spec → Design → Task → Code开发完整闭环。最好feature可以先人工判断拆解到一些小的功能迭代，避免一次性输入太多需求。多轮交互，在doc需求阶段可以多轮review，导出到知识库组内review和修改![细粒度的功能feature，可以和需求卡片对应](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=660a9a7ba9b64013979bd34d7e98e3af&docGuid=RN5VmdE8AR-g7r "细粒度的功能feature，可以和需求卡片对应")![需求&设计文档](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aedb650c09fe46068f9c8c1d47ba2285&docGuid=oIiEDXSgAca3op "需求&设计文档")模块开发0到1 ✅ 已开展围绕项目和编程语言构建一套工程脚手架+项目rules，并给出一些示例开发环境的快速标准化构建(语言版本、库版本等)![代码规约、版本要求等规则](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cfcb898426434502a9e0bca0d59e1252&docGuid=RN5VmdE8AR-g7r "代码规约、版本要求等规则")脚手架沉淀迭代从传统后端脚手架升级到ai能力的脚手架，可复用[https://github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)前端开发（面向后端同学）  ✅ 已开展后端同学需求提前准备下前端基础知识（环境工具、组件库、typescript、react等基础概念）产品&前端同学定义前端工程、设计规范等要求后端可以根据需求和规约针对需求快速上手一些功能开发和调试![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c8bb3b44cc13470f9e0a2c011acc01dc&docGuid=oIiEDXSgAca3op "")|
|**系统设计**​|根据需求文档，设计软件的总体架构、数据库结构、模块划分及接口等，分为概要设计和详细设计，为编码打下蓝图。||
|**编码实现**​|开发人员根据设计文档，选择合适的编程语言和工具，编写出可实现软件功能的实际代码。||
|**软件测试**​|通过单元测试、集成测试、系统测试等多种方法，尽可能发现并修复代码中的缺陷，确保软件质量。|单测覆盖率提升   ✅ 已开展首先rules中需要明确下单测覆盖率要求，比如增量代码覆盖率超过80%，但召回率比较低，还需要进一步优化。单测的编码分隔和用的库，测试用例风格，mock规则，可以rules中明确存量代码可以逐步让ai补充下单测覆盖率功能测试⏳ **未开展**e2e测试⏳ **未开展**|
|**部署上线**​|将测试通过的软件部署到生产环境（如应用服务器、应用商店），使用户可以正式访问和使用。|部署流水线⏳ **未开展**，计划尝试基于Skills+厂内一些MCP服务走通一些场景|
|**运行维护**​|软件上线后最长的阶段，包括修复发现的错误、更新功能以适应新需求、提升性能等，以延长软件生命周期|部分模块的重构优化 ⭐ 成熟快速对齐代码中日志一些格式，风格存量代码中部分逻辑重构，函数拆分，精简，错误修正线上问题分析定位，结合日志+代码快速定位根因![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9a44de8800d6495889481d5c9431aeec&docGuid=oIiEDXSgAca3op "")存量功能优化，例如连接池模块优化，支持动态调整连接池参数等功能![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9e123ebd25b84faa97db409505b74555&docGuid=RN5VmdE8AR-g7r "")![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=493658d22b7b4b6d8a7e8d4945675cd3&docGuid=RN5VmdE8AR-g7r "")代码内部的日志/监控指标补充![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cb00b25f479e4851bac1d0b523e2a7ea&docGuid=RN5VmdE8AR-g7r "")采到的坑，最好明确下使用的库和版本，否则这部分调试会比较麻烦，甚至可能ai会自己造轮子![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c24029e4ae804b9685522dac867538da&docGuid=RN5VmdE8AR-g7r "")命令行/sdk工具等自动生成  ⭐️ [dcos-authz-cli试点 - 杨桐](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/jPVgeifnCf/FNNiSIA8nW/5bdDUGm1EI0Kgq?t=mention&mt=doc&dt=doc)代码业务串讲辅助deepwiki+代码可以生成新人串讲模板，并可以提炼出一些核心问题和学习计划![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e8c7e15767194dcc990d255fb2dfcbb6&docGuid=RN5VmdE8AR-g7r "")代码review辅助多模型直接互相review，Ducc和Zulu互相针对新的commit 互相review代码change内容比较多，不好直接理解改动意图，会用上面的评审按钮，总结下改动内容![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bbd409fe2c574496b1edc696583ee38e&docGuid=RN5VmdE8AR-g7r "")|



## 能力扩展
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=33e842db67ef4a9a897e2264401d409e&docGuid=oIiEDXSgAca3op "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=971a1d7c149f42bc93907b6d0cef86fe&docGuid=oIiEDXSgAca3op "")


|能力|用途|
|-|-|
|rules 规则|**核心定义**：约束 AI Agent 行为的**硬性准则 / 逻辑规范**，包括执行条件、禁忌操作、优先级、流程规范等，是 Agent“该怎么干 / 不能干什么” 的依据。**核心用途**：保障 Agent 行为的合规性、稳定性和目标一致性，避免无效 / 错误操作（如 “调用工具前必须校验参数”“优先使用本地缓存而非远程请求”“禁止泄露隐私数据”）。**关联**：规则会限定**技能**的使用方式，也会指导**记忆**的存储 / 读取逻辑（如 “超过 7 天的临时记忆自动清理”）。|
|skills 技能|**核心定义**：AI Agent 完成**单一具体操作**的模块化能力，是构成 “综合能力” 的最小可复用单元，体现 Agent “具体会什么操作”。**核心用途**：实现任务的拆解与落地，让 Agent 能通过组合不同技能完成复杂任务（如 “文本解析技能”“Python 代码执行技能”“API 调用技能”“数据可视化技能”），支持技能的独立开发、迭代与复用。**关联**：多个技能组合形成**能力**，技能的执行流程受**规则**约束，技能的执行结果可存入**记忆**。|
|subagents 子代理|**核心定义**：由主 Agent 调度、具备**专项能力 / 技能**的次级 AI Agent，是主 Agent 的 “分身”，专注于处理某一类细分任务，无全局决策权限。**核心用途**：实现主 Agent 的**任务拆解与分布式执行**，提升复杂任务的处理效率和专业性（如主 Agent 负责 “数据分析项目统筹”，子代理分别负责 “数据采集”“数据清洗”“图表生成”）；降低主 Agent 的逻辑复杂度。**关联**：子代理的能力 / 技能由主 Agent 定义，子代理的行为受主 Agent 制定的**规则**约束，子代理的执行结果可同步至主 Agent 的**记忆**，主 Agent 通过**MCP**与子代理交互。|
|mcp 模型上下文协议|**核心定义**：AI Agent（主 / 子）之间、Agent 与外部工具 / 系统之间进行**上下文信息交互的标准化协议**，定义了信息的格式、传输方式、交互流程、上下文关联规则等。**核心用途**：解决 Agent 之间 / Agent 与工具间的**上下文割裂问题**，保障信息传递的准确性和一致性（如子代理向主 Agent 反馈任务结果时，通过 MCP 携带任务上下文、执行步骤、中间数据）；实现 Agent 与外部系统的无缝对接，提升兼容性。**核心设计要点**：通常包含**上下文标识、数据格式、交互指令、错误反馈、上下文生命周期**等模块。**关联**：是主 Agent 与**子代理**、Agent 与外部工具的 “通信语言”，协议中会嵌入**规则**（如信息传输的加密规则、上下文过期规则），协议传输的核心数据包括**记忆**片段和**技能**执行结果。|
|memory 记忆|**核心定义**：AI Agent 存储的**历史信息与状态数据**，是 Agent 具备 “持续学习” 和 “上下文感知” 能力的核心，分为不同类型适配不同场景。**核心分类 & 用途**：**短期记忆（工作记忆）**：存储当前任务的**实时上下文**（如执行步骤、中间结果、用户即时指令），支撑任务的连续执行；**长期记忆**：存储跨任务的**通用信息**（如用户偏好、技能执行经验、规则更新记录），支撑 Agent 的持续学习和个性化服务；**情景记忆**：存储特定场景 / 任务的**完整记录**（如某次数据分析的全流程、用户的历史需求），支撑任务的复盘与复用。**关联**：**技能**的执行会产生记忆数据，**规则**会定义记忆的存储 / 读取 / 清理逻辑，**子代理**的执行结果会同步至主 Agent 的记忆，**MCP**负责记忆数据的标准化传输，记忆的积累会逐步强化 Agent 的**能力**。|
|hook 钩子|**核心定义**：AI Agent 执行全流程中**可插拔、无侵入的触发式逻辑节点**，基于预设**事件触发条件**（如技能执行前 / 后、记忆存储失败、子代理调度时）触发自定义操作，是 Agent 实现流程扩展、行为管控、异常处理的轻量型机制，不修改核心业务逻辑，仅对流程进行 “附加式” 增强。|



#### 业界参考
[https://skills.sh/](https://skills.sh/)

[https://github.com/obra/superpowers/blob/main/.claude-plugin/plugin.json](https://github.com/obra/superpowers/blob/main/.claude-plugin/plugin.json)

[https://github.com/affaan-m/everything-claude-code/blob/main/rules/golang/testing.md?plain=1](https://github.com/affaan-m/everything-claude-code/blob/main/rules/golang/testing.md?plain=1)



#### 当前用法
##### Rules 规则
```
.claude/rules/
├── api_documentation.md      # API接口文档管理规则
├── sql_management.md         # 数据库SQL管理规范
├── mock_generation.md        # Mock生成规范
├── code_coverage.md          # 代码覆盖率要求
├── start.md                  # 项目开发规则（Go语言规范）
├── common/                   # 通用规则
│   ├── coding-style.md       # 代码风格
│   ├── security.md           # 安全指南
│   └── testing.md            # 测试要求
└── golang/                   # Go语言规则
    ├── coding_style.md       # Go编码风格
    ├── hooks.md              # Go Hooks配置
    ├── patterns.md           # Go设计模式
    ├── security.md           # Go安全规范
    └── testing.md            # Go测试规范
```


|规则|核心要求|
|-|-|
|**API文档**|接口协议变更必须同步更新文档到`hack/api_doc/`|
|**SQL管理**|表结构变更需同时更新`hack/db/create_table.sql`和`hack/db/update/YYYYMMDD*.sql`|
|**Mock生成**|新增interface必须配置`//go:generate`注解生成mock|
|**代码覆盖率**|增量代码覆盖率必须大于40%（规则文档显示）或80%（skill要求）|
|**Go编码风格**|使用 gofmt/goimports，小接口，错误包装|



##### Skills 技能
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=07d4f8dda1354848ad003b541e9efc2a&docGuid=oIiEDXSgAca3op "")
|技能名|描述|文件位置|
|-|-|-|
|`coverage-check`|检查代码修改后的覆盖率，确保达到80%阈值|[.claude/skills/coverage-check/SKILL.md](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/skills/coverage-check/SKILL.md)|
|`brainstorming`|创意工作前的需求探索和设计验证|[.claude/skills/brainstorming/SKILL.md](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/skills/brainstorming/SKILL.md)|
|`api-doc-gen`|API文档自动生成（Python实现）|[.claude/skills/api-doc-gen/](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/skills/api-doc-gen/)|

* **coverage-check 技能能力**

```
/coverage-check           # 分析覆盖率报告
make test                  # 运行测试生成覆盖率
go tool cover -func=...    # 查看详细覆盖率
go tool cover -html=...    # 生成HTML报告
```


* **brainstorming 技能能力**

```
一次只问一个问题
首选多选题，减少开放式问题
提出2-3种方案并分析权衡
分段呈现设计（200-300字）
设计文档写入docs/plans/YYYY-MM-DD-<topic>-design.md
```


* **api-doc-gen 技能能力**

```
api-doc-gen 是一个基于 Python 的 API 文档自动生成工具，用于解析 Go Handler 文件中的 Swagger 注解，生成 Markdown 格式的接口文档。

文件结构

.claude/skills/api-doc-gen/
├── __init__.py
├── models.py           # 数据结构定义
├── parser.py           # Swagger注解解析器
├── model_parser.py     # Go结构体解析器
├── doc_generator.py   # Markdown文档生成器
├── templates/         # Jinja2模板目录
│   ├── api_doc.md.jinja2      # 接口文档模板
│   └── index.md.jinja2        # 索引页模板
└── README.md
```


##### Subagents 子代理
|代理ID|描述|工具权限|
|-|-|-|
|`test-coverage`|Go代码覆盖率提升专家，分析覆盖率报告、编写单元测试|Bash, Read, Write, Edit, Glob, Grep|
|`api-doc-gen`|API文档生成专家，解析Swagger注解生成Markdown|Bash, Read, Write, Glob, Grep, Edit|

* **test-coverage 子代理能力**
    * 解析`coverage.out`文件
    * 识别低于80%覆盖率的文件和函数
    * 编写表驱动测试
    * Mock外部依赖
    * 增量提升覆盖率

* **api-doc-gen 子代理能力**

```
python3 hack/scripts/api_doc_gen.py              # 生成所有文档
python3 hack/scripts/api_doc_gen.py --tag <名称>  # 生成指定Tags文档
python3 hack/scripts/api_doc_gen.py --stats     # 查看统计信息
```
---

##### MCP 模型上下文协议
|插件|状态|配置文件|
|-|-|-|
|`claude-mem@thedotmack`|✅ 已启用|[.claude/settings.json](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/settings.json)|



|功能|说明|
|-|-|
|`search`|跨会话记忆搜索，查找历史解决方案|
|`save_memory`|保存重要信息到持久化记忆库|
|`timeline`|获取特定记忆的上下文历史|
|`get_observations`|获取记忆的详细信息|



* 查询："我们之前是如何解决这个问题的？"
* 查询："上次是怎么实现X功能的？"
* 保存：重要的架构决策、解决方案、最佳实践



##### Memory 记忆
|技能|描述|
|-|-|
|`claude-mem:make-plan`|创建包含文档发现的实现计划|
|`claude-mem:do`|使用子代理执行计划|
|`claude-mem:mem-search`|搜索跨会话的持久化记忆数据库|



通过 `claude-mem@thedotmack` 插件实现持久化记忆，存储在外部记忆服务中。



##### Hook 钩子


|事件|触发条件|Hook脚本|说明|
|-|-|-|-|
|`SessionStart`|startup/resume/clear/compact|[session-start.sh](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/hooks/session-start.sh)|检查legacy skills目录，注入superpowers使用说明|
|`PostAction`|Edit/Write操作后|[post-action.sh](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/hooks/post-action.sh)|检测Go文件修改，提示覆盖率检查|
|`PostAction`|Edit/Write操作后|[api-doc-check.sh](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/hooks/api-doc-check.sh)|检测Handler文件修改，提示生成API文档|

* **check-coverage.sh 独立脚本**
    * 覆盖率阈值：80%
    * 支持修改文件覆盖率检查
    * 显示未覆盖代码行
    * 生成HTML报告




Hook输出格式

```
{
  "hookSpecificOutput": {
    "hookEventName": "PostAction",
    "additionalContext": "<coverage-reminder>...</coverage-reminder>"
  }
}
```
---

##### 配置文件
|文件|作用|
|-|-|
|[.claude/settings.json](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/settings.json)|MCP插件启用配置|
|[.claude/settings.local.json](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/settings.local.json)|权限配置|
|[.claude/hooks/hooks.json](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/hooks/hooks.json)|Hook事件映射配置|
|[.claude/agents/agents.json](vscode-webview://0jululbul5s839lbbegicgsusdhm087meaeq31rnn38m9ck18qde/.claude/agents/agents.json)|子代理注册配置|

---

## 
## 26年-Harness Engineer
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=38a02681782c4349b2584240a7c30064&docGuid=oIiEDXSgAca3op "")
Harness 不是 Agent。它是管理 Agent 如何运行的软件系统。

|计算机概念|AI Agent 对应|
|-|-|
|CPU（原始处理能力）|LLM（模型推理能力）|
|RAM（有限工作记忆）|上下文窗口|
|操作系统|Harness|
|应用程序|Agent|



### 核心组件
|组件|职责|类比|
|-|-|-|
|工具集成层|通过标准协议连接外部 API、数据库、代码执行环境|设备驱动程序|
|内存与状态管理|多层记忆——工作上下文、会话状态、长期记忆|内存管理 + 文件系统|
|上下文工程|动态策划每次模型调用中出现的信息|进程调度器|
|规划与分解|引导模型通过结构化任务序列推进|任务调度器|
|验证与防护|格式校验、安全过滤、自我纠正循环|防火墙 + 权限系统|
|模块化与可扩展|可独立启用、禁用或替换的可插拔组件|内核模块|



* **上下文工程（Context Engineering）**

不再是写一个静态 prompt，而是设计动态的信息策划系统：什么信息在什么时候进入 Agent 的上下文窗口，什么信息该被剪裁掉，什么信息需要持久化到长期记忆。

* **约束设计（Constraint Design）**

为 Agent 设定清晰的行为边界：哪些操作可以自主执行，哪些需要人工审批，遇到歧义时的降级策略是什么，错误恢复的重试逻辑如何设计。

* **工具编排（Tool Orchestration）**

决定 Agent 可以使用哪些工具、以什么顺序使用、工具之间的数据如何流转。这包括 MCP 协议配置、自定义工具链搭建、子 Agent 委派策略。

* **规格治理（Spec Governance）**

维护从 constitution → spec → plan → tasks 的完整规格体系，确保规格与代码的一致性，建立规格的版本化和演化机制。

* **质量闭环（Quality Loop）**

设计验证链——不只是最终测试，而是在 Agent 执行的每一步都嵌入验证点：代码生成后的静态检查、API 契约的一致性校验、安全扫描、性能基线对比。



### 从 Vibe Coding 到 Spec Coding 的迁移
如果你今天还停留在 Vibe Coding 阶段，最小启动路径是：

1. **先用 Plan Mode**：在 Cursor 或 Claude Code 中养成「先 plan 后写」的习惯——这就是轻量版 SDD
2. **写第一份 spec**：挑一个中等复杂度的功能，按 spec → plan → tasks → implement 走一遍
3. **工具辅助**：用 Spec Kit（`specify init . --ai cursor-agent`）生成完整的 spec 目录结构
4. **迭代**：第一份 spec 一定是粗糙的，但修正一份 spec 远比修正一坨乱码容易

### 从 Spec Coding 到 Harness Engineer 的迁移
当你的 Spec Coding 流程稳定后，开始构建 Harness：

1. **Constitution 先行**：为项目建立「宪法」—— 质量标准、测试要求、安全底线、架构原则
2. **Rule 体系**：用 `.cursor/rules/` 或 `CLAUDE.md` 定义 Agent 行为约束
3. **Skills 注入**：把团队的领域知识封装成可复用的 Skills
4. **MCP 打通**：通过 MCP 协议连接团队的内部工具、API、数据库
5. **验证链路**：在每个关键节点嵌入自动化验证——不是事后补测试，而是构建在流程中



## **参考材料**
[Comate 插件端 （厂内）官方文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/mcV1ZM02Cz/prNS4F6K_KH9eg?t=mention&mt=doc&dt=doc)



[https://openai.com/zh-Hans-CN/index/harness-engineering/](https://openai.com/zh-Hans-CN/index/harness-engineering/)

[https://www.zhihu.com/question/2016648624256340425/answer/2018446438896522524](https://www.zhihu.com/question/2016648624256340425/answer/2018446438896522524)



qoder:

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c4800ff849a04ca38bc0a8c6519c507a&docGuid=oIiEDXSgAca3op "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=69d0cc9804b14e93a317962baef1867f&docGuid=oIiEDXSgAca3op "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=add7aa23ad624b279ecfc159fa835500&docGuid=oIiEDXSgAca3op "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0209e35f620f4e26a00e141233f1de50&docGuid=oIiEDXSgAca3op "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=42d2e102345144608ae86f32d1796b98&docGuid=oIiEDXSgAca3op "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
