---
title: "ITP开发者文档"
description: "ITPInterface test platform"
date: "2026-10-11"
category: "项目架构文档"
source: "F:\\百度工作\\01_code\\code\\baidu\\core\\itp_0324\\baidu\\inner-os\\itp\\README.md"
---
# ITP开发者文档
	
ITP(Interface test platform)

主要用于各类接口测试活动。通用性的解决了集群运行、接口权限、自动录制、协议处理、自动修复等问题，整合商业服务质量部原有的优秀接口测试服务。由搜索公司QAEP团队与各业务产品线联合开发与维护。目前在搜索公司几十个产品中广泛使用，希望开源爱好者一起贡献。

## 背景
在过去几年中, ECOM-QA在接口测试方面, 积累了非常多的效果优良的测试平台或服务, 如已开源的Itest框架、在糯米广泛使用的dcom序列自动化平台、NMTest、以及在联盟团队广泛使用的BAT平台等

各平台在目标业务线都取得了非常突出的效果, 但同时也存在功能重复及优势功能不能复用等问题

为解决上述问题, 集中优质资源, 由ECOMQA-TC、ECOMQA-EP和各业务线共同打造了统一的ITP平台, 平台集成原有平台服务的优势能力, 广泛支持原平台所支持的测试场景与使用习惯。将原有平台服务的优势能力最大化的对外输出, 同时集中力量解决通用问题。

平台覆盖ECOM广泛应用的HTTP(JSON/SOAP/Protobuf)、Dubbo、RMI等协议, 支持单一接口测试和工作流类型的序列化接口测试, 支持 数据驱动、参数传递、扩展函数、ABTest等常用测试能力。同时平台通过分布式运行集群、CTP等, 实现大规模测试支持, 并与其它平台, 如Season、CTP、泰坦等实现平台协同, 成为平台画布中的组成部分。

