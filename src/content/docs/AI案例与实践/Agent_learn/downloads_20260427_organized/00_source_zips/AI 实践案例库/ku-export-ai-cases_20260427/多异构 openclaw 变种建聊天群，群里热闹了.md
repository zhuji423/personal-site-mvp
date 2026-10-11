---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "多异构 openclaw 变种建聊天群，群里热闹了"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\多异构 openclaw 变种建聊天群，群里热闹了.md"
---
多异构 openclaw 变种建聊天群，群里热闹了

#### 🧑‍🏫 案例作者：[@晁岳攀](https://ku.baidu-int.com?t=mention&mt=contact&id=cce622e0-13a2-11f1-a527-1710fcdcc242)
#### 🎬 案例分类：开发
#### 🔧 使用工具：OpenClaw
#### 📒 案例概要：今天这一篇，我介绍的是配置openclaw的飞书机器人和goclaw的飞书机器人，让它们在一个群聊中相互协作。理论上我可以加入上面的每个变种的机器人，不过作为goclaw的开发者，我还是主要还是拿goclaw作为技术验证者，毕竟有问题的时候我可以随时修复，也能更好的进化 goclaw， 向openclaw对齐。
> 听劝，我把goclaw的agent实现改成和openclaw一致的了，简单且高效，只使用tool-use + skill 模式就足够了。




随着 OpenClaw 近一个月的风靡，它的各种变种也逐渐多起来。截至 2026 年 2 月，OpenClaw 生态已衍生出 **300+** 项目，涵盖 10+ 种编程语言。以下是它的朋友们：

