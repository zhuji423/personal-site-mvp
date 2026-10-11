---
title: "v0.4.0（2026-02-27）"
description: "Release log"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🛠️TestOne-SDK\\📁 📦qep-delivery-data\\📄 Release log.md"
---
Release log

# v0.4.0（2026-02-27）
* ⚠️不兼容升级
    *  send_text_msg_to_group升级
    * send_custom_msg_to_group升级

* 新增
    * send_text_msg_to_user
    * send_md_msg_to_user
    * send_md_msg_to_group


# v0.3.3（2026-01-27）
* ICafeUtils新增获取空间类型列表
* ICafeUtils新增获取空间某个类型下的状态列表

# v0.3.0（2025-12-08）
* 删除过期作废的 LazyMindCaseUtils
* 删除过期作废的 NewCaseUtils

# v0.2.18（2025-11-24）
* QadcUtils新增支持写入数据  详见2.10.2[📦qep-delivery-data](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI#anchor-8a7b1fc0-c8eb-11f0-9c76-8505eaab4397?t=mention&mt=doc&dt=doc)
* QadcUtils新增支持更新数据 详见2.10.3 [📦qep-delivery-data](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI#anchor-d8f4d880-c8eb-11f0-9c76-8505eaab4397?t=mention&mt=doc&dt=doc)



# v0.2.15（2025-11-19）
* 支持发送工作卡到群聊， 详见 2.11.3 [📦qep-delivery-data](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI#anchor-54dd7220-c55b-11f0-96e4-9dfdf04b7d2a?t=mention&mt=doc&dt=doc)
* 支持发送工作卡到单聊， 详见2.11.4  [📦qep-delivery-data](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI#anchor-5fed5310-c55b-11f0-96e4-9dfdf04b7d2a?t=mention&mt=doc&dt=doc)
* 利用TestOne服务号给用户发消息  详见2.11.5 [📦qep-delivery-data](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/SNsADSWPchsxiI#anchor-02ae8420-c55c-11f0-ba16-7dd101151a04?t=mention&mt=doc&dt=doc)

# v0.2.14 (2025-10-17)
* **提交hash**: e1e95f1
* **主要改动**:
    * 支持生成打开如流对话框超链接
    * 修改文件: `infoflow_utils.py`（新增23行）


# v0.2.13 (2025-09-11)
* **提交hash**: bda83ca
* **主要改动**:
    * SDK支持文件上传功能
    * 富文本组件改用URL模式，减少大文本场景数据库存储压力
    * 修改文件: `testone_utils.py`（新增80行）


# v0.2.12 (2025-09-02)
* **提交hash**: 0fb79fd
* **提交信息**: zhongtaiQA-2060 侧边栏 dep_delivery_data sdk icafe增加上线发布信息
* **主要改动**: 仅版本号升级（实质改动在v0.2.12g）

# v0.2.12g (2025-09-02)
* **提交hash**: 40c1d5e
* **主要改动**:
    * iCafe增加上线发布信息支持
    * 修改文件: `__init__.py`（版本号临时标记为灰度版本"g"）


# v0.2.11 (2025-08-14)
* **提交hash**: f47a5e5
* **主要改动**:
    * 去除data包中iCafe相关工具类的请求URL和参数日志打印（安全增强）
    * 避免麒麟任务日志无权限管控场景下敏感信息泄露
    * 修改文件: `icafe_utils.py`（21行改动）


# v0.2.10 (2025-05-14)
* **提交hash**: 1125aa6
* **主要改动**:
    * SDK支持群机器人推送Markdown类型的消息
    * 新增文件: `data/infoflow.py`（23行）
    * 修改文件: `infoflow_utils.py`


# v0.2.9 (2025-03-20)
* **提交hash**: 6c869da
* **主要改动**:
    * 数据SDK新增鸿蒙类型和其他APP以及插件的支持
    * 修改文件: `data/enums.py`（14行改动）


# v0.2.8 (2024-12-03)
* **提交hash**: 763f84d
* **主要改动**:
    * 风险分析改为异步服务，避免超时异常
    * 修改文件: `kirin_utils.py`（新增27行）


# v0.2.7 (2024-10-23)
* **提交hash**: ce5dcda
* **主要改动**:
    * 支持批量查询卡片的研发数据链信息
    * 修改文件: `icafe_utils.py`（新增25行）


# v0.2.6 (2024-10-17)
* **提交hash**: 3df32e1
* **主要改动**:
    * 适配QaMate 3.0根据卡片获取Case签章API
    * 新增文件: `qamate_utils.py`（45行）
    * 修改文件: `case_utils.py`


# v0.2.5 (2024-09-28)
* **提交hash**: 796572e
* **主要改动**:
    * Go覆盖率不基于base_revision区分
    * 前端展示覆盖率获取时间
    * 修改文件: `data/cov_table.py`（15行改动）


# v0.2.4 (2024-09-12)
* **提交hash**: e5d0929
* **主要改动**:
    * SDK升级，支持用户指定表单项的宽度
    * 修改文件: `data/testone_obj.py`（33行改动）
    * 修改文件: `testone_utils.py`（71行改动）


# v0.2.3 (2024-09-04)
* **提交hash**: 9cb2014
* **主要改动**:
    * 数据SDK升级——获取卡片的变更代码支持根据注解&正则表达式过滤
    * 修改文件: `code_utils.py`（7行改动）


# v0.2.2 (2024-08-21)
* **提交hash**: a0ad260
* **主要改动**:
    * 获取工具执行历史记录，需要默认过滤调试结果
    * SDK调用NewCaseUtils新增警告提示，方便后续下线
    * 修改文件: `data/bug.py`（8行）、`case_utils.py`（2行）


# v0.2.1 (2024-08-19)
* **提交hash**: 7a09e3a
* **主要改动**:
    * PHP/GO/JS覆盖率展示-表格版增加story覆盖率和分支覆盖率的筛选字段
    * **注意**: 此版本主要改动在component SDK，data SDK仅版本号对齐


# v0.2.0 (2024-07-26) 
* **提交hash**: 549842f
* **主要改动**:
    * SDK升级，支持业务自定义参数解析
    * 数据SDK支持用户自定义参数控制是否查询关联卡片和子卡片
    * 修改文件: `data/icafe.py`（4行）、`icafe_utils.py`（36行大幅改动）


# v0.1.9 (2024-07-25)
* **提交hash**: 371c3e9
* **主要改动**:
    * JS语言的覆盖率，增加icafeId参数
    * 修改文件: `cov_table_utils.py`（3行）


# v0.1.8 (2024-07-19)
* **提交hash**: 4c4160e
* **主要改动**:
    * 数据SDK支持新建iCafe卡片的时候绑定父卡片、关联、评论卡片
    * 修改文件: `icafe_utils.py`（新增21行）


# v0.1.7 (2024-07-11)
* **提交hash**: 71f8437
* **主要改动**:
    * SDK日志升级，避免直接打印输出用户的token信息（安全增强）
    * SDK升级新增表单提交数据参数规范定义
    * 修改文件: `code_utils.py`、`kirin_utils.py`、`testone_utils.py`（共4处改动）


# v0.1.6 (2024-07-08)
* **提交hash**: 3e4fa86
* **主要改动**:
    * 代码覆盖率展示工具-Php/Go/JS等，优化异常边界条件，修复判空条件
    * 修改文件: `cov_table_utils.py`（2行）


# v0.1.5 (2024-07-08)
* **提交hash**: 2cf660a
* **主要改动**:
    * 代码覆盖率展示工具优化异常边界条件
    * 修改文件: `cov_table_utils.py`（2行）


# v0.1.4 (2024-07-07)
* **提交hash**: b1691e3
* **主要改动**:
    * 代码覆盖率展示工具优化
    * 仅版本号升级


# v0.1.3 (2024-07-04)
* **提交hash**: 38ce89a
* **主要改动**:
    * covTableTool的报告地址改为富文本渲染
    * 仅版本号升级（主要改动在component SDK）


# v0.1.2 (2024-06-27)
* **提交hash**: 5f8a3cf
* **主要改动**:
    * 服务端代码变更信息获取公共工具-表格展示
    * 仅版本号升级（主要改动在component SDK）


# v0.1.1 (2024-06-27)
* **提交hash**: 0b193e2
* **主要改动**:
    * 服务端代码变更信息获取公共工具-表格展示
    * 仅版本号升级（主要改动在component SDK）


# v0.1.0 (2024-05-30) 
* **提交hash**: 61ef905
* **主要改动**:
    * 优化业务IQL表达式错误场景的SDK异常抛出，方便用户理解
    * 修改文件: `icafe_utils.py`（5行改动）


# v0.0.9 (2024-05-24)
* **提交hash**: 5d67831
* **主要改动**:
    * 数据sdk发布0.0.9: UT/SA问题列表
    * 仅版本号升级（主要改动在tools SDK）


# v0.0.8 (2024-03-18)
* **提交hash**: a577a4d
* **主要改动**:
    * 工具SDK支持如流发送图片消息
    * DIFF函数接口支持获取函数对应的AB实验信息
    * 修改文件: `data/code.py`（2行）、`data/infoflow.py`（新增23行）、`icafe_utils.py`（2行）


# 2024-01-18 v0.0.7
支持批量获取ICafe卡片状态变化历史，返回类型： List[ICafeCardStatusHistory]

```
result = ICafeUtils("ICAFE用户名", "ICAFE虚拟密码").get_card_status_history("youtrack", [465,466])
for card in result:
    print(item.sequence)
    for history in item.histories:
        print(history.operator)
        print(history.operationTime)
        print(history.targetStatusId)
        print(history.targetStatusName)
```
支持批量获取ICafe卡片其他字段变化历史, 返回类型：List[ICafeCardChangeRecord]

```
result = ICafeUtils("ICAFE用户名", "ICAFE虚拟密码").get_card_status_history("youtrack", [465,466])
for card in result:
    print(item.sequence)
    for history in item.histories:
        print(history.operator)
        print(history.operationTime)
        print(history.operationType)
        print(history.diffDescription)
```
# 2023-12-25  v0.0.6
 修复根据卡片获取变更代码(CodeUtils.get_diff_code_by_icafeid)返回结果错误

> * 函数变更类型未正确赋值，全部是 None
> * 返回的数据结构不对，定义的是 List[FuncDiffInfo]  实际返回的是 List[Dict]
> 
使用方需要注意：

* 函数变更类型修复，无影响
* 获取变更函数的取值逻辑需要升级, 升级方式参考

```
result = CodeUtils("guyouda", "---").get_diff_code_by_icafeid("FEEDADS-2307")
# 升级前
for item in result:
    for func in item.funcList:
        print(func["name"])
        print(func["updateType"])
        print(func["icafeIdList"])

# 升级后
for item in result:
    for func in item.funcList:
        print(func.name)
        print(func.updateType)
        print(func.icafeIdList)
```


# 2023-12-22  v0.0.5
支持如流群消息

* 普通文本消息
* @特定用户消息
* @全员消息

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


# 2023-12-15 v0.0.4
支持部分常见icafe操作

* 新建卡片
* 修改卡
* 评论卡片
* 获取卡片评论

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")

