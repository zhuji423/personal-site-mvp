---
title: "**先瞄准，再开枪（明确目标）**"
description: "测试场景借助skills的工作模式搭建及效果分享"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\测试场景借助skills的工作模式搭建及效果分享.md"
---
测试场景借助skills的工作模式搭建及效果分享

#### 🧑‍🏫 案例作者：[@程亚琳](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：测试、工作流自动化
#### 🔧 使用工具：Ducc
#### 📒 案例概要：根据知识库文档链接生成接口测试用例并执行
[文档目录]
# **先瞄准，再开枪（明确目标）**
**要干什么？**

**要怎么干？**

**需要准备什么？**

我要对接口进行测试

【任务】根据知识库文档链接生成接口测试用例并执行

我想让skills帮我干

[任务]1、解析知识库链接；2、根据知识库内容生成测试用例

我需要两个skill

[任务]1、生成解析知识库链接的skill；2、生成根据知识库内容生成测试用例的skill

# **工欲善其事，必先利其器（借助工具）**
先安装好用的skills，有了好的工具，接下来的活能够事半功倍

[https://github.com/anthropics/skills/blob/main/README.md](https://github.com/anthropics/skills/blob/main/README.md)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5f891349ce8f41d0ab4f7350349671d1&docGuid=vGgqSkiIREhPQC "")
[https://github.com/obra/superpowers/blob/main/README.md](https://github.com/obra/superpowers/blob/main/README.md)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f804a9e695b5411f9227fc58314e1be1&docGuid=vGgqSkiIREhPQC "")
# **先造骨架，再填血肉（创建skill）**
## 1、生成解析知识库链接的skill，baidu-ku-content
在数字员工项目中，写过解析知识库链接的脚本和能力，借助已有的工具，将已有的能力封装为独立的工具+skill

![已有能力的封装](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b2edfda67e0048bea6f4e7ed3720a145&docGuid=vGgqSkiIREhPQC "已有能力的封装")
![已有能力构建的skill](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=936540118bf34e3d9eba58c4a54f1b3e&docGuid=vGgqSkiIREhPQC "已有能力构建的skill")
![使用方式说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8aa2d599a9104d89b79bc65445fe0fff&docGuid=vGgqSkiIREhPQC "使用方式说明")
![直接输入知识库链接，完成解析](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=999eab7e45924e9691eca3875a3c5e54&docGuid=vGgqSkiIREhPQC "直接输入知识库链接，完成解析")
![skill生成完成，分享及复用方式](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bb6d258cbaff4fc083843bcc53499110&docGuid=vGgqSkiIREhPQC "skill生成完成，分享及复用方式")
![baidu-ku-content 结构](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c10a057b04e94339aec41d4f063a3d1a&docGuid=vGgqSkiIREhPQC "baidu-ku-content 结构")
baidu-ku-content 已提交至skills广场，按需安装使用：[https://console.cloud.baidu-int.com/onetool/space/4451/skills/252](https://console.cloud.baidu-int.com/onetool/space/4451/skills/252)



## 2、生成根据知识库内容生成测试用例的skill，api-test-case-generator
从无到有，直接提要求生成skill

![自动调起skill工具superpowers:brainstorming](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3608befbac9447ffbdf85d95485342e5&docGuid=vGgqSkiIREhPQC "自动调起skill工具superpowers:brainstorming")
![确认过程的交互](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d6efca3bd10a4193a1ec070b81858eaa&docGuid=vGgqSkiIREhPQC "确认过程的交互")


![自动调起skill工具superpowers: writing-skills)](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=34e748b931574e35a6aec70f5c6fd9b7&docGuid=vGgqSkiIREhPQC "自动调起skill工具superpowers: writing-skills)")
![skill创建完成及说明](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=24d103502c0e457c9e68fcc1592d5d83&docGuid=vGgqSkiIREhPQC "skill创建完成及说明")


![自动调起skill工具example-skills:skill-creator](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8050f8035b61457aae3cb2b8d4e28dba&docGuid=vGgqSkiIREhPQC "自动调起skill工具example-skills:skill-creator")
![确认过程的交互](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=21ca1257145d411fad9a8f9335dac5f6&docGuid=vGgqSkiIREhPQC "确认过程的交互")
![确认过程的交互](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5fc111bc7aaa46d88daf965717f69775&docGuid=vGgqSkiIREhPQC "确认过程的交互")
![检索到相关的skill](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=62608c6df3d04b54b86fae5538956b2c&docGuid=vGgqSkiIREhPQC "检索到相关的skill")


## 3、使用方式（组合拳开干）
直接抛链接

![直接使用](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=57cdefcbec2242889b4010962506878d&docGuid=vGgqSkiIREhPQC "直接使用")
![输入知识库文档链接，开始任务](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3680c2b9142c4978be0836a00464bbe1&docGuid=vGgqSkiIREhPQC "输入知识库文档链接，开始任务")
![生成测试用例完成](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3deaa7e38b034c37b295c7329583f856&docGuid=vGgqSkiIREhPQC "生成测试用例完成")
![执行用例](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1f8227ce5ec344038a21101d5afc0928&docGuid=vGgqSkiIREhPQC "执行用例")


## 4、用例更新（惊喜功能）
抛链接询问文档变更是否需要调整用例

![接口文档变更对比及用例更新](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e0de7f4564cc4197ade3135786d1ed3b&docGuid=vGgqSkiIREhPQC "接口文档变更对比及用例更新")
![用例更新后自动执行并给出调整部分](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e009197117ee4cf1b5108da91e9b61f6&docGuid=vGgqSkiIREhPQC "用例更新后自动执行并给出调整部分")
# **复盘**
## **好的经验（可复用的方法论）**
1. **确定作用范围：**

    * 项目级工具推荐使用项目级skill

2. **明确需求，不求一步到位**：

    * 根据需求逐步拆解，逐步实现，过程中有走偏的情况及时提出要求改正

3. **借助官方工具**：

    * 推荐安装本文提到的工具（选择其中一个也OK）

## **反模式（需避免的坑）**
1. **skill的触发稳定性不足**

    * 基础的skill工具如果有范围重叠的部分，会随机进行使用。如果没有按照预期触发工具，建议指定skill进行使用

2. **不建议长时间死磕一个任务**

    * 长时间没有生成结果，或存在任务中断，建议重新另起一个终端

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
