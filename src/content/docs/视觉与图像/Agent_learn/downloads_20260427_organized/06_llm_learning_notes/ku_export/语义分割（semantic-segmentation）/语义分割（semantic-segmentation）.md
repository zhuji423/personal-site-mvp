---
title: "语义分割（semantic-segmentation）"
description: "1、支持的算法DeepLabV3（）FCN（）LRASPP2、应用from torchvision.io.image import readimagefrom torchvision.models.segmentation import f"
date: "2026-04-28"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\语义分割（semantic-segmentation）\\语义分割（semantic-segmentation）.md"
---
# 语义分割（semantic-segmentation）
这里以torchvision库为例，其他也可用

1、支持的算法DeepLabV3（*）FCN（*）LRASPP2、应用from torchvision.io.image import read_imagefrom torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weightsfrom torchvision.transforms.functional import to_pil_imageimg = read_image("gallery/assets/dog1.jpg")# Step 1: Initialize model with the best available weightsweights = FCN_ResNet50_Weights.DEFAULTmodel = fcn_resnet50(weights=weights)model.eval()# Step 2: Initialize the inference transformspreprocess = weights.transforms()# Step 3: Apply inference preprocessing transformsbatch = preprocess(img).unsqueeze(0)# Step 4: Use the model and visualize the predictionprediction = model(batch)["out"]normalized_masks = prediction.softmax(dim=1)class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta["categories"])}mask = normalized_masks[0, class_to_idx["dog"]]to_pil_image(mask).show()3、效果在 COCO val2017的子集,Pascal VOC数据集中存在的20个类别上评估：

| Weight | Mean IoU | pixelwise Acc | Params | GFLOPS | Recipe |
| --- | --- | --- | --- | --- | --- |
| DeepLabV3_MobileNet_V3_Large_Weights.COCO_WITH_VOC_LABELS_V1 | 60.3 | 91.2 | 11.0M | 10.45 | link |
| DeepLabV3_ResNet101_Weights.COCO_WITH_VOC_LABELS_V1 | 67.4 | 92.4 | 61.0M | 258.74 | link |
| DeepLabV3_ResNet50_Weights.COCO_WITH_VOC_LABELS_V1 | 66.4 | 92.4 | 42.0M | 178.72 | link |
| FCN_ResNet101_Weights.COCO_WITH_VOC_LABELS_V1 | 63.7 | 91.9 | 54.3M | 232.74 | link |
| FCN_ResNet50_Weights.COCO_WITH_VOC_LABELS_V1 | 60.5 | 91.4 | 35.3M | 152.72 | link |
| LRASPP_MobileNet_V3_Large_Weights.COCO_WITH_VOC_LABELS_V1 | 57.9 | 91.2 | 3.2M | 2.09 | link |

4、应用与可视化更多详情参考：

(1)太长不看import torchimport numpy as npfrom torchvision.io import read_imagefrom pathlib import Pathimport matplotlib.pyplot as pltimport torchvision.transforms.functional as Ffrom torchvision.utils import draw_segmentation_masksfrom torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weightsdef show(imgs):    if not isinstance(imgs, list):        imgs = [imgs]    fig, axs = plt.subplots(ncols=len(imgs), squeeze=False)    for i, img in enumerate(imgs):        img = img.detach()        img = F.to_pil_image(img)        axs[0, i].imshow(np.asarray(img))        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])dog1_int = read_image(str(Path('data') / 'cat_dog.jpg'))dog_list = [dog1_int]weights = FCN_ResNet50_Weights.DEFAULTtransforms = weights.transforms(resize_size=None)model = fcn_resnet50(weights=weights, progress=False)model = model.eval()batch = torch.stack([transforms(d) for d in dog_list])output = model(batch)['out']normalized_masks = torch.nn.functional.softmax(output, dim=1)class_dim = 1num_classes = normalized_masks.shape[1]all_classes_masks = normalized_masks.argmax(class_dim) == torch.arange(num_classes)[:, None, None, None]print(f"shape = {all_classes_masks.shape}, dtype = {all_classes_masks.dtype}")# The first dimension is the classes now, so we need to swap itall_classes_masks = all_classes_masks.swapaxes(0, 1)dogs_with_masks = [    draw_segmentation_masks(img, masks=mask, alpha=.6)    for img, mask in zip(dog_list, all_classes_masks)]show(dogs_with_masks)![](/personal-site-mvp/img/doc-placeholder.svg)

