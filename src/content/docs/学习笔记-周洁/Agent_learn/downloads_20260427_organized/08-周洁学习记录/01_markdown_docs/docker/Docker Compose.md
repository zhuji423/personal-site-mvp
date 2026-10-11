---
title: "第三层 其他配置 网络、卷、全局规划"
description: "Docker Compose"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\docker\\Docker Compose.md"
---
Docker Compose

### 一、介绍
Compose 项目是 Docker 官方的开源项目，负责实现对 **Docker 容器集群的快速编排。**快速编排指站在项目角度将一组相关联容器整合在一起，对这组容器按照指定顺序进行启动。

通过 Compose，可以使用 YML 文件来配置应用程序需要的所有服务。然后，使用一个命令，就可以从 YML 文件配置中创建并启动所有服务。使用 Docker Compose 可以轻松、高效的管理容器。

**Compose 使用的三个步骤：**

1. 使用 **Dockerfile **定义应用程序的环境。
2. 使用 **docker-compose.yml** 定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。
3. 最后，执行 **docker-compose up **命令来启动并运行整个应用程序。

Compose 允许用户通过一个单独的 docker-compose.yml 模板文件(YAML格式)来定义一组相关联的应用容器为一个项目(project)。

### 二、安装
参考：[Docker安装与配置](./docker_引用文档/Docker安装与配置.md)第三部分

