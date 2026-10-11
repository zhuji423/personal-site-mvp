---
title: "1.引言"
description: "🌟电商产研AI Coding实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\🌟电商产研AI Coding实践.md"
---
🌟电商产研AI Coding实践

#### 🧑‍🏫 案例作者：[@文胜平](https://ku.baidu-int.com?t=mention&mt=contact&id=5f55cd40-fcee-11f0-a22f-7f37e5cf3d1e)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文总结了百度电商搜索产研团队利用AI编程工具（如Comate、Cursor）提升研发效率的实践经验。通过需求迭代六个阶段划分任务，结合具体案例展示了AI在临时简易任务、调研梳理任务及复杂项目中的应用效果，显著提升开发效率。同时，提出了AI编程的核心痛点与优化思路，强调上下文管理与进阶协作的重要性。
**本文档视频讲解：**[电商产研AI Coding实践](https://learn.baidu.com/dulearn/app-dulearn-page.html#/home/course-detail/56995?activityId=8747?t=mention&mt=doc&dt=sdk)

# 1.引言
随着大语言模型（LLM）技术的快速发展，AI 编程工具（如 Comate、Cursor、GitHub Copilot）已经从实验性工具演变为生产力革命的核心驱动力。 结合[Robin@10月总监会：内化AI能力，成为真正AI native的公司](https://news.family.baidu.com/newsDetail/225857?t=mention&mt=doc&dt=sdk)的总体方针， 对百度电商搜索产研团队的实践经验，系统性地总结 AI 编程在 产研日常开发场景下的实践。 



**从以下四个维度展开详细介绍：**

1. **产研日常工作**
2. **实践案例**
3. **实践总结**
4. **AI 编程核心痛点与优化思路**

# 2.产研日常工作
****

产研需求迭代流程，主要为以下的 **六个主要阶段** ，其中 **技术调研 + 开发阶段**** ** 两个阶段，合计时间占比通常为 **60% 左右** ； 对应阶段的应用场景相对明确，利用 AI 编程开展研发工作，具备较大的效率提升空间。

**需求阶段**

**技术调研阶段**

**开发阶段**

**测试阶段**

**发布阶段**

**监控阶段**

* 需求沟通、评审 
* 交互&UI评审
* 方案调研、编写
* 前后端方案对齐
* 代码开发
* 自测
* 联调
* CodeReview
* 部署测试
* 走查、问题修复
* 预发布验证
* 单台上线验证
* 全量上线验证
* 系统稳定性监控
* 线上业务监控





其中研发阶段的工作任务可初步划分为以下三类，具体信息如下：

|**任务类型**|**任务说明**|**双周任务频次 （单人）**|**任务耗时占比（粗略估算）**|
|-|-|-|-|
|临时简易任务|单任务耗时约 0.5 天・数据转换处理・数据查询分析|1-3 个|20%|
|正常迭代任务|单任务耗时约 1 周|1-2 个|70%|
|调研梳理任务|单任务耗时约 1 天|1 个|10%|



# 3. 实践案例
## 3.1 案例概述   -  以电商视频化项目整理
* **痛点**：
    * 临时性需求：临时性脚本处理，统计分析需求较多，影响正常项目进展；
    * 重复性基础工作：需要反复消耗人力跟进；
    * 跨技术栈能力要求高：平台类功能开发需要同时掌握前端（Vue）+ 后端（Go），人才储备不足；

* **思路**：根据具体应用场景，使用合适的技术选型，结合AI IDE 提升开发效率；
* **实践场景**：

|**应用场景**|**场景说明**|**实践案例**|**传统开发方式耗时**|**AI辅助开发耗时**|**开发效率提升**|**适用度**|
|-|-|-|-|-|-|-|
|临时简易任务| 数据转换处理SQL数据查询|案例1：Python数据处理脚本案例2：SQL数据统计|0.5天以内|30分钟左右|80%+|非常高|
|调研梳理任务|业务代码梳理技术框架梳理|案例3：eFlow框架总结|1-2天|0.5天|70%+|高|
|简单难度项目|单个系统模块，一种 开发语言|案例4：视频评论规模化生产|1-2天|0.5天|60%+|高|
|中等难度项目|包含多个系统模块，多种开发语言|案例5：视频内容平台审核功能|5天|2天|约 60%|中|
|||案例6：数字人直播间后台配置功能|5天|2天|约 60%|中|

实践案例涵盖多种开发语言，包括 Python、Go、TypeScript、Vue 以及 SQL 。

在实际工作场景中，多数研发人员通常能够熟练运用 2 - 3 种开发语言。而借助 AI 编程工具，研发人员不仅可以快速拓展自身技术栈，还能够迅速将新掌握的技术应用到实际研发项目中。 



### 3.1.1 **Demo 效果示例：**
通过案例 6 来 演示介绍，在相对复杂的场景中，AI 编程目前在实际业务中达成的效果；



**Tips**:  Comate对话链接：[https://console.cloud.baidu-int.com/comatestack/share/3695?token=3029ad4a](https://console.cloud.baidu-int.com/comatestack/share/3695?token=3029ad4a)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f95dcbac79e74b35af3311b857f8d6fa&docGuid=V-sP_1fw48uWB9 "")


**产品需求示例：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f324660d94fa488d8f67df2b90dc324e&docGuid=V-sP_1fw48uWB9 "")




**最终效果展示：**

![输入prompt ](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d32464de9c144b9b8c9ac5b3219b6b85&docGuid=V-sP_1fw48uWB9 "输入prompt ")
![step1: 技术方案说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=992ee1cc7d654486b3ef159ddcb708d7&docGuid=V-sP_1fw48uWB9 "step1: 技术方案说明")
![Step2 : 前端效果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e57ad320954b49e985a948d8bc957b01&docGuid=V-sP_1fw48uWB9 "Step2 : 前端效果")


**录屏Demo示例：**

[附件]
[附件]






## 3.2 实践案例详情
### 3.2.1 **案例1：Python数据处理脚本**
* **需求描述**：将每天的视频生产数据（万级别），按照指定表格要求，天级导出全量明细信息，通过邮件/如流发送给指定人员 ；( 限制约束：业务初期，暂无平台审核能力，且数据较多sugar无法一次性展现) 
* **效率**：**1- 2 小时 → 30分钟（约10分钟生成代码 + 20分钟测试）**
* **常见场景**：日常工具编写



**一个天级别任务全量明细任务导出脚本 audit_video.py**

**功能描述**

1. 从 MySQL 数据库提取视频数据
2. 解析复杂 JSON 字段
3. 生成 CSV 报表
4. 通过邮件发送报表

**传统开发流程**

**工作量拆解**:

* 数据库连接模块：10 分钟
* JSON 解析模块：10 分钟
* CSV 生成模块：10 分钟
* 邮件发送模块：10 分钟
* 集成测试：10 - 20 分钟

**总计**: 约 1-2 小时

**AI 辅助开发流程**

**Step 1**:  明确需求，SQL 连接 账号、密码信息

**Step 2**:  明确 读取 的数据表 ， 输出的文件格式

**Step 3**:  输出的 csv 表头定义

**Step 4:  **输出的字段赋值

**时间**: 约 20 分钟（含测试）

**AI生成优势总结：**

* 单个脚本基本1-2轮对话 即可使用，
* 整体编码时间基本在10分钟内完成
* 数据库、文件、网络、数据解析等固定操作流程效率非常高
* 自动添加异常处理和类型注解





### **input -> output**
#### **输入：**
**Prompt:**

```
参考文档 @audit.md  ，整体目标要求，使用 Python 任务输出至 @audit_video.py
1. 读取 MySQL 数据库
2. 获取 t_video 表中数据，处理数据最终输出至 CSV 文件中
3. CSV 表头定义：日期、编号、query、实体、实体类型、实体类目、分镜板块、分镜脚本、nid、数字人形象ID、百家号链接、原始视频链接
4. 字段格式
   日期=xx
   编号=xx
   实体=input_data.entity
   实体类目=input_data.category
   分镜板块=input_data.story_board_list[x].name
   分镜脚本=input_data.story_board_list[x].content
   数字人形象ID=output_data.video_combine_data.base_info.figure.vis_id
   nid=video_data.result.dispatch_bjh_nid
```


**说明：**audit.md 文件为输入内容明细，  图片内容为 audit.md 中 输入内容节选示例**；**

[附件]
![json 定义](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=382734d50fe84c1588748f6634893274&docGuid=5BHwcRow_9pXQl "json 定义")
![SQL 定义](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=49b5e516de73483a8df4fc460f9d8849&docGuid=5BHwcRow_9pXQl "SQL 定义")
![需要输出的 csv 格式内容定义](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9021d163175342cfafc15a5585e50434&docGuid=5BHwcRow_9pXQl "需要输出的 csv 格式内容定义")
#### **输出：**


**python脚本片段： csv表头定义、  json字段解析节选**

![CSV 表头定义](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dddaf9c04b254c6f9e9fdae23da32526&docGuid=5BHwcRow_9pXQl "CSV 表头定义")
![复杂json 数据解析](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a693394ffa424316a2095fe0b93d2477&docGuid=5BHwcRow_9pXQl "复杂json 数据解析")


**完整输出的代码脚本，约300行**

[附件]




### 




### 3.2.2 **案例2：SQL数据统计**
* **需求描述**：统计视频化生产各阶段成功的数据漏斗，包含  Query下发 - 视频脚本生产 - 数字人生产 - 素材处理 - 云剪辑 - 封面审核 -  百家号发布  多个阶段；
* **效果：****1-2小时 → 20分钟**



**多表关联查询汇总数据**

**功能描述**

功能包括：

1. 从三张数据库表中关联查询多个汇总数据信息， `t_task` 、`t_video`、 `ai_video_cover_audit_record` ，产出数据分析漏斗
2. 涉及三张表中 复杂的 聚合查询、子查询、关联查询功能

**传统开发流程**

**工作量拆解**:

1. 咨询业务同学，熟悉理解 `t_task`、`t_video`、

`ai_video_cover_audit_record` 三个表的结构和关联关系

2. 子查询 /  UNION  / Left JOIN 等 相对复杂语句语法 查询，处理字段对齐问题
3. 调试日期分组和聚合逻辑
4. 优化查询性能，考虑索引使用情况

**时间**: 约 1-2 小时

**AI 辅助开发流程**

**Step 1**: AI辅助，快速理解基本表结构定义，表关联关系

**Step 2**: 复制表定义到对话窗口

**Step 3**: 说明需要聚合产出的字段定义

**Step 4：**SQL验证 ， 微调

**时间**: 约 20 分钟

**AI生成总结：**

✅ 优势:

* **对于非专业数据分析师，可以快速生成复杂关联统计 SQL，**
* **降低子查询/关联查询/聚合查询 等语法糖的记忆难度，以及错误排查时间**
* 自动处理字段对齐和聚合逻辑
* 生成可读性好的字段别名和中文注释

⚠️ 注意事项:

* AI 生成的 SQL 需要在实际环境验证
* 性能优化需要结合数据量和索引情况（特别是 `create_time` 字段的索引）





###### Step1: SQL 表关联分析： 
**输入说明**：快速了解指定的数据库表详细定义 以及 关联关系

**输出说明**：包含指定表的关联关系， 核心状态字段解释，ER图可视化分析；

### **input -> output**
#### **输入：**
**Prompt:**

```
# 角色：数据分析师

# 分析数据库表，产出 数据库ER关系图，表关联关系，输出至  sql.md

# SQL表定义 

t_task ： xxx

t_video ： xxx

ai_video_cover_audit_record: xxx
```


















#### **输出：**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9f6c2d3c798c4c5cb1ab5bddacaca2bb&docGuid=5BHwcRow_9pXQl "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b3fc4b5a8f1149038f8a741a8309cbbc&docGuid=5BHwcRow_9pXQl "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=be358f88603e403fbe8d220872ee0f6e&docGuid=5BHwcRow_9pXQl "")




###### Step2: SQL 生成：
* **输入说明**：根据第一轮对话的产出文档，梳理核心需要 关键指标定义，人工校验整理prompt
* **输出验证**：由于数据安全/隔离等问题， 最终生成的查询SQL， 需要自行通过 mysql 命令行/客户端 查询工具验证；

### **input -> output**
#### **输入：**
**Prompt : **

```
#角色：你是一个资深数据分析师
#任务：分析以下数据表，产出统计分析SQL语句 
#输入：
1.sql 模型定义 :  xxx 表内容
2，统计指标
Query下发总数: `t_task` 表每日创建的任务数
视频任务总数: `t_video` 表每日去重的视频ID数量
慧播星-成功: `status = 3` 的视频数量
素材处理-成功: `ecom_status > 4` 的视频数量
云剪辑-成功: `ecom_status = 8` 的视频数量
封面审核-通过: `ai_video_cover_audit_record` 表中 `status = 2` 的记录数
百家号发布-成功: `publish_status = 2` 的视频数量

3. 关联关系： t_video.video_id = ai_video_cover_audit_record.video_id
```


















#### **输出：**
**SQL ：**

```

SELECT
    stat_date AS "日期",
    SUM(task_total) AS "Query下发总数",
    SUM(video_total) AS "视频任务总数",
    SUM(hbx_success) AS "慧播星-成功",
    SUM(material_success) AS "素材处理-成功",
    SUM(cloud_edit_success) AS "云剪辑-成功",
    SUM(audit_passed) AS "封面审核-通过",
    SUM(publish_success) AS "百家号发布-成功"
FROM
    (
        -- t_task 按日期统计
        SELECT
            DATE(create_time) AS stat_date,
            COUNT(*) AS task_total,
            0 AS video_total,
            0 AS hbx_success,
            0 AS material_success,
            0 AS cloud_edit_success,
            0 AS audit_passed,
            0 AS publish_success
        FROM
            t_task
        WHERE
             {create_time [conditions.dateTimeRange]}
        GROUP BY
            DATE(create_time)
        
        UNION ALL
        
        -- t_video 按日期统计
        SELECT
            DATE(v.create_time) AS stat_date,
            0 AS task_total,
            COUNT(DISTINCT v.video_id) AS video_total,
            COUNT(CASE WHEN v.status = 3 THEN 1 END) AS hbx_success,
            COUNT(CASE WHEN v.ecom_status > 4 THEN 1 END) AS material_success,
            COUNT(CASE WHEN v.ecom_status = 8 THEN 1 END) AS cloud_edit_success,
            COUNT(CASE WHEN a.status = 2 THEN 1 END) AS audit_passed,
            COUNT(CASE WHEN v.publish_status = 2 THEN 1 END) AS publish_success
        FROM
            t_video v
            LEFT JOIN ai_video_cover_audit_record a ON v.video_id = a.video_id
        WHERE
             {v.create_time [conditions.dateTimeRange]}
        GROUP BY
            DATE(v.create_time)
    ) combined_stat
GROUP BY
    stat_date
ORDER BY
    stat_date DESC -- 按日期降序排列
```


**效果验证：**

[https://sugar.baidu-int.com/group/shop/report/r_1013e-8io7hz53-o8znq3?](https://sugar.baidu-int.com/group/shop/report/r_1013e-8io7hz53-o8znq3?)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=59b5d301ae7b453cbe024bcfe7fdb224&docGuid=5BHwcRow_9pXQl "")














### 3.2.3 **案例3：eFlow框架总结**
* **需求描述：** 对 eflow 工作流框架 进行系统分析，产出技术文档总结，进行 内部框架分享与推广介绍 ； -- 包含 8 个代码仓库；
* **效率：****1-2天 → 0.5天**
* **常见场景**：代码转换为文档沉淀、接收新业务快速熟悉
* **AI编程环境**：Cursor + Claude 4.5 sonnet； （cursor当前对于多代码仓库的工作区分析能力较好）



**任务：eflow框架总结**

**功能描述**

1. 将现有代码 与 设计文档整合，优化项目文档总结
2. 各模块功能定位清晰，输出内容通俗易懂
3. 图文并茂的输出，易于是其他阅读者快速理解

**传统总结流程**

**工作量拆解**:

1. **需求拆解**：明确架构分析维度，包括模块职责、技术实现路径、业务流程映射、系统集成场景
2. **文档精读**：查阅 eFlow 官方设计文档，梳理系统定位、整体技术栈（Go 语言、分布式架构等）
3. **代码阅读**：逐个分析`operator`、`scheduler`、`remote-worker`等模块源码，记录模块间接口定义与通信机制
4. **设计图绘制**：基于 Mermaid 语法 或 其他流程图工具，手动编写模块依赖图、工作流时序图，确保与代码逻辑一致
5. **代码示例注释**：挑选核心功能代码（如任务调度逻辑、SDK 调用流程），人工添加技术选型与业务场景说明
6. **多源校验：**对比文档、代码、设计图的一致性，优化架构表述的专业性与可读性

**时间：约 1-2 天**

**AI 辅助总结流程**

**Step 1: 需求定义**：向 AI 明确 “eFlow 分布式工作流引擎架构分析，采用 TOT 四分支方法，输出模块化架构大纲、Mermaid 设计图、关键代码解析”

**Step 2: 素材投喂**：上传代码仓库结构（`folders` JSON）、官方设计文档链接，让 AI 快速获取架构上下文

**Step 3:** **架构生成**：要求 AI 输出分层架构说明，包含各模块（如`operator-service` `go-sdk`）的职责边界与技术实现

**Step 4: 设计图生成**：让 AI 基于 Mermaid 语法生成模块依赖图、工作流执行流程图初稿

**Step 5**:** 代码解析**：将核心代码片段输入 AI，生成带技术注释的逻辑说明（如分布式调度的并发控制）

**Step 6**: **人工精校**：对 AI 生成的架构细节、代码注释进行业务场景验证，补充复杂流程的人工经验（如异常重试机制）

**时间：约 0.5天**

### AI 生成总结
**✅ 优势：**

* 快速输出**架构全景框架**，覆盖模块、技术、业务、集成维度，减少人工梳理时间 ，** 基本能达到 60分左右水准**
* 自动化生成**Mermaid 设计图**（如模块依赖图、工作流时序图），降低绘图门槛
* 代码示例**注释专业性强**，能解析技术选型逻辑（如 Go 语言在分布式工作流中的性能优势）
* TOT 方式**结构化呈现**，让架构分析逻辑更清晰

**⚠️ 注意事项**：

* AI 生成的**分布式架构细节**（如节点容错、数据一致性方案）需结合生产环境实际配置验证
* 复杂业务场景的**工作流分支逻辑**（如审批流的多节点跳转），需人工介入校准以匹配真实业务规则
* 生成的**代码示例**需本地编译运行，确认依赖管理、逻辑正确性（如`remote-worker`的通信协议兼容性）
* 对于 “go-sdk” 与业务系统的**集成场景**，需补充人工经验说明（如自定义扩展点的实现规范）





### **input -> output**
#### **输入：**
**工作区定义： **将代码仓库使用工作区模式打开，便于代码索引

[附件]
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=21d42475fcf544058eca1d55925bb28d&docGuid=5BHwcRow_9pXQl "")




**Prompt:**

```
# 角色
你是一个Go资深架构师，熟悉 workflow 流程机制

#需求：
对当前工作空间内代码进行深度阅读源码，对相关内容进行总结  
{"folders":[{"name":"operator","path":"eflow/operator"},{"name":"operator-service","path":"eflow/operator-service"},{"name":"common","path":"eflow/common"},{"name":"go-sdk","path":"eflow/go-sdk"},{"name":"scheduler","path":"eflow/scheduler"},{"name":"remote-worker","path":"eflow/remote-worker"},{"name":"platform","path":"eflow/platform"},{"name":"docs","path":"eflow/docs"}]}

# 任务
1. 使用TOT方式 进行分析理解
2. 包含多种软件设计图，并给出关键代码示例

# 框架整体设计参考 
[eflow总体设计] https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/DYLToDytsxUpHi
```












#### **输出：**
[eFlow分布式工作流引擎架构](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/PvEMRMw2EjEibR?t=mention&mt=doc&dt=doc)

**整体框架大纲 - 快速理解复杂工程项目**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=eed9554e77ee496e93b3c8cefdafacfd&docGuid=5BHwcRow_9pXQl "")


[Mermaid-代码即图表的艺术](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/1WJH2s7Mv_/gCYbITl8oa0r5k?t=mention&mt=doc&dt=doc) ， 可快速生成多种软件设计图，提升框架可读性；

** 系统整体架构 - 框架图**

```
graph TB
    %% 用户接入层
    subgraph "用户接入层"
        WebUI[Web管理界面<br/>platform模块]
        RestAPI[REST API<br/>platform模块]
        SDKClient[Go SDK客户端<br/>go-sdk模块]
    end

    %% 核心服务层
    subgraph "核心服务层"
        Scheduler[调度引擎<br/>scheduler模块]
        RemoteWorker[远程工作器<br/>remote-worker模块]
        OperatorService[算子服务<br/>operator-service模块]
    end

    %% 算子执行层
    subgraph "算子执行层"
        OperatorFramework[算子框架<br/>operator模块]
        CustomOperators[自定义算子实现]
    end

    %% 基础设施层
    subgraph "基础设施层"
        CommonLib[公共组件库<br/>common模块]
        InterfaceLayer[接口定义层<br/>interface模块]
        Documentation[文档资料<br/>docs模块]
    end

    %% 外部依赖
    subgraph "外部存储与消息"
        Etcd[(etcd<br/>配置管理)]
        Redis[(Redis<br/>状态存储)]
        SNDB[(SNDB<br/>结果存储)]
        Pulsar[Pulsar<br/>消息队列]
        MySQL[(MySQL<br/>元数据存储)]
    end

    %% 数据流向
    WebUI --> Scheduler
    RestAPI --> Scheduler
    SDKClient --> RemoteWorker
    Scheduler --> RemoteWorker
    Scheduler --> OperatorService
    RemoteWorker --> OperatorFramework
    OperatorService --> OperatorFramework
    OperatorFramework --> CustomOperators

    %% 基础设施依赖
    Scheduler --> CommonLib
    RemoteWorker --> CommonLib
    OperatorService --> CommonLib
    CommonLib --> InterfaceLayer

    %% 外部存储连接
    Scheduler --> Redis
    Scheduler --> SNDB
    Scheduler --> Pulsar
    SDKClient --> Etcd
    WebUI --> MySQL

    %% 样式定义
    classDef userLayer fill:#e3f2fd
    classDef coreLayer fill:#f3e5f5
    classDef operatorLayer fill:#e8f5e8
    classDef infraLayer fill:#fff3e0
    classDef storageLayer fill:#fce4ec

    class WebUI,RestAPI,SDKClient userLayer
    class Scheduler,RemoteWorker,OperatorService coreLayer
    class OperatorFramework,CustomOperators operatorLayer
    class CommonLib,InterfaceLayer,Documentation infraLayer
    class Etcd,Redis,SNDB,Pulsar,MySQL storageLayer
```
****

**eFlow核心组件交互流程图: 下图详细展示了一个完整工作流任务从提交到完成的全流程交互**

```
sequenceDiagram
    participant User as 用户
    participant Platform as Platform服务
    participant Scheduler as Scheduler调度器
    participant etcd as etcd配置中心
    participant Queue as 消息队列
    participant SDK as Go SDK
    participant Operator as 算子服务
    participant Redis as Redis状态存储
    participant SNDB as SNDB结果存储

    Note over User,SNDB: 1. 配置阶段
    User->>Platform: 配置工作流图
    Platform->>MySQL: 保存配置到数据库
    Platform->>etcd: 同步配置到etcd

    Note over User,SNDB: 2. 任务提交阶段
    User->>Scheduler: 提交工作流数据
    Scheduler->>Redis: 初始化任务状态
    Scheduler->>SNDB: 存储输入数据
    Scheduler->>Queue: 发送任务到消息队列

    Note over User,SNDB: 3. 分布式协调阶段
    SDK->>etcd: Leader选举
    SDK->>etcd: 监听配置变更
    SDK->>etcd: 获取任务分配

    Note over User,SNDB: 4. 任务执行阶段
    Queue->>SDK: 消费任务消息
    SDK->>Operator: 调用算子执行
    Operator->>SNDB: 获取输入数据
    Operator->>Operator: 执行业务逻辑
    Operator->>SNDB: 存储输出结果

    Note over User,SNDB: 5. 结果回调阶段
    SDK->>Queue: 发送执行结果
    Queue->>Scheduler: 调度器接收结果
    Scheduler->>Redis: 更新任务状态
    Scheduler->>etcd: 获取下游任务配置

    Note over User,SNDB: 6. 流程继续或结束
    alt 有下游任务
        Scheduler->>Queue: 触发下游任务
    else 流程结束
        Scheduler->>Redis: 标记流程完成
        Scheduler->>SNDB: 存储最终状态
    end
```


### 
### 3.2.4 **案例4：**视频评论规模化生成
* **需求描述**：产品提供 prompt 以及 视频脚本内容或 数据来源，研发规模化生成视频评论， 反馈给产品进行评估；   
* **问题**：
    * 大模型客户端（Deepsekk / ChatGPT ） 与业务中实际（千帆api） 可使用的 大模型不一样，效果存在差异； 
    * 产品调研时测试的 case较少，需要更多评估数据进行验证；
    * 大部分大模型客户端存在token使用限制，无法规模化使用；
    * 评论生成的Prompt 需要多轮优化，技术系统需要具有一定的配置化能力；

* **效率：****1-2天 → 0.5天**
* **常见场景**：功能调研
* **AI编程环境**：Comate + Claude opus 4.5



**输入prompt、 视频脚本 、 产出评论示例** 

![prompt](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=72281bb4601f4428935f274a4a515147&docGuid=5BHwcRow_9pXQl "prompt")
![输入视频脚本 + 大模型输出评论](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=19e3fddc8e264a209778083b0070769d&docGuid=5BHwcRow_9pXQl "输入视频脚本 + 大模型输出评论")


**AI 开发流程**

**简单评论生成能力：批量产出AIGC评论，导出excel表格给产品评估**

**功能描述**

1. 调研&熟悉 千帆SDK , 具体API 使用
2. 通用的大模型组件功能开发，SDK功能集成
3. Prompt 、 JSON 、CSV 等基础业务组件功能开发
4. 上述组件能力串联，脚本批量处理

**传统开发流程**

**工作量拆解**:

1. 方案调研，API 字段熟悉 ， 0.5天
2. 基础组件功能开发 ，  0.5 天
3. 业务功能开发 ，         0.5 天
4. 功能调试                    0.5天

**时间**:  1 - 2 天 （取决于功能封装/扩展 程度）

**AI 辅助开发流程**

**Step 1**:  集成接口调研，熟悉基础调用逻辑

**Step 2**: 人工编排任务流程步骤，完善prompt

**Step 3**:  输出技术方案，优化以及确认方案

**Step 4：**功能调试输出，验证

**时间**:  约 0.5天

**AI生成总结：**

✅ **优势**:

* 规范化的文档 / 字段理解能力
* 业务上下文关联不强的场景下，代码生成可用率非常高，2-3轮对话基本可完成相关功能
* 通用组件，如 SDK调用、网络、IO等标准化流程的处理
* 

⚠️ **注意事项**:

* AI 生成的 SQL 需要在实际环境验证
* 性能优化需要结合数据量和索引情况
* 嵌套 JSON 解析需要特别说明



**完成代码**：[评审：DS-sousuo2023-9192 调用大模型规模化生成评论功能](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/ejob-search/reviews/118984521/files/base...latest/shared/llm_client/README.md?t=mention&mt=doc&dt=sdk)





###### **Step1：基础大模型调用组件生成**


### **input -> output**
#### **输入：**
**Prompt: **

```
任务：在@shared创建一个 通用的llm 大模型调用公共组件

# 1. 千帆 python SDK说明
引入 https://cloud.baidu.com/doc/qianfan-docs/s/Fm9l6ocai 具体内容
xxx 网页具体内容 ，复制到对话框

# 2. 配置化管理
相关apikey , 模版等 使用配置化管理形式 

# 3. 保持整体功能的 复用性 和 拓展性 ，代码简洁 

# 4. 先编写技术方案计划，然后再进行代码编写

# 6. API接口请求示例
https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb
xxx,  网页具体内容 ，复制到对话框内容

```


输入的完整 prompt 内容，以及对话示例截图

会话详情 ：[https://console.cloud.baidu-int.com/comatestack/share/3512?token=30827d76](https://console.cloud.baidu-int.com/comatestack/share/3512?token=30827d76)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a2ededc417754448aedeb94e14c08b21&docGuid=byrTHGszdbZv1x "")


#### **输出：**
**技术方案 以及 编码完成总结**

![技术方案概述](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=644ae4a211054f59beb5e422e6a0713d&docGuid=byrTHGszdbZv1x "技术方案概述")
![实现效果总结](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=301e0c5779374ae2a497721edccb1c0c&docGuid=byrTHGszdbZv1x "实现效果总结")








**功能组件 以及 组件验证测试**

![功能组件说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0bc6e198948c42c88dc221ae3aa0eb23&docGuid=byrTHGszdbZv1x "功能组件说明")
![组件验证效果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=67660683d876435789c264a93b859f80&docGuid=byrTHGszdbZv1x "组件验证效果")










###### **Step2：业务功能组件生成**


### **input -> output**
#### **输入：**
**Prompt: **

```

# 任务
读取  #comment.csv   内容，然后调用  #client.py 大模型客户端，产出出评论 ， 整体先给出技术方案 ，然后再编写代码



# 需求说明
## 架构 
1. 保持内容拓展性，功能解耦 
2. 配置化管理能力
3. 一次性对话提交文章篇数可以配置

## 输入prompt 
1. 可配置化 
2. 具体prompt示例 内容：
prompt：
``` 
一：角色：你是一个资深 UGC 内容评论专家，阅读UGC内容产出针对特定内容的评论，评论风格需贴合抖音、小红书、b站、视频号生态的自然互动氛围，让人划到就想点赞，引起回复冲动。
二：任务
 1. 假设以下是一篇抖音视频脚本，请你根据每个视频作为一个普通抖音用户发表你的评论，每个视频生成3条评论
2. 字数弹性：评论字数的上限是50字，每篇视频下既有短评也有中长评；
 3. 表达克制：希望生成的评论语言风格上更加自然、真实、准确、多样，采用生活化口语，避免书面语句，尽量少使用感叹号
 4. 结构多元：希望生成的评论杜绝模板化，同一篇视频下的评论句式要不一致。
5、以下是通过脚本识别对应可参考的评论角度例子：
【参数对比】类脚本的评论参考：
17和16rpo推荐哪个？
冲了
纠结17还是16pro，平时拍视频和照片比较多
扬声器和马达也不一样么？
推荐换17嘛 平时就打游戏 刷视频 聊天什么的 有没有长焦无所谓
特别喜欢拍照，出去旅游啥的，打打王者刷视频。我有ccd和苹果xsmax了买16pro还是17基础啊
16pro有激光雷达 长焦 可变焦闪光灯 usb3速率 钛合金机身 第二代传感器位移防抖 proraw 录音棚级4麦克风阵列 这些17都没有 拍视频也不是只有一个长焦的差距 16p是4k120 17是4k60
【品类对比】类脚本的评论参考：
凤梨不用泡盐水，菠萝要泡盐水，是不是真的?
帮我看看这是菠萝还是凤梨
凤梨跟菠萝都是同一种水果，各地区叫法不同，凤梨是改良后的品种，实际上都是菠萝，难怪说凤梨跟菠萝吃起来连味道都一样，原来都是同一种水果
好像说最好的辨认方法是叶子有刺的是菠萝
我就说带刺的是菠萝 我姐家以前种过 给我整不会了
【品牌对比】类脚本的评论参考：
阿迪好看的都是三叶草，太贵了，耐克便宜的也有好看的，至少在我这一下就拉开了，足球鞋现在耐克的我个人穿的也更习惯
现在阿迪设计的衣服都太时尚了。
耐克营收居然比阿迪高这么多 不过也能理解 耐克的鞋都还不错 阿迪我感觉只有那个平底德训鞋的几个系列好看
Nike 从2010年买的第一双到现在 一直喜欢
阿迪这两年明显进步很大啊。反而耐克默默无闻
阿迪有点太复古了 有人觉得吗

 输出内容
1. 输出评论内容格式 ，严格按照json输出
{
 "query":"xx",
 "query":"标题",
 "comment": ["xx","xx","xx"]
}
``` 

## 后续，相关评论写回 评论列  @comment.csv 

```


**完整 prompt 内容连接，以及对话示例截图**

会话详情： [https://console.cloud.baidu-int.com/comatestack/share/353?token=2e3b4f53](https://console.cloud.baidu-int.com/comatestack/share/3513?token=2e3b4f53)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5ab58cb3628047ad81459fcfb0dadd8d&docGuid=byrTHGszdbZv1x "")
#### **输出：**
**技术方案 ：**

![技术方案概述](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=69090280f1234a25becebc797b44761f&docGuid=byrTHGszdbZv1x "技术方案概述")
![方案完成总结](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2f4df7b273514f9ea96bcc91fe53132e&docGuid=byrTHGszdbZv1x "方案完成总结")


**输出示例代码：**

![示例简易的配置能力](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cbb5af584f624105b09ee242ed15e13b&docGuid=byrTHGszdbZv1x "示例简易的配置能力")
![执行入口示例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=662530ffc00a470fb29ea59a604c7b0e&docGuid=byrTHGszdbZv1x "执行入口示例")


**任务脚本执行：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ca8d9f95a08544669891285221fce4ad&docGuid=byrTHGszdbZv1x "")


**产出的业务数据**：[评论内容测试](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/Yf_UfOc5hT/22a2230894184d?t=mention&mt=doc&dt=sheet)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=19e3fddc8e264a209778083b0070769d&docGuid=5BHwcRow_9pXQl "")


### 3.2.5 **案例5：**视频内容平台审核功能（前后端全栈开发） 
* **需求描述**：[商品购买视频化需求文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/hL9qmu1Vaz/OIng_xu57HN8Dk?t=mention&mt=doc&dt=doc) ， 基于现有ecbaseAI视频功能 ， 新增一个 spu_video 审核页面， 在现有平台基础上 ，包含列表页、审核任务创建、领取、审核内容 ，基础数据统计等能力；
* **问题：**
    * 按照常规流程，需要 前端+后端研发，需要相互对齐技术方案，协调排期等 ，拉长了整体开发工作量；
    * 需要开发 后端（Go技术栈） + 前端 (Vue技术栈)  ，同时会这两种语言 且 熟练开发的人员少； 

* **效率**：**5天 → 2天（方案设计 + 开发 + 联调）**
* **常见场景**：特定场景下，业务需求的功能迭代
* **AI编程环境**：Cursor + Claude 4.5 sonnet

|**阶段**|**传统方案**|**AI 开发方案**|**工作量拆解**|
|-|-|-|-|
|设计|1天|2小时|框架熟悉、原有逻辑熟悉、数据库字段定义、接口字段定义|
|后端开发|1.5天|0.5天|4个接口开发|
|前端开发|1.5天|0.5天|3个页面开发|
|联调|1天|0.5天|3个页面、4个接口联调|
|**总计**|**5天**|**2天**|**效率提升 60%**|

**前后端总对话轮次**: 11 轮 ， 完成本次 需求的** 90% 开发工作量**；

    * 规则生成：4 轮（前端 + 后端 Rules）
    * 方案设计 + 代码生成：3 轮
    * 代码验证 + 修复：4 轮（前端2轮 + 后端2轮）



##### 整体效果 
**线上地址**： [https://ecbase.baidu-int.com/aivideo/spu/list](https://ecbase.baidu-int.com/aivideo/spu/list)

**产品需求示例**：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2fa6968ebabf418d8621ac7463268df3&docGuid=t0Wg1AdIFUwIoJ "")


**前端页面：**

![审核列表页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7a5295d322ee4904909d7cbfb1dd6fe3&docGuid=5BHwcRow_9pXQl "审核列表页")
![审核详情页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d15f8e16dc5b4ec7b65a83579483db2f&docGuid=5BHwcRow_9pXQl "审核详情页")






##### AI 开发流程
[Rules 规则实践 - 平台功能开发](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/wTBI15BgnNqQ-N?t=mention&mt=doc&dt=doc)

审核功能：基于 GDP 应用的平台全栈功能开发（前端 + 后端）

**场景描述**

功能包括：

1. 开发 SPU 视频审核功能，包括：

* 后端：4个 RESTful API（列表、创建、领取、审核）
* 前端：2个页面（任务列表、视频列表、审核详情）
* 数据库：1 张表（ai_spu_video_audit）

**传统开发流程**

**工作量拆解**:

* 技术方案设计：1天
* 数据库设计：0.5天
* 后端开发：1.5天
* 前端开发：1.5天
* 联调测试：1天

**时长：约5天**

**AI 辅助开发流程**

* 规则生成：4 轮（前端 + 后端 Rules）（第一次需要）
* 方案设计 + 代码生成：3 轮
* 代码验证 + 修复：4 轮（前端2轮 + 后端2轮）
* 耗时：约1天 
* 其他：后端数据单独处理 1天

**总时长：约2天**

**AI生成总结：**

✅ **优势**:

* 全栈功能快速搭建，效率提升 60%
* 代码规范性好，符合团队 Rules
* 前端页面结构完整，可直接使用

⚠️ **挑战**:

* **需求描述要清晰**: 一次性描述不清楚，需要分模块迭代

1. **善用 Rules 规则**: 规则越完善，生成代码质量越高
2. **保持人工审查**: AI 是助手，最终决策权在人
3. **建立反馈循环**: 将常见问题补充到 Rules 中





###### **Step1: 规则生成 **  -  
一次整体生成，后续逐步迭代 ； 非每次必要；

### **input -> output**
#### **输入：**
**Prompt:**

**详细流程**:

**第1-4轮：生成 Rules 规则 & 规则优化 ;   ****默认生成规则可能存在功能缺失、代码冗余等问题，需人工review 完善**

```
深度阅读源码，创建rules, 
1. .cursor/rules/xxx.mdc   ，规则文件 后缀 .mdc
2. 按照  通用类规则(base)、语言类规则(language)、框架类规则(framework)、业务类规则(biz)  4类 规则 进行生成，
3. 生成4个文件夹，模块化的生成每类规则，保持核心规则的简练；
```


#### **输出：**
**规则：**

**前端规则：**[文件页：baidu/ps-shangpin/comate-rules  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/comate-rules/blob/master/cursor/rules/content-platform-tpl/README.mdc?t=mention&mt=doc&dt=sdk)



![前端规则列表](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=05a15d18c64741e5b7774813e9e12c95&docGuid=V-sP_1fw48uWB9 "前端规则列表")
![项目框架概览](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b4e3056a3a5f41129d9a21c1d8282da7&docGuid=V-sP_1fw48uWB9 "项目框架概览")
![具体创建API 任务调用代码示例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6cff29e1a5c3443cbee4832e174111ae&docGuid=V-sP_1fw48uWB9 "具体创建API 任务调用代码示例")


**后端规则：**[文件页：baidu/ps-shangpin/comate-rules  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/comate-rules/blob/master/cursor/rules/content-platform/README.md?t=mention&mt=doc&dt=sdk)

![后端规则列表](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc3ce18ba249425fae0d021fba4a31fb&docGuid=V-sP_1fw48uWB9 "后端规则列表")
![项目架构概览](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cd9b6150f87747c38e12b11459f29681&docGuid=V-sP_1fw48uWB9 "项目架构概览")
![具体调用 API 任务调用代码示例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0f91e44e2daf46f59799036b69feb4a5&docGuid=V-sP_1fw48uWB9 "具体调用 API 任务调用代码示例")








###### Step2: 技术方案编写
###### Step3: 业务代码编写&微调
### **input -> output**
#### **输入：**
**Prompt:**

**第5-7轮：生成技术方案并执行   **

[附件]
1. **需求分析**

```
根据需求说明 ，以及当前 @aivideo.mdc 业务框架 ，产出技术文档输出至  @plan.md  ，核心能力聚焦在 审核能力

# 产品需求说明
xxx 
```


2. **后端代码生成**

```
基于技术方案，生成后端代码：  @plan.md
```
3. **前端代码生成**

```
基于技术方案，生成前端代码： @plan.md
```
**第8-11轮：验证和修复**

* 后端联调测试，修复数据解析问题
* 前端样式调整，优化用户体验
* 权限控制逻辑补充
* 边界条件处理





**[aivideo.mdc]  为规则文件，通过上述rules生成；规则文件介绍**

[附件]
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b8ffbb7c77d342eebb3d4832850d4f3a&docGuid=t0Wg1AdIFUwIoJ "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0a749755ef5d41eeafbe488e82ca7963&docGuid=t0Wg1AdIFUwIoJ "")
#### **输出：**


**实现方案概览：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4eeb9bb2c0824962a6fd82dda43395eb&docGuid=5BHwcRow_9pXQl "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a4a2187d1d8747b6b80c6ff0ed9679f8&docGuid=5BHwcRow_9pXQl "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=af9e6d5cc7ae42a582a647da1de03793&docGuid=5BHwcRow_9pXQl "")


