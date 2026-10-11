---
title: "异步 python asyncawait"
description: "异步 python async/await"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\语言学习\\python\\异步 python asyncawait.md"
---
异步 python async/await

在 Python 中，`async` 和 `await` 是用于编写异步代码的关键字。

用途：可以在等待 I/O 操作（如网络请求、文件读写等）时执行其他任务，从而提高程序的并发性和效率。

### 1. 基本用法 async/await
* 使用 `async def` 定义一个异步函数
* 异步函数不能直接调用，必须使用 `await` 来等待其执行完成
* 使用 `asyncio.run()` 来运行异步程序

```
import asyncio
import time


def now():
    return time.strftime("%H:%M:%S", time.localtime())


async def fetch_data():
    print("[%s]开始获取数据" % now())
    await asyncio.sleep(2)  # 模拟 I/O 操作
    print("[%s]数据获取完成" % now())
    return "数据"


async def main():
    result = await fetch_data()
    print("获取到的数据: %s" % result)


if __name__ == "__main__":
    asyncio.run(main())
```
![](/personal-site-mvp/img/docs-assets/image_001_7.png "")
### 2. 并发执行多个任务 `asyncio.gather()`
* 使用 `asyncio.gather()` 来并发执行多个异步任务

```
import asyncio


async def task1():
    await asyncio.sleep(1)
    return "任务1完成"


async def task2():
    await asyncio.sleep(2)
    return "任务2完成"


async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)  # 输出: ['任务1完成', '任务2完成']

if __name__ == "__main__":
    asyncio.run(main())
```
### 3. 创建任务并立即调度执行 `asyncio.create_task()`
`asyncio.create_task()` 用于创建一个任务并立即调度它执行：

```
import asyncio
import time


def now():
    return time.strftime("%H:%M:%S", time.localtime())


async def fetch_data():
    print("[%s]开始获取数据" % now())
    await asyncio.sleep(2)  # 模拟 I/O 操作
    print("[%s]数据获取完成" % now())
    return "数据"


async def main():
    task = asyncio.create_task(fetch_data())
    print("任务已创建")
    await task  # 等待任务完成
    print("任务已完成")

if __name__ == "__main__":
    asyncio.run(main())

```
### 4. 超时控制 `asyncio.wait_for()`
使用 `asyncio.wait_for()` 来设置超时时间：

```
async def main():
    try:
        result = await asyncio.wait_for(fetch_data(), timeout=1.0)
        print(result)
    except asyncio.TimeoutError:
        print("任务超时")
```
### 5. 异步上下文管理器 `async with`
使用 `async with` 来管理异步资源，进入时会调用 `__aenter__`，退出时会调用 `__aexit__`

```
import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("进入上下文")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is not None:
            print(f"发生异常: {exc}")
        print("退出上下文")
        return True  # 返回 True 表示异常已处理

async def main():
    async with AsyncContextManager() as manager:
        print("在上下文中执行操作")
        raise ValueError("测试异常")

if __name__ == "__main__":
    asyncio.run(main())
```
![](/personal-site-mvp/img/docs-assets/image_002_6.png "")
异步上下文管理器还可以处理异常。如果在 `async with` 块中发生异常，`__aexit__` 方法会接收到异常信息（`exc_type`, `exc`, `tb`），并可以根据需要处理。

### 6. 异步迭代器 `async for`
使用 `async for` 来迭代异步生成器：

```
async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for item in async_generator():
        print(item)
```
### 7. 异步队列 `asyncio.Queue`
`asyncio.Queue` 用于在异步任务之间传递数据：

```
async def producer(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"消费: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await producer_task
    await queue.join()
    consumer_task.cancel()
```
### 8. 异步锁 `asyncio.Lock`
`asyncio.Lock` 用于在异步代码中实现互斥锁：

```
async def worker(lock, name):
    async with lock:
        print(f"{name} 获得了锁")
        await asyncio.sleep(1)
        print(f"{name} 释放了锁")

async def main():
    lock = asyncio.Lock()
    await asyncio.gather(worker(lock, "任务1"), worker(lock, "任务2"))
```
![](/personal-site-mvp/img/docs-assets/image_003_7.png "")
### 9. 异步信号量 `asyncio.Semaphore`
`asyncio.Semaphore` 用于限制并发任务的数量：

```
async def worker(semaphore, name):
    async with semaphore:
        print(f"{name} 获得了信号量")
        await asyncio.sleep(1)
        print(f"{name} 释放了信号量")

async def main():
    semaphore = asyncio.Semaphore(2)  # 限制并发任务的数量为2
    await asyncio.gather(worker(semaphore, "任务1"), worker(semaphore, "任务2"), worker(semaphore, "任务3"))
```
![](/personal-site-mvp/img/docs-assets/image_004_4.png "")
### 10. 异步事件 `asyncio.Event`
`asyncio.Event` 用于在异步任务之间进行事件通知：

```
async def waiter(event):
    print("等待事件")
    await event.wait()
    print("事件已触发")

async def setter(event):
    await asyncio.sleep(1)
    print("触发事件")
    event.set()

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))
```
![](/personal-site-mvp/img/docs-assets/image_005_4.png "")
通过 `asyncio` 模块提供的工具，可以轻松地编写并发、超时控制、资源共享等复杂的异步逻辑。
