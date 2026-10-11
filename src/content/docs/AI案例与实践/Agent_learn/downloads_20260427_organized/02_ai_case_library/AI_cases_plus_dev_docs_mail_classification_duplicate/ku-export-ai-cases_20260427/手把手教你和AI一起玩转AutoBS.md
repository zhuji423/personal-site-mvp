---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "手把手教你和AI一起玩转AutoBS"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\手把手教你和AI一起玩转AutoBS.md"
---
手把手教你和AI一起玩转AutoBS

#### 🧑‍🏫 案例作者：[@邢越](https://ku.baidu-int.com?t=mention&mt=contact&id=60c458c0-fceb-11f0-a003-7d5b31265d1b)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Onetool，Comate，Cursor
#### 📒 案例概要：本文介绍了如何使用Comate AI IDE与AutoBS平台结合，通过MCP市场安装和配置iCode、知识库等插件，利用AI助手进行代码审查、数据流分析、AQL修改等任务。详细步骤包括环境搭建、工具配置、数据流拓扑分析、代码修改与验证，实现高效、智能化的网络配置管理。
Comate AI IDE发布后，我惊喜地发现在MCP市场，出现了梦寐以求的iCode、iCafe、知识库，甚至还有Noah。这样的话，曾经毫无交互性的用户手册、排查手册，都可以人机协同了！

抱着试一试的心态，我在开会的夹缝间，经过2天的尝试，竟然跑通了“新增字段”手册的大部分。

### 工具篇


#### 安装Comate AI IDE
*简单到，你不可能说你不会！*



