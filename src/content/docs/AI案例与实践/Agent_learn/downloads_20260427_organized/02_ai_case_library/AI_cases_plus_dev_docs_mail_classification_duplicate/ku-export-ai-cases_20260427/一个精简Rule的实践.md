---
title: "[AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)"
description: "一个精简Rule的实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\一个精简Rule的实践.md"
---
一个精简Rule的实践

#### 🧑‍🏫 案例作者：[@张立理](https://ku.baidu-int.com?t=mention&mt=contact&id=af2da150-fcec-11f0-99bb-6710623192ee)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了通过自动记忆功能生成的memory.mdr文件，用于记录和规范模型行为。该文件通过总结历史任务中的规范型问题，自动激活并遵守未来任务中的相应条目。文中提到，模型在更新记忆时会直接参考对话中的代码示例，导致记忆文件冗长。经过测试，发现模型能理解文字说明，因此删除了大部分代码示例，仅保留必要部分，使Rule内容更加精简。
## 自动记忆
在我的项目中，有一个叫`memory.mdr`的Rule，它是由模型自己总结每一次任务中提出的规范型问题，在全局自动激活的`behavior.mdr`里来描述。

```
### 记忆

`.comate/rules/memory.mdr`是一个特殊的文件，当在对话中出现对你某一个具有通性的行为的明确的肯定或否定时，你**必须**更新这个文件，从对话中总结出在未来需要遵守的条目，在文件后追加该条目。

记忆文件中尽量不要加入代码示例，仅使用文字描述规范即可，当需要代码示例时，用户会主动告知。

当新增的条目与这个文件中的旧内容有冲突时，你也**必须**删除冲突的旧内容。
```
实际上，在任务中明确说“记下来”之类的，确实会自动更新。

![](/personal-site-mvp/img/doc-placeholder.svg "")
## 问题
在模型更新这个记忆时，最大的问题是它会直接参考对话中改过的代码，留下几个示例，最后经过一段时间，这个记忆长成了这样。

```
---
description:
globs:
alwaysApply: true
---
## 系统记忆

本规则中记录了在历史任务中产生并沉淀的规则，在你的任务执行过程中，需要格外注意此处罗列的条目，并严格遵守。

### JSX 内联逻辑规范

**禁止在 JSX 中内联超过 1 行的逻辑表达式**，包括但不限于：

1. 多行的三元表达式
2. 多行的 map/filter 等数组方法回调
3. 多行的条件渲染逻辑

**处理方式：**

- 将多行逻辑提取为独立的 `renderXxx` 函数
- 对于 `map` 等回调，将回调函数提取为独立函数
- JSX 中只保留简洁的单行函数调用

**示例：**

```tsx
// ❌ 错误：多行内联逻辑
<div>
  {messages.map((message, index) => (
    <MessageItem key={index} message={message} />
  ))}
</div>

// ✅ 正确：提取为独立函数
const renderMessageItem = (message: MessageType, index: number) => (
  <MessageItem key={index} message={message} />
);

<div>{messages.map(renderMessageItem)}</div>
```

### 多行字符串格式化

**在测试文件或其他需要多行字符串的场景中，使用 `dedent` 库来格式化字符串**，以保持代码的可读性和美观性。

**处理方式：**

- 安装 `dedent` 作为开发依赖
- 在文件顶部导入 `dedent`
- 使用 `dedent` 包裹所有多行模板字符串
- 保持适当的缩进，让代码层次清晰

**示例：**

```typescript
// ❌ 错误：难以阅读的多行字符串
const input = `<tool_result>
<status>succeeded</status>
</tool_result>`;

// ✅ 正确：使用 dedent 格式化
import dedent from 'dedent';

const input = dedent`
    <tool_result>
    <status>succeeded</status>
    </tool_result>
`;
```

### 动态类名组装规范

**当遇到较长或复杂的动态 class 组装时，使用 `classnames` 库来提高代码可读性和可维护性**。

**处理方式：**

- 安装 `classnames` 依赖
- 在文件顶部导入 `classNames`
- 将静态样式按逻辑分组为多个字符串参数
- 将动态样式使用对象形式表达，键为类名，值为布尔条件
- 将 `classNames()` 调用提取为独立变量，避免在 JSX 属性中出现多行语句

**示例：**

```tsx
// ❌ 错误：复杂的模板字符串拼接
<button
    className={`
        w-10 h-10 rounded-full bg-blue-500 text-white
        flex items-center justify-center shadow-lg transition-all
        ${disabled ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-600 cursor-pointer'}
    `}
>

// ✅ 正确：使用 classnames 并提取为变量
import classNames from 'classnames';

const buttonClassName = classNames(
    'w-10 h-10 rounded-full bg-blue-500 text-white',
    'flex items-center justify-center shadow-lg transition-all',
    {
        'opacity-50 cursor-not-allowed pointer-events-none': disabled,
        'hover:bg-blue-600 active:scale-95 cursor-pointer': !disabled,
    }
);

