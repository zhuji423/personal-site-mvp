---
title: "chatglm2-6b运行与微调"
description: "cd ~/zhoujie19git clone https://github.com/THUDM/ChatGLM2-6B下载模型至模型目录"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\chatglm2-6b运行与微调\\chatglm2-6b运行与微调.md"
---
# chatglm2-6b运行与微调
1、下载项目与模型下载项目至个人目录

cd ~/zhoujie19git clone https://github.com/THUDM/ChatGLM2-6B下载模型至模型目录

cd ~/shareDataGIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/THUDM/chatglm2-6b  # GIT_LFS_SKIP_SMUDGE=1表示LFS文件跳过逐个下载模型的LFS文件

python3 download.py 'THUDM/chatglm2-6b' '.' 'pytorch_model-00001-of-00007.bin'![](/personal-site-mvp/img/doc-placeholder.svg)

2、环境直接使用的容器

sudo docker ps -a  # 查看容器sudo docker start 19309b91b548  # 启动容器sudo docker attach 19309b91b548  # 进入容器![](/personal-site-mvp/img/doc-placeholder.svg)

在gpt容器中启动jupyter lab，方便修改代码

jupyter lab --port=8888 --allow-root  --no-browser在自己的电脑上执行端口映射，打开localhost:8838，输入token，连接jupyter。

ssh -N -L localhost:8838:localhost:8888 star@172.18.12.1413、运行代码中的 THUDM/chatglm-6b 替换为本地的 chatglm-6b 文件夹的路径

![](/personal-site-mvp/img/doc-placeholder.svg)

运行

 python3 web_demo.py![](/personal-site-mvp/img/doc-placeholder.svg)

本机执行 ssh -N -L localhost:8839:localhost:7860 star@172.18.12.141 ，浏览器打开 localhost:8839

![](/personal-site-mvp/img/doc-placeholder.svg)

先试试没有微调的效果

4、微调1）准备训练数据准备数据问答对训练train.json及验证文件val.json ，以 ADGEN (广告生成) 数据集为例。这里只取了200条，解压在ptuning目录下。

2）调整训练参数进入ptuning修改训练脚本train.sh

PRE_SEQ_LEN=128LR=2e-2NUM_GPUS=1CUDA_VISIBLE_DEVICES=0 python3 main.py \    --do_train \    --train_file AdvertiseGen/train.json \    --validation_file AdvertiseGen/dev.json \    --preprocessing_num_workers 10 \    --prompt_column content \    --response_column summary \    --overwrite_cache \    --model_name_or_path /shareData/chatglm2-6b \    --output_dir output/chatglm2-6b-pt-$PRE_SEQ_LEN-$LR \    --overwrite_output_dir \    --max_source_length 64 \    --max_target_length 128 \    --per_device_train_batch_size 1 \    --per_device_eval_batch_size 1 \    --gradient_accumulation_steps 16 \    --predict_with_generate \    --max_steps 3000 \    --logging_steps 10 \    --save_steps 1000 \    --learning_rate $LR \    --pre_seq_len $PRE_SEQ_LEN \    --quantization_bit 43）启动训练bash train.sh![](/personal-site-mvp/img/doc-placeholder.svg)

![](/personal-site-mvp/img/doc-placeholder.svg)

4）评估训练效果修改evaluate.sh，并执行

PRE_SEQ_LEN=128CHECKPOINT=chatglm2-6b-pt-128-2e-2STEP=3000NUM_GPUS=1CUDA_VISIBLE_DEVICES=0 python3 main.py \    --do_predict \    --validation_file AdvertiseGen/dev.json \    --test_file AdvertiseGen/dev.json \    --overwrite_cache \    --prompt_column content \    --response_column summary \    --model_name_or_path /shareData/chatglm2-6b \    --ptuning_checkpoint ./output/$CHECKPOINT/checkpoint-$STEP \    --output_dir ./output/$CHECKPOINT \    --overwrite_output_dir \    --max_source_length 64 \    --max_target_length 64 \    --per_device_eval_batch_size 1 \    --predict_with_generate \    --pre_seq_len $PRE_SEQ_LEN \    --quantization_bit 4![](/personal-site-mvp/img/doc-placeholder.svg)

相比于chatgml，怎么chatgml2效果反而更差了，可能因为数据量小有波动，但是为啥速度也低了。。。

![](/personal-site-mvp/img/doc-placeholder.svg)

5）运行微调后的模型修改web_demo.sh

PRE_SEQ_LEN=128CUDA_VISIBLE_DEVICES=0 python3 web_demo.py \    --model_name_or_path /shareData/chatglm2-6b \    --ptuning_checkpoint output/chatglm2-6b-pt-128-2e-2/checkpoint-3000 \    --pre_seq_len $PRE_SEQ_LEN重新运行 

 bash web_demo.sh本机执行 ssh -N -L localhost:8839:localhost:7860 star@172.18.12.141 ，浏览器打开 localhost:8839

![](/personal-site-mvp/img/doc-placeholder.svg)

微调后能够理解格式化的服装描述，并给出相应的广告词，证明了微调的效果

