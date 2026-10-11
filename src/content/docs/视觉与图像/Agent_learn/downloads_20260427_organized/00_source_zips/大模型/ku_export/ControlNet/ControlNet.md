---
title: "ControlNet"
description: "2、安装1）安装 sd-webui-controlnet插件在插件库里搜一下然后安装sd-webui-controlnet，或者直接用https://github.com/Mikubill/sd-webui-controlnet安装"
date: "2026-10-11"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\ControlNet\\ControlNet.md"
---
# ControlNet
1、作用同一个Prompt，两次生成的结果都不尽相同.ControlNet插件可以轻易的通过Prompt生成类似动作的人物的图片。

2、安装1）安装 sd-webui-controlnet插件在插件库里搜一下然后安装sd-webui-controlnet，或者直接用https://github.com/Mikubill/sd-webui-controlnet安装

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e40a5468c2404bffbe49198bd0f31d42&docGuid=oDwQKyA0GkX1zP)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2a3e3d84fbfd4518b671644f046e7776&docGuid=oDwQKyA0GkX1zP)

安装完成后应用插件并重启，能看到controlnet已经装好了

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a4ef4cfb76d648cea4a8dd50c8bb9cec&docGuid=oDwQKyA0GkX1zP)

2）下载ControlNet模型https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main

ControlNet是用来改变Stable Diffusion主模型表现的，所以有自己的参数文件。而不同的控制，当然就会有不同的参数文件。先看下有哪些预处理：

canny：边缘检测器，在提取曲线和直线上不错，但是易受噪声影响depth：深度图表征图像中目标的距离，base表示近，黑色表示远hed：适合人检测边缘生成轮廓mlsd：快速直线检测器，对于室内设计，建筑图，街景等，不要传入带人像或者曲线normal：生成表面有3d质感的图openpose：关键点pidinet：检测曲线和直线边缘，类似于hed，但通常会产生更清晰的线条和更少的细节scribble：涂鸦seg：为不同对象分类不同的颜色mlsd、depth在室内设计都不错

OpenPose该模型主要是一种快速关键点检测模型，可以提取人体姿势，如手、腿和头的位置，这样Stable Diffusion在生成图时就能参照这些姿势来生成类似的图片。更多功能参考：

下载文件control_v11p_sd15_openpose.pth 到Stable Diffusion的目录：stable-diffusion-webui\extensions\sd-webui-controlnet\models

wget https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth重启后

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=19c8cb062acb4fb48b7a605662427885&docGuid=oDwQKyA0GkX1zP)

3、使用上传一张姿势图，预处理选择OpenPose和刚下载的模型，其他保持不变，勾选允许预览，然后点击与处理后面的小太阳按钮来预览下pose

勾选启用

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=28d6e4534cd64360a51834402739b941&docGuid=oDwQKyA0GkX1zP)

重新输入提示词，进行生成，唔。。。





