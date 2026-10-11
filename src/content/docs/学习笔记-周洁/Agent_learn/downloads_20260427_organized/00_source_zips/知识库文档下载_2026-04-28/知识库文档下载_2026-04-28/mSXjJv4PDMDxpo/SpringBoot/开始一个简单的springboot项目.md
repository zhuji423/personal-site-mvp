---
title: "一、创建项目"
description: "开始一个简单的springboot项目"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\SpringBoot\\开始一个简单的springboot项目.md"
---
开始一个简单的springboot项目

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间

建议框架：

![](/personal-site-mvp/img/docs-assets/image_001_23.png "")
下面是初学时写的，建议别往下看了。。。。。。。浪费时间

---

IDEA版本：2020.2.3 (Community Edition)

Spring Boot：v2.5.0

mysql版本：5.7.30

# 一、创建项目
1.File->new->project；

![](../../assets/ev8Rjxs0sBHX9o/image_002.bin "")
2.选择“Spring Initializr”，点击next；（jdk1.8默认即可）

![](../../assets/ev8Rjxs0sBHX9o/image_003.bin "")
注：社区版为Spring Assistant,没有的话在插件里安装选用

![](../../assets/ev8Rjxs0sBHX9o/image_004.bin "")
3.完善项目信息，组名可不做修改，项目名可做修改；最终建的项目名为：zjtest，点击next；

![](../../assets/ev8Rjxs0sBHX9o/image_005.bin "")
4.Web下勾选Spring Web；Template Englines勾选Thymeleaf；SQL勾选：MySQL Driver，JDBC API 和 MyBatis Framework三项；点击next；

![](../../assets/ev8Rjxs0sBHX9o/image_006.bin "")
5.选择项目路径，点击finish；打开新的窗口；

![](../../assets/ev8Rjxs0sBHX9o/image_007.bin "")
如果提示路径不存在，选择创建

6.刚创建好的项目目录结构

![](../../assets/ev8Rjxs0sBHX9o/image_008.bin "")
7.点击右侧的Maven，点击设置（扳手图标）进行项目Maven仓库的配置；

![](../../assets/ev8Rjxs0sBHX9o/image_009.bin "")
8.（1）选择本地Maven路径；（2）勾选配置文件后边的选项，然后修改为本地Maven的配置文件，它会根据配置文件直接找到本地仓库位置；

![](../../assets/ev8Rjxs0sBHX9o/image_010.bin "")
9.配置完后，如果没有自动导包，可以点击左上角重新导包按钮，或者下载按钮，选择下载所有源文件和文档

![](../../assets/ev8Rjxs0sBHX9o/image_011.bin "")
10.在templates文件下新建index.html页面，作为启动的初始页面；

![](../../assets/ev8Rjxs0sBHX9o/image_012.bin "")
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello</title>
</head>
<body>
这是一个SpringBoot项目。
</body>
</html>
```
11.在com.example.test下新建controller文件夹，在controller文件夹下建一个简单的helloController类；（Controller类要添加@Controller注解，项目启动时，SpringBoot会自动扫描加载Controller）

```
package com.example.demo.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class helloController {

    @RequestMapping("/index")
    public String sayHello(){
        return "index";
    }
}
```
12.在resources文件夹下application中先配置DataSource基本信息，application文件有两种文件格式，一种是以.properties为后缀，一种是以.yml为后缀的，两种配置方式略有差别，详情可参考这个[网址](https://blog.csdn.net/qq_29648651/article/details/78503853)。在这我是用.yml后缀的文件格式。右键application文件选择Refact，选择Rename，将后缀改为yml；

**application.yml**

```
spring:
  datasource:
    name: test  #数据库名
    url: jdbc:mysql://localhost:3306/ZjtestDatabase #url
    username: root  #用户名
    password:   #密码
    driver-class-name: com.mysql.jdbc.Driver  #数据库链接驱动
