---
title: "NLP学习2：基础应用"
description: "1.1 加载TokenEmbedding安装 pip install --upgrade paddlenlp -i https://pypi.org/simple"
date: "2026-10-11"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\NLP学习2：基础应用\\NLP学习2：基础应用.md"
---
# NLP学习2：基础应用
本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间一、词向量词向量（Word embedding），即把词语表示成实数向量。“好”的词向量能体现词语直接的相近关系。词向量已经被证明可以提高NLP任务的性能，例如语法分析和情感分析。

1.1 加载TokenEmbedding安装 pip install --upgrade paddlenlp -i https://pypi.org/simple

TokenEmbedding()参数

embedding_name 将模型名称以参数形式传入TokenEmbedding，加载对应的模型。默认为w2v.baidu_encyclopedia.target.word-word.dim300的词向量。unknown_token 未知token的表示，默认为[UNK]。unknown_token_vector 未知token的向量表示，默认生成和embedding维数一致，数值均值为0的正态分布向量。extended_vocab_path 扩展词汇列表文件路径，词表格式为一行一个词。如引入扩展词汇列表，trainable=True。trainable Embedding层是否可被训练。True表示Embedding可以更新参数，False为不可更新。默认为True。from paddlenlp.embeddings import TokenEmbedding# 初始化TokenEmbedding， 预训练embedding未下载时会自动下载并加载数据token_embedding = TokenEmbedding(embedding_name="w2v.baidu_encyclopedia.target.word-word.dim300")# 查看token_embedding详情print(token_embedding)1.1.1 Embedding使用TokenEmbedding.search() 获得指定词汇的词向量

test_token_embedding = token_embedding.search("中国")print(test_token_embedding)TokenEmbedding.cosine_sim() 计算词向量间余弦相似度

语义相近的词语余弦相似度更高，说明预训练好的词向量空间有很好的语义表示能力。

score1 = token_embedding.cosine_sim("女孩", "女人")score2 = token_embedding.cosine_sim("女孩", "书籍")print('score1:', score1)print('score2:', score2)![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c88bd3bb55fec1082967cae3ac4afc15)

1.1.2 词向量映射到低维空间安装 pip install --upgrade visualdl

# 获取词表中前1000个单词labels = token_embedding.vocab.to_tokens(list(range(0, 1000)))# 取出这1000个单词对应的Embeddingtest_token_embedding = token_embedding.search(labels)# 引入VisualDL的LogWriter记录日志from visualdl import LogWriterwith LogWriter(logdir='output/token_hidi') as writer:    writer.add_embeddings(tag='test', mat=[i for i in test_token_embedding], metadata=labels)运行Python代码之后，在终端上输入：

1.2 基于TokenEmbedding衡量句子语义相似度使用词袋模型（Bag of Words，简称BoW）计算句子的语义向量：

将两个句子分别进行切词，并在TokenEmbedding中查找相应的单词词向量（word embdding）。根据词袋模型，将句子的word embedding叠加作为句子向量（sentence embedding）。计算两个句子向量的余弦相似度。1.2.1 基于TokenEmbedding的词袋模型使用BoWEncoder搭建一个BoW模型用于计算句子语义。

import paddleimport paddle.nn as nnimport paddlenlpclass BoWModel(nn.Layer):    def __init__(self, embedder):        super().__init__()        self.embedder = embedder        emb_dim = self.embedder.embedding_dim        self.encoder = paddlenlp.seq2vec.BoWEncoder(emb_dim)        self.cos_sim_func = nn.CosineSimilarity(axis=-1)    def get_cos_sim(self, text_a, text_b):        text_a_embedding = self.forward(text_a)        text_b_embedding = self.forward(text_b)        cos_sim = self.cos_sim_func(text_a_embedding, text_b_embedding)        return cos_sim    def forward(self, text):        # Shape: (batch_size, num_tokens, embedding_dim)        embedded_text = self.embedder(text)        # Shape: (batch_size, embedding_dim)        summed = self.encoder(embedded_text)        return summedmodel = BoWModel(embedder=token_embedding)1.2.2 构造Tokenizer使用TokenEmbedding词表构造Tokenizer。

from data import Tokenizertokenizer = Tokenizer()tokenizer.set_vocab(vocab=token_embedding.vocab)data.py

