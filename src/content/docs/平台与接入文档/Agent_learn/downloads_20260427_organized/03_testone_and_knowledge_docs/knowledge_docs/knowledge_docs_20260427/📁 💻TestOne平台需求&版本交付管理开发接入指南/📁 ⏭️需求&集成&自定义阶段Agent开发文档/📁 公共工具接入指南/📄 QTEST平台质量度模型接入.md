---
title: "1、函数型工具接入指南"
description: "QTEST平台质量度模型接入"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📁 公共工具接入指南\\📄 QTEST平台质量度模型接入.md"
---
QTEST平台质量度模型接入

工具负责人：[@石雪](https://ku.baidu-int.com?t=mention&mt=contact&id=4e54fc10-2346-11ef-ab70-adaaacc283ba)

注意：

* 只支持在测试阶段Agent使用  
* 必须是走QTEST提测的卡片才支持



# 1、函数型工具接入指南
## 1.1、升级依赖
将 qep-delivery-tools 版本升级到 0.0.9 或者以上版本

> 1、修改requirements.txt 文件
>     qep-delivery-tools==xxx   ->  qep-delivery-tools==0.0.9
> 2、更新包
>     pip3 install -r requirements.txt -U
注意：

* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt
* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt
* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt



由于打包的时候会根据requirements.txt引用的版本号进行打包，不更新requirements.txt文件，会导致本地测试符合预期，但是上线后出现依赖引入异常



## 1.2、修改测试阶段Agent
```
...
from qep_delivery_tools import QtestRiskModelTool
...


all_tools = [
    ...
    QtestRiskModelTool(TESTONE_USERNAME, TESTONE_TOKEN, KIRIN_USERNAME, KIRIN_TOKEN, service_id)  # 自己需求对应的业务在QTEST平台配置的服务标识ID 获取方式：QTEST->左侧导航栏->质量度特征配置
    ...

]
```
# 2、服务型工具接入指南
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"服务端-质量度风险模型-服务型tool"，点击选择

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.2、配置参数
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.3、修改参数
![](/personal-site-mvp/img/doc-placeholder.svg "")
