---
title: "🔍 用 dodo 实践公有云 DNS 控制面日志排障：从告警到根因，AI 带你飞"
description: "用dodo实践公有云DNS日志排障：从告警到根因，AI 带你飞！效率提升67%，成本仅0.5元！"
date: "2026-04-27"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\用dodo实践公有云DNS日志排障：从告警到根因，AI 带你飞！效率提升67%，成本仅0.5元！.md"
---
用dodo实践公有云DNS日志排障：从告警到根因，AI 带你飞！效率提升67%，成本仅0.5元！

#### 🧑‍🏫 案例作者：[@陈廷政](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：运维
#### 🔧 使用工具：dodo
#### 📒 案例概要：AI助手dodo辅助DNS日志排障，从告警到代码分析自动完成，效率提升67%，成本仅0.5元。
# 🔍 用 dodo 实践公有云 DNS 控制面日志排障：从告警到根因，AI 带你飞
> 作者：陈廷政
> 日期：2026-03-24
> 标签：#AI实践 #DNS排障 #dodo #效能提升
---

## 📌 前言：一次"意外"的排障之旅
某个平凡的下午，我收到了一条告警：

```
{报警}{warning}{dudns-ctrl.IP.all:instance:controller_log_error}
{异常比例:0.0%}{正常(1):6.dudns-ctrl.IP.all}
{controller日志有error}{03-23 16:31:15}
```
以往遇到这种告警，我的内心 OS 是："又要开始漫长的日志查询、代码翻阅之旅了..." 😮‍💨

但这次不同，我决定试试百度工程效能部新推出的 AI 助手 **dodo**，看看它能不能帮我提效。

**剧透：结果超乎想象！** 🎉

---

## 🎯 任务目标
从 Noah 告警出发，完成以下完整排障流程：

1. ✅ 解析告警信息，提取关键参数
2. ✅ 访问 BLS 日志平台查询错误日志
3. ✅ 定位错误码和错误消息
4. ✅ 拉取相关代码仓库
5. ✅ 分析代码逻辑，找到根本原因
6. ✅ 给出排障建议

---

## 🚀 实战过程：dodo 带我飞
### 第一步：告警信息解析
我把告警信息直接丢给 dodo：

```
帮忙分析下原因：
{报警}{warning}{dudns-ctrl.IP.all:instance:controller_log_error}
{异常比例:0.0%}{正常(1):6.dudns-ctrl.IP.all}
{controller日志有error}{03-23 16:31:15}
http://alert.baidu.com/alert/detail/1jgbuMXCxo
```
**dodo 的反应**：

它没有直接给我一个"我不知道"的回复，而是：

1. 🌐 自动打开浏览器访问告警详情页面
2. 📊 提取关键信息：

    * 告警时间：2026-03-23 16:31:15（持续 69 秒）
    * 受影响主机：gajl-sys-dudnsctrl01.gajl
    * 异常机房：gajl（单机房问题）
    * 告警级别：warning（已恢复）

```
┌─────────────────────────────────────┐
│  告警详情（dodo 自动提取）          │
├─────────────────────────────────────┤
│ 时间：2026-03-23 16:31:15          │
│ 主机：gajl-sys-dudnsctrl01.gajl    │
│ 状态：已恢复 ✓                     │
│ 异常实例：6.dudns-ctrl.IP.all      │
└─────────────────────────────────────┘
```
**我的感受**：哇，这就是自动化的力量！我只是提供了一个链接，dodo 就自己去访问了页面并提取了关键信息。💪

---

### 第二步：BLS 日志平台查询
dodo 没有停下来，它继续问我：

> "现在让我去 BLS 日志平台查询具体的错误日志内容..."
然后它自动：

