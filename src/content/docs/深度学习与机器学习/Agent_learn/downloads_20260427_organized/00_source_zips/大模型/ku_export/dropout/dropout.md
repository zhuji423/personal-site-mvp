---
title: "dropout"
description: "在神经网络中Dropout通过修改神经网络本身结构来实现，对于某一层的神经元，通过定义的概率将神经元置为0，这个神经元就不参与前向和后向传播，就如同在网络中被删除了一样，同时保持输入层与输出层神经元的个数不变，然后按照神经网络的学习方法进行"
date: "2026-10-11"
category: "深度学习与机器学习"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\dropout\\dropout.md"
---
# dropout
引入Dropout主要是为了防止过拟合。

在神经网络中Dropout通过修改神经网络本身结构来实现，对于某一层的神经元，通过定义的概率将神经元置为0，这个神经元就不参与前向和后向传播，就如同在网络中被删除了一样，同时保持输入层与输出层神经元的个数不变，然后按照神经网络的学习方法进行参数更新。在下一次迭代中，又重新随机删除一些神经元（置为0），直至训练结束。
Dropout应该算是AlexNet中一个很大的创新，现在神经网络中的必备结构之一。Dropout也可以看成是一种模型组合，每次生成的网络结构都不一样，通过组合多个模型的方式能够有效地减少过拟合，Dropout只需要两倍的训练时间即可实现模型组合（类似取平均）的效果，非常高效。
如下图：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e77dcb25cbd9414db8be8065f3c51374&docGuid=eyB5_W_R6y96T_)



