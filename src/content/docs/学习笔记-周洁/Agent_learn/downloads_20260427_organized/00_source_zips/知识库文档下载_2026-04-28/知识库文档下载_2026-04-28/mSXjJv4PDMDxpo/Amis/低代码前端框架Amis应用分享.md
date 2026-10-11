---
title: "低代码前端框架Amis应用分享"
description: "低代码前端框架Amis应用分享"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Amis\\低代码前端框架Amis应用分享.md"
---
低代码前端框架Amis应用分享

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间

## 
## 一、背景
### 1.1、目的
1. 了解Amis能帮助我们做什么，适合什么场景
2. 能够快速上手搭建一个后台管理系统

任务管理页面:

![](../../assets/SRHABbyoIDK6GE/image_001.bin "")
任务创建页面:

![](../../assets/SRHABbyoIDK6GE/image_002.bin "")
### 1.2、Amis应用场景
通过简单的json配置生成页面，有大量组件可供使用，支持简单接口交互，支持可视化界面编辑，不需要学习各种前端框架和工具，减少页面开发工作量，提升效率。amis不适用于有非常复杂交互逻辑或对页面样式有较高自定制要求。

可用于进行数据可视化、后台信息管理、数据标注、测试报告。

[http://amis.baidu.com/group/learn-amis/index/newTask?embed=true](http://amis.baidu.com/group/learn-amis/index/newTask)

### 1.3、Amis与 ShowX、Sugar的区别
 ShowX偏向于进行数据可视化，而amis主要是数据操作。

 ShowX可视化组件丰富表单组件较少，而amis表单组件丰富可视化组件较少。

 ShowX支持API + SQL + EXCEL直接连接数据源进行数据录入，而amis以API接入数据（大部分情况需要自己编写后端）。

|平台|Amis|ShowX|
|-|-|-|
|定位|数据操作|数据可视化|
|表单组件|丰富|较少|
|可视化组件|较少|丰富|
|数据录入|API|API+SQL+ EXCEL|
|接口交互|支持|不支持|

如何选用：当只需要连接数据源展示数据，没有接口交互功能的要求，选择使用showx进行可视化。如果涉及到表单填写、接口交互的数据操作，适合使用amis。

Sugar 与 ShowX定位类似，区别在于Sugar有大屏展示，界面布局更高级, 图表更多。不足点是细节功能上会少一点, 比如批量添加权限, 报警, 表内条件查询, 常量替换 等功能，sugar主要做商业版，对于和百度内部业务耦合的功能优先级会低一些。 

sugar：

![](../../assets/SRHABbyoIDK6GE/image_003.bin "")
showX：

![](../../assets/SRHABbyoIDK6GE/image_004.bin "")
相关链接：[ShowX](http://showx.baidu.com/docs)、[Sugar](https://sugar.baidu-int.com/docs/ProductDescription)

### 1.4、Amis原理：配置与组件
amis 的渲染过程是将 json 转成对应的 React 组件。先通过 json 的 type 找到对应的 Component，然后把其他属性作为 props 传递过去完成渲染。（可以不用深究，感兴趣可以去[官网](https://baidu.github.io/amis/zh-CN/docs/extend/internal)看看，有详细介绍）

## 二、快速创建一个简单demo
### 2.1、创建群组
[http://amis.baidu.com/groups/my](http://amis.baidu.com/groups/my)

创建群组

![](../../assets/SRHABbyoIDK6GE/image_005.bin "")
填写信息

![](../../assets/SRHABbyoIDK6GE/image_006.bin "")
### 2.2、新建页面
进入群组

![](../../assets/SRHABbyoIDK6GE/image_007.bin "")
开始创建页面

![](../../assets/SRHABbyoIDK6GE/image_008.bin "")
填写页面基本信息，schema和其他设置不做修改

![](../../assets/SRHABbyoIDK6GE/image_009.bin "")
确认后刷新页面

![](../../assets/SRHABbyoIDK6GE/image_010.bin "")
点击编辑进入可视化编辑界面

### 2.3、可视化编辑界面
![](../../assets/SRHABbyoIDK6GE/image_011.bin "")
左侧包括大纲（组件树结构）、组件、代码，代码中的json决定了页面的布局组成与接口交互方式；

中间为当前的页面渲染情况，用于观察页面效果，像按钮触发弹窗等就需要使用最上方的预览按钮进行预览查看；

右侧包括常规（组件配置）、接口（api交互）、外观（组件样式，类似css）、其他（联动时使用）。

### 2.4、添加组件
点击页面中的加号，添加一个简单的增删查改组件，保持默认值，点击确定

![](../../assets/SRHABbyoIDK6GE/image_012.bin "")
可以看到代码区和页面都有所改变

![](../../assets/SRHABbyoIDK6GE/image_013.bin "")
点击右上角保存并退出编辑界面。

### 2.5、接口mock功能
在后端接口没写完之前，可以先用mock接口调好前端页面。

在管理中心-》系统配置-》API相关 中打开mock功能

![](../../assets/SRHABbyoIDK6GE/image_014.bin "")
在管理中心-》API Mock 中新建mock数据

**mock数据**

```
{
  "status": 0,
  "msg": "ok",
  "data": [
    {
      "task_name": "V1.4.1",
      "version": "1.4.0",
      "status": "1",
      "usr": "zhangsan",
      "time": "2021-05-31 18:22:22"
    },
    {
      "task_name": "V2.1.4",
      "version": "2.1.0",
      "status": "0",
      "usr": "lisi",
      "time": "2021-06-01 19:01:01"
    }
  ]
}
```


![](../../assets/SRHABbyoIDK6GE/image_015.bin "")
![](../../assets/SRHABbyoIDK6GE/image_016.bin "")
### 2.6、页面展示
重新进入任务管理的可视化编辑界面，点击crud组件，在代码中修改数据获取api为http://fake.com/api/getTaskInfo，修改columns中的字段信息(对应mock数据名)

**json配置**

```
{
    "type": "page",
    "title": "任务管理",
    "remark": "任务管理界面",
    "body": [
        {
            "type": "crud",
            "api": "http://fake.com/api/getTaskInfo",
            "columns": [
                {
                    "name": "task_name",
                    "label": "任务名称"
                },
                {
                    "name": "version",
                    "label": "版本号"
                },
                {
                    "label": "状态",
                    "name": "status"
                },
                {
                    "label": "操作人",
                    "name": "usr"
                },
                {
                    "label": "记录时间",
                    "name": "time"
                }
            ],
            "bulkActions": [
            ],
            "itemActions": [
            ]
        }
    ]
}
```
![](../../assets/SRHABbyoIDK6GE/image_017.bin "")
保存后退出，一个简单的demo就搭建好了。实际应用中的接口api需要自己开发。

![](../../assets/SRHABbyoIDK6GE/image_018.bin "")
如果想隐藏左边栏，在地址后加入'embed=true'，如 [http://amis.baidu.com/group/learn-amis/index/newTask?embed=true](http://amis.baidu.com/group/learn-amis/index/newTask?embed=true) 

## 三、应用示例
结构：

* 前端：Amis，
* 后端：写好接口服务后打包到kirin上
* 数据库：qadc

### 3.1、后台管理系统CRUD
#### 3.1.1、数据表与后端接口api
##### （1）数据表
[amis_test](http://qadc-offline.bcc-szwg.baidu.com:8092/#/market?firstLevel=业务数据&secondLevel=amis_test)

![](../../assets/SRHABbyoIDK6GE/image_019.bin "")
##### （2）接口API
调用url：[http://kirin.baidu-int.com/api/tool/211446](http://kirin.baidu-int.com/api/tool/211446)

|req_type|功能|调用示例|参数|
|-|-|-|-|
|0|新建任务接口|[http://kirin.baidu-int.com/#/task-info?tid=&id=963451743](http://kirin.baidu-int.com/#/task-info?tid=&id=963451743)|太长不看|
|1|查询所有任务接口|[http://kirin.baidu-int.com/#/task-info?tid=&id=963453524](http://kirin.baidu-int.com/#/task-info?tid=&id=963453524)|{"usr":"zhoujie19","req_type":"1"}|
|2|删除任务接口|[http://kirin.baidu-int.com/#/task-info?tid=&id=963455062](http://kirin.baidu-int.com/#/task-info?tid=&id=963455062)|{"usr":"zhoujie19","req_type":"2","new_version":"3.2.8"}|
|3|表单初始化接口|[http://kirin.baidu-int.com/#/task-info?tid=&id=963456529](http://kirin.baidu-int.com/#/task-info?tid=&id=963456529)|{"usr":"zhoujie19","req_type":"3","new_version":"4.2.1"}|

##### （3）全局关键字
在系统配置-》宏定义中添加全局关键字，设置调用地址KIRIN_URL，NAME和TOKEN

![](../../assets/SRHABbyoIDK6GE/image_020.bin "")
##### （4）全局接口适配器
后端接口部署在kirin，需对返回的数据（如下所示）进行解析："response"为真正需要的接口返回。

**kirin接口返回格式**

```
{
    "message": "success",
    "result": {
        "taskId": 1,            // 本次调用的唯一id标识
        "taskStatus":3,         // 任务状态：1-新建，2-执行中，3-执行成功，4-执行失败,5-被终止,6-执行超时,7-超出并发限制
        "response":"xxxx",      // 服务处理的输出结果，***接口真正需要的数据***
        "stdout":"xxx"          // 当status=4时，stdout服务调用时的错误输出信息，其他为null
    },
    "status": true              // 请求正常status=true，反之为false
}
```
在系统配置-》API相关中修改API返回适配器

![](../../assets/SRHABbyoIDK6GE/image_021.bin "")
```
var data = JSON.parse(response.result.response); // 输入为 response 对象
response = data; // 处理完后, 输出直接赋值到 response 变量
console.log('return final', response)
```
修改API发送适配器，所有的发送请求会携带当前的操作人信息

![](../../assets/SRHABbyoIDK6GE/image_022.bin "")
```
// 操作人信息
var tmp = data
var origin = data['parameter'].slice(1)
tmp['parameter'] = '{\"usr\":\"' + headers['AMIS_USER'] + '\",'+ origin
modifier = {
  data: tmp
};
```
修改API返回适配器执行环境和数据体格式

![](../../assets/SRHABbyoIDK6GE/image_023.bin "")
#### 3.1.2、新建任务页面
##### （1）子页面设置
在管理中心-》页面管理-》新建文件夹 后台管理系统CRUD

![](../../assets/SRHABbyoIDK6GE/image_024.bin "")
将任务管理的父级页面改为后台管理系统CRUD，同时新建页面

![](../../assets/SRHABbyoIDK6GE/image_025.bin "")
页面管理页中点击后台管理系统CRUD，可以看到两个子页面

![](../../assets/SRHABbyoIDK6GE/image_026.bin "")
##### （2）form表单组件
进入新建任务页面，修改页面内容（核心是[form表单组件](https://baidu.github.io/amis/zh-CN/components/form/index)）

![](../../assets/SRHABbyoIDK6GE/image_027.bin "")
其中，actions控制重置、提交等按钮操作，controls控制表单字段与页面布局，initApi控制表单初始值。

**actions：**

```
"actions": [
        {
          "type": "reset",
          "label": "重置"
        },
        {
          "type": "submit",
          "label": "提交",
          "actionType": "ajax",
          "api": {
            "method": "post",
            "url": "KIRIN_URL",
            "data": {
              "name": "NAME",
              "token": "TOKEN",
              "parameter": "这里省略，太长了...看源码",
          },
          "level": "primary",
          "dataType": "json"
        }
      ]
```
这里需要将表单数据处理为kirin接受的接口格式，调用新建任务接口，后端将数据插入qadc。

**controls：**

这里的表单内容使用fieldSet组件划分为3部分

![](../../assets/SRHABbyoIDK6GE/image_028.bin "")
以版本信息为例，controls中的每一个元素为表单的一个字段

![](../../assets/SRHABbyoIDK6GE/image_029.bin "")
典型的一些数据输入：

|type|示例|json配置|
|-|-|-|
|text|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=7353930ca495cc09f6667efeec01b30c "")|{
  "type": "text",
  "name": "new_version",
  "label": "版本号",
  "required": true,
  "placeholder": "示例：8.0.1"
}|
|switch|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=d288a0ffc9bb11bd05d6a77bf4694acb "")|{
  "type": "switch",
  "label": "是否为正式版",
  "name": "is_stable",
  "value": 0,
  "trueValue": 1,
  "falseValue": 0,
  "required": false
}|
|select|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=b89cec3b127bd7542f56d9d5fa026429 "")|  展开源码 {
  "type": "select",
  "label": "客户端类型",
  "name": "client_type",
  "value": "2",
  "required": true,
  "searchable": false,
  "options": [
    {
      "label": "Android",
      "value": "2"
    },
    {
      "label": "iPhone",
      "value": "1"
    },
    {
      "label": "WP",
      "value": "3"
    },
    {
      "label": "Win8",
      "value": "4",
      "disabled": true
    },
    {
      "label": "iPad",
      "value": "5"
    }
  ]
}|
|city|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=4923a87f9a1fe62ac9bbb8bad3aa8285 "")|{
  "type": "city",
  "label": "使用城市",
  "name": "city",
  "allowDistrict": false,
  "placeholder": "选择城市",
  "labelRemark": null,
  "searchable": "true",
  "required": true
}|

比较实用的还有：[DiffEditor 对比编辑器](https://baidu.github.io/amis/zh-CN/components/form/diff-editor) 、[Editor 编辑器](https://baidu.github.io/amis/zh-CN/components/form/editor) 、[Color 颜色选择器](https://baidu.github.io/amis/zh-CN/components/form/color) 、[Rich-Text 富文本编辑器](https://baidu.github.io/amis/zh-CN/components/form/rich-text) 

**initApi：**

```
"initApi": {
                "method": "post",
                "url": "KIRIN_URL",
                "data": {
                    "name": "NAME",
                    "token": "TOKEN",
                    "parameter": "{\"req_type\":\"3\",\"new_version\":\"$new_version\"}"
                },
                "dataType": "json"
            }
```
当链接携带new_version数据时，如点击任务管理页面的编辑按钮，就会跳转到[http://amis.baidu.com/group/learn-amis/index/newTask?new_version=4.2.1](http://amis.baidu.com/group/learn-amis/index/newTask?new_version=4.2.1) ，调用表单初始化接口，这里的版本号作为key后端查询表后返回数据作为表单初始值。需要注意的是，重置按钮是指重新调用初始化接口，而不是清空表单内容。

![](../../assets/SRHABbyoIDK6GE/image_030.bin "")
新建任务页面地址： [http://amis.baidu.com/group/learn-amis/index/newTask](http://amis.baidu.com/group/learn-amis/index/newTask)

![](../../assets/SRHABbyoIDK6GE/image_031.bin "")
#### 3.1.3、任务管理页面
##### （1）crud组件
任务管理页面主要使用[crud组件](https://baidu.github.io/amis/zh-CN/components/crud)

![](../../assets/SRHABbyoIDK6GE/image_032.bin "")
api设置为页面初始化时调用查询所有任务接口，columns用于设置具体展示的字段或操作，loadDataOnce设为true表示一次加载所有数据在前端进行分页，defaultParams中设置了每页展示元素个数。

|类型|示例|配置json|
|-|-|-|
|text|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c28abea1e00cb8db3f4ed7ed779423d2 "")|{
  "name": "task_name",
  "label": "任务名称",
  "sortable": true,
  "quickEdit": true
}|
|map|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=3d079f939ac2f939ffe0981a29db5711 "")|  展开源码 {
  "type": "map",
  "label": "客户端类型",
  "name": "client_type",
  "map": {
    "1": "iPhone",
    "2": "Android",
    "3": "WP",
    "4": "Win8",
    "5": "iPad"
  },
  "sortable": true,
  "quickEdit": {
    "type": "select",
    "options": [
      {
        "label": "Android",
        "value": "2"
      },
      {
        "label": "iPhone",
        "value": "1"
      },
      {
        "label": "WP",
        "value": "3"
      },
      {
        "label": "Win8",
        "value": "4",
        "disabled": true
      },
      {
        "label": "iPad",
        "value": "5"
      }
    ]
  }
}|
|map|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=b1dc228b36852054bd263b12bce80ba3 "")|{
  "type": "map",
  "label": "状态",
  "name": "is_stable",
  "map": {
    "0": "<span class=\"label label-danger\">未上线</span>",
    "1": "<span class=\"label label-success\">已上线</span>"
  },
  "sortable": true
}|

这里任务名称和客户端类型quickEdit设为true，可以快速编辑，但是还没来得及写对应的quickSaveApi接口。

##### （2）交互逻辑
![](../../assets/SRHABbyoIDK6GE/image_033.bin "")
**查看**

点击后，触发drawer组件，将数据中的字段展示出来。

**编辑**

点击后，携带版本号信息跳转至新建任务页面，[http://amis.baidu.com/group/learn-amis/index/newTask?new_version=5.2.1](http://amis.baidu.com/group/learn-amis/index/newTask?new_version=5.2.1) ，触发表单初始化接口，改变form组件初始值。

**删除**

点击后，触发删除任务接口，后端进行数据删除操作（将is_detete置为true）。

任务管理页面地址： [http://amis.baidu.com/group/learn-amis/index/manage](http://amis.baidu.com/group/learn-amis/index/manage)

![](../../assets/SRHABbyoIDK6GE/image_034.bin "")
### 3.2、风险评估报告
#### 3.2.1、报告样例
地址：[http://amis.baidu.com/group/learn-amis/report/report1](http://amis.baidu.com/group/learn-amis/report/report1)

![](../../assets/SRHABbyoIDK6GE/image_035.bin "")
**一些前端细节：**

|描述|示例|json配置|说明|
|-|-|-|-|
|表格数据飘红飘绿|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=c6e36847b4322bfdc06e0d041c7f451e "")|  展开源码 {
  "type": "tpl",
  "label": "CTS覆盖率",
  "name": "cov_merge",
  "tpl": "<% var num = data.cov_merge %> <% if(num>=60){%> <span class='text-success'><%-num %>%</span><% } %> <% if(num<60 && num>=0){%><span class='text-danger'><%-num %>%</span> <% }%> <% if(num==-1){%>暂无数据 <% }%>"
}|[6,∞）飘红%，[0,60) 飘绿%，为-1显示暂无数据|
|url链接|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=d2f7b4509f842728e3c07760cd18607d "")|{
    "name": "url",
    "type": "tpl",
    "label": "报告链接",
    "tpl": "${url|raw}"
}|url: "<a href="http://test.perf-analysis.baidu-int.com/report/report_old_cardan/368851" target="_blank" class="a-Link"><span class="a-TplField">http://test.perf-analysis.baidu-int.com/report/report_old_cardan/368851</span></a>"这里的值为链接的html，不加raw就是直接显示值|
|弹窗为表格|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=7f072b1201a38a4827fa42ba0c417845 "")点击后：![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=66b43c1372722e14865928cba0f186d7 "")|{
  "type": "operation",
  "label": "Cts覆盖代码详情",
  "buttons": [
    {
      "type": "button",
      "icon": "fa fa-eye",
      "actionType": "dialog",
      "dialog": {
        "size": "lg",
        "title": "Cts覆盖代码详情",
        "body": {
          "type": "tpl",
          "label": "Cts覆盖代码详情",
          "name": "cts_branch_check_detail",
          "tpl": "${cts_branch_check_detail|raw}"
        }
      }
    }
  ]
}|cts_branch_check_detail: "<ul><li>product/second_step/xxxx.cpp<ul><li><pre> 100行 至 101行，是否是防御新分支：否，是否有断言：否</pre>&nbsp;&nbsp;&nbsp;&nbsp;代码行内容：aaa/bbb/xxx.cpp:100,</br>&nbsp;&nbsp;&nbsp;&nbsp;aaa/bbb/xxx.cpp:101</li></ul></li><li>product/secp/xxxx.cpp<ul><li><pre> 100行 至 101行，是否是防御新分支：否，是否有断言：否</pre>&nbsp;&nbsp;&nbsp;&nbsp;代码行内容：aaa/bbb/xxx.cpp:200</li></ul></li><li>product/second/xxxx.cpp<ul><li><pre> 100行 至 101行，是否是防御新分支：否，是否有断言：否</pre>&nbsp;&nbsp;&nbsp;&nbsp;代码行内容：aaa/bbb/xxx.cpp:100</li></ul></li></ul>"这里的值为表格的html，不加raw就是直接显示值|
|标注交互|![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=f5f796f81d67c2a88f8b59c81d0108cb "")标注后：![](http://rte.weiyun.baidu.com/api/imageDownloadAddress?attachId=65427a6cb7c529eebeb8f942f86ff7d8 "")|接口返回：  展开源码 {"status": 0, "msg": "分级风险结论误报已标注", "data": {"show_msg2": "人工标注分级结果：可自主测试。误报原因：测试test，标注人：zhoujie19，标注时间：2021-06-02 03:17:12", "tag2": "2"}}|reload设置用返回的值重新加载标注结果对应的字段，tag2控制确认、误报、重置的禁用状态|



**页面逻辑：**

页面初始化会调用**页面初始化**接口，返回数据进行整个页面的渲染。

点击确认按钮，调用**准入标注确认**接口，重置按钮显示，并禁用标注功能。

点击误报按钮，会弹出表单填写误报原因，提交后调用**准入标注误报**接口，重置按钮显示，并禁用标注功能。

点击重置将清除标注结果，并调用**准入标注重置**接口。

![](../../assets/SRHABbyoIDK6GE/image_036.bin "")
详细实现记录：[质量度风险评估报告（Amis平台）](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1199071983)

#### 3.2.2、form动态刷新与联动
地址：[http://amis.baidu.com/group/learn-amis/report/report2](http://amis.baidu.com/group/learn-amis/report/report2)

![](../../assets/SRHABbyoIDK6GE/image_037.bin "")
这里表单和表格是两个平级的组件，将表格name设置为table，通过name进行联动。

使用到的接口功能：

|req_type|功能|
|-|-|
|0|查询所有产品线信息|
|9|查询各产品线和业务方向历史配置信息|
|10|查询产品线已配置过的业务方向列表|

**页面逻辑：**

页面初始化会调用**查询所有产品线信息**接口，通过返回数据动态获取到表单组件产品线名可选择列表。

表格会根据产品线名和业务方向的值变动，调用**查询各产品线和业务方向历史配置信息**接口，刷新数据，未选择时返回所有数据。

表单选择产品线名为手百服务，调用**查询产品线已配置过的业务方向列表**接口，通过返回数据动态获取到业务方向可选择列表。表格根据产品线名和业务方向的值变动而刷新。

这里有3个关键的属性：

|属性名|类型|默认值|说明|
|-|-|-|-|
|submitOnChange|boolean|false|表单修改即提交|
|target|string||传值给表格|
|reload|string||操作完后刷新表格对象|

![](../../assets/SRHABbyoIDK6GE/image_038.bin "")
详细接口API：[8.4.1.1-准入特征配置交互接口API](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1266574444)

#### 3.2.3、前端json定制生成
地址：[http://amis.baidu.com/group/learn-amis/report/report2](http://amis.baidu.com/group/learn-amis/report/report2)

![](../../assets/SRHABbyoIDK6GE/image_039.bin "")
有时候会面临多个模块需要展示，但是不确定具体有几个模块，这样amis前端的json配置就不是固定的，需要根据模块多少进行改变。

这里使用一个很重要的[schemaApi](https://baidu.github.io/amis/zh-CN/components/service#%E5%8A%A8%E6%80%81%E6%B8%B2%E6%9F%93%E9%A1%B5%E9%9D%A2)，通过它可以实现动态渲染页面内容。

页面有两个平级的service服务，是因为表格不像crud没有数据加载功能，需要在外面套一层service服务来进行api调用数据渲染。第一个service服务对应rb测试情况的数据，第二个service服务对应多个卡片信息。两个服务之间是完全独立的。

使用到的接口功能：

|req_type|功能|
|-|-|
|0|获取卡片对应的schema信息|
|1|页面数据初始化|
|5|卡片信息初始化|

**页面逻辑：**

页面初始化时，第一个service服务会调用**页面数据初始化**接口，获得rb测试情况部分的数据。

同时，第二个service服务调用**获取卡片对应的schema信息**接口，返回的值就是多个卡片信息的json配置，再根据json配置的内容，调用其中的**卡片信息初始化**接口，获得每个卡片的数据。

至此页面加载完成。

![](../../assets/SRHABbyoIDK6GE/image_040.bin "")
这里每个测试结果之所以有两个，是为了实现当测试状态为成功时折叠测试结果内容。实现方法是一个组件设置为默认折叠，一个设置默认展开，设置visibleOn属性根据测试状态只显示其中一个组件，另一个隐藏。



amis开发的原则：数据处理能放后端的尽量放后端处理吧。。。

这么长，感谢看完喵~

---

相关链接：[https://aisuda.bce.baidu.com/amis/zh-CN/docs/index](https://aisuda.bce.baidu.com/amis/zh-CN/docs/index)

amis组件库：[https://baidu.github.io/amis/zh-CN/components/page](https://baidu.github.io/amis/zh-CN/components/page)

amis示例：[https://baidu.github.io/amis/examples/index](https://baidu.github.io/amis/examples/index)

github地址：[https://github.com/baidu/amis](https://github.com/baidu/amis)

kirin官方文档：[http://wiki.baidu.com/pages/viewpage.action?pageId=1043213149](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1043213149)



![](/personal-site-mvp/img/docs-assets/image_041.png "")

