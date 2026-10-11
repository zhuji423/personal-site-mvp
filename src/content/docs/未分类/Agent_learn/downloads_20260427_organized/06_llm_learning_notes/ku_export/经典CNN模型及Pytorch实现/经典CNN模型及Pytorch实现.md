---
title: "经典CNN模型及Pytorch实现"
description: "特定的filter，去跟图片做卷积，就可以识别出图片中的某些特征，比如边界。CNN，主要就是通过一个个的filter，不断地提取特征，从局部的特征到总体的特征，从而进行图像识别等等功能。这些filter，可以通过大量的数据，来让机器自己去“"
date: "2026-04-28"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\经典CNN模型及Pytorch实现\\经典CNN模型及Pytorch实现.md"
---
# 经典CNN模型及Pytorch实现
基础卷积![](/personal-site-mvp/img/doc-placeholder.svg)

特定的filter，去跟图片做卷积，就可以识别出图片中的某些特征，比如边界。CNN，主要就是通过一个个的filter，不断地提取特征，从局部的特征到总体的特征，从而进行图像识别等等功能。这些filter，可以通过大量的数据，来让机器自己去“学习”得到。

池化MaxPooling，采用了一个2×2的窗口，并取步长stride=2。目的：提取区域主要特征，减少参数量，防止过拟合。

![](/personal-site-mvp/img/doc-placeholder.svg)

总结| 模型 | 亮点 | 结构 | 影响 | 实际训练效果minist |
| --- | --- | --- | --- | --- |
| LeNet (1998)论文：Gradient-based learning applied to document recognition | 网络结构比较完整，包括卷积层、pooling层、全连接层，这些都是现代CNN网络的基本组件 | 由2个卷积层，2个池化层，2个全连接层组成。卷积核都是5×5，stride=1，池化层使用maxpooling。 | 广为流传LeNet诞生于1998年，网络结构比较完整，被认为是CNN的开端 | Accuracy: 98.77%，运行时间:86.63秒 |
| AlexNet (2012)论文：ImageNet Classification with Deep Convolutional Neural Networks | 提高训练速度：ReLU做激活函数&双GPU实现；减少过拟合：使用dropout和数据增强；提高精度：使用LRN局部归一化；提高精度、不容易产生过拟合：重叠池化。 | 包含5个卷积层、3个全连接层。最后一层使用softmax做分类输出 | 2012年Geoffrey和他学生Alex在ImageNet的竞赛中，刷新了image classification的记录，一举奠定了deep learning 在计算机视觉中的地位。 | Accuracy: 98.99%，运行时间:377.76秒 |
| VGGNet (2015)论文：Very Deep Convolutional Networks for Large-Scale Image Recognition | LRN作用不大；提升网络层数效果越好；3：1配比conv+ReLU和pooling提取图像特征。2个3x3卷积堆叠等于1个5x5卷积，3个3x3堆叠等于1个7x7卷积，采用更多次更小的卷积核可以带来更多非线性因素，利于函数的拟合。 | 全部使用3×3卷积核的堆叠，来模拟更大的感受野，并且网络层数更深。VGG有五段卷积，每段卷积后接一层最大池化。卷积核数目逐渐增加。 | VGG-Net来自 Andrew Zisserman 教授的组 (Oxford)，在2014年的 ILSVRC localization and classification 两个问题上分别取得了第一名和第二名，VGG-Net使用更多的层，通常有16－19层，而AlexNet只有8层。同时，VGG-Net的所有 convolutional layer 使用同样大小的 convolutional filter，大小为 3 x 3。该网络结构的16层版本在学术界被广泛使用，并在其他如目标检测、目标语义分割等视觉任务上取得了显著的效果。 | Accuracy: 98.81%，运行时间:275.36秒 |
| GoogNet (2014)论文： Going Deeper with Convolutions | 通过设计最优的局部结构（Inception模块），通过增加网络宽度的方式来增加网络复杂度，让网络可以自己去应该如何选择卷积核。这种设计减少了参数 ，同时提高了网络对多种尺度的适应性。使用了1×1卷积可以使网络在不增加参数的情况下增加网络复杂度。 |  | GoogLeNet在2014年的ImageNet竞赛中夺冠并取得了6.7%的Top-5分类错误率。目前在ImageNet数据集上人类识别的Top-5错误率为5.1%，GoogLeNet的结果表明卷积神经网络模型在该数据集上已经逼近人类的识别能力。 | Accuracy: 99.43%，运行时间:629.74秒 |
| ResNet (2016)论文：Deep Residual Learning for Image Recognition | 为了解决由于网络变深导致梯度小时/爆炸的问题，ResNet引入了跳层连接组成残差模块，该结构能够将网络加深到任意深度。 |  | 在2015年的ImageNet竞赛上就出现了152层的网络结构，即ResNet，这远远超出GoogLeNet的22层和VGGNet的16层。ImageNet数据集的识别精度上，ResNet网络的表现超出了人类的认识水平，获得了3.57%的Top-5分类错误率。 | Accuracy: 99.29%，运行时间:402.61秒 |

一、LeNet 19981. 介绍Yann Lecun在1988年提出的LeNet是早期具有代表性的一个卷积神经网络。LeNet-5网络模型已经使用了近些年卷积神经网络中能见到的几乎所有基础操作，包括卷积层、池化层和反向传播训练方法等。

当时Lecun使用该网络模型帮助银行识别文档中的手写数字，输入的图像仅有32像素×32像素大小而且是灰度图像。该模型结构受限于当时的计算能力，不能用来设计为更加复杂的模型，也不能处理更大的图像。

数据集：minist 6k*28*28

论文：Gradient-based learning applied to document recognition

2. 结构分析![](/personal-site-mvp/img/doc-placeholder.svg)

输入层 INPUT
输入32×32×1的图像设输入尺寸为𝑊×𝑊，卷积核尺寸为𝐹×𝐹，卷积步长为𝑆，填充宽度为𝑃，则卷积后输出的尺寸为(𝑊−𝐹+2𝑃)/𝑆+1第一个卷积层 CONV1  5*5*6使用6个尺寸为5×5的滤波器，在卷积的过程中不做边缘填充，步长为𝑠𝑡𝑟𝑖𝑑𝑒=1。单个核的卷积输出尺寸为32−5+1=28。由于有6个卷积核，所以整个卷积层输出得到为Feature Map为 28×28×6。

