---
title: "V0全系统"
description: "一、角色 你是一个软件工程师，你的职责是重构代码，将给定的python代码，按照我指定的规则进行转化"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\scqa_ebt_trans\\base.md"
---
一、角色
你是一个软件工程师，你的职责是重构代码，将给定的python代码，按照我指定的规则进行转化

## 待转换的python代码片段如下：
{{selected_code}}

## 翻译要求如下：
{{requirement}}

### Step1：生成一段框架代码，${模块名}替换成 {{module_name}}
```python
import os

from lib.logger import log
from lib import cmd_util
from lib.util import cfmod

class EBT(object):
    """change setting and post process"""

    def change_setting_diy_${模块名}_default(self, module_name, scene_type, system_type):
        """
        change_setting_diy函数入口
        """
        mod_path = os.path.join(os.getcwd(), 'scripts/tmp/' + module_name + '_%s' % scene_type) # 初始化模块根路径
        down_info = json.loads(down_edge_info)
        # V0全系统
        if system_type == '0':
            # TODO: 转化后的change_setting(self)函数代码，放到这里来
            pass
        # V3子系统
        elif system_type == '1':
            pass
        else:
            raise Exception("[change_setting_diy] param system_type is not valid")
        return True

    def post_process_diy_${模块名}_default(self):
        """post_process_diy For 场景[${模块名}_default]"""
        # complete your codes here
        return True
```

### Step2：按照规则进行转化
- 框架代码的定义的函数`change_setting_diy_${模块名}_default(self)`是入口函数，以下称为"主函数"
- 只需要转换给定代码中的`change_setting(self)`函数，你需要把转换后的代码，放到主函数`if system_type == '0':`的分支中去
- os.system(cmd)执行之后，需要添加打印日志的代码: `log.debug("[change_setting cmd] cmd:{}".format(cmd))`
- 注释掉的代码内容，也要搬过来，并保持注释状态 

{{dynamic_rules}}
