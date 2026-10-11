---
title: "经典StableDiffusion模型"
description: "其他模型都需要和主模型搭配使用。"
date: "2026-04-27"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\经典StableDiffusion模型\\经典StableDiffusion模型.md"
---
# 经典StableDiffusion模型
五种主要模型分类| 模型分类 | 模型介绍 | 训练成本 | 体积 | 文件后缀 |
| --- | --- | --- | --- | --- |
| Dreambooth checkpoint（常用） | 主模型可以分为基础大模型和基于基础大模型fine-tuning的微调大模型，需要大量图片作为训练样本。一般微调的大模型可以分为二大类：写实类（人物、风景）和 二次元类（2d、2.5d、3d等）。 | 高，大量图片，高硬件配置，个人较难训练 | 2G+ | *.ckpt, *.safetensors |
| LoRA（常用） | 全名：Low-Rank Adaptation作用：生成特定的人物/物体或特定风格的图像LoRA是在主模型的基础上进行训练的小模型，可以多个LoRA合并使用，可调节不同LoRA的权重。特点：轻巧，训练高效，针对性比较强 | 低，个人电脑可以训练，20mins-2hour | 几十-几百M | *.pt, *.safetensors |
| Textual Inversion | 简称embedding，可以用来调整程序对文本理解能力 | 个人可以训练 | 几十-几百K | *.pt, images |
| Hypernetwork | 网络风格模型，常用于画风、效果的转换，但同样也可以用于生成指定的角色。Hypernetwork在一些比较精细的效果上不是特别出众，所以现在在使用度上也越来越少了。 | 个人可以训练 | 几百M | *.pt, *.ckpt, *.safetensors |
| VAE（Aesthetic Embedding Aesthetic Gradient） | 风格嵌入，美学嵌入模型，类似于滤镜作用 | 个人可以训练 | 几百M |  |
| 其他 | 插件类型的模型，适用于单一场景 | - |  |  |

其他模型都需要和主模型搭配使用。

一般下载时会有几种后缀模型文件可选择，作用都一样。但*.safetensors 后缀的更安全，推荐直接下载此后缀的使用，但早期训练的一些主要是*.ckpt后缀的。

主模型推荐| 分类 | 模型 | 大小 | 描述 | 风格 | 地址 |
| --- | --- | --- | --- | --- | --- |
| 2D | MeinaMix | 3.28G | 2D就选它！ |  | https://civitai.com/models/7240/meinamix |
| 2.5D | FaceBombMix | 1.99G | 脸部细节绝了 |  | https://civitai.com/models/7152/facebombmix |
| 3D | ReV Animated | 5.13G | 顶级3D生产力，配合lora更牛逼！ |  | https://civitai.com/models/7371/rev-animated |
| 写实 | ChilloutMix | 3.97G | 大名鼎鼎的亚洲美女模型。市面上你看到的大量的AI美女，基本上都是这个模型生成的。 |  | https://civitai.com/models/6424/chilloutmix |
| 写实 | AWPortrait | 1.99G | 艺术照。偏向于艺术风。 |  | https://civitai.com/models/61170/awportrait |
| 万能 | Deliberate | 1.99G | 啥都行，万金油。风格上偏油画和数绘风格。值得注意的是，这个模型的提示词必须非常详细地填写。 |  | https://civitai.com/models/4823?modelVersionId=15236 |



Stable Diffusion 爆款人气模型评测（2/2.5次元篇）

