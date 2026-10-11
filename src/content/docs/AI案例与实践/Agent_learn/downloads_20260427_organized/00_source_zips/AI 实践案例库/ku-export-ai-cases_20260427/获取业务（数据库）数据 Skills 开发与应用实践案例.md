---
title: "MySQL 专用"
description: "获取业务（数据库）数据 Skills 开发与应用实践案例"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\获取业务（数据库）数据 Skills 开发与应用实践案例.md"
---
获取业务（数据库）数据 Skills 开发与应用实践案例

#### 🧑‍🏫 案例作者：[@李静静](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：数据分析、测试
#### 🔧 使用工具：Ducc
#### 📒 案例概要：让 AI Agent帮你自动完成数据获取：
✅ 一句话搞定：用自然语言说出需求，AI 自动执行
✅ 安全可靠：强制只读模式，不会误删误改数据
✅ 统一操作：MySQL、Redis、MongoDB
[文档目录]
## 一、业务背景
### 1.1 我们遇到的问题
在日常测试工作中，经常需要从数据库获取业务数据，比如：

🔍 **问题排查**：程序出现问题，需要查看具体的数据
🧪 **测试准备**：需要从生产环境获取真实数据用于测试
📊 **数据分析**：分析用户行为、业务趋势等
🎭 **Mock 生成**：基于真实数据生成测试数据

但传统的数据获取方式存在很多痛点：

#### 痛点 1：操作繁琐，效率低 ⏱️
```
传统流程：
1. 登录跳板机（需要输入密码、验证码）
2. 连接数据库（记住IP、端口、账号密码）
3. 编写查询语句（MySQL、Redis、MongoDB 语法各不相同）
4. 执行查询
5. 手工复制粘贴结果
6. 格式转换（转成 JSON、Excel 等）
```
#### 痛点 2：容易误操作，有安全风险 ⚠️
* 使用有写权限的账号，容易误删、误改数据
* 密码直接写在脚本里，容易泄露到 Git 历史
* 生产数据库操作没有保护机制

### 1.2 我们的解决方案
我们开发了一个 **retrieving-database-data Skill**，让 AI Agent（Ducc/Claude Code）帮你自动完成数据获取：

✅ **一句话搞定**：用自然语言说出需求，AI 自动执行
✅ **安全可靠**：强制只读模式，不会误删误改数据
✅ **统一操作**：MySQL、Redis、MongoDB 用同一种方式
✅ **零学习成本**：不需要记命令、不需要记连接信息

---

## 二、Skill 工作流程
### 2.1 整体流程图
```
graph TB
    A[用户：自然语言描述需求] --> B[AI Agent 识别意图]
    B --> C{参数是否完整?}
    C -->|不完整| D[AI 询问缺失参数]
    D --> C
    C -->|完整| E[AI 构造执行命令]
    E --> F[安全检查：只读验证]
    F --> G[连接数据库]
    G --> H[执行数据查询]
    H --> I[格式化输出结果]
    I --> J[保存到文件/展示给用户]

    style A fill:#e1f5ff
    style F fill:#fff4e1
    style J fill:#e7f9e7
```
### 2.2 完整参数列表
```
--db-type          数据库类型 (mysql/redis/mongo)
--env              环境名称 (用于配置文件)
--host             数据库主机
--port             数据库端口
--database         数据库名称
--user             用户名
--password         密码（不推荐）
--password-env     密码环境变量名（推荐）
--config           配置文件路径
--fields           逗号分隔字段名，只返回指定字段

# MySQL 专用
--table            表名
--query            SQL 查询（仅 SELECT）

# Redis 专用
--key              单个键
--keys             多个键（逗号分隔）
--pattern          键模式（如 "user:*"）
--decode           解码格式 (json/string/raw)

# MongoDB 专用
--collection       集合名称
--filter           查询过滤器（JSON）
--projection       投影（JSON）
--sort             排序（JSON）
--aggregate        聚合管道（JSON）

# 通用选项
--limit            限制返回数量
--page-size        分页大小
--page             页码（从 1 开始）
--count-only       仅返回数量
--batch-size       批量获取大小
--fields           仅返回指定字段（逗号分隔，如 "id,name,email"）
--output           输出文件路径
--format           输出格式 (json/yaml/csv/pretty)
--pretty           美化输出
--verbose          详细输出


批量查询选项:
--batch-field      批量查询的字段名（如 "id", "name", "status"）
--batch-values     批量查询的值列表（逗号分隔，如 "1,2,3"）
--batch-split-output   将批量查询结果分文件输出
--output-dir       批量查询分文件输出的目录
--output-pattern   批量查询输出文件名模式（默认: {{field}}_{{value}}.json）
```
### 2.3 流程说明
#### 第一步：用户用自然语言描述需求 💬
不需要记命令，直接说出你的需求：

