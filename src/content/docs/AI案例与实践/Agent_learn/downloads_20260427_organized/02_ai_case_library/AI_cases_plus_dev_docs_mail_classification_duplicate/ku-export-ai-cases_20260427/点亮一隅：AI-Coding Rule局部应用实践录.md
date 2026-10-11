---
title: "需求"
description: "点亮一隅：AI-Coding Rule局部应用实践录"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\点亮一隅：AI-Coding Rule局部应用实践录.md"
---
点亮一隅：AI-Coding Rule局部应用实践录

#### 🧑‍🏫 案例作者：[@蔡雪婷](https://ku.baidu-int.com?t=mention&mt=contact&id=b93b1c80-fce3-11f0-b36c-e1355fea6a07)
#### 🎬 案例场景：测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文分享了使用AI-Coding Rule进行局部代码优化的实践。初期面对代码风格不一致、变量命名不清晰等问题，通过引入Zulu工具，制定并执行了一系列编码规范，统一了变量命名，重构了冗余代码，提升了代码可维护性，并通过自动化测试验证优化效果，最终实现了代码质量的显著提升。
# 需求
* 初期设计不规范，多人开发代码风格不一致
* 变量命名不清晰，重复定义多
* 重构代码，统一管理变量
* 提升可维护性

# Zulu 使用
### 公式
[流程图]
### 公式代数
##### 【信息检索，学习方法，确认方案】给出背景、框定范围，提出一些问题，让zulu分析问题并寻找其他问题、提出优化方案（，但是不要修改）
### **prompt**
### **效果展示**
这是一个自动化测试case文件，里面定义了对TTS SDK的一些接口、参数的测试；帮我分析一下这个文件里的参数定义，多分析几个test开头的测试函数，我想让这个测试文件里的一些公用变量抽离到@interface里面，录制音频的paramDict这个变量不够具像化，想改成如recordParamDict这种更易懂的并放到@interface里面，result和re两个变量也非常容易混淆，而且现在很多re都是定义在test函数里的，非常松散；帮我看一下这个文件是否有以上问题，还有没有其他的风格问题；并针对这些问题告诉我优化方案，具体怎么操作，但是不要直接修改我的文件

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
这里我觉得方案不够好（我不想把断言检查提取为公共方法），而且步骤不够清晰，因此优化了prompt



### **prompt**
### **效果展示**
不要把断言检查提取为公共方法，将上述的修改方案给出一份详细的按步骤的可执行优化技术方案，并生成一个文件给我（因为对话框里出现代码框的话复制有点麻烦）







![](/personal-site-mvp/img/doc-placeholder.svg "")
---

阅读修改方案后，看起来比较靠谱

##### 【代码对比，获取实现步骤】没有参考的代码，考虑到功能比较简单，此步骤略
##### 【局部测试，确认正确性，关注一个步骤的效果】挑一个测试用例尝试运行rules
### **prompt**
### **效果展示**
```
优化技术方案
变量命名优化
将paramDict统一改为recordParamDict
将分散的re变量统一提取到@interface中
提取常用局部变量到@interface
结构优化
在@interface中添加共享变量
删除重复的局部变量定义
统一结果变量命名
代码组织优化
保持原有断言逻辑不提取
优化测试数据准备方式
增强代码可读性

---
基于以上方案，完成 testNewOnlineAudioCtrl函数的优化，你可以操作testNewOnlineAudioCtrl函数和非test开头的函数
```


分析case发现整体原始测试用例代码行数为112，优化后代码行数为52，减少50%；

但是对于「不设置某参数」的理解有误，需要优化

![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
```
优化技术方案
变量命名优化
将paramDict统一改为recordParamDict
将分散的re变量统一提取到@interface中
提取常用局部变量到@interface
结构优化
在@interface中添加共享变量
删除重复的局部变量定义
统一结果变量命名
代码组织优化
保持原有断言逻辑不提取
优化测试数据准备方式
增强代码可读性
不设置参数就是不设置，不可以设置Null值

---
基于以上方案，完成 testNewOnlineAudioCtrl函数的优化，你可以操作testNewOnlineAudioCtrl函数和非test开头的函数
```


虽然本次没有抽离出公共函数了，但是也可接受，风险更低

![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 【检查代码的正确性，积极利用现有脚本】运行测试用例校验是否有BUG
需连接iOS真机，case执行通过，人工review也没毛病

![](/personal-site-mvp/img/doc-placeholder.svg "")
##### 【加上验证要求，执行余量任务】创建rules文件，运用rules小批量优化测试用例
由于本身就是自动化测试用例，因此修改后直接跑自动化执行即可

### **prompt**
### **效果展示**
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


实际只改了一个函数😢，看来还是有点问题，看这个函数改的没问题，再尝试换个问法进行小批量修改

![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
聪明了，五个全改了😊

![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 【审核代码，确保最终结果正确性】人工CR后提交代码
icoding检测发现存在编码规范问题，再次修改rules（实际上是之前我的编码不规范，大模型学习导致的）

### **prompt**
### **效果展示**
![](/personal-site-mvp/img/doc-placeholder.svg "")


![](/personal-site-mvp/img/doc-placeholder.svg "")


# Rules 经验分享
#### 立规则，定向提质
#### 出代码，增效减错
#### **控风险，防患未然**
* AI自动生成规则初稿，明确开发方向，人工修订--杜忠良/杨青霖/蔡雪婷
* 规则约束AI，聚焦重点，防“幻觉”干扰--杜忠良
* 渐进式策略，动态优化完善规则--孔团结/蔡雪婷
* AI处理重复编码，解放开发者精力--杨哲栋
* 生成标准化模板，规避命名与兼容问题--缪冉
* 统一编码规范，提升团队协作效率--杨哲栋/蔡雪婷
* 赋能AI自动检测线程安全、内存泄漏等深层隐患，提前发现Bug，筑起代码质量防线--缪冉
* 驱动AI总结成功案例，提炼共性经验与模式，高效生成技术文档，加速团队知识沉淀--孔团结



# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
