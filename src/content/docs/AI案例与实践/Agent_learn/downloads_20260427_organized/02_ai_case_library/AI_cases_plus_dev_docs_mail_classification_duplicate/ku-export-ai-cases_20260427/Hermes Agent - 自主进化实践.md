---
title: "引言"
description: "Hermes Agent - 自主进化实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Hermes Agent - 自主进化实践.md"
---
Hermes Agent - 自主进化实践

#### 🧑‍🏫 案例作者：[@程鸣权](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：办公
#### 🔧 使用工具：Hermes
#### 📒 案例概要：Hermes Agent通过自动创建Skills和更新用户画像实现自主进化，有效地补齐OpenClaw的深度学习能力（能够自主进化，越用越好）
# 引言
Hermes Agent的一些火的原因和理论公司内有很多调研文档，例如：[Hermes Agent 技术调研](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/pfs9ugM5RS/t4iLoq50BJ9jcu?t=mention&mt=doc&dt=doc)、[02 | Hermes-Agent 功能与特点分析报告](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/FRuDYMvplN/AKXgiho6ewNV_e?t=mention&mt=doc&dt=doc)

因此，对于理论知识，本文就不再过多赘述，本文重点讲述的是 **Hermes Agent自主进化实践、Hermes如何实现自主进化的，以及对未来的一些思考。**

# Hermes Agent 实践
> **本次实践，采用的模型是MiniMax-M2.7模型，****模型上下文长度配置1M****；**
### 实践一：完成复杂任务后，**自动创建Skills**
### **Hermes Agent--Skills自动创建实践****（Skills更新也类似）**
##### **如何触发自动创建？****---用户需要在同一个主题下，进行多轮交互，让Hermes调用10次以上工具，触发自动创建Skills。**
![执行结果，并自动沉淀成Skills](/personal-site-mvp/img/doc-placeholder.svg "执行结果，并自动沉淀成Skills")
![下次运行，基于刚创建好的Skills，执行效率更高](/personal-site-mvp/img/doc-placeholder.svg "下次运行，基于刚创建好的Skills，执行效率更高")
**Hermes Agent可将复杂任务执行过程，自动沉淀生成Skills；**

**生成的Skills质量是比较高的：**

* 本次实践使用：MiniMax-M2.7模型，模型上下文长度配置1M；
* 创建的Skills如下：

[附件]
![](/personal-site-mvp/img/doc-placeholder.svg "")
**怎么实现的？**

1. **达到触发条件：**当一个轮次里连续执行了 10 次以上工具调用，且期间没有主动用过 `skill_manage`，就会在回复用户之后触发。*（设置在Hermes源码里）*
2. **触发后的执行流程：**

```
后台悄悄 fork(启动) 一个新的 AIAgent（这个AIAgent有独立的review prompt）     
    ↓
把完整对话历史 + review prompt 喂给它      
    ↓
review agent 自己判断：这次对话有没有值得保存为 skill 的内容？      
    ↓
有 → 调用 skill_manage 创建/更新 skill（例如：💾 Skill 'hacker-news-podcast-ruliu' created.）
无 → 输出 "Nothing to save." 然后结束
```
**具体实践Query示例：**去Hacker News抓取排名前10的新闻，挑出前3篇。然后，调用当前模型MiniMax的语音合成接口，给我生成一段播客音频报告。最后把音频和文本总结，发送到我的如流上

**第一次输入Query**

**执行工具未达到10次以上，因此未达到触发条件**

Query：去Hacker News抓取排名前10的新闻，挑出前3篇。然后，调用当前模型MiniMax的语音合成接口，给我生成一段播客音频报告。最后把音频和文本总结，发送到我的如流上

![执行过程，大概8次左右工具调用](/personal-site-mvp/img/doc-placeholder.svg "执行过程，大概8次左右工具调用")
![执行结果](/personal-site-mvp/img/doc-placeholder.svg "执行结果")
**第二次输入Query**

**执行工具达到触发条件，自动创建Skills**

Query：生成的播客文本总结是中文的，所以你生成的音频也应该是中文的，给我生成中文的音频文件。另外，MINIMAX_API_KEY是否可以用oneapi里的api_key呢？oneapi里的api_key是：xxxxx

![执行过程，增加了2次工具调用，因此达到了10次工具调用的触发条件](/personal-site-mvp/img/doc-placeholder.svg "执行过程，增加了2次工具调用，因此达到了10次工具调用的触发条件")
![执行结果，并自动沉淀成Skills](/personal-site-mvp/img/doc-placeholder.svg "执行结果，并自动沉淀成Skills")
**第三次输入Query**

**基于创建好的Skills，执行更高效**

Query:去Hacker News挑出前3篇。然后生成播客给我

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
[附件]
### 实践二：**用户画像（USER.md）自动更新 & 压缩**
### **Hermes Agent--用户画像自动更新 & 压缩实践**
##### **用户画像自动更新**
**怎么实现的？**

* **触发场景1：后台定期审查**，和Skills自动创建的逻辑基本一致；
* **触发场景2：对话实时触发, **模型在正常对话中认为有必要更新画像, 即可随时调用
* **触发场景3：上下文需要压缩时**,** **模型会先看压缩前的上下文是否需要保存到画像

