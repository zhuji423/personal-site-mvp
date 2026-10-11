---
title: "NLP学习3：理解"
description: "根据结果在不在原文：抽取式、生成式抽取式根据抽取结果结构：实体抽取、关系抽取、事件抽取评测指标："
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\NLP学习3：理解\\NLP学习3：理解.md"
---
# NLP学习3：理解
本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间一、信息抽取技术与应用1.1 背景定义：自动从无结构&半结构文本中抽取结构化信息

分类：

根据结果在不在原文：抽取式、生成式抽取式根据抽取结果结构：实体抽取、关系抽取、事件抽取评测指标：

precision：预测正确/预测个数recall：预测正确/标注个数F1：2*precision*recall/(recall+precision)核心：解码设计

1.2 信息抽取技术1.2.1 实体抽取从文本中抽取出文本内容，并识别为预定义的类别。

解码设计：BIO，模型：crf条件随机场

实际问题：重叠嵌套；不连续

1.2.2 关系抽取从文本中抽取出一对实体和预定义的关系类型，得到实体关系三元组。关系失败有方向的，分为头实体和尾实体。

关系抽取分两步：实体抽取、关系分类

多步抽取方案：pipeline，一次模型抽取：joint

序列标注解码设计：BIO+关系标签，模型：crf条件随机场

[BIO] + [关系类别] + [头尾实体]SD代表关系『部位疾病』1和2代表头实体和尾实体![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e7e3adfb4d4f1e12a623c53e67cfacc3)

多分类序列标注解决重叠关系抽取

解码设计：BIO+关系标签+多分类，模型：sigmoid独立多分类

一个字可以被标识为多个类别有多个B类别，代表不同实体关系一个I类别标识单词范围SD代表关系『部位疾病』CH代表关系『病变部位』1，2代表头实体和尾实体![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ff644d2976aca1341d0e5f908fa053e4)

Pointer解决实体对组合

解码设计：Pointer+多类别+阶段抽取，模型：PointerNetwork

Pointer会预测实体的start和end位置CH代表关系『病变部位』先预测头实体，再根据头实体预测相关的尾实体![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=776e793a2e06344d7a179dcda441c7f0)

TPLinker解决关系分类问题（复杂实体连接）

解码设计：TPLinker（Token Pair Linking ），模型：TPLinke

两两字间进行多分类EH-ET类别代表一个实体的头尾SD代表关系『部位疾病』SH-OH代表关系中头尾实体的第一个字互相连接ST-OT代表关系中头尾实体的最后一个字互相连接![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ef1771fade20cf06888cf6c307902891)

关系抽取的其他问题：远监督噪音，文档级抽取，开放域关系抽取

1.2.3 事件抽取从文本中抽取出预定义的事件触发词和事件要素

可以拆成关系抽取

1.3 实践：实体关系抽取 对于每个 token，根据其在实体span中的位置（包括B、I、O三种），我们为其打上三类标签，并且根据其所参与构建的predicate种类，将 B 标签进一步区分。给定 schema 集合，对于 N 种不同 predicate，以及头实体/尾实体两种情况，共 2N 种 B 标签，再合并 I 和 O 标签，故每个 token 一共有 (2N+2) 个标签，如下图所示。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=25fb7acbc47c81c8f497a6d42fbab22a)

二、情感分析技术与应用2.1 定义对带有感情色彩的主观性文本进行分析分类

应用：电商评论分析、舆情分析、

难点：不同实体同一描述分类不同、反讽、网络新词

2.2 技术发展脉络词级情感分析词级别的情感分析，即构建情感词典。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=0efe888c68962a9158063b6318093533)

构建情感词典常见的方法包括人工标注和自动化方法

基于点互信息的方法：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=1f4e0bb6decf920a46bd30f79c292f7c)

基于标签传播的方法：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=daa774bb0fefcc9b110d064a9cd6febd)

句子/篇章级情感分析主要经历了三个阶段：基于规则的方法、传统机器学习、深度学习的方法

传统机器学习的方法：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=8abdde77e8eda1e46bfba633d0b01d34)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=540955868ed2e23036af48525e6478ff)

深度学习的方法：

①

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=d2dd391d1d4cac5fe2b9895e32993425)

模型结构：卷积层+池化层+全连接层（FC）

模型特点：权值共享 表达能力更强（ngram特征）

②

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e16bdaac328b28f11a3f774c42497636)

模型结构：正向LSTM+反向LSTM+全连接层

模型特点：权值共享 序列建模能力更强

目标级情感分析给定评价对象的情感分析、评价对象、情感联合抽取

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e061facb694bbf51da5a57c285cd442a)

模型结构 ：双向LSTM+target嵌入表示 +attention结构

模型特点：学习target相关的语义表示 序列建模能力强

2.3 基于预训练的情感分析SKEP：基于情感知识增强的预训练

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=2e29c80cf55c352aa48539cb1584e16c)

一些公开数据集：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c87de54718f8349eb2702a50a979f16d)

2.4 实践：文本情感分析https://aistudio.baidu.com/aistudio/projectdetail/2076560?channelType=0&channel=0



