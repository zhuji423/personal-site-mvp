---
title: "2. 构建知识图谱（首次运行）"
description: "Graphify + Ducc 构建本地代码知识图谱"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\Graphify + Ducc 构建本地代码知识图谱.md"
---
Graphify + Ducc 构建本地代码知识图谱

#### 🧑‍🏫 案例作者：[@杨桐](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：信息洞察、知识加工、开发
#### 🔧 使用工具：Ducc
#### 📒 案例概要：Graphify结合Ducc构建代码知识图谱，提升代码理解与开发效率，支持增量更新和自动监听。
## 概述


**Graphify** 是一个强大的知识图谱构建工具，可以将代码仓库、文档、论文等任何文件集合转换为可导航的知识图谱。结合 **Ducc（达克）** 代码助手，可以显著提升代码理解和开发效率。



[https://github.com/safishamsi/graphify](https://github.com/safishamsi/graphify)





**核心优势：Token效率大幅提升**

根据测试数据，使用Graphify后查询时的token消耗能降低到原始文件的1/71.5倍，即节省71.5倍的token。这意味着在Claude Code中询问代码架构问题时，不再需要让AI助手先grep一堆文件，而是直接读取精炼的知识图谱。



**Graphify采用两阶段处理流程与Claude Code完美结合：**

1. **AST解析阶段**：对代码文件使用tree-sitter做本地语法解析，提取类、函数、导入、调用关系等结构信息，全程本地运行、不调用LLM，完全零token消耗
2. **语义提取阶段**：对文档、论文、图片等非代码内容，通过Claude子代理并行处理，提取概念、关系、设计动机



**多模态支持能力**

Graphify支持代码、PDF、Markdown、截图、流程图、白板照片甚至外语图片等多种文件类型，通过Claude vision从这些内容中提取概念和关系，并把它们连接到同一张图里。



**持久化知识管理**

生成的图谱可以持久化存储，几周后查询无需重新读取原始文件。输出包括：

* `graph.html`：可交互的图谱，可点击节点、搜索、按社区过滤
* `GRAPH_REPORT.md`：核心节点、意外连接、建议问题的汇总报告
* `graph.json`：持久化图谱数据



**实际应用效果**

当Claude Code内置Graphify后，你问它"这个模块是做什么的"，它不再是从零开始读代码，而是直接引用图谱中的路径和关系。这对于：

* **大型代码库**：十几万行代码的项目
* **复杂架构**：多模块、多语言混合
* **知识密集型**：需要理解设计意图的业务
* **长期维护**：持久化图谱减少重复理解



---

## 快速开始
### 前置条件
* Python 3.8+
* 已安装 graphify（`pip install graphifyy`） 可以直接给claude-code说 安装并配置 [https://github.com/safishamsi/graphify](https://github.com/safishamsi/graphify)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e7f1bcb5f5d0455a8692f0ebaa2b5a60&docGuid=Y2815b4ElrG459 "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=788d8e93120a441998ee99b2b4670680&docGuid=Y2815b4ElrG459 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b527e7b5cff74753b82f76162261b42c&docGuid=Y2815b4ElrG459 "")




* Ducc（达克）代码助手

### 5 分钟快速上手
`# 1. 进入项目根目录
cd /path/to/your/project

# 2. 构建知识图谱（首次运行）
/graphify .

# 3. 查看生成的报告
cat graphify-out/GRAPH_REPORT.md

# 4. 在浏览器中查看可视化图谱
open graphify-out/graph.html  # Mac
# 或直接双击 graph.html 文件
`

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=16853fdae4874c9c8fcc18fce6a54367&docGuid=Y2815b4ElrG459 "")
---

## 详细使用指南
### 初始构建知识图谱
#### 基础命令
`# 对当前目录构建知识图谱
/graphify .

# 对指定路径构建
/graphify /path/to/codebase

# 深度模式（更多推断关系）
/graphify . --mode deep

# 跳过可视化（仅生成报告和JSON）
/graphify . --no-viz
`

#### 执行流程
Graphify 的构建过程包括以下步骤：

`Step 1: 文件检测
  ↓
Step 2: 结构提取 (AST) - 代码文件
  ↓
Step 3: 语义提取 (LLM) - 文档、图片
  ↓
Step 4: 图构建和聚类
  ↓
Step 5: 社区标注
  ↓
Step 6: 生成输出（HTML、JSON、Obsidian）
  ↓
Step 7: 可选导出（Neo4j、SVG、GraphML）
`

#### 输出文件
构建完成后，`graphify-out/` 目录包含：

|文件/目录|说明|
|-|-|
|`graph.json`|持久化的知识图谱数据（核心文件）|
|`GRAPH_REPORT.md`|完整的分析报告|
|`graph.html`|交互式可视化图谱|
|`obsidian/`|Obsidian 兼容的知识库|
|`cost.json`|Token 使用统计|

---

### 理解输出结果
#### GRAPH_REPORT.md 结构
`# Graph Report

## 统计信息
- 节点数: X
- 边数: Y
- 社区数: Z

## God Nodes (核心节点)
# 影响力最大的节点

## Surprising Connections (意外连接)
# 跨社区的有趣连接

## Suggested Questions (建议问题)
# 可以询问图谱的问题

## Communities (社区详情)
# 每个社区的节点和内聚度评分
`

#### 核心概念
* **节点（Node）**: 代码实体（函数、类、模块）或概念
* **边（Edge）**: 节点间的关系
    * `calls`: 函数调用
    * `implements`: 接口实现
    * `references`: 引用关系
    * `conceptually_related_to`: 概念关联

* **置信度（Confidence）**:
    * `EXTRACTED`: 源码中明确存在的关系
    * `INFERRED`: 推断的关系
    * `AMBIGUOUS`: 不确定，需要人工审查

* **社区（Community）**: 通过聚类发现的紧密关联的节点组

---

### 增量更新
当代码变更后，使用增量更新只处理变化的文件：

`# 增量更新（只处理新/修改的文件）
/graphify . --update

# 重新聚类（不重新提取）
/graphify . --cluster-only
`

#### 增量更新的优势
* **节省成本**: 只对新文件使用 LLM 进行语义提取
* **更快速度**: 跳过未变更文件的提取过程
* **保留历史**: 之前的图谱结构不会被破坏

#### 工作原理
1. 对比当前文件状态与上次运行时的 manifest
2. 识别新增或修改的文件
3. 只对这些文件执行提取
4. 合并到现有图谱中
5. 重新计算聚类和社区

---

### 自动监听更新
#### 使用 --watch 模式
`# 在后台启动监听
python3 -m graphify.watch . --debounce 3

# 或使用 nohup 在后台运行
nohup python3 -m graphify.watch . --debounce 3 > graphify-watch.log 2>&1 &
`

#### Watch 模式行为
|变更类型|行为|
|-|-|
|代码文件 (.go, .py, .ts, etc.)|自动重建图谱（无需 LLM）|
|文档/图片|标记需要更新，需手动运行 `/graphify --update`|
|文件删除|从图谱中移除相关节点|

#### Debounce 参数
`--debounce 3` 表示等待 3 秒无新变更后再触发重建，避免频繁重建。

#### 停止监听
`# 查找并停止 watch 进程
ps aux | grep "graphify.watch"
kill <PID>
`

---

### 查询知识图谱
#### 模式选择
|模式|标志|适用场景|
|-|-|-|
|BFS（广度优先）|默认|"X 连接到什么？" - 广泛上下文|
|DFS（深度优先）|`--dfs`|"X 如何到达 Y？" - 追踪特定路径|

#### 查询命令示例
`# BFS 查询 - X 连接到什么？
/graphify query "ProductHandler 如何连接到数据库？"

# DFS 查询 - 追踪路径
/graphify query "从用户请求到数据库写入的完整流程" --dfs

# 限制 token 预算
/graphify query "机器状态管理" --budget 3000

# 查找最短路径
/graphify path "HTTP请求" "数据库"

# 解释单个节点
/graphify explain "ProductDao"
`

#### 在 Ducc 中查询
由于 `/graphify` 是 Ducc 的 skill，你可以直接在 Ducc 对话中：

`用户：帮我分析一下机器状态管理的代码结构
Ducc：我来查询知识图谱...
[执行 /graphify query]
`



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3b75d4c0e7064683a656d2e31a589c7d&docGuid=Y2815b4ElrG459 "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=69ffa03446224117a3fbd6a543563c30&docGuid=Y2815b4ElrG459 "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=833fb966811940eba5b378681b2abdf2&docGuid=Y2815b4ElrG459 "")


