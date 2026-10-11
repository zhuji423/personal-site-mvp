---
title: "一、Coding Agent 技巧"
description: "Coding Agent技巧&Agent Skills初探"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Coding Agent技巧&Agent Skills初探.md"
---
Coding Agent技巧&Agent Skills初探

#### 🧑‍🏫 案例作者：[@王同森](https://ku.baidu-int.com?t=mention&mt=contact&id=eff5bb30-fda7-11f0-82b9-a94b94b98b9c)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了Coding Agent的使用技巧，强调任务专注性和4S原则，避免角色限定和过长上下文。同时，介绍了Agent Skills的概念，通过结构化流程提升AI编码的专业性和效率。详细解释了Skills的基本用法、高级特性（reference与script）、与其他技术的对比，以及应用场景和优缺点。旨在帮助开发者利用Skills实现更精准、高效的AI编码。
**本文档视频讲解：**[Coding Agent技巧&Agent Skills初探](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/57205?activityId=8747?t=mention&mt=doc&dt=sdk)

# 一、Coding Agent 技巧


# 1、**Coding Agent的核心：一切都是Context**
#### Context 示意图
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### Agent底层本质是各类「文本」、「图片」等内容的拼装
#### 图中Context，既他们来自于「广义」的文件系统
#### 所有的Tool都是获取Context的手段，既检索、列表、读取


## Coding Agent 技巧 - 专注任务
### 三段式
* **第一段：****背景信息 - 重要**
    * 给足上下文（文件、图片、目录、规则等等）- 可以直接添加
    * 使用文字充分解释背景

* **第二段：描述****本次任务的业务逻辑 - 非常非常重要**
    * 分点描述，讲述业务的实现过程、条件
    * 足够细化，细化到具体的文件、类、函数、属性等

* **第三段：最后收尾，告诉Agent****从哪里开始****进行分析和生成（有时会和背景重合）**
    * 如告诉Agent写代码的起始文件：所有的代码生成从对底层的SQL语句编写开始、所有的代码从xxxx文件开始
    * 如告诉Agent做任务分析的入口：你要先检索互联网相关的知识、你要先深度阅读本仓库的根目录




![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")




### 4S 原则
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 注意与示例
### 注意
* ❌ 角色限定类：你是一个计算机编程专家。。。
    * Coding Agent 这些软件，实际上已经内置有非常精巧的提示词了，只需要专注任务，加了之后反而可能影响效果
    * 如果不是编程相关的，可以增加这个角色限定

* ❌ 一直使用同一个上下文窗口
    * 上下文窗口是有一定限制的，目前厂内的 comate 一般设置的是 128k、200K，上下文越长的情况下，输出越慢且效果不好




### 示例
* 通过这些官方提示词可以看出来，绝大多数都是专注任务，明确说明要去做什么

[Claude 官方提示词，中文版（含API Prompt）](https://mp.weixin.qq.com/s/rdKcT76ayfV-H9wkfLVaJQ?t=mention&mt=doc&dt=sdk)



# 二、Agent Skills
## 概念——什么是 Agent skills
#### 最最最通俗的理解：一个执行流程的使用说明（其实还是 prompt，只是使用方式不一样）


### 目的
* **让 AI 从"什么都懂一点"的通用助手，变成"这件事我熟"的领域专家。**
* skills 通过将团队专业知识固化为可跨项目跨团队复用的 Skill，实现**一次配置永久复用**、**按需加载知识节省 Token**，同时以固定流程规范解决 AI 编码不符合团队规则、重复劳动、上下文浪费、能力不可复用及输出质量不稳定的问题。



### 举例
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


* 此时就会有一个疑问，这不是就是平常写的 system prompt 这种形式吗？
* 不急，我们先体验一把试试，后面再去进行。



## 基本用法
### skills 结构介绍
![](/personal-site-mvp/img/doc-placeholder.svg "")


### 使用过程 - ducc
##### 自己编写/ copy 一份已有的 skill.md 文件，/Users/用户名/.claude/skills/mcp-builder/SKILL.md
* 每一个 skill 最好放在自己单独的目录中，文件夹名字最好与 skill 的元数据部分保持一致
* .claude 这个文件夹可能看不到，需要 command + shift + .  才可以显示隐藏（安装过 commate）
* 比如这里，我从 [https://github.com/ComposioHQ/awesome-claude-skills?tab=readme-ov-file#](https://github.com/ComposioHQ/awesome-claude-skills?tab=readme-ov-file#) 下载了几个我用来演示的 skills

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 打开 ducc （终端或者界面都可以）
* 询问下有什么 

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 基本使用
* 直接在 ducc 中**告诉需要他帮你完成的任务**
* 通过对话可知，他可以自动调用相关的 skills，然后按照这个过程实现相应的任务。

![](/personal-site-mvp/img/doc-placeholder.svg "")


* 此时之前的疑问我们还是没有解决，下面我们进行基本原理的解释。



## 基本原理
#### 最大特点：渐进式披露 - 按需加载
* 当一个 Agent 去解决用户提出的要求的时候，首先会去**获取所有的 skills 的元数据（也就是简介）**
    * **并没有把所有的 skills 内容全部加载到上下文中**

* 拿到 skills 列表之后，Agent 决定**使用哪一个 skill 比较合适**
* Agent 去拿对应的 **Skill，获取完整的相应任务的流程实现**
* Agent 按照 skills 去逐步完成相应的任务

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 高级用法 - reference 与 script
### reference 与 script 都是 skills 中的高级用法，都是按需中的按需。
![](/personal-site-mvp/img/doc-placeholder.svg "")


### 区别
|**对比维度**|**Reference（****参考资料****）**|**Script（****可执行脚本****）**|
|-|-|-|
|**本质**|条件触发的补充资料文件|可执行的代码脚本|
|**核心作用**|提供 Claude 需要参考的文档资料|自动化执行特定任务|
|**内容类型**|文档、说明、指南、模板等文本内容|Python、Bash 等可执行代码|
|**加载时机**|按需读取（任务满足预设条件时）|按需执行（用户触发特定需求时）|
|**上下文占用**|**占用上下文窗口（需要读取到模型）**|**几乎不占用（仅执行不读取）**|
|**典型场景**|• API 文档
• 写作规范
• 样式指南
• 流程模板|• PDF 生成
• 文件上传
• 数据处理
• 格式转换|
|**触发方式**|在 SKILL.md 中设置条件触发规则|在 SKILL.md 中定义执行指令|
|**优势**|• 知识复用
• 标准化参考
• 避免重复解释|• 自动化执行
• 确定性结果
• 节省 Token|



## 对比
|对比维度|**Skills（技能）**|**Subagents（子智能体）**|**MCP（模型上下文协议）**|**Rules（规则）**|
|-|-|-|-|-|
|**本质**|可复用的能力文件夹|独立的 AI 实例|外部系统连接协议|轻量级配置规则|
|**核心定位**|教 AI** "怎么做"**|专门干某件事的 AI Agent|接通**外部数据/工具**|简单的**行为约束**|
|**主要内容**|SKILL.md + scripts + references + assets|独立系统提示 + 工具权限|标准化的**获取信息**的接口/工具|简单指令/约束|
|**触发方式**|**自动触发**（场景识别）|**手动创建**（显式调度）|**工具调用**|始终生效|
|**上下文**|按需加载（渐进式披露）|独立上下文窗口|作为工具返回数据|注入系统提示|
|**支持并行**|❌ 否|✅ **是**（最多10个）|❌ 否|❌ 否|
|**状态记忆**|✅ 有完整过程由**主 Agent 执行**|❌ 无状态主 Agent 并不会获取 subagent 的具体上下文，**只关注最终的执行结果**|部分（特定服务器）|✅ 有|
|**工具权限**|继承主 Agent|可独立配置|作为通道传递|不可配置|
|**适用场景**|重复性任务、标准化流程|复杂任务分解、并行处理|外部数据/工具集成|简单规则、约束|
|**学习曲线**|★★☆☆☆ 中等|★★★★☆ 陡峭|★★★☆☆ 较陡|★☆☆☆☆ 平缓|



|对比维度|**Skills (Claude Skills)**|**Dify**|**n8n**|
|-|-|-|-|
|**核心定位**|AI 能力定义与流程规范|LLM 应用构建平台|工作流自动化平台|
|**核心作用**|教 AI "怎么做"|快速构建 AI 应用|连接各种系统和服务|
|**主要功能**|标准化流程、知识封装、脚本执行|RAG、知识库、Prompt IDE、Agent|系统集成、数据同步、自动化任务|
|**技术架构**|文件夹 + Markdown + 脚本|Python + Rust + React|Node.js + Vue.js|
|**部署方式**|本地文件系统（~/.skills/）|Docker/Kubernetes/SaaS|Docker/本地/SaaS|
|**学习曲线**|★☆☆☆☆ 平缓|★★☆☆☆ 较平缓|★★★☆☆ 中等  |
|**AI 原生能力**|⭐⭐⭐⭐⭐ 完全原生|⭐⭐⭐⭐⭐ 完全原生|⭐⭐⭐☆☆ 增强中（2025年新增）|
|**系统集成**|依赖 MCP/Scripts|有限（通过 API）|⭐⭐⭐⭐⭐ 400+ 集成|
|**知识库管理**|references/ 文件夹|⭐⭐⭐⭐⭐ 内置 RAG 框架|❌ 无内置支持|
|**Prompt 工程**|SKILL.md 中定义|⭐⭐⭐⭐⭐ Prompt IDE|❌ 无专门工具|
|**并行处理**|❌ 否（单实例）|⭐⭐⭐☆☆ 部分（队列式）|✅ 是（DAG 节点）|
|**典型场景**|标准化流程、代码审查、文档规范|智能客服、知识问答、内容生成|跨系统同步、ETL、自动化任务|

## 应用场景
### 具体解决的问题
#### 专业知识鸿沟
❌ 问题：AI 能写代码，但不知道你团队的编码规范、审批流程、内部规则

✅ 解决：把团队的专业知识、经验、规范固化成 Skill，让 AI 掌握

#### 重复劳动的效率问题
❌ 问题：每次都要重新解释"要什么格式"、"怎么做"

✅ 解决：一次配置，永久复用，AI 自动按规范执行

#### 上下文爆炸
❌ 问题：把所有知识塞进上下文，Token 浪费严重

✅ 解决：渐进式披露，按需加载，节省上下文

#### 能力不可复用
❌ 问题：**每个项目、每个团队都在重复打造定制化 Agent**

✅ 解决：Skills 可跨项目、跨团队复用

#### 标准化输出质量
❌ 问题：AI 输出质量不稳定，有时好有时坏

✅ 解决：固定流程和规范，保证输出一致性



### 应用场景
* 当我们搭建一个 agent 的时候，可以直接通过写 skill.md 文件直接实现
* HR支持、IT服务台、数据分析查询、流程自动化，均可以通过 Agent + skill 文件实现



### 缺点
依赖大模型能力，这也带来了一些问题：

* 依赖模型的调用与实现，就有可能造成**识别/输出的不稳定**（相对 n8n 或者 dify 这种）
* 相对 n8n 或者 dify 这种一次搭建，一直使用。**运营成本也更高，因为 token 在燃烧**。





## Skills 此时其实已经突破了 Coding Agent 的边界，变成了一种 Agent 的设计方式。
## 我们不再是专门去写代码、搭建复杂的流程去实现一些固定化的流程，而是通过一份 Skill.md 文件去实现各种功能的 Agent，这才是我认为影响最大的部分。


最后，也需要说明一下，归根结底，Skills 其实还是一种 prompt 工具的变形与边界扩展，它也有它的缺陷与不足，大家也要理智对待，

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