import numpy as npimport jiebaimport paddlefrom collections import defaultdictfrom paddlenlp.data import JiebaTokenizer, Pad, Stack, Tuple, Vocabclass Tokenizer(object):    def __init__(self):        self.vocab = {}        self.tokenizer = jieba        self.vocab_path = 'vocab.txt'        self.UNK_TOKEN = '[UNK]'        self.PAD_TOKEN = '[PAD]'    def set_vocab(self, vocab):        self.vocab = vocab        self.tokenizer = JiebaTokenizer(vocab)    def build_vocab(self, sentences):        word_count = defaultdict(lambda: 0)        for text in sentences:            words = jieba.lcut(text)            for word in words:                word = word.strip()                if word.strip() != '':                    word_count[word] += 1        word_id = 0        for word, num in word_count.items():            if num < 5:                continue            self.vocab[word] = word_id            word_id += 1        self.vocab[self.UNK_TOKEN] = word_id        self.vocab[self.PAD_TOKEN] = word_id + 1        self.vocab = Vocab.from_dict(self.vocab,                                     unk_token=self.UNK_TOKEN, pad_token=self.PAD_TOKEN)        # dump vocab to file        self.dump_vocab(self.UNK_TOKEN, self.PAD_TOKEN)        self.tokenizer = JiebaTokenizer(self.vocab)        return self.vocab    def dump_vocab(self, unk_token, pad_token):        with open(self.vocab_path, "w", encoding="utf8") as f:            for word in self.vocab._token_to_idx:                f.write(word + "\n")    def text_to_ids(self, text):        input_ids = []        unk_token_id = self.vocab[self.UNK_TOKEN]        for token in self.tokenizer.cut(text):            token_id = self.vocab.token_to_idx.get(token, unk_token_id)            input_ids.append(token_id)        return input_ids    def convert_example(self, example, is_test=False):        input_ids = self.text_to_ids(example['text'])        if not is_test:            label = np.array(example['label'], dtype="int64")            return input_ids, label        else:            return input_idsdef create_dataloader(dataset,                      trans_fn=None,                      mode='train',                      batch_size=1,                      pad_token_id=0):    """    Creats dataloader.    Args:        dataset(obj:`paddle.io.Dataset`): Dataset instance.        mode(obj:`str`, optional, defaults to obj:`train`): If mode is 'train', it will shuffle the dataset randomly.        batch_size(obj:`int`, optional, defaults to 1): The sample number of a mini-batch.        pad_token_id(obj:`int`, optional, defaults to 0): The pad token index.    Returns:        dataloader(obj:`paddle.io.DataLoader`): The dataloader which generates batches.    """    if trans_fn:        dataset = dataset.map(trans_fn, lazy=True)    shuffle = True if mode == 'train' else False    sampler = paddle.io.BatchSampler(        dataset=dataset, batch_size=batch_size, shuffle=shuffle)    batchify_fn = lambda samples, fn=Tuple(        Pad(axis=0, pad_val=pad_token_id),  # input_ids        Stack(dtype="int64")  # label    ): [data for data in fn(samples)]    dataloader = paddle.io.DataLoader(        dataset,        batch_sampler=sampler,        return_list=True,        collate_fn=batchify_fn)    return dataloader1.2.3 查看相似语句相关度以提供的样例数据text_pair.txt为例，该数据文件每行包含两个句子。

text_pairs = {}with open("input/text_pair", "r", encoding="utf8") as f:    for line in f:        text_a, text_b = line.strip().split("\t")        if text_a not in text_pairs:            text_pairs[text_a] = []        text_pairs[text_a].append(text_b)# 获取句子以及其对应的向量label_list = []embedding_list = []for text_a, text_b_list in text_pairs.items():    text_a_ids = paddle.to_tensor([tokenizer.text_to_ids(text_a)])    embedding_list.append(model(text_a_ids).flatten().numpy())    label_list.append(text_a)    for text_b in text_b_list:        text_b_ids = paddle.to_tensor([tokenizer.text_to_ids(text_b)])        print("text_a: {}".format(text_a))        print("text_b: {}".format(text_b))        print("cosine_sim: {}".format(model.get_cos_sim(text_a_ids, text_b_ids).numpy()[0]))        print()        embedding_list.append(model(text_b_ids).flatten().numpy())        label_list.append(text_b)with LogWriter(logdir='output/sentence_hidi') as writer:    writer.add_embeddings(tag='test', mat=embedding_list, metadata=label_list)

二、预训练语言模型及应用2.1 基于预训练的语义理解技术词向量从海量的无标注语料数据学习通用的语言表示

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=efb8de087d0709d9f37395e6eada5b9c)

CBOW & Skip-Ngram（2013年）

CBOW：基于临近词（上下文）预测词Skip-Ngram：基于词预测临近词（上下文）一般来说，CBOW比Skip-gram训练速度快，训练过程更加稳定，原因是CBOW使用上下文average的方式进行训练，每个训练step会见到更多样本。而在生僻字（出现频率低的字）处理上，skip-gram比CBOW效果更好，原因是skip-gram不会刻意回避生僻字(CBOW结构中输入中存在生僻字时，生僻字会被其它非生僻字的权重冲淡)。

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=1ed0bcdaaa89f2566d9035dc77996078)

应用于下游任务：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=ca8ca4a7b59c01c82852cb464dbfce57)

问题：

上下文无关词向量怎么解决歧义问题过于专注于词本身的解释性和效果：词向量的可解释性(结构和语义)；缺乏对下游应用任务关注；词向量是静态固定的，无法根据上下文语义调整词向量；在下游任务中，其余的模型参数仍然需要重新训练!问题词向量&句向量联合建模Pre-training & Fine-tuning机制Pre-training：在大规模数据集上学习尽可能好的通用表示

