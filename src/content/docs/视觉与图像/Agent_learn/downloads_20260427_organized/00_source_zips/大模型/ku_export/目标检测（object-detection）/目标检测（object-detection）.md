---
title: "目标检测（object-detection）"
description: "1、支持的算法Faster R-CNN（）FCOSRetinaNetSSD（）SSDlite好奇为啥没有yolo"
date: "2026-10-11"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\目标检测（object-detection）\\目标检测（object-detection）.md"
---
# 目标检测（object-detection）
这里以torchvision库为例，其他也可用

1、支持的算法Faster R-CNN（*）FCOSRetinaNetSSD（*）SSDlite好奇为啥没有yolo

2、应用from torchvision.io.image import read_imagefrom torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weightsfrom torchvision.utils import draw_bounding_boxesfrom torchvision.transforms.functional import to_pil_imageimg = read_image("test/assets/encode_jpeg/grace_hopper_517x606.jpg")# Step 1: Initialize model with the best available weightsweights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULTmodel = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)model.eval()# Step 2: Initialize the inference transformspreprocess = weights.transforms()# Step 3: Apply inference preprocessing transformsbatch = [preprocess(img)]# Step 4: Use the model and visualize the predictionprediction = model(batch)[0]labels = [weights.meta["categories"][i] for i in prediction["labels"]]box = draw_bounding_boxes(img, boxes=prediction["boxes"],                          labels=labels,                          colors="red",                          width=4, font_size=30)im = to_pil_image(box.detach())im.show()3、效果在 COCO val2017上目标检测准确率：

| Weight | Box MAP | Params | GFLOPS | Recipe |
| --- | --- | --- | --- | --- |
| FCOS_ResNet50_FPN_Weights.COCO_V1 | 39.2 | 32.3M | 128.21 | link |
| FasterRCNN_MobileNet_V3_Large_320_FPN_Weights.COCO_V1 | 22.8 | 19.4M | 0.72 | link |
| FasterRCNN_MobileNet_V3_Large_FPN_Weights.COCO_V1 | 32.8 | 19.4M | 4.49 | link |
| FasterRCNN_ResNet50_FPN_V2_Weights.COCO_V1 | 46.7 | 43.7M | 280.37 | link |
| FasterRCNN_ResNet50_FPN_Weights.COCO_V1 | 37 | 41.8M | 134.38 | link |
| RetinaNet_ResNet50_FPN_V2_Weights.COCO_V1 | 41.5 | 38.2M | 152.24 | link |
| RetinaNet_ResNet50_FPN_Weights.COCO_V1 | 36.4 | 34.0M | 151.54 | link |
| SSD300_VGG16_Weights.COCO_V1 | 25.1 | 35.6M | 34.86 | link |
| SSDLite320_MobileNet_V3_Large_Weights.COCO_V1 | 21.3 | 3.4M | 0.58 | link |

4、应用与可视化更多详情参考：

绘制由 torchvision 检测模型生成的边界框。加载 Faster R-CNN 模型:torchvision.models.detection.fasterrcnn_resnet50_fpn

import torchimport numpy as npfrom torchvision.io import read_imagefrom torchvision.utils import draw_bounding_boxesfrom pathlib import Pathimport matplotlib.pyplot as pltimport torchvision.transforms.functional as Ffrom torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weightsdef show(imgs):    if not isinstance(imgs, list):        imgs = [imgs]    fig, axs = plt.subplots(ncols=len(imgs), squeeze=False)    for i, img in enumerate(imgs):        img = img.detach()        img = F.to_pil_image(img)        axs[0, i].imshow(np.asarray(img))        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])dog1_int = read_image(str(Path('data') / 'cat_dog.jpg'))dog_list = [dog1_int]weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULTtransforms = weights.transforms()model = fasterrcnn_resnet50_fpn(weights=weights, progress=False)model = model.eval()images = [transforms(d) for d in dog_list]outputs = model(images)print(outputs)score_threshold = .8dogs_with_boxes = [    draw_bounding_boxes(dog_int, boxes=output['boxes'][output['scores'] > score_threshold], colors=["red", "yellow"], width=4)    for dog_int, output in zip(dog_list, outputs)]show(dogs_with_boxes)![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fabcebdd4d43484797817f194e46b333&docGuid=7dvIVx_RSEciuI)



