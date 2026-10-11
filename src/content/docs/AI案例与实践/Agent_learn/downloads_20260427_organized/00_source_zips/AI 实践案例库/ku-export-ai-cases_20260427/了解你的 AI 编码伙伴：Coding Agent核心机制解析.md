---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "了解你的 AI 编码伙伴：Coding Agent核心机制解析"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\了解你的 AI 编码伙伴：Coding Agent核心机制解析.md"
---
了解你的 AI 编码伙伴：Coding Agent核心机制解析

#### 🧑‍🏫 案例作者：[@孟小萱](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：知识加工
#### 🔧 使用工具：Comate、Claude
#### 📒 案例概要：本文基于开源项目源码研究与实践经验，系统性地拆解 Coding Agent 的工作原理。旨在帮助开发者在了解Coding Agent后，与AI伙伴更好的协作配合，更高效的提问和拿到有效结果。
> 笔名：无糖可乐
> 话题标签：“Coding Agent”、“AI编程”、“大模型应用”
> 一句话重点介绍：在了解Coding Agent 的核心工作机制后，与AI伙伴的协作更佳顺畅。
> 200字导读：AI 编码工具正在从"智能补全"演进为能自主完成复杂任务的 Coding Agent。本文基于开源项目源码研究与实践经验，系统性地拆解 Coding Agent 的工作原理。旨在帮助开发者在了解Coding Agent后，与AI伙伴更好的协作配合，更高效的提问和拿到有效结果。
## 背景
AI 编码工具的发展速度快得有点"离谱"。从开始使用 GitHub Copilot 的代码补全，到使用Claude Code、Cursor、Comate IDE等完成复杂编程任务，AI 不再只是个「智能补全工具」，它能读懂你的代码库、执行终端命令、甚至帮你调试问题，成为你的“编码伙伴”。

我自己在团队里推 AI 编码工具的时候，发现一个很有意思的现象：大家都在用，但很少有人真正理解它是怎么工作的。有人觉得它"很神奇"，有人吐槽它"经常乱来"，还有人担心"会不会把代码搞乱"。这些困惑的背后,其实都指向同一个问题：我们对这个"伙伴"还不够了解。

就像你不会无脑信任一个新来的同事一样，要和 AI 编码伙伴配合好，你得知道它的工作方式、能力边界、以及怎么"沟通"才更有效。

在经过多次的实践尝试后，我尝试探索它的底层原理，并写下了这篇文章记录，主要围绕了这些内容展开：

* Coding Agent 的核心工作机制，包括身份定义、工具调用、环境感知等基础组成。
* 从零实现一个最小化 Coding Agent 的完整过程，以建立对 Agent 工作流程的直观理解。
* 上下文管理、成本控制、冲突管控等生产环境中的关键技术问题及其解决方案。
* Rule、MCP、Skill 等能力扩展机制的原理与应用场景。

在了解原理后，我和伙伴的协作更佳顺畅，让伙伴更清晰的了解我的意图，我拿到有效的回答。

## 概念
### 从Workflow到Agent
取一个实际的例子：休假申请。

如果我们的需求非常简单：

> 一键申请明天的休假。
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5f74241d33f74f08970eb5e304f30222&docGuid=PF4hInBwkN_YJv "")
这个需求可以被简化为一个**固定的工作流**：

1. 打开网页。
2. 填写起始时间。
3. 填写结束时间。
4. 填写休假原因。
5. 提交表单。

全过程**没有任何模糊的输入**，使用程序化即可完成，是最原始的工作流形态。

如果需求再模糊一些：

> 申请后天开始3天休假。
这个需求的特点是没有明确的起始和截止时间，**需要从语义上分析出来**：

1. 起始时间：后天。
2. 休假时长：3天。
3. 转换日期：10.14 - 10.16。
4. 执行申请：提交表单。

这是一个**工作流中使用大模型提取部分参数**的典型案例，是模型与工作流的结合。

如果需求更加模糊：

> 国庆后休假连上下个周末。
这样的需求**几乎没有任何直接确定日期的信息**，同时由于年份、休假安排等动态因素，**大模型不具备直接提取参数的能力**。将它进一步分解，需要一个**动态决策、逐步分析**的过程：

1. 知道当前年份。
2. 知道对应年份的国庆休假和调休安排。
3. 知道国庆后第一天是星期几。
4. 国庆后第一天到下个周末设为休假日期。
5. 额外补充调休的日期。
6. 填写并提交表单。

可以看出来，其中1-5步都是用来最终确定休假日期的，且需要**外部信息输入**，单独的大模型无法直接完成工作。这是一个典型的**Agent流程**，通过**大模型的智能**与**工具访问外部信息**结合实现用户需求。

### 什么是Agent
Agent是以**大模型为核心**，为**满足用户的需求**，使用一个或多个**工具**，自动进行**多轮模型推理**，最终得到结果的工作机制。

```
graph TD
    A[用户输入] --> B[大模型处理]
    B --> C{需要调用工具?}
    C -->|是| D[工具调用]
    C -->|否| H[生成最终回答]
    D --> E[工具实现]
    E --> F[工具返回结果]
    F --> B
    H --> I[结束退出]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style D fill:#ffe1f5
    style E fill:#ffe1f5
    style F fill:#ffe1f5
    style H fill:#e1ffe1
    style I fill:#f0f0f0

```
### 什么是Coding Agent
在Agent的基本定义的基础上，通过提示词、上下文、工具等元素强化“编码”这一目的，所制作的特化的Agent即为Coding Agent。

Coding Agent的最大特征是在**工具的选取**上，模拟工程师进行代码编写的环境，提供一套**完整的编码能力**，包括：

* 阅读和查询代码：
    * 读取文件，对应`cat` 命令。
    * 查看目录结构，对应`tree` 命令。
    * 通配符查找，对应`ls`命令（如`**/*.test.ts` 、`src/components/**/use*.ts`）。
    * 正则查找，对应`grep` 命令（如`function print\(.+\)` 可以找函数定义）。
    * LSP（Language Server Protocol），用于提供查找定义、查找引用、检查代码错误等能力。

* 编写或修改代码：
    * 写入文件。
    * 局部编辑文件。
    * 删除文件。

* 执行或交互命令：
    * 执行终端命令。
    * 查看终端命令`stdout`输出。
    * 向终端命令`stdin` 输入内容。


除此之外，通常Coding Agent还具备一些强化效果而设定的工具，通常表现为与Agent自身或外部环境进行交互，例如经常能见到的TODO、MCP、Subagent等等。





