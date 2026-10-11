---
title: "1、函数型工具接入指南"
description: "QaMate脑图用例生成工具"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\公共工具接入指南\\QaMate脑图用例生成工具.md"
---
QaMate脑图用例生成工具

**本工具只支持icafe内容的生成，如需要ku内容参考**[端到端用例生成](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/ZV7hybZXiu/jfnxEJUuHDOXgb?t=mention&mt=doc&dt=doc)

# 1、函数型工具接入指南
### 安装公共工具sdk
1. 需先配置百度pip源，可参考[3.1-python-sdk](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/J71vLy9tCR/sVfJHD86pLJ4pE#anchor-7ab65880-9a04-11ec-9861-8367451d60a1?t=mention&mt=doc&dt=doc)
2. pip install qep_delivery_tools
3. 若已安装qep_delivery_tools请先卸载再安装最新版本：0.4.4



### QAMate平台Token获取
[https://qamate.baidu-int.com/lazymind/#/case/index](https://qamate.baidu-int.com/lazymind/#/case/index)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aac524e75d424233a9ac00b9d8724a57&docGuid=RBIl16sMLoTvPq "")


### 调用方式
在agent.py中调用QaMate脑图用例生成工具sdk

from qep_delivery_tools import BrainCaseGenerateTool

tool = BrainCaseGenerateTool(ak, sk, case_info, generation, callback, sign)

tool_result = tool.execute(self.parameter)

```
import logging

from qep_delivery_tools import BaseAgent
from qep_delivery_tools import BrainCaseGenerateTool
from qep_delivery_tools import SignInfo
from qep_delivery_tools import CaseInfo
from qep_delivery_tools import Parameter
from qep_delivery_tools import AgentResult
from qep_delivery_tools import ToolResultCallbackRequest

from common.constants import TESTONE_USERNAME
from common.constants import TESTONE_TOKEN


class XXXXXStageAgent(BaseAgent):
    """
    XXXXX阶段agent
    """

    def __init__(self, parameter: Parameter):
        super().__init__(parameter)

    def execute(self) -> AgentResult:
        """
        Agent 执行工具的入口，这里可以添加一些业务逻辑
        """
        # 用例信息，必填
        # Qamate 空间 id，必填
        qamate_module_id = 6 
        # Qamate 计划 id，选填
        qamate_group_id = 1
        # Qamate 用例在用例树中的父节点id, 选填
        parent_tree_node_id = 1
        # 用例名称，选填
        case_name = "test"
        # 用例类型，选填
        os_type = 0
        case_info = CaseInfo(qamate_module_id, qamate_group_id, parent_tree_node_id, case_name, os_type)
        
        # 签章配置，默认使用平台上的签章配置，选填
        # 签章阶段, 选填
        sign_stage = [0, 1]
        # 签章方式, 选填
        sign_type = 0
        sign_info = SignInfo(sign_stage, sign_type)
        
        # 触发用户, 可用testone平台触发用户赋值，trigger_user = self.parameter.operator
        trigger_user = "zhangsan"
        # QAMateToken，从QAMate平台获取
        qamate_token = "1111111XXXXXX222222"
        # 生成策略 联系QAMate获取
        generate_task_key = "XXX"
        
        # tool初始化
        tool = BrainCaseGenerateTool(trigger_user, qamate_token, case_info, self.parameter.icafe_ids, generate_task_key, sign_info)

        # tool执行
        tool_result = tool.execute(self.parameter)
        callback_request = ToolResultCallbackRequest(self.parameter.engine_task_id, [tool_result])

        # tool执行完成，结果回调
        try:
            is_success = self.callback(TESTONE_USERNAME, TESTONE_TOKEN, callback_request)
        except Exception as e:
            logging.error("tool result callback failed: %s", e)
            is_success = False
        if not is_success:
            logging.error("tool result callback failed")

        # agent执行结束，返回agent结果
        return AgentResult(self.parameter.engine_task_id)
```
### 参数说明
|参数名|必填参数|参数类型|参数说明|参数案例|备注|
|-|-|-|-|-|-|
|qamate_module_id|是默认取testOne关联的qamate产品线|int|业务 Qamate 空间id|1|qamate 业务线id; int;|
|qamate_group_id|否默认『未计划』|int|业务 Qamate 用例计划 id|1|qamate 用例计划id; int|
|parent_tree_node_id|否默认『根节点』|int|Qamate 用例树中的父节点 id|0|qmate 用例前序用例树节点id; int|
|case_name|否默认为story标题内容|string|用例名称|生成用例|脑图名|
|os_type|否默认业务配置值|int|用例端类型|1|用例类型; int; 枚举值 1-Android; 2-iOS; 3-Android&ios; 4-server, 5-web, 6-harmony|
|sign_stage|否默认业务配置|list|端签章阶段|[0,1]|签章阶段; int; 必填; 枚举值 0-准入, 1-准出|
|sign_type|否默认业务配置|int|用例签章方式|0|签章类型; int; 必填; 枚举值 0-分端签章, 1-共同签章|
|trigger_user|是|string|调用来源，触发用户|zhangsan|可使用testone平台参数"触发用户"来赋值self.parameter.operator|
|qamate_token|是|string|在 QAMate 平台业务配置中查看业务自身的 Token|jhd4cd11wuh3duw1f6sferf2vbg5|[https://qamate.baidu-int.com/lazymind/#/case/index](https://qamate.baidu-int.com/lazymind/#/case/index)![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aac524e75d424233a9ac00b9d8724a57&docGuid=RBIl16sMLoTvPq "")|
|story_list|是|List[string]|脑图用例生成参数，需求卡片列表|self.parameter.icafe_ids|使用testone平台参数"卡片列表"来赋值self.parameter.icafe_ids|
|generate_task_key|否|str|生成策略|||



### 生成查看
**前往 Qamate 用例平台，查看具体的生成用例.使用操作步骤，请参看下面的文档**

[脑图用例生成工具](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/LWyELLqriZ/1d556876ea9f47?t=mention&mt=doc&dt=doc)

# 2、服务型工具接入指南
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=24389a323a84442994d7f3394eea4990&docGuid=RBIl16sMLoTvPq "")
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"QAMate-脑图用例工具-服务型tool"，点击选择

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b5151378129d405e9cfe9812d14d33f4&docGuid=RBIl16sMLoTvPq "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4d9304a78843436eb616e42a79fe356d&docGuid=RBIl16sMLoTvPq "")
## 2.2、修改参数
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=68d9d518f1744b16957886ef6ca5fc5f&docGuid=RBIl16sMLoTvPq "")