---

## 集成到开发工作流
### 方案一：Git Hook 自动更新
`# 安装 post-commit hook
graphify hook install

# 之后每次 commit 后自动重建图谱
git commit -m "feat: add new feature"
# → hook 自动执行增量更新
`

### 方案二：CI/CD 集成
在 CI 流水线中构建和更新知识图谱：

`# .gitlab-ci.yml 或类似文件
stages:
  - build-graph

build-knowledge-graph:
  stage: build-graph
  script:
    - pip install graphifyy -q
    - /graphify . --mode deep
    - cp -r graphify-out/ artifacts/
  artifacts:
    paths:
      - graphify-out/
    expire_in: 1 week
`

### 方案三：Claude Code Hooks 集成
使用 Claude Code 的 `postToolUse` hooks 在代码编辑后自动触发更新。

#### 配置方式
编辑 `~/.claude/settings.json`：

`{
  "permissions": {
    "allow": [
      "Bash(go test:*)",
      "Bash(go build:*)",
      "Bash(*graphify*)"
    ]
  },
  "hooks": {
    "postToolUse": [
      {
        "pattern": "Edit.*\\.(go|py|ts|js)$",
        "command": "bash -c 'if [ -f graphify-out/graph.json ]; then touch graphify-out/.needs_update; fi'",
        "description": "代码编辑后标记需要更新图谱"
      }
    ]
  }
}
`

