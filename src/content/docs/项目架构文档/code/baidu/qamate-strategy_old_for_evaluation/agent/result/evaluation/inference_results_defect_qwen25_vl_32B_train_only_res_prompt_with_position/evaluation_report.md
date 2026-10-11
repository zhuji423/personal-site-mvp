---
title: "缺陷检测模型评估报告\\n\\n## 1. 存在性评估\\n- 精确率 (Precision): 0.985- 召回率 (Recall): 0.691- F1分数: 0.812- 准确率 (Accuracy): 0.687- 混淆矩阵: TP=6"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy_old_for_evaluation\\agent\\result\\evaluation\\inference_results_defect_qwen25_vl_32B_train_only_res_prompt_with_position\\evaluation_report.md"
---
# 缺陷检测模型评估报告\n\n## 1. 存在性评估\n- 精确率 (Precision): 0.985- 召回率 (Recall): 0.691- F1分数: 0.812- 准确率 (Accuracy): 0.687- 混淆矩阵: TP=67, FP=1, TN=1, FN=30\n\n## 2. 类型评估\n- 评估样本数: 67- 平均语义相似度: 0.591 ± 0.077- 条件准确率: 0.881- 匹配分布: {'perfect': 30, 'partial': 29, 'mismatch': 8}\n\n## 3. 位置评估\n- 评估样本数: 67- 平均相对距离: 7.275 ± 6.562- 位置准确率: 0.015- 定位分布: {'precise': 0, 'good': 1, 'rough': 2, 'failed': 64}\n\n## 4. 综合指标\n- 严格精确率: 0.020- 加权性能分数: 0.594\n