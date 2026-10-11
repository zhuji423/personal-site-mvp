---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "2 小时,0 行手写代码,我用 Claude 做了一个生产级 VSCode 插件"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\2 小时,0 行手写代码,我用 Claude 做了一个生产级 VSCode 插件.md"
---
2 小时,0 行手写代码,我用 Claude 做了一个生产级 VSCode 插件

#### 🧑‍🏫 案例作者：[@刘伟](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发
#### 🔧 使用工具：Claude
#### 📒 案例概要：之前没写过 VSCode 插件、没接触过 Chrome Cookie 加密机制、不了解 UUAP SSO。
2 小时后,独立做了一个能自动读取浏览器登录态、实时监控 Comate 模型用量的 插件。
之前没写过 VSCode 插件、没接触过 Chrome Cookie 加密机制、不了解 UUAP SSO。

2 小时后,独立做了一个能自动读取浏览器登录态、实时监控 Comate 模型用量的 VSCode 插件——8 个核心文件,1000+ 行代码,打包后 `.vsix` 可以直接分发给同事使用。

这篇文章记录这 2 小时真实发生的事。

0 行手写代码,不意味着什么都不用想。恰恰相反——我花了大量时间在判断:这个方案能不能落地、这个报错的根因是什么、Claude 给的方向是不是对的。代码是 Claude 写的,但每一个关键决策是我做的。

---

## 一、为什么做这个
每天用 Comate 写代码,但配额是月度的。经常到月底才发现快用完了,或者不知道哪个模型消耗最快。官方只有一个网页可以看用量:`https://oneapi-comate.baidu-int.com/mine`,每次打开都要切浏览器、登录 SSO、刷新——很烦。

想法很朴素:**能不能在 VSCode 状态栏实时看到配额?超过阈值还能有颜色告警。**

但真要做,门槛全是盲区:

* VSCode 插件开发没做过
* 内网接口要 SSO 登录,插件是独立进程,怎么拿到登录态?
* Chrome 的 Cookie 是加密的,macOS Keychain 怎么解?
* UUAP 的 cookie 分散在好几个域,怎么精确过滤?

全是陌生领域。但我想试试:**这种"每个环节都不会但整体目标清晰"的任务,AI 辅助到底能走多远。**

---

## 二、最终效果
先看成品:

**状态栏**(右下角常驻):

![](/personal-site-mvp/img/doc-placeholder.svg "")
```
🟢 1494.16/3000 (49.8%) · 2007 次   ← 正常
🟡 2200/3000  (73.3%) · 2007 次     ← 黄色警示(背景同步变黄)
🔴 2750/3000  (91.7%) · 2007 次     ← 红色警告(背景同步变红)
```
**详情面板**(点击状态栏打开):

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 月度卡片(已用 / 剩余 / 上限 / 累计请求)
* 月度进度条,70% 黄、90% 红
* 按来源使用(zulu / dodo / ducc / iCode / others 的饼状占比)
* 按模型统计表(Claude Opus / Sonnet / Haiku、GLM、MiniMax、Gemini)
* 按日统计表
* 原始响应调试视图(可折叠,对齐字段用)

**零打扰自动登录**:只要浏览器里登录过 Comate,插件启动时**静默从 Chrome SQLite 读 Cookie、解密、验证、使用**。用户全程不需要任何操作。

**失效自动恢复**:Cookie 过期时,插件**静默重读浏览器** → 验证 → 替换 → 重试。用户只看到状态栏闪了一下"重新认证"就恢复了。

---

## 三、系统架构
```
flowchart TD
    subgraph UI["🖥️ VSCode UI 层"]
        direction LR
        SB["状态栏<br/>🟢🟡🔴 实时用量"]
        DP["Webview 详情面板<br/>卡片/模型/日统计"]
        LW["Webview 登录向导<br/>三合一兜底"]
    end

    subgraph Core["⚙️ 核心逻辑"]
        direction TB
        TM["🔄 定时器<br/>60s 自动刷新"]
        FSM["🧠 认证状态机<br/>有Cookie → 测试 → 失败 → 静默恢复"]
        API["📡 API 客户端<br/>all_info / usage_statistics"]
    end

    subgraph Auth["🔐 鉴权层(核心难点)"]
        direction TB
        BC["🦀 浏览器 Cookie 读取<br/>SQLite + Keychain + AES-128"]
        CU["⚡ cURL 导入<br/>正则提取 Cookie 字段"]
        MP["📋 手动粘贴(兜底)"]
    end

    subgraph Storage["💾 本地存储"]
        SS[("OS Keychain<br/>vscode.SecretStorage")]
    end

    UI --> Core
    Core --> API
    Core --> Auth
    Auth --> SS
    SS --> API
    API -.Cookie 失效.-> FSM
    FSM -.自动恢复.-> BC
```
---

