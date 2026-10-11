---
title: "加入urls中初始链接"
description: "核心控制器部分 controller"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\核心控制器部分 controller.md"
---
核心控制器部分 controller

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
![](../../../assets/5hOY6XUXTqQ29v/image_001.bin "")
```
def controller(seedfile_list, url_queue, res_queue, max_depth, crawl_thread_list, save_thread):
    """
    构建启动抓取线程
    :param seedfile_list: 种子列表
    :param url_queue: url管理队列
    :param res_queue: res保存队列
    :param max_depth: 最大抓取深度
    :param crawl_thread_list: 抓取线程列表
    :param save_thread: 收集结果线程
    :return:
    """
    # 加入urls中初始链接
    url_queue.put_list(seedfile_list)
    # 启动抓取线程
    for crawl_thread in crawl_thread_list:
        crawl_thread.start()
    # 启动保存线程
    save_thread.start()

    cur_depth = 1
    while True:
        logging.info("***************************** 当前抓取深度：%d，最大抓取深度：%d *****************************"
                     % (cur_depth, max_depth))
        url_queue.join()
        # 深度 cur_depth 抓取结束，更新 url_queue、res_queue
        if cur_depth < max_depth:
            for crawl_thread in crawl_thread_list:
                url_queue.put_list(crawl_thread.get_url_list_cur())
                res_queue.put_list(crawl_thread.get_res_list_cur())
                crawl_thread.clear()
        elif cur_depth == max_depth:
            for crawl_thread in crawl_thread_list:
                res_queue.put_list(crawl_thread.get_res_list_cur())
                crawl_thread.clear()
                crawl_thread.stop()
            break
        cur_depth += 1

    res_queue.join()
    save_thread.stop()

    for crawl_thread in crawl_thread_list:
        crawl_thread.join()
```