## 内部组成
### 上下文结构
```
graph TB
    subgraph BP["Base Prompt"]
        style BP fill:#FFE5E5,stroke:#FF9999,stroke-width:2px
        BP1[Base Prompt Content]
        style BP1 fill:#FFFFFF,stroke:#FF9999
    end
    
    subgraph AP["Agent Prompt"]
        style AP fill:#FFF4E5,stroke:#FFB366,stroke-width:2px
        AP1[Guideline] ~~~ AP2[Tool]
        style AP1 fill:#FFFFFF,stroke:#FFB366
        style AP2 fill:#FFFFFF,stroke:#FFB366
    end
    
    subgraph EC["Environment Context"]
        style EC fill:#E5F9FF,stroke:#66D9FF,stroke-width:2px
        EC1[Structure] ~~~ EC2[Rule] ~~~ EC3[Skill] ~~~ EC4[MCP] ~~~ EC5[Memory]
        style EC1 fill:#FFFFFF,stroke:#66D9FF
        style EC2 fill:#FFFFFF,stroke:#66D9FF
        style EC3 fill:#FFFFFF,stroke:#66D9FF
        style EC4 fill:#FFFFFF,stroke:#66D9FF
        style EC5 fill:#FFFFFF,stroke:#66D9FF
    end
    
    subgraph UC["User Context"]
        style UC fill:#F0FFE5,stroke:#99FF66,stroke-width:2px
        UC1[Query] ~~~ UC2[Attachment]
        style UC1 fill:#FFFFFF,stroke:#99FF66
        style UC2 fill:#FFFFFF,stroke:#99FF66
    end
    
    subgraph CP["Compression"]
        style CP fill:#FFE5FF,stroke:#FF99FF,stroke-width:2px
        CP1[Compression Content]
        style CP1 fill:#FFFFFF,stroke:#FF99FF
    end
    
    subgraph MH["Message History"]
        style MH fill:#FFF9E5,stroke:#FFDD66,stroke-width:2px
        MH1[User 1] --> MH2[Assistant 1] --> MH3[User 2] --> MH4[Assistant 2] --> MH5[User 3] --> MH6[Assistant 3]
        style MH1 fill:#FFFFFF,stroke:#FFDD66
        style MH2 fill:#FFFFFF,stroke:#FFDD66
        style MH3 fill:#FFFFFF,stroke:#FFDD66
        style MH4 fill:#FFFFFF,stroke:#FFDD66
        style MH5 fill:#FFFFFF,stroke:#FFDD66
        style MH6 fill:#FFFFFF,stroke:#FFDD66
    end
    
    subgraph RM["Reminder"]
        style RM fill:#E5FFE5,stroke:#66FF99,stroke-width:2px
        RM1[Time] ~~~ RM2[Todo] ~~~ RM3[Note]
        style RM1 fill:#FFFFFF,stroke:#66FF99
        style RM2 fill:#FFFFFF,stroke:#66FF99
        style RM3 fill:#FFFFFF,stroke:#66FF99
    end
    
    BP --> AP
    AP --> EC
    EC --> UC
    UC --> CP
    CP --> MH
    MH --> RM

```
### 身份定义
一个Agent首先会将模型定义成一个具体的身份（红色与橙色部分），例如在社区里常见的这样的说法：

> You are a Senior Front-End Developer and an Expert in React, Nexts, JavaScript, TypeScript, HTML, **CSS** and modern UI/UX **frameworks**.
在身份的基础上，再附加工作的目标和步骤拆解，比如Cline有类似这样的内容：

