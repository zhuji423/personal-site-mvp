---
title: "1、http服务器"
description: "「系统的高可用」 当某个节点宕机后可以迅速将流量转移至其他节点。 「系统的高性能」 多台服务器共同对外提供服务，为整个系统提供了更高规模的吞吐。 「系统的拓展性」 当业务再次出现增长或萎靡时，可再加入/减少节点，灵活伸缩。"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Nginx.md"
---
Nginx

### 一、概念介绍
#### 1、背景
解决什么问题：①单体结构的部署方式无法承载日益增长的业务流量。②当后端节点宕机后，整个系统会陷入瘫痪，导致整个项目不可用。在这种背景下，引入**负载均衡**技术可带来的收益：

* 「系统的高可用」 当某个节点宕机后可以迅速将流量转移至其他节点。
* 「系统的高性能」 多台服务器共同对外提供服务，为整个系统提供了更高规模的吞吐。
* 「系统的拓展性」 当业务再次出现增长或萎靡时，可再加入/减少节点，灵活伸缩。

主要有两种负载方案，「「硬件层面与软件层面」」 ，比较常用的硬件负载器有`A10、F5`等，但这些机器动辄大几万乃至几十万的成本，因此一般大型企业会采用该方案，如银行、国企、央企等。而成本有限，但依旧想做负载均衡的项目，那么可在软件层面实现，如典型的`Nginx`。

#### 2、Nginx介绍
Nginx（“engine x”）是一款高性能的Web服务器和反向代理服务器，它采用事件驱动的异步结构，具有内存占用少、稳定性高、能够处理大量的并发请求，具有高效和低资源消耗等特点。 Nginx常常被用作Web服务器、**负载均衡**器、**反向代理**和缓存服务器等。

Nginx 引入前后，客户端请求处理流程的对比：

![](/personal-site-mvp/img/doc-placeholder.svg "")
原本客户端是直接请求目标服务器，由目标服务器直接完成请求处理工作，但加入`Nginx`后，所有的请求会先经过`Nginx`，再由其进行分发到具体的服务器处理，处理完成后再返回`Nginx`，最后由`Nginx`将最终的响应结果返回给客户端。

### 二、环境搭建
安装[Nginx安装与配置](./Nginx_引用文档/Nginx安装与配置.md)

### 三、常用功能
3个最常用的功能：Web服务器、负载均衡、反向代理。

```

user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;

    # 1、http服务器
    server {
        listen 8836 default_server;
        listen [::]:8836 default_server;
        server_name _;
        charset utf-8;
        root    /work/nginx/datas;                # 文件存放目录
        autoindex on;

        # 下载
        location / {
            autoindex_format html;                # 首页格式为HTML
            autoindex_exact_size off;             # 文件大小自动换算
            autoindex_localtime on;               # 按照服务器时间显示文件时间

            default_type application/octet-stream;# 将当前目录中所有文件的默认MIME类型设置为
                                                # application/octet-stream

            if ($request_filename ~* ^.*?\.(txt|doc|pdf|rar|gz|zip|docx|exe|xlsx|ppt|pptx)$){
                # 当文件格式为上述格式时，将头字段属性Content-Disposition的值设置为"attachment"
                add_header Content-Disposition: 'attachment;';
            }
            sendfile on;                          # 开启零复制文件传输功能
            sendfile_max_chunk 1m;                # 每个sendfile调用的最大传输量为1MB
            tcp_nopush on;                        # 启用最小传输限制功能

    #       aio on;                               # 启用异步传输
            directio 5m;                          # 当文件大于5MB时以直接读取磁盘的方式读取文件
            directio_alignment 4096;              # 与磁盘的文件系统对齐
            output_buffers 4 32k;                 # 文件输出的缓冲区大小为128KB

    #       limit_rate 1m;                        # 限制下载速度为1MB
    #       limit_rate_after 2m;                  # 当客户端下载速度达到2MB时进入限速模式
            max_ranges 4096;                      # 客户端执行范围读取的最大值是4096B
            send_timeout 20s;                     # 客户端引发传输超时时间为20s
            postpone_output 2048;                 # 当缓冲区的数据达到2048B时再向客户端发送
            chunked_transfer_encoding on;         # 启用分块传输标识
        }
    }

    # 2、反向代理
    server {  
        listen       8090;
        server_name  localhost;
        location / {  
            proxy_pass http://localhost:8082;
        }  
    }  

    # 3、负载均衡
    upstream nginx_flask{   
        # 请求分发权重比为1:2  
        server localhost:8081 weight=1;   
        server localhost:8082 weight=2;  
    }  

    server {  
        listen       8080;
        server_name  localhost;
        location / {  
            proxy_pass http://nginx_flask;
        }  
    }  
}

```
启动容器

