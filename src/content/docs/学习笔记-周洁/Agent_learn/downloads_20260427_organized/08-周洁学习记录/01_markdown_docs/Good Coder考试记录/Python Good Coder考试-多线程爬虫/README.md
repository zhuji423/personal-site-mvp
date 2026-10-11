---
title: "Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved"
description: "Python Good Coder考试-多线程爬虫"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\README.md"
---
Python Good Coder考试-多线程爬虫



考题：
迷你定向网页抓取器
在调研过程中，经常需要对一些网站进行定向抓取。由于python包含各种强大的库，使用python做定向抓取比较简单。请使用python开发一个迷你定向抓取器mini_spider.py，实现对种子链接的广度优先抓取，并把URL长相符合特定pattern的网页内容（图片或者html等）保存到磁盘上。

程序运行：
`python mini_spider.py -c conf/spider.conf` 
配置文件spider.conf：
```
[spider] 
url_list_file: ./urls ; 种子文件路径 
output_directory: ./output ; 抓取结果存储目录 
max_depth: 1 ; 最大抓取深度(种子为0级) 
crawl_interval: 1 ; 抓取间隔. 单位：秒 
crawl_timeout: 1 ; 抓取超时. 单位：秒 
target_url: .*\.(html|gif|png|jpg|bmp)$ ; 需要存储的目标网页URL pattern(正则表达式) ,需要考虑兼容抓取html等情况，不止是抓取图片
thread_count: 8 ; 抓取线程数 
```

种子文件每行一条链接，例如：
http://cup.baidu.com/spider/
http://www.baidu.com 
http://www.sina.com.cn 

## 一、知识学习总结
[命令行参数处理 Argparse](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1324885986)

[多线程 Threading](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1327182183)

[核心控制器部分 controller](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1327181958)

[正则表达式 Re](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1324451767)

[线程间的同步 Queue](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1324896954)

[配置文件读取 ConfigParser](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1324891374)

[页面内容处理 bs4](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1327185098)

二、代码部分

### 2.1 代码流程
![](../../../../_remote_images/08-周洁学习记录/local_assets/rUFdymG5krIUMN/image_001.bin "")
蓝色控制器部分是核心实现：

![](../../../../_remote_images/08-周洁学习记录/local_assets/rUFdymG5krIUMN/image_002.bin "")
### 2.2 代码结构
```
project

mini_spider.py: 主程序入口  
lib目录：存放不同模块的代码  
    config_load.py: 读取配置文件  
    seedfile_load.py: 读取种子文件  
    url_table.py: 构建url管理队列  
    res_table.py: 结果保存队列  
    crawl_thread.py: 实现抓取线程  
    webpage_download.py: 下载网页  
    webpage_parse.py: 对抓取网页的解析  
    webpage_save.py: 将网页保存到磁盘   
logs目录: 存放日志文件  
tests目录: 存放单测文件  
    test_config_load.py: 测试配置文件  
    test_parse_url.py: 测试抓取链接  
conf目录: 存放配置文件  
    spider.conf: 配置文件  
README.md: 说明文档  
urls: 种子文件
```
**2.3 代码主逻辑**

```
################################################################################
#
# Copyright (c) 2020 Baidu.com, Inc. All Rights Reserved
#
################################################################################

"""
Desc:    迷你定向网页抓取器
实现对种子链接的广度优先抓取，并把URL长相符合特定pattern的网页内容（图片或者html等）保存到磁盘上

Authors: zhoujie19(zhoujie19@baidu.com)
Date:    2020/10/14
"""

import argparse
import time

import lib.log as log
import lib.config_load as config_load
import lib.seedfile_load as seedfile_load
import lib.url_table as url_table
import lib.res_table as res_table
import lib.crawl_thread as crawl_thread
import lib.webpage_save as webpage_save


def main(conf_path):
    """
    主程序入口
    :param conf_path: 配置文件路径
    :return:
    """
    # 日志初始化, 设置日志写入文件和控制台
    log.init_log('./logs/mini_spider_%s' % time.strftime('%Y-%m-%d', time.localtime(time.time())))

    # 读取配置文件
    spider_config = config_load.main(conf_path)
    # 读取种子文件
    seedfile_list = seedfile_load.main(spider_config.url_list_file)

    # 构建url管理队列
    url_queue = url_table.main()
    # 构建res保存队列
    res_queue = res_table.main()

    # 构建抓取线程列表
    crawl_thread_list = crawl_thread.main(url_queue, res_queue, spider_config.thread_count, spider_config.target_url,
                                          spider_config.crawl_interval, spider_config.crawl_timeout)
    # 构建收集结果线程
    save_thread = webpage_save.main(res_queue, spider_config.output_directory)

    # 对抓取进行控制
    crawl_thread.controller(seedfile_list, url_queue, res_queue, spider_config.max_depth, crawl_thread_list, save_thread)


if __name__ == '__main__':
    # 命令行参数处理
    desc = """迷你定向网页抓取器"""
    argparse = argparse.ArgumentParser(prog="mini_spider", description=desc)
    argparse.add_argument("-v",
                          "--version",
                          action="version",
                          version="%(prog)s 1.0",
                          help="显示版本信息")
    argparse.add_argument("-c",
                          "--config",
                          required=True,
                          help="必填选项，输入爬虫配置文件路径")
    args = argparse.parse_args()
    main(args.config)
```
### 2.4 Icode地址
[http://console.cloud.baidu-int.com/devops/icode/repos/baidu/personal-code/zhoujie19_goodcoder_python/reviews/15532069/files](http://console.cloud.baidu-int.com/devops/icode/repos/baidu/personal-code/zhoujie19_goodcoder_python/reviews/15532069/files)



![](/personal-site-mvp/img/doc-placeholder.svg "")