> [https://github.com/cline/cline/blob/4b9dbf11a0816f792f0b3229a08bbb17667f4b73/src/core/prompts/system-prompt/components/objective.ts](https://github.com/cline/cline/blob/4b9dbf11a0816f792f0b3229a08bbb17667f4b73/src/core/prompts/system-prompt/components/objective.ts)
> 1. Analyze the user's task and set clear, achievable goals to accomplish it. Prioritize these goals in a logical order.
> 2. Work through these goals sequentially, utilizing available tools one at a time as necessary. Each goal should correspond to a distinct step in your problem-solving process. You will be informed on the work completed and what's remaining as you go.
> 3. Remember, you have extensive capabilities with access to a wide range of tools that can be used in powerful and clever ways as necessary to accomplish each goal. Before calling a tool, do some analysis within `<thinking></thinking>` tags. First, analyze the file structure provided in `environment_details` to gain context and insights for proceeding effectively. Then, think about which of the provided tools is the most relevant tool to accomplish the user's task. Next, go through each of the required parameters of the relevant tool and determine if the user has directly provided or given enough information to infer a value. When deciding if the parameter can be inferred, carefully consider all the context to see if it supports a specific value. If all of the required parameters are present or can be reasonably inferred, close the thinking tag and proceed with the tool use. BUT, if one of the values for a required parameter is missing, DO NOT invoke the tool (not even with fillers for the missing params). DO NOT ask for more information on optional parameters if it is not provided.
> 4. Once you've completed the user's task, you must use the attempt_completion tool to present the result of the task to the user. You may also provide a CLI command to showcase the result of your task; this can be particularly useful for web development tasks, where you can run e.g. `open index.html` to show the website you've built.
> 5. The user may provide feedback, which you can use to make improvements and try again. But DO NOT continue in pointless back and forth conversations, i.e. don't end your responses with questions or offers for further assistance.
> 
不用特别仔细地看每一句话，多数Coding Agent会提供一些详实的行动准则、目标要求，这部分称为“Guideline”。

有一些Coding Agent可以在多种模式（或者说智能体）之间进行切换，例如Cursor有Edit、Ask、Plan等，RooCode有Architect、Orchestrator等，有些产品还支持自定义模式。

Cursor

RooCode

选择不同的模式时，实际上会产生不同的目标要求、行为准则，即不同的Guideline环节。因此系统提示词中的身份部分，通常会分成不变的Base Prompt（红色）和可变的Agent Prompt（橙色）两个部分来管理，实际开始任务时再拼装起来。

### 工具调用
Agent的另一个最重要的组成部分是工具，没有工具就无法称之为一个Agent。让Agent能够使用工具，就必须要有2部分信息：

1. 有哪些工具可以用，分别是什么作用。
2. 如何指定使用一个工具。

对于第一点（哪些工具），在Agent开发过程中，一般视一个工具为一个**函数**，即由以下几部分组成一个工具的定义：

1. 名称。
2. 参数结构。
3. 输出结构。

实际在调用模型时，“输了结构”往往是不需要提供给模型的，但在Agent的实现上，它依然会被预先定义好。而“名称”和“参数结构”会统一组合成一个结构化的定义，通常所有工具都只接收1个参数（对象类型），用JSON Schema表示参数结构。

一个典型的工具定义：

```
{
  "name": "read",
  "description": "Read the contents of a file. Optionally specify line range to read only a portion of the file.",
  "parameters": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "The file path to read from"
      },
      "lineStart": {
        "type": "integer",
        "description": "The starting line number (1-indexed). If not specified, reads from the beginning of the file."
      },
      "lineEnd": {
        "type": "integer",
        "description": "The ending line number (1-indexed). If not specified, reads to the end of the file."
      }
    },
    "required": ["path"]
  }
}
```
可以简单地把这个工具理解成对应的TypeScript代码：

```
interface ReadToolParameter {
		path: string;
		lineStart?: number;
		lineEnd?: number;
}

async function read(parameters: ReadToolParameter) {
		// 工具实现
}
```
对于第2点（指定使用工具），则是要让大模型知道工具调用的具体格式。这在业界通常有2种做法。

第1种以Claud Code、Codex等为典型，使用大模型提供的Function Calling格式调用，分为以下几步：

1. 在调用大模型时，通过一个`tools` 字段传递所有的工具定义。
2. 模型会返回一个消息中包含`tool_calls` 字段，里面每一个对象是一个工具的调用，使用`id` 作为唯一标识。
3. 工具产生的结果，以一条`role: 'tool'` 的消息返回，其中`tool_call_id` 与调用的`id`对应，`content` 是工具的结果（这里各家模型厂商的实现略有不同，其中Anthropic要求`role: user`，但content字段中传递toolResult，其结构是`[{type: 'tool_result',tool_use_id: toolBlock.id, content: toolResultContent}]`,`tool_use_id`与调用的id对应）。

第2种方式是以Cline、RooCode为典型，使用一种自定义的文本格式来表示工具调用，通常选择XML的结构，例如对于Cline，读取一个文件的结构如下：

```
<read_file>
<path>src/index.ts</path>
</read_file>
```
只要在模型返回的消息中出现这样的结构，就会被解析为一个工具调用，得到的结果以普通的`role: 'user'` 的消息返回，包括实际内容和一些提示相关的信息。

```
Content of src/index.ts:

Note:

- this file is truncated to line 1000, file has a total 2333 lines.
- use read_file with line_start and line_end parameters to read more content.
- use seach_in_files tool searching for specific patterns in this file.

...
```
### 环境感知
Coding Agent之所以可以在一个代码库上执行任务，除了通过工具来遍历、检索代码外，另一个因素是Agent实现会在调用模型时**主动地**提供一部分与项目有关的信息。

其中对Coding Agent工作最有用的信息之一是代码库的结构，即一个表达出目录、文件结构的树型区块。这部分信息通常会符合以下特征：

1. 尽可能地保留目录的层级结构，使用换行、缩进的形式表达。
2. 遵循`.gitignore` 等项目配置，被忽略的文件不会表现在树结构中。
3. 当内容过多时，有一定的裁剪的策略，但同时尽可能多地保留信息。

以Cursor为例，这部分的内容大致如下：

```
<project_layout>
Below is a snapshot of the current workspace's file structure at the start of the conversation. This snapshot will NOT update during the conversation. It skips over .gitignore patterns.

codex-cursor/
  - AGENTS.md
  - CHANGELOG.md
  - cliff.toml
  - codex-cli/
    - bin/
      - codex.js
      - rg
    - Dockerfile
    - package-lock.json
    - package.json
    - scripts/
      - build_container.sh
      - build_npm_package.py
      - init_firewall.sh
      - [+4 files (1 *.js, 1 *.md, 1 *.py, ...) & 0 dirs]
  - codex-rs/
    - ansi-escape/
      - Cargo.toml
      - README.md
      - src/
        - lib.rs
</project_layout>
```
当内容数量超过阈值时，会采用**广度优先**的保留策略（即尽可能地保留上层目录结构），同时对于被隐藏的文件或子目录，会形如`[+4 files (1 *.js, 1 *.md, 1 *.py, ...) & 0 dirs]`这样保留一个不同文件后缀的数量信息。

除了目录结构外，还有一系列**默认需要模型感知**的信息，在一个Coding Agent的工作环境中，它通常分为2大类，各自又有一系列的细项：

1. 系统信息：
    1. 操作系统（Windows、macOS、Linux，具体版本）。
    2. 命令行语言（Shell、Powershell、ZSH）。
    3. 常见的终端命令是否已经安装（`python3` 、`node` 、`jq` 、`awk`等，包含具体版本）。
    4. 代码库目录全路径。

2. 为Agent扩展能力的信息：
    1. Rule（自动激活的部分）。
    2. Skill（摘要描述部分）。
    3. MCP（需要的Server和Tool列表）。
    4. Memory（通常是全量）。


需要注意的是，环境信息这部分，**一般不出现在系统提示词中，而是和用户提问的消息放置在一起。**

### 简单实现
在身份定义、工具调用、环境感知这3部分最基础的Agent组成都达成后，简单地使用大模型的API，进行自动化的工具调用解析、执行、发送新一轮模型调用，可以非常简单地实现一个最小化的Coding Agent。

可以尝试用以下的提示词，使用任意现有的Coding Agent产品，为你编写一个实现，并自己调试一下，感受Coding Agent的最基础的逻辑：

```
我希望基于大模型实现一个Coding Agent，以下是我的具体要求：

1. 使用Claude作为模型服务商，使用环境变量管理我的API Key。
2. 默认使用Claude Sonnet 4.5模型。
3. 使用Anthropic's Client SDK调用模型。
4. 不需要支持流式输出。
5. 使用TypeScript编写。

以下是Agent提供的工具：

1. read({path: string})：读取一个文件的内容
2. list({directory: string})：列出一个目录下的一层内容，其中目录以`/`结尾
3. write({path: string, content: string})：向文件写入内容
4. edit({path: string, search: string, replace: string})：提供文件中的一块内容

以下是交互要求：

1. 通过NodeJS CLI调用，支持`query`和`model`两个参数，可以使用`yargs`解析参数。
2. 在System消息中，简短地说明Coding Agent的角色定义、目标和行为准则等。
3. 在第一条User消息中，向模型提供当前的操作系统、Shell语言、当前目录绝对路径信息，同时包含跟随`query`参数的内容，组织成一条模型易于理解的消息。
4. 对每一次模型的工具调用，在控制台打印工具名称和标识性参数，其中标识性参数为`path`或`directory`，根据工具不同来决定。
5. 如果模型未调用工具，则将文本打印到控制台。

请在当前目录下建立一个`package.json`，并开始实现全部的功能。
```
## 优质上下文工程
### 成本控制
大模型是一个非常昂贵的工具，以Claude为例，它的官方API价格如下：

|**Model**|**Base Input Tokens**|**5m Cache Writes**|**1h Cache Writes**|**Cache Hits & Refreshes**|**Output Tokens**|
|-|-|-|-|-|-|
|Claude Opus 4.5|$5 / MTok|$6.25 / MTok|$10 / MTok|$0.50 / MTok|$25 / MTok|
|Claude Sonnet 4.5|$3 / MTok|$3.75 / MTok|$6 / MTok|$0.30 / MTok|$15 / MTok|
|Claude Haiku 4.5|$1 / MTok|$1.25 / MTok|$2 / MTok|$0.10 / MTok|$5 / MTok|

我们可以观察到一些特征：

1. 输出的价格是输入的5倍（但实际考虑到输出与输出的数量比例，输出的价格根本不值一提）。
2. 缓存输入（Cache Writes）比正常输入（Base Input）更贵一些，约1.25倍。
3. 缓存命中（Cache Hits）的价格比正常输入（Base Input）要便宜很多，为1/10的价格。

这就意味着，**一个良好使用缓存的Agent实现，其成本会比不用缓存降低8-10倍**。因此所有的Coding Agent一定会**细致地梳理内容结构，最大化利用缓存**。

在大模型的API中，缓存通常以“块”为单位控制，例如：

1. 系统提示词中不变的部分。
2. 系统提示词中可变部分。
3. 工具定义。
4. 每一条消息，单条消息也可以拆成多个块。

继续观察Claude对于缓存控制的文档：

|**What changes**|**Tools cache**|**System cache**|**Messages cache**|**Impact**|
|-|-|-|-|-|
|**Tool definitions**|✘|✘|✘|Modifying tool definitions invalidates the entire cache|
|**Web search toggle**|✓|✘|✘|Enabling/disabling web search modifies the system prompt|
|**Citations toggle**|✓|✘|✘|Enabling/disabling citations modifies the system prompt|
|**Tool choice**|✓|✓|✘|Changes to `tool_choice` parameter only affect message blocks|
|**Images**|✓|✓|✘|Adding/removing images anywhere in the prompt affects message blocks|
|**Thinking parameters**|✓|✓|✘|Changes to extended thinking settings affect message blocks|

可以看到，在大模型API中各种参数一但有所变动，缓存都会大量失效（至少消息缓存全部失效，大概率系统缓成失效），这就会造成成本的极大提升。因此，在Coding Agent实现中，都会**从一开始就确定所有参数，整个任务不做任何变更**。一些很经典的实例：

1. 一次任务不会一部分消息开思考模式，一部分不开，因为思考参数会让全部的消息缓存失效。
2. 切换不同模式（如Edit、Ask、Plan）时，虽然能使用的工具不同，但只是在消息中增加说明，而不会真的将`tools` 字段改变。

另外，Coding Agent会**尽可能保持历史消息内容完全不变**，以最大化地缓存消息。例如对于一个进行了10轮模型调用的任务，理论上第10次调用中，前9轮的消息内容都会命中缓存。但如果此时擅自去修改了第1轮的工具调用结果（例如试图删除读取的文件内容），看似可能消息的长度减少了，但实际因为缓存被破坏，造成的是10倍的成本提升。

总而言之，**缓存是一个至关重要的因素，Coding Agent的策略优化通常以确保缓存有效为前提，仅在非常必要的情况下破坏缓存**。

### 空间管理
Coding Agent因为会自动地与大模型进行多轮的交互，随着不断地读入文件、终端命令输出等信息，上下文的长度会变得非常的大，而大模型通常只具备128K左右的总长度，因此如何将大量内容“适配”到有限的长度中，是一个巨大的挑战。

控制上下文长度的第一种方式是“**裁剪**”，即在整个上下文中，将没用的信息删除掉。试想如下的场景：

1. 模型读取了一个文件的内容。
2. 模型将文件中`foo` 这一行改成了`bar` 。
3. 模型又将文件中`eat` 这一行改成了`drink` 。

假设我们对模型每一次修改文件，都**返回最新的文件内容**，如果这个文件有1000行，那么1次读取、2次修改，就会**产生3000行的空间占用**。

一种优化方式就是，在这种**连续**的读-改的场景下，只保留最后一条消息中有全文内容，即上述3次模型调用后，出现在上下文中的内容实际是这样的：

```
<!-- Assistant -->
read(file)

<!-- User -->
[This file has been updated later, outdated contents are purged from here]

<!-- Assistant -->
edit(file, foo -> bar)

<!-- User -->
The edit has been applied successfully.

--- a/file
+++ b/file
@@ -23,1 +23,1 @@
-foo
+bar

[This file has been updated later, outdated contents are purged from here]

<!-- Assistant -->
edit(file, eat -> drink)

<!-- User -->
The edit has been applied successfully, the new file content is as below:

```
{content of file}
```
```
可以看到，通过**将连续对同一文件的修改进行裁剪**，可以只保留最新的内容，同时又使用`unidiff` 之类的形式保留中间编辑的差异信息，最大限度地降低空间占用，又能保留模型的推理逻辑。

但裁剪**不能使用在非连续的消息中**，随意地使用剪裁逻辑，很有可能**破坏消息缓存结构**，进而使模型调用的输入无法通过缓存处理，几倍地增加模型的调用成本。

即便裁剪有一定效果，但随着更多的内容进入到上下文中，始终会有将上下文占满的时候，此时模型将完全无法进行推理。为了避免这种情况出现，Coding Agent通常会使用“**压缩**”这一技术，即将前文通过模型摘要成少量的文字，同时又保留比较关键的推理链路。

通常，压缩在上下文即将用完的时候触发，如已经使用了90%的上下文则启动压缩，压缩的目标是将90%的内容变为10%的长度，即省出80%的空间供后续推理。

压缩本身是一个模型的任务，即将所有的上下文（可以选择性地保留最新的1-2对消息）交给模型，同时附带一个压缩的要求，让模型完成工作。这个压缩的要求的质量将决定压缩的最终结果，一个比较典型的实现是Claude Code的“八段式摘要”法：

```
const COMPRESSION_SECTIONS = [
  "1. Primary Request and Intent",    // 主要请求和意图
  "2. Key Technical Concepts",        // 关键技术概念
  "3. Files and Code Sections",       // 文件和代码段
  "4. Errors and fixes",              // 错误和修复
  "5. Problem Solving",               // 问题解决
  "6. All user messages",             // 所有用户消息
  "7. Pending Tasks",                 // 待处理任务
  "8. Current Work"                   // 当前工作
];
```
通过将信息压缩成8部分内容，能够最大限度地保留工作目标、进度、待办的内容。

### 独立上下文
在实际的应用中，其实大概率是不需要128K上下文用满的，但真实表现又往往是**上下文不够用**。这中间存在的差异，在于2类情况：

1. 为了满足一个任务，需要收集大量的信息，但收集到正常信息的过程中，会引入无效的、错误的内容，占用上下文。
2. 一个任务足够复杂，分解为多个小任务后各自占用部分上下文，但加起来以后会超出限制。

试想一下，对于一个这样的任务：

> 修改我的Webpack配置，调整文件拆分逻辑，让最终产出的各个JS文件大小尽可能平均。
但是很“不幸”地，这个项目中存在6个`webpack.config.ts`文件，且最终`splitChunks` 配置在一个名为`optimization.ts` 的文件中管理，那么对于Coding Agent来说，这个任务中就可能存在大量无意义的上下文占用：

1. 读取了6个`webpack.config.ts` ，一共2000行的配置内容，但没有任何`splitChunks` 的配置，包含了大量`import` 其它模块。
2. 又读取了10个被`import` 的模块，最终找到了`optimization.ts` 文件。
3. 经过修改后，执行了一次`npm run build` 来分析产出，发现JS的体积不够平均。
4. 又修改`optimization.ts` ，再次编译，再看产出。
5. 循环往复了8次，终于在最后一次实现了合理的`splitChunks` 配置。

这里面的“6个`webpack.config.ts` ”、“10个其它模块”、“8次优化和编译”都是对任务最终目标并不有效的内容，如果它们占用150K的上下文，这个任务就不得不在中途进行1-2次的压缩，才能够最终完成。

为了解决这个问题，当前多数的Coding Agent都会有一个称为“**Subagent**”的概念。就好比一个进程如果只能使用4GB的内存，而要做完一件事需要16GB，最好的办法就是开5个进程。Subagent是一种**类似子进程的，在独立的上下文空间中运行，与主任务仅进行必要信息交换的工作机制**。

再回到上面的案例，在Subagent的加持下，我们可以将它变成以下的过程：

1. 启动一个Subagent，给定目标“找到Webpack文件拆分的代码”。
    1. 读取6个`webpack.config.ts` 。
    2. 读取10个被`import` 的模块。
    3. 确定目标文件`optimization.ts` 。
    4. 返回总结：在`optimization.ts` 中有文件拆分的配置，当前配置为……。

2. 启动一个Subagent，给定目标“修改`optimization.ts` ，使产出的JS体积平均，执行`npm run build`并返回不平均的文件“。
    1. 修改`optimization.ts`。
    2. 执行`npm run build`，得到命令输出。
    3. 分析输出，找到特别大的JS文件，返回总结：配置已经修改，当前`xxx.js` 体积为平均值的3倍（723KB），其它文件体积正常。

3. 启动一个Subagent，给定目标“分析`dist/stats.json`，检查`xxx.js` 中的模块，修改`optimization.ts` 使其分为3个250KB左右的文件，执行`npm run build`并返回不平均的文件”。
    1. ……
    2. ……

4. 继续启动6次Subagent，直到结果满意。

```
graph TB
    Start([开始]) --> MainAgent[主 Agent<br/>目标: 优化 Webpack 文件拆分]
    
    MainAgent --> SubAgent1
    
    subgraph SubAgent1[Subagent 1: 查找配置]
        SA1_Start[接收目标:<br/>找到 Webpack 文件拆分的代码] --> SA1_Step1[读取 6 个<br/>webpack.config.ts]
        SA1_Step1 --> SA1_Step2[读取 10 个被 import<br/>的模块]
        SA1_Step2 --> SA1_Step3[确定目标文件<br/>optimization.ts]
        SA1_Step3 --> SA1_Return[返回总结:<br/>在 optimization.ts 中有文件拆分配置<br/>当前配置为...]
    end
    
    SubAgent1 --> MainAgent_Eval1{评估结果}
    MainAgent_Eval1 --> SubAgent2
    
    subgraph SubAgent2[Subagent 2: 初步优化]
        SA2_Start[接收目标:<br/>修改 optimization.ts 使产出 JS 体积平均<br/>执行 npm run build 并返回不平均文件] --> SA2_Step1[修改 optimization.ts]
        SA2_Step1 --> SA2_Step2[执行 npm run build<br/>获取命令输出]
        SA2_Step2 --> SA2_Step3[分析输出<br/>找到特别大的 JS 文件]
        SA2_Step3 --> SA2_Return[返回总结:<br/>配置已修改, xxx.js 体积为平均值 3 倍<br/>723KB, 其它文件体积正常]
    end
    
    SubAgent2 --> MainAgent_Eval2{评估结果}
    MainAgent_Eval2 --> SubAgent3
    
    subgraph SubAgent3[Subagent 3: 深度分析]
        SA3_Start[接收目标:<br/>分析 dist/stats.json, 检查 xxx.js 模块<br/>修改 optimization.ts 使其分为 3 个 250KB 文件<br/>执行 npm run build 并返回不平均文件] --> SA3_Step1[分析 dist/stats.json<br/>检查 xxx.js 中的模块]
        SA3_Step1 --> SA3_Step2[修改 optimization.ts<br/>配置拆分策略]
        SA3_Step2 --> SA3_Step3[执行 npm run build<br/>获取命令输出]
        SA3_Step3 --> SA3_Step4[分析输出<br/>检查文件体积分布]
        SA3_Step4 --> SA3_Return[返回总结:<br/>文件拆分结果...]
    end
    
    SubAgent3 --> MainAgent_Eval3{评估结果}
    MainAgent_Eval3 --> SubAgent4
    
    subgraph SubAgent4[Subagent 4-9: 迭代优化]
        SA4_Start[接收目标:<br/>继续优化文件拆分] --> SA4_Process[重复流程:<br/>1. 分析 stats.json<br/>2. 调整 optimization.ts<br/>3. 执行构建<br/>4. 分析结果]
        SA4_Process --> SA4_Return[返回总结:<br/>优化结果...]
    end
    
    SubAgent4 --> MainAgent_EvalN{评估结果<br/>是否满意?}
    MainAgent_EvalN -->|否, 继续优化| SubAgent4
    MainAgent_EvalN -->|是, 达到目标| End([结束<br/>文件拆分优化完成])
    
    style MainAgent fill:#e1f5ff,stroke:#0066cc,stroke-width:3px
    style SubAgent1 fill:#fff4e6,stroke:#ff9800,stroke-width:2px
    style SubAgent2 fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px
    style SubAgent3 fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
    style SubAgent4 fill:#fce4ec,stroke:#e91e63,stroke-width:2px
    style Start fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
    style End fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px

```
不难看出来，这种模式下主体的Coding Agent实际是在"**指挥**"**Subagent做事**，自身的上下文占用是非常有限的。而Subagent仅**“专注”于一个小目标**，也不需要太多的上下文，最终通过这类不断**开辟新上下文空间**的方式，将一个复杂的任务完成。

### 注意力优化
如果你经常使用Coding Agent，或在业界早期有过比较多的使用经验，你可能会发现这种情况：Coding Agent在完成一个任务到一半时，忘了自己要做什么，草草地结束了任务，或偏离了既定目标产生很多随机的行为。

会发生这样的情况，有一定可能是裁剪、压缩等策略使有效的上下文信息丢失了，但更多是因为简单的一个用户需求被大量的代码内容、命令输出等推理过程所掩盖，权重弱化到已经不被大模型“注意到”，因此最初的目标也就完全丢失了。

Coding Agent一个很重要的任务，就是在长时间运作的同时随时调整大模型的注意力，使其始终聚焦在最终目标、关注当前最需要做的工作，不要偏离预先设定的路线。为了实现这一效果，Coding Agent产品提出了2个常见的概念。

第一称为**TODO**，在很多的产品中，你会看到Agent先将任务分解成几个步骤，转为一个待办列表。这个列表在界面上始终处于固定的位置，随着任务的推进会逐步标记为完成。这个TODO实际上**并不是给用户看的，而是给模型看的**。

在实际的实现中，每一次调用模型时，在最后一条消息（一般就是工具调用的结果）上，除了原始消息内容外，会增加一个称为“Reminder”的区域。这个区域因为始终出现在所有消息的最后，通常来说在模型的注意力中优先级更高，而且**绝对不会受其它因素影响而消失**。

Reminder中可以放置任意内容，比较经典的有：

1. TODO及进度。用于模型时刻理解目标、进展、待办。

```
<reminders>
- Planned todos:
  - [x] Explore for code related to "print" function
  - [x] Add "flush" parameter to function
  - [ ] Refactor all "print" function calls to relect the new parameter
</reminders>
```
1. 工具子集。如前面《缓存》相关的描述，因为修改工具定义会使缓存失效，因此当切换模式使得可用的工具减少时，一般仅在Reminder中说明部分工具不可用，由模型来遵循这一约束，而不是直接删除部分工具。

```
<!-- 切换至Ask模式 -->
<reminders>
- You can ONLY use these tools from now on:
  - read
  - list
  - grep
  - bash
</reminders>
```
1. 行为指示。例如当模型连续多次给出名称、参数都一模一样的工具调用时，说明模型处在一种不合理的行为表现上，此时在Reminder中增加提示，让模型感知到当前状态的错误，就有可能调整并脱离错误的路线。

```
<!-- Assistant -->
read(file)

<!-- User -->
The file content: ...

<!-- Assistant -->
read(file)

<!-- User -->
The file content: ...

<reminders>
- Your are using read tool the second time with exactly the same parameters, this usually means an unexpected situation, you should not use this tool again in your response.
</reminders>
```
1. 状态提示。例如激活某一个Skill时，Reminder中可以提示“当前正在使用名为X的Skill“，这种提示可以让模型更加专注于完成一个局部的工作。

```
<reminders>
- You are currently working with the skill "ppt" active, be focused on this task until you quit with exit_skill tool.
</reminders>
```
需要额外注意的是，**Reminder仅在最后一条消息中出现，当有新的消息时，旧消息上的Reminder会被移除**。基于这一特征，我们知道**Reminder是永远无法命中缓存的**，因此Reminder部分的内容长度要有控制，避免造成过多的成本消耗。

### 冲突管控
随着Coding Agent能力的发展，当下执行的任务时间越来越长、编辑的文件越来越多，同时更多的用户也习惯与在Agent工作的同时自己也进行编码工作，甚至让多个Agent任务并发执行。这种“协同”形态下，不少用户曾经遇到过这样的问题：

> 自己将Agent生成的代码做了一些修正，但之后Agent又把代码改了回去。
这个现象的基本原因也很清楚，就是**Agent并不知道你改动过代码**。例如以下的过程使Agent读取并编辑了一个文件：

```
<!-- Assistant -->
read(file)

<!-- User -->
The file content:
...
console.log('hello');
...
<!-- Assistant -->
edit(file, hello -> Hello)

<!-- User -->
Edit has been applied successfully.
```
这个时候，在模型见到的上下文中，这个文件中的代码显然是`console.log('Hello');` 。假设乃又将它改成了`console.trace('Hello');` ，后面模型依然会基于`.log` 来修改代码，用户看起来就是代码“改了回去”。

解决这种共同编辑文件的冲突，实际上有多种方法：

* 加锁法。当Agent读取、编辑一个文件时，更新模型认知的文件内容的快照。当这个Agent再一次编辑这个文件时，读取文件当前的实际内容，和快照做比对，如果内容不一样，拒绝这一次编辑，随后要求Agent重新读取文件（更新快照与实际内容一致）再进行编辑。这是一种**主流的做法**，不过**Agent实现上的细节比较重**。

```
<!-- Assistant -->
edit(file, console.log...)

<!-- User -->
This edit is rejected, the file has been modified since your last read or edit, you should read this file again before executing any write or edit actions.

<!-- Assistant -->
read(file)

<!-- User -->
The file content: ...

<!-- Assistant -->
edit(file, console.trace...);
```
* 推送法。监听所有模型读取、编辑过的文件的变更，当文件发生变更时，在**下一次模型调用**时，不断通过Reminder区域追加这些变更，让模型“实时”地知道文件有所变化，直到文件被下一次读取。这种方式能**让模型更早地感知变化**，但**推送信息可能过多**，**影响成本和推理速度。**

```
<!-- Assistant -->
run_command(ls)

<!-- User -->
The command output: ...

<reminders>
- These files have been modified since your last read or edit, you should read before write or edit to them:
  - file
  - file
  - ...
</reminders>
```
* 隔离法。使用Git Worktree方案，直接让不同的Agent任务在文件系统上隔离，在一个独立的Git分支上并行工作，相互不受干扰。在任务完成后，用户检查一个任务的全部变更，在采纳时再合并回实际的当前Git分支，有冲突的由用户解决冲突。这种方法让Agent**根本不需要考虑冲突问题**，但缺点是**系统资源占用高**，且**有合并冲突风险**。

文件编辑冲突只是一个比较常见的现象，实际上用户和Agent、多个Agent并行工作，可能造成的冲突还有很多种，例如：

> 用户敲了半行命令`ls -`，Agent直接在终端里敲新的命令`grep "print" -r src`执行，导致最后的命令是`ls -grep "print" -r src` ，是一个不合法的命令。
终端的抢占也是一种冲突，但相对更容易解决，只要让每一个Agent任务独占自己的终端，永远不与用户、其它Agent任务相交叉即可。

### 持久记忆
我们都知道，模型是没有状态的，所以每一次Agent执行任务，对整个项目、对用户的倾向，都是从零开始的过程。这相当于**历史经验无法积累**，很多曾经调整过的细节、优化过的方向都会被重置。虽然可以通过比如Rule这样的方式去持久化这些“经验”，但需要用户主动的介入，使用成本是相对比较高的。

因此当前很多Coding Agent产品都在探索“记忆”这一能力，争取让Agent变得**用的越多越好用**。记忆这个话题真正的难点在于：

1. 如何触发记忆。
2. 如何消费记忆。
3. 什么东西算是记忆。

首先对于“如何触发”这一问题，常见于2种做法：

1. 工具型。定义一个`update_memory` 工具，将记忆作为一个字符串数组看待，工具能够对其进行增、删改，模型在任务过程中实时地决定调用。往往模型并不怎么喜欢使用这类工具，经常见于用户有强烈情感的描述时才出现，比如“记住这一点”、“不要再……”。
2. 总结型。在每一次对话结束后，将对话全部内容发送给模型，并配上提示词进行记忆的提取，提取后的内容补充到原本记忆中。总结型的方案往往又会过度地提取记忆，将没必要的信息进行持久化，干扰未来的推理。
3. 存储型。不进行任何的记忆整理和提取，而是将所有任务的原始过程当作记忆，只在后续“消费”的环节做精细的处理。

然后在“如何消费”的问题下，也常见有几种做法：

1. 始终附带。记忆内容记录在文件中，Agent实现中将文件内容附带在每一次的模型请求中。即模型始终能看到所有的记忆，这无疑会**加重模型的认知负担**，也**占用相当多的上下文空间**，因为很多记忆可能是与当前任务无关的。
2. 渐进检索。本身不带记忆内容到模型，但将记忆以文件系统的形式存放，Agent可以通过`read` 、`list`、`grep` 等工具来检索记忆。配合“存储型”的触发方式，能让全量的历史任务都成为可被检索的记忆。但这种方式要求模型有比较强的对记忆的认知，在正确的时刻去找相关的记忆。但往往因为**根本不知道记忆里有什么**，进而**无法知道什么时候应该检索**，最终几乎不触发检索。

而最终的问题，“什么东西是记忆”，是当下Coding Agent最难以解决的问题之一。错误的、不必要的记忆甚至可能造成实际任务效果的下降，因此精确地定义记忆是Agent实现的首要任务。

通常来说，记忆会分为2种大的方向：

1. 事实型。如“使用4个空格作为缩进”、“不要使用`any` 类型“，这些都是事实。事实是无关任何情感、不带主观情绪的。
2. 画像型。如”用户更喜欢简短的任务总结“就是一种对用户的画像。画像是单个用户的特征，并不一定与项目、代码、架构相关。

在Coding Agent上，往往更倾向于对”事实型“的内容进行记忆，而不考虑用户画像型的记忆。

同时，从业界的发展，可以看到越来越多的模型厂商在从底层进行记忆能力的开发，如最近Google的Titan架构就是一种记忆相关的技术。可能未来某一天，Agent实现上已经不需要再关注记忆的逻辑与实现，模型自身将带有持久化的记忆能力。

## 能力扩展
在实际应用中,还需要一些机制来让Agent更好地适应特定的项目、团队和个人习惯。当前主流的Coding Agent产品都提供了Rule、MCP、Skill这三种扩展能力,它们各有侧重,共同构成了Agent的能力增强体系。

### Rule
当面对业务的repo往往存在一些领域相关的知识而非模型的知识库中已有的内容，这些往往需要凭借老员工的经验或者读取大量代码库的信息进行总结后才能明白，这些内容便适合放到Rule中，作为静态的不会频繁改动的内容放入Environment Context中长期Cache。

好的Rule应当足够精简、可操作且范围明确，人看不懂的规则或者描述不清的规则模型是一定搞不定无法遵守的。

* 将Rule控制在 500 行以内。
* 将较大的规则拆分为多个可组合的规则，采取按需的方式，按照 文件路径/关键场景 激活Rule；对于特定场景激活的Rule，采取编写**索引的方式**创建Rule，让模型渐进式激活，比如项目针对网络请求和错误处理相关做了项目维度的封装处理，但这种情况并不是每个文件ts/tsx文件都会遇到的诉求，比如在项目的rules目录下创建index.mdr（curso是.mdc文件），编写下面的激活的条件：
    * 当编码涉及以下任一情况时，必须立刻阅读 [08-api-error-handling.mdc](mdr:.cursor/rules/08-api-error-handling.mdc)
        *   需要进行API调用获取数据
        * 处理异步操作的错误和加载状态


* 提供具体示例或参考文件，针对xx情况正确的方式是`code`。
* 避免模糊的指导，比如交互式的东西模型交互不了，不需要写进去。
* 为了模型能够积极验证每次改动是否符合预期，告知模型改动后可以执行的正确的构建命令，以及某些自定义命令（比如自动化测试）引导模型在后台启动命令，在xx秒后读取日志文件的内容进行结果的判断。

### MCP
**MCP(Model Context Protocol)**是Anthropic提出的一种标准化的工具扩展协议，它允许开发者以统一的方式为Coding Agent添加新的能力。

与Rule的"声明式约束"不同，MCP是一种实时工具调用协议，即通过MCP server的方式进行连接，来扩展Agent可以做的事情。

一个典型的场景是集成外部服务。比如你的项目托管在GitHub上，可以让Agent直接访问GitHub实现创建Issue、查询PR状态、添加评论等功能：

```
{
    "mcpServers": {
        "github": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {
                "GITHUB_PERSONAL_ACCESS_TOKEN": "<your-github-token>"
            }
        }
    }
}
```
配置好后，Agent就能在代码审查过程中自动创建Issue记录问题、查询相关PR的讨论、甚至根据代码变更自动生成commit message。

MCP的另一个优势是实现门槛低。一个MCP Server本质上就是一个标准输入输出的程序,它通过JSON-RPC协议与Agent通信，当模型需要外部能力的时候，调用MCP Server，而模型无需关心其内部代码实现，Agent只需要按照固定的协议去连接获取内容。

### Skill
#### 什么是Skill
随着模型能力的提升，使用Agent完成的任务复杂度逐渐增加，使用Coding Agent可以进行本地代码执行和文件系统完成跨领域的复杂任务。但随着这些Agent的功能越来越强大，我们需要更具可组合性、可扩展性和可移植性的方法，为它们配备特定领域的专业知识，因此Agent Skill作为一种为Agent扩展能力的标准诞生。Skill 将指令、脚本和资源的文件夹打包，形成专业领域的知识，Agent在初始化的时候会获取可用的Skills列表，并在需要的时候动态加载这些内容来执行特定任务。

随着 Skill 复杂性的增加，它们可能包含过多的上下文信息，无法放入单个配置文件中`SKILL.md`，或者某些上下文信息仅在特定场景下才相关。在这种情况下，Skill可以在当前目录中bundle额外的文件，并通过文件名引用这些文件，这些额外的文件提供了更多详细信息，Coding Agent 可以根据需要选择浏览和查找这些信息。Skill 是**渐进式触发**的， 因此`SKILL.md`中`name`和 `description`很关键，这会始终存在于Agent的环境上下文中提供给模型，模型会根据这些描述信息来决定是否在当前任务中触发该Skill，当你明确希望使用某个Skill完成任务，可以在prompt中指定“使用xxxx Skill完成xx任务”。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e17e0ecd924f40678f63af09431d054a&docGuid=PF4hInBwkN_YJv "")
#### Skill和代码执行
LLM在很多任务上表现出色，但许多操作需要使用编写代码 -> 代码执行的方式，带来更高效的操作、确定性的以及可靠性的结果。生成式的模型常常通过生成可执行代码的方式去验证/计算结果。

