---
title: "一、AI Coding 的底层共同原理"
description: "从工具到工程：AI Coding 的方法论与实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\从工具到工程：AI Coding 的方法论与实践.md"
---
从工具到工程：AI Coding 的方法论与实践

#### 🧑‍🏫 案例作者：[@黄玲](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Onetool、Ducc
#### 📒 案例概要：从AI Coding工具的底层原理引申至通用AI Coding实践中会遇到的常见问题。通过在onetool发布mcp的实践引入个人能力到工程能力的升级重要性
观察：大家都在用，但体验差异巨大。越是复杂的项目，AI Coding 的稳定性越差。

思考：不是模型问题，是工程问题。

# 一、AI Coding 的底层共同原理
## 以 Claude Code 与 Cursor 为例
在讨论 AI Coding 工具时，很多人关注的是 **工具能力差异**，例如：

* Cursor 是否更适合写代码
* Claude Code 是否更适合工程任务

但如果从底层看，这些工具其实遵循 **同一套核心原理**。理解这些原理，可以帮助我们：

1. 更好地使用不同 AI Coding 工具
2. 设计自己的 AI Coding Workflow
3. 将 AI Coding 从个人能力升级为工程能力

---

# 二、AI Coding 的本质
AI Coding 的本质并不是AI 写代码，而是AI 在上下文中进行推理并执行任务

因此 AI Coding 的基本公式可以表示为：

**AI Coding = LLM + Context + Tools**

|三层能力|作用||
|-|-|-|
|LLM|语言模型能力|编程语言知识框架知识算法能力软件工程知识|
|Context|项目知识与任务信息|AI 必须理解代码库才能写正确代码。Context来源包括：代码、文档、需求、架构典型 Context 包括：当前文件调用链项目架构需求文档|
|Tools|执行能力（读代码 / 修改代码 / 执行命令）|读取文件修改代码执行shell运行测试|

无论是 **Claude Code** 还是 **Cursor**，底层都遵循这个模型。这三层能力决定了 AI Coding 工具的上限。

||Cursor|Claude Code|
|-|-|-|
|Context|Cursor 主要依赖：代码索引、embedding、语义搜索工作方式：对代码库建立索引通过语义搜索找到相关代码将相关代码提供给模型优点：检索速度快适合局部代码修改缺点：对复杂工程理解有限|Claude Code 更偏向 **动态探索代码库**：tree、grep、read fileAI 会主动：查看项目结构搜索相关代码阅读关键文件优点：更适合理解复杂工程可以处理跨模块修改|
|Tool 执行|IDE编辑代码|命令行执行shell命令、测试、代码修改这也是为什么 Claude Code 可以完成 **完整工程任务**。|



---

# 三、AI Coding 实践过程中常见且重要的几类问题
## 1、context管理
### 1.1 技术挑战
如何在有限的 Token 预算内，给 AI 提供最相关的信息？  

如果 context 管理不好，会导致 AI Coding 从“高效协作”变成“随机生成”。

### 1.2 实践中遇到过的问题
在复杂工程需求下用ducc实现需求，没有进行context管理，最终可能出现的问题：

/compact 保留plan中的所有核心实现与所有上报详细分类信息                                                                                        

  ⎿  Error: Error during compaction: Error: API Error: The model has reached its context window limit.

**问题：**

* 当前上下文已经接近最大长度
* 压缩本身需要再消耗 token
* 结果“还没压缩就爆了”
* 此时几乎没有办法在当前session进行操作

**解决：**

|解决方案||
|-|-|
|方案一|直接开新 session：退出当前 Claude Code --> 重新进入 --> `/init` --> 手动粘贴当前 plan 核心内容优点：100% 解决不再有 context 历史污染缺点：需要你自己决定哪些是“核心”|
|方案二|减少压缩目标原始命令：/compact 保留plan中的所有核心实现与所有上报详细分类信息 改成：/compact 只保留 plan最终结构、上报分类最终版本结果：最简单的/compact 仍然无法执行。|
|方案三工程级建议（长期）|1、每完成一个阶段，都执行：请总结当前阶段核心决策，限制在 xxx token。删除前面大段推理。2、skills进行context管理3、Plan 不应该只存在对话里。正确做法是：docs/  
    architecture.md  
    plan.md  
    test_spec.md Claude 只负责 读文件、更新文件、修改文件，不要让“唯一版本”存在于会话上下文。|



