---
title: "1、函数型工具接入指南"
description: "GO/PHP/JS覆盖率-表格版工具接入指南"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\公共工具接入指南\\GO_PHP_JS覆盖率-表格版工具接入指南.md"
---
GO/PHP/JS覆盖率-表格版工具接入指南

工具负责人：[@汪世涛](https://ku.baidu-int.com?t=mention&mt=contact&id=8e478870-3452-11ef-b16b-83bf3f71b02a)[@王胜](https://ku.baidu-int.com?t=mention&mt=contact&id=3a02f550-2346-11ef-ab70-adaaacc283ba)

# 1、函数型工具接入指南
## 1.1、升级依赖
> 1、修改requirements.txt 文件
>     qep-delivery-tools==0.4.3  (或者更高版本)
>     qep-delivery-data==0.2.5 (或者更高版本)
>     qep-delivery-component==0.2.8  (或者更高版本)
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
from qep_delivery_tools import CovTableTool   # 引入相关工具
...

def execute(self, parameter: Parameter) -> ToolResult:
    """
    Agent 执行工具的入口，这里可以添加一些业务逻辑
    """
    # icafe_username，icafe用户名，必填 ICAFE_USERNAME, ICAFE_PASSWORD为内置ICafeUtils的账号和密码，需要替换成自己的。获取账号密码详见https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/NbX2gitgSF/4cc48b299a6846
    # icafe_passwork, icafe密码， 必填
    # "language"语言类型， 必填，目前可取值：go、js
    # "type" 类型，必填 取值枚举：最新-latest，最大-max
    # "stage" 阶段，非必填 目前支持：可选值为 "Story_test"、"RD_test"、"Zhunru_test"、"QA_test"、"Zhunchu_test"或 "all"。其中default为"all"
    # "cover_type" 覆盖率类型，非必填 目前支持：可选值为"all"（分支覆盖率和story覆盖率）、"branch"（分支覆盖率）、"story"（story覆盖率）。其中default为"all"
    ...
    # 当前阶段的所有工具列表
    all_tools = [
        ... 
        CovTableTool(language="xx", type="xx", icafe_username=ICAFE_USERNAME, icafe_password=ICAFE_PASSWORD)
        # CovTableTool(language="xx", type="xx", icafe_username=ICAFE_USERNAME, icafe_password=ICAFE_PASSWORD, stage="Story_test", cover_type="branch")
        ...
    ]
    ...
```
> 以下仅以测试阶段为例，如果需要在其他阶段使用，参考更改其他阶段的Agent即可
> 业务自己获取卡片下的所有module和branch，并构造入参。优点是，每一个不同的module和branch可自定义language和type
```
...
from qep_delivery_data import ICafeUtils
from qep_delivery_data import split_icafe_card_to_space_and_sequence
from qep_delivery_tools import CovTableTool   # 引入相关工具
...

def execute(self, parameter: Parameter) -> ToolResult:
    """
    Agent 执行工具的入口，这里可以添加一些业务逻辑
    """
    # ICAFE_USERNAME, ICAFE_PASSWORD为内置ICafeUtils的账号和密码，需要替换成自己的
    # 获取账号密码详见https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/NbX2gitgSF/4cc48b299a6846
    utils = ICafeUtils(icafe_username, icafe_passwork)
    unique_pairs = set()
    module_branch_icafe_id_mapping = dict()
    for icafe_id in parameter.icafe_ids:
        # 获取空间ID和卡片ID
        space_id, card_id = split_icafe_card_to_space_and_sequence(icafe_id)
        # 获取module和branch
        result = utils.get_code_dev_info(space_id, int(card_id))
        if len(result.codeReview) != 0:
            for entry in result.codeReview:
                if entry.projectName and entry.branch:
                    unique_pairs.add((entry.projectName, entry.branch))
                    module_branch_icafe_id_mapping[f'{entry.projectName}{entry.branch}'] = icafe_id
        elif len(result.codeMerge) != 0:
            for entry in result.codeMerge:
                if entry.projectName and entry.branch:
                    unique_pairs.add((entry.projectName, entry.branch))
                    module_branch_icafe_id_mapping[f'{entry.projectName}{entry.branch}'] = icafe_id
        else:
            continue
    params = list()
    for module, branch in unique_pairs:
        # "language"为语言类型，目前可取值：go、js
        # "type"取值枚举：最新-latest，最大-max
        # 如果language为js，必须要传递一个参数icafeId
        if language == "js":
            icafe_id = module_branch_icafe_id_mapping.get(f'{module}{branch}')
            params.append({"module": module, "branch": branch,
                           "language": language, "type": type, "icafeId": icafe_id})
        else:
            params.append({"module": module, "branch": branch, "language": language, "type": type})
        
   
    ...
    # 当前阶段的所有工具列表
    all_tools = [
        ... 
        # param示例：[{"module": "baidu/newapp/server-admin", "branch": "server-admin_1-5-497_BRANCH", "language": "go", "type": "latest"}]
        CovTableTool(params)   # 注册到当前阶段需要执行的Tool列表
        # CovTableTool(params, stage="Story_test", cover_type="story")   # 当前支持传递阶段，即stage，目前支持：可选值为 "Story_test"、"RD_test"、"Zhunru_test"、"QA_test"、"Zhunchu_test"或 "all"。其中default为"all"
        ...
    ]
    ...
```
## 1.3、执行效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=104988fe17fc4259a5ec2fe6cb2befff&docGuid=382346940cae47 "")


# 2、服务型工具接入指南
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d96dc009e2394b40bb3db8bcf1381a0c&docGuid=382346940cae47 "")
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"PHP/GO/JS覆盖率展示-表格版-服务型tool"，点击选择

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5b513ce438db4112b11fcae581bfab9c&docGuid=382346940cae47 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=21bde80ebc4140e4a6000baed033a23f&docGuid=382346940cae47 "")
## 2.2、配置参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9fa3edf160314ec48430bb8b84ef8c26&docGuid=382346940cae47 "")
## 2.3、修改参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2419a006dee749f89e23599b3e32b1cb&docGuid=382346940cae47 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cd269314f14e47cd86b964ea1728ee0f&docGuid=382346940cae47 "")

