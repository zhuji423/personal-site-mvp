---
title: "可选高级字段（Karpathy 原版设计）"
description: "用 Obsidian + Claude Code 管理个人知识库：让 LLM 成为你的知识编译器"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\用 Obsidian + Claude Code 管理个人知识库：让 LLM 成为你的知识编译器.md"
---
用 Obsidian + Claude Code 管理个人知识库：让 LLM 成为你的知识编译器

#### 🧑‍🏫 案例作者：[@柴延晨](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：知识加工、工作流自动化
#### 🔧 使用工具：Claude、Comate
#### 📒 案例概要：用Obsidian和Claude Code构建知识管理系统：LLM作为编译器自动整理笔记，实现知识可持续积累。
> 这篇文章来自我在 Obsidian + Claude Code 上实践了一个月后的系统性总结。
> 核心思路来自 Andrej Karpathy 的 llm-wiki 思路，我结合 Obsidian 做了具体落地。
---

## 一、从一个熟悉的痛点说起
你大概经历过这样的场景：

* 读完一篇好文章，在 Notion 里记了笔记。两个月后完全不记得它在哪
* 在你的笔记APP中积累了几百个碎片笔记，但每次想用某个知识点时还是得重新搜索，甚至重新读原文
* 用了 AI 助手，每次都要重新解释背景，它对你积累的知识一无所知

**根本问题不是工具不够好，是知识在收集之后没有被"编译"。**

你的笔记是源码，但你从来没有 build 过。

---

## 二、为什么选择 Obsidian + Claude Code
先说工具选择，再讲系统设计。

**Obsidian** 是本地 Markdown 笔记工具，三个核心优势：

* 本地存储，数据完全掌控
* 双链（`[[ ]]`）天然构建知识网络
* 插件生态丰富，可定制性强

**Claude Code** 是 Anthropic 官方的 CLI 助手，两个关键能力：

* 能直接读写本地文件，理解目录结构
* 可以通过 Schema 文件长期"记住"你的规范

两者的结合点很简单：**Obsidian 负责存储与展示，Claude Code 负责编译与维护。**

你的笔记就是源码，Claude Code 就是编译器，Obsidian 就是 IDE。

---

## 三、软件工程类比：为什么这个类比有效
作为开发者，我们有几十年积累的工程直觉：

![](/personal-site-mvp/img/doc-placeholder.svg "")
这些直觉可以**直接平移**到个人知识管理，不需要重新发明轮子。

靠人工定期整理笔记 = 靠人工做回归测试：理论上可以，实际上不可持续。

---

## 四、与传统 RAG 的本质区别
在讲具体设计之前，先说清楚这套方案和"给 AI 喂文档、然后检索"的传统 RAG 有什么不同：

![](/personal-site-mvp/img/doc-placeholder.svg "")
**核心洞察（来自 Karpathy）**：

> 知识应该"编译一次、持续维护"，而非每次查询时重新推导。
---

## 五、快速上手：从最小系统开始
不需要一开始就建立完整的目录结构。最小可用系统只需要三样东西：

1. **一个 Inbox 目录** — 扔进去就行，不用考虑分类
2. **一个 Knowledge 目录** — LLM 编译产物落这里
3. **一个 wiki-compiler Prompt** — 告诉 LLM 怎么从 Inbox 编译到 Knowledge

其他的（健康检查、输出归档、搜索工具）都是后续按需添加的。

---

## 六、三层架构设计
整个系统分为三层，职责严格分离：



![](/personal-site-mvp/img/doc-placeholder.svg "")
**关键边界**：Wiki 层不是人机协作写作区，是 LLM 的专属维护区。
人只负责两件事：**往 raw 里喂素材、从 wiki 里读内容**。



**_Pending 层的定位**：不是数据流的终点，而是人机协作的交接节点。LLM 发现问题写入这里，人看完裁决，LLM 再执行修改。健康报告处理完后可以归档或清理，不需要长期保留。

---

## 七、知识流转全貌
下面是从"发现一篇好文章"到"知识可被 LLM 直接使用"的完整流程：

![](/personal-site-mvp/img/doc-placeholder.svg "")
---

## 八、知识条目的数据结构设计
每个 Wiki 页面的 frontmatter 是知识库的"认识论状态"，不只是元数据：

```

---
tags: [知识域标签]
source:
  - https://原始来源URL
  - 或本地文件名
created: 2026-04-05
updated: 2026-04-05
related: [[相关概念1]], [[相关概念2]]

# 可选高级字段（Karpathy 原版设计）
confidence: high | medium | speculative
status: active | superseded | archived
open-questions:
  - 这个概念有什么地方还没想清楚？
contradictions:
  - Source A 说 X，Source B 说 Y，待确认

---
```
`contradictions` 字段值得特别说明：**知识库不应该粉饰矛盾**。
当两个来源对同一问题的描述不一致时，LLM 在编译时显式标注出来，等待人工最终裁决——这比静默地选择其中一个要诚实得多。

---

## 九、目录结构设计
我的 Vault 按功能编号分区，知识流转经过以下节点：

