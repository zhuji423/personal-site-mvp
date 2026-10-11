---
title: "StableDiffusion 基本原理"
description: "Stable Diffusion不仅是一个完全开源的模型（代码，数据，模型全部开源），而且它的参数量只有1B左右，大部分人可以在普通的显卡上进行推理甚至精调模型。毫不夸张的说，Stable Diffusion的出现和开源对AIGC的火热和发"
date: "2026-10-11"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\StableDiffusion 基本原理\\StableDiffusion 基本原理.md"
---
# StableDiffusion 基本原理
Stable Diffusion是一个文本到图像的潜在扩散模型，使用来自LAION-5B数据库子集的512x512图像进行训练。

Stable Diffusion不仅是一个完全开源的模型（代码，数据，模型全部开源），而且它的参数量只有1B左右，大部分人可以在普通的显卡上进行推理甚至精调模型。毫不夸张的说，Stable Diffusion的出现和开源对AIGC的火热和发展是有巨大推动作用的，因为它让更多的人能快速地上手AI作画。

SD基本原理SD是一个基于latent的扩散模型，它在UNet中引入text condition来实现基于文本生成图像。SD的工作核心来源于Latent Diffusion(papel)，常规的扩散模型是基于pixel的生成模型，而Latent Diffusion是基于latent的生成模型，它先采用一个autoencoder（自动编码器）将图像压缩到latent空间，然后用扩散模型来生成图像的latents，最后送入autoencoder的decoder模块就可以得到生成的图像。



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d8bdf736ffd846d38333c8a1ad9c9300&docGuid=M8V97qXwOYq-8W)

基于latent的扩散模型的优势在于计算效率更高效，因为图像的latent空间要比图像pixel空间要小，这也是SD的核心优势。文生图模型往往参数量比较大，基于pixel的方法往往限于算力只生成64x64大小的图像，比如OpenAI的DALL-E2和谷歌的Imagen，然后再通过超分辨模型将图像分辨率提升至256x256和1024x1024；而基于latent的SD是在latent空间操作的，它可以直接生成256x256和512x512甚至更高分辨率的图像。

SD模型结构如下图所示，主要包括三个模型：

CLIP text encoder：提取输入text的text embeddings ，通过cross attention方式送入扩散模型的UNet中作为condition。具体的是采用目前OpenAI所开源的最大CLIP模型：clip-vit-large-patch14。UNet：扩散模型的主体，用来实现文本引导下的latent生成。autoencoder（VAE）：encoder将图像压缩到latent空间，而decoder将latent解码为图像；![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=71db216b60a14ad49ef656ae8549571d&docGuid=M8V97qXwOYq-8W)

对于SD模型，其autoencoder模型参数大小为84M，CLIP text encoder模型大小为123M，而UNet参数大小为860M，所以SD模型的总参数量约为1B。

CLIP text encoder文本编码器负责将输入提示（例如“An astronaut riding a horse”）转换为text embeddings，以便U-Net能够理解。它通常是一个简单的基于transformer的编码器，将一系列输入tokens映射到一系列latent text embeddings。受Imagen启发，SD在训练期间不训练文本编码器，而是直接使用已经训练好的CLIP文本编码器CLIPTextModel。

UNetU-Net模型由编码器和解码器两个部分组成，每个部分都由ResNet块组成。编码器将图像表示压缩为较低分辨率的图像表示，而解码器将较低分辨率的图像表示解码回原始的高分辨率图像表示，这样做可以减少噪声。更具体地说，U-Net输出预测噪声残差，可以用来计算预测去噪图像表示。为了防止U-Net在降采样时丢失重要信息，通常在编码器的下采样ResNet和解码器的上采样ResNet之间添加短路连接。此外，稳定扩散U-Net能够通过交叉注意力层将其输出与文本嵌入条件化。通常在ResNet块之间将交叉注意力层添加到U-Net的编码器和解码器部分。

autoencoder（VAE）VAE模型由编码器和解码器两部分组成。编码器用于将图像转换为低维潜在表示（latent），作为U-Net模型的输入。相反，解码器将潜在表示转换回图像。

在潜在扩散训练期间，编码器用于获取图像的潜在表示，以进行正向扩散过程，该过程在每个步骤中应用更多的噪声。在推理期间，通过反向扩散过程生成的去噪潜变量使用VAE解码器转换回图像。正如我们将在推理期间看到的那样，我们只需要VAE解码器。

SD推理过程|  | 首先根据输入text，用text encoder提取text embeddings，同时初始化一个随机噪音noise（latent上的，512x512图像对应的noise维度为64x64x4），然后将text embeddings和noise送入扩散模型UNet中生成去噪后的latent（多步迭代的去噪），最后送入autoencoder的decoder模块得到生成的图像. |
| --- | --- |



