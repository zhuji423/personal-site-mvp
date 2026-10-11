---
title: "README"
description: "@Request.application def hellorequest: return Response'Hello World'"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\flask\\README.md"
---
flask

### 一、框架介绍
flask框架是python中的一个轻量级的前后端开发框架。一个核心两个库( Jinja2 模板引擎 和 WSGI工具集)

#### Django与flask
Django是个大而全的web框架，它内置许多模块，flask是一个小而精的轻量级框架，Django功能大而全，Flask只包含基本的配置, Django的一站式解决的思路，能让开发者不用在开发之前就在选择应用的基础设施上花费大量时间。Django有模板，表单，路由，基本的数据库管理等等内建功能。与之相反，Flask只是一个内核，默认依赖于2个外部库： Jinja2 模板引擎和 WSGI工具集--Werkzeug , flask的使用特点是基本所有的工具使用都依赖于导入的形式去扩展，flask只保留了web开发的核心功能。

##### Jinja2 模板引擎
参考：[jinja2](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/gYo3d7xR2rAMlX?t=mention&mt=doc&dt=doc)

##### WSGI工具集
WSGI（web服务器网关接口）是python中用来规定web服务器如何与python Web服务器如何与Python Web程序进行沟通的标准，本质上就是一个socket服务端。而 Werkzeug模块 就是WSGI一个具体的实现。

```
from werkzeug.wrappers import Request, Response

@Request.application
def hello(request):
    return Response('Hello World!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, hello)
```
flask正是依赖于这个werkzeug模块，由wekzeug模块实现了socket服务端的功能，hello必然是加括号运行了，才会执行hello里面的代码，而在我们的flask中app.run()会调用run_simple(host, port, self, **options)把上面代码例子的hello替换成了self也就是app。app()会触发Flask类的__call__方法。

所以所flask程序的入口就在__call__方法中，而__call__方法返回self.wsgi_app(environ, start_response)，所以整个程序的执行过程都在 self.wsgi_app(environ, start_response)中.

```
1 app.run() 调用 werkzeug.serving的run_simple(host, port, self, **options)
2 self()等价于app(), app()调用Flask类的__call__方法
3 Flask类的__call__方法返回了 self.wsgi_app(environ, start_response)
4 flask程序的执行过程都在 self.wsgi_app(environ, start_response)中
```
### 二、开始一个 flask项目
##### get接口
```
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello flask!'


if __name__ == '__main__':
    app.run()
```
app.run()实现了flask程序在开发环境下运行起来,并且默认ip和端口是127.0.0.1:5000

![](/personal-site-mvp/img/docs-assets/image_001_16.png "")
![](/personal-site-mvp/img/docs-assets/image_002_13.png "")
##### post接口
```
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hi", methods=["post"])
def users():
    data = request.json
    return jsonify({"code": 0, "meg": "success", "data": data["usr"]})
    
if __name__ == '__main__':
    host = '0.0.0.0'
    app.run(host=host, port=8015)
```
![](/personal-site-mvp/img/docs-assets/image_003_12.png "")
### 三、应用
[如流智能机器人](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/T8z-H2mrKBbRL8?t=mention&mt=doc&dt=doc)
