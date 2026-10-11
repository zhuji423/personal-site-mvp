---
title: "目录概览"
description: "电商Claude Code使用经验"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\电商Claude Code使用经验.md"
---
电商Claude Code使用经验

#### 🧑‍🏫 案例作者：[@刘棪](https://ku.baidu-int.com?t=mention&mt=contact&id=d847a650-fce5-11f0-978a-0562e20eae48)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate，Ducc
#### 📒 案例概要：本文分享了电商领域中Claude Code的应用经验，从提示词工程到上下文工程的转变，介绍了Claude Code的核心理念和实践案例。通过Projects、Skills、Subagent和MCP四大构件实现智能体开发生态，支持高内聚、低耦合的开发模式。详细展示了如何通过Claude Code实现一个html2video的MCP Server项目，包括技术栈、功能特性及项目结构，体现了上下文工程在提升开发效率和代码质量上的重要作用。
**本文档视频讲解：**[电商Claude Code使用经验](http://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56815?activityId=8747?t=mention&mt=doc&dt=sdk)

#### 对于开发者
* 从提示词工程到上下文工程应用
* 开发者编程模式的变化，管理指导多个AI实现

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 目录概览
1. 案例演示
2. Claude Code 理念
3. Claude Code 核心概念
4. 实践和经验总结

# 案例演示
**需求**：实现一个 html2video 的 MCP Server

[附件]
上面示例是一个完全通过决策指导AI 0手写代码实现的

## AI 生成语法正确但逻辑错误？缺少宏观架构理解？输出的不可预测性....
### **“看似正确”的幻觉与隐藏错误**
### **上下文理解有限与“短视”**


⬇️

早期的大模型应用严重依赖于冗长且精巧的提示词（Prompt）。然而，提示词本质上是**短暂、会话化且高度耦合于单一上下文**的。这种模式在企业级应用中暴露出诸多瓶颈：知识无法沉淀、流程无法复用、安全边界模糊、系统难以迭代和维护。

### 范式转移：从提示词工程到智能体系统工程
### 提示词工程 ➡️ 上下文工程
Claude 推出一套层次分明、职责单一的构件，成功地实现了范式转移：

* Projects：提供持久化的项目上下文与环境
* Skills：封装可复用的领域知识与操作流程
* Subagent：实现任务的专精化分解与安全执行
* MCP：打通外部工具与数据源的标准化通道

这四大构件共同构成了一个支持高内聚、低耦合的智能体开发生态。



> 上下文工程：[https://arxiv.org/abs/2510.26493](https://arxiv.org/abs/2510.26493)
# Claude 理念
Anthropic 采用的是经典的**编排者-工作者（Orchestrator-Worker）模式**：

![](/personal-site-mvp/img/doc-placeholder.svg "")
上图完整展示了其工作流程。当用户提交一个查询时，系统的工作流如下：

1. **启动与规划：**系统创建一个**主研究员智能体 (Lead Researcher)**。它首先思考并制定一个研究计划，并将这个计划**保存到记忆 (Memory)**中。这是至关重要的一步，因为它确保了在长流程任务中，即使上下文窗口被截断，核心目标和计划也不会丢失。
2. **委派与并行：**主智能体根据计划，创建多个**专门的子智能体 (Subagents)**，并为每个子智能体分配具体的、独立的子任务。（在图中，创建了两个 sub-agents）
3. **执行与评估 (引入“交错思考”)：**每个子智能体独立地执行任务（如网络搜索）。关键在于，它们使用**“交错思考” (Interleaved Thinking)**的技术。这意味着，在两次工具调用之间，Agent 会插入一个“思考步骤”，用于评估上一步工具返回的结果质量，识别信息差距，并迭代优化自己的下一步行动。
4. **综合与决策：**子智能体将它们的发现返回给主智能体（**压缩**）。主智能体**综合这些结果**，并判断是否需要进一步的研究。如果需要，它可以创建更多的子智能体或调整策略。
5. **引用与输出：**一旦收集到足够的信息，系统会调用一个专门的**引用智能体 (CitationAgent)**，它负责处理所有文档和研究报告，确保所有声明都有据可查。最终，一份带有精确引用的完整研究结果将返回给用户。

# ⬇️
![](/personal-site-mvp/img/doc-placeholder.svg "")
可以想象成对话窗口是主 Agent 的调度窗口，他会根据任务的思考和执行，调用 subagents 以及 skills、mcp、plugins等

# Claude 核心概念：缩小上下文、指导LLM降低生成幻觉
### 记忆
###### 技术本质
CLAUDE.md（项目记忆）：是项目的“大脑”。在该文件中定义项目架构、代码规范、测试命令等。Claude 会在每次会话开始时读取此文件，确保上下文一致性。注意：手动精简这个文件，只保留关键指令。加载机制：Claude 从当前工作目录开始，向上递归查找 CLAUDE.md 直至根目录。

###### 实战演练
```
# HTML to Video MCP Service

## 概述
这是一个通过 MCP 提供网页转视频服务的 Node.js 项目。此 MCP 服务可以将任何 HTML 网页地址转换为视频文件，支持多种格式和质量设置。基于 MCP 协议设计，可与 Claude Desktop 等客户端无缝集成。

## 技术栈
- TypeScript
- Puppeteer - 网页截图和录制
- FFmpeg - 视频编码处理
- Next.js
- Zod - 参数校验
- Express.js - MCP服务端

## 功能特性
- ✅ 将 HTML URL 转换为视频 (MP4, WebM, GIF)
- ✅ 可自定义分辨率、时长、帧率
- ✅ 支持低、中、高三种质量预设
- ✅ 异步处理，支持状态查询
- ✅ 网页预览生成
- ✅ 自动清理旧文件
- ✅ 符合 MCP 协议规范

## 项目结构
```
/Users/liuyan29/claude-demo/
├── .claude/
│   ├── CLAUDE.md          # 项目说明文档
│   └── skills/             # 项目相关的技能定义
├── src/
│   ├── index.ts           # MCP服务端入口
│   ├── types/
│   │   └── index.ts       # TypeScript类型定义
│   └── utils/
│       ├── videoGenerator.ts   # 视频生成核心逻辑
│       └── videoProcessor.ts   # FFmpeg视频处理
├── package.json
├── tsconfig.json
└── README.md
```

## MCP 工具定义
### html2video.convert
将 HTML 网页转换为视频文件

**参数：**
- `url` (string, required): 目标网页URL
- `format` (string, optional): 输出格式，默认为 "mp4"，支持 "mp4", "webm", "gif"
- `duration` (number, optional): 视频时长（秒），默认为 30
- `frameRate` (number, optional): 帧率，默认为 30
- `width` (number, optional): 视频宽度，默认为 1280
- `height` (number, optional): 视频高度，默认为 720
- `quality` (string, optional): 质量设置，默认为 "medium"，支持 "low", "medium", "high"
- `outputPath` (string, optional): 输出文件路径

**返回：**
- `success` (boolean): 转换是否成功
- `message` (string): 处理结果消息
- `videoPath` (string): 生成的视频文件路径（成功时）
- `preview` (string): 网页预览图路径

### html2video.preview
生成网页预览截图

**参数：**
- `url` (string, required): 目标网页URL
- `width` (number, optional): 截图宽度，默认为 1280
- `height` (number, optional): 截图高度，默认为 720
- `outputPath` (string, optional): 输出文件路径

**返回：**
- `success` (boolean): 生成是否成功
- `message` (string): 处理结果消息
- `previewPath` (string): 预览图文件路径

### html2video.status
查询视频转换任务状态

**参数：**
- `jobId` (string, required): 任务ID（计划支持）

**返回：**
- `status` (string): 任务状态（pending, processing, completed, failed）

## 安装

### 本地安装
```bash
git clone <repository-url>
cd html-to-video-mcp
npm install
npm run build
```


### Agent Skills：动态技能
> [https://code.claude.com/docs/zh-CN/skills](https://code.claude.com/docs/zh-CN/skills)
给予文件操作权限 ，在特定任务下路由到 skills 通过脚本执行特定任务让结果更准确

###### 适用场景
组织工作流；个人常用流程；个人生产力工具；专业领域技能；需跨对话重复使用的专业操作。（例如，一个 mcp-builder Skill 可以指导 Claude 如何创建高质量的 MCP 服务器）；

###### 技术本质
Skills 是一个符合特定结构的文件包，其核心创新在于**分级暴露**机制。这不是简单地将长提示词打包，而是一种高效的上下文管理策略：

1. 元数据扫描：Claude 根据任务描述优先扫描所有 Skills 的 SKILL.md。

![](/personal-site-mvp/img/doc-placeholder.svg "")
2. 指令加载：仅当匹配成功后才加载详细的指令文档。

![](/personal-site-mvp/img/doc-placeholder.svg "")
3. 资源按需加载：内含的代码脚本或者数据文件只在具体操作需要时才被载入。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


###### 实战演练：实现一个 MCP builder 的 Skill
![](/personal-site-mvp/img/doc-placeholder.svg "")


### Subagent
> [https://code.claude.com/docs/zh-CN/sub-agents](https://code.claude.com/docs/zh-CN/sub-agents)
###### 技术本质
当有复杂任务无法通过单个 skill 完成，那么可以将专注的工作委托给配置了任务特定提示、工具和行为的 AI agents（即 Subagents）。Subagents 是 Claude Code 和 Agent SDK 中的高级功能，本质上是拥有独立系统提示词、专用上下文窗口和特定工具权限的微型智能体。**主智能体作为调度员，根据任务描述自动调度或由开发者显式调用最合适的 Subagents**。其核心价值是：

* 安全沙盒：通过工具权限控制实现“权责分离”。
* 专业分工：并行处理异构任务，提升效率与质量。
* 上下文隔离：防止专项任务的复杂上下文污染主会话。

###### 适合场景
专业任务分工（代码审查、测试生成）；上下文隔离（避免主对话杂乱）；并行处理；

###### 工作原理
1. **配置**：你创建 subagent 配置，定义其行为、工具和系统提示
2. **委派**：主 AI 可以自动将任务委派给合适的 subagents
3. **执行**：Subagents 独立工作，使用其配置的工具完成任务
4. **结果返回**：它们将结果和执行摘要返回到主对话中

###### 实战演练：实现一个 Code Reviewer 的 Subagent
![](/personal-site-mvp/img/doc-placeholder.svg "")
```
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is simple and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```


### MCP
> [https://code.claude.com/docs/zh-CN/mcp](https://code.claude.com/docs/zh-CN/mcp)
###### 技术本质
MCP 是一个开放标准，解决了智能体与外部环境连接的“最后一公里”问题。它采用 CS 模型：

* MCP Server：由数据或工具提供方实现，暴露统一的 API（如访问数据库等）
* MCP Client：只需实现一次MCP协议即可连接所有兼容的 Server

这避免了为每个数据源开发定制化连接器的重复劳动，实现了“一次集成，处处可用”。

###### 适合场景
访问外部数据；使用业务工具；连接开发环境

###### 实战演练：实现一个 html2video 的 MCP Server
# 实践和经验总结
基于 Comate、Ducc 工具实现一个html2video 的 MCP Server

相关文档：[Ducc（达克）使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/CMZnRdLpiznoht?t=mention&mt=doc&dt=doc)



#### 实践总结
[RIPER-5](https://forum.cursor.com/t/i-created-an-amazing-mode-called-riper-5-mode-fixes-claude-3-7-drastically/65516)模式：AI 编码行为协议，目标是通过一个强制性的、分阶段的流程来约束 AI 的行为，确保其在执行复杂编码任务时的每一步操作都**安全、可控且符合预期**。它将复杂的编码任务分解为五个明确定义且循序渐进的阶段：Research（研究）、Innovate（创新）、Plan（计划）、Execute（执行）和 Review（审查）。每个阶段都有其特定的目标、允许的行为和禁止的行为，以及明确的输出格式和转换条件。

||**❌不好的指令**|**✅好的指令**|
|-|-|-|
|明确指令|帮我修复这个 bug|src/components/Price.tsx 中的价格千位分割计算错误，请检查代码并修复问题|
|提供上下文|优化这段代码|这段代码是tab列表切换逻辑，目前性能较慢，请优化：[粘贴代码]|
|复杂任务分步执行|帮我实现用户表迁移脚本|第一步：分析当前的数据库结构第二步：设计新的用户表第三步：编写迁移脚本|

手动思维链：

    1. 在指令中加入“一步一步地思考”
    2. 构建引导式推理流程：在xxx操作前，首先xxxx，其次xxx，最后xxx
    3. 使用标签阐述推理过程：<thinking></thinking>

![](/personal-site-mvp/img/doc-placeholder.svg "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