该层的参数：

滤波器的核： (5×5+1)×6=156，每个滤波器除了5×5的核以外，还有一个偏置。神经元的个数：28×28×6。在卷积层中，卷积核每移动一步产生一个神经元的输出，也就相当于一个神经元。卷积的过程中，不做边缘填充，对于32×32的输入，一个5×5的卷积核产生28×28个输出，共有6个卷积核，有28×28×6个神经元。可训练参数：(5×5+1)×6，每个滤波器5*5=25个单元参数（unit)和一个偏置参数(bias)，一共6个滤波器总共的连接数： (5×5+1)×6×28×28=122304。可训练参数数量 *  feature map 的大小。池化层输入尺寸为𝑊×𝑊，池化尺寸为𝐹×𝐹，池化步长为𝑆，则池化后的输出尺寸为(𝑊−𝐹)/𝑆+1池化层 POOL1
池化层用于降采样，其输入是上一卷积层的输出为28×28×6。在本层采用尺寸2×2的池化单元，池化时的沿长和宽的步长均为2。 池化后的输出尺寸为(28−2)/2+1=14，深度为6，则池化的输出为14×14×6。采样方式：4个输入相加，乘以一个可训练参数，再加上一个可训练偏置，结果通过sigmoid。可训练参数：2x6（和的权+偏置这两个参数）连接个数： (2×2+1)×14×14×6=5880第二个卷积层 CONV2  5*5*16
该层的输入为14×14×6，使用16个核为5×5，步长为1。则其输出尺寸为14−5+1=10。整个层的输出为10×10×16。第二个池化层 POOL2输入是10×10×16，池化参数和第一个池化层一样采用尺寸2×2的池化单元，池化时步长为2， 输出尺寸为(10−2)/2+1=5，其输出为5×5×16，参数个数是(1+1)×16=32，连接数(2×2+1)×5×5×16=2000

第三个卷积层 CONV3  120
120个5×5的卷积核，输入的是5×5×16，输入的Feature Map和输出的Feature Map是全连接，输出尺寸为5−5+1=1，其输出为1×1×120(卷积核和输入尺寸相同，且没有边缘填充)。其卷积核的参数是5×5×16+1。 而输出的120个神经元每个都和上一层的相连，则连接和参数的个数相同为(5×5×16+1)×120=48120全连接层  84
输入是120维的向量，本层有84个神经元，参数个数是(120+1)×84=10164输出层  10
全连接层，10个神经元，代表10个不同的数字。参数/连接个数为84×10=8403. 核心代码LeNet-5网络结构核心代码如下：

import torch.nn as nnimport torch.nn.functional as Fclass LeNet(nn.Module):    def __init__(self, num_classes=10):        super().__init__()        self.conv1 = nn.Conv2d(3, 6, 5)  # in_channels, out_channels, kernel_size, stride=1, padding=0        self.conv2 = nn.Conv2d(6, 16, 5)        self.fc1 = nn.Linear(16 * 5 * 5, 120)        self.fc2 = nn.Linear(120, 84)        self.fc3 = nn.Linear(84, num_classes)    def forward(self, x):        x = F.max_pool2d(F.relu(self.conv1(x)), kernel_size=(2, 2))        x = F.max_pool2d(F.relu(self.conv2(x)), kernel_size=(2, 2))        x = x.view(x.size()[0], -1)  # 多维度的tensor展平成一维        x = F.relu(self.fc1(x))        x = F.relu(self.fc2(x))        x = self.fc3(x)        return x4. 结构参数明细![](/personal-site-mvp/img/doc-placeholder.svg)

5. 影响LeNet-5 与现在通用的卷积神经网络在某些细节结构上还是有差异的，例如 LeNet-5 采用的激活函数是 sigmoid，而目前图像一般用 tanh，relu，leakly relu 较多；LeNet-5 池化层处理与现在也不同；多分类最后的输出层一般用 softmax，与 LeNet-5 不太相同。LeNet-5 是一种用于手写体字符识别的非常高效的卷积神经网络。CNN 能够得出原始图像的有效表征，这使得 CNN 能够直接从原始像素中，经过极少的预处理，识别视觉上面的规律。然而，由于当时缺乏大规模训练数据，计算机的计算能力也跟不上，LeNet-5 对于复杂问题的处理结果并不理想。二、AlexNet 20121. 介绍在LeNet之后，随着计算能力的提升，研究者不断地提升模型的表达能力。最明显的是卷积层数的增加，每一层的内部通道数目也在增加。其中的一个经典网络模型就是2012年ImageNet竞赛的冠军AlexNet。AlexNet凭借深度学习方法打败了以往所有传统的特征算法（包括SIFT），并且准确率大幅提高。

AlexNet成功的另一个原因是ImageNet数据集（12.8w张）的出现。在大数据时代，深度模型的学习离不开大量数据的训练，而此前一直没有能够让深度模型充分训练的大规模数据。AlexNet以绝对优势取得2012年ImageNet竞赛冠军后，使得深度学习逐渐成为学术研究热点，卷积神经网络称为计算机视觉任务上的主要模型。

数据集：ImageNet 1.2m*469*387，由于ImageNet数据集过于庞大，对于个人学习而言可以用CIFAR-10数据集

论文：ImageNet Classification with Deep Convolutional Neural Networks

2. 结构分析网络包含8个带权重的层；前5层是卷积层，剩下的3层是全连接层。最后一层全连接层的输出是1000维softmax的输入，softmax会产生1000类标签的分布。