#### Hook 参数说明
|参数|说明|
|-|-|
|`pattern`|正则表达式，匹配工具调用时触发|
|`command`|要执行的命令|
|`description`|钩子描述（用于日志）|
|`debounce`|（可选）防抖时间（秒），避免频繁触发|

#### 推荐的轻量级方案
由于 graphify 更新需要一定时间，推荐使用**标记 + 延迟更新**的方式：

1. **Hook 只做轻量级标记**：

`{
  "hooks": {
    "postToolUse": [
      {
        "pattern": "Edit.*\\.(go|py|ts|js)$",
        "command": "touch graphify-out/.needs_update",
        "description": "标记需要更新图谱"
      }
    ]
  }
}
`

2. **使用 Ducc 定时任务检查并更新**：

`# 在 Ducc 中设置 Cron 任务
/graphify . --update --no-viz
`

#### 各方案对比
|方案|触发时机|优点|缺点|
|-|-|-|-|
|**Git Hook**|`git commit` 后|可靠，与提交流程绑定|只在提交时更新|
|**Claude Code Hooks**|Edit 工具后|即时响应，开发时实时|可能频繁触发|
|**--watch 模式**|文件系统变更|自动化程度高，免费（代码）|需要后台进程|
|**手动 + Cron**|定时/手动|灵活可控|需要主动触发|

#### 最佳实践组合
推荐**组合使用**多种方案：

`# 1. 初始化：使用 graphify 自带 git hook
graphify hook install

# 2. 开发时：使用 watch 模式（后台运行）
nohup python3 -m graphify.watch . --debounce 5 > .graphify-watch.log 2>&1 &

# 3. Claude Code hooks：标记需要更新
# 在 ~/.claude/settings.json 中配置轻量级标记

# 4. 定期：CI/CD 中构建完整图谱
`

### 方案四：Ducc 工作流集成
在 Ducc 的配置中启用知识图谱：

`// ~/.claude/settings.json
{
  "skills": {
    "graphify": {
      "autoUpdate": true,
      "watchMode": true,
      "graphPath": "/path/to/project/graphify-out/graph.json"
    }
  }
}
`

