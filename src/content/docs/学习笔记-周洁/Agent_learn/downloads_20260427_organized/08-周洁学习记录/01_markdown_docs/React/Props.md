---
title: "Props"
description: "在 React 中，props（属性）是组件之间传递数据的主要方式。通过 props，父组件可以将数据传递给子组件，子组件则可以通过 props 接收这些数据并进行相应的处理。"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\React\\Props.md"
---
Props

在 React 中，`props`（属性）是组件之间传递数据的主要方式。通过 `props`，父组件可以将数据传递给子组件，子组件则可以通过 `props` 接收这些数据并进行相应的处理。

#### 1. 传递基本数据类型
将字符串、数字、布尔值等基本数据类型作为 `props` 传递给子组件。

```
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

const element = <Welcome name="Alice" />;
```
#### 2. 传递对象
将对象作为 `props` 传递给子组件。

```
function UserProfile(props) {
  return (
    <div>
      <h1>{props.user.name}</h1>
      <p>{props.user.email}</p>
    </div>
  );
}

const user = { name: "Alice", email: "alice@example.com" };
const element = <UserProfile user={user} />;
```
#### 3. 传递函数
将函数作为 `props` 传递给子组件，并在子组件中调用它。

```
function Button(props) {
  return <button onClick={props.onClick}>Click me</button>;
}

function handleClick() {
  alert('Button clicked!');
}

const element = <Button onClick={handleClick} />;
```
#### 4. 默认 Props
为组件设置默认的 `props` 值，当父组件没有传递该 `props` 时，将使用默认值。

```
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

Welcome.defaultProps = {
  name: "Guest"
};

const element = <Welcome />; // 输出: Hello, Guest!
```
#### 5. 传递子组件
将子组件作为 `props.children` 传递给父组件。

```
function Card(props) {
  return (
    <div className="card">
      {props.children}
    </div>
  );
}

const element = (
  <Card>
    <h1>Title</h1>
    <p>This is a card content.</p>
  </Card>
);
```
#### 6. 使用解构赋值
使用解构赋值来简化 `props` 的使用。

```
function Welcome({ name }) {
  return <h1>Hello, {name}!</h1>;
}

const element = <Welcome name="Alice" />;
```
#### 7. 传递多个 Props
可以传递多个 `props` 给子组件。

```
function UserProfile({ name, email }) {
  return (
    <div>
      <h1>{name}</h1>
      <p>{email}</p>
    </div>
  );
}

const element = <UserProfile name="Alice" email="alice@example.com" />;
```