卷积层C1  11*11*96
该层的处理流程是： 卷积-->ReLU-->池化-->归一化。卷积，输入是227×227，使用96个11×11×3的卷积核，步长为4，输出尺寸(227-11)/4+1=55，得到的FeatureMap为55×55×96ReLU，将卷积层输出的FeatureMap输入到ReLU函数中。池化，使用3×3步长为2的池化单元（重叠池化，步长小于池化单元的宽度），输出尺寸为(55−3)/2+1=27，输出为27×27×96局部响应归一化，使用k=2,n=5,α=10−4,β=0.75进行局部归一化，输出的仍然为27×27×96，输出分为两组，每组的大小为27×27×48卷积层C2  5*5*256
该层的处理流程是：卷积-->ReLU-->池化-->归一化卷积，输入是2组27×27×48。使用2组，每组128个尺寸为5×5×48的卷积核，并作了边缘填充padding=2，卷积的步长为1，则输出尺寸为(27+2×2-5)/1+1=27，输出的FeatureMap为2组，每组的大小为27×27×128ReLU，将卷积层输出的FeatureMap输入到ReLU函数中池化运算的尺寸为3×3，步长为2，池化后图像的尺寸为(27−3)/2+1=13，输出为13×13×256局部响应归一化，使用k=2,n=5,α=10−4,β=0.75进行局部归一化，输出的仍然为13×13×256，输出分为2组，每组的大小为13×13×128卷积层C3  3*3*384
该层的处理流程是： 卷积-->ReLU卷积，输入是13×13×256，使用2组每组192个尺寸为3×3×256的卷积核，做了边缘填充padding=1，卷积的步长为1，输出尺寸(13+2×1-3)/1+1=13，则输出的FeatureMap为13×13×384ReLU，将卷积层输出的FeatureMap输入到ReLU函数中卷积层C4  3*3*384
该层的处理流程是： 卷积-->ReLU
该层和C3类似。卷积，输入是13×13×384，使用2组每组192个尺寸为3×3×192的卷积核，做了边缘填充padding=1，卷积的步长为1，输出尺寸(13+2×1-3)/1+1=13，则输出的FeatureMap为13×13×384ReLU，将卷积层输出的FeatureMap输入到ReLU函数中卷积层C5  3*3*256
该层处理流程为：卷积-->ReLU-->池化卷积，输入为13×13×384，使用2组每组为128尺寸为3×3×192的卷积核，做了边缘填充padding=1，卷积的步长为1，输出尺寸(13+2×1-3)/1+1=13，则输出的FeatureMap为13×13×256ReLU，将卷积层输出的FeatureMap输入到ReLU函数中池化，池化运算的尺寸为3×3，步长为2，池化后图像的尺寸为 (13−3)/2+1=6，即池化后的输出为6×6×256全连接层FC6  4096
该层的流程为：（卷积）全连接 -->ReLU -->Dropout卷积->全连接： 输入为6×6×256，该层有4096个卷积核，每个卷积核的大小为6×6×256。由于卷积核的尺寸刚好与待处理特征图（输入）的尺寸相同，即卷积核中的每个系数只与特征图（输入）尺寸的一个像素值相乘，一一对应，因此，该层被称为全连接层。由于卷积核与特征图的尺寸相同，卷积运算后只有一个值，因此，卷积后的像素层尺寸为4096×1×1，即有4096个神经元。ReLU，这4096个运算结果通过ReLU激活函数生成4096个值Dropout，抑制过拟合，随机的断开某些神经元的连接或者是不激活某些神经元全连接层FC7  4096
流程为：全连接-->ReLU-->Dropout全连接，输入为4096的向量ReLU，这4096个运算结果通过ReLU激活函数生成4096个值Dropout，抑制过拟合，随机的断开某些神经元的连接或者是不激活某些神经元输出层  1000
第七层输出的4096个数据与第八层的1000个神经元进行全连接，经过训练后输出1000个float型的值，这就是预测结果。3. 核心代码AlexNet网络结构核心代码如下：

import torch.nn as nnimport torch.nn.functional as Fclass AlexNet(nn.Module):    def __init__(self, num_classes=1000):        super().__init__()        self.features = nn.Sequential(            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),            nn.ReLU(inplace=True),            nn.LocalResponseNorm(size=5, alpha=1e-4, beta=0.75),            nn.MaxPool2d(kernel_size=3, stride=2),            nn.Conv2d(64, 192, kernel_size=5, padding=2),            nn.ReLU(inplace=True),            nn.LocalResponseNorm(size=5, alpha=1e-4, beta=0.75),            nn.MaxPool2d(kernel_size=3, stride=2),            nn.Conv2d(192, 384, kernel_size=3, padding=1),            nn.ReLU(inplace=True),            nn.Conv2d(384, 256, kernel_size=3, padding=1),            nn.ReLU(inplace=True),            nn.Conv2d(256, 256, kernel_size=3, padding=1),            nn.ReLU(inplace=True),            nn.MaxPool2d(kernel_size=3, stride=2),        )        self.classifier = nn.Sequential(            nn.Dropout(),            nn.Linear(256 * 6 * 6, 4096),            nn.ReLU(inplace=True),            nn.Dropout(),            nn.Linear(4096, 4096),            nn.ReLU(inplace=True),            nn.Linear(4096, num_classes)        )    def forward(self, x):        x = self.features(x)        x = x.view(x.size(0), 256 * 6 * 6)        x = self.classifier(x)        return x4. 结构参数明细![](/personal-site-mvp/img/doc-placeholder.svg)

5. 影响AlexNet是在LeNet的基础上加深了网络的结构，学习更丰富更高维的图像特征。AlexNet的特点：

更深的网络结构使用层叠的卷积层，即卷积层+卷积层+池化层来提取图像的特征使用Dropout抑制过拟合使用数据增强Data Augmentation抑制过拟合使用Relu替换之前的sigmoid的作为激活函数多GPU训练添加了归一化LRN（Local Response Normalization，局部响应归一化）层三、VGGNet 20151. 介绍文章于2015年由牛津大学视觉几何组（Visual Geometry Group）发表在ICLR上，VGGNet名字由此而来，和GoogLeNet一起参加了ILSVRC 2014的比赛，GoogLeNet第一，VGGNet第二。两者的设计思路区别很大，GoogLeNet通过模块化操作以及多支路使得网络加宽和变深，而VGGNet则是逐步缩小特征图分辨率和逐步升高特征图维度使得网络可以变得很深，而且也证明网络的深度其实是卷积网络模型性能优良的关键性因素之一。尽管VGGNet使用了如此多的参数，其依然没有夺得ImageNet竞赛的冠军。但是该网络结构的16层版本在学术界被广泛使用，并在其他如目标检测、目标语义分割等视觉任务上取得了显著的效果。