代码既可以作为可执行工具，也可以作为文档。Skill中应该明确让模型是应该直接运行脚本，还是应该将其作为参考信息读取到上下文中。

#### 如何创建Skill
每个Skill由一个必需的 SKILL.md 文件和可选的bundle资源组成，Skill 应该只包含完成任务所需的信息。

```
skill-name/
├── SKILL.md (必需)
│   ├── YAML frontmatter 元数据 (必需)
│   │   ├── name: (必需)
│   │   ├── description: (必需，这是 skill 的主要触发机制,帮助模型理解何时使用该 skil)
│   │   └── compatibility: (可选)
│   └── Markdown 说明 (必需)
└── bundle的资源 (可选)
    ├── scripts/          - 可执行代码 (Python/Bash/等)
    ├── references/       - 需要时加载到上下文的文档
    └── assets/           - 用于输出的文件 (模板、图标、字体等)
```
举一个具体的例子，比如当我们需要进行批量项目的技术栈migrate，比如将less迁移postcss，中间涉及一系列的复杂步骤，比如：

* 安装postcss以及postcss plugin的依赖
* 配置postcss的config
* 分析项目用到了哪些less varibale替换成css vars
* 删除mixin并替换
* 一系列的其他兼容less的语法转换...
* 替换文件后缀

