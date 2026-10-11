---
title: "ReadFileLineByLine 文件读取类 （实现逐行读取）"
description: "ReadFileLineByLine 文件读取类 （实现逐行读取）"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\C++ Good Coder考试-词表解析读取工具类\\ReadFileLineByLine 文件读取类 （实现逐行读取）.md"
---
ReadFileLineByLine 文件读取类 （实现逐行读取）

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
**no_copy_common.h**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/05/08
// Des:     DISALLOW_COPY_AND_ASSIGN 宏禁止拷贝构造函数和赋值构造函数通用文件


#ifndef NO_COPY_COMMON_H
#define NO_COPY_COMMON_H

#define DISALLOW_COPY_AND_ASSIGN(TypeName) \
        TypeName(const TypeName&); \
        TypeName& operator=(const TypeName&)

#endif  // NO_COPY_COMMON_H
```
**read_file_line_by_line.h**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     逐行读取文档头文件 


#ifndef READ_FILE_LINE_BY_LINE_H
#define READ_FILE_LINE_BY_LINE_H

#include <fstream>
#include <string>

#include "no_copy_common.h"

namespace parse {
class ReadFileLineByLine {
public:
    ReadFileLineByLine() {
        _index = 1;
    }
    ~ReadFileLineByLine() {
        _file.close();
    }
    bool open_file(const std::string& file_name);
    std::string get_index_line(int index);
    std::string get_next_line();
    bool has_next_line();
private:
    std::ifstream _file;
    int _index;
    DISALLOW_COPY_AND_ASSIGN(ReadFileLineByLine);
};

}  // namespace parse

#endif  // READ_FILE_LINE_BY_LINE_H
```
**read_file_line_by_line.cpp**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     逐行读取文档文件 


#include "../include/read_file_line_by_line.h"

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

namespace parse {
std::string ReadFileLineByLine::get_index_line(int index) {
    std::string line;
    while (has_next_line() and _index <= index) {
        line = get_next_line();
    }
    return line;
}

bool ReadFileLineByLine::open_file(const std::string& file_name) {
    std::cout << "正在打开文件: " << file_name << std::endl;
    _file.open(file_name);
    if (!_file.is_open()) {
        std::cout << "打开文件 " << file_name << " 失败" << std::endl;
        return false;
    }
    return true;
}

std::string ReadFileLineByLine::get_next_line() {
    std::string line;
    std::getline(_file, line);
    std::cout << "逐行读取Line" << _index << ": " << line << std::endl;
    _index += 1;
    return line;
}

bool ReadFileLineByLine::has_next_line() {
    return _file.peek() != EOF;
}

}  // namespace parse
```