VGGNet比较流行的有VGG-16和VGG-19两个。

VGGNet的设计主要还是参考的AlexNet，只不过网络的设计更为优雅和具有逻辑，而且相比AlexNet和GoogLeNet没有繁琐的参数的设置，可以使得网络层数从11层逐步提升至19层，网络的性能也逐渐提升。

论文：Very Deep Convolutional Networks for Large-Scale Image Recognition

2. 结构分析vggnet就是在Alexnet 的基础上拓宽了网络深度，本质上网络模型仍然是由卷积层和全连接层组成。

下图是来自https://neurohive.io/en/popular-networks/vgg16/ 中VGG-16架构的截图：

VGG-16(13个卷积层+3个全连接层)与VGG-19(16个卷积层+3个全连接层)的区别：每个卷积层后跟ReLU

VGG-16：2个卷积层+Max Pooling+2个卷积层+Max Pooling+3个卷积层+Max Pooling+3个卷积层+Max Pooling+3个卷积层+Max Pooling+3个全连接层。VGG-19：2个卷积层+Max Pooling+2个卷积层+Max Pooling+4个卷积层+Max Pooling+4个卷积层+Max Pooling+4个卷积层+Max Pooling+3个全连接层。3. 核心代码从VGG 6个结构中选择了A、B、D、E这四个来搭建模型，建立的cfg字典包含了这4个结构。例如对于vgg16，[64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M']表示了卷积层的结构。64表示conv3-64，'M'表示maxpool，128表示conv3-128，256表示conv3-256，512表示conv3-512。

import torch.nn as nnimport torch.nn.functional as FNET_CONF = {    'vgg11': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],    'vgg13': [64, 64, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],    'vgg16': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],    'vgg19': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M'],}def VGGLayers(configs):    layers = []    in_channels = 3    for v in configs:        if v == "M":            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]        else:            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)            layers += [conv2d, nn.ReLU(True)]            in_channels = v    return nn.Sequential(*layers)class VGGNet(nn.Module):    def __init__(self, num_classes=1000):        super().__init__()        self.features = VGGLayers(NET_CONF['vgg16'])        self.classifier = nn.Sequential(            nn.Linear(512 * 7 * 7, 4096),            nn.ReLU(inplace=True),            nn.Dropout(),            nn.Linear(4096, 4096),            nn.ReLU(inplace=True),            nn.Linear(4096, num_classes)        )    def forward(self, x):        x = self.features(x)        x = x.view(x.size(0), 512 * 7 * 7)        x = self.classifier(x)        return x4. 结构参数明细![](/personal-site-mvp/img/doc-placeholder.svg)

5. 影响提升网络层数。3：1配比conv+ReLU和pooling提取图像特征。 输入层以及前三个max-pooling层后的第一个conv用来维度升高，维度变化为【3，64，128，256，512】，其余的卷积操作既不改变特征图分辨率也不改变维度。可以说非常优雅了～VGG-16有两种形式，一种是加入额外的1x1 filter，一种是加入额外的3x3 filter。额外的1x1用于输入通道的线性变化，不会改变特征图的感受野，一般后面还会跟着一个ReLU非线性激活函数，卷积的步长基本都是1。1x1卷积核看似没什么用，但配合ReLU()函数可以增加更多非线性因素，其实就是更容易逼近函数。2个3x3卷积堆叠等于1个5x5卷积，3个3x3堆叠等于1个7x7卷积，采用更多次更小的卷积核可以带来更多非线性因素，利于函数的拟合。关于为什么不用一个7x7而使用3个3x3（3个3x3卷积核的感受野和一个7x7是一致的），主要有两点，最重要的一点是可以显著降低参数量，7x7/（3x3x3）=1.81，可以减小81%的参数量，第二点就是如果使用3个3x3，那么可以有3个ReLU激活函数，可以提高网络判别能力。去掉了AlexNet中的LRN层，因为在VGGNet中，LRN不会提高精度，而且增大了显存。四、GoogNet 20141. 介绍论文： Going Deeper with Convolutions

GoogLeNet在2014年的ImageNet竞赛中夺冠并取得了6.7%的Top-5分类错误率。目前在ImageNet数据集上人类识别的Top-5错误率为5.1%，GoogLeNet的结果表明卷积神经网络模型在该数据集上已经逼近人类的识别能力。

 Inception系列是谷歌出品的网络结构，就是把多个卷积或池化操作，放在一起组装成一个网络模块，设计神经网络时以模块为单位去组装整个网络结构。

主要经历了v1、v2、v3以及v4阶段的发展。Inception-v1（GoogLeNet）主要的motivation是如何在不大幅增加网络参数和计算量的同时使得网络变得更宽和层级更深，主要是设计一种最优的稀疏卷积架构并去不断的重复这种卷积架构以加深网络层级，同时在稀疏卷积架构模块中加入多支路来使得每一层级变宽。这篇文章用到1x1卷积和全局平均池化（Global Average Pooling）主要参考自2014年《Network in Network》，这篇文章对此后网络设计有着深远影响。

2. 结构分析GoogLeNet网络结构如下图所示：

![](/personal-site-mvp/img/doc-placeholder.svg)

原始的Inception模块如下图所示，包含几种不同大小的卷积层，即1×1卷积层、3×3卷积层和5×5卷积层，还包括一个3×3的最大池化层。这些卷积层和池化层得到的特征拼接在一起作为最终的输出，同时也是下一个模块的输入。左为不加1x1进行维度降低Inception模块，右为加入1x1进行维度降低Inception模块

![](/personal-site-mvp/img/doc-placeholder.svg)

