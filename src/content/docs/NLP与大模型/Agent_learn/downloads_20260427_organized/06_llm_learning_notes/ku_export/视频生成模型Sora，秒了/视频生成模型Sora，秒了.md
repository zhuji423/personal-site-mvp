---
title: "视频生成模型Sora，秒了"
description: "看视频效果，我们已经很难区分这些视频是来自于Sora生成，还是电影、纪录片、游戏、动漫这些经过高成本制作的精美内容的片段。"
date: "2026-04-28"
category: "NLP与大模型"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\视频生成模型Sora，秒了\\视频生成模型Sora，秒了.md"
---
# 视频生成模型Sora，秒了
1、突破在这之前视频生成的天花板是Runway，支持最多18s视频生成，镜头相对固定，与其说是视频，不如说是动图，且效果较差，至于pika更不用说。虽然Runway上次更新也有视频生成迎来GPT时刻的说法，但实际上还是一个不太可用的玩具水平，而Sora是真正迎来了视频生成的GPT时刻。

看视频效果，我们已经很难区分这些视频是来自于Sora生成，还是电影、纪录片、游戏、动漫这些经过高成本制作的精美内容的片段。

![](/personal-site-mvp/img/doc-placeholder.svg)

2、应用text-video1、给定文本描述生成视频画面image-video2、基于静态图片生成动图视频video-video3、视频到视频的转场过渡4、视频前后扩展5、语言控制视频风格的改变

| 分类 | 功能 | 输入 | 输出 | 备注 |
| --- | --- | --- | --- | --- |
| text-video | 1、给定文本描述生成视频画面 | 文本Prompt: Photorealistic closeup video of two pirate ships battling each other as they sail inside a cup of coffee.
逼真的特写视频，展示两艘海盗船在一杯咖啡内航行时互相争斗的情况。 |  | 不符合现实规律的视频也能生成 |
| image-video | 2、基于静态图片生成动图视频 | 图片：文本Prompt: A Shiba Inu dog wearing a beret and black turtleneck.
一只戴着贝雷帽和黑色高领毛衣的柴犬。 |  |  |
| video-video | 3、视频到视频的转场过渡 | 视频开头：视频结尾： | 视频过渡： | 将毫不相关的两个视频丝滑过渡到一起 |
|  | 4、视频前后扩展 | 同一视频向前扩展，可以看到2个视频最终的画面是一致的 |  | 可以使用此方法向前和向后扩展视频以产生无缝的无限循环 |
|  | 5、语言控制视频风格的改变 | 原始视频： | prompt：make it have dinosaurs 出现恐龙 prompt：make it claymation animation style 粘土动画风格 |  |



3、实现论文地址： https://openai.com/research/video-generation-models-as-world-simulators

核心技术：transformer+diffusion结构

1）将视频数据转化为patchespatches相当于语言模型tokenes的概念，语言模型通过已知tokens预测下一个tokens，Sora通过已知patches预测下一个patches

![](/personal-site-mvp/img/doc-placeholder.svg)

将原始视频作为输入，并输出在时间和空间上压缩的潜在表示latent space 。同时得到解码器decoder。

2）基于patches进行训练Sora 在这个压缩的潜在空间中，针对一系列latent space 进行训练。

3）通过diffusion还原画面![](/personal-site-mvp/img/doc-placeholder.svg)

根据已知已知patches预测下一个patches得到latent space，通过decoder映射回像素空间，并通过diffusion扩散模型进一步还原画面。



官网：https://openai.com/sora

参考： https://yunyinghui.feishu.cn/wiki/BaCEwe3AliqYERkc9dVcfW0BnXg

