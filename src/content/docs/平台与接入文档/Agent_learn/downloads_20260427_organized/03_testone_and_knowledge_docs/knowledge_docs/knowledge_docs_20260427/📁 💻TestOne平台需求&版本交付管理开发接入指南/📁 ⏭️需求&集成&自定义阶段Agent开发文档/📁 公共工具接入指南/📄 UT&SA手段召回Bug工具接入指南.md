---
title: "1、函数型工具接入指南"
description: "UT&SA手段召回Bug工具接入指南"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📁 公共工具接入指南\\📄 UT&SA手段召回Bug工具接入指南.md"
---
UT&SA手段召回Bug工具接入指南

工具负责人：[@王胜](https://ku.baidu-int.com?t=mention&mt=contact&id=3a02f550-2346-11ef-ab70-adaaacc283ba)[@侯澄](https://ku.baidu-int.com?t=mention&mt=contact&id=3d156570-2346-11ef-ab70-adaaacc283ba)

# 1、函数型工具接入指南
## 1.1、升级依赖
> 1、修改requirements.txt 文件
>     qep-delivery-tools==0.1.0  (或者更高版本)
>     qep-delivery-component==0.0.2.1  (或者更高版本)
> 2、更新包
>     pip3 install -r requirements.txt -U
注意：

* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt
* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt
* 禁止 直接 pip3 install qep-delivery-tools更新本地环境，但是不修改requirements.txt



由于打包的时候会根据requirements.txt引用的版本号进行打包，不更新requirements.txt文件，会导致本地测试符合预期，但是上线后出现依赖引入异常



## 1.2、修改Agent
> 以下仅以测试阶段为例，如果需要在其他阶段使用，参考更改其他阶段的Agent即可
```
...
from qep_delivery_tools import UtSaBugTool   # 引入相关工具
...

def execute(self) -> AgentResult:
    """
    Agent 执行工具的入口，这里可以添加一些业务逻辑
    """
    # 当前阶段的所有工具列表
    all_tools = [
        ...
        UtSaBugTool()    # 注册到当前阶段需要执行的Tool列表
        ...
    ]
    ...
```


## 1.3、执行效果
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 2、服务型工具接入指南
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"UT&SA召回问题-服务型tool"，点击选择

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")