Fine-tuning：利用学习好的通用表示初始化下游任务网络

加速收敛减少任务相关监督数据的需求应用典范：基于ImageNet 数据集训练得到的模型（pre-trainedmodel）被广泛应用于其他CV 任务的初始化–通过精细参数微整（fine-tuning）即可实现很好的任务效果。

在nlp领域：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=9170e97de8d091453d62bf1abfb2be9f)

2.2 预训练模型在NLP经典任务的应用2.2.1 ELMoPre-training阶段：

使用Bi-LSTM语言模型建模两层LSTM双向语言模型建模（L->R，R->L）无监督训练，训练数据1BWord![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=6da3ab4d7506d5e2cdb5347b9a86879e)

Fine-tuning阶段:

基于Feature-Based方式Pre-trainingmodel作为纯粹的表示抽取器，表示依赖fine-tuning任务网络结构适配针对特定任务，有若干参数是可学的需要进行任务相关网络结构设计优点：解决了多义词问题，词性也能对应起来

缺点：

不完全双向预训练：模型的前向和后向LSTM两个模型是分别训练的，仅在Loss Function阶段进行了结合。需进行任务相关网络结构设计：每种类型的下游任务都需要进行特定的网络结构设计和搭建仅有词向量，无句向量：ELMo在预训练阶段仅学习了语言模型，无句向量学习任务2.2.2 GPT![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=9bc1d5ac273accb24c2156d0c59cc9bd)

Pre-training阶段：

使用12层TransformerDecoder替换Bi-LSTM更大规模预训练数据：1BWord&BooksCorpus(+0.8billion)Pre-training 目标：

传统语言模型任务（单向）：根据前几个字预测下一个字Transformer结构具备比LSTM更好的文本特征抽取能力

Fine-tuning阶段:

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=b3abc69ba6e9d929c3cf687a6b3c4400)

基于Model-Based方式：Pre-trainingmodel作为任务网络的一部分参与任务学习，新增参数少，网络结构改动小

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=51e2279e44caf04c6bc69cba89a89883)

优点：极大地简化了任务相关网络结构！解决了问题2：需进行任务相关网络结构设计（ELMo）

缺点：

单向预训练：预训练阶段仅采用传统单向语言模型作为训练目标仅有词向量，无句向量：GPT在预训练阶段仅学习了语言模型，无句向量学习任务2.2.3 BERT![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c586a7913b67807a4e66e212181e85a3)

Pre-training阶段：

使用12层TransformerEncoder交互式式双向语言模型建模（LM ->Auto-Encoder）引入sentence-level预训练任务更大规模预训练数据：BooksCorpus+Wikipedia(+2.5billion)Pre-training 目标：

同时训练token-level&sentence-leveltaskMask-LM任务（Mask token）:15%mask概率，在pre-training阶段实现交互式双向Next-sentence句对预测任务：预测当前句的下一句话Mask-LM任务解决了ELMo和GPT中的无交互式双向语言模型的缺点，Next-sentence句对预测任务解决了ELMo和GPT中的无句向量的缺点。

Fine-tuning过程(两种选择)：

Feature-based表示迁移(ELMo) ：Pre-trainingmodel作为纯粹的表示抽取器，表示依赖fine-tuning任务网络结构适配Model-based表示迁移(GPT) ：Pre-trainingmodel作为任务网络的一部分参与任务学习Model-based 更胜一筹：

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=bac2eb66cc67d430a44f06b421e1017c)

2.2.4 ERNIEPre-training阶段：

使用12层TransformerEncoder交互式式双向语言模型建模（LM ->Auto-Encoder）sentence-level预训练任务更大规模预训练数据(百度自建预训练语料库)Pre-training 目标：

同时训练token-level&sentence-leveltaskMask-LM任务（Mask word & entity ）:15%mask概率，在pre-training阶段实现交互式双向Next-sentence句对预测任务：预测当前句的下一句话(与BERT类似)除了mask token改为mask word，感觉跟bert没啥区别。。。

2.2.5 总结![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=4af12d2315e4c820501bd2a854145b95)

2.3 实践：文本语义相似度计算题目：基于预训练模型 ERNIE-Gram 实现语义匹配

给定两段文本，让模型来判断两段文本是不是语义相似。LCQMC 数据集是基于百度知道相似问题推荐构造的通问句语义匹配数据集。训练集中的每两段文本都会被标记为 1（语义相似） 或者 0（语义不相似）。

数据加载# 加载 Lcqmc 的训练集、验证集train_ds, dev_ds = load_dataset("lcqmc", splits=["train", "dev"])# 输出训练集的前 10 条样本for idx, example in enumerate(train_ds):    if idx <= 10:        print(example)![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=88d967ebd36cd58069b0bfc45ba83632)

数据预处理实现组 batch、tokenize 等预处理逻辑，将原始明文数据转换成网络训练的输入数据。