```
"我想从 MySQL 数据库 10.138.27.208 获取 fetch_data 表的数据，
数据库名是 exec_record，端口 8306，用户名 root，
获取 100 条记录，保存到 output/users.json"
```
#### 第二步：AI Agent 理解并识别 🤖
AI Agent（Ducc/Claude Code）会：

* 识别关键词："MySQL"、"数据库"、"获取数据" → 触发 `fetching-database-data ` skill
* 提取参数：数据库类型、主机、端口、表名、限制条数、输出路径等

#### 第三步：参数完整性检查 ✅
如果参数不完整，AI 会主动询问：

```
AI: "我需要以下信息来连接数据库：
1. 数据库密码是什么？
2. 需要输出什么格式？(JSON/CSV/YAML)
3. 是否需要限制查询条件？"
```
#### 第四步：安全检查（核心！）🔒
在执行前，系统会自动进行安全验证：

* ✅ **只读验证**：确保只执行查询操作（SELECT/GET/FIND）
* ❌ **拦截写操作**：任何 INSERT/UPDATE/DELETE/DROP 都会被拒绝
* 🔐 **密码保护**：推荐使用环境变量，避免密码泄露

#### 第五步：连接并获取数据 🔄
系统会：

1. 使用提供的连接信息连接数据库
2. 执行查询操作
3. 自动处理分页、限制等逻辑

#### 第六步：格式化输出 📄
支持多种输出格式：

* **JSON**：适合程序处理
* **CSV**：适合导入 Excel
* **YAML**：适合配置文件
* **Pretty Print**：适合终端查看

---

## 三、实践案例
### 3.1 案例一：快速批量获取MySQL测试数据
#### 场景
需要从测试环境数据库获取 100 条用户数据，用于本地功能测试。**可支持输出整体数据/特定字段；批量查询可输出至整个文件/单个不同的文件。**

#### 传统方式（~5 分钟）
```
1. 打开终端，登录跳板机
   $ ssh user@jumphost.example.com
   输入密码、二次验证...

2. 连接 MySQL
   $ mysql -h 10.138.27.208 -P 8306 -u root -p
   输入密码...

3. 选择数据库并查询
   mysql> use exec_record;
   mysql> SELECT * FROM fetch_data LIMIT 100;

4. 复制结果到本地
   手工选中、Ctrl+C、Ctrl+V...

5. 转换格式
   使用在线工具或脚本转成 JSON...
```
**耗时**: 约 5 分钟
**痛点**: 步骤繁琐、容易出错、重复劳动

#### 使用 fetching-database-data（~10 秒）
**用户输入：**

