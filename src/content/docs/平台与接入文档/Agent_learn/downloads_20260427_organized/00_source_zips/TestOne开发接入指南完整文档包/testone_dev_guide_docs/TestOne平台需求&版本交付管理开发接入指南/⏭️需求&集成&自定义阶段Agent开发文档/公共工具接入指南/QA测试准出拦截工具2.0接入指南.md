---
title: "1、函数型工具接入指南"
description: "QA测试准出拦截工具2.0接入指南"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\公共工具接入指南\\QA测试准出拦截工具2.0接入指南.md"
---
QA测试准出拦截工具2.0接入指南

工具负责人：[@陈伟](https://ku.baidu-int.com?t=mention&mt=contact&id=15747e80-ad5b-11ef-98c6-e99aa5a13800)

对应麒麟服务：214332、214349

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b22859144eec4d9f816b32ecf2278397&docGuid=9ti1hRa5AM-ZzH "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c3843382b4144516a8bab91f205acdd6&docGuid=9ti1hRa5AM-ZzH "")
接入前请咨询[@陈伟](https://ku.baidu-int.com?t=mention&mt=contact&id=9c743540-ad5d-11ef-98c6-e99aa5a13800)是否支持



# 1、函数型工具接入指南
## 1.1、升级依赖
将 qep-delivery-tools 版本升级到 0.4.9 或者以上版本，qep-delivery-data 版本升级到0.2.8或者以上版本

> 1、修改requirements.txt 文件
>     qep-delivery-tools==xxx   ->  qep-delivery-tools==0.4.9
>     qep-delivery-data==xxx   ->  qep-delivery-data==0.2.8
> 2、更新包
>     pip3 install -r requirements.txt -U
注意：

* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt
* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt
* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt



由于打包的时候会根据requirements.txt引用的版本号进行打包，不更新requirements.txt文件，会导致本地测试符合预期，但是上线后出现依赖引入异常



## 1.2、修改Agent
> 修改测试阶段Agent
```
...
from qep_delivery_tools import TestFinishInterceptTool   # 引入相关工具
...

def execute(self) -> AgentResult:
    """
    Agent 执行工具的入口，这里可以添加一些业务逻辑
    """
    # 当前阶段的所有工具列表
    all_tools = [
        ...
        TestFinishInterceptTool(kirin_username, kirin_token, extend_timeout)    # 注册到当前阶段需要执行的Tool列表
        ...
    ]
    ...
```


## 1.3、执行效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ed928681e754bd785496ddaef017f05&docGuid=PfnFSWTva1sux4 "")


# 2、服务型工具接入指南
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=94144594ceaf413e8e90323f094e3e95&docGuid=PfnFSWTva1sux4 "")
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"QA测试准出拦截工具2.0-服务型tool"，点击选择

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=037c911fd6cc489c9319eb366aacf3ed&docGuid=PfnFSWTva1sux4 "")
## 2.2、配置参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=85b9e81d461742819588c179e96e83a1&docGuid=PfnFSWTva1sux4 "")
## 2.3、修改参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b6ac7133570743258e1f51af013d1a51&docGuid=PfnFSWTva1sux4 "")

