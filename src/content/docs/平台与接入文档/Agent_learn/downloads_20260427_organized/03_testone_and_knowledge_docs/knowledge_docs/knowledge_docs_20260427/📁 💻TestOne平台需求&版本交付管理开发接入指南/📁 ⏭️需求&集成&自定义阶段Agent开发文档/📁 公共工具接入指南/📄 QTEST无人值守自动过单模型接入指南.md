---
title: "!/usr/bin/python3"
description: "QTEST无人值守自动过单模型接入指南"
date: "2026-04-27"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 💻TestOne平台需求&版本交付管理开发接入指南\\📁 ⏭️需求&集成&自定义阶段Agent开发文档\\📁 公共工具接入指南\\📄 QTEST无人值守自动过单模型接入指南.md"
---
QTEST无人值守自动过单模型接入指南

目前只适配了百家号的，其他的不支持



在tools下新增工具    qtest_unattended_tool.py

```
# !/usr/bin/python3

# -*- coding: utf-8 -*-

"""
@author: GuYouda
@date:   2024/5/23
@desc:   QTEST提测平台无人值守模型工具
"""
import json
import logging
import traceback
from typing import Dict, List
from typing import Optional

import requests

from qep_delivery_component import ComponentOperateConfig
from qep_delivery_component import RichTextComponent
from qep_delivery_data import KirinUtils
from qep_delivery_tools import BaseTool
from qep_delivery_tools import Parameter
from qep_delivery_tools import ToolResult


class QtestUnattendedModelTool(BaseTool):
    """
    服务端流水线无人值守自动准出过单策略迁移，仅支持从流水线跳转到QTEST提测的需求
    """

    def __init__(self, testone_username: str, testone_token: str, kirin_username: str, kirin_token: str,
                 custom_kirin_tool_id: int = 213380, rule_strategy: str = "",
                 threshold: float = None):
        """
        初始化
        :param testone_username: TestOne平台用户名
        :param testone_token: Testone平台用户对应的API访问Token
        :param kirin_username: 麒麟用户名
        :param kirin_token: 麒麟Token
        :param rule_strategy: 业务自己的策略规则
        :param custom_kirin_tool_id: 业务自定义的麒麟策略ID，如果没有，设置为213880即可
        :param threshold: 阈值
        """
        super().__init__("7116c507072def69d6faa89b70396090")
        self.kirin_strategy_id = 213380
        self.testone_username = testone_username
        self.testone_token = testone_token
        self.kirin_username = kirin_username
        self.kirin_token = kirin_token

        # 业务自定义参数
        self.custom_kirin_tool_id = custom_kirin_tool_id
        self.rule_strategy = rule_strategy
        self.threshold = threshold

        if (not self.testone_username or not self.testone_token
                or not self.kirin_username or not self.kirin_token):
            logging.error("参数异常，请确认参数是否合法")
            raise Exception("参数异常，请确认参数是否合法")

    def prepare_model_parameter(self, parameter: Parameter) -> List[Dict]:
        """
        准备请求参数
        :return: 注意：针对非QTEST提测的需求，返回None
        """
        model_param = []

        # 如果多张卡片合并提测的，根据每张卡片获取到的结果都是一样的
        url = "https://testone.baidu-int.com/api/testCard/getSubmitTestInfoByIcafeId?icafeId={}".format(
            parameter.icafe_ids[0]
        )
        headers = {
            "Content-Type": "application/json",
            "username": self.testone_username,
            "token": self.testone_token,
        }

        try:
            # 调用TestOne接口，获取卡片的提测信息
            logging.info("get submit test info from testone, url:[%s], parameter:[%s]", url, model_param)
            res = requests.get(url, headers=headers)
            logging.info("response:[%s]", res.text)

            content = json.loads(res.content)
            if content["code"] != 0 or content["data"] is None:
                logging.error("未获取到卡片[{}]的提测信息，请确认卡片是否已提测", parameter.icafe_ids)
                return model_param

            if content["data"]["testId"] == 0:
                logging.info("当前卡片[{}]不是从QTEST提测，不支持调用服务端质量度模型", parameter.icafe_ids)
                return model_param

            # 调用QTEST接口，获取提测单详细信息
            qtest_id = content["data"]["testId"]
            url = "http://10.169.46.156:8888/newtice/api/record/getTiceDataByIds"
            logging.info("get submit test info from qtest, url:[%s], qtest_id:[%s]", url, qtest_id)
            res = requests.post(url, data=json.dumps([qtest_id], ensure_ascii=False).encode("utf-8"),
                                headers={"Content-Type": "application/json"})
            logging.info("response:[%s]", res.text)

            content = json.loads(res.content)
            if content["errNo"] != 0 or content["data"] is None or len(content["data"]) == 0 \
                    or len(content["data"][0]["module_info"]) == 0:
                logging.error("获取提测单详情异常: {}", qtest_id)
                return model_param

            # 判断如果不是流水线提测的，返回None
            for code in content["data"][0]["module_info"]:
                if not code.get("fromAgile", False):
                    continue
                model_param.append(
                    {
                        "AGILE_ENV": {
                            "AGILE_PIPELINE_BUILD_ID": content["data"][0]["pipeline_build_id"],
                            "AGILE_MODULE_NAME": code.get("codeModule", ""),
                            "AGILE_COMPILE_BRANCH": code.get("modulebranch", ""),
                            "AGILE_REVISION": code.get("revision", "")
                        },
                        "strategy_info": {
                            "kirin_tool_id": self.custom_kirin_tool_id,
                            "rule_strategy": self.rule_strategy,
                            "threshold": self.threshold
                        }
                    }
                )
        except Exception as e:
            logging.error(e)
            logging.error(traceback.format_exc())

        return model_param

    def execute(self, parameter: Parameter) -> Optional[ToolResult]:
        """
        执行
        """
        strategy_param = self.prepare_model_parameter(parameter)
        if len(strategy_param) == 0:
            return None

        # 依次分析所有的提测模块，全部可以无人值守准出，才算
        high_risk = False
        risk_summary = "无人值守模型判断可以准出"
        result_list = []

        for item in strategy_param:
            kirin_task_id = 0
            try:
                kirin_response = KirinUtils(self.kirin_username, self.kirin_token).call_kirin_api(
                    self.kirin_strategy_id, json.dumps(item, ensure_ascii=False))
                kirin_task_id = kirin_response.taskId
                strategy_response = json.loads(kirin_response.response)

                # execute: 低风险, 可自动准出
                # skip: 高风险, 不可自动准出
                execute = strategy_response.get("result", "") == "execute"
                if strategy_response.get("reason"):
                    reason = strategy_response.get("reason", "")
                else:
                    reason = "无人值守模型判断可以准出" if execute else "无人值守模型判断不可以准出"
            except Exception as e:
                logging.error(e)
                execute = True
                reason = "无人值守模型调用异常，默认不可以准出"

            if not execute:
                high_risk = True
                risk_summary = "无人值守模型判断不可以准出"

            result_list.append(
                "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
                    "<a href='https://kirin.baidu-int.com/#/task-info?toolId=&taskId={}' target='_blank'>{}</a>".format(
                        kirin_task_id, kirin_task_id),
                    "<font color='green'>准出通过</font>" if execute else "<font color='red'>准出不通过</font>"
                    , reason, json.dumps(item["AGILE_ENV"], ensure_ascii=False)
                )
            )

        if high_risk:
            head = "<font color='red'>无人值守模型判断准出不通过</font>, 详情如下:</br>"
        else:
            head = "<font color='green'>无人值守模型判断准出通过</font>, 详情如下:</br>"

        detail = """
        {}
        <table border="1" cellspacing="0" bordercolor="gray">
            <thead>
                <tr>
                    <th>麒麟任务ID</th>
                    <th>准出是否通过</th>
                    <th>原因</th>
                    <th>代码信息</th>
                </tr>
            </thead>
            <tbody>
                {}
            </tbody>
        </table>
        """.format(head, "".join(result_list))

        # 构建前端组件
        component_info = RichTextComponent(ComponentOperateConfig(expand=True, enable_refresh=False), detail)

        # 返回工具执行结果
        return ToolResult(self.tool_id, component_info, high_risk=high_risk, risk_summary=risk_summary)


```


修改测试阶段Agent代码

```
...
from tools.qtest_unattended_tool import QtestUnattendedModelTool
...


def execute(self):
    all_tools = [
      ...
      QtestUnattendedModelTool(TESTONE_USERNAME, TESTONE_TOKEN, KIRIN_USERNAME, KIRIN_TOKEN)
      ...
    ]
    
```

