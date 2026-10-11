---
title: "1、项目概述"
description: "和dodo一起开发信息流-TDA-Query Skill 实践分享"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\和dodo一起开发信息流-TDA-Query Skill 实践分享.md"
---
和dodo一起开发信息流-TDA-Query Skill 实践分享

#### 🧑‍🏫 案例作者：[@邵凯](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：数据分析
#### 🔧 使用工具：dodo、Ducc
#### 📒 案例概要：TDA-Query Skill（信息流数据查询助手）
📒 业务痛点：数据表众多（30+张）、字段复杂（每个表几十个字段），工程化的方式开发知识，解决业务数据分析痛点问题。
AI 不是要替代人，而是要放大人的能力。今天更强大了吗？

探索一下？渐进式披露、契约式引用

# 1、项目概述
## 背景与目标
**项目名称**：TDA-Query Skill（信息流数据查询助手）

**业务痛点**：

* 数据表众多（30+张）、字段复杂（每个表几十个字段），openflag、mode 等业务字段的比特位含义分散在各处，难以查找。
* SQL 语法门槛高，缺少系统性的文档和查询模板

**项目成果**：

* ✅ 完整的 tda-query Skill，覆盖 30+ 数据表
* ✅ 详细的字段文档（包含 openflag 比特位、mode 字段等）
* ✅ SQL 查询模板和使用示例

---

## Skill 最终成果
### 目录结构
```
> **生成时间**: 2026-03-26

---

## 📊 统计信息

| 项目 | 数量 |
|------|------|
| 总文件夹数 | 10 |
| 总文件数 | 24 |

---

## 🌲 完整目录树

```
feedtdasql/
└── .claude/
    ├── CLAUDE.md
    └── skills/
        └── tda-query/
            ├── SKILL.md
            ├── examples/
            │   ├── business-dictionary.md
            │   └── feed-examples.md
            ├── references/
            │   └── tables/
            │       ├── account/
            │       │   └── xxx.md
            │       ├── feed-adlib/
            │       │   ├── composeinfo.md
            ...........................
            │       ├── history/
            │       │   └── fengchao_biz_feed_optlog.md
            │       └── report/
            │           ├── xxxx.md
            └── templates/
                └── feed-query-templates.md
```
---

## 📁 文件夹列表

| # | 文件夹路径 | 说明 |
|---|-----------|------|
| 1 | `.claude/` | Claude Code 配置目录 |
| 2 | `.claude/skills/` | Skill 技能目录 |
| 3 | `.claude/skills/tda-query/` | TDA 查询技能 |
| 4 | `.claude/skills/tda-query/examples/` | 查询示例 |
| 5 | `.claude/skills/tda-query/references/` | 参考文档 |
| 6 | `.claude/skills/tda-query/references/tables/` | 数据表文档 |
| 7 | `.claude/skills/tda-query/references/tables/account/` | 账户信息表 |
| 8 | `.claude/skills/tda-query/references/tables/feed-adlib/` | 广告库切片表 |
| 9 | `.claude/skills/tda-query/references/tables/history/` | 历史操作记录表 |
| 10 | `.claude/skills/tda-query/references/tables/report/` | 报表数据表 |

---

## 📄 文件列表（按类型分类）

### 1. 核心配置文件

| 文件路径 | 说明 |
|---------|------|
| `.claude/CLAUDE.md` | Claude Code 项目说明文档 |
| `.claude/skills/tda-query/SKILL.md` | TDA 查询技能主文档 |

### 2. 示例文档（examples/）

| 文件路径 | 说明 |
|---------|------|
| `examples/business-dictionary.md` | 业务术语字典 |
| `examples/feed-examples.md` | 信息流查询示例 |

### 3. 模板文档（templates/）

### 4. 数据表文档（references/tables/）

#### 4.1 账户信息表（account/）

#### 4.2 广告库切片表（feed-adlib/）

#### 4.3 历史操作记录表（history/）

#### 4.4 报表数据表（report/）- 共4个文件

---
*文档生成时间：2026-03-26*
*维护者：shaokai*

```
### 效果
1、当前还在路上，持续迭代

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
---

# 2、完整开发历程
## 阶段 1：知识输入
### 基础知识提供指定设计模式：
给dodo的输入：

帮我把这个知识库 （[PM自助跑数指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/r-bYkNEv9L/j7hAfoEszr-o0W?t=mention&mt=doc&dt=doc)）  改造成claude code  skill 。

1、要求常用知识放  SKILL.md 

