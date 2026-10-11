---
title: "一、实践简介"
description: "使用zulu开发竞品评测展示页"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\使用zulu开发竞品评测展示页.md"
---
使用zulu开发竞品评测展示页

#### 🧑‍🏫 案例作者：[@郭耀阳](https://ku.baidu-int.com?t=mention&mt=contact&id=76ffd240-fce6-11f0-8d13-5521f5c787e8)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了借助zulu从0到1开发OCR竞品评测展示页的实践，通过自然语言描述需求，zulu自动化完成了数据存储结构设计、Flask前后端服务开发等任务。过程中积累了使用zulu的心得和踩坑经验，展示了AI在降低开发成本、提升效率方面的能力，为团队推广AI内化提供了参考。
# 一、实践简介
##### **1、背景**
为了保证本品OCR服务的业内领先性，视觉QA会季度级别周期性展开竞品评测。

然而，当前输出结论仅以知识库表格的形式展示，页面上全是数字，无法可视化地直观展示多个竞品在多个评测集上的横向对比结果。

因此需要额外开发一个竞品评测展示页，功能包括：常用的下拉框切换、柱状图对比、详情页数据、版本对比等。

##### **2、亮点**
借助zulu从0到1开发全栈需求，以“零代码”为目标，仅通过自然语言描述就能完成诸如数据存储结构设计、Flask前后端服务开发、编译调试等开发操作。

最终，全部核心功能均在zulu主导下自动化闭环完成，显著提升了研发效率并降低了重复性开发劳动。

过程中积累了一些使用zulu的心得和踩坑经验，在此分享给大家，希望能为团队后续推广AI内化提供有益参考。

# 二、关键词
zulu、从0到1、低代码、全栈、评测结果展示

# 三、具体实施
### 0、开发流程与结果展示
### **开发流程设计**
### **结果展示**
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 1、数据层开发
#### 数据库操作前置准备
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
本项目预期需要与数据库交互，进行表格创建、数据增删改查等操作，因此为了简化Prompt，预先配置MySQL MCP

#### 数据表结构设计
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
通过自然语言描述，将需求同步给zulu，让它帮忙设计表数据结构，同时将SQL语句提供出来。

这一步顺利完成，zulu能充分理解建表需求，给出恰当的多表协同存储方案，SQL review也没有问题。

#### DDL执行
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
得益于预先配置的MySQL MCP，zulu能够顺利链接数据库执行建表操作。

之后，zulu建议填充评测数据，设计并验证数据录入流程，采纳！

### 2、测试数据录入&Demo展示
#### 数据录入系统设计
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
zulu能够主动通过ORM简化数据库操作

#### 代码开发
![创建样本数据](/personal-site-mvp/img/doc-placeholder.svg "创建样本数据")
![有个路径不对的Bug](/personal-site-mvp/img/doc-placeholder.svg "有个路径不对的Bug")
#### 脚本执行
![不断修复bug并执行](/personal-site-mvp/img/doc-placeholder.svg "不断修复bug并执行")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![导出评测结果](/personal-site-mvp/img/doc-placeholder.svg "导出评测结果")
![结果图（乱码）](/personal-site-mvp/img/doc-placeholder.svg "结果图（乱码）")
zulu能够自动执行终端命令并校验执行日志结果，如果发生报错能够分析日志提出改进办法

1、zulu不会长期等待执行结果，如果日志很长，它会将校验工作交给人来处理

2、zulu执行部分命令需要人工确认，可以通过配置让其自动执行大部分非敏感操作（Deny List）

