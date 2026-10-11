---
title: "一、页面结构"
description: "Amis平台使用总结（质量度风险评估报告）"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Amis\\Amis平台使用总结（质量度风险评估报告）.md"
---
Amis平台使用总结（质量度风险评估报告）

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间


# 一、页面结构
## 1. 页面布局结构
![](../../assets/g_Oq3XkIyrHhv0/image_001.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_002.bin "")
## 2. 页面逻辑结构
页面初始化会调用**页面初始化**接口，返回数据进行整个页面的渲染。

点击评估结果中准入风险结论确认按钮，调用**准入标注确认**接口。

点击评估结果中准入风险结论误报按钮，会弹出表单填写误报原因，提交后调用**准入标注误报**接口。

重置按钮显示，并禁用标注功能，点击重置将清除标注结果，并调用**准入标注重置**接口。

分级与准入类似。

点击确认提交并触发流水线，将调用**流水线触发**接口，对标注进行核验，只有准入和分级均标注时才会根据url的pipelineBuildId和stageConfId进行流水线触发（[流水线触发代码](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1210247360)）并返回标注结果给流水线。

![](../../assets/g_Oq3XkIyrHhv0/image_003.bin "")
## 3. 质量度风险评估报告后端接口
[质量度风险评估报告API](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1198290745)

# 二、API接口部分
## 1. 页面初始化initApi（）接口
page 可以配置 initApi 从远端拉取数据，当配置了 initApi 且返回数据后，当前 page 渲染器，以及所有孩子渲染器都能取到这个这个变量。

这里使用 initApi 在一开始加载页面渲染需要的所有数据。

initApi的使用如下图，参数在后面会详细介绍。

![](../../assets/g_Oq3XkIyrHhv0/image_004.bin "")
返回数据：

![](../../assets/g_Oq3XkIyrHhv0/image_005.bin "")
返回数据中 result 对应**评估结果**模块数据，project_status 对应**项目情况**模块，test_process 对应**测试过程风险**模块，code_risk对应**代码风险**模块

返回结果中的数据使用方法如下：

![](../../assets/g_Oq3XkIyrHhv0/image_006.bin "")
## 2. Api Mock
在后端接口没写完之前，可以先用假接口调好前端页面。

![](../../assets/g_Oq3XkIyrHhv0/image_007.bin "")
/api/init 中填入上节的返回数据，再将initApi（）接口改写为 "initApi": "http://fakedomain.com/api/init" 页面就会根据假数据进行渲染。

这样可以在没写后端接口的时候先调好页面结构。

通过api mock可以定好前后端沟通的接口格式，方便前后端解耦。

## 3. 数据映射
### 3.1 数据初始化处理
这里后端是打包成服务发布在kirin上，对接口格式有一定要求。以初始化接口发请求为例：

![](../../assets/g_Oq3XkIyrHhv0/image_008.bin "")
开发完后端接口后，在posterman测试接口结果通过。在Amis添加数据映射，包装为符合kirin的接口格式

![](../../assets/g_Oq3XkIyrHhv0/image_009.bin "")
或者在代码中直接设置：