```
其中test为数据库名称，3306为默认的端口号。[Mac本机mysql应用](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1513928897)

13.运行项目启动类DemoApplication.java

![](../../assets/ev8Rjxs0sBHX9o/image_013.bin "")
![](../../assets/ev8Rjxs0sBHX9o/image_014.bin "")
处理：提示信息表明数据库驱动com.mysql.jdbc.Driver'已经被弃用了、应当使用新的驱动com.mysql.cj.jdbc.Driver'

所以，按照提示更改jdbc.properties配置 .com.mysql.jdbc.Driver  改为  com.mysql.cj.jdbc.Driver。重新运行。

14.在浏览器中输入localhost:8080,回车显示初始的index界面；

![](../../assets/ev8Rjxs0sBHX9o/image_015.bin "")
注意：当运行出现端口已被占用，

![](../../assets/ev8Rjxs0sBHX9o/image_016.bin "")
可能是因为升级或者idea关闭上次的服务还在运行，打开localhost:8080发现服务还在，这时找到运行的进程并杀死

![](../../assets/ev8Rjxs0sBHX9o/image_017.bin "")
或者一劳永逸，在pom.xml文件中将fork强制设置成false，从而不再使用单独进程启动。

![](../../assets/ev8Rjxs0sBHX9o/image_018.bin "")
到这项目的初步搭建已经完成，下面可以下一些简单的业务逻辑，比如从数据库获取信息，登录之类的简单功能；

# 二、与数据库交互
1.在进行下一步编写时，我们先来链接一下数据库；点击右侧的Database，点“加号”，新建数据库链接；

没有图标的话，直接点击View----->ToolWindows------>Database即可。仍然没有的话，在plugins安装Database Tools and SQL。如果以上都没找到，可能和我一样用的社区版，找Database  Navigator代替。

![](../../assets/ev8Rjxs0sBHX9o/image_019.bin "")
![](../../assets/ev8Rjxs0sBHX9o/image_020.bin "")
2.填写数据库相关信息，点击Test Connection，提示链接成功，点击Ok；

![](../../assets/ev8Rjxs0sBHX9o/image_021.bin "")
3.如果链接失败可能是驱动的问题，点击左上角的小扳手，进入数据库设置界面，修改mysql版本。（没遇到这个问题，木有图）

4.连接成功后，显示数据库信息，user表的基本信息也显示了，下面就照这个来了；

![](../../assets/ev8Rjxs0sBHX9o/image_022.bin "")
没有数据的话，数据库右键refresh，刷新数据。

# 三、项目构成
## 1.SpringBoot的四层
大概分为四层：

（1）DAO层：包括XxxMapper.java(数据库访问接口类)，XxxMapper.xml(数据库链接实现)；（这个命名，有人喜欢用Dao命名，有人喜欢用Mapper，看个人习惯了吧）

（2）Bean层：也叫model层，模型层，entity层，实体层，就是数据库表的映射实体类，存放POJO对象；

（3）Service层：也叫服务层，业务层，包括XxxService.java(业务接口类)，XxxServiceImpl.java（业务实现类）；（可以在service文件夹下新建impl文件放业务实现类，也可以把业务实现类单独放一个文件夹下，更清晰）

（4）Web层：就是Controller层，实现与web前端的交互。

依照上面四层，创建目录结构如下：

![](../../assets/ev8Rjxs0sBHX9o/image_023.bin "")
## 2.代码展示
（1）在application配置文件中添加MyBatis配置：

**application.yml**

```
spring:
  datasource:
    name: test  #数据库名
    url: jdbc:mysql://localhost:3306/ZjtestDatabase #url
    username: root  #用户名
    password:   #密码
    driver-class-name: com.mysql.cj.jdbc.Driver  #数据库链接驱动


