---
title: "一、AI生图的演变"
description: "AIGC生图系列分享-第一讲"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AIGC生图系列分享-第一讲.md"
---
AIGC生图系列分享-第一讲

#### 🧑‍🏫 案例作者：[@刘棪](https://ku.baidu-int.com?t=mention&mt=contact&id=30064a60-fcee-11f0-8b70-ed9b10b99124)
#### 🎬 案例场景：设计
#### 🔧 使用工具：Stable Diffusion，Nano Banana，Seedream，Midjourney，Gemini，豆包
#### 📒 案例概要：本文介绍了AI生图技术的演变，包括DALL-E 2、Stable Diffusion等模型的发展，以及文生图技术的核心步骤。还对比了多个AI生图模型的能力与价格，并展示了模型在图像生成质量和应用场景上的差异。此外，探讨了提示词的变化对生成图像的影响，以及一些创意玩法和业务应用场景。
# 一、AI生图的演变
### 从工具产品看
DALL-E 2, Midjourney, Stable Diffusion 相继发布。

Nano Banana Pro, Seedream 4.5, Z-Image...

Gemini, Lovart, 即梦/豆包, 美图/搞定, Figma, Manus...

从生成图像到模拟世界，包括全模态、世界模型、具身智能...

### 从技术架构角度看
**=> 文生图为例，第一个是理解文字输入，第二个是使用这个理解去生成新的图片 <=**

➡️ Stable Diffusion（2022）：VAE的效率、U-Net的精细预测能力、CLIP的语义理解能力“三驾马车”验证了潜在扩散模型在图像生成领域的强大实力与广阔前景。（备注：在DDPM出现之前，图片生成主要是通过变分自编码器(VAE)和生成对抗网络(GAN)来完成的。）

Denoising Diffusion Probabilistic Models (DDPM/Diffusion)：前向扩散过程是不断往输入图片中添加高斯噪声，反向扩散过程是将噪声不断还原为原始图片

![前向扩散过程](/personal-site-mvp/img/doc-placeholder.svg "前向扩散过程")
![反向扩散过程](/personal-site-mvp/img/doc-placeholder.svg "反向扩散过程")
VAE（变分自编码器）是一种生成模型，它通过编码器将输入数据压缩为潜在空间中的概率分布（均值和方差），再从中采样，并由解码器重建数据。训练时，它同时优化重建误差和潜在分布的正则项（KL散度），使潜在空间连续、有结构，从而能生成新样本或进行插值。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
CLIP：是由OpenAI提出的多模态预训练算法，它的主要思想是通过一个超大的图像-文本数据集，来训练一个图像Encoder和一个文本Encoder。如果是相关的文本和图片，编码后的特征向量应该是相似的，如果是不相关的文本和图片，编码后的特征向量应该是不相似的。这个数据集有超过4亿个图片和文本的pair，完全是大力出奇迹。

![CLIP的零样本（Zero-Shot）分类流程实现图文对齐](/personal-site-mvp/img/doc-placeholder.svg "CLIP的零样本（Zero-Shot）分类流程实现图文对齐")
U-Net ➡️ DiT：DiT (Diffusion Transformer) 继承于 ViT 思想，实现从「局部描细节」到「全局拼构图」跃迁。举个栗子，U-Net 画人脸就像先描眉毛再画眼睛，而 DiT 是先把整张脸的比例布局规划好。当你要画「蒙娜丽莎在太空站吃火锅」这种复杂场景时，DiT 的全局把控力就体现出来了。

