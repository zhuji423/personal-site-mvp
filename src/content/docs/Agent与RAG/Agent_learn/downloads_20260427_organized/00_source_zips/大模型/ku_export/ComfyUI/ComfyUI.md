---
title: "ComfyUI"
description: "ComfyUI 使用户能够通过链接不同的块（称为节点）来构建复杂的图像生成工作流程。这些节点可以包括各种任务，如加载检查点模型、输入提示、指定采样器等。ComfyUI 实际上就是一个比较专业的 Stable Diffusion 运行界面，只"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\ComfyUI\\ComfyUI.md"
---
# ComfyUI
自从AI绘画StableDiffusion开源以后，就有社区开发者推出了方便用户使用的图形界面，其中就一款就是最常见的WebUI，但要论专业度还得是ComfyUI，这是一款专业程度较高的StableDiffusion图形界面，它收到了全球AI创作者的追捧，但与WebUI不同的是，ComfyUI是节点式工作流。项目地址：https://github.com/comfyanonymous/ComfyUI一、介绍ComfyUI 是一个为 Stable Diffusion 专门设计的基于节点的图形用户界面（GUI）。

ComfyUI 使用户能够通过链接不同的块（称为节点）来构建复杂的图像生成工作流程。这些节点可以包括各种任务，如加载检查点模型、输入提示、指定采样器等。ComfyUI 实际上就是一个比较专业的 Stable Diffusion 运行界面，只不过是节点式的。

二、安装

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c5fd79fc045c472db66a784f613ff1d2&docGuid=toFfQY4OG03GUv)

三、使用以FLUX.1-dev使用为例

1、下载模型unet模型flux1-dev.safetensors建议使用modelscope能快一些，且不容易下载中断，模型：FLUX.1-dev

from modelscope.hub.file_download import model_file_downloaddef download_file(model_id, file):    """    下载模型    """    model_file_download(model_id=model_id, file_path=file, cache_dir='.')if __name__ == '__main__':    download_file('AI-ModelScope/FLUX.1-dev', 'flux1-dev.safetensors')运行脚本，完成下载后将flux1-dev.safetensors文件(23G)复制到ComfyUI/models/unet/目录下

mv AI-ModelScope/FLUX___1-dev/flux1-dev.safetensors ComfyUI/models/unet/vae模型ae.safetensorsfrom modelscope.hub.file_download import model_file_downloaddef download_file(model_id, file):    """    下载模型    """    model_file_download(model_id=model_id, file_path=file, cache_dir='.')if __name__ == '__main__':    download_file('AI-ModelScope/FLUX.1-dev', 'ae.safetensors')完成下载后将ae.safetensors文件(335M)复制到ComfyUI/models/vae/目录下

mv AI-ModelScope/FLUX___1-dev/ae.safetensors ComfyUI/models/vae/clip模型flux_text_encoders 模型：flux_text_encoders

from modelscope.hub.file_download import model_file_downloaddef download_file(model_id, file):    """    下载模型    """    model_file_download(model_id=model_id, file_path=file, cache_dir='.')if __name__ == '__main__':    download_file('AI-ModelScope/flux_text_encoders', 'clip_l.safetensors')    download_file('AI-ModelScope/flux_text_encoders', 't5xxl_fp16.safetensors')    # download_file('AI-ModelScope/flux_text_encoders', 't5xxl_fp8_e4m3fn.safetensors')完成下载后将clip_l.safetensors(246M)、t5xxl_fp16.safetensors(9.79G)、t5xxl_fp8_e4m3fn.safetensors(4.89G)这3个文件复制到ComfyUI/models/clip/目录下

t5xxl_fp16和t5xxl_fp8_e4m3fn只要挑一个下载就行，fp16效果更好，fp8配置要求更低，这里我只用了t5xxl_fp16

mv AI-ModelScope/flux_text_encoders/clip_l.safetensors ComfyUI/models/clip/mv AI-ModelScope/flux_text_encoders/t5xxl_fp16.safetensors ComfyUI/models/clip/loar模型（可选）模型：flux-lora-collection

目前Xlabs-AI团队放出的七款Lora模型，分别是动漫，艺术、迪士尼、MJV6、毛绒、写实、风景。下载所需要的loar模型文件放置到ComfyUI\models\loras目录下。

更多模型资源 C站 civitai除了以上的官方基础模型，也可以在c站使用别人训练好的lora和checkpoint

https://civitai.com/search/models?baseModel=Flux.1%20D&modelType=LORA&modelType=Checkpoint&sortBy=models_v9&query=flux

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5ca83107c3c34402b9ff0949f7a22a65&docGuid=toFfQY4OG03GUv)

C站常用的模型有两种：一种是CKPT，一种是lora。 

CKPT：经过训练的图片合集，被称作模型，也就是chekpoint。模型体积较大，一般单个模型的大小在几个GB左右Lora：是一种体积较小的绘画模型，是对大模型的微调。与每次作画只能选择一个大模型不同，lora模型可以在已选择大模型的基础上添加一个甚至多个。一般体积在几十到几百兆左右。 可以简单的将其理解为—— lora模型就像 主模型的风格滤镜。2、使用加载工作流配置文件点击界面load加载工作流配置

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e1217ab13653489eb9d3fe28201bfc7d&docGuid=toFfQY4OG03GUv)

至此，Flux.1的ComfyUI工作流就可以应用了。更改prompt，点击queue prompt加入生成队列，开始生成。

完成生成后右键点击图片，进行更多操作

an inflatable white model of the Arc de Triomphe in Paris, huge and fluffy, drone shot, drone footage, hyper realistic巴黎凯旋门的白色充气模型，巨大而蓬松，无人机拍摄，无人机镜头，超现实一次生成4张512*512:

Trump is holding a table tennis racket and Biden is swinging a badminton racket. A close-up shows the badminton hitting Trump in the face.川普拜登乒乓球大战羽毛球![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=69ab5e070f66484bb2ed8b0a8aee2a65&docGuid=toFfQY4OG03GUv)

