---
title: "PaConvert单元测试编写步骤"
description: "【Comate】Zulu编写Pytorch单测实践"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\【Comate】Zulu编写Pytorch单测实践.md"
---
【Comate】Zulu编写Pytorch单测实践

#### 🧑‍🏫 案例作者：[@周威](https://ku.baidu-int.com?t=mention&mt=contact&id=d4dc0490-fce3-11f0-8676-9989e547574d)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了利用Zulu编写Pytorch单测的实践，旨在通过自动化手段保障Pytorch到Paddle代码转换的正确性。面对Pytorch API数量庞大、使用场景多样的挑战，Zulu被用来总结单测编写规范，覆盖参数组合、输入输出形式等，显著提高了测试覆盖范围。通过多轮迭代优化，Zulu成功修改了不规范的单测文件，新增大量测试用例，展现了AI在自动化测试中的巨大潜力。
## 背景
飞桨PaConvert工具支持Pytorch到Paddle的代码自动转换，可以降低Pytorch深度学习框架到Paddle之间代码迁移成本。我们通过编写Pytoch单测来保障任意Pytorch场景下的代码，能否正确转写到Paddle，当前已经存在了大量的Pytorch单测，但是存在两个问题：

1. Pytorch API数量庞大，有高达2000+个，有些API并没完全覆盖单测，需要人工编写单测，耗时耗力
2. Pytorch API的使用场景很多，有些API高达10+个参数，存在各种排列组合的用法，单元测试必须覆盖所有用法，需要编写大量case，耗时耗力



因此考虑用Zulu来完成这部分工作，这部分工作将有利于『保障转换后的Paddle API行为与PyTorch API行为完全一致』。 



## Rule编写过程
**会话链接**：[https://console.cloud.baidu-int.com/comatestack/share/3334](https://console.cloud.baidu-int.com/comatestack/share/3334)



计划先让Zulu总结一份 单测编写步骤与规范，然后将其作为Rule来完成以上2个任务。因此先给了一些语料让Zulu自己来分析。

> #tests #README.md #CONTRIBUTING.md #test_Tensor_device.py
> PaConvert是一个深度学习代码转换的工具库，能自动将Pytorch的代码转换为Paddle代码。为确保转换前后结果的正确，需要编写单元测试。当前已经有了大量单测，请根据当前单测的写法，总结单元测试的编写步骤与规范。包括具体用什么库、文件位置及命名方式、有哪些测试要求规范、有什么规律。给出一份详细的单元测试编写步骤，以及一份单元测试规范。
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3e9e2c88f5144128a0ce1618e86b7c89&docGuid=6DdQPI7dkxlFGf "")
可以看出Zulu给出了单元测试编写规范，内容也基本正确，但和我预期的还有些区别。我这里上面写的 "测试要求规范" 其实是指单测的具体内容方面的规范，而Zulu给出的基本上是写法、命名这些格式规范，这里应该是没有表达清楚需求。

精选了几个写得很完整的单测，让Zulu学习下，重写一份规范。

> #test_Tensor_new_zeros.py #test_add.py #test_max.py #test_split.py
> 你这里给出的规范主要都是一些代码规范上的，这些虽然也没错，但不是我的主要目的。我的目的是增加测试覆盖范围，因此我需要你分析单测在输入形式、输出形式、case数量方面的规范，因为每一个单测都需要包含该接口的所有用法，测试范围需要足够广。我重新给出了几个写得比较好的单测，你可以进一步分析，然后给出一份关于单测测试范围的详细规范。
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6b985e7c3654edf998aa902ea779dc4&docGuid=6DdQPI7dkxlFGf "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2277d1dc775749bf962df09079549fdb&docGuid=6DdQPI7dkxlFGf "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c6e9404b426745a68d28876c078a470b&docGuid=6DdQPI7dkxlFGf "")
内容很详细，包含8条。看起来基本OK了，但这里其实 **参数组合覆盖、参数形式覆盖、参数别名 **这几条最重要，针对这里还想局部优化下，因此继续引导。

> 总结的规范基本正确，注意你需要考虑到 Python参数传入的所有情况，例如输入可以通过 位置参数、默认参数、关键字参数形式传入，如果一个接口包含了多种参数，那么就有很多组合方式。
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=26cd9fc0baaf46d49ae5caec65f74a80&docGuid=6DdQPI7dkxlFGf "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1fce91b966534fdf9afc0dccf3f38937&docGuid=6DdQPI7dkxlFGf "")
这次总结的很好了，包括各种参数用法，尤其是给出了这个 参数组合矩阵，可以看出Zulu已经完全get我的想法了。