![用户画像自动更新](/personal-site-mvp/img/doc-placeholder.svg "用户画像自动更新")
![更新后的画像](/personal-site-mvp/img/doc-placeholder.svg "更新后的画像")
##### **用户画像自动压缩**
**怎么实现的？**

* User Profile 上限：1,375 chars；
* 如果模型想将新的内容加入User Profile中，会被拒绝；
* 这时模型会自己做取舍，通过replace/remove的方法把一些过时信息给去掉；

![用户画像自动压缩](/personal-site-mvp/img/doc-placeholder.svg "用户画像自动压缩")
**用户画像自动更新，实践Query示例：**

**【对话实时触发，触发自动更新画像】**

Query：你默认以后SANDBOX_USERNAME=chengmingquan

![](/personal-site-mvp/img/doc-placeholder.svg "")
**【后台定期审查，触发自动更新画像】**

Query：调用一次get-ugate-token、enterprise-search

![](/personal-site-mvp/img/doc-placeholder.svg "")
**【用户画像上限后，触发压缩画像】**

画像：USER PROFILE [99% — 1,365/1,375 chars]

![](/personal-site-mvp/img/doc-placeholder.svg "")
**整体更新逻辑示例说明：**

```
graph TD
    A["User Profile 自动更新"] --> T1["场景1: 后台定期审查"]
    A --> T2["场景2: 模型主动保存"]
    A --> T3["场景3: 压缩前刷写"]

    T1 --> T1a["每 10 轮对话触发"]
    T1a --> T1b["fork review agent"]
    T1b --> T1c["审查对话：用户有新的偏好/身份信息？"]
    T1c -->|"有"| WRITE

    T2 --> T2a["用户说了偏好/纠正/个人信息"]
    T2a --> WRITE

    T3 --> T3a["上下文要压缩了"]
    T3a --> T3b["给模型一次机会保存"]
    T3b --> WRITE

    WRITE["memory(target='user')"] --> CHECK{"超 1,375 chars？"}
    CHECK -->|"否"| OK["add 成功"]
    CHECK -->|"是"| REJECT["add 被拒"]
    REJECT --> TRIM["模型自行 replace/remove 旧条目"]
    TRIM --> WRITE

    style CHECK fill:#fff9c4
    style REJECT fill:#fce4ec
    style OK fill:#c8e6c9
```
# 个人的一些思考
### **Hermes背后的一些启示**
### **未来的多智能体生态**
1. **Hermes是对OpenClaw的互补，Hermes重点在于"能学会做更多事"**
    1. OpenClaw走的是连接广度（更多渠道、更多技能、更多控制权）；
    2. Hermes走的是学习深度（闭环进化、记忆分层、自主生成）；

2. **建好让大模型更易于理解的CLI基建仍然非常重要**
    1. Hermes的爆火来自于Skills自主进化，但换个角度想，Skills自主进化解决的是「怎么更聪明地使用一个工具」，但如果「工具本身就很好用」，如何聪明使用就会被弱化。


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
结合Claude Code、OpenClaw、Hermes各自的优势，并引入"容错机制"：

1. Claude Code负责统筹全局，可以安装在个人电脑上；
2. OpenClaw和Hermes作为执行者，在沙箱环境里完成任务；

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 源码分析
### 整体项目架构
```
hermes-agent/
├── agent/              # Agent 核心（提示构建、模型元数据、上下文压缩、显示）
├── tools/              # 40+ 工具（自注册到 registry）
├── hermes_cli/         # CLI 命令行接口
├── gateway/            # 多平台消息网关
│   └── platforms/      # 各平台适配器
├── skills/             # 内置技能库（20+ 类别）
├── optional-skills/    # 可选技能
├── cron/               # 定时任务调度
├── honcho_integration/ # Honcho 用户建模
├── acp_adapter/        # Agent Communication Protocol（编辑器集成）
├── docker/             # Docker 部署
├── environments/       # RL 训练环境
├── run_agent.py        # ★ Agent 运行核心（AIAgent 类、对话循环）
├── model_tools.py      # ★ 工具编排层（发现、注册、调度）
├── toolsets.py          # ★ 工具集定义与组合
├── cli.py              # CLI TUI 主入口
├── mcp_serve.py        # MCP 服务器模式
├── batch_runner.py     # 批量轨迹生成
└── rl_cli.py           # RL 训练 CLI
```
### Hermes框架
![](/personal-site-mvp/img/doc-placeholder.svg "")
Hermes Agent 的心脏是 `run_agent.py` 中的 `AIAgent` 类，核心方法 `run_conversation()` 是一个约 2300 行的巨型方法，实现了工业级的 ReAct（Reasoning + Acting）循环。

##### 循环的骨架
主循环的设计异常清晰——一个 `while` 循环不断与 LLM 对话，直到 LLM 决定不再调用工具、直接回复用户为止：

* 这个 “思考-行动-观察” 的节奏非常明确：LLM 思考后，要么调用工具（行动），等待工具结果（观察），然后回到循环顶部再次思考；要么直接输出最终回复。

```
graph TD
    A["用户输入 message"] --> B["run_conversation()"]
    
    B --> C["准备阶段<br/>构建 prompt / 记忆预取 / 上下文压缩"]
    C --> D["Agent Loop 主循环"]
    
    D --> E["组装请求参数<br/>_build_api_kwargs()"]
    E --> F["调用模型 API<br/>流式 / 非流式"]
    F --> G{"模型返回什么？"}
    
    G -->|"tool_calls 工具调用"| H["执行工具"]
    H --> D
    
    G -->|"文本回复（无工具）"| I["最终响应"]
    
    G -->|"异常 / 截断"| J["重试 / 回退"]
    J --> D
    
    I --> K["后处理<br/>记忆同步 / 会话持久化"]
    K --> L["返回结果给用户"]

    style A fill:#e1f5fe
    style D fill:#fce4ec
    style F fill:#c8e6c9
    style G fill:#fff9c4
    style L fill:#e1f5fe
```
### Hermes核心System Prompt
Hermes核心的system prompt = Agent身份 + 工具指导 + 记忆快照 + 技能列表 + 上下文文件 + 时间模型信息 + 平台提示，共 7 层按 `\n\n` 拼接。

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### Hermes--请求模型的参数：
[附件]
##### Hermes--System Prompt：
[附件]
个人的一些理解：

```
SOUL.md：You are Hermes Agent, an intelligent AI assistant created by Nous Research. You are helpful, knowledgeable, and direct. You assist users with a wide range of tasks including answering questions, writing and editing code, analyzing information, creative work, and executing actions via your tools. You communicate clearly, admit uncertainty when appropriate, and prioritize being genuinely useful over being verbose unless otherwise directed below. Be targeted and efficient in your exploration and investigations.

MEMORY_GUIDANCE（memory工具可用时加载）：You have persistent memory across sessions. Save durable facts using the memory tool: user preferences, environment details, tool quirks, and stable conventions. Memory is injected into every turn, so keep it compact and focused on facts that will still matter later.
Prioritize what reduces future user steering — the most valuable memory is one that prevents the user from having to correct or remind you again. User preferences and recurring corrections matter more than procedural task details.
Do NOT save task progress, session outcomes, completed-work logs, or temporary TODO state to memory; use session_search to recall those from past transcripts. If you've discovered a new way to do something, solved a problem that could be necessary later, save it as a skill with the skill tool.
SESSION_SEARCH_GUIDANCE（session检索工具可用时加载）：When the user references something from a past conversation or you suspect relevant cross-session context exists, use session_search to recall it before asking them to repeat themselves.
SKILLS_GUIDANCE（skill_manage可用时加载）：After completing a complex task (5+ tool calls), fixing a tricky error, or discovering a non-trivial workflow, save the approach as a skill with skill_manage so you can reuse it next time.
When using a skill and finding it outdated, incomplete, or wrong, patch it immediately with skill_manage(action='patch') — don't wait to be asked. Skills that aren't maintained become liabilities.

MEMORY.md（路径：~/.hermes/memories/MEMORY.md）
USER.md（路径：~/.hermes/memories/USER.md）
Ps：这2个目录下，会有文件锁，主要是防止并发写入冲突，进程要想写MEMORY.md/USER.md时，会先对MEMORY.md加文件锁（即：MEMORY.md.lock）

技能列表

上下文信息（用户可以在这里，给 agent 注入项目级的上下文指令（类似 Claude Code 的 CLAUDE.md、Cursor 的 .cursorrules））

时间和模型信息：（里面还可以传Session ID信息，但默认是关闭的。具体是在特定场景上可能会用到：多个并发会话需要让模型知道自己的 session id，方便调试或会话隔离。）

最后平台格式信息：You are a CLI AI Agent. Try not to use markdown but simple text renderable inside a terminal.
（不同平台的Prompt不一样，目前已内置：whatsapp、telegram、discord、slack、signal、email、cron、cli、sms）
```
# 附录：相关学习资料
[https://www.youtube.com/watch?v=TUwxkihxHVE](https://www.youtube.com/watch?v=TUwxkihxHVE)

[https://www.bilibili.com/video/BV1zRdaBcE9x/?spm_id_from=333.337.search-card.all.click&vd_source=8f3ca13066af2af5c91b1307e5d4a1e0](https://www.bilibili.com/video/BV1zRdaBcE9x/?spm_id_from=333.337.search-card.all.click&vd_source=8f3ca13066af2af5c91b1307e5d4a1e0)

[https://zhuanlan.zhihu.com/p/2022015752258027715](https://zhuanlan.zhihu.com/p/2022015752258027715)

[https://www.zhihu.com/question/2026454682885791949/answer/2026781901529072037](https://www.zhihu.com/question/2026454682885791949/answer/2026781901529072037)

[Hermes Agent 技术调研](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/pfs9ugM5RS/t4iLoq50BJ9jcu?t=mention&mt=doc&dt=doc)

[02 | Hermes-Agent 功能与特点分析报告](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/FRuDYMvplN/AKXgiho6ewNV_e?t=mention&mt=doc&dt=doc)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
