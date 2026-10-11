---
title: "Flux"
description: "目前开源的只有："
date: "2026-04-28"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\Flux\\Flux.md"
---
# Flux
一、介绍前Stability AI 核心成员 Robin Rombach 创立了Black Forest Labs公司，并开源了 FLUX.1系列模型。为了在易用性和模型功能之间取得平衡，FLUX.1 有三个版本：pro（最好的）、dev和schnell：

目前开源的只有：

FLUX.1-dev——官方提供的适用于非商业用途，开源的、经过指导蒸馏的模型FLUX.1-schnell——官方提供的适合本地开发和个人使用，图像生成速度更快的模型 ![](/personal-site-mvp/img/doc-placeholder.svg)

二、结合ComfyUI使用

![](/personal-site-mvp/img/doc-placeholder.svg)

a100机子生成1024*1024的图片，采用dev+fp16，生成时间在11～12秒

三、文生图效果插画风格| prompt | 生成图片 |
| --- | --- |
| Chinese architecture, snow mountain, Buddha statue, sunset, lake, ancient temple, wild geese, pine tree, flat illustration, pastel, poster, ultra hd, 8K, super high detail中国建筑、雪山、佛像、日落、湖泊、古庙、大雁、松树、平面插图、粉彩、海报、超高清、8K、超高清细节 |  |
| The sunset and the lone duck fly together, and the autumn water is the same color as the sky. UTAGAWA HIROSHIGE落霞与孤鹜齐飞，秋水共长天一色 浮世绘风格 |  |
| Full color three-quarter view manga style illustration, of an handsome young chap with mid-length wavy blonde hair and blue eyes, wearing a robe made of white flowers and green leaves, a laurel leaf wreath on his head, he is sitting on a large rock in a summer forest at dusk, a small creek with clear water nearby, soft sun rays shining through trees, neutral warm color tone全彩四分之三视角漫画风格插图，一个英俊的年轻人，有着中等长度的波浪形金发和蓝色眼睛，穿着白色花朵和绿叶制成的长袍，头上戴着月桂叶花环，黄昏时分，他坐在夏日森林里的一块大石头上，附近有一条小溪，清澈的水，柔和的阳光透过树林，中性暖色调 |  |

人物写实风格| prompt | 生成图片 |
| --- | --- |
| medium shot pov photograph of a slim attractive Asian woman, standing at viewer's door, wearing a plain navy blue t-shirt, holding a birthday cake that has text 'Love ma sheen' written with pink fruit jam on it, facing camera, looking at viewer, long straight dark brown hair, smiling slightly, on a sunny day in a European town, town street in the background, center composition, soft diffused natural lighting中等比例的pov照片，一位苗条迷人的亚洲女性站在观众的门口，穿着一件朴素的海军蓝t恤，手里拿着一个生日蛋糕，上面写着“Love ma sheen”和粉红色果酱，面对镜头，看着观众，一头直直的深棕色长发，微微微笑，在一个阳光明媚的欧洲城镇，背景是城镇街道，中心构图，柔和的漫射自然光 |  |
| cinematic medium shot photograph of a fluffy ragdoll cat, standing next to an oven, wearing light blue apron, holding a baking sheet with many letter-shaped cookies, the cookies aligned into text 'Love you everyday', each letter is a cookie, the cat is looking at viewer in a sunny kitchen, the cat has white fur and light grey fur around its face, pale blue eyes一只毛茸茸的布娃娃猫，站在烤箱旁，穿着浅蓝色围裙，拿着一张有许多字母形状饼干的烤盘，饼干排列成“Love you everyday”字样，每个字母都是一块饼干，猫在阳光明媚的厨房里看着观众，猫脸上有白色和浅灰色的皮毛，淡蓝色的眼睛 |  |

建筑物&产品写实风格| prompt | 生成图片 |
| --- | --- |
| A luxurious infinity pool with bright turquoise water surrounded by smooth , white curved walls and arches, the architecture has a minimalist Mediterranean style with clean lines and rounded edges这是一个豪华的无边泳池，明亮的绿松石色海水被光滑的白色弧形墙壁和拱门环绕，建筑具有极简主义的地中海风格，线条简洁，边缘圆润 |  |
| cinematic still close-up photograph of a tall light blue perfume bottle, rectangular luxurious modern design, silver tall cylinder cap, with text 'Parole d'Eau Dans Le Bleu Qui Petille' in cursive on its white label, transparent bottle with pale blue liquid inside, water droplets around the bottle, placed on a metal bench near the sea, at sunny seaside with bright blue sky and ocean in the background一个高高的淡蓝色香水瓶的电影特写照片，矩形豪华的现代设计，银色高筒盖，白色标签上草书写着“Parole d'Eau Dans Le Bleu Qui Petitle”，透明的瓶子里有淡蓝色的液体，瓶子周围有水滴，放在海边的金属长凳上，阳光明媚，背景是明亮的蓝天和大海 |  |
| an inflatable white model of the Arc de Triomphe in Paris, huge and fluffy, drone shot, drone footage, hyper realistic巴黎凯旋门的白色充气模型，巨大而蓬松，无人机拍摄，无人机镜头，超现实 |  |

工业海报| prompt | 生成图片 |
| --- | --- |
| An advertising poster for "Life beyond caused by one self" featuring the brand's SUV model in white color, parked on snowcovered ground with pine trees and mountains behind it. The text is written above or below the car in bold letters. It has an elegant style, with soft lighting and a blue background, in the style of a minimalist design.“超越自我的生活”的广告海报，以该品牌的白色SUV车型为特色，停在白雪覆盖的地面上，后面有松树和山脉。文字以粗体字写在汽车的上方或下方。它具有优雅的风格，柔和的灯光和蓝色的背景，采用极简主义设计风格。 |  |

图标设计| prompt | 生成图片 |
| --- | --- |
| Create a logo icon for a TV station called "KORK" tv. Should be dynamic and sophisticated. Something that will be timeless and strong. On white background.为一家名为“KORK”的电视台创建一个标志图标。应该是动态的和复杂的。一种永恒而强大的东西。在白色背景上。 |  |

四、训练参考：





