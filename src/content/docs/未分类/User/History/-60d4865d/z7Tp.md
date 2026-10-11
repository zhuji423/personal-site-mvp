---
title: "Python 工具函数脚本集合"
description: "每个函数都是独立的脚本文件，包含完整的测试用例。"
date: "2026-01-08"
category: "未分类"
source: "F:\\百度工作\\06_comate_aiide_config\\User\\History\\-60d4865d\\z7Tp.md"
---
# Python 工具函数脚本集合

每个函数都是独立的脚本文件，包含完整的测试用例。

## 1. 时间相关函数

### 1.1 __[time.py](http://time.py)

**函数名称：** 获取指定格式的时间

**函数介绍：** 根据指定的日期格式和时间偏移量，返回格式化的时间字符串。支持年、月、日、时、分、秒等多种时间单位的偏移计算。

**参数说明：**

- `format_str`：日期格式，如 `yyyy-MM-dd HH:mm:ss`
- `shifting`：时间偏移量，如 `-1d`（昨天），`+1y`（明年），可选参数

**返回值：** 格式化后的时间字符串

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re
import argparse

def time_func(format_str: str, shifting: str = '') -> str:
    """
    获得指定格式的时间
    :param format_str: 日期格式，如 yyyy-MM-dd hh:mm:ss
    :param shifting: 时间偏移量，如 -1d, +1y
    :return: 格式化的时间字符串
    """
    current_time = [datetime.now](http://datetime.now)()
    
    # 如果有时间偏移量
    if shifting:
        pattern = r'^([+-]?)(\d+)([yMdHms])$'
        match = re.match(pattern, shifting)
        if not match:
            raise ValueError("Invalid shifting format. Use '+1y', '-3m', '-1d', etc.")
        
        sign = [match.group](http://match.group)(1) if [match.group](http://match.group)(1) else '+'
        num = int([match.group](http://match.group)(2))
        unit = [match.group](http://match.group)(3)
        
        if sign == '-':
            num = -num
        
        # 根据单位类型调整时间
        if unit == 'y':
            current_time = current_time + relativedelta(years=num)
        elif unit == 'M':
            current_time = current_time + relativedelta(months=num)
        elif unit == 'd':
            current_time = current_time + relativedelta(days=num)
        elif unit == 'H':
            current_time = current_time + relativedelta(hours=num)
        elif unit == 'm':
            current_time = current_time + relativedelta(minutes=num)
        elif unit == 's':
            current_time = current_time + relativedelta(seconds=num)
    
    # 转换Java风格的格式为Python风格
    python_format = format_str.replace('yyyy', '%Y').replace('MM', '%m').replace('dd', '%d')
    python_format = python_format.replace('HH', '%H').replace('hh', '%H')
    python_format = python_format.replace('mm', '%M').replace('ss', '%S')
    
    return current_time.strftime(python_format)

def main():
    parser = argparse.ArgumentParser(description='获取指定格式的时间')
    parser.add_argument('--format', type=str, required=True, help='时间格式')
    parser.add_argument('--shifting', type=str, default='', help='时间偏移量')
    
    args = parser.parse_args()
    print(time_func(args.format, args.shifting))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: 当前时间")
    print(time_func('yyyy-MM-dd HH:mm:ss'))
    
    print("\n测试用例 2: 昨天同一时刻")
    print(time_func('yyyy-MM-dd HH:mm:ss', '-1d'))
    
    print("\n测试用例 3: 今天日期")
    print(time_func('yyyyMMdd'))
    
    print("\n测试用例 4: 一年前")
    print(time_func('yyyy-MM-dd', '-1y'))
```

---

### 1.2 __[timeStamp.py](http://timeStamp.py)

**函数名称：** 获取13位时间戳

**函数介绍：** 获取当前时间的13位时间戳（毫秒级），支持时间偏移量计算。常用于接口测试中需要毫秒级时间戳的场景。

**参数说明：**

- `shifting`：时间偏移量，如 `-1d`（昨天此刻），可选参数

**返回值：** 13位时间戳字符串（毫秒）

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re
import argparse

def timestamp_func(shifting: str = '') -> str:
    """
    获得当前时间戳（13位毫秒）
    :param shifting: 时间偏移量，如 -1d, +1y
    :return: 13位时间戳字符串
    """
    current_time = [datetime.now](http://datetime.now)()
    
    # 如果有时间偏移量
    if shifting:
        pattern = r'^([+-]?)(\d+)([yMdHms])$'
        match = re.match(pattern, shifting)
        if not match:
            raise ValueError("Invalid shifting format. Use '+1y', '-1d', etc.")
        
        sign = [match.group](http://match.group)(1) if [match.group](http://match.group)(1) else '+'
        num = int([match.group](http://match.group)(2))
        unit = [match.group](http://match.group)(3)
        
        if sign == '-':
            num = -num
        
        # 根据单位类型调整时间
        if unit == 'y':
            current_time = current_time + relativedelta(years=num)
        elif unit == 'M':
            current_time = current_time + relativedelta(months=num)
        elif unit == 'd':
            current_time = current_time + relativedelta(days=num)
        elif unit == 'H':
            current_time = current_time + relativedelta(hours=num)
        elif unit == 'm':
            current_time = current_time + relativedelta(minutes=num)
        elif unit == 's':
            current_time = current_time + relativedelta(seconds=num)
    
    # 返回13位时间戳（毫秒）
    return str(int(current_time.timestamp() * 1000))

def main():
    parser = argparse.ArgumentParser(description='获取13位时间戳')
    parser.add_argument('--shifting', type=str, default='', help='时间偏移量')
    
    args = parser.parse_args()
    print(timestamp_func(args.shifting))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: 当前时间戳")
    print(timestamp_func())
    
    print("\n测试用例 2: 昨天同一时刻的时间戳")
    print(timestamp_func('-1d'))
    
    print("\n测试用例 3: 一小时后的时间戳")
    print(timestamp_func('+1H'))
```

---

### 1.3 __[timeStamp10.py](http://timeStamp10.py)

**函数名称：** 获取10位时间戳

**函数介绍：** 获取当前时间的10位时间戳（秒级），支持时间偏移量计算。这是Unix标准时间戳格式。

**参数说明：**

- `shifting`：时间偏移量，如 `-1d`（昨天此刻），可选参数

**返回值：** 10位时间戳字符串（秒）

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re
import argparse

def timestamp10_func(shifting: str = '') -> str:
    """
    获得当前时间戳（10位秒）
    :param shifting: 时间偏移量，如 -1d, +1y
    :return: 10位时间戳字符串
    """
    current_time = [datetime.now](http://datetime.now)()
    
    # 如果有时间偏移量
    if shifting:
        pattern = r'^([+-]?)(\d+)([yMdhms])$'
        match = re.match(pattern, shifting)
        if not match:
            raise ValueError("Invalid shifting format. Use '+1y', '-1d', etc.")
        
        sign = [match.group](http://match.group)(1) if [match.group](http://match.group)(1) else '+'
        num = int([match.group](http://match.group)(2))
        unit = [match.group](http://match.group)(3)
        
        if sign == '-':
            num = -num
        
        # 根据单位类型调整时间
        if unit == 'y':
            current_time = current_time + relativedelta(years=num)
        elif unit == 'M':
            current_time = current_time + relativedelta(months=num)
        elif unit == 'd':
            current_time = current_time + relativedelta(days=num)
        elif unit == 'h':
            current_time = current_time + relativedelta(hours=num)
        elif unit == 'm':
            current_time = current_time + relativedelta(minutes=num)
        elif unit == 's':
            current_time = current_time + relativedelta(seconds=num)
    
    # 返回10位时间戳（秒）
    return str(int(current_time.timestamp()))

def main():
    parser = argparse.ArgumentParser(description='获取10位时间戳')
    parser.add_argument('--shifting', type=str, default='', help='时间偏移量')
    
    args = parser.parse_args()
    print(timestamp10_func(args.shifting))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: 当前时间戳")
    print(timestamp10_func())
    
    print("\n测试用例 2: 昨天同一时刻的时间戳")
    print(timestamp10_func('-1d'))
    
    print("\n测试用例 3: 一分钟前的时间戳")
    print(timestamp10_func('-1m'))
```

---

### 1.4 __[getWeekDate.py](http://getWeekDate.py)

**函数名称：** 获取星期对应的日期

**函数介绍：** 根据指定的星期几和周期偏移量，计算对应的日期。例如可以计算3周前的周一是哪一天。

**参数说明：**

- `week`：星期几，取值1-7（1=周一，7=周日）
- `shifting`：周期偏移量，负数往前，正数往后
- `format_str`：日期格式，如 `yyyy-MM-dd`

**返回值：** 格式化后的日期字符串

```python
from datetime import datetime, timedelta
import argparse

def get_week_date_func(week: int, shifting: int, format_str: str) -> str:
    """
    获得星期对应的日期
    :param week: 星期几，取值范围1-7（1=周一，7=周日）
    :param shifting: 周期偏移量，负数表示往前，正数表示往后
    :param format_str: 日期格式，如 yyyy-MM-dd
    :return: 格式化的日期字符串
    """
    if not 1 <= week <= 7:
        raise ValueError("Week must be between 1 and 7")
    
    current_time = [datetime.now](http://datetime.now)()
    
    # 获取当前是星期几（1=周一，7=周日）
    current_weekday = current_time.isoweekday()
    
    # 计算目标日期
    # 首先计算本周的目标星期几
    days_diff = week - current_weekday
    target_date = current_time + timedelta(days=days_diff)
    
    # 再加上周期偏移
    target_date = target_date + timedelta(weeks=shifting)
    
    # 转换Java风格的格式为Python风格
    python_format = format_str.replace('yyyy', '%Y').replace('MM', '%m').replace('dd', '%d')
    
    return target_date.strftime(python_format)

def main():
    parser = argparse.ArgumentParser(description='获得星期对应的日期')
    parser.add_argument('--week', type=int, required=True, help='星期几（1-7）')
    parser.add_argument('--shifting', type=int, required=True, help='周期偏移量')
    parser.add_argument('--format', type=str, required=True, help='日期格式')
    
    args = parser.parse_args()
    print(get_week_date_func(args.week, args.shifting, args.format))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: 3周前的周一")
    print(get_week_date_func(1, -3, 'yyyy-MM-dd'))
    
    print("\n测试用例 2: 2周后的周三")
    print(get_week_date_func(3, 2, 'yyyy-MM-dd'))
    
    print("\n测试用例 3: 本周五")
    print(get_week_date_func(5, 0, 'yyyy-MM-dd'))
    
    print("\n测试用例 4: 下周日")
    print(get_week_date_func(7, 1, 'yyyyMMdd'))
```

---

## 2. 随机函数

### 2.1 __[randomInt.py](http://randomInt.py)

**函数名称：** 生成随机整数

**函数介绍：** 在指定范围内生成随机整数。如果不指定范围，默认生成0到9999999之间的随机数。

**参数说明：**

- `min_val`：取值下限，可选参数
- `max_val`：取值上限，可选参数

**返回值：** 随机整数

```python
import random
import argparse

def random_int_func(min_val: int = None, max_val: int = None) -> int:
    """
    获得指定范围的随机整数
    :param min_val: 取值下限
    :param max_val: 取值上限
    :return: 随机整数
    """
    # 如果参数未设置，使用默认范围
    if min_val is None or max_val is None:
        min_val = 0
        max_val = 9999999
    
    return random.randint(min_val, max_val)

def main():
    parser = argparse.ArgumentParser(description='获得指定范围的随机整数')
    parser.add_argument('--min', type=int, default=None, help='取值下限')
    parser.add_argument('--max', type=int, default=None, help='取值上限')
    
    args = parser.parse_args()
    print(random_int_func(args.min, args.max))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: -100到100的随机整数")
    print(random_int_func(-100, 100))
    
    print("\n测试用例 2: 0到100的随机整数")
    print(random_int_func(0, 100))
    
    print("\n测试用例 3: 默认范围的随机整数")
    print(random_int_func())
    
    print("\n测试用例 4: 生成5个随机数")
    for i in range(5):
        print(f"  第{i+1}个: {random_int_func(1, 10)}")
    # 使用命令行参数时调用主函数
    main()
```

---

### 2.2 __[randomString.py](http://randomString.py)

**函数名称：** 生成随机字符串

**函数介绍：** 生成指定长度的随机字符串。可以自定义字符范围，如果不指定则默认使用英文字母和数字。

**参数说明：**

- `length`：字符串长度
- `characters`：允许出现的字符，可选参数

**返回值：** 随机字符串

```python
import random
import string
import argparse

def random_string_func(length: int, characters: str = '') -> str:
    """
    获得随机字符串
    :param length: 字符串长度
    :param characters: 允许出现的字符，为空则使用英文和数字
    :return: 随机字符串
    """
    if not characters:
        # 默认使用英文字母和数字
        characters = string.ascii_letters + string.digits
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description='获得随机字符串')
    parser.add_argument('--length', type=int, required=True, help='字符串长度')
    parser.add_argument('--characters', type=str, default='', help='允许的字符')
    
    args = parser.parse_args()
    print(random_string_func(args.length, args.characters))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: 长度为10，只包含abc的随机字符串")
    print(random_string_func(10, 'abc'))
    
    print("\n测试用例 2: 长度为8，默认字符范围的随机字符串")
    print(random_string_func(8))
    
    print("\n测试用例 3: 长度为6，只包含数字的随机字符串")
    print(random_string_func(6, '0123456789'))
    
    print("\n测试用例 4: 生成5个随机字符串")
    for i in range(5):
        print(f"  第{i+1}个: {random_string_func(5, 'xyz')}")
    # 使用命令行参数时调用主函数
    main()
```

---

## 3. 取模函数

### 3.1 __[mod.py](http://mod.py)

**函数名称：** 取模运算

**函数介绍：** 执行取模运算，并支持结果左侧补零到指定长度。常用于ID生成、哈希分片等场景。

**参数说明：**

- `dividend`：被除数
- `divider`：除数
- `length`：总长度，不足时左侧补0，可选参数

**返回值：** 取模结果字符串

```python
import argparse

def mod_func(dividend: int, divider: int, length: int = None) -> str:
    """
    通用取模函数，支持取模及补全长度
    :param dividend: 被除数
    :param divider: 除数
    :param length: 总长度，不足左侧用0补全
    :return: 取模结果（字符串）
    """
    if divider == 0:
        raise ValueError("Divider cannot be zero")
    
    result = dividend % divider
    
    # 如果指定了长度，左侧补0
    if length is not None:
        return str(result).zfill(length)
    
    return str(result)

def main():
    parser = argparse.ArgumentParser(description='通用取模函数')
    parser.add_argument('--dividend', type=int, required =True, help='被除数')
    parser.add_argument('--divider', type=int, required=True, help='除数')
    parser.add_argument('--length', type=int, default=None, help='总长度')
    
    args = parser.parse_args()
    print(mod_func(args.dividend, args.divider, args.length))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: 34 % 32")
    print(mod_func(34, 32))
    
    print("\n测试用例 2: 34 % 32，补全到4位")
    print(mod_func(34, 32, 4))
    
    print("\n测试用例 3: 100 % 7")
    print(mod_func(100, 7))
    
    print("\n测试用例 4: 100 % 7，补全到6位")
    print(mod_func(100, 7, 6))
    # 使用命令行参数时调用主函数
    main()
```

---

## 4. 数学函数

### 4.1 __MATH_[abs.py](http://abs.py)

**函数名称：** 取绝对值

**函数介绍：** 计算数值的绝对值，返回非负数。

**参数说明：**

- `value`：输入数值

**返回值：** 绝对值

```python
import math
import argparse

def math_abs_func(value: float) -> float:
    """
    取绝对值
    :param value: 输入值
    :return: 绝对值
    """
    return abs(value)

def main():
    parser = argparse.ArgumentParser(description='取绝对值')
    parser.add_argument('--value', type=float, required=True, help='输入值')
    
    args = parser.parse_args()
    print(math_abs_func(args.value))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: abs(-1.0)")
    print(math_abs_func(-1.0))
    
    print("\n测试用例 2: abs(5.5)")
    print(math_abs_func(5.5))
    
    print("\n测试用例 3: abs(-100)")
    print(math_abs_func(-100))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.2 __MATH_[ceil.py](http://ceil.py)

**函数名称：** 向上取整

**函数介绍：** 返回不小于给定数值的最小整数（向上取整）。

**参数说明：**

- `value`：输入数值

**返回值：** 向上取整后的整数

```python
import math
import argparse

def math_ceil_func(value: float) -> int:
    """
    取不小于value的下一个整数（向上取整）
    :param value: 输入值
    :return: 向上取整结果
    """
    return math.ceil(value)

def main():
    parser = argparse.ArgumentParser(description='向上取整')
    parser.add_argument('--value', type=float, required=True, help='输入值')
    
    args = parser.parse_args()
    print(math_ceil_func(args.value))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: ceil(-1.5)")
    print(math_ceil_func(-1.5))
    
    print("\n测试用例 2: ceil(2.1)")
    print(math_ceil_func(2.1))
    
    print("\n测试用例 3: ceil(5.0)")
    print(math_ceil_func(5.0))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.3 __MATH_[floor.py](http://floor.py)

**函数名称：** 向下取整

**函数介绍：** 返回不大于给定数值的最大整数（向下取整）。

**参数说明：**

- `value`：输入数值

**返回值：** 向下取整后的整数

```python
import math
import argparse

def math_floor_func(value: float) -> int:
    """
    取不大于value的下一个整数（向下取整）
    :param value: 输入值
    :return: 向下取整结果
    """
    return math.floor(value)

def main():
    parser = argparse.ArgumentParser(description='向下取整')
    parser.add_argument('--value', type=float, required=True, help='输入值')
    
    args = parser.parse_args()
    print(math_floor_func(args.value))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: floor(-1.5)")
    print(math_floor_func(-1.5))
    
    print("\n测试用例 2: floor(2.9)")
    print(math_floor_func(2.9))
    
    print("\n测试用例 3: floor(5.0)")
    print(math_floor_func(5.0))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.4 __MATH_[round.py](http://round.py)

**函数名称：** 四舍五入

**函数介绍：** 对数值进行四舍五入运算，返回最接近的整数。

**参数说明：**

- `value`：输入数值

**返回值：** 四舍五入后的整数

```python
import argparse

def math_round_func(value: float) -> int:
    """
    四舍五入
    :param value: 输入值
    :return: 四舍五入结果
    """
    return round(value)

def main():
    parser = argparse.ArgumentParser(description='四舍五入')
    parser.add_argument('--value', type=float, required=True, help='输入值')
    
    args = parser.parse_args()
    print(math_round_func(args.value))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: round(-1.2)")
    print(math_round_func(-1.2))
    
    print("\n测试用例 2: round(2.5)")
    print(math_round_func(2.5))
    
    print("\n测试用例 3: round(3.7)")
    print(math_round_func(3.7))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.5 __MATH_[max.py](http://max.py)

**函数名称：** 取最大值

**函数介绍：** 比较两个数值，返回较大的那个。

**参数说明：**

- `value1`：第一个数值
- `value2`：第二个数值

**返回值：** 两数中的最大值

```python
import argparse

def math_max_func(value1: float, value2: float) -> float:
    """
    取两个值中的最大值
    :param value1: 第一个值
    :param value2: 第二个值
    :return: 最大值
    """
    return max(value1, value2)

def main():
    parser = argparse.ArgumentParser(description='取最大值')
    parser.add_argument('--value1', type=float, required=True, help='第一个值')
    parser.add_argument('--value2', type=float, required=True, help='第二个值')
    
    args = parser.parse_args()
    print(math_max_func(args.value1, args.value2))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: max(3, 5)")
    print(math_max_func(3, 5))
    
    print("\n测试用例 2: max(-1, -5)")
    print(math_max_func(-1, -5))
    
    print("\n测试用例 3: max(3.14, 2.71)")
    print(math_max_func(3.14, 2.71))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.6 __MATH_[min.py](http://min.py)

**函数名称：** 取最小值

**函数介绍：** 比较两个数值，返回较小的那个。

**参数说明：**

- `value1`：第一个数值
- `value2`：第二个数值

**返回值：** 两数中的最小值

```python
import argparse

def math_min_func(value1: float, value2: float) -> float:
    """
    取两个值中的最小值
    :param value1: 第一个值
    :param value2: 第二个值
    :return: 最小值
    """
    return min(value1, value2)

def main():
    parser = argparse.ArgumentParser(description='取最小值')
    parser.add_argument('--value1', type=float, required=True, help='第一个值')
    parser.add_argument('--value2', type=float, required=True, help='第二个值')
    
    args = parser.parse_args()
    print(math_min_func(args.value1, args.value2))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: min(3, 5)")
    print(math_min_func(3, 5))
    
    print("\n测试用例 2: min(-1, -5)")
    print(math_min_func(-1, -5))
    
    print("\n测试用例 3: min(3.14, 2.71)")
    print(math_min_func(3.14, 2.71))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.7 __MATH_[pow.py](http://pow.py)

**函数名称：** 幂运算

**函数介绍：** 计算底数的指数次幂，支持小数指数（如开方运算）。

**参数说明：**

- `base`：底数
- `exponent`：指数

**返回值：** 幂运算结果

```python
import argparse

def math_pow_func(base: float, exponent: float) -> float:
    """
    计算乘方
    :param base: 底数
    :param exponent: 指数
    :return: base的exponent次方
    """
    return pow(base, exponent)

def main():
    parser = argparse.ArgumentParser(description='计算乘方')
    parser.add_argument('--base', type=float, required=True, help='底数')
    parser.add_argument('--exponent', type=float, required=True, help='指数')
    
    args = parser.parse_args()
    print(math_pow_func(args.base, args.exponent))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: pow(2, 3)")
    print(math_pow_func(2, 3))
    
    print("\n测试用例 2: pow(5, 2)")
    print(math_pow_func(5, 2))
    
    print("\n测试用例 3: pow(2, 0.5)")
    print(math_pow_func(2, 0.5))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.8 __MATH_[sqrt.py](http://sqrt.py)

**函数名称：** 开平方

**函数介绍：** 计算数值的平方根。输入必须为非负数。

**参数说明：**

- `value`：输入数值（非负）

**返回值：** 平方根

```python
import math
import argparse

def math_sqrt_func(value: float) -> float:
    """
    开平方
    :param value: 输入值
    :return: 平方根
    """
    if value < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(value)

def main():
    parser = argparse.ArgumentParser(description='开平方')
    parser.add_argument('--value', type=float, required=True, help='输入值')
    
    args = parser.parse_args()
    print(math_sqrt_func(args.value))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: sqrt(4)")
    print(math_sqrt_func(4))
    
    print("\n测试用例 2: sqrt(9)")
    print(math_sqrt_func(9))
    
    print("\n测试用例 3: sqrt(2)")
    print(math_sqrt_func(2))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.9 __MATH_[add.py](http://add.py)

**函数名称：** 加法运算

**函数介绍：** 计算两个数值的和。

**参数说明：**

- `value1`：第一个加数
- `value2`：第二个加数

**返回值：** 两数之和

```python
import argparse

def math_add_func(value1: float, value2: float) -> float:
    """
    计算加和
    :param value1: 第一个值
    :param value2: 第二个值
    :return: 两数之和
    """
    return value1 + value2

def main():
    parser = argparse.ArgumentParser(description='计算加和')
    parser.add_argument('--value1', type=float, required=True, help='第一个值')
    parser.add_argument('--value2', type=float, required=True, help='第二个值')
    
    args = parser.parse_args()
    print(math_add_func(args.value1, args.value2))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: add(2, 3)")
    print(math_add_func(2, 3))
    
    print("\n测试用例 2: add(1.5, 2.5)")
    print(math_add_func(1.5, 2.5))
    
    print("\n测试用例 3: add(-1, 5)")
    print(math_add_func(-1, 5))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.10 __MATH_[sub.py](http://sub.py)

**函数名称：** 减法运算

**函数介绍：** 计算两个数值的差。

**参数说明：**

- `value1`：被减数
- `value2`：减数

**返回值：** 两数之差

```python
import argparse

def math_sub_func(value1: float, value2: float) -> float:
    """
    计算差值
    :param value1: 被减数
    :param value2: 减数
    :return: 两数之差
    """
    return value1 - value2

def main():
    parser = argparse.ArgumentParser(description='计算差值')
    parser.add_argument('--value1', type=float, required=True, help='被减数')
    parser.add_argument('--value2', type=float, required=True, help='减数')
    
    args = parser.parse_args()
    print(math_sub_func(args.value1, args.value2))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: sub(5, 3)")
    print(math_sub_func(5, 3))
    
    print("\n测试用例 2: sub(1.0, 0.5)")
    print(math_sub_func(1.0, 0.5))
    
    print("\n测试用例 3: sub(-1, 5)")
    print(math_sub_func(-1, 5))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.11 __MATH_[mul.py](http://mul.py)

**函数名称：** 乘法运算

**函数介绍：** 计算两个数值的积。

**参数说明：**

- `value1`：第一个乘数
- `value2`：第二个乘数

**返回值：** 两数之积

```python
import argparse

def math_mul_func(value1: float, value2: float) -> float:
    """
    计算乘积
    :param value1: 第一个值
    :param value2: 第二个值
    :return: 两数之积
    """
    return value1 * value2

def main():
    parser = argparse.ArgumentParser(description='计算乘积')
    parser.add_argument('--value1', type=float, required=True, help='第一个值')
    parser.add_argument('--value2', type=float, required=True, help='第二个值')
    
    args = parser.parse_args()
    print(math_mul_func(args.value1, args.value2))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: mul(2, 3)")
    print(math_mul_func(2, 3))
    
    print("\n测试用例 2: mul(1.5, 2)")
    print(math_mul_func(1.5, 2))
    
    print("\n测试用例 3: mul(-2, 5)")
    print(math_mul_func(-2, 5))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.12 __MATH_[div.py](http://div.py)

**函数名称：** 除法运算

**函数介绍：** 计算两个数值的商。除数不能为零。

**参数说明：**

- `value1`：被除数
- `value2`：除数（非零）

**返回值：** 两数之商

```python
import argparse

def math_div_func(value1: float, value2: float) -> float:
    """
    计算商
    :param value1: 被除数
    :param value2: 除数
    :return: 两数之商
    """
    if value2 == 0:
        raise ValueError("Division by zero")
    return value1 / value2

def main():
    parser = argparse.ArgumentParser(description='计算商')
    parser.add_argument('--value1', type=float, required=True, help='被除数')
    parser.add_argument('--value2', type=float, required=True, help='除数')
    
    args = parser.parse_args()
    print(math_div_func(args.value1, args.value2))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: div(6, 3)")
    print(math_div_func(6, 3))
    
    print("\n测试用例 2: div(1.0, 2)")
    print(math_div_func(1.0, 2))
    
    print("\n测试用例 3: div(10, 4)")
    print(math_div_func(10, 4))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.13 __MATH_[sin.py](http://sin.py)

**函数名称：** 正弦函数

**函数介绍：** 计算角度的正弦值。支持弧度制和角度制输入。

**参数说明：**

- `angle`：角度值（默认为弧度）
- `in_degrees`：是否使用角度制，可选参数

**返回值：** 正弦值

```python
import math
import argparse

def math_sin_func(angle: float, in_degrees: bool = False) -> float:
    """
    计算正弦值
    :param angle: 角度（默认为弧度）
    :param in_degrees: 是否为角度制
    :return: 正弦值
    """
    if in_degrees:
        angle = math.radians(angle)
    return math.sin(angle)

def main():
    parser = argparse.ArgumentParser(description='计算正弦值')
    parser.add_argument('--angle', type=float, required=True, help='角度值')
    parser.add_argument('--degrees', action='store_true', help='使用角度制')
    
    args = parser.parse_args()
    print(math_sin_func(args.angle, args.degrees))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: sin(π/2) 弧度")
    print(math_sin_func(math.pi/2))
    
    print("\n测试用例 2: sin(90) 角度")
    print(math_sin_func(90, in_degrees=True))
    
    print("\n测试用例 3: sin(30) 角度")
    print(math_sin_func(30, in_degrees=True))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.14 __MATH_[cos.py](http://cos.py)

**函数名称：** 余弦函数

**函数介绍：** 计算角度的余弦值。支持弧度制和角度制输入。

**参数说明：**

- `angle`：角度值（默认为弧度）
- `in_degrees`：是否使用角度制，可选参数

**返回值：** 余弦值

```python
import math
import argparse

def math_cos_func(angle: float, in_degrees: bool = False) -> float:
    """
    计算余弦值
    :param angle: 角度（默认为弧度）
    :param in_degrees: 是否为角度制
    :return: 余弦值
    """
    if in_degrees:
        angle = math.radians(angle)
    return math.cos(angle)

def main():
    parser = argparse.ArgumentParser(description='计算余弦值')
    parser.add_argument('--angle', type=float, required=True, help='角度值')
    parser.add_argument('--degrees', action='store_true', help='使用角度制')
    
    args = parser.parse_args()
    print(math_cos_func(args.angle, args.degrees))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: cos(0) 弧度")
    print(math_cos_func(0))
    
    print("\n测试用例 2: cos(90) 角度")
    print(math_cos_func(90, in_degrees=True))
    
    print("\n测试用例 3: cos(60) 角度")
    print(math_cos_func(60, in_degrees=True))
    # 使用命令行参数时调用主函数
    main()
```

---

### 4.15 __MATH_[tan.py](http://tan.py)

**函数名称：** 正切函数

**函数介绍：** 计算角度的正切值。支持弧度制和角度制输入。

**参数说明：**

- `angle`：角度值（默认为弧度）
- `in_degrees`：是否使用角度制，可选参数

**返回值：** 正切值

```python
import math
import argparse

def math_tan_func(angle: float, in_degrees: bool = False) -> float:
    """
    计算正切值
    :param angle: 角度（默认为弧度）
    :param in_degrees: 是否为角度制
    :return: 正切值
    """
    if in_degrees:
        angle = math.radians(angle)
    return math.tan(angle)

def main():
    parser = argparse.ArgumentParser(description='计算正切值')
    parser.add_argument('--angle', type=float, required=True, help='角度值')
    parser.add_argument('--degrees', action='store_true', help='使用角度制')
    
    args = parser.parse_args()
    print(math_tan_func(args.angle, args.degrees))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: tan(π/4) 弧度")
    print(math_tan_func(math.pi/4))
    
    print("\n测试用例 2: tan(45) 角度")
    print(math_tan_func(45, in_degrees=True))
    
    print("\n测试用例 3: tan(0) 角度")
    print(math_tan_func(0, in_degrees=True))
    # 使用命令行参数时调用主函数
    main()
```

---

## 5. 表达式计算函数

### 5.1 __[MATHEXP.py](http://MATHEXP.py)

**函数名称：** 数学表达式计算

**函数介绍：** 计算字符串形式的数学表达式，支持加减乘除、括号、幂运算等。可以指定返回值类型（整数或浮点数）。

**参数说明：**

- `expression`：数学表达式字符串，如 `1+2*3`
- `return_type`：返回类型，`b/s/i/l` 为整数，`f/d` 为浮点数

**返回值：** 表达式计算结果

```python
import re
import argparse

def math_exp_func(expression: str, return_type: str = 'f') -> any:
    """
    计算数学表达式
    :param expression: 数学表达式字符串
    :param return_type: 返回类型 b=byte, s=short, i=int, l=long, f=float, d=double
    :return: 计算结果
    """
    try:
        # 计算表达式
        result = eval(expression)
        
        # 根据返回类型转换
        if return_type.lower() in ['b', 's', 'i', 'l']:
            return int(result)
        elif return_type.lower() in ['f', 'd']:
            return float(result)
        else:
            return result
    except Exception as e:
        raise ValueError(f"Expression evaluation failed: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='计算数学表达式')
    parser.add_argument('--expression', type=str, required=True, help='数学表达式')
    parser.add_argument('--type', type=str, default='f', help='返回类型')
    
    args = parser.parse_args()
    print(math_exp_func(args.expression, args.type))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: 1+2*3, byte型")
    print(math_exp_func('1+2*3', 'b'))
    
    print("\n测试用例 2: 5+(1+2*3)*4, short型")
    print(math_exp_func('5+(1+2*3)*4', 's'))
    
    print("\n测试用例 3: (10+5)/3, float型")
    print(math_exp_func('(10+5)/3', 'f'))
    
    print("\n测试用例 4: 2**3 + 4*5, int型")
    print(math_exp_func('2**3 + 4*5', 'i'))
    # 使用命令行参数时调用主函数
    main()
```

---

## 6. 加密函数

### 6.1 __[MD5.py](http://MD5.py)

**函数名称：** MD5加密

**函数介绍：** 对输入字符串进行MD5哈希加密，返回32位小写十六进制字符串。常用于数据签名、密码加密等场景。

**参数说明：**

- `param`：待加密的字符串

**返回值：** 32位MD5加密结果（小写）

```python
import hashlib
import argparse

def md5_func(param: str) -> str:
    """
    MD5计算函数
    :param param: 输入字符串
    :return: 32位MD5加密结果（小写）
    """
    # 创建MD5对象
    md5_hash = [hashlib.md](http://hashlib.md)5()
    
    # 更新哈希对象（需要编码为字节）
    md5_hash.update(param.encode('utf-8'))
    
    # 返回32位十六进制字符串
    return md5_hash.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='MD5加密函数')
    parser.add_argument('--param', type=str, required=True, help='输入字符串')
    
    args = parser.parse_args()
    print(md5_func(args.param))

if __name__ == "__main__":
    # 测试用例
    print("测试用例 1: MD5('aavsd')")
    print(md5_func('aavsd'))
    
    print("\n测试用例 2: MD5('hello')")
    print(md5_func('hello'))
    
    print("\n测试用例 3: MD5('123456')")
    print(md5_func('123456'))
    
    print("\n测试用例 4: MD5('[test@example.com](mailto:test@example.com)')")
    print(md5_func('[test@example.com](mailto:test@example.com)'))
    main()
```