## 四、方法论:设计对话,而非让 AI 自由发挥
全程代码都是 Claude 写的,但**不是扔一句"帮我做个 VSCode 插件监控 Comate 用量"完事**。

我的流程是这样的:

```
确认目标(描述产品形态,给 Claude 看接口样例)
↓
Claude 给出方案,我判断哪些可行、哪些有坑
↓
让 Claude 写第一版,跑起来
↓
每次报错/不对劲,把具体信息贴给 Claude
↓
Claude 分析 + 修复,我验证
↓
功能稳定后,提迭代(图标/告警/自动化)
↓
循环
```
这个循环最关键的一步是**每次和 Claude 对话时提供"足够的上下文"**。

举个对比:

**差的提问**:"我的插件跑不起来,有错。"
→ Claude 只能猜一堆可能。

**好的提问**:"error TS6059: File '/Users/liuwei53/Desktop/vscode/extension.ts' is not under 'rootDir' '/Users/liuwei53/Desktop/vscode/src'."
→ Claude 立刻能给出"你把文件放错目录了,正确的结构是 xxx,执行 `mkdir -p src && mv ...` 这几条命令搞定"。

再比如,当 Cookie 读取出错时,Claude 让我贴真实响应,我把一整段 cURL 扔过去:

> `curl 'https://oneapi-comate.baidu-int.com/api/status' -H 'Accept: ...' -b 'UUAP_TRACE_TOKEN=...; SECURE_ZT_GW_TOKEN=...' ...`
Claude 立刻识别出:"关键的 SECURE_* cookie 全在父域上,我们的 SQL 查询只匹配了子域,漏掉了。修复方式是改成按 cookie 作用域精确匹配"。

**Claude 做 AI 的能力越来越强,但它吞吐上下文的能力比你贴出来的有限很多**。你得主动把关键信息喂进去——报错、真实响应、期望行为、已有代码。

**Claude 负责实现和验证,我负责判断和决策。** 做什么、先做哪个、这条路值不值得继续——这些是这 2 小时里真正花时间的地方。

---

## 五、系统真正的复杂度在哪里
### 5.1 鉴权:看似简单,实际是整个项目最难的部分
内网接口要 SSO 登录。插件不是浏览器,怎么拿到登录态?

我最初想当然以为这很容易。但实际 Claude 一上来就摆清楚了三条路,并直接给出了技术现实:

|方案|可行性|说明|
|-|-|-|
|手动粘贴 Cookie|✅ 最快|用户体验差,Cookie 过期要重填|
|浏览器内嵌 Webview 登录|⚠️ 坑多|VSCode webview 的 session 和浏览器隔离,SSO 还会禁止 iframe|
|从 Chrome SQLite 读 Cookie|✅ 好用|macOS Keychain 授权一次后永久无感|

我一开始倾向"Webview 登录",听起来最优雅。但 Claude 直白地告诉我:**"VSCode 扩展 API 不暴露 webview 的 cookie 读取能力,且 SSO 系统一般会设 X-Frame-Options: DENY,iframe 大概率被浏览器直接拒绝"**。

如果我不听这个警告,可能会花几小时在一个死路上。**Claude 在"告诉你什么方案不可行"上的价值,不亚于它写代码。**

最后选的是方案一先跑通,方案三作为终态——结合成一个"登录向导",三种方式一站式。

### 5.2 Chrome Cookie 加密:细节决定成败
macOS 上 Chrome 的 Cookie 存储方式:

1. SQLite 文件:`~/Library/Application Support/Google/Chrome/Default/Network/Cookies`
2. 加密方式:`v10` 前缀 + AES-128-CBC
3. 密钥派生:PBKDF2(从 Keychain 读的密码, 'saltysalt', 1003 轮, 16 字节, SHA1)
4. IV:16 个空格字符
5. **Chrome M118+ 还在明文前加了 32 字节 SHA256(host_key) 做 origin binding**

这最后一条最坑。如果不处理,解密出来的 cookie value 前 32 字节是乱码,表面看没报错但 API 会拒绝。Claude 在第一次实现时就把这个"旁路细节"写进去了:

