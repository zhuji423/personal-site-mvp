---
title: "**1、智能总结关了**"
description: "数字员工固定调用TestOne插件配置"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\如流&ducc&skills&沙箱开发接入指南\\⚙️数字员工注册配置\\数字员工固定调用TestOne插件配置.md"
---
数字员工固定调用TestOne插件配置

如流@数字员工的时候，数字员工后端会根据用户的Query+数字员工设定的角色+配置的插件信息等采用AI综合决定该如何处理，目前已知可能的问题

* 响应比较慢
* 不能稳定的调起自己的插件

# **1、智能总结关了**
![智能总结关了](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f9c97fa9c968491987f066aeb362656c&docGuid=FKQgR3rnlGVnHY "智能总结关了")


# **2、添加干预规则**
**使用正则 .* 实现所有请求一律调起指定的插件**

> 更多用法请参考：[规则干预](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/2tsPs8CtSd/ewNKeMwvuP/mma7C3MbCgkRyw?t=mention&mt=doc&dt=doc)
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f662f5f22522469eae0130a02a3f06d3&docGuid=FKQgR3rnlGVnHY "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f1cabf9921c244e0b14645dfce022391&docGuid=_gPg3pATLaJb5i "")