```
我想从 MySQL 数据库获取用户数据：
- 主机：10.138.27.208
- 端口：8306
- 数据库：exec_record
- 用户名：root
- 密码环境变量： MYSQL_READONLY_PASSWORD
- 表名：fetch_data
- 限制：100 条记录
- 输出字段：name
- 输出到：output/users.json
- id 为 1,2,3 的用户信息

帮我查询 MySQL 数据库的订单数据：
- 连接信息：10.138.27.208:3306，数据库 exec_record，用户 root
- 密码环境变量：MYSQL_READONLY_PASSWORD
- SQL 查询：SELECT * FROM orders WHERE status='completed' AND created_at > '2026-01-01' LIMIT 100
- 输出格式：JSON，保存到 output/completed_orders.json
```
**调用Skill 自动执行：**

```
1. 识别需求 → 触发 retrieving-database-data skill
2. 检查依赖 → 自动安装 pymysql、pyyaml
3. 连接数据库 → 验证连接成功
4. 执行查询 → SELECT * FROM fetch_data WHERE id IN (1, 2, 3)
5. 保存结果 → ✓ Fetched 3 records → output/users.json (当前表只有三条数据)
```
**结果展示：**

```
查询结果：
✅ 批量查询成功！
执行的 SQL: SELECT * FROM fetch_data WHERE id IN (1, 2, 3)

查询结果：共 3 条记录，按 id 分组
{
  "1": [{"id": 1, "name": "lijingjing18"}],
  "2": [{"id": 2, "name": "zhangrui31"}],
  "3": [{"id": 3, "name": "yanshifeng"}]
}
成功获取 3 条记录（表中共有 3 条数据）
已过滤，只保留 name 字段
保存到：output/users.json
数据内容：
[
  {"name": "lijingjing18"}, 
  {"name": "zhangrui31"}, 
  {"name": "yanshifeng"}
]

成功过滤了其他字段（如 id），只保留了 name 字段
```

**优势**: 一句话搞定、自动化、零出错

### 3.2 案例二：从redis获取数据并输出csv格式
#### 场景
需要从测试环境数据库获取 20 条数据，用于本地功能测试。

#### 传统方式
```
1. 登录 Redis
2. 使用 KEYS session:* (危险！可能阻塞 Redis)
3. 逐个 GET 每个 key
4. 手工整理数据
5. 导入 Excel 分析
```
**问题**: KEYS 命令可能阻塞生产 Redis，影响业务

#### 使用 fetching-database-data Skill
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8068fd0de76644ff8fce91734ef35854&docGuid=lZt2eL2QM0GXoC "")
**自动调用Skill中的执行脚本**

```
cd /Users/lijingjing18/baidu/tpg-devops/lmm/data-plugins/data-construction-toolkit-1.0.0
&& python3 lib/data-gen/cli/fetch.py --db-type redis --host 10.27.143.106 --port 8379 --password xxxx --database 2 --pattern "*" --limit 20 --decode json --format csv --output output/redis.csv
```
**耗时**: 约 30 秒
**优势**: 自动化、结果直观、支持 csv格式

**SKill 自动使用安全的 SCAN 命令**：

* ✅ 使用 SCAN 代替 KEYS，不阻塞 Redis
* ✅ 自动限制数量，避免内存溢出
* ✅ 自动解码 JSON 格式
* ✅ 直接输出可分析的文件

### 3.3 案例三：使用配置文件获取数据库数据
#### 场景
对于经常访问的数据库，我们可以将数据库信息写入配置文件，方便直接获取数据

#### 使用 fetching-database-data** Skill**
```
"我要从数据库获取数据，使用配置文件mysql测试环境的信息。"
```
**调用Skill 检索配置文件，询问待确认信息**：

```
Read db_config.yaml
Globpattern: "**/db_config*.yaml"
Found 1 file
Read db_config.yaml

好的，我看到配置文件了。但是配置文件中使用了环境变量来存储密码（password_env）。要使用配置文件，我需要先设置环境变量。
Bash 使用配置文件从 MySQL 测试环境获取数据

✅ 使用配置文件获取数据成功！

已从 MySQL 测试环境成功获取数据：

配置文件: config/db_config.yaml
环境: test (测试环境)
数据库: 10.138.27.208:8306 / exec_record
表名: fetch_data
获取记录数: 3 条（表中实际只有 3 条记录）
输出文件: output/config_test.json
```
**使用配置文件的好处**：

