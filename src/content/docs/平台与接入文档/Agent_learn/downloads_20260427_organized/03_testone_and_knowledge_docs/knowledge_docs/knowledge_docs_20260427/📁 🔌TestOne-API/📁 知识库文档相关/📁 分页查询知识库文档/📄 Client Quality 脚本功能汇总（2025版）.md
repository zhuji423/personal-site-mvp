---
title: "Client Quality 脚本功能汇总"
description: "Client Quality 脚本功能汇总（2025版）"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 知识库文档相关\\📁 分页查询知识库文档\\📄 Client Quality 脚本功能汇总（2025版）.md"
---
Client Quality 脚本功能汇总（2025版）

# Client Quality 脚本功能汇总
## 目录结构
```
client_quality/
├── core_scripts/          # 【推荐】核心脚本目录
│   ├── client_scoring_engine.py   # 客户端评分引擎（稳定性驱动混合算法）
│   ├── client_scores_SoftMin.py   # 客户端评分引擎（SoftMin SLA算法）
│   ├── province_isp_scorer.py     # 省份运营商评分系统
│   ├── hive_direct_query.py       # Hive 直接查询工具
│   └── run_provice_scorer.sh     # 批量省份评分执行脚本
│
├── old_core/              # 旧版本兼容脚本
│   ├── client_fault_statistics.py      # 故障数据收集（旧版）
│   ├── final_analysis_report.py        # 成功率分析（旧版）
│   └── unified_client_scorer_improved.py  # 统一评分引擎（改进版）
│
├── output/                # 输出目录
├── input/                # 输入数据目录
├── data/                 # 省份运营商评分数据
├── dcdn_lists/           # 异常矿机列表
├── results/              # 分析结果
│
├── anomaly_detection.py        # 异常矿机检测工具
├── search_client_timeline.py   # 矿机详情查询工具
├── tsdb_ratio.py              # TSDB 节点 ratio 数据拉取
├── analyze_data_inconsistency.py  # 数据不一致分析
└── analyze_threshold.py        # 阈值配置分析
```
## 脚本状态说明
|状态|说明|
|-|-|
|🟢 **活跃脚本**|主要功能脚本，持续维护和使用|
|🟡 **辅助脚本**|一次性分析工具，偶尔使用|
|🔴 **可废弃脚本**|功能已被新版本迭代，建议使用新版本|

---

## 1. 核心脚本（推荐使用）
### core_scripts/client_scoring_engine.py 🟢
**功能**: 客户端评分引擎 - 基于稳定性驱动的混合评分算法

**核心算法设计初衷**:
该算法旨在平衡"基础表现"和"稳定性"两个维度，适合评估需要持续稳定运行的客户端（如CDN矿机）。设计理念如下：

1. **双重评分模型**: 基础表现(40%) + 稳定性表现(60%)

    * 基础分反映整体性能水平（平均成功率 × 0.8）
    * 稳定性分基于标准差进行惩罚，波动越大扣分越多

2. **波动惩罚机制**: 基于标准差的多级梯度惩罚

    * 临界波动(标准差>15)：惩罚系数0.8 → 稳定性极差
    * 高波动(标准差10-15)：惩罚系数0.6 → 稳定性差
    * 中等波动(标准差5-10)：惩罚系数0.4 → 稳定性一般
    * 低波动(标准差≤5)：无惩罚 → 稳定

3. **等级划分**:

    * 优秀(≥90): 表现稳定且质量卓越
    * 良好(75-90): 整体良好但存在改进空间
    * 一般(60-75): 基本达标但稳定性不足
    * 较差(<60): 存在明显性能问题

**数据流向**:

```
输入:
  └── tb_client_quality_stats 表（数据库）

处理:
  └── 数据读取 → 成功率计算 → 评分计算 → 数据库存储

输出:
  └── tb_client_scores_avgstd  # 数据库表
```
**运行方式**:

```
# 不指定日期，默认使用昨天
python core_scripts/client_scoring_engine.py

# 指定日期（格式：YYYYMMDD）
python core_scripts/client_scoring_engine.py --date 20260301

# 简写日期会自动补全为完整格式
python core_scripts/client_scoring_engine.py --date 01
```
---

