---
title: "Transformer"
description: "谷歌的Transformer模型最早是用于机器翻译任务，当时达到了SOTA效果。Transformer改进了RNN最被人诟病的训练慢的缺点，利用self-attention机制实现快速并行。并且Transformer可以增加到非常深的深度，"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\Transformer\\Transformer.md"
---
# Transformer
本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间一、背景谷歌团队2018提出的用于生成词向量的BERT算法在NLP的11项任务中取得了非常出色的效果，堪称2018年深度学习领域最振奋人心的消息。而BERT算法又是基于Transformer，Transformer又是基于attention机制。

谷歌的Transformer模型最早是用于机器翻译任务，当时达到了SOTA效果。Transformer改进了RNN最被人诟病的训练慢的缺点，利用self-attention机制实现快速并行。并且Transformer可以增加到非常深的深度，充分发掘DNN模型的特性，提升模型准确率。

二、Transformer结构2.1 整体结构![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=c1bdf66aebcb41a8aa5705db8faa16b6&docGuid=kZyK-SysB9muxw)

2.2 Transformer的inputs 输入![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=6c1df3dbcda143ba9262bf4daca0776a&docGuid=kZyK-SysB9muxw)

Transformer输入是一个序列数据，以"Tom chase Jerry" 翻译成中文"汤姆追逐杰瑞"为例：

Encoder 的 inputs就是"Tom chase Jerry" 分词后的词向量。可以是任意形式的词向量，如word2vec，GloVe，one-hot编码。

positional encoding在输入的时候需要给每一个词向量添加位置编码，获取词语出现在句子中的位置信息。

positional encoding怎么获取：

1.数据训练学习：类似于训练学习词向量，如goole在之后的bert中的positional encoding。

2.使用正余弦位置编码：如《Attention Is All You Need》论文中Transformer。

考虑效率原因，将positional encoding与词向量相加，而不是拼接。

![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=296dd2380dac4b50b05f736348ce8148&docGuid=kZyK-SysB9muxw)

Encoder接受英文"Tom chase Jerry"，Decoder接受中文"汤姆追逐杰瑞"。

只是在有target数据时也就是在进行有监督训练时才会接受Outputs Embedding，进行预测时则不会接收。

2.3 Transformer Encoder![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=9d4acd32e19242d192ac4704226a36f5&docGuid=kZyK-SysB9muxw)

Encoder block是由6个encoder堆叠而成，N=6。

一个encoder由Multi-Head Attention 和 全连接神经网络Feed Forward Network构成。

（1）Multi-Head Attentionself-attention假如输入序列是"Thinking Machines"，x1，x2就是对应地"Thinking"和"Machines"添加过位置编码之后的词向量，然后词向量通过三个权值矩阵转变成为计算Attention值所需的Query，Keys，Values向量。

![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=052f6b15a8f3446bb9e81f89c969d383&docGuid=kZyK-SysB9muxw)

X矩阵是由"Tinking"和"Machines"词向量组成的矩阵，通过变换得到Q，K，V。假设词向量是512维，X矩阵的维度是(2,512)，W均是(512,64)维，得到的Query，Keys，Values就都是(2,64)维。

得到Q，K，V之后，计算Attention值：

步骤1： 输入序列中每个单词之间的相关性得分，上篇中说过计算相关性得分可以使用点积法，就是用Q中每一个向量与K中每一个向量计算点积步骤2： 对于输入序列中每个单词之间的相关性得分进行归一化，归一化的目的主要是为了训练时梯度能够稳定。dk就是K的维度dk=64步骤3： 通过softmax函数，将每个单词之间的得分向量转换成[0,1]之间的概率分布，同时更加凸显单词之间的关系。经过softmax后，score转换成一个值分布在[0,1]之间的(2,2)α概率分布矩阵步骤4： 根据每个单词之间的概率分布，然后乘上对应的Values值，α与V进行点积，V的为维度是(2,64)，(2,2)x(2,64)最后得到的Z是(2,64)维的矩阵计算过程：

![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=86b314a44a784b1d912b952ec826c826&docGuid=kZyK-SysB9muxw)

Multi-Head Attentionself-attention只使用了一组权值矩阵来进行变换得到Query，Keys，Values。而Multi-Head Attention使用多组权值矩阵得到多组Query，Keys，Values，然后每组分别计算得到一个Z矩阵，最后将得到的多个Z矩阵进行拼接。Transformer里面是使用了8组。

![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=2d9693fa45c44bbdab1436ed2ec86259&docGuid=kZyK-SysB9muxw)

（2）Add＆Normalize在经过Multi-Head Attention得到矩阵Z之后，并没有直接传入全连接神经网络FNN，而是经过了一步：Add＆Normalize。

AddAdd，就是在Z的基础上加了一个残差块X，加入残差块X的目的是为了防止在深度神经网络训练中发生退化问题。

ResNet 残差神经网络举个例子：假如某个神经网络的最优网络层数是18层，但是在设计的时候并不知道到底多少层是最优解，设计了32层。要想达到18层神经网络的最优效果，必须保证这多出来的14层网络必须进行恒等映射F(x)=x，才能保证这多出来的14层神经网络不会影响最优的效果。

但现实是要想保证训练出来恒等映射h(X)=X是很困难地，ResNet 残差神经网络就是来解决神经网络退化的问题。

残差块：

![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=f945ab3f6af24e71add0bc3dd5b19513&docGuid=kZyK-SysB9muxw)

