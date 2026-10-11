---
title: "README"
description: "C++ Good Coder考试-词表解析读取工具类"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\C++ Good Coder考试-词表解析读取工具类\\README.md"
---
C++ Good Coder考试-词表解析读取工具类

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 一、认证试题
在我们的开发任务中，最常见的一项工作就是解析并读取各种词表文件，请设计并实现一个通用的词表解析读取工具类(一个或者几个class/struct组成)， 解析并读取如下形式的词表：

<col1>\t<col2>\t...\t<coln>

每一行都是一条记录，每一列可能的类型包括：

* int * float * char * * 形如num:item1,item2,item3的数组（可以理解为T[num]的数组，T是用户给出某种build-in类型） * 其他用户自定义类型(需要灵活支持多种自定义类型)

每一列的数据中均不包含\t字符，每一行以\n结尾。

[02 认证试题](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1036741331)

## 二、代码部分
### 2.1、代码结构
```
project  
  
demo.py: 运行入口  
include目录：  
    no_copy_common.h: 禁止拷贝构造函数和赋值构造函数通用文件  
    parse.h: 行内容解析文件头文件  
    private_parse.h: 用户自定义解析文件头文件  
    public_parse.h: 通用解析文件头文件  
    read_file_line_by_line.h: 逐行读取文档头文件  
src目录:  
    parse.cpp: 行内容解析文件  
    private_parse.cpp: 用户自定义解析文件  
    public_parse.cpp: 通用解析文件  
    read_file_line_by_line.cpp: 逐行读取文档  
test目录：存放单元测试文件  
    main.cpp: 单元测试运行入口  
  
README.md: 说明文档  
data目录: 存放数据文件  
    data.txt: 待解析文件
```
![](../../../../_remote_images/08-周洁学习记录/local_assets/oSBCcbI9TzQp5F/image_001.bin "")
### 2.2、具体实现
[.vscode配置与运行](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1470858500)

[ReadFileLineByLine 文件读取类 （实现逐行读取）](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1470858510)

[Parser 解析类 （兼容通用与用户自定义）](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1470858530)

[使用GTest进行单元测试](https://wiki2ku.baidu-int.com/pubapi/urlmap?id=1623224846)

### 2.3、demo运行
#### 待解析数据
**data.txt**

```
test1\t123\t2.4\n
test2\t123\t2.4\n
test3\t123\t2.4\n
test4\t123\t2.4\n
test5\t123\t2.4\tzhoujie 26 153.8\t11 22 33\n
```
#### 程序入口
**demo.py**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/19
// Des:     词表解析读取工具类demo文件 


#include <iostream>

#include "include/read_file_line_by_line.h"
#include "include/parse.h"

using namespace std;
using namespace parse;

int main() {
    string file_name = "./data/data.txt";
    ReadFileLineByLine file_reader;
    Parser parser(0);  // 初始行数 分割分隔符

    // 打开文件
    if (!file_reader.open_file(file_name)) {
        return -1;
    }
    cout << endl;

    // 读取第一行内容 test1\t123\t2.4\n
    char* x = new char[20];
    int y = 0;
    float z = 0;
    string line1 = file_reader.get_index_line(1);
    cout << "当前待处理行内容: " << line1 << endl;
    parser.parse_line(line1);  // 解析第一行
    parser.get_column(0, x);  // 解析第一行 第1列 的 字符串
    parser.get_column(1, &y);  // 解析第一行 第2列 的 整数
    parser.get_column(2, &z);  // 解析第一行 第3列 的 小数
    cout << "读取第一行结果：" << x << ", " << y << ", " << z << ", " << endl;
    // 解析错误数据
    float wr = 0;
    parser.get_column(0, &wr);
    cout << "读取错误格式结果：" << wr << endl;
    cout << endl;
    delete[] x;

    // 读取第五行内容 test5\t123\t2.4\tzhoujie 26 153.8\t11 22 33\n
    Person person;
    int* lst = new int[3];
    vector<int> vec;
    string line2 = file_reader.get_index_line(5);
    cout << "当前待处理行内容: " << line2 << endl;
    parser.parse_line(line2);  // 解析第五行
    parser.get_column(3, &person);  // 解析第五行 第4列 的 自定义Person结构
    cout << "读取自定义结构Person结果：" << person.name << ", " << person.age << ", " << person.height << endl;
    parser.get_column(4, &lst);  // 解析第五行 第5列 的 自定义数组结构 使用 int*
    cout << "读取自定义数组(使用 int*)结果：";
    for (int i = 0; i < 3; i++) {
        cout << lst[i] << " ";
    }
    cout << endl;
    parser.get_column(4, &vec);  // 解析第五行 第5列 的 自定义数组结构 使用 vector<int>
    cout << "读取自定义数组(使用 vector<int>)结果：";
    for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    delete[] lst;

    return 0;
}
```
#### 运行结果
![](../../../../_remote_images/08-周洁学习记录/local_assets/oSBCcbI9TzQp5F/image_002.bin "")
### 2.4、Icode地址
[https://console.cloud.baidu-int.com/devops/icode/repos/baidu/goodcoder/zhoujie19_cpp/reviews/17058061/files](https://console.cloud.baidu-int.com/devops/icode/repos/baidu/goodcoder/zhoujie19_cpp/reviews/17058061/files)


