---
title: "自定义阶段agent接入（版本迭代中，步骤会有变化，请密切关注）"
description: "自定义阶段agent接入（版本迭代中，步骤会有变化，请密切关注）"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\自定义阶段agent接入（版本迭代中，步骤会有变化，请密切关注）.md"
---
自定义阶段agent接入（版本迭代中，步骤会有变化，请密切关注）

#### 找[@陈艺能](https://ku.baidu-int.com?t=mention&mt=contact&id=50555850-795b-11ef-8eff-c9a0611b210e)注册自定义阶段，提供自定义阶段名称，获取自定义阶段的id
#### 基于agent模板开发自定义阶段agent
[文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/tree/master/agent?t=mention&mt=doc&dt=sdk)

##### **1）升级sdk**
qep-delivery-tools升级到0.4.1

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=32ebaa47d5924055881051b0ac5ec7f0&docGuid=4AEvQUaFm5WHWC "")


##### **2）在代码中注册自定义阶段对应的agent**
其中的**自定义阶段id**和**自定义阶段agent类**更改成业务所需的值

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cd500f9c624348719c000487bcc63f0e&docGuid=4AEvQUaFm5WHWC "")


##### 3）基于入参运行对应的agent
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a0cee7af51274112a5f800f72a3076d3&docGuid=4AEvQUaFm5WHWC "")


##### **4）在agents文件夹中管理自定义阶段agent**
在agent中调用自定义阶段tool

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a2464a4ba7944d349677c21a0ae5689b&docGuid=4AEvQUaFm5WHWC "")


##### **5) 在tools文件夹中管理自定义阶段tool**
在开发者中心创建一个私有函数型tool，获取到工具id，替换到代码中

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e522d687ddab45b9ba30ce3fef3f4350&docGuid=4AEvQUaFm5WHWC "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6f135ae82be84f96bf00b95690df9003&docGuid=4AEvQUaFm5WHWC "")


##### **6）打包部署到kirin平台**
获取到kirin服务id

##### **7）在开发者中心创建一个自定义阶段的agent**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ef6ea912dd5948858a2b250d719b9429&docGuid=4AEvQUaFm5WHWC "")
注册好了以后，找[@楼瀚琼](https://ku.baidu-int.com?t=mention&mt=contact&id=5cb80d20-795d-11ef-8eff-c9a0611b210e)，将第一步获取到的自定义阶段id给到楼瀚琼，由楼瀚琼在后端直接配置到agent上（暂时不支持前端直接映射阶段）

##### 8）调试
输入自定义版本号，找[@陈艺能](https://ku.baidu-int.com?t=mention&mt=contact&id=ce0db920-795d-11ef-8eff-c9a0611b210e)，在后端配置版本号与需求卡片的映射，点击执行，可以看到测试结果



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f2fe47df770342c396783dd4b4bfbb30&docGuid=4AEvQUaFm5WHWC "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc542f4d67ea4d86b0b3eccb8fe1bd9d&docGuid=4AEvQUaFm5WHWC "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=544b21caaecc4add8bbdce91747969da&docGuid=4AEvQUaFm5WHWC "")
##### 9）组合排列阶段，配置agent，正式执行
找[@陈艺能](https://ku.baidu-int.com?t=mention&mt=contact&id=a8145ec0-7cca-11ef-8f5f-8d8eaec1d136)给多个自定义阶段排列执行顺序（前端Q4提供）

找[@楼瀚琼](https://ku.baidu-int.com?t=mention&mt=contact&id=ba3861f0-7cca-11ef-8f5f-8d8eaec1d136)给每个自定义阶段配置相应的agent（前端Q4提供）

找[@陈艺能](https://ku.baidu-int.com?t=mention&mt=contact&id=d12a19d0-7cca-11ef-8f5f-8d8eaec1d136)演示版本和卡片的绑定方法和触发整个流程中的各个阶段的方法




