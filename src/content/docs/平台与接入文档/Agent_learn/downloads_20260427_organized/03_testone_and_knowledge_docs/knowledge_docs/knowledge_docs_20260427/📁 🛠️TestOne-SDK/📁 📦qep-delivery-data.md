---
title: "1、说明"
description: "📦qep-delivery-data"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🛠️TestOne-SDK\\📁 📦qep-delivery-data.md"
---
📦qep-delivery-data

# 1、说明
## **1.1、python版本**
* python3
* python2（目前不支持，未来也没有可能支持。放弃吧，别挣扎了，往前看）

## **1.2、外部直接依赖**
以下为qep-delivery-data直接依赖的其他第三方lib库(不包括系统自带的)，pip install qep-delivery-data的时候会自动安装

* requests

## **1.3、权限相关**
> 开放的SDK内部，其中部分数据获取依赖相关平台的权限控制，由于SDK的代码为全公开的，因此SDK不会以任何形式提供相关的账号密码，均需要调用方自行从相关平台获取。
目前涉及到的账号密码/token的类以及对应平台如下

|需要权限的类|涉及平台|token或账号密码申请方式|
|-|-|-|
|TestOneUtils|TestOne|浏览器直接打开：[https://testone.baidu-int.com](https://testone.baidu-int.com)![](/personal-site-mvp/img/doc-placeholder.svg "")|
|CodeUtils|TestOne|1、浏览器直接打开：[https://testone.baidu-int.com](https://testone.baidu-int.com)![](/personal-site-mvp/img/doc-placeholder.svg "")2、将自己的username  token 给到 zhangshiduo, 添加访问权限|
||||
|ICafeUtils|iCafe|自行从icafe平台获取文档： [获取虚拟密码](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/NbX2gitgSF/4cc48b299a6846?t=mention&mt=doc&dt=doc)|
|KirinUtils|Kirin|[https://kirin.baidu-int.com/#/index](https://kirin.baidu-int.com/#/index)![](/personal-site-mvp/img/doc-placeholder.svg "")|
|QaMateUtils|QaMate|# 当前业务的ID和Token，获取方式参考： [OPENAPI](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/ZV7hybZXiu/zCcTzK2McQYBnI?t=mention&mt=doc&dt=doc)|
|QadcUtils|QADC|[http://qadc.baidu-int.com/?#/market](http://qadc.baidu-int.com/?#/market)![](/personal-site-mvp/img/doc-placeholder.svg "")|

## **1.4、日志相关**
> SDK有打印调用参数返回日志，为了避免和使用方定义的日志格式，级别等不一致，没有默认开启。如需打印日志，需要自己的代码中完成对logging的初始化。或者使用SDK提供的默认初始化方式。开启方式如下：
> from qep_delivery_data import init_log  # 引入初始化函数
> ...
> init_log()  # 在自己的代码适当位置，初始化日志
> ...
## **1.5、安装(仅限公司内网)**
### **方式1 (推荐)**
pip3 install --index-url [http://pip.baidu.com/root/baidu/+simple/](http://pip.baidu.com/root/baidu/+simple/)  --trusted-host pip.baidu.com -U qep-delivery-data

![](/personal-site-mvp/img/doc-placeholder.svg "")
### **方式2**
> 说明：当前sdk仅发布在公司内部pip源，需要配置公司内部pip源。
> 配置方式（如已配置，忽略）：
> vim ~/.pip/pip.conf  (pip.conf文件内容 )
> 
> [global]
> timeout = 60
> index = [http://pip.baidu-int.com/search/](http://pip.baidu-int.com/search/)
> index-url = [http://pip.baidu-int.com/simple/](http://pip.baidu-int.com/simple/)
> trusted-host = pip.baidu-int.com
> [list]
> format = columns
pip3 install -U qep-delivery-data

![](/personal-site-mvp/img/doc-placeholder.svg "")
## **1.6、删除**
 pip3 uninstall qep-delivery-data

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 2、使用指南
注：本SDK只是将各种常用的各平台各渠道数据获取能力进行汇总，旨在方便大家快速知道目前都有哪些公共的开放数据，以及减少重复开发的能力。如果封装的数据格式或者数据能力无法满足述求，可像平台提需求完善，或者自行开发即可。

## 2.1、需求相关
### 2.1.1、根据ICafe卡片批量获取需求详情
功能：

获取业务线在TestOne平台的需求的基本信息。

版本：

>=0.0.1

需要权限：

是

输入：

需求卡片iCafe列表

输出：

TestOne平台任务列表

```
from qep_delivery_data import TestoneUtils


def sample():
    # 获取任务列表
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN")
    tasks = utils.get_tasks_by_icafe_id_list(["routine00-16668", "routine00-16536"])
    for task in tasks:
        print(task)


if __name__ == '__main__':
    sample()
```
### 2.1.2、根据业务版本查询需求
功能：

版本下所有需求卡片

版本：

>=0.0.2

需要权限：

是

输入：

业务线，版本

输出：

TestOne平台任务列表

```
from qep_delivery_data import TestoneUtils


def sample():
    # 获取任务列表
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN")
    tasks = utils.get_tasks_by_version(222, '搜索', '13.47.0')
    for task in tasks:
        print(task)


if __name__ == '__main__':
    sample()
```


### 2.1.3、需求关联Bug查询
功能：

获取需求关联的Bug列表

版本：

>=0.0.1

需要权限：

是

输入：

需求卡片iCafe列表

输出：

需求卡片关联的Bug列表

```
from qep_delivery_data import TestoneUtils


def sample():
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN") 
    bugs = utils.get_bugs_by_task_icafe_id_list(["routine00-16668", "routine00-16536"])
    for bug in bugs:
        print(bug)


if __name__ == '__main__':
    sample()
```
### 2.1.4、按照特定条件筛选Bug
功能：

按照特定条件筛选Bug

版本：

>=0.0.5

需要权限：

是

输入：

筛选条件，Bug的各种特征字段，字段过多详见TestoneUtils.get_bugs()函数参数注释

输出：

符合要求的Bug列表

```
from qep_delivery_data import TestoneUtils


def sample():
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN") 
    bugs = utils.get_bugs(creator='qep-testone@baidu.com', createAfter='2023-10-01 00:00:00', createBefore='2023-12-01 00:00:00')
    for bug in bugs:
        print(bug)


if __name__ == '__main__':
    sample()
```


## 2.2、版本相关
### 2.2.1、获取业务版本列表
功能：

获取业务版本列表

版本：

>=0.0.2

需要权限：

是

输入：

业务线

输出：

版本列表

```
from qep_delivery_data import TestoneUtils


def sample():
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN") 
    versions = utils.get_versions(222, '基础')
    for version in versions:
        print(version)


if __name__ == '__main__':
    sample()
```


## 2.3、需求Case签章信息
### 2.3.1、需求Case签章信息
功能：

获取需求Case签章基本信息

版本：

>=0.2.6

需要权限：

是  

输入：

需求卡片iCafeId 

输出：

需求卡片关联的Case签章信息

```
from qep_delivery_data import QaMateCaseUtils 


def sample():
    module_id = 0 # 模块ID
    token = "" # 模块token
    # 当前业务的ID和Token，获取方式参考： https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/LWyELLqriZ/zCcTzK2McQYBnI
    utils = QaMateCaseUtils(module_id, token)
    result = utils.get_case_sign_detail_by_icafe_id("haokanapp-all-36659")
    print(result)

```
## 2.4、排期日历相关
### 2.4.1、获取业务线全部QA的工作排期
功能：

获取业务线全部QA排期

版本：

>=0.0.2

需要权限：

是

输入：

业务线  时间

输出：

QA排期列表

```
from qep_delivery_data import TestoneUtils


def sample():
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN")
    result = utils.get_qa_calendars_by_dept(222, "搜索", '2023-11-20 00:00:00', '2023-12-01 23:59:59')
    for item in result:
        print(item)


if __name__ == '__main__':
    sample()
```
### 2.4.2、获取业务线QA个人的工作排期
功能：

获取业务QA个人排期

版本：

>=0.0.2

需要权限：

是

输入：

用户名  时间

输出：

排期列表

```
from qep_delivery_data import TestoneUtils


def sample():
    utils = TestoneUtils("XXXX", "XXXX")
    result = utils.get_calendars_by_qa('zhangyifeng03', '2023-11-20 00:00:00', '2023-12-01 23:59:59')
    for item in result:
        print(item)


if __name__ == '__main__':
    sample()
```
## 2.5、业务线相关
### 2.5.1、获取testone全部业务线
功能：

获取TestOne全部业务线

版本：

>=0.0.1

需要权限：

是

输入：

无

输出：

业务线列表

```
from qep_delivery_data import TestoneUtils


def sample():
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN")
    result = utils.get_all_departments()
    for item in result:
        print(item)


if __name__ == '__main__':
    sample()
```


### 2.5.2、获取业务线下QA列表
功能：

获取TestOne业务线下属QA

版本：

>=0.0.1

需要权限：

是

输入：

业务线信息

输出：

QA列表

```
from qep_delivery_data import TestoneUtils


def sample():
    utils = TestoneUtils("YOUR_NAME", "YOUR_TOKEN")
    
    result = utils.get_qa_by_department(222, [])
    for item in result:
        print(item)

    result = utils.get_qa_by_department(222, ["基础", "内核"])
    for item in result:
        print(item)

    result = utils.get_qa_by_department(222, ["基础"], 0)
    for item in result:
        print(item)


if __name__ == '__main__':
    sample()
```


## 2.6、变更代码
目前仅支持Android  iOS 其他方向接入请咨询 [@王冬冬](https://ku.baidu-int.com?t=mention&mt=contact&id=92960170-2eb4-11ef-82bb-6b3597131cd8)[@张士铎](https://ku.baidu-int.com?t=mention&mt=contact&id=9625b7e0-2eb4-11ef-82bb-6b3597131cd8)

### 2.6.1、根据iCafe卡片（需求/Bug）获取变更代码文件&类&函数
功能：

获取需求变更代码文件信息

版本：

>=0.0.1

需要权限：

是 (拿到自己在TestOne的username token 后，找[@张士铎](https://ku.baidu-int.com?t=mention&mt=contact&id=a6b3d8d0-2eb4-11ef-82bb-6b3597131cd8)添加授权)

输入：

需求卡片iCafeId 

输出：

需求卡片关联的代码文件信息

```
from qep_delivery_data import CodeUtils


def sample():
    utils = CodeUtils("YOUR_NAME", "YOUR_TOKEN")
    changed_files = utils.get_diff_code_by_icafeid("FEEDADS-2307")  # 获取变更代码文件信息
    for file in changed_files:
        print(file)


if __name__ == '__main__':
    sample()
```
### 2.6.2、获取版本代码变更文件
功能：

获取版本变更代码文件信息

版本：

>=0.0.1

需要权限：

是 (拿到自己在TestOne的username token 后，找[@张士铎](https://ku.baidu-int.com?t=mention&mt=contact&id=yyE8IhIl)添加授权)

输入：

APP  端  版本  代码库列表

输出：

版本变更的代码文件

```
from qep_delivery_data import CodeUtils
from qep_delivery_data import AppIdEnum
from qep_delivery_data import ClientEnum


def sample():
    utils = CodeUtils("YOUR_NAME", "YOUR_TOKEN")
    changed_files = utils.get_integration_test_diff_code(AppIdEnum.BAIDU_APP, ClientEnum.ANDROID, "13.46.0", [])
    for file in changed_files:
        print(file)

if __name__ == '__main__':
    sample()
```


## 2.7、代码函数调用关系
功能：

获取函数的上下游调用关系

版本：

>=0.0.1

需要权限：

是 (拿到自己在TestOne的username token 后，找[@张士铎](https://ku.baidu-int.com?t=mention&mt=contact&id=a6b3d8d0-2eb4-11ef-82bb-6b3597131cd8)添加授权)

输入：

APP  端  版本   分支  函数列表

输出：

版本变更的代码文件

```
from qep_delivery_data import AppIdEnum
from qep_delivery_data import ClientEnum
from qep_delivery_data import CodeUtils


def sample():
    utils = CodeUtils("YOUR_NAME", "YOUR_TOKEN")
    result = utils.get_func_chain_info(
        AppIdEnum.BAIDU_APP, ClientEnum.ANDROID, "13.45.0",
        [
            "com.baidu.searchbox.feed.net::FeedOutbackRequester::refreshWithForm(String,Map,Map,int,int,ResponseCallback)",
            "com.baidu.searchbox.encrypt.decrypt::EncryptDecryptUtils::getIv()",
            "com.baidu.searchbox.account.config::IAccountConfig_Impl::<init>()",
            "com.baidu.searchbox.account.config::IAccountConfig_Impl_Factory::get()"
        ],
        "master"
    )
    for item in result:
        print(item)


if __name__ == '__main__':
    sample()

```


## 2.8、iCafe常用API集合
* 详见 [ICafe相关](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/fgTU24fcONs15d?t=mention&mt=doc&dt=doc)

## 2.9、麒麟平台API集合
### 2.9.1、调用麒麟策略
功能：

调用麒麟策略

版本：

>=0.0.1

需要权限：

是

输入：

策略ID，策略参数

输出：

策略执行结果

```
from qep_delivery_data import KirinUtils


def sample():
    utils = KirinUtils("guyouda", "xxxxxxxxxxxxx")
    param = {
        "strategy_type": 2,
        "story_list": [
            {"id": 1355, "deptId": 26674, "subDirection": "工作台", "taskType": 1, "taskLabel": "",
             "client": "Android",
             "version": "2.1.0", "title": "线上回归-qtest-不拦截", "status": "开发中", "icafeId": "youtrack-326",
             "icafeCardType": "Story", "icafeParentCard": "", "icafePlan": "TestOne/2.1.0", "groupId": 0,
             "rd": "高立哲", "rdValue": "gaolizhe", "devDays": 0.0, "submitTestTime": None, "onlineTime": None,
             "qa": "高立哲", "qaValue": "gaolizhe", "testDays": 0.0, "testStartTime": None, "testFinishTime": None,
             "caseIds": "", "testType": 0, "testReason": "", "createdTime": "2023-11-17 19:35:27",
             "creator": "testOne",
             "updateTime": "2023-11-20 11:36:59", "operator": "testOne", "assignTaskId": 0, "assignReason": "",
             "assignDetail": "", "secondmentFormId": "", "extInfo": "", "isDeleted": 0, "dimensionStatus": "待测试",
             "showcaseStatus": "", "showcaseRemark": ""}]
    }
    result = utils.call_kirin_api(213493, json.dumps(param, ensure_ascii=False))
    print(result)

```
### 2.9.2、麒麟策略执行结果
功能：

获取麒麟策略执行结果

版本：

>=0.0.1

需要权限：

是

输入：

任务ID

输出：

策略执行结果

```
import json
import unittest

from qep_delivery_data import KirinUtils
from qep_delivery_data import init_log

def sample():
    # 初始化日志
    init_log()
    
    utils = KirinUtils("YOUR_NAME", "YOUR_TOKEN")
 
    # 测试获取任务结果
    task_result = utils.get_task_result(5598101447)
    print(task_result)
    strategy_response = json.loads(task_result.response)
    print(strategy_response)

```
## 2.10 QADC平台API集合
### 2.10.1、根据SQL查询数据结果
功能：

根据SQL查询数据结果

版本：

>=0.0.1

需要权限：

是

输入：

表  SQL

输出：

数据结果

```
import json
import unittest

from qep_delivery_data import QadcUtils


def sample():
    utils = QadcUtils("guyouda", "---------")

    result = utils.get_result_from_qadc(
        "card_code_commit", "SELECT * FROM card_code_commit_2023 ORDER BY @timestamp DESC", 1, 100)
    self.assertEqual(result.code, 0)
    self.assertGreater(len(result.data), 0)
    for item in result.data:
        print(item)
```
### 2.10.2、写入数据
功能：

写入数据

版本：

>=0.2.18

需要权限：

是

输入：

List[Dict]

输出：

写入结果

```
import json
import unittest

from qep_delivery_data import QadcUtils


def sample():
    utils = QadcUtils("QADC_USER", "QADC_TOKEN")
    result = utils.insert_data_to_qadc("http_api_format", [{"product": "IM", "method": "GET",
                                                            "uri_path": "/api/v1/user/info", "id": 1}])
    self.assertEqual(result.code, 0)
    self.assertGreater(result.data, 1)
```
### 2.10.3、更新数据
功能：

更新数据

版本：

>=0.2.18

需要权限：

是

输入：

List[Dict]

输出：

更新结果

```
import json
import unittest

from qep_delivery_data import QadcUtils


def sample():
    result = utils.update_data_to_qadc("http_api_format", "id", [{"product": "IM", "method": "POST", "id": 1,
                                                                      "uri_path": "/api/v1/user/info"}])
    self.assertEqual(result.code, 0)
    self.assertGreater(result.data, 1)
```
## 2.11 如流消息API集合
* 详见 [如流相关](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/kUxvGcs1KPqoht?t=mention&mt=doc&dt=doc)

## 2.12 iCode代码CR统计
### 2.12.1 获取代码提交行数统计
功能：

获取用户指定时间段内的代码提交行信息统计

详见：[提交行数（工程师维度、代码库维度、产品维度和部门维度、团队维度）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/kYHClhRTZr/s79OoPxYCwyL9N?t=mention&mt=doc&dt=doc)

版本：

>=0.0.8

需要权限：

是

输入：

邮箱列表，时间范围

输出：

代码提交行统计结果，数据格式参考 [提交行数（工程师维度、代码库维度、产品维度和部门维度、团队维度）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/kYHClhRTZr/s79OoPxYCwyL9N?t=mention&mt=doc&dt=doc)

```
from qep_delivery_data import ICodeCRUtils

def sample():
    utils = ICodeCRUtils({hetu_app_id}, {hetu_secret_key})
    result = utils.get_engineer_commit_lines("2024-01-01", "2024-02-01", ["guyouda@baidu.com", "shixue01@baidu.com"])
    
    
if __name__ == '__main__':
    sample()
```
### 2.12.2 获取CR次数统计
功能：

获取用户指定时间段内的CR次数天数统计

详见：[提评审统计数据(可按工程师与代码库查询)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/kYHClhRTZr/aTyZg9t1KiTWM0?t=mention&mt=doc&dt=doc)

版本：

>=0.0.8

需要权限：

是

输入：

邮箱列表，时间范围

输出：

代码提交行统计结果，数据格式参考 [提评审统计数据(可按工程师与代码库查询)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/kYHClhRTZr/aTyZg9t1KiTWM0?t=mention&mt=doc&dt=doc)

```
from qep_delivery_data import ICodeCRUtils

def sample():
    utils = ICodeCRUtils({hetu_app_id}, {hetu_secret_key})
    result = utils.get_engineer_code_review_info("2024-01-01", "2024-02-01", ["guyouda@baidu.com", "shixue01@baidu.com"])
    
    
if __name__ == '__main__':
    sample()
```
### 2.12.2 获取CR评论信息统计
功能：

获取用户指定时间段内的CR评论信息统计

详见：[评论统计数据(可按工程师与代码库查询)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/kYHClhRTZr/QuR0ZWVRf8Ajl6?t=mention&mt=doc&dt=doc)

版本：

>=0.0.8

需要权限：

是

输入：

邮箱列表，时间范围

输出：

代码提交行统计结果，数据格式参考 [评论统计数据(可按工程师与代码库查询)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/_SKPgSwp2G/kYHClhRTZr/QuR0ZWVRf8Ajl6?t=mention&mt=doc&dt=doc)

```
from qep_delivery_data import ICodeCRUtils

def sample():
    utils = ICodeCRUtils({hetu_app_id}, {hetu_secret_key})
    result = utils.get_engineer_code_review_comment_info("2024-01-01", "2024-02-01", ["guyouda@baidu.com", "shixue01@baidu.com"])
    
    
if __name__ == '__main__':
    sample()
```


![](/personal-site-mvp/img/doc-placeholder.svg "")