3. 核心代码import torchimport torch.nn as nnclass Inception(nn.Module):    """    1、输入通过Inception模块的4个分支分别计算，得到的输出宽和高相同(因为使用了padding)，而通道不同。    2、将4个分支的通道进行简单的合并，即得到Inception模块的输出。    3、每次卷积之后都使用批正则化`BatchNorm2d`，并使用relu函数进行激活。    """    def __init__(self, in_planes, n1x1, n3x3red, n3x3, n5x5red, n5x5, pool_planes):        super(Inception, self).__init__()        # 1x1 conv branch        self.b1 = nn.Sequential(            nn.Conv2d(in_planes, n1x1, kernel_size=1),            nn.BatchNorm2d(n1x1),            nn.ReLU(True),        )        # 1x1 conv -> 3x3 conv branch        self.b2 = nn.Sequential(            nn.Conv2d(in_planes, n3x3red, kernel_size=1),            nn.BatchNorm2d(n3x3red),            nn.ReLU(True),            nn.Conv2d(n3x3red, n3x3, kernel_size=3, padding=1),            nn.BatchNorm2d(n3x3),            nn.ReLU(True),        )        # 1x1 conv -> 5x5 conv branch        self.b3 = nn.Sequential(            nn.Conv2d(in_planes, n5x5red, kernel_size=1),            nn.BatchNorm2d(n5x5red),            nn.ReLU(True),            # 2个3x3卷积代替1个5x5卷积            nn.Conv2d(n5x5red, n5x5, kernel_size=3, padding=1),            nn.BatchNorm2d(n5x5),            nn.ReLU(True),            nn.Conv2d(n5x5, n5x5, kernel_size=3, padding=1),            nn.BatchNorm2d(n5x5),            nn.ReLU(True),        )        # 3x3 pool -> 1x1 conv branch        self.b4 = nn.Sequential(            nn.MaxPool2d(3, stride=1, padding=1),            nn.Conv2d(in_planes, pool_planes, kernel_size=1),            nn.BatchNorm2d(pool_planes),            nn.ReLU(True),        )    def forward(self, x):        outpus = [self.b1(x), self.b2(x), self.b3(x), self.b4(x)]        return torch.cat(outpus, dim=1)class GoogLeNet(nn.Module):    def __init__(self):        super().__init__()        self.pre_layers = nn.Sequential(            nn.Conv2d(3, 192, kernel_size=3, padding=1),            nn.BatchNorm2d(192),            nn.ReLU(True),        )        self.a3 = Inception(192, 64, 96, 128, 16, 32, 32)        self.b3 = Inception(256, 128, 128, 192, 32, 96, 64)        self.maxpool = nn.MaxPool2d(3, stride=2, padding=1)        self.a4 = Inception(480, 192, 96, 208, 16, 48, 64)        self.b4 = Inception(512, 160, 112, 224, 24, 64, 64)        self.c4 = Inception(512, 128, 128, 256, 24, 64, 64)        self.d4 = Inception(512, 112, 144, 288, 32, 64, 64)        self.e4 = Inception(528, 256, 160, 320, 32, 128, 128)        self.a5 = Inception(832, 256, 160, 320, 32, 128, 128)        self.b5 = Inception(832, 384, 192, 384, 48, 128, 128)        self.avgpool = nn.AvgPool2d(8, stride=1)        self.linear = nn.Linear(1024, 10)    def forward(self, x):        out = self.pre_layers(x)        out = self.a3(out)        out = self.b3(out)        out = self.maxpool(out)        out = self.a4(out)        out = self.b4(out)        out = self.c4(out)        out = self.d4(out)        out = self.e4(out)        out = self.maxpool(out)        out = self.a5(out)        out = self.b5(out)        out = self.avgpool(out)        out = out.view(out.size(0), -1)        out = self.linear(out)        return out4. 结构参数明细![](/personal-site-mvp/img/doc-placeholder.svg)

5. 影响通过设计最优的局部结构（Inception模块）并在其基础上扩展以加深网络深度，使得网络达到22层，模块化的结构同样方便他人进行修改和增删；最优的局部结构（Inception模块），目的在于设计一种稀疏的卷积架构，设计不同卷积核大小的多支路使得网络每一层级变得更宽，但是同时又不像直接提升神经元大小那样会带来参数量的巨大提升；AlexNet中使用了3个高达上千维的全连接网络，这是其网络模型参数高达60 M的核心原因，因此GoogLeNet取消了全连接层，并使用全局平均池化（Global Average Pooling）来代替，这种设计表现的效果同样不俗，但是在网络最后面还是添加了一个全连接层，主要是为了方便大家进行finetune迁移学习；在主体网络中的两个阶段加入辅助监督子网络，子网络主要由GAP、Conv和两个FC层组成，以减轻梯度消失的问题。因为22层的网络在当时已经很深了，梯度消失问题会存在，在网络的中间阶段进行监督，有助于减轻这种问题；在网络的前面使用的还是和AlexNet一致的conv+lrn+max网络(但是层的具体设置不一样)，因为作者发现只有在网络的中后期使用Inception模块效果才比较好，不过作者也说了，这不是必要的操作，可能是基础设施的训练低效的原因； 使用了1x1的卷积核来进行维度降低，这种设计同样也是SqueezeNet参数量如此小的主要原因。测试阶段使用不同尺度和裁剪后的图像进行测试以及使用多模型进行预测，最高可以降低top-5 error rate 6.67%。6. 后续改进Inception-v2（BN）（2015）论文：Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift改进点：在v1的基础上加入batch normalization技术，在tensorflow中，使用BN在激活函数之前效果更好；将5×5卷积替换成两个连续的3×3卷积，使网络更深，参数更少。

Inception-v3（2015）论文：Rethinking the Inception Architecture for Computer Vision改进点：核心思想是将卷积核分解成更小的卷积，如将7×7分解成1×7和7×1两个卷积核，使网络参数减少，深度加深。

Inception-v4（2016）论文：Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning改进点：引入了ResNet，使训练加速，性能提升。但是当滤波器的数目过大（>1000）时，训练很不稳定，可以加入activate scaling因子来缓解。

五、ResNet 20161. 介绍论文：Deep Residual Learning for Image Recognition

从LeNet到AlexNet再到VGGNet，在ImageNet竞赛上网络深度有逐渐加深的趋势。在2015年的ImageNet竞赛上就出现了152层的网络结构，即ResNet，这远远超出GoogLeNet的22层和VGGNet的16层。ImageNet数据集的识别精度上，ResNet网络的表现超出了人类的认识水平，获得了3.57%的Top-5分类错误率。为了解决由于网络变深导致梯度小时/爆炸的问题，ResNet引入了跳层连接，该结构能够将网络加深到任意深度。