定义样本转换函数# 因为是基于预训练模型 ERNIE-Gram 来进行，所以需要首先加载 ERNIE-Gram 的 tokenizer，# 后续样本转换函数基于 tokenizer 对文本进行切分tokenizer = paddlenlp.transformers.ErnieGramTokenizer.from_pretrained('ernie-gram-zh')# 对训练集的第 1 条数据进行转换input_ids, token_type_ids, label = convert_example(train_ds[0], tokenizer)print(input_ids)print(token_type_ids)print(label)# 为了后续方便使用，我们使用python偏函数（partial）给 convert_example 赋予一些默认参数from functools import partial# 训练集和验证集的样本转换函数trans_func = partial(    convert_example,    tokenizer=tokenizer,    max_seq_length=512)def convert_example(example, tokenizer, max_seq_length=512, is_test=False):    """    将 1 条明文数据的 query、title 拼接起来，根据预训练模型的 tokenizer 将明文转换为 ID 数据    返回 input_ids 和 token_type_ids    """    query, title = example["query"], example["title"]    encoded_inputs = tokenizer(        text=query, text_pair=title, max_seq_len=max_seq_length)    input_ids = encoded_inputs["input_ids"]    token_type_ids = encoded_inputs["token_type_ids"]    if not is_test:        label = np.array([example["label"]], dtype="int64")        return input_ids, token_type_ids, label    # 在预测或者评估阶段，不返回 label 字段    else:        return input_ids, token_type_ids![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=40ca1a206a7cba8ea48e5fc10087d84c)

组装 Batch 数据 & Padding需要将样本组合成 Batch 数据，对于不等长的数据还需要进行 Padding 操作，便于 GPU 训练。

| API | 简介 |
| --- | --- |
| paddlenlp.data.Stack | 堆叠N个具有相同shape的输入数据来构建一个batch |
| paddlenlp.data.Pad | 将长度不同的多个句子padding到统一长度，取N个输入数据中的最大长度 |
| paddlenlp.data.Tuple | 将多个batchify函数包装在一起 |

# 我们的训练数据会返回 input_ids, token_type_ids, labels 3 个字段# 因此针对这 3 个字段需要分别定义 3 个组 batch 操作batchify_fn = lambda samples, fn=Tuple(    Pad(axis=0, pad_val=tokenizer.pad_token_id),  # input_ids    Pad(axis=0, pad_val=tokenizer.pad_token_type_id),  # token_type_ids    Stack(dtype="int64")  # label): [data for data in fn(samples)]def batch_or_padding():    """    组装 Batch 数据 & Padding    """    from paddlenlp.data import Stack, Pad, Tuple    a = [1, 2, 3, 4]    b = [3, 4, 5, 6]    c = [5, 6, 7, 8]    result = Stack()([a, b, c])    print("Stacked Data: \n", result)    print()    a = [1, 2, 3, 4]    b = [5, 6, 7]    c = [8, 9]    result = Pad(pad_val=0)([a, b, c])    print("Padded Data: \n", result)    print()    data = [        [[1, 2, 3, 4], [1]],        [[5, 6, 7], [0]],        [[8, 9], [1]],    ]    batchify_fn = Tuple(Pad(pad_val=0), Stack())    ids, labels = batchify_fn(data)    print("ids: \n", ids)    print()    print("labels: \n", labels)    print()![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=88696f5db5cc0e1cdee923289c2e1363)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e3a02c4136f1bf26f26cf7227fb829b3)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=7b995dd80fc78910a9850cf16062abdf)

定义 Dataloader基于组 batchify_fn 函数和样本转换函数 trans_func 来构造训练集的 DataLoader, 支持多卡训练.