1. 🔐 登录 BLS 平台（[https://console.bce.baidu.com/bls/）](https://console.bce.baidu.com/bls/）)
2. 🔎 查询 `dudns-ctrl-api-log` 日志集
3. ⏰ 设置时间范围：2026-03-23 16:31:00 - 16:33:00
4. 🖥️ 筛选主机：gajl-sys-dudnsctrl01.gajl
5. 🚨 过滤日志级别：ERROR

几分钟后，dodo 返回了查询结果：

```
{
  "错误总数": 833,
  "错误级别": "ERROR",
  "错误位置": "base_common.py:553",
  "HTTP状态": 500,
  "错误代码": 11126,
  "错误消息": "zone flag is not running, action zone_update_svc_to_svip failed"
}
```
```
┌──────────────────────────────────────────┐
│  BLS 日志查询结果                        │
├──────────────────────────────────────────┤
│ ❌ 833 条相同错误                        │
│ 📍 base_common.py:553                    │
│ 🔢 错误码：11126 (EZONE_ERR)            │
│ 💬 "zone flag is not running"           │
└──────────────────────────────────────────┘
```
**我的感受**：这也太智能了吧！它不仅知道去哪里查日志，还知道怎么设置筛选条件。如果是我自己手动操作，光登录、找日志集、设置筛选条件就得花 10 分钟。🤯

---

### 第三步：代码仓库拉取与分析
接下来是重头戏。dodo 说：

> "让我拉取 dudns-controller 代码仓库，分析 base_common.py 第 553 行及 zone_update_svc_to_svip 操作逻辑..."
它做了什么？

1. 📦 自动拉取 `baidu/bin/npi-dudns-controller` 代码仓库
2. 🔍 定位 `base_common.py` 文件（在 `dnsop/common/` 目录下）
3. 📖 读取第 553 行及周边代码
4. 🕵️ 搜索 `zone_update_svc_to_svip` 相关代码
5. 📊 分析错误码定义（在 `lib/ERR.py` 中找到 `EZONE_ERR = 11126`）

然后，dodo 给我展示了关键代码片段：

**错误检查逻辑（zone_data.py:496-502）：**

```
# check flag whether is running
if record.flag != ZONE_CREATE_SUCCESS:
    self.code = ERR.EZONE_ERR
    self.message = "zone flag is not %s, action %s failed" \
        % (ZONE_CREATE_SUCCESS, ZONE_ACT_UPDATE_SVC_TO_SVIP)
    BaseCommon.log_controller_status(self.code, self.message, self.request_id, self.action, 2)
    return None
```
**日志记录逻辑（base_common.py:559-570）：**

```
@staticmethod
def log_controller_status(code, msg, req_id, action, level):
    if level == 0:
        GlobalLog.info("dudns controller %s, success, status 200. id: %s" % (action, req_id))
    elif level == 1:
        GlobalLog.warning("dudns controller %s, failed, status 400. id: %s, code: %d, msg: %s"
            % (action, req_id, code, msg))
    else:
        GlobalLog.error("dudns controller %s, failed, status 500. id: %s, code: %d, msg: %s"
            % (action, req_id, code, msg))
```
**我的感受**：天啊，它居然能自己去拉代码、找文件、定位代码行！我平时要做这些操作，得先找到代码库地址、git clone、grep 搜索关键字、vim 打开文件... 至少要 15 分钟。现在 dodo 几分钟就搞定了！🚀

---

### 第四步：根本原因分析
dodo 最后给出了清晰的根因分析：

> **根本原因**：
> `zone_update_svc_to_svip` 操作要求 zone 的 flag 状态必须为 "running"（即 ZONE_CREATE_SUCCESS）。但实际上该 zone 的 flag 状态不是 "running"，可能是 "processing"、"failed" 等其他状态。
> 代码在 zone_data.py 第 497 行进行了严格的前置条件检查：
> * 当 `record.flag != ZONE_CREATE_SUCCESS` 时，直接返回错误码 11126
> * 这个错误被记录为 level 2（ERROR），对应 HTTP 500 状态码
> * 在 1 分钟内（07:06:57 - 07:08:20）发生了 833 次相同错误
> 
**排障建议**：

1. 🔍 检查 zone 状态：查询对应 zone 在数据库中的 flag 字段值
2. ⏳ 等待 zone 就绪：如果 zone 状态是 "processing"，需要等待其变为 "running"
3. 🔧 修复失败 zone：如果 zone 状态是 "failed"，需要先删除后重新创建
4. 📊 监控告警：建立针对 zone 状态异常的监控，避免在非 "running" 状态下尝试执行 zone_update_svc_to_svip 操作

```
排障流程总结：
┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐
│ Noah 告警  │ -> │ BLS 日志   │ -> │ 代码分析   │ -> │ 根因定位   │
│ 提取关键词 │    │ 查询错误   │    │ 找到逻辑   │    │ 给出建议   │
└────────────┘    └────────────┘    └────────────┘    └────────────┘
```
---

## 📊 数据说话：效率提升有多大？
让我们用数据对比一下**传统排障**和 **dodo 辅助排障**的差异：

|维度|传统方式|dodo 辅助|提升|
|-|-|-|-|
|**总耗时**|~45 分钟|~15 分钟|**↓ 67%**|
|**操作步骤**|手动 10+ 步|交互 3 次|**↓ 70%**|
|**认知负担**|高（需记忆多个系统、命令）|低（自然语言交互）|**↓ 80%**|
|**出错概率**|中（URL 拼错、参数遗漏）|低（AI 自动处理）|**↓ 90%**|

**Token 消耗统计**（本次实践）：

* 输入 Token：~30,000
* 输出 Token：~28,000
* 总 Token：**~58,000**（约 0.5 元人民币成本）

**时间消耗明细**：

```
┌─────────────────────────────────┬──────────┬──────────┐
│ 步骤                            │ 传统方式 │ dodo方式 │
├─────────────────────────────────┼──────────┼──────────┤
│ 1. 解析告警信息                 │  5 min   │  1 min   │
│ 2. 登录BLS平台+查询日志         │ 10 min   │  3 min   │
│ 3. 拉取代码+定位文件            │ 15 min   │  5 min   │
│ 4. 阅读代码+分析逻辑            │ 10 min   │  4 min   │
│ 5. 总结根因+给出建议            │  5 min   │  2 min   │
├─────────────────────────────────┼──────────┼──────────┤
│ **总计**                        │ **45min**│ **15min**│
└─────────────────────────────────┴──────────┴──────────┘
```
**投入产出比（ROI）**：

* 人力成本节省：30 分钟 × 200 元/小时 ÷ 60 = **100 元**
* AI Token 成本：**0.5 元**
* **ROI = 100 / 0.5 = 200:1** 🎉

---

## 💎 收益与价值
### 1️⃣ 效率提升显著
* **时间节省**：从 45 分钟缩短到 15 分钟，节省 67% 时间
* **操作简化**：从 10+ 步手动操作简化为 3 次自然语言交互
* **认知减负**：不需要记忆多个系统的 URL、查询语法、代码路径

### 2️⃣ 质量提升明显
* **全面性**：dodo 会主动补全遗漏的步骤（比如自动拉取代码）
* **准确性**：减少了人为操作错误（URL 拼错、参数遗漏）
* **可追溯**：完整的排障流程记录，方便后续复盘和知识沉淀

### 3️⃣ 知识沉淀
通过这次实践，我不仅解决了问题，还学到了：

* Noah 告警的标准解析流程
* BLS 日志平台的高效查询方法
* dudns-controller 的核心代码逻辑
* zone 状态机的转换规则

更重要的是，dodo 帮我把这些知识系统化地整理了下来，形成了可复用的经验。

---

## 🤔 不足与启示
### 不足之处
1. **浏览器操作耗时较长**

    * 现象：访问 Noah 告警页面、BLS 日志平台等操作耗时 3-5 分钟
    * 原因：需要加载页面、登录、等待渲染
    * 改进方向：如果这些平台能提供 API 接口，dodo 可以直接调用，速度会更快

2. **需要多轮交互**

    * 现象：需要我说"继续"才会进行下一步
    * 原因：dodo 需要确认每一步的结果，避免方向错误
    * 改进方向：对于标准化的排障流程，可以设计成一键式操作

3. **依赖权限配置**

    * 现象：首次使用需要授权（BLS 登录、代码库访问）
    * 原因：涉及内部系统，需要身份认证
    * 改进方向：建立统一的权限管理机制

### 启示与思考
#### 1. AI 不是替代人，而是增强人的能力
dodo 没有完全替代我的思考，而是：

* 替我做了繁琐的操作（登录、查询、拉取代码）
* 给我提供了结构化的信息（日志摘要、代码片段）
* 帮我建立了知识连接（告警 → 日志 → 代码 → 根因）

我仍然需要：

* 判断分析结果是否合理
* 决定下一步的行动方案
* 将经验转化为可复用的知识

#### 2. 标准化流程最适合 AI 辅助
这次排障之所以效果好，是因为：

* 流程相对标准：告警 → 日志 → 代码 → 根因
* 数据源明确：Noah、BLS、iCode
* 目标清晰：找到根本原因

**启示**：越是标准化、重复性高的工作，越适合 AI 辅助。

#### 3. 人机协作的最佳实践
* **人**负责：
    * 定义问题和目标
    * 做出关键决策
    * 验证结果的合理性
    * 总结经验和规律

* **AI**负责：
    * 执行繁琐操作
    * 检索和整理信息
    * 提供结构化建议
    * 自动化重复工作


**最佳协作模式**：人提供方向和判断，AI 提供执行和支撑。

---

## 🎓 学习成果总结
通过这次实践，我系统学习了：

### 核心技能点
1. **Noah 告警分析**：解析告警信息，提取关键参数（时间、主机、操作类型、错误码）
2. **BLS 日志平台查询**：通过 BLS 平台查询错误日志，定位具体错误信息
3. **Sugar 报表系统**：查询 DNS zone 的用户数据和状态信息
4. **代码溯源分析**：从错误日志反推代码逻辑，定位根本原因

### 工具链掌握
* BLS 日志平台：[https://console.bce.baidu.com/bls/](https://console.bce.baidu.com/bls/)
* Sugar 报表系统：[https://sugar.baidu-int.com](https://sugar.baidu-int.com)
* iCode 代码库：baidu/bin/npi-dudns-controller

### 关键知识点
* zone 表的 flag 字段状态枚举：processing / running / failed / nsunchange
* zone_update_svc_to_svip 操作要求 zone 状态必须为 running
* 错误码 11126 (EZONE_ERR) 表示 zone 状态检查失败
* 错误日志记录在 dudns-ctrl-api-log 日志集中

---

## 🚀 后续优化方向
### 系统层面
1. **建立 zone 状态监控**

    * 监控 zone 状态变化，避免在非 running 状态下执行敏感操作
    * 设置状态转换超时告警

2. **完善告警规则**

    * 增加状态前置检查失败的专项告警
    * 区分不同类型的错误，避免告警疲劳

3. **优化错误提示**

    * 在错误消息中明确说明当前状态和期望状态
    * 提供自动修复建议

### 个人层面
1. **建立排障知识库**

    * 将常见问题的排障流程文档化
    * 形成可复用的排障模板

2. **提升 AI 使用技巧**

    * 学习更高效的 prompt 技巧
    * 掌握更多 dodo 的高级功能

3. **分享经验**

    * 在团队内分享 AI 辅助排障的最佳实践
    * 帮助更多同学提效

---

## 🎉 结语
这次用 dodo 实践 DNS 日志排障，让我深刻体会到了 AI 辅助研发的威力：

* ✅ **效率提升**：67% 的时间节省
* ✅ **质量提升**：更全面、更准确的分析
* ✅ **知识沉淀**：系统化的学习和总结

更重要的是，这次经历让我重新思考了**人与 AI 的关系**：

> AI 不是来替代我们的，而是来增强我们的能力的。
> 未来的研发，不是"人 vs AI"，而是"人 + AI"。
如果你也想体验 dodo 的强大能力，欢迎加入 **dodo 用户群（群号：12645561）**，和其他小伙伴一起交流使用技巧、反馈问题或提出建议！

让我们一起，用 AI 让研发工作更高效、更有趣！🚀

---

**附录：完整排障流程图**

```
                     🚨 Noah 告警触发
                            │
                            ↓
              ┌─────────────────────────┐
              │  Step 1: 解析告警信息   │
              │  - 提取时间、主机       │
              │  - 识别异常类型         │
              └─────────────────────────┘
                            │
                            ↓
              ┌─────────────────────────┐
              │  Step 2: BLS 日志查询   │
              │  - 登录 BLS 平台        │
              │  - 查询错误日志         │
              │  - 提取错误码和消息     │
              └─────────────────────────┘
                            │
                            ↓
              ┌─────────────────────────┐
              │  Step 3: 代码溯源分析   │
              │  - 拉取代码仓库         │
              │  - 定位错误代码行       │
              │  - 分析业务逻辑         │
              └─────────────────────────┘
                            │
                            ↓
              ┌─────────────────────────┐
              │  Step 4: 根因定位       │
              │  - zone 状态检查失败    │
              │  - 前置条件不满足       │
              │  - 给出修复建议         │
              └─────────────────────────┘
                            │
                            ↓
                     ✅ 问题解决！
```
---

> 📝 **文档版本**：v1.0
> 📅 **最后更新**：2026-03-24
> 👤 **作者**：陈廷政 ([chentingzheng@baidu.com](mailto:chentingzheng@baidu.com))
> 🏷️ **关键词**：AI实践、DNS排障、dodo、效能提升、BLS日志、代码分析
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
