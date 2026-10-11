---
title: "1  项目详情"
description: "https://www.figma.com/design/mA092k15UJC41hwJHcWmtB/%E3%80%90%E8%A7%86%E8%A7%89%E6%A0%87%E6%B3%A8%E3%80%91%E6%9E%81%E9%8"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\lib\\req_agent\\ku\\VcYhvKGG7kMq2W.md"
---
极速版影视频道

# 1  项目详情
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0ebeb334451e4891868745eb33b3e207&docGuid=VcYhvKGG7kMq2W "")
**设计图稿**

[https://www.figma.com/design/mA092k15UJC41hwJHcWmtB/%E3%80%90%E8%A7%86%E8%A7%89%E6%A0%87%E6%B3%A8%E3%80%91%E6%9E%81%E9%80%9F%E7%89%88%E5%BD%B1%E8%A7%86%E9%A2%91%E9%81%93?node-id=0-1&p=f&t=tdgGUKQFnYVyx6xc-0](https://www.figma.com/design/mA092k15UJC41hwJHcWmtB/%E3%80%90%E8%A7%86%E8%A7%89%E6%A0%87%E6%B3%A8%E3%80%91%E6%9E%81%E9%80%9F%E7%89%88%E5%BD%B1%E8%A7%86%E9%A2%91%E9%81%93?node-id=0-1&p=f&t=tdgGUKQFnYVyx6xc-0)

**MRD**

[[ailite-27808] 【非随】极速版影视频道](https://console.cloud.baidu-int.com/devops/icafe/issue/ailite-27808/show?source=drawer-header?t=mention&mt=doc&dt=sdk)

# 2 需求背景
极速版打造“免费看”心智，提升影视资源消费渗透和全链路体验，需要新建独立的影视频道场域，希望打造一站式影视看搜心智

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

开发：5pd（1.8-1.14）

联调：3pd（1.15-1.17）

提测：1.17

测试：1.20-1.21

上线：1.22

### 搜索接口文档
[影视频道数据查询](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MYFIkxNl2o/ZCDp8kUOFE/G_08V1IYG1t0Wc?t=mention&mt=doc&dt=doc)

[影视历史记录查询](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MYFIkxNl2o/ZCDp8kUOFE/38fgK8poF9zUlZ?t=mention&mt=doc&dt=doc)

### 配置文档
[极速版影视频道shceme](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/Zb2Pr-3Cwi/f2k21intVxYBkl?t=mention&mt=doc&dt=doc)

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
                "scheme":"xxx" //跳转scheme 
            },{
                "name":"角斗士2",     
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                  
                "recommendWords": ["神枪手瓦西里vs康尼"],
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], 
                "tags":["剧情","冒险","动作","探险"],  
                "publishTime": "2023-04-28",    //发布时间
                "scheme":"xxx" //跳转scheme 
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
                "scheme":"xxx" //跳转scheme 
            },{
                "name":"角斗士2",     
                "poster":"http://t12.baidu.com/it/u=180566760,3490304975&fm=58&app=83&f=JPEG?w=400&h=533",                  
                "starring":["保罗·麦斯卡","佩德罗·帕斯卡","丹泽尔·华盛顿","康妮·尼尔森"], 
                "tags":["剧情","冒险","动作","探险"],
                "publishTime": "2023-04-28",    //发布时间 
                "scheme":"xxx" //跳转scheme 
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
                    "scheme":"xxx" //跳转scheme 
            }],
            "moduleScheme":"xx" //更多推荐的跳转scheme
        }
}
```
3. **影视频道历史列表**
接口地址：/baiduboxapp/basic/movieChannel/history

请求类型：GET

参数：公参&cookie

请求时机：返回首页时更新历史数据

结果返回：

```
{
    "data":{
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
```
# 
# 4 详细设计
## 4.1 流程图
[流程图]


## 4.2 存储设计
### 4.2.1 GCP
```
key : movie_channel_info
{
  "diamond": [
    {
      "name": "我的下载",
      "icon": "https://matrix-fe.cdn.bcebos.com/movie-channel/download2.png",
      "scheme": "baiduboxapp://v9/ucenter/downloadCenter",
      "clickType": "yingshi_jingang_1"
    },
    {
      "name": "我的收藏",
      "icon": "https://matrix-fe.cdn.bcebos.com/movie-channel/collect2.png",
      "scheme": "baiduboxapp://v14/favor/openFavor?params=%7B%22ubcSrc%22%3A%20%22yingshi_feedtab%22%2C%22classtification%22%3A%22search_web_video%22%7D",
      "clickType": "yingshi_jingang_2"
    },
    {
      "name": "影视片库",
      "icon": "https://matrix-fe.cdn.bcebos.com/movie-channel/film-library2.png",
      "scheme": "baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_8&sa=gh_speed_channel_movie_8&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%25E5%25BD%25B1%25E8%25A7%2586%25E4%25BD%259C%25E5%2593%2581%26title%3D%25E5%25BD%25B1%25E8%25A7%2586%25E7%2589%2587%25E5%25BA%2593%26resource_id%3D51274%26top%3D%257B%2522sfhs%2522%253A0%257D%26ms%3D1%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26ext%3D%257B%2522sf_tab_name%2522%253A%252B%25E7%2594%25B5%25E5%25BD%25B1%252B%257D%26stat0%3D%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%26frorder%3D1%26q_ext%3D%257B%2522video_type_list%2522%253A%255B%2522%25E7%2594%25B5%25E5%25BD%25B1%2522%252C%2522%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%2522%252C%2522%25E7%25BB%25BC%25E8%2589%25BA%2522%252C%2522%25E5%258A%25A8%25E6%25BC%25AB%2522%252C%2522%25E7%25BA%25AA%25E5%25BD%2595%25E7%2589%2587%2522%255D%257D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26sa%3Dgh_speed_channel_movie_8",
      "clickType": "yingshi_jingang_3"
    },
    {
      "name": "我的网盘",
      "icon": "https://matrix-fe.cdn.bcebos.com/movie-channel/netdisk2.png",
      "scheme": "baiduboxapp://swan/OyIvf6LYVhKkbIHS1USP7xnSKYxc36SH/pages/home/index?from=1026350x_1026350y&_baiduboxapp=%7B%22from%22%3A%221091001310001000%22%2C%22ext%22%3A%7B%7D%7D&callback=_bdbox_js_275&upgrade=0",
      "clickType": "yingshi_jingang_4"
    }
  ],
  "history": {
    "scheme": "https://m.baidu.com/ssid=a8b2d4c6b5adb7e7c7e166742689/s?word={name}{type}免费看&kg_sid={urlSign}&gh_speed_channel_movie_7",
    "topNum": 4,
    "moduleScheme": "baiduboxapp://history/openHistory?params=%7B%22ubcSrc%22%3A%20%22yingshi_feedtab%22%2C%22classtification%22%3A%22search_web_video%22%7D",
    "totalNum": 10,
    "imageType": "cover",
    "imagePrefix": "https://aladdin-movies.cdn.bcebos.com/nature/watch/screenshot/",
    "imageSuffix": ".png",
    "playSchemePrefix": "baiduboxlite://v1/browser/open?landingPageType=gh_speed_channel_movie_9&url="
  },
  "television": {
    "topNum": 3,
    "totalNum": 10,
    "moduleScheme": "baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_4&sa=gh_speed_channel_movie_4&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%25E7%2583%25AD%25E9%2597%25A8%25E6%25A6%259C%26ms%3D1%26title%3D%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%25E7%2583%25AD%25E9%2597%25A8%25E6%25A6%259C%26resource_id%3D51274%26dspName%3Diphone%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26sort_key%3D2%26stat0%3D%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%26stat1%3D%25E5%2585%25A8%25E9%2583%25A8%26stat2%3D%25E5%25A4%25A7%25E9%2599%2586%26stat3%3D%25E5%2585%25A8%25E9%2583%25A8%26q_ext%3D%257B%2522query_key%2522%253A3%252C%2522is_person_related%2522%253A0%252C%2522video_type_list%2522%253A%255B%255D%257D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26lid%3D9605529277435270874%26sa%3Dgh_speed_channel_movie_4",
    "scheme": "https://m.baidu.com/ssid=a8b2d4c6b5adb7e7c7e166742689/s?word={name} 电视剧 免费看&sa=gh_speed_channel_movie_1&kg_sid={urlSign}"
  },
  "recommend": {
    "moduleScheme": "baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_6&sa=gh_speed_channel_movie_6&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%25E5%25BD%25B1%25E8%25A7%2586%25E4%25BD%259C%25E5%2593%2581%26title%3D%25E5%25BD%25B1%25E8%25A7%2586%25E7%2589%2587%25E5%25BA%2593%26resource_id%3D51274%26top%3D%257B%2522sfhs%2522%253A0%257D%26ms%3D1%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26ext%3D%257B%2522sf_tab_name%2522%253A%252B%2525E7%252594%2525B5%2525E5%2525BD%2525B1%252B%257D%26stat0%3D%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%26frorder%3D1%26q_ext%3D%257B%2522video_type_list%2522%253A%255B%2522%25E7%2594%25B5%25E5%25BD%25B1%2522%252C%2522%25E7%2594%25B5%25E8%25A7%2586%25E5%2589%25A7%2522%252C%2522%25E7%25BB%25BC%25E8%2589%25BA%2522%252C%2522%25E5%258A%25A8%25E6%25BC%25AB%2522%252C%2522%25E7%25BA%25AA%25E5%25BD%2595%25E7%2589%2587%2522%255D%257D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26sa%3Dgh_speed_channel_movie_6",
    "scheme": "https://m.baidu.com/ssid=a8b2d4c6b5adb7e7c7e166742689/s?word={name}{type}免费看&sa=gh_speed_channel_movie_3&kg_sid={urlSign}"
  },
  "categoryList": [
    {
      "id": 2,
      "name": "电视剧"
    },
    {
      "id": 1,
      "name": "电影"
    },
    {
      "id": 3,
      "name": "综艺"
    },
    {
      "id": 4,
      "name": "动漫"
    },
    {
      "id": 7,
      "name": "纪录片"
    }
  ],
  "movie": {
    "scheme": "https://m.baidu.com/ssid=a8b2d4c6b5adb7e7c7e166742689/s?word={name} 电影 免费看&sa=gh_speed_channel_movie_2&kg_sid={urlSign}",
    "totalNum": 10,
    "topNum": 3,
    "moduleScheme": "baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_5&sa=gh_speed_channel_movie_5&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%25E7%2594%25B5%25E5%25BD%25B1%25E7%2583%25AD%25E9%2597%25A8%25E6%25A6%259C%26ms%3D1%26title%3D%25E7%2594%25B5%25E5%25BD%25B1%25E7%2583%25AD%25E9%2597%25A8%25E6%25A6%259C%26resource_id%3D51274%26dspName%3Diphone%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26sort_key%3D1%26stat0%3D%25E7%2594%25B5%25E5%25BD%25B1%26stat1%3D%25E5%2585%25A8%25E9%2583%25A8%26stat2%3D%25E5%25A4%25A7%25E9%2599%2586%26stat3%3D%25E5%2585%25A8%25E9%2583%25A8%26q_ext%3D%257B%2522query_key%2522%253A3%252C%2522is_person_related%2522%253A0%252C%2522video_type_list%2522%253A%255B%255D%257D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26lid%3D9605529277435270874%26sa%3Dgh_speed_channel_movie_5"
  },
  "basic": {
    "queryList": [
      {
        "id": 2,
        "name": "电视剧热门榜"
      },
      {
        "id": 1,
        "name": "电影热门榜"
      },
      {
        "id": 3,
        "name": "综艺"
      },
      {
        "id": 4,
        "name": "动漫"
      },
      {
        "id": 7,
        "name": "纪录片"
      }
    ]
  }
}
```


```
key : movie_channel_experiment
{
  "isDiamond": true,
  "isHistory": true,
  "isMovie": true,
  "isRecommend": true,
  "isTelevision": true,
  "isHistoryRec": true
}
```


# 跳转拼接
电视剧榜单

```
baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_4&sa=gh_speed_channel_movie_4&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%E7%94%B5%E8%A7%86%E5%89%A7%E7%83%AD%E9%97%A8%E6%A6%9C%26ms%3D1%26title%3D%E7%94%B5%E8%A7%86%E5%89%A7%E7%83%AD%E9%97%A8%E6%A6%9C%26resource_id%3D51274%26dspName%3Diphone%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26sort_key%3D1%26stat0%3D%E7%94%B5%E8%A7%86%E5%89%A7%26stat1%3D%E5%85%A8%E9%83%A8%26stat2%3D%E5%A4%A7%E9%99%86%26stat3%3D%E5%85%A8%E9%83%A8%26q_ext%3D%7B%22query_key%22%3A3%2C%22is_person_related%22%3A0%2C%22video_type_list%22%3A%5B%5D%7D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26lid%3D9605529277435270874%26sa%3Dgh_speed_channel_movie_4
```


电影榜单

```
baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_5&sa=gh_speed_channel_movie_5&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%E7%94%B5%E5%BD%B1%E5%89%A7%E7%83%AD%E9%97%A8%E6%A6%9C%26ms%3D1%26title%3D%E7%94%B5%E5%BD%B1%E7%83%AD%E9%97%A8%E6%A6%9C%26resource_id%3D51274%26dspName%3Diphone%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26sort_key%3D1%26stat0%3D%E7%94%B5%E5%BD%B1%26stat1%3D%E5%85%A8%E9%83%A8%26stat2%3D%E5%A4%A7%E9%99%86%26stat3%3D%E5%85%A8%E9%83%A8%26q_ext%3D%7B%22query_key%22%3A3%2C%22is_person_related%22%3A0%2C%22video_type_list%22%3A%5B%5D%7D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26lid%3D9605529277435270874%26sa%3Dgh_speed_channel_movie_5
```
推荐榜单

```
baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_6&sa=gh_speed_channel_movie_6&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%E5%BD%B1%E8%A7%86%E4%BD%9C%E5%93%81%26title%3D%E5%BD%B1%E8%A7%86%E7%89%87%E5%BA%93%26resource_id%3D51274%26top%3D%7B%22sfhs%22%3A0%7D%26ms%3D1%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26ext%3D%7B%22sf_tab_name%22%3A%2B%25E7%2594%25B5%25E5%25BD%25B1%2B%7D%26stat0%3D%E7%94%B5%E8%A7%86%E5%89%A7%26frorder%3D1%26q_ext%3D%7B%22video_type_list%22%3A%5B%22%E7%94%B5%E5%BD%B1%22%2C%22%E7%94%B5%E8%A7%86%E5%89%A7%22%2C%22%E7%BB%BC%E8%89%BA%22%2C%22%E5%8A%A8%E6%BC%AB%22%2C%22%E7%BA%AA%E5%BD%95%E7%89%87%22%5D%7D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26sa%3Dgh_speed_channel_movie_6
```
影视库

```
baiduboxlite://v1/browser/open?from=1&landingPageType=gh_speed_channel_movie_8&sa=gh_speed_channel_movie_8&url=https%3A%2F%2Fsenode.baidu.com%2Faladdin-landing%2Fpage%2FyuleGeneric%3Ffrom_sf%3D1%26word%3D%E5%BD%B1%E8%A7%86%E4%BD%9C%E5%93%81%26title%3D%E5%BD%B1%E8%A7%86%E7%89%87%E5%BA%93%26resource_id%3D51274%26top%3D%7B%22sfhs%22%3A0%7D%26ms%3D1%26openapi%3D1%26trigger_srcid%3D51251%26tn%3Dtangram%26pd%3Dmovie_general%26ext%3D%7B%22sf_tab_name%22%3A%2B%E7%94%B5%E5%BD%B1%2B%7D%26stat0%3D%E7%94%B5%E8%A7%86%E5%89%A7%26frorder%3D1%26q_ext%3D%7B%22video_type_list%22%3A%5B%22%E7%94%B5%E5%BD%B1%22%2C%22%E7%94%B5%E8%A7%86%E5%89%A7%22%2C%22%E7%BB%BC%E8%89%BA%22%2C%22%E5%8A%A8%E6%BC%AB%22%2C%22%E7%BA%AA%E5%BD%95%E7%89%87%22%5D%7D%26fxqPattern%3D1%26isColumn%3D1%26page_type%3D0%26isQingJingYe%3D1%26gh_speed_channel_movie_8
```




# 上线流程
1. GCP配置上线
2. 代码上线（sbox-basic）
3. 同步搜索FE上线-打点 已经上线




TODO：

1. 引导弹窗是否需要—— 不需要
2. Feed tab 是否需要feed 侧RD介入—— 不需要
3. 主版二期的需要加吗？各种tag—— 不需要
4. 一期各个模块的顺序不变——确认