# 定义分布式 Sampler: 自动对训练数据进行切分，支持多卡并行训练batch_sampler = paddle.io.DistributedBatchSampler(train_ds, batch_size=32, shuffle=True)# 基于 train_ds 定义 train_data_loader# 因为我们使用了分布式的 DistributedBatchSampler, train_data_loader 会自动对训练数据进行切分train_data_loader = paddle.io.DataLoader(    dataset=train_ds.map(trans_func),    batch_sampler=batch_sampler,    collate_fn=batchify_fn,    return_list=True)# 针对验证集数据加载，我们使用单卡进行评估，所以采用 paddle.io.BatchSampler 即可# 定义 dev_data_loaderbatch_sampler = paddle.io.BatchSampler(dev_ds, batch_size=32, shuffle=False)dev_data_loader = paddle.io.DataLoader(    dataset=dev_ds.map(trans_func),    batch_sampler=batch_sampler,    collate_fn=batchify_fn,    return_list=True)模型搭建# 我们基于 ERNIE-Gram 模型结构搭建 Point-wise 语义匹配网络# 所以此处先定义 ERNIE-Gram 的 pretrained_modelpretrained_model = paddlenlp.transformers.ErnieGramModel.from_pretrained('ernie-gram-zh')# pretrained_model = paddlenlp.transformers.ErnieModel.from_pretrained('ernie-1.0')# 定义 Point-wise 语义匹配网络model = PointwiseMatching(pretrained_model)class PointwiseMatching(nn.Layer):    # 此处的 pretained_model 在本例中会被 ERNIE-Gram 预训练模型初始化    def __init__(self, pretrained_model, dropout=None):        super().__init__()        self.ptm = pretrained_model        self.dropout = nn.Dropout(dropout if dropout is not None else 0.1)        # 语义匹配任务: 相似、不相似 2 分类任务        self.classifier = nn.Linear(self.ptm.config["hidden_size"], 2)    def forward(self,                input_ids,                token_type_ids=None,                position_ids=None,                attention_mask=None):        # 此处的 Input_ids 由两条文本的 token ids 拼接而成        # token_type_ids 表示两段文本的类型编码        # 返回的 cls_embedding 就表示这两段文本经过模型的计算之后而得到的语义表示向量        _, cls_embedding = self.ptm(input_ids, token_type_ids, position_ids,                                    attention_mask)        cls_embedding = self.dropout(cls_embedding)        # 基于文本对的语义表示向量进行 2 分类任务        logits = self.classifier(cls_embedding)        probs = F.softmax(logits)        return probs模型训练&评估from paddlenlp.transformers import LinearDecayWithWarmupepochs = 3num_training_steps = len(train_data_loader) * epochs# 定义 learning_rate_scheduler，负责在训练过程中对 lr 进行调度lr_scheduler = LinearDecayWithWarmup(5E-5, num_training_steps, 0.0)# Generate parameter names needed to perform weight decay.# All bias and LayerNorm parameters are excluded.decay_params = [    p.name for n, p in model.named_parameters()    if not any(nd in n for nd in ["bias", "norm"])]# 定义 Optimizeroptimizer = paddle.optimizer.AdamW(    learning_rate=lr_scheduler,    parameters=model.parameters(),    weight_decay=0.0,    apply_decay_param_fun=lambda x: x in decay_params)# 采用交叉熵 损失函数criterion = paddle.nn.loss.CrossEntropyLoss()# 评估的时候采用准确率指标metric = paddle.metric.Accuracy()# 因为训练过程中同时要在验证集进行模型评估，因此我们先定义评估函数@paddle.no_grad()def evaluate(model, criterion, metric, data_loader, phase="dev"):    model.eval()    metric.reset()    losses = []    for batch in data_loader:        input_ids, token_type_ids, labels = batch        probs = model(input_ids=input_ids, token_type_ids=token_type_ids)        loss = criterion(probs, labels)        losses.append(loss.numpy())        correct = metric.compute(probs, labels)        metric.update(correct)        accu = metric.accumulate()    print("eval {} loss: {:.5}, accu: {:.5}".format(phase,                                                    np.mean(losses), accu))    model.train()    metric.reset()# 接下来，开始正式训练模型global_step = 0tic_train = time.time()for epoch in range(1, epochs + 1):    for step, batch in enumerate(train_data_loader, start=1):        input_ids, token_type_ids, labels = batch        probs = model(input_ids=input_ids, token_type_ids=token_type_ids)        loss = criterion(probs, labels)        correct = metric.compute(probs, labels)        metric.update(correct)        acc = metric.accumulate()        global_step += 1        # 每间隔 10 step 输出训练指标        if global_step % 10 == 0:            print(                "global step %d, epoch: %d, batch: %d, loss: %.5f, accu: %.5f, speed: %.2f step/s"                % (global_step, epoch, step, loss, acc,                   10 / (time.time() - tic_train)))            tic_train = time.time()        loss.backward()        optimizer.step()        lr_scheduler.step()        optimizer.clear_grad()        # 每间隔 100 step 在验证集和测试集上进行评估        if global_step % 100 == 0:            evaluate(model, criterion, metric, dev_data_loader, "dev")# 训练结束后，存储模型参数save_dir = os.path.join("checkpoint", "model_%d" % global_step)os.makedirs(save_dir)save_param_path = os.path.join(save_dir, 'model_state.pdparams')paddle.save(model.state_dict(), save_param_path)tokenizer.save_pretrained(save_dir)模型预测跑的比较慢，直接下载训练好的

wget https://paddlenlp.bj.bcebos.com/models/text_matching/ernie_gram_zh_pointwise_matching_model.tartar -xvf ernie_gram_zh_pointwise_matching_model.tar测试数据：

# 测试数据由 2 列文本构成 tab 分隔# Lcqmc 默认下载到如下路径head -n3 "${HOME}/.paddlenlp/datasets/LCQMC/lcqmc/lcqmc/test.tsv"![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=4c8529948eda2e72697ddc9accba31a3)