<button className={buttonClassName}>
```

### 函数参数提取规范

**当函数只有一个参数且该参数跨多行时，必须将参数提取为独立变量**。

**处理方式：**

- 将多行参数提取为独立的常量
- 如果 TypeScript 允许，必须为该变量标注类型
- 变量命名应清晰表达其用途
- 在函数调用时使用该变量

**示例：**

```tsx
// ❌ 错误：多行参数直接传入函数
pluginBabel({
    include: /\.(?:jsx|tsx)$/,
    babelLoaderOptions(opts) {
        opts.plugins?.unshift('babel-plugin-react-compiler');
    },
})

// ✅ 正确：提取为独立变量并标注类型
import type {PluginBabelOptions} from '@rsbuild/plugin-babel';

const babelOptions: PluginBabelOptions = {
    include: /\.(?:jsx|tsx)$/,
    babelLoaderOptions(opts) {
        opts.plugins?.unshift('babel-plugin-react-compiler');
    },
};

pluginBabel(babelOptions)
```

**适用场景：**
- React 组件的复杂 props 对象
- 插件配置对象
- 复杂的函数参数对象
- 任何跨越多行的单一参数
```
可以看到，文件中有大量的代码示例，考虑到这是一个**自动激活**的规则，这些示例很占上下文，并且代码会不会影响后续的真正业务代码生成，如模型错误地以为这代码可以抄，这些都不确定。

但是如果把代码示例删掉，又会有另一个疑问：**只有文字，模型能知道是什么意思吗？**

## 模型理解测试
为了能够移除代码，就需要测试一下模型对文字部分的理解能力，我的方案是：**把文本给模型，让模型提供正确和错误的示例，和当前Rule中的示例比对一下**。

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
从表现来看，模型是可以理解这些文字说明对应的代码是长什么样的，所以可以放心地删除。

## 结果
最后对`memory.mdr`里的所有代码示例进行了测试，只有一条“`className`分组”的规则模型理解不够准确，需要保留示例代码，其它的均可以删除，最终的Rule内容精简了很多。

```
---
description:
globs:
alwaysApply: true
---
## 系统记忆

本规则中记录了在历史任务中产生并沉淀的规则，在你的任务执行过程中，需要格外注意此处罗列的条目，并严格遵守。

### JSX 内联逻辑规范

禁止在 JSX 中内联超过 1 行的逻辑表达式，包括但不限于：

1. 多行的三元表达式
2. 多行的 map/filter 等数组方法回调
3. 多行的条件渲染逻辑

处理方式：

- 将多行逻辑提取为独立的 `renderXxx` 函数
- 对于 `map` 等回调，将回调函数提取为独立函数
- JSX 中只保留简洁的单行函数调用

### 多行字符串格式化

在需要多行字符串的场景中，使用 `dedent` 库来格式化字符串，以保持代码的可读性和美观性。

处理方式：

- 安装 `dedent` 作为开发依赖
- 在文件顶部导入 `dedent`
- 使用 `dedent` 包裹所有多行模板字符串
- 保持适当的缩进，让代码层次清晰

### 动态类名组装规范

当遇到较长或复杂的动态 class 组装时，使用 `classnames` 库来提高代码可读性和可维护性。

处理方式：

- 安装 `classnames` 依赖
- 在文件顶部导入 `classNames`
- 将静态样式按逻辑分组为多个字符串参数
- 将动态样式使用对象形式表达，键为类名，值为布尔条件
- 将 `classNames()` 调用提取为独立变量，避免在 JSX 属性中出现多行语句
- 每组参数添加注释说明类别

示例：

```js
classNames(
    'w-10 h-10 rounded-full',
    'bg-blue-500 text-white',
    'flex items-center justify-center',
    'shadow-lg transition-all',
    {
        'opacity-50 cursor-not-allowed pointer-events-none': disabled,
        'hover:bg-blue-600 active:scale-95 cursor-pointer': !disabled,
    }
)
```

### 函数参数提取规范

当函数只有一个参数且该参数跨多行时，必须将参数提取为独立变量。

处理方式：

- 将多行参数提取为独立的常量
- 如果 TypeScript 允许，必须为该变量标注类型
- 变量命名应清晰表达其用途
- 在函数调用时使用该变量

适用场景：
- React 组件的复杂 props 对象
- 插件配置对象
- 复杂的函数参数对象
- 任何跨越多行的单一参数

### 组件根节点命名规范

当组件的根节点使用 Emotion styled 处理时，该 styled 组件的名称统一命名为 `Layout`。

处理方式：

- 使用 `const Layout = styled.div\`...\`;` 创建根节点样式组件
- 在 JSX 中使用 `<Layout>` 作为组件的根容器
- 保持命名一致性，便于代码维护和理解

```
# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
