---
title: "1、函数型工具接入指南"
description: "QaMate接口用例生成工具使用指南"
date: "2026-04-28"
category: "项目架构文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📁 公共工具接入指南\\📄 QaMate接口用例生成工具使用指南.md"
---
QaMate接口用例生成工具使用指南

工具负责人：[@陈蕾](https://ku.baidu-int.com?t=mention&mt=contact&id=6aa4e8d0-2346-11ef-ab70-adaaacc283ba)

# 1、函数型工具接入指南
### 安装公共工具sdk
1. 需先配置百度pip源，可参考[3.1-python-sdk](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/J71vLy9tCR/sVfJHD86pLJ4pE#anchor-7ab65880-9a04-11ec-9861-8367451d60a1?t=mention&mt=doc&dt=doc)
2. pip install -U qep_delivery_tools==0.4.12



### 调用方式
在agent.py中调用QaMate接口用例生成工具sdk

from qep_delivery_tools import QaMateCaseGenerateTool

tool = QaMateCaseGenerateTool(notify_user, itp_groupid, itp_suite_id, itp_run_params, callback_addr, case_status, run_mode, module_ai_config_list, ai_ext_info, yapi_api_ids)

tool_result = tool.execute(self.parameter)

```
import logging

from qep_delivery_tools import BaseAgent
from qep_delivery_tools import QaMateCaseGenerateTool
from qep_delivery_tools import AiExtInfo
from qep_delivery_tools import ModuleAiConfig
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
        notify_user = "zhangsan"  # 通知人
        itp_groupid = 3  # 用例集合id，选填
        itp_suite_id = 15  # 用例文件id，选填
        itp_run_params = "{\"host\": \"www.baidu.com\",\"zookeeper\": \"www.baidu.com\",\"registerPath\": \"www.baidu.com\",\"config\": \"{\\\"key\\\":\\\"value\\\"}\", \"ip\": \"\", \"port\": \"\"}"  # 环境运行信息，选填
        callback_addr = "http://example.baidu-int.com/callback"  # 回调地址，只支持post，选填
        case_status = 0  # 生成后case的状态，选填。取值范围: 0: 启用(默认); 1: 不启用
        run_mode = "branch"  # 生成模式，选填。取值范围: task: 每次任务都是全新生成(默认); branch: 按照分支粒度生成，同模块同分支的用例生成到一个目录，且进行生成去重; testsone: 按照testone提测单id维度生成，同testone提测单的用例生成到一个目录，且进行生成去重
        
        # 模块信息，选填
        ai_ext_info = AiExtInfo("status取0", strategy_ids="1")  # 生成诉求信息，选填
        yapi_api_ids = [3, 6]  # 模版id列表，选填
        module_ai_config = ModuleAiConfig("baidu/kpd-edu-server/edu-web-go", ai_ext_info, yapi_api_ids)
        module_ai_config_list = [module_ai_config]
  
        # tool初始化，配置module_ai_config时，可以在module_ai_config中配置ai_ext_info和yapi_api_ids
        tool = QaMateCaseGenerateTool(notify_user, itp_groupid, itp_suite_id, itp_run_params, callback_addr, case_status, run_mode, module_ai_config_list)
        # tool初始化，不配置module_ai_config时，可以直接配置yapi_api_ids和ai_ext_info
        # tool = QaMateCaseGenerateTool(notify_user, itp_groupid, itp_suite_id, itp_run_params, callback_addr, ai_ext_info=ai_ext_info, yapi_api_ids=yapi_api_ids)
        
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
参数描述

|参数名|参数类型|参数说明|参数案例|备注|
|-|-|-|-|-|
|notify_user|string|通知人|||
|itp_groupid|integer|用例集合id|||
|itp_suite_id|integer|用例文件id|||
|itp_run_params|string|环境运行信息|{\"host\": \"www.baidu.com\",\"zookeeper\": \"www.baidu.com\",\"registerPath\": \"www.baidu.com\",\"config\": \"{\\\"key\\\":\\\"value\\\"}\", \"ip\": \"\", \"port\": \"\"}|jsonstringhost对应计划配置中的hostzookeeper对应计划配置中的zookeeperregisterPath对应计划配置中的registerPathconfig对应需要替换的全局变量ip和port对应需要测试的环境ip和port|
|callback_addr|str|回调地址，只支持post|"http://example.baidu-int.com/callback"||
|case_status|int|生成后case的状态|0|取值范围:     0: 启用(默认);     1: 不启用|
|run_mode|str|生成模式|"branch"|取值范围:     task: 每次任务都是全新生成(默认);     branch: 按照分支粒度生成，同模块同分支的用例生成到一个目录，且进行生成去重;     testsone: 按照testone提测单id维度生成，同testone提测单的用例生成到一个目录，且进行生成去重|
|module_ai_config_list|list|模块信息|[        {            "aiExtInfo": {                "normalAssertDesc": "status取0",//普通断言描述                "exceptionAssertDesc":"",//异常断言描述                "paramDesc": "",//参数描述                "sampleStrategyIds": "1"//生成策略            },            "module": "baidu/kpd-edu-server/edu-web-go",//模块            "yapiApiIds": []//itp对应的模版id        }    ]|针对模块具体的参数诉求和对应的接口文档模版id|
|ai_ext_info|object|生成诉求信息|{                "normalAssertDesc": "status取0",//普通断言描述                "exceptionAssertDesc":"",//异常断言描述                "paramDesc": "",//参数描述                "sampleStrategyIds": "1"//生成策略            }|如果对模块未配置module_ai_config_list，将使用此信息覆盖|
|yapi_api_ids|array[int]|模版id list|[integer,integer]|如果对模块未配置module_ai_config_list，将使用此信息覆盖|
|case_gen_type|int|用例生成类型设置0:默认筛选+新接口生成,1:筛选生成但生成case失败不影响plan接口,2:筛选+生成且影响plan结果,3:仅筛选,4:仅流量生成,5:筛选+流量生成,6:筛选+流量+新接口生成,7:流量+新接口生成|0||



### 执行效果
#### 执行成功
* 有接口影响

![](/personal-site-mvp/img/doc-placeholder.svg "")
* 无接口影响

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 执行失败
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 页面内部功能
当用户无当前页面权限，页面将会弹窗跳转到试用产品线首页

#### 生成详情
点击生成详情将跳转展示任务进度

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 重新生成
点击重新生成，将会重新执行tool，生成新的用例，覆盖上次结果

#### 运行case
点击运行case，将会执行环境搭建，环境搭建完毕将会进行测试任务，生成相关的计划并运行。如果在itp_run_params定义了ip和port将会跳过环境搭建过程。

#### 测试报告
点击测试报告将会页面切换至计划运行详情页面，无计划运行点击跳转有提示跳转失败。

# 2、服务型工具接入指南
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.1、选择工具
在配置中心的某个测试阶段增加服务型tool，搜索"QAMate-接口用例工具-服务型tool"，点击选择

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.2、配置参数
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 2.3、修改参数
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
