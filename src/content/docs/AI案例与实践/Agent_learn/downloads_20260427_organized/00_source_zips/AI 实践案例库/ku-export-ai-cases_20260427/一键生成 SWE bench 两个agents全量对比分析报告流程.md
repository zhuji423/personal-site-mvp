---
title: "AI Coding Agent 对比分析系统架构文档"
description: "一键生成 SWE bench 两个agents全量对比分析报告流程"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\一键生成 SWE bench 两个agents全量对比分析报告流程.md"
---
一键生成 SWE bench 两个agents全量对比分析报告流程

#### 🧑‍🏫 案例作者：[@陈一言](https://ku.baidu-int.com?t=mention&mt=contact&id=1fbbad00-fcec-11f0-bcb8-cb5d2a7c9372)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了一个基于大模型的自动化分析系统，用于深度对比两个AI Coding Agent在SWE-bench测试集上的性能差异。系统通过数据准备、案例分类、并行处理、日志压缩、路径对比和综合分析等步骤，自动化提取策略层面的洞察，生成全面的对比分析报告。该系统具有滚动压缩/聚合、并发处理、多层次分析等技术亮点，支持灵活配置和扩展，帮助团队快速理解AI Coding Agent的优劣势。
# AI Coding Agent 对比分析系统架构文档
## 系统概述
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ab06f5cc1eb449ed93678ff565f45517&docGuid=ZcKvLBkbVniQEZ "")
这是一个由Zulu 辅助搭建的基于大模型的自动化分析系统，用于深度对比两个 AI Coding Agent 在 SWE-bench 测试集上的性能差异。系统通过调用大语言模型（LLM）对测试日志进行压缩、对比和聚合分析，最终生成全面的策略优劣势报告。

**核心价值**：自动化地从海量测试日志中提取策略层面的洞察，帮助开发团队理解不同 AI Coding Agent 的优劣势，指导产品改进方向。

---

## 系统架构
### 整体流程图
```
graph TB
    Start([开始: 一键生成对比报告])
    
    subgraph Step1[步骤1: 数据准备]
        Pull[拉取测试数据<br/>copy_and_stats.py]
        Extract[解压 result.tar.gz]
        Stats[计算通过率统计]
        Pull --> Extract --> Stats
    end
    
    subgraph Step2[步骤2: 案例分类]
        LoadJSON[加载测试结果 JSON]
        CalcSets[计算案例集合]
        OnlyA[only_agent1_resolved]
        OnlyB[only_agent2_resolved]
        Both[both_resolved]
        Neither[both_unresolved]
        LoadJSON --> CalcSets
        CalcSets --> OnlyA
        CalcSets --> OnlyB
        CalcSets --> Both
        CalcSets --> Neither
    end
    
    subgraph Step3A[步骤3a: Agent1 胜出案例处理]
        direction TB
        CasesA[Agent1 胜出的案例列表]
        
        subgraph ParallelCompressA[并行滚动压缩]
            direction LR
            LogA1[Agent1 日志1] --> CompressA1[Claude 4.5 Haiku<br/>滚动压缩]
            LogA2[Agent1 日志2] --> CompressA2[Claude 4.5 Haiku<br/>滚动压缩]
            LogA3[Agent1 日志...] --> CompressA3[Claude 4.5 Haiku<br/>滚动压缩]
            
            LogB1[Agent2 日志1] --> CompressB1[Claude 4.5 Haiku<br/>滚动压缩]
            LogB2[Agent2 日志2] --> CompressB2[Claude 4.5 Haiku<br/>滚动压缩]
            LogB3[Agent2 日志...] --> CompressB3[Claude 4.5 Haiku<br/>滚动压缩]
        end
        
        subgraph ParallelCompareA[并行路径对比]
            direction LR
            Compare1[Case1: 成功 vs 失败<br/>Gemini 2.5 Pro]
            Compare2[Case2: 成功 vs 失败<br/>Gemini 2.5 Pro]
            Compare3[Case...: 成功 vs 失败<br/>Gemini 2.5 Pro]
        end
        
        AggregateA[综合分析<br/>Gemini 2.5 Pro<br/>滚动聚合所有对比]
        ReportA[生成报告:<br/>agent1_beats_agent2/report.txt]
        
        CasesA --> ParallelCompressA
        CompressA1 & CompressB1 --> Compare1
        CompressA2 & CompressB2 --> Compare2
        CompressA3 & CompressB3 --> Compare3
        Compare1 & Compare2 & Compare3 --> AggregateA
        AggregateA --> ReportA
    end
    
    subgraph Step3B[步骤3b: Agent2 胜出案例处理]
        direction TB
        CasesB[Agent2 胜出的案例列表]
        
        subgraph ParallelCompressB[并行滚动压缩]
            direction LR
            LogC1[Agent2 日志1] --> CompressC1[Claude 4.5 Haiku<br/>滚动压缩]
            LogC2[Agent2 日志2] --> CompressC2[Claude 4.5 Haiku<br/>滚动压缩]
            LogC3[Agent2 日志...] --> CompressC3[Claude 4.5 Haiku<br/>滚动压缩]
            
            LogD1[Agent1 日志1] --> CompressD1[Claude 4.5 Haiku<br/>滚动压缩]
            LogD2[Agent1 日志2] --> CompressD2[Claude 4.5 Haiku<br/>滚动压缩]
            LogD3[Agent1 日志...] --> CompressD3[Claude 4.5 Haiku<br/>滚动压缩]
        end
        
        subgraph ParallelCompareB[并行路径对比]
            direction LR
            Compare4[Case1: 成功 vs 失败<br/>Gemini 2.5 Pro]
            Compare5[Case2: 成功 vs 失败<br/>Gemini 2.5 Pro]
            Compare6[Case...: 成功 vs 失败<br/>Gemini 2.5 Pro]
        end
        
        AggregateB[综合分析<br/>Gemini 2.5 Pro<br/>滚动聚合所有对比]
        ReportB[生成报告:<br/>agent2_beats_agent1/report.txt]
        
        CasesB --> ParallelCompressB
        CompressC1 & CompressD1 --> Compare4
        CompressC2 & CompressD2 --> Compare5
        CompressC3 & CompressD3 --> Compare6
        Compare4 & Compare5 & Compare6 --> AggregateB
        AggregateB --> ReportB
    end
    
    FinalReport[生成最终汇总报告<br/>final_comparison.txt]
    End([结束])
    
    Start --> Step1
    Step1 --> Step2
    Step2 --> Step3A
    Step2 --> Step3B
    OnlyA -.案例列表.-> CasesA
    OnlyB -.案例列表.-> CasesB
    Step3A --> FinalReport
    Step3B --> FinalReport
    FinalReport --> End
    
    style Start fill:#e1f5e1
    style End fill:#ffe1e1
    style ReportA fill:#fff4e1
    style ReportB fill:#fff4e1
    style FinalReport fill:#e1f0ff
    style ParallelCompressA fill:#f0f0f0
    style ParallelCompressB fill:#f0f0f0
    style ParallelCompareA fill:#f5f5f5
    style ParallelCompareB fill:#f5f5f5
```
**流程说明**：