2、涉及到的较多的知识 放到 reference 文件夹、输出格式放的 templates 文件夹、脚本放到 scripts 文件夹、示例放到 examples 文件夹。

3、渐进式的设计模式。

### 裁剪冗余知识
发现生成skill 文档里有非信息流相关的信息，会导致sql 生成不准确，进行裁剪。并补充信息流常用跑数sql 作为示例生成examples

给dodo的输入：

我是信息流团队，不需要关注仅凤巢（fengchao）相关部分的知识。

同时分析这个知识库文档：[信息流常用跑数SQL](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/r-bYkNEv9L/tHMcflEwcJmn6W?t=mention&mt=doc&dt=doc)

里面有一些示例和更多信息流相关知识。

去掉这个skill 里所有凤巢相关的信息



### 细化信息流相关表字段信息
给dodo的输入：

1、每个table 表结构和字段含义作为一个参考文档，每个table 一个 md 文档。[信息流库(FC_Feed)表CREATE TABLE建表语句字段信息](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/HFvYssokSp/KPio8JLt2FsYC_?t=mention&mt=doc&dt=doc)使用这个文档里的表结构，补充对应表名对应的 字段信息。

SKILL.md 里建立一个速查表，记录每个表名称、含义、每个表的引用md文档。

2、关键表字段信息说明

unitsetting ： [unitsetting定义](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/r-bYkNEv9L/HZdpiBvkTr31AT?t=mention&mt=doc&dt=doc)

plansetting ：[plansetting定义](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/r-bYkNEv9L/RTOSiUCQ2vsdF_?t=mention&mt=doc&dt=doc)

usersetting ：[usersetting定义](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/r-bYkNEv9L/4jE1ankUzoSvBo?t=mention&mt=doc&dt=doc)

projectsetting：[projectsetting定义](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/r-bYkNEv9L/sfoxoZL9AMMrBY?t=mention&mt=doc&dt=doc)

这几个表用这个几个文档补充字段取值含义

3、参考文档 补充对应表 字段信息：[三、辅助表](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/r-bYkNEv9L/N_hbjQthkExXTW?t=mention&mt=doc&dt=doc)

### 更多来自tda 上相关离线表字段信息
给dodo的输入：从tda 上搜索离线表，复制表字段信息贴给dodo

1、cpd_ns.baikal_olap_feed.hourlyfeedsvideostats_t1

2、cpd_ns.baikal_olap_effective.hourlyfeedsnewtargetconversionstats_t1

```
用户、计划、单元、创意、视频粒度：展现、点击、消费 表：cpd_ns.baikal_olap_feed.hourlyfeedsvideostats_t1
字段：
序号    字段名称    描述    字段类型    取值样例    字段权限
1    
UserId
用户id    BIGINT        有
2    
Date
日期    STRING        有
3    
Hour
时刻    INT        有
4    
PlanId
计划id    BIGINT        有
5    
UnitId
单元id    BIGINT        有
6    
IdeaId
创意id    BIGINT        有
7    
VideoId
视频id    BIGINT        有
8    
Type
类型    INT        有
9    
MTag
推广设备    INT        有
10    
CMatchId
cmatch    INT        有
11    
Slot
slot    INT        有
12    
FeedFlowType
流量类型    INT        有
13    
PClicks
点击    BIGINT        有
14    
Pay
消费    BIGINT        有
15    
CpmPay
消费中cpm部分    BIGINT        有
16    
PageViews
展现    BIGINT        有
```
### 核心字段文档补充
#### 补充 openflag 字段说明
给dodo的输入：

帮我补充一下：相关表的 openflag 字段 ，[信息流各层级openflag取值定义](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/J7r1It3PG5/I1YRmU5vRohGmL?t=mention&mt=doc&dt=doc)

#### 添加新的 mode 字段
给dodo 的输入：

如下表增加字段：

projectinfo：

`projectmode` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '项目类型。0：普通项目，1：省心投项目',

planinfo：

  `planmode` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '计划类型。0：普通方案，1：省心投方案',

unitinfo：

  `unitmode` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '0：普通单元，1：省心投单元',

ideainfo：

  `ideamode` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创意类型，0：普通创意，1：省心投创意',

## 阶段 2：修改优化SKLL存在的问题
阅读、试用当前版本的SKILL内容，可以发现一下可以优化的点，进行调整。

#### 修复 SKILL.md 错误引用
给dodo 的输入：

SKILL 文档这个内容都是错误的，详细的 md 文档引用路由都错了

