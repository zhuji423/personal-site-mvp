---
title: "克隆项目"
description: "自制LLM Wiki 和使用"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\自制LLM Wiki 和使用.md"
---
自制LLM Wiki 和使用

#### 🧑‍🏫 案例作者：[@杨桐](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：知识加工
#### 🔧 使用工具：Claude
#### 📒 案例概要：一个基于大语言模型（LLM）的个人知识库工具，受 Andrej Karpathy 的 LLM Wiki 启发。
LLM Wiki 让你将原始文档（运维手册、FAQ、事故报告、技术文档等）自动分析、结构
## 
## 背景
一个基于大语言模型（LLM）的个人知识库工具，受 [Andrej Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 启发。

LLM Wiki 让你将原始文档（运维手册、FAQ、事故报告、技术文档等）自动分析、结构化后生成 Markdown Wiki 页面，并支持自然语言查询和健康检查。



项目地址：[https://github.com/atom-yt/llm-wiki](https://github.com/atom-yt/llm-wiki)

## 核心特性
* **三层架构设计**：原始源材料（Raw Sources）→ LLM 生成的 Wiki → Schema 配置
* **智能摄入**：自动提取关键知识点，创建/更新 Wiki 页面
* **自然语言查询**：基于 Wiki 内容生成带引用的答案
* **健康检查**：检测孤立页面、内容矛盾、过时声明等问题
* **Web UI 界面**：可视化浏览和管理知识库
* **CLI 工具**：命令行操作，支持脚本化
* **支持多种 LLM**：兼容 OpenAI API 格式的服务



## DEMO
#### 知识上传&摄入
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bacd5ef644dd4e2b855a44e40f558d78&docGuid=TV4G4YvWOVOE2W "")




#### 结构化数据
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e15f05195f2f43ff8bc02c959496f32a&docGuid=TV4G4YvWOVOE2W "")


#### 知识查询
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0bd6486928114530b52caf7de1a1e866&docGuid=TV4G4YvWOVOE2W "")




## 安装
```
# 克隆项目
git clone https://github.com/atom-yt/llm-wiki.git
cd llm-wiki

# 安装后端
pip install -e .

# 安装前端（可选，用于 Web UI）
cd web
npm install
```
## 快速开始
### 1. 初始化 Wiki
```
llm-wiki init
```
这将创建 `wiki-data/` 目录结构：

```
wiki-data/
├── config.yaml    # LLM 配置文件
├── raw/           # 原始源文件
│   └── assets/    # 附件目录
├── wiki/          # LLM 生成的 Wiki 页面
│   ├── index.md   # 全局索引
│   └── log.md     # 操作日志
└── schema/        # Wiki 结构定义
    └── schema.md  # 页面类型与格式规范
```
### 2. 配置 LLM
编辑 `wiki-data/config.yaml` 或设置环境变量：

```
export LLM_WIKI_API_KEY="sk-your-api-key-here"
```
### 3. 摄入知识
```
# 添加源文件到 raw/ 目录
cp your-doc.md wiki-data/raw/

# 摄入
llm-wiki ingest wiki-data/raw/your-doc.md
```
### 4. 查询知识
```
llm-wiki query "如何处理这个问题？"
```
### 5. 启动 Web UI
```
llm-wiki serve
```
访问 `http://127.0.0.1:8000` 使用 Web 界面。

## CLI 命令
|命令|说明|
|-|-|
|`llm-wiki init [name]`|初始化 Wiki 目录|
|`llm-wiki ingest <file>`|摄入源文件|
|`llm-wiki query <question>`|查询知识库|
|`llm-wiki lint [--fix]`|健康检查|
|`llm-wiki serve`|启动 Web UI|

使用 `--root` 或 `-r` 指定自定义数据目录：

```
llm-wiki --root my-wiki ingest my-wiki/raw/doc.md
```
## Web UI 功能
* **Dashboard**：总览统计和最近操作日志
* **Wiki Browser**：按类型浏览所有 Wiki 页面
* **Ingest**：上传源文件并触发摄入操作
* **Query**：自然语言查询知识库
* **Health Check**：运行健康检查并修复问题

## Wiki 页面类型
|类型前缀|说明|
|-|-|
|`source-*`|原始文档摘要|
|`entity-*`|工具、服务、系统组件|
|`concept-*`|概念、模式、原则|
|`procedure-*`|操作步骤、排障流程|
|`incident-*`|事故记录、事后复盘|
|`query-*`|归档的查询答案|

## 适用场景
* **技术文档管理**：运维手册、API 文档、开发指南
* **事故分析**：故障复盘、根因分析
* **竞品分析**：产品对比、市场分析
* **研究笔记**：论文阅读、文献综述
* **个人知识库**：读书笔记、学习记录

## REST API
|方法|路径|说明|
|-|-|-|
|GET|`/api/pages`|列出所有 Wiki 页面|
|GET|`/api/pages/{name}`|获取单个页面内容|
|POST|`/api/ingest`|摄入源文件|
|POST|`/api/query`|查询知识库|
|POST|`/api/lint`|健康检查|

