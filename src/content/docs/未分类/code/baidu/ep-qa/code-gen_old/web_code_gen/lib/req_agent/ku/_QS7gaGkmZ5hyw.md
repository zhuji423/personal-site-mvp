---
title: "1  项目详情"
description: "【非随】影视频道一级页优化"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\lib\\req_agent\\ku\\_QS7gaGkmZ5hyw.md"
---
【非随】影视频道一级页优化

# 1  项目详情
**MRD**

[[ailite-28617] 【非随】影视频道一级页优化](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-28617/show?source=copy-shortcut?t=mention&mt=doc&dt=sdk)

# 2 需求
**背景**

一期数据背景[极速版影视频道数据分析](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/uXaL-WkWdt/fqVp4suxR9/YRsXpYGv74RMqW?t=mention&mt=doc&dt=doc)：影视频道一期上线后，搜索影视垂类规模和体验指标正向显著，影视搜索pv+0.71%（节前SA回搜pv+3w/日，春节SA回搜pv+3.5w/日； 预计推全后频道pv+3.8w/日），搜索影视uv+0.99%，搜索影视活跃度+0.87%，影视有满意消费pv+0.57%；但搜索大盘、整体端/feed规模、时长趋于持平，仍有优化空间

频道有点渗透16%（对比短剧频道有点渗透23%），**点击率需提升**

**收益**

1. 提升点击率：现状16%，预估提升至 20%+
2. 提升时长：影视总时长+5.7万分钟（=11wUV*4%*13min有点用户人均时长）
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4bc3e501bb7b404fac2d5067403032f5&docGuid=_QS7gaGkmZ5hyw "")
# 3 沟通地图
## 内部
|    角色|    接口人|备注|
|-|-|-|
|   PM|     @王琪||
|   SRD|   @潘超毅 ||
|FE|    @唐豪健||
|SQA|    @董美雪||
|CRQ|@孙广威||
## 模块拆分
|接口内容|备注|
|-|-|
|影视频道首页||
|影视推荐分类列表||
整体时间暂定

开发：3pd （12.17-12.19）

联调：

提测：

测试：

上线：

### 搜索接口文档
[影视频道数据查询](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MYFIkxNl2o/ZCDp8kUOFE/G_08V1IYG1t0Wc?t=mention&mt=doc&dt=doc)

[影视历史记录查询](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MYFIkxNl2o/ZCDp8kUOFE/38fgK8poF9zUlZ?t=mention&mt=doc&dt=doc)



### 接口文档
1. **影视频道首页**
接口地址：/baiduboxapp/basic/movieChannel/home

请求类型：GET

参数：公参&cookie

结果返回：

```
{
	"data":{
        "diamond":[{
            "name":"我的下载", //名称
            "icon":"xxxx",  // 图标icon
            "scheme":"xxxx" //跳转scheme
            "clickType":"yingshi_jingang_1" //* yingshi_jingang_1（我的下载）* yingshi_jingang_2（我的收藏）* yingshi_jingang_3（影视片库）* yingshi_jingang_4（我的网盘）
        },{
            "name":"我的下载",
            "icon":"xxxx", 
            "scheme":"xxxx" //跳转scheme
            "clickType":"yingshi_jingang_2" //
        }],
        "history":{           //历史记录
            "list":[{
                "name":"角斗士2",     //名称
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                    //封面图
                "recommendWords": ["神枪手瓦西里vs康尼"], //推荐词
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], //主演名称
                "tags":["剧情","冒险","动作","探险"], //剧情tag
                "watchProcess": "已观看至41%", //观看进度
                "scheme":"xxx", //跳转scheme   
                "publishTime": "2023-04-28",    //发布时间
                "type":"history" //类型 history:历史, recommend:推荐
            },{
                "name":"角斗士2",     
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                  
                "recommendWords": ["神枪手瓦西里vs康尼"],
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], 
                "tags":["剧情","冒险","动作","探险"], 
                "scheme":"xxx", //跳转scheme 
                "publishTime": "2023-04-28", 
                "type":"recommend"
            }],
            "moduleScheme":"xx" //完整榜单的跳转scheme
        }
        "television":{             //电视剧热榜
            "list":[{
                "name":"角斗士2",     //名称
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                    //封面图
                "recommendWords": ["神枪手瓦西里vs康尼"], //推荐词
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], //主演名称
                "tags":["剧情","冒险","动作","探险"], //剧情tag
                "socre":"6.6", //分数    
                "publishTime": "2023-04-28",    //发布时间
                "scheme":"xxx", //跳转scheme 
                //-----------新增-----------------
                "hotValue":"2323", //热度值
                "flag":"" //左上角标识
            },{
                "name":"角斗士2",     
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                  
                "recommendWords": ["神枪手瓦西里vs康尼"],
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], 
                "tags":["剧情","冒险","动作","探险"],  
                "publishTime": "2023-04-28",    //发布时间
                "scheme":"xxx", //跳转scheme 
                //-----------新增-----------------
                "hotValue":"2323", //热度值
                "flag":"" //左上角标识
            }],
            "moduleScheme":"xx" //完整榜单的跳转scheme
        },
        "movie":{            //电影热榜
            "list":[{
                "name":"角斗士2",     //名称
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                    //封面图
                "recommendWords": ["神枪手瓦西里vs康尼"],
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], //主演名称
                "tags":["剧情","冒险","动作","探险"], //剧情tag
                "publishTime": "2023-04-28",    //发布时间
                "scheme":"xxx", //跳转scheme
                //-----------新增-----------------
                "hotValue":"2323", //热度值
                 "flag":"" //左上角标识
            },{
                "name":"角斗士2",     
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                  
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], 
                "tags":["剧情","冒险","动作","探险"],
                "publishTime": "2023-04-28",    //发布时间 
                "scheme":"xxx", //跳转scheme
                //-----------新增-----------------
                "hotValue":"2323", //热度值
                 "flag":"" //左上角标识
            }],
            "moduleScheme":"xx" //完整榜单的跳转scheme
        },
        "recommend":{
            "moduleScheme":"xx" //更多推荐的跳转scheme
            "categoryList":[{
                "id":2,
                "name":"电视剧"
            },{
                 "id":1,
                 "name":"电影"
            },{
                 "id":3,
                 "name":"综艺"
            },{
                 "id":4,
                 "name":"动漫"
            },{
                 "id":7,
                 "name":"纪录片"
            }],
            "list":[{
                    "name":"角斗士2",     
                    "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                  
                    "recommendWords": ["神枪手瓦西里vs康尼"],
                    "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], 
                    "tags":["剧情","冒险","动作","探险"],
                    "publishTime": "2023-04-28",    //发布时间  
                    "scheme":"xxx"
             }]
        }
    }
}
```
2. **影视频道推荐分类列表**
接口地址：/baiduboxapp/basic/movieChannel/recommend

