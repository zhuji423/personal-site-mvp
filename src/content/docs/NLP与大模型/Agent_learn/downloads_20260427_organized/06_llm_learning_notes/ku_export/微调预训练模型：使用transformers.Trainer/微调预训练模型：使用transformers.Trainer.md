---
title: "微调预训练模型：使用transformers.Trainer"
description: "import evaluateimport numpy as npfrom datasets import loaddataset, Audiofrom transformers import pipelinefrom transforme"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\微调预训练模型：使用transformers.Trainer\\微调预训练模型：使用transformers.Trainer.md"
---
# 微调预训练模型：使用transformers.Trainer
一、微调示例对 distilbert-base-uncased 模型使用数据集 rotten_tomatoes（烂番茄电影影评数据集） 进行微调

import evaluateimport numpy as npfrom datasets import load_dataset, Audiofrom transformers import pipelinefrom transformers import AutoTokenizer, AutoModelForSequenceClassificationfrom transformers import TrainingArgumentsfrom transformers import DataCollatorWithPaddingfrom transformers import Trainerfrom huggingface_hub import snapshot_downloaddef finetuning():    """    模型微调    """    # 训练参数    training_args = TrainingArguments(        output_dir="./output/my_model",        learning_rate=1e-3,        per_device_train_batch_size=16,        per_device_eval_batch_size=16,        num_train_epochs=10,    )    # 1、加载预训练模型    model_name = "distilbert-base-uncased"    model = AutoModelForSequenceClassification.from_pretrained(model_name, cache_dir='./models/')    tokenizer = AutoTokenizer.from_pretrained(model_name)    # 2、加载数据集    dataset = load_dataset("rotten_tomatoes")    # 3、处理数据集    def tokenize_dataset(dataset):        return tokenizer(dataset["text"])    # 分词    dataset = dataset.map(tokenize_dataset, batched=True)    # 创建批次    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)    # 4、设定度量指标    accuracy = evaluate.load("accuracy")    def compute_metrics(eval_pred):        logits, labels = eval_pred        predictions = np.argmax(logits, axis=-1)        return accuracy.compute(predictions=predictions, references=labels)    # 5、创建训练    trainer = Trainer(        model=model,        args=training_args,        train_dataset=dataset["train"],        eval_dataset=dataset["test"],        tokenizer=tokenizer,        data_collator=data_collator,        compute_metrics=compute_metrics    )    # 6、训练    trainer.train()    # 7、保存模型    trainer.save_model()二、使用过程中的问题1、预训练模型下载太慢了在目录中包含着flax_model.msgpack、tf_model.h5和pytorch_model.bin几个不同框架模型文件，我们只要pytorch的模型

可以单独下载，参考

from huggingface_hub import snapshot_downloaddef load_model():    """    下载预训练模型    """    snapshot_download(        repo_id="distilbert-base-uncased",        ignore_patterns=["*.h5", "*.ot", "*.msgpack"],        cache_dir='./models/'    )![](/personal-site-mvp/img/doc-placeholder.svg)

2、日志警告Some weights of the model checkpoint at distilbert-base-uncased were not used when initializing![](/personal-site-mvp/img/doc-placeholder.svg)

这是个警告信息，不是报错信息。这只说明对应的加载的预训练模型与任务类型不完全对应。要么出现有些参数用不到的情况，要么出现有些参数没有、需要随机初始化的情况。忽略即可。

如果想直接删除这个信息，可以使用：

from transformers import logginglogging.set_verbosity_error()

三、使用微调好的进行预测def predict():    """    测试模型    """    model_path = "./output/my_model"    model = AutoModelForSequenceClassification.from_pretrained(model_path)    tokenizer = AutoTokenizer.from_pretrained(model_path)    sentence = "I really do not like it."    sen_code = tokenizer.encode_plus(sentence)    tokens_tensor = torch.tensor([sen_code['input_ids']])    model.eval()    outputs = model(tokens_tensor)    predictions = np.argmax(outputs[0].detach().numpy(), axis=-1)    print(predictions)

