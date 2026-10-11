---
title: "Hook状态管理"
description: "React 提供了一些内置的 Hook，用于在函数组件中复用状态逻辑。以下是一些常见的 React 内置 Hook，并附带简洁的示例："
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\React\\Hook状态管理.md"
---
Hook

React 提供了一些内置的 Hook，用于在函数组件中复用状态逻辑。以下是一些常见的 React 内置 Hook，并附带简洁的示例：

### useState
用于在函数组件中添加状态。

```
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```
### useEffect
用于在函数组件中执行副作用操作，比如数据获取、订阅、手动 DOM 操作等。

```
import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []); // 空数组表示只在组件挂载和卸载时执行

  return (
    <div>
      {data ? <p>{data.message}</p> : <p>Loading...</p>}
    </div>
  );
}
```
### useContext
用于在函数组件中访问 React 的 Context。

```
import React, { useContext } from 'react';

const ThemeContext = React.createContext('light');

function ThemeButton() {
  const theme = useContext(ThemeContext);

  return (
    <button style={{ background: theme === 'dark' ? 'black' : 'white', color: theme === 'dark' ? 'white' : 'black' }}>
      I am styled by theme context!
    </button>
  );
}
```
### useReducer
用于管理复杂的状态逻辑，类似于 Redux 的 reducer。

```
import React, { useReducer } from 'react';

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
    </div>
  );
}
```
### useCallback
用于缓存函数，避免在每次渲染时重新创建函数。

```
import React, { useState, useCallback } from 'react';

function ParentComponent() {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <ChildComponent onClick={increment} />
    </div>
  );
}

function ChildComponent({ onClick }) {
  return <button onClick={onClick}>Increment</button>;
}
```
### useMemo
用于缓存计算结果，避免在每次渲染时重新计算。

```
import React, { useState, useMemo } from 'react';

function ExpensiveCalculation({ a, b }) {
  const result = useMemo(() => {
    // 假设这是一个复杂的计算
    return a + b;
  }, [a, b]);

  return <p>Result: {result}</p>;
}

function App() {
  const [a, setA] = useState(1);
  const [b, setB] = useState(2);

  return (
    <div>
      <ExpensiveCalculation a={a} b={b} />
      <button onClick={() => setA(a + 1)}>Increment A</button>
      <button onClick={() => setB(b + 1)}>Increment B</button>
    </div>
  );
}
```
### useRef
用于在函数组件中创建一个可变的引用，通常用于访问 DOM 元素或存储不需要触发重新渲染的值。

```
import React, { useRef } from 'react';

function TextInputWithFocusButton() {
  const inputEl = useRef(null);

  const onButtonClick = () => {
    inputEl.current.focus();
  };

  return (
    <div>
      <input ref={inputEl} type="text" />
      <button onClick={onButtonClick}>Focus the input</button>
    </div>
  );
}
```

