---
title: "StableDiffusion lora练图"
description: "2、预处理https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1ecb303c4dee41f8bee6ef4f5e4026e1&d"
date: "2026-10-11"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\StableDiffusion lora练图\\StableDiffusion lora练图.md"
---
# StableDiffusion lora练图
一、数据与预处理注意：图片质量>图片数量，风格、功能性Lora>真人>二次元，二次元是最简单的lora：）。1、原始数据网上找找，同一个人的20张照片

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=91989d5bae9a46fba80086799a844473&docGuid=uJzwWuby77-5fb)

2、预处理![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1ecb303c4dee41f8bee6ef4f5e4026e1&docGuid=uJzwWuby77-5fb)

生成op文件夹

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d6f16d53f8454b4a8baed414e4f98c49&docGuid=uJzwWuby77-5fb)

处理一下目录层级关系，后面训练会用

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b59ba22fe2ca4093a6f1c67b34a75381&docGuid=uJzwWuby77-5fb)

repeat=10

3、打标（新手就别打标了）很重要的步骤，打标。所谓打标就是监督学习，告诉SD我们要它学什么。这里我们就是想学一个角色，这个角色有很多特征，比如她头上有花花，短发，眼睛样子等。因此我们要把这些角色特征的描述词，从txt文件中的描述中删除。如果是练人物lora图，就把面部的标签都去掉。换句话说，如果我们不删除那些特征，模型是不会把这些特征学给这个角色名的，而是专门学给具体的描述词。

安装插件：https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2486adf84d6a42229644704b9ef391e0&docGuid=uJzwWuby77-5fb)

加载预处理的数据

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=89a6a852bb5545ea98c440aa3bfb323e&docGuid=uJzwWuby77-5fb)

开始批量打标

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5e4d6e5510434592a8fc2606ee7e57b9&docGuid=uJzwWuby77-5fb)

这就是可以批量编辑的地方，进行批量remove，即批量删除不想要的特征词：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=923f76bd0ddd4f5b8949079f43f7dba5&docGuid=uJzwWuby77-5fb)

打勾删除，记得删除后保存下。点击保存所有更改按钮。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=529ed969f4fb4a39a9cff3f5439675a3&docGuid=uJzwWuby77-5fb)

二、训练不想用gui的，直接用lora-scripts 配合文档脚本直接训练，下面的不用看了（其实两者核心训练代码是一样的）

1、安装 kohya_ss地址：https://github.com/bmaltais/kohya_ss

git clone https://github.com/bmaltais/kohya_ss.gitcd kohya_sschmod +x ./setup.sh./setup.shpip install -r requirements.txt运行

bash gui.sh --listen 127.0.0.1 --server_port 7860 --inbrowser --share![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7b8337697c6645f48b4e96d9daae0ca1&docGuid=uJzwWuby77-5fb)

在本地机子执行 ssh -N -L localhost:8838:localhost:7860 star@172.18.12.141 浏览器打开 localhost:8838

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=73ebe7804697414eb79368101bec555e&docGuid=uJzwWuby77-5fb)

2、训练1）基础大模型选择合适的大模型人物练图选择ChilloutMix，更多基础大模型参考：

下载模型方法参考：，下载好后在目录/work/stable-diffusion-webui/models/Stable-diffusion中会有模型文件chilloutmix_NiPrunedFp16Fix.safetensors

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e34b4f09e58f46fca7945d022d66416a&docGuid=uJzwWuby77-5fb)

2）选定数据![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0852b5bd092c453a9f615a931dd3ec04&docGuid=uJzwWuby77-5fb)

3）训练参数20个epoch，每4个epoch保存一次

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=00702ee50a854483b7066bc2b2195362&docGuid=uJzwWuby77-5fb)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ad0c832fb4a448d5a967f769a750bf19&docGuid=uJzwWuby77-5fb)

详细参数解释：

