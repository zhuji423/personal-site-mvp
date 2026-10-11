---
title: "react-syntax-highlighter markdown代码高亮渲染"
description: "react-syntax-highlighter markdown代码高亮渲染"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\React\\react-syntax-highlighter markdown代码高亮渲染.md"
---
react-syntax-highlighter markdown代码高亮渲染

```
import React from 'react';
import ReactMarkdown from 'react-markdown';
import { CopyOutlined } from '@ant-design/icons';
import { Button } from 'antd';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { darcula } from 'react-syntax-highlighter/dist/esm/styles/prism';
import copy from 'copy-to-clipboard';

// 自定义代码块组件
const CodeBlock = ({ language, value }) => {
    const handleCopy = () => {
        copy(value);
    };

    // 使用默认的 language 参数
    const defaultLanguage = 'text';

    return (
        <div style={{ position: 'relative' }}>
            <button
                onClick={handleCopy}
                style={{
                    position: 'absolute',
                    top: '5px',
                    right: '5px',
                    backgroundColor: '#333',
                    color: '#fff',
                    border: 'none',
                    padding: '5px 10px',
                    cursor: 'pointer',
                    borderRadius: '3px',
                }}
            >
                复制
            </button>
            <SyntaxHighlighter language={language || defaultLanguage} style={darcula}>
                {value}
            </SyntaxHighlighter>
        </div>
    );
};

// 使用 ReactMarkdown 渲染 Markdown
const MarkdownRenderer = ({ markdown }) => {
    const handleCopyAll = () => {
        copy(markdown);
    };

    return (
        <div>
            <ReactMarkdown
                children={markdown}
                components={{
                    code({ node, inline, className, children, ...props }) {
                        const match = /language-(\w+)/.exec(className || '');
                        return !inline && match ? (
                            <CodeBlock
                                language={match[1]}
                                value={String(children).replace(/\n$/, '')}
                                {...props}
                            />
                        ) : (
                            <code className={className} {...props}>
                                {children}
                            </code>
                        );
                    },
                }}
            />
            <Button
                type="primary"
                icon={<CopyOutlined />}
                onClick={handleCopyAll}
                style={{ position: 'fixed', bottom: '20px', right: '20px' }}
            >
                复制Markdown
            </Button>
        </div>
    );
};

export default MarkdownRenderer;
```


```
function App() {
  return (
    <div className="App" style={{ padding: '20px' }}>
      <MarkdownRenderer markdown={markdownText} />
    </div>
  );
}
```


[附件: 屏幕录制2024-10-30 下午4.22.45.mov | 5.3MB | video/quicktime | fileId=9b858592998b4dbe9616d426f5dea918]
