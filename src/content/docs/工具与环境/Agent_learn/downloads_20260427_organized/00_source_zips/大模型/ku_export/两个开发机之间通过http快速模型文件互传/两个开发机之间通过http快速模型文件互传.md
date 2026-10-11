---
title: "两个开发机之间通过http快速模型文件互传"
description: "ifconfig -ahttps://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0db09005c38c43d9816eccb9045a"
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\两个开发机之间通过http快速模型文件互传\\两个开发机之间通过http快速模型文件互传.md"
---
# 两个开发机之间通过http快速模型文件互传
发送机操作1、查看ip

ifconfig -a![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0db09005c38c43d9816eccb9045aad5f&docGuid=ZzcJqpu4dgFnW3)

2、打开http 文件传送250端口

sudo python3 -m http.server 250![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0ab2822fb4f84dc79db516f4ff84a795&docGuid=ZzcJqpu4dgFnW3)

接收机操作1、在接收机上请求文件

wget http://172.18.12.141:250/shareData/text2vec-base-chinese/pytorch_model.bin![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=05db55431600464ba88bd1700b19b0f4&docGuid=ZzcJqpu4dgFnW3)

每秒10m+太爽了



注意：以上情况适用于给别人开服务，让其他人能方便快速获取到上G的模型文件，接收方无需提供发送方机子密码。

如果是自己机子互传用scp命令就行，需要接收方知道发送方机子密码，速度是差不多的。

scp star@172.18.12.141:/home/star/shareData/text2vec-base-chinese/pytorch_model.bin .![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b3da9ae00ff04c77b54cef10b2bc5a36&docGuid=ZzcJqpu4dgFnW3)

开发机：

scp root@kongdefu.bcc-szth.baidu.com:/root/zhoujie19/feed/baidu/hpb/feature-extractor/output.tar.gz ./