**前端**

**生成代码**：[评审：DS-sousuo2023-8678 spu_video 审核能力开发](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/content-platform-tpl/reviews/118529227?t=mention&mt=doc&dt=sdk) 



**后端**

[评审：DS-sousuo2023-8677 spu_video 审核能力开发](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/content-platform/reviews/118532729/files/base...latest?t=mention&mt=doc&dt=sdk)



**代码质量评估**:

* 后端功能可用度：70%（主要是业务逻辑复杂度）
* 前端功能可用度：90%+（页面结构和交互基本完善）

**实际产出**:

* 后端代码：约 800 行（4个API + 业务逻辑）
* 前端代码：约 1200 行（3个页面 + 组件）
* 几乎无手写代码（除了 MySQL 表定义）









### 3.2.6 **案例6：**数字人直播间后台配置功能（前后端全栈开发） 
* **需求描述**：[数字人直播-配置后台](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/y9DjkdFuHO/Ba5iUKB0cX/OWJX939iQCNUIe?t=mention&mt=doc&dt=doc) ， 基于现有shop-platform 的数字人直播间配置功能 ， 优化页面配置能力，在现有平台基础上 ，包含列表页、列表查询，单条数据的CRUD操作，批量数据导入能力 ，基础数据统计等能力； 
* **效率**：**5天 → 2天（方案设计 + 开发 + 联调）**
* **AI编程环境**：**Comate + Claude opus 4.5  ， 与 案例3.5.2 进行比较**