[附带了正确的表结构信息，展示了实际存在的文件路径]

#### **添加的重要提醒（这些是关键经验、易错点）**
给dodo的输入：

1、报表数据（如 fengchao_biz_feed_idea_scp_olap）统计消费时，

  不要加 `AND isdel=0` 条件，因为已删除的创意在删除前产生的消费仍然是有效的。

  只有查询广告库切片数据（如 ideainfo）时才需要过滤 isdel。

2、消费统计一般需要将单位转换为元

3、计算用户消费、计划消费、单元消费、创意消费 使用`udw_ns.default.fengchao_biz_feed_idea_scp_olap`  按照用户、计划、单元进行汇总即可

明确要计算项目消费的时使用 `cpd_ns.baikal_olap_feed.hourlyfeedsprojectstats_t1`

明确要统计视频消费的时使用 `cpd_ns.baikal_olap_feed.hourlyfeedsvideostats_t1` 

明确要统计视频转化的时使用 `cpd_ns.baikal_olap_effective.hourlyfeedsnewtargetconversionstats_t1`

4、多表关联时必须指定表别名，避免字段名称重名导致问题

---

# 3、知识输入方法论
这是整个创建过程中最关键的部分。你通过 3** 种不同方式** 系统性地为我提供了知识、规则和上下文，让我能够准确理解业务并生成高质量产物。

### 方式 1：知识库文档链接（权威知识源）
**使用场景**：当需要详细的业务规则定义时

**示例**：

```
帮我补充一下：相关表的 openflag 字段，
https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/gv0WKdV3ZF/J7r1It3PG5/I1YRmU5vRohGmL
```
**为什么有效**：

* ✅** 便捷性：**自己手动从知识库复制粘贴其实很费劲
* ✅ **完整性**：包含完整的字段定义、比特位说明、业务含义

---

### 方式 2：结构化数据直接粘贴（精准输入）
**使用场景**：当需要补充字段定义或更新表结构时

**示例 1：mode 字段补充**

```
如下表增加字段：
projectinfo：`projectmode` int(11) unsigned NOT NULL DEFAULT '0'
             COMMENT '项目类型。0：普通项目，1：省心投项目',
planinfo：`planmode` int(11) unsigned NOT NULL DEFAULT '0'
          COMMENT '计划类型。0：普通方案，1：省心投方案',
```
**示例 2：完整表结构**

```
fengchao_biz_feed_idea_scp_olap 表结构：
date STRING 日期 20200522
ideaid BIGINT 创意ID 123123
unitid BIGINT 单元ID 123123
planid BIGINT 计划ID 123123
userid BIGINT 用户ID（账户ID） 630152
show BIGINT 展现数 1000
click BIGINT 点击数 500
pay BIGINT 消费（单位：分） 80
real_pv BIGINT 过滤掉延时的曝光数 10
```
**为什么有效**：

* ✅ **无歧义**：字段名、类型、说明、示例值一目了然
* ✅ **可复制**：我可以直接解析并转换为文档格式
* ✅ **高效**：比用自然语言描述"这个表有9个字段"快100倍
* ✅ **准确**：避免了口述过程中的误解

---

### 方式 3：问题示例 + 正确答案（纠错式反馈）
**使用场景**：当发现我生成的内容有错误时

**示例**：

```
SKILL 文档这个内容都是错误的，详细的 md 文档引用路由都错了

[然后附带了正确的表结构信息，展示了实际存在的文件路径]
```
---

### 知识输入的综合效果
通过上述 3 种方式的组合，你构建了一个**完整的知识闭环**：

```
知识库文档（权威来源）
    ↓
结构化数据（精准输入）
    ↓
我生成初版文档
    ↓
错误示例纠正（对比学习）
    ↓
我修复并生成正式版
    ↓
最终产物（符合规范、可追溯、可部署）icode 代码库管理
```


---

# 4、协作模式与工作方法
### 渐进式指导
没有一次性给出完整需求，而是：

* **第一步**：先补充最核心的字段文档（openflag、mode）
* **第二步**：发现结构问题后要求修复（SKILL.md 重写）
* **第三步**：完善项目配置（CLAUDE.md）
* **第四步**：持续添加新表（素材、人群、媒体包等）

这种方式让我能够：

* 每次专注解决一个具体问题
* 逐步理解项目的整体结构
* 在迭代中发现和修复遗留问题

---

# 5、关键经验总结
### 对 AI 助手的使用建议
#### 1. 分阶段提需求
* ✅ **先核心功能，再完善细节**