1. **数据准备阶段**：拉取并解压测试数据，计算通过率
2. **案例分类阶段**：将所有案例分为4个集合
3. **并行处理阶段**（核心）：

    * 对每个 `only_solved_by_X` 集合中的每个 case：
        * **并行调用 Claude 4.5 Haiku** 进行滚动压缩（成功和失败路径）
        * **并行调用 Gemini 2.5 Pro** 对比成功/失败路径

    * **滚动聚合**所有对比结果，生成综合报告

4. **最终汇总**：生成两份报告的总结

**关键特性**：

* ⚡ **并行压缩**：多个案例的日志同时压缩（ThreadPoolExecutor）
* 🔄 **滚动机制**：处理超长日志和大量案例
* 📊 **双向对比**：生成 `agent1_beats_agent2` 和 `agent2_beats_agent1` 两份报告

---

## 核心模块详解
### 1. copy_and_stats.py - 数据拉取与统计
**功能**：从远程 SWE-bench 测试环境复制结果到本地并计算统计指标

**关键类**：`TestCopyAndStats`

**工作流程**：

1. 验证源文件存在性
2. 使用 `sudo cp` 复制日志目录和 JSON 文件
3. 解压所有 `result.tar.gz` 文件
4. 计算通过率并更新 JSON

**输出**：

* 日志目录：`data/{product}_verified_{model}/`
* 统计 JSON：`data/zulu.eval_{product}_swebench_docker_{model}.json`

**关键指标**：

* `pass_rate` = `resolved_instances` / `completed_instances`

---

### 2. summarize_trajectory.py - 日志压缩
**功能**：使用 LLM 压缩完整日志，提取策略路径关键信息

**关键类**：`TrajectorySummarizer`

**核心技术**：

#### 滚动压缩机制（Rolling Compression）
类似 RNN 的状态维护机制，用于处理超长日志：

```
第1块: [日志前500K字符] → LLM → [压缩摘要1]
第2块: [压缩摘要1] + [日志中250K字符] → LLM → [压缩摘要2]
第3块: [压缩摘要2] + [日志后250K字符] → LLM → [最终摘要]
```
**分析维度**（11个）：