mybatis:
  mapper-locations: classpath:mapper/*.xml  #配置映射文件
  type-aliases-package: com.example.demo.bean #配置实体类
```
（2）pom.xml文件配置信息



```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>
   <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.5.0</version>
      <relativePath/> <!-- lookup parent from repository -->
   </parent>
   <groupId>com.example</groupId>
   <artifactId>zjtest</artifactId>
   <version>0.0.1-SNAPSHOT</version>
   <name>demo</name>
   <description>Demo project for Spring Boot</description>
   <properties>
      <java.version>1.8</java.version>
   </properties>
   <dependencies>
      <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-jdbc</artifactId>
      </dependency>
      <!--thymeleaf模板引擎配置-->
      <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-thymeleaf</artifactId>
      </dependency>
      <!--Web依赖-->
      <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-web</artifactId>
      </dependency>
      <!--MyBatis配置-->
      <dependency>
         <groupId>org.mybatis.spring.boot</groupId>
         <artifactId>mybatis-spring-boot-starter</artifactId>
         <version>2.1.0</version>
      </dependency>
      <!--MySQL数据库配置-->
      <dependency>
         <groupId>mysql</groupId>
         <artifactId>mysql-connector-java</artifactId>
         <scope>runtime</scope>
      </dependency>
      <!--单元测试配置-->
      <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
      <dependency>
         <groupId>junit</groupId>
         <artifactId>junit</artifactId>
         <version>4.13</version>
         <scope>test</scope>
      </dependency>
   </dependencies>

   <build>
      <plugins>
         <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
               <fork>false</fork> <!-- 不再使用单独进程启动 -->
            </configuration>
         </plugin>
      </plugins>
   </build>

</project>
```
（3）Bean实体类，依据数据库表，生成set和get方法；

**UserBean**

```
package com.example.demo.bean;

public class UserBean {
    private int id;
    private String name;
    private String password;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
```
（4）DAO层访问数据库接口文件： 

**UserMapper**

```
package com.example.demo.dao;

import com.example.demo.bean.UserBean;

public interface UserMapper {

    UserBean getInfo(String name,String password);

}
```
（5）DAO层访问数据库实现文件（需在resource包下创建mapper文件夹，然后再创建一个UserMapper.xml.在application配置文件中mybatis:mapper-locations:对应的就是该文件地址），注意<mapper>标签的namespace属性要填写 访问数据库接口类文件路径：

**UserMapper.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<mapper namespace="com.example.demo.dao.UserMapper">

    <select id="getInfo" parameterType="String" resultType="com.example.demo.bean.UserBean">
        SELECT * FROM user WHERE name = #{name} AND password = #{password}
    </select>

</mapper>
```
（6）Service层业务接口类编写： 

**UserService**

```
package com.example.demo.service.impl;

        import com.example.demo.bean.UserBean;
        import com.example.demo.dao.UserMapper;
        import com.example.demo.service.UserService;
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    //将DAO注入Service层
    @Autowired
    private UserMapper userMapper;

    @Override
    public UserBean loginIn(String name, String password) {
        return userMapper.getInfo(name,password);
    }
}
```
（7）Service层业务实现类编写，注意要注解@Service，注入DAO： 

**UserServiceImpl**

```
package com.example.demo.service.impl;

        import com.example.demo.bean.UserBean;
        import com.example.demo.dao.UserMapper;
        import com.example.demo.service.UserService;
        import org.springframework.beans.factory.annotation.Autowired;
        import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    //将DAO注入Service层
    @Autowired
    private UserMapper userMapper;

    @Override
    public UserBean loginIn(String name, String password) {
        return userMapper.getInfo(name,password);
    }
}
```
（8）项目启动类DemoApplication.java要添加注解@MapperScan项目启动时扫描mapper接口，否则会报错找不到mapper文件：

**DemoApplication.java**

```
package com.example.demo;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.example.demo.dao")
public class DemoApplication {

   public static void main(String[] args) {
      SpringApplication.run(DemoApplication.class, args);
   }

}
```
（9） controller层，注意添加@controller注解，注入Service服务：

**LoginController**

```
package com.example.demo.controller;

import com.example.demo.bean.UserBean;
import com.example.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class LoginController {

    //将Service注入Web层
    @Autowired
    UserService userService;

    @RequestMapping("/login")
    public String show(){
        return "login";
    }

    @RequestMapping(value = "/loginIn",method = RequestMethod.POST)
    public String login(String name,String password){
        UserBean userBean = userService.loginIn(name,password);
        if(userBean!=null){
            return "success";
        }else {
            return "error";
        }
    }

}
```
（10）html文件

![](../../assets/ev8Rjxs0sBHX9o/image_024.bin "")
login.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
<body>
<form role="form" action = "/loginIn" method="post">
    账号：<input type="text" id="name" name = "name"> <br>
    密码：<input type="password" id = "password" name = "password"> <br>
    <input type="submit" id = "login" value = "login">
</form>

</body>
</html>
```
success.html 

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>success</title>
</head>
<body>
<h1>登录成功！</h1>
</body>
</html>
```
 error.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>error</title>
</head>
<body>
<h1>登录失败！</h1>
</body>
</html>
```
## 3.编写测试类
编写测试类，看是否能成功 访问数据库，获取数据库信息：

pom.xml中的测试配置

![](../../assets/ev8Rjxs0sBHX9o/image_025.bin "")
![](../../assets/ev8Rjxs0sBHX9o/image_026.bin "")
编写测试基类

**DemoApplicationTests**

```
package com.example.demo;

import org.junit.After;
import org.junit.Before;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.web.WebAppConfiguration;

@RunWith(SpringRunner.class)
@SpringBootTest
//由于是Web项目，Junit需要模拟ServletContext，因此我们需要给我们的测试类加上@WebAppConfiguration。
@WebAppConfiguration
public class DemoApplicationTests {

   @Before
   public void init() {
      System.out.println("开始测试-----------------");
   }

   @After
   public void after() {
      System.out.println("测试结束-----------------");
   }
}
```
编写login测试类

**LoginTest**

```
package com.example.demo;

import com.example.demo.bean.UserBean;
import com.example.demo.service.UserService;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;

public class LoginTest extends DemoApplicationTests {

    @Autowired
    UserService userService;
    @Test
    public void contextLoads() {
        UserBean userBean = userService.loginIn("zhoujie","zhoujie19941113");
        System.out.println("该用户ID为：");
        System.out.println(userBean.getId());
    }
}
```
了解更多测试： [SpringBoot使用Junit单元测试](https://blog.csdn.net/weixin_39800144/article/details/79241620)

运行测试类，看是否成功获取数据库信息：

![](../../assets/ev8Rjxs0sBHX9o/image_027.bin "")
# 四、运行
运行DemoApplication.java文件，启动项目，无任何WARN警告信息，进入浏览器输入localhost:8080/login

![](../../assets/ev8Rjxs0sBHX9o/image_028.bin "")
![](../../assets/ev8Rjxs0sBHX9o/image_029.bin "")
![](../../assets/ev8Rjxs0sBHX9o/image_030.bin "")

