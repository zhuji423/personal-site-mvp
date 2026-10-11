---
title: "Chrome Extensions 插件开发"
description: "Chrome Extensions 插件开发"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Chrome Extensions 插件开发.md"
---
Chrome Extensions 插件开发

## 一、编写一个简单Chrome插件
### 插件开发文件
创建一个新的目录来存放Chrome插件文件。

```
mkdir chrome-extension
cd chrome-extension
```
#### 1、`manifest.json` 配置文件
`manifest.json` 是Chrome插件的配置文件，定义了插件的基本信息、权限、资源等。

```
{
  "manifest_version": 3,
  "name": "My Chrome Extension",
  "version": "1.0",
  "description": "A simple Chrome extension example.",
  "permissions": [
    "activeTab",
    "scripting",
    "storage"
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "images/icon.png",
      "48": "images/icon.png",
      "128": "images/icon.png"
    }
  },
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ]
}
```
#### 2、创建图标
在 `images` 目录下放置插件的图标文件（如 `icon.png`）

![icon.png](/personal-site-mvp/img/docs-assets/image_001.png "icon.png")
#### 3、`popup.html` 插件图标弹出页面
`popup.html` 是点击插件图标时弹出的页面。

```
<!DOCTYPE html>
<html>
<head>
  <title>My Extension Popup</title>
  <style>
    body {
      width: 200px;
      padding: 10px;
    }
  </style>
</head>
<body>
  <h1>Hello, World!</h1>
  <button id="clickMe">Click Me</button>
  <script src="popup.js"></script>
</body>
</html>
```
`popup.js` 是 `popup.html` 的脚本文件，处理弹出页面中的交互逻辑。

```
document.getElementById('clickMe').addEventListener('click', () => {
  alert('Button clicked!');
});
```
#### 4、`background.js` 处理后台任务
`background.js` 是后台脚本，用于处理插件的后台任务。

```
chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed!');
});
```
#### 5、`content.js` 操作网页DOM
`content.js` 是内容脚本，可以操作当前网页的DOM。

```
console.log('Content script loaded!');
```
### 加载插件到Chrome
1. 打开Chrome浏览器，进入 `chrome://extensions/`。启用“开发者模式”。
2. 点击“加载已解压的扩展程序”，选择插件项目目录。

![](/personal-site-mvp/img/docs-assets/image_002.png "")
3. 调试和测试：

    * 使用Chrome开发者工具（F12）调试你的插件。
    * 检查控制台输出，确保没有错误。

![](/personal-site-mvp/img/docs-assets/image_003.png "")
### 发布插件（可选）
如果希望将插件发布到Chrome Web Store，需要：

1. 打包插件（在 `chrome://extensions/` 中点击“打包扩展程序”）。
2. 注册为Chrome Web Store开发者。
3. 提交插件并等待审核。

## 二、复杂的页面翻译插件
### 插件功能
一句话描述功能：翻译页面实时渲染。

[附件: 屏幕录制2025-01-16 下午6.42.36.mov | 3.5MB | video/quicktime | fileId=f1742b8781ec4287bd4aa7149e60811e]
### 准备测试用例
先生成一个测试页面，用来试翻译效果：