### 1.3 最常见的 Context 问题
|问题|现象|case|
|-|-|-|
|Context 膨胀爆炸（Context Explosion）|随着对话持续：对话历史不断增长代码片段越来越多日志越来越多推理过程越来越长最终出现：context window limit或者：AI 回答越来越慢AI 开始遗忘关键信息`/compact` 失败|AI Coding 的典型模式是：需求→ 设计→ 代码→ 调试→ 修改→ 再调试每一步都在 **累积上下文**。但很多内容其实是：中间推理过期代码已解决问题却仍然留在 context 里。|
|Context 压缩不精准|即使做了压缩（compact / summarize），也可能出现：**重要信息被删****次要信息被保留**|例如，压缩后留下：我们讨论了并发问题但丢失：线程上限 15批量 size = 100写文件必须单线程这会导致 AI：重新设计或产生错误假设|
|Context 目标/语义不清晰|context 很多，但 **目标不明确**。|例如：这里是代码A这里是日志这里是测试这里是之前讨论但没有明确：当前目标：修复 CSV 并发写冲突结果 AI 会：Spelunking（到处找）Synthesizing（尝试整合）最后 Honking（长篇解释）但不解决问题。|



### 1.4 Context 管理的几类工程解决方案
||||
|-|-|-|
|编码过程中的 Compact 意识|**Compact 不是命令，而是一种工作习惯。**核心原则：不要等 context 爆炸再压缩。而是 **持续做信息提纯**。每完成一个阶段：需求阶段 → 总结需求设计阶段 → 总结架构实现阶段 → 总结关键实现例如：请总结当前阶段核心决策，限制在xxx tokens：- 并发模型- IO策略- 数据结构这样可以：删除大量中间推理保留真正关键的信息|保留：最终设计关键约束接口定义未解决问题删除：推理过程试错代码已解决 bug|
|成熟 AI Coding 流程（推荐）|一个成熟的流程通常是：1 需求定义 2 架构设计 3 Plan生成 4 分阶段实现 5 每阶段compact 6 更新文档其中**Plan / Docs 是长期 context，**而不是 **聊天记录是 context**||



### 1.5 核心结论
如果 context 信息密度高、结构清晰、持续压缩，即使模型一般，也能稳定工作。

反之，即使最强模型，也会出现 胡乱修改、重复推理、context 爆炸。

---

## 2、渐进式披露
在 **AI Coding** 实践中，**渐进式披露（Progressive Disclosure）** 是一条非常重要的工程原则。它的核心思想是：

> **不要一次性把所有信息丢给 AI，而是按照任务推进的阶段，逐步提供最相关的信息。**
一个常见错误是：一次性提供大量信息

```
这里是整个需求说明
这里是完整架构设计
这里是几十个代码文件
这里是日志
这里是测试
请帮我修改 bug
```
问题：

* Context 信噪比下降
* 推理目标变模糊
* Context Window 被快速消耗



我们应当每一步只提供解决当前问题所需要的最小信息集合，在任务推进中逐步增加信息。渐进式披露可以概括为一句话：

> **让 AI 在“逐步展开的上下文”中工作，而不是在“信息洪流”中寻找答案。**
在 AI Coding 中，这一原则可以显著：

* 保持 Context 清晰
* 降低推理发散
* 提高 AI 输出稳定性
* 延长可用的 context window

---

# 四、将 AI Coding 从个人能力升级为工程能力
## 可复用资产 ：rules&skills&mcp
|资产类型|解决问题|本质||
|-|-|-|-|
|Rules|约束 AI 行为|规范|Rules（规则）是最基础的资产。目标是让 AI **在工程边界内工作**。它的作用是：**给 AI 设定明确的工程约束**。如果没有规则，AI Coding 往往会出现：随意修改架构生成不符合团队规范的代码引入不必要的依赖修改无关模块|
|Skills|固化能力|方法|Skills（技能）是把“优秀 prompt 或工作流程沉淀为模板。很多工程师在使用 AI 时，效率高低差别很大，本质原因是：是否掌握有效的 prompt 方法。Skills 的作用就是**把这些方法变成团队资产。**|
|MCP|扩展能力边界|工具|**MCP（Model Context Protocol）** 是一种让 AI 调用外部系统能力的机制。它可以理解为：**AI 的插件系统**通过 MCP，AI 可以直接访问：数据库日志系统代码库API这样 AI 就不仅仅是“聊天工具”，而是可以真正参与工程流程。|

