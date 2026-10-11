---
title: "CV1qQKpTUy0wjs"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\lib\\req_agent\\ku\\CV1qQKpTUy0wjs.md"
---
测试

### 一、搜A
#### **搜A框架**
|模块|详情|demo|
|-|-|-|
|顶bar|返回：点击后返回上一级页面 新会话入口：点击后唤起新一轮会话，新会话无对话历史，上一轮会话的记录计入首页的「历史」tab 注：每次冷启后，从首页点击对话框则自动开启一轮新对话（可参考DS）；杀App前若用户未手动点击「新会话」，则始终在一个对话轮次里进行问答；|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0ddcb58a0a8d48dbb8ba2fb9b38fdba9&docGuid=iAp4a-vfmO254Q "")|
|页面中元素|问题卡 结果卡 详细需求见下方||
|底bar|对话框 框内展示功能：语音搜索 支持以下方式输入： 打字输入 点击对话框空白处唤起输入面板 语音输入（详细交互见首页部分） 需端上调用语音识别能力转换为文本给策略 ![语音搜索交互](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc008e071c44491faaf4241c201922f6&docGuid=iAp4a-vfmO254Q "语音搜索交互")||
#### **搜A结果页**
[流程图]
##### **问题卡**
|模块|详情|demo|
|-|-|-|
|问|样式：标题样式，参考秘塔 展示内容： 纯文本：左对齐展示即可，无markdown格式|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ca90770f3b0748038e76eed7d260db23&docGuid=iAp4a-vfmO254Q "")|
##### **结果卡：**搜索结果部分+组件挂载
###### loading过程
|环节|第一步|第二步|第三步|
|-|-|-|-|
|示意图|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=72e88612357e476ebd626599e24eaff3&docGuid=iAp4a-vfmO254Q "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=50955f9b14d94babb090a1752b227d68&docGuid=iAp4a-vfmO254Q "")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3390c16b0ccd4c6bb18157cc792a42fa&docGuid=iAp4a-vfmO254Q "")|
|详情|文案：分析问题类型 交互：不可点|文案：全网搜索XX篇资料（XX：由策略返回） 交互：点击后唤起半屏面板，展示引用的所有网站 引用来源半屏面板： 按顺序依次排列引用的网站 仅展示：序号+标题+副标题（若取不到副标题，可不展示） 点击某一网站后使用搜C展示该网站 ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=80e41392345746c4836091f43480128b&docGuid=iAp4a-vfmO254Q "")|文案：搜索完成 交互： loading态全部收起，展示为一行 该部分支持点击，点击后展开，展示「第二步」中的效果|
###### 搜索结果部分（详细策略通路见：[一期策略需求list](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/beG16fCNKV/_YF_tVH3B-/s0VS7Z9NglXsqa#anchor-3fd43ca0-fd66-11ef-a6c7-973c840ce64b?t=mention&mt=doc&dt=doc)）
|结果类型|场景|详情|demo|
|-|-|-|-|
|网址卡|网址直达 Q：www.baidu.com  Q：访问www.baidu.com  Q：进入 www.baidu.com  Q：baidu.com Q：baidu.com Q；https://www.baidu.com ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a42ca245cd69438a88e8fa0a65d72fe2&docGuid=iAp4a-vfmO254Q "")|该环节策略已校验网址域名为正确，无loading过程 展示结构：文本+网址卡 文本（端写死）：「为你找到如下网址：」 网址卡：策略返回网址，前端渲染 网址封面+网址名称+副标题+网址，取分享页的逻辑 可点，点击后使用搜C页展示该网站 展示效果：可使用打字机效果，但速度需要快一点，直给 支持用户长按复制回答的文本内容|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=21f3c07858854b26915f65b6129e7c84&docGuid=iAp4a-vfmO254Q "")|
||其他寻址意图（仅支持单个网址） 关键词示例Q： Q：北京人才网 Q：公积金官网 Q：腾讯首页 Q：化工英才网|该环节策略包含网址域名错误&关键词寻址等其他寻址意图query，含loading过程 展示结构：文本+网址卡+个性化文本（新增）+溯源模块 文本：策略返回 网址卡：策略返回网址，前端渲染 网址封面+网址名称+副标题+网址，取分享页的逻辑 可点，点击后使用搜C页展示该网站 个性化文本：策略单独返回，需对齐技术通路 溯源模块： 展示内容：取策略返回相关性判断后的TOP5相关链接 展示效果：平铺展示索引网址（参考perplexity样式），网址封面+icon+标题 展示策略：最多平铺5个溯源卡 交互：点击平铺的网址后使用搜C页展示三方网址 展示效果：可使用打字机效果，但速度需要快一点 支持用户长按复制回答的文本内容||
|对话式结果|需深度思考 复杂问题分析、推理假设验证、多维度评估、创造性方案场景（推理过程有部分价值增益）|该环节策略已判断为非资源消费&寻址意图，则全部走对话式结果，含loading过程 卡片结构：思考过程+正式回答+溯源模块 思考过程： 组成： 文本：缩进展示，文字置灰 引用超链：在有引用的句子后展示带序号的引用icon，点击后进使用搜C页展示该网址 交互：默认使用展开态展示，生成时页面跟随思考进度中滚动，生成后自动收起 收起态：一行字，文案「已完成深度思考>」，点击后展开全部思考过程 可参考DS，在思考部分左侧增加icon，并播放转圈动效表示正在生成 正式回答： 组成： 文本（需枚举所有格式测试）：支持文字加粗、有序/无序列表、分割线、标题、emoji展示、表格展示，结果中可能内含超链接，需支持加下划线并可点 引用超链：在正文中引用的part后可使用icon展示引用网址，用户点击后使用搜C页展示该网址 溯源模块： 展示内容：取策略返回相关性判断后的TOP5相关链接 展示效果：平铺展示索引网址（参考perplexity样式），网址封面+icon+标题 展示策略：最多平铺5个溯源卡 交互：点击平铺的网址后使用搜C页展示三方网址 打字机效果展示，页面跟随打字的速度滚动展示；若用户滑动页面，则停止跟随，响应用户滑动手势 支持用户长按复制回答的文本内容 页面元素权重：正式回答＞思考过程＞溯源＞loading|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=27f8be4854864c1c9452e6e95b60bcf8&docGuid=iAp4a-vfmO254Q "")|
|影视资源卡 |精准query Q：xxx 在线播放 Q：xxx 免费视频 Q：xxx全集 Q：xxx 最新剧集|该环节策略已判断为资源消费意图，含loading过程 展示文本+资源卡+溯源模块（实则为转码页入口） 文本：策略返回，支持格式同上 正版资源卡： 展示逻辑：在策略返回的资源链接中，寻找白名单域名（爱优腾等），作为该正版卡的展示；若无返回的链接中无白名单中的域名，则该资源卡不展示 基础信息区：影视封面+影视名字+影片类型（电影 or 电视剧）+上映年份+主演（展示两位即可）+（豆瓣评分，看是否可以拿得到）+来源&icon（正版来源） 交互：卡片支持点击，点击播放btn跳转入对应的H5页面 溯源模块： 展示内容：取策略返回的资源链接（踢掉白名单域名） 展示效果：平铺展示索引网址（参考perplexity样式），网址封面+icon+标题 展示策略：最多平铺5个溯源卡 交互：点击平铺的网址后使用搜C转码页播放该资源 支持用户长按复制回答的文本内容|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ee3abaa49b8a4071b868b5b0f3a443d3&docGuid=iAp4a-vfmO254Q "")|
###### 组件挂载（仅在最新返回的结果卡下进行挂载，用户发送新的query，则将上一次结果卡的组件挂载隐藏）
|模块|详情|demo|
|-|-|-|
|重新生成|用户对当前问题回答不满意时，可以触发重新回答（注：仅最近一次生成的结果支持，历史的结果不支持） 一定展示 展示位置：回复卡下方 文案：重新生成 设计样式要求：用户可get功能含义 基本交互： 用户点击重新生成后，当前回复结果全部收起，打字机式生成新的结果，并在对话气泡下方增加「指示器」能力，并且该「指示器」可切换展示不同版本的生成结果 生成的历史内容需记录在首页的「历史」中 策略特殊逻辑：如果第一次回答的结果，未调用深度推理；重新回答时，必须调用深度推理 有效的一次回答结果判断：用户生成到非loading模块的结果，即深度思考 or 正文回答的部分|![重新生成功能示意](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f7aea74f78874242aa4941f83c6091e6&docGuid=iAp4a-vfmO254Q "重新生成功能示意")|
|结果反馈|一定展示 踩：点击「踩」后，icon高亮，展示toast：「感谢您的反馈」||
|复制全文|一定展示 点击复制后，复制当前结果的正文回答部分的文本内容（网址卡&资源卡不被复制），弹出「复制成功」toast||
|猜你想搜（新增）|选择性展示（策略给标识判断是否展示） 展示位置：上述组件挂载下方 展示时机：仅在刚刚返回的结果卡下展示，用户发送新的query后，上一个结果的猜搜组件消失 展示数量：最多三个 交互：点击某一query后，在当前会话中，自动发送该query作为问题，猜你想搜挂载消失，并返回展示结果||
##### **兜底情况**
|场景|详情|demo|
|-|-|-|
|网址卡展示元素缺失|仅网页封面缺失：设计给一张兜底图，正常展示标题+副标题 仅副标题缺失：不展示副标题，正常展示主标题+封面+网址链接 仅主标题缺失 or 缺失两个元素以上：退化为小卡，展示网址链接+兜底封面图即可|![兜底小卡](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4867fc65d2354c1d9ce61cc647d74ad2&docGuid=iAp4a-vfmO254Q "兜底小卡")|
|资源卡展示元素缺失|仅影视封面缺失：设计给一张兜底图 缺失部分影视延展信息（如演员等信息）：设计给兼容的布局规则即可||
##### **停止生成&断网情况**
|场景|详情|demo|
|-|-|-|
|结果生成中停止生成|结果生成时，「语搜」btn变为「停止生成」btn 用户点击「停止生成」btn后，保留已生成的部分结果，在结果下方展示提示文案+组件挂载+再次编辑btn 提示文案：你已停止生成本次回答 再次编辑btn：点击后，自动唤起输入框，并默认展示本次的query，支持用户编辑 or 再次发送 详细交互见下方|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f3d116e0254740f984e49189fea80fe1&docGuid=iAp4a-vfmO254Q "")|
|生成中断网/错误|停止生成，保留已生成的内容（若无内容则直接展示文案），展示文案：「网络错误，请稍后再试」 展示「重试」btn： 该功能区别与组件挂载中的「重新生成」，仅作为生成失败时提供给用户重试 交互：点击后重新判断意图&生成结果|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1f6e138d417e42b792ba20dcfa89959d&docGuid=iAp4a-vfmO254Q "")|
[流程图]
##### **获取地理位置权限**
* 地理位置相关query示例：附近的美食、附近好玩的地方等与精准位置强相关的query
  * 天气等大范围query不调权限弹窗（待与策略确认）