![基于LVLM的图像编辑流程](/personal-site-mvp/img/doc-placeholder.svg "基于LVLM的图像编辑流程")
![不同生成模型概览](/personal-site-mvp/img/doc-placeholder.svg "不同生成模型概览")
### 从提示词变化看
||**典型例子**|**效果图**|
|-|-|-|
|短语、英文描述为主随机性大，像“开盲盒”|masterpiece, best quality, **1 girl**, **loli**, small breasts, **animal ears**, cute, Age: 12, Height: 145, hair ribbon, cute face, shy, **long hair**, white hair, dress, **illustration**, city
**Negative prompt**: nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, hands
Steps: 40, Sampler: Euler a, CFG scale: 13, Seed: 353263948, Size: 1216x512, Model hash: 6569e224, Clip skip: 2|![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|
|逻辑语句、结构化描述为主可控性和准确性提升显著|**万能公式 = 主体内容 + 场景设定 + 风格参照 + 色彩/色调 + 构图视角 + 附加细节****主体内容**：一位戴着贝雷帽的年轻男烘焙师，身着白色烘焙服，手持裱花袋装饰蛋糕。**场景设定**：白天的烘焙店，透明的玻璃橱柜摆满了各种蛋糕，墙上挂着烘焙工具。**风格**：超清8K写实摄影风格，浅景深虚化处理。**色彩/色调**：暖白与浅棕为主，蛋糕的色彩与烘焙店的温馨背景对比。**构图视角**：45度中景俯拍，橱柜对角线延伸构图。**图片细节**：裱花袋中奶油的挤出，蛋糕上的装饰图案，烘焙服的棉质纹理可见，灯光在蛋糕上的反射，比例 「4:3」|![](/personal-site-mvp/img/doc-placeholder.svg "")|





**微调技术：**

* LoRA：主要用于风格和特征的微调，通过小样本图片微调模型训练角色或特定场景风格
* ControlNet：对图像的特定部分（如线条、深度、姿势等）进行预处理，然后结合提示词进行生成图像，从而实现对图像细节的精确控制。主要在于结构和布局的精确控制

# 二、模型能力对比
|**模型**|**最新版本&时间**|**独特优势**|**价格和最大分辨率**|**功能**|
|-|-|-|-|-|
|Nano Banana|Nano Banana Pro2025.11|强大逻辑推理与语义理解能力，在保持角色/场景高度一致性及复杂提示词的精准还原上处于领先地位|价格：￥0.29-￥0.58分辨率：4K|✅ 参考生图：最多14张✅ 文生图✅ 图片编辑|
|Seedream|Seedream 4.52025.12|生成与编辑一体化的架构，并具备卓越的中文文字渲染与复杂指令遵循能力|价格：￥0.05-￥0.22分辨率：4K|✅ 参考生图：最多10张✅ 文生图✅ 图片编辑|
|Flux|Flux.2系列2025.11|以极致的写实摄影质感和纹理细节著称，并引入了支持多达10张参考图的强力一致性控制|价格：￥0.36-￥0.45分辨率：4K|✅ 参考生图：最多10张✅ 文生图✅ 图片编辑|
|Stable Diffusion|SD 3.52024.10|开源生图，丰富的定制能力，以及有各类专业模型||✅ 文生图✅ 图生图✅ 局部重绘✅ 智能扩展✅ ControlNet/LoRA等|
|Midjourney|V72025.4|“审美”为核心竞争力：拥有最大的设计师群体，并通过获得用户反馈建立审美数据的护城河||✅ 参考生图：最多5张✅ 文生图✅ 图片编辑✅ 语音画图|



# 三、模型效果对比
> Nano Banana Pro更真实更生活，Seedream 4.5适合海报宣传画场景
||**Seedream 4.5**|**Nano Banana Pro**|**Seedream 4.0**|**分析**|
|-|-|-|-|-|
|||![](/personal-site-mvp/img/doc-placeholder.svg "")![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|Seedream: 两个及其以上参考图生成容易出现幻觉|
|![](/personal-site-mvp/img/doc-placeholder.svg "")把图片当中顺丰24h速发改成顺丰48h慢发， 把25mm+改成15nm-，把5A级特等大果改成1A级精品小果。|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|**Seedream 4.5: **图像画面自然，没有出现异常问题，效果优秀。|
|![](/personal-site-mvp/img/doc-placeholder.svg "")把人物的穿搭拆开，放到浅白色背景中，简洁的日系海报风格排版，上方写着“OOTD”的艺术字。|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|**Seedream 4.5: **海报的画面设计效果观感较好，效果优秀。|
|![](/personal-site-mvp/img/doc-placeholder.svg "")基于原图的布偶猫，手绘创作科普风格图像，展示猫的习性（如夜行性、爱清洁、捕猎本能）、特点（身体灵活、感官敏锐、社交属性）、起源（古埃及驯化历史、演化脉络）。采用 “猫形象 + 分栏信息图” 排版，文字清晰易读，搭配简洁图标，配色清新明快，呈现兼具教育性与观赏性的科普海报风格。||![](/personal-site-mvp/img/doc-placeholder.svg "")|![](/personal-site-mvp/img/doc-placeholder.svg "")|gemini-3-pro：生成的图片更加详尽，整体的分布也更加适宜，但是图片底部的中文描述有些瑕疵。seedream-4-0：生成的图片中的图片部分的比重过多，并且文字存在明显畸形，部分字体颜色偏浅|

# 四、其他邪修玩法
> 🍌：[https://gemini.google.com/app](https://gemini.google.com/app)；🫘：[https://www.doubao.com/chat/create-image](https://www.doubao.com/chat/create-image)；即梦：手机APP


1. OOTD穿搭

> **提示词**：把人物的穿搭拆开，放在画面右边浅色背景竖列摆放，左侧粘贴原始参考图
![小红书效果](/personal-site-mvp/img/doc-placeholder.svg "小红书效果")
![参考图](/personal-site-mvp/img/doc-placeholder.svg "参考图")
![生成效果](/personal-site-mvp/img/doc-placeholder.svg "生成效果")
![参考图](/personal-site-mvp/img/doc-placeholder.svg "参考图")
![🫘效果图](/personal-site-mvp/img/doc-placeholder.svg "🫘效果图")
![🍌效果图](/personal-site-mvp/img/doc-placeholder.svg "🍌效果图")
![参考图](/personal-site-mvp/img/doc-placeholder.svg "参考图")
![效果图](/personal-site-mvp/img/doc-placeholder.svg "效果图")
2. 多图融合

> **提示词**：让图1里的女生，穿上图2图3的裙子和衣服，穿上图4的鞋子，跨上图图5的包包，再让女生站在图6的草地上
> **提示词**：一张我站在迪拜国际机场与世界著名足球运动员莱昂内尔·梅西并肩的真实高清照片。我们俩都自然地微笑着，摆出一张随意的照片。我是个年轻女孩，深棕色凌乱的头发，穿着米色裤子、浅奶油色衬衫、长方形黑色太阳镜和背包。莱昂内尔·梅西身穿白色T恤、黑色外套、黑色牛仔裤和运动鞋。背景展示了一个现代玻璃机场航站楼，周围有人。自然光，自然会面的名人氛围，超写实，焦点锐利，专业摄影，4K画质，逼真肤色
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
3. 故事书/连环画制作

> **提示词**：我的女儿奥莉五岁，非常害怕看牙医。请创作一本温暖的故事书，帮助她缓解焦虑。采用柔和的水彩画风，画面明亮温馨。
![我将先为故事设计角色，再根据角色生成分镜图，帮助奥莉缓解看牙医的焦虑。](/personal-site-mvp/img/doc-placeholder.svg "我将先为故事设计角色，再根据角色生成分镜图，帮助奥莉缓解看牙医的焦虑。")
![分镜 1：奥莉抱着小兔子玩偶，坐在沙发上，听到妈妈说 “明天要去看牙医”，她的小脸立刻皱了起来，眼睛里泛起了泪光。](/personal-site-mvp/img/doc-placeholder.svg "分镜 1：奥莉抱着小兔子玩偶，坐在沙发上，听到妈妈说 “明天要去看牙医”，她的小脸立刻皱了起来，眼睛里泛起了泪光。")
![分镜 2：晚上，奥莉躺在床上睡不着，小兔子玩偶在她身边，她想象着牙医诊所里有可怕的工具，吓得用被子蒙住了头。](/personal-site-mvp/img/doc-placeholder.svg "分镜 2：晚上，奥莉躺在床上睡不着，小兔子玩偶在她身边，她想象着牙医诊所里有可怕的工具，吓得用被子蒙住了头。")
![分镜 3：妈妈走进奥莉的房间，坐在床边，温柔地告诉她：“牙医叔叔很温柔，会帮助奥莉保护牙齿，就像给牙齿讲故事一样。”](/personal-site-mvp/img/doc-placeholder.svg "分镜 3：妈妈走进奥莉的房间，坐在床边，温柔地告诉她：“牙医叔叔很温柔，会帮助奥莉保护牙齿，就像给牙齿讲故事一样。”")
![分镜 4：第二天，奥莉和妈妈来到牙医诊所，诊所里有很多彩色的玩具和图画，牙医叔叔戴着微笑的口罩，手里拿着像小喇叭一样的工具，笑着对奥莉说：“你好呀，奥莉！”](/personal-site-mvp/img/doc-placeholder.svg "分镜 4：第二天，奥莉和妈妈来到牙医诊所，诊所里有很多彩色的玩具和图画，牙医叔叔戴着微笑的口罩，手里拿着像小喇叭一样的工具，笑着对奥莉说：“你好呀，奥莉！”")
![第一章：小小担忧     奥莉的牙齿有点疼，她好担心要去看牙医。她的小松鼠朋友闪闪看出了她的不安。 “别怕，奥莉，”闪闪说，“我们一起去一个神奇的地方，那里会让你的牙齿好起来的！”](/personal-site-mvp/img/doc-placeholder.svg "第一章：小小担忧     奥莉的牙齿有点疼，她好担心要去看牙医。她的小松鼠朋友闪闪看出了她的不安。 “别怕，奥莉，”闪闪说，“我们一起去一个神奇的地方，那里会让你的牙齿好起来的！”")
![第二章：微笑森林之旅     闪闪带着奥莉穿过了一片神奇的森林。这里的树叶像牙齿一样白，花朵都在对着他们微笑。他们踩着五颜六色的石头小路，向着一个巨大的牙齿房子](/personal-site-mvp/img/doc-placeholder.svg "第二章：微笑森林之旅     闪闪带着奥莉穿过了一片神奇的森林。这里的树叶像牙齿一样白，花朵都在对着他们微笑。他们踩着五颜六色的石头小路，向着一个巨大的牙齿房子")
![第三章：牙齿仙子的魔法     牙医诊所里竟然住着一位牙齿仙子！她穿着白大褂，背上有一对闪亮的翅膀。奥莉坐上了像火箭一样的椅子，戴上酷酷的太阳镜。仙子阿姨用会吹泡泡的魔法棒轻轻地检查她的牙齿，闪闪在一](/personal-site-mvp/img/doc-placeholder.svg "第三章：牙齿仙子的魔法     牙医诊所里竟然住着一位牙齿仙子！她穿着白大褂，背上有一对闪亮的翅膀。奥莉坐上了像火箭一样的椅子，戴上酷酷的太阳镜。仙子阿姨用会吹泡泡的魔法棒轻轻地检查她的牙齿，闪闪在一")
![第四章：勇敢的奥莉     治疗结束了，奥莉的牙齿再也不疼了！她得到了一个“勇敢的小病人”贴纸和一个小玩具作为奖励。她和闪闪开心地向牙齿仙子挥手告别。 “看牙医一点都不可怕！”奥莉笑着说。天空出现了一](/personal-site-mvp/img/doc-placeholder.svg "第四章：勇敢的奥莉     治疗结束了，奥莉的牙齿再也不疼了！她得到了一个“勇敢的小病人”贴纸和一个小玩具作为奖励。她和闪闪开心地向牙齿仙子挥手告别。 “看牙医一点都不可怕！”奥莉笑着说。天空出现了一")
....

# 五、业务应用场景
1、AIGC图文配图生成

> **美妆下：从内容点击表现上看 AIGC>妙笔>通用uiapi**
> **3C数码下：从内容点击表现上看 AIGC>FE模板>通用uiapi**
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
2、AIGC视频封面生成

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
3、新品会场视频封面生成

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
4、直播 Banner 生成

![](/personal-site-mvp/img/doc-placeholder.svg "")
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