## 
## mcp实践
平台：[https://console.cloud.baidu-int.com/onetool/square](https://console.cloud.baidu-int.com/onetool/square)

### 1、table便捷查询工具-zulu可用
#### 背景
在生命周期管理项目中，调试测试时有查询table行为。项目内部已实现适配该项目单独查询table的工具。但如果非该项目，且想快速进行table查询，就需要写脚本调用api等方案，重复实现查询行为。在mcp市场搜索当前没有table查询相关的mcp，因此调研后用**最小成本实现一个MCP并发布到广场。**

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### OneTool创建MCP的三种模式
其中脚本转换MCP可以作为实现table测试查询的最小成本实现

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 需要提供的信息
* 基本信息--全局变量
* 工具配置--工具定义参数、脚本
    * 脚本中的必需的参数都可以从全局变量以及工具参数中作为变量获得
    * 本地验证完毕后，可在个人空间发布后，订阅测试使用


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 创建zulu订阅mcp演示
* 接入：可以手动配置后把config填入本地，写上对应参数。
* 脚本MCP订阅依赖：npx（代码空间打开一般都能直接用）
    * 本机通过`npx`启动`mcp-script-runner`
    * runner读取本地配置中的`env`
    * 将这些env作为**HTTP头**或**gRPC元数据**附加到请求中
    * 远程MCP服务校验`MCP_USER/PASSWORD`等参数


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 使用详情
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 问题：在物理机或开发机环境（非代码空间），没有npx的命令情况下，无法使用该mcp
![](/personal-site-mvp/img/doc-placeholder.svg "")
为什么一定需要npx？npx的作用是什么？

* 从配置中观察参数，实质是用npx命令在本地起了一个mcp server 进程（对用户无感知）

**1. 拉包（如果本地没有）：**-y 参数表示自动确认安装，npx 会从 npm registry 下载  @baidu/mcp-script-runner 到 /root/.npm/_npx/ 缓存目录

     ** 2. 起进程：**下载完成后，执行包的 bin 入口（即 output/app.js），传入 --serverName table-query-tool-v1 参数

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 详细分析@baidu/mcp-script-runner包内容
    * 创建 MCP Server 实例


```
const server = new Server({      name: "script-runner-server",
      name: "script-runner-server",
      version: "1.0.0"
  }, {
      capabilities: { tools: { listChanged: true } }
  }); // 声明支持 tools.listChanged，即工具列表可动态变更（配合 30 秒轮询配置更新）。
```
    * 注册两个请求处理器
        * ListTools — 列出所有可用工具：
            * 遍历全局配置 appConfGlobal.servers[].tools[]
            * 将每个工具的 toolView（name、description、inputSchema）返回给客户端

        * CallTool — 执行工具调用：
            * 根据工具名查找配置（getToolConfigByName）
            * 合并两类参数为环境变量：
            * serverParams — 服务端参数（如 MCP_USER、MCP_PASSWORD，来自远端配置）
            * arguments — 客户端传入的调用参数
            * 调用 runScriptContent(type, content, envs) 执行脚本
            * 用 truncateByPrefix 截取输出前缀之后的内容
            * 根据退出码 code !== 0 判断是否出错


    * startServer() — 启动服务

```
  function startServer() {
      const transport = new StdioServerTransport();
      server.connect(transport);
  } //创建 stdio 传输层，通过标准输入/输出与客户端通信。
```


**总结：**公司提供的脚本转mcp，可以专注实现工具逻辑，不用单独关心mcp server的创建。

---

## skills实践
没有npx，不用mcp可以吗？

* 可以写一个skill，也可以替代这个功能。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
* ducc 安装

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 测试使用
    * 第一次使用时需在对话中指定配置、下次对话时默认使用上次配置，可修改。
    * 配置填写不完整会提示
    * 提供表名、rowkey查询即可


![第一次使用时需在对话中指定配置](/personal-site-mvp/img/doc-placeholder.svg "第一次使用时需在对话中指定配置")
![配置填写不完整会提示](/personal-site-mvp/img/doc-placeholder.svg "配置填写不完整会提示")
![查询即可](/personal-site-mvp/img/doc-placeholder.svg "查询即可")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
