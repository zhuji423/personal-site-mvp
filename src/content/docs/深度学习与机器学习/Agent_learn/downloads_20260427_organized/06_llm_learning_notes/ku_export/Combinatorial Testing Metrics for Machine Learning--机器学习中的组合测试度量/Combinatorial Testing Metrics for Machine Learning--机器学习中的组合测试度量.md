---
title: "Combinatorial Testing Metrics for Machine Learning--机器学习中的组合测试度量"
description: "目的预测在一个数据集上训练并应用于另一个数据集的模型的性能的问题。"
date: "2026-04-28"
category: "深度学习与机器学习"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\Combinatorial Testing Metrics for Machine Learning--机器学习中的组合测试度量\\Combinatorial Testing Metrics for Machine Learning--机器学习中的组合测试度量.md"
---
# Combinatorial Testing Metrics for Machine Learning--机器学习中的组合测试度量
本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间关键词：组合测试、机器学习、操作包络、迁移学习、测试集选择

论文地址：



![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ac135c00443fd5f3dcf5afe05181f099)

目的预测在一个数据集上训练并应用于另一个数据集的模型的性能的问题。

定义了一种用于比较机器学习数据集的集合差异度量，并提出数据集之间的差异是组合覆盖函数：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=6873aa109adc6103b1da0700909e4812)

、

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ba37a816cdbffc6d4309f6cb75f6f52e)

。

核心思路度量定义了一个新的组合覆盖度量来比较数据集，侧重于第一级粒度（存在/不存在组合）。

t-way 值组合：将特定值分配给t个因子，或(因子，值)元祖的数值组合。

t-way 覆盖率：用于描述集合中出现的有效t-way值组合的比例。

用k个因子和它们各自的值定义一个宇宙，使得U是所有有效例子的集合，并且让Ut是有效t-way值组合的集合。给定数据集D ⊆ U，定义Dt为出现在D中的t-way值组合集。

D的t-way组合覆盖率是：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=6873aa109adc6103b1da0700909e4812)

 对于某个已定义的全集的覆盖范围的度量

 设S和T为数据集，定义St，Tt为分别出现在S，T中的t-way值组合的集合。集差Tt\St是出现在T中而不在s中的集合。定义t-way差集组合覆盖率：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ba37a816cdbffc6d4309f6cb75f6f52e)

。描述了两个数据集之间的差异。

SDCCt是一个介于0和1之间的分数。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=6da278af17388b57eb3025d76e1db52d)

| （0，1） | 0 | （0，1） | 0 | 1 |
| --- | --- | --- | --- | --- |

差集组合覆盖率是有向的，SDCCt(T\S)值越高，两组数据差异性越大。

应用强调了度量在两个不同领域的应用。（1）演示了基于数据中可解释特征的度量工具，可用于故障定位和可解释的分类。（2）使用度量定义模型的运行范围可扩展到以下方面的应用：迁移学习，训练和测试数据集的选择以及指导数据收集和标记工作。

A.故障定位

t-way值组合的集合差分已被应用于故障定位问题。多种集合论运算可用于减少确定性软件中可能的故障触发值组合的集合。

背景：运行测试集通常会导致大量通过测试和少量失败测试，但是失败测试中只有一小部分值组合会导致失败。Pt =通过测试的值组合，Ft =未通过测试的值组合，Ct =故障触发值组合，①计算Ft\Pt（在Ft但不在Pt）肯定包含Ct识别故障触发值。②如果Ft中的特定t-way值组合包含在所有包含相同t因子的较高强度值组合中，则t路值组合足以检测到错误。

B.可解释分类

ML中的分类问题和CT中的故障定位问题本质上是一样的。这个过程可以被看作是故障定位问题的一般化，其中失败的测试是类，通过的测试是非类——失败的测试有什么独特的因子值组合？

C.模型运行范围扩展

考虑在图像中检测白色卡车的问题。从俯视图来看，中午在浅色背景下的白色卡车可能比下午晚些时候在同样浅色背景下的白色卡车更难检测，在下午晚些时候，阴影存在或者从侧面来看，使得地平线破坏了背景。

为了在这些环境中的每一个中按预期执行，预计在训练数据集中必须包括“足够的”代表性例子。挑战在于如何定义上下文环境并衡量训练例子的代表性。

在一个环境中训练的模型被部署到一个新的环境中，可能不需要再训练或微调。其中CC是数据集相对于某个已定义的全集的覆盖范围的度量，SDCC描述了两个数据集之间的有向差异，并可用于测量训练模型的源数据集S和部署模型的目标数据集T之间的距离。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=0c25e67bca73654f3340a87f5ab0bf19)

当有多个数据集时，s数据集SDCCt(T\S)值最小，提供了源对目标中上下文的最佳覆盖。

可用于指导数据收集或标记工作。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c210cac5a3c4194fa9d9123ad7dfdb11)

卫星图像北方数据集和南方数据集，12个特征，6种取值范围

| CCt(south)=60/72=0.83 | CCt(north)=67/72=0.93 |
| --- | --- |

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=789c44a77bdf280b81fa711f67dcdb2f)

T\S黑，T∩S灰，¬T亮

| SDCCt(T\S)=1/60=0.02 | SDCCt(T\S)=8/67=0.12 |
| --- | --- |

D.测试集设计（不太对劲。。）

数据集被划分为训练集、验证集和测试集。当数据集很大并且应用随机选择时，希望测试集代表训练集。

一个简单的随机算法进行几个随机分区，并保留SDCC最低（最相似）的一个作为测试集。这相当于在模型的工作范围内进行测试。

另一种测试策略是，通过选择T使SDCCt(T \S)接近1会创建一个包含许多未训练上下文的测试集。这些数据可以作为新环境可能出现的挑战的参考。

启发收获对于解决一个数据集上训练并应用于另一个数据集的模型的性能的问题提供一定启发，为数据集的选用提供参考，在迁移模型到新环境降低性能损失。

注：

组合测试：是一种黑盒方法，使用伪穷举策略对大输入空间测试集成系统。被应用于：具有嵌入式ML组件的自主车辆系统的测试用例生成、测试神经网络的内部状态空间、特征选择、可解释得ML。

ppt：



