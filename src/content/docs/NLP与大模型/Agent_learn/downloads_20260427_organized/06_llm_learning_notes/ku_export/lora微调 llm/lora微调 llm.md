---
title: "lora微调 llm"
description: "git clone https://github.com/mymusise/ChatGLM-Tuning数据集下载至data/"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\lora微调 llm\\lora微调 llm.md"
---
# lora微调 llm
1、chatglm下载代码

git clone https://github.com/mymusise/ChatGLM-Tuning数据集下载至data/

数据预处理，tokenize_dataset_rows.py 修改本地加载"/shareData/chatglm-6b"

python3 tokenize_dataset_rows.py \    --jsonl_path data/train.jsonl \    --save_path data/train \微调，finetune.py 修改本地加载 "/shareData/chatglm-6b"

CUDA_VISIBLE_DEVICES=0 python3 finetune.py \    --dataset_path data/train \    --lora_rank 8 \    --per_device_train_batch_size 4 \    --gradient_accumulation_steps 4 \    --max_steps 3000 \    --save_steps 1000 \    --save_total_limit 2 \    --learning_rate 2e-2 \    --fp16 \    --remove_unused_columns false \    --logging_steps 50 \    --output_dir output![](/personal-site-mvp/img/doc-placeholder.svg)

使用未量化的fp16，训练200条数据需要3小时

2、llama 

