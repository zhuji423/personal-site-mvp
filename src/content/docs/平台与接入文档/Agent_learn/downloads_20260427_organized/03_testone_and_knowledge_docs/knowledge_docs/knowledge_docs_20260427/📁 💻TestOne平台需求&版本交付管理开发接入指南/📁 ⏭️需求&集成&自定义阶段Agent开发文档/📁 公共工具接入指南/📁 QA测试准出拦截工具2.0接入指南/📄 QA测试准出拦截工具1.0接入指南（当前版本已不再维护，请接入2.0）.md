---
title: "1、函数型工具接入指南"
description: "QA测试准出拦截工具1.0接入指南（当前版本已不再维护，请接入2.0）"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📁 公共工具接入指南\\📁 QA测试准出拦截工具2.0接入指南\\📄 QA测试准出拦截工具1.0接入指南（当前版本已不再维护，请接入2.0）.md"
---
QA测试准出拦截工具1.0接入指南（当前版本已不再维护，请接入2.0）

工具负责人：[@陈伟](https://ku.baidu-int.com?t=mention&mt=contact&id=15747e80-ad5b-11ef-98c6-e99aa5a13800)

对应麒麟服务：213411

![](/personal-site-mvp/img/doc-placeholder.svg "")
接入前请咨询[@陈伟](https://ku.baidu-int.com?t=mention&mt=contact&id=9c743540-ad5d-11ef-98c6-e99aa5a13800)是否支持



# 1、函数型工具接入指南
## 1.1、升级依赖
将 qep-delivery-tools 版本升级到 0.0.4 或者以上版本

> 1、修改requirements.txt 文件
>     qep-delivery-tools==xxx   ->  qep-delivery-tools==0.0.4
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
from qep_delivery_tools import QaTestFinishInterceptTool   # 引入相关工具
...

def execute(self) -> AgentResult:
    """
    Agent 执行工具的入口，这里可以添加一些业务逻辑
    """
    # 当前阶段的所有工具列表
    all_tools = [
        ...
        QaTestFinishInterceptTool()    # 注册到当前阶段需要执行的Tool列表
        ...
    ]
    ...
```


## 1.3、执行效果
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 2、服务型工具接入指南
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"QA测试准出拦截工具1.0-服务型tool"，点击选择

![](/personal-site-mvp/img/doc-placeholder.svg "")


## 2.2、配置参数
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.3、修改参数
![](/personal-site-mvp/img/doc-placeholder.svg "")

