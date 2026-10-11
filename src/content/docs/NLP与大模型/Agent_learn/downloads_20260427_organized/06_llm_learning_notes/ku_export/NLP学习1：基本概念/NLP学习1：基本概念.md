---
title: "NLP学习1：基本概念"
description: "- 好评/差评判别、情感分析、舆情分析"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\NLP学习1：基本概念\\NLP学习1：基本概念.md"
---
# NLP学习1：基本概念
本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间一、背景1.1 场景- 分词、词性标注、命名实体识别

- 好评/差评判别、情感分析、舆情分析

- 快递单信息自动识别

- 搜索

- 智能问答和对话

- 机器同传

二、基础概念2.1 词向量字、词计算机中两种表示方式：one-hot表示和分布式表示

one-hot表示：把每个词表示为一个长向量。这个向量的维度是词表大小，向量中只有一个维度的值为1，其余维度为0，这个维度就代表了当前的词。 例如：苹果 [0,0,0,1,0,0,0,0,···] 。one-hot表示不能展示词与词之间的关系，且特征空间非常大。embedding表示：word embedding指的是将词转化成一种分布式表示，又称词向量。分布式表示将词表示成一个定长的连续的稠密向量。优点:(1)词之间存在相似关系；(2)词向量能够包含更多信息，并且每一维都有特定的含义。不能对特征向量进行删减。2.1.1 word2vec2013年，Mikolov提出的经典word2vec算法通过上下文来学习语义信息。word2vec包含两个经典模型：CBOW（Continuous Bag-of-Words）和Skip-gram：

CBOW：通过上下文的词向量推理中心词。Skip-gram：根据中心词推理上下文。![](/personal-site-mvp/img/doc-placeholder.svg)

举个例子，句子“Pineapples are spiked and yellow”：两者都是先在句子中选定一个中心词，并把其它词作为这个中心词的上下文。把“spiked”作为中心词，把“Pineapples、are、and、yellow”作为中心词的上下文。

CBOW：使用上下文的词向量推理中心词，这样中心词的语义就被传递到上下文的词向量中，如“spiked → pineapple”，从而达到学习语义信息的目的。Skip-gram：使用中心词的词向量去推理上下文，这样上下文定义的语义被传入中心词的表示中，如“pineapple → spiked”， 从而达到学习语义信息的目的。论文：Efficient Estimation of Word Representations in Vector Space

2.1.2 预训练词向量word2vec之后，涌现了更多word embedding方式，如Glove、fasttext、ElMo等。如今，已有很多预训练完成的词向量，可直接调用使用，用来初始化，可提升简单网络的收敛速度、精度。

代码链接：https://github.com/PaddlePaddle/PaddleNLP/tree/develop/paddlenlp/embeddings

2.2 RNN和CNN网络CNN卷积神经网络

RNN/LSTM/GRU 循环神经网络

在RNN中，目前使用最广泛的模型便是LSTM(Long Short-Term Memory，长短时记忆模型)模型，该模型能够更好地建模长序列。除RNN外，卷积神经网络（Convolutional Neural Networks，简称CNN）也被用来对文本进行建模。

2.3 TransformerTransformer中抛弃了传统的CNN和RNN，整个网络结构完全是由Attention机制组成。更准确地讲，Transformer由且仅由Self-Attenion和Feed Forward Neural Network组成。只要计算资源够，可以通过堆叠多层Transformer来搭建复杂网络。

考虑到RNN（或者LSTM，GRU等）类模型只能从左向右依次计算或者从右向左依次计算，带来了一定的局限性：

时刻t的计算依赖t−1时刻的计算结果，这样限制了模型的并行能力；顺序计算的过程中信息会丢失，尽管LSTM等门机制的结构一定程度上缓解了长期依赖的问题，但是对于特别长期的依赖现象，LSTM依旧无能为力。Transformer的提出解决了上面两个问题:

使用了Attention机制，将序列中的任意两个位置之间的距离缩小为一个常量；无需依次输入序列信息，因此具有更好的并行性，符合现有的GPU框架。![](/personal-site-mvp/img/doc-placeholder.svg)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=777a6312c6986a3b3b91b7d898dc669b)

