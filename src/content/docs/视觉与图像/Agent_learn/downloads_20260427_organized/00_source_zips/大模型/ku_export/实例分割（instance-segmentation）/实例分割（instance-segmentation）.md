---
title: "实例分割（instance-segmentation）"
description: "1、支持的算法Mask R-CNN（）2、效果在 COCO val2017上的Box and Mask MAPs："
date: "2026-10-11"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\实例分割（instance-segmentation）\\实例分割（instance-segmentation）.md"
---
# 实例分割（instance-segmentation）
这里以torchvision库为例，其他也可用

1、支持的算法Mask R-CNN（*）2、效果在 COCO val2017上的Box and Mask MAPs：

| Weight | Box MAP | Mask MAP | Params | GFLOPS | Recipe |
| --- | --- | --- | --- | --- | --- |
| MaskRCNN_ResNet50_FPN_V2_Weights.COCO_V1 | 47.4 | 41.8 | 46.4M | 333.58 | link |
| MaskRCNN_ResNet50_FPN_Weights.COCO_V1 | 37.9 | 34.6 | 44.4M | 134.38 | link |

3、应用与可视化更多详情参考：

（1）太长不看import torchimport numpy as npfrom torchvision.io import read_imagefrom pathlib import Pathimport matplotlib.pyplot as pltimport torchvision.transforms.functional as Ffrom torchvision.utils import draw_segmentation_masksfrom torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weightsdef show(imgs):    if not isinstance(imgs, list):        imgs = [imgs]    fig, axs = plt.subplots(ncols=len(imgs), squeeze=False)    for i, img in enumerate(imgs):        img = img.detach()        img = F.to_pil_image(img)        axs[0, i].imshow(np.asarray(img))        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])dog1_int = read_image(str(Path('data') / 'cat_dog.jpg'))dog_list = [dog1_int]weights = MaskRCNN_ResNet50_FPN_Weights.DEFAULTtransforms = weights.transforms()model = maskrcnn_resnet50_fpn(weights=weights, progress=False)model = model.eval()images = [transforms(d) for d in dog_list]output = model(images)print(output)proba_threshold = 0.5score_threshold = .75boolean_masks = [    out['masks'][out['scores'] > score_threshold] > proba_threshold    for out in output]dogs_with_masks = [    draw_segmentation_masks(img, mask.squeeze(1))    for img, mask in zip(dog_list, boolean_masks)]show(dogs_with_masks)![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01df1ed3c62749da9f28769b9a596a80&docGuid=WC4AbEPlB8v2pY)

（2）详细解释使用Mask-RCNN 模型。

from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weightsweights = MaskRCNN_ResNet50_FPN_Weights.DEFAULTtransforms = weights.transforms()images = [transforms(d) for d in dog_list]model = maskrcnn_resnet50_fpn(weights=weights, progress=False)model = model.eval()output = model(images)print(output)对于批次中的每个图像，模型输出一些检测（或实例）。每个输入图像的检测数量各不相同。每个实例都由其边界框、标签、分数和掩码来描述。

输出的组织方式如下：输出是一个长度为batch_size的列表。列表中的每个条目对应一个输入图像，它是一个带有“boxes”、“labels”、“scores”和“masks”键的字典。与这些键关联的每个值都包含num_instances元素。在上面的例子中，第一个图像中检测到 3 个实例，第二个图像中检测到 2 个实例。

实例分割的掩码和语义分割模型的掩码有很大不同。

dog1_output = output[0]dog1_masks = dog1_output['masks']print(f"shape = {dog1_masks.shape}, dtype = {dog1_masks.dtype}, "      f"min = {dog1_masks.min()}, max = {dog1_masks.max()}")这里的掩码对应于概率，表明对于每个像素，它属于该实例的预测标签的可能性有多大。这些预测的标签对应于同一输出字典中的“标签”元素。

查看为第一张图像的实例预测了哪些标签。

print("For the first dog, the following instances were detected:")print([weights.meta["categories"][label] for label in dog1_output['labels']])继续绘制这些蒙版。由于draw_segmentation_masks() 需要布尔掩码，需要将这些概率转换为布尔值。这些掩码的语义是“该像素属于预测类别的可能性有多大？”。因此，将这些掩码转换为布尔值的一种自然方法是使用 0.5 的概率对它们进行阈值处理。

proba_threshold = 0.5dog1_bool_masks = dog1_output['masks'] > proba_thresholdprint(f"shape = {dog1_bool_masks.shape}, dtype = {dog1_bool_masks.dtype}")# There's an extra dimension (1) to the masks. We need to remove itdog1_bool_masks = dog1_bool_masks.squeeze(1)show(draw_segmentation_masks(dog1_int, dog1_bool_masks, alpha=0.9))![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7783b93f9e9f4aae8c5978883ebdbd43&docGuid=vOjw4s4B0Cgjd8)

该模型似乎正确地检测到了狗，但它也将树与人混淆了。

print(dog1_output['scores'])
# tensor([0.9987, 0.7187, 0.6525], grad_fn=<IndexBackward0>)在绘制掩模时，可以只要求那些得分较高的掩模。在这里使用 0.75 的分数阈值，并绘制第二只狗的掩模。

score_threshold = .75boolean_masks = [    out['masks'][out['scores'] > score_threshold] > proba_threshold    for out in output]dogs_with_masks = [    draw_segmentation_masks(img, mask.squeeze(1))    for img, mask in zip(dog_list, boolean_masks)]show(dogs_with_masks)![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3c5f6de633ed4d3e98149c2b636763ce&docGuid=vOjw4s4B0Cgjd8)





