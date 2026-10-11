---
title: "orp查看iknow集群的机器实例"
description: "orp查看iknow集群的机器实例"
date: "2026-04-28"
category: "工具与环境"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\04_personal_knowledge_export\\knowledge_export_20260427\\orp查看iknow集群的机器实例.md"
---
orp查看iknow集群的机器实例

本页面由边俊柯于2022/04/08迁移自wiki 孟新萍空间
如果是非orp的集群，通过开发机 [mengxinping@cq01-rdqa-dev066.cq01.baidu.com](mailto:mengxinping@cq01-rdqa-dev066.cq01.baidu.com) 登陆中转机

1、ssh [tc-iknow-spam00.tc](http://tc-iknow-spam00.tc) 

2、sudo -iu rd（1,2两部等同于命令ssh -t [mengxinping@tc-iknow-spam00.tc](mailto:mengxinping@tc-iknow-spam00.tc) sudo -u rd -iH）

3、list all submit  就是查询到的模块 

[图片文件未导出：image_001.bin（原路径：`./ku_assets/CKf99Ha4WxzIFR/image_001.bin`）]
4、ssh db-iknow-tips00.db01 

但是现在大部分的app都迁移到了orp上， 那么怎么去check 基础知道的模块呢？

**首先登陆基础知道的orp中转机**

**1、ssh -t  mengxinping**[@cq02-orp-rd00.cq02.baidu.com](mailto:chenzhenyu01@cq02-orp-rd00.cq02.baidu.com)** sudo -u rd -iH （或者ssh -t **[username@yf-orp-apollo.yf01](mailto:qinpiqi@yf-orp-apollo.yf01)** sudo -u rd -iH 主意改中转机需要BAIDU_NS_KSN_orp权限，op不鼓励使用）**

**2、ofind iknow-normal 或者 ofind iknow-wap  （前者是pc的， 后者是手机浏览器的）**

[图片文件未导出：image_002.bin（原路径：`./ku_assets/CKf99Ha4WxzIFR/image_002.bin`）]
3、ssh 一台机器 ，然后 cdapp iknow-normal

具体操作例子：

1、list服务机（机器是动态变化的）

**ofind spamdata**

[图片文件未导出：image_003.bin（原路径：`./ku_assets/CKf99Ha4WxzIFR/image_003.bin`）]
2、登陆服务机

ssh dbl-orp-app0136.dbl01

3、进入服务根目录

cdapp spamdata

 

 

**
**
