---
title: "一、Rules 相关知识简单回顾"
description: "AI Coding 工程实践思路探讨 （Rules+ Skill + MCP + CLI）"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI Coding 工程实践思路探讨 （Rules+ Skill + MCP + CLI）.md"
---
AI Coding 工程实践思路探讨 （Rules+ Skill + MCP + CLI）

#### 🧑‍🏫 案例作者：[@王庆方](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、测试、提示词、Sub-agent
#### 🔧 使用工具：Comate、Claude
#### 📒 案例概要：AI Coding工程实践：Agent工作流、工具分类与案例解析
**本文档视频讲解：**[AI Coding工程实践思路探讨](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/57694?isFromPc=1&reportLog=true?t=mention&mt=doc&dt=sdk)

上次分享内容：[平台端到端AI内化思路探讨（Rules + MCP）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/R26J56Iu2s/Wdrv5TjTzWILv4?t=mention&mt=doc&dt=doc)

# 一、Rules 相关知识简单回顾
## 1.1 Agentic AI 简介（Coding Agent 是 AI Coding 的基础）
 Agentic AI 课程：[https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbv/welcome!](https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbv/welcome!)

Agent 出现，将 AI 开发的重心从**“提示词工程”的**一轮全中模式（Zero-shot Prompting） 转向了多次迭代的 **“Agentic Workflows”。**

1. **性能飞跃：**GPT-3.5 在智能体工作流的加持下，其编程测试（HumanEval）表现甚至能超越 GPT-4。（代码生成准确率，从 **48%** 飙升至 **80%** 以上）
2. **迭代思维：不仅仅是提示词工程，**构建一个能自我修正的系统，比写出一个完美的提示词更重要。
    1. 引入Reflection：执行->观察->反思->修正；

3. **规划&工具使用：**
    1. Agent 会先做多步规划，应对多步骤、长时间跨度的复杂任务。
    2. AI 不再只靠猜，它知道自己什么时候“不知道”，并主动调用外部工具。

4. **muti-agent workflows（sub-agent）：**建设专家角色的sub-agent 协助工作；(第三章 展开说)

![](/personal-site-mvp/img/doc-placeholder.svg "")


听完课程，Agent 有几个关键点，是我们可以参与的，更好帮助我们利用好 coding agent。

* **预先备好 tools：**这里的tools 比较泛，包括了后面讲的 Rules、MCP、CLI、Skill、tools（模型自备） 等。如果大家使用 Agent 不准备这些tools，就相当于停留在第一个阶段。

