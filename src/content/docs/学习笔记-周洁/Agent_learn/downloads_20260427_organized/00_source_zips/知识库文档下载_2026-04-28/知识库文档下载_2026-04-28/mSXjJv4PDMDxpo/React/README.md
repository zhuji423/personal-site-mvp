---
title: "README"
description: "教程：https://zh-hans.react.dev/learnhttps://zh-hans.react.dev/learn"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\React\\README.md"
---
React

教程：[https://zh-hans.react.dev/learn](https://zh-hans.react.dev/learn)

### 一、介绍
React是一款前端JavaScript库，专为构建用户界面而设计。

**一些核心概念：**

* **组件化开发：**组件化开发是一种软件开发模式，它将应用程序拆分为独立、可复用的组件，每个组件负责特定的功能或 UI 部分。
* **JSX 语法：**JSX（JavaScript XML）是一种 JavaScript 的语法扩展，允许开发者在 JavaScript 代码中编写类似 HTML 的结构，提高代码的可读性和开发效率。
* **虚拟 DOM：**虚拟 DOM 是 React 中用于优化 DOM 操作的一种技术，通过轻量级的 JavaScript 对象树来代表真实 DOM 的结构，提高性能。
* **单向数据流：**单向数据流是一种数据管理模式，规定数据只能从父组件流向子组件，简化了数据流的管理，使得状态变化更加可预测和易于调试。

### 二、安装环境
#### 1、安装Node.js 和 npm
Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行时环境，用于在服务器端运行 JavaScript 代码

[安装Node.js 和 npm](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/ODAYjaGQMpUI6T?t=mention&mt=doc&dt=doc)

#### 2、启动一个新的 React 项目
```
npx create-react-app myapp
cd myapp
```
得到

![](/personal-site-mvp/img/docs-assets/image_001_10.png "")
在终端运行 npm start

### 三、简单使用
#### 创建和嵌套组件
自己的组件必须以大写字母开头

```
// 创建组件
function MyButton() {
  return (
    <button>
      I'm a button
    </button>
  );
}

export default function MyApp() {
  return (
    <div>
      <MyButton />   // 嵌套组件
    </div>
  );
}
```
#### 使用 JSX 编写标签
更多jsx语法：[JSX（JavaScript XML）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/eTYF1eMFCA29xg?source=137?t=mention&mt=doc&dt=doc)

|html|jsx|
|-|-|
|<!-- Hello world -->
<div class="awesome" style="border: 1px solid red">
  <label for="name">Enter your name: </label>
  <input type="text" id="name" />
</div>
<p>Enter your HTML here</p>|<>
  {/* Hello world */}
  <div className="awesome" style={{ border: "1px solid red" }}>
    <label htmlFor="name">Enter your name: </label>
    <input type="text" id="name" />
  </div>
  <p>Enter your HTML here</p>
</>|

组件不能返回多个 JSX 标签。必须将它们包裹到一个共享的父级中，比如 `<div>...</div>` 或使用空的 `<>...</>` 包裹多个相邻的 JSX 元素

```
export default function Square() {
  return (
    <>
      <button className="square">X</button>
      <button className="square">X</button>
    </>
  );
}
```
#### 添加样式
使用 `className` 指定CSS 

```
<img className="avatar" />
```
单独的.css文件

```
.avatar {
  border-radius: 50%;
}
```
#### 显示数据
```
const user = {
  name: 'Hedy Lamarr',
  imageUrl: 'https://i.imgur.com/yXOvdOSs.jpg',
  imageSize: 90,
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={'Photo of ' + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```
#### 条件渲染
|if…else…|if…else…|if…|
|-|-|-|
|let content;
if (isLoggedIn) {
  content = <AdminPanel />;
} else {
  content = <LoginForm />;
}
return (
  <div>
    {content}
  </div>
);|<div>
  {isLoggedIn ? (
    <AdminPanel />
  ) : (
    <LoginForm />
  )}
</div>|<div>
  {isLoggedIn && <AdminPanel />}
</div>|

#### 渲染列表
```
const products = [
  { title: 'Cabbage', id: 1 },
  { title: 'Garlic', id: 2 },
  { title: 'Apple', id: 3 },
];

export default function ShoppingList() {
  const listItems = products.map(product =>
    <li key={product.id}>
      {product.title}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );
}
```
#### 响应事件
```
function MyButton() {
  function handleClick() {
    alert('You clicked me!');
  }

  return (
    <button onClick={handleClick}>
      Click me
    </button>
  );
}
```
#### 更新界面
```
import { useState } from 'react';

export default function MyApp() {
  return (
    <div>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
```
#### 使用Hook
hook详细用法参考：[Hook状态管理](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/R7KftcGssEiecE?source=137?t=mention&mt=doc&dt=doc)

以 `use` 开头的函数被称为 Hook，类似上个例子中的useState。

#### 组件间共享数据
```
import { useState } from 'react';

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return (
    <button onClick={onClick}>
      Clicked {count} times
    </button>
  );
}
```
### 三、完整页面
#### 后端接口 
web接口开发：go（[gdp2框架使用&接口开发](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/L_N99Ya8Czw6GO?source=137?t=mention&mt=doc&dt=doc)）、python（[flask](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/z_l_G7DFX3gGYh?source=137?t=mention&mt=doc&dt=doc)）

get [http://localhost:8080/api/code_trans_info/list](http://localhost:8080/api/code_trans_info/list) 页面展示接口信息

```
{
    "status": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "id": 17,
                "module_name": "baidu/b2b/b2bmatch",
                "url": "getOneTpInfoAction",
                "php_code": "",
                "demand_desc": "接口名称：getOneTpInfo",
                "go_code": "",
                "operator": "zhoujie19",
                "update_time": "2024-08-30T11:28:52+08:00",
                "demand_status": 0,
                "is_deleted": 0,
                "created_at": "2024-08-15T19:40:04+08:00"
            }
        ]
    }
}
```
#### 前端完整实现
##### 文件结构
![](/personal-site-mvp/img/docs-assets/image_002_9.png "")
##### 解决跨域（http-proxy-middleware）
跨域使用http-proxy-middleware库

```
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://localhost:8080',
      changeOrigin: true
    })
  );
};
```
##### 核心组件（axios+antd）
ui使用antd库、接口调用使用axios库

```
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table, Tag } from 'antd';

const CodeMigration = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/api/code_trans_info/list')
      .then(response => {
        setData(response.data.data.items);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  const columns = [
    {
      title: '模块名',
      dataIndex: 'module_name',
      key: 'module_name',
    },
    {
      title: 'URL',
      dataIndex: 'url',
      key: 'url',
    },
    {
      title: '生成的需求描述',
      dataIndex: 'demand_desc',
      key: 'demand_desc',
      render: (text) => (
        <span style={{ maxWidth: 200, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', display: 'inline-block' }}>
          {text}
        </span>
      ),
    },
    {
      title: '操作人',
      dataIndex: 'operator',
      key: 'operator',
    },
    {
      title: '更新时间',
      dataIndex: 'update_time',
      key: 'update_time',
    },
    {
      title: '需求状态',
      dataIndex: 'demand_status',
      key: 'demand_status',
      render: (status) => (
        <Tag color={status === 0 ? 'red' : 'green'}>
          {status === 0 ? '待审核' : '已审核'}
        </Tag>
      ),
    },
  ];

  return (
    <Table
      dataSource={data}
      columns={columns}
      rowKey="id"
    />
  );
};

export default CodeMigration;
```
##### 使用组件
```
import CodeMigration from './components/CodeMigration';

function App() {
  return (
    <div className="App" style={{ padding: '20px' }}>
      <CodeMigration />
    </div>
  );
}

export default App;
```
##### 页面渲染
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>React App</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```
```
import { createRoot } from 'react-dom/client';
import App from './App';

const rootElement = document.getElementById('root');
const root = createRoot(rootElement);

root.render(<App />);
```
##### 依赖
执行`npm install 包名 --save`命令后，package.json文件会自动更新包名与版本，同时安装的包会放在根目录的node_modules目录下

![](/personal-site-mvp/img/docs-assets/image_003_9.png "")
#### 运行
在终端运行 npm start，打开浏览器 http://localhost:3000/

![](/personal-site-mvp/img/docs-assets/image_004_6.png "")
### 四、使用大模型生成react代码
[需求到React代码生成](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/aK9mGXB2ET/iyUmqrU16Mq0Lp?t=mention&mt=doc&dt=doc)






