---
title: "StableDiffusion使用"
description: "二、简单使用chekpoint1、不同风格模型C站 civitaiC站: https://civitai.com，常用的有两种：主要用得到的模型文件就两种，一种是CKPT，一种是lora。"
date: "2026-04-28"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\StableDiffusion使用\\StableDiffusion使用.md"
---
# StableDiffusion使用
一、安装参考：

二、简单使用chekpoint1、不同风格模型C站 civitaiC站: https://civitai.com，常用的有两种：主要用得到的模型文件就两种，一种是CKPT，一种是lora。 

CKPT：经过训练的图片合集，被称作模型，也就是chekpoint。模型体积较大，一般真人版的单个模型的大小在7GB左右，动漫版的在2-5个G之间。 推荐：ReV Animated（顶级3D生产力）、MeinaMix（2D就选它）、ChilloutMix（亚洲美女写实模型库），更多：。Lora：是一种体积较小的绘画模型，是对大模型的微调。与每次作画只能选择一个大模型不同，lora模型可以在已选择大模型的基础上添加一个甚至多个。一般体积在几十到几百兆左右。 可以简单的将其理解为—— lora模型就像 主模型的风格滤镜。它的加载方式就像是游戏中的 MOD补丁、DLC扩展包 。图片模型与参数选自己喜欢的风格图片点进去，https://civitai.com/models/7240/meinamix

跟着点击某张图片进去，在右边面板上有它使用的Prompt和Negative prompt等参数。

![](/personal-site-mvp/img/doc-placeholder.svg)

点击右下角copy得到参数：

1girl,red hair, flaming eye, katana, flames, burning houses, glowing, sidelighting, wallpaper,Negative prompt: (worst quality, low quality:1.4), (zombie, sketch, interlocked fingers, comic),Steps: 40, Size: 512x1024, Seed: 519946054, Model: Meina V10 - baked VAE, Version: v1.2.1, Sampler: DPM++ SDE Karras, CFG scale: 7, Clip skip: 2, Model hash: 77b7dc4ef0, Hires steps: 15, Hires upscale: 2, Hires upscaler: R-ESRGAN 4x+ Anime6B, Denoising strength: 0.42、安装模型1）点击Civirai Helper——填写地址比如：https://civitai.com/models/7240/meinamix——点击获取模型Get Model Info by Civitai Url

2）选择子文件夹——选择模型版本——点击下载模型

![](/personal-site-mvp/img/doc-placeholder.svg)

慢慢等待，在日志能看到进度，默认CKPT下载目录是stable-diffusion-webui/models/Stable-diffusion/xxx.safetensors，Lora下载目录是stable-diffusion-webui/models/Lora/xxx.safetensors

![](/personal-site-mvp/img/doc-placeholder.svg)

下载完成后，模型中选择刚刚下载的，就可以制作图了

3、使用prompt生成相同风格图在提示词中粘入参数

1girl,red hair, flaming eye, katana, flames, burning houses, glowing, sidelighting, wallpaper,Negative prompt: (worst quality, low quality:1.4), (zombie, sketch, interlocked fingers, comic),Steps: 40, Size: 512x1024, Seed: 519946054, Model: Meina V10 - baked VAE, Version: v1.2.1, Sampler: DPM++ SDE Karras, CFG scale: 7, Clip skip: 2, Model hash: 77b7dc4ef0, Hires steps: 15, Hires upscale: 2, Hires upscaler: R-ESRGAN 4x+ Anime6B, Denoising strength: 0.4点击生成下面的第一个箭头按钮，会自动读取参数

![](/personal-site-mvp/img/doc-placeholder.svg)

点击生成，1280*1024出图大概5s

![](/personal-site-mvp/img/doc-placeholder.svg)

![](/personal-site-mvp/img/doc-placeholder.svg)

三、使用lora详情见：

作用：同画风、同人物风格、同服饰风格、特定元素

四、使用ControlNet详情见：

作用：同姿势图片、同面部表情、线稿上色、建筑渲染、图像扩展、画质修复

五、进阶使用1、自定义图片姿势同上，第四部分这个例子就是

2、线稿生成图片（懒人福音）实例1：

唔。。。像，太像了

实例2：再用自己之前画的线稿试试，大概思路和实例1差不多，就是图生图，controlNet用danny，把相似度控制一下

可以看出来画手还是不太行，细节不能看，需要再局部绘制，但是懒得改了。。

3、局部绘制（P掉某个人）使用图生图的局部绘制功能，上传图片后，鼠标会变成一个黑色的画笔，半径大小可以点击右方的笔一样的按钮来调整。将要去掉的部分涂黑后点击生成。

这下可以快乐p掉游客照中的路人了2333

4、生成式填充（图片扩展）ControlNet升级到1.2.224或以上版本才能用

在stable-diffusion-webui/extensions/sd-webui-controlnet/models目录下载相关模型文件

sudo wget https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint.pth图生图中修改controlnet参数

5、深度换脸在扩展插件中，安装插件：https://github.com/s0md3v/sd-webui-roop

![](/personal-site-mvp/img/doc-placeholder.svg)

试了几个插件，感觉效果都不好，最好的方式是用人物几十张照片自己练lora，非常相似，可以用来做艺术照生成，涉及到隐私模型慎重不要分享，再次警告只做个人学习使用⚠️，过程可参考：

6、一些使用场景瞎设想艺术照生成（上传几张照片生成艺术照）小天才画家（把小孩子的涂鸦转为3d）表情制作生成器（gif版需要结合其他工具）Q版形象生成（上传动漫截图，产出Q版头像，是否版权问题？）绘本制作（可结合gpt自动生成故事走向快速选定或自己写故事走向生成画面，难点在于形象的前后一致性）ip设计广告图生成（假人模特秒变大美女、大帅哥）| 小天才画家 |  | stable diffusion 使用controlnet，基础模型选择一个3d的 |
| --- | --- | --- |
| 表情制作生成器 |  |  |
| Q版形象生成 |  |  |
| 绘本制作 |  |  |
| ip设计 |  |  |
| 广告图生成 |  |  |

SD真真生产力工具，还有很多用法，自己搜吧，都差不多。。。。

适合前端小伙伴可以🍠搜icon生成、海报制作，有很多不错的思路，大概用到的知识（lora、controlnet）基本本篇文章都有介绍～



六、一些相关工作

这个系列都可以看看



![](/personal-site-mvp/img/doc-placeholder.svg)