```
docker run -d --name nginx  --network=host \
-v /usr/local/docker/nginx/conf/conf.d/default.conf:/etc/nginx/conf.d/default.conf \
-v /usr/local/docker/nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
-v /usr/local/docker/nginx/html/:/usr/share/nginx/html/ \
-v /usr/local/docker/nginx/logs/:/var/log/nginx/ \
-v /root/zhoujie19/:/work/ \  # 工作目录
nginx
```
不同的功能重点修改：/usr/local/docker/nginx/conf/nginx.conf配置文件

#### HTTP服务器
Nginx是一个HTTP服务器。可以将服务器上的静态文件（如HTML、图片）通过HTTP协议展现给客户端。把所有的静态资源的放到nginx上，可以使应用动静分离，性能更好。

修改nginx.conf的http部分，在http最下面新增：

```
    # 1、http服务器
    server {
        listen 8836 default_server;
        listen [::]:8836 default_server;
        server_name _;
        charset utf-8;
        root    /work/nginx/datas;                # 文件存放目录
        autoindex on;

        # 下载
        location / {
            autoindex_format html;                # 首页格式为HTML
            autoindex_exact_size off;             # 文件大小自动换算
            autoindex_localtime on;               # 按照服务器时间显示文件时间

            default_type application/octet-stream;# 将当前目录中所有文件的默认MIME类型设置为
                                                # application/octet-stream

            if ($request_filename ~* ^.*?\.(txt|doc|pdf|rar|gz|zip|docx|exe|xlsx|ppt|pptx)$){
                # 当文件格式为上述格式时，将头字段属性Content-Disposition的值设置为"attachment"
                add_header Content-Disposition: 'attachment;';
            }
            sendfile on;                          # 开启零复制文件传输功能
            sendfile_max_chunk 1m;                # 每个sendfile调用的最大传输量为1MB
            tcp_nopush on;                        # 启用最小传输限制功能

    #       aio on;                               # 启用异步传输
            directio 5m;                          # 当文件大于5MB时以直接读取磁盘的方式读取文件
            directio_alignment 4096;              # 与磁盘的文件系统对齐
            output_buffers 4 32k;                 # 文件输出的缓冲区大小为128KB

    #       limit_rate 1m;                        # 限制下载速度为1MB
    #       limit_rate_after 2m;                  # 当客户端下载速度达到2MB时进入限速模式
            max_ranges 4096;                      # 客户端执行范围读取的最大值是4096B
            send_timeout 20s;                     # 客户端引发传输超时时间为20s
            postpone_output 2048;                 # 当缓冲区的数据达到2048B时再向客户端发送
            chunked_transfer_encoding on;         # 启用分块传输标识
        }
    }
```
修改配置后，重启容器

```
docker restart nginx
```
文件存放在本机工作目录~/zhoujie19/nginx/datas，对应容器的/work/nginx/datas。

访问localhost:8836，对应文件服务器

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 反向代理
Nginx也是反向代理服务器。说反向代理之前先说一下正向代理。就是访问国外网被墙了，然后找个代理服务，通过该服务器访问国外网站，这个是正向代理。

反向代理是 客户端向服务器发送请求时，会首先经过 Nginx 服务器，由服务器将请求分发到相应的 WEB 服务器。正向代理是代理客户端，而反向代理则是代理服务器。

1、修改nginx.conf的http部分

```
    # 2、反向代理
    server {  
        listen       8090;
        server_name  localhost;
        location / {  
            proxy_pass http://localhost:8082;
        }  
    }  
```
2、启动2个服务

在演示功能之前，先用flask起两个后台服务，在不同的端口，flask详情参考：[flask](./React/React_引用文档/flask.md)

```
import sys
from flask import Flask

PORT = sys.argv[1]
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello %s\n' % PORT


if __name__ == '__main__':
    print(PORT)
    app.debug = True
    app.run(host='0.0.0.0', port=PORT)
```
```
nohup python3 demo.py 8081 &  # 运行之后别忘了删掉进程
nohup python3 demo.py 8082 &
```
试下服务是否可用

