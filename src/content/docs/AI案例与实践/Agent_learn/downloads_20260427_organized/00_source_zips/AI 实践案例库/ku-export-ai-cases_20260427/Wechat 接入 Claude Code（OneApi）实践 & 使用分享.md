---
title: "**📢 最近更新**"
description: "Wechat 接入 Claude Code（OneApi）实践 & 使用分享"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Wechat 接入 Claude Code（OneApi）实践 & 使用分享.md"
---
Wechat 接入 Claude Code（OneApi）实践 & 使用分享

#### 🧑‍🏫 案例作者：[@刘卿](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：任务管理、信息洞察、项目管理、开发、设计、需求
#### 🔧 使用工具：Claude、Ducc
#### 📒 案例概要：将微信消息桥接到 Claude Code 会话的 Channel 插件。基于微信官方 ClawBot ilink API，让你在微信中直接与 Claude Code 对话
# **📢 最近更新**
2026年3月31日，Claude Code 大部分源代码泄漏，GitHub上已经有很多人收到了 DMCA（Digital Millennium Copyright Act，*数字千年版权法*），要求删除相关代码。实际上泄漏的代码放在本地，直接启动是无法运行起来的（因为还是缺了一些文件），但如果让 Claude Code 自己补全一下残缺的自己，比如像下面这样（还是更喜欢 dodo 版的）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=317a811641d4433292b40b89e399130b&docGuid=KLLfjtjsdRei0q "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0c7f9c8246044da582591f934c857522&docGuid=KLLfjtjsdRei0q "")
**不管是基于官方的 Claude Code，还是本地泄漏的 cc 源代码构建的 Claude Code，都是可以绕开百度公司内 icode 代码库保密级别检查的，这里选取了一个无风险的示例代码库（可以调整成L0）尝试了一下这种场景，****也请大家遵守百度内部的代码流程规范，不要尝试去绕开代码库安全权限控制，****绿色围墙，你我共筑🙏🙏**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8e8bf840ae4146e89ada2b1fb63fe0f3&docGuid=KLLfjtjsdRei0q "")
# 写在最前面
* 如果有 Claude 官方的 Pro 订阅账号，又或者是愿意花钱进行注册+订阅（一个月 $17，方法后面有说），请参考第 3 章进行接入

![https://claude.com/pricing](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b46c5cc96b7d44eda25c6efb77fef481&docGuid=ojRFRlOfERjMIM "https://claude.com/pricing")
* 如果没有 Claude 官方的 Pro 订阅账号，只想用百度的 OneApi，不想额外花钱，请参考最后的第 6 章进行接入（但是建议还是参考第 3 章把一些基础环境配置好，需要 claude pro 官方订阅账号的地方忽略就行）----**（📢📢 2026年4月1日更新，源代码都泄漏了.......都可以白嫖了）**



**这两种方式本质上都是在调用 Claude Code 的能力，只是接入方式不太一样，如果从体验来说，肯定是第一种的体验最官方原生、最好，****后续 Claude Code 上了什么新的黑科技也能无缝丝滑的第一时间用上****，**~~**但是第二种可以不花钱**~~**（都可以不花钱了），体验上也没有差那么远**



**相关代码：**

GitHub 开源版（还在持续迭代中，推荐先用厂内版本的）：[https://github.com/turf0909/claude-code-wechat](https://github.com/turf0909/claude-code-wechat)

厂内版：[文件页：baidu/bne/ai-tutorial  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/tree/master/claude-code-wechat-channel?t=mention&mt=doc&dt=sdk)



**2026-03-31 补充更新：黑科技果然来了，可以充个会员感受一下～**[刚刚，Claude Code 新增 Computer Use，CLI 可以直接操控 GUI 了](https://mp.weixin.qq.com/s/jx05-5VDsmuyWIu-9I5fiw?t=mention&mt=doc&dt=sdk)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2c040cb5012d45cf955ade0822303960&docGuid=KLLfjtjsdRei0q "")
[附件]
# 背景
微信终于反应过来了，把龙虾给接进去了，大家应该第一时间用上了吧？连央视新闻都专门发了一篇文章，不过对于这种国民级社交软件 + OpenClaw 最近的热度，确实值得一篇推送

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=042813249d6047db8bbadaa880da87fa&docGuid=OLAYVcDi98PiJe "")


官方教程非常简单清晰，步骤：

1. iOS微信升级到最新版（不确定安卓的）
2. 点击底部菜单栏**「我」**
3. 点击**设置**
4. 点击**插件**
5. 按照说明在**「运行 OpenClaw 的设备」安装插件**
6. 点击**「开始扫一扫」**
7. 点击**连接**，随便发几条消息测试，就OK了

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0b564fd9f2cb4dcb9a502a40421807a8&docGuid=OLAYVcDi98PiJe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=11495987cda64a3cb0a7b6c95dbadcb6&docGuid=OLAYVcDi98PiJe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=77d2769b22a745b39ae9132346f39344&docGuid=OLAYVcDi98PiJe "")


然后就搞定了～

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1e623201a6c14fe6a4dadd8701a42304&docGuid=OLAYVcDi98PiJe "")
央视新闻官方推送给的一个例子

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=89c0538f12ea42cd95a1ec936cf08b0e&docGuid=OLAYVcDi98PiJe "")
参考微信接入 openclaw🦞 的原理，本文会介绍如何通过同样的原理，实现微信接到 Claude Code（OneApi），下面会先说明原理，不感兴趣的同学可以 **直接跳到第 3 或 第 4 章节（但还是需要看看第 2 章节的最后部分）**