定义预测函数def predict(model, data_loader):    batch_probs = []    # 预测阶段打开 eval 模式，模型中的 dropout 等操作会关掉    model.eval()    with paddle.no_grad():        for batch_data in data_loader:            input_ids, token_type_ids = batch_data            input_ids = paddle.to_tensor(input_ids)            token_type_ids = paddle.to_tensor(token_type_ids)                        # 获取每个样本的预测概率: [batch_size, 2] 的矩阵            batch_prob = model(                input_ids=input_ids, token_type_ids=token_type_ids).numpy()            batch_probs.append(batch_prob)        batch_probs = np.concatenate(batch_probs, axis=0)        return batch_probs定义预测数据的 data_loadertokenizer = paddlenlp.transformers.ErnieGramTokenizer.from_pretrained('ernie-gram-zh')# 预测数据的转换函数# predict 数据没有 label, 因此 convert_exmaple 的 is_test 参数设为 Truetrans_func = partial(    convert_example,    tokenizer=tokenizer,    max_seq_length=512,    is_test=True)# 预测数据的组 batch 操作# predict 数据只返回 input_ids 和 token_type_ids，因此只需要 2 个 Pad 对象作为 batchify_fnbatchify_fn = lambda samples, fn=Tuple(    Pad(axis=0, pad_val=tokenizer.pad_token_id),  # input_ids    Pad(axis=0, pad_val=tokenizer.pad_token_type_id),  # segment_ids): [data for data in fn(samples)]# 加载预测数据test_ds = load_dataset("lcqmc", splits=["test"])batch_sampler = paddle.io.BatchSampler(test_ds, batch_size=32, shuffle=False)# 生成预测数据 data_loaderpredict_data_loader = paddle.io.DataLoader(    dataset=test_ds.map(trans_func),    batch_sampler=batch_sampler,    collate_fn=batchify_fn,    return_list=True)定义预测模型# 选择预训练ernie grampretrained_model = paddlenlp.transformers.ErnieGramModel.from_pretrained('ernie-gram-zh')model = PointwiseMatching(pretrained_model)加载已训练好的模型参数# 刚才下载的模型解压之后存储路径为 ./ernie_gram_zh_pointwise_matching_model/model_state.pdparamsstate_dict = paddle.load("./ernie_gram_zh_pointwise_matching_model/model_state.pdparams")# state_dict = paddle.load("pointwise_matching_model/ernie1.0_base_pointwise_matching.pdparams")model.set_dict(state_dict)开始预测for idx, batch in enumerate(predict_data_loader):    if idx < 1:        print(batch)# 执行预测函数y_probs = predict(model, predict_data_loader)# 根据预测概率获取预测 labely_preds = np.argmax(y_probs, axis=1)输出预测结果# 我们按照千言文本相似度竞赛的提交格式将预测结果存储在 lcqmc.tsv 中，用来后续提交# 同时将预测结果输出到终端，便于大家直观感受模型预测效果test_ds = load_dataset("lcqmc", splits=["test"])with open("lcqmc.tsv", 'w', encoding="utf-8") as f:    f.write("index\tprediction\n")        for idx, y_pred in enumerate(y_preds):        f.write("{}\t{}\n".format(idx, y_pred))        text_pair = test_ds[idx]        text_pair["label"] = y_pred        print(text_pair)三、词法分析技术与应用3.1 词法分析概念应用词法分析：分词并对每个词进行分类，包括：分词、词性标注、实体识别三个任务

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=d83ee19200fc9c5a399f6a3b53589a40)

应用：搜索、对话问答、信息抽取

3.2 词法分析技术发展3.2.1 字符串匹配基于字符串匹配方法

前向/后向/词长最大匹配、最少词数、策略组合代表应用：mmseg分词、IK分词（ES服务常用）优缺点：方法简单可控，速度快；难以解决歧义及新词的问题，如：我们/经常/有意/见/分歧vs我们/经/常有/意见/分歧![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c20279091c33916af21345f565e091df)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=7e08d064462a3cbfc3b13c2a71e4cc85)

3.2.2 统计语言模型基于词的语言模型

基于词典构造有向无环图计算有向无环图最大概率路径【统计语言模型】代表应用：jieba、ICTCLAS(NLPIR)缺点：难以解决新词问题![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=dcfb0492986625b091c0394cdb47f076)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=3691784dc34587b5d4b841798eab0173)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=d391ea5a98743ffae3555084a368d8f3)

3.2.3 序列标注输入和输出都是序列，这里以字为单位输入序列和输出序列是一一对应的分类问题的一个推广，一种结构化的分类![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=d6a8a9a1b3c5b4a711fc4283f9731ea1)

RNN![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=9725c35922ee7b0912147fe8f831f41b)

CRF![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=68c187106c59dd783dd55364583bfe9d)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=0aff9ab70ac9cc68c7be4971dc3d6621)

预训练模型![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=77706638250ad290417df3f77368d347)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=b393233f185f36303cb2170fe99c5ca1)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=5b9daae9d9d58d4e8eda83216a8c1d5d)

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=e129e99ab6dcef2d98769a87208edd55)

3.3 开源算法LAC地址： https://github.com/baidu/lac

3.3.1 词性与重要性标签集合词性和专名类别标签集合：