从经验来看，网络的深度对模型的性能至关重要，当增加网络层数后，网络可以进行更加复杂的特征模式的提取，所以当模型更深时理论上可以取得更好的结果。但是更深的网络其性能一定会更好吗？实验发现深度网络出现了退化问题（Degradation problem）：网络深度增加时，网络准确度出现饱和，甚至出现下降。

ResNet主要采用跳层连接组成残差模块，包括一个跳层连接和若干卷积层等操作。其中卷积层等操作主要学习一个原始输入x的补充值，参考资料中称为残差值。这样就可将单分支网络结构中的每几层变为双分支结构，增加的跳层连接分支是简单的Identity映射，即f(x)=x操作。

2. 结构分析（1）残差模块的巧妙设计

![](/personal-site-mvp/img/doc-placeholder.svg)

解决的问题：网络退化。

理想情况是模型层数越来越深，效果至少不会变差，即后面的网络什么都不做。问题就出现在这里，什么都不做就是神经网络最难做到的东西。

![](/personal-site-mvp/img/doc-placeholder.svg)

举个例子：

假设第一个网络在训练集和测试集上可以得到很好的性能（甚至可以理解为接近100%）。那么在这个新的网络，由于我们copy了前四层的参数，理论上前四层已经足够满足我们的性能要求，那么新增加的层便显得有些多余，如果这个新的网络也要达到性能100%，则新增加的层要做的事情就是“恒等映射”，也即后面几个紫色的层要实现的效果为 f(x)=x。这样一来，网络的性能一样能达到100%。而退化现象也表明了，实际上新增加的几个紫色的层，很难做到恒等映射。又或者能做到，但在有限的时间内很难完成（即网络要用指数级别的时间才能达到收敛）。这时候，巧妙的通过添加”桥梁“，使得难以优化的问题瞬间迎刃而解。可以看到通过添加这个桥梁，把数据原封不动得送到FC层的前面，而对于中间的紫色层，可以很容易的通过把这些层的参数逼近于0，进而实现的功能。![](/personal-site-mvp/img/doc-placeholder.svg)



实际上，网络性能通常未能达到100%，可以假设最初的网络（只有前四层）的性能到了98%等等，如果不添加跳连接，增加三个紫色层之后的新网络同样难以进行优化。而通过跳连接，可以把前四层的输出先送到FC层前面，也就相当于告诉紫色层：”兄弟你放心，我已经做完98%的工作了，你看看能不能在剩下的2%中发点力，你要是找不出提升性能的效果也没事的，我们可以把你的参数逼近于0，所以放心大胆的找吧。"

我们把整个映射看成100%，则前面四层网络实现了98%的映射关系，而残余的映射由紫色层完成，Residual 另一个翻译就是"残余，残留“的意思，也就是让每一个残差块，只关注残余映射的一小部分，真的是恰到好处。

当然了，实际上网络运行的时候，我们并不会知道哪几层就能达到很好的效果，然后在它们的后面接一个跳连接，于是一开始便在两个层或者三个层之间添加跳连接，形成残差块，每个残差块只关注当前的残余映射，而不会关注前面已经实现的底层映射。

（2）网络整体结构

典型的网络有resnet50, resnet101

![](/personal-site-mvp/img/doc-placeholder.svg)

ResNet34的网络结构图：

![](/personal-site-mvp/img/doc-placeholder.svg)

3. 核心代码import torch.nn as nn# 3x3 convolutiondef conv3x3(in_channels, out_channels, stride=1):    return nn.Conv2d(in_channels, out_channels, kernel_size=3,                     stride=stride, padding=1, bias=False)# Residual blockclass ResidualBlock(nn.Module):    def __init__(self, in_channels, out_channels, stride=1, downsample=None):        super(ResidualBlock, self).__init__()        self.conv1 = conv3x3(in_channels, out_channels, stride)        self.bn1 = nn.BatchNorm2d(out_channels)        self.relu = nn.ReLU(inplace=True)        self.conv2 = conv3x3(out_channels, out_channels)        self.bn2 = nn.BatchNorm2d(out_channels)        self.downsample = downsample    def forward(self, x):        residual = x        out = self.conv1(x)        out = self.bn1(out)        out = self.relu(out)        out = self.conv2(out)        out = self.bn2(out)        if self.downsample:            residual = self.downsample(x)        out += residual        out = self.relu(out)        return out    class ResNet(nn.Module):    def __init__(self, block, layers, num_classes=10):        super().__init__()        self.in_channels = 16        self.conv = conv3x3(3, 16)        self.bn = nn.BatchNorm2d(16)        self.relu = nn.ReLU(inplace=True)        self.layer1 = self.make_layer(block, 16, layers[0])        self.layer2 = self.make_layer(block, 32, layers[1], 2)        self.layer3 = self.make_layer(block, 64, layers[2], 2)        self.avg_pool = nn.AvgPool2d(8)        self.fc = nn.Linear(64, num_classes)    def make_layer(self, block, out_channels, blocks, stride=1):        downsample = None        if (stride != 1) or (self.in_channels != out_channels):            downsample = nn.Sequential(                conv3x3(self.in_channels, out_channels, stride=stride),                nn.BatchNorm2d(out_channels))        layers = []        layers.append(block(self.in_channels, out_channels, stride, downsample))        self.in_channels = out_channels        for i in range(1, blocks):            layers.append(block(out_channels, out_channels))        return nn.Sequential(*layers)    def forward(self, x):        out = self.conv(x)        out = self.bn(out)        out = self.relu(out)        out = self.layer1(out)        out = self.layer2(out)        out = self.layer3(out)        out = self.avg_pool(out)        out = out.view(out.size(0), -1)        out = self.fc(out)        return out4. 影响提出residual结构（残差结构），并搭建超深的网络结构(突破1000层)使用Batch Normalization加速训练(丢弃dropout)六、其他模型SqueezeNet （2016）：SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and <0.5MB model size

创新点：fire模块，解决模型压缩

DenseNet （2017）：Densely Connected Convolutional Networks

