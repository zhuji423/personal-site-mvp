---
title: "torchvision"
description: "简介torchvision是pytorch的一个图形库，它服务于PyTorch深度学习框架的，主要用来构建计算机视觉模型。以下是torchvision的构成："
date: "2026-04-27"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\torchvision库\\torchvision库.md"
---
# torchvision
官网：https://pytorch.org/vision/stable/index.html

简介torchvision是pytorch的一个图形库，它服务于PyTorch深度学习框架的，主要用来构建计算机视觉模型。以下是torchvision的构成：

torchvision.datasets: 一些加载数据的函数及常用的数据集接口，设计上继承 torch.utils.data.Dataset，主要包括：MNIST、CIFAR10/100、ImageNet、COCO等。torchvision.models: 包含常用的模型结构（含预训练模型），例如AlexNet、VGG、ResNet等；torchvision.transforms: 常用的图片变换，例如裁剪、旋转等；torchvision.utils: 其他的一些有用的方法。torchvision.datasets在这个包中提前处理好了很多图片数据集：

MNISTCOCOCaptionsDetectionLSUNImageFolderImagenet-12CIFARSTL10SVHNPhotoTour所有数据集详情： https://pytorch.org/vision/stable/datasets.html#

以minist加载为例：

def load_data():    """    数据集读取器    """    transform = transforms.Compose([        transforms.ToTensor(),        # 0.1307和0.3081是mnist数据集的均值和标准差，由数据集提供方给出        transforms.Normalize((0.1307,), (0.3081,))    ])    train_dataset = datasets.MNIST(root='../dataset/mnist/', train=True, download=True, transform=transform)    train_loader = DataLoader(train_dataset, shuffle=True, batch_size=BATCH_SIZE)    test_datasets = datasets.MNIST(root='../dataset/mnist/', train=False, download=True, transform=transform)    test_loader = DataLoader(test_datasets, shuffle=False, batch_size=BATCH_SIZE)    return train_loader, test_loadertorchvision.models子模块中包含以下模型结构：

AlexNetVGGResNetSqueezeNetDenseNet通过pretrined=True可以加载预训练模型。pretrained默认值是False，不赋值和赋值False效果一样。

import torchvision.models as modelsresnet18 = models.resnet18(pretrained=True)vgg16 = models.vgg16(pretrained=True)alexnet = models.alexnet(pretrained=True)squeezenet = models.squeezenet1_0(pretrained=True)densenet = models.densenet_161()torchvision.transformstorchvision.transforms主要是用于常见的一些图形变换。

torchvision.transforms.Compose()类。这个类的主要作用是串联多个图片变换的操作。

# 图像预处理步骤transform = transforms.Compose([    transforms.Resize(96), # 缩放到 96 * 96 大小    transforms.ToTensor(), # 转化为Tensor    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)) # 归一化])