上面过程中其实总结了不少规范，虽然有些不是特别重要，但规范越全越好，所以让Zulu根据上文记忆，将所有规范合并起来，给我一个最终版：

> 我们已经总结出了不少规范，规范其实是越全越好，因为请你将上面总结出来的规范取一个并集，给出一份最终规范文档
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0869dbd9e9c74709bb0b8e849c13bb02&docGuid=6DdQPI7dkxlFGf "")
（这里是一个病句，将 因此 打成了因为，但效果不受影响）

这次直接当最终版用了，写入到Rule文件：

```
---
description: PaConvert单元测试规范
globs: tests/test_*.py
alwaysApply: false
---

# PaConvert单元测试编写步骤

1. 创建测试文件

- 在tests/目录下创建测试文件
- 命名格式：test_<API名称>.py 或 test_<功能模块>_<功能名称>.py

2. 编写测试用例

```python
# 1. 导入必要模块
import textwrap
import pytest
from apibase import APIBase

# 2. 创建测试类实例
obj = APIBase("torch.API名称") 

# 3. 编写测试函数
def test_case_1():
    # 使用textwrap.dedent处理多行字符串
    pytorch_code = textwrap.dedent("""
        import torch
        # PyTorch测试代码
        result = torch.API调用
    """)
    # 运行测试
    obj.run(pytorch_code, ["result"])
```

3. 添加特殊条件

```python
@pytest.mark.skipif(
    condition=特殊条件, 
    reason="跳过原因说明"
)
def test_case_with_condition():
    ...
```

# PaConvert单元测试编写规范

1. 文件规范
1.1 文件结构
- 位置：tests/目录下
- 命名：test_<API名称>.py或test_<模块>_<功能>.py
- 必须包含Apache 2.0许可证声明

1.2 测试类
- 继承自APIBase或自定义测试基类
- 类实例化：obj = APIBase("torch.target_api")

2. 测试用例设计规范
2.1 基础覆盖要求
- 每个API的测试用例越多越好

2.2 参数覆盖矩阵
测试维度    覆盖要求           示例
参数数量    所有参数都要测到    dtype, device, requires_grad等
参数形式    位置/关键字/混合参数    func(a,b) vs func(x=a,y=b)
参数顺序    不同参数顺序组合    func(a,b,c) vs func(c=c,a=a)
默认参数    显式传递和默认值    func(a) vs func(a, dim=0)
特殊值        None/空值/边界值    size=0, dim=None
表达式        表达式作为参数        func(1+1, 2*3)

2.3 输入输出覆盖
测试类型    要求           示例
基础功能    最小可用案例    简单张量输入
维度组合    1D/2D/3D输入   不同shape的张量
类型组合    不同dtype组合   float32+float64等
广播机制    不同shape运算    [3]+[1]
梯度计算    前向+反向传播     Tensor.backward()验证
原地操作    inplace操作验证    out=参数

3. 参数传递规范
3.1 参数形式组合
```python
# 1. 纯位置参数
func(a, 2, 1)

# 2. 位置+关键字
func(a, 2, dim=1)

# 3. 纯关键字
func(tensor=a, size=2, dim=1)

# 4. 关键字乱序
func(dim=1, size=2, tensor=a)

# 5. 默认参数
func(a, 2)  # 默认dim=0

# 6. 可变参数
args = (a,2,1); func(*args)
kwargs = {'tensor':a}; func(**kwargs)
```

3.2 特殊参数场景
- 参数别名测试
- 表达式作为参数
- 变量作为参数
- 不支持的功能明确标记
```python
@pytest.mark.skip(reason="Not supported")
def test_unsupported_case():
    ...
```


4. 运行验证方式
```
pytest tests/test_xxx.py
```

5. 完整示例模板
```python
# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
# Licensed under Apache License 2.0

import textwrap
import pytest
from apibase import APIBase

obj = APIBase("torch.target_api")

# 1. 基础用法
def test_case_1():
    pytorch_code = textwrap.dedent("""
        import torch
        result = torch.target_api(torch.tensor([1,2,3]))
    """)
    obj.run(pytorch_code, ["result"])

# 2. 参数组合
def test_case_2():
    pytorch_code = textwrap.dedent("""
        import torch
        result = torch.target_api(torch.tensor([1,2,3]), dim=1, dtype=torch.float32)
    """)
    obj.run(pytorch_code, ["result"])

# 3. 关键字参数乱序  
def test_case_3():
    pytorch_code = textwrap.dedent("""
        import torch
        result = torch.target_api(dtype=torch.float32, input=torch.tensor([1,2,3]), dim=1)
    """)
    obj.run(pytorch_code, ["result"])

