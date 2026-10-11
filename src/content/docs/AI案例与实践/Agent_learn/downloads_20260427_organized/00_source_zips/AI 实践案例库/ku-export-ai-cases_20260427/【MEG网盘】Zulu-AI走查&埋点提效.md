---
title: "背景及目标"
description: "【MEG网盘】Zulu-AI走查&埋点提效"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\【MEG网盘】Zulu-AI走查&埋点提效.md"
---
【MEG网盘】Zulu-AI走查&埋点提效

#### 🧑‍🏫 案例作者：[@赵雪含](https://ku.baidu-int.com?t=mention&mt=contact&id=c6248950-fcec-11f0-a200-dfe62479dd45)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了MEG网盘通过AI赋能研发，实现UI自动修复和埋点自动生成机制，提升研发效率。AI走查工具通过点选元素、输入修改意见实现UI问题自动识别与修复，埋点生成工具则实现全量埋点自动化生成、校验与插桩。该方案显著减少人工操作，提高走查响应速度和埋点数据质量，使研发人员能专注于核心业务逻辑。
# 背景及目标
通过AI赋能研发，围绕“**自动修复 + 智能验证 + 多角色协同**”三大核心目标，提效链路全流程：

* **搭建 UI 自动修复能力，**引入对话式走查与 UI 替换机制，降低手动改动成本，提高走查响应速度
* **埋点自动生成机制，**全量埋点生成 / 校验 / 查询 / 验证，实现埋点全链路自动化，降低人力成本，提升埋点数据质量与效率

# 效果示例
##### **1. AI走查交互链路**
开始->点选->输入修改意见->保存修改->发起评审->结束

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7be0aabfac874812ac51514f42afae14&docGuid=trHudEuiITtarV "")
使用同一账号，H5页面可在端点选，Web端可同步

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6c90a7fbdbc94ffa9da4ca8c972ee158&docGuid=trHudEuiITtarV "")
输入你的修改需求，支持换图、字体、宽高等修改

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=711b9853bd754b9ea4c82c331f43c1f5&docGuid=trHudEuiITtarV "")
确认保留当前修改，可多次修改，撤销不保留当前修改

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=97035f2bf78847fdb5ea101af56bafa7&docGuid=trHudEuiITtarV "")
完成，结束本次修改，发起评审，关联指定研发

|Web-走查 |NA-走查|
|-|-|
|[附件]|[附件]|

##### **2. 埋点生成交互链路**
开始->AI生成->手动补充->列表确认->AI插桩->发起评审->结束

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ac6752f6e57947188492211fc6d590ab&docGuid=pNNrRUVZEMkAxZ "")
打开面板后，点击【AI埋点按钮】，开始页面级埋点分析

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=64b47f072df549028144aab98969c209&docGuid=pNNrRUVZEMkAxZ "")
AI分析的同时可同时手动【选择页面元素】或【直接输入描述】添加新埋点

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9b2d4a9025d74ae7a627dc33b689a229&docGuid=pNNrRUVZEMkAxZ "")
*【AI生成】和【手动补充】完成后会将埋点配置展示在【待生成埋点列表】

* 确认无误后点击【生成按钮】开始AI插桩

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a58b699e80884f53b46c40a71e0a40ed&docGuid=pNNrRUVZEMkAxZ "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7b1fe890e32c40d4a2bf2310ceab7a64&docGuid=pNNrRUVZEMkAxZ "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=af571af890f7499bb5c142a7f221fc16&docGuid=pNNrRUVZEMkAxZ "")
AI插桩时精准识别【埋点配置文件】与【对应页面文件】按照项目规范生成埋点代码

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=97035f2bf78847fdb5ea101af56bafa7&docGuid=trHudEuiITtarV "")
完成，结束本次修改，发起评审，关联指定研发

# 使用方式
##### **1. npm 包添加**
在项目 `package.json` 中引入走查插件依赖：

```
npm install @baidu/ai-helper-plugin@0.0.1-alpha.14
npm install -g @comate/zulu

"dependencies":{
    "@baidu/ai-helper-plugin":"^0.0.1-alpha.14"
}
```
插件最新版本参考[版本迭代记录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/8MCddZCpuH/Te0jZAd04C/J8RirNr98s0fkA?t=mention&mt=doc&dt=doc)



##### **2. 插件引入配置（vue.config.js）**
Webpack 示例：在 `vue.config.js` 中注册 `AiHelperPlugin`：

```
const { AiHelperPlugin } = require('@baidu/ai-helper-plugin');

module.exports = {
    configureWebpack: {
        plugins: [
            AiHelperPlugin({
                bundler: 'webpack',
                licenseKey: '3858c0d8-ab1c-4dc0-88e1-a31882d617cd', // 去文心快码官网寻找自己的licenseKey
                port: 8091, // 与页面端口不一致即可
                cr: { // 修改最终评审人，百度邮箱前缀
                    reviewer: 'zhaoxuehan'
                }
            })
        ],
    }
}
```


##### **3. 环境启动**
* **开发机启动：**

```
# Node 手动注入
export PATH=/home/bae/noderuntime/bin:$PATH

# 启动开发服务（默认端口 :8080）
npm run serve

# 服务访问示例
http://shangtianhan.bcc-szwg.baidu.com:8080/operation/activitys/traditionalAct/main
```
* **本地调试启动：**本地服务可直接安装并调试插件，无需推送到远端。

```
# 启动开发服务（默认端口 :8080）
npm run serve

# 本地服务示例
http://local.pan.baidu.com:8080/operation/activitys/traditionalAct/main
```
> 为便于走查与代码回写验证，支持在 **本地开发环境** 与 **独立测试环境** 两种方式启动。


# 结果验证
**实验范围：** 共验证 **网盘运营侧2 个项目**，所有验证页面均通过 **AI 走查工具** 完成 **UI 问题识别与修改建议生成**。

**问题修复能力：** 工具可直接修复走查问题约 **85%**，其余为需人工处理的逻辑或代码结构问题。

**效率提升：**

* **UI 侧：** 单页验证耗时平均 **30 min**，传统人工走查约需 **0.5 天/页**，整体节省 **60%+ 时间成本**；同时显著减少人工理解偏差。
* **RD 侧：** 仅需完成环境搭建与代码审核，走查与修复过程自动化执行，释放研发人力以聚焦核心业务逻辑与高复杂度问题。

# Zulu 辅助走查优势
**对业务方（UI）：**

* **提效显著**：可直接通过页面浮层点选元素，描述问题即可自动触发智能修改
* **实时验证**：走查过程可视化，页面热更新反馈，提高走查响应速度与准确率
* **减少沟通成本**：无需再通过截图、走查文档等方式向研发同步问题

**对开发者（RD）：**

* **节省调试与改动时间**：AI 自动生成修改建议与 diff，研发只需审核确认
* **专注核心研发任务**：样式微调、重复性修复交由智能体处理，把时间投入到架构与核心逻辑
* **减少来回沟通**：无需反复确认 UI 意图或复现场景，一次查看即能确认修改

# Zulu 生成埋点代码优势
**对业务方（PM）：**

* **配置更轻量**：无需编写文档或描述事件规则，仅需在页面点选关键元素即可自动生成埋点方案
* **验证更直观**：埋点触发链路实时可视化，页面内即可确认曝光/点击是否存在/生效

**对开发者（RD）：**

* **跳过重复劳动**：AI 自动生成埋点代码，研发只需审核并合入。
* **统一团队规范**：生成代码自动符合团队埋点规范，减少人为偏差与返工

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