途径一，[官网安装](https://comate.baidu.com/zh/download?track=AIIDEfromBaidu-Int)

途径二，点击度管家 -> 点击“应用魔方” -> 第一页“Comate AI IDE”

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


#### 安装MCP's
*如果不清楚MCP是什么、做什么，你真的已经out了！抓紧去问问文小言/deepseek/豆包*



##### 找到MCP市场
随便打开一个项目（文件夹） -> 右上角打开“AI*” -> 展开选择MCP -> 点击MCP市场 -> 搜索和添加

![打开项目](/personal-site-mvp/img/doc-placeholder.svg "打开项目")
![找到mcp1](/personal-site-mvp/img/doc-placeholder.svg "找到mcp1")
![找到mcp2](/personal-site-mvp/img/doc-placeholder.svg "找到mcp2")


##### 调试已安装MCP
**绿色**才说明“正常”，其他情况下可以反复尝试 “更新全部” 或 切换“启用”，甚至重启AI IDE...

如果还不ok，需要看下mcp执行日志，一般比较好定位问题~

![mcp查看](/personal-site-mvp/img/doc-placeholder.svg "mcp查看")
![mcp日志调试](/personal-site-mvp/img/doc-placeholder.svg "mcp日志调试")


##### icode 
*icode采用最最方便的npx安装方式，配置最少*

点击“添加” -> 会弹出一段代码、直接选择 -> 自动写入到.mcp -> 点击已安装查看 -> 绿色说明ok了！

![一键安装icode](/personal-site-mvp/img/doc-placeholder.svg "一键安装icode")
接下来试试聊天

```
使用username:xingyue,从icode获取代码库下载到当前目录下的子目录，proto-desc代码库：baidu/im-data/proto-desc
```
![icode下载代码库](/personal-site-mvp/img/doc-placeholder.svg "icode下载代码库")


##### 知识库
点击“添加” -> 会弹出一段代码、直接选择 -> 自动写入到.mcp -> 点击已安装查看 -> 绿色还需要配权限！

![安装知识库mcp](/personal-site-mvp/img/doc-placeholder.svg "安装知识库mcp")
配置权限

* 很不幸知识库的 ak/sk，要求你先持有一个数字身份 [🗂️ 知识库开放能力](https://ku.baidu-int.com/d/83jpltYsT1u0cu?t=mention&mt=doc&dt=doc)，并使用该数字身份的 ak/sk。 
* 如果你的团队确实没有，欢迎咨询我们借用。
* 接下来你需要把我们的数字权限，赋予文档“可读”。

填完 ak/sk，并赋予文档权限后，可以正常聊天了（其实AIIDE理解实施能力较Cursor有非常大的差距，见下图对比，不要因为AIIDE对AI灰心丧气...）

```
请读取总结知识库文档 OsDqSjjvKebh6N 的内容，输出给fcstorage winfo层级 新增字段 alabel需要几步
```
![ours(AI IDE)](/personal-site-mvp/img/doc-placeholder.svg "ours(AI IDE)")
![others(Cursor)](/personal-site-mvp/img/doc-placeholder.svg "others(Cursor)")
##### AutoBS
AutoBS平台已发布了MCP 版本。直接编辑.mcp，照猫画虎添加如下内容：

```
"autobs": {
  "command": "npx",
  "args": ["-y", "@baidu/autobs-mcp-server"]
}
```
安装后检查 绿色，就可以聊天了

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
### 应用篇


#### 碎片化协同


##### 理解层级字段
prompt中的知识库文档做了些hack：

* 问题：当前知识库MCP不支持指定分段阅读，只能全篇阅读。数据流说明文档太长了，导致Agent陷入死循环 读全篇->token爆炸->压缩->读全篇->...。
* 解法：[主文档](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/MUyZ7Y-BGz/AJBDUY1sTG/Jv9ciFPXJIaHmo)内是索引，让模型进一步阅读。

```
当前@BizDataTables.proto 里面的field都很不好理解，在知识库DAS接口文档 Jv9ciFPXJIaHmo 中有字段说明，请对应给@BizDataTables.proto 的field加注释。
1.DAS接口文档：
1.1 读取方法：获取文档内容，找到层级对应标题，标题所辖内容包括详情知识库url，从url路径的最后一部分拿到知识库id，获取内容查看该层级详情
1.2 凤巢：知识库 Jv9ciFPXJIaHmo 
2.操作方法：
- 遍历BizDataTables.proto的message，对每个message
  - 在主索引中，通过名字锁定要读取的对应文档doc
  - 阅读doc中字段后，给message的对应field添加注释
  - summarize上下文后再处理下一个message
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 确定D数据类型
```
**必须**通过autobs mcp（而不是本地文件），获得fcstorage模块的D数据类型。
数据流概念
- 模块：module，代表数据订阅者，订阅下游数据
- 下游数据：apptask，某模块在某平台订阅的数据名。内部包含：基准snapshot、增量stream
- 数据和数据类型：数据被订阅，数据背后可能共享相同的数据类型
操作：
    1. D平台下游数据：在 AutoBS平台 找到 fcstorage 模块，确定对应的 PS平台对应的下游数据，从而推导出对应的 D平台对应的下游数据 （PS数据类型_D）
```
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 分析要修改的AQL
```
**必须**通过autobs mcp（而不是本地文件），获得fcstorage检索应用当前的所有AQL和分别的作用。补充重要概念：
应用方面：
- 检索应用：app，代表可部署到线上的检索服务，部署后成为数据订阅者“模块”
- 平台：platform，一个模块/检索应用有多平台
- 数据层级：level
- 数据表：Table，支持ssd表格
- 检索语句：AQL（Ads SQL），声明驼峰（如`FcWinfoSeek`）会生成全大写的（如`FC_WINFO_SEEK`） 
```
![](/personal-site-mvp/img/doc-placeholder.svg "")


##### 获取传输数据类型
```
**必须**通过autobs mcp（而不是本地文件），获得fcstorage模块 PS平台订阅 的 FENGCHAO元素 涉及的数据类型。
数据流概念
- 模块(module)：代表数据订阅者，订阅下游数据
- 下游数据(apptask)：某模块在某平台订阅的数据名。内部包含：基准snapshot、增量stream
- 数据(data)和数据类型(type)：数据被订阅，数据背后可能共享相同的数据类型
操作：

1. 在 AutoBS平台 获取模块`fcstorage`的 “PS平台下游数据”；
2. 计算“PS平台下游数据”的沿途数据：在 AutoBS平台 获取模块`fcstorage`的数据流拓扑。按“收集数据算法”获得 “PS平台下游数据” 的沿途数据：
- 拓扑说明：服务关联其数据输出 input_data ->(服务)-> output_data，一般来说有5~6层：
  - 从数据源服务（source），
  - [optional]经过重分库服务（merger），
  - [2~3层]经过扩散层服务（spread），
  - 经过数据元素（element）集成到 PS平台下游数据（apptask）中，
  - 模块订阅下游数据。
- 收集数据算法：
  - 对下游数据的每一个元素
    - [init]收集该元素的input_data和output_data，把该元素的input_data加入tododata
    - [run]依次弹出tododata设置curdata，直到空
      - 查找output_data=curdata的服务，按','分隔input_data获取input_datas，收集input_datas，并加入tododata

3. 遍历“PS平台下游数据”的每一个沿途数据，
3.1 获取该数据对应的数据类型；

```
BSRD TODO：①未收集基准。

![](/personal-site-mvp/img/doc-placeholder.svg "")


#### 整体完成
以下要求你的IDE和模型能力足够强，从经验来看 Cursor+Claude/Grok 可以执行成功！

```
参考下面操作 在fcstorage模块ps平台的winfo层级中新增material_label2字段：

## 任务目标
1. 在 fcstorage 的 winfo 层级添加字段 `material_label`
2. 修改AQL `FC_WINFO_SEEK` 返回该新加字段

## 相关概念

凤巢：搜索广告检索，也叫FENGCHAO、FC
原生：推荐广告检索，也叫FEED
百青藤：联盟广告检索，也叫BES

## 相关文档

1.DAS接口文档：
1.1 读取方法：获取文档内容，找到层级对应标题，标题所辖内容包括详情知识库url，从url路径的最后一部分拿到知识库id，获取内容查看该层级详情
1.2 凤巢：知识库 Jv9ciFPXJIaHmo 
1.3 原生：知识库 -
1.4 百青藤：知识库 - 
 
## 相关代码库
 
1.1 获取方法：使用username:xingyue，从icode获取代码库下载到当前工作区
1.2 proto-desc代码库：baidu/im-data/proto-desc
1.3 databus-proto代码库：baidu/im-data/databus-proto

## 相关平台

通过autobs mcp，获取 autobs平台信息，覆盖如下核心概念：
应用方面：
- 检索应用：app，代表可部署到线上的检索服务，部署后成为数据订阅者“模块”
- 平台：platform，一个模块/检索应用有多平台
- 数据层级：level
- 数据表：Table，支持ssd表格
- 检索语句：AQL（Ads SQL），声明驼峰（如`FcWinfoSeek`）会生成全大写的（如`FC_WINFO_SEEK`） 
数据流方面：
- 模块：module，代表数据订阅者，订阅下游数据
- 下游数据：apptask，某模块在某平台订阅的数据名。内部包含：基准snapshot、增量stream
- 数据和数据类型：数据被订阅，数据背后可能共享相同的数据类型
**重要**：
① 注意区分”模块“和”检索应用“，用模块查看数据流，用检索应用编码表&AQL。比如`fcstorage`作为模块和检索应用，不仅id不同、detail也不同。

## 实施清单
整体信息流很大，建议：
1. 每个阶段产出记录到文档方便后续查看，并执行"/summarize"压缩上下文；
2. 代码库不要逐行read，而应该grep；

### 阶段1: 需求确认和字段定义

- [ ] **1.1 确定层级&字段**
  - 查看 DAS 接口文档中`winfo` 层级的内容
  - 确认 `winfo` 的层级序号：`winfo` 层级标题中 “Level=<层级序号>; winfo级别相关”，就是winfo的层级序号
  - 确认 `material_label` 字段类型和序号：在winfo层级下的字段表格中，
  -- 字段序号，`material_label`字段对应的“序号/行号”列，如果没有则以proto-desc库中的递增序号为准
  -- 字段类型，`material_label`字段的类型列（uint32, string, bytes, float等）
**重要**：
① 记录层级&字段的序号和类型，后续所有proto中必须一致
② 如果所查找层级或字段在文档中不存在，则提醒“联系DAS RD更新文档”，终止掉流程

### 阶段2: Proto更新

- [ ] **2.1 更新全局描述proto（如需要）**
  - 代码库：`baidu/im-data/proto-desc`
  - 文件：`fc_source.proto`
  - 操作：
    1. 在对应的 message 中添加字段：
    ```protobuf
    message Level_[层级需要] {
        // ... 现有字段 ...
        optional [字段类型] material_label = [字段序号];  // 新增字段
    }
    ```

- [ ] **2.2 更新D数据类型proto**
  - 代码库：`baidu/im-data/databus-proto`
  - 操作：
    1. D平台下游数据：在 AutoBS平台 找到 fcstorage 模块，确定对应的 PS平台对应的下游数据，从而推导出对应的 D平台对应的下游数据 （PS数据类型_D）
    4. 修改D数据类型：**只更新**D平台下游数据的 `data.proto`，添加字段（序号必须与全局描述proto一致）
**重要**：
① 如果所查找 D平台下游数据 中不存在，则提醒“联系BSS RD，请他们确认”，终止掉流程

- [ ] **2.3 提醒“等待databus-proto RB拉出”**
  - 每日晚8点自动拉 RB
  - 在 Databus 平台“类型管理”中，更新 D平台下游数据 的proto版本
  - 点击“生效”

### 阶段3: AutoBS平台配置

在AutoBS平台 找到检索应用`fcstorage`， 并获取 `fcstorage` 检索应用的细节，明确指出待修改点：

- [ ] **3.1 层级配置**
  - 找到 `winfo` 层级内容，
  - 修改增加`material_label` 字段

- [ ] **3.2 表配置**
  - 找到 `WinfoTable` 表格内容，
  - 修改增加`material_label` 字段，
  - 未特别说明，则不需要，否则关注**自定义字段配置**
    - 如需要存储在 SSD

- [ ] **3.3 配置AQL查询（关键步骤）**
  - 找到 `FC_WINFO_SEEK` 的 AQL配置
  - 在 SELECT 子句中添加 `material_label`，列出AQL具体修改前后区别
**注意**：确保字段名与表格配置中的字段名完全一致

- [ ] **3.4 提醒“去Autobs平台完成修改，查看生成CR”**
  - 提交配置后，进入**生成CR**页面
  - 按顺序生成，合入这些CR
    1. databus-proto CR（如需要）
    2. BS CR

### 阶段4: 修改数据流的数据类型
**注意**：严格按拓扑算法执行Topo推导，这样效率最高！否则拉出不需要修改的同级数据，会产生更多无效read&modify。

1. 在 AutoBS平台 获取模块`fcstorage`的 “PS平台下游数据”；
2. 计算“PS平台下游数据”的沿途数据：在 AutoBS平台 获取模块`fcstorage`的数据流拓扑。按“收集数据算法”获得 “PS平台下游数据” 的沿途数据：
- 拓扑说明：服务关联其数据输出 input_data ->(服务)-> output_data，一般来说有5~6层：
  - 从数据源服务（source），
  - [optional]经过重分库服务（merger），
  - [2~3层]经过扩散层服务（spread），
  - 经过数据元素（element）集成到 PS平台下游数据（apptask）中，
  - 模块订阅下游数据。
- 收集数据算法：
  - 对下游数据的每一个元素
    - [init]收集该元素的input_data和output_data，把该元素的input_data加入tododata
    - [run]依次弹出tododata设置curdata，直到空
      - 查找output_data=curdata的服务，按','分隔input_data获取input_datas，收集input_datas，并加入tododata

3. 遍历“PS平台下游数据”的每一个沿途数据，
3.1 获取该数据对应的数据类型；
3.2 修改数据类型，在对应的 message 中添加字段：
- 代码库：`baidu/im-data/databus-proto`
- 操作：修改每个上游数据类型的 `data.proto`，添加字段（序号必须与全局描述proto一致）

4. 更新das proto
- 代码库： baidu/im-data/proto-desc
- 文件：fc.proto
**注意**：层级名称均为level_id

## 关键检查点

### 字段类型一致性检查
- [ ] 所有proto中的字段类型和序号完全一致

```
### 总结篇
* **“Talk is cheap, Show me the Code”**。用程序化语言和AI对话是最高效的，因为程序简洁、具体和逻辑性强。
* **“计算机科学最重要的思想是分治”**。整体来自碎片的组织，和写程序一样，调试好每部分，把共同的抽取出来，就能整体执行。
* **“千里之行始于足下”**。Prompt是新的编程环境和语言，和写CPP一样，选好IDE工具、熟能生巧。

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
