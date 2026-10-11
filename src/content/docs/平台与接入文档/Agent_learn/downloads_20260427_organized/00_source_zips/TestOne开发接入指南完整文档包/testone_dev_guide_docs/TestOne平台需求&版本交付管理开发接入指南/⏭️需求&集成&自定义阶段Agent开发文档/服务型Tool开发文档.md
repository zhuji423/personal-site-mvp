---
title: "服务型Tool开发文档"
description: "服务型Tool开发文档"
date: "2026-10-11"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\TestOne开发接入指南完整文档包\\testone_dev_guide_docs\\TestOne平台需求&版本交付管理开发接入指南\\⏭️需求&集成&自定义阶段Agent开发文档\\服务型Tool开发文档.md"
---
服务型Tool开发文档

### **1.开发模板**
[文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/tree/master/tool?t=mention&mt=doc&dt=sdk)

依赖安装：pip3 install -r requirements.txt -U --index-url [http://pip.baidu.com/root/baidu/+simple/](http://pip.baidu.com/root/baidu/+simple/) --trusted-host pip.baidu.com  --no-cache-dir

### **2.部署要求**
服务型tool开发后打包：sh build.sh (不要搞错build.sh文件[文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/tool/build.sh?t=mention&mt=doc&dt=sdk))

部署到kirin，当前kirin仅支持python3.11

### **3.配置方法**
##### **1）注册**
提供kirin服务url、超时时间、同步或异步、工具名称、工具类型、工具功能描述等信息

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=771feee1add445b694dd1ce1e3299c49&docGuid=1z9riftjDVS9XD "")
##### 2）部署kirin测试环境
当注册时添加了接口地址：http://kirin.baidu-int.com/api/tool/xxxxxx，平台支持直接在平台上实现kirin服务的测试环境部署

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ef6bb0567cb94bc58ee61161ab224d7a&docGuid=1z9riftjDVS9XD "")
① 上传新包，并用新包部署测试环境

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=286b5b45e0024ba7a5498a370fca3716&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b6ce4e26b01d40d3a2d4f8bde5025bc4&docGuid=1z9riftjDVS9XD "")
② 选中历史包，并用历史包部署测试环境

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=86de3f516f0d48aaa284df735d5a0ccc&docGuid=1z9riftjDVS9XD "")
##### 3）调试
添加测试参数，可以选择测试kirin的测试环境和kirin的线上环境。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7488f4188dc941cf843e9013c57d1693&docGuid=1z9riftjDVS9XD "")
① 测试环境调试。请基于执行结果，调整tool代码，确保前端展示符合预期

说明：当前测试环境没有调试成功的任务，因此"上线"无法点击。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5d63848a3ac74c909d1c471fa380fb50&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aadd9236ee7b420dade316eada0a4e3f&docGuid=1z9riftjDVS9XD "")
② 线上环境调试。先保证kirin服务已通过kirin平台的审核，发起kirin平台的审核后可以找[@侯澄](https://ku.baidu-int.com?t=mention&mt=contact&id=4EOaqzMr)加速审核。再确保线上环境已部署。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=22859fd543cf47f0a2d3d229dfad24e0&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c0978c66cd1e4460b24b3d7a4d793f8d&docGuid=1z9riftjDVS9XD "")
##### 4）上线
① 上线前确认

* kirin服务已通过kirin平台的审核
* 在包部署到测试环境后，有执行成功的测试环境的调试任务

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d9d3d48aa3004a85831c9cb098292d69&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6b52dc600cd4ccba41f9b2950338247&docGuid=1z9riftjDVS9XD "")
② 上线失败，请按照提示词进行相关操作

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6d0413a195c94ecebd1ed93d14d26060&docGuid=1z9riftjDVS9XD "")
③ 上线成功，展示安装进度

* 可以安装

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8f52f13f07d149f2a4a100ae6e4c64ba&docGuid=1z9riftjDVS9XD "")
* 展示安装进度

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3cc38ef76133484ba6c90671ab2aa589&docGuid=1z9riftjDVS9XD "")
* 安装完成

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f03b4859e8e2407e9e9738aeb4296d18&docGuid=1z9riftjDVS9XD "")
##### 5）审核：将私有函数型tool升级为服务型tool
**工具调用类型**：

