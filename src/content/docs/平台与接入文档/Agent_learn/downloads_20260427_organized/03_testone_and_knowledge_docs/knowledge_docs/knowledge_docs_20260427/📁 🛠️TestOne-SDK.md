---
title: "依赖关系"
description: "🛠️TestOne-SDK"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🛠️TestOne-SDK.md"
---
🛠️TestOne-SDK

注意：

* 必须在requirements.txt规范管理依赖以及版本号，避免由于安装最新版本导致的不兼容问题
* 必须参考或者直接使用 build.sh 脚本将平台提供的SDK和Agent代码服务 打包到一起
* 不要找麒麟同学帮忙安装以下SDK，也不要直接使用麒麟平台公共提供的以下SDK，避免由于其他用户升级或者降级公共依赖版本导致自己业务Agent的异常

# 依赖关系
[流程图]
# 版本兼容性要求
> 注意
> * 升级qep-delivery-tools版本的时候，请确认对应的 qep-delivery-data qep-delivery-component是否兼容
> * 建议使用平台下方给出的版本组合，避免导致不必要的问题
> * 升级前做好本地环境测试验证、麒麟测试环境测试验证
> 
|qep-delivery-tools|qep-delivery-component|qep-delivery-data|备注|
|-|-|-|-|
|0.6.0|0.5.0|0.2.9||
|0.5.4|0.4.0|0.2.9|qep-delivery-component支持markdown组件支持饼图组件支持折线图组件qep-delivery-tools新增AIQA支持|
|0.5.0|0.3.0|0.2.9|qep-delivery-tools 从0.5.0以下的版本升级到 0.5.0及以上版本的时候，请参考以下文档进行处理，否则会存在Agent执行失败的问题[Release log](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/m0rgI-sR2fr10n#anchor-754326a0-2046-11f0-a6b1-9b5397714676?t=mention&mt=doc&dt=doc)|
|0.4.15|0.2.18|0.2.8||
|0.4.12|0.2.16|0.2.8|qep-delivery-component表单输入组件支持多行文本输入自定义提测报告自持用户自行控制各个公共字段是否必填；自定义提测报告新增默认用户邮箱合法性校验|
|0.4.12|0.2.14|0.2.8|qep-delivery-component表格组件支持用户设定部分列支持前端排序; 表单组件支持定制整体填写说明表单组件支持用户定制表单提交按钮名字；风险组件支持用户指定链接打开方式qep-delivery-tools升级支持解析表单接口debug参数优化QaMate Case生成任务ID生成方式质量度模型工具异常支持重试；支持用户指定异常场景默认风险高低qep-delivery-componentKirinUtils新增获取麒麟异步返回结果函数|
|0.4.6|0.2.12|0.2.7|表格组件支持下钻，打开子表格详见：[表格组件](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/Ai5UXxByKYMxVz?t=mention&mt=doc&dt=doc)|
|0.4.6|0.2.11|0.2.7|qep-delivery-component支持开发者指定内嵌页面的高度优化使用体验![](/personal-site-mvp/img/doc-placeholder.svg "")qep-delivery-tools支持自定义阶段表单组件调起麒麟策略支持定义阶段的Agent支持服务型Tool业务配置参数|
|0.4.0|0.2.10|0.2.7|qep-delivery-component支持表格筛选支持表单隐藏部分字段qep-delivery-data支持批量获取研发数据链 ICafeUtils.batch_get_code_dev_info适配qamate 3.0  QaMateCaseUtils.get_case_sign_detail_by_icafe_id|
|0.4.0|0.2.8|0.2.4|qep-delivery-component优化表单组件样式，支持自定义表单项宽度qep-delivery-data新增获取提测报告的接口封装  详见 TestOneUtils.get_submit_test_report|
|0.4.0|0.2.7|0.2.3|qep-delivery-tools新增服务端QTEST质量度模型公共工具，详见[服务端-质量度模型工具1.0接入指南（当前版本已不再维护，请接入2.0）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/dzi1oGoZzVaUZb?source=137?t=mention&mt=doc&dt=doc)qep-delivery-component同一个工具支持执行结果支持多个组件组合展示，详见[组合组件](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/_BH1klc7lopPG4?source=137?t=mention&mt=doc&dt=doc)支持业务自定义提测报告组件（后端暂未上线，暂勿使用） [提测报告组件](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/iLNz7Ogp8_kvxs?source=137?t=mention&mt=doc&dt=doc)表格组件升级, qep-delivery-component==0.2.7，详见：[表格组件](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/Ai5UXxByKYMxVz?t=mention&mt=doc&dt=doc)顶部默认去除右上角 菜单栏（使用频率过低，大片空白影响美观）支持指定单元格类型文本富文本超链 （支持多个）独立页面打开当前页面浮层打开qep-delivery-data根据卡片获取变更代码 支持根据注解 正则表达式过滤，详见SDK CodeUtils.get_diff_code_by_icafeid|
|0.3.8|0.2.4|0.2.2|qep-delivery-dataNewCaseUtils废弃，请使用LazyMindCaseUtils代替。请及时替换，否则后续版本删除后代码运行会报错IDE会有方法废弃提示运行代码会有警告日志![](/personal-site-mvp/img/doc-placeholder.svg "")|
|0.3.5|0.2.4|0.2.0|qep-delivery-component  详见[⏭️需求&集成&自定义阶段Agent开发文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/NzwrklmOjkeBeQ#anchor-d7570c20-2340-11ef-ab70-adaaacc283ba?t=mention&mt=doc&dt=doc)表格组件支持指定宽度表格内容支持指定类型文本富文本链接新页面打开当前页面弹窗打开 （影响体验不支持当前页面直接打开）【注意】废弃表格组件的rich_text参数  使用参数 *type=TableColumnTypeEnum.RICH_TEXT 替代 （继续使用*rich_text=True 前端富文本渲染不生效，代码执行会有警告不会失败，后续版本移除此参数后继续使用会报错 *）*错误使用方案：![](/personal-site-mvp/img/doc-placeholder.svg "")正确使用方案：![](/personal-site-mvp/img/doc-placeholder.svg "")|
|0.3.5|0.2.3|0.2.0|qep-delivery-tools支持使用TestOne服务号给用户发送消息 详见：[使用TestOne服务号给用户发消息](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/Q-SJ0hDSkZwR1G?t=mention&mt=doc&dt=doc)qep-delivery-component表单组件新增以下几种类型  详见：[表单组件](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/J4ml-aakRSAq-n?t=mention&mt=doc&dt=doc)CodeFormDetailDateFormDetailDatetimeFormDetailUserSelectFormDetail表格输入组件支持指定每一行的宽度|
|0.3.3|0.2.1|0.2.0||
|0.3.2|0.2.1|0.1.9||
|0.3.1|0.2.1|0.1.8||
|0.3.0|0.2.1|0.1.8||
|0.2.9|0.2.1|0.1.7||
|0.2.8|0.2.1|0.1.7||
|0.2.7|0.2.1|0.1.6||
|0.2.6|0.2.0|0.1.6||
|0.2.0|0.2.0|0.1.2||
|||||

# SDK升级流程建议
平台SDK升级过程，会做到兼容历史版本。但是可能会存在部分测试不充分的Bug，或者业务Agent依赖的多个SDK版本组合不合法导致等因素，升级版本号后，可能会存在部分兼容问题，请做好自测。

* 执行本地单测，确保所有用例均可以执行通过
* 升级SDK（修改requirements.txt，安装新版本）
* 再次执行单测，确保所有用例均可以执行通过



## 怎么测试验证
**直接执行所有的用例，查看是否有异常失败**

![](/personal-site-mvp/img/doc-placeholder.svg "")
**我从不写测试用例怎么办？**

* 部署到麒麟测试环境，在TestOne页面，在线调试，选择测试环境，看效果确认 

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


## 怎么升级版本
```
qep-delivery-data==xxx
qep-delivery-component==xxx
qep-delivery-tools==xxx
```
```
pip3 install -r requirements.txt -U --index-url http://pip.baidu.com/root/baidu/+simple/ --trusted-host pip.baidu.com  --no-cache-dir
```
```
# 为了避免SDK升级不兼容导致的线上问题，直接将指定版本的组件SDK打包到当前目录和策略代码部署在一起
component_sdk_version=$(cat requirements.txt | grep '^qep-delivery-component' | awk -F '^qep-delivery-component*==*' '{print $2}')
pip3 install --no-deps --target=output/agent --no-cache-dir -i http://pip.baidu-int.com/simple/ --trusted-host pip.baidu-int.com qep-delivery-component==${component_sdk_version}

data_sdk_version=$(cat requirements.txt | grep '^qep-delivery-data' | awk -F '^qep-delivery-data*==*' '{print $2}')
pip3 install --no-deps --target=output/agent --no-cache-dir -i http://pip.baidu-int.com/simple/ --trusted-host pip.baidu-int.com qep-delivery-data==${data_sdk_version}

tools_sdk_version=$(cat requirements.txt | grep '^qep-delivery-tools' | awk -F '^qep-delivery-tools*==*' '{print $2}')
pip3 install --no-deps --target=output/agent --no-cache-dir -i http://pip.baidu-int.com/simple/ --trusted-host pip.baidu-int.com qep-delivery-tools==${tools_sdk_version}

rm -rf output/agent/qep_delivery*.dist-info
```
# 
## 
## 