| 标签 | 含义 | 标签 | 含义 | 标签 | 含义 | 标签 | 含义 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n | 普通名词 | f | 方位名词 | s | 处所名词 | nw | 作品名 |
| nz | 其他专名 | v | 普通动词 | vd | 动副词 | vn | 名动词 |
| a | 形容词 | ad | 副形词 | an | 名形词 | d | 副词 |
| m | 数量词 | q | 量词 | r | 代词 | p | 介词 |
| c | 连词 | u | 助词 | xc | 其他虚词 | w | 标点符号 |
| PER | 人名 | LOC | 地名 | ORG | 机构名 | TIME | 时间 |

词语重要性各类别标签集合：

| 标签 | 含义 | 常见于词性 |
| --- | --- | --- |
| 0 | query中表述的冗余词 | p, w, xc ... |
| 1 | query中限定较弱的词 | r, c, u ... |
| 2 | query中强限定的词 | n, s, v ... |
| 3 | query中的核心词 | nz, nw, LOC ... |

![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=a8d43b18a7e670cd3a7410fa0ccb076c)

3.3.2 功能与使用分词from LAC import LACtext = u"LAC是个优秀的分词工具"texts = [u"LAC是个优秀的分词工具", u"百度是一家高科技公司"]# 分词lac = LAC(mode='seg')seg_result = lac.run(text)print(seg_result)['LAC', '是', '个', '优秀', '的', '分词', '工具']

词性标注与实体识别# 词性标注与实体识别lac = LAC(mode='lac')lac_result = lac.run(text)print(lac_result)[['LAC', '是', '个', '优秀', '的', '分词', '工具'], ['nz', 'v', 'q', 'a', 'u', 'n', 'n']]

词语重要性# 词语重要性lac = LAC(mode='rank')rank_result = lac.run(text)print(rank_result)[['LAC', '是', '个', '优秀', '的', '分词', '工具'], ['nz', 'v', 'q', 'a', 'u', 'n', 'n'], [3, 0, 0, 2, 0, 3, 1]]

3.4 实践：快递单信息识别地址： https://aistudio.baidu.com/aistudio/projectdetail/1317771

任务：拿到一个快递单作为模型输入，例如“张三18625584663广东省深圳市南山区学府路东百度国际大厦”，需要识别出具体的信息

| 抽取实体/字段 | 符号 | 抽取结果 |
| --- | --- | --- |
| 姓名 | P | 张三 |
| 电话 | T | 18625584663 |
| 省 | A1 | 广东省 |
| 市 | A2 | 深圳市 |
| 区 | A3 | 南山区 |
| 详细地址 | A4 | 百度国际大厦 |

序列标注模型标签集合可以定义为：label = {P-B, P-I, T-B, T-I, A1-B, A1-I, A2-B, A2-I, A3-B, A3-I, A4-B, A4-I, O}

| 标签 | 定义 |
| --- | --- |
| P-B | 姓名起始位置 |
| P-I | 姓名中间位置或结束位置 |
| T-B | 电话起始位置 |
| T-I | 电话中间位置或结束位置 |
| A1-B | 省份起始位置 |
| A1-I | 省份中间位置或结束位置 |
| A2-B | 城市起始位置 |
| A2-I | 城市中间位置或结束位置 |
| A3-B | 县区起始位置 |
| A3-I | 县区中间位置或结束位置 |
| A4-B | 详细地址起始位置 |
| A4-I | 详细地址中间位置或结束位置 |
| O | 无关字符 |

对于句子“张三18625584663广东省深圳市南山区百度国际大厦”，每个汉字及对应标签为：

