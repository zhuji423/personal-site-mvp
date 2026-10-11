---
title: "Maven构建运行Java项目 helloworld"
description: "Maven构建运行Java项目 helloworld"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Maven\\Maven构建运行Java项目 helloworld.md"
---
Maven构建运行Java项目 helloworld



## 
## 一、 **archetype** 插件创建项目
archetype 也就是原型，是一个 Maven 插件，准确说是一个项目模板，它的任务是根据模板创建一个项目结构。

在 MVN 文件夹下创建一个基于 maven 的 java 应用项目。

```
mvn archetype:generate "-DgroupId=org.zj.test" "-DartifactId=test-wordcount" "-DarchetypeArtifactId=maven-archetype-quickstart" "-DinteractiveMode=false"
```
参数说明：

* -DgourpId: 组织名，公司网址 + 项目名称
* -DartifactId: 项目名-模块名
* -DarchetypeArtifactId: 指定 ArchetypeId，maven-archetype-quickstart，创建一个简单的 Java 应用
* -DinteractiveMode: 是否使用交互模式

得到

![](../../assets/EfnO68tIHNvxVq/image_001.bin "")
pom.xml 文件，代码如下，Maven 已经添加了 JUnit 作为测试框架。

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.zj.test</groupId>
  <artifactId>test-wordcount</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>test-wordcount</name>
  <url>http://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```
## 二、构建运行项目
### 2.1 构建
执行以下命令开始构建项目：

```
cd /Users/zhoujie19/IdeaProjects/MVN/test-wordcount
mvn clean package
```
执行完后，构建了项目并创建了最终的 jar 文件

![](../../assets/EfnO68tIHNvxVq/image_002.bin "")
过程：

* maven 的两个目标，首先清理目标目录（clean），然后打包项目构建的输出为 jar（package）文件。
* 打包好的 jar 文件可以在test-wordcount\target 中获得，名称为test-wordcount-1.0-SNAPSHOT.jar。
* 测试报告存放在test-wordcount\target\surefire-reports 文件夹中。
* Maven 编译源码文件，以及测试源码文件。
* 接着 Maven 运行测试用例。
* 最后 Maven 创建项目包。

### 2.2 运行
```
cd /Users/zhoujie19/IdeaProjects/MVN/test-wordcount/target/classes
java org.zj.test.App
```
![](../../assets/EfnO68tIHNvxVq/image_003.bin "")
## 三、添加其他的 Java 文件到项目
创建 Util 类 Util.java

**Util.java**

```
package org.zj.test;

public class Util {
    public static void printMessage(String message){
        System.out.println(message);
    }
}
```
更新 App 类来使用 Util 类

**App.java**

```
package org.zj.test;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Util.printMessage("Hello World2!");
    }
}
```
构建后运行

```
cd /Users/zhoujie19/IdeaProjects/MVN/test-wordcount
mvn clean compile


cd /Users/zhoujie19/IdeaProjects/MVN/test-wordcount/target/classes
java org.zj.test.App
```
![](../../assets/EfnO68tIHNvxVq/image_004.bin "")
## 四、Maven常用命令与插件
Maven是通过pom.xml来执行任务的，其中的build标签描述了如何来编译及打包项目，而具体的编译和打包工作是通过build中配置的 plugin 来完成。当然plugin配置不是必须的，默认情况下，Maven 会绑定以下几个插件来完成基本操作。

[生命周期](https://blog.csdn.net/qq_36761831/article/details/91039311?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.baidujs&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.baidujs)

（1）maven clean

对项目进行清理，清理的过程中会删除删除target目录下编译的内容。

（2）maven compile

编译项目源代码。

（3）maven test

对项目的运行测试。

（4）mvn package

可以打包后的文件存放到项目的 target 目录下，打包好的文件通常都是编译后生成的class文件。

（5）maven install

在本地仓库生成仓库的安装包可以供其他项目引用，同时打包后的文件存放到项目的 target 目录下。

对项目打包有三种打包方式，pom打包，jar包和war包。打包方式在pom.xml文件中进行指定。

pom工程一般是聚合工程，代表父工程，负责管理jar包的版本、maven插件的版本等，主要做统一的依赖管理。

jar包就是普通的打包方式，可以是pom工程的子工程。

war包的都是web工程，是可以直接放到tomcat下运行的工程。

打成pom包和jar包的工程在新建的时候可以不需要制定maven项目的原型，达成war包的项目需要制定maven项目原型，指定的原型通常为maven-archetype-webapp，代表web项目。
