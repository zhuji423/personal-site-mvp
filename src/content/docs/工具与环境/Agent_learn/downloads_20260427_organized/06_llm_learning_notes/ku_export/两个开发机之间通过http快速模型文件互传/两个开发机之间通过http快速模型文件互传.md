---
title: "两个开发机之间通过http快速模型文件互传"
description: "ifconfig -a../../../remoteimages/7d4e5d4f01ad43d014ceab2f5eb1ad040db5308a.png"
date: "2026-04-28"
category: "工具与环境"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\两个开发机之间通过http快速模型文件互传\\两个开发机之间通过http快速模型文件互传.md"
---
# 两个开发机之间通过http快速模型文件互传
发送机操作1、查看ip

ifconfig -a![](/personal-site-mvp/img/doc-placeholder.svg)

2、打开http 文件传送250端口

sudo python3 -m http.server 250![](/personal-site-mvp/img/doc-placeholder.svg)

接收机操作1、在接收机上请求文件

wget http://172.18.12.141:250/shareData/text2vec-base-chinese/pytorch_model.bin![](/personal-site-mvp/img/doc-placeholder.svg)

每秒10m+太爽了



注意：以上情况适用于给别人开服务，让其他人能方便快速获取到上G的模型文件，接收方无需提供发送方机子密码。

如果是自己机子互传用scp命令就行，需要接收方知道发送方机子密码，速度是差不多的。

scp star@172.18.12.141:/home/star/shareData/text2vec-base-chinese/pytorch_model.bin .![](/personal-site-mvp/img/doc-placeholder.svg)

开发机：

scp root@kongdefu.bcc-szth.baidu.com:/root/zhoujie19/feed/baidu/hpb/feature-extractor/output.tar.gz ./

