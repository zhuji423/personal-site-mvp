---
title: "输出校验与修正约束"
description: "相关文件说明 - .lumos/requirement.md 业务需求说明及生成流程引导，流程分析必须遵循的输入依据 - .lumos/designindex.md 代码库职责与文件索引参考 - .lumos/featureclarify."
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\task_generator\\fallback.md"
---
# 输出校验与修正约束

相关文件说明
- `.lumos/requirement.md` 业务需求说明及生成流程引导，流程分析必须遵循的输入依据
- `.lumos/design_index.md` 代码库职责与文件索引参考
- `.lumos/feature_clarify.md` 当前功能点澄清与判定结果文件，需在发现问题时进行修复或调整

**本任务的完成标志不是功能点产出本身，而是：**
- 针对每个功能点，反思并修复 `designConfig` 参数配置；
- 完成所有必要的后续层级设计（Step2 / Step3），
- 并输出完整、可校验的设计结果。

**请严格按照执行要求约束分析流程完成所有任务。**

## 自校验与回溯分析
* 当前进行自校验与回溯分析，重点检查是否存在以下问题：
- 功能点或验收标准拆分遗漏
- **职责范围误判**，包括但不限于：
    - 将**纯配置类变更**误判为无需变更；
        → **纯配置类变更**必须在资源对象层进行设计生成配置详情，并分析其对接口或行为的影响；
    - **将“尚未实现的需求”误判为“已有能力已覆盖”**；
- 设计配置参数判定过严或存在逻辑错误
- 分析流程未完整按输入 query 执行而**中途终止**

## 修正触发与流程继续规则（关键）

### 修正触发
- 若在自校验或回溯分析中发现上述任一问题，**必须触发修正流程**：
    - 修正所有受影响的分析结论、职责判定及设计配置参数；
    - 重新完成 **Step1：需求分析与功能澄清**，并产出完整、可校验的 `feature_clarify.md`。

### 流程继续规则
- **修正完成并不代表流程结束，必须基于修正后的 `designConfig` 继续执行后续流程**：
    - 对每个功能点，**以 Step1 输出的 `designConfig` 为后续流程驱动判定依据**：
        - 只要 `designConfig.resource = true` 或 `designConfig.capability` 非空，
            则 **必须执行 Step2（`foundation-design`）**；
    - 对每个功能点：
        - 只要 `designConfig.application != none`，
            则 **必须执行 Step3（`api-design` / `execute-design`）**；

# 重要约束

功能点产出**不是任务终点**，必须以功能点的 `designConfig` 作为唯一流程驱动依据，持续执行后续步骤（Step2 / Step3），**不得在中间阶段终止**，**直到所有功能点的必要步骤全部完成功能点各层级实现设计**并输出结果。