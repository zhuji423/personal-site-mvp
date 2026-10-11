---
title: "打印异常，只打印第一和最后一行"
description: "页面内容处理 bs4"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\Python Good Coder考试-多线程爬虫\\页面内容处理 bs4.md"
---
页面内容处理 bs4

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
详细教程： [https://cuiqingcai.com/1319.html](https://cuiqingcai.com/1319.html) 重点关注 7. 搜索文档树

### 页面下载
```
def is_url(url):
    """
    判断url是否合法
    """
    pattern = r"^https?:/{2}\w.+$"
    res = re.match(pattern, url)
    if res:
        return True
    else:
        return False


def main(thread_name, crawl_url, crawl_timeout):
    """
    下载url
    :param thread_name: 线程名
    :param crawl_url: 下载url
    :param crawl_timeout: 抓取超时时间
    :return: 返回url对应的网页内容
    """
    crawl_res = None
    try:
        if is_url(crawl_url):
            crawl_res_req = requests.get(crawl_url, timeout=crawl_timeout)
            if crawl_res_req and crawl_res_req.status_code == requests.codes.ok:
                crawl_res = crawl_res_req.text
                logging.info('%s 从 url:%s 抓取页面信息，status_code: %s'
                             % (thread_name, crawl_url, crawl_res_req.status_code))
        else:
            logging.error("url:%s 是无效地址" % crawl_url)
    except Exception as e:
        # 打印异常，只打印第一和最后一行
        formatted_lines = traceback.format_exc().splitlines()
        logging.error("下载 url:%s 失败, %s, %s" % (crawl_url, formatted_lines[0], formatted_lines[-1]))
    finally:
        return crawl_res
```
### 页面解析
```
def get_url_list_or_res_list(crawl_url, urls, target_re):
    """
    获取 url_list 、res_list
    :param crawl_url: 当前抓取url
    :param urls: 页面元素
    :param target_re: 正则对象
    :return 返回的url_list 或 res_list
    """
    fanal_list = []
    for url in urls:
        href_url = url.get("href")
        if not href_url:
            continue
        elif href_url.startswith("http"):
            final_url = href_url
        elif "javascript:location.href" in href_url:
            # javascript:location.href="/url"
            final_url = url_parse.urljoin(crawl_url, href_url.split("=")[-1].split("\"")[-2])
        else:
            final_url = url_parse.urljoin(crawl_url, href_url)
        # 匹配校验
        if target_re.match(final_url):
            fanal_list.append(final_url)
    return fanal_list


def main(crawl_url, webpage_res, target_re):
    """
    下载url
    :param crawl_url: 当前抓取url
    :param webpage_res: 下载的网页内容
    :param target_re: 正则对象
    :return url_list: 子网页的url
    :return res_list: 网页抓取内容
    """
    url_list = []
    res_list = []
    if webpage_res:
        soup = bs4.BeautifulSoup(webpage_res, "html.parser")
        # 获取所有的<a><link><img>
        tag_a_link_res = soup.find_all(["a", "link"])
        tag_a_link_img_res = soup.find_all(["a", "link", "img"])

        url_list = get_url_list_or_res_list(crawl_url, tag_a_link_res, target_re)
        res_list = get_url_list_or_res_list(crawl_url, tag_a_link_img_res, target_re)
        logging.info("%s 页面含新url个数:%s，页面获取到符合正则限定的数据个数:%s" % (crawl_url, len(url_list), len(res_list)))
    return url_list, res_list
```

