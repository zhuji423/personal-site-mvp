---
title: "Bert系列预训练模型"
description: "CV领域，深度学习的突破在于基于大规模的无监督预训练，然后微调。先基于ImageNet搞出个预训练模型，然后再在不同任务上的小规模数据上微调。"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\Bert系列预训练模型\\Bert系列预训练模型.md"
---
# Bert系列预训练模型
一、背景NLP中预训练模型的发展历史NLP领域，可以回溯到Word2vec和GloVe统治的时代，主要是得到词向量矩阵，然后用于深度学习模型的初始化。当然，第二代PTMs就保留了整体的模型，代表性的突破应该囊括ELMo, GPT, 和BERT这几类。

CV领域，深度学习的突破在于基于大规模的无监督预训练，然后微调。先基于ImageNet搞出个预训练模型，然后再在不同任务上的小规模数据上微调。

预训练模型的优势NLP任务：缺乏大规模人工标注的数据，但是有超大规模的文本库。

优势：

基于大规模文本库的预训练可以很好的学习到通用的语言表示，有助于下游应用任务；提供更好的模型初始化方法，从而得到具有更好泛化能力的模型，并且加速目标任务的收敛速度；可以被看成一种正则化方法，防止模型在小规模标注数据上过拟合。GPT与BERT区别

bert是双向的，属于自编码模型

gpt是单向，更适合文本生成，属于自回归模型

![](/personal-site-mvp/img/doc-placeholder.svg)

二、BERT详细分析论文链接：BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

BERT，Bidirectional Encoder Representation from Transformers，其Encoder由双向Transformer构成。模型的主要创新点都在pre-train方法上，即用了Masked LM和Next Sentence Prediction两种方法分别捕捉词语和句子级别的representation。

BERT模型的结构：

![](/personal-site-mvp/img/doc-placeholder.svg)

对比OpenAI GPT(Generative pre-trained transformer)，BERT是双向的Transformer block连接，能更好的关注到上下文信息；对比ELMo，虽然都是双向的，但是Bert采用Transformer抽取特征效果要优于ELMo采用LSTM抽取特征。

Bert的输入由三种Embedding组成：

![](/personal-site-mvp/img/doc-placeholder.svg)

其中：

Token Embeddings是词向量，第一个单词是CLS标志，可以用于之后的分类任务Segment Embeddings用来区别两种句子，用于Pre-train中的分类任务Pre-train任务主要有两个，其一是Masked LM，其二是Next Sentence Prediction

论文链接：BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

BERT为什么如此有效？

引入Masked Language Model(MLM)预训练目标，能够获取上下文相关的双向特征表示；引入Next Sentence Prediction(NSP)预训练目标，擅长处理句子或段落的匹配任务；引入强大的特征抽取机制Transformer(多种机制并存)：Multi-Head self attention：多头机制类似于“多通道”特征抽取，self attention通过attention mask动态编码变长序列，解决长距离依赖（无位置偏差）、可并行计算；Feed-forward ：在位置维度计算非线性层级特征；Layer Norm & Residuals：加速训练，使“深度”网络更加健壮；引入大规模、高质量的文本数据；transformer详细介绍： 

2.1 预训练任务MLM: 掩码语言模型Masked LM 此任务预训练的目标就是语言模型，在训练过程中作者随机mask 15%的token，而不是把像cbow一样把每个词都预测一遍。最终的损失函数只计算被mask掉的那个token。

NSP:下句预测Next Sentence Prediction 因为涉及到QA和NLI之类的任务，增加了第二个预训练任务，目的是让模型理解两个句子之间的联系。训练的输入是句子A和B，B有一半的几率是A的下一句，输入这两个句子，模型预测B是不是A的下一句。预训练的时候可以达到97-98%的准确度。

注：语料的选取很关键，要选用document-level的而不是sentence-level的，这样可以具备抽象连续长序列特征的能力。

2.2 finetuning微调任务通过调整模型的输入输出部分，Bert模型可实现在不同的任务上进行fine-tune。

单句子分类：CLS+句子。利用CLS进行分类多句子分类：CLS+句子A+SEP+句子B。利用CLS分类SQuAD：CLS+问题+SEP+文章。利用所有文章单词的输出做计算start和endNER：CLS+句子。利用句子单词做标记![](/personal-site-mvp/img/doc-placeholder.svg)

2.3 代码实现可参考：