网络由若干相同的layer 堆叠组成，每个layer主要由多头注意力（Multi-Head Attention）和全连接的前馈（Feed-Forward）网络这两个 sub-layer 构成。

Multi-Head Attention 用于实现 Self-Attention，相比于简单的 Attention 机制，其将输入进行多路线性变换后分别计算 Attention 的结果，并将所有结果拼接后再次进行线性变换作为输出。Feed-Forward 网络会对序列中的每个位置进行相同的计算（Position-wise），其采用的是两次线性变换中间加以 ReLU 激活的结构。此外，每个 sub-layer 后还施以 Residual Connection 和 Layer Normalization 来促进梯度传播和模型收敛。

关于Transformer的理解：http://jalammar.github.io/illustrated-transformer/

2.4 预训练模型Transformer结构的出现催生了众多高质量的预训练模型。2018年开始，以BERT为代表的语义表示预训练模型取得了巨大突破，横扫各大NLP任务基准，带来了预训练+细调的NLP技术变革，该技术逐渐成为突破AI认知技术的关键性技术。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=5285256f1183ede24b4cc81dd6d7c62c)

2.4.1 BERTBERT，Bidirectional Encoder Representation from Transformers，其Encoder由双向Transformer构成。模型的主要创新点都在pre-train方法上，即用了Masked LM和Next Sentence Prediction两种方法分别捕捉词语和句子级别的representation。

BERT模型的结构：

![](/personal-site-mvp/img/doc-placeholder.svg)

对比OpenAI GPT(Generative pre-trained transformer)，BERT是双向的Transformer block连接，能更好的关注到上下文信息；对比ELMo，虽然都是双向的，但是Bert采用Transformer抽取特征效果要优于ELMo采用LSTM抽取特征。

Bert的输入由三种Embedding组成：

![](/personal-site-mvp/img/doc-placeholder.svg)

其中：

Token Embeddings是词向量，第一个单词是CLS标志，可以用于之后的分类任务Segment Embeddings用来区别两种句子，用于Pre-train中的分类任务Pre-train任务主要有两个，其一是Masked LM，其二是Next Sentence Prediction：

Masked LM

此任务预训练的目标就是语言模型，在训练过程中作者随机mask 15%的token，而不是把像cbow一样把每个词都预测一遍。最终的损失函数只计算被mask掉的那个token。

Next Sentence Prediction

因为涉及到QA和NLI之类的任务，增加了第二个预训练任务，目的是让模型理解两个句子之间的联系。训练的输入是句子A和B，B有一半的几率是A的下一句，输入这两个句子，模型预测B是不是A的下一句。预训练的时候可以达到97-98%的准确度。

注：语料的选取很关键，要选用document-level的而不是sentence-level的，这样可以具备抽象连续长序列特征的能力。

通过调整模型的输入输出部分，Bert模型可实现在不同的任务上进行fine-tune。

单句子分类：CLS+句子。利用CLS进行分类多句子分类：CLS+句子A+SEP+句子B。利用CLS分类SQuAD：CLS+问题+SEP+文章。利用所有文章单词的输出做计算start和endNER：CLS+句子。利用句子单词做标记![](/personal-site-mvp/img/doc-placeholder.svg)

论文链接：BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

2.4.2 ERNIE传统的pre-training 模型主要基于文本中words 和 sentences 之间的共现进行学习，事实上，训练文本数据中的词法结构、语法结构、语义信息也同样是很重要的。命名实体识别中人名、机构名、组织名等名词包含的概念信息对应了词法结构，句子之间的顺序对应了语法结构，文章中的语义相关性对应了语义信息。ERNIE 还可以在大型数据集合中进行增量训练。

论文链接：ERNIE: Enhanced Language Representation with Informative Entities

2.5 深度学习任务流程数据集准备- 数据处理- 组网 - 模型训练&评估 - 模型预测&部署

以句子分类为例，NLP任务数据处理通用流程：

![](/personal-site-mvp/img/doc-placeholder.svg)