创新点：建立前面层与后面层之间的跨层连接替代resnet的相加

MobileNet（2017）：MobileNets: Effificient Convolutional Neural Networks for Mobile Vision Applications

创新点：提出了一种深度可分离卷积架构（DW+PW 卷积）

七、实际应用在mac m1上运行，参数：epoch=10, batch_size=512, learning_rate=0.001

在minist数据集上的训练代码：

import timeimport matplotlib.pyplot as pltimport torchfrom torchvision import transformsfrom torchvision import datasetsfrom torch.utils.data import DataLoaderimport torch.optim as optimfrom models.CNN.LeNet import LeNetfrom models.CNN.AlexNet import AlexNetfrom models.CNN.VGGNet import VGGNetfrom models.CNN.GoogLeNet import GoogLeNetfrom models.CNN.ResNet import ResNetdef train(model, device, train_loader, opt, loss_func, epoch):    """    训练    """    model.train()    for batch_idx, (data, target) in enumerate(train_loader):        data, target = data.to(device), target.to(device)        # 清除梯度        opt.zero_grad()        # 前向计算的过程        output = model(data)        loss = loss_func(output, target)        # 后向传播，更新参数的过程        loss.backward()        # 最小化loss,更新参数        opt.step()        loss_list.append(loss.item())        # 每训练50批次的数据，打印下当前Loss的情况        if (batch_idx + 1) % 20 == 0:            print('Train Epoch: {} [{}/{} ({:.4f}%)]\tLoss: {:.6f}'.format(                epoch, batch_idx * len(data), len(train_loader.dataset),                100. * batch_idx / len(train_loader), loss.item()))def test(model, device, test_loader):    """    预测    """    model.eval()    correct = 0    with torch.no_grad():        for data, target in test_loader:            data, target = data.to(device), target.to(device)            output = model(data)            pred = torch.max(output, dim=1)[1]            correct += torch.eq(pred, target).sum().item()    print('\nAccuracy: {}/{} ({:.4f}%)\n'.format(        correct, len(test_loader.dataset),        100. * correct / len(test_loader.dataset)))def load_data():    """    数据集读取器    """    transform = transforms.Compose([        transforms.ToTensor(),        # 0.1307和0.3081是mnist数据集的均值和标准差，由数据集提供方给出        transforms.Normalize((0.1307,), (0.3081,))    ])    train_dataset = datasets.MNIST(root='../dataset/mnist/', train=True, download=True, transform=transform)    train_loader = DataLoader(train_dataset, shuffle=True, batch_size=BATCH_SIZE)    test_datasets = datasets.MNIST(root='../dataset/mnist/', train=False, download=True, transform=transform)    test_loader = DataLoader(test_datasets, shuffle=False, batch_size=BATCH_SIZE)    return train_loader, test_loaderdef plot_lost(loss_list, model_name):    """    可视化损失变化    """    plt.figure(figsize=(10, 5))    freqs = [i for i in range(len(loss_list))]    # 绘制训练损失变化曲线    plt.plot(freqs, loss_list, color='#e4007f', label="%s Train loss" % model_name)    # 绘制坐标轴和图例    plt.ylabel("loss", fontsize='large')    plt.xlabel("freq", fontsize='large')    plt.legend(loc='upper right', fontsize='x-large')    plt.savefig("output/img/loss_%s.jpg" % model_name)if __name__ == '__main__':    T1 = time.time()    BATCH_SIZE = 512  # 大概需要2G的显存    EPOCHS = 10  # 总共训练批次    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")    loss_list = []    train_loader, test_loader = load_data()    model = LeNet().to(DEVICE)    # model = AlexNet().to(DEVICE)    # model = VGGNet().to(DEVICE)    # model = GoogLeNet().to(DEVICE)    # model = ResNet().to(DEVICE)    opt = optim.Adam(model.parameters())    loss_func = torch.nn.CrossEntropyLoss()    for epoch in range(1, EPOCHS + 1):        train(model, DEVICE, train_loader, opt, loss_func, epoch)        test(model, DEVICE, test_loader)    model_name = model.__class__.__name__    # 保存模型参数    torch.save(model.state_dict(), 'output/%s.pth' % model_name)    # 可视化损失变化    plot_lost(loss_list, model_name)    T2 = time.time()    print('程序运行时间:%s秒' % (round(T2 - T1, 6)))简化后适用于minist的模型结构：