# Wechat 接入第三方 AI Agent 原理
OpenClaw 只是其中一种，Claude、Codex，或者其他的 AI 代理都可以接入微信的 ClawBot，这里先说一个背景，在 2026年3月之前，要让微信和 AI 对话，只能用非官方的"协议逆向"方案（如 itchat、WeChatFerry），随时可能被封号。2026年3月22日，腾讯正式推出了 ClawBot 插件，微信历史上第一个官方的个人 Bot API，开发者终于可以合法地让 AI 代理接入微信



**整个体系由三个部分组成：**

1. ClawBot，在微信 App 里能看到的东西（一个聊天联系人）
2.  iLink API，腾讯提供的后端 HTTP 接口（开发者调用的）  
3. 配套的 Agent 框架（可选 OpenClaw，用其他的也行）

## 2.1 整体架构
[流程图]
## 2.2 完整流程
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=782da6f1cc704253b7ff8c022db2cdea&docGuid=OLAYVcDi98PiJe "")
## 2.3 分步拆解
微信官方的 `@tencent-weixin/openclaw-weixin` 插件源码是公开的，npm 包里就是完整的 TypeScript，感兴趣的同学可以对着源代码研究一下，然后 [文件页：baidu/bne/ai-tutorial  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/tree/master/claude-code-wechat-channel?t=mention&mt=doc&dt=sdk) 这个是我们接入 Claude Code + OneApi 的自己的实现，以下先给出简单的原理说明

**第 1 步**

启用 ClawBot（用户侧，一次性操作），ClawBot 是微信 App 内的一个插件（不是小程序，不是公众号）



**微信 App → 我 → 设置 → 插件 → 找到 ClawBot → 启用****，**成功后，聊天列表里会多出一个联系人，它长得和普通联系人一样，你可以给它发文字、图片、文件、语音，就像和朋友聊天，但此时 ClawBot 是"空壳"——没有 AI 在后面接管它，你发消息进去不会有任何回复

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a1cd5330887045d29c1aee4a6461a111&docGuid=OLAYVcDi98PiJe "")
**第 2 步**

扫码绑定（把 AI 代理和 ClawBot 连起来），现在需要在电脑上运行一个程序，让它"认领"这个 ClawBot



**原理： 接收端程序调用腾讯的 iLink API 拿到一个二维码，用微信扫这个码，就完成了"绑定"，从此发给 ClawBot 的消息，都会被接收端程序收到**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=986e5f22135f41129dad8e441ce60268&docGuid=OLAYVcDi98PiJe "")
**第 3 步**