![](/personal-site-mvp/img/doc-placeholder.svg "")
* **拆分任务 planning workflows：**将宏大的任务，类似于【**人类的工作逻辑】**，拆成几步（顺序执行）。（agent 本身也会这么做，我们拆的更细，防止他拆错）-- 【每个人做事的思路不同，区分度最高的一件事情，是关键核心】
* **外部反馈：**真实的外部反馈，会进一步提升效果。【写skill 的时候，多给一些例子或者参考，有结果后，澄清结果等】

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 1.2 概念澄清：Tools 的分类（Skills、Rules、MCP、CLI、tools）
内部讨论帖子：[https://news.family.baidu.com/businessTopic/36](https://news.family.baidu.com/businessTopic/36)

![](/personal-site-mvp/img/doc-placeholder.svg "")


**基本的Coding Agent 的组成：**

[流程图]


### **1.2.1 Skills 与 Rules 的区别（区分Coding Agent）**
 [AGENTS.md](https://agents.md/) 的前世今生，多家大厂和社区联合推动（OpenAI、Google、Cursor、Factory 等），为了解决 Agent 指令碎片化、多工具协作困难问题。

|工具 / 厂商|Agent 指令文件|位置 / 命名|核心作用|是否私有规范|
|-|-|-|-|-|
|Cursor|`.cursorrules` / `.cursor/rules/*.md`|项目根目录或 `.cursor/` 目录|定义代码风格、生成规则、Agent 行为约束|是|
|Claude Code (Anthropic)|`CLAUDE.md`|项目根目录|提供项目上下文、构建方式、注意事项|是|
|GitHub Copilot|`.github/copilot-instructions.md`|`.github/` 目录|指导 Copilot 生成和修改代码的规则|是|
|OpenAI Codex|`AGENTS.md`|项目根目录|统一 Agent 行为、构建、测试、规范说明|否（开放标准）|
|Google Gemini / Jules|`GEMINI.md`|项目根目录|提供给 Gemini Agent 的项目指引|是|
|**通用标准（社区）**|****`AGENTS.md`****|**项目根目录**|**跨工具统一 Agent 指令与上下文**|**否（开放标准）**|
|**百度 comate zulu**|** Rules.md**|`.comate/rules`****|定义代码风格、生成规则、Agent 行为约束|是|

|**Comate Zulu**|**Claude Code（Cursor）等**|
|-|-|
|Rules ≈ Skill|Skill 包含 Rules|
|zulu 没有像 Claude Code一样，细致的区分这两个概念，使用时都放在 .comate/rules/ 下面，反而是区分 Rules的不同类型：**信息类：**主要阐明“我有什么”，**用来增强模型上下文对业务知识的理解。****指令类：**按照指令完成一个完成功能，**告诉模型完成具体步骤。****约束类：**告诉模型什么能做什么不能做，**用来防止模型做一些事情。****索引类：**一系列Rules的集合，非具体的信息和指令，类似导读，**让模型决策选择使用。****注意：**每一个rules ，都需要注明 description（When to use），方便模型触发。![](/personal-site-mvp/img/doc-placeholder.svg "")| Claude 强调Skill 是特定完成某一种功能、能力的work flow ；**Skill：**主动能力，类似于，zulu 的 指令类，完成某一个事情；**Rules（reference）：**类似 zulu 的 信息类、约束类的Rules，会放在 ./reference 目录下，是被动知识，SKILL.md 的 workflow 步骤里会适当引用；**注意：**./reference/*.md 不写 description（When to use），只在模型需要时被动调用；**学习地址：****Agent Skills with Anthropic ******[https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/ldn5c3/introduction](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/ldn5c3/introduction)**git hub地址（Claude 内置的Skills 参考）：-- 开源版本**[https://github.com/anthropics/skills](https://github.com/anthropics/skills)|
|![](/personal-site-mvp/img/doc-placeholder.svg "")![主要阐明“我有什么”，用来增强模型上下文](/personal-site-mvp/img/doc-placeholder.svg "主要阐明“我有什么”，用来增强模型上下文")![按指令完成一个完整功能](/personal-site-mvp/img/doc-placeholder.svg "按指令完成一个完整功能")![防止模型做一些事情（正向激励、负向压制）](/personal-site-mvp/img/doc-placeholder.svg "防止模型做一些事情（正向激励、负向压制）")![Rules 的集合的非具体的信息和指令，方便模型引用，过滤无效或者不必要的信息，类似导读，描述怎么选](/personal-site-mvp/img/doc-placeholder.svg "Rules 的集合的非具体的信息和指令，方便模型引用，过滤无效或者不必要的信息，类似导读，描述怎么选")|Comate Zulu 适配 Claude 的 skill![](/personal-site-mvp/img/doc-placeholder.svg "")|

### 1.2.2 MCP 与CLI 与 tools
|**概念**|****|****|
|-|-|-|
|MCP|2024年11月，当 Anthropic 发布 MCP（Model Context Protocol）；我厂的mcp 广场：[https://console.cloud.baidu-int.com/onetool/square](https://console.cloud.baidu-int.com/onetool/square)![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")||
||**方式一：Streamable HTTP（远程服务型）**|**方式二： npx 启动（本地进程型）**|
||![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")[附件]|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")[附件]|
|CLI|最近出现MCP 的热度在下降的趋势：[MCP is dead. Long live the CLI ](https://ejholmes.github.io/2026/02/28/mcp-is-dead-long-live-the-cli.html)（MCP 已死，CLI 当立）的说法。-- 如果模型能够直接阅读官方文档并正确变成处理接口，那么在 MCP Server 中内置额外指令的必要性就会下降。（token 爆炸、response 引入歧义） OpenClaw 爆火，发现OpenClaw 不支持 MCP，仅支持 CLI。有Issue ，但是否做，还得继续看。[https://github.com/openclaw/openclaw/issues/8188](https://github.com/openclaw/openclaw/issues/8188)Anthropic 2025年11月也发布：[https://www.anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp)建议将 MCP Server 作为代码 API 提供（比如Doc 等），让 Agent 通过编写代码进行交互，而不是直接调用api；-- MCP 仅作为工具交互的通用标准。原本需要 150,000 tokens 的工作流，被压缩到约 2,000 tokens，减少了 98.7%； -- 还没问问题，token 已经消耗完了。CLI = Command Line Interface （工具命令的通用语言）.上述语境中的CLI，就是一个持久的服务器环境，让LLM可以在其中编写、执行、存储代码，可以允许访问网络、文件权限等。Claude Code CLI 和 Gemini CLI 是 **【命令行智能体】**![非交互模式](/personal-site-mvp/img/doc-placeholder.svg "非交互模式")![交互模式](/personal-site-mvp/img/doc-placeholder.svg "交互模式")Gemini3 Flash模型（免费体验）：查看配额：[https://aistudio.google.com/rate-limit?project=gen-lang-client-0133885084](https://aistudio.google.com/rate-limit?project=gen-lang-client-0133885084) 命令行登录google 账号 或者 申请API key 都能登陆申请API key：[https://aistudio.google.com/api-keys?project=gen-lang-client-0133885084](https://aistudio.google.com/api-keys?project=gen-lang-client-0133885084)||
|tools|一般指，模型自带的 funciton： [https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)![](/personal-site-mvp/img/doc-placeholder.svg "")||



**题外话：**欢迎大家，把可用的Skills 贡献到**小刚Claw**：[小刚Claw来了，解锁研发新范式](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/-JBYaHD72V/fafhLKlFlQgSJo?t=mention&mt=doc&dt=doc)，提升商业研发的整体研发效率。

# 二、案例介绍
Claude 官方建议【三级渐进式加载（Progressive Disclosure）】

1. **元数据 -- 必在上下文使用**
    1. skill 的 name：建议有限个词（小写） + “-” 链接，能描述功能（动词+ing）；
    2. skill 的 description 要写清楚：
        1. 该skill的功能；
        2. 什么时候触发；（可以用关键词触发）


2. **内容 -- 触发使用**
    1. skill 内容没有格式限制。
    2. 推荐包含以下部分：
        1. 分步骤说明；
        2. 输入格式、输出格式，或输入输出示例；
        3. 常见边界情况（edge cases）；

    3. 实用建议：
        1. 控制在 500 行以内；
        2. 将详细的参考资料拆分到单独文件：这里只保留基础内容，并链接到更高级或特定领域的内容
        3. SKILL.md 与 reference/ 在同一层目录（避免嵌套文件引用）
        4. **简洁至上（不要重复）、命令式语气（祈使句）、自由度匹配风险（高中低）：**
            1. 高自由度（文本指引）→ 多种方案都可以时
            2. 中自由度（伪代码/带参脚本）→ 有偏好模式但允许变化
            3. 低自由度（具体脚本，少量参数）→ 操作脆弱、必须严格执行时



3. **额外文件夹：-- agent 按需判断使用**
    1. /scripts ： 可执行脚本，说清楚是【执行】 还是 【参考】；
    2. /assets： 资产，比如文档模版、设计logo、表格schema等；
    3. /references：保持每个reference 的 *.md 文件聚焦**【单一主题】**，超过 300行（下图过期了），顶部添加目录；




学习地址：[https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)

![](/personal-site-mvp/img/doc-placeholder.svg "")
|**高自由度**|**中自由度**|**低自由度**|
|-|-|-|
|## 代码风格优化优化代码可读性，考虑以下方面：- 变量命名是否清晰- 函数是否过长需要拆分- 是否有重复逻辑可提取|## 生成 SQL 查询按以下模式生成查询：SELECT {需要的字段}FROM {表名}WHERE dt = '{最近的分区日期}'  AND {用户指定的过滤条件}ORDER BY {排序字段} DESCLIMIT {默认1000，用户可指定}注意：- 始终使用分区字段 dt 过滤- 大表必须加 LIMIT|## 部署到生产环境严格按以下步骤执行，不可跳过或调整顺序：1. 运行 `scripts/pre_check.py --env prod` 确认环境就绪2. 运行 `scripts/backup.sh` 备份当前版本3. 运行 `scripts/deploy.sh --version {version} --env prod`4. 运行 `scripts/health_check.py --timeout 60`5. 若健康检查失败，立即运行 `scripts/rollback.sh`|
|代码审查、方案撰写、架构建议|SQL 生成、API 调用、配置生成|生产部署、数据库迁移、风险操作|

## 2.1 自助报警排查（AFS 冷数据分析 -- 低自由度）
介绍scripts 用法

**示例：**分析 shaolin 集群 turing 账户 /user/turing_dataflow/ecom/dushuai/kr_siku_merge_table 路径的大头和冷数据情况

[附件]
## 2.2 Bigflow2Spark（史帕克MR2Spark 类似 -- 中自由度）
建议针对以下几种情况做保护（Rules 命令禁止操作，但被LLM绕过）：

1. Goal > Rules（目标压过规则），Goal 是优化查询，rules:不要改变表结构，但是，Agent推理认为，不加索引完不成，对线上数据库直接执行执行 CREATE INDEX；
2. 语义规避：rules : Do not delete database，但是，agent：“truncate ≠ delete”、“drop temp table is ok”、“recreate is fine”；
3. Tool abstraction 漏洞（MCP/Skill），skill 写：禁止删除用户数据，但 MCP tool 提供：cleanup_workspace()，agent：调用 cleanup，cleanup 内部删库；



1. 介绍高级特性Claude Code hooks 用法：[https://code.claude.com/docs/zh-CN/cli-reference](https://code.claude.com/docs/zh-CN/cli-reference)
    1. 注意：Hook 只能检查 Claude **直接执行**的命令文本，无法追踪子进程行为。-- 合理

2. Comate IDE 使用，需要自己多注意保护；

## 2.3  迁移任务（不阅读旧代码的情况下完成旧代码迁移到新架构 -- 高自由度）






# **三、附录：muti-agent workflows 介绍（sub-agent）**
##### **更高级用法（3周前提交的skill-creator skill，使用了Agentic AI 课程里讲的muti-agent workflow 模式）**
##### [https://github.com/anthropics/skills/pull/465/changes#diff-0fb7a28fe1c4a1e1ca3c344ef5d93020ab453409836311d6cb2b5425b9dc3a8f](https://github.com/anthropics/skills/pull/465/changes#diff-0fb7a28fe1c4a1e1ca3c344ef5d93020ab453409836311d6cb2b5425b9dc3a8f)
![3月19号截图](/personal-site-mvp/img/doc-placeholder.svg "3月19号截图")


|****|**name**|**Role**|
|-|-|-|
|analyzer.md|**Post-hoc Analyzer Agent**事后分析 Agent：分析盲测对比结果，理解**为什么胜者会赢**，并生成改进建议。|在盲比较器（blind comparator）决定胜者之后，Post-hoc Analyzer 会通过查看 skill 和执行 transcript 来“去盲”（unblind）结果。目标是提取**可执行的洞察（actionable insights）**：胜者为什么更好？败者如何改进？|
|comparator.md|Blind Comparator Agent盲比较Agent：在**不知道是哪一个 skill 生成输出的情况下**比较两个结果。|Blind Comparator 负责判断哪个输出更好地完成了评测任务。你会收到两个输出，标记为 A 和 B，但**你不知道它们分别来自哪个 skill**。这样可以避免对某个 skill 或实现方式产生偏见。你的判断**完全基于输出质量和任务完成情况**。|
|grader.md|**Grader Agent**评分Agent：对执行过程记录（transcript）和输出结果进行评估，判断是否满足预期（expectations）|Grader 会审查执行记录（transcript）和输出文件，然后判断每一条预期（expectation）是通过还是失败。请为每一个判断提供清晰的证据。你有两个职责：**对输出进行评分，以及对评测本身（evals）进行批判性审视**。一个“弱断言”得到通过评分，比没有评分更糟——它会制造虚假的信心。当你发现某个断言很容易被满足（没有区分度），或者存在重要结果却没有被任何断言覆盖时，请明确指出。|

![关键词：Running and evaluating test cases](/personal-site-mvp/img/doc-placeholder.svg "关键词：Running and evaluating test cases")
[流程图]


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