F(X)是经过第一层线性变化并激活后的输出，该图表示在残差网络中，第二层进行线性变化之后激活之前，F(X)加入了这一层输入值X，然后再进行激活后输出。在第二层输出值激活前加入X，这条路径称作shortcut连接。

h(X)=F(X)+X，我们要让h(X)=X，那么是不是相当于只需要让F(X)=0就可以了，这里巧妙用学习残差F(x)=0更新该冗余层的参数来代替学习h(x)=x。因为初始化神经网络的参数的时候就是设置的[0,1]之间的随机数，经过网络变换后很容易接近于0。相比与学习h(x)=x，模型要更快到学习F(x)=0。
并且ReLU能够将负数激活为0，过滤了负数的线性变化，也能够更快的使得F(x)=0。



Transformer中加上的X也就是Multi-Head Attention的输入，X矩阵。

Normalize在神经网络进行训练之前，都需要对于输入数据进行Normalize归一化，目的有二：1，能够加快训练的速度。2.提高训练的稳定性。

为什么使用Layer Normalization（LN）而不使用Batch Normalization（BN）：

LN是在同一个样本中不同神经元之间进行归一化，而BN是在同一个batch中不同样本之间的同一位置的神经元之间进行归一化。

BN是对于相同的维度进行归一化，但是NLP中输入的都是词向量，一个300维的词向量，单独去分析它的每一维是没有意义地，在每一维上进行归一化也是适合地，因此这里选用的是LN。

![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=9e65803fd43a40a5a07ad15760f27c64&docGuid=kZyK-SysB9muxw)

（3）Feed-Forward Networks全连接层公式：

![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=77c38391e07a4eb6b9fe3780ccd2dd51&docGuid=kZyK-SysB9muxw)

这里的全连接层是一个两层的神经网络，先线性变换，然后ReLU非线性，再线性变换。

这里的x就是Multi-Head Attention的输出Z，引用上面的例子Z是(2,64)维的矩阵，假设W1是(64,1024)，其中W2与W1维度相反(1024,64)，那么按照上面的公式：

FFN(Z)=(2,64)x(64,1024)x(1024,64)=(2,64)，维度没有发生变化，这两层网络就是为了将输入的Z映射到更加高维的空间中(2,64)x(64,1024)=(2,1024)，然后通过非线性函数ReLU进行筛选，筛选完后再变回原来的维度。



然后经过Add＆Normalize，输入下一个encoder中，经过6个encoder后输入到decoder中。

2.4 Transformer Decoder![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=87db8208e55d47a3bf13402c6f086e3d&docGuid=kZyK-SysB9muxw)

Decoder block也是由6个decoder堆叠而成，N=6。灰框部分是一个decoder的内部结构，一个decoder由Masked Multi-Head Attention，Multi-Head Attention 和 全连接神经网络FNN构成。

比Encoder多了一个Masked Multi-Head Attention，其他的结构与encoder相同。

（1）Masked Multi-Head Attention与Encoder的Multi-Head Attention计算原理一样，只是多加了一个mask码。mask 表示掩码，它对某些值进行掩盖，使其在参数更新时不产生效果。Transformer 模型里面涉及两种 mask，分别是 padding mask 和 sequence mask。

1.padding mask

要对输入序列进行对齐：给在较短的序列后面填充 0、序列太长则截取内容。不应该把注意力放在填充的位置上，把这些位置的值加上一个非常大的负数(负无穷)，经过 softmax，这些位置的概率就会接近0。

2.sequence mask

sequence mask 是为了使得 decoder 不能看见未来的信息。对于一个序列，在 time_step 为 t 的时刻，解码输出应该只能依赖于 t 时刻之前的输出，而不能依赖 t 之后的输出。做法：产生一个上三角矩阵，上三角的值全为0。



在Encoder中的Multi-Head Attention也是需要进行mask地，只不过Encoder中只需要padding mask即可，而Decoder中需要padding mask和sequence mask。

Encoder中的Multi-Head Attention是基于Self-Attention地，Decoder中的第二个Multi-Head Attention就只是基于Attention，它的输入Quer来自于Masked Multi-Head Attention的输出，Keys和Values来自于Encoder中最后一层的输出。



经过了第二个Multi-Head Attention之后的Feed Forward Network与Encoder中一样，然后进入下一个decoder，如此经过6层decoder之后到达最后的输出层。

2.5 Transformer的输出![](https://ku.baidu-int.com/wiki/attach/image/api/imageDownloadAddress?attachId=ee90b7a256d745e0852f0f045471514c&docGuid=kZyK-SysB9muxw)

首先经过一次线性变换，然后Softmax得到输出的概率分布，然后通过词典，输出概率最大的对应的单词作为预测输出。

三、优缺点优点：
1.效果好
2.可以并行训练，速度快
3.很好地解决了长距离依赖的问题
缺点：
1.完全基于self-attention，对于词语位置之间的信息有一定的丢失，虽然加入了positional encoding来解决这个问题，但也还存在着可以优化的地方。

四、应用

五、其他1、Transformer的整体架构是怎样的？由哪些部分组成？

2、Transformer Encoder 与 Transformer Decoder 有哪些不同？

3、Encoder-Decoder attention 与self-attention mechanism有哪些不同？

4、multi-head self-attention mechanism具体的计算过程是怎样的？

5、Transformer在GPT和Bert等词向量预训练模型中具体是怎么应用的？有什么变化？



附录：

Attention is All You Need

BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding



nlp中的Attention注意力机制+Transformer详解

图解Transformer（完整版）

https://blog.csdn.net/Tink1995/article/details/105080033