### 三、快速开始
[https://docs.docker.com/compose/gettingstarted/](https://docs.docker.com/compose/gettingstarted/)

场景：使用 Python 启动一个 Web 服务，输出一个`hello()`方法，每次访问的时候在 Redis 缓存中进行计数，并且将统计的结果打印到页面中。

#### 1、搭建环境
1）为项目创建目录composetest

```
mkdir composetest
```
2）在项目目录中创建程序文件 app.py

```
import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)
```
3）在项目目录中创建另一个依赖文件 requirements.txt 

```
flask
redis
```
#### 2、创建 Dockerfile
在项目目录中，创建文件 Dockerfile

```
FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
这段代码表示:

* 使用基础镜像 Python 3.6
* 将当前目录映射到镜像/code目录下
* 设置工作目录为 /code
* 安装依赖包
* 启动 app.py 程序

#### 3、定义 docker-compose.yml 文件
在项目目录中创建配置文件 docker-compose.yml

```
version: "3.8"  #代表使用docker-compose项目的版本号
services:
  web:
    build: .  #指定Dockerfile的上下文目录
    ports:  #宿主机和容器的端口映射
      - "5000:5000"
    volumes:
      - .:/code
  redis:
     image: "redis:alpine"
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 4、使用 Compose 构建项目
在项目目录下，执行命令 

```
docker-compose up
```
启动成功后的效果：

![](/personal-site-mvp/img/doc-placeholder.svg "")
ctr+c停止服务，docker-compose start启动服务后，查看启动的两个容器：

```
docker-compose ps
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
默认服务名：项目名_服务名_副本数量

#### 5、测试 app.py 应用
![](/personal-site-mvp/img/doc-placeholder.svg "")
可以看到，每访问一次，计数+1。

docker-compose.yml 下载的镜像:

```
docker images
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
docker-compose.yml 创建的网络:

```
docker network ls
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
项目中的两个服务都在这个网络下面，查看这个网络的元信息：

```
sudo docker network inspect  composetest_default
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
停止 docker-compose: 在docker-compose.yml 文件同级目录下输入命令：

```
docker-compose down
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 四、docker-compose.yml 文件解析
一个 docker-compose.yml 文件可以分为三层：

```
#第一层 版本号
version: "3.8"  #代表使用docker-compose项目的版本号
#第二层：services 服务配置
services:
  web:
    build: .
    ports:  #宿主机和容器的端口映射
      - "5000:5000"
    volumes:
      - .:/code
  redis:
     image: "redis:alpine"
# 第三层 其他配置 网络、卷、全局规划
```
#### build 指令
指定 Dockerfile 所在文件夹的路径（可以是绝对路径，或者相对 docker-compose.yml 文件的路径）。 Compose 将会利用它自动构建这个镜像，然后使用这个镜像。

```
version: "3.8" 
services:
  web:
    build: .  #指定Dockerfile的上下文目录为当前目录
```
也可以使用 `context `指令指定 Dockerfile 所在文件夹的路径。使用` dockerfile `指令指定 Dockerfile 文件名。使用 arg 指令指定构建镜像时的变量。

```
version: '3'
services:
  webapp:
    build:
      context: ./dir #定Dockerfile的上下文目录为当前目录的dir目录下
      dockerfile: Dockerfile-alternate
      args: 
        buildno: 1
```
#### command 指令
覆盖容器启动后默认执行的命令，类似于docker run image 命令

以下面的Dockerfile文件为例，容器启动后执行的是 java -jar apps.jar

```
FROM openjdk:8-jre
EXPOSE 8081
ENV APP_PATH=/apps
WORKDIR $APP_PATH
COPY apps.jar $APP_PATH
ENTRYPOINT ["java","-jar"]
CMD ["apps.jar"]
```
如果想要容器启动后执行的是 java -jar test.jar，在docker-compose.yml文件中使用指令 command: [“test.jar”]

```
version: '3'
services:
  webapp:
    build:
      context: ./dir #定Dockerfile的上下文目录为当前目录的dir目录下
      dockerfile: Dockerfile-alternate
      args: 
        buildno: 1
    command: ["test.jar"]
```
#### container_name 指令（不推荐使用）
指定容器名称。默认将会使用 项目名称_服务名称_序号 这样的格式。

```
container_name: docker-web-container
```
注意: 指定容器名称后，该服务将无法进行扩展（scale），因为 Docker 不允许多个容器具有相同的名称。

#### depends_on 指令
解决容器的依赖、启动先后的问题。以下例子中会先启动 redis 、db 再启动 web：

```
version: '3'
services:
  web:
    build: .
    depends_on: # web服务依赖于db和web服务
      - db
      - redis

  redis:
    image: redis

  db:
    image: postgres
```
注意：在启动web服务时，并不会等待 redis 、db 服务进入ready状态，而只是等到它们被启动状态(running状态)了。

#### environment 指令
设置环境变量，相当于 docker run -e。可以使用数组或字典两种格式。

只给定名称的变量会自动获取运行 Compose 主机上对应变量的值，可以用来防止泄露不必要的数据。

```
version: '3'

services:
  mysql:
    image: mysql:5.7
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: root  #字典格式
      
#====================================================
    environment:
      - "MYSQL_ROOT_PASSWORD=root"  #数组格式
      - "SESSION_SECRET"
```
#### env_file 指令
从文件中获取环境变量，可以为单独的文件路径或列表。

如果通过 docker-compose -f FILE 方式来指定 Compose 模板文件，则 env_file 中变量的路径会基于模板文件路径。

如果有变量名称与 environment 指令冲突，则按照惯例，以 environment 为准。

```
env_file: .env

env_file: #指定多个环境变量文件
  - ./common.env
  - ./.env
  - /opt/secrets.env
```
环境变量文件中每一行必须符合格式，支持 # 开头的注释行。

环境变量文件 .env：推荐使用这种命名，因为在Linux下，这种方式命名的文件属于隐藏文件，一定程度上防止泄露不必要的数据。

```
MYSQL_ROOT_PASSWORD=root
```
#### expose 指令
用来指定镜像构建过程中容器暴露的端口号，但不映射到宿主机，只被连接的服务访问。

该指令compose配置文件中一般不用，都在Dockerfile文件中使用EXPOSE指定。

#### image 指令
指定为镜像名称或镜像 ID。如果镜像在本地不存在，Compose 将会尝试拉取这个镜像，相当于 docker run image（镜像名）。

#### networks 指令
指定启动容器时使用的网络，相当于 docker run --network

```
version: "3"
services:

  some-service:
    networks:
     - some-network  #指定使用的网络
     - other-network

networks:   #创建网络
  some-network:
  other-network:
```
#### ports 指令
指定宿主机和容器端口映射，或者仅仅指定容器的端口（宿主将会随机选择端口）都可以。

注意：当使用 HOST:CONTAINER格式来映射端口时，如果你使用的容器端口小于 60 并且没放到引号里，可能会得到错误结果，因为YAML会自动解析xx:yy这种数字格式为 60 进制。为避免出现这种问题，建议数字串都采用引号包括起来的字符串格式。

#### volumes 指令
用来指定宿主机目录和容器目录映射

```
version: "3"

services:
  my_src:
    image: mysql:8.0
    volumes:  #数据卷名称挂载
      - mysql_data:/var/lib/mysql

volumes:  #定义数据卷名称
  mysql_data:
```
#### restart 指令
指定容器退出后的重启策略为始终重启。该命令对保持服务始终运行十分有效。

```
restart: always
```
### 五、实际使用
#### 1、搭建[WordPress](https://so.csdn.net/so/search?q=WordPress&spm=1001.2101.3001.7020)
WordPress是使用PHP语言开发的开源博客平台。

新建一个名为wordpress的文件夹，然后进入这个文件夹，创建 docker-compose.yml 文件：

```
version: "3"
services:

   db:
     image: mysql:8.0
     command:
      - --default_authentication_plugin=mysql_native_password
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci     
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: somewordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_USER: wordpress
       WORDPRESS_DB_PASSWORD: wordpress
volumes:
  db_data:
```
启动，执行命令 启动 Compose

```
docker-compose up 
```
启动成功后，查看运行的容器服务：

![](/personal-site-mvp/img/doc-placeholder.svg "")
浏览器使用localhost:8000 访问测试：

![注册账户并登录](/personal-site-mvp/img/doc-placeholder.svg "注册账户并登录")
![后台](/personal-site-mvp/img/doc-placeholder.svg "后台")
![前台](/personal-site-mvp/img/doc-placeholder.svg "前台")
关闭服务并删除容器

```
docker-compose down
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
#### 2、安装使用Milvus
```
version: '3.5'

services:
  etcd:
    container_name: milvus-etcd
    image: quay.io/coreos/etcd:v3.5.5
    environment:
      - ETCD_AUTO_COMPACTION_MODE=revision
      - ETCD_AUTO_COMPACTION_RETENTION=1000
      - ETCD_QUOTA_BACKEND_BYTES=4294967296
      - ETCD_SNAPSHOT_COUNT=50000
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/etcd:/etcd
    command: etcd -advertise-client-urls=http://127.0.0.1:2379 -listen-client-urls http://0.0.0.0:2379 --data-dir /etcd
    healthcheck:
      test: ["CMD", "etcdctl", "endpoint", "health"]
      interval: 30s
      timeout: 20s
      retries: 3

  minio:
    container_name: milvus-minio
    image: minio/minio:RELEASE.2023-03-20T20-16-18Z
    environment:
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: minioadmin
    ports:
      - "9001:9001"
      - "9000:9000"
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/minio:/minio_data
    command: minio server /minio_data --console-address ":9001"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3

  standalone:
    container_name: milvus-standalone
    image: milvusdb/milvus:v2.3.0
    command: ["milvus", "run", "standalone"]
    environment:
      ETCD_ENDPOINTS: etcd:2379
      MINIO_ADDRESS: minio:9000
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/milvus:/var/lib/milvus
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9091/healthz"]
      interval: 30s
      start_period: 90s
      timeout: 20s
      retries: 3
    ports:
      - "19530:19530"
      - "9091:9091"
    depends_on:
      - "etcd"
      - "minio"

networks:
  default:
    name: milvus
```
参考：[Milvus安装与配置](./docker 安装常用服务_引用文档/Milvus安装与配置（及可视化界面attu）.md)

### 六、常用命令