* **私有函数型tool**: tool的功能代码直接写在agent的代码中，若同一个tool想要运用到不同的agent（或不同的业务线）时，agent的开发者需要copy工具代码到另一个agent中，不方便tool升级; 
* **公共函数型tool**: tool的调用方式和功能由平台侧统一提供，agent的开发者可以在agent中直接调用tool的sdk，由平台侧负责sdk的升级; 
* **服务型tool**: 独立于agent存在，在配置中心直接配置，由tool的开发者负责tool的升级，可以低成本地落地到更多业务线；

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8163b3867c254e619931b57f760d6753&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=661be53395ee408d9969d64e4476ead9&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6b394821bb67456a9ad585781f38bca3&docGuid=1z9riftjDVS9XD "")
用户注册tool后，默认是私有函数型tool，当tool的信息中包含接口地址且接口地址属于kirin服务时，比如[http://kirin.baidu-int.com/api/tool/214231](http://kirin.baidu-int.com/api/tool/214231)，可以在完成线上环境调试后，点击"发布为服务型tool"来发起审核（若想快点通过审核，可以找找[@楼瀚琼](https://ku.baidu-int.com?t=mention&mt=contact&id=kKgfSuTe)，[@顾友达](https://ku.baidu-int.com?t=mention&mt=contact&id=043a5260-7571-11ef-a39f-df0d8349b618)，[@汪世涛](https://ku.baidu-int.com?t=mention&mt=contact&id=074c7460-7571-11ef-a39f-df0d8349b618)），出现错误提示请按照提示对服务进行修改

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a5129598b01f44419c0af2781c8a320c&docGuid=1z9riftjDVS9XD "")
##### 6）配置使用
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5b9a8f5b64024c2295f39c0f8b5a9277&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b5a38a6499e64a8c914635ba6147fa2a&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac51530d65a54d74b78b1ea11c32387f&docGuid=1z9riftjDVS9XD "")
### **4.执行逻辑说明**
服务型tool和agent的执行顺序（当前服务型tool只支持需求测试，不支持集成测试）：

[流程图]
### **5.执行结果处理：**
风险：agent和服务型tool中有一个以上的tool结果是高风险，则测试阶段是高风险。服务型tool高风险会阻止测试阶段流转。

(若高风险时不想阻塞测试阶段流转，可以使用is_block参数实现。不建议使用，容易导致高风险被忽略)

结果展示：服务型tool和agent中普通tool的执行结果会一起展示。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3a7af9717a8746e9a9a76c4f287b7b1b&docGuid=hxL6n1aifLh3fx "")
### **6.业务参数配置：**
当同一个tool配置到不同业务线需要配置不同业务参数时，服务型tool提供业务参数配置机制

**1）提供业务参数模板**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=40626bf1bb9748db9e6114b61c67d606&docGuid=dWYfOOHY6jp-75 "")
模板以json格式存储在数据库中，比如

[{"**key**":"**inform_bug_space**","**label**":"订阅bug空间的业务线","**value**":"222_搜索,1583_纵横四海","**required**":true},{"**key**":"**inform_icafe_space**","**label**":"订阅需求空间的业务线","**value**":"222_基础,410_好看视频,222_内核","**required**":false},{"**key**":"inform_official_account","**label**":"订阅公众号的业务线","**value**":"550_feed","**required**":false}]

① key（截图中第一列）用于服务型tool参数解析。

② label（截图中第二列）用于前端展示，方便不同业务线配置服务型tool的业务参数时理解参数的作用。

③ value（截图中第三列）用于前端展示，参数值的示例。

④ required（截图中第四列）表示该参数是否必填。

**2）配置业务参数**

添加好上图中的参数模板，在配置页添加或修改服务型tool时会出现业务参数配置弹窗

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b63544a2abce4735820a0962310947bd&docGuid=1z9riftjDVS9XD "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6539ba8cf13e4b57ab57bc69d9c19495&docGuid=1z9riftjDVS9XD "")
业务参数以json格式存储在数据库中，比如

{"**inform_bug_space**":"222_搜索,222_基础","**inform_icafe_space**":"999_手百"}

服务型tool可以从引擎的请求参数ext_data中获取到该业务参数

**3）特殊参数类型支持**

**业务线**：由于智能交付平台确定业务线需要通过业务线id和子方向名来双重确定。用户不易获取。因此约定特殊字符串#PRODUCT，支持将普通的输入框变成多选框

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b29614d375684e239ccf941a4b5cf324&docGuid=1z9riftjDVS9XD "")
模板以json格式存储在数据库中，比如

[{"key":"**inform_bug_space**","label":"订阅bug空间的业务线","value":"**#PRODUCT**","required":true},{"key":"**inform_icafe_space**","label":"订阅需求空间的业务线","value":"**#PRODUCT**","required":false}，{"key":"**inform_official_account**","label":"订阅公众号的业务线","value":"**#PRODUCT**","required":false}]

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac12efd0acad450fa1c88e2be68e5a27&docGuid=1z9riftjDVS9XD "")
业务参数以json格式存储在数据库中，比如

{"inform_bug_space":[{"label":"大FEED-服务端",**"value":"550-服务端"**,"key":"550-服务端"},{"label":"百度APP-基础",**"value":"222-基础"**,"key":"222-基础"},{"label":"百度APP-内核",**"value":"222-内核"**,"key":"222-内核"}],"inform_icafe_space":[{"label":"小说-服务端",**"value":"310-服务端"**,"key":"310-服务端"},{"label":"小说-客户端",**"value":"310-客户端"**,"key":"310-客户端"},{"label":"百度APP-基础",**"value":"222-基础"**,"key":"222-基础"}],"inform_official_account":[{"label":"好看视频-好看视频",**"value":"410-好看视频"**,"key":"410-好看视频"}],"type":"HIGH"}

****


