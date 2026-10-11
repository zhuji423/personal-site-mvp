---
title: "react-katex 渲染LaTeX（含LaTeX用法总结）"
description: "react-katex 渲染LaTeX（含LaTeX用法总结）"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\LaTeX_引用文档\\react-katex 渲染LaTeX（含LaTeX用法总结）.md"
---
react-katex 渲染LaTeX（含LaTeX用法总结）

## 一、安装依赖
```
npm install react-katex katex
```
## 二、简单示例
1. 创建 `MathJaxExample` 组件

在 `./components/MathJaxExample.js` 文件中创建 `MathJaxExample` 组件：

```
import React from 'react';
import { InlineMath } from 'react-katex';
import 'katex/dist/katex.min.css'; // 引入 KaTeX 的样式

const MathJaxExample = ({ formula }) => {
  return (
    <div>
      <InlineMath math={formula} />
    </div>
  );
};

export default MathJaxExample;
```
2. 在 `App` 组件中使用 `MathJaxExample`

```
import React from 'react';
import MathJaxExample from './components/MathJaxExample';

const formulaText = 'E = mc^2';

function App() {
  return (
    <div className="App" style={{ padding: '20px' }}>
      <MathJaxExample formula={formulaText} />
    </div>
  );
}

export default App;
```
3. 运行项目