|**阶段**|**传统方案**|**AI 开发方案**|**工作量拆解**|
|-|-|-|-|
|设计|1天|2小时|框架熟悉、原有逻辑熟悉、数据库字段定义、接口字段定义|
|后端开发|1.5天|0.5天|RESTful 风格，SPU/品类直播间各6个接口（CRUD + 批量上传）|
|前端开发|1.5天|0.5天|页面路由、搜索表单、数据表格、新增弹窗、批量上传弹窗|
|联调|1天|0.5天|2个页面、6个接口联调|
|**总计**|**5天**|**2天**|**效率提升 60%**|





**基于Comate 进行开发整体效果总结：**在引入Claude / Gemini 等海外模型后，复杂业务场景下，代码可用率有明显提升，开发体验接近使用 Cursor ；

|**方案**|**Comate + Claude opus 4.5**|**Cursor + Claude 4.5 sonnet**|
|-|-|-|
|**技术方案完整度**|**使用工作区打开：一次性生成的前后端方案 部分可用，整体需拆分设计，前后端方案需单独优化****后端方案**：**基本可用， 但是存在方案冗余问题**** **， 没有考虑到 复用性 ， 需人工review 后 二次修改了方案；**前端方案**:  **不可用， 使用了 react技术栈进行生成 （代码库为vue技术栈）**** **，猜测是没有获取到 太多前端的上线文内容， 后续人工单独基于项目生成了对应方案；|**使用工作区打开： 一次性可基本完成前技术方案后端设计**|
|**大模型响应效率**|**响应非常快，稳定性高**|**响应速度一般，且请求连接容易断开**|
|**Rules总结**|**基本能描述清楚框架分层，业务功能； 描述相对简练；**|**能明确描述框架分层 ，业务功能，细节更加丰富 ，有汇总说明，但同时存在过渡冗余现象，导致 rules的内容过多；**|
|**CR**|前端：[评审：DS-sousuo2023-9178 数字人配置优化](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/shop-platform-tpl/reviews/118971667/files/base...latest?t=mention&mt=doc&dt=sdk)后端：[评审：DS-sousuo2023-9177 数字人配置优化](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/shop-platform/reviews/118971564/files/base...latest/.cursor/rules/biz/architecture.mdc?t=mention&mt=doc&dt=sdk)|**前端：**[评审：DS-sousuo2023-8678 spu_video 审核能力开发](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/content-platform-tpl/reviews/118529227?t=mention&mt=doc&dt=sdk) **后端：**[评审：DS-sousuo2023-8677 spu_video 审核能力开发](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/content-platform/reviews/118532729/files/base...latest?t=mention&mt=doc&dt=sdk)|
|**效果**|线上地址（待上线）：[https://mall.baidu-int.com/search/liveroom](https://mall.baidu-int.com/search/liveroom/room)测试地址：[http://wsp.bcc-szzj.baidu.com:8081/search/liveroom/spu](http://wsp.bcc-szzj.baidu.com:8081/search/liveroom/spu)![列表页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8edcd957d7b749cf8ad4c5f7a879d8e7&docGuid=l7sKsAdOkZ9Koq "列表页")![单条新增](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e5d09ada2c9544a0b7fcf1e553667e48&docGuid=l7sKsAdOkZ9Koq "单条新增")![批量导入](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc05221439764c9880f617e8dbf8a78c&docGuid=l7sKsAdOkZ9Koq "批量导入")|线上地址： [https://ecbase.baidu-int.com/aivideo/spu/list](https://ecbase.baidu-int.com/aivideo/spu/list)![审核列表页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7a5295d322ee4904909d7cbfb1dd6fe3&docGuid=5BHwcRow_9pXQl "审核列表页")![审核详情页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d15f8e16dc5b4ec7b65a83579483db2f&docGuid=5BHwcRow_9pXQl "审核详情页")|



###### Step1: 技术方案生成
不同大模型下生成的技术方案评估：**claude opus 4.5  >=   claude 4.5 sonnet  >   gemini 3 **

### **不同大模型生成技术方案对比**
** claude opus 4.5 **

**claude 4.5 sonnet **

**Gemini 3 pro **

**方案概述：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2d88cf0fc547434588cb9e850de5d2e1&docGuid=l7sKsAdOkZ9Koq "")
**对话详情链接：**

