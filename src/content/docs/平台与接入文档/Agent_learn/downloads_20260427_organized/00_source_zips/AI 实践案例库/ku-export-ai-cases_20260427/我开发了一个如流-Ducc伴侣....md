---
title: "ChangeLOG 更新记录"
description: "我开发了一个如流-Ducc伴侣..."
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\我开发了一个如流-Ducc伴侣....md"
---
我开发了一个如流-Ducc伴侣...

#### 🧑‍🏫 案例作者：[@周豪哲](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：工作流自动化、开发
#### 🔧 使用工具：如流机器人、Ducc
#### 📒 案例概要：使用如流控制你的开发机！
## why petway


目前厂内的龙虾和Dodo都是基于沙盒打造的。但是但是但是

在沙盒中的限制比较多

同时如果要在自己的开发机上部署一个龙虾或者是Dodo也相对比较麻烦。

龙虾和Dodo的定位偏向于通用Agent，而我们在开发机上的需求往往是一个简单快速的编程助手，而非一个运行缓慢的龙虾。



**一个想法自然就产生了：我能不能通过如流控制开发机上的已经有的Coding Agent ，比如现在大家的开发机上应该都会有 Ducc (ClaudeCode)**

**在一周的碎片时间里面，我开发了 Petway --- 一个位于如流和开发机 ducc 中间的 gateway**

## 可用功能


* **直接在如流和你开发机上的ducc对话**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7651d749753b49b1bd940f1b262464ca&docGuid=Lh-lZOhqggKgqw "")
* **使用 /new 命令新建对话，使用 /sessions 或者是 /switch 命令在多个对话之间切换。 使用 /help 命令查看更多可用命令**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e13d078986ba41c9a414c3a52d7a3630&docGuid=Lh-lZOhqggKgqw "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2ac0c8be6f354bbd8668d30e7c5abedf&docGuid=Lh-lZOhqggKgqw "")


* **在如流上批准Ducc的写操作 接收 SubAgent 启动信息**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=44e54c740ad846eb9399a95ce50f945c&docGuid=Lh-lZOhqggKgqw "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e702bd11ed6742e382c559ba7242a3f6&docGuid=Lh-lZOhqggKgqw "")




demo 视频 （这里跑得慢是上游模型慢，不是petway自己跑得慢）



[附件]
# 


# ChangeLOG 更新记录
[CHANGELOG](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/vYG2DD61t2/1fbhex9fgj-fQA?t=mention&mt=doc&dt=doc)



现在Petway可以用表情回复你了！

0.5.0 版本 现在Petway会把代码diff在一个网页上展示，如流限制（不能展示太多文本）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=90eecfaff3cb4134bc9966585ab92a06&docGuid=6EYySECKX4A6FR "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8305bb5c506f4e128b8176293d667d62&docGuid=6EYySECKX4A6FR "")




0.4.1 版本 现在Petway可以像Dodo一样用表情回复了

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ea830a748fb441ae859cabe65c154b91&docGuid=Lh-lZOhqggKgqw "")
## 创建机器人
在如流通过和如流机器人服务号对话，直接创建

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8aa727f7c31b4a9cb8d146fec3be2823&docGuid=Lh-lZOhqggKgqw "")
机器人创建时候，权限记得选择，接收群聊@机器人消息，以及发送消息到群聊



在 [如流机器人管理后台](http://id.qy.baidu-int.com/static/ge/login.html#/) 创建/管理你的机器人，获取以下信息：

[http://id.qy.baidu-int.com/static/ge/login.html#/](http://id.qy.baidu-int.com/static/ge/login.html#/)



1. **app_key / app_secret** -- 在管理后台的机器人详情页获取
2. **encoding_aes_key** -- 配置"接收消息服务器"时，填写回调 URL 后点击"随机生成"即可得到 Token 和 EncodingAESKey（也可手动输入，22 个字符，范围 a-z A-Z 0-9）
3. **agent_id** -- 机器人的 agent ID，在机器人详情页可以看到
4. **group_id** -- 你要让机器人服务的群聊 ID
5. **回调地址** -- 填写 `http://<your-server-ip>:8965/callback`（需要先启动服务，后台才能验证通过）





步骤截图如下：



找到你的机器人

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ab102bde6cc745289e0a24efd95011fe&docGuid=Lh-lZOhqggKgqw "")


AppKey 和 AppSecret 这里也能获取到，点击下方设置接收消息服务器里面配置回调地址&获取aesKey  这里填地址and获取aeskey

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e5c4d23f2b074e49a0a86b8db16e8140&docGuid=Lh-lZOhqggKgqw "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fd74bfa8991b4cba9b1bbd825d4a26f8&docGuid=Lh-lZOhqggKgqw "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0c6a9ab2da9d4853861f4f11d6cfa3a2&docGuid=Lh-lZOhqggKgqw "")


