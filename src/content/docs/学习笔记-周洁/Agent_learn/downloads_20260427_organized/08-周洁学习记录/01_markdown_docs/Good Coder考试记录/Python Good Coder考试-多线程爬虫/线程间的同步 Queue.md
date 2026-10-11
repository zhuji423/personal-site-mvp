---
title: "线程间的同步 Queue"
description: "线程间的同步 Queue"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\线程间的同步 Queue.md"
---
线程间的同步 Queue

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 
## 一、 基础知识
Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列**Queue**，LIFO（后入先出）队列**LifoQueue**，和优先级队列**PriorityQueue**。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

**常用方法：**

qsize() 返回队列的大小

empty() 如果队列为空，返回True,反之False

full() 如果队列满了，返回True,反之False，Queue.full 与 maxsize 大小对应

**task_done()**

意味着之前入队的一个任务已经完成。由队列的消费者线程调用。每一个get()调用得到一个任务，接下来的task_done()调用告诉队列该任务已经处理完毕。

如果当前一个join()正在阻塞，它将在队列中的所有任务都处理完时恢复执行（即每一个由put()调用入队的任务都有一个对应的task_done()调用）。

**join()**

阻塞调用线程，直到队列中的所有任务被处理掉。

只要有数据被加入队列，未完成的任务数就会增加。当消费者线程调用task_done()（意味着有消费者取得任务并完成任务），未完成的任务数就会减少。当未完成的任务数降到0，join()解除阻塞。

**put(item[, block[, timeout]])**

将item放入队列中。

1. 如果可选的参数block为True且timeout为空对象（默认的情况，阻塞调用，无超时）。
2. 如果timeout是个正整数，阻塞调用进程最多timeout秒，如果一直无空空间可用，抛出Full异常（带超时的阻塞调用）。
3. 如果block为False，如果有空闲空间可用将数据放入队列，否则立即抛出Full异常

其非阻塞版本为put_nowait等同于put(item, False)

**get([block[, timeout]])**

从队列中移除并返回一个数据。block跟timeout参数同put方法

其非阻塞方法为 get_nowait() 相当与 get(False)

## 二、生产者消费者应用实例
```
from Queue import Queue
import time,threading
q=Queue(maxsize=0)
 
def product(name):
    count=1
    while True:
        q.put('气球兵{}'.format(count))
        print ('{}训练气球兵{}只'.format(name,count))
        count+=1
        time.sleep(5)
def consume(name):
    while True:
        print ('{}使用了{}'.format(name,q.get()))
        time.sleep(1)
        q.task_done()
t1=threading.Thread(target=product,args=('wpp',))
t2=threading.Thread(target=consume,args=('ypp',))
t3=threading.Thread(target=consume,args=('others',))
 
t1.start()
t2.start()
t3.start()
```
## 三、具体应用
### 3.1 UrlQueue
```
class UrlQueue(object):
    """
    url管理队列
    """
    def __init__(self):
        """
        初始化url队列
        """
        self.url_queue = queue.Queue()
        self.url_set = set()  # 去重
        self.timeout = 5  # 获取队列，timeout等待时间
        self.lock = threading.Lock()

    def put_list(self, url_list):
        """
        新增url列表
        """
        if isinstance(url_list, list):
            for url in url_list:
                if url is not None:
                    self.lock.acquire()
                    try:
                        if url not in self.url_set:
                            self.url_queue.put(url)
                            self.url_set.add(url)
                    finally:
                        self.lock.release()

    def get(self):
        """
        取url
        """
        try:
            return self.url_queue.get(timeout=self.timeout)
        except Exception as e:
            logging.info("队列中暂无url")

    def task_done(self):
        """
        已完成
        """
        self.url_queue.task_done()

    def join(self):
        """
        阻塞
        """
        self.url_queue.join()
```
### 3.2 ResQueue
```
class ResQueue(object):
    """
    res管理类
    """

    def __init__(self):
        """
        初始化res队列
        """
        self.res_queue = queue.Queue()
        self.timeout = 5  # 获取队列，timeout等待时间

    def put_list(self, res_list):
        """
        新增res列表
        """
        if isinstance(res_list, list):
            for res in res_list:
                self.res_queue.put(res)

    def get(self):
        """
        取结果
        """
        try:
            return self.res_queue.get(timeout=self.timeout)
        except Exception as e:
            logging.info("队列中暂无res")

    def task_done(self):
        """
        已完成
        """
        self.res_queue.task_done()

    def join(self):
        """
        阻塞
        """
        self.res_queue.join()
```