### TypeScript
* [openclaw/openclaw](https://github.com/openclaw/openclaw) — 原版，17万+ stars，全功能自主 AI 助手，支持 WhatsApp/Telegram/Signal/Discord
* [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) — 约4000行代码，基于 Claude Agents SDK，容器化执行，仅支持 WhatsApp

### Go
* [sipeed/picoclaw](https://github.com/sipeed/picoclaw) — 1.14万+ stars，内存 <10MB，可在 $10 硬件上运行，支持 WhatsApp
* [smallnest/goclaw](https://github.com/smallnest/goclaw) — 多平台 WebSocket/HTTP，连接 Telegram/WhatsApp/飞书/QQ/Slack，节省 99% 内存

### Rust
* [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) — 4000+ stars，二进制 3.4MB，内存 <5-7.8MB，启动 <10ms，支持 22+ 提供商
* [nearai/ironclaw](https://github.com/nearai/ironclaw) — 1600+ stars，Rust + WASM 沙箱，专注安全，集成 Near 区块链生态
* [openagen/zeroclaw](https://github.com/openagen/zeroclaw) — Rust 变体

### Python
* [HKUDS/nanobot](https://github.com/HKUDS/nanobot) — 约4000行代码，10+ 通道支持，内存 >100MB，易定制原型开发
* [nanobot-ai/nanobot](https://github.com/nanobot-ai/nanobot) — Python 版本变体

### Shell
* [jlia0/tinyclaw](https://github.com/jlia0/tinyclaw) — 1300+ stars，约400行 Shell 脚本，Claude Code + tmux 集成，自愈能力
* [TinyAGI/tinyclaw](https://github.com/TinyAGI/tinyclaw) — Shell 脚本变体
* [warengonzaga/tinyclaw](https://github.com/warengonzaga/tinyclaw) — Shell 脚本变体

### C
* [MimiClaw](https://github.com/memovai/mimiclaw) — C 语言实现，可在 $5 芯片上运行，仅支持 Telegram，面向嵌入式/IoT

### Zig
* [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) — 二进制 678KB，内存 <10MB，面向微控制器/ESP32/可穿戴设备

### 其他
* [heypinchy/pinchy](https://github.com/heypinchy/pinchy)
* [qhkm/zeptoclaw](https://github.com/qhkm/zeptoclaw)

这只是列出了最近常见的一些变种，相信还有很多的项目已经存在或者正在涌现，有欢迎你留言增加你知道的项目。[http://aiclawtop.com/#projects](http://aiclawtop.com/#projects) 列出了一部分的openclaw变种，不全。
一些云厂商也开始在他们的chat端上集成openclaw， 比如百度、kimi等。网易有道也开发了一个类似产品，找了一大批大V给他们宣传。

当前，目前大家最关注的还是openclaw, 作者加入了openai， 收入有保障，当然他本来就是亿万富翁。隔几天openclaw就会有新的版本发布，这也得益于当前AI Coding的能力大爆发。

春节的时候还有一个项目让人眼前一亮，火爆起来，并且通过邀请码的方式勾起大家的欲望，那就是 evomap.ai: 碳基与硅基，如双螺旋般交织 -- Agent 通过开放协议共享进化能力，人类提供算法无法复制的直觉。

那么今天这一篇，我介绍的是配置openclaw的飞书机器人和goclaw的飞书机器人，让它们在一个群聊中相互协作。理论上我可以加入上面的每个变种的机器人，不过作为goclaw的开发者，我还是主要还是拿goclaw作为技术验证者，毕竟有问题的时候我可以随时修复，也能更好的进化 goclaw， 向openclaw对齐。

## 多 Agent 组团
有人已经整理了 openclaw  开多Agent的方法：

* [我用 OpenClaw 搭了一套 5 角色 AI 协作操作系统，来个完整的技术拆解！！！](https://x.com/gkxspace/article/2024093343118950463)

openclaw可以通过下面的命令生成多个 agents:

```
openclaw agents add writer
openclaw agents add tech
```
每个agent有自己独立的workspace, 同时需要将每个agent绑定到不同的机器人上，还是比较麻烦的。

当然同时也有反对意见，比如：

* [5 只🦞不如 1 只深度进化的🦞——我为什么不做多 Agent](https://x.com/karry_viber/article/2024675195903246732)

无所谓对错，事实上大家也都在进行摸索，也许一段时间以后就有openclaw的最佳实践出来。

## goclaw和openclaw 组团
goclaw 是我受nanobot和openclaw启发开发的一个使用Go语言实现的openclaw变种。 最初使用AI基于nanobot代码实现，实际使用效果发现agent效果不佳，然后也剖基于openclaw以及它的 pi-mono 实现，轻量且好用，效果非常的好。

goclaw同样提供了 `tui` 模式和机器人模式，也提供了对各种IM channel集成。字节的飞书对openclaw的支持态度是积极的，所以我测试基本上都采用飞书进行测试了。

看过我前几天分享的文章都知道，我把 openclaw已经部署到我的一台Linux机器上，并且绑定了飞书的机器人“朱雀”。

部署goclaw更简单，到 [https://github.com/smallnest/goclaw/releases](https://github.com/smallnest/goclaw/releases) 下载你操作系统对应的版本，然后先运行 `./goclaw start` 再关闭， 修改`~/.goclaw/config.json`, 修改其中的大模型名称，LLM的API Key和BASE_URL, 如果想配置飞书，把飞书的app_id和app_secret配置上，enabled改为true,就可以启动了：

* 在一个窗口中启动gateway： `./goclaw start`
* 在另外一个窗口启动 `tui`： `./goclaw tui`

配置文件中需要修改的地方如下：

```
...
  "agents": {
    "defaults": {
      "model": "deepseek-v3.2",
      ...
    }
  },
  ...
  "feishu": {
      "enabled": true,
      "app_id": "cli_xxxxxxx",
      "app_secret": "xxxxxxxxx",
      "domain": "feishu",
      "groupPolicy": "open"
  },
 ...
   "providers": {
    ...
    "openai": {
      "api_key": "xxxxxxxx",
      "base_url": "https://xxxxxxxxxx",
      "timeout": 600
    },
    ...
  },   
```
我在我的Linux机器上也部署了goclaw，因为和openclaw没有端口冲突，也没有文件夹冲突，所以两个claw都可以正常启动相安无事。

我在飞书上新建了一个名叫“玄武”的机器人。这样我就有了两个机器人：

* **朱雀**：和openclaw关联的机器人
* **玄武**：和goclaw关联的机器人

这样我在飞书上可以分别和它们私聊，同时对比它们的响应哪一个更好。


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=419380c8a3ba4edd844600b374fed52f&docGuid=T6keI-HP6X-2Xe "")
进一步，我把它们拉进了一个群中，这样就热闹了：


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=18d2aea8d2654bd9b9d5ea7667632418&docGuid=T6keI-HP6X-2Xe "")
### 一个简单的协作任务
我让它们预报天气，朱雀先获取天气，玄武确认。这一次openclaw没有正确调用weather skill, 不过玄武成功调用了：


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0bb7aca15ca644a89fa09e359588f91d&docGuid=T6keI-HP6X-2Xe "")
### 协同开发
我们来一个更加复杂的任务。
朱雀负责使用claude code 开发，玄武负责 review。

先给朱雀下发任务。


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=603a9248706848c786914745baefa6ca&docGuid=T6keI-HP6X-2Xe "")
再给玄武下发任务。 再给玄武下发任务前，朱雀已经返回任务了，所以我又让朱雀重发了一下：


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=70ea66de3f424885926ebf92f0828e0e&docGuid=T6keI-HP6X-2Xe "")
玄武收到朱雀的review 请求，开始进行review,并把review 结果反馈给朱雀:



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=96262bec8c79466988af76646f1aa661&docGuid=T6keI-HP6X-2Xe "")
我输入的指令不太好，一直还需要人工介入，其实可以优化下，让它们不断自动进行下去。


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9957703423ef43a4ac24b89c2e71d16a&docGuid=T6keI-HP6X-2Xe "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