#### Bug修复
![修复乱码问题](/personal-site-mvp/img/doc-placeholder.svg "修复乱码问题")
![最终解决方案](/personal-site-mvp/img/doc-placeholder.svg "最终解决方案")
![改为英文实现](/personal-site-mvp/img/doc-placeholder.svg "改为英文实现")
![放置字体，修改需求](/personal-site-mvp/img/doc-placeholder.svg "放置字体，修改需求")
![Demo展示](/personal-site-mvp/img/doc-placeholder.svg "Demo展示")
### 3、真实数据录入
#### 初步设计与代码生成
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
**踩坑**：因为之前比较顺利，就同时给zulu安排了数据导入和前端设计工作，这是不可取的。应该控制任务的范围，一下子让它做多个任务，它在流程设计上会出问题，也会输出太多信息，不方便检查

#### 流程演示
![](/personal-site-mvp/img/doc-placeholder.svg "")
这里zulu初步完成了系统设计和代码编写，要求启动服务进行展示，但其实只是花架子，问题很多

#### Bu修复-未成功
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
**踩坑**：如[通用文字识别](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/t7n0qKWNJW/43yjc0xqVd/7c3dfcd7fb1e40?t=mention&mt=doc&dt=sheet)，需要导入的表格数据结构非常复杂，尽管已经在query中详细介绍了表格中每行每列的设计思路，zulu仍然只能以错误的方式导入。通过设计测试用例，zulu发现导入错误后会自动修改代码，这就陷入了不断修改重试的循环，持续1个小时仍未能解决问题。因此如果是过于复杂的长尾需求，仍建议人工编写脚本，也可以尝试通过提供信息类和指令类rules，引导zulu更高效的进行代码生成。

### 4、前端开发
因此，在前端代码生成之前提前配置了rules，避免再次陷入修改循环。

（虽然给zulu一次安排全部任务它无法可靠的完成，但对于从0到1的项目，它至少可以完成粗略的架构设计和base代码，这就能够通过rules自动生成简化编写成本）

