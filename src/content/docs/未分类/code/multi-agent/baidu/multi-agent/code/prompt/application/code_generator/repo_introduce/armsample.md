---
title: "armsample 编码规则"
description: "1. 先通过类型为UtsStrategyCtx的变量（此处是ctx，通常会通过参数传入），获取采样工具变量sampleTool（注意nil值校验） 2. 再调用sampleTool的成员方法IsHitSidByGroup，传入armutsj"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\multi-agent\\baidu\\multi-agent\\code\\prompt\\application\\code_generator\\repo_introduce\\armsample.md"
---
# armsample 编码规则
armsample是一个amis平台对应的ab实验命中判断工具（sdk），经常配合前置的amis配置，在代码中对用户实验命中进行判断

# 核心概念
* amis平台：是一个外部配置平台，当需要开ab实验的时候，研发会在该平台上配置对应的实验配置，并以一个唯一的实验名称（groupName）来标识该实验
* 实验名称：在library/consts/arm_uts_jst.go文件中集中维护
* 实验组：一个实验通常包含多个实验组，一个实验组对应一个sid，命中任何一个实验组意味着命中该实验
* 对照组：一个实验也可以包含多个对照组，一个对照组对应一个sid，命中任何一个对照组意味着不命中该实验

# 实验命中
armsample支持灵活的实验命中判断，常见的有以下几种方式：

## 1.判断用户命中ab实验中任何一个实验组
* 适用场景：当不需要关心具体命中了哪一个试验组，只需要判断是否命中任何一个实验组（即实验）时，使用此方法
* 参考示例：
```go
sampleTool := ctx.GetSampleTool()
	if sampleTool != nil && sampleTool.IsHitSidByGroup(constsLib.LitqCqgLtQInitExp) {
		uscore = 9999.0
		quantile = 9
	}
````

1. 先通过类型为UtsStrategyCtx的变量（此处是ctx，通常会通过参数传入），获取采样工具变量sampleTool（注意nil值校验）
2. 再调用sampleTool的成员方法IsHitSidByGroup，传入arm_uts_jst.go文件中预定义好的对应的实验名称为参数，判断是否命中试验组中的任何一个实验

## 2.判断用户命中实验中具体的一个实验组
* 适用场景：当需要判断命中具体的某一个实验组时（通常是需要针对不同的实验组做不同的处理）
* 参考示例：
```go
sampleTool := ctx.GetSampleTool()
    sidInfo := sampleTool.GetHitSidInfoByGroup(constsLib.LiteCqgLostRedbagExp)

    // 命中实验组1
    if sidInfo.IsGroupA() {
        taskConf = vActLostFirstRedbagLiteConf1
    }

    // 命中实验组2
    if sidInfo.IsGroupB() {
        taskConf = vActLostFirstRedbagLiteConf2
    }
```

* 示例介绍： 这个示例先后判断了用户是否命中实验组1、实验组2
  1. 先通过类型为UtsStrategyCtx的变量（此处是ctx，通常会通过参数传入），获取采样工具变量sampleTool（注意nil值校验）
  2. 再调用sampleTool的成员方法IGetHitSidInfoByGroup，传入arm_uts_jst.go文件中预定义好的对应的实验名称为参数，获取用户命中实验组的情况信息sidInfo（类型为SidInfo）
  3. 接着调用sidInfo的成员方法IsGroupA来判断用户是否命中实验组1
  4. 最后调用sidInfo的成员方法IsGroupA来判断用户是否命中实验组1
* 补充说明：SidInfo类型通过多个成员方法支持多实验组的判断，以下是成员方法及实验组的对应关系
  1. IsGroupA -> 实验组1
  2. IsGroupB -> 实验组2
  3. IsGroupC -> 实验组3
  4. IsGroupD -> 实验组4
  5. IsGroupE -> 实验组5
  6. IsGroupF -> 实验组6
  7. IsGroupG -> 实验组7

# 使用优先级
* 如果不需要判断具体的实验组命中，或者多个实验组的预期变更一致，则使用第一种方式判断实验命中
* 否则，使用第二种方式判断实验命中