---
title: "**实践简介**"
description: "skill助力检测引擎验证"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\skill助力检测引擎验证.md"
---
skill助力**检测引擎验证

#### 🧑‍🏫 案例作者：[@程亚琳](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：数据分析、测试
#### 🔧 使用工具：Ducc
#### 📒 案例概要：在**检测引擎验证工作中，检测引擎产出的文件为parque文件，parque不方便直接查看，且存在大量不需要关注的日志内容。本文将使用skill实现一个用于快速对比两个 Parquet 文件差异的自动
# **实践简介**
在盗刷检测引擎验证工作中，检测引擎产出的文件为parque文件，parque不方便直接查看，且存在大量不需要关注的日志内容。本文将使用skill实现一个用于快速对比两个 Parquet 文件差异的自动化工具，专门用于防盗刷盗刷检测引擎验证场景中的数据比对分析。



**案例贡献人：**程亚琳

**关键词：**Coding Agent、skill、项目级工具建设



# **具体实施**
#### skill是怎么来的？
```
请帮我创建一个当前项目级的skill，作用是在用户提问"当前结果为xx1.parque, 历史parque为xx2.parque，请帮我对比结果"，将用户提供的两个parquet文件使用trans_parquet2csv.py转为两个csv文件，如果文件名中包含geo则对比r     
  iskTag列的数据是否一致，如果不一致则输出基于历史版本缺少了什么多了什么。如果文件名中包含cdn则对比ip列的是否一致，如果不一致则输出基于历史版本多了哪些ip，少了哪些ip   
```
![按照需求生成一个skill脚本](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b93c48193ff742958c08a2da132f65ba&docGuid=Y6ZrDM9-vLVpv5 "按照需求生成一个skill脚本")
![调用方式说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=320de044aef54f31b330dcb13634288e&docGuid=Y6ZrDM9-vLVpv5 "调用方式说明")
![安装依赖环境](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c0e9ed8ede214c10a267f5a92bf7818b&docGuid=Y6ZrDM9-vLVpv5 "安装依赖环境")
#### 尝试调用skill（失败）
![geolog检测结果验证（一致时）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d4e938c3b22946f0a36c3c79de84679c&docGuid=Y6ZrDM9-vLVpv5 "geolog检测结果验证（一致时）")
![geolog检测结果验证（不一致时）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5e122874fa4b4758a6686e3b9ce57b66&docGuid=Y6ZrDM9-vLVpv5 "geolog检测结果验证（不一致时）")


![cdnlog检测结果验证（一致时）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2c8df8775bd242cb90832fc2b87a8777&docGuid=Y6ZrDM9-vLVpv5 "cdnlog检测结果验证（一致时）")
![cdnlog检测结果验证（不一致时）](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8d11e26ce4fe4344a95fde125cb75ae0&docGuid=Y6ZrDM9-vLVpv5 "cdnlog检测结果验证（不一致时）")


#### 优化skill
![将达到预期的实现过程保存到skill中](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=15f67714959645ca8efe5d9deb6e84e2&docGuid=Y6ZrDM9-vLVpv5 "将达到预期的实现过程保存到skill中")
![尝试重新调用提示未加载](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bf46ec75151440058630a19c874925cb&docGuid=Y6ZrDM9-vLVpv5 "尝试重新调用提示未加载")


#### 如何加载skill？
![重启加载](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bfd8195784a34784b4f5b9c386338424&docGuid=Y6ZrDM9-vLVpv5 "重启加载")
![skill 的格式需要放在 .claude/skills/<name>/SKILL.md 目录下，文件名必须是 SKILL.md](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=925a5d508caa46b18a0b212bdf062aad&docGuid=Y6ZrDM9-vLVpv5 "skill 的格式需要放在 .claude/skills/<name>/SKILL.md 目录下，文件名必须是 SKILL.md")
#### 我的项目级skill：
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ab3f4413547c4415a811f9c77a4592a4&docGuid=Y6ZrDM9-vLVpv5 "")


#### 为什么要用skill？
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c102ecd49cf441a0b422a9c5bce07a93&docGuid=Y6ZrDM9-vLVpv5 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=050f1fa0599044c493ee86b5dfa4af0c&docGuid=Y6ZrDM9-vLVpv5 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8a22c2a6a320452bb99c3feefcb732d7&docGuid=Y6ZrDM9-vLVpv5 "")
![流程固定的场景，直接使用zulu询问，每次回答都需要重新生成code且结果偏离预期](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9405cd106b724774804941581c6d7c84&docGuid=Y6ZrDM9-vLVpv5 "流程固定的场景，直接使用zulu询问，每次回答都需要重新生成code且结果偏离预期")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=969fc11da65d41cb8b42d61bd5889f9b&docGuid=Y6ZrDM9-vLVpv5 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5883b8637aa74e72a63aa62218272b56&docGuid=Y6ZrDM9-vLVpv5 "")
#### 使用skill的效果
![cdnlog检测对比](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f9edbb21aa3248dca3c8847dfa84fa30&docGuid=Y6ZrDM9-vLVpv5 "cdnlog检测对比")
![cdnlog检测对比](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=91a4df9de9304b22b51b3bb1731106b2&docGuid=Y6ZrDM9-vLVpv5 "cdnlog检测对比")
![geolog检测对比](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3233d0ac6e8f4707976f49247349d2a1&docGuid=Y6ZrDM9-vLVpv5 "geolog检测对比")
![geolog检测对比](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=621941b0fc224518aaffed0bb8a2f3de&docGuid=Y6ZrDM9-vLVpv5 "geolog检测对比")
结果清晰且无其他多余操作



#### skill分享给研发使用，应用于自测环节
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc3c85ac05dd4c54a374b45d72613f60&docGuid=Y6ZrDM9-vLVpv5 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f800a7da5519435ab4406e9d70613f0a&docGuid=Y6ZrDM9-vLVpv5 "")
# **复盘**
## **好的经验（可复用的方法论）**
1. **确定作用范围：**

    * 项目级工具推荐使用项目级skill

2. **不求一步到位**：

    * 首次生成的skill可以根据结果进行过程优化。

3. **skill 的格式**：

    * 需要放在 .claude/skills/<name>/SKILL.md 目录下，文件名必须是 SKILL.md。

## **反模式（需避免的坑）**
1. **首次生成的skill不建议直接分享使用**

    * 首次生成的skill建议多使用正向和反向的case验证通过后再进行分享使用

  

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
