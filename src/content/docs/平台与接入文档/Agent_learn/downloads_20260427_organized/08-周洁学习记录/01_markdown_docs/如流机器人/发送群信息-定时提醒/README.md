---
title: "计算今天对应的top250的序号"
description: "发送群信息-定时提醒"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\如流机器人\\发送群信息-定时提醒\\README.md"
---
发送群信息-定时提醒

### 一、申请机器人
[https://qy.baidu.com/doc/index.html#/inner_serverapi/robot?id=添加机器人](https://qy.baidu.com/doc/index.html#/inner_serverapi/robot?id=添加机器人)

### 二、定时提醒
#### 1、使用示例
每日定时推送消息：包括天气、假期时间和电影推荐

![](/personal-site-mvp/img/doc-placeholder.svg "")
***不想自己部署运行，想吃现成的，跳转本文第三部分***

#### 2、项目运行
运行：

```
python3 main.py '{"hi_webhook": "http://apiin.im.baidu.com/api/msg/groupmsgsend?access_token=d88b984607d9623546453e8", "group_id":733255}, "start_time": "2024-03-21"}'
```
* group_id 如流群号
* hi_webhook 机器人配置
* start_time 第一次运行时间 （之后的250个工作日会对应不同的top250电影推荐信息）

需要注意的是机器人的拥有者需要为群管理才能发送

![](/personal-site-mvp/img/doc-placeholder.svg "")
可以设置成每天定时运行，程序会自己判定法定节假日不推送，在参数里加debug可以发上一个工作日的内容用于节假日里debug

项目代码：

```
.
├── data
│   ├── card
│   │   ├── 10437779.png
│   │   ├── 10463953.png
...
│   │   └── 6985810.png
│   ├── jiaqi_conf.json
│   └── movie_conf.json
├── lib
│   ├── douban_api.py
│   ├── jiaqi.py
│   ├── movie.py
│   ├── movie_img_create.py
│   └── tianqi.py
└── main.py
```
[附件: everday_movie.zip | 87.6MB | application/zip | fileId=a54976f2d1ec4a509968db00d47f265b]
推荐电影信息的爬取参考：[豆瓣top250数据爬取与推荐图生成](./发送群信息-定时提醒_引用文档/豆瓣top250数据爬取与推荐图生成.md)

#### 3、代码构成
##### 主程序
```

"""
Desc:    后端具体功能实现文件

Authors: zhoujie19(zhoujie19@baidu.com)
Date:    2021/09/29
Kirin:   212400
"""
import sys
import time
import traceback
import json

import requests

from lib import jiaqi, tianqi, movie


HI_GROUP_ID = 0
HI_WEBHOOK1 = ''
HI_WEBHOOK2 = ''


def send_message(toid, body, hi_webhook):
    """
    发送信息到hi群
    """
    data = {
        "message": {
            "header": {
                "toid": [toid]
            },
            "body": body
        }
    }
    url = hi_webhook
    headers = {"Content-Type": "application/json"}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    req_dic = json.loads(req.content)
    return req_dic


def hi_robot(content_lst, img_code, param):
    """
    发送信息到hi群
    """
    hi_webhook = HI_WEBHOOK1
    if 'hi_webhook' in param:
        hi_webhook = param['hi_webhook']
    group_id = HI_GROUP_ID
    if 'group_id' in param:
        group_id = param['group_id']

    body = [
        {
            "content": '\n'.join(content_lst),
            "type": "TEXT"
        }

    ]
    send_message(group_id, body, hi_webhook)

    if img_code is not None:
        hi_webhook = HI_WEBHOOK2
        if 'hi_webhook' in param:
            hi_webhook = param['hi_webhook']
        body = [
            {
                "content": img_code,
                "type": "IMAGE"
            }
        ]
        send_message(group_id, body, hi_webhook)


def happy_every_day():
    """
    每日提醒
    """
    try:
        param = json.loads(sys.argv[1])
        content_lst = []

        if not jiaqi.check_is_holiday() or 'debug' in param:
            # 计算今天对应的top250的序号
            start_time = None
            if 'start_time' in param:
                start_time = param['start_time']
            day_diff = jiaqi.get_work_days(start_time)

            # 查询天气
            weathers = tianqi.main()
            day_info = '%s %s %s摄氏度 %s级风' % \
                       (time.strftime("%Y年%m月%d日", time.localtime()),
                        weathers['weather'], weathers['hot'], weathers['wind'])
            content_lst.append(day_info)

            # 查询最近一年假期
            holidays = jiaqi.main()
            for holiday in holidays:
                diff_info = '距离%s还有：%s天' % (holiday, holidays[holiday])
                content_lst.append(diff_info)
            content_lst.append('')

            # 查询电影信息根据序号
            if -1 < day_diff < 250:
                movies = movie.main(day_diff)
                douban_info = movies['desc']
                content_lst.append(douban_info)
                hi_robot(content_lst, movies['img_code'], param)

            else:
                # 电影推荐结束了
                hi_robot(content_lst, None, param)

            print(content_lst)

    except:
        print('执行碰到异常：%s' % traceback.format_exc())


if __name__ == '__main__':
    happy_every_day()

```
##### 工具类
###### （1）天气
申请和风天气api

```
"""
Desc:    获取天气

Authors: zhoujie19(zhoujie19@baidu.com)
Date:    2022/10/01

"""
import json
import requests

HEFENG_API = ''


def main():
    """
    入口
    """
    res = None
    req = requests.get(HEFENG_API)
    req_res = json.loads(req.content)
    if 'HeWeather6' in req_res:
        now = req_res['HeWeather6'][0]['now']
        res = {
            'weather': now['cond_txt'],
            'wind': now['wind_sc'],
            'hot': now['tmp']
        }
    print(res)
    return res


if __name__ == "__main__":
    main()
```
###### （2）假期倒计时
```

"""
Desc:    获取最近一年国家法定假期

Authors: zhoujie19(zhoujie19@baidu.com)
Date:    2022/09/29

"""
import json
import time
import datetime
import calendar

import chinese_calendar
from dateutil.relativedelta import relativedelta


def count_differ_days(time_a, time_b):
    """
    计算日期相差天数
    """
    d1 = datetime.date(time_a.year, time_a.month, time_a.day)
    d2 = datetime.date(time_b.year, time_b.month, time_b.day)

    return (d1 - d2).days


def get_holidays(year, month):
    """
    获取指定月份节假日
    """
    with open('data/jiaqi_conf.json', "rb") as f:
        JIAQI = json.load(f)
    fading_holidays = ['春节', '元旦节', '除夕', '元宵节', '清明节', '劳动节', '端午节', '中秋节', '国庆节']
    for item in JIAQI:
        if item['year'] == str(year):
            year_cont = item['list']
            for day_item in year_cont:
                cur_month = day_item['date'].split('-')[1]
                if day_item['name'] in fading_holidays and cur_month == str(month):
                    cur = datetime.datetime.strptime(day_item['date'], '%Y-%m-%d')
                    day_diff = count_differ_days(cur, datetime.datetime.now())
                    if day_diff > 0 and day_item['name'] not in holidays:
                        holidays[day_item['name']] = day_diff


def get_gongzi_diff():
    """
    本月最后一个工作日
    """
    today = datetime.date.today()
    last = today.replace(day=calendar.monthrange(today.year, today.month)[1])
    if last.weekday() < 5:
        gongzi_day = last
    else:
        gongzi_day = last - datetime.timedelta(days=1 + last.weekday() - 5)
    return count_differ_days(gongzi_day, datetime.datetime.now())


def main():
    """
    入口
    """
    global holidays

    NOW = datetime.datetime.now()
    delta = relativedelta(months=1)
    fmt = lambda dt: dt.strftime("%Y-%m")
    mons = (fmt(NOW + delta * i) for i in range(0, 13))
    mons = list(mons)
    print(mons)

    holidays = {
        '周末': max(0, 6 - int(time.strftime("%w", time.localtime()))),
        '发工资': get_gongzi_diff()
    }
    for mon in mons:
        mon_group = mon.split('-')
        get_holidays(int(mon_group[0]), int(mon_group[1]))

    print(holidays)
    return holidays


def get_work_days(start_time):
    """
    判断距离开始日期过去了几个工作日
    """
    if start_time is None:
        start_time = '2022-9-29'
    order = -1
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
    end_time = datetime.datetime.now()
    differ_days = count_differ_days(end_time, start_time)
    for i in range(differ_days + 1):
        cur = start_time + datetime.timedelta(days=i)
        is_workday = chinese_calendar.is_workday(cur)
        if is_workday:
            order += 1
    # 挂了8天
    print('diff day: ', order)
    return order


def check_is_holiday():
    """
    判断今天是否是节假日
    """
    input_time = datetime.datetime.now()
    is_holiday = chinese_calendar.is_holiday(input_time)
    if is_holiday:
        print('%s is holiday!' % input_time)
    else:
        print('%s is not holiday!' % input_time)
    return is_holiday


if __name__ == "__main__":
    main()
    # print(get_work_days())

```
###### （3）电影推荐
```
"""
Desc:    获取电影推荐

Authors: zhoujie19(zhoujie19@baidu.com)
Date:    2022/10/01

"""
import base64
import json


def process_img_code(doubanId):
    """
    card base64编码
    """
    with open('data/card/%s.png' % doubanId, "rb") as f:
        # 使用base64进行加密
        base64_data = str(base64.b64encode(f.read()).decode())
    return base64_data


def main(day_diff=0):
    """
    入口
    """
    with open('data/movie_conf.json', "rb") as f:
        DOUBAN_CONF = json.load(f)

    movie = DOUBAN_CONF[str(day_diff)]
    img_code = process_img_code(movie['doubanId'])
    res = {
        'doubanId': movie['doubanId'],
        'desc': '今日影荐：%s    ————《%s》' % (movie['slogan'], movie['name']),
        'img_code': img_code
    }
    print(movie['doubanId'], res['desc'])
    return res


if __name__ == "__main__":
    main(0)

```
类似的用法还有：

每天中午晚上吃饭提醒小机器人（实现起来就比较简单了）

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 三、立刻使用
服务已经打包好放到kirin平台上了

##### http接口
**post **http://kirin.baidu-int.com/api/tool/212400

```
{
    "parameter": "{\"hi_webhook\":\"{hi_webhook}\",\"group_id\": {group_id}},\"start_time\":\"{start_time}\"",
    "name": "zhoujie19",
    "token": ""
}
```
* hi_webhook 、group_id群号、start_time开始时间 需要改成自己的
* token 在 [http://kirin.baidu-int.com/#/home](http://kirin.baidu-int.com/#/home) 右上角查看自己的token

![](/personal-site-mvp/img/doc-placeholder.svg "")
就能在群里看到今日信息了，确定没问题你写一个定时任务，每天调这个接口就好了（还是得动手，气不气）
