---
title: "1  项目详情"
description: "新增短剧widget"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\lib\\req_agent\\ku\\MRi0VcvICjS6lu.md"
---
新增短剧widget



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3dfa422d528e49fca84c72bf78cb7e54&docGuid=MRi0VcvICjS6lu "")
开发：11.4-11.8

联调：11.11-11.15

提测：11.15

# 1  项目详情
**MRD**

[[ailite-25967] 【v6.38~v6.39】新增短剧widget](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-25967/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)

# 2 产品形态
  

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cb0b3aada799454bbb144c6165bc3f8f&docGuid=MRi0VcvICjS6lu "")
# 3 沟通地图
## 内部
|    角色|    接口人|备注|
|-|-|-|
|   PM|   @王啸飞||
|   SRD|   @潘超毅     @李云清||
|  FE|   @刘艳丽||
|CRD|    @王贵龙     @潘启硕||
|搜索 SRD|     @赵然||
|SQA|      ||
| FEQA| ||
|CRQ|||


## 模块拆分
### C端
|接口内容|接口描述|代码库|备注|
|-|-|-|-|
|静默添加接口|增加短剧widget静默添加顺序|文件页：baidu/searchbox/sbox-basic  *master||
|widget详情|获取我得更新，续看，历史，热榜数据 格式处理返回|文件页：baidu/searchbox/ugact  *master||
### 脚本
|任务内容|任务描述|    代码库|备注|
|-|-|-|-|
|脚本增加push数据存储|续看和更新保存数据库|文件页：baidu/searchbox/bdapp_frontend  *master||
### 下游依赖
|任务内容|任务描述|接口人|备注|
|-|-|-|-|
|短剧热榜|获取短剧热榜|@孙记风|短剧list内网服务|
# 4 详细设计
## 4.1 接口设计
### 4.1.1 silentadd静默添加--对and端接口
#### 4.1.1.1 静默添加条件
|条件|内容|控制方|备注|
|-|-|-|-|
|触发时机|长播：用户对该剧合集下的子视频播放时长>=50秒（仅限于单一视频，非多视频累加）|端||
||点赞：用户对该剧合集下的子视频点赞pv>=1|||
||分享：用户对该剧合集下的子视频分享pv>=1|||
||评论：用户对该剧合集下的子视频评论pv>=1|||
||追剧：用户对该剧合集下的子视频追剧pv>=1|||
|触发条件|对应机型完成了静默添加突破|端||
||用户手机上没有短剧widget|端携带addedwidgets，server依此判断||
||该用户未被静默添加过——CUID维度|端携带addedwidgets，server依此判断||
||该用户没有拒绝过端内短剧widget引导添加弹窗|端再看一下|拒绝了target就不带|
|风险规避|技术逻辑，通过插件形式下发|端||
||给用户静默添加上以后删除插件|端||
||开关：出现舆情后进行功能关闭，不再进行下发（但已经安装的无法删除）|server||
|实验|实验组1: 默装|server|统一用端的控制|
||实验组2: 授权弹窗|？|引导授权弹窗与server无关，端获取实验开关|
|地域屏蔽|"北京", "上海", "广州", "深圳", "东莞", "南京", "西安", "武汉", "杭州", "成都", "天津"|server||
**静默安装widget优先级：**任务中心widget>存钱罐widget>游戏中心widget>短剧widget>清理加速widget>搜索widget

**主动添加-端内引导弹窗--**与server无关

