---
title: "原代码文件"
description: "你将收到一个原始代码文件，以及一个或多个包含模型生成修改内容的代码块，格式为 SEARCH/REPLACE。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-agent\\code_agent\\prompt\\api_code_generate\\GDP\\11-format_diff.md"
---
你将收到一个原始代码文件，以及一个或多个包含模型生成修改内容的代码块，格式为 SEARCH/REPLACE。

你的任务是：
基于原始文件，依次处理每个 SEARCH/REPLACE 修改块，在原文中执行插入或替换操作，输出最终融合后的完整代码文件。

修改规则如下：
- 当`SEARCH` 部分为空
  * `REPLACE` 部分逻辑在原代码文件中语义上已完整实现或和原始实现存在冲突，则优先保留原始实现。
  * `REPLACE` 部分逻辑在原始文件中不存在对应逻辑，视为新增代码，应寻找语义上合适的位置进行插入。
- 当 `SEARCH` 部分不为空
  * 若 `SEARCH` 与原文件中某段代码完全匹配，则用对应的 `REPLACE` 内容进行替换。
  * 若 `SEARCH` 在原文件中无法完全匹配，则需根据语义理解，定位最接近的实现片段，并以 `REPLACE` 内容进行替换。

示例：
* 示例原代码文件：
```go
package test

import (
	"context"

	"icode.baidu.com/baidu/test/module/test"
)

const (
	testConst = "test_const"
)

type TestInterface interface {
	TestFunc(ctx context.Context) error               // 测试函数
	TestData(ctx context.Context, testParam string) error // 测试数据
}

type service struct {
}

// Option 定义一个用于扩展的选项类型
type Option func(*service)

// NewTestService 创建 Service 实例
func NewTestService(opts ...Option) TestInterface {
	s := &service{}
	for _, opt := range opts {
		opt(s)
	}
	return s
}
```
* 示例模型生成代码块
<generate_code>
```go
<<<<<<< SEARCH
=======
package test1

import (
    "ctx"
)

type TestInterfaceGen interface {
  TestFunc(ctx context.Context) error // 测试函数
} 

func TestFunc(ctx context.Context) error {
  return nil
}
>>>>>>> REPLACE
```
</generate_code>
* 示例融合代码文件输出：
* 说明：当前文件为service层函数导出入口文件，从语义上看模型生成代码要实现功能当前文件已完全满足，且从当前文件来看导出函数并不应该实现在当前文件中，模型返回的修改结果属于重复生成且不符合当前代码规范，应当保持原代码内容输出即可。
```go
package test

import (
	"context"

	"icode.baidu.com/baidu/test/module/test"
)

const (
	testConst = "test_const"
)

type TestInterface interface {
	TestFunc(ctx context.Context) error               // 测试函数
	TestData(ctx context.Context, testParam string) error // 测试数据
}

type service struct {
}

// Option 定义一个用于扩展的选项类型
type Option func(*service)

// NewTestService 创建 Service 实例
func NewTestService(opts ...Option) TestInterface {
	s := &service{}
	for _, opt := range opts {
		opt(s)
	}
	return s
}
```

# 原代码文件
```go
{{origin_content}}
```

# 模型生成的代码块
<generate_code>
{{diff_codes}}
</generate_code>

# 输出要求：
- 理解原代码设计实现，保证符合原设计要求；
- 保证代码逻辑正确、结构清晰；
- 保持语义一致、风格统一；
- 避免重复、遗漏或逻辑冲突。

# 输出格式：仅按以下格式输出融合后的代码即可
* 说明：{简要思考}
```go
{融合后的代码}
```