## 快速开始
使用 Petway 需要 Python 3.12 以上环境，且 pip 已配置百度源（开发机默认已配置）。无需源码，直接装。

### 1. 安装 Python 3.12（CentOS 7）
开发机系统自带 Python 版本太旧，需要通过 deck 安装：

```
# 初始化 deck（如果还没有的话）
source /home/opt/deck/1.0/etc/bashrc

# 切换到 deck 2.0
deck switch 2.0

# 安装 Python 3.12
deck install python-3.12.0

# 将 Python 3.12 加入 PATH（写入 ~/.zshrc 或 ~/.bashrc）
export PATH="/home/work/.deck/2.0/python-3.12.0/bin:$PATH"

# 验证
python3 --version  # 应输出 Python 3.12.x
```
如果 `python3` 版本不对，把 `export PATH="/home/work/.deck/2.0/python-3.12.0/bin:$PATH"` 移到 `~/.zshrc` 或 `~/.bashrc` 的最上方。

### 2. 安装 Petway
```
# 方案 1: 使用 uv tool（推荐，永久安装）
pip3 install uv
uv tool install petway --index-url https://pip.baidu-int.com/simple/

# 方案 2: 使用 pip3
pip3 install petway --index-url https://pip.baidu-int.com/simple/

# 方案 3: 使用 --user 安装到用户目录
pip3 install --user petway --index-url https://pip.baidu-int.com/simple/
```
遇到 `externally-managed-environment` 错误时：