```
Vault/
│
├── 01_Inbox/               ← [收集层] Web Clipper 剪藏直接落这里
│   ├── assets/             ← 文章图片本地化存储（防 URL 失效）
│   └── README.md           ← 收集箱使用规范
│
├── 04_Knowledge/           ← [Wiki 层] LLM 完整所有权
│   ├── AI/
│   │   ├── _Maps/          ← AI 领域知识地图（MOC）
│   │   └── {概念名}.md     ← 各个知识条目
│   ├── 知识管理/
│   │   ├── _Maps/
│   │   └── {概念名}.md
│   └── {其他领域}/
│
├── 05_Toolkit/
│   └── Prompts/
│       └── wiki-compiler.md  ← [Schema 层] 编译器行为规范 Prompt
│
├── 07_Pending/             ← [待处理区] LLM 写入，人审阅裁决后处理
│   ├── qa/
│   └── health/
│
└── 06_Daily/               ← 兼任操作日志（log.md 的替代）
    └── YYYY.MM.DD.md
```
`_Maps/`** 的设计**：每个知识域有一个置顶的 Map 文件，作为该领域的导航入口。下划线前缀确保文件列表中排列最前。这是 Obsidian 社区的 MOC（Map of Content）实践。

---

## 十、Schema：让 LLM 成为规范编辑者的关键
架构中最容易被忽视的是 Schema 层。

三层目录只是容器，是 `wiki-compiler.md` 这个 Prompt 文件决定了 LLM 如何工作：

```
CLAUDE.md / wiki-compiler.md 的核心作用：
┌──────────────────────────────────────────────────────┐
│  定义知识库的目录结构（LLM 写哪里）                     │
│  定义各知识域的范围（哪些内容归入哪个目录）               │
│  定义处理步骤（分类 → 摘要 → 提取 → 写入 → 双链 → Map） │
│  定义输出格式（frontmatter 字段、文件名规则）            │
│  定义更新策略（已有条目如何追加，不重复已有内容）         │
└──────────────────────────────────────────────────────┘
```
**没有 Schema，LLM 是一个能力强大但行为随机的助手。**
**有了 Schema，它变成一个遵守规范的知识编辑者。**

Schema 和知识库一起演进：当你发现 LLM 的某个处理方式不符合你的需求时，修改 Schema，下次编译自动生效。

---

## 十一、健康检查：知识库的 CI/Lint
随着知识条目增多，会出现三类问题：

```
问题类型          示例                        处理方式
─────────────────────────────────────────────────────────
1. 一致性冲突    "RAG"在两个文件里定义矛盾    合并，保留最新版本
2. 完整性缺失    某条目没有 source 字段       LLM 补充或标注待填
3. 孤岛笔记      某文件入链+出链都少于 2 个   找到应连接的概念，补双链
```
**执行方式（Claude Code 指令）**：

```
读取 04_Knowledge/ 下所有文件，
检查以下三点：
1. 概念定义冲突：同名概念在不同文件中是否描述矛盾
2. 完整性缺失：哪些条目缺少定义、来源或 related 字段
3. 孤岛笔记：入链+出链少于2的文件

输出健康报告到对话，等我确认后再修改文件。
```
建议每周一次，或每次大批量编译后执行。

---

## 十二、我的使用模式
典型一天的工作流很简单：浏览器看到好文章，用 Obsidian 的 Web Clipper 一键剪藏到 Inbox；晚上打开 Claude Code，让 LLM 把 Inbox 的新资料编译进 Knowledge；之后任何时候问它问题，它都能从已编译的知识库中直接回答。

每周执行一次健康检查，看看有没有需要人工裁决的矛盾或孤岛笔记。

---

## 十三、实践建议
### 图片资产本地化
Web Clipper 剪藏的文章通常包含外链图片，时间久了 URL 失效，LLM 也无法访问外链。

**推荐做法（Obsidian 设置）**：

* Settings → Files and links → Attachment folder path 设为 `01_Inbox/assets/`
* Settings → Hotkeys → 绑定 "Download attachments for current file"（建议 `Ctrl+Shift+D`）
* 每次 Clip 完文章后，按快捷键将图片下载到本地

### 不要对 Wiki 层直接写作
Wiki 层是 LLM 的专属维护区，人只读不写。

如果你的想法与某个知识点相关，写进 Inbox，让 LLM 编译进 Wiki。

但**不是所有内容都要经过 Inbox**：

* Inbox 是外部内容进入知识库的入口（文章、论文、播客稿等）
* 日记、工作文档、系统文件等操作性文档，有自己的目录，直接写进去就好
* 这些文档本身也是知识库的一部分，但不需要被"编译"

区分清楚"待编译的原始资料"和"直接使用的操作性文档"，系统边界就清晰了。

### Schema 是核心资产
你和 LLM 共同演进的 CLAUDE.md / wiki-compiler Prompt，是整个系统中最有价值的部分。
比任何单个知识条目都重要——它决定了所有未来条目的质量。

---

## 十四、这套系统适合谁
**适合**：

* 长期在某个领域持续积累知识（AI、产品、投资、某技术栈）
* 习惯用 Markdown 笔记工具
* 有使用 Claude Code / Cursor / 类似 AI 编程助手的习惯
* 知识库规模达到"靠记忆找不到东西"的阶段

**不适合**：

* 只是偶尔记录几篇笔记，不需要复杂系统
* 对 Markdown 不熟悉，笔记以语音/手写为主
* 没有持续输入习惯（Inbox 长期为空，系统没有意义）

---

## 结语
这套系统最大的价值不是让你"搜索更快"——而是**让知识积累变得可持续**。

传统笔记系统的问题是：积累越多，维护越难，最终要么废弃，要么变成没人敢动的存档。

把 LLM 作为编译器引入之后，每一篇新资料进来，知识库都被主动更新一次。矛盾被标注出来，缺失被填补，双链被维护。你不需要每隔一段时间做一次"大扫除"，系统自己保持在一个可用状态。

这才是 "knowledge base" 的字面含义：一个**碱基**，而不是一个档案柜。

---

*参考资料：*[Andrej Karpathy - llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
