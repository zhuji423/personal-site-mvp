---
title: "种子文件路径"
description: "配置文件读取 ConfigParser"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\配置文件读取 ConfigParser.md"
---
配置文件读取 ConfigParser

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
ConfigParser 是用来读取配置文件的包。配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容。

```
[spider]
# 种子文件路径
url_list_file: ./urls
# 抓取结果存储目录
output_directory: ./output
# 最大抓取深度(种子为0级)
max_depth: 1
# 抓取间隔. 单位：秒
crawl_interval: 1
# 抓取超时. 单位：秒
crawl_timeout: 1
# 需要存储的目标网页URL pattern(正则表达式) ,需要考虑兼容抓取html等情况，不止是抓取图片
target_url: .*\.(html|gif|png|jpg|bmp)$
# 抓取线程数
thread_count: 8

[test]
name: zhoujie19
```
使用ConfigParser 首选需要初始化实例，并读取配置文件：

```
import configparser

cf = configparser.ConfigParser()

filename = cf.read(conf_path)
print(filename)
# ['conf/spider.conf']
if len(filename) == 0:
    logging.error("配置文件：%s 不存在" % conf_path)
    sys.exit(1)
# sections() 得到所有的section，以列表形式返回
sec = cf.sections()
print(sec)
# ['spider', 'test']

# options(section) 得到section下的所有option
opt = cf.options("spider")
print(opt)
# ['url_list_file', 'output_directory', 'max_depth', 'crawl_interval', 'crawl_timeout', 'target_url', 'thread_count']

# items 得到section的所有键值对
value = cf.items("spider")
print(value)
# [('url_list_file', './urls'), ('output_directory', './output'), ('max_depth', '1'), ('crawl_interval', '1'), ('crawl_timeout', '1'), ('target_url', '.*\\.(html|gif|png|jpg|bmp)$'), ('thread_count', '8')]

# get(section,option) 得到section中的option值，返回string/int类型的结果
max_depth = cf.get("spider", "max_depth")
thread_count = cf.getint("spider", "thread_count")
print(max_depth, thread_count)
# 1 8
```
**应用：**

```
"""
Desc:    读取抓取配置文件

Authors: zhoujie19(zhoujie19@baidu.com)
Date:    2020/12/15
"""

import configparser
import logging
import sys
import traceback


class SpiderConfig(object):
    """
    抓取配置类
    """
    def __init__(self, url_list_file, target_url, output_directory, max_depth, crawl_interval, crawl_timeout,
                 thread_count):
        """
        抓取配置类初始化
        :param url_list_file: 种子文件路径，必需
        :param target_url: 需要存储的目标网页URL pattern(正则表达式) ,需要考虑兼容抓取html等情况，默认 .*\.(html|gif|png|jpg|bmp)$
        :param output_directory: 抓取结果存储目录，默认 ./output
        :param max_depth: 最大抓取深度(种子为0级)，默认 1
        :param crawl_interval: 抓取间隔. 单位：秒，默认 1
        :param crawl_timeout: 抓取超时. 单位：秒，默认 1
        :param thread_count: 抓取线程数，默认 1
        """
        self.url_list_file = url_list_file
        self.target_url = target_url if target_url is not None else '.*\.(html|gif|png|jpg|bmp)$'
        self.output_directory = output_directory if output_directory is not None else './output'
        self.max_depth = max_depth if max_depth is not None else 1
        self.crawl_interval = crawl_interval if crawl_interval is not None else 1
        self.crawl_timeout = crawl_timeout if crawl_timeout is not None else 1
        self.thread_count = thread_count if thread_count is not None else 1


def main(conf_path):
    """
    加载爬虫配置文件信息
    :param conf_path: 配置文件路径
    :return: spider_config: 配置类 SpiderConfig 实例
    """
    cf = configparser.ConfigParser()
    filename = cf.read(conf_path)
    if len(filename) == 0:
        logging.error("配置文件：%s 路径无效" % conf_path)
        sys.exit("配置文件：%s 路径无效" % conf_path)
    section_name = 'spider'
    # 得到所有的section，以列表形式返回
    if section_name in cf.sections():
        try:
            # 得到section下的所有option
            opt = cf.options(section_name)
            url_list_file = cf.get(section_name, "url_list_file")  # 必需
            # 非必需
            target_url = cf.get(section_name, "target_url") if "target_url" in opt else None
            output_directory = cf.get(section_name, "output_directory") if "output_directory" in opt else None
            max_depth = cf.getint(section_name, "max_depth") if "max_depth" in opt else None
            crawl_interval = cf.getint(section_name, "crawl_interval") if "crawl_interval" in opt else None
            crawl_timeout = cf.getint(section_name, "crawl_timeout") if "crawl_timeout" in opt else None
            thread_count = cf.getint(section_name, "thread_count") if "thread_count" in opt else None
            logging.info("读取配置信息结果：url_list_file: %s, target_re: %s, output_directory: %s, max_depth: %s, "
                         "crawl_interval: %s, crawl_timeout: %s, thread_count: %s"
                         % (url_list_file, target_url, output_directory, max_depth,
                            crawl_interval, crawl_timeout, thread_count))
            spider_config = SpiderConfig(url_list_file, target_url, output_directory, max_depth, crawl_interval,
                                         crawl_timeout, thread_count)
            return spider_config
        except Exception as e:
            logging.error("配置文件：%s 格式异常, msg is [%s]" % traceback.format_exc())
            sys.exit("配置文件：%s 格式异常，请检查配置内容" % conf_path)
    else:
        logging.error("配置文件：%s 中不含[spider]，请检查配置" % conf_path)
        sys.exit("配置文件：%s 中不含[spider]，请检查配置" % conf_path)
```