```
pip3 install --break-system-packages petway --index-url https://pip.baidu-int.com/simple/
```
### 3. 获取机器人凭证
在 [如流机器人管理后台](http://id.qy.baidu-int.com/static/ge/login.html#/) 创建机器人，记下：

|凭证|在哪拿|
|-|-|
|`app_key` / `app_secret`|机器人详情页|
|`encoding_aes_key`|"接收消息服务器"配置处，点"随机生成"（22 字符，a-z A-Z 0-9）|
|`agent_id`|机器人详情页|
|`group_id`|你要让机器人服务的群聊 ID|

### 4. 启动
```
petway
```
首次启动自动创建 `~/.petway/` 目录和默认配置文件 `~/.petway/app.toml`。

### 5. 编辑配置
编辑 `~/.petway/app.toml`，填写以下必填项：

```
app_name = "petway"
port = 8965

[infoflow]
app_key = "your_app_key"           # <-- 必填
app_secret = "your_app_secret"     # <-- 必填
encoding_aes_key = "your_key"      # <-- 必填，22 字符
agent_id = 123456                   # <-- 必填
group_id = 789012                   # <-- 必填

[whitelist]
users = ["your_username"]           # <-- 必填，如流用户名

[bridge]
enabled = true
default_agent = "claude"

[bridge.agents.claude]
backend = "subprocess"
work_dir = "/home/work/your-project"   # <-- 必填
```
### 6. 重启并配置回调
```
petway
```
回到如流机器人管理后台，回调地址填：

```
http://<your-server-ip>:8965/callback
```
点验证保存。完成。

---

## 更新
```
# uv tool
uv tool upgrade petway --index-url https://pip.baidu-int.com/simple/

# pip3
pip3 install --upgrade petway --index-url https://pip.baidu-int.com/simple/
```
---

## 使用
在群里直接 @机器人 或发消息即可。Petway 会为每个用户维护独立的 Ducc 会话。

### 斜杠命令
|命令|说明|
|-|-|
|`/new`|开始新会话|
|`/sessions`|查看当前会话列表|
|`/stop`|停止当前回复|
|`/add-group [群ID] [工作目录]`|添加群聊到允许列表（管理员）|
|`/remove-group <群ID>`|移除群聊授权（管理员）|
|`/list-groups`|列出已授权群聊（管理员）|

### 权限审批
当 Ducc 需要执行敏感操作（编辑文件、运行命令等）时，会发送交互卡片。只有会话发起者和白名单管理员可以点击批准。

---

## 配置说明
配置文件位置：`~/.petway/app.toml`

### 必填配置
```
[infoflow]
app_key = ""              # 机器人 AppKey
app_secret = ""           # 机器人 AppSecret
encoding_aes_key = ""     # 消息加解密密钥，22 字符
agent_id = 0              # 机器人 Agent ID
group_id = 0              # 默认群聊 ID

[whitelist]
users = []                # 管理员如流用户名列表

[bridge]
enabled = true
default_agent = "claude"

[bridge.agents.claude]
backend = "subprocess"
work_dir = "/home/work"   # Ducc 工作目录
```
### 处理中提示
用户发消息后，Petway 会给消息加一个 emoji 反应（默认键盘输入表情），表示正在处理。

```
[indicator]
delay = 1.0               # 延迟秒数，避免快速响应时闪烁
emoji_code = "d135"       # 如流 emoji 代码，为空时改为发文字消息
```
### 模型预设
可选。不配置则使用 CLI 默认模型。

```
[models.claude.default]
default = "claude-sonnet-4-20250514"
haiku = "claude-3-5-haiku-20241022"
sonnet = "claude-sonnet-4-20250514"
opus = "claude-opus-4-20250514"

[models.claude.opus_only]
default = "claude-opus-4-20250514"
opus = "claude-opus-4-20250514"
```
修改后新会话立即生效，无需重启。

### 群聊访问控制
Petway 按群聊维度控制访问：

* `config.infoflow.group_id` 配置的群聊始终允许
* 其他群聊通过 `/add-group` 命令添加

### 会话管理
```
[sessions]
keep_alive = 3600           # 空闲会话保持秒数
max_per_user = 10           # 每用户最大会话数
db_path = "~/.petway/sessions.db"
```
### Bridge 详细配置
```
[bridge]
enabled = true
default_agent = "claude"
max_sessions = 20           # 全局最大活跃会话数
max_per_agent = 10          # 单 Agent 最大活跃会话数
idle_timeout = 1800         # 空闲驱逐时间（秒）
max_lifetime = 7200         # 会话最大存活时间（秒）

[bridge.agents.claude]
backend = "subprocess"
work_dir = "/home/work"
cli_path = "ducc"           # CLI 路径，默认 ducc
permission_mode = "default" # default / bypassPermissions / acceptEdits / dontAsk
model = ""                  # 指定模型名称，空则用默认
verbose = true
mute_tools = ["Read", "Glob", "Grep", "WebFetch"]  # 静默通知的工具
```
### 完整配置参考
|配置项|默认值|说明|
|-|-|-|
|`port`|`8965`|服务监听端口|
|`[infoflow].*`|--|如流机器人凭证|
|`[whitelist].users`|`[]`|管理员用户名，支持热加载|
|`[indicator].delay`|`1.0`|处理中提示延迟秒数|
|`[indicator].emoji_code`|`"d135"`|emoji 代码，空则发文字|
|`[bridge].enabled`|`true`|启用 bridge 模式|
|`[bridge].default_agent`|`"claude"`|默认 Agent|
|`[bridge].max_sessions`|`50`|全局最大会话数|
|`[bridge].max_per_agent`|`30`|单 Agent 最大会话数|
|`[bridge.agents.<name>].permission_mode`|`"default"`|权限模式|
|`[bridge.agents.<name>].cli_path`|`"ducc"`|CLI 路径|
|`[bridge.agents.<name>].mute_tools`|--|静默工具列表|
|`[bridge.agents.<name>].allowed_tools`|`[]`|自动通过的工具|
|`[bridge.agents.<name>].disallowed_tools`|`[]`|禁止的工具|
|`[bridge.agents.<name>].system_prompt`|--|自定义系统提示词|
|`[bridge.agents.<name>].max_turns`|--|最大对话轮数|
|`[bridge.agents.<name>].setting_sources`|`[]`|设置来源|
|`[models.<backend>.<preset>]`|--|模型预设，可选|
|`[sessions].keep_alive`|`3600`|空闲保持秒数|
|`[sessions].max_per_user`|`10`|每用户最大会话|
|`[sessions].db_path`|`"~/.petway/sessions.db"`|数据库路径|
|`[logging].file_enabled`|`true`|日志写入文件|
|`[logging].log_dir`|`"~/.petway/logs"`|日志目录|
|`[logging].console_level`|`"INFO"`|控制台日志级别|
|`[logging].file_level`|`"DEBUG"`|文件日志级别|

---

## 文件位置
|文件|路径|
|-|-|
|配置文件|`~/.petway/app.toml`|
|日志|`~/.petway/logs/petway.log`|
|数据库|`~/.petway/sessions.db`|







[评审：DS-sousuo2023-10820 update doc](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/petway/reviews/120434050/files/base...latest/CHANGELOG.md?t=mention&mt=doc&dt=sdk)

欢迎大家一起建设Petway

后续可能会支持更多 agent 后端！也许是 Multi-Agent 联动？

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