上面的工作可以通过清晰的流程描述，并配合脚本实现，因此可以作为一个Skill将经验变成可复制的，一个less-to-postcss的skill的结构：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=930f918f3c7943f9a508dfc174665e36&docGuid=PF4hInBwkN_YJv "")
#### Skill的使用
人人都可以创建Skill，也可以让Agent来编写Skill，这是Skill非常便捷的地方。Skill通过instructions和code赋予Coding Agent新的能力。虽然这使其功能强大并有很高的自由度，但也意味着恶意SKill可能会在其使用环境中引入漏洞，诱使模型窃取数据并执行非预期操作。仅从可信来源安装Skill，如果无法确信来源可信，在使用前请务必进行彻底审核。

Skill的出现并不是替代MCP的出现，而是相互配合，在合适的场景下选取Skill或是MCP。某些任务Skill和MCP Server均可完成，但Skill通过执行代码的方式可以一次性加载完整流程，但MCP Server要经历多次查询和多轮对话往返，这种情况下Skill更为合适，但这不意味着绝对的优势，比如标准化文档创建这个典型的场景，创建PPT/Word/Excel在本地使用Skill即可完成，但数据的提供则需要借助MCP Server进行查询。因此Skill擅长的是在本地通过执行`code`的方式完成复杂任务，在用户私有数据、动态数据查询这些情况下Skill就无法搞定了，这和用户的数据库以及隐私强关联，需要让模型无法感知在执行过程中的隐私信息，Skill能够与MCP Server互补完成更为复杂的流程。

