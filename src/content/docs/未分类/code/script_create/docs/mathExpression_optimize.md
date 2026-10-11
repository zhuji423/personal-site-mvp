---
title: "mathExp 函数安全优化说明"
description: "原代码直接使用 eval 计算表达式，存在严重的安全隐患：攻击者可以输入 import'os'.system'rm -rf /' 这样的恶意代码执行任意命令。"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\script_create\\docs\\mathExpression_optimize.md"
---
# mathExp 函数安全优化说明

## 修改思路概述

原代码直接使用 `eval()` 计算表达式，存在严重的安全隐患：攻击者可以输入 `__import__('os').system('rm -rf /')` 这样的恶意代码执行任意命令。

修改后的代码采用**多层防御**策略：
1. **字符白名单过滤** - 正则表达式验证输入只包含安全字符
2. **AST 解析** - 将表达式解析为抽象语法树
3. **运算符白名单** - 只允许预定义的数学运算符
4. **递归求值** - 遍历 AST 节点，只处理允许的节点类型

---

## 代码详细解析

### 1. 导入必要的模块

```python
import re       # 正则表达式，用于字符白名单验证
import argparse # 命令行参数解析
import ast      # 抽象语法树，用于安全解析表达式
import operator # Python 内置运算符函数
```

### 2. 定义允许的运算符白名单

```python
ALLOWED_OPERATORS = {
    ast.Add: operator.add,    # + 加法
    ast.Sub: operator.sub,    # - 减法
    ast.Mult: operator.mul,   # * 乘法
    ast.Div: operator.truediv,# / 除法
    ast.Pow: operator.pow,    # ** 幂运算
    ast.USub: operator.neg,   # - 负号（一元）
    ast.UAdd: operator.pos,   # + 正号（一元）
}
```

**含义**：将 AST 的运算符节点类型映射到 Python 的实际运算函数。只有在这个字典中的运算符才会被允许执行。

---

### 3. 主函数定义

```python
def math_exp_func(expression: str, return_type: str = 'f') -> any:
    """
    计算数学表达式（安全版本，只允许数学运算）
    :param expression: 数学表达式字符串
    :param return_type: 返回类型 b=byte, s=short, i=int, l=long, f=float, d=double
    :return: 计算结果
    """
```

---

### 4. 内部递归求值函数 `_eval()`

```python
def _eval(node):
    """递归计算AST节点"""
```

这是核心安全逻辑，递归遍历 AST 树的每个节点。

#### 4.1 处理数字节点

```python
if isinstance(node, ast.Num):  # 数字
    return node.n
```

**含义**：如果节点是数字（如 `123`、`3.14`），直接返回其数值。`ast.Num` 是 Python AST 中表示数字字面量的节点类型。

#### 4.2 处理二元运算（如 `1+2`）

```python
elif isinstance(node, ast.BinOp):  # 二元运算
    left = _eval(node.left)        # 递归计算左操作数
    right = _eval(node.right)      # 递归计算右操作数
    op_type = type(node.op)        # 获取运算符类型
    if op_type in ALLOWED_OPERATORS:
        return ALLOWED_OPERATORS[op_type](left, right)
    else:
        raise ValueError(f"不允许的运算符: {op_type}")
```

**含义**：
- `ast.BinOp` 表示二元运算（如 `a + b`）
- 先递归计算左右操作数
- 检查运算符是否在白名单中
- 如果在白名单中，调用对应的运算函数
- 如果不在，抛出异常拒绝执行

**示例**：对于表达式 `1+2*3`，AST 结构为：
```
      BinOp(+)
      /      \
    Num(1)  BinOp(*)
             /     \
          Num(2)  Num(3)
```
递归顺序：先计算 `2*3=6`，再计算 `1+6=7`

#### 4.3 处理一元运算（如 `-5`）

```python
elif isinstance(node, ast.UnaryOp):  # 一元运算
    operand = _eval(node.operand)    # 递归计算操作数
    op_type = type(node.op)          # 获取运算符类型
    if op_type in ALLOWED_OPERATORS:
        return ALLOWED_OPERATORS[op_type](operand)
    else:
        raise ValueError(f"不允许的运算符: {op_type}")
```