![](/personal-site-mvp/img/doc-placeholder.svg "")
3、代理访问服务

使用浏览器访问localhost:8090，由于nginx反向代理接受客户机请求， 根据proxy_pass对应的http路径，将请求转发到服务localhost:8082。

![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 负载均衡
所谓负载均衡，就是 Nginx 把请求均匀的分摊给上游的应用服务器，这样即使某一个服务器宕机也不会影响请求的处理，或者当应用服务器扛不住了，可以随时进行扩容。负载均衡和反向代理通常是一起使用的。

```
# 3、负载均衡
    upstream nginx_flask{   
        # 请求分发权重比为1:2  
        server localhost:8081 weight=1;   
        server localhost:8082 weight=2;  
    }  

    server {  
        listen       8080;
        server_name  localhost;
        location / {  
            proxy_pass http://nginx_flask;
        }  
    }  
```
将请求发送到2个不同的服务，分发权重比为1:2  

访问localhost:8080，多次刷新

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
使用浏览器访问localhost:8080，由于nginx反向代理接受客户机请求，根据proxy_pass对应的http路径，将请求转发到upstream nginx_flask上，按比重分发至两个不同的服务localhost:8081和localhost:8082。

#### 动静分离
在软件开发中，有些请求是需要后台处理的，有些请求是不需要经过后台处理的（如：css、html、jpg、js等等文件），这些不需要经过后台处理的文件称为静态文件。让动态网站里的动态网页根据一定规则把不变的资源和经常变的资源区分开来，动静资源做好了拆分以后，我们就可以根据静态资源的特点将其做缓存操作。提高资源响应的速度。

#### 其他功能
##### 资源压缩
##### 缓冲区
##### 缓存机制
##### 实现IP黑白名单
##### 跨域配置
##### 防盗链设计
##### 大文件传输配置
##### 配置SLL证书
##### 高可用
##### 性能优化


### 四、详情组成
#### 1、主配置文件nginx.conf
nginx.conf由六个模块组成：

* 全局块：全局配置，对全局生效
* events块：配置影响 Nginx 服务器与用户的网络连接
* http块：配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置
* server块：配置虚拟主机的相关参数，一个 http 块中可以有多个 server 块
* location块：用于配置匹配的 uri
* upstream块：配置后端服务器具体地址，负载均衡配置不可或缺的部分

注意：location 匹配的内容来源是来自网页的URI,而不是URL（URL代表整个链接如：www.baidu.com/images/search，而URI则是/images/search。所以nginx的location匹配的是URI）

##### 全局配置模块
配置文件从头开始到 events 块之间的内容，主要设置的是影响nginx服务器整体运行的配置指令。比如 worker_process，值越大，可以支持的并发处理量也越多，但是还是和服务器的硬件相关

![](/personal-site-mvp/img/doc-placeholder.svg "")
worker_process 工程进程数量，一般设置为cpu核数

##### I/O 事件配置 events
![](/personal-site-mvp/img/doc-placeholder.svg "")
worker_connections 每个进程处理的事件数

##### HTTP 配置 http
这部分是 Nginx 服务器配置中最频繁的部分，代理、缓存和日志定义等绝大多数功能和第三方模块的配置都在这里。

###### location
###### upstream
#### **2、进程组件角色**
* Master 进程：监视工作进程的状态 ; 当工作进程死掉后重启一个新的 ; 处理信号和通知工作进程。
* Worker 进程：处理客户端请求，从主进程处获得信号做相应的事情。
* Cache Loader 进程：加载缓存索引文件信息，然后退出。
* Cache Manager 进程：管理磁盘的缓存大小，超过预定值大小后最少使用数据将被删除。

![](/personal-site-mvp/img/doc-placeholder.svg "")
nginx采用多进程的模式，nginx在启动后，会有一个master进程和多个worker进程。master进程主要用来管理worker进程，包含：接收来自外界的信号，向各worker进程发送信号，监控worker进程的运行状态，当worker进程退出后(异常情况下)，会自动重新启动新的worker进程。而基本的网络事件，则是放在worker进程中来处理了。多个worker进程之间是对等的，他们同等竞争来自客户端的请求，各进程互相之间是独立的。一个请求，只可能在一个worker进程中处理，一个worker进程，不可能处理其它进程的请求。

#### **3、请求处理流程**
![](/personal-site-mvp/img/doc-placeholder.svg "")