import torch.nn as nnimport torch.nn.functional as Fclass LeNet(nn.Module):    def __init__(self, num_classes=10):        super().__init__()        self.conv1 = nn.Conv2d(1, 6, 5)  # in_channels, out_channels, kernel_size, stride=1, padding=0        self.conv2 = nn.Conv2d(6, 16, 5)        self.fc1 = nn.Linear(16 * 4 * 4, 120)        self.fc2 = nn.Linear(120, 84)        self.fc3 = nn.Linear(84, num_classes)    def forward(self, x):        x = F.max_pool2d(F.relu(self.conv1(x)), kernel_size=(2, 2))        x = F.max_pool2d(F.relu(self.conv2(x)), kernel_size=(2, 2))        x = x.view(x.size()[0], -1)  # 多维度的tensor展平成一维        x = F.relu(self.fc1(x))        x = F.relu(self.fc2(x))        x = self.fc3(x)        return ximport torch.nn as nnclass AlexNet(nn.Module):    def __init__(self, num_classes=10):        super().__init__()        self.features = nn.Sequential(            nn.Conv2d(1, 10, kernel_size=5, stride=1, padding=2),            nn.ReLU(inplace=True),            nn.LocalResponseNorm(size=5, alpha=1e-4, beta=0.75),            nn.MaxPool2d(kernel_size=2, stride=2),            nn.Conv2d(10, 20, kernel_size=3, stride=1, padding=1),            nn.ReLU(inplace=True),            nn.LocalResponseNorm(size=5, alpha=1e-4, beta=0.75),            nn.MaxPool2d(kernel_size=2, stride=2),            nn.Conv2d(20, 40, kernel_size=3, stride=1, padding=1),            nn.ReLU(inplace=True),            nn.Conv2d(40, 40, kernel_size=3, stride=1, padding=1),            nn.ReLU(inplace=True),            nn.Conv2d(40, 20, kernel_size=3, stride=1, padding=1),            nn.ReLU(inplace=True)        )        self.classifier = nn.Sequential(            nn.Dropout(),            nn.Linear(20 * 7 * 7, 400),            nn.ReLU(inplace=True),            nn.Dropout(),            nn.Linear(400, 100),            nn.ReLU(inplace=True),            nn.Linear(100, num_classes)        )    def forward(self, x):        x = self.features(x)        x = x.view(x.size(0), -1)        x = self.classifier(x)        return ximport torch.nn as nnNET_CONF = {    'minist': [6, 6, 'M', 16, 16, 16, 'M'],    'vgg11': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],    'vgg13': [64, 64, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],    'vgg16': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],    'vgg19': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M'],}def VGGLayers(configs, in_channels):    layers = []    for v in configs:        if v == "M":            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]        else:            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)            layers += [conv2d, nn.ReLU(True)]            in_channels = v    return nn.Sequential(*layers)class VGGNet(nn.Module):    def __init__(self, num_classes=10):        super().__init__()        self.features = VGGLayers(NET_CONF['minist'], in_channels=1)        self.classifier = nn.Sequential(            nn.Linear(16 * 7 * 7, 500),            nn.ReLU(inplace=True),            nn.Dropout(),            nn.Linear(500, 200),            nn.ReLU(inplace=True),            nn.Dropout(),            nn.Linear(200, num_classes)        )    def forward(self, x):        x = self.features(x)        x = x.view(x.size(0), -1)        x = self.classifier(x)        return ximport torchimport torch.nn as nnclass Inception(nn.Module):    """    1、输入通过Inception模块的4个分支分别计算，得到的输出宽和高相同(因为使用了padding)，而通道不同。    2、将4个分支的通道进行简单的合并，即得到Inception模块的输出。    3、每次卷积之后都使用批正则化`BatchNorm2d`，并使用relu函数进行激活。    """    def __init__(self, in_planes, n1x1, n3x3red, n3x3, n5x5red, n5x5, pool_planes):        super().__init__()        # 1x1 conv branch        self.b1 = nn.Sequential(            nn.Conv2d(in_planes, n1x1, kernel_size=1),            nn.BatchNorm2d(n1x1),            nn.ReLU(True),        )        # 1x1 conv -> 3x3 conv branch        self.b2 = nn.Sequential(            nn.Conv2d(in_planes, n3x3red, kernel_size=1),            nn.BatchNorm2d(n3x3red),            nn.ReLU(True),            nn.Conv2d(n3x3red, n3x3, kernel_size=3, padding=1),            nn.BatchNorm2d(n3x3),            nn.ReLU(True),        )        # 1x1 conv -> 5x5 conv branch        self.b3 = nn.Sequential(            nn.Conv2d(in_planes, n5x5red, kernel_size=1),            nn.BatchNorm2d(n5x5red),            nn.ReLU(True),            # 2个3x3卷积代替1个5x5卷积            nn.Conv2d(n5x5red, n5x5, kernel_size=3, padding=1),            nn.BatchNorm2d(n5x5),            nn.ReLU(True),            nn.Conv2d(n5x5, n5x5, kernel_size=3, padding=1),            nn.BatchNorm2d(n5x5),            nn.ReLU(True),        )        # 3x3 pool -> 1x1 conv branch        self.b4 = nn.Sequential(            nn.MaxPool2d(3, stride=1, padding=1),            # nn.Conv2d(in_planes, pool_planes, kernel_size=1),            # nn.BatchNorm2d(pool_planes),            nn.ReLU(True),        )    def forward(self, x):        outpus = [self.b1(x), self.b2(x), self.b3(x), self.b4(x)]        return torch.cat(outpus, dim=1)class GoogNet(nn.Module):    def __init__(self, num_classes=10):        super().__init__()        self.layer1 = nn.Sequential(            nn.Conv2d(1, 10, kernel_size=5),            nn.MaxPool2d(2),            nn.ReLU(True)        )        self.incep1 = Inception(10, 16, 16, 24, 16, 24, 24)        self.layer2 = nn.Sequential(            nn.Conv2d(74, 20, kernel_size=5),            nn.MaxPool2d(2),            nn.ReLU(True)        )        self.incep2 = Inception(20, 16, 16, 24, 16, 24, 24)        self.fc = torch.nn.Linear(1344, num_classes)    def forward(self, x):        out = self.layer1(x)        out = self.incep1(out)        out = self.layer2(out)        out = self.incep2(out)        out = out.view(out.size(0), -1)        out = self.fc(out)        return outimport torch.nn as nnimport torch.nn.functional as F# 3x3 convolutiondef conv3x3(channel):    return nn.Conv2d(channel, channel, kernel_size=3, stride=1, padding=1, bias=False)class ResidualBlock(nn.Module):    def __init__(self, channel):        super().__init__()        self.conv1 = nn.Sequential(            conv3x3(channel),            nn.BatchNorm2d(channel),            nn.ReLU(inplace=True)        )        self.conv2 = nn.Sequential(            conv3x3(channel)        )    def forward(self, x):        out = self.conv1(x)        out = self.conv2(out)        out += x        out = F.relu(out)        return outclass ResNet(nn.Module):    def __init__(self, num_classes=10):        super().__init__()        self.conv1 = nn.Sequential(            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=5),            nn.BatchNorm2d(32),            nn.ReLU(),            nn.MaxPool2d(2)        )        self.reslayer1 = ResidualBlock(32)        self.conv2 = nn.Sequential(            nn.Conv2d(in_channels=32, out_channels=16, kernel_size=5),            nn.BatchNorm2d(16),            nn.ReLU(),            nn.MaxPool2d(2)        )        self.reslayer2 = ResidualBlock(16)        self.fc = nn.Linear(16 * 4 * 4, num_classes)    def forward(self, x):        out = self.conv1(x)        out = self.reslayer1(out)        out = self.conv2(out)        out = self.reslayer2(out)        out = out.view(out.size(0), -1)        out = self.fc(out)        return out

注：库中包含常用的模型结构（含预训练模型），例如AlexNet、VGG、ResNet等；

