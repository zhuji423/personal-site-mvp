---
title: "docker pull [镜像名]:[版本号]  // 版本号可省略，省略会下载最新版本"
description: "Nginx安装与配置"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Nginx_引用文档\\Nginx安装与配置.md"
---
Nginx安装与配置

### 一、使用docker安装（linux）
1、拉取Nginx镜像文件

docker pull [镜像名]:[版本号]  // 版本号可省略，省略会下载最新版本

```
# docker pull [镜像名]:[版本号]  // 版本号可省略，省略会下载最新版本
docker pull nginx
```
2、查看下载好的镜像文件  

```
docker images
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
3、创建并运行Nginx容器

```
docker run -d --name nginx-zj -p 8050:80 nginx
```
命令详解：

* docker run 启动一个镜像
* -d 表示后台允许
* --name nginx-zj  表示为当前容器起一个别名
* -p 8050:80 表示将本机的8050端口映射到nginx镜像的80端口

4、查看正在运行的容器

```
docker ps
```
5、查看Nginx是否部署成功

```
curl localhost:8050
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
6、进入Nginx容器当中操作

```
docker exec -it nginx-zj /bin/bash
```
ctr+d退出，退出后还是运行状态

![](/personal-site-mvp/img/doc-placeholder.svg "")
7、创建挂载文件夹，复制配置

本机创建 /usr/local/docker/nginx/conf，从容器复制配置到本机

```
docker cp nginx-zj:/etc/nginx/conf.d /usr/local/docker/nginx/conf/conf.d/
docker cp nginx-zj:/etc/nginx/nginx.conf /usr/local/docker/nginx/conf/
docker cp nginx-zj:/usr/share/nginx/html/ /usr/local/docker/nginx/html/
```
8、移除旧容器，创建挂载文件的nginx容器：

```
docker stop nginx-zj
docker rm nginx-zj
```
```
docker run -d --name nginx  --network=host \
-v /usr/local/docker/nginx/conf/conf.d/default.conf:/etc/nginx/conf.d/default.conf \
-v /usr/local/docker/nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
-v /usr/local/docker/nginx/html/:/usr/share/nginx/html/ \
-v /usr/local/docker/nginx/logs/:/var/log/nginx/ \
-v ~/zhoujie19/:/work/ \
nginx
```
初始的nginx.conf：

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
}

```
打开 http://localhost:80

![](/personal-site-mvp/img/doc-placeholder.svg "")
修改配置/usr/local/docker/nginx/conf/nginx.conf后，重启容器

```
docker restart nginx
```
### 二、mac m1安装