### core_scripts/client_scores_SoftMin.py 🟢
**功能**: 客户端评分引擎 - 基于 SoftMin 的高敏感度 SLA 评分算法

**核心算法设计初衷**:
该算法专门为SLA（服务等级协议）监控设计，对"深坑"（严重故障）极其敏感，适合对服务质量要求极高的场景。设计理念如下：

1. **SoftMin 惩罚机制**:

    * 对"深坑"（严重掉线）施加指数级惩罚
    * 对"微小波动"高度包容
    * 数学原理：SoftMin = log(mean(exp(k*x))) / k，当k越大，对最小值的惩罚越严重

2. **LogSumExp 防溢出**:

    * 原始公式: raw_soft_min = log(mean(exp(k * gaps))) / k
    * 当k=1000时，exp(1000)会溢出
    * 优化公式: z_max + log(mean(exp(z - z_max))) / k，绝对不会溢出

3. **SLA Nines 映射**:

    * 99% 成功率 → 90分（优秀）
    * 90% 成功率 → 60分（及格）
    * 公式: score = 30 + nines * 30，其中 nines = -log10(gap)

4. **样本量降级**:

    * 数据点<6 或总请求<100 时，评分上限 85 分
    * 防止样本量过少导致评分失真

**数据流向**:

```
输入:
  └── tb_client_quality_stats 表（数据库）

处理:
  └── 数据读取 → 成功率计算 → SoftMin评分 → 数据库存储

输出:
  └── tb_client_scores_softmin  # 数据库表
```
**运行方式**:

```
python core_scripts/client_scores_SoftMin.py --date 20260301
```
---

### core_scripts/province_isp_scorer.py 🟢
**功能**: 省份运营商评分系统 - 基于 SoftMin_K1000 的小时级评分算法

**核心算法设计初衷**:
专为CDN质量监控设计，按省份+运营商维度进行小时级评分，捕捉短暂的服务质量下降。设计理念如下：

1. **小时级聚合**: 每小时60个分钟级数据点计算一个评分
2. **SoftMin_K1000**: 对深坑施加指数级惩罚
3. **有效数据阈值**: 有效数据点<10个时跳过该组合

**数据流向**:

```
输入:
  └── TSDB (百度监控系统) - cdnsli_ratio.datasource.prov.isp 指标

处理:
  └── TSDB拉取 → 数据分组 → SoftMin_K1000评分 → DB存储

输出:
  └── tb_acl_scores_hour  # 数据库表
```
**运行方式**:

```
# 不指定日期，默认使用昨天
python core_scripts/province_isp_scorer.py

# 指定日期（格式：YYYY-MM-DD）
python core_scripts/province_isp_scorer.py --date 2026-03-01

# 指定并发数
python core_scripts/province_isp_scorer.py --date 2026-01-31 --max-workers 10
```
---

### core_scripts/run_provice_scorer.sh 🟢
**功能**: 批量省份运营商评分执行脚本

**配置方式**:

```
# 在脚本中修改日期范围
START_DATE="2026-02-06"
END_DATE="2026-02-28"
```
**运行方式**:

```
bash core_scripts/run_provice_scorer.sh
```
---

## 2. 数据处理脚本
### anomaly_detection.py 🟢
**功能**: 增强型异常矿机检测工具

**核心特性**:

* 三阶段分析流程：目标节点筛选 → 地区矿机分析 → 异常检测
* 严格异常检测算法（融合 IQR/Gap/均值偏离/头部均值检测）
* 自动限制异常比例（默认 <=20%）
* 小样本自动跳过

**数据流向**:

```
输入:
  └── 命令行参数: date, start_time, end_time
  └── monitordata_{date} 表

处理:
  └── 正常节点筛选 → 地区分析 → 异常检测算法

输出:
  └── logs/anomaly_detection.log
  └── results/anomaly_detection_results_*.md
  └── dcdn_lists/dcdn_list_*.md
```
**运行方式**:

```
python anomaly_detection.py 25 12:00 14:00
```
---