## 项目地址
git路径:
[http://icode.baidu.com/repos/baidu/inner-os/itp/tree/master](baidu/inner-os/itp)

平台在线地址:
[http://itp.baidu.com](http://itp.baidu.com) 

平台测试环境地址:
[http://itp.baidu.com:8580](http://itp.baidu.com:8580)

平台开发测试环境地址:
[http://itp.baidu.com:8080](http://itp.baidu.com:8080)

河图地址:
[http://hetu.baidu.com/api/platform/index?platformId=1813](http://hetu.baidu.com/api/platform/index?platformId=1813)

文档地址(史上最全):
[http://agroup.baidu.com/itp/md/article/331349](http://agroup.baidu.com/itp/md/article/331349)

Hi群: 开发者群 1591264 ，用户群 1508946
联系人: suhanyuan01@baidu.com; maxing01@baidu.com; huangwei15@baidu.com

## 代码结构

ITP 代码包含：
* itest-executor：主要用于实际的接口访问、断言等具体操作的处理，被itp/tasktracker引用。
* itp：
  * itp-web: itp web模块
  * itp-tasktracker: itp 分布式执行模块
* resource：包含各类初始化脚本
* lts：分布式调度模块，改造并使用了外部开源框架，原github地址：https://github.com/ltsopensource/light-task-scheduler
 
## 架构图

![ITP architecture](http://itp.baidu.com:8555/doc/architecture.png)

## 编译说明

## 各模块开发及测试说明

### itest-executor
【模块说明】
* executor：核心模块，单独编译为jar包供tasktacker引用，同时可作为开放sdk
* example：executor作为sdk时的使用案例

【executor】

example不做过多介绍，主要介绍executor模块。
executor处理的操作为itp中的操作一级，不同的操作对应的入口方法为
xxxRequestExecutor的invokeRequestAndVerify方法，沿该方法可下钻找到详细处理逻辑
PS：
1.需特别注意的是代码中混入了凤巢的特有逻辑，后续会逐步剥离
2.cookie和返回header的处理方式为保存传递，保存在envconfig中

【编译方法】

可使用maven直接编译，或使用build.sh编译。

【关于测试】

建议该模块独立测试，可以编写相应单元测试，test目录下已有部分测试，可参考。

### tasktracker
【模块说明】
* tasktracker：核心模块，基于lts框架实现了itp的业务逻辑。
  * bo: 业务实体定义（其中还包括了对SEASON平台交互所使用的类定义）；
  * common: spring框架，mybatis框架，以及jdbc基础配置类；
  * function: itp平台提供的自定义函数模块（基于java SPI规范实现）；
  * runner: 基于lts框架，主要的业务实现入口类，分别对应不同粒度的接口测试逻辑实现。
  * service: 对接SEASON平台的接口和实现类；
  * support: 其他支持类；
  * util: 工具类，提供了参数替换，参数传递，邮件提醒，验证拼装等逻辑。
* web：
  * bo: 持久化层实体，基于业务库表结构定义；
  * common: 静态常量和枚举定义；
  * facde: 封装了持久化层的逻辑，引用了bo和common空间下的类；
  * mapper: mybatis持久化层配置文件。

【tasktracker】

runner空间下各种Runner实现不同测试逻辑；
其中JobRunner封装了底层实现，直接和itest-executor交互，不同的操作对应的入口方法为
xxxRequestExecutor的invokeRequestAndVerify方法，传入参数包括request对象和envConfig对象：
  request：封装了和本次操作相关的请求和验证信息；
  envConfig：封装了操作执行时使用到的环境信息，如：权限，db，redis，cookie等。
沿该方法可下钻itest-executor层查看到详细处理逻辑。

注意：tasktracker日志输出当前包括log4j和ltsBiz两种，log4j是常规的服务端日志，打印到容器日志中；ltsBiz日志是lts框架开放的
业务日志输出方式，会打印到日志数据库（itp暂时采用Mongo），并实时地展现在itp-web界面上供用户查看。
日志打印方式：常规地调用com.baidu.ecom.itest.api.utils.LogUtil的info(), debug(),.error()等方法即可，无需关注底层两种
logger的维护工作。

【编译方法】

可使用maven直接编译，或使用build.sh编译。

【关于测试】

建议该模块独立测试，可以编写相应单元测试，test目录下已有部分测试，可参考。

### itp-web
#### server端代码
【模块说明】
* web：核心模块，基于lts框架实现了itp的业务逻辑。
  * action: controller层，接口定义
  * bo: 业务实体定义
  * common: spring框架，mybatis框架，以及jdbc基础配置类；
  * enums: 枚举类型定义
  * filter: uuap相关filter
  * mapper: mapper类定义
  * service: service层
  * sharding: 分表相关类
  * util: 工具类，提供了array、date、string等自定义的处理逻辑。
  * vo: 视图实体定义
  * websocket: websocket相关方法
* jobclient：lts框架的jobclient.jar的实现类
* logger: lts框架logger包的实现类
* 其他工具
  * jackson: 为了返回给前端时候一些特殊数值处理引的包

【编译方法】
* server模块使用maven编译,本地开发使用local标签

#### 前端代码
【模块说明】
* WebContent\assets\src: 源代码
* WebContent\assets\mockserve: mock数据

【编译方法】
<br>前端代码使用gulp编译，编译步骤：
* 1.安装node(如果已安装请忽略)
    下载地址 http://nodejs.cn/
* 2.安装打包的插件包(如果已安装请忽略)
    <br>cd assets;
    <br>npm install;
    <br>npm install gulp -g
* 3.前端开发后代码编译
    <br>gulp
    <!--npm install;
    npm run dev;   -->


#### itp-web本地开发配置说明
``注：修改完之后使用local profile, 执行maven的clean install命令, 则``<br>
``src/main/resources/local里的配置会被拷贝到WEB-INF/classes中,``<br>
``web.xml使用WebContent/WEB-INF/local/web.xml,``<br>
``具体profile相关配置在pom.xml中``<br>

 一、仅开发后端接口
 <br> 目前本地开发直接使用local标签编译，部署tomcat即可，不需要修改配置。
 <br> 启动tomcat无报错之后，假如tomcat启动端口为8080，则可以通过访问http://localhost:8080/itp/user 尝试访问
 <br> 接口访问无误后，可以通过url访问、测试其他新接口
 
 二、开发前端，或前后端一起开发，需要配置nginx<br>
假设服务启动的tomcat端口是8080, 但是nginx监听的是8090端口<br>
1、安装nginx并启动<br>
2、编译itp前端文件，假设前端编译后目录为D:\baidu\ecom-ep\itp\itp\itp-web\WebContent\assets\dist\dev<br>
3、在nginx中指定前端文件路径即可，配置例如:<br>
```
    server {
        listen       8090;
        server_name  localhost;

        location ~* \.(html|xmind|js|css|png|jpeg|jpg|gif|ico|pdf|xlsx|woff|ttf|woff2|swf|map)$ {
            expires -1;
            index  index.html;
            root D:\baidu\ecom-ep\itp\itp\itp-web\WebContent\assets\dist\dev;
            # root /Users/xxx/baidu/inner-os/itp/itp/itp-web/WebContent/assets/dist/dev/js/vendor
        }

        location = / {
            #index index.html;
        }

        location ~ /* {
            proxy_pass http://localhost:8080;
            #proxy_pass http://cp01-ecomep-itp01-2.epc.baidu.com:8080;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header   Host   $host;
            proxy_set_header   Referer $http_referer;
            proxy_set_header   Cookie $http_cookie;
            proxy_set_header   X-Real-IP  $remote_addr;
            proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
            proxy_buffer_size 4k;
            proxy_buffers 32 4k;
            proxy_busy_buffers_size 64k;
          }
```
其中<br>
root D:\baidu\ecom-ep\itp\itp\itp-web\WebContent\assets\dist\dev; 指定的是前端的文件目录, 以自己本地目录为准<br>
如果开发web-server，可以把proxy_pass配置为自己的tomcat启动ip和端口,proxy_pass http://localhost:8080; 指定了本地itp web后端服务地址<br>
如果只是开发前端，可以不启动server，直接把服务指向cp01-ecomep-itp01-2.epc.baidu.com:8080，即配置为"proxy_pass http://cp01-ecomep-itp01-2.epc.baidu.com:8080;" ,使用itp开发环境web-server<br>
三、如果开发权限相关接口<br>
需要手动修改部分配置才能生效。<br>
1、conf/local/configuration.properties<br>
itp.host配置, 本地服务访问地址，例如
```
itp.host=localhost:8080
或者
itp.host=localhost:8090（如果使用nginx）
```
2、WebContent/WEB-INF/local/web.xml<br>
将\<\!-- uuap begin -->\<-- uuap end -->之间的内容取消注释，并且把所有itp.baidu.com:8080，修改为本地服务访问地址，和1中地址一致。


【关于测试】<br>
暂无


### generator
【模块说明】
generator 是一个maven-plugin，可以用于从工程中抽取接口信息，抽取得到的信息可在itp平台直接导入为api模版，简化用例编写

如何使用：

1.在工程中引入插件

    <dependency>
      <groupId>com.baidu.itp</groupId>
      <artifactId>generator</artifactId>
      <version>1.0-SNAPSHOT</version>
      <scope>test</scope>
    </dependency>

2.执行maven命令：

    mvn generator:{goal}   针对不同的工程类型，goal不同，例如springmvc：mvn itp:generator:springmvc-generator

    如果使用本地仓库里的插件 mvn com.baidu.itp:generator:springmvc-generator
    
3.命令执行完会在target目录的generated-itp下生产报告api.out,拷贝到itp平台即可导入

【如何开发】

项目特点不同，解析api的方法不同，工程初始只提供了对spring mvc的解析，若需要解析其他工程，可开发自己的解析函数

在com.baidu.itp.generator.mojo 下 创建自己的mojo（继承AbstractGeneratorMojo），实现其中的execute和print方法即可，可参考已写好的其他mojo，如SpringMvcGeneratorMojo

【编译方法】

可使用maven直接编译

【关于测试】

对插件执行mvn install后，可在被测工程里引入你install到本地仓库的插件，执行mvn generator:{你的goal}，查看生产的文件

### 管理后台
[开发环境管理后台地址](http://10.94.242.72:8083/node-manager.htm)
可以查看启动的节点是否已注册成功。



## 如何贡献
1.暂时分为新的贡献者和稳定开发者

2.新的贡献者,可以先merge到develop分支上,成为稳定的开发者,可以直接提交master,并加入到开发组中

3.针对Bug修复，需先创建issue，修复提交的commit中关联issue

4.针对新feature添加，贡献者如果想做那一块,建议先线下和下述成员沟通下

    suhanyuan01@baidu.com

    maxing01@.baidu.com
    
    huangwei15@baidu.com
      
  同时创建新的issue，每次commit同样需关联 issue

5.尽量不要引入多余的jar包,如果是那种插件扩展,可以将jar设置为provided

6.其他添加中...... 合作愉快

## 测试
测试方法已写于各模块说明中，不做赘述

## 讨论
## 快速开始