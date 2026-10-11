---
title: "NLP学习4：问答"
description: "检索式问答：两阶段段落检索→阅读理解"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\NLP学习4：问答\\NLP学习4：问答.md"
---
# NLP学习4：问答
本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间一、检索式文本问答1.1 背景应用：搜索引擎、智能设备、智能客服

检索式问答：两阶段段落检索→阅读理解

1.2 机器阅读理解输入：给定篇章+问题，输出：答案

评估方式：EM、F1score

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=25ab77adc5f3d5278aa06958370e09cb)

1.3 段落

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e9ec0d6cc0015788f126c1c191ac2db6)

理解

基于LSTM+注意力机制

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=9f4cca9d5ed34410551174dfd402bfdc)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=f9414fa295ab9154c164c1dc5ed1f67c)

基于预训练模型![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ea4b57bd3ae6a5e98d4e1c129d151299)

1.3 段落检索检索式问答：

不同于单篇章阅读理解，没有给定文档需要从大规模文档集合中找答案主要分为两步：①从大规模文档中检索得到Top-K段落②从K个候选段落中抽取答案：阅读理解任务

检索模型稀疏向量检索基于词的稀疏表示匹配能力有限，只能捕捉字面匹配不可学习稠密向量检索基于对偶模型结构，进行稠密向量（embedding）表示能够建模语义匹配可学习的文本匹配中的两种模型结构：

对偶式模型结构：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=02351a1df84206ec671e60fa0f237e31)

可用于快速索引问题和段落之间难以交互交互式模型结构：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=335f3cb17d854cf891c3c5a3bd170be2)

推理时计算效率较低问题和段落之间充分交互，模型能力更强经典语义检索模型：DPR（in-batch负采样，数据构造方式）

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=2b2c5f4c1e4a87967174f95729261940)

正样本构造方式：使用BM25算法从wikipedia中检索，top100中匹配答案

负样本选取方式：

Random：从语料中随机抽取BM25：使用BM25检索的不包含答案的段落Gold：训练集中其他问题的答案段落1.4 实践：机器阅读理解https://aistudio.baidu.com/aistudio/projectdetail/2017189?channelType=0&channel=0



数据集：Dureaderrobust数据集