```
---
description: OCR竞品评测平台的开发规范和最佳实践
globs:
alwaysApply: true
---

## **1. 项目概述与核心概念**

**项目描述:** 这是一个基于Flask的OCR竞品评测数据可视化平台，用于展示和比较不同OCR产品在各种测试场景下的效果指标。系统通过Web界面提供直观的图表和数据对比，帮助用户分析OCR产品的优劣。

**关键名词解释:**
- **竞品 (Competitor):** 参与评测的OCR产品提供商，如百度、阿里云、腾讯云等
- **测试场景 (Test Scenario):** 不同的OCR应用场景，如通用文字识别、手写体识别、证件识别
- **评测指标 (Evaluation Metric):** 衡量OCR性能的具体指标，如准确率、召回率、F-score等
- **评测集 (Evaluation Set):** 特定场景下的测试数据集，包含样本类型和数量信息
- **版本 (Version):** 评测数据的时间版本，如2025Q3、2025Q4

## **2. 关键代码定位与文件说明**

**核心目录/文件:**
- `ocr_eval/app.py` - **Flask应用主入口**，包含所有API路由和业务逻辑
- `ocr_eval/models.py` - **SQLAlchemy数据模型定义**，定义所有数据库表结构
- `ocr_eval/config.py` - **配置文件**，包含数据库连接信息和枚举类型定义
- `ocr_eval/importer/data_loader.py` - **数据导入工具**，支持从JSON文件批量导入数据
- `ocr_eval/importer/tongyong_excel_data_importer.py` - **Excel数据导入器**，专门处理评测数据Excel文件
- `ocr_eval/templates/comparison_platform.html` - **前端主页面模板**，包含所有UI和JavaScript逻辑
- `sql/create_ocr_evaluation_tables.sql` - **数据库初始化脚本**，创建所有必要的表结构

**重点关注:**
- 所有数据库操作必须通过 **SQLAlchemy ORM** 进行，禁止直接使用原生SQL
- 前端数据展示依赖 **Chart.js** 图表库，所有图表配置在 `comparison_platform.html` 中定义
- 数据导入功能集中在 **`data_loader.py`** 和 **`tongyong_excel_data_importer.py`** 中

## **3. 数据结构**

**数据库表数据结构**
1. competitors表为竞品类型，其name字段为竞品厂商名称，type字段为竞品场景名称，id为编号，description为描述
2. evaluation_metrics表为评测指标类型，其name字段为指标名称，type字段为指标大类，id为编号，description为描述，unit为单位，is_higher_better为是否高为优
3. evaluation_sets表为样本集类型，其name字段为样本集名称，sample_type字段为对应的评测场景类型，id为编号，scenario_id为对应test_scenarios表的评测场景类型，description为描述，sample_count为样本数量
4. test_scenarios表为评测场景类型，其name字段为评测场景类型名称，type字段为评测场景类型名称，id为编号，description为描述
5. evaluation_results表为评测结果数据，competitor_id为对应competitors表竞品类型，scenario_id为对应test_scenarios表评测场景类型，evaluation_set_id为对应evaluation_sets表样本集类型，metric_id为对应evaluation_metrics表评测指标类型，value为指标值，version为评测版本

## **4. 规范与注意事项**

**应该做 (Should):**
- **应该** 所有API端点返回统一的JSON格式：`{'success': boolean, 'data': any, 'message': string}`
- **应该** 数据库操作使用 `with app.app_context():` 包装，确保Flask应用上下文正确
- **应该** 前端改动应当参照数据库表数据结构进行改动，必要时需要参照mcp.json链接数据库查询
- **应该** 前端图表使用Chart.js配置，保持一致的视觉风格和交互行为
- **应该** 数据导入前进行验证，确保数据格式和完整性
- **应该** 使用SQLAlchemy的声明式基类定义数据模型，保持一致性

**不应该做 (Not):**
- **禁止** 在Controller中直接拼接SQL语句，必须使用SQLAlchemy ORM
- **不要** 在前端硬编码数据，所有动态数据应通过API获取
- **禁止** 忽略异常处理，所有数据库操作应有适当的错误处理
- **不要** 在模板中编写复杂的业务逻辑，应将逻辑放在后端
- **禁止** 在配置文件中暴露敏感信息，如数据库密码应通过环境变量管理

**前端开发规范:**
- 使用Bootstrap 5.x作为CSS框架
- Chart.js图表配置应保持响应式布局
- JavaScript代码应包含完整的错误处理
- 所有异步操作使用Promise和async/await

**数据模型规范:**
- 所有模型类继承自 `Base = declarative_base()`
- 表名使用复数形式，如 `competitors`, `test_scenarios`
- 外键关系使用 `relationship` 正确定义
- 时间戳字段使用 `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`
```
#### 前端代码开发
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
zulu在前端代码开发颇具优势，叠加rules的引导和约束，前端代码快速成型，期间出现的“切换下拉框数据加载失败”、“柱状图宽度问题”、“竞品取消勾选无效”等问题都顺利解决。

TODO：1、借助开源组件库优化页面样式；2、支持前端数据导入导出；3、支持多版本数据对比；4、优化缓存与性能；5、添加鉴权等

# 四、复盘
##### 1、模式：（好的经验）
* ***如何初始化****：从零到壹的项目，可以先提出宏观复杂的需求，让zulu帮忙进行架构设计，之后再分步骤一一实现*
* ***如何高效生成****：zulu虽然可以根据日志循环修复问题，但针对复杂场景，添加信息类和指令类rules，能够引导zulu更高效的进行代码生成*
* ***如何回退改动****：连续的代码修改后，zulu回退修改的代码比较麻烦，可以通过git等进行快速的代码缓存和回退，也可以让zulu每次复制文件进行修改*

##### 2、反模式（不要这么做）
* ***自动清理****：zulu修复bug时会频繁的新增测试脚本进行校验，如果让**zulu自动清理无效代码，会删掉很多重要脚本*
* ***盲目等待****：不要让zulu一直挣扎修复，持续三次没能修复就需要人工介入了，可以配置rules，也可以进一步优化提示词质量或者亲自上阵*

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