完整 API 文档请参考 [hack/docs/usage.md](hack/docs/usage.md)。

## 开发
```
# 后端开发
pip install -e .

# 前端开发
cd web
npm install
npm run dev

# 构建前端
npm run build
```
## 配置参考
完整的 `config.yaml` 选项：

```
llm:
  api_key: ""                              # LLM API 密钥
  base_url: "https://api.openai.com/v1"   # API 基础 URL
  model: "gpt-4o"                          # 模型名称

wiki:
  root: "."              # Wiki 根目录
  raw_dir: "raw"         # 原始文件目录
  wiki_dir: "wiki"       # Wiki 页面目录
  schema_dir: "schema"   # Schema 定义目录
```
## 许可证
MIT

# 0.2.0 - 语义搜索与交互式 Ingest
发布时间: 2026-04-08

---

## 新增功能
### 交互式 Ingest 工作流
* **分步审查**: 用户可以逐步审查 LLM 分析结果
    * 提取关键点阶段：可批准、拒绝或编辑关键点
    * 页面提案阶段：查看 create/update 操作，选择合并策略
    * 应用阶段：批准后批量应用更改

* **智能页面选择**: 使用 BM25 算法选择相关页面，而非按字母顺序
* **合并策略**: 支持四种页面合并策略
    * `append`: 在现有内容后追加，带来源标注
    * `prepend`: 在开头添加最新内容
    * `merge`: LLM 智能合并，保留两份信息
    * `replace`: 完全覆盖

* **来源追踪**: 自动在 front-matter 中记录 `sources` 字段

### 三层语义检索系统
```
优先级 1: QMD CLI 语义搜索（如果已安装）
  ↓ 不可用
优先级 2: SimpleEmbedder TF-IDF 嵌入（768 维向量）
  ↓ 无索引
优先级 3: BM25 关键词搜索
```
* **SimpleEmbedder**: 无需外部依赖的本地 TF-IDF 嵌入生成器
* **智能索引**: `llm-wiki index [--force]` 命令建立语义索引
* **自动回退**: QMD 不可用时自动降级到 SimpleEmbedder/BM25

### 增强的跨引用跟踪
* **链接图缓存**: `.link_graph.json` 持久化，避免 O(n²) 重复计算
* **孤立页面检测**: 自动发现无入站链接的页面
* **枢纽页面发现**: 找出站链接最多的页面
* **矛盾检测**: LLM 辅助检测页面间的矛盾并标记

### 双格式日志系统
* **Markdown 格式**: 人类可读的操作日志
* **JSON 格式**: 机器可解析的日志，带 `entry_id`
* **审计查询**: 支持按页面/ID 查询历史
* **统计信息**: 支持 `get_stats()` 获取统计

### Schema 管理工具
* **自动分析**: `llm-wiki schema --analyze` 自动分析 Wiki 结构
* **改进建议**: LLM 生成针对性的 Schema 改进建议

---

## 新增 CLI 命令
|命令|说明|
|-|-|
|`llm-wiki index [--force]`|建立语义搜索索引|
|`llm-wiki schema --analyze`|分析 Wiki 并建议改进|

---

## 新增 API 端点
|端点|方法|说明|
|-|-|-|
|`/api/ingest/start`|POST|开始交互式 ingest，提取关键点|
|`/api/ingest/propose`|POST|基于批准的关键点生成页面提案|
|`/api/ingest/apply`|POST|应用批准的页面更改|
|`/api/qmd/index`|POST|建立或更新语义索引|
|`/api/qmd/status`|GET|获取搜索模式状态|

---

## 前端新增
### 新增页面
* **交互式 Ingest** (`/ingest-interactive`): 5 步工作流 UI
    * 步骤进度条显示
    * 关键点审查（可点击选择/取消）
    * 用户反馈输入框
    * 页面提案审查（显示 diff，可批准/拒绝）
    * 合并策略选择下拉框
    * 应用进度提示


### 功能增强
* **查询页面**: 显示当前搜索模式和索引状态
    * QMD / SimpleEmbedder / BM25 模式标签
    * 已索引页面/总页面数统计
    * 一键重建索引按钮


---

## 性能优化
|项目|优化前|优化后|
|-|-|-|
|链接计算|O(n²) 每次|O(1) 查询 + O(log n) 更新|
|页面选择|随机顺序|BM25 相关性评分|
|搜索速度|仅 LLM|三层回退，QMD 最高效|

---

## 配置变更
无配置文件变更，所有新功能向后兼容。

---

## 升级说明
### 用户体验
* **推荐操作**: 运行 `llm-wiki index` 建立语义索引，提升搜索质量
* **Web UI**: 访问 `/ingest-interactive` 使用新的交互式 ingest 流程

### 兼容性
* **向后兼容**: 现有 Wiki 无需任何修改即可使用新功能
* **渐进增强**: 可选择性启用新功能，不影响现有工作流

---

## 已知限制
* **QMD CLI**: 需要额外安装 [qmd](https://github.com/qmd) 命令行工具才能使用最高级语义搜索
* **SimpleEmbedder**: 使用 TF-IDF，语义理解能力有限，但无需外部依赖

---

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