* 弹窗展示频控：弹窗展示的7天后，若用户输入强地理位置相关的query则重复该流程
[流程图]
### 二、搜C
#### 定位&整体交互
|模块|详情|
|-|-|
|定位|页面定位：承载所有来源的落地页 来源： 搜索页： 溯源模块中的网址点击 影视资源卡 网址卡点击 ... 发现列表页点击|
|整体交互|仅百家号落地页支持下滑进新融合沉浸式消费|
#### 落地页需求
##### 第三方网站
|模块|详情|demo|
|-|-|-|
|来源|来源：搜A页中点击所有的第三方网站 溯源模块中的网址点击 网址卡点击 ...|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fb7b2572582a4444a7cec7f46c023021&docGuid=iAp4a-vfmO254Q "")|
|第三方页面|顶bar： 返回：点击后返回上一级页面 回首页：用户点击后，回到首页 页面展示效果：对齐safari展示手机端网页效果即可 若网页加载失败，设计出失败的兜底页面，展示「重新加载」btn，点击后重新加载当前页面（对齐主版） 底bar： 对话框：用户点击后直接进搜A全屏盖住当前页||
##### 新融合落地页
**视频&动态落地页**：基本对齐新融合落地页，但需删减部分功能保证极简体验

###### 1. 新融合落地页（一二跳）
|模块|详情|demo|
|-|-|-|
|顶bar|返回：点击后返回上一级页面 投屏？（看成本） 回首页：用户点击后，回到首页|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3799cff97fe54581b9a5dcdb6f692ec6&docGuid=iAp4a-vfmO254Q "")|
|手势处理|长按屏幕两侧快进，（热区大小同主版？或整个屏幕都做热区） 支持拖动进度条 视频资源：拖动进度条可锚定进度 动态资源：拖动进度条锚定图片（交互同主版） 动态资源支持左右滑消费图片 支持单击暂停/继续播放 屏蔽长按菜单面板||
|视窗布局规则|横版视频&竖版视频的视窗布局规则同主版||
|信息展示|展示位置同线上： 作者头像&昵称：点击后进入号主页，号主页迁移部分功能 标题及展开按钮 视频资源：点「展开」后，标题区上移（对齐线上交互） 动态资源：点「展开」后，调半屏面板展示全部标题，半屏面板中不展示评论区&评论框，且隐藏搜索框；用户关闭半屏面板后再展示搜索框 半屏面板屏蔽「查看原文」btn 横版视频在视窗上方展示标题| ![动态资源点击展开](https://newicafe.baidu.com/rest/v5/attachment/file/stream/21809698 "动态资源点击展开")|
|底bar|对话框：用户点击后直接进搜A全屏盖住当前页面 若用户点击语音搜索，当前资源则暂停播放，待用户语音输入完毕后恢复播放||
|自动连播|视频&动态资源支持自动连播模式，连播逻辑对齐主版||
|合集双btn&短剧特殊卡|合集资源&短剧资源展示合集双btn（逻辑对齐主版）： 选集：点击后进入合集落地页，并调起选集半屏面板，选集半屏面板影藏搜索框 下一集：点击后进入合集落地页，并播放下一集内容 短剧资源：信息区异化为短剧剧集信息（封面+短剧名+集数），同线上 ![](https://newicafe.baidu.com/rest/v5/attachment/file/stream/21803588 "")|![](https://newicafe.baidu.com/rest/v5/attachment/file/stream/21809712 "")|
|横屏播放|横版视频视窗下方展示「全屏观看」按钮，点击后进入横屏播放，横屏下无搜索框 横屏后支持功能： 单击暂停 拖动进度条 投屏功能：看成本是否一期做的上 长按两侧快进 作者头像&昵称：点击后转竖屏进入号主页|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8c840e69265a4f4db1f9bc0f858968e3&docGuid=iAp4a-vfmO254Q "")|
###### 2. 合集落地页
|模块|详情|demo|
|-|-|-|
|顶bar|返回：点击后返回上一级页面 投屏？（看成本） 回首页：用户点击后，回到首页|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=62d6b79e2c144f9e96d915a1f4f35f88&docGuid=iAp4a-vfmO254Q "")|
|合集标题|同线上，展示在顶bar下方 展示文案： 合集：「合集：合集名」 短剧：「短剧：短剧名」||
|手势处理|同新融合落地页||
|视窗布局规则|同新融合落地页||
|信息展示|作者头像&昵称：点击后进入号主页，号主页迁移部分功能 标题及展开按钮：点「展开」后，标题区上移（对齐线上交互）||
|合集挂载|展示位置：标题下方 展示文案：合集名+选集 交互：点击后调起选集半屏面板（交互同线上）||
|底bar|对话框：用户点击后直接进搜A全屏盖住当前页面 若用户点击语音搜索，当前资源则暂停播放，待用户语音输入完毕后恢复播放||
|自动连播|视频&动态资源支持自动连播模式，连播逻辑对齐主版||
|横屏播放|横版视频视窗下方展示「全屏观看」按钮，点击后进入横屏播放，横屏下无搜索框，交互同上||
##### 图文落地页
**图文落地页：保证与新融合落地页的框架基本一致，体验优先**