```
npm start
```
![](/personal-site-mvp/img/doc-placeholder.svg "")
## 三、完整页面
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
```
import React from 'react';
import { Table } from 'antd';
import { InlineMath } from 'react-katex';
import 'katex/dist/katex.min.css';

// 数据源
const latexExamples = [
    {
        category: '数学符号',
        description: '加减乘除',
        latex: 'a \\div b - c \\times d  + e = f',
    },
    {
        category: '数学符号',
        description: '关系符号无穷大',
        latex: '\\geq,\\leq,\\neq,\\equiv,\\infty',
    },
    {
        category: '数学符号',
        description: '希腊字母',
        latex: `\\alpha, \\beta, \\gamma, \\delta, \\epsilon, \\zeta \\\\
            \\eta, \\theta, \\iota, \\kappa, \\lambda, \\mu \\\\ 
            \\nu, \\xi, o, \\pi, \\rho, \\sigma \\\\ 
            \\tau, \\upsilon, \\phi, \\chi, \\psi, \\omega`,
    },
    {
        category: '数学符号',
        description: '求和积分符号',
        latex: '\\sum \\ \\int',
    },
    {
        category: '数学符号',
        description: '根号分数向量',
        latex: '\\sqrt[x]{y} \\ \\frac{a}{b} \\ \\vec{a}',
    },
    {
        category: '数学符号',
        description: '上标下标',
        latex: 'a^x_y, a_{y,z}',
    },
    {
        category: '排版结构',
        description: '换行',
        latex: 'a\\\\c',
    },
    {
        category: '排版结构',
        description: '分组',
        latex: '123^{456}_{789}',
    },
    {
        category: '排版结构',
        description: '空格',
        latex: 'a\\enspace b,\\ a\\quad b,\\ a\\qquad b \\\\ a\\ b,\\ a\\;b,\\ a\\,b,\\ a\\!b',
    },
    {
        category: '排版结构',
        description: '省略号',
        latex: '\\dots,\\ \\cdots,\\ \\vdots,\\ \\ddots',
    },
    {
        category: '公式',
        description: '向量标量',
        latex: '\\overrightarrow{AB},\\ \\overline{m+n}',
    },
    {
        category: '公式',
        description: '求和',
        latex: '\\sum_{i=1}^{k}a_i',
    },
    {
        category: '公式',
        description: '累乘',
        latex: '\\prod_{i=1}^{n}a_i',
    },
    {
        category: '公式',
        description: '极限',
        latex: '\\lim_{x\\to 0}',
    },
    {
        category: '公式',
        description: '积分',
        latex: '\\int_0^\\infty{f(x)dx}',
    },
    {
        category: '公式',
        description: '三角函数',
        latex: '\\sin x',
    },
    {
        category: '公式',
        description: '对数',
        latex: '\\log_ab',
    },
    {
        category: '公式',
        description: '取整',
        latex: '\\lceil \\frac{21}{5}\\rceil=5,\\ \\lfloor \\frac{21}{5}\\rfloor=4',
    },
    {
        category: '公式',
        description: '取模',
        latex: 'a\\equiv 1(mod\\enspace n)',
    },
    {
        category: '公式',
        description: '下括号',
        latex: '\\underbrace{a+b+\\cdots+z}_{26}',
    },
    {
        category: '公式',
        description: '复杂公式',
        latex: '\\int_a^b f(x) \\, dx',
    },
    {
        category: '矩阵',
        description: '矩阵',
        latex: `\\begin{matrix} 1&2\\\\ 3&4\\\\ \\end{matrix}\\ 
            \\begin{pmatrix} 1&2\\\\ 3&4\\\\ \\end{pmatrix}\\ 
            \\begin{Bmatrix} 1&2\\\\ 3&4\\\\ \\end{Bmatrix}\\ 
            \\begin{Vmatrix} 1&2\\\\ 3&4\\\\ \\end{Vmatrix}`,
    },
    {
        category: '矩阵',
        description: '分列矩阵',
        latex: '\\left[\\begin{array}{cc|c} 1&2&3\\\\ 4&5&6 \\end{array} \\right]',
    },
    {
        category: '矩阵',
        description: '阵列',
        latex: `\\begin{array}{c|lll} 
            {↓}&{a}&{b}&{c}\\\\ 
            \\hline 
            {R_1}&{c}&{b}&{a}\\\\ 
            {R_2}&{b}&{c}&{c}\\\\ 
        \\end{array}`,
    },
    {
        category: '矩阵',
        description: '复杂矩阵',
        latex: `\\begin{bmatrix} 
            {a_{11}}&{a_{12}}&{\\cdots}&{a_{1n}}\\\\ 
            {a_{21}}&{a_{22}}&{\\cdots}&{a_{2n}}\\\\ 
            {\\vdots}&{\\vdots}&{\\ddots}&{\\vdots}\\\\ 
            {a_{m1}}&{a_{m2}}&{\\cdots}&{a_{mn}}\\\\ 
        \\end{bmatrix}`,
    },
    {
        category: '矩阵',
        description: '方程组',
        latex: `\\begin{cases} 
            a_1x+b_1y+c_1z=d_1\\\\ 
            a_2x+b_2y+c_2z=d_2\\\\ 
            a_3x+b_3y+c_3z=d_3\\\\ 
        \\end{cases}`,
    },
    {
        category: '表格',
        description: '简单表格',
        latex: `\\begin{array}{ccc}
            \\hline
            \\text{A} & \\text{B} & \\text{C} \\\\
            \\hline
            1 & 2 & 3 \\\\
            4 & 5 & 6 \\\\
            \\hline
        \\end{array}`,
    },
    {
        category: '表格',
        description: '带边框表格',
        latex: `\\begin{array}{|c|c|c|}
            \\hline
            \\text{A} & \\text{B} & \\text{C} \\\\
            \\hline
            1 & 2 & 3 \\\\
            \\hline
            4 & 5 & 6 \\\\
            \\hline
        \\end{array}`,
    }
];

// 表格列配置
const columns = [
    {
        title: '分类',
        dataIndex: 'category',
        key: 'category',
        render: (text, record, index) => {
            // 合并分类列
            const isFirstInCategory =
                index === 0 || latexExamples[index - 1].category !== record.category;
            return {
                children: text,
                props: {
                    rowSpan: isFirstInCategory ? latexExamples.filter((item) => item.category === record.category).length : 0,
                },
            };
        },
    },
    {
        title: '功能描述',
        dataIndex: 'description',
        key: 'description',
    },
    {
        title: 'LaTeX 语法',
        dataIndex: 'latex',
        key: 'latex',
        render: (text) => (
            <code style={{
                backgroundColor: '#f0f0f0',
                color: '#d63384',
                padding: '4px 8px',
                borderRadius: '4px',
                fontFamily: 'monospace',
            }}>
                {text}
            </code>
        ),
    },
    {
        title: '显示效果',
        dataIndex: 'latex',
        key: 'display',
        render: (text) => <MathJaxExample formula={text} />, // 动态渲染 LaTeX 公式
    },
];

const ShowLaTeX = () => {
    return (
        <div style={{ padding: '20px' }}>
            <h1>LaTeX 常用语法示例</h1>
            <Table
                dataSource={latexExamples}
                columns={columns}
                rowKey="latex" // 使用 latex 作为每行的唯一标识
                pagination={false} // 禁用分页
            />
        </div>
    );
};

const MathJaxExample = ({ formula }) => {
    return (
        <div>
            <InlineMath math={formula} />
        </div>
    );
};

export default ShowLaTeX;
```