### 推荐工作流
`1. 项目初始化时
   → 运行 /graphify . 构建初始图谱
   → 安装 git hook: graphify hook install

2. 日常开发时（三选一或组合）
   → 方案A: 使用 --watch 模式自动监听（推荐）
   → 方案B: 配置 Claude Code hooks 标记更新
   → 方案C: 依赖 git commit 触发更新

3. 需要理解代码时
   → 使用 /graphify query 查询图谱
   → 查看 graph.html 可视化

4. 重大重构后
   → 运行 /graphify . --mode deep 重建
`

---

## 使用 Graphify vs 不使用的区别
### 对比表格
|维度|不使用 Graphify|使用 Graphify|
|-|-|-|
|**代码理解**|逐文件阅读，难以建立全局视图|一张图谱展示全貌，快速定位|
|**依赖分析**|手动追踪 import，易遗漏|自动提取所有依赖关系|
|**跨文件关系**|需要记忆或手动记录|持久化存储，随时查询|
|**新人上手**|需要大量时间熟悉架构|通过图谱快速了解模块关系|
|**重构影响**|难以评估修改的影响范围|通过图谱直观看到影响链路|
|**代码搜索**|基于文件名或字符串|基于语义关系，更智能|
|**上下文保持**|跨会话丢失|持久化 JSON，永久保留|
|**自动化程度**|依赖人工|自动提取、更新、分析|

### 详细对比
#### 1. 代码理解效率
**不使用 Graphify**:

`阅读 main.go → 发现调用 handler → 找到 handler 文件
→ 阅读 handler → 调用 domain → 找到 domain
→ 阅读 domain → 调用 dao → 找到 dao
→ ... 耗时约 30 分钟
`

**使用 Graphify**:

`执行 /graphify query "用户请求处理流程"
→ 立即获得完整调用链
→ 高亮关键节点和边
→ 耗时约 30 秒
`

#### 2. 影响分析
**不使用 Graphify**:

* 需要 grep 搜索所有引用
* 可能遗漏间接依赖
* 难以评估跨模块影响

**使用 Graphify**:

* 查询节点的所有邻居
* 可视化显示影响范围
* 自动识别受影响的社区

#### 3. 新人上手
**不使用 Graphify**:

`新人需要：
1. 阅读 README 和架构文档
2. 逐个浏览主要目录
3. 运行代码理解行为
4. 询问团队成员
→ 估计需要 1-2 周熟悉
`

**使用 Graphify**:

`新人可以：
1. 查看 graph.html 可视化
2. 运行 /graphify explain 理解核心模块
3. 查看 GRAPH_REPORT.md 中的社区分析
4. 使用 suggested questions 探索
→ 估计 2-3 天就能上手
`

#### 4. 上下文持久化
**不使用 Graphify**:

* 每个 Ducc 会话都是独立的
* 需要重新解释项目背景
* 之前发现的关系容易遗忘

**使用 Graphify**:

* graph.json 持久化存储所有关系
* 跨会话保持上下文
* 可以持续积累知识

---

## 最佳实践
### 1. 选择合适的模式
`# 日常开发：快速模式
/graphify .

# 深度分析：深度模式
/graphify . --mode deep

# 大型项目：分模块处理
/graphify ./internal/handler
/graphify ./internal/domain
`

### 2. 定期重建
对于长期维护的项目，建议：

* 每月运行一次 `--mode deep` 重建
* 日常使用 `--update` 或 `--watch`

### 3. 社区标注
Graphify 会自动生成社区标签，但你也可以自定义：

`# 在 .graphify_labels.json 中编辑社区标签
{
  "0": "用户认证模块",
  "1": "产品管理",
  "2": "机器调度"
}
`

### 4. 与 Obsidian 集成
`# 生成 Obsidian vault
/graphify . --html

# 在 Obsidian 中打开 graphify-out/obsidian/ 作为 vault
# 可以享受：
# - 双向链接
# - Graph View 可视化
# - 丰富的插件生态
`

### 5. Neo4j 集成（高级）
`# 导出 Neo4j Cypher 脚本
/graphify . --neo4j

# 或直接推送到 Neo4j
/graphify . --neo4j-push bolt://localhost:7687

# 在 Neo4j 中使用 Cypher 查询
MATCH (n)-[r]->(m) RETURN n, r, m LIMIT 100
`