#### 2. 提供具体上下文
* ✅ **附带知识库链接、表结构、示例**
    * 好的做法：直接粘贴 SQL DDL 格式的字段定义
    * 避免：模糊描述"帮我加一些字段"

* ✅ **使用结构化格式传递信息**
    * 好的做法：


```
projectinfo：`projectmode` int(11) unsigned NOT NULL DEFAULT '0'
             COMMENT '项目类型。0：普通项目，1：省心投项目',
```
    * 避免：自然语言描述"projectinfo 表需要一个表示项目类型的字段"

#### 3. 及时反馈调整
* ✅ **发现问题立即指出并提供正确示例**
    * 好的做法："SKILL 文档这个内容都是错误的，详细的 md 文档引用路由都错了"
    * 避免：等到最后再一次性提出所有修改意见

* ✅ **指出问题时说明原因**
    * 好的做法：指出"引用路径错误"并展示正确的目录结构
    * 避免：只说"这个不对"


---

# 6、可复制的最佳实践
### 1. Skill 开发流程
#### 第一步：确定 Skill 的核心价值
* **明确业务痛点**：PM 跑数门槛高
* **定义目标用户**：PM 和业务人员
* **确定核心功能**：SQL 查询助手

#### 第二步：规划目录结构
```
.claude/skills/<skill-name>/
├── SKILL.md              # 主文档，包含使用说明和快速索引
├── references/           # 参考文档
│   ├── tables/          # 按业务分类的数据表文档
│   │   ├── feed-adlib/  # 广告库切片
│   │   ├── report/      # 报表数据
│   │   └── account/     # 账户信息
├── examples/            # 查询示例
└── templates/           # SQL 模板
```
#### 第三步：渐进式填充内容
1. **先核心**：补充最重要的表文档和字段说明
2. **再完善**：添加查询示例和 SQL 模板
3. **后优化**：重构文档结构，添加索引

#### 第四步：验证与迭代
1. **自我验证**：检查文档引用路径
2. **用户反馈**：根据使用情况调整
3. **持续更新**：添加新表、新字段

---

# 7、后续改进建议
#### 1. 补充 SQL 示例
**目标**：在 `examples/` 目录下添加更多实战 SQL

**内容**：

* 常见的统计分析场景
* 复杂查询的拆解步骤
* 性能优化技巧

**示例**：

* 统计每天的消费 TOP 10 账户
* 分析省心投 vs 普通项目的消费对比
* 查询撞线账户的消费趋势

---

#### 2. 添加故障排查
**目标**：在 `references/` 目录下添加 FAQ 文档

**内容**：

* 常见报错及解决方案
* 权限申请指南
* SQL 优化建议

**示例**：

* "Permission denied" → 如何申请表权限
* "Query timeout" → 如何优化查询性能
* "Data not found" → 检查 event_day 是否正确

---

#### 3. 性能优化建议
**目标**：在文档中添加大表查询的最佳实践

**内容**：

* 分区裁剪技巧（指定 event_day 范围）
* 避免全表扫描
* 使用 LIMIT 限制结果集

**示例**：

```
-- 不推荐：全表扫描
SELECT * FROM cpd_ns.fcdb6789.ideainfo WHERE userid = 123456;

-- 推荐：指定 event_day
SELECT * FROM cpd_ns.fcdb6789.ideainfo
WHERE event_day = '20260301' AND userid = 123456;
```
---

# 8、总结
这个过程证明了：**AI 不是要替代人，而是要放大人的能力。** 你的业务理解和决策能力，结合我的执行效率和文档生成能力，创造了 1+1>2 的效果。

---

# 9、特别感谢
dodo：有你真好，帮我提取转换知识，感谢dodo背后的团队 [报到！你的全能工作搭子dodo来啦！](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/z97pwhZizu/hy296wAZ7z/K_zUOSYGUYNlg6?t=mention&mt=doc&dt=doc)**厂内最佳助手没有之一**

ducc：缺你不可，厂内专属claude code，感谢ducc背后团队 [Ducc（达克）使用说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/B8wSneaLSC/CMZnRdLpiznoht#anchor-d6225870-b46f-11f0-a4c8-75908b76cb4a?t=mention&mt=doc&dt=doc)

---

*文档生成时间：2026-03-25*
*作者：dodo（在 shaokai 的指导下完成）*



更多分享：[Claude Code SKILL 渐进式披露](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/ziSuB9omVG/ujkFQ2FF1wqbYM?t=mention&mt=doc&dt=doc)


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