1. 原始 Query
2. 工具调用历史
3. 规划内容（粒度、灵活性、执行力）
4. 问题解决路径（时序流程图）
5. 错误处理
6. 记忆压缩策略
7. 最终结果
8. 异常表现
9. 底层机制观察
10. Remarkable 特性
11. 与人类工程师对比

**并发处理**：

* 使用 `ThreadPoolExecutor` 并发处理多个日志
* 默认 5 个 worker，可配置

**输出**：

* `*_trajectory_summary.txt`（与原日志同目录）

---

### 3. compare_trajectories.py - 路径对比
**功能**：对比成功和失败的两个 trajectory summary，分析差异

**关键类**：`TrajectoryComparer`

**LLM 提示词策略**：

* 输入：成功路径摘要 + 失败路径摘要
* 输出：结构化对比分析

**分析框架**：

1. **关键差异总结**（3-5句话）
2. **成功路径优势**（至少3点）

    * 优势描述
    * 具体体现（引用原文）
    * 重要性分析

3. **失败路径缺陷**（至少3点）

    * 缺陷描述
    * 具体体现
    * 失败原因

4. **策略层面启示**
5. **系统底层机制观察**

    * 上下文获取能力
    * 策略规划能力
    * 异常处理能力
    * 记忆压缩能力

**输出**：

* `data/{winner}_beats_{loser}/{case_name}.txt`

---

### 4. aggregate_analysis.py - 综合分析
**功能**：汇总所有单个 case 的对比，提炼全局策略规律

**关键类**：`AggregateAnalyzer`

**核心技术**：

#### 滚动聚合机制（Rolling Aggregation）
处理大量案例对比结果：

```
第1批案例: [案例1-N] → LLM → [初步分析]
第2批案例: [初步分析] + [案例N+1 - M] → LLM → [更新分析]
...
最终: [完整综合分析报告]
```
**分析框架**：

1. **执行摘要**
2. **成功策略关键优势**

    * 重要性评分（1-10）
    * 影响范围（案例数/占比）
    * 典型案例举例

3. **失败策略致命缺陷**

    * 严重程度评分（1-10）
    * 影响范围
    * 根本原因

4. **模式识别**

    * 共同模式
    * 关键决策点差异

5. **改进建议**（优先级排序）
6. **数据统计**

**输出**：

* `data/{winner}_beats_{loser}/report.txt`

---

### 5. generate_comparison_report.py - 一键流程
**功能**：自动化完整流程，从数据拉取到最终报告生成

**关键类**：`ComparisonReportGenerator`

**特性**：

* **测试模式**：限制处理案例数量（默认每类3个）
* **并发控制**：可配置最大 worker 数（默认10）
* **随机延迟**：避免 API 限流（0.1-0.5秒）

**执行步骤**：

1. 检测并拉取测试数据（如需）
2. 加载测试结果 JSON
3. 计算案例集合差异
4. 保存对比元数据 JSON
5. 处理 agent2 胜出案例
6. 处理 agent1 胜出案例
7. 生成最终汇总报告

**输出**：

* `data/comparison_{p1}_{m1}_vs_{p2}_{m2}.json`（元数据）
* `data/{winner}_beats_{loser}/`（详细对比）
* `data/final_comparison_{p1}_{m1}_vs_{p2}_{m2}.txt`（汇总）

---

## LLM 调用策略
### API 封装
所有模块通过 `call_openrouter_api.py` 统一调用 LLM API

### 重试机制
* 最大重试次数：3次
* 指数退避：2^attempt + random(0,1) 秒
* 失败处理：返回详细错误信息

### 模型选择
* **日志压缩**：`anthropic/claude-haiku-4.5`（性价比高）
* **路径对比**：`google/gemini-2.5-pro`（深度分析）
* **综合分析**：`google/gemini-2.5-pro`（全局视角）

### 成本优化
* 滚动压缩/聚合：避免单次请求过长
* 并发控制：平衡速度与成本
* 测试模式：开发调试时限制案例数

---

