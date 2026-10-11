---
title: "0、效果演示"
description: "💡完整方案&源码：沙箱+ducc+skills+AI干活并流式推送如流"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🤖如流&ducc&skills&沙箱开发接入指南\\📁 💡完整方案&源码：沙箱+ducc+skills+AI干活并流式推送如流.md"
---
💡完整方案&源码：沙箱+ducc+skills+AI干活并流式推送如流

开放源码（没权限的话直接申请读权限即可）：[文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/quick_start_with_sandbox_ducc.py?t=mention&mt=doc&dt=sdk)

**遇到问题？**[@呼叫客服](infoflow://APICenter?data=eyJBUElOYW1lIjogIkJkSGlKcy5zZXJ2aWNlLmhpLm9wZW4iLCAidmVyc2lvbiI6IDY1LCAiZGF0YSI6IHsidHlwZSI6ICIxIiwgInVzZXJpZCI6ICJndXlvdWRhIiwgImRyYWZ0IjogIuW/q+mGkumGkizmnaXmtLvkuoYoKl4tXinPgSgq4pWvXuKVsCkifX0=)

**不知道能干嘛？没思路？不妨看看这些场景，也许就有你需要的** [🧐各场景解决方案&SKILL源码(持续更新中...)](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/-wSQPmA1pGf6pA?t=mention&mt=doc&dt=doc)

# 0、效果演示
|输入Query|返回结果|
|-|-|
|甩个报错日志过去，自己登录线上机器，找到对应的实例，检索异常日志，读代码定位问题，修复代码，建卡，提代码，发消息摇人CR....{    "code": 500,    "msg": "服务内部异常Cannot invoke \"java.lang.Integer.equals(Object)\" because the return value of \"com.baidu.qep.delivery.engine.aiqa.bean.req.SaveOrUpdateCronJobReq.getAiworkerId()\" is null",    "requestId": "20260319-engine-03-87d1-373504d18417",    "data": null}|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|总结下这个文档 [🧩实战:基于数据库+日志+代码+知识库SKILL实现业务日常咨询&答疑&问题定位&监控报警等](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/Zol1bZ2Jtk3VVH?t=mention&mt=doc&dt=doc) |![](/personal-site-mvp/img/doc-placeholder.svg "")|
|帮查下这个卡片的内容 [[feed00-65499] 【产品】【图文】客户端测试](https://console.cloud.baidu-int.com/devops/icafe/issue/feed00-65499/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk) |![](/personal-site-mvp/img/doc-placeholder.svg "")|
|有修改iCafe卡片的SDK吗|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|**侧边栏应该怎么接入，成本大吗**|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|怎么管理AIQA的上下文记忆数据|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|提取一下 [[BaiduSearchbox-50231] 【在线 - 百度App】【安卓手百】+动态发布页面没有发布按钮+5702365+5702365 + 互动&社交/动态/发布动态](https://console.cloud.baidu-int.com/devops/icafe/issue/BaiduSearchbox-50231/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)  这个iCafe卡片内容里面的图片链接，给一下对应的源码|![自己尝试，遇到问题自己解决](/personal-site-mvp/img/doc-placeholder.svg "自己尝试，遇到问题自己解决")![生成代码](/personal-site-mvp/img/doc-placeholder.svg "生成代码")![给出使用方式](/personal-site-mvp/img/doc-placeholder.svg "给出使用方式")|
|20260304-engine-00-a643-8d747550cffb|![](/personal-site-mvp/img/doc-placeholder.svg "")|
|帮查下search-data-25344这张卡片今天pushDataToSkg的日志|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|分析下最近90天以来总体接口的访问PV UV情况，找出波动较大的接口|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|**这些场景太简单？更多可实现的效果参考** [🧩实战:基于数据库+日志+代码+知识库SKILL实现业务日常咨询&答疑&问题定位&监控报警等](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/Zol1bZ2Jtk3VVH?source=137?t=mention&mt=doc&dt=doc)||

# 1、源码介绍
开放源码（没权限的话直接申请读权限即可）：[文件页：baidu/ep-qa/qep_delivery_open_source  *master](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/quick_start_with_sandbox_ducc.py?t=mention&mt=doc&dt=sdk)

同一份代码服务,支持以下3个渠道调起并流式回复

* 如流单聊or群聊@数字员工
* 如流侧边栏
* TestOne平台前端

Demo具备的功能

* 调用公司的沙箱平台,申请沙箱环境,并将 skills+代码扔到沙箱调起ducc执行
    * 记忆管理(当前是否有可用的沙箱,有的话直接复用,没有的话申请新的)
    * 申请沙箱
    * 代码文件上传到沙箱环境
    * 远程调用沙箱执行任务
    * 沙箱干活并实时流式推送数据到TestOne平台/如流对话框/如流侧边栏
    * 执行完毕以后,产出的中间文件上传BOS持久化
    * ducc(ClaudeCode)的session管理, 多轮会话复用session
    * 更多功能详见SDK...

* 直接调用DeepSeek(或者自己更换为其他模型),进行各种问答

# 2、准备环境
建议先参考以下文档跑通流程，再看此文档

* [🚀QuickStart：30分钟快速看见效果](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/rKjIOhc7cB82Rv?t=mention&mt=doc&dt=doc)
* [代码空间版](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/Yj6Y_IsOpw96FE?source=137?t=mention&mt=doc&dt=doc)



> 运行环境: python3.10+ 
> 建议使用iCoding, 方便直接调试验证
> 创建一个独立的虚拟环境: python3 -m venv venv 
> 激活虚拟环境: source venv/bin/activate
> 依赖安装: pip3 install -r requirements.txt -U --index-url [http://pip.baidu.com/root/baidu/+simple/](http://pip.baidu.com/root/baidu/+simple/) --trusted-host pip.baidu.com --no-cache-dir
# 3、基于沙箱+ducc+skills+AI的复杂场景
## 3.1、账号更换
> 针对暂时还没有ToB的ducc以及模型账户的同学，直接使用自己开发机的ducc也行
> 此时无需 BAIDU_CC_XXX, ANTHROPIC_XXX, E2B_API_KEY 相关的账户也可使用
> 具体怎么调用本地的ducc, 请参考:[代码空间版](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/3LoFUu-M_a/U-RwwdZ7ut/Yj6Y_IsOpw96FE?source=137?t=mention&mt=doc&dt=doc)
**环境变量提供相关依赖的TOKEN**

> 修改 ~/.bash_profile, 在底部新增以下内容
```
# TestOne: username是公司的邮箱前缀，token打开 https://testone.baidu-int.com/ 右上角获取
export TESTONE_USERNAME='<TESTONE_USERNAME>'
export TESTONE_TOKEN='<TESTONE_TOKEN>'

# Icafe: username是公司的邮箱前缀，password请让用户浏览器直接打开 https://console.cloud.baidu-int.com/api/icafe/users/virtual 获取
export ICAFE_USERNAME='<ICAFE_USERNAME>'
export ICAFE_PASSWORD='<ICAFE_PASSWORD>'

# infoflow: 登录机器人后台获取对应的appKey和appSecret https://qy.baidu-int.com/index.html
export INFOFLOW_APP_KEY='<INFOFLOW_APP_KEY>'
export INFOFLOW_APP_SECRET='<INFOFLOW_APP_SECRET>'
```


**修改 quick_start_with_sandbox_ducc.py   resources/task.py 更新相关的账号信息**



## 3.2、代码解读
* 代码入口 [quick_start_with_sandbox_ducc.py ](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/ep-qa/qep_delivery_open_source/blob/master/ai-agent/quick_start_with_sandbox_ducc.py)

# 4、日常开发调试
* 日常开发建议使用icoding机器,启动quick_start_with_sandbox_ducc.py 即可,将自己服务的http接口注册到TestOne平台即可

# 5、线上部署使用
* **建议**使用kirin平台
* 或者参考quick_start_with_sandbox_duccpy 给出来的API示例,自己部署自己运维服务
