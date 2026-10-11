---
title: "1、接入指南"
description: "Server端代码变更影响分析信息-表格版"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\公共工具接入指南\\Server端代码变更影响分析信息-表格版.md"
---
Server端代码变更影响分析信息-表格版

工具负责人：[@汪世涛](https://ku.baidu-int.com?t=mention&mt=contact&id=66695440-3458-11ef-b16b-83bf3f71b02a)[@王冬冬](https://ku.baidu-int.com?t=mention&mt=contact&id=68c91630-3458-11ef-b16b-83bf3f71b02a)

# 1、接入指南
## 1.1、升级依赖
> 1、修改requirements.txt 文件
>     qep-delivery-tools==0.1.3  (或者更高版本)
>     qep-delivery-data==0.1.2  (或者更高版本)
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
from qep_delivery_tools import ServerDiffAffectTool   # 引入相关工具
...

def execute(self) -> AgentResult:
    """
    Agent 执行工具的入口，这里可以添加一些业务逻辑
    """
    # 当前阶段的所有工具列表
    all_tools = [
        ...
        ServerDiffAffectTool(qadc_username, qadc_token, story_id, module_name, branch_name) # 注册到当前阶段需要执行的Tool列表
        ...
    ]
    ...
```


## 1.3、执行效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=92869de5c1634b5ca4b6c7964fe5eeac&docGuid=cdefdf7c403c4b "")
