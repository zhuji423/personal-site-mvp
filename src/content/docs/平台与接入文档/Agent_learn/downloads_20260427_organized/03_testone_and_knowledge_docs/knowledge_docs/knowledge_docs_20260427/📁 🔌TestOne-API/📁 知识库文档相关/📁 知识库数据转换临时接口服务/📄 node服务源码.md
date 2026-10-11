---
title: "应用"
description: "node服务源码"
date: "2026-04-28"
category: "平台与接入文档"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\03_testone_and_knowledge_docs\\knowledge_docs\\knowledge_docs_20260427\\📁 🔌TestOne-API\\📁 知识库文档相关\\📁 知识库数据转换临时接口服务\\📄 node服务源码.md"
---
node服务源码

```

import {mdSerialize, htmlSerialize, mdDeserialize, htmlDeserialize} from '@baidu/morpho-data-transform';
import express from 'express';

const app = express();
const port = process.env.PORT || 3000;

// 配置中间件解析JSON请求体
app.use(express.json({limit: '10mb'}));

// 验证请求参数的中间件
const validateJsonParseRequest = (req, res, next) => {
    const { type, json } = req.body;
    
    // 检查必需参数是否存在
    if (!type || !json) {
        return res.json({
            code: 400,
            message: '缺少必需参数：type 或 json',
            data: null
        });
    }

    // 验证 type 参数
    if (!['html', 'markdown'].includes(type)) {
        return res.json({
            code: 400,
            message: 'type 参数只能是 html 或 markdown',
            data: null
        });
    }

    // 验证 json 类型是否为对象数组
    if (!Array.isArray(json)) {
        return res.json({
            code: 400,
            message: 'json 参数必须是对象数组',
            data: null
        });
    }

    // 验证 json 对象数组是否有值
    if (json.length === 0) {
        return res.json({
            code: 400,
            message: 'json 对象数组不能为空',
            data: null
        });
    }

    next();
};

// JSON解析HTML和MD接口
app.post('/kuJsonParse', validateJsonParseRequest, (req, res) => {
    try {
        const { type, json } = req.body;
        
        // 将 JSON 转换为字符串
        let result = '';
        
        if (type === 'html') {
            result = htmlSerialize(json);
        } else {
            result = mdSerialize(json, {
                standard: true,
            });
        }
        
        res.json({
            code: 0,
            message: 'success',
            data: result
        });
    } catch (error) {
        res.json({
            code: 400,
            message: '解析时发生错误',
            data: error.message
        });
    }
});

const validateMdHtmlToJsonRequest = (req, res, next) => {
    const { type, data } = req.body;

    // 检查必需参数是否存在
    if (!type || !data) {
        return res.json({
            code: 400,
            message: '缺少必需参数：type 或 data',
            data: null
        });
    }

    // 验证 type 参数
    if (!['html', 'markdown'].includes(type)) {
        return res.json({
            code: 400,
            message: 'type 参数只能是 html 或 markdown',
            data: null
        });
    }

    // 验证 data 类型
    if (typeof data !== 'string') {
        return res.json({
            code: 400,
            message: 'data 参数必须是字符串',
            data: null
        });
    }

    next();
};

// HTML和MD解析JSON
app.post('/kuMdHtmlToJson', validateMdHtmlToJsonRequest, (req, res) => {
    try {
        // [INFO]防止依赖库报错
        global.window = {};

        const { type, data } = req.body;

        let result = '';
        
        if (type === 'html') {
            result = htmlDeserialize(data);
        } else {
            result = mdDeserialize(data);
        }
        
        res.json({
            code: 0,
            message: 'success',
            data: result
        });
    } catch (error) {
        console.log(error)
        res.json({
            code: 400,
            message: '解析时发生错误',
            data: error.message
        });
    }
})

// 启动服务器
app.listen(port, () => {
    console.log(`服务器运行在 ${port} 端口`);
});

```
```
{
  "name": "ku-parse",
  "version": "0.0.1",
  "description": "知识库数据解析，支持 json、markdown、html 三种数据格式的相互转换",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "start": "PORT=8080 node index.js",
    "dev": "PORT=8080 nodemon index.js"
  },
  "author": "TestOne",
  "license": "ISC",
  "dependencies": {
    "@baidu/morpho-data-transform": "^0.0.105",
    "body-parser": "^1.20.2",
    "express": "^4.18.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.3"
  }
}

```
## 使用版本：
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 更新服务步骤：
### 进入开发机
ssh testone@testone-test.bcc-szzj.baidu.com

### 进入 /zhangtao77/kuParse
### 升级包
```
npm install @baidu/morpho-data-transform@latest --legacy-peer-deps
```
### 验证下
```
cat ./package.json
```
### 切换node版本为24
```
deck select nodejs-24.4.1
# 应用
source ~/.deck/2.0/etc/bashrc
# 验证下
node -v
# v24.4.1
```
### 停掉之前的进程
```
# 查看 8080 端口占用
lsof -i :8080
# kill 进程
kill -9 <PID>
```
### 启动服务
```
nohup npm start > nohup.log 2>&1 &
```