# 4. 梯度计算
def test_case_4():
    pytorch_code = textwrap.dedent("""
        import torch
        x = torch.tensor([1.,2.], requires_grad=True)
        y = torch.target_api(x)
        y.backward()
    """)
    obj.run(pytorch_code, ["y", "x.grad"])

# 5. 边界条件
def test_case_5():
    pytorch_code = textwrap.dedent("""
        import torch
        result = torch.target_api(torch.empty(0))
    """)
    obj.run(pytorch_code, ["result"])
```
```


## Rule应用
**会话链接**：[https://console.cloud.baidu-int.com/comatestack/share/3342](https://console.cloud.baidu-int.com/comatestack/share/3342)



由于该目录下有上千个文件，全量文件规范扫描与修改的reiview成本较大，所以目前尝试做一个小批量修改，让找到5个不规范单测进行修改，看看效果

> 根据#paconvert-test-rule.mdr 分析 #tests 目录所有文件内容，选择其中最不符合规范的5个文件进行修改，修改时注意只新增代码，不修改以前的代码。无需关注其中的一些配置文件、工具文件，只关注tests/根目录文件，子目录不关注。
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d000be1282b142ce90df0a6e9d8cdeb5&docGuid=6DdQPI7dkxlFGf "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f2ff78285c9347708cb85b0ac3a49472&docGuid=6DdQPI7dkxlFGf "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f2e89b1ef30445c94fde9442554f3d1&docGuid=6DdQPI7dkxlFGf "")
Zulu首先给出了Plan，然后顺利修改完成了5个单测文件，运行了一下，一共新增23个测试case，其中有7个失败，16个直接运行成功：（还是有点超预期的）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a7ac74b3738f487d9f4c62e8f1815f3a&docGuid=6DdQPI7dkxlFGf "")
能运行成功的case已经merge了，CI验证通过 [https://github.com/PaddlePaddle/PaConvert/pull/768](https://github.com/PaddlePaddle/PaConvert/pull/768)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3ca26acffd154bceac778ddee1a93d79&docGuid=6DdQPI7dkxlFGf "")


运行失败的case人工分析了下，这里是使用了错误的用法：输入数据类型dtype不一致。如果将Pytorch的官网API文档给Zulu，预计可以写对。

```
torch.add(torch.tensor([1, 2, 3]), torch.tensor([1, 4, 6]), alpha=0.5)
```
这里说明模型对Pytorch框架的专有知识还存在一些缺乏，这一块深度学习知识其实是比较深的，当前通用Rule无法完全解决问题，还依赖一个很大的Pytorch专有知识数据库，未来可以结合MCP从官网查询文档、检索文档知识，增加更多专有**信息类Rule**，预计可以降低写错概率。这就还需要更多精细的打磨了。



## 体会
1. 引导AI编写Rule时，可以精选一些good case让AI来学习总结，结果会更符合预期
2. 需求需要描述清楚，含糊的描述容易把路走偏了
3. 打错几个字影响不大，AI会从上下文整体理解
4. 在等待AI回答过程中，自己是有预期答案的，需要循循善诱，一步步朝预期方向校正。人负责纠偏，AI负责即时反馈
5. AI无法保证代码100%正确，需要人工review，这个成本目前还少不了



## **小组总结**
|**组员**|**业务场景**|**心得**|
|-|-|-|
|赵青涛|[使用AIIDE修复cms漏洞](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/zU4PU6Vprl/vfPKTitKnt/tqoEes1-p_CW5Q?t=mention&mt=doc&dt=doc)|最大价值在于ide的功能完善性，本质上还是prompt工程，其实子啊开发中已经在使用了，但是有了ide，对于提效还是有进一步帮助的。|
|元日升|FD代码覆盖率提升，单测补充|多轮对话进行迭代，使用尽可能准确专业的语言描述引导AI去解决问题|
|张博|大模型训练组件研发与开源|在高频迭代的研发场景，存在这很多迭代过程中无用/废弃的代码，可通过 zulu 生成一个死代码检查工具，一键检查出所有死代码并删除|
|罗跃东|paddlecloud平台化功能开发|通过使用Zulu，编写规则，能够自动化生成标准的API接口、数据库CRUD操作等一连串整体的代码，在rules添加业务逻辑描述，告诉它之后，它都能自动帮助完成实现，且有高质量的单测|
|高煜坤|强化学习基建controller中控|通过一步步引导ai解读代码库技术栈、包、整体流程，对代码库的理解更加扎实，开发起来更得心应手|

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