#### 4.1.1.2 流程图
[流程图]
#### 4.1.1.3 协议
|PATH|/baiduboxapp/basic/widget/silentaddlite|
|-|-|
|METHOD|POST|
|Content-Type|application/x-www-form-urlencoded|
|Get参数|客户端公参|
|Post参数|如下|
|字段名称|字段类型|字段值|
|-|-|-|
|deviceLevel|string|-1: 未获取到, 1:低端机, 2:中端机, 3:高端机,|
|addedWidget|string|{     "1-1901": { // key格式: widgetType-id         "id": "1", // id, string         "addType": "0", //添加类型: string 0: 标准添加, 1: 静默添加        "widgetType":"1",// widget类型，1nawidget，2 openwidget         "delete": "0" // 0：未删除，1：已删除（仅静默添加存在该状态）     } }|
|targetWidgets|string|{     "1-1": { // key格式: widgetType-id         "id": "1", // id, string // 搜索widget，增加实验开关         "widgetType":"1" // widget类型，1nawidget，2 openwidget     },      "1-1900": { // key格式: widgetType-id         "id": "1900", // id, string // 金币激励widget         "widgetType":"1" // widget类型，1nawidget，2 openwidget     },     "1-1901": { // key格式: widgetType-id     "id": "1901", // id, string // 存钱罐widget     "widgetType":"1" // widget类型，1nawidget，2 openwidget     },   "2-207552936573408": { // key格式: widgetType-id     "id": "207552936573408", // id, string // 游戏widget     "widgetType":"2" // widget类型，1nawidget，2 openwidget     } "2-212378996573258: { // key格式: widgetType-id     "id": "212378996573258", // id, string // 短剧widget     "widgetType":"2" // widget类型，1nawidget，2 openwidget     } }|
### 4.1.2 openwidget内容--对fe接口
#### 4.1.2.1 流程图
[流程图]
#### 4.1.2.2 协议
接口path: /inner/playlet/widgetDetail

请求类型：POST

参数：

|     字段名|  类型| 实例|备注|
|-|-|-|-|
|     appname|string|baiduboxlite|公参，query里fe会带|
|     osbranch|string|a2|公参，query里fe会带|
|     playlet|object|{"historyData":
  [
    {"setId":"9547468937562488367","nid":"sv_4611530927918348481","watchSequence":1}
  ]
}|body参数 和端对齐|


```
{
    "errno": 0,
    "timestamp": "1720529288",
    "logid": "2260411628",
    "data": {
        "scheme": "", // 左上角，【短剧】字样：点击跳转至视频底bar短剧tab
        "updateModel":{     //我的更新模块
            "type":"new",  //default：兜底，new：最新
            "title":"我不是神医", //标题
            "sequence":1, //第X集
            "img": "", // 背景图
            "scheme":"" //跳转地址 合计落地页第x集的scheme 或者 为短剧底bar scheme
        },
        "incessantModel":{
            "type":"new",  //default：兜底，new：最新
            "title":"我不是神医", //标题
            "sequence":1, //第X集
            "img": "", // 背景图
            "scheme":"" //跳转地址 合计落地页第x集的scheme 或者 为短剧底bar scheme
        },
        "historyModel":{
            "type":"new",  //default：兜底，new：最新
            "title":"我不是神医", //标题
            "sequence":1, //第X集
            "img": "", // 背景图
            "scheme":"" //跳转地址 合计落地页第x集的scheme 或者 为短剧底bar scheme
        },
        "hotlist":{
            "scheme":"", //底bar热榜 免费榜的scheme
            "data":[{
                "title":"阴阳先生", //标题
                "scheme":"", //跳转地址 合计落地页第x集的scheme
            }]
        }
    }
}
```
#### 4.1.2.3 scheme
|类型|场景|拼接规则|下发scheme|备注|
|-|-|-|-|-|
|短剧底bar|左上角 无用户数据兜底|原样下发|baiduboxlite://v11/appTab/select?item=video&params=%7B%22channel%22%3A%2213%22%2C%22pd%22%3A%22feed%22%2C%22refresh%22%3A%221%22%2C%22extRequest%22%3A%7B%22video_source%22%3A%22widget_duanju%22%7D%7D|不分端|
|短剧底bar next|合集落地页拼前缀 热榜免费榜scheme拼前缀|baiduboxlite://v11/appTab/select?item=video&params=%7B%22channel%22%3A%2213%22%2C%22pd%22%3A%22feed%22%2C%22refresh%22%3A%221%22%2C%22extRequest%22%3A%7B%22video_source%22%3A%22widget_duanju%22%7D%7D&next=|--|--|
|合集落地页|有用户数据(续看，更新，历史，热榜)|底bar-next+urlencode(合集落地页) 合集落地页开头用baiduboxlite|baiduboxlite://v11/appTab/select?item=video&params=%7B%22channel%22%3A%2213%22%2C%22pd%22%3A%22feed%22%2C%22refresh%22%3A%221%22%2C%22extRequest%22%3A%7B%22video_source%22%3A%22widget_duanju%22%7D%7D&next=baiduboxlite%3A%2F%2Fvideo%2FinvokeVideoDetail%3Fparams%3D%257B%2522vid%2522%253A%2522sv_5017307450866622239%2522%252C%2522pd%2522%253A%2522personal%2522%252C%2522tpl%2522%253A%2522flowcollection%2522%252C%2522title%2522%253A%2522%25E5%25BC%2580%25E5%25B1%2580%25E6%25B6%2588%25E8%25B4%25B9%25E4%25BA%2586%25E4%25B8%2580%25E4%25B8%25AA%25E4%25BA%25BF%2522%252C%2522page%2522%253A%2522collection_video_landing%2522%252C%2522ext%2522%253A%257B%2522needStatistic%2522%253A%25221%2522%252C%2522actionType%2522%253A%2522collection%2522%252C%2522pd%2522%253A%2522personal%2522%252C%2522collId%2522%253A%25228949428246486847267%2522%252C%2522resourceType%2522%253A%2522miniVideo%2522%252C%2522videoWidth%2522%253A%2522480%2522%252C%2522videoHeight%2522%253A%2522854%2522%252C%2522collectionPanel%2522%253A%25220%2522%257D%252C%2522nid%2522%253A%2522sv_sv_5017307450866622239%2522%252C%2522from%2522%253A%2522feed%2522%252C%2522extRequest%2522%253A%257B%2522collection_nid_src%2522%253A%2522sv_5017307450866622239%2522%252C%2522authorCollId%2522%253A%2522sv_8949428246486847267%2522%252C%2522resourceType%2522%253A%2522miniVideo%2522%252C%2522is_microvideo%2522%253A%25220%2522%257D%252C%2522extLog%2522%253A%257B%2522pd%2522%253A%2522personal%2522%252C%2522sub_template%2522%253A%2522theatre_playlet%2522%257D%252C%2522first_id%2522%253A%2522%2522%252C%2522videoInfo%2522%253A%257B%2522title%2522%253A%2522%25E5%25BC%2580%25E5%25B1%2580%25E6%25B6%2588%25E8%25B4%25B9%25E4%25BA%2586%25E4%25B8%2580%25E4%25B8%25AA%25E4%25BA%25BF%2522%252C%2522posterImage%2522%253A%2522%2522%252C%2522vid%2522%253A%25228949428246486847267%2522%252C%2522duration%2522%253A131%252C%2522page%2522%253A%2522video_landing%2522%252C%2522pageUrl%2522%253A%2522https%253A%252F%252Fsv.baidu.com%252Fvideoui%252Fpage%252Fvideoland%253Fcontext%253D%25257B%252522nid%252522%25253A%252522sv_sv_5017307450866622239%252522%25252C%252522sourceFrom%252522%25253A%252522bjh%252522%25257D%2522%252C%2522ext_log%2522%253A%257B%2522vType%2522%253A4%252C%2522tab%2522%253A%2522%2522%252C%2522mtNew%2522%253A%2522rn%2522%252C%2522duration%2522%253A131%252C%2522authorID%2522%253A%25221800557714669324%2522%252C%2522pd%2522%253A%2522personal%2522%252C%2522mt%2522%253A1%252C%2522searchID%2522%253A%2522d0bf91370cbaa737%2522%252C%2522pdRec%2522%253A%2522personal%2522%252C%2522is_microvideo%2522%253A%25220%2522%252C%2522is_microvideo_src%2522%253A%25220%2522%252C%2522nid_src%2522%253A%2522sv_5017307450866622239%2522%252C%2522locid%2522%253A%2522http%253A%252F%252Fwww.internal.video.baidu.com%252F41932e989335c8f574be8038df8841a1.html%2522%257D%252C%2522clarityUrl%2522%253A%255B%257B%2522key%2522%253A%2522sd%2522%252C%2522rank%2522%253A0%252C%2522title%2522%253A%2522%25E6%25A0%2587%25E6%25B8%2585%2522%252C%2522url%2522%253A%2522http%253A%252F%252Fvd2.bdstatic.com%252Fmda-qgpc6x0jwaxj7qzp%252F360p%252Fh264_cae%252F1721810263591584960%252Fmda-qgpc6x0jwaxj7qzp.mp4%2522%252C%2522videoBps%2522%253A783%252C%2522vodVideoHW%2522%253A%2522854%2524%2524480%2522%252C%2522videoSize%2522%253A12.5%252C%2522download_url%2522%253A%2522%2522%257D%255D%252C%2522poster%2522%253A%2522https%253A%252F%252Fpic.rmb.bdstatic.com%252Fbjh%252Fvideo%252Ffff9735b9a82fe46130b6a0b0d1e49dc.jpeg%2522%252C%2522resourceType%2522%253A%2522miniVideo%2522%252C%2522from%2522%253A%2522feed%2522%252C%2522ext%2522%253A%257B%2522preview_6s_url%2522%253A%2522%2522%257D%257D%257D||
|热榜免费榜(联调用)|右上角|底bar-next+urlencode(热榜scheme) 热榜scheme(短剧用) baiduboxlite://talos/invokeTalosPage?bizparams=%7B%22boardTabList%22%3A%5B%22free_top%22%2C%22limit_top%22%5D%2C%22extRequest%22%3A%7B%22shortplay_source%22%3A%22feed%22%2C%22sub_template%22%3A%22list_ranking%22%2C%22tab_id%22%3A%22%22%7D%2C%22from%22%3A%22feed%22%2C%22initTab%22%3A%221%22%2C%22isPlaylet%22%3A%221%22%2C%22name%22%3A%22hot%22%2C%22page%22%3A%22widget%22%2C%22pd%22%3A%22feed%22%2C%22source%22%3A%22widget%22%7D&startparams=%7B%22bundleName%22%3A%22FeedSnVideoTheater%22%2C%22mainBizName%22%3A%22box.rnplugin.feedvideo%22%2C%22moduleName%22%3A%22FeedSnVideoTheater%22%2C%22subBizName%22%3A%22FeedSnVideoTheater%22%7D|baiduboxlite://v11/appTab/select?item=video&params=%7B%22channel%22%3A%2213%22%2C%22pd%22%3A%22feed%22%2C%22refresh%22%3A%221%22%2C%22extRequest%22%3A%7B%22video_source%22%3A%22widget_duanju%22%7D%7D&next=baiduboxlite%3A%2F%2Ftalos%2FinvokeTalosPage%3Fbizparams%3D%257B%2522boardTabList%2522%253A%255B%2522free_top%2522%252C%2522limit_top%2522%255D%252C%2522extRequest%2522%253A%257B%2522shortplay_source%2522%253A%2522feed%2522%252C%2522sub_template%2522%253A%2522list_ranking%2522%252C%2522tab_id%2522%253A%2522%2522%257D%252C%2522from%2522%253A%2522feed%2522%252C%2522initTab%2522%253A%25221%2522%252C%2522isPlaylet%2522%253A%25221%2522%252C%2522name%2522%253A%2522hot%2522%252C%2522page%2522%253A%2522widget%2522%252C%2522pd%2522%253A%2522feed%2522%252C%2522source%2522%253A%2522widget%2522%257D%26startparams%3D%257B%2522bundleName%2522%253A%2522FeedSnVideoTheater%2522%252C%2522mainBizName%2522%253A%2522box.rnplugin.feedvideo%2522%252C%2522moduleName%2522%253A%2522FeedSnVideoTheater%2522%252C%2522subBizName%2522%253A%2522FeedSnVideoTheater%2522%257D|不分端 正式链接需要pm申请|
### 4.1.3 脚本
[流程图]
## 4.2 存储设计
### 4.2.1 GCP
```
{
    "common":{
        "landScheme":"" //合集落地页scheme前缀
    }
    "xukan":{    //续看
        "img":"",
        "scheme":""    // 短剧底barscheme
    },
    "update":{    //我得更新
        "img":"",
        "scheme":"" // 短剧底barscheme
    },
    "history":{   //历史
       "img":"",
       "scheme":"" // 短剧底barscheme
    },
    "hotlist":{
        "scheme":"" //短剧底bar 热榜免费榜 scheme
    }
}
```
静默添加开关gcp：

* 线下：[http://ccs-offline.bcc-bdbl.baidu.com:8080/gcp-platform/index#/app/46/config/8642](http://ccs-offline.bcc-bdbl.baidu.com:8080/gcp-platform/index#/app/46/config/8642)
widget配置gcp: 

* 线下：[http://ccs-offline.bcc-bdbl.baidu.com:8080/gcp-platform/index#/app/46/config/8611](http://ccs-offline.bcc-bdbl.baidu.com:8080/gcp-platform/index#/app/46/config/8611)
### 4.2.2 数据库
```
# 用户短剧历史表
CREATE TABLE `playlet_user_push_history` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'auto id',
  `nid` varchar(64) NOT NULL DEFAULT '' COMMENT '短剧子集id',
  `reason` varchar(16) NoT NULL DEFAULT '' COMMENT '续看：xukan，更新：gengxin'
  `cuid` varchar(64)  NOT NULL DEFAULT '' COMMENT '用户cuid',
  `event_day` varchar(16) NOT NULL DEFAULT '0' COMMENT '日期',
  `status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE  CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='短剧用户推送历史'


## 测试数据
insert into playlet_user_push_history(`nid`,`reason`,`cuid`,`event_day`) values('4984705977635185686','gengxin','5F796C292EF7A59FDCDFA9C34838BA7F4C423A061FSAFJTNMAB','20241120'),
('4207611407238234609','xukan','5F796C292EF7A59FDCDFA9C34838BA7F4C423A061FSAFJTNMAB','20241120'),
('4778472608848239935','gengxin','C683D57BCFD60C9324CEE5278BBAEECA|VXEEWDM4I','20241120'),
('4804770551997287750','xukan','C683D57BCFD60C9324CEE5278BBAEECA|VXEEWDM4I','20241120'),
('4718247924551406653','gengxin','921CAB681A8FA6B7AB061EABF8630D6A3E015E138OSSIMAOCKL','20241120'),
('3995747551079508659','xukan','921CAB681A8FA6B7AB061EABF8630D6A3E015E138OSSIMAOCKL','20241120'),
('4185767590107954603','gengxin','18214EEC5202AB22E05EB3AC94DC127D|VNWPNR4KK','20241120'),
('4984705977635185686','xukan','18214EEC5202AB22E05EB3AC94DC127D|VNWPNR4KK','20241120'),
('4606886526656196587','gengxin','3E522287F1F24D25D82E5002D66D2A70B8F32BFAEFLFJECCJLR','20241120'),
('5621057811453552908','xukan','3E522287F1F24D25D82E5002D66D2A70B8F32BFAEFLFJECCJLR','20241120'),
('4771117893801917850','gengxin','CC1A357A77BA0AC3694705247818FF7832658B3B6FLEQQTOMPQ','20241120'),
('4072203990544006072','xukan','CC1A357A77BA0AC3694705247818FF7832658B3B6FLEQQTOMPQ','20241120'),
('5750028287655848468','gengxin','1FD2355DE46E8F782725A01E9F0E92A4|0','20241120'),
('4589319891382736842','xukan','1FD2355DE46E8F782725A01E9F0E92A4|0','20241120'),
('4922958005915295869','gengxin','86D1AE87509CAEBD896424207EB5E3A1679661116OIPOOHTFGR','20241120'),
('5535776373805837933','xukan','86D1AE87509CAEBD896424207EB5E3A1679661116OIPOOHTFGR','20241120'),
('4888181505608329323','gengxin','7ED7EF4CA00EFE18A4BD1FCB78F00|V4UKKFZDT','20241120'),
('4977687146349675196','xukan','7ED7EF4CA00EFE18A4BD1FCB78F00|V4UKKFZDT','20241120'),
('2471758382462282969','gengxin','F1F694E2C62B19F9A355337F6D70B217|VWSXPWBUR','20241120'),
('4663818121869670259','xukan','F1F694E2C62B19F9A355337F6D70B217|VWSXPWBUR','20241120'),
('5017930088003365896','gengxin','1E8AB5082FBA2A7FF733B60E30638B1D9BECC813DOBADCEMJTO','20241120'),
('5750028287655848468','xukan','1E8AB5082FBA2A7FF733B60E30638B1D9BECC813DOBADCEMJTO','20241120')


```
# 5 测试场景
## 5.1 silentaddlite接口
**命中条件：appver>=6.39 sid 有地域屏蔽**

**openwidgetid: 212378996573258**

|场景|子场景|期待表现|server表现|
|-|-|-|-|
|mock旧版本/ios等兼容 |target不携带 212378996573258|不下发212378996573258|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3c770893aaa24aa2b8dca4b2b7fb7b3f&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2104957beca44602a5d587c53f313f2b&docGuid=MRi0VcvICjS6lu "") done|
|用户已有静默安装|add里有未删除的静默widget|不下发任何，return unkonw|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0f96a5216e214333be7bb2757251999f&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3a93f9ea78c445cf9b25265e6e33b1c4&docGuid=MRi0VcvICjS6lu "") done|
|用户没有默认安装|target不携带2x|不下发2x|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=30e7d436e7d344cfaa18413e594b031c&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ae811c8d76ce47709cec984e8cd67f94&docGuid=MRi0VcvICjS6lu "") done|
||target携带2x version>=|下发2x|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=29c1f0a98b4848babb26c756ab02a670&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7abf7a8d96a34457af285df9b1691f94&docGuid=MRi0VcvICjS6lu "") done|
||target携带2x version<|不下发2x|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=461bd879b4f54808a4117fc076d7b553&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ef2804563ba4f87ac8b61a14f829075&docGuid=MRi0VcvICjS6lu "") done|
||target携带2x added携带2x，未删除 version>=|不下发2x|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=eae062542af14686881bfb21af911f7e&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3837de9d222347c38bff641091ed5361&docGuid=MRi0VcvICjS6lu "") done|
||target携带2x added携带2x，已删除 version>=|不下发2x|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3d5fa72a94594bfc84b7f99ee8ac6860&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f3f2176556304af389f255bf7dc2b82c&docGuid=MRi0VcvICjS6lu "") done|
||target携带2x version>= 但有其他优先级更高的target|不下发2x 下发高优先级|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1a4bb987c804418990c7429546a68f3b&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=941b6ff0476a40c59925dda8ec1b2011&docGuid=MRi0VcvICjS6lu "") done|
||target携带2x version>= 地域屏蔽cuid|不下发2x|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3874cbd033bb49aa9d3318863080ea3f&docGuid=MRi0VcvICjS6lu "") done|
## 5.2 widgetdetail接口
|场景|子场景|期待表现|server表现|
|-|-|-|-|
|与搜索proxy联调|携带cookie|能解析出cuid|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=db374b67dc694a8c9845437d5f7ff79a&docGuid=MRi0VcvICjS6lu "") done|
||携带参数正常|下发数据正常|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=15fe4d41eabe4ee182dca22ae9e46c94&docGuid=MRi0VcvICjS6lu "") done|
|我的更新模块|数据为空|下发兜底|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc1342f0c3c1454692ee5f89891c8f4b&docGuid=MRi0VcvICjS6lu "") done|
||数据正常|下发对应短剧物料|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=056d671c0fc949678c6188ba10087c90&docGuid=MRi0VcvICjS6lu "") done|
|我的续看模块|数据为空|下发兜底|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e95f08d15605408aaf76cea81e4f94f3&docGuid=MRi0VcvICjS6lu "") done|
||数据正常|下发对应短剧物料|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9ebb5f32e85a491990d7b013575cd004&docGuid=MRi0VcvICjS6lu "") done|
|我的历史模块|携带历史数据为空|下发兜底|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d96d915abf5d49339230334c9e221a4f&docGuid=MRi0VcvICjS6lu "") done|
||历史数据不为空--有非重复数据|下发和更新&续看不重复的一条|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=41c67416d21c4b9db42534e949525da7&docGuid=MRi0VcvICjS6lu "") done|
||历史数据不为空--重复数据|下发历史第一条|"incessantModel":{"nid":"9169015662584649386"}} {"historyData":[{"setId":"8949428246486847267","nid":"sv_9169015662584649386","watchSequence":11}]} ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d8340ac9a1f148a0b9bcfc402f4fb184&docGuid=MRi0VcvICjS6lu "") done|
|热榜|数据为空|下发兜底|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7c4873209d0f454f835ba7f5a20ba8c4&docGuid=MRi0VcvICjS6lu "") 强制数据为空 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d457347258de482e891bf2379f8b0375&docGuid=MRi0VcvICjS6lu "") done|
||数据正常--够3条|下发对应短剧物料|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8a803ad0934046d6bb8554ad2e40b833&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=05498c5755ed4c3f830d73d7919602e1&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac4f394e656f4a93826ce80008a53d3e&docGuid=MRi0VcvICjS6lu "") done|
||数据正常--不够3条|下发对应短剧物料 不足兜底补齐|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6a4358615aed459c8478a5fc17503586&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=281c9aa5ff3a4f6a932c6cab51c3433a&docGuid=MRi0VcvICjS6lu "") done|
|兜底场景|模拟下游接口error|下发兜底物料|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d8a640312bb944c2aea6256e9e5df49c&docGuid=MRi0VcvICjS6lu "") mock error ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=022884e0b6574384a56a2ba2f4e139f6&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=eb4d454c11764d0a81f2d958e86821f1&docGuid=MRi0VcvICjS6lu "") 返回兜底 done|
|数据校验|链接是否和nid对应 跳转是否正常|热榜|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8a803ad0934046d6bb8554ad2e40b833&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=05498c5755ed4c3f830d73d7919602e1&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac4f394e656f4a93826ce80008a53d3e&docGuid=MRi0VcvICjS6lu "") 热榜前三 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=01aa77dbc70447b286de12bcc94ac5a1&docGuid=MRi0VcvICjS6lu "") 顺序正常，热榜scheme正常  ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fb9fc4eef7d14d7dbd11c90f928f8c1d&docGuid=MRi0VcvICjS6lu "") 进合集落地页正常 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=74fce89821d446909565cebc2df70179&docGuid=MRi0VcvICjS6lu "") back回底bar正常 done|
|||续看|"incessantModel":{"nid":"3931292186488115840"} ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=705e7593e71a41a080333b6573754d34&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=20302f58f1f244f88e1c4e5c545cb75a&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7ff8c39f152f43849144b9b3669c8888&docGuid=MRi0VcvICjS6lu "") done|
|||更新|"updateModel":{"nid":"5246297570866006123"} ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e461009a98f14495b7f2071a50fdf57d&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=162a067d173047b8be8c7e2af670d5cc&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=77da0c8bfc6b40e686f9489f7b2441bd&docGuid=MRi0VcvICjS6lu "") done|
|||历史|his: [{9547468937562488367 sv_4611530927918348481 1}] ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cef3ddae9afb481b98892173d8e936e8&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c5811c69117045659ef5d8743f1f6e50&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c6e4545ed5ee4723be412ee3584d3707&docGuid=MRi0VcvICjS6lu "") done|
|||免费榜scheme|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=edcedc49cd6d475181ed674acfe62c6f&docGuid=MRi0VcvICjS6lu "") done|
|||底bar scheme|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0e3fd28c52ca4fef872b95c088c98692&docGuid=MRi0VcvICjS6lu "") done|
# 流量预估
widget总体吊起量级PV 1w，QPS 个位数，集群可控

# 上线流程
1. DB 表上线--done
2. GCP配置上线
* widget-switch，widget-conf [http://ccs.baidu-int.com/gcp-platform/index#/app/46/config/7613/check](http://ccs.baidu-int.com/gcp-platform/index#/app/46/config/7613/check) [http://ccs.baidu-int.com/gcp-platform/index#/app/46/config/7612/check](http://ccs.baidu-int.com/gcp-platform/index#/app/46/config/7612/check) --done
* 热榜scheme找pm要正式环境的--done
3. 代码上线--done
* 确认opendwidget线上id--done
## 预览回归
### silentaddlite
|场景|server表现|
|-|-|
|有其他优先级|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=708f870f507b47608b94788b34647bd4&docGuid=MRi0VcvICjS6lu "") done|
|无其他优先级，但appver不满足|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=557dd02bbcc84db9a8c7a9f07c72ac98&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=662b069a0f7c47fda6d72a1b237f88c4&docGuid=MRi0VcvICjS6lu "") done|
|无其他优先级，appver满足|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fdf2421525fb49ed8aae085807eb1c9a&docGuid=MRi0VcvICjS6lu "") done|
|有added|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7900708387584640902ba1aa2a7d0c06&docGuid=MRi0VcvICjS6lu "") done|
|安装过又删除|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5f7ed73157df451eb9c8ad990f3858e4&docGuid=MRi0VcvICjS6lu "") done|
|地域屏蔽 |![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3552093daa374b63866b9e516b435883&docGuid=MRi0VcvICjS6lu "") done|
### widgetdetail
|场景|子场景|期待表现|server表现|
|-|-|-|-|
|与搜索proxy联调|携带cookie|能解析出cuid|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ddd8e7a0a09249bfb46032070a856829&docGuid=MRi0VcvICjS6lu "") done|
||携带参数正常|下发数据正常|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=48d490fc521a498abbe121204d228f25&docGuid=MRi0VcvICjS6lu "") done|
|我的更新模块|数据为空|下发兜底|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0fdb33ac0213497a9bb9aa902bd96ea4&docGuid=MRi0VcvICjS6lu "") done|
||数据正常|下发对应短剧物料|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=830c7f5c5659460a999a56b58b19509c&docGuid=MRi0VcvICjS6lu "") done|
|我的续看模块|数据为空|下发兜底|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ebbdd519f7fd4357906896f16cbc60f4&docGuid=MRi0VcvICjS6lu "") done|
||数据正常|下发对应短剧物料|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aed378a946e94e2390a5d0cb74c4add5&docGuid=MRi0VcvICjS6lu "") done|
|我的历史模块|携带历史数据为空|下发兜底|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a7cdfbec6f1c4a93861a24a5c40e8c90&docGuid=MRi0VcvICjS6lu "") done|
||历史数据不为空--有非重复数据|下发和更新&续看不重复的一条|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b5937e16c1224d2586d89869f873d260&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=55b6c0328c8a40a8976588bf939e3165&docGuid=MRi0VcvICjS6lu "") 第一条历史和update重复 下发第二条 done|
||历史数据不为空--重复数据|下发历史第一条|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d1bde83ff6a144918bf4b0fdac8be746&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7875448b434e40dd906d7b23976583be&docGuid=MRi0VcvICjS6lu "") done|
|热榜|数据正常|下发对应短剧物料|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e51bdac728d04e61b2c8f818259acf69&docGuid=MRi0VcvICjS6lu "") done|
|数据校验|链接是否和nid对应 跳转是否正常|widget样式|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=665b56533758488e91d1fc1195b63321&docGuid=MRi0VcvICjS6lu "")  ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=76ca4a2006874890ba58cf61f5c5b67a&docGuid=MRi0VcvICjS6lu "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=49802bcdadfc4d76a15aeefbaf12441f&docGuid=MRi0VcvICjS6lu "") done|
|||热榜|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc6b152772d94228a1cbf1f980453135&docGuid=MRi0VcvICjS6lu "") done|
|||续看|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0ce6ec9ce16e443fa7c2b0dd75eb7c7b&docGuid=MRi0VcvICjS6lu "") done|
|||更新|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=513cd081af214b08bf3c98a830543590&docGuid=MRi0VcvICjS6lu "") done|
|||历史|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9e72934a4f9646aaa9b61fb37fcf16dd&docGuid=MRi0VcvICjS6lu "") done|
|||免费榜scheme|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ae5f784cf6ae41529bbf9311b775bd87&docGuid=MRi0VcvICjS6lu "") done|
|||底bar scheme|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=352d43afaf9e4f6280a91b449939664f&docGuid=MRi0VcvICjS6lu "") done|