**含义**：处理单目运算符，如 `-5`、`+3`。同样检查运算符是否在白名单中。

#### 4.4 处理表达式根节点

```python
elif isinstance(node, ast.Expression):
    return _eval(node.body)
```

**含义**：`ast.Expression` 是 `ast.parse(mode='eval')` 返回的根节点类型，直接递归处理其 body。

#### 4.5 拒绝其他节点类型

```python
else:
    raise ValueError(f"不支持的表达式类型: {type(node)}")
```

**含义**：任何不在上述列表中的节点类型（如 `ast.Call` 函数调用、`ast.Import` 导入语句等）都会被拒绝。这是防止代码注入的关键。

---

### 5. 主执行逻辑

```python
try:
```

#### 5.1 字符白名单验证

```python
# 验证表达式只包含安全字符
if not re.match(r'^[\\d\\s+\\-*/().]+$', expression):
    raise ValueError("表达式包含非法字符")
```

**含义**：
- `r'^[\\d\\s+\\-*/().]+$'` 是正则表达式模式
- `^` 匹配字符串开头
- `\\d` 匹配数字 0-9
- `\\s` 匹配空白字符（空格、制表符等）
- `+` 匹配加号
- `\\-` 匹配减号
- `*` 匹配乘号
- `/` 匹配除号
- `(` `)` 匹配括号
- `.` 匹配小数点
- `+` 量词，表示前面的字符可以出现一次或多次
- `$` 匹配字符串结尾

**作用**：如果输入包含字母（如 `import`）、下划线（如 `__import__`）或其他非法字符，直接拒绝。

**示例**：
- `1+2*3` ✓ 通过
- `(10+5)/3` ✓ 通过
- `2**3+4*5` ✓ 通过
- `__import__('os')` ✗ 拒绝（包含下划线和字母）
- `eval('1+1')` ✗ 拒绝（包含字母）

#### 5.2 解析 AST

```python
# 解析并计算表达式
tree = ast.parse(expression, mode='eval')
result = _eval(tree)
```

**含义**：
- `ast.parse(expression, mode='eval')` 将字符串解析为 AST
- `mode='eval'` 表示解析为表达式模式（只能解析表达式，不能解析语句）
- 然后调用 `_eval()` 递归计算结果

#### 5.3 类型转换

```python
# 根据返回类型转换
if return_type.lower() in ['b', 's', 'i', 'l']:
    return int(result)
elif return_type.lower() in ['f', 'd']:
    return float(result)
else:
    return result
```

**含义**：根据用户指定的返回类型，将结果转换为整数或浮点数。

---

### 6. 异常处理

```python
except Exception as e:
    raise ValueError(f"Expression evaluation failed: {str(e)}")
```

**含义**：捕获所有异常，统一抛出 `ValueError`，避免泄露内部错误信息。

---

## 安全对比

### 原代码（不安全）

```python
result = eval(expression)  # 直接执行任意代码！
```

攻击示例：
```python
math_exp_func("__import__('os').system('rm -rf /')", 'f')
# 会直接执行删除文件命令！
```

### 新代码（安全）

```python
# 1. 字符白名单拦截
if not re.match(r'^[\\d\\s+\\-*/().]+$', expression):
    raise ValueError("表达式包含非法字符")
# __import__('os') 会被这里拦截

# 2. AST 解析拦截
tree = ast.parse(expression, mode='eval')
# 即使绕过字符检查，AST 也不会解析函数调用

# 3. 运算符白名单拦截
if op_type in ALLOWED_OPERATORS:  # 只允许数学运算符
    # ...
else:
    raise ValueError("不允许的运算符")
```

---

## 总结

| 防御层 | 作用 | 拦截的攻击 |
|--------|------|------------|
| 字符白名单 | 正则表达式过滤非法字符 | `import`、`eval`、`__` 等 |
| AST 解析 | 只解析表达式，不解析语句 | 函数调用、导入语句 |
| 运算符白名单 | 只允许预定义运算符 | 任何未授权的 AST 节点 |
| 递归求值 | 只处理允许的节点类型 | 所有非法节点类型 |

这种**纵深防御**策略确保即使某一层被绕过，其他层仍能阻止攻击。