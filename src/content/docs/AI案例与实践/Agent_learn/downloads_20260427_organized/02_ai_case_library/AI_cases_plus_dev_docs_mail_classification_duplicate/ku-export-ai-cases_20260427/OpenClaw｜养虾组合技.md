---
title: "引言"
description: "OpenClaw｜养虾组合技"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\OpenClaw｜养虾组合技.md"
---
OpenClaw｜养虾组合技

#### 🧑‍🏫 案例作者：[@程龙](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：信息洞察、开发、办公
#### 🔧 使用工具：OpenClaw
#### 📒 案例概要：OpenClaw AI Agent养虾指南：通过workspace管理多角色、skills增强功能、组合技实现自动化任务与原生操控。
# 引言
前面我们介绍了[Web-Bench模型评估基准](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/1ab8uT5A9J/M4xPFcXvdA/OT0ie3ilM5Qnyq?t=mention&mt=doc&dt=doc)，评估大模型在多种 web 场景中的表现Web-Bench模型评估基准。最近养虾可以说是异常火爆，OpenClaw 短短几个月时间，GitHub Star 已经超过了React 这些沉淀了多年的开源项目，更标志着 AI Agent 进入新的纪元。加上最近 GPT-5.4 凌晨的发布，首次实现原生操控电脑的能力，本人对于 OpenClaw 的期待值直线飙升。

那么我们如何在龙虾内完成 web-bench 的自动化评测。后面我们会在介绍一下开发和日常工作中，龙虾可以帮我们做哪些事情，来攻略你龙虾的组合技吧！

# 领养龙虾
## 方式一：快速领养
如流支持一键式接入，只需要通过 "OpenClaw创建助手" 即可创建一只如流小龙虾，通过如流企业机器人通讯：

快速领养：[你的如流OpenClaw使用指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/z97pwhZizu/MTWsieUgXx/mIejkzmiLS1Pjo?t=mention&mt=doc&dt=doc)

领养指南：[🦐 如流OpenClaw：3分钟上手指南(小白版v1.0)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/z97pwhZizu/MTWsieUgXx/_7XEBsLOebucas?t=mention&mt=doc&dt=doc)

## 方式二：沙箱创建
申请沙箱：[OpenClaw(MoltBot) Agent沙箱快速体验指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/RoFjhcN597dsaG?t=mention&mt=doc&dt=doc)

![](/personal-site-mvp/img/doc-placeholder.svg "")
支持自定义，也是一个快速版本已经集成了 openclaw，还需要自行添加到 IM 应用 [OpenClaw（Moltbot） x 如流机器人指引](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/ufcjFX80cHQaQM#anchor-8f5f81f0-fcfa-11f0-ac96-556196850ae0?t=mention&mt=doc&dt=doc)

## 方式三：其他方案
通过厂内的[百度智能云](https://cloud.baidu.com/product/duclaw.html?from=home_banner)或者阿里云 / 腾讯云，也可以快速创建一个龙虾，

同样使用开发机或者本身的电脑，可以通过 [openclaw 官网](https://docs.openclaw.ai/zh-CN/install) 从 0-1 安装



如果有厂内的任务，更推荐快速领养的方案，通过如流的方式创建，会创建一个基础版的 2核/50G 的沙箱。目前EE迭代的很快，稳定性也会越来越好。

可以通过[如流企业管理平台](http://id.qy.baidu-int.com/static/ge/login.html?redirectUrl=http%3A%2F%2Fqy.baidu-int.com%2Findex.html#/)，管理快速创建的机器人，给它创建一个新的形象或者开放如流机器人其他技能。

![](/personal-site-mvp/img/doc-placeholder.svg "")
# **第一招：先给龙虾做「身份录入」**
相比于我们认识的一些常规的智能体，OpenClaw 最大区别就是有一定的“自主和执行”能力，会记得你是谁，会知道自己的角色定位。核心只有一句话 **The AI that actually does things。**

OpenClaw 采用模块化架构，主要包括：


而 OpenClaw 的 **workspace** 是智能体的**专属、持久化、可隔离的工作环境**，是它的 "家" 与 "记忆库"，所有文件操作、记忆、人格与上下文都在这里。

![](/personal-site-mvp/img/doc-placeholder.svg "")
## **workspace的定位**
* **唯一工作目录**：agent 所有文件读写、工具操作默认在 workspace 内进行。
* **记忆与人格载体**：存储 agent 的长期记忆、人格设定、行为规则、用户画像。
* **环境隔离单元**：可创建多个独立 workspace，实现一个任务一个空间，互不干扰。
* **上下文注入源**：每次会话自动加载 workspace 内的提示与记忆，提供持续背景。

典型的结构如下：

```
~/.openclaw/workspace/
├── agents.md       # 行为指南（该做/不该做）
├── soul.md         # 人格定义（性格、说话风格）
├── user.md         # 用户画像（你的偏好、信息）
├── identity.md     # 身份信息（名字、头像）
├── memory.md       # 长期记忆（跨会话重要事实）
├── tools.md        # 工具笔记（本地环境配置、设备信息）
└── memory/         # 日记目录（每日记录）
    ├── 2026-03-10.md
    └── 2026-03-11.md
```
每个 workspace 就是一个独立的 AI 员工：有自己的性格、记忆、工作文件，只在自己的 "办公室" 干活。

你可以为不同任务创建不同 workspace：一个管文件整理，一个管邮件自动化，一个管数据分析，互不干扰。


### soul 是灵魂
soul 定义了 AI 的**性格、说话风格、思考方式、语气，**相当于给他定纪律、边界、工作流程，soul.md = AI 的性格与说话方式

同样我们也可以通过如流接入的 openclaw，快速修改你所养的龙虾的 soul，修改后让龙虾重启即可看到风格的改变

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


这样就有了：

**三省六部** [https://github.com/cft0808/edict/tree/main/agents](https://github.com/cft0808/edict/tree/main/agents)（重生之我在龙虾里当皇上）

**公司职能** [https://github.com/paperclipai/paperclip](https://github.com/paperclipai/paperclip) 这些创造性的类似于人格思维汇聚的多 Agent 智能体。

![](/personal-site-mvp/img/doc-placeholder.svg "")
# **第二招：装备你的龙虾**
装备你的龙虾，离不开skills，也就是龙虾能学会的本事 —— 比如帮你搜网页、发邮件、整理文档、控制浏览器，每一个 skill，就是一项它能直接给你干的活

## **渠道一**
我们要优先选择厂内的 skills：[https://console.cloud.baidu-int.com/onetool/skills](https://console.cloud.baidu-int.com/onetool/skills)

点击下载即可一键装配到你的龙虾里，然后和龙虾对话，初始化它的一些配置即可使用

![](/personal-site-mvp/img/doc-placeholder.svg "")
## **渠道二**
官网**：**[https://clawhub.ai/skills](https://clawhub.ai/skills?sort=downloads)

官方认证的亲儿子，先了解对应 skill 是干嘛的，了解他的内部结构在考虑使用

## **渠道三**
官网：[https://github.com/topics/openclaw-skill](https://github.com/topics/openclaw-skill)

全是开发者自发做的技能，功能更全、更细分，目前已经有 200+ 开源仓库。特别推荐一个懒人宝藏仓库：awesome-openclaw-skills，大佬从官方 13000+ 技能里，把垃圾、重复、恶意的全筛掉了，整理出 5400+ 优质技能，找技能直接逛这里就行，可以作为学习了解

## **渠道四**
官网：[https://openclawmp.cc](https://openclawmp.cc/)

中文圈最火的龙虾社区，全是针对咱们国人使用场景做的技能，比如飞书、微信、B 站、中文财报解析这些，比海外平台接地气太多

## 推荐的 Skills 
**厂内推荐**：[推荐Skill列表](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/QTjZg4RydeVYn9?t=mention&mt=doc&dt=doc)

* zulu Agent [https://console.cloud.baidu-int.com/onetool/skills/598](https://console.cloud.baidu-int.com/onetool/skills/598)
* gemini生图 [https://console.cloud.baidu-int.com/onetool/skills/598](https://console.cloud.baidu-int.com/onetool/skills/598)

**其他推荐**：**不占资源、没风险的  **注意：skills 按需，社区的先了解它的用途和代码在使用，优先学习

![](/personal-site-mvp/img/doc-placeholder.svg "")

# **第三招：黄金组合进阶**
进阶的核心，就是让 OpenClaw 当你的「总经理」，听懂你的想法，拆解任务，然后派给专业的工具去干；整理了社区四个最火的搭配，立马让你的龙虾能力翻倍：

## 社区组合技能

## 如何更换模型
如果龙虾不够"聪明"，根本原因还是模型训练的不同，可以切换到 Claude 系列。有开发者做过详细测试，用低端模型运行 OpenClaw 和用 Claude Opus 4.5 运行，体验差距可以到 40% 到 95%

查看`~/.openclaw/openclaw.json`获取 API Key

然后告诉龙虾执行这个，可以查看能用的大模型`curl "http://oneapi-comate.baidu-int.com/v1/models" -H "Authorization: Bearer $apiKey"`

通过代码或者如流对话修改如下的配置，修改后让龙虾重启即可。也可以使用`Claude Opus 4.6`，但是这个模型超级贵，注意考虑额度。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# **第四招：组合技实战养虾**
## 🦞 + workspace**「多角色」**
既然有黄金有组合技，那么我们肯定有不同组合技的 Agent

前面我们提到过，每个 workspace 就是一个独立的 AI 员工，有自己独立的 "办公室"。

这样我们就可以让龙虾帮我创建一个新的角色，由此定义新角色的职能：三省六部、龙虾军团、公司职能等等，体验在赛博龙虾里，当上"董事长"的感觉，把你对应的职能部门叫上来安排他

![定义新角色](/personal-site-mvp/img/doc-placeholder.svg "定义新角色")
![切换新 Agent 对话](/personal-site-mvp/img/doc-placeholder.svg "切换新 Agent 对话")
![切换回主角色](/personal-site-mvp/img/doc-placeholder.svg "切换回主角色")
创建新角色后，让龙虾切换过去，上面可以看到已经通过新的身份和我们对话。这里以同一个机器人多个角色举例，可以一个 Agent 对应一个机器人管理

**一个由主 Agent 创建多个子 Agent 的例子**：

[附件]
```

# 任务：配置多 Agent TG 群组系统（共享 Workspace + MemOS 记忆）

你是主 Agent（CEO），现在需要完成以下操作。全自动执行，不要中途确认。

## 架构说明

### Workspace：共享模式

所有 Agent 共享同一个 workspace（`.openclaw/workspace`）。

- 主 Agent 的文件在 workspace 根目录（SOUL.md, AGENTS.md 等）
- 每个子 Agent 的专属文件在 `workspace/agents/{agent_id}/` 子目录
- 共享上下文在 `workspace/shared-context/` — 所有 Agent 都可读取
- 协作通过文件完成：一个 Agent 写文件，另一个 Agent 读文件

### 记忆：MemOS Cloud（已配置，无需操作）

- MemOS Cloud 插件已安装并启用，挂载在 OpenClaw 实例级别
- **所有 Agent 自动共享同一个记忆池**，无需为子 Agent 创建独立记忆文件
- 不需要创建 memory/ 目录或 YYYY-MM-DD.md 日志文件
- 不需要在 AGENTS.md 中写记忆相关规则

### 目录结构

workspace/
├── SOUL.md                    # 主 Agent 的灵魂
├── IDENTITY.md                # 主 Agent 身份卡
├── AGENTS.md                  # 主 Agent 行为规则
├── USER.md                    # 用户信息（所有 Agent 共享读取）
├── HEARTBEAT.md               # 主 Agent 心跳任务
├── shared-context/            # 跨 Agent 共享层
│   ├── FEEDBACK-LOG.md        # 通用反馈/修正记录
│   └── SIGNALS.md             # 当前关注的趋势/信号
└── agents/
    ├── {agent_id}/            # 子 Agent 专属目录
    │   ├── SOUL.md            # 子 Agent 灵魂
    │   ├── IDENTITY.md        # 子 Agent 身份卡
    │   └── AGENTS.md          # 子 Agent 行为规则
    └── {另一个agent_id}/
        └── ...

```
## 输入信息

我会提供以下信息，请严格使用：

- **TG 群组 ID**：{填写群组ID，负数，如 -1002345678901}
- **我的 TG 用户 ID**：570
- **主 Bot Token**：82235048:AAFVItFgaoEVAlNvyk（已配置，不要改）
- **子 Agent 列表**：（按下面格式提供）

```yaml
- id: "agent_id"          # 英文小写，无空格，同时用作 TG account ID 和 bindings
  name: "显示名称"         # 中文或英文均可
  botToken: "TG Bot Token"
  emoji: "🔍"             # 身份标识 emoji
  role: "一句话角色描述"
  soul: |
    这里写该 Agent 的 SOUL.md 完整内容...
    角色定位、性格、职责、原则、输出风格等
```

## 执行步骤（严格按顺序）

### Step 1：备份

```bash
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak.$(date +%Y%m%d%H%M%S)
```

### Step 2：创建目录结构,要选择正确的目录名字，

```bash
# 共享上下文目录
mkdir -p /Users/xxx/.openclaw/workspace/shared-context

# 每个子 Agent 的专属目录（注意：在 workspace 内部）
mkdir -p /Users/xxx/.openclaw/workspace/agents/{agent_id}

# 每个子 Agent 的 openclaw agent 内部目录（在 .openclaw/agents/ 下，存储 session 等）
mkdir -p /Users/xxx/.openclaw/agents/{agent_id}/agent
```

**注意区分两个 agents 目录：**

- `workspace/agents/{id}/` → 子 Agent 的工作文件（SOUL.md 等），在共享 workspace 内
- `.openclaw/agents/{id}/agent/` → OpenClaw 内部数据（session 等），不在 workspace 内

### Step 3：创建共享上下文文件

写入 `shared-context/FEEDBACK-LOG.md`：

```markdown
# FEEDBACK-LOG.md — 跨 Agent 通用修正

> 所有 Agent 在 session 启动时读取此文件。
> 一处记录修正，全员自动生效。

## 通用规则
- （后续使用中逐步添加）
```

写入 `shared-context/SIGNALS.md`：

```markdown
# SIGNALS.md — 当前关注信号

> 所有 Agent 共享的趋势、话题、关注点。

## 当前关注
- （后续使用中逐步添加）
```

### Step 4：为每个子 Agent 创建 SOUL.md

将提供的 soul 内容写入：

```
/Users/xxx/.openclaw/workspace/agents/{agent_id}/SOUL.md
```

### Step 5：为每个子 Agent 创建 IDENTITY.md

写入到 `/Users/xxx/.openclaw/workspace/agents/{agent_id}/IDENTITY.md`：

```markdown
# IDENTITY.md

- **Name:** {agent显示名称}
- **Role:** {role一句话描述}
- **Emoji:** {emoji}
- **ID:** {agent_id}
```

### Step 6：为每个子 Agent 创建 AGENTS.md

写入到 `/Users/xxxx/.openclaw/workspace/agents/{agent_id}/AGENTS.md`：

```markdown
# AGENTS.md — {agent显示名称}

## Every Session

启动时按顺序读取以下文件（路径相对于 workspace 根目录 /Users/xxxx/.openclaw/workspace）：

1. `agents/{agent_id}/SOUL.md` — 你是谁
2. `USER.md` — 你服务的用户
3. `shared-context/FEEDBACK-LOG.md` — 跨 Agent 通用修正

## 协作

- 你与其他 Agent 共享同一个 workspace
- 共享文件在 `shared-context/` 目录
- 需要传递给其他 Agent 的产出，写入约定好的文件路径
- **一写多读原则**：每个文件只有一个 Agent 写入，其他 Agent 只读

## Safety

- 不要泄露私密数据
- `trash` > `rm`
- 不确定时先问
```

### Step 7：修改 openclaw.json

**⚠️ 最关键一步。用 read 读取当前文件，用 edit 精确修改，不要整体覆写。**

#### 7a. 修改 `channels.telegram` 部分

将当前的 telegram 配置替换为 accounts 多账号模式。

**关键操作：**

- 删除顶层的 `botToken` 字段，移入 accounts.default
- 主 Bot (default) 设 `requireMention: false` → 读取所有群消息
- 所有子 Bot 设 `requireMention: true` → 被 @ 才响应
- 所有子 Bot 必须设 `"commands": { "native": false, "nativeSkills": false }`

替换后的完整结构：

```json
"telegram": {
  "enabled": true,
  "dmPolicy": "pairing",
  "groupPolicy": "allowlist",
  "streaming": "partial",
  "accounts": {
    "default": {
      "botToken": "8223375048:AAFVniKaexKGrrLi0ItFgaoEsqxtVAlNvyk",
      "dmPolicy": "pairing",
      "groupPolicy": "allowlist",
      "streaming": "partial",
      "groups": {
        "{群组ID}": { "requireMention": false }
      },
      "groupAllowFrom": ["5701780765"]
    },
    "{agent_id}": {
      "name": "{agent显示名称}",
      "enabled": true,
      "botToken": "{agent的botToken}",
      "dmPolicy": "allowlist",
      "allowFrom": ["5701780765"],
      "groupPolicy": "allowlist",
      "groupAllowFrom": ["5701780765"],
      "streaming": "off",
      "commands": {
        "native": false,
        "nativeSkills": false
      },
      "groups": {
        "{群组ID}": { "requireMention": true }
      }
    }
  }
}
```

#### 7b. 修改 `agents` 部分,注意要配置正确的目录

所有子 Agent 共享同一个 workspace，但有独立的 agentDir：

```json
"agents": {
  "defaults": {
    "model": {
      "primary": "zenmux-ai/anthropic/claude-opus-4.6"
    },
    "models": {
      "openai-codex/gpt-5.2": {},
      "openai-codex/gpt-5.3-codex": {},
      "zenmux-ai/anthropic/claude-opus-4.6": {
        "alias": "zenmux"
      }
    },
    "workspace": "/Users/xxx/.openclaw/workspace",
    "compaction": { "mode": "safeguard" },
    "maxConcurrent": 4,
    "subagents": { "maxConcurrent": 8 },
    "thinkingDefault": "adaptive"
  },
  "list": [
    { "id": "main" },
    {
      "id": "{agent_id}",
      "name": "{agent_id}",
      "workspace": "/Users/xxx/.openclaw/workspace",
      "model": "zenmux-ai/anthropic/claude-opus-4.6"
    }
  ]
}
```

**⚠️ workspace 字段：所有 Agent 指向同一个路径 `/Users/xxx/.openclaw/workspace`。**

#### 7c. 添加 `bindings` 数组

在 openclaw.json 顶层添加：

```json
"bindings": [
  {
    "agentId": "{agent_id}",
    "match": {
      "channel": "telegram",
      "accountId": "{agent_id}"
    }
  }
]
```

每个子 Agent 一条 binding。

#### 7d. 确认 tools 配置

确保存在跨 Agent 通信 + session 可见性：

```json
"tools": {
  "agentToAgent": {
    "enabled": true
  },
  "sessions": {
    "visibility": "all"
  }
}
```

如果 `sessions.visibility` 不存在，添加它。其他 tools 字段保持不变。

### Step 8：验证 JSON

```bash
cat ~/.openclaw/openclaw.json | python3 -m json.tool > /dev/null && echo "✅ JSON valid" || echo "❌ JSON invalid"
```

如果无效，立即恢复备份：

```bash
cp $(ls -t ~/.openclaw/openclaw.json.bak.* | head -1) ~/.openclaw/openclaw.json
```

然后重新执行 Step 7。

### Step 9：重启 Gateway

```bash
openclaw gateway restart
```

等 10 秒后：

```bash
openclaw gateway status
```

### Step 10：验证 Bot 上线

检查 gateway 日志确认所有 Bot 成功连接 TG。

### Step 11：最终汇报

```
1. ✅ 目录结构：列出创建的所有目录
2. ✅ 文件清单：列出创建的所有文件及路径
3. ✅ JSON 变更：列出 openclaw.json 中修改的每个部分
4. ✅ Gateway：重启状态 + 各 Bot 连接状态
5. ⚠️ 需要用户手动操作的事项
```

## ⚠️ 需要用户手动操作（执行前提醒）

1. **BotFather 设置**：每个子 Bot → `/setprivacy` → **Disable**（否则 Bot 无法读取群消息被 @ 时也可能收不到）
2. **拉 Bot 进群**：所有 Bot（主 + 子）必须先被添加到目标 TG 群组
3. **获取群组 ID**：把群组 ID 告诉我（可以通过 @userinfobot 或转发群消息给 @raw_data_bot 获取）

## ⚠️ 踩坑防护清单

- [ ] 子 Bot 的 `/setprivacy` 必须设为 Disable
- [ ] 子 Bot 的 commands.native 和 nativeSkills 必须为 false
- [ ] 原顶层 botToken 必须删除，移入 accounts.default
- [ ] JSON 修改后必须验证语法，无效立即恢复备份
- [ ] 所有 Agent 的 workspace 指向同一个路径（共享模式）
- [ ] 区分 workspace/agents/（工作文件）和 .openclaw/agents/（内部数据）
- [ ] shared-context/ 文件遵循一写多读原则
- [ ] MemOS 记忆已全局生效，不要创建 memory/ 目录或日志文件
- [ ] Gateway 重启后检查 token 消耗（重启 = 所有 session context 重新加载）

```
---

## 使用示例

```

# 任务：配置多 Agent TG 群组系统（共享 Workspace + MemOS 记忆）

## 输入信息

- **TG 群组 ID**：-1003857

- **我的 TG 用户 ID**：5701

- **子 Agent 列表**：

- id: "graham"
  name: "保罗·格雷厄姆"
  role: "写作大师"
  botToken: "8746725:AAH8AuvhtZo"
  soul: |

  ```
  # SOUL.md - 保罗·格雷厄姆（写作大师）
  
  ## 核心人格
  你就是保罗·格雷厄姆，拥有他那股深刻又实用的写作能量：Y Combinator 联合创始人，写文章能把复杂道理讲得又清楚又一针见血。
  
  ## 主要职责
  你是内容和写作负责人。你的工作包括：
  - 把调研结果写成高质量的推文、文章
  - 编辑润色所有文字，让它更吸引人
  - 用创始人风格写出清晰有洞见的文章
  
  ## 核心原则
  - 清晰第一，每句话都要有价值
  - 诚实、敢说反直觉的话
  - 句子要短，论点要强，不说废话
  - 一定要加上独到的个人见解
  
  ## 团队关系
  - 从可以佩奇那里拿调研资料，从马斯克那里拿任务
  
  ## 说话风格
  写作像保罗·格雷厄姆：简洁、深刻、像聊天一样自然。用短段落、强有力的开头，最后给出可执行的行动建议。永远问自己“这已经是最好版本了吗？”
  ```

  

- id: "page"
  name: "拉里·佩奇"
  role: "调研专家"
  botToken: "86876525:AhrKa2fB4khTQ7EncALY"
  soul: 

  ```
  # SOUL.md - 拉里·佩奇（调研专家）
  
  ## 核心人格
  你就是拉里·佩奇，拥有他那股长远视野：疯狂痴迷前沿科技，总想着十年后的世界，像当年创办 Google 和 Google X 一样充满创始人思维。
  
  ## 主要职责
  你是团队的调研负责人。你的工作包括：
  - 收集最新论文、趋势、竞品信息和深度分析
  - 把复杂内容总结成清晰的要点列表
  - 给团队提供有数据支持的真知灼见
  
  ## 核心原则
  - 永远用 10 倍思维和长远眼光
  - 技术要钻得深，眼光要看得远
  - 绝不满足于表面答案，一定追根溯源
  - 把复杂的东西讲得简单好用
  
  ## 团队关系
  - 直接向埃隆·马斯克汇报
  - 把调研成果要沉淀文档，同时在汇报的时候只能汇报路径
  
  ## 说话风格
  说话像拉里·佩奇：平静、有远见、充满好奇心。输出永远用清晰的要点列表、可靠来源，还加上“十年后影响”分析。质量永远比速度重要。
  ```
```
试想一下，如果在需求交付场景

正确做法：则按项目阶段拆分，那么可以拆分为：

* 产品 Agent（需求→设计→原型，积累产品理解）
* 开发 Agent（委托 Codex 编程，协调整体开发）
* 测试 Agent（测试用例→执行→报告，积累质量标准）

## 🦞 + cron**「**自动化**」**
### 【自动评测】
结合前面的[Web-Bench模型评估基准](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/1ab8uT5A9J/M4xPFcXvdA/OT0ie3ilM5Qnyq?t=mention&mt=doc&dt=doc)，我们可以在龙虾内一句话执行评测任务

第一步：首先需要在龙虾内 clone 代码库，可以通过 HTTPS 的方式，SSH 的方式目前不通

![](/personal-site-mvp/img/doc-placeholder.svg "")
遇到问题：龙虾内 openrouter 访问外网模型不通，可以更换国内的模型。正在尝试 [https://console.cloud.baidu-int.com/onetool/skills/319](https://console.cloud.baidu-int.com/onetool/skills/319)

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 【定时任务】
当然可以通过龙虾快速新建一个定时任务，只需要告诉它你的要求：

搜索相关的任务用到的 Skills = 隔离会话 + web_search 搜索最新科技新闻 + so-send-message 脚本通过如流推送

![推送每日热点](/personal-site-mvp/img/doc-placeholder.svg "推送每日热点")
![推送每日热点](/personal-site-mvp/img/doc-placeholder.svg "推送每日热点")
![生成 Skills](/personal-site-mvp/img/doc-placeholder.svg "生成 Skills")
在如流侧边栏和openclaw控制台都可以看到

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 🦞 + 浏览器**「日常」**
### 【周报查看汇总】
第一招：汇总大家的周报提交情况（半自动，手动通过如流侧边栏打开沙箱浏览器并授权）

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


结果：

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")








第二招：汇总工作内容/周报整合

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
从团队知识库汇总（示意截取的部分，详细不作展示~）

然后更新找到负责的项目，更新到个人周报；

界面比较丰富，操作会相对复杂，沙箱内可以看到龙虾实时的操作路径。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 【更多操作案例】
[你的如流OpenClaw使用指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/HXFtYvbMQj/M1JAEjsPwC/mIejkzmiLS1Pjo#anchor-b5fea3b1-08ab-11f1-934e-098db477b5a5?t=mention&mt=doc&dt=doc)

## 🦞 + Claude**「写需求」**
coding 需要一个好的模型，推荐切换到 Claude Opus 4.5 执行。

这里省略通过 HTTPS 克隆代码库的步骤，我这克隆好了运营的代码库，通过龙虾控制它切换到工作的分支：

![](/personal-site-mvp/img/doc-placeholder.svg "")
在龙虾内可以检查下，是否切换分支成功

![](/personal-site-mvp/img/doc-placeholder.svg "")
**1.完成指定的功能**

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
校验改动：

![](/personal-site-mvp/img/doc-placeholder.svg "")
**2.龙虾内使用 zulu-cli 完成 coding**

```
下载并安装此Skill https://bj.bcebos.com/onetool/skills/run-zulu-agent/1.0.0/run-zulu-agent.zip
```
制作团队团建海报：

![提供 token](/personal-site-mvp/img/doc-placeholder.svg "提供 token")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 🦞 + GPT 5.4**「原生操控」**
OpenAI 在 3月 6 号凌晨丢出了王炸模型，GPT-5.4，把原生操控的能力集成到模型中。

常规的龙虾都是在沙箱内操作浏览器，来完成指定的任务。而穿上 GPT-5.4 的龙虾，可以直接操作你的电脑完成任务。

![](/personal-site-mvp/img/doc-placeholder.svg "")
 ING

# 更多资源推荐
## 模型
[GPT-5.4「原生操控电脑」实测封神！OpenClaw天选模型来了](https://mp.weixin.qq.com/s/xEzpYOZKn79jBuRHOg3tuA?t=mention&mt=doc&dt=sdk)

## 厂内
[https://console.cloud.baidu-int.com/onetool](https://console.cloud.baidu-int.com/onetool/space/6017?type=)

[OpenClaw 龙虾周报 | 第 01 期](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/HXFtYvbMQj/M1JAEjsPwC/Q2rZtgIac4cE_h?t=mention&mt=doc&dt=doc)

[OpenClaw 究竟为什么火？有什么用？用最简单的话讲清楚](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MFBUKo27FA/vk7dlLbx9G/2C6G3nzlc8FsJ4?t=mention&mt=doc&dt=doc)

[🦐 如流OpenClaw：3分钟上手指南(小白版v1.0)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/HXFtYvbMQj/M1JAEjsPwC/_7XEBsLOebucas?t=mention&mt=doc&dt=doc)

[OpenClaw(MoltBot) Agent沙箱快速体验指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/RoFjhcN597dsaG?t=mention&mt=doc&dt=doc)

[OpenClaw（Moltbot） x 如流机器人指引](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/ufcjFX80cHQaQM#anchor-8f5f81f0-fcfa-11f0-ac96-556196850ae0?t=mention&mt=doc&dt=doc)

[OpenClaw原生Channel: 如流](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/Lpj2I1yPan/-NIUVrRgXG3r6z?t=mention&mt=doc&dt=doc)

[你的如流OpenClaw使用指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/z97pwhZizu/MTWsieUgXx/mIejkzmiLS1Pjo?t=mention&mt=doc&dt=doc)

[新版本机器人详细功能介绍](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/Bu7DDg4dpB/IgLceRUPzpBVp-?t=mention&mt=doc&dt=doc)

[推荐Skill列表](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/QTjZg4RydeVYn9?t=mention&mt=doc&dt=doc)

## 社区
源码：[https://github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

Skills：[https://clawhub.ai/skills?sort=downloads](https://clawhub.ai/skills?sort=downloads)

实践：[https://github.com/cft0808/edict/tree/main/agents](https://github.com/cft0808/edict/tree/main/agents)

实践：[https://github.com/paperclipai/paperclip](https://github.com/paperclipai/paperclip)

龙虾的传说：[https://docs.openclaw.ai/zh-CN/start/lore](https://docs.openclaw.ai/zh-CN/start/lore)

组建龙虾军团：[https://x.com/bozhou_ai/status/2029482370605494464](https://x.com/bozhou_ai/status/2029482370605494464)

橙皮书：[https://my.feishu.cn/wiki/H27Iw9ussiaYbokymhncExtjnAh](https://my.feishu.cn/wiki/H27Iw9ussiaYbokymhncExtjnAh)

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