```
if (plain.length > 32) {
  const hostHash = crypto.createHash('sha256').update(hostKey).digest();
  if (plain.slice(0, 32).equals(hostHash)) {
    return plain.slice(32).toString('utf8');  // 剥离 host hash 前缀
  }
}
```
我完全不知道这个机制的存在,也不会想到去问。**Claude 对这类"广为人知但我不知道"的细节的覆盖,是传统独立开发最难替代的价值。**

### 5.3 Cookie 作用域:SSO 场景下的大坑
这是我们调试中最久的一个问题。代码跑通了,从浏览器读到 **93 条 cookie**,但 API 始终返回 HTML(SSO 重定向页)。

为什么?因为 UUAP 是百度内部的 SSO,关键 cookie 分散在**好几个父域**:

* `oneapi-comate.baidu-int.com` — 子域本身的 `session`
* `.baidu-int.com` — 大部分 `SECURE_*` token
* `.uuap.*` — UUAP 自己的 token

我一开始写的 SQL 是 `host_key LIKE '%baidu-int.com%'`,看似够宽,但问题在于:

**不同域下会有同名 cookie**,比如多个站点都叫 `session`。我们读了 93 条 cookie,里面可能有 5-6 个不同的 `session`,合成 HTTP Cookie 头时按"最后写入"覆盖,结果**发给 oneapi-comate 的 **`session`** 是别的站点的**——服务端校验失败,返回 HTML,被我们错误地当成"Cookie 过期"。

调试过程:

1. **我**:状态栏显示"加载失败,Cookie 可能已过期"
2. **Claude**:先确认浏览器里能不能访问 API,再看实际返回的 HTML 是什么
3. **我**:贴上 `/api/status` 的完整 cURL
4. **Claude**:"看这些 `SECURE_*` 都在父域上,但我们可能同时读到了其他站点的同名 cookie。建议改成'按 cookie 作用域精确匹配',只取 host 完全匹配或父域作用域覆盖的"
5. **我**:改代码,验证,搞定

**这个问题的难点不在于"写一段代码",而在于"知道问题发生在哪"**。Claude 拿到 cURL 的一瞬间就定位到了,省下来的排查时间可能是一整天。

### 5.4 无感登录 + 自动恢复
基础方案跑通后,我提了个更高的要求:

> "能不能做到这个登录是用户无感知的?比如用户在浏览器登录过 oneapi 自动获取,没有登录再去引导呢?降低成本"
Claude 立刻给出了完整设计:

```
插件激活
  ↓
有保存的 cookie? → 试一次 API
  ├─ 成功 → 正常工作
  └─ 失败 ↓
            静默从浏览器读取(不弹任何 UI)
              ├─ 成功 → 验证有效 → 替换 cookie → 重试请求
              └─ 失败 → 这时才弹引导
```
设计里还包含了防御性细节,都是 Claude 主动加的:

* **验证步骤**:静默读到的 cookie 不直接保存,先 `fetchAllInfo` 试一下,真有效才替换
* **防无限循环**:`isRetry` 参数 + `silentRecoveryInFlight` 防止并发恢复
* **用户名独立处理**:这个必须用户提供,不能自动获取,所以单独引导

这种"想到用户可能遇到的边界情况,主动防御"的能力,远比我自己闭门造车高。**如果我自己写,可能要到用户反馈"疯狂弹窗"后才会想到加锁。**

---

## 六、关键转折:Claude 诚实的时候
### 6.1 直接否定我想走的路(Webview 登录)
我上来就想要 Webview 登录——在 VSCode 里嵌入登录页,用户点几下就好。Claude 没有顺着我说,而是直接指出两个致命问题:

1. VSCode webview 的 session 跟浏览器隔离,登录完的 cookie 在 webview 里,插件 API 拿不到
2. SSO 系统普遍禁止 iframe 嵌入(`X-Frame-Options: DENY`)

它说:"建议先用方案 A(手动粘贴)跑通,后面再看是否升级"。

**这是一个很好的"AI 诚实"的例子**。如果 AI 只是迎合用户,可能会先写一堆 webview 代码,跑起来发现不行,再回头推翻——浪费几小时。

### 6.2 看懂真实数据后立刻对齐字段
我贴出第一次 API 返回的 JSON 后,Claude 立刻对比出它猜的字段名跟实际不一致:

|之前猜的|实际字段|
|-|-|
|`data.quota` / `data.used_quota`|`data.monthly_quota_limit` / `data.monthly_used_quota`|
|`data[]` (数组)|`data.model_stats` + `data.daily_model_stats`|
|`count`|`request_count`|

它主动说:"模型汇总服务端已经算好了,前端不用再聚合"——还顺手优化了交互。

### 6.3 承认"浏览器自动读取"的局限,主动加 cURL 导入
自动读取调通后,Claude 主动说:**"浏览器自动读取偶尔会因为 SSO 多域 cookie 处理不全而失败"**,并加了 cURL 导入作为兜底。

现在的登录向导三方式并存:

* 🚀 **从浏览器读取**(推荐,一键)
* ⚡ **从 cURL 导入**(最稳,30 秒)
* 📋 **手动粘贴**(兜底)

即使自动方式失败,用户 30 秒也能搞定。**承认"我不能 100% 保证",并设计 fallback,这是成熟工程的标志**。

---

## 七、Claude 也会错:一些例子
对着这个项目用了 2 小时 Claude,不全是完美体验。它也会在一些地方犯错,以下都是真实发生的:

### 7.1 第一次写的字段名全猜错了
最初 Claude 猜的 `AllInfoResponse` 接口跟真实响应完全不同:

```
// Claude 第一版猜的
interface AllInfoResponse {
  data?: { quota?: number; used_quota?: number; ... }
}

// 实际长这样
interface AllInfoResponse {
  data?: { monthly_quota_limit?: number; monthly_used_quota?: number; ... }
}
```
它自己知道是猜的,在代码里还留了注释提醒我"第一次运行时,在 DevTools 里把真实 JSON 贴下来对比字段名"。但如果我没注意到这行注释、直接相信它的字段名,就会跑不起来还不知道为啥。

**应对**:永远拿真实响应验证 AI 猜的数据结构。

### 7.2 文件路径一再放错
过程中至少 3 次出现"文件不在正确目录"的问题——`extension.ts` 放在根目录而不是 `src/`、`launch.json` 放在根目录而不是 `.vscode/`。每次都是我先跑出 TS 报错,Claude 才反应过来。

**应对**:项目开始前就和 AI 对齐目录结构,并让 AI 每次创建文件时显式带上完整路径。

### 7.3 浏览器 Cookie 读取,第一版没考虑作用域
第一版的 SQL 查询直接 `host_key LIKE '%oneapi-comate.baidu-int.com%'`,导致 UUAP 父域的关键 cookie 漏读。后来又改成 `LIKE '%baidu-int.com%'`,又带来了同名 cookie 冲突。最后才改成按 cookie 作用域精确匹配。

如果我对 cookie 作用域规则不熟,可能会在"第一次修复有 bug"阶段放弃。Claude 的第一版不是最优解,需要多次迭代才收敛到正确的实现。

**应对**:涉及"广为知晓但你不熟"的领域,多问一句"这个方案有没有已知的坑/边界情况?"

### 7.4 整体感受:越到后期越需要反复提醒
小项目阶段(前 1 小时),Claude 对话连贯、记得住之前的决策。

到后期要加图标、改告警颜色、完善文档时,有时 Claude 会重新"猜"之前已经决定好的东西——比如重写 `updateStatusBar` 时,部分变量名和之前保存到的版本对不上。

**应对**:对长上下文项目,每次让 AI 改一个模块时,先把完整的现状贴出来;或者维护一份"当前代码状态"的速记文档。

---

## 八、0 行代码,我真正做的是什么
回看整个过程,我没写任何一行 TS 代码。但我花了大量时间在:

1. **描述目标**:什么叫"监控用量",长什么样,要哪些指标
2. **判断可行性**:Webview 登录能不能行、Chrome Cookie 能不能读
3. **提供真实数据**:贴 cURL、贴 API 响应、贴报错
4. **决策优先级**:先做最小可用,再加无感登录,再加三色告警
5. **验证结果**:状态栏对不对、面板好不好用、失效恢复符不符合预期
6. **反问和推广**:"能不能做成无感的"、"能不能加三色告警"

代码不是瓶颈。**这些"想清楚要什么、判断什么能做、拿到真实数据反馈"的事才是瓶颈**。Claude 不会替你做这些。

---

