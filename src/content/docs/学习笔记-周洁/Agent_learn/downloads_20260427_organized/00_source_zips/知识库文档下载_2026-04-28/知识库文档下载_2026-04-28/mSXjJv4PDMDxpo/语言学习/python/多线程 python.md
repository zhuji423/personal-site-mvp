---
title: "线程数量"
description: "多线程 python"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\语言学习\\python\\多线程 python.md"
---
多线程 python

### 方式1 ThreadPoolExecutor
```
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 线程数量
MAX_THREAD_NUM = 3


def main(sources):
    """
    使用多线程并发执行任务
    """

    def func(task):
        """
        执行
        """
        # 随机5～20s，模拟执行时常
        delay = random.randint(5, 20)
        time.sleep(delay)

        now = time.strftime("%H:%M:%S", time.localtime())
        print('[%s][%s]: %s， 耗时 %s 秒' % (now, threading.current_thread().name, task['name'], delay))

        # 模拟执行 超时为None
        if delay <= 15:
            task['delay'] = delay
            return task

        return None

    cur = 0
    total_files = len(sources)
    res = []
    print('[%s]start!' % time.strftime("%H:%M:%S", time.localtime()))
    with ThreadPoolExecutor(max_workers=MAX_THREAD_NUM, thread_name_prefix="thread") as executor:
        futures = []
        for idx, source in enumerate(sources):
            # 提交任务并添加延迟
            future = executor.submit(func, source)
            futures.append(future)
            if idx < MAX_THREAD_NUM:
                time.sleep(1)  # 每个任务间隔启动(qps限制)

        for future in as_completed(futures):
            cur += 1
            result = future.result()
            print("完成任务: %s/%s..." % (cur, total_files))
            if result is not None:
                res.append(result)
    return res


if __name__ == "__main__":
    sources = [
        {
            "name": "test1",
            "param": {"a": 1}
        },
        {
            "name": "test2",
            "param": {"b": 2}
        },
        {
            "name": "test3",
            "param": {"c": 3}
        },
        {
            "name": "test4",
            "param": {"d": 4}
        },
        {
            "name": "test5",
            "param": {"e": 5}
        }
    ]
    res = main(sources)
    print(res)

```
![](/personal-site-mvp/img/docs-assets/image_001_8.png "")
### 方式2 threading.Thread
多线程大大压缩获取数据时间

```
import threading
import collections
import time

# 线程数量
THREAD_NUM = 3

lock = threading.Lock()
result_list = collections.deque()


def task_generate():
    """
    生成器读取生成任务
    """
    for task in task_lst:
        yield task


def loop(task):
    """
    线程控制
    """
    while True:
        try:
            with lock:
                task_cur = next(task)
        except StopIteration:
             break

        # 具体处理逻辑
        print('[%s][%s], name: %s' % (time.strftime("%H:%M:%S", time.localtime()),
                                      threading.current_thread().name, task_cur['name']))
        result_list.append(task_cur['param'])
        time.sleep(1)


def main(para):
    """
    主程序入口
    """
    global task_lst
    # 任务列表
    task_lst = para
    # 生成器读取生成任务
    api_gen = task_generate()

    # 多线程任务执行
    thread_num = THREAD_NUM if len(para) > THREAD_NUM else len(para)
    print('thread_num: %s' % thread_num)
    threads = []
    for i in range(0, thread_num):
        t = threading.Thread(target=loop, name='Thread %s' % i, args=(api_gen,))
        threads.append(t)
        t.start()
    # 等待所有线程完成
    for t in threads:
        t.join()

    return list(result_list)


if __name__ == "__main__":
    para = [
        {
            "name": "test1",
            "param": {"a": 1}
        },
        {
            "name": "test2",
            "param": {"b": 2}
        },
        {
            "name": "test3",
            "param": {"c": 3}
        },
        {
            "name": "test4",
            "param": {"d": 4}
        },
        {
            "name": "test5",
            "param": {"e": 5}
        }
    ]
    res = main(para)
    print("res: ", res)

```


![](/personal-site-mvp/img/docs-assets/image_002_7.png "")