* ✅ 统一管理数据库连接配置
* ✅ 支持多环境切换（test/prod）
* ✅ 密码通过环境变量管理更安全
* ✅ 命令行参数更简洁

---

## 四、思考与反思
### 4.1 我们做对了什么 ✅
#### 1. 安全是第一优先级
**设计理念**: 预防大于补救

我们在代码层面强制只读保护，而不是靠规范约束：

* ✅ 所有写操作（INSERT/UPDATE/DELETE/DROP）都会被拦截
* ✅ 推荐使用只读数据库账号
* ✅ 密码存在环境变量，不会泄露到代码仓库

#### 2. 用户体验至上
**设计理念**: 让复杂的事情变简单

* 自然语言交互，不需要记命令
* 参数不全时，AI 主动询问
* 统一的操作方式（MySQL/Redis/MongoDB）
* 多种输出格式自动适配

#### 3. AI 深度集成
**设计理念**: AI 是助手，不是工具

不是简单地"把命令行封装成 AI 能调用的"，而是：

* AI 通过Skill的调用 能理解用户的真实意图
* AI 通过Skill的调用 能主动收集缺失参数
* AI 通过Skill的调用 能检查依赖并自动安装
* AI 通过Skill的调用 能分析结果并给出建议

### 4.2 我们遇到的挑战 🤔
#### 挑战 1：大数据集如何处理？
**问题**: 有时需要获取几十万条数据，一次性加载会内存溢出。

**当前方案**:

* 提供分页参数（--page-size、--page）
* 建议用户分批获取

**改进方向**:

* 支持流式输出
* 自动分片并合并
* 提供进度条显示

#### 挑战 2：如何让用户信任 AI？
**问题**: 部分用户担心 AI 会执行危险操作。

**应对策略**:

1. **透明化**: AI 会先展示要执行的命令，用户确认后才执行
2. **安全保障**: 明确告知只读保护机制

### 4.4 经验总结 📝
#### 关键经验 1：安全机制必须代码强制
❌ **不要**: 依赖文档规范、用户自觉
✅ **要做**: 代码层面强制拦截、自动验证

#### 关键经验 2：简化操作才是王道
❌ **不要**: 提供一堆参数让用户选
✅ **要做**: 智能推荐、自动填充、主动询问

#### 关键经验 3：从真实场景出发
❌ **不要**: 闭门造车、想当然设计
✅ **要做**: 调研用户痛点、快速验证、持续迭代

---

## 五、未来展望&总结
### 5.1 后续需完善的能力
1. **数据脱敏功能**: 自动识别并脱敏敏感字段
2. **性能优化**: 支持大数据集流式输出
3. **跨数据库联合查询**: 一次查询多个数据源
4. **数据对比工具**: 自动对比不同环境的数据差异
5. **数据分析：**对于获取的数据进行不同层面的分析
6. **定时任务**: 支持定期获取数据并通知



**打造智能数据助手**

```
用户："最近一周订单量下降了，帮我查查原因"

AI：
1. 自动获取订单数据
2. 对比历史数据发现趋势
3. 关联用户行为数据分析
4. 生成可视化报告
5. 给出可能的原因和建议
```
---

### 5.2 关键要素
#### 成功的关键在于：
1. **安全优先**: 代码强制 + 多层保护
2. **简化操作**: 自然语言 + Skill调用

#### 可复制经验：
这个案例的经验可以推广到其他场景：

* ✅ **任何重复性操作** 都可以用 Skill 封装
* ✅ **任何需要安全保护的操作** 都应该代码强制
* ✅ **任何复杂命令** 都可以用 AI 简化
* ✅ **以用户体验为中心** 是成功的关键

---



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