## 九、工程细节:最终产出了什么
```
comate-usage-monitor/
├── icon.png                      # 128x128 插件图标
├── icon_256.png                  # 高清版,README 用
├── package.json                  # 插件 manifest
├── README.md                     # 用户文档
├── CHANGELOG.md                  # 版本日志
├── .vscodeignore                 # 打包过滤
├── tsconfig.json
├── .vscode/
│   ├── launch.json               # F5 调试配置
│   └── tasks.json
└── src/
    ├── extension.ts              # 主入口,定时器 + 状态栏 + 恢复逻辑
    ├── api.ts                    # HTTP 客户端 + 类型定义
    ├── dashboard.ts              # Webview 详情面板(卡片/模型/日统计)
    ├── loginWizard.ts            # Webview 登录向导(三合一)
    └── browserCookies.ts         # Chrome SQLite + Keychain + AES-128
```
**代码规模**:约 1000 行 TypeScript。

**依赖**:零第三方 npm 包。所有功能用 Node 原生 API(`https`、`crypto`、`child_process`)和 VSCode API 完成。

**打包产物**:`comate-usage-monitor-0.0.2.vsix`,体积约 40KB。

---

## 十、结果
插件现在在我的 VSCode 里常驻,每次打开 VSCode 状态栏就显示当前用量,颜色一眼看出是否告急。Cookie 失效时会自动重读浏览器,无感恢复。

同事拿到 `.vsix` 文件 → `Cmd+Shift+P` → Install from VSIX → 输入用户名 → 完事。全程零配置。

---

## 附录:如果不用 AI,这个项目需要多少时间
### 技术栈覆盖
|领域|涉及内容|
|-|-|
|VSCode 扩展开发|Extension Host、StatusBarItem、Webview、SecretStorage、命令系统|
|前端|Webview 内的 HTML/CSS/JS,响应式布局,VSCode 主题色|
|Node.js|SQLite 操作、进程调用(`security`、`sqlite3`)、AES 加密|
|密码学|PBKDF2 派生密钥、AES-128-CBC 解密、Chrome M118+ host binding|
|操作系统|macOS Keychain API、文件系统、Chrome user data 目录结构|
|网络协议|HTTP/HTTPS 请求、Cookie 作用域规则、SSO 流程|
|工程化|TypeScript、vsce 打包、.vsix 分发|

### 时间估算(不用 AI)
|模块|估算工时|
|-|-|
|学 VSCode 扩展开发基础|1 周|
|设计产品形态(UI、交互、状态栏、面板)|2 天|
|Cookie 鉴权方案调研(这是最耗时的)|1 周|
|Chrome Cookie 加密细节研究(Keychain / AES / host hash)|3 天|
|Cookie 作用域正确性调试|2 天|
|核心功能实现(API、状态栏、定时器、面板)|1 周|
|无感登录 + 自动恢复|3 天|
|登录向导 Webview(UI + 交互)|2 天|
|cURL 导入 / 手动粘贴|1 天|
|图标设计|半天|
|文档(README / CHANGELOG)|1 天|
|打包、调试、联调|2 天|
|**合计**|**约 5 周**|

### 说明
* 按"没做过 VSCode 插件、但有前端基础的工程师"估算
* 最大不确定性在"Chrome Cookie 加密"—— 如果卡在某个环节(比如 M118+ 的 host hash 没搜到),可能多花几天
* 实际完成:**1 人,2 小时,0 行手写代码**

---

## 写在最后
这不是一个"AI 多神奇"的故事。而是一个"**人 + AI 协作的最佳实践**"的样本:

* **人提供**:真实需求、真实数据、方向判断、优先级决策
* **AI 提供**:陌生领域的知识、代码实现、边界情况提醒、可选方案对比

当你清楚自己要什么,当你愿意把真实上下文喂给 AI,当你在 AI 犯错时有判断力把它纠回来——**盲区再多,都可以靠"明确目标 + 快速反馈"在极短时间内完成原本不可能的事**。

代码是 AI 写的,但这个插件是我做的。

---

#### 工具:Claude Opus 4.7(通过 Claude.ai)
#### 插件文件:
[附件]
#### 插件链接：
[https://console.cloud.baidu-int.com/devops/icode/dev/marketplace/detail/liuwei53.comate-usage-monitor/0.0.2](https://console.cloud.baidu-int.com/devops/icode/dev/marketplace/detail/liuwei53.comate-usage-monitor/0.0.2)

####  文件内部分发,欢迎试用
#### 联系:@liuwei53
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
