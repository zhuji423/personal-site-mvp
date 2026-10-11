---
title: "1.引言"
description: "电商Agent Skill 实践：实现领域知识重用与工作流自动化"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\电商Agent Skill 实践：实现领域知识重用与工作流自动化.md"
---
电商Agent Skill 实践：实现领域知识重用与工作流自动化

#### 🧑‍🏫 案例作者：[@文胜平](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：知识加工、提示词、信息洞察、任务管理、数据分析、工作流自动化
#### 🔧 使用工具：OpenClaw、如流机器人、Cursor、Comate、Claude、知识库
#### 📒 案例概要：电商Agent Skills模块化扩展AI能力，实现领域知识重用与工作流自动化，提升效率。
[文档目录]


# 1.引言
## 1.1 Agent Skills 是什么
[Agent Skill](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/xtshFPEZoxNZYV?t=mention&mt=doc&dt=doc) - Claude Agent Skill（Claude 技能系统）于**2025 年 10 月 16 日**由 Anthropic 正式发布，同时推出了官方博客与技术文章进行 详细介绍[https://claude.com/blog/skills](https://claude.com/blog/skills)。2025 年 12 月 18 日，Anthropic 将其升级为开放标准（Open Standard），命名为 Agent Skills，推动跨平台兼容生态建设。



Agent Skills 是扩展 Claude 功能的模块化能力。每个 Skill 包含指令、元数据和可选资源（脚本、模板），Claude 在相关时会自动使用这些资源。



**为什么使用 Skills**

Skills 是可重用的、基于文件系统的资源，为 Claude 提供特定领域的专业知识：工作流、上下文和最佳实践，将通用代理转变为专家。与提示不同（提示是对话级别的一次性任务指令），Skills 按需加载，无需在多个对话中重复提供相同的指导。







**主要优势**：

* **专业化 Claude**：为特定领域的任务定制功能
* **减少重复**：创建一次，自动使用
* **组合功能**：结合 Skills 构建复杂工作流



**SKILL 文件组织结构  --  三层渐进式披露架构  YMAL定义 -> SKILL.md -> resource**

```
技能名称/
├── SKILL.md（必需）
│   ├── YAML frontmatter元数据（必需）
│   │   ├── name:（必需）
│   │   └── description:（必需）
│   └── Markdown说明（必需）
└── 捆绑资源（可选）
    ├── scripts/          - 可执行代码（Python/Bash等）
    ├── references/       - 旨在需要时加载到上下文的文档
    └── assets/           - 在输出中使用的文件（模板、图标、字体等）
```


**Skill示例**：

![](/personal-site-mvp/img/doc-placeholder.svg "")






**官网定义**： [https://agentskills.io/specification](https://agentskills.io/specification)

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 2.概述


## 2.1 Skills 生态


|**厂商**|**跟进时间**|**关键动作**|
|-|-|-|
|**OpenAI**|2025 年 12 月 12 日2025 年 12 月 20 日|・悄悄在 Codex CLI 和 ChatGPT 中加入 Skills 支持・在 Codex 文档中正式增补 Skills 支持・推出类似 Claude Skills 的功能，内部代号 "Hazelnuts"|
|**Cursor**|2025 年 12 月 18 日|・在 Anthropic 发布 Agent Skills 开放标准当天宣布支持・成为首批支持该开放标准的头部开发工具之一|
|**GitHub Copilot**|2025 年 12 月 18 日|・发布更新，正式支持 Agent Skills 开放标准・与 Claude Opus 4.5 的发布同步进行|



**补充说明**

1. **Claude Skills 核心特性**：采用简单 Markdown 文件、渐进式加载（令牌高效）、无需服务器部署、跨 Web / 桌面 / CLI 平台使用Anthropic。
2. **OpenAI 早期布局**：在 Claude Skills 发布前 10 天（2025 年 10 月 6 日），OpenAI 曾发布 AgentKit，为后续技能系统奠定基础。
3. **生态协同**：2025 年 12 月 9 日 Anthropic 将 MCP（模型上下文协议）捐赠给 Linux 基金会，12 月 18 日 Skills 成为开放标准，标志 AI 代理技术从 "军备竞赛" 转向 "标准化协作"。
4. **ChatGPT 正式版 Skills**：预计于 2026 年 1 月全面推出，将包含技能编辑器，并支持将现有自定义 GPT 转换为 Skill。



**Anthropics** : [https://github.com/anthropics/skills](https://github.com/anthropics/skills)

**Openai** : [https://github.com/openai/codex/blob/main/docs/skills.md](https://github.com/openai/codex/blob/main/docs/skills.md)



## 2.2 Skills 架构
Skills 在代码执行环境中运行，Claude 具有文件系统访问、bash 命令和代码执行功能。可以这样想：Skills 作为虚拟机上的目录存在，Claude 使用与您在计算机上导航文件相同的 bash 命令与它们交互。

![](/personal-site-mvp/img/doc-placeholder.svg "")




## 2.3 Agent Skill 与 MCP的对比
[AI Agent Skill 领域深度研究：MCP vs Prompt/Skills 对比分析](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/C4agfOM9IR2CaK?t=mention&mt=doc&dt=doc)（点击向原作者申请阅读权限）

### **Skill**
### **Mcp**
知识共享 —— 经验、最佳实践、工作流



* 轻量型 Markdown 文件 —— 全员可创建
* 渐进式加载 —— Token 使用更高效
* 无需服务器部署
* 跨端适配网页端 + 桌面端 + 命令行界面（多数能力模块均支持）

功能扩展 —— 对接各类应用程序接口、数据库、工具



* 需编写代码并完成服务器部署
* 启动时加载所有工具定义
* 适配复杂外部集成场景，能力强大
* 令牌消耗更高，部署流程更复杂



**核心要点**

Skill能力模块与多功能连接平台（MCP）互为补充。通过能力模块实现知识共享，借助多功能连接平台（MCP）完成功能扩展，二者协同使用能发挥最佳效果！

**Skills 更像“把 SOP 打包”**：流程、清单、产物格式这些东西，装上就能用。
**MCP 更像“统一接口”**：把 GitHub、Notion、浏览器、数据库这类外部系统能力接进来。



![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")




## 2.4 社区热门Skills排行榜 Top 20
数据来源：SkillsMP · 2026年1月19日   [https://skillsmp.com/](https://skillsmp.com/)

> 说明：热度值基于GitHub Stars和使用量综合计算，已剔除功能重复的Skills。


|**方向**|**Skill名称**|**热度**|**功能介绍**|
|-|-|-|-|
|**开发工作流类**|create-pr|169.7k|自动创建GitHub PR，格式化标题，通过CI校验|
|****|skill-lookup|142.6k|技能查找与安装器，问什么Skills都能找到|
|****|frontend-code-review|126.3k|前端代码审查，支持tsx/ts/js文件检查清单|
|****|component-refactoring|126.3k|组件重构专家，安全拆分和优化React组件|
|****|github-code-review|48.2k|GitHub代码审查+AI协调，多Agent协同评审|
|**AI/LLM开发类**|cache-components-expert|137.2k|缓存组件专家，优化LLM应用的缓存策略|
|****|opus-4.5-migration|47.2k|Opus 4.5迁移指南，升级现有Claude应用|
|****|confidence-check|19.8k|置信度检查，让Claude评估自己的回答可靠性|
|****|context-engineering|5.5k|上下文工程基础，优化Prompt设计|
|****|multi-agent-patterns|5.5k|多Agent架构模式，设计协作式AI系统|
|**************专项技术类**|dify-frontend-testing|124.9k|Dify前端测试，专为Dify平台优化|
|****|electron-chromium-upgrade|119.6k|Electron升级指南，Chromium版本迁移|
|****|zig-syscalls-bun|86k|Zig系统调用，Bun运行时底层开发|
|****|cloudflare-skill|2.8k|Cloudflare全平台开发，60+产品一站式指南|
|**技能创作与管理类**|skill-writer|96k|技能编写器，帮你创建高质量SKILL.md|
|****|skill-creator|38.5k|技能创建向导，从零开始设计Skills|
|****|llm-project-methodology|5.5k|LLM项目方法论，AI项目最佳实践|
|**综合框架类**|obra/superpowers|29.1k|超能力框架，TDD+YAGNI+DRY方法论全家桶|
|****|awesome-claude-skills|21.6k|社区精选合集，50+经过验证的Skills|
|****|skillport|229|跨Agent技能管理器，一处管理多处使用|



# 3.实践案例
## 3.0 案例概述
**痛点**

* **临时性需求**：临时脚本处理、大量统计分析需求，影响正常项目进度
* **重复性基础工作**：需要重复人工跟进，经验难以沉淀和复用

### 
**实践场景**

|**应用场景**|**场景说明**|**实践案例**|**传统处理方式耗时**|**Agent Skill 辅助处理耗时**|**使用人群**|**适用度**|
|-|-|-|-|-|-|-|
|**临时简易任务**|简单的需求编排，数据处理场景|案例1: 代码千行Bug率分析案例2: 团队迭代情况分析|1 - 2小时|5-30分钟|产品、运营 等平常需要频繁处理 标准化文档的 角色**仅使用**|非常高|
|**知识梳理任务**|业务SOP沉淀，skill创建于管理|案例3: Skill创建与管理案例4: Skill创建工具使用案例5: 结合MCP的Skill开发|30分钟-数小时|约2分钟|有较强AI使用经验的 角色；|高|
|**临时排查任务**|产品一句话需求，bug排查|案例6: 一句话产品需求生产skill|0.5 - 1天|2小时内|基础使用AI 进行 单系统开发的角色|高|
|**中等难度项目**|多种业务场景，复杂需求编排逻辑|从**vibe coding -> spec coding -> spec + skill**   ，3个阶段， 逐步使用不同的方案，实践当前AI Coding 比较热门的知识，|1-2 天|0.5天内|深度使用AI 进行 跨系统的角色|中|





**内部实践：**

[文件页：baidu/ps-shangpin/Agent-Skills  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/Agent-Skills/tree/master?t=mention&mt=doc&dt=sdk)



## 3.1 报告分析 - 周报/例会等场景
### 3.1.1 代码千行Bug率分析
### **未使用Skill**
### **使用Skill**
**处理流程：**

1.人工导出数据，准备数据集

2.人工理解指标定义

3.摘录 或 使用已处理好的脚本执行

4.人工分析汇总报告



耗时： 约30分钟

**处理流程：**

1.人工导出数据，准备数据集 （ 看获取数据集成本，是否可集成至skill内）

2.将数据放入指定目录文件夹内

3.使用 xxx技能 ，按照指定模板生成报告





耗时：约5分钟

* **开发环境**： Cursor + Auto ( GPT 5.2 Codex )
* **效果：**

数据源 ： [月度效能统计](https://sugar.baidu-int.com/group/measure/report/r_1013e-5tgj8lmr-o84v72?__scp__=Baidu&conditions=%7B%22time_type%22%3A%22monthly%22%2C%22date_range%22%3A%222026-01-01~2026-01-31%22%2C%22dep_name%22%3A%22%E7%94%B5%E5%95%86-%E6%95%B4%E4%BD%93%22%2C%22has_wb%22%3A%221%22%7D) 

![原始数据 - 约100人数据](/personal-site-mvp/img/doc-placeholder.svg "原始数据 - 约100人数据")
![分析结论 - 指定方向13人统计](/personal-site-mvp/img/doc-placeholder.svg "分析结论 - 指定方向13人统计")


* **Skill 概览**

 - SKILL.md 详情

[附件]
![](/personal-site-mvp/img/doc-placeholder.svg "")


**使用方式：** 输入咒语  ** 使用 bug-evaluation  skill 分析   **** [使用 skill-name skill 分析]**

![](/personal-site-mvp/img/doc-placeholder.svg "")


### 3.1.2 团队当前迭代情况分析
当前电商搜索团队以双周迭代形式进行 产品需求的管理，为保障业务迭代的顺利进行，一般由方向PMO,产研负责人进行统计分析，但相关分析操作涉及的**口径多且复杂**，每周大概需要 **0.5-1小时**在整理相关材料上，且相关分析经验内部沉淀/分享有一定难度；  在沉淀相关skill后，无相关分析经验的同学，在**5分钟内**可以完成相关内容整理；   

* **开发环境：** Cursor + Auto ( GPT 5.2 Codex )
* **效果：**

![](/personal-site-mvp/img/doc-placeholder.svg "")


* **整体流程**： 参考3.1.1 步骤，基本一致； 主要差别在于 数据源获取，以及口径定义

**Skill说明**

![SKILL 说明](/personal-site-mvp/img/doc-placeholder.svg "SKILL 说明")
**CSV输入数据集示例： 从icafe 导出**

![](/personal-site-mvp/img/doc-placeholder.svg "")


**业务口径定义：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 3.2 创建Skill 
### 3.2.1  使用skill 创建 skill  ( 非套娃 )
### 
### **未使用Skill**
### **使用Skill**
**处理流程：**

1.人工整理流程，SOP

2.编写SKILL.MD

3.编写脚本 - 可能需要



耗时： 约30分钟 - x 小时不等 （ 新人刚开始接触，可能无从下手）

**处理流程：**

1. 人工整理流程，SOP
2. 使用 skill-creator 工具创建 skill
3. 等待 skill按照默认格式创建





耗时：约2分钟



* **开发环境：** Comate Zulu + Claude 4.5 sonnet



#### **Step1: 将skill-creator  加载到本地目录**
* **skill-creator：**[文件页：baidu/ps-shangpin/Agent-Skills  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/Agent-Skills/blob/master/Skill-manage/skill-creator/SKILL.md?t=mention&mt=doc&dt=sdk) 

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### Step2：使用本地的 skill-creator 创建 目标skill
![](/personal-site-mvp/img/doc-placeholder.svg "")




### 3.2.2 结合MCP 的Skill - 向icafe创建卡片
* **开发环境**： Comate Zulu + Claude 4.5 sonnet

#### **效果预览：**
* 使用skill
* skill中调用mcp 

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")




**Icafe空间地址：**

https://console.cloud.baidu-int.com/devops/icafe/space/lumos/planbox/1101792/issue?viewId=148657
![](/personal-site-mvp/img/doc-placeholder.svg "")


#### Step1  添加mcp
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")




#### Step2: 创建skill & 拓展skill能力 
**参考3.2.1 step2截图** ，在相关基础上 ， 如遇见skill能力不满足 ，可优化补齐

![](/personal-site-mvp/img/doc-placeholder.svg "")


## 3.3 日常工具沉淀
### 3.3.1 一句话的产品需求 - 沉淀为skill
**产品需求**：希望返回这批出卡Q下的商品相关信息，包括商品URL，到手价，原价及其他价格信息，各种优惠券信息等，目的是看下目前到手价的数据是否跟页面价格差很多，是否需要其他优惠券计算逻辑

**需求整理-RD**：[热卖卡Q商品信息分析](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/UGBstI2e9v2udZ?t=mention&mt=doc&dt=doc) - 人工整理 ， 且包含两个不同接口的  get请求链接 ， 输出字段 ， 输出内容字段对齐；  该功能后续产品可能需要周期性的使用，进行评估任务

![](/personal-site-mvp/img/doc-placeholder.svg "")
**主要功能点**：

* 调用热卖卡商品接口获取数据
* 调用BMC商品接口获取数据
* 热卖卡商品数据 与  BMC商品数据进行整合，数据对比



**使用模型对比：**由于claude 4.5 模型整体较贵（单Query预估价格 ￥10元） ，同时验证近期上线的新模型GLM4/7 ，进行验证效果；[Comate Zulu、Ducc智能体价格和使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/rNpMbaN7tz7o2Z?t=mention&mt=doc&dt=doc)

|****|**ducc + glm4.7 （默认可内部使用模型）**|**ducc+  claude 4.5 sonnet **|
|-|-|-|
|**体验**|整体花了差不多10分钟 ，未成功生成 |一次性开发完成 ，  中途补充的 BMC接口调用的  http-header 也能正常识别|
|**主要问题**|响应时间问题：内置模型响应较慢编码问题：卡在接口调用的curl  http-header设置阶段|暂无|
|**交付内容**|仅 指定 skill 内容 ，py文件，无其他额外验证产出|有明确交付物情况![](/personal-site-mvp/img/doc-placeholder.svg "")|
|其他|简单脚本任务处理OK |其中这一段 是感觉比较惊艳的 ，【由于有1000个查询词，这个任务会需要一些时间（大约16-20分钟，因为每个请求间隔1秒）】，需求中并未提到，但是claude自动补充完善在py文件中了![](/personal-site-mvp/img/doc-placeholder.svg "")|





### **输入**
### **输出**
[热卖卡Q商品信息分析](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/UGBstI2e9v2udZ?t=mention&mt=doc&dt=doc)**，导出为 plan.md **

```
# 任务 
根据 @cps_goods_diff/plan.md  任务内容 ， @cps_goods_diff/SKILL.md  skill规划 ，数据输入  @cps_goods_diff/assets/query.txt   完成整个skill 开发 ，  

# 要求
1. 先明确任务方案
2. 实际进行开发 ，根据skill-creator 规范
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
**最终CSV文件：**

![](/personal-site-mvp/img/doc-placeholder.svg "")
**SKILL.MD文件**

![](/personal-site-mvp/img/doc-placeholder.svg "")




### 3.3.2 常用的编码能力 - 沉淀为skill
**应用场景： **日常的 固定的编码流程，工作处理，可以沉淀为 skill ，提升大模型指令遵循的 准确性； 例如 指定模块编码 （mvc模式下，新增一个接口调用） 、 CR 、埋点；



**prompt:**

```
使用skill-creator 沉淀一个 gdp 框架 ral 网络请求的skill,参考
/Users/wen/repository/baidu/ps-shangpin/context-mcp/conf/servicer/qianfan.toml相关任务
```
![](/personal-site-mvp/img/doc-placeholder.svg "")


**输出： **主要还是以模板化的思路，提供明确的案例，降低大模型幻觉，保证代码统一性；（可根据每个团队规范，自由变更）

**解决的问题**：部分老项目中，比如简单的 CRUD功能中 ，包含标准流程，但新增中可能 部分字段存在差异 ，通过此方式，保留主体流程准确 ， 部分细节内容根据 具体的  接口/输入的 变更 ，大模型自行理解后完成代码开发；

skill 地址： [文件页：baidu/ps-shangpin/Agent-Skills  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/Agent-Skills/blob/master/Code/gdp/gdp-ral-client/SKILL.md?t=mention&mt=doc&dt=sdk)

![](/personal-site-mvp/img/doc-placeholder.svg "")




### 






## 3.4 复杂业务场景下的使用skill
以下介绍说明 ， 通过从不同方式，进行3个需求的开发，包含前后端开发的案例2个， MCP工具开发1个； 

从**vibe coding -> spec coding -> spec + skill**   ，3个阶段， 逐步使用不同的方案，实践当前AI Coding 比较热门的知识， 

|****|**实现方式**|**文档**|**效果**|
|-|-|-|-|
|**阶段一：vibe coding**|vibe方式 + rules 结合|[🌟电商产研AI Coding实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/t0Wg1AdIFUwIoJ?t=mention&mt=doc&dt=doc)|内容审核  [https://ecbase.baidu-int.com/aivideo/spu/list](https://ecbase.baidu-int.com/aivideo/spu/list)![](/personal-site-mvp/img/doc-placeholder.svg "")|
|**阶段二：spec coding**|以SPEC模式来优化整体研发效果|[⭐️ 电商Comate Spec模式实践 - 从 VibeCoding 到 SpecCoding](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/IdUVi69h2Oh3w7?t=mention&mt=doc&dt=doc)|MCP工具开发 ，数据库查询工具![](/personal-site-mvp/img/doc-placeholder.svg "")|
|**阶段三：spec + skill 结合**|整体先试用spec模式，指定场景使用skill 完成|****[⭐️ 电商本地知识工程实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/C9U3wC_9skbauC?t=mention&mt=doc&dt=doc)|**知识库平台开发**![](/personal-site-mvp/img/doc-placeholder.svg "")|



  



**电商知识库平台前后端功能开发**

由于属于跨项目应用，Cursor / Kiro 在此场景下，目前支持较好 ；    本次使用了 Kiro 作为验证； [⭐️ Kiro Spec实践 - 性价比/效率的选择](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/PMjJTwrwgPJeuN?t=mention&mt=doc&dt=doc)

||**说明**|**截图**|
|-|-|-|
|**创建spec任务**|使用 spec 模式 + skill 方式，进行功能开发；  skill 为提前通过 代码库逻辑沉淀 ；|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|**使用skill 能力进行编码**||![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|**功能验证**||![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|**实际效果**||![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|













## 3.5 Openclaw 中使用Skill结合
**痛点**：如何将知识有效构建/应用到实际业务场景中，如何让用户更方便的使用；  通过Openclaw可以快速应用；





**内容详情参考**：[🦞电商Openclaw养殖经验 - 半天构建了一个简易企业知识库的问答能力](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/kyAZfxp3u3Bs30?t=mention&mt=doc&dt=doc)

通过前置的如流知识库授权，进行指定知识库问答内容；可关联 员工自己的如流知识库权限；





**提示词：**

阿拉丁平台是百度内部系统  [阿拉丁平台使用指南📚](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/uXaL-WkWdt/DnAv7zkcCc/6hBZoq-oq7jE38?t=mention&mt=doc&dt=doc)

遍历访问对应链接内所有关联链接内容，学习整体阿拉丁技能知识 ， 构建 阿拉丁系统的知识 



**输入示例：**

![](/personal-site-mvp/img/doc-placeholder.svg "")




**问答效果**：

![](/personal-site-mvp/img/doc-placeholder.svg "")




# 4.Skill 进阶
## 4.1 Skill 管理
Agent Skill 是智能体（Agent）针对特定任务的**可执行、可复用、可组合的具象化能力模块**，是连接大模型通用认知能力与实际业务落地的核心桥梁，其核心价值在于将大模型的 “泛化理解” 转化为 “精准执行”。

**现状**：目前对于大多数同学而言，还处于使用的初级阶段，以本地使用为主； 主要诉求为想知道有哪些工具，本地如何方便管理，以下介绍好用的网站、Skill 看方便大家的使用；





### 4.1.1 skill 安装管理器 
目前市面上的AI编程工具实在有些太多了，我自己就安装有`Cursor`, `Kiro`, `Antigravity`  , `Comate` 等等。近段时间，skills出来后，各种AI IDE如果需要添加，配置skills就会显得非常麻烦。有没有一个方法，可以**一次性安装配置skill给每个IDE进行使用**呢？ Vercel Labs 团队的`find-skill` 的开源项目，正是解决这个痛点的。并且还同步上线了一个skills 市场。使用`add-skill` 可以方便快捷安装技能包.

[https://skills.sh](https://skills.sh)

![网站列表页](/personal-site-mvp/img/doc-placeholder.svg "网站列表页")
![安装命令](/personal-site-mvp/img/doc-placeholder.svg "安装命令")
### 4.1.2 本地 skill 管理
当前现状下，大部分的skill能力还是主要以存储在本地的形式进行开发和使用，并未形成统一的规范，因此当务之急是快速有一个版本的 skill管理器，能够知晓当前存在的skill情况；



搜索电商产研本地skill ： [文件页：baidu/ps-shangpin/Agent-Skills  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/Agent-Skills/blob/master/README.md?t=mention&mt=doc&dt=sdk)

#### **SKILL 管理能力**
![](/personal-site-mvp/img/doc-placeholder.svg "")


#### ** 本地SKILL分析结论**
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 
### 4.1.3 [Skills（Onetool平台）使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/hIjfMHbFLJkYcW?t=mention&mt=doc&dt=doc)
[Skills使用指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/LnaYMVuaJzUEyt?t=mention&mt=doc&dt=doc)****

**Step1. 定位目标 Skill**：可通过 Skill 页面提供的**分类场景导航**及**关键词搜索能力**，快速定位并筛选符合业务需求的目标 Skill。Skill卡片包含名称、简介、场景。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**Step2. 进入 Skill 详情页查看信息**：点击 Skill 列表页中的 Skill 卡片进入详情页，用户可查看该 Skill 的**基础信息与使用说明**，包括名称、适用场景、发布人、联系人、功能简介、详细文档、安装命令，以及创建时间与更新时间。

![](/personal-site-mvp/img/doc-placeholder.svg "")
**Step3. 复制安装命令并在Zulu上使用**：在 Skill 详情页中复制对应的安装命令，并在 Zulu 终端环境中执行该命令，即可完成 Skill 的安装。

![](/personal-site-mvp/img/doc-placeholder.svg "")


#### 


### 4.1.4 Openclaw hub
[OpenClaw「App」榜单，国产Skill下载量冲上第一：能给龙虾接入现实世界](https://mp.weixin.qq.com/s/rbigQZU5XyoCWNd2P6sJ9Q?t=mention&mt=doc&dt=sdk)

[百度搜索Skill登顶ClawHub全球第一：3.6万次下载背后的国产AI搜索革命](https://mp.weixin.qq.com/s/hcAekzJsB5yBHwNt5e4PFQ?t=mention&mt=doc&dt=sdk)



**地址**：[https://clawhub.ai/](https://clawhub.ai/)

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


有趣的是，百度对于开源社区的合作态度，最近也得到了 OpenClaw 原作者 Peter Steinberger 点赞。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 
## 4.2 元技能
**元技能（Meta‑Skill）** 是**管理、创建、发现、组合、迭代其他技能**的高阶能力，是 AI Agent 与个人能力系统的 “操作系统”。

### 一、元技能的核心定义
* **本质**：**关于技能的技能**，是能力的 “底层引擎”。
* **类比**：普通技能是 “App”，元技能是 “OS”；普通技能解决具体问题，元技能让你**拥有、管理、进化能力**。
* **核心价值**：实现**能力自治、自我扩展、持续进化**。



### 二、核心元技能详解（含自我进化、元技能自管理类）
|元技能名称|定位|核心功能|工作流程|典型场景|
|-|-|-|-|-|
|find‑skill（技能发现/检索）|AI/Agent的技能搜索引擎+商店[https://skills.sh/vercel-labs/skills/find-skills](https://skills.sh/vercel-labs/skills/find-skills)|1. 从海量技能库中精准匹配可用技能；2. 自动检索、评估、安装技能；3. 让Agent从“被动执行”变为主动发现能力|1. 用户提出需求（如“优化React性能”）；2. 自动激活`find‑skill`，检索技能生态；3. 返回匹配结果+安装命令；4. 一键安装并调用|1. 不知道有什么技能可用时；2. 快速扩展Agent能力边界；3. 动态适配新任务需求|
|skill‑creator（技能创造者）|创建技能的元技能，是自我进化的核心引擎[https://skills.sh/anthropics/skills/skill-creator](https://skills.sh/anthropics/skills/skill-creator)|1. 零代码/低代码生成标准Skill包；2. 内置创建→测试→评估→迭代闭环；3. 支持自定义工作流、复杂逻辑、多步骤自动化；4. 实现能力自我复制与扩展|1. 捕获意图：明确功能、触发条件、输出格式；2. 访谈研究：定义边界、输入输出、成功标准；3. 编写草稿：自动生成`SKILL.md`+配置文件；4. 测试优化：AI辅助调试、迭代；5. 发布集成：打包、安装、上线|1. 把个人工作流封装为可复用Skill；2. 让Agent自主生成新能力；3. 构建专属能力生态|
|self-improve-agent（自我进化）|Agent能力迭代的核心元技能，实现自我优化升级[https://skills.sh/charon-fan/agent-playbook/self-improving-agent](https://skills.sh/charon-fan/agent-playbook/self-improving-agent)|1. 自动收集技能运行反馈数据；2. 分析能力短板与优化空间；3. 迭代技能逻辑、提升执行效率；4. 联动其他元技能完成自我升级；5. 记录进化轨迹，形成迭代闭环|1. 技能执行完成后，自动收集反馈；2. 对比预期效果与实际结果，定位不足；3. 调用skill-optimizer优化技能逻辑；4. 测试优化后的技能，验证效果；5. 固化优化成果，进入下一轮进化循环|1. 技能执行效率偏低时；2. 任务需求变更，需适配新场景；3. 发现技能存在漏洞或不足；4. 长期使用后，需优化技能性能|





**内容可到 Onetool平台下载**

[https://console.cloud.baidu-int.com/onetool/skills](https://console.cloud.baidu-int.com/onetool/skills)

![](/personal-site-mvp/img/doc-placeholder.svg "")




## 4.3 Skill 加载机制
### 4.3.1  Claude Code  skill 加载机制 （mac 为例） 
#### 4.3.1.1 配置形式
Claude Code 在 macOS 系统中的安装和配置文件结构如下：

**全局配置目录**：

```
~/.claude/
```
主要配置文件包括：

* config.json：全局配置文件
* settings.json：用户设置文件
* [CLAUDE.md](http://CLAUDE.md)：全局记忆文件
* history.jsonl：对话历史记录

**技能存储目录**：

```
~/.claude/skills/
```
**插件目录**：

```
~/.claude/plugins/
```
Claude Code 支持通过 Homebrew 安装，执行以下命令即可完成安装：

```
brew install claude-code
```
#### 4.3.1.2 三层渐进式披露架构
Claude Code 的 skill 加载机制采用了独特的**三层渐进式披露（Progressive Disclosure）架构**：

**Level 1 - 元数据层**：

技能名称和描述预加载在系统提示中，使 Claude 无需加载全部内容即可了解可用技能。这一层级的信息在系统启动时加载，占用极少的上下文空间。** --  YMAL定义部分**

**Level 2 - 核心指令层**：

完整的 [skill.md](http://skill.md) 文件仅在 Claude 判断技能适用于当前任务时加载。这种按需加载机制大大提高了上下文窗口的使用效率。 **-- SKILL.md**

**Level 3 - 资源层**： -- **assets / references / scripts**

支持按需加载的补充文档和资源文件。

以下是 Claude Code 技能定义的示例：

```
---
name: database-migration
description: 数据库迁移自动化技能
version: 1.0.0
author: Claude Team
---

# 数据库迁移技能

## 功能概述
本技能提供自动化数据库迁移功能，支持以下数据库类型：
- PostgreSQL
- MySQL
- SQLite

## 触发条件
当用户在对话中提及"数据库迁移"、"schema变更"或"database migration"时激活。

## 操作流程
1. 分析当前数据库连接配置
2. 检测schema变更
3. 生成迁移脚本
4. 执行迁移前验证
5. 执行数据库迁移
6. 生成迁移报告
```


### 4.3.2 IDE加载机制原理
[主流AI IDE/Agent系统（Cursor、Claude Code、Kiro、Codex、Antigravity）的skill 加载机制](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/BTO10w8OoeIWXS?t=mention&mt=doc&dt=doc)

随着AI驱动的开发环境向**多工具协同**、**统一技能生态**演进，Cursor、Claude Code、Kiro、Codex、Antigravity五大主流AI IDE/Agent系统在macOS平台的技能加载机制，成为决定开发效率与工具兼容性的核心。同时，`find-skill`（Vercel Labs出品）作为统一技能管理工具，通过**目录共享、符号链接、多源聚合**能力，实现了多平台技能的互通与统一管理。

本研究将深度拆解五大系统在macOS下的**技能加载核心原理、目录结构、配置方案**，并完整集成`find-skill`的多平台关联逻辑，补充网页端接入方案，形成覆盖“本地加载-跨平台同步-网页管理”的完整技术体系。



#### 4.3.2.1 基础目录架构（macOS 示例）
主流AI工具在macOS下均遵循**“应用程序目录+用户数据目录”**的双路径规范，技能存储严格区分**全局（跨项目复用）**与**项目级（当前项目专属）**两个层级。

|系统|全局技能目录|项目级技能目录|应用程序路径|
|-|-|-|-|
|Cursor|`~/.cursor/skills/`|`./.cursor/skills/`|`/Applications/Cursor.app`|
|Claude Code|`~/.claude/skills/`|`./.claude/skills/`|（通过Homebrew安装，CLI工具）|
|Kiro|`~/.kiro/skills/`|`./.kiro/skills/`|`/Applications/Kiro.app`|
|Codex|`~/.codex/skills/`|`./.codex/skills/`|（通过npm/Homebrew安装）|
|Antigravity|`~/.gemini/antigravity/skills/`|`./.agent/skills/`|`/Applications/Antigravity.app`|

#### 4.3.2.1 五大系统加载机制核心差异
|维度|Cursor|Claude Code|Kiro|Codex|Antigravity|
|-|-|-|-|-|-|
|加载策略|渐进式披露 + 热重载|三层分层加载 + MCP|语义驱动按需加载|权限延迟编译|模块化动态加载|
|作用域层级|项目级 + 全局级（兼容其他平台）|全局级（项目级需手动配置）|工作区级 + 全局级|项目级 + 插件级|工作区级 + 全局级|
|macOS 适配特性|进程分离、arm64 架构支持|MCP 协议集成 macOS 工具|轻量 GUI、语义匹配优化|沙箱权限适配、Homebrew 路径支持|16 个专业代理、预制 Skill Kit|
|热重载支持|原生支持（FSEvents）|支持（文件监控）|支持（模式切换触发）|需插件支持|支持（模块热替换）|





![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 5.后续计划
## 5.1 Skill沉淀 & 托管：
* 沉淀更多结合 当前业务，可实际落地的skill，赋能业务
* skill 托管能力，编写更多业务skill 在onetool托管，提升效率



## 5.2 Skill 编排能力
参考类似 superpower 的 skill编排能力，在 日常业务双周产研需求迭代中，落地优秀实践案例，优化&解决流程卡点，真正实现 全链路提效；



## 5.3 Skill 的应用拓展
* 对话式方向： 如流 Openclaw ，
* code agent 方向： comate / ducc IDE工具 持续研究使用









# 参考
skill 社区进展发展非常快 ，初次写文档的时间为 1月中旬，陆续沉淀更多实践内容 已经到 3月中旬， 各种新的内容层出不穷，需要多多实践； 





[2026年Claude Code Skills排行榜：Top 20完整版（已去重）](https://mp.weixin.qq.com/s/DZMbz7rJ4hjEl7NhCA9OqQ?t=mention&mt=doc&dt=sdk)

[我们花了两天时间，终于造出了能自我进化的Skills管理器。](https://mp.weixin.qq.com/s/hCN9UV_R4YVIz9AI6gyOrQ?t=mention&mt=doc&dt=sdk)





**更多团队实践沉淀参考：**

[AI-Coding-Topic分享](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/1MxrXIeQB-1zzC?t=mention&mt=doc&dt=doc)

![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