## 数据流与存储
### 目录结构
```
data/
├── {product}_verified_{model}/          # 测试日志
│   ├── {case_id}/
│   │   ├── result.tar.gz               # 压缩包
│   │   ├── {case_id}_result/           # 解压后
│   │   │   ├── {case_id}_{product}_logs/
│   │   │   │   ├── store/chat_session_* (Zulu)
│   │   │   │   │   └── *_trajectory_summary.txt
│   │   │   │   └── projects/-testbed/*.jsonl (Claude)
│   │   │   │       └── *_trajectory_summary.txt
│   │   └── ...
│   └── ...
├── zulu.eval_{product}_swebench_docker_{model}.json  # 统计数据
├── comparison_{p1}_{m1}_vs_{p2}_{m2}.json            # 对比元数据
├── {winner}_beats_{loser}/                           # 对比结果
│   ├── {case_id}.txt                                 # 单案例对比
│   └── report.txt                                    # 综合报告
└── final_comparison_{p1}_{m1}_vs_{p2}_{m2}.txt       # 最终汇总
```
### 关键数据格式
#### 统计 JSON
```
{
  "total_instances": 500,
  "completed_instances": 450,
  "resolved_instances": 300,
  "unresolved_instances": 150,
  "pass_rate": 0.6667,
  "resolved_ids": ["case1", "case2", ...],
  "unresolved_ids": ["case3", "case4", ...]
}
```
#### 对比元数据 JSON
```
{
  "comparison_metadata": {
    "test_1": {...},
    "test_2": {...}
  },
  "case_categories": {
    "only_test1_resolved": {
      "count": 50,
      "case_ids": [...]
    },
    "only_test2_resolved": {...},
    "both_resolved": {...},
    "both_unresolved": {...}
  }
}
```
---

## 使用场景
### 场景1: 快速对比（推荐）
```
python3 workflows/generate_comparison_report.py zulu dsv3p1 cc dsv3p1
```
### 场景2: 测试模式（开发调试）
```
python3 workflows/generate_comparison_report.py \
  zulu dsv3p1 cc dsv3p1 \
  --test-mode \
  --test-limit 3 \
  --max-workers 5
```
### 场景3: 手动逐步分析
```
# 步骤1: 拉取数据
python3 workflows/copy_and_stats.py zulu dsv3p1

# 步骤2: 压缩日志
python3 workflows/summarize_trajectory.py data/zulu_verified_dsv3p1/

# 步骤3: 对比案例
python3 workflows/compare_trajectories.py \
  data/zulu_verified_dsv3p1/case1/*_summary.txt \
  data/cc_verified_dsv3p1/case1/*_summary.txt

# 步骤4: 综合分析
python3 workflows/aggregate_analysis.py zulu dsv3p1 cc dsv3p1
```
---

## 技术亮点
### 1. 滚动压缩/聚合机制
* **问题**：日志文件可能超过 LLM 上下文窗口
* **解决**：类似 RNN 的状态维护，逐块处理并累积摘要
* **优势**：
    * 支持任意长度日志
    * 保持信息连贯性
    * 避免信息丢失


### 2. 并发处理
* **ThreadPoolExecutor**：充分利用 I/O 等待时间
* **随机延迟**：避免 API 限流
* **进度跟踪**：实时显示处理进度

### 3. 多层次分析
* **单案例层**：详细对比成功/失败路径
* **全局层**：提炼跨案例的策略规律
* **量化评估**：重要性/严重程度评分

### 4. 灵活配置
* 测试模式：快速验证流程
* 并发控制：平衡速度与成本
* 模型选择：根据任务复杂度选择

---

## 依赖与环境
### Python 依赖
```
requests
tenacity
```
### 系统要求
* Python 3.6+
* Linux 环境（使用 sudo 权限）
* 网络访问（调用 OpenRouter API）

### API 配置
需要在 `call_openrouter_api.py` 中配置 API key

---

## 扩展性
### 支持新的 Agent
1. 在 `copy_and_stats.py` 中配置路径
2. 在 `summarize_trajectory.py` 中添加日志格式识别规则
3. 运行完整流程

### 支持新的分析维度
1. 修改 `COMPRESSION_PROMPT_TEMPLATE` 添加新维度
2. 修改 `COMPARISON_PROMPT_TEMPLATE` 调整对比框架
3. 修改 `AGGREGATE_PROMPT_TEMPLATE` 更新聚合逻辑

### 优化成本
1. 调整 `max_tokens_per_chunk`
2. 使用更便宜的模型
3. 启用测试模式限制案例数

---

## 最佳实践
### 1. 首次使用
* 使用 `--test-mode` 验证流程
* 检查输出质量
* 调整提示词（如需）

### 2. 生产环境
* 关闭测试模式
* 增加并发数（10-20）
* 监控 API 成本

### 3. 问题排查
* 检查日志文件格式
* 验证 API key 配置
* 查看详细错误信息

### 4. 结果解读
* 关注量化指标（评分、占比）
* 交叉验证典型案例
* 结合业务场景理解

---

## 总结
这是一个**基于 LLM 的智能分析系统**，核心价值在于：

1. **自动化**：从数据拉取到报告生成全自动
2. **深度分析**：不仅统计数字，更提取策略洞察
3. **可扩展**：支持新 Agent、新维度、新模型
4. **成本可控**：滚动机制 + 并发优化 + 测试模式

通过这个系统，团队可以快速理解不同 AI Coding Agent 的优劣势，指导产品迭代方向。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