![参考截图生成页面代码](/personal-site-mvp/img/docs-assets/image_004.png "参考截图生成页面代码")
|原始页面|插件作用后预期页面|
|-|-|
|![生成测试页面效果](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=98544360ab1f4406a9d3777ba0d3f736&docGuid=Zc9bbvfwmtf9r0 "生成测试页面效果")|![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=170376ab8e8c4474b9fe1a241aeb9d67&docGuid=Zc9bbvfwmtf9r0 "")|
|<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chrome for developers</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Google Sans', Arial, sans-serif;
        }

        body {
            min-height: 100vh;
        }

        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem 2rem;
            border-bottom: 1px solid #eee;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .logo-section img {
            width: 24px;
            height: 24px;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            align-items: center;
        }

        .right-section {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .main-nav {
            border-bottom: 1px solid #eee;
            padding: 0 2rem;
        }

        .main-nav ul {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .main-nav a {
            display: block;
            padding: 1rem 0;
            text-decoration: none;
            color: #5f6368;
        }

        .main-content {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .content-left {
            flex: 1;
        }

        .content-right {
            flex: 1;
            display: flex;
            justify-content: center;
        }

        h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            color: #202124;
        }

        p {
            font-size: 1.2rem;
            color: #5f6368;
            margin-bottom: 2rem;
        }

        .buttons {
            display: flex;
            gap: 1rem;
        }

        .btn {
            padding: 0.8rem 1.5rem;
            border-radius: 24px;
            text-decoration: none;
            font-weight: 500;
        }

        .btn-primary {
            background-color: #1a73e8;
            color: white;
        }

        .btn-secondary {
            border: 1px solid #1a73e8;
            color: #1a73e8;
        }

        .extension-icon {
            width: 300px;
            height: 300px;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="logo-section">
            <img src="https://www.gstatic.com/images/branding/product/1x/chrome_48dp.png" alt="Chrome logo">
            <span>chrome for developers</span>
        </div>
        <nav class="nav-links">
            <a href="#">Get inspired</a>
            <a href="#">Blog</a>
            <a href="#">Docs</a>
            <a href="#">New in Chrome</a>
        </nav>
        <div class="right-section">
            <input type="search" placeholder="Search">
            <button>Theme</button>
            <select>
                <option>English</option>
            </select>
            <a href="#">Sign in</a>
        </div>
    </header>

    <nav class="main-nav">
        <ul>
            <li><a href="#" style="color: #1a73e8; border-bottom: 2px solid #1a73e8;">Overview</a></li>
            <li><a href="#">Get Started</a></li>
            <li><a href="#">Develop</a></li>
            <li><a href="#">How To</a></li>
            <li><a href="#">AI</a></li>
            <li><a href="#">Reference</a></li>
            <li><a href="#">Samples</a></li>
            <li><a href="#">Chrome Web Store</a></li>
        </ul>
    </nav>

    <main class="main-content">
        <div class="content-left">
            <h1>Welcome to Extensions!</h1>
            <p>Make Chrome more powerful by customizing the browser to your needs.</p>
            <div class="buttons">
                <a href="#" class="btn btn-primary">Start building</a>
                <a href="#" class="btn btn-secondary">Publish to the Web Store</a>
            </div>
        </div>
        <div class="content-right">
            <svg class="extension-icon" viewBox="0 0 100 100">
                <path fill="#4285F4" d="M50,0 L75,25 L75,75 L50,100 L25,75 L25,25 Z"/>
                <path fill="#34A853" d="M0,25 L25,25 L25,75 L0,75 Z"/>
                <path fill="#EA4335" d="M75,25 L100,25 L100,75 L75,75 Z"/>
                <path fill="#FBBC04" d="M25,75 L75,75 L75,100 L25,100 Z"/>
                <rect fill="white" x="35" y="35" width="30" height="30"/>
            </svg>
        </div>
    </main>
</body>
</html>||

### 开发翻译插件
#### 1、简单的插件渲染页面
##### popup.html插件页面
![](/personal-site-mvp/img/docs-assets/image_005.png "")
```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>Page Translator</title>
  <script src="lib/crypto-js.min.js"></script>
  <script src="lib/fanyi.js"></script>
  <script src="popup.js"></script>
  <style>
    body {
      width: 300px;
      padding: 15px;
      font-family: Arial, sans-serif;
    }
    .container {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    .language-group {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    .language-group label {
      font-size: 14px;
      color: #333;
    }
    select, button {
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #ccc;
    }
    button {
      background-color: #1a73e8;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #1a73e8d4;
    }
   
  </style>
</head>
<body>
  <div class="container">
    <div class="language-group">
      <label for="sourceLanguage">原始语言：</label>
      <select id="sourceLanguage">
        <option value="auto">自动检测</option>
        <option value="zh">简体中文</option>
        <option value="cht">繁体中文(繁體中文）</option>
        <option value="en">英语（English）</option>
        <option value="jp">日语（日本語）</option>
        <option value="kor">韩语（한국어）</option>
        <option value="fra">法语（Français）</option>
        <option value="spa">西班牙语（Español）</option>
        <option value="th">泰语（ภาษาไทย）</option>
        <option value="ara">阿拉伯语（العربية）</option>
        <option value="ru">俄语（Русский）</option>
        <option value="pt">葡萄牙语（Português）</option>
        <option value="de">德语（Deutsch）</option>
        <option value="it">意大利语（Italiano）</option>
        <option value="el">希腊语（Ελληνικά）</option>
        <option value="nl">荷兰语（Nederlands）</option>
        <option value="pl">波兰语（Polski）</option>
        <option value="bul">保加利亚语（Български）</option>
        <option value="est">爱沙尼亚语（Eesti）</option>
        <option value="dan">丹麦语（Dansk）</option>
        <option value="fin">芬兰语（Suomi）</option>
        <option value="cs">捷克语（Čeština）</option>
        <option value="rom">罗马尼亚语（Română）</option>
        <option value="slo">斯洛文尼亚语（Slovenščina）</option>
        <option value="swe">瑞典语（Svenska）</option>
        <option value="hu">匈牙利语（Magyar）</option>
        <object value="vie">越南语（Tiếng Việt）</object>
      </select>
    </div>
    <div class="language-group">
      <label for="targetLanguage">目标语言：</label>
      <select id="targetLanguage">
        <option value="zh">简体中文</option>
        <option value="cht">繁体中文(繁體中文）</option>
        <option value="en">英语（English）</option>
        <option value="jp">日语（日本語）</option>
        <option value="kor">韩语（한국어）</option>
        <option value="fra">法语（Français）</option>
        <option value="spa">西班牙语（Español）</option>
        <option value="th">泰语（ภาษาไทย）</option>
        <option value="ara">阿拉伯语（العربية）</option>
        <option value="ru">俄语（Русский）</option>
        <option value="pt">葡萄牙语（Português）</option>
        <option value="de">德语（Deutsch）</option>
        <option value="it">意大利语（Italiano）</option>
        <option value="el">希腊语（Ελληνικά）</option>
        <option value="nl">荷兰语（Nederlands）</option>
        <option value="pl">波兰语（Polski）</option>
        <option value="bul">保加利亚语（Български）</option>
        <option value="est">爱沙尼亚语（Eesti）</option>
        <option value="dan">丹麦语（Dansk）</option>
        <option value="fin">芬兰语（Suomi）</option>
        <option value="cs">捷克语（Čeština）</option>
        <option value="rom">罗马尼亚语（Română）</option>
        <option value="slo">斯洛文尼亚语（Slovenščina）</option>
        <option value="swe">瑞典语（Svenska）</option>
        <option value="hu">匈牙利语（Magyar）</option>
        <object value="vie">越南语（Tiếng Việt）</object>
      </select>
    </div>
    <button id="translateBtn">翻译页面</button>
  </div>
</body>
</html>
```
##### popup.js执行脚本
这里先用固定值来模拟翻译，点击翻译按钮后：

![](/personal-site-mvp/img/docs-assets/image_006.png "")
核心逻辑是通过浏览器扩展 API 获取当前页面的内容，并递归遍历页面中的文本节点，使用模拟的翻译函数对文本进行翻译并替换原文本。

```
document.addEventListener('DOMContentLoaded', function () {
    const translateBtn = document.getElementById('translateBtn');
    const sourceLanguage = document.getElementById('sourceLanguage');
    const targetLanguage = document.getElementById('targetLanguage');

    translateBtn.addEventListener('click', function () {
        console.log('Translate button clicked');
        // 获取当前活动标签页
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            if (chrome.runtime.lastError) {
                console.error('Error getting active tab:', chrome.runtime.lastError);
                return;
            }

            // 获取用户选择的语言
            const config = {
                sourceLanguage: sourceLanguage.value,
                targetLanguage: targetLanguage.value,
            };

            // 在当前标签页执行脚本
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: translatePageText,
                args: [config]
            }).catch(error => {
                console.error('Error executing script:', error);
            });
        });
    });
});

// 翻译页面文本的函数
function translatePageText(config) {
    console.log('Translating page text with config:', config);

    // 调用 Translate API
    function translateText(text, sourceLanguage, targetLanguage) {
        // 模拟翻译逻辑
        return new Promise((resolve) => {
            // 模拟异步翻译逻辑
            setTimeout(() => {
                resolve(' (翻译)');
            }, 100); // 模拟异步延迟
        });
    }

    // 遍历文档中的所有文本节点
    function walkText(node) {
        if (node.nodeType === 3) { // Text node
            if (node.nodeValue.trim() !== '') {
                translateText(node.nodeValue, config.sourceLanguage, config.targetLanguage).then(translatedText => {
                    node.nodeValue = node.nodeValue + ' ' + translatedText;
                });
            }
        } else {
            // 跳过脚本和样式标签
            if (node.nodeName !== 'SCRIPT' && node.nodeName !== 'STYLE') {
                for (let child of node.childNodes) {
                    walkText(child);
                }
            }
        }
    }

    try {
        walkText(document.body);
        console.log('Page text modification completed');
    } catch (error) {
        console.error('Error while modifying page text:', error);
    }
}
```
#### 2、页面状态切换(翻译-原始)
[附件: 屏幕录制2025-01-15 下午4.46.03.mov | 1.8MB | video/quicktime | fileId=bc425376dbb642ebafcf1da2e8d01077]
##### popup.js执行脚本
* 翻译与原文切换：
    * 新增了一个翻译状态跟踪 `isTranslated_${tabId}`，用于跟踪不同标签是否已经翻译，页面刷新置于false，页面关闭时删除。
    * 点击按钮时，动态更新按钮文本：“翻译页面”、“显示原文”。
    * 根据翻译状态，决定执行翻译函数 (`translatePageText`) 还是恢复原文函数 (`restoreOriginalText`)。

* 保存与恢复原文：
    * 新增了一个全局数组 `originalTexts`，用于保存页面中每个文本节点的原文内容。
    * 新增了一个函数 `restoreOriginalText`，用于将页面文本恢复为原文。

* 优化交互：
    * 点击按钮后插件页面自动消失（因此需要使用 `chrome.storage.local` 将翻译状态持久化，确保在插件页面重新打开时能够记住之前的状态）


```
document.addEventListener('DOMContentLoaded', function () {
    const translateBtn = document.getElementById('translateBtn');
    const sourceLanguage = document.getElementById('sourceLanguage');
    const targetLanguage = document.getElementById('targetLanguage');

    // 获取当前活动标签页
    getActiveTab().then(async (tabs) => {
        const tabId = tabs[0].id;

        // 从存储中获取当前标签页的 isTranslated 状态
        const result = await chrome.storage.local.get([`isTranslated_${tabId}`]);
        let isTranslated = result[`isTranslated_${tabId}`] || false; // 默认值为 false
        console.log(`Current isTranslated state for tab ${tabId}:`, isTranslated);

        updateButtonText(isTranslated);

        translateBtn.addEventListener('click', async function () {
            try {
                const config = {
                    sourceLanguage: sourceLanguage.value,
                    targetLanguage: targetLanguage.value,
                };

                await executeScript(tabId, isTranslated ? restoreOriginalText : translatePageText, isTranslated ? [] : [config]);

                // 切换状态并保存到存储中
                isTranslated = !isTranslated;
                await saveTranslationState(tabId, isTranslated);

                updateButtonText(isTranslated); // 更新按钮文本
                window.close(); // 关闭插件页面
            } catch (error) {
                console.error('Error during translation process:', error);
            }
        });
    });

    // 获取当前活动标签页
    function getActiveTab() {
        return new Promise((resolve, reject) => {
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                if (chrome.runtime.lastError) {
                    reject(chrome.runtime.lastError);
                } else {
                    resolve(tabs);
                }
            });
        });
    }

    // 执行脚本
    function executeScript(tabId, func, args) {
        return chrome.scripting.executeScript({
            target: { tabId },
            func,
            args
        }).catch(error => {
            console.error('Error executing script:', error);
            throw error;
        });
    }

    // 保存翻译状态
    function saveTranslationState(tabId, isTranslated) {
        return new Promise((resolve) => {
            const state = {};
            state[`isTranslated_${tabId}`] = isTranslated;
            chrome.storage.local.set(state, function () {
                console.log(`isTranslated state saved for tab ${tabId}:`, isTranslated);
                resolve();
            });
        });
    }

    // 更新按钮文本的函数
    function updateButtonText(isTranslated) {
        translateBtn.textContent = isTranslated ? '显示原文' : '翻译页面';
    }
});

// 保存原文内容
let originalTexts = [];

// 翻译页面文本的函数
async function translatePageText(config) {
    console.log('Translating page text with config:', config);

    // 模拟翻译逻辑
    async function translateText(text, sourceLanguage, targetLanguage) {
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve(' (翻译)');
            }, 100); // 模拟异步延迟
        });
    }

    // 遍历文档中的所有文本节点
    function walkText(node) {
        if (node.nodeType === 3) { // Text node
            if (node.nodeValue.trim() !== '') {
                originalTexts.push({ node, originalText: node.nodeValue }); // 保存原文
                translateText(node.nodeValue, config.sourceLanguage, config.targetLanguage).then(translatedText => {
                    node.nodeValue = node.nodeValue + ' ' + translatedText;
                });
            }
        } else if (node.nodeName !== 'SCRIPT' && node.nodeName !== 'STYLE') {
            for (let child of node.childNodes) {
                walkText(child);
            }
        }
    }

    try {
        originalTexts = []; // 清空之前的原文内容
        walkText(document.body);
        console.log('Page text modification completed');
    } catch (error) {
        console.error('Error while modifying page text:', error);
    }
}

// 恢复原文的函数
function restoreOriginalText() {
    try {
        originalTexts.forEach(({ node, originalText }) => {
            node.nodeValue = originalText; // 恢复原文
        });
        console.log('Original text restored');
    } catch (error) {
        console.error('Error while restoring original text:', error);
    }
}
```
##### content.js
避免翻译后页面刷新，翻译状态还停留在已翻译，每次刷新都需要重置翻译状态。

`chrome.tabs` API 是一个高权限的 API，只能在 后台脚本（background script） 或 弹出页脚本（popup script） 中使用，而不能在内容脚本中直接使用。

```
console.log('Content script loaded');

// 向 Service Worker 发送消息，请求当前标签页的 ID
chrome.runtime.sendMessage({ action: 'getActiveTabId' }, function (response) {
    if (response && response.tabId) {
        const activeTabId = response.tabId;
        console.log('Active tab ID:', activeTabId);

        // 将存储中 `isTranslated_${tabId}` 的状态设置为 false
        chrome.storage.local.set({ [`isTranslated_${activeTabId}`]: false }, function () {
            console.log(`isTranslated_${activeTabId} set to false`);
        });
    } else {
        console.error('Failed to get active tab ID');
    }
});

```
##### background.js
```
// 监听来自内容脚本的消息
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'getActiveTabId') {
    // 获取当前激活的标签页 ID
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      if (tabs.length > 0) {
        const activeTabId = tabs[0].id;
        sendResponse({ tabId: activeTabId }); // 返回标签页 ID
      } else {
        sendResponse({ error: 'No active tab found' });
      }
    });
    return true; // 保持消息通道打开，以便异步发送响应
  }
});

// 监听标签页关闭事件
chrome.tabs.onRemoved.addListener(function (tabId) {
  // 清理存储中对应的 `isTranslated` 状态
  chrome.storage.local.remove(`isTranslated_${tabId}`, function () {
      console.log(`isTranslated_${tabId} removed from storage`);
  });
});
```
注意：更改配置文件manifest.json或background.js、content.js需要重新加载插件

![](/personal-site-mvp/img/docs-assets/image_007.png "")
只更改popup.js、popup.html页面效果会实时更新

#### 3、拆分模块、引入库
将翻译函数单独放在一个lib/fanyi.js文件里，并在翻译函数中调用crypto-js库的CryptoJS

注释掉popup.js中的翻译函数：

```
// // 模拟翻译逻辑
// async function translateText(text, sourceLanguage, targetLanguage) {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             resolve(' (翻译)');
//         }, 100); // 模拟异步延迟
//     });
// }
```
新建lib/fanyi.js

```
// 模拟翻译逻辑
async function translateText(text, sourceLanguage, targetLanguage) {
    console.log(CryptoJS.MD5(text).toString());  // 使用 lib/crypto-js.min.js 中的 CryptoJS
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(' (翻译)');
        }, 100); // 模拟异步延迟
    });
}
```
下载[crypto-js.min.js](https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js)放在lib/crypto-js.min.js

在popup.html中引入（注意顺序）：

```
  <script src="lib/crypto-js.min.js"></script>
  <script src="lib/fanyi.js"></script>
  <script src="popup.js"></script>
```
![](/personal-site-mvp/img/docs-assets/image_008.png "")
在配置manifest.json中引入子模块lib/fanyi.js与外部库lib/crypto-js.min.js

```
{
  "manifest_version": 3,
  "name": "Page Transformer",
  "version": "1.0",
  "description": "Transform the current page into a predefined layout.",
  "permissions": [
    "activeTab",
    "scripting",
    "storage"
  ],
  "host_permissions": [
    "<all_urls>"
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "images/icon.png",
      "48": "images/icon.png",
      "128": "images/icon.png"
    }
  },
  "web_accessible_resources": [
    {
      "resources": ["lib/crypto-js.min.js", "lib/fanyi.js"],
      "matches": ["<all_urls>"]
    }
  ],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["lib/crypto-js.min.js", "lib/fanyi.js", "content.js"]
    }
  ]
}
```
#### 4、调用API进行翻译
翻译api使用的百度翻译（免费额度100万字符/月，需要申请下基本都能秒过）： [http://api.fanyi.baidu.com/doc/21](http://api.fanyi.baidu.com/doc/21)

先测下接口能用不：

```
// 引入 crypto-js 库
const CryptoJS = require('crypto-js');

// 百度翻译 API 的配置
const appid = ''; // 替换为你的百度翻译 APPID
const key = ''; // 替换为你的百度翻译密钥
const apiUrl = 'https://fanyi-api.baidu.com/api/trans/vip/translate';

// 生成随机数
function generateSalt() {
    return Math.floor(Math.random() * 10000).toString();
}

// 生成签名
function generateSign(q, salt) {
    const str = appid + q + salt + key;
    // 使用 lib/crypto-js.min.js 中的 CryptoJS 进行 MD5 加密
    return CryptoJS.MD5(str).toString();
}

// 翻译函数，包含缓存逻辑
async function translateText(text, sourceLanguage, targetLanguage) {
    console.log('Translating text:', text);
    return new Promise((resolve, reject) => {
        // 调用百度翻译 API
        const salt = generateSalt();
        const sign = generateSign(text, salt);
        console.log(sign);

        const params = new URLSearchParams();
        params.append('q', text);
        params.append('from', sourceLanguage); // 源语言设置为自动检测
        params.append('to', targetLanguage);
        params.append('appid', appid);
        params.append('salt', salt);
        params.append('sign', sign);

        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: params,
        })
            .then(response => response.json())
            .then(data => {
                if (data.error_code) {
                    throw new Error(`Baidu Translate API error: ${data.error_code}`);
                }
                const translatedText = data.trans_result[0].dst;
                console.log('[API]from:', text, 'to:', translatedText);
            })
            .catch(error => {
                console.error('Error translating text:', error);
                reject(error);
            });
    });
}


// 示例使用
translateText('Hello, world!', 'auto', 'zh').then(translatedText => {
    console.log('Translated text:', translatedText);
}).catch(error => {
    console.error('Error translating text:', error);
});

```
运行：

```
npm install crypto-js
node bd.js
```
![能用](/personal-site-mvp/img/docs-assets/image_009.png "能用")
修改fanyi.js:

```
// 百度翻译 API 的配置
const appid = ''; // 替换为你的百度翻译 APPID
const key = ''; // 替换为你的百度翻译密钥
const apiUrl = 'https://fanyi-api.baidu.com/api/trans/vip/translate';

// 生成随机数
function generateSalt() {
    return Math.floor(Math.random() * 10000).toString();
}

// 生成签名
function generateSign(q, salt) {
    const str = appid + q + salt + key;
    // 使用 lib/crypto-js.min.js 中的 CryptoJS 进行 MD5 加密
    return CryptoJS.MD5(str).toString();
}

// 翻译函数，包含缓存逻辑
async function translateText(text, sourceLanguage, targetLanguage) {
    return new Promise((resolve) => {
        // 调用百度翻译 API
        const salt = generateSalt();
        const sign = generateSign(text, salt);

        const params = new URLSearchParams();
        params.append('q', text);
        params.append('from', sourceLanguage); // 源语言设置为自动检测
        params.append('to', targetLanguage);
        params.append('appid', appid);
        params.append('salt', salt);
        params.append('sign', sign);

        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: params,
        })
            .then(response => response.json())
            .then(data => {
                if (data.error_code) {
                    throw new Error(`Baidu Translate API error: ${data.error_code}`);
                }
                const translatedText = data.trans_result[0].dst;
                resolve(translatedText); 
            })
            .catch(error => {
                console.error('Error translating text:', error.message);
            });
    });
}
```
为了保证翻译api调用不频繁，修改popup.js中的walkText函数：这里限定使用每 0.12 秒调用一次（结合具体qps设定）

```
// 遍历文档中的所有文本节点
function walkText(node) {
    if (node.nodeType === 3) { // Text node
        if (node.nodeValue.trim() !== '') {
            originalTexts.push({ node, originalText: node.nodeValue }); // 保存原文
            // 使用 setTimeout 延迟调用 translateText
            setTimeout(() => {
                translateText(node.nodeValue, config.targetLanguage).then(translatedText => {
                    node.nodeValue = node.nodeValue + ' ' + translatedText;
                });
            }, originalTexts.length * 150); // 每 0.12 秒调用一次
        }
    } else if (node.nodeName !== 'SCRIPT' && node.nodeName !== 'STYLE') {
        for (let child of node.childNodes) {
            walkText(child);
        }
    }
}
```
同时为了防止跨域错误，在配置manifest.json的permissions中引入declarativeNetRequest、declarativeNetRequestWithHostAccess：

```
{
  "manifest_version": 3,
  "name": "Page Transformer",
  "version": "1.0",
  "description": "Transform the current page into a predefined layout.",
  "permissions": [
    "activeTab",
    "scripting",
    "storage",
    "declarativeNetRequest", 
    "declarativeNetRequestWithHostAccess"
  ],
  "host_permissions": [
    "<all_urls>"
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "images/icon.png",
      "48": "images/icon.png",
      "128": "images/icon.png"
    }
  },
  "web_accessible_resources": [
    {
      "resources": ["lib/crypto-js.min.js", "lib/fanyi.js"],
      "matches": ["<all_urls>"]
    }
  ],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["lib/crypto-js.min.js", "lib/fanyi.js", "content.js"]
    }
  ]
}
```
同时在background.js中加入跨域规则：

```
// 定义规则以修改响应头
const rule = {
  id: 1,
  priority: 1,
  action: {
    type: "modifyHeaders",
    responseHeaders: [
      { header: "Access-Control-Allow-Origin", operation: "set", value: "*" }
    ]
  },
  condition: {
    urlFilter: "*", // 匹配所有 URL
    resourceTypes: ["xmlhttprequest", "main_frame", "sub_frame"]
  }
};

// 添加规则
chrome.declarativeNetRequest.updateDynamicRules({
  addRules: [rule],
  removeRuleIds: [rule.id] // 可选：移除规则
});
```
![完工](/personal-site-mvp/img/docs-assets/image_010.png "完工")
#### 5、加入页面翻译缓存
修改popup.js，加入会话缓存，缓存空间5m，每个标签由自己的缓存，关闭标签后缓存自动清除

![翻译后会看到缓存](/personal-site-mvp/img/docs-assets/image_011.png "翻译后会看到缓存")
![还原原文后再次翻译时，能看到是从缓存取的值](/personal-site-mvp/img/docs-assets/image_012.png "还原原文后再次翻译时，能看到是从缓存取的值")
```
    // 遍历文档中的所有文本节点
    function walkText(node) {
        if (node.nodeType === 3) { // Text node
            if (node.nodeValue.trim() !== '') {
                originalTexts.push({ node, originalText: node.nodeValue }); // 保存原文

                // 检查 Session Storage 中是否有翻译结果
                const cacheKey = `${config.sourceLanguage}_${config.targetLanguage}_${node.nodeValue}`;
                const cachedTranslation = sessionStorage.getItem(cacheKey);

                if (cachedTranslation) {
                    // 如果缓存中有翻译结果，直接使用
                    console.log('[Cached]from:', node.nodeValue, 'to:', cachedTranslation);
                    node.nodeValue = node.nodeValue + ' ' + cachedTranslation;
                } else {
                    // 使用 setTimeout 延迟调用 translateText
                    setTimeout(() => {
                        translateText(node.nodeValue, config.sourceLanguage, config.targetLanguage)
                            .then(translatedText => {
                                console.log('[API]from:', node.nodeValue, 'to:', translatedText);
                                // 更新节点内容
                                node.nodeValue = node.nodeValue + ' ' + translatedText;

                                // 将翻译结果存入 Session Storage
                                sessionStorage.setItem(cacheKey, translatedText);
                            })
                            .catch(error => {
                                console.error("Error translating text:", error);
                            });
                    }, originalTexts.length * 150); // 每 0.12 秒调用一次
                }
            }
        } else if (node.nodeName !== 'SCRIPT' && node.nodeName !== 'STYLE') {
            for (let child of node.childNodes) {
                walkText(child);
            }
        }
    }
```
#### 其他改进
* 自动翻译该网站
* 来源语言自动检测
* 段落在下方新建翻译段落
* 图片orc识别，获取文字与位置，根据像素得到文字背景色

### 完整项目
```
.
├── images
│   └── icon.png
├── lib
│   ├── crypto-js.min.js
│   └── fanyi.js
├── manifest.json
├── background.js
├── content.js
├── popup.html 
├── popup.js
└── test  // 测试页面
    ├── img
    │   └── chrome_48dp.png
    ├── index.html
    └── test.html
```
[附件: chrome-extension.zip | 35.7KB | application/zip | fileId=2810ce14a7094a02ad8a7c0386bbf47e]
### 













