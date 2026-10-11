---
title: "README"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_0324\\baidu\\inner-os\\itp\\itp\\itp-web\\src\\main\\resources\\README.md"
---
## web模块开发配置说明
``注：修改完之后使用local profile, 执行maven的clean install命令, 则``
``src/main/resources/local里的配置会被拷贝到WEB-INF/classes中,``
``web.xml使用WebContent/WEB-INF/local/web.xml,``
``具体profile相关配置在pom.xml中``
``
### 一、本地不使用nginx
#### 1、conf/local/configuration.properties
master和slave的jdbcUrl配置, 测试环境主从为同一个
```
master.jdbc.jdbcUrl=jdbc:mysql://cp01-ecomep-itp01-2.epc.baidu.com:7777/itp_dev?autoReconnect=true&useUnicode=true&characterEncoding=utf8&zeroDateTimeBehavior=convertToNull&noAccessToProcedureBodies=true&connectTimeout=60000&socketTimeout=60000
slave.jdbc.jdbcUrl=jdbc:mysql://cp01-ecomep-itp01-2.epc.baidu.com:7777/itp_dev?autoReconnect=true&useUnicode=true&characterEncoding=utf8&zeroDateTimeBehavior=convertToNull&noAccessToProcedureBodies=true&connectTimeout=60000&socketTimeout=60000
```
itp.host配置, 例如供fe测试的服务部署地址为
```
itp.host=itp.baidu.com:8080
```
黄蔚的开发机配置为
```
itp.host=10.99.199.181:8080
```
#### 2、conf/local/applicationContext-servlet.xml
静态资源文件的地址修改
```
<mvc:resources mapping="/css/**" location="/assets/dist/dev/css/"/>
<mvc:resources mapping="/fonts/**" location="/assets/dist/dev/fonts/"/>
<mvc:resources mapping="/js/**" location="/assets/dist/dev/js/"/>
<mvc:resources mapping="/templates/**" location="/assets/dist/dev/templates/"/>
<mvc:resources mapping="/**.ico" location="/assets/"/>
```
此处需要先根据/WebContent/WEB-INF/README.md 中的说明,
在WebContent/assets目录下执行npm run dev命令,
才会生成dist/dev目录, 如果用的是非dev标签, 则生成是其他目录
#### 3、WebContent/WEB-INF/local/web.xml
首页地址, 指定文件目录
```
<welcome-file-list>
    <welcome-file>assets/dist/dev/index.html</welcome-file>
</welcome-file-list>
```
uuap相关
本地开发, 开发非权限接口时可以注释掉整段.
开发权限相关接口时需要打开, 需要把
```itp.baidu.com:8080```
修改为本机服务访问ip和端口, 例如
```10.99.199.181:8080```
### 二、若本地使用nginx
例如服务启动的tomcat端口是8080, 但是nginx监听的是8888端口, 则一中配置的端口需要修改为8888
包括：
1、conf/configuration.properties中itp.host
2、web.xml中uuap的配置