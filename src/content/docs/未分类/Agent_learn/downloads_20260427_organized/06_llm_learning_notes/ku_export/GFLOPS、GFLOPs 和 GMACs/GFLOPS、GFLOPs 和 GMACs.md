---
title: "GFLOPS、GFLOPs 和 GMACs"
description: "FLOPs（Floating Point Operations）：浮点运算次数，用来衡量模型计算复杂度，常用来做神经网络模型速度的间接衡量标准。GFLOPs指模型需要进行十亿（10^9）次浮点运算。理论上GFLOPs越高越好。"
date: "2026-04-27"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\GFLOPS、GFLOPs 和 GMACs\\GFLOPS、GFLOPs 和 GMACs.md"
---
# GFLOPS、GFLOPs 和 GMACs
1、定义FLOPS(Floating Point Operations Per Second)：每秒浮点运算次数，是一个衡量硬件速度的指标。GFLOPS指硬件设备每秒可以进行十亿（10^9）次浮点运算。



FLOPs（Floating Point Operations）：浮点运算次数，用来衡量模型计算复杂度，常用来做神经网络模型速度的间接衡量标准。GFLOPs指模型需要进行十亿（10^9）次浮点运算。理论上GFLOPs越高越好。



MACs(Multiply–Accumulate Operations):乘加累积操作数。通常情况下，1 MACs包含一个乘法操作与一个加法操作，大约包含2 FLOPs。GMACs指模型需要进行十亿次（10^9）乘加运算。通常情况下，GMACs与GFLOPs之间存在一个大约1:2的比例关系，因为每个乘加运算需要进行两个浮点运算（一个乘法和一个加法）。但是这个比例关系取决于具体的计算任务和计算机架构，所以并不是绝对准确的。



2、计算VGG16的GFLOPs和参数量

from thop import profileimport torchimport torchvision.models as models model = models.vgg16()device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")model.to(device)input = torch.zeros((1, 3, 224, 224)).to(device)flops, params = profile(model.to(device), inputs=(input,)) print("参数量：", params)print("FLOPS：", flops)