---

## 常见问题
### Q1: Graphify 支持哪些编程语言？
**A:** 支持所有语言，但代码的 AST（抽象语法树）提取只对以下语言有特殊优化：

* Python
* JavaScript/TypeScript
* Go
* Java
* C/C++
* Rust

其他语言的代码仍然可以通过语义提取（LLM）来分析。

### Q2: 增量更新会丢失之前的信息吗？
**A:** 不会。增量更新会：

1. 保留现有图谱的所有节点和边
2. 只更新变更文件的相关部分
3. 重新计算聚类，但不会删除未变更的关系

### Q3: 知识图谱文件可以提交到 Git 吗？
**A:** 建议：

* `graph.json` - **可以提交**，是可读的 JSON
* `GRAPH_REPORT.md` - **可以提交**，有用的文档
* `graph.html` - **不建议提交**，文件较大
* `obsidian/` - **可选提交**，取决于团队是否使用 Obsidian

在 `.gitignore` 中添加：

`graphify-out/graph.html
graphify-out/obsidian/
`

### Q4: Watch 模式会消耗大量资源吗？
**A:** 不会。Watch 模式：

* 使用文件系统监听（inotify），CPU 占用极低
* 代码变更使用 AST 提取，不调用 LLM，免费快速
* 只在文档/图片变更时标记需要更新

### Q5: 如何处理敏感代码？
**A:** Graphify 支持跳过敏感文件：

`# 在 .gitignore 中列出敏感文件
secrets/
*.key
`

或者使用环境变量控制：

`export GRAPHIIFY_SKIP_PATTERNS="secrets/,*.key"
/graphify .
`

### Q6: 知识图谱可以用于其他项目吗？
**A:** 可以！Graphify 不限于代码仓库，也适用于：

* 文档集合（论文、技术文档）
* 笔记库（Markdown、Notion 导出）
* 混合内容（代码 + 文档 + 图片）

### Q7: Token 成本如何控制？
**A:** 优化建议：

1. 使用 `--update` 而非完全重建
2. 代码文件使用 AST 提取（免费）
3. 设置 `--budget` 限制查询的 token 使用
4. 查看 `cost.json` 了解历史消耗

---

## 附录：命令速查表
`# === 构建命令 ===
/graphify .                          # 基础构建
/graphify . --mode deep              # 深度模式
/graphify . --update                 # 增量更新
/graphify . --cluster-only           # 仅重新聚类
/graphify . --no-viz                 # 跳过可视化
/graphify . --svg                    # 导出 SVG

# === 监听命令 ===
python3 -m graphify.watch .          # 监听当前目录
python3 -m graphify.watch . --debounce 5  # 自定义防抖时间

# === 查询命令 ===
/graphify query "问题"                # BFS 查询
/graphify query "问题" --dfs         # DFS 查询
/graphify query "问题" --budget 3000 # 限制 token
/graphify path "概念A" "概念B"        # 查找路径
/graphify explain "节点名"            # 解释节点

# === Git Hook ===
graphify hook install                # 安装 hook
graphify hook uninstall              # 卸载 hook
graphify hook status                 # 查看 hook 状态

# === Neo4j 集成 ===
/graphify . --neo4j                  # 导出 Cypher
/graphify . --neo4j-push bolt://localhost:7687  # 推送到 Neo4j

# === MCP 服务器 ===
/graphify . --mcp                    # 启动 MCP 服务器
`

---

## 总结
使用 **Graphify + Ducc** 构建代码知识图谱，可以带来以下核心价值：

1. **快速理解**: 新人快速上手项目，老员工快速理解不熟悉的模块
2. **影响分析**: 重构时清晰了解影响范围，降低风险
3. **持久化知识**: 项目知识不再依赖个人记忆，团队共享
4. **智能查询**: 基于语义关系而非文件名的智能搜索
5. **自动化更新**: 代码变更后图谱自动更新，保持同步

**开始使用**: 只需在项目根目录运行 `/graphify .`，即可开始你的知识图谱之旅！

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