# Train data path | 设置训练用模型、图片$pretrained_model = "./sd-models/model.ckpt" # base model path | 底模路径$is_v2_model = 0 # SD2.0 model | SD2.0模型 2.0模型下 clip_skip 默认无效$parameterization = 0 # parameterization | 参数化 本参数需要和 V2 参数同步使用 实验性功能$train_data_dir = "./train/aki" # train dataset path | 训练数据集路径$reg_data_dir = "" # directory for regularization images | 正则化数据集路径，默认不使用正则化图像。# Network settings | 网络设置$network_module = "networks.lora" # 在这里将会设置训练的网络种类，默认为 networks.lora 也就是 LoRA 训练。如果你想训练 LyCORIS（LoCon、LoHa） 等，则修改这个值为 lycoris.kohya$network_weights = "" # pretrained weights for LoRA network | 若需要从已有的 LoRA 模型上继续训练，请填写 LoRA 模型路径。$network_dim = 32 # network dim | 常用 4~128，不是越大越好$network_alpha = 32 # network alpha | 常用与 network_dim 相同的值或者采用较小的值，如 network_dim的一半 防止下溢。默认值为 1，使用较小的 alpha 需要提升学习率。# Train related params | 训练相关参数$resolution = "512,512" # image resolution w,h. 图片分辨率，宽,高。支持非正方形，但必须是 64 倍数。$batch_size = 1 # batch size$max_train_epoches = 10 # max train epoches | 最大训练 epoch$save_every_n_epochs = 2 # save every n epochs | 每 N 个 epoch 保存一次$train_unet_only = 0 # train U-Net only | 仅训练 U-Net，开启这个会牺牲效果大幅减少显存使用。6G显存可以开启$train_text_encoder_only = 0 # train Text Encoder only | 仅训练 文本编码器$stop_text_encoder_training = 0 # stop text encoder training | 在第N步时停止训练文本编码器$noise_offset = 0 # noise offset | 在训练中添加噪声偏移来改良生成非常暗或者非常亮的图像，如果启用，推荐参数为 0.1$keep_tokens = 0 # keep heading N tokens when shuffling caption tokens | 在随机打乱 tokens 时，保留前 N 个不变。$min_snr_gamma = 0 # minimum signal-to-noise ratio (SNR) value for gamma-ray | 伽马射线事件的最小信噪比（SNR）值  默认为 0# Learning rate | 学习率$lr = "1e-4"$unet_lr = "1e-4"$text_encoder_lr = "1e-5"$lr_scheduler = "cosine_with_restarts" # "linear", "cosine", "cosine_with_restarts", "polynomial", "constant", "constant_with_warmup"$lr_warmup_steps = 0 # warmup steps | 学习率预热步数，lr_scheduler 为 constant 或 adafactor 时该值需要设为0。$lr_restart_cycles = 1 # cosine_with_restarts restart cycles | 余弦退火重启次数，仅在 lr_scheduler 为 cosine_with_restarts 时起效。# Output settings | 输出设置$output_name = "aki" # output model name | 模型保存名称$save_model_as = "safetensors" # model save ext | 模型保存格式 ckpt, pt, safetensors# Resume training state | 恢复训练设置$save_state = 0 # save training state | 保存训练状态 名称类似于 <output_name>-??????-state ?????? 表示 epoch 数$resume = "" # resume from state | 从某个状态文件夹中恢复训练 需配合上方参数同时使用 由于规范文件限制 epoch 数和全局步数不会保存 即使恢复时它们也从 1 开始 与 network_weights 的具体实现操作并不一致# 其他设置$min_bucket_reso = 256 # arb min resolution | arb 最小分辨率$max_bucket_reso = 1024 # arb max resolution | arb 最大分辨率$persistent_data_loader_workers = 0 # persistent dataloader workers | 容易爆内存，保留加载训练集的worker，减少每个 epoch 之间的停顿$clip_skip = 2 # clip skip | 玄学 一般用 2$multi_gpu = 0 # multi gpu | 多显卡训练 该参数仅限在显卡数 >= 2 使用$lowram = 0 # lowram mode | 低内存模式 该模式下会将 U-net 文本编码器 VAE 转移到 GPU 显存中 启用该模式可能会对显存有一定影响# 优化器设置$optimizer_type = "AdamW8bit" # Optimizer type | 优化器类型 默认为 AdamW8bit，可选：AdamW AdamW8bit Lion SGDNesterov SGDNesterov8bit DAdaptation AdaFactor# LyCORIS 训练设置$algo = "lora" # LyCORIS network algo | LyCORIS 网络算法 可选 lora、loha、lokr、ia3、dylora。lora即为locon$conv_dim = 4 # conv dim | 类似于 network_dim，推荐为 4$conv_alpha = 4 # conv alpha | 类似于 network_alpha，可以采用与 conv_dim 一致或者更小的值$dropout = "0"  # dropout | dropout 概率, 0 为不使用 dropout, 越大则 dropout 越多，推荐 0~0.5， LoHa/LoKr/(IA)^3暂时不支持# 远程记录设置$use_wandb = 0 # enable wandb logging | 启用wandb远程记录功能$wandb_api_key = "" # wandb api key | API，通过https://wandb.ai/authorize获取$log_tracker_name = "" # wandb log tracker name | wandb项目名称,留空则为"network_train"优化器选择Lion，

欠拟合或初始loss高：增大unet，repeat或epoch

过拟合或初始loss低：提高text_lr，降低学习步数repeat或epoch

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=42522fca9ecd4aa6ae586f87c2336194&docGuid=uJzwWuby77-5fb)

3、测试训练效果训练完的lora应该看下不同epoch的结果，排除欠拟合和过拟合的模型，用最合适的模型。

1) 安装插件：https://github.com/kohya-ss/sd-webui-additional-networks

2) 训练好的lora模型放到这个插件的model/lora目录下: stable-diffusion-webui/extensions/sd-webui-additional-networks/models/lora

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e3b4c4056be14146a482363dc7b40939&docGuid=uJzwWuby77-5fb)

3）直接用简单的prompts遍历所有的模型和weights

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fdee0ae2808d4f6db74259389be435ff&docGuid=uJzwWuby77-5fb)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=47230f6e269e42aaa7680da4db9b7d0c&docGuid=uJzwWuby77-5fb)

运行结果：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1ee6c4d506ff4c3bb410df96d0a093f0&docGuid=uJzwWuby77-5fb)

用模型lyf_lora-000016，选权重0.9

三、使用训练好的lora将模型lyf_lora-000016.safetensors移至目录/stable-diffusion-webui/models/Lora

刷新一下页面，然后就能在stable diffusion webui里愉快地出图啦~

声明：仅用于个人学习使用。。。。。

一些报错：1、Enable xformers for U-Netpip install -U xformers

