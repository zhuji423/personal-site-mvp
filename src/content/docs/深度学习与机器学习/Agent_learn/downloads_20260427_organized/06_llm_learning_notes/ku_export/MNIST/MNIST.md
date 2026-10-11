---
title: "MNIST"
description: "MNIST数据库是非常经典的一个数据集，就像你学编程起初写一个“Hello Word”的程序一样，学Deep Learning你就会写识别MNIST数据集的Model。"
date: "2026-04-28"
category: "深度学习与机器学习"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\MNIST\\MNIST.md"
---
# MNIST
数据集介绍MNIST数据集官网：http://yann.lecun.com/exdb/mnist/

MNIST数据库是非常经典的一个数据集，就像你学编程起初写一个“Hello Word”的程序一样，学Deep Learning你就会写识别MNIST数据集的Model。

MNIST数据集是由0〜9手写数字图片和数字标签所组成的，由60000个训练样本和10000个测试样本组成，每个样本都是一张28 * 28像素的灰度手写数字图片。MNIST数据库一共有四个文件案，分别为：

1. train-images-idx3-ubyte.gz：训练集图片（9912422字节），55000张训练集，5000张验证集

2. train-labels-idx1-ubyte.gz：训练集图片对应的标签（28881字节），

3. t10k-images-idx3-ubyte .gz：测试集图片（1648877字节），10000张图片

4. t10k-labels-idx1-ubyte.gz：测试集图片对应的标签（4542字节）

图片是指0〜9手写数字图片，而标签则是对应该图片之实际数字。

网络结构1、全连接神经网络经典的全连接神经网络来包含四层网络：输入层、两个隐含层和输出层。

![](/personal-site-mvp/img/doc-placeholder.svg)

输入层：将数据输入给神经网络。在该任务中，输入层的尺度为28×28的像素值。隐含层：增加网络深度和复杂度，隐含层的节点数是可以调整的，节点数越多，神经网络表示能力越强，参数量也会增加。在该任务中，中间的两个隐含层为10×10的结构，通常隐含层会比输入层的尺寸小，以便对关键信息做抽象，激活函数使用常见的Sigmoid函数。输出层：输出网络计算结果，输出层的节点数是固定的。如果是回归问题，节点数量为需要回归的数字数量。如果是分类问题，则是分类标签的数量。在该任务中，模型的输出是回归一个数字，输出层的尺寸为1。2、卷积神经网络卷积神经网络由多个卷积层和池化层组成。卷积层负责对输入进行扫描以生成更抽象的特征表示，池化层对这些特征表示进行过滤，保留最关键的特征信息。

![](/personal-site-mvp/img/doc-placeholder.svg)