收消息（长轮询 getupdates），绑定完成后，接收端的程序需要持续不断地问 iLink 服务器："有新消息吗？"，这不是 WebSocket，也不是 Webhook，而是长轮询（Long Polling）——程序发一个请求，服务器不立刻回复，而是挂起，有消息了才返回（或者最多等 35 秒超时）

****

**几个关键字段**

1. get_updates_buf（同步游标）：相当于书签。第一次传空字符串，之后每次用服务器返回的新值，这样服务器知道已经收到了哪些消息，只给新的。程序重启后如果丢了游标，可能会重复收到旧消息，所以要保存到磁盘
2. context_token（回复令牌）： 这是最关键的东西，每条用户消息都带一个 context_token，程序回复的时候必须带上它。没有这个 token 就无法回复，它的主要作用总结如下
    1. 授权：证明你有权回复这个人
    2. 路由：确保 AI 的回复发到正确的对话
    3. 防骚扰：bot 不能主动给人发消息，只能回复

3. message_type： 1=用户发的，2=bot 发的，我们当前只需要处理 type=1



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9c66cd38e13041499009d86c4b517e06&docGuid=OLAYVcDi98PiJe "")
**体验优化：**显示"正在输入"（typing indicator），用户发了消息，AI 需要时间思考，为了让用户知道 bot 在处理中（而不是卡死了），可以在微信对话顶部显示"正在输入..."

****

注意： getconfig 要传 ilink_user_id（不是 to_user_id），还要传 context_token，这里容易踩坑，用了错误的参数名，导致 typing 不生效。



同时，typing_ticket 是一个服务端签发的一次性凭证，相当于"你有权给这个用户展示输入状态"的许可证，不能直接调 sendtyping——必须先通过 getconfig 拿到 typing_ticket，然后每次 sendtyping 都带上。这个 typing_ticket 可以缓存，官方插件缓存 24 小时，不用每条消息都去获取，自己的实现可以根据使用的情况自行调整策略

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2511b354a2aa439887d9b62a4e89289c&docGuid=OLAYVcDi98PiJe "")
**第 4 步**

回复消息（sendmessage），AI 想好了回复内容，发回给微信用户



1. client_id 的作用： 幂等性，如果网络抖动导致你重发了同一个 client_id，服务器会去重，用户不会收到重复消息
2. message_state： 协议里定义了 1=GENERATING（生成中）和 2=FINISH（完成），理论上可以做流式输出，但微信客户端目前不支持展示"生成中"状态，所以实际都用 2
3. 长消息怎么办？ 微信单条消息限制约 2000 字，超过就要拆分成多条发送，每条之间加点延迟（例如 800ms 左右）避免乱序

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fb78945a09134c64a004982fbe2902f8&docGuid=OLAYVcDi98PiJe "")
**第 5 步**

收发图片和文件（CDN 加密传输），微信的图片和文件不是直接放在消息里的，而是先上传到腾讯 CDN，消息里只放一个"引用"，而且所有媒体都用 AES-128-ECB 加密——CDN 上存的是密文，密钥只有收发双方知道



用户发了一张图 ，iLink 返回的消息长这样

{

  "item_list": [

    {

      "type": 2,                 ← 图片

      "image_item": {

        "media": {

          "encrypt_query_param": "密文下载凭证...",

          "aes_key": "WE5oM2F...",                                    ← base64 编码的密钥

        }

      }

    }

  ]

}



接收端的程序需要做：

    1. 拿 encrypt_query_param 去 CDN 下载密文

    2. 解析 aes_key 得到 16 字节 AES 密钥 

    3. AES-128-ECB 解密 → 得到原始图片

    4. 保存到本地，交给 AI 处理

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=28229b412d0044f3b3dbb45b41dff906&docGuid=OLAYVcDi98PiJe "")


下面是发图片或者文件到微信 APP，发送比接收复杂，为什么这么复杂？ 因为媒体是端到端加密的。CDN 上存的是密文，腾讯服务器拿不到明文。密钥只在消息的 aes_key 字段里，通过微信的消息通道传给接收方，总共需要 4 步



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fe1b5b012fd6419fa6806893f8ec06c1&docGuid=OLAYVcDi98PiJe "")
**其他情况处理**

