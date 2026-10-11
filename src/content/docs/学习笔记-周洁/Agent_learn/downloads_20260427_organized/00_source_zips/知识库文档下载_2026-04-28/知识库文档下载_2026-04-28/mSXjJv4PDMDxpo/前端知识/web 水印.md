---
title: "web 水印"
description: "缺点：需要前后端配合，增加了页面请求和服务端资源开销，防攻击能力也较差。"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\前端知识\\web 水印.md"
---
web 水印

## 一、常见实现方案
### 1、简单水印
制作一个半透明的logo图片，设为文章或者表格的背景图片

```
background-image:url("./logo.png");
```
实现图片平铺关键的 `CSS` 属性是 `background-repeat`，值为 `repeat` 时是平铺，这也是它的默认值，所以可以省略。

### 2、全页面水印
避免被图片、视频、控件遮挡，使用一个层级比较高且覆盖整个页面的元素来承载

```
div.watermark{
  position: fixed;
  left:0;
  top:0;
  width: 100vw;
  height: 100vh;
  background-image:url("./logo.png");
  opacity: .5;
  z-index: 3000;
}
```
使该元素“可穿透”，“看得见、摸不着”，不再影响页面操作：

```
pointer-events: none;
```
### 3、动态水印
根据用户信息动态生成水印图片，用于溯源

#### **服务端方案**
页面上发起的图片请求中可以附带用户信息，服务端根据这些参数动态生成图片，并将图片数据作为该请求的响应返给页面，页面拿到后将其用作水印。

缺点：需要前后端配合，增加了页面请求和服务端资源开销，防攻击能力也较差。

#### **Canvas 方案**
`HTML5` 引入 `Canvas` 特性使得浏览器自身具备了绘图能力。可拿到水印图片的 `data URI` 数据，用作水印承载元素的背景图片平铺展示即可。

```
const canvasElement = document.createElement('canvas');
const context = canvasElement.getContext('2d');
canvasElement.width = 200;
canvasElement.height = 200;
context.rotate((-30 * Math.PI) / 180);
context.font = '400 26px Arial';
context.fillStyle = '#B9C0CA';
context.textAlign = 'center';
context.textBaseline = 'middle';
context.fillText('水印文字', 70, 130);
const watermark = canvasElement.toDataURL('image/png');
```
优点：不需要服务端配合，在前端就可以完成，且有助于减少请求和服务端资源开销。曾经面临的浏览器兼容问题现在也不再是问题，该方案已逐渐流行起来。

#### **SVG 方案**
适用于纯文字的水印，可以不生成图片直接实现平铺。

注：动态创建大量 `DOM` 节点，通过 `CSS` 控制排列当然可以实现，但是繁琐且性能差，优雅更无从谈起。

`SVG` 具有文本和图像的双重特性。可以通过 `SVG` 的相关属性精准控制字体位置、大小、颜色、透明度和旋转角度等参数。

```
<svg width="200" height="200" xmlns="">
  <text x="50%" y="50%" font-size="30" fill="#a2a9b6" fill-opacity="0.3" font-family="system-ui, sans-serif" text-anchor="middle" dominant-baseline="middle" transform='rotate(-45, 100 100)'>水印文字</text>
</svg>
```
考虑到浏览器兼容性，用作背景图片时，建议将 `SVG` 编码为 `Base64`（或转义特定字符）:

```
background-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZm9udC1zaXplPSIzMCIgZmlsbD0iI2EyYTliNiIgZmlsbC1vcGFjaXR5PSIwLjMiIGZvbnQtZmFtaWx5PSJzeXN0ZW0tdWksIHNhbnMtc2VyaWYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGRvbWluYW50LWJhc2VsaW5lPSJtaWRkbGUiIHRyYW5zZm9ybT0ncm90YXRlKC00NSwgMTAwIDEwMCknPuawtOWNsOaWh+WtlzwvdGV4dD48L3N2Zz4=");
```
## 二、水印安全
可见水印大都是基于 `DOM` 的，找到这个 `DOM` 节点，通过浏览器插件、抓包工具等在页面上注入一段 `JavaScript` 或者 `CSS` 代码对其进行篡改或删除并不困难。

### 可见水印
防止外部代码篡改，一种思路是把水印元素封装起来，与外部环境进行隔离。

#### **Shadow DOM**
使用 `Element.attachShadow()` 方法来将一个 `shadow root` 附加到任何一个元素上。它接受一个配置对象作为参数，该对象有一个 `mode` 属性，值可以是 `open` 或者 `closed` 。`open` 表示可以通过页面内的 `JavaScript` 方法来获取 `Shadow DOM`。而 `closed` 则表示不可以从外部获取 `Shadow DOM` 。

```
Element.attachShadow({mode: 'closed'});
```
![](/personal-site-mvp/img/docs-assets/image_001_13.png "")
`Shadow DOM` 中的样式本身就是隔离的，除非主动使用 `CSS` 变量、`part` 属性等暴露，外部样式是不会影响到组件内的。

#### **Mutation Observer**
还有一种常见的攻击场景——人为修改，比如在浏览器控制台直接修改或删除对应的 `DOM` 元素。

![](/personal-site-mvp/img/docs-assets/image_002_11.png "")
可以考虑`“监听”`这种行为，一旦发生就马上修复，比如重新插入一个。
`MutationObserver` 就可以用来监听 `DOM` 变动，`DOM` 的任何变动，比如节点的增减、属性的变动、文本内容的变动，通过该 `API` 都可以得到通知。可以使用 `MutationObserver API` 来监听水印元素 `DOM` 变化，一旦监听到 `DOM` 元素被修改或者删除，就立即重新插入一个。

### **不可见水印（盲水印）**
不可见水印通常具有比可见水印更好的隐蔽性和抗攻击性。虽不可见，但通过一定的技术手段是可以将水印信息从其载体上提取出来的，这就使得其载体具备了溯源能力。

`Web` 上基于 `DOM` 的盲水印大都不靠谱，而另一方面数字图像是信息隐藏和数字水印领域研究最多和最早的一种载体，相较于 Web，数字图像领域有着更为成熟的数字水印算法。

但这种水印主要是针对**数字图像**。

#### LSB 水印
灰度图像的一个像素有 `256` 种状态，通常用灰度值（ `0-255` ）表示，`0` 表示黑色，`255` 表示白色，灰度值越大表示亮度越高。

灰度可用一个字节，即 `8` 比特二进制数表示，其中最高位对图像的贡献最大，最低位对图像的贡献最小，称为最低比特位（`Least Significant Bit`，`LSB`）。

比特位越低包含的图像信息就越少，最低位平面类似于随机噪声。因此，改变低位对图像的成像质量影响不大。

`LSB` 水印就是利用了这一点，用水印信息替换载体图像的最低比特位，这样原图像的 `7`个高位平面就与表示水印信息的最低位平面组成了新的图像。

![](/personal-site-mvp/img/docs-assets/image_003_11.png "")
`LSB` 水印鲁棒性（防攻击性）较差，水印信息容易被抹去。

#### 频域水印
在图像频域嵌入水印信息的大致流程为：把原始图像通过离散傅里叶变换转换到频域（变换域），把水印文字信息混入，再经过离散傅里叶变换的逆变换，便得到了载有水印信息的图像。水印信息隐匿性较好。

通常多选择在图像频域的中频部分嵌入信息，因为高频部分易于被各种信号处理方法破坏，而人的视觉又对低频部分比较敏感，容易察觉低频部分的变化。

![](/personal-site-mvp/img/docs-assets/image_004_7.png "")