[https://console.cloud.baidu-int.com/comatestack/share/3500?token=3febcae7](https://console.cloud.baidu-int.com/comatestack/share/3500?token=3febcae7)

**方案概述：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2d9a5cfc841e4c94872ccea17b1a19d5&docGuid=l7sKsAdOkZ9Koq "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=24e6e806f3bc4e94a2cb6cd6316d8bb5&docGuid=l7sKsAdOkZ9Koq "")
**对话详情链接：**

****[https://console.cloud.baidu-int.com/comatestack/share/3498?token=583c42cb](https://console.cloud.baidu-int.com/comatestack/share/3498?token=583c42cb)

**方案概述：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=549cafdd14cb4396b6bf1e589c1c5f87&docGuid=l7sKsAdOkZ9Koq "")
**对话详情链接：**

****[https://console.cloud.baidu-int.com/comatestack/share/3499?token=b83c6e4b](https://console.cloud.baidu-int.com/comatestack/share/3499?token=b83c6e4b)

**技术方案选择：**

1. 使用方案：**基于claude opus 4.5**生成的技术方案 开发
2. 开发进度：当前 80% 功能开始时间 **约半天 ， **剩余部分主要为后端数据存储交互，需额外处理； 前端基本无需人工编写代码
3. 注意事项：  为提升代码生成准确率 ，每个代码库需单独使用comate打开



###### Step2:  业务代码编写
### **input -> output**
#### **输入：**
**Prompt:**

**第一轮会话：技术方案生成**

[https://console.cloud.baidu-int.com/comatestack/share/3500?token=3febcae7](https://console.cloud.baidu-int.com/comatestack/share/3500?token=3febcae7)

**技术方案设计**

```
# 角色： 技术架构师 - claude opus 4.5

# 前后端规范说明
     #README.mdc     #README.mdc  


# 任务 ： 产出前后端技术方案 ，输出至     #claude-opus-plan.md  

# 路由导航
参考 http://wsp.bcc-szzj.baidu.com:8081/search/page/liveCategoryConfig 
增加 
1. /search/page/liveSPU
2. /search/page/liveCategory

## Spu 直播间
SPU直播间
一、基础功能
1、支持查询字段和查询方式如下
    * 主播UID：输入，精准匹配
    
剩余部分 ... 复制对用模块内容


## 品类直播间
剩余部分 ...  复制 需求文档中对应模块文字内容
```


**第二轮会话：**

1. **后端代码生成 : **[https://console.cloud.baidu-int.com/comatestack/share/3516?token=97ca8593](https://console.cloud.baidu-int.com/comatestack/share/3516?token=97ca8593)

```
# claude-opus-plan.md  根据计划编写后端代码 
```


**第三轮会话：**

2. **前端代码生成: **[https://console.cloud.baidu-int.com/comatestack/share/3517?token=30e030d6](https://console.cloud.baidu-int.com/comatestack/share/3517?token=30e030d6)

```
# claude-opus-plan.md  根据计划编写前端代码 
```


#### **输出：**


**实现方案概览：**

![后端代码完成总结](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=efbec6b4e896454d89de77be7412eeb0&docGuid=byrTHGszdbZv1x "后端代码完成总结")
![前端代码完成总结说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6247d689621145ebb25350143b1cc5c0&docGuid=byrTHGszdbZv1x "前端代码完成总结说明")


**前端**

**生成代码**：[评审：DS-sousuo2023-9178 数字人配置优化](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/shop-platform-tpl/reviews/118971667/files/base...latest/src/composables/index.ts?t=mention&mt=doc&dt=sdk)



**后端：**[评审：DS-sousuo2023-9177 数字人配置优化](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/shop-platform/reviews/118971564/files/base...latest/model/dao/mdb/search/live_room.go?t=mention&mt=doc&dt=sdk)



**代码质量评估**:

* 后端功能可用度：60%+ （ 有多种数据交互判断处理，代码复用性需优化）
* 前端功能可用度：90%+ （页面结构和交互基本完善）







# 4.实践总结
## **4.1 概述**
AI 编程工具（Comate、Cursor、Claude Code）的核心使用逻辑：把 AI 当 “高潜力实习生”

AI 编程工具的本质 —— 它们不是 **“全能专家”**，而是 “**基础知识扎实、需要明确指引、能高效分担基础工作**” 的协作伙伴。结合后端 / 数据开发的实际场景，可以把这种使用逻辑落地为 “**明确边界、优化指令、借力提效**” 三大核心，让 AI 真正成为生产力放大器。

|**AI 的核心能力（对应 “实习生优势”）**|**AI 的能力边界（对应 “实习生局限”）**|
|-|-|
|1. 快速完成重复性基础工作（如 CRUD 接口、Shell 脚本、SQL 查询、Redis 操作封装）；2. 精准识别语法错误、逻辑漏洞（如 Go 代码的 nil 指针、SQL 的语法错误、MapReduce 的任务依赖问题）3. 提供多方案参考（如 “用 Go 实现限流有几种方式”）；4. 高效处理信息整理（如把官方文档转化为代码示例、总结日志中的错误规律）|1. 无法独立完成 “模糊需求”（如只说 “写个数据抓取服务”，AI 会生成通用模板，无法匹配你的业务场景）；2. 缺乏架构设计和决策能力（如 “微服务拆分”“大数据集群部署方案”，需你主导核心决策）；3. 生成的方案可能 “理论可行、实际有坑”（如 AI 推荐的 Redis 连接池参数不适合高并发场景、Shell 脚本未考虑权限问题）；4. 对 “业务强相关的定制化需求” 缺乏判断力（如 “根据公司数据模型设计分库分表方案”，需你提供业务规则）|

核心结论：**AI Coding 的价值在于 “分担” 而非 “替代”—— 把重复、低价值的基础工作交给它，你聚焦于需求拆解、架构设计、方案验证等核心决策**。**AI 的能力上限，取决于你的指令清晰度和决策判断力**。



## 4.2  简单需求： 精准的 Prompt 是关键 
**好的 Prompt 特征  符合**   **SMART 原则**:

* **S**pecific（具体）：明确说明要实现的功能
* **M**easurable（可衡量）：给出输入输出示例
* **A**chievable（可实现）：任务复杂度适中
* **R**elevant（相关）：提供上下文信息
* **T**ime-bound（有边界）：限定实现范围



### 大型语言模型（LLM）的精确输出控制
## Prompt Structuring (提示结构化)
通过精心设计提示的结构和组成部分（如角色扮演、明确指令、上下文信息、示例、输出引导语等），来系统地引导LLM的行为和输出。

```
# 角色
你是一位经验丰富的旅行规划师。

# 用户背景
用户计划进行为期7天的欧洲家庭旅行，有两个小孩 (5岁和8岁)，预算为5000美元，偏好自然风光和儿童友好活动。

# 任务
请为该用户提供一份包含三个不同国家选择的行程建议大纲。每个建议应包括：
1. 国家名称
2. 推荐停留城市 (2-3个)
3. 主要活动亮点 (3-5项，侧重儿童友好和自然)
4. 预估费用概要

请确保语气友好且信息实用。
```


## Output Format Control (输出格式控制) 
指定LLM输出文本的特定格式，例如JSON、XML、Markdown、CSV，或者自定义的结构化文本模式，将模型的自然语言能力转化为结构化的、机器可读的数据

```
Prompt: "请从以下产品描述中提取产品名称、价格和主要特性，并以JSON格式返回，包含键：product_name，price，features(特性列表)。描述：'新款智能手表，售价$199，支持心率监测、GPS定位和长达7天的电池续航。'"
期望输出

# json 示例 
{
  "product_name": "智能手表",
  "price": 199.00,
  "features": ["心率监测", "GPS定位", "长达7天的电池续航"]
}

```
#### **复杂数据提示例****：**
* **复杂数据提取与格式化**：
    * `Prompt Structure`: 定义角色（数据分析师），提供输入文本，明确指令提取特定信息。
    * `Output Format Control`: 要求输出为嵌套JSON结构。
    * `Response Constraints`: 限制日期格式为YYYY-MM-DD，数值字段必须为正数，特定字段（如`category`）的值必须来自预定义的枚举列表。

* 

```
# 角色
你是一个精准的数据提取AI。

# 输入文本
"订单号OD12345，客户张三，购买了产品A（数量2，单价50元）和产品B（数量1，单价100元），下单日期2023-10-26。希望尽快发货。"

# 任务与约束
请从上述文本中提取订单信息，并以下方JSON格式输出。
- `order_id` 必须以 "OD" 开头。
- `customer_name` 不能为空。
- `items` 列表中的每个项目必须包含 `product_name`, `quantity` (整数), `unit_price` (浮点数)。
- `total_amount` 必须是所有项目金额的总和。
- `order_date` 必须是 YYYY-MM-DD 格式。
- `priority` 字段根据文本推断，可选值为 "high", "medium", "low"。

# 输出格式
{
  "order_id": "string",
  "customer_name": "string",
  "items": [
    {
      "product_name": "string",
      "quantity": "integer",
      "unit_price": "float"
    }
  ],
  "total_amount": "float",
  "order_date": "string (YYYY-MM-DD)",
  "priority": "string (high/medium/low)"
}

```








## 4.3  复杂需求：沉淀项目规则 /  提供有效的上下文内容
**项目规则核心价值**

* **提升生产力**：减少对AI生成代码的人工修改，让AI更"懂你"
* **保障代码质量**：确保AI遵循统一的编码标准和最佳实践
* **强化项目规范**：将项目级约定内化到AI的行为中



### 4.3.1 规则分类体系
|规则类型|触发机制|适用场景|关键配置|
|-|-|-|-|
|Always（始终应用）|规则存在且启用时，始终包含在AI上下文中|全局编码规范、核心技术栈声明、安全准则|内容本身是关键|
|Specific Files（自动附加）|文件路径与globs字段匹配时自动附加|特定模块规范、文件类型标准、组件库说明|必须配置globs字段|
|Intelligently（智能选择）|AI根据语义和description智能判断|代码模板、解决方案、工作流程指导|清晰的description|
|Manual（手动应用）|用户通过@ruleName显式调用|不常用规则、测试调试、探索方案|易记的name|

### 4.3.2 规则库示例
**后端服务（Go 语言  -  GDP框架） ： 示例**

|分类|文件名称|生效范围|内容|说明|
|-|-|-|-|-|
|base|project-overview.mdc|始终生效|项目架构和目录结构|分层架构、依赖关系、初始化流程|
||README.mdc|始终生效|项目简介和核心模块|项目概览、业务模块、入口文件|
|framework|gdp-framework.mdc|始终生效|GDP框架使用指南|Boot、GHTTPServer、Logit、RAL等核心组件|
||architecture-patterns.mdc|手动使用|架构模式和设计原则|分层架构、依赖注入、RESTful资源、中间件|
|language|code-style.mdc|应用于*.go|代码风格指南|命名、注释、格式化、项目特定风格|
|biz|decision.mdc|手动使用|决策模块开发指南|选购卡、实体卡片、Excel数据解析|
||aivideo.mdc|手动使用|AI视频模块开发指南|审核活动、审核记录、封面审核|
||crud-operations.mdc|手动使用|CRUD操作开发指南|RESTful资源、数据库操作、HTTP接口|

**规则示例代码库**：

* 后端规则：[baidu/ps-shangpin/comate-rules/content-platform](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/comate-rules)
* 前端规则：[baidu/ps-shangpin/comate-rules/content-platform-tpl](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ps-shangpin/comate-rules)





---



# 5. AI 编程核心痛点与优化思路
## 5.1. 核心痛点
当前 使用 AI 编程工具（Comate、Cursor、Claude Code 等）核心痛点集中在 **上下文管理 **与 **进阶协作 **。

## 5.2 关键问题与落地思路
### 5.2.1 上下文长度问题
* **痛点**：大型任务因上下文超限，效果差、逻辑乱
* **解决思路**：大任务拆解为小任务
    * 工具自动拆分：todo list，或claude code中的Skill调用
    * 手动拆分：先设计、总结，再分步实施




### 5.2.2 上下文缺失问题
当前上下文较为依赖人工输入，是编写prompt的一大效率瓶颈。

当前实践较成功的一个场景是F2C（figma to code 设计稿生成代码），figma本身支持以mcp方式，将设计稿细节提供给模型，包括图层细节。

|**缺失类型**|**解决思路**|**难点**|
|-|-|-|
|项目结构 / 开发规范|制定 Rules（固化规范要求）||
|依赖库使用（第三方 / 内部）|MCP 工具接入（开源用 Context7，内部库自建 MCP）|部分库本身缺乏文档或有误，需ai校验总结|
|接口定义（Proto/JSON API）|Proto 直接用接口文件JSON API 通过 Swagger 自动生成，以文件或 MCP 引入|接口文档维护成本高，自动生成对现有开发体系冲击大|
|数据依赖（DB 表结构 / 样例数据）|基于 MCP 提供表结构查询、样例数据查询能力||

### 5.2.3 进阶问题与应对
1. **需求文档适配AI编程**

    * **痛点：**产品方案需经过多轮评审校对，补充边界、异常、分支情况的考虑，且有些考虑在实际开发中再明确。
    * **思路**：结合代码库逻辑，自动分析 MRD 缺失（边界 / 异常场景），辅助 PM 补全，提升第一版需求质量
    * **难点**：MRD 含大量图片，大模型理解成本高

2. **大型系统方案设计**

    * **痛点**：大型系统涉及众多模块，针对每次需求，要分析变更范围，目前完全依赖人工，进入具体模块开发后，再引入AI辅助
    * **思路**：以系统设计的文档+具体代码库+数据表结构作为输入，结合具体需求自动分析改动范围。可一定程度优化工作流程，但仍无法应对搜索、feed等超大规模系统。
    * **难点**：很多系统本身就是长期迭代行程，没人说的清楚理念

3. **提升并行工作能力**

    * **痛点**：当前主要落地场景是提效，主要手段是『结对编程』方式**频繁交互**，更理想的模式是将有一定规模的任务交给AI，按需介入回收结果，实现并行处理（人在沟通、模型在工作）
    * **思路**：
        * 短期看，可将一些重复且复杂任务以Skill等方式沉淀，中间步骤准确率高就可以执行更大的任务
        * 长期看，可能是伪命题？只要AI做的够快，就不需要并行




## 5.3 优化实践
### 5.3.1 引入模型上下文服务
开源库使用开源的context7提供上下文，公司内部自建baidu-context平台，收集常用库文档，提供上下文。[context服务方案](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/zjXmUt2XiK/lt1BHU8Z8v/Wh-_yGVSICZITG?t=mention&mt=doc&dt=doc)(本身也是通过ai coding方式，生成了90%+代码)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b98a1c75f82f4b648ad90e83e5d15698&docGuid=V-sP_1fw48uWB9 "")


**平台示例：** [http://yangxiaotong-dev.bcc-bdbl.baidu.com:8180/](http://yangxiaotong-dev.bcc-bdbl.baidu.com:8180/)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01fa0aa6f194473483056b58a3e9ba0e&docGuid=V-sP_1fw48uWB9 "")
结合简单的rules，模型可自己通过mcp 查询框架使用实例，减少人工编写prompt成本，提升生成准确率。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=17a5bb63fc3c4530a4ed9c7311c4d926&docGuid=V-sP_1fw48uWB9 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5b87dab6b90f40d4a7855f63c1bfe15f&docGuid=V-sP_1fw48uWB9 "")


---

# 附录
##  参考资料
**官方文档**

* [Comate规则使用说明](https://cloud.baidu.com/doc/COMATE/s/Zm9l4agw3)
* [Cursor官方文档](https://cursor.com/docs)
* [Cursor Rules工作原理](https://cursor.com/ja/docs/context/rules)

**内部实践**

* [talospro代码生成实践-zulu篇](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/au0U6X20tD/PpEGlZM_X3QVML)
* [百度App Rules方案](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/qCCPuIpbfn/_7x3r1CnhB/LbSYr0-M0-hcy1)
* [电商后端AI实践案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/5BHwcRow_9pXQl?t=mention&mt=doc&dt=doc)
* [Comate 使用海外大模型实践](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/K4aC71pX9v/pOrzfg2tYX/l7sKsAdOkZ9Koq?t=mention&mt=doc&dt=doc)

**外部实践**

* [AI编程最佳实践](https://mp.weixin.qq.com/s/rfanrMtMMuyUTwsDYmlxSg)
* [Cursor Rules优化](https://kirill-markin.com/zh/zhishi/cursor-ide-ai-bianma-guize-youhua/)

**系统提示词参考**

* [AI工具系统提示词代码库](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
* [Cursor Agent Prompt 2.0](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/Cursor%20Prompts/Agent%20Prompt%202.0.txt)



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4613ef81958a4bd7969a8a2a693c8510&docGuid=t0Wg1AdIFUwIoJ "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