|模块|详情|demo|
|-|-|-|
|顶bar|返回：点击后返回上一级页面 回首页：用户点击后，回到首页|![](https://newicafe.baidu.com/rest/v5/attachment/file/stream/21809852 "")|
|标题区|展示标题+作者头像+昵称 作者头像&昵称支持点击，点击后进入该作者的号主页||
|正文区|支持展示所有文本格式||
|文中挂载|不展示，全部删掉（考虑到有商品、小说挂载，新端无法承接）| |
|文末挂载|屏蔽||
|底bar|对话框：用户点击后直接进搜A全屏盖住当前页面||
|长按能力|支持正文区长按复制，样式以视觉稿为准 屏蔽长按搜索能力||
|侧滑进号主页|屏蔽||
|评论区|屏蔽不做展示，用户下滑到正文底部后进新融合||
##### 转码页
|模块|详情|demo|
|-|-|-|
|来源|资源消费意图结果卡中的溯源模块，点击任一网址进入对应网站的转码页||
|转码页|页面效果：基本对齐视频新融合容器播放 顶bar： 返回：点击后返回上一级页面 回首页：用户点击后，回到首页 手势处理（对齐新融合落地页）： 长按屏幕两侧快进，（热区大小同主版？或整个屏幕都做热区） 支持拖动进度条 支持单击暂停/继续播放 屏蔽长按菜单面板 信息展示（展示位置同线上）：影视剧名称、当前剧集（即：第XX集，电影则不展示） 视窗布局规则：横版视频&竖版视频的视窗布局规则同主版 功能：支持投屏（考虑成本可不做） 原网页入口：可设计为标签样式，用户点击后将当前页面刷新为转码页的原网址（应法务要求） 进入原网页后，顶bar展示「清爽模式」标签，点击后返回转码页 流畅播能力：详见资源消费部分 底bar： 对话框：用户点击后直接进搜A全屏盖住当前页面 若用户点击语音搜索，当前资源则暂停播放，待用户语音输入完毕后恢复播放用户点击后唤起对话半屏面板，继承之前的对话历史 转横屏： 横版视频视窗下方展示「全屏观看」按钮，点击后进入横屏播放 横屏后支持功能：暂停、拖动进度条、投屏、长按两侧快进 （3.13.新增）特殊交互： 理想方案：上下滑可切换上下集，类比合集二级页（可考虑成本不做） 简版方案：该页面不支持上下滑，用户可在点击挂载在选集面板中切集|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=114dacdebc9c4f018714adc2f3dd8041&docGuid=iAp4a-vfmO254Q "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a2cb30210316403e9cb371397e9d3369&docGuid=iAp4a-vfmO254Q "") ![原网页](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b139db15a94845a6ae0c01a9f43a6cdf&docGuid=iAp4a-vfmO254Q "原网页")|
|选集挂载|电视剧体裁——选集挂载： 文案：选集 展示位置：信息区右侧 交互：点击挂载后可唤起选集半屏面板 半屏面板内： 信息区：影视封面、影视剧名、剧集数、剧集简介、播放源（指该网站内的不同信源）、选集btn（点击后切换对应的剧集播放）|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a3e9a9662dc446a5a8742b8058b0bdf6&docGuid=iAp4a-vfmO254Q "") ![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=31f83baa50414e26a8706f3df79297d5&docGuid=iAp4a-vfmO254Q "")|
||电影体裁—详情挂载： 文案：电影详情 展示位置：信息区右侧 交互：点击挂载后可唤起选集半屏面板 半屏面板内： 信息区：电影封面、电影名、电影简介、播放源、清晰度选择btn（若电影在原网页有区分上下集，则展示上下集btn）||