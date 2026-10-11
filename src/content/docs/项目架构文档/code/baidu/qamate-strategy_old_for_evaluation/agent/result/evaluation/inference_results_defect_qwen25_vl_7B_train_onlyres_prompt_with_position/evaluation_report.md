---
title: "缺陷检测模型评估报告\\n\\n## 1. 存在性评估\\n- 精确率 (Precision): 1.000- 召回率 (Recall): 0.153- F1分数: 0.265- 准确率 (Accuracy): 0.170- 混淆矩阵: TP=1"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\qamate-strategy_old_for_evaluation\\agent\\result\\evaluation\\inference_results_defect_qwen25_vl_7B_train_onlyres_prompt_with_position\\evaluation_report.md"
---
# 缺陷检测模型评估报告\n\n## 1. 存在性评估\n- 精确率 (Precision): 1.000- 召回率 (Recall): 0.153- F1分数: 0.265- 准确率 (Accuracy): 0.170- 混淆矩阵: TP=15, FP=0, TN=2, FN=83\n\n## 2. 类型评估\n- 评估样本数: 15- 平均语义相似度: 0.611 ± 0.072- 条件准确率: 0.933- 匹配分布: {'perfect': 10, 'partial': 4, 'mismatch': 1}\n\n## 3. 位置评估\n- 评估样本数: 15- 平均相对距离: 5.340 ± 4.560- 位置准确率: 0.200- 定位分布: {'precise': 2, 'good': 1, 'rough': 0, 'failed': 12}\n\n## 4. 综合指标\n- 严格精确率: 0.050- 加权性能分数: 0.446\n