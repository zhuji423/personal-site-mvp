---
title: "安装GPU版pytorch"
description: "安装GPU版pytorch"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\Nvidia Docker_引用文档\\安装GPU版pytorch.md"
---
安装GPU版pytorch

### 1、cuda
![](/personal-site-mvp/img/doc-placeholder.svg "")
cuda版本 12.0

### 2、pytorch
[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

![](/personal-site-mvp/img/doc-placeholder.svg "")
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```
检查是否安装成功

```
import torch
print(torch.cuda.is_available())
exit()
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
注：mac m1不是cuda是mps，用  print(torch.backends.mps.is_available())

查看gpu使用情况：每隔一秒刷新

```
watch -n 1 nvidia-smi  
```