(2)详细解释使用 FCN Resnet-50 模型。

from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weightsweights = FCN_ResNet50_Weights.DEFAULTtransforms = weights.transforms(resize_size=None)model = fcn_resnet50(weights=weights, progress=False)model = model.eval()batch = torch.stack([transforms(d) for d in dog_list])output = model(batch)['out']print(output.shape, output.min().item(), output.max().item())分割模型的输出是形状为(batch_size, num_classes, H, W)的张量 。每个值都是一个非标准化分数，使用 softmax 将它们标准化[0, 1]，表示给定像素属于给定类别的可能性有多大。

绘制已检测到的狗和猫的掩模：

sem_class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta["categories"])}normalized_masks = torch.nn.functional.softmax(output, dim=1)dog_and_boat_masks = [    normalized_masks[img_idx, sem_class_to_idx[cls]]    for img_idx in range(len(dog_list))    for cls in ('dog', 'cat')]show(dog_and_boat_masks)![](/personal-site-mvp/img/doc-placeholder.svg)

模型对狗分类有信心，但对猫分类则不太有信心。

torchvision.utils.draw_segmentation_masks 函数可用于在原始图像上绘制这些蒙版。该函数期望掩码为布尔掩码，但上面的掩码为[0, 1]的概率。要获得布尔掩码，可以执行以下操作：

class_dim = 1boolean_dog_masks = (normalized_masks.argmax(class_dim) == sem_class_to_idx['dog'])print(f"shape = {boolean_dog_masks.shape}, dtype = {boolean_dog_masks.dtype}")show([m.float() for m in boolean_dog_masks])现在使用布尔掩码将 draw_segmentation_masks()绘制在原始图像之上：

from torchvision.utils import draw_segmentation_masksdogs_with_masks = [    draw_segmentation_masks(img, masks=mask, colors=["red"], alpha=0.7)    for img, mask in zip(dog_list, boolean_dog_masks)]show(dogs_with_masks)![](/personal-site-mvp/img/doc-placeholder.svg)

为单个图像绘制掩模：

num_classes = normalized_masks.shape[1]dog1_masks = normalized_masks[0]class_dim = 0dog1_all_classes_masks = dog1_masks.argmax(class_dim) == torch.arange(num_classes)[:, None, None]print(f"dog1_masks shape = {dog1_masks.shape}, dtype = {dog1_masks.dtype}")print(f"dog1_all_classes_masks = {dog1_all_classes_masks.shape}, dtype = {dog1_all_classes_masks.dtype}")dog_with_all_masks = draw_segmentation_masks(dog1_int, masks=dog1_all_classes_masks, alpha=.6)show(dog_with_all_masks)![](/personal-site-mvp/img/doc-placeholder.svg)

在上图中看到只绘制了 2 个遮罩：背景遮罩和狗遮罩。这是因为该模型认为只有这 2 个类别是所有像素中最有可能的类别。如果模型检测到另一个类是其他像素中最有可能的，就会在上面看到它的掩模。

背景类是索引为0的类，删除背景蒙版:masks=dog1_all_classes_masks[1:]

为整批图像绘制掩模：

class_dim = 1all_classes_masks = normalized_masks.argmax(class_dim) == torch.arange(num_classes)[:, None, None, None]print(f"shape = {all_classes_masks.shape}, dtype = {all_classes_masks.dtype}")# The first dimension is the classes now, so we need to swap itall_classes_masks = all_classes_masks.swapaxes(0, 1)dogs_with_masks = [    draw_segmentation_masks(img, masks=mask, alpha=.6)    for img, mask in zip(dog_list, all_classes_masks)]show(dogs_with_masks)![](/personal-site-mvp/img/doc-placeholder.svg)