![](../../assets/g_Oq3XkIyrHhv0/image_004.bin "")
${story_id} 指连接中对应的值，如 [http://autolu.amis.baidu.com/autolu_report?story_id=2389_1319](http://autolu.amis.baidu.com/autolu_report?story_id=2389_1319)

从kirin返回的值需要进行适配，具体过程查看第4节。

### 3.2 字段携带全局变量
点击评估结果中准入风险结论确认按钮，调用**准入标注确认**接口。请求参数与返回格式如下。

![](../../assets/g_Oq3XkIyrHhv0/image_011.bin "")
is_exemption_real 字段为标注结果，这里点击确认，携带的值应与准入评估结果一致。

![](../../assets/g_Oq3XkIyrHhv0/image_012.bin "")
### 3.3 字段携带表单内容
点击评估结果中准入风险结论误报按钮，会弹出表单填写误报原因，提交后调用**准入标注误报**接口。

"parameter": "{\"story_id\":\"${story_id}\",\"req_type\":\"3\",\"is_exemption_real\":\"${result.recheck1}\",\"comments\":\"${comments}\"}"

控件中name指定字段名

![](../../assets/g_Oq3XkIyrHhv0/image_013.bin "")
## 4. Api返回适配器
kirin返回的数据格式：

![](../../assets/g_Oq3XkIyrHhv0/image_014.bin "")
amis需要的数据格式是response部分

在系统配置/api相关中修改

![](../../assets/g_Oq3XkIyrHhv0/image_015.bin "")
# 三、前端界面部分
## 1. 结果卡片选择展示处理
因为无法在初始化环节动态修改plane组件的样式，这里的处理方法是写两种样式允许准入与不允许准入，通过 visibleOn 控制只显示其中一个。

比如： "visibleOn": "data.result.predict_y1==1"

![](../../assets/g_Oq3XkIyrHhv0/image_016.bin "")
渲染的时候只会显示其中一个。

## 2. map映射
![](../../assets/g_Oq3XkIyrHhv0/image_017.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_018.bin "")
## 3. 根据数值范围自动更新样式
![](../../assets/g_Oq3XkIyrHhv0/image_019.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_020.bin "")
"tpl": "<% var num = data.cov_merge %> <% if(num>=60){%> <span class='text-success'><%-num %></span><% } %> <% if(num<60){%><span class='text-danger'><%-num %></span> <% }%>"

需要自己写JavaScript语句进行处理。

## 4. 字符串换行缩进格式转换
![](../../assets/g_Oq3XkIyrHhv0/image_021.bin "")
detail = '调用函数:\n[\n\t{}\n],\n 被调函数:\n[\n\t{}\n]' .format(',\n\t'.join(indegree['list']), ',\n\t'.join(outdegree['list']))
detail = detail.replace('\n', '</br>').replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;')

## 5. 详情页链接可达
为详情页的文件名添加字段url

![](../../assets/g_Oq3XkIyrHhv0/image_022.bin "")
## 6. 弹窗内html解析
![](../../assets/g_Oq3XkIyrHhv0/image_023.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_024.bin "")
使用 "tpl": "${job_skip_detail|raw}" 进行html解析

![](../../assets/g_Oq3XkIyrHhv0/image_025.bin "")
## 7. 不同长度字符串对齐
![](../../assets/g_Oq3XkIyrHhv0/image_026.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_027.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_028.bin "")
# 四、踩坑日记
## 1. kirin无法连接Amis
请求kirin的数据parameter要强制替换成json字符串格式，否则kirin会处理失败

![](../../assets/g_Oq3XkIyrHhv0/image_004.bin "")
## 2. 反向标注
标注接口请求格式与返回数据如下：

![](../../assets/g_Oq3XkIyrHhv0/image_030.bin "")
点击评估结果中分级风险结论误报按钮，会弹出表单填写误报原因，提交后调用分级标注误报接口。

is_exemption_real 的值与分级结果是异或关系，amis接口不支持自己写逻辑，这里在页面初始化的时候，给传来的result加了字段recheck，相当于将异或逻辑放到后端。

"parameter": "{\"story_id\":\"${story_id}\",\"req_type\":\"3\",\"is_exemption_real\":\"${result.recheck1}\",\"comments\":\"${comments}\"}"

在传参中

## 3. 标注模块交互
因为amis没法修改局部变量，只能通过后端接口传来辅助参数，再通过辅助参数利用 visibleOn、disabledOn、hiddenOn 来进行交互。

![](../../assets/g_Oq3XkIyrHhv0/image_031.bin "")
点击评估结果中分级风险结论确认按钮，调用分级**标注确认**接口。

点击评估结果中分级风险结论误报按钮，会弹出表单填写误报原因，提交后调用分级**标注误报**接口。

![](../../assets/g_Oq3XkIyrHhv0/image_032.bin "")
重置按钮显示，并禁用标注功能，显示标注结果。点击重置将清除标注结果，并调用分级**标注重置**接口。

![](../../assets/g_Oq3XkIyrHhv0/image_033.bin "")
分级标注接口：

![](../../assets/g_Oq3XkIyrHhv0/image_034.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_035.bin "")
![](../../assets/g_Oq3XkIyrHhv0/image_036.bin "")
分级标注逻辑：

|按钮|初始值|visibleOn|disabledOn|点击效果|标注结果文本显示|
|-|-|-|-|-|-|
|确认|tag2=0||tag2!=0|tag2=1|"人工标注分级结果：可自主测试"|
|误报|tag2=0||tag2!=0|tag2=2|"人工标注分级结果：可自主测试</br>误报原因：qwe"|
|重置|tag2=0|tag2!=0||tag2=0|""|

按钮组：



```
"actions": [
        {
            "type": "button",
            "disabledOn": "tag2!=0",
            "reload": "cao2?tag2=${tag2}&show_msg2=${show_msg2}&tag2_msg=${tag2_msg}",
            "label": "确认",
            "actionType": "ajax",
            "level": "primary",
            "api": {
                "method": "post",
                "url": "http://kirin.baidu-int.com/api/tool/210607",
                "data": {
                    "&": "$$",
                    "name": "zhoujie19",
                    "token": "",
                    "parameter": "{\"story_id\":\"${story_id}\",\"req_type\":\"4\",\"is_exemption_real\":\"$result.predict_y2\"}"
                },
                "dataType": "json"
            },
            "className": "font-thin",
            "size": "sm",
            "icon": "glyphicon glyphicon-ok"
        },
        {
            "type": "button",
            "disabledOn": "tag2!=0",
            "label": "误报",
            "actionType": "drawer",
            "drawer": {
                "title": "标记误报",
                "closeOnEsc": true,
                "actions": [
                    {
                        "label": "提交误报",
                        "type": "submit",
                        "actionType": "ajax",
                        "level": "primary",
                        "api": {
                            "method": "post",
                            "url": "http://kirin.baidu-int.com/api/tool/210607",
                            "data": {
                                "&": "$$",
                                "name": "zhoujie19",
                                "token": "",
                                "parameter": "{\"story_id\":\"${story_id}\",\"req_type\":\"5\",\"is_exemption_real\":\"${remark}\",\"comments\":\"${comments}\"}"
                            },
                            "dataType": "json"
                        },
                        "reload": "cao2?tag2=${tag2}&show_msg2=${show_msg2}&tag2_msg=${tag2_msg}"
                    }
                ],
                "body": [
                    {
                        "type": "form",
                        "mode": "normal",
                        "controls": [
                            {
                                "type": "button-group",
                                "required": true,
                                "name": "remark",
                                "label": "分级风险标注",
                                "description": "请选择分级风险~",
                                "options": [
                                    {
                                        "label": "无人值守",
                                        "value": "2",
                                        "disabledOn": "data.result.predict_y2==2"
                                    },
                                    {
                                        "label": "可自主测试",
                                        "value": "1",
                                        "disabledOn": "data.result.predict_y2==1"
                                    },
                                    {
                                        "label": "不可自主测试",
                                        "value": "0",
                                        "disabledOn": "data.result.predict_y2==0"
                                    }
                                ]
                            },
                            {
                                "type": "text",
                                "name": "comments",
                                "required": true,
                                "placeholder": "请输入误报原因",
                                "label": "误报原因"
                            }
                        ]
                    }
                ],
                "size": "md",
                "type": "drawer"
            },
            "className": "font-thin",
            "size": "sm",
            "icon": "glyphicon glyphicon-remove"
        },
        {
            "type": "button",
            "tooltip": "取消标注结果",
            "reload": "cao2?tag2=${tag2}&show_msg2=${show_msg2}&tag2_msg=${tag2_msg}",
            "label": "重置",
            "actionType": "ajax",
            "api": {
                "method": "post",
                "url": "http://kirin.baidu-int.com/api/tool/210607",
                "data": {
                    "&": "$$",
                    "name": "zhoujie19",
                    "token": "",
                    "parameter": "{\"story_id\":\"${story_id}\",\"req_type\":\"8\"}"
                },
                "dataType": "json"
            },
            "className": "font-thin",
            "size": "sm",
            "visibleOn": "tag2!=0"
        }
    ]
```
# 五、报告落地
[http://amis.baidu.com/group/zjtest/test?story_id=2413_1360&pipelineBuildId=38305970&stageConfId=1402708](http://amis.baidu.com/group/zjtest/test?story_id=2413_1360&pipelineBuildId=38305970&stageConfId=1402708)



相关链接：

[AMIS帮助文档](http://amis.baidu.com/docs/examples/pages/simple)

[Amis部分案例分析](http://amis.baidu.com/group/demo/crud-single?page=1)