![](https://ai-studio-static-online.cdn.bcebos.com/1f716a6ad48649cc99c56c27108773bea6b0afa3f36e4efba4851641658b2414)

数据准备提前准备训练数据(训练集train.txt、验证集dev.txt、测试集test.txt)和词典数据。词典数据包括：

输入文本词典word.dic对输入文本中特殊字符进行转换的词典q2b.dic标记标签的词典tag.dic自定义数据集# 下载并解压数据集from paddle.utils.download import get_path_from_urlURL = "https://paddlenlp.bj.bcebos.com/paddlenlp/datasets/waybill.tar.gz"get_path_from_url(URL, "./")file = open('data/train.txt')for i, line in enumerate(file):    if 0 < i < 3:        print('%d: ' % i, line.split()[0])        print('   ', line.split()[1])![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=6c234c36696a7e99ea17d3bcd8371257)

from functools import partialimport paddlefrom paddlenlp.datasets import MapDatasetfrom paddlenlp.data import Stack, Tuple, Padfrom paddlenlp.transformers import ErnieTokenizer, ErnieForTokenClassificationfrom paddlenlp.metrics import ChunkEvaluatorfrom utils import convert_example, evaluate, predict, load_dict数据加载train_ds, dev_ds, test_ds = load_dataset_locate(datafiles=(    './data/train.txt', './data/dev.txt', './data/test.txt'))for i in range(2):    print(train_ds[i])(['1', '6', '6', '2', '0', '2', '0', '0', '0', '7', '7', '宣', '荣', '嗣', '甘', '肃', '省', '白', '银', '市', '会', '宁', '县', '河', '畔', '镇', '十', '字', '街', '金', '海', '超', '市', '西', '行', '5', '0', '米'], ['T-B', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'P-B', 'P-I', 'P-I', 'A1-B', 'A1-I', 'A1-I', 'A2-B', 'A2-I', 'A2-I', 'A3-B', 'A3-I', 'A3-I', 'A4-B', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I'])(['1', '3', '5', '5', '2', '6', '6', '4', '3', '0', '7', '姜', '骏', '炜', '云', '南', '省', '德', '宏', '傣', '族', '景', '颇', '族', '自', '治', '州', '盈', '江', '县', '平', '原', '镇', '蜜', '回', '路', '下', '段'], ['T-B', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'T-I', 'P-B', 'P-I', 'P-I', 'A1-B', 'A1-I', 'A1-I', 'A2-B', 'A2-I', 'A2-I', 'A2-I', 'A2-I', 'A2-I', 'A2-I', 'A2-I', 'A2-I', 'A2-I', 'A3-B', 'A3-I', 'A3-I', 'A4-B', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I', 'A4-I'])def load_dataset_locate(datafiles):    """    数据加载    """    def read(data_path):        with open(data_path, 'r', encoding='utf-8') as fp:            next(fp)  # Skip header            for line in fp.readlines():                words, labels = line.strip('\n').split('\t')                words = words.split('\002')                labels = labels.split('\002')                yield words, labels    if isinstance(datafiles, str):        return MapDataset(list(read(datafiles)))    elif isinstance(datafiles, list) or isinstance(datafiles, tuple):        return [MapDataset(list(read(datafile))) for datafile in datafiles]数据处理label_vocab = load_dict('./data/tag.dic')tokenizer = ErnieTokenizer.from_pretrained('ernie-1.0')trans_func = partial(convert_example, tokenizer=tokenizer, label_vocab=label_vocab)train_ds.map(trans_func)dev_ds.map(trans_func)test_ds.map(trans_func)print(train_ds[0])def convert_example(example, tokenizer, label_vocab):    tokens, labels = example    tokenized_input = tokenizer(        tokens, return_length=True, is_split_into_words=True)    # Token '[CLS]' and '[SEP]' will get label 'O'    labels = ['O'] + labels + ['O']    tokenized_input['labels'] = [label_vocab[x] for x in labels]    return tokenized_input['input_ids'], tokenized_input[        'token_type_ids'], tokenized_input['seq_len'], tokenized_input['labels']

数据读入ignore_label = -1batchify_fn = lambda samples, fn=Tuple(    Pad(axis=0, pad_val=tokenizer.pad_token_id),  # input_ids    Pad(axis=0, pad_val=tokenizer.pad_token_type_id),  # token_type_ids    Stack(),  # seq_len    Pad(axis=0, pad_val=ignore_label)  # labels): fn(samples)train_loader = paddle.io.DataLoader(    dataset=train_ds,    batch_size=36,    return_list=True,    collate_fn=batchify_fn)dev_loader = paddle.io.DataLoader(    dataset=dev_ds,    batch_size=36,    return_list=True,    collate_fn=batchify_fn)test_loader = paddle.io.DataLoader(    dataset=test_ds,    batch_size=36,    return_list=True,    collate_fn=batchify_fn)加载预训练模型model = ErnieForTokenClassification.from_pretrained("ernie-1.0", num_classes=len(label_vocab))更多预训练模型参考：PaddleNLP Transformer API

设置Fine-Tune优化策略，模型配置

metric = ChunkEvaluator(label_list=label_vocab.keys(), suffix=True)loss_fn = paddle.nn.loss.CrossEntropyLoss(ignore_index=ignore_label)optimizer = paddle.optimizer.AdamW(learning_rate=2e-5, parameters=model.parameters())模型训练与评估模型训练的过程通常有以下步骤：

从dataloader中取出一个batch data将batch data喂给model，做前向计算将前向计算结果传给损失函数，计算loss。将前向计算结果传给评价方法，计算评价指标。loss反向回传，更新梯度。重复以上步骤。每训练一个epoch时，程序将会评估一次，评估当前模型训练的效果。

step = 0for epoch in range(10):    for idx, (input_ids, token_type_ids, length, labels) in enumerate(train_loader):        logits = model(input_ids, token_type_ids)        loss = paddle.mean(loss_fn(logits, labels))        loss.backward()        optimizer.step()        optimizer.clear_grad()        step += 1        print("epoch:%d - step:%d - loss: %f" % (epoch, step, loss))    evaluate(model, metric, dev_loader)    paddle.save(model.state_dict(),                './ernie_result/model_%d.pdparams' % step)模型预测preds = predict(model, test_loader, test_ds, label_vocab)file_path = "ernie_results.txt"with open(file_path, "w", encoding="utf8") as fout:    fout.write("\n".join(preds))# Print some examplesprint(    "The results have been saved in the file: %s, some examples are shown below: "    % file_path)print("\n".join(preds[:10]))

