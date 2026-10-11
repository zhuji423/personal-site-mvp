---
title: "云服务器简单部署flask（chatgpt）"
description: "云服务器简单部署flask（chatgpt）"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\flask\\如流智能机器人（闲聊plato、p图、chatgpt）_引用文档\\云服务器简单部署flask（chatgpt）.md"
---
云服务器简单部署flask（chatgpt）

### 1、租一个云服务器
获得公网ip：43.137.46.199

### 2、安装环境上传代码包
安装flask

```
pip install Flask
```
上传main.py文件到云服务器

```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hi", methods=["GET"])
def users():
    return jsonify({"code": 0, "meg": "success"})


if __name__ == '__main__':
    host = '0.0.0.0'
    app.run(host=host, port=8015, debug=True)

```
### 3、安全组设置
端口自己定，这里以8015端口为例，打开8015端口

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 4、运行
运行

```
python3 main.py
```
用postman测下接口 地址为 http://公网ip:端口/hi

![](/personal-site-mvp/img/doc-placeholder.svg "")
### 5、做chatgpt接口转发
```
import json

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

CHATGPT_API_KEY = ''
CHATGPT_API_URL = 'https://api.openai.com/v1/completions'


def chatgpt_api(data):
    """
    处理内容
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % CHATGPT_API_KEY}
    req = requests.post(CHATGPT_API_URL, data=json.dumps(data), headers=headers)
    req_dic = json.loads(req.content)
    return req_dic


@app.route('/', methods=['POST'])
def get_data():
    data = request.json
    print(data)
    res = chatgpt_api(data)

    return jsonify(res)


@app.route("/hi", methods=["GET"])
def users():
    return jsonify({"code": 0, "meg": "success"})


if __name__ == '__main__':
    host = '0.0.0.0'
    app.run(host=host, port=8015, debug=True)

```
运行

```
python3 chatgpt.py
```
用postman测下接口 地址为 http://公网ip:端口

![](/personal-site-mvp/img/doc-placeholder.svg "")
后台运行

```
nohup python3 chatgpt.py &
```
查看日志

```
tail -f nohup.out
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
查看后台情况

```
ps -axjf  |grep  python3
```
杀死进程

```
kill -9 60479
```

