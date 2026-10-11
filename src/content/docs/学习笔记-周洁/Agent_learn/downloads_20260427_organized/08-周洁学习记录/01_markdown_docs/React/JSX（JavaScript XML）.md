---
title: "JSX（JavaScript XML）"
description: "JSX（JavaScript XML）"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\React\\JSX（JavaScript XML）.md"
---
JSX（JavaScript XML）

JSX（JavaScript XML）是 React 中用于描述 UI 结构的语法扩展。它允许在 JavaScript 代码中编写类似 HTML 的结构。

#### 1. 基本元素
JSX 允许直接在 JavaScript 中编写 HTML 元素。

```
const element = <h1>Hello, World!</h1>;
```
#### 2. 嵌套元素
可以将多个元素嵌套在一起。

```
const element = (
  <div>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
  </div>
);
```
#### 3. 表达式嵌入
可以使用花括号 `{}` 在 JSX 中嵌入 JavaScript 表达式。

```
const name = "Alice";
const element = <h1>Hello, {name}!</h1>;
```
#### 4. 属性
可以像在 HTML 中一样为元素添加属性，但有些属性名需要使用驼峰命名法（如 `className` 代替 `class`）。

```
const element = <img src="/personal-site-mvp/img/doc-placeholder.svg" alt="A beautiful image" className="image-class" />;
```
#### 5. 条件渲染
可以使用三元运算符或 `&&` 运算符来实现条件渲染。

```
const isLoggedIn = true;
const element = (
  <div>
    {isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign up.</h1>}
  </div>
);
```
或者使用 `&&` 运算符：

```
const isLoggedIn = true;
const element = (
  <div>
    {isLoggedIn && <h1>Welcome back!</h1>}
  </div>
);
```
#### 6. 列表渲染
可以使用 `map` 方法来渲染列表。

```
const numbers = [1, 2, 3, 4, 5];
const listItems = numbers.map((number) =>
  <li key={number.toString()}>{number}</li>
);

const element = <ul>{listItems}</ul>;
```
#### 7. 事件处理
可以为元素添加事件处理函数。

```
function handleClick() {
  alert('Button clicked!');
}

const element = <button onClick={handleClick}>Click me</button>;
```
#### 8. 组件
可以将 JSX 封装在自定义组件中。

```
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

const element = <Welcome name="Alice" />;
```

