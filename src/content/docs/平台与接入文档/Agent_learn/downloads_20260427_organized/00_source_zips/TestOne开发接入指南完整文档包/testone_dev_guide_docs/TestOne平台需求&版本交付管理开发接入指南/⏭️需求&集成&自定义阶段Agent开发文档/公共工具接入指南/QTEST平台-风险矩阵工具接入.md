---
title: "1、函数型工具接入指南"
description: "QTEST平台-风险矩阵工具接入"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\公共工具接入指南\\QTEST平台-风险矩阵工具接入.md"
---
QTEST平台-风险矩阵工具接入

工具负责人：[@石雪](https://ku.baidu-int.com?t=mention&mt=contact&id=4e54fc10-2346-11ef-ab70-adaaacc283ba)

注意：

* 只支持在测试阶段Agent使用  
* 必须是走QTEST提测的卡片才支持

风险矩阵能力介绍：[策略使用须知](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/wtP_bONRck/W9oFtQ3j_SG-Ho#anchor-759ec600-d771-11ee-bda4-a7fec5a507e9?t=mention&mt=doc&dt=doc)

# 1、函数型工具接入指南
## 1.1、升级依赖
将 qep-delivery-tools 版本升级到 0.3.1 或者以上版本， 参考：[SDK版本升级指南](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/tuuZlyo_neWnQq?t=mention&mt=doc&dt=doc)

## 1.2、修改测试阶段Agent
```
...
from qep_delivery_tools import QTestRiskMatrixTool
...


all_tools = [
    ...
    
    # param TESTONE_USERNAME: TestOne平台用户名
    # param TESTONE_TOKEN: Testone平台用户对应的API访问Token
    # param KIRIN_USERNAME: 麒麟用户名
    # param KIRIN_TOKEN: 麒麟Token
    # param QADC_USERNAME: QADC用户名
    # param QADC_TOKEN: QADC token
    # param service_id: 自己需求对应的业务在QTEST平台配置的服务标识ID 获取方式：QTEST->左侧导航栏->质量度特征配置
    QTestRiskMatrixTool(TESTONE_USERNAME, TESTONE_TOKEN, KIRIN_USERNAME, KIRIN_TOKEN, QADC_USERNAME, QADC_TOKEN, service_id)  # 自己需求对应的业务在QTEST平台配置的服务标识ID 获取方式：QTEST->左侧导航栏->质量度特征配置
    ...

]
```
# 2、服务型工具接入指南
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1c2e232a93a041308f7a1cbeab0f1f20&docGuid=a25378d7c7404f "")
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"风险矩阵-服务型tool"，点击选择

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=59ab4726896d47388d6956df9f1c40ab&docGuid=a25378d7c7404f "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f3040f768d0f45cab09852ec15f644a1&docGuid=a25378d7c7404f "")
## 2.2、配置参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b96e690cfe62479c9feddb6cd9b87ee5&docGuid=a25378d7c7404f "")
## 2.3、修改参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ba6681496c54db2909570c61178f270&docGuid=a25378d7c7404f "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f6d1f923f0e4e219fb56061e66127a5&docGuid=a25378d7c7404f "")
