---
title: "IMDB评论情感识别"
description: "def download: 通过python的requests类，下载存储在 https://dataset.bj.bcebos.com/imdb%2FaclImdbv1.tar.gz的文件 corpusurl = \"https://dat"
date: "2026-04-28"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\IMDB评论情感识别\\IMDB评论情感识别.md"
---
# IMDB评论情感识别
数据集介绍IMDB的电影评论数据是一个开源的英文数据集，由训练数据和测试数据组成。每个数据都分别由若干小文件组成，每个小文件内部都是一段用户关于某个电影的真实评价，以及观众对这个电影的情感倾向（是正向还是负向），数据集下载的代码如下：

def download():# 通过python的requests类，下载存储在# https://dataset.bj.bcebos.com/imdb%2FaclImdb_v1.tar.gz的文件    corpus_url = "https://dataset.bj.bcebos.com/imdb%2FaclImdb_v1.tar.gz"    web_request = requests.get(corpus_url)    corpus = web_request.content    # 将下载的文件写在当前目录的aclImdb_v1.tar.gz文件内    with open("./aclImdb_v1.tar.gz", "wb") as f:        f.write(corpus)    f.close()download()网络结构1、循环神经网络RNN循环神经网络的输入是一个序列信息。假设给定任意一句话[x0,x1,...,xn]，其中每个xi都代表了一个词，如“我，爱，人工，智能”。循环神经网络从左到右逐词阅读这个句子，并不断调用一个相同的RNN Cell来处理时序信息。每阅读一个单词，循环神经网络会先将本次输入的单词通过embedding lookup转换为一个向量表示。再把这个单词的向量表示和这个模型内部记忆的向量hh融合起来，形成一个更新的记忆。最后将这个融合后的表示输出出来，作为它当前阅读到的所有内容的语义表示。当循环神经网络阅读过整个句子之后，我们就可以认为它的最后一个输出状态表示了整个句子的语义信息。

![](/personal-site-mvp/img/doc-placeholder.svg)

循环神经网络开始从左到右阅读这个句子，在未经过任何阅读之前，循环神经网络中的记忆向量是空白的。其处理逻辑如下：

网络阅读单词“我”，并把单词“我”的向量表示和空白记忆相融合，输出一个向量h1，用于表示“空白+我”的语义。网络开始阅读单词“爱”，这时循环神经网络内部存在“空白+我”的记忆。循环神经网络会将“空白+我”和“爱”的向量表示相融合，并输出“空白+我+爱”的向量表示h2，用于表示“我爱”这个短语的语义信息。网络开始阅读单词“人工”，同样经过融合之后，输出“空白+我+爱+人工”的向量表示h3，用于表示“空白+我+爱+人工”语义信息。最终在网络阅读了“智能”单词后，便可以输出“我爱人工智能”这一句子的整体语义信息。

在实现当前输入xtxt​和已有记忆ht−1融合的时候，循环神经网络采用相加并通过一个激活函数tanh的方式实现：

![](/personal-site-mvp/img/doc-placeholder.svg)

tanh函数是一个值域为（-1,1）的函数，其作用是长期维持内部记忆在一个固定的数值范围内，防止因多次迭代更新导致数值爆炸。同时tanh的导数是一个平滑的函数，会让神经网络的训练变得更加简单。

2、长短时记忆网络LSTM当阅读很长的序列时，网络内部的信息会变得越来越复杂，甚至会超过网络的记忆能力，使得最终的输出信息变得混乱无用。长短时记忆网络（Long Short-Term Memory，LSTM）内部的复杂结构正是为处理这类问题而设计的。

![](/personal-site-mvp/img/doc-placeholder.svg)

与RNN区别：

长短时记忆网络的结构和循环神经网络非常类似，都是通过不断调用同一个cell来逐次处理时序信息。每阅读一个新单词xt，就会输出一个新的输出信号ht，用来表示当前阅读到所有内容的整体向量表示。不过二者又有一个明显区别，长短时记忆网络在不同cell之间传递的是两个记忆信息，而不像循环神经网络一样只有一个记忆信息，此外长短时记忆网络的内部结构也更加复杂。

遗忘机制：

长短时记忆网络最大的特点是在更新内部记忆时，引入了遗忘机制。即容许网络忘记过去阅读过程中看到的一些无关紧要的信息，只保留有用的历史信息。

输入门：控制有多少输入信号会被融合；遗忘门：控制有多少过去的记忆会被遗忘；输出门：控制多少处理后的信息会被输出；长短时记忆网络的Cell有三个输入：

![](/personal-site-mvp/img/doc-placeholder.svg)

得到这两个信号之后，长短时记忆网络没有立即去融合这两个向量，而是计算了权重。

![](/personal-site-mvp/img/doc-placeholder.svg)

通过学习这些门的权重设置，长短时记忆网络可以根据当前的输入信号和记忆信息，有选择性地忽略或者强化当前的记忆或是输入信号，帮助网络更好地学习长句子的语义信息：

![](/personal-site-mvp/img/doc-placeholder.svg)