```
graph TB
    User[用户: 创建竞品分析报告]
    
    subgraph Context["Env Context"]
        Skill["竞品分析Skill<br/>步骤1: GitHub数据<br/>步骤2: 内部文档<br/>步骤3: 市场信息<br/>步骤4: 格式化"]
    end
    
    subgraph Agent["Agent推理与执行"]
        Think["理解任务:<br/>这是竞品分析,<br/>Skill说要4步"]
        Step1["执行步骤1:<br/>调用GitHub MCP"]
        Step2["执行步骤2:<br/>调用Drive MCP"]
        Step3["执行步骤3:<br/>调用Web Search"]
        Step4["执行步骤4:<br/>汇总并格式化"]
    end
    
    subgraph MCP["MCP工具"]
        M1[GitHub MCP]
        M2[Drive MCP]
        M3[Web Search]
    end
    
    User --> Think
    Skill -.从cache读取.-> Think
    
    Think --> Step1
    Step1 --> Step2
    Step2 --> Step3
    Step3 --> Step4
    
    Step1 -.调用.-> M1
    Step2 -.调用.-> M2
    Step3 -.调用.-> M3
    
    M1 -.返回结果.-> Step1
    M2 -.返回结果.-> Step2
    M3 -.返回结果.-> Step3
    
    Step4 --> Output[输出报告]
    
    style Context fill:#e1f5ff
    style Agent fill:#fff4e1
    style MCP fill:#ffe1f5
```


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