三、BERT系列模型改进| 优化方向 | 项目 | 详情 | 备注 |
| --- | --- | --- | --- |
| 改进【生成任务】 | MASS(微软) | 统一预训练框架:通过类似的Seq2Seq框架，在预训练阶段统一了BERT和LM模型；Encoder中理解unmasked tokens；Decoder中需要预测连续的[mask]tokens，获取更多的语言信息；Decoder从Encoder中抽取更多信息；当k=1或者n时，MASS的概率形式分别和BERT中的MLM以及GPT中标准的LM一致（k为mask的连续片段长度）） | 论文：https://arxiv.org/pdf/1905.02450.pdf代码：https://github.com/microsoft/MASS详读： |
|  | UNILM (微软) | 统一预训练框架:和直接从mask矩阵的角度统一BERT和LM；3个Attention Mask矩阵：LM、MLM、Seq2Seq LM； | 论文：https://arxiv.org/pdf/1905.03197.pdf详读：注意：UNILM中的LM并不是传统的LM模型，仍然是通过引入[MASK]实现的； |
| 引入【知识】 | ERNIE 1.0 (百度) | 在预训练阶段引入知识（实际是预先识别出的实体），引入3种[MASK]策略预测：Basic-Level Masking：跟BERT一样，对subword进行mask，无法获取高层次语义；Phrase-Level Masking：mask连续短语；Entity-Level Masking：mask实体； | 论文：https://arxiv.org/pdf/1904.09223.pdf |
|  | ERNIE (THU) | 基于BERT预训练原生模型，将文本中的实体对齐到外部的知识图谱，并通过知识嵌入得到实体向量作为ERNIE的输入；引入改进的预训练目标 Denoising entity auto-encoder (DEA)：要求模型能够根据给定的实体序列和文本序列来预测对应的实体； | 论文：https://arxiv.org/pdf/1905.07129v3.pdf由于语言表征的预训练过程和知识表征过程有很大的不同，会产生两个独立的向量空间。为解决上述问题，在有实体输入的位置，将实体向量和文本表示通过非线性变换进行融合，以融合词汇、句法和知识信息； |
| 引入【多任务学习机制】 | MTDNN(微软) | 在下游任务中引入多任务学习机制 | 论文：https://arxiv.org/pdf/1901.11504.pdf
代码：https://github.com/namisan/mt-dnn多任务学习(Multi-task Learning)[19]是指同时学习多个相关任务，让这些任务在学习过程中共享知识，利用多个任务之间的相关性来改进模型在每个任务的性能和泛化能力。多任务学习可以看作是一种归纳迁移学习，即通过利用包含在相关任务中的信息作为归纳偏置(Inductive Bias)来提高泛化能力。 |
|  | ERNIE 2.0 (百度) | 在预训练阶段引入多任务学习主要包含3个方面的任务：word-aware 任务：捕捉词汇层面的信息；structure-aware 任务：捕捉句法层面的信息；semantic-aware 任务：捕捉语义方面的信息；主要的方式是构建增量学习（后续可以不断引入更多的任务）模型，通过多任务学习持续更新预训练模型，这种连续交替的学习范式不会使模型忘记之前学到的语言知识。将3大类任务的若干个子任务一起用于训练，引入新的任务时会将继续引入之前的任务，防止忘记之前已经学到的知识，具体是一个逐渐增加任务数量的过程[22]： (task1)->(task1,task2)->(task1,task2,task3)->…->(task1，task2,…,taskN)， | 论文：https://arxiv.org/pdf/1907.12412v2.pdf |
| 改进【mask策略】 | BERT WWM(Google) | 原生BERT模型：按照subword维度进行mask，然后进行预测；按照whole word维度进行mask，然后进行预测； | 论文：https://arxiv.org/pdf/1906.08101.pdf注意：BERT WWM、ERNIE等系列、SpanBERT旨在隐式地学习预测词（mask部分本身的强相关性）之间的关系[23]，而在 XLNet 中，是通过 PLM 加上自回归方式来显式地学习预测词之间关系； |
|  | ERNIE等系列 | 引入外部知识，按照entity维度进行mask，然后进行预测； |  |
|  | SpanBert | 不需要按照先验的词/实体/短语等边界信息进行mask，而是采取随机mask：采用Span Masking：根据几何分布，随机选择一段空间长度，之后再根据均匀分布随机选择起始位置，最后按照长度mask；通过采样，平均被遮盖长度是3.8 个词的长度；引入Span Boundary Objective：新的预训练目标旨在使被mask的Span 边界的词向量能学习到 Span中被mask的部分；新的预训练目标和MLM一起使用； | 论文：https://arxiv.org/pdf/1908.09091.pdf
代码：https://github.com/facebookresearch/SpanBERT |
| 进行【精细调参】 | RoBERTa(FaceBook) | 丢弃NSP，效果更好；动态改变mask策略，把数据复制10份，然后统一进行随机mask；对学习率的峰值和warm-up更新步数作出调整；在更长的序列上训练：不对序列进行截短，使用全长度序列； | 论文：https://arxiv.org/pdf/1907.11692 |

参考推荐一篇综述：https://arxiv.org/pdf/2302.09419.pdf