请求类型：GET

参数：公参&cookie

|   参数名|  类型| 含义|
|-|-|-|
|id| int|推荐类型id|
|pageNum|int|页码（第一页从0开始）|
|historyRecNum|int|历史记录中-推荐的数量|
结果返回：

```
{
    "data":{
            "categoryList":[{
                "id":2,
                "name":"电视剧"
            },{
                 "id":1,
                 "name":"电影"
            },{
                 "id":3,
                 "name":"综艺"
            },{
                 "id":4,
                 "name":"动漫"
            },{
                 "id":7,
                 "name":"综艺"
            }],
            "list":[{
                    "name":"角斗士2",     
                    "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                  
                    "recommendWords": ["神枪手瓦西里vs康尼"],
                    "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], 
                    "tags":["剧情","冒险","动作","探险"],  
                    "scheme":"xxx", //跳转scheme 
                    "hotValue":"343434" //热度值----新增
            }],
            "moduleScheme":"xx" //更多推荐的跳转scheme
        }
}
```
# 4 详细设计
**金刚位**：金刚位下线，配置GCP金刚位diamond 字段值为0

**历史**：根据历史最新的历史记录获取tag，从电视剧榜单获取同类型的tag，并且与电视榜去重

**推荐**：

* 电视剧、电影 固定从下游结果第4位取
* 热度值：从gcp获取y值，对比下游的x值（从下游列表字段获取），计算热度值
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cd5bb997fc294127b548cbf7393ee902&docGuid=_QS7gaGkmZ5hyw "")
**电视剧/电影榜单**：

* 电视剧从下游结果列表第一位取
* 热度值：从gcp获取y值，对比下游的x值（从下游列表字段new_hot_value获取），计算热度值
* 评分：从gcp获取y值，对比下游的x值（从下游列表字段douban_score获取），计算评分
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=98e31a2d3ff1442a93da9f0ad61522eb&docGuid=_QS7gaGkmZ5hyw "")
**搜索结果页query：**

  * 实验组1：XXX 电视剧 在线观看
  * 实验组2：XXX 电视剧
  * 对照组：  XXX 电视剧 免费看
## 流程图
[流程图]
## 4.2 存储设计
### 4.2.1 GCP
```
key：movie_channel_rule

{
    // 榜单
    "hotList":{
        "hotValue":{        //热度值
            "max":30000,
            "min":20000
        },
        "socreVaule":{      //分数值
            "max":30000,
            "min":20000
        }
    },
    // 推荐
    "recommend":{
        "hotValue":{        //热度值
            "max":30000,
            "min":20000,
            "compare":1000000 //比较的值
        }
    }
}
```




# 上线流程
1. GCP配置上线
2. 代码上线（sbox-basic）