---
title: "EP部门大模型快速使用"
description: "ssh star@172.18.12.141 登陆gpu机子，不用跳板机sudo docker start text-generation-webui-zj 启动容器sudo docker attach text-generation-we"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\EP部门大模型快速使用\\EP部门大模型快速使用.md"
---
# EP部门大模型快速使用
开源模型需要gpu机子账号密码（联系任彦伟）

使用：

ssh star@172.18.12.141  # 登陆gpu机子，不用跳板机sudo docker start text-generation-webui-zj  # 启动容器sudo docker attach text-generation-webui-zj  # 进入容器cd /work/text-generation-webui  # 进入工程目录python3 server.py --api --model=chatglm2-6b --model-dir=/shareData/models/  --trust-remote-code  # 开启服务，不同模型启动服务命令不同![](/personal-site-mvp/img/doc-placeholder.svg)

ssh -N -L localhost:8838:localhost:7860 star@172.18.12.141  # 本地mac上执行后打开浏览器localhost:8838# 将star@172.18.12.141机子的7860号端口转发到本机8838号端口，也可以将8838替换其他端口号![](/personal-site-mvp/img/doc-placeholder.svg)

![](/personal-site-mvp/img/doc-placeholder.svg)

已可用的模型：

| 模型 | 命令 |
| --- | --- |
| Llama-2-13B-chat-GPTQ | python3 server.py --api --model=Llama-2-13B-chat-GPTQ --model-dir=/shareData/models/   |
| Llama-2-70B-GPTQ | python3 server.py --api --model=Llama-2-70B-GPTQ --model-dir=/shareData/models/ --no_inject_fused_attention --no_inject_fused_mlp   # 不禁用融合的话显存40g不够，禁用后推理速度稍变慢 由15token/s到7token/s |
| chatglm2-6b | python3 server.py --api --model=chatglm2-6b --model-dir=/shareData/models/  --trust-remote-code  # 必要要加--trust-remote-code |
| chatglm-6b | python3 server.py --api --model=chatglm-6b --model-dir=/shareData/models/  --trust-remote-code  # 必要要加--trust-remote-code |
| codegeex2-6b | python3 server.py --api --model=codegeex2-6b --model-dir=/shareData/models/ --trust-remote-code  # 必要要加--trust-remote-code |
| CodeLlama-13B-GGML | python3 server.py --api --model=CodeLlama-13B-GGML --model-dir=/shareData/models/ --n-gpu-layers=64  # 不加--n-gpu-layers GGML模型会默认用cpu跑 |
| CodeLlama-13B-Instruct-GPTQ | python3 server.py --api --model=CodeLlama-13B-Instruct-GPTQ --model-dir=/shareData/models/  |
| vicuna-13b-v1.3.0-GPTQ | python3 server.py --api --model=vicuna-13b-v1.3.0-GPTQ --model-dir=/shareData/models/  |
| WizardCoder-15B-1.0-GPTQ | python3 server.py --api --model=WizardCoder-15B-1.0-GPTQ --model-dir=/shareData/models/  |
| starcoderplus-GPTQ | python3 server.py --api --model=starcoderplus-GPTQ --model-dir=/shareData/models/  |
| Llama-2-7b-hf | python3 server.py --api --model=Llama-2-7b-hf --model-dir=/shareData/models/  |
| Llama-2-7b-hf + chinese-llama-2-lora-7b |  |
| llama-7b-hf + alpaca-lora-7b |  |

详细使用：

文心需要WENXIN_AK、WENXIN_SK（联系谢楠）

使用文档： https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/d5ylCrGrW0LuyQ

gpt4.0需要openai账号（联系任彦伟）

gpt页面地址：https://chat.openai.com



