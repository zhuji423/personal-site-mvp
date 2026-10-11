---
title: "1、创建iCoding实例"
description: "iCoding PyCharm Python3.11开发环境搭建"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-dev-docs_20260427\\iCoding PyCharm Python3.11开发环境搭建.md"
---
iCoding PyCharm Python3.11开发环境搭建

# 1、创建iCoding实例
[https://console.cloud.baidu-int.com/devops/icode/dev/resource/newResource](https://console.cloud.baidu-int.com/devops/icode/dev/resource/newResource)

* 选择自己的代码库分支
* 选择IDE，建议优先Pycharm

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=58cc9fc1a7964acf8007e005b8d8f4bc&docGuid=UaF7Alnr5tTh2Q "")
# 2、python3.11开发环境搭建
由于iCoding默认的Python版本只到3.9，但是目前开发以及线上要求的版本是Python3.11, 故需要自行安装3.11版本

```
bash -c "$( curl https://qep-testone.bj.bcebos.com/packages/install_python3-11-2_for_icoding.sh )"
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=03cd10ff82224ba192cc4f446a395965&docGuid=UaF7Alnr5tTh2Q "")


Python安装位置：/root/opt/deck/2.0/python-3.11.2

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ba19f6e00fcd4593bc1de7e004ff1598&docGuid=UaF7Alnr5tTh2Q "")
# 3、IDE配置
File -> Setting  -> Project -> Python Interpreter  -> Virtialenv Environment

> python安装位置：/root/opt/deck/2.0/python-3.11.2
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9b3beebd69754444ae67ea6b35dc3647&docGuid=UaF7Alnr5tTh2Q "")


激活本地虚拟环境 source venv/bin/activate

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=867606ac5d0e4ccf8c4c883115efa77a&docGuid=UaF7Alnr5tTh2Q "")


# 4、安装其他依赖
```
pip3 install -r requirements.txt -U --index-url http://pip.baidu.com/root/baidu/+simple/ --trusted-host pip.baidu.com  --no-cache-dir
```
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c0655e9cda574dd7a968b3a2dfbea467&docGuid=UaF7Alnr5tTh2Q "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=778b17f06c604af78daf808a257eada3&docGuid=UaF7Alnr5tTh2Q "")
