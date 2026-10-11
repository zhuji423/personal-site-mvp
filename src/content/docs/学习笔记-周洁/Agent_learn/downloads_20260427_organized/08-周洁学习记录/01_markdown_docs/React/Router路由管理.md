---
title: "Router路由管理"
description: "Router路由管理"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\React\\Router路由管理.md"
---
Router路由管理

React Router 是 React 社区中最流行的路由库，它允许在单页应用（SPA）中实现客户端路由。通过 React Router，可以定义不同的路由，并将它们映射到不同的组件，从而实现页面之间的导航。

## 简单应用
### 安装 React Router
```
npm install react-router-dom
```
### 简单示例
```
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

// 定义一些示例组件
const Home = () => <h2>Home</h2>;
const About = () => <h2>About</h2>;
const Topics = () => <h2>Topics</h2>;
const NotFound = () => <h2>404 Not Found</h2>;

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/topics">Topics</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/topics" element={<Topics />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
```
* **Router**: 路由器组件，用于包裹整个应用，并管理路由的上下文。
* **Route**: 路由组件，用于定义路径和对应的组件。
* **Link**: 链接组件，用于在应用内部进行导航，类似于 HTML 中的 `<a>` 标签。
* **Routes**: 用于包裹多个 `Route` 组件，并确保只渲染第一个匹配的路由。
* **Redirect**: 用于重定向到其他路径。

### 运行
```
npm start
```
## 动态路由
动态路由是指在 URL 中包含动态参数的路由。这些参数可以在路由组件中被提取和使用，从而实现更灵活和动态的页面渲染。在 React Router 中，动态路由通过在路径中使用冒号 `:` 来定义动态参数。

* **动态参数**: 在路径 `/users/:id` 中，`:id` 是一个动态参数。
* **useParams**: 在 `UserProfile` 组件中使用 `useParams` Hook 来获取动态参数 `id` 的值。

```
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, useParams } from 'react-router-dom';

// 定义一些示例组件
const Home = () => <h2>Home</h2>;
const About = () => <h2>About</h2>;
const Topics = () => <h2>Topics</h2>;
const NotFound = () => <h2>404 Not Found</h2>;

// 动态路由组件
const UserProfile = () => {
  // 使用 useParams 获取动态参数
  const { id } = useParams();
  return <h2>User Profile: {id}</h2>;
};

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/topics">Topics</Link>
            </li>
            <li>
              <Link to="/users/1">User 1</Link>
            </li>
            <li>
              <Link to="/users/2">User 2</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/topics" element={<Topics />} />
          <Route path="/users/:id" element={<UserProfile />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
```
## 嵌套路由
嵌套路由是指在一个路由组件中嵌套另一个路由组件，从而实现更复杂的页面结构，例如带有侧边栏或导航栏的应用。

* **父路由**: `TopicsLayout` 组件是一个父路由组件，它包含一个导航栏和 `Outlet` 组件。
* **子路由**: 在 `TopicsLayout` 组件中定义的子路由，例如 `topic1` 和 `topic2`。
* **Outlet**: 用于在父组件中渲染子组件。当子路由匹配时，对应的子组件将被渲染到 `Outlet` 的位置。
* **index 路由**: 当访问 `/topics` 路径时，`index` 路由会匹配并渲染 `Topics` 组件。

```
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Outlet } from 'react-router-dom';

// 定义一些示例组件
const Home = () => <h2>Home</h2>;
const About = () => <h2>About</h2>;
const Topics = () => <h2>Topics</h2>;
const NotFound = () => <h2>404 Not Found</h2>;

// 嵌套路由组件
const TopicsLayout = () => {
  return (
    <div>
      <h2>Topics</h2>
      <nav>
        <ul>
          <li>
            <Link to="topic1">Topic 1</Link>
          </li>
          <li>
            <Link to="topic2">Topic 2</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </div>
  );
};

const Topic1 = () => <h3>Topic 1</h3>;
const Topic2 = () => <h3>Topic 2</h3>;

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/topics">Topics</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/topics" element={<TopicsLayout />}>
            <Route path="topic1" element={<Topic1 />} />
            <Route path="topic2" element={<Topic2 />} />
            <Route index element={<Topics />} />
          </Route>
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
```
## 程序化导航
程序化导航是指在 React 应用中通过代码而不是用户点击链接来触发页面导航。这在某些场景下非常有用，例如在表单提交后自动导航到另一个页面，或者在某些条件满足时重定向用户。

* **useNavigate**: 在 `Login` 组件中使用 `useNavigate` Hook 来获取 `navigate` 函数。
* **navigate**: `navigate` 函数用于触发导航。你可以传递一个路径字符串或一个对象来指定目标路径。
* **handleLogin**: 一个模拟登录的函数，根据登录结果调用 `navigate` 函数进行导航。

```
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, useNavigate } from 'react-router-dom';

// 定义一些示例组件
const Home = () => <h2>Home</h2>;
const About = () => <h2>About</h2>;
const Topics = () => <h2>Topics</h2>;
const NotFound = () => <h2>404 Not Found</h2>;

// 程序化导航示例组件
const Login = () => {
  const navigate = useNavigate();

  const handleLogin = () => {
    // 模拟登录成功
    const isLoggedIn = true;

    if (isLoggedIn) {
      // 登录成功后导航到首页
      navigate('/');
    } else {
      // 登录失败后导航到登录页面
      navigate('/login');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/topics">Topics</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/topics" element={<Topics />} />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
```

