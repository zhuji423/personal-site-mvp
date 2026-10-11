---
title: "torchvision 目标检测、语义分割、实例分割应用"
description: "1、可视化import torchimport numpy as npimport matplotlib.pyplot as pltimport torchvision.transforms.functional as Fplt.rcPar"
date: "2026-04-28"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\torchvision 目标检测、语义分割、实例分割应用\\torchvision 目标检测、语义分割、实例分割应用.md"
---
# torchvision 目标检测、语义分割、实例分割应用
源文件：

1、可视化import torchimport numpy as npimport matplotlib.pyplot as pltimport torchvision.transforms.functional as Fplt.rcParams["savefig.bbox"] = 'tight'def show(imgs):    if not isinstance(imgs, list):        imgs = [imgs]    fig, axs = plt.subplots(ncols=len(imgs), squeeze=False)    for i, img in enumerate(imgs):        img = img.detach()        img = F.to_pil_image(img)        axs[0, i].imshow(np.asarray(img))        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])torchvision.utils.make_grid 函数可用于创建表示网格中多个图像的张量。该实用程序需要单个 dtype 图像uint8作为输入。

from torchvision.utils import make_gridfrom torchvision.io import read_imagefrom pathlib import Pathdog1_int = read_image(str(Path('data') / 'dog1.jpg'))dog2_int = read_image(str(Path('data') / 'dog2.jpg'))dog_list = [dog1_int, dog2_int]grid = make_grid(dog_list)show(grid)![](/personal-site-mvp/img/doc-placeholder.svg)

2、目标检测绘制由 torchvision 检测模型生成的边界框。加载 Faster R-CNN 模型:torchvision.models.detection.fasterrcnn_resnet50_fpn

from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weightsweights = FasterRCNN_ResNet50_FPN_Weights.DEFAULTtransforms = weights.transforms()images = [transforms(d) for d in dog_list]model = fasterrcnn_resnet50_fpn(weights=weights, progress=False)model = model.eval()outputs = model(images)print(outputs)绘制模型检测到的分数大于给定阈值的框。

score_threshold = .8dogs_with_boxes = [    draw_bounding_boxes(dog_int, boxes=output['boxes'][output['scores'] > score_threshold], colors=["red"], width=4)    for dog_int, output in zip(dog_list, outputs)]show(dogs_with_boxes)![](/personal-site-mvp/img/doc-placeholder.svg)

3、语义分割使用 FCN Resnet-50 模型。

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

4、实例分割使用Mask-RCNN 模型。

from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weightsweights = MaskRCNN_ResNet50_FPN_Weights.DEFAULTtransforms = weights.transforms()images = [transforms(d) for d in dog_list]model = maskrcnn_resnet50_fpn(weights=weights, progress=False)model = model.eval()output = model(images)print(output)对于批次中的每个图像，模型输出一些检测（或实例）。每个输入图像的检测数量各不相同。每个实例都由其边界框、标签、分数和掩码来描述。

输出的组织方式如下：输出是一个长度为batch_size的列表。列表中的每个条目对应一个输入图像，它是一个带有“boxes”、“labels”、“scores”和“masks”键的字典。与这些键关联的每个值都包含num_instances元素。在上面的例子中，第一个图像中检测到 3 个实例，第二个图像中检测到 2 个实例。

实例分割的掩码和语义分割模型的掩码有很大不同。

dog1_output = output[0]dog1_masks = dog1_output['masks']print(f"shape = {dog1_masks.shape}, dtype = {dog1_masks.dtype}, "      f"min = {dog1_masks.min()}, max = {dog1_masks.max()}")这里的掩码对应于概率，表明对于每个像素，它属于该实例的预测标签的可能性有多大。这些预测的标签对应于同一输出字典中的“标签”元素。

查看为第一张图像的实例预测了哪些标签。

print("For the first dog, the following instances were detected:")print([weights.meta["categories"][label] for label in dog1_output['labels']])继续绘制这些蒙版。由于draw_segmentation_masks() 需要布尔掩码，需要将这些概率转换为布尔值。这些掩码的语义是“该像素属于预测类别的可能性有多大？”。因此，将这些掩码转换为布尔值的一种自然方法是使用 0.5 的概率对它们进行阈值处理。

proba_threshold = 0.5dog1_bool_masks = dog1_output['masks'] > proba_thresholdprint(f"shape = {dog1_bool_masks.shape}, dtype = {dog1_bool_masks.dtype}")# There's an extra dimension (1) to the masks. We need to remove itdog1_bool_masks = dog1_bool_masks.squeeze(1)show(draw_segmentation_masks(dog1_int, dog1_bool_masks, alpha=0.9))![](/personal-site-mvp/img/doc-placeholder.svg)

该模型似乎正确地检测到了狗，但它也将树与人混淆了。

print(dog1_output['scores'])
# tensor([0.9987, 0.7187, 0.6525], grad_fn=<IndexBackward0>)在绘制掩模时，可以只要求那些得分较高的掩模。在这里使用 0.75 的分数阈值，并绘制第二只狗的掩模。

score_threshold = .75boolean_masks = [    out['masks'][out['scores'] > score_threshold] > proba_threshold    for out in output]dogs_with_masks = [    draw_segmentation_masks(img, mask.squeeze(1))    for img, mask in zip(dog_list, boolean_masks)]show(dogs_with_masks)![](/personal-site-mvp/img/doc-placeholder.svg)



![](/personal-site-mvp/img/doc-placeholder.svg)



