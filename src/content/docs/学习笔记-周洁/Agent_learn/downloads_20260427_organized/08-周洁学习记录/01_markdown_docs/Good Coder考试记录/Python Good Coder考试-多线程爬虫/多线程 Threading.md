---
title: "多线程 Threading"
description: "多线程 Threading"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\多线程 Threading.md"
---
多线程 Threading

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 一、线程基础
Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。

_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。

threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法： 

* threading.currentThread(): 返回当前的线程变量。 
* threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
* threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

* **run**(): 用以表示线程活动的方法。
* **start**():启动线程活动。
* **join**([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
* isAlive(): 返回线程是否活动的。
* getName(): 返回线程名。
* setName(): 设置线程名。

## 二、实际应用
2.1 配合queue一起学习

[线程间的同步 Queue](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1324896954)

2.2 抓取线程

```
class CrawlThread(threading.Thread):
    """
    抓取线程
    """
    def __init__(self, url_queue, res_queue, crawl_interval, crawl_timeout, target_re,
                 thread_name="crawl_thread"):
        """
        抓取线程初始化
        :param url_queue: url管理队列
        :param res_queue: 结果保存队列
        :param crawl_interval: 抓取间隔. 单位：秒
        :param crawl_timeout: 抓取超时. 单位：秒
        :param target_re: 正则对象
        """
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.url_queue = url_queue
        self.res_queue = res_queue
        self.crawl_interval = crawl_interval
        self.crawl_timeout = crawl_timeout
        self.target_re = target_re
        self.stop_event = threading.Event()
        self.url_list_cur = list()  # 待抓取url列表
        self.res_list_cur = list()  # 待保存res列表

    def run(self):
        """
        执行
        """
        try:
            logging.info("%s 初始化完成，开始执行" % self.thread_name)

            while not self.stop_event.is_set():
                crawl_url = self.url_queue.get()
                if crawl_url:
                    logging.info("%s 开始执行抓取url:%s" % (self.thread_name, crawl_url))
                    webpage_res = webpage_download.main(self.thread_name, crawl_url, self.crawl_timeout)
                    url_list, res_list = webpage_parse.main(crawl_url, webpage_res, self.target_re)
                    self.url_list_cur.extend(url_list)
                    self.res_list_cur.extend(res_list)
                    self.url_queue.task_done()
                time.sleep(self.crawl_interval)
        except Exception as e:
            logging.error("保存抓取文件异常, msg is [%s]" % traceback.format_exc())

    def get_url_list_cur(self):
        """
        获取待抓取url列表
        """
        return self.url_list_cur

    def get_res_list_cur(self):
        """
        获取待保存res列表
        """
        return self.res_list_cur

    def clear(self):
        """
        清理待抓取url列表与保存res列表
        """
        self.url_list_cur.clear()
        self.res_list_cur.clear()

    def stop(self):
        """
        结束线程
        """
        self.stop_event.set()
```
2.3 保存线程

```
class SaveThread(threading.Thread):
    """
    保存线程
    """
    def __init__(self, res_queue, output_directory, thread_name="save_thread"):
        """
        初始化保存线程
        :param res_queue: 结果保存队列
        :param output_directory: 抓取结果存储目录
        """
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.res_queue = res_queue
        self.output_directory = output_directory
        self.stop_event = threading.Event()

    def run(self):
        """
        启动线程
        """
        try:
            logging.info("%s 初始化完成，开始执行" % self.thread_name)

            with open(self.output_directory, 'w') as outfile:
                while not self.stop_event.is_set():
                    res = self.res_queue.get()
                    if res:
                        logging.info("保存 %s" % res)
                        outfile.write(res + os.linesep)
                        self.res_queue.task_done()
        except Exception as e:
            logging.error("保存抓取文件异常, msg is [%s]" % traceback.format_exc())

    def stop(self):
        """
        结束线程
        """
        self.stop_event.set()
```