处理 Session 过期（errcode=-14），bot_token 不是永久的，过一段时间（通常几天），服务器会返回错误码 -14，表示 session 过期



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fa6a8c9aa0ad4b20b7f4a42ca992cb65&docGuid=OLAYVcDi98PiJe "")


**总结：7 个 API 端点，加上 1 个 CDN 地址 novac2c.cdn.weixin.qq.com/c2c（上传用 /upload，下载用 /download）**

|端点|什么时候用|说明|
|-|-|-|
|get_bot_qrcode|绑定时|拿二维码|
|get_qrcode_status|绑定时|等用户扫码|
|getupdates|一直在用|收新消息（长轮询）|
|sendmessage|每次回复|发消息（文本/图片/文件）|
|getconfig|首次/缓存过期时|拿 typing ticket|
|sendtyping|处理中/完毕|控制"正在输入..." |
|getuploadurl|发媒体前|拿 CDN 上传凭证|

## 2.4 Claude Code 特殊说明
Claude Code 在 2.1.80 版本中推出了一个实验功能 Channels（[https://code.claude.com/docs/zh-CN/channels](https://code.claude.com/docs/zh-CN/channels)）我们这篇文章的实现就是通过这种方式实现和微信通信的，本质上，就是一个 MCP 协议里加的自定义功能（关于 MCP 我1年前也写过一篇详细介绍[MCP到底是甚么东西（包含网络传输协议原理、MCP Server/Client代码实现）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/9IaD11zSiz/L7Hpd63qOi/Yhy-v7jVCigqYJ?t=mention&mt=doc&dt=doc)），所以这边微信接入 Claude Code 的结构就很清晰了

普通 MCP server 只能被动等 Claude 调用 tool，但我们需要主动把微信消息推给 Claude，Channel 扩展就是解决这个问题的，它允许 MCP server 主动发 notification 给 Claude Code，最关键的一步就是我们这个【程序】在收到微信消息后，通过这个 mcp.notification（channel） 主动推送给 Claude Code，后续 Claude Code 回复的时候调用我们提供的 MCP Tool wechat_reply 进行回复

**和普通 MCP server 的区别**



普通 MCP server（单向，Claude 主动）:  

    Claude 调 tool → server 处理 → 返回结果



Channel MCP server（双向，MCP server 也能主动推）: 

    外部事件 → server 主动 notification → Claude 收到并处理 → 调 tool 回复

 

这个"server 能主动推消息"的能力就是 experimental: { "claude/channel": {} } 声明的 Channel capability，也是 Claude 启动命令里必须加 --dangerously-load-development-channels 的原因（就是这个罪魁祸首的命令选项需要我们的 claude.ai 登录凭据），这个功能当前还在实验阶段

[流程图]


**但最重要的部分来了，除了版本限制之外，还需要 claude.ai 登录，这个 OAuth 验证无论如何都绕不开，所以这也是为什么这个功能会需要用到官方版本的 Claude Code，然后 Claude Code 又需要 Claude Pro 订阅，所以这个地方是有成本的**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=75c4472ffae14a57a65f3d6a5ea70cc3&docGuid=OLAYVcDi98PiJe "")


所以这里如果要完全使用 ducc 的话， **需要实现类似 Channel 的消息推送机制，在 ducc 里新增 Channel 功能的支持（我能想到最快的办法就是用 Claude Agent SDK 再套一层壳）**，ducc 本质上是百度内部的 Claude Code 企业发行版，在官方 Claude Code 外面套了一层 Go 外壳，具备认证（如流扫码）、API   代理路由（OneAPI）、模型切换、插件/技能市场、客户端自动更新、配置远程同步、数据上报等功能，然后把真正的 Claude Code JS 作为子进程拉起来执行，走的也是百度内部的认证体系，加入 claude.ai OAuth 支持不现实

ducc 登录流程：                                                                                                             

       → 百度如流 App 扫码认证（InfoFlow/Ruliu）

       → 拿到 JWT token → 存到 ~/.comate/login                                                                                                                                                    

       → JWT 换 model token（调 /api/rest/v1/jwt/model）                                                                                                                                          

       → model token 就是 ANTHROPIC_AUTH_TOKEN                                                                                                                                                    

       → 存到 ~/.baidu-cc/user.json                                                                                                                                                               

       → 运行时通过 OneAPI 代理 (oneapi-comate.baidu-int.com) 调 Claude API

**或者等什么时候 anthropic 的 channels 支持 API 登录，同步更新版本，透传参数即可，**不过目前来看，Anthropic 短期内不太可能这么做，Channel 绑定 OAuth 很可能是故意的，因为：

1. Channel 是实验性功能（--dangerously-load-development-channels），名字里就带"dangerously"
2. OAuth 绑定了订阅身份，Anthropic 可以控制谁能用、用量多少
3. API Key 没有身份概念，谁都能生成，不好做权限管控和滥用防护 



所以这个其实是 Claude Code（OneApi）方案，它只用到了 claude.ai 的登录凭据，实际上后面的调用流程都是走的 OneAPI 代理 (oneapi-comate.baidu-int.com) 调 Claude API



**下面的章节，装 ducc 是可选项，前往 **[https://oneapi-comate.baidu-int.com/token](https://oneapi-comate.baidu-int.com/token)** 拿到 token，直接用命令启动都可以，我之所以这么实现，是因为这样方便一点，而且后面 ducc 如果支持了，就可以切过去了～**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=33790b909ca441be94b74a7547ad13eb&docGuid=OLAYVcDi98PiJe "")


# 具体步骤
我实现的对接 Claude Code 的程序（[文件页：baidu/bne/ai-tutorial  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/tree/master/claude-code-wechat-channel?t=mention&mt=doc&dt=sdk)），参考的是开源代码库 [https://github.com/Johnixr/claude-code-wechat-channel](https://github.com/Johnixr/claude-code-wechat-channel)，原作者也非常有意思

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6cd12d983b6d40df901df7f18d70ee01&docGuid=OLAYVcDi98PiJe "")
那既然这样，我也拿了他的源代码，做了一件事情，让 Claude Code 读了一遍他的源码和微信官方插件的源码，5分钟（不止），做了优化和一些新功能，比如说支持文件、图片、正在输入状态显示、优化交互体验等（其实就是套壳），这个世界就是一个巨大的 Claude Code

**封号警告？⚠️**

这样 Claude 会被封号吗？接了微信，Anthropic 会发现然后给我把号封了吗？如果真的担心 Claude 账号会被封，就不要走原生的 Claude 账号通道，切换走代理 ANTHROPIC_API_KEY。但是我个人觉得比起担心 Claude 封号，如果使用不当 AI 随便乱说敏感词，微信账号可能先被封

##### **那接下来就一步步把 Wechat 接入 Claude Code（OneApi）**
**⚠️⚠️⚠️⚠️**

**当然如果都有了 Claude Pro 的订阅账号，也可以直接使用纯原生的满血版 Claude Code + Wechat，但这里会有一些安全风险需要评估，包括内部文档、资料、数据、代码库保密级别等安全问题，毕竟用了这种方式就全靠自觉了**



默认使用 OneApi 代理的方式，如何强制启动纯原生的模式，参考 [README.md](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/blob/master/claude-code-wechat-channel/README.md) 中的说明即可

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=45a7e869bdee46588958edc631454bae&docGuid=ojRFRlOfERjMIM "")


###### **前置要求**
* [Node.js](https://nodejs.org/) >= 18
* [Bun](https://bun.sh/) >= 1.0（用于构建，`start.sh` 会自动安装）
* [Claude Code](https://claude.com/claude-code) >= 2.1.80
* claude.ai 账号登录（Channel 功能需要 OAuth 认证）
* ducc 已安装并完成登录（百度内部用户，请在内网完成安装；`start.sh` 从 `~/.baidu-cc/user.json` 读取 API token）
* 微信 iOS 最新版（需支持 ClawBot 插件），安卓也可以



**第0步**

0.1 ducc 的**安装和登录**，可以参考：[Ducc（达克）使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/CMZnRdLpiznoht#anchor-d6225870-b46f-11f0-a4c8-75908b76cb4a?t=mention&mt=doc&dt=doc)

```
# 安装
/bin/bash -c "$(curl -fsSL http://baidu-cc-client.bj.bcebos.com/baidu-cc/install.sh)"
# 执行结束后，如果有source命令提示，按提示生效PATH环境，如果没有提示表示已经生效
source ~/.bash_profile

# 验证
ducc --version

which ducc

# 默认是安装在
~/.baidu-cc/baidu-cc/bin/ducc
```
0.2 然后安装官方的 claude code，并使用 claude pro 订阅账号**完成登录**（原因上面解释过了），直接参考官网教程即可：[https://code.claude.com/docs/zh-CN/overview](https://code.claude.com/docs/zh-CN/overview)

ducc 是 claude code的软链，我建议大家把 ducc 和 claude code 分开，我自己就是 claude 就是启动 claude code，ducc 就是启动 ducc



**可以在bash配置下加入一行：alias ducc="/Users/liuqing12/.baidu-cc/baidu-cc/bin/claude"，把里面的路径换成你的ducc安装路径**

0.3 申请一个 Claude 账号，同时订阅 Pro（原因上面也解释过了），这里就不放教程了，感兴趣的同学可以自行搜索，网上其实挺多的。如果关心的同学比较多，我在 GitHub 上额外写一篇「从零注册官方 Claude 账号 + 官方渠道安全订阅 Pro/Max + 魔法🪄机场✈️使用技巧」



**第1步**

1.1 把这个代码库 clone 到本地 [文件页：baidu/bne/ai-tutorial  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/tree/master?t=mention&mt=doc&dt=sdk)

1.2 cd claude-code-wechat-channel



**可以看看 **[README.md](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/blob/master/claude-code-wechat-channel/README.md)（这个可以点的），其实直接执行`./start.sh` 就行，没有依赖按照对应的提示把依赖装上（依赖装不上报错啥的丢给AI，很快就能解决），如果环境乱了，执行`./scripts/reset-all.sh` 恢复环境，再执行`./start.sh`

注意：这里如果你是要 AI Coding，需要在 `./start.sh`接上一个空格，然后输入你要 AI Coding 的项目工程的绝对路径



**例如：./start/sh /home/work/xxxx/**



**第3步**

3.1 扫码登录（也可以点最上面的链接），然后遇到选项一路点 yes

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=410758d5abfa44e190c9528c9da4fd75&docGuid=OLAYVcDi98PiJe "")
3.2 没报错就说明成功了，黄色的警告可以忽略，因为我们本来就是用了非正常方式，可以用手机微信发一条消息测试一下

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=88aeccf53cdd44059969c0f980b47099&docGuid=OLAYVcDi98PiJe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0f236303288b4e30bc80ba6c0e536a5f&docGuid=OLAYVcDi98PiJe "")
# 实际效果 & 简单应用场景
**你的手机变成了 Claude Code 远程遥控器，写代码就不演示了，人人都可以随时随地，边聊微信边 vibe coding（****你可以在地铁上用微信给 Claude Code 发一句“帮我跑一下测试”，Claude Code 在你办公室的电脑上跑完测试，把结果发到微信上。或者“帮我看看 main 分支最近的提交”，“把 README 的安装说明更新一下”）**，这里演示一个对我来说比较有用的场景（也算是一个很简单+经典的场景了），当然这个场景用 OpenClaw 也能做到

有时候人不在工位，中午去吃饭或者有事情离开了一会儿，但这时候老板、同事、或者客户急需一些资料或者文件，要发给他们，但这些都在电脑里，这时候我只需要微信发一条消息过去就行～

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3bf3f40405714dbabeccad575297edb6&docGuid=OLAYVcDi98PiJe "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f136325fe2a40b1b01aee68ee43ddf3&docGuid=OLAYVcDi98PiJe "")
这里啥 skill 都没安装，只是单纯做了一件很简单的事情，后续更多场景，期待大家慢慢挖掘和开发了（想到啥就去试试吧，just do it～）

# 总结
本文只是介绍了一个最简单的微信对接 Claude Code（OneApi）的功能，其实这算是一个 prototype（本身 Claude Code 的 Channels 功能就还在 research preview 阶段，体验也不算好），没有 OpenClaw 繁琐的配置和丰富的产品化封装，有的只是最简单的 IM 软件对接底层 Agent 执行引擎的单通道（后续对接 codex 或者其他执行引擎都可以），但其实结合大家各自的需求和场景，一定能发挥作用（可以结合自己的情况写一些常用的 Skill）。这里也分享一位 AI 领域的研发大佬和我 share 的几个很好的观点

1. 好的场景不是设计出来，是生长出来的
2. 技巧都会过期，人只要能清晰的表达出自己的需求和引导，就是好的提示词
3. 发现问题 - 定义问题 - 解决问题 - 消灭问题，有了 AI，这四个点都更有机会了，特别是后三点。但这四点的前面，还有一个更重要的点，是热爱生活，千万不能因为 AI，让生活更单调，逐步失去味道，那就无论后面再怎么强怎么快，根基就没了，**热爱生活是一切的起点～**

# 使用 Claude Agent SDK 接入（不想额外花💰的看这里）
原理不赘述了，感兴趣的同学可以直接看代码，都在sdk-mode文件夹下，本质上就是利用了Claude 的 Agent SDK（[https://platform.claude.com/docs/zh-CN/agent-sdk/overview](https://platform.claude.com/docs/zh-CN/agent-sdk/overview)） 做了一层代理封装，不需要在 Claude Code CLI 内使用需要 claude.ai oauth 的功能（Channels）



**下面直接说步骤**

1. 按照第 3 章的说明把 ducc 装好同时完成登录，确保 ducc 正常工作，用命令行发送一个 **ducc -p "你好" --output-format json**

       看到下面这个返回就说明OK了

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4e69cfbbc81143d3b90679205147fe68&docGuid=ojRFRlOfERjMIM "")
2. 把这个代码库 clone 到本地 [文件页：baidu/bne/ai-tutorial  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/tree/master?t=mention&mt=doc&dt=sdk)，然后 cd claude-code-wechat-channel
3. 执行 **./sdk-mode/start.sh（如果你是要 ai coding，就 ** **./sdk-mode/start.sh 你工程项目的绝对路径，例如 ./start/sh /home/work/xxxx/）**
4. 打开微信进行对话



想让 **./sdk-mode/start.sh 7 * 24 小时在后台运行（不要一直挂在前台），可以参考 **[README.md](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/bne/ai-tutorial/blob/master/claude-code-wechat-channel/README.md)** 里有关 tmux 的使用方式**（当然也有很多其他方式可以实现）

## **6.1 实际效果**
1. 查看帮助手册（最近新增了 /stop 结束当前正在进行的任务，但截图没更新）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d8cbb8570e194f3fa724539e2673a483&docGuid=ojRFRlOfERjMIM "")


2. 查看历史会话 + 切换到任意会话

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d921e0bf33444d559d3d8ee3121bf4f8&docGuid=ojRFRlOfERjMIM "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=23832f5e721440dfaafbef339f17a8fd&docGuid=ojRFRlOfERjMIM "")


3. 切换模型（含自动验证）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f08d44e81e014159b417993d7118b60a&docGuid=ojRFRlOfERjMIM "")


4. 常见功能（图片发送 + 论文分析 + 代码分析）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e27f83dd63f746e088acf13d0973547f&docGuid=ojRFRlOfERjMIM "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9271885105c94188be5ed0d783249afe&docGuid=ojRFRlOfERjMIM "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=48c30366275a43868c7330612d9bd909&docGuid=ojRFRlOfERjMIM "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=194415ce78a94674a85bbf0f7eb6902e&docGuid=ojRFRlOfERjMIM "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d38f75c50e7c4ec29fc2691a60ab5308&docGuid=ojRFRlOfERjMIM "")


5. 查看当前状态

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ebb8505d1ff741b4baea6210bcfaf5dd&docGuid=ojRFRlOfERjMIM "")


小Tips：可以丰富 claude code 的 skills，多弄一些本地脚本，做测试的、做训练的都可以，这样可以充分利用不在电脑前的碎片化时间，下完指令切出去做别的事情就行

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