### search_client_timeline.py 🟡
**功能**: 矿机详情查询工具 - 按时序显示单个矿机的成功率数据

**运行方式**:

```
python search_client_timeline.py --client-id <矿机ID>
```
---

### tsdb_ratio.py 🟡
**功能**: TSDB 节点 ratio 数据拉取工具

**核心能力**:

* 从百度 TSDB 系统查询节点级 ratio 指标
* 批量处理 CDN 节点，支持并发查询
* 按小时时间粒度聚合数据

---

## 3. 辅助分析脚本
### analyze_data_inconsistency.py 🟡
**功能**: 分析数据不一致的原因

**分析内容**:

* 检查 client_fault_statistics.py 的 SQL 逻辑
* 分析缺失 client 的具体情况

---

### analyze_threshold.py 🟡
**功能**: 阈值配置分析脚本 - 格式化并展示 threshold.json 文件中的重要信息

---

## 4. 旧版本脚本（兼容保留）
### old_core/client_fault_statistics.py 🟡
**功能**: 故障数据收集（单一功能版本）

### old_core/final_analysis_report.py 🟡
**功能**: 成功率分析（单一功能版本）

### old_core/unified_client_scorer_improved.py 🟡
**功能**: 统一评分引擎（改进版）

---

## 数据库表结构
|表名|用途|读写|Note|
|-|-|-|-|
|`monitordata_{date}`|客户端监控原始数据|读|anomaly_detection.py|
|`tb_client_quality_stats`|客户端质量统计|读/写|hive_direct_query.py|
|`tb_client_scores_avgstd`|客户端评分（稳定性驱动算法）|写|client_scoring_engine.py|
|`tb_client_scores_softmin`|客户端评分（SoftMin SLA算法）|写|client_scores_SoftMin.py|
|`tb_acl_scores_hour`|省份运营商小时评分|写|province_isp_scorer.py|

---

## 评分算法对比
|特性|稳定性驱动混合算法|SoftMin SLA算法|
|-|-|-|
|算法核心|基础分(40%) + 稳定性分(60%)|SoftMin_K1000 + LogSumExp|
|惩罚对象|波动（标准差）|深坑（最小值）|
|适用场景|评估客户端整体稳定性|SLA监控，对故障敏感|
|评分范围|0-100分|0-100分|
|等级划分|优秀≥90, 良好75-90, 一般60-75, 较差<60|优秀≥90, 良好75-90, 一般60-75, 较差<60|
|特殊处理|无|样本量<6或请求<100时上限85分|

**设计初衷总结**:

* **稳定性驱动算法**: 适合评估长期稳定运行的设备，波动大则扣分严重
* **SoftMin SLA算法**: 适合SLA监控，只要有一次深坑（严重故障），评分就会大幅下降

---

## 最佳实践
### 1. 客户端评分流程（推荐）
**方式1: 使用稳定性驱动算法**

```
python core_scripts/client_scoring_engine.py --date 25
```
**方式2: 使用SoftMin SLA算法**

```
python core_scripts/client_scores_SoftMin.py --date 25
```
### 2. 省份运营商评分流程
```
# 单日评分
python core_scripts/province_isp_scorer.py --date 2026-01-31

# 批量多日评分
bash core_scripts/run_provice_scorer.sh
```
### 3. 异常检测
```
python anomaly_detection.py 25 12:00 14:00
```
### 4. 矿机排查
```
python search_client_timeline.py --client-id <矿机ID>
```
---

## 脚本选择指南
|用途|推荐脚本|算法特点|
|-|-|-|
|客户端稳定性评估|core_scripts/client_scoring_engine.py|基础表现40% + 稳定性60%，波动大扣分多|
|客户端SLA监控|core_scripts/client_scores_SoftMin.py|SoftMin算法，对深坑敏感|
|省份运营商评分|core_scripts/province_isp_scorer.py|小时级SoftMin_K1000评分|
|批量省份评分|core_scripts/run_provice_scorer.sh|连续多天自动执行|
|异常矿机检测|anomaly_detection.py|多阶段严格检测算法|
|矿机详情查询|search_client_timeline.py|时序成功率展示|
