---
title: "一、背景"
description: "OpenClaw记忆终于可以\"换芯\"了—ContextEngine 实践报告"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\OpenClaw记忆终于可以换芯了—ContextEngine 实践报告.md"
---
OpenClaw记忆终于可以"换芯"了—ContextEngine 实践报告

#### 🧑‍🏫 案例作者：[@程鸣权](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：通用
#### 🔧 使用工具：OpenClaw
#### 📒 案例概要：OpenClaw在v2026.3.7版本引入可插拔上下文管理插件架构ContextEngine，解决无法更改OpenClaw上下文管理引擎的问题。官方推荐的插件lossless-claw基于无损压缩论文，通过分层DAG摘要与不可变存储双态系统，在长上下文基准测试中表现超越竞品，实现记忆持久化且支持按需回溯，标志着OpenClaw向平台化演进。
#### OpenClaw上下文引擎调研结论：（ContextEngine&Lossless-claw）
**1、上下文引擎可插拔：**之前OpenClaw上下文管理逻辑是写死的，例如：对话过长如何压缩历史、如何拼接上下文、如何丢失旧信息，这些都是固定内部实现，插件无法介入。**ContextEngine 可以不改任何底层代码，只通过插拔不同的上下文引擎实现完全不同的上下文策略**。

**2、官方推荐的上下文引擎**[lossless-claw](https://github.com/Martian-Engineering/lossless-claw)：**做到始终保持上下文信息不丢失**

* **具体做法：**建设双态记忆系统，把所有对话原样存进数据库，用分层摘要压缩历史、用检索工具按需恢复细节，让 Agent 在无限长的会话中既装得下上下文、又不丢任何信息；
* **效果：**在OOLONG 基准测试中，超越Claude Code（lossless-claw:74.8 vs Clade Code:70.3）；

# 一、背景
3.9日，OpenClaw 连续发布了 v2026.3.7 和 v2026.3.8 两个大版本，累计89 次代码提交、200+ Bug 修复，还带来了一个全新的插件架构。

其中最核心的亮点是：**上下文管理终于可以"自由插拔"了**。

这个功能叫 **ContextEngine**，是 OpenClaw 近半年来最重要的一次升级。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 二、ContextEngine：半年来OpenClow最重要的一个功能
##### **本文重点聊聊这次更新的”头号明星”——可插拔上下文引擎（ContextEngine）。**
### 2.1 为什么这个功能重要？
所有基于大模型的 Agent 都面临一个核心痛点：**上下文窗口有限**。当对话越来越长，早期的记忆就会被”压缩”或”丢弃”。

OpenClaw 之前的做法是硬编码在核心代码里的压缩逻辑（compaction）——简单粗暴，不可替换。

结果就是：

* 长时间运行的 Agent 会”断片”，忘记之前说过的话；
* Token 消耗居高不下，因为压缩策略不够智能；
* 开发者想用 RAG、知识图谱等替代方案，**改不了**——核心代码锁死了；



社区为此吵了半年。`Issue #22201` 从 2025 年底就开始讨论，终于在 v2026.3.7 正式合并。

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 2.2 **ContextEngine**怎么做到的？
**核心思路：把上下文管理从核心代码中抽离出来，变成一个可插拔的插件接口。**

它暴露了完整的生命周期钩子，这意味着插件可以在`上下文生成`、`压缩`、`拼接`以及`子Agent生命周期管理`的各个阶段介入，从而实现完全不同的上下文策略

|**钩子**|**触发时机**|**用途**|
|-|-|-|
|bootstrap|初始化上下文引擎时|加载配置、建立连接等准备工作|
|ingest|新消息进入到上下文时|自定义如何接收和存储新的上下文内容|
|assemble|组装发送给模型的上下文|决定哪些上下文拼装进模型的 prompt|
|compact|压缩/修剪上下文时|**自定义压缩/修剪策略（核心差异点）**|
|afterTurn|每轮对话结束后|清理、统计、持久化等后处理|
|prepareSubagentSpawn|子 Agent 创建前|决定传递哪些上下文给子 Agent|
|onSubagentEnded|子 Agent 结束后|回收子 Agent 的结果，合并回主上下文|

*Ps：**当不配置任何 ContextEngine 插件时，行为和之前完全一致（*`LegacyContextEngine`* 兜底）。零破坏性变更。*

### 2.3 官方重点推荐的插件 lossless-claw
ContextEngine 上线的同时，社区已经拿出了第一个重量级插件——**lossless-claw**，基于”无损上下文管理”论文实现。

在 **OOLONG 基准测试**中：

|方案|得分|
|-|-|
|lossless-claw（OpenClaw 插件）|74.8|
|Claude Code|70.3|

**在长上下文场景下差距更大。** 这意味着 OpenClaw 的 Agent 在长时间运行后，记忆保持能力已经超越了 Anthropic 的官方产品。

一位核心贡献者在 X 上的评价：”这不只是一个功能更新，这是把 OpenClaw 从一个工具变成一个**平台**的关键转折点。”

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 三、企业实践：如何安装和配置
### **3.1 安装 lossless-claw 插件：**
`openclaw plugins install @martian-engineering/lossless-claw`

### 3.2 openclaw.json配置
```
{
  "plugins": {
    "slots": {
      "contextEngine": "lossless-claw"   // 替换默认上下文引擎
    },
    "entries": {
      "lossless-claw": {
        "enabled": true,
        "config": {
          "freshTailCount": 10,         // 最近 N 条消息始终保持原样，不会被压缩
          "contextThreshold": 0.45,     //当已用上下文占模型窗口的比例超过此值时，进行无损压缩
          "summaryModel": "Claude Sonnet 4.6",    // LCM进行记忆压缩时，选择的模型
          "summaryProvider": "openapi"            // LCM进行记忆压缩时，使用的Provider
        }
      }
    }
  }
}
```
### 3.2 效果验证
1、用户设置了contextThreshold后，当上下文的tokens超过阈值后，会自动进行无损压缩。

|压缩前|压缩后|
|-|-|
|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|

2、压缩的具体信息，会用 "sum_" 为前缀的ID存储。

![](/personal-site-mvp/img/doc-placeholder.svg "")
3、之前信息不会做任何丢失，提问仍然可以回答出来。

***Ps：在20+轮之前的说的记忆，仍然可以回答出来***

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 四、Lossless-Claw的技术原理（进阶）
### 4.1 思路来源
演示Demo：[https://losslesscontext.ai](https://losslesscontext.ai/) 

Lossless-Claw 的思路来自 **Martian Engineering 团队的原创研究**，发表为正式论文：[LCM: Lossless Context Management](https://papers.voltropy.com/LCM)。

核心成员包括 **Josh Lehman **（也是 OpenClaw的维护者）。

Lossless-Claw不是对已有论文的复现，而是团队基于分布式系统经验和认知科学中**情景记忆→语义记忆**的渐进巩固机制提出的原创方案。

---

### 4.2 核心思路：解决什么问题，怎么解决
##### **1、要解决的问题**
即使模型有 1M token 的上下文窗口，多日 Agent 会话中工具调用、文件内容、推理过程的累积也会超限。当前主流方案是**滑动窗口截断**——直接丢弃旧消息，信息**不可逆地丢失**。

##### **2、解决方案：分层 DAG 摘要 + 不可变存储**
LCM 的核心洞察是维护一个**双态记忆系统**：

**1. 不可变存储（Immutable Store）**

* 每条消息、每个工具结果**原样持久化**到 SQLite，永不修改
* 这是唯一的"事实来源"（source of truth）

**2. 活跃上下文（Active Context）**

* 每轮发给模型的实际内容 = 最近的原始消息 + 预计算的摘要节点
* 摘要是"不可变历史的物化视图，是缓存而非事实来源"

##### **3、摘要 DAG 结构**
摘要形成一个**有向无环图（DAG）**，按深度分层：

![](/personal-site-mvp/img/doc-placeholder.svg "")
每一层的压缩策略不同：

|深度|粒度|保留内容|
|-|-|-|
|D0（叶节点）|8+ 条消息，~20K tokens → 800-1200 tokens|文件路径、具体决策、时间戳|
|D1|合并 4+ 个 D0|会话级叙事，小时级时间线|
|D2|合并 4+ 个 D1|跨会话轨迹，天级时间线|
|D3+|合并 4+ 个 D2|持久记忆，仅保留日期范围里程碑|

##### **4、三级容错保证收敛**
|级别|策略|Temperature|
|-|-|-|
|正常|标准提示词|0.2|
|激进|"只保留持久事实"|0.1，压缩比更高|
|兜底|确定性截断至 ~512 tokens|无需 LLM 调用|

即使 LLM 调用失败，系统也**保证压缩一定能完成**。

##### **5、按需回溯工具**
当摘要缺少细节时，Agent 可以用 4 个工具回溯：

|工具|作用|
|-|-|
|`lcm_grep`|正则/全文搜索历史消息和摘要|
|`lcm_describe`|查看某个摘要或文件的完整内容和元数据|
|`lcm_expand_query`|派遣子 Agent 沿 DAG 向下追溯，回答具体问题|
|`lcm_expand`|底层 DAG 遍历（仅子 Agent 可用）|

一些参考材料：

[刚刚，OpenClaw史上最猛更新！AI记忆可自由插拔，开发者等了半年-36氪](https://36kr.com/p/3715160552878469?t=mention&mt=doc&dt=sdk)

[https://zhuanlan.zhihu.com/p/2014651669925884581](https://zhuanlan.zhihu.com/p/2014651669925884581)

[https://github.com/Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw)

[https://github.com/openclaw/openclaw/releases](https://github.com/openclaw/openclaw/releases)

[https://finance.sina.cn/stock/jdts/2026-03-09/detail-inhqkhip3726339.d.html](https://finance.sina.cn/stock/jdts/2026-03-09/detail-inhqkhip3726339.d.html)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
