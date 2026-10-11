---
title: "**一、Ducc缺少记忆能力**"
description: "Claude-Mem 实践案例：让 Ducc 拥有完整的历史记录"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Claude-Mem 实践案例：让 Ducc 拥有完整的历史记录.md"
---
Claude-Mem 实践案例：让 Ducc 拥有完整的历史记录

#### 🧑‍🏫 案例作者：[@骆金昌](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：通用
#### 🔧 使用工具：Claude
#### 📒 案例概要：通过安装开源插件 Claude-Mem，为 Ducc补上缺失的历史记录能力——自动记录每次会话的操作、决策和发现，下次对话时按需召回，让 Coding Agent从「每天归零」变成「越用越懂你的项目」。
## 结论
* Ducc 缺少历史记录能力，内置的 Auto Memory 只是个 200 行的便利贴——不自动记、不能搜、装不下
    * Claude-Mem 补上了这块短板：全程自动记录、AI 提炼结构化笔记、三层漏斗按需搜索、语义检索，Token 节省 70%
    * 两者搭配效果最好：Auto Memory 放不变的共识（规范、偏好），Claude-Mem 记变化的经验（操作历史、决策过程）
    * 核心观点：Agent 的壁垒不是模型能力，是经验积累。 模型是智商，记忆是经验——有历史记录的

* Ducc，才能从「每天归零的实习生」变成「越用越强的老员工」
* **缺点：会导致使用的tokens增加，因为会自动调用ducc对历史会话压缩。**

**安装上后，还是非常好用的。不需要把之前的工作重新说一次了！！**

![](/personal-site-mvp/img/doc-placeholder.svg "")
# **一、Ducc缺少记忆能力**
### **Ducc缺少历史记录**
Ducc（Claude Code）是没有历史记录功能；但是内置有长期记忆（Auto Memory）。

![](/personal-site-mvp/img/doc-placeholder.svg "")
长期记忆一般是不开启的，开启方法如下，然后重启下生效

![](/personal-site-mvp/img/doc-placeholder.svg "")
### Auto Memory 的三个硬伤
#### 硬伤 1：不自动记录会话历史
Auto Memory **不会记录你做了什么**。它不知道你昨天修了哪个 bug、上周做了什么决策、三天前发现了什么坑。

#### 硬伤 2：全量加载，不能搜索
每次开会话，Auto Memory 把整个 MEMORY.md **一股脑全塞进系统提示**——**没有搜索能力，只有全量加载。**

#### 硬伤 3：200 行上限，装不下真正的经验
一个中等规模的项目，持续使用几周后，真正有价值的经验远不止 200 行。你要么忍痛删旧的，要么眼睁睁看着有用的信息被截断。

# 二、安装Claude-Mem
**Claude-Mem** 是一个开源的 Claude Code 记忆插件（github.com/thedotmack/claude-mem），能让 Coding Agent 自动记录每次会话的操作历史，并在下次会话时智能召回。

### **安装**
`ducc plugin marketplace add thedotmack/claude-mem`

`ducc plugin install claude-mem`

然后启动ducc，输入以下Query安装环境和测试，一路Enter，估计就能成功了！

```
完整测试claude-mem Skill的功能（特别观察Prompt、Observation、Session数量是否一致）；如果遇到问题，参考 https://docs.claude-mem.ai/troubleshooting 解决。必须全部测试都通过了，才向我交付；

注意：我用的是ducc，CLAUDE_CODE_PATH大概率如下：
"CLAUDE_CODE_PATH": "/Users/luojinchang/.comate/baidu-cc/bin/ducc"
```
### 直接使用
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


## 三、Claude-Mem 补上了什么？
||Auto Memory（内置）|Claude-Mem（插件）|
|-|-|-|
|**记录方式**|AI 主动判断才写入|自动记录每次操作|
|**记录内容**|关键经验和偏好|完整会话历史、观察、决策、发现|
|**存储**|一个 MEMORY.md 文件|SQLite 数据库 + 向量搜索引擎|
|**容量**|200 行上限|无上限|
|**检索**|每次全量加载|按需语义搜索|
|**跨会话**|只保留最新状态|完整历史时间线|

一句话总结：**Auto Memory 是便利贴，Claude-Mem 是工作笔记本 + 搜索引擎。**

---

## 四、Claude-Mem 的四个关键设计
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 设计 1：全程自动记录，零打扰
系统在 5 个关键节点自动拦截：

|你在做什么|系统在做什么|
|-|-|
|打开 Ducc|翻开历史笔记，注入相关上下文|
|每次说话|记下你的原话|
|AI 每执行一个操作|记下做了什么、结果是什么|
|关闭 Ducc|写当日工作总结|

一次会话中，AI 的操作可能 **100+ 次**，每次都被捕获。但不是什么都记——例行操作自动跳过，**只保留有价值的信息**。

对比 Auto Memory：你不需要等 AI「主动判断」，也不需要手动提醒它「记住这个」。

### 设计 2：用 AI 观察 AI，自动写「工作周报」
**后台有另一个 AI 在「观察」正在工作的 AI，自动提炼结构化记忆。**

为什么不直接存聊天记录？因为修一个 bug 可能涉及 20 次操作，但需要记住的就一句话。观察者 AI 把 **20 次操作浓缩成一条高质量笔记**。

每条笔记有：类型（修 bug / 新功能 / 发现 / 决策）、一句话标题、关键事实、概念标签。

对比 Auto Memory：**Auto Memory 存的是「结论」，Claude-Mem 存的是「过程 + 结论」。** 当你需要追溯「为什么当时这么做」时，只有 Claude-Mem 能回答。

### 设计 3：三层漏斗搜索，按需加载
这是和 Auto Memory 最大的区别——**不是全量加载，而是按需搜索**。

|层级|做什么|类比|
|-|-|-|
|第 1 层|只看标题|翻书的目录|
|第 2 层|看感兴趣的几条前后文|翻到那一页速览|
|第 3 层|只展开真正需要的 2-3 条|逐字精读|

Auto Memory 每次开会话加载全部 200 行 = 浪费 Token + 注意力分散。

Claude-Mem 只加载真正相关的几条 = **省 70% Token，AI 输出质量更高。**

### 设计 4：语义搜索，不只是关键词匹配
Auto Memory 没有搜索能力。Claude-Mem 有两个搜索引擎：

* **全文搜索**——你搜「登录失败」，找到所有包含这四个字的记录
* **语义搜索**——还能找到写着「用户认证异常」「Token 过期」的记录——意思相近，但用词不同

对比 Auto Memory：**便利贴只能用眼睛扫，笔记本可以用搜索引擎查。**

---

## 五、最佳实践：两者搭配使用
**不是二选一，而是互补。**

|适合放 Auto Memory 的|适合交给 Claude-Mem 的|
|-|-|
|项目基本信息（技术栈、目录结构）|每次会话的操作记录|
|团队编码规范|bug 修复过程和根因|
|你的个人偏好|技术决策的前因后果|
|反复出现的解决方案|「三天前那个问题怎么解决的？」|

**Auto Memory 是底座，放不变的共识。Claude-Mem 是日志，记变化的经验。**

底座保证每次会话有基本认知，日志保证需要时能查到任何历史。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
