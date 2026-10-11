---
title: "1、创建iCoding实例"
description: "iCoding PyCharm Python3.11开发环境搭建"
date: "2026-04-28"
category: "工具与环境"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-dev-docs_20260427\\iCoding PyCharm Python3.11开发环境搭建.md"
---
iCoding PyCharm Python3.11开发环境搭建

# 1、创建iCoding实例
[https://console.cloud.baidu-int.com/devops/icode/dev/resource/newResource](https://console.cloud.baidu-int.com/devops/icode/dev/resource/newResource)

* 选择自己的代码库分支
* 选择IDE，建议优先Pycharm

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 2、python3.11开发环境搭建
由于iCoding默认的Python版本只到3.9，但是目前开发以及线上要求的版本是Python3.11, 故需要自行安装3.11版本

```
bash -c "$( curl https://qep-testone.bj.bcebos.com/packages/install_python3-11-2_for_icoding.sh )"
```
![](/personal-site-mvp/img/doc-placeholder.svg "")


Python安装位置：/root/opt/deck/2.0/python-3.11.2

![](/personal-site-mvp/img/doc-placeholder.svg "")
# 3、IDE配置
File -> Setting  -> Project -> Python Interpreter  -> Virtialenv Environment

> python安装位置：/root/opt/deck/2.0/python-3.11.2
![](/personal-site-mvp/img/doc-placeholder.svg "")


激活本地虚拟环境 source venv/bin/activate

![](/personal-site-mvp/img/doc-placeholder.svg "")


# 4、安装其他依赖
```
pip3 install -r requirements.txt -U --index-url http://pip.baidu.com/root/baidu/+simple/ --trusted-host pip.baidu.com  --no-cache-dir
```
![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")
