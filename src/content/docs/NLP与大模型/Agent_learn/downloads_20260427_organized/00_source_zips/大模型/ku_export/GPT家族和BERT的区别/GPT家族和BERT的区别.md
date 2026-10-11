---
title: "GPT家族和BERT的区别"
description: "1、自回归与自编码无监督表征学习首先在大规模未标记的文本语料库上预训练神经网络，然后在下游任务中，对这些模型或表示进行finetune。在这种共享的思想中，存在不同的无监督预训练目标。其中，自回归（Autoregressive，简称AR）语"
date: "2026-10-11"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\GPT家族和BERT的区别\\GPT家族和BERT的区别.md"
---
# GPT家族和BERT的区别
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5e38c6e0d9eb41ebb8c24679636a04db&docGuid=yyqg3Add1Rj0cD)

1、自回归与自编码无监督表征学习首先在大规模未标记的文本语料库上预训练神经网络，然后在下游任务中，对这些模型或表示进行finetune。在这种共享的思想中，存在不同的无监督预训练目标。其中，自回归（Autoregressive，简称AR）语言建模和自编码（Autoencoder，简称AE）一直是最成功的两个预训练目标。将此与Transformer架构联系起来，Transformer encoder是一个AE模型，Transformer decoder则是一个AR模型。

蓝色表示Transformer encoder（AE模型），红色表示Transformer decoder（AR模型），灰色表示Transformer Encoder-Decoder（seq2seq模型）。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=79012d004a174cefb060dbde8e3584d3&docGuid=yyqg3Add1Rj0cD)

2、Autoregressive自回归AR模型，代表作GPT，从左往右学习的模型。AR模型从一系列time steps中学习，并将上一步的结果作为回归模型的输入，以预测下一个time step的值。AR模型通常用于生成式任务，在长文本的生成能力很强，比如自然语言生成（NLG）领域的任务：摘要、翻译或抽象问答。

优点：AR模型擅长生成式NLP任务。AR模型使用注意力机制，预测下一个token，因此自然适用于文本生成。此外，AR模型可以简单地将训练目标设置为预测语料库中的下一个token，因此生成数据相对容易。缺点：AR模型只能用于前向或者后向建模，不能同时使用双向的上下文信息，不能完全捕捉token的内在联系。3、Autoencoder自编码AE模型，代表作BERT，它不会进行精确的估计，但却具有从被mask的输入中，重建原始数据的能力，即fill in the blanks（填空）。AE模型通常用于内容理解任务，比如自然语言理解（NLU）中的分类任务：情感分析、提取式问答。

优点：上下文依赖：AR的表示仅仅到位置t之前（比如左边的所有token），BERT的表示可以涵盖前后向两边的上下文。BERT使用双向transformer，在语言理解相关的任务中表现很好。缺点：输入噪声：BERT在预训练过程中使用【mask】符号对输入进行处理，这些符号在下游的finetune任务中永远不会出现，这会导致预训练-微调差异。而AR模型不会依赖于任何被mask的输入，因此不会遇到这类问题。BERT在对联合条件概率进行因式分解时，基于一个独立假设：在给定了unmasked tokens时，所有待预测（masked）的tokens是相互独立的。4、Encoder-Decoder（Seq2seq模型）encoder-decoder模型同时使用编码器和解码器。它将每个task视作序列到序列的转换/生成（比如，文本到文本，文本到图像或者图像到文本的多模态任务）。对于文本分类任务来说，编码器将文本作为输入，解码器生成文本标签。Encoder-decoder模型通常用于需要内容理解和生成的任务，比如机器翻译。

T5、BART和BigBird是Encoder-Decoder模型。





