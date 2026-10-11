---
title: "Parser 解析类 （兼容通用与用户自定义）"
description: "Parser 解析类 （兼容通用与用户自定义）"
date: "2026-10-11"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\知识库文档下载_2026-04-28\\知识库文档下载_2026-04-28\\mSXjJv4PDMDxpo\\Good Coder考试记录\\C++ Good Coder考试-词表解析读取工具类\\Parser 解析类 （兼容通用与用户自定义）.md"
---
Parser 解析类 （兼容通用与用户自定义）

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
### 代码构成：
![](../../../assets/AHh76ohHHGAqAw/image_001.bin "")
public_parse用于处理通用数据，用户自定义数据结构在private_parse文件中进行数据解析，主要通过重载完成对多种数据格式的解析。 public_parse：其中定义了通用的int、float、char*的解析方法。 private_parse：自定义结构的解析可以在private_parse中自行编写，当前定义了int*、vector<int>、和自定义结构Person。

### 代码实现：
宏禁止拷贝构造函数和赋值构造函数通用文件:

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
解析文件：

**parse.h**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     行内容解析文件头文件


#ifndef  PARSER_H
#define  PARSER_H

#include <string>
#include <vector>

#include "no_copy_common.h"
#include "public_parse.h"
#include "private_parse.h"

namespace parse {
class Parser {
public:
    // 使用初始化列表初始化数据成员
    explicit Parser(int col_num): _col_num(col_num) {
    }
    bool parse_line(const std::string& line, const std::string& delim = "\\t");
    void init_words_vector();

    template<class T> 
    bool get_column(const int index, T* result) {
        if (index < _col_num) {
            std::string word = _words_vector[index];
            const char* c_word = word.c_str();
            return parse(c_word, result);
        }
        return false;
    } 
private:
    std::vector<std::string> _words_vector;
    int _col_num;
    DISALLOW_COPY_AND_ASSIGN(Parser);
};

}  // namespace parse

#endif  // PARSER_H
```
**parse.cpp**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     行内容解析文件头文件


#include "../include/parse.h"

#include <iostream>
#include <string>
#include <vector>

namespace parse {
bool Parser::parse_line(const std::string& line, const std::string& delim) {
    // 初始化
    init_words_vector();
    std::string::size_type pos1, pos2;
    pos2 = line.find(delim);
    pos1 = 0;
    while(std::string::npos != pos2) {
        _words_vector.push_back(line.substr(pos1, pos2-pos1));
        pos1 = pos2 + delim.size();
        pos2 = line.find(delim, pos1);
    }
    if(pos1 != line.length()) {
        _words_vector.push_back(line.substr(pos1));
    }
    _col_num = line.size();
    return true;
};

void Parser::init_words_vector() {
    std::vector<std::string> tmp;
    _words_vector.swap(tmp);
};

}  // namespace parse
```
通用解析文件：

**public_parse.h**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     通用解析文件头文件


#ifndef  PUBLIC_PARSER_H
#define  PUBLIC_PARSER_H

#include <stdint.h>

namespace parse {
bool parse(const char* str, int* result);
bool parse(const char* str, char* result);
bool parse(const char* str, float* result);
bool parse(const char* str, uint32_t* result);
bool parse(const char* str, uint64_t* result);

}  // namespace parse

#endif  // PUBLIC_PARSER_H
```
**public_parse.cpp**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     通用解析文件


#include "../include/public_parse.h"

#include <stdint.h>
#include <stdio.h>
#include <string>

namespace parse {
bool parse(const char* str, int* result) {
    if (NULL != str) {
        if (1 == sscanf(str, "%d", result)) {
            return true;
        }
    }
    return false;
}

bool parse(const char* str, float* result) {
    if (NULL != str) {
        if (1 == sscanf(str, "%f", result)) {
            return true;
        }
    }
    return false;
}

bool parse(const char* str, char* result) {
    if (NULL != str && NULL != result) {
        // 方法一 SA禁止使用const_cast
        // char *pCh = const_cast<char *>(str);
        // result = pCh;

        // 方法二 SA禁止使用strcpy
        // strcpy(result, str);

        // 方法三
        const char* start_str = str;
        char* result_str = result;
        while ('\t' != *start_str && '\n' != *start_str && '\0' != *start_str) {
            *result_str++ = *start_str++;
        }
        *result_str = '\0';

        return true;
    }
    return false; 
}

}  // namespace parse
```
用户自定义解析文件：

**private_parse.h**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     用户自定义解析文件头文件


#ifndef  PRIVATE_PARSER_H
#define  PRIVATE_PARSER_H

#include <stdio.h>
#include <string>
#include <vector>

namespace parse {
// Person 类型
typedef struct Person 
{
    std::string name;
    int age;
    float height;
}Person;

bool parse(const char* str, Person* result);
bool parse(const char* str, std::vector<int>* result);
bool parse(const char* str, int** result);

}  // namespace parse

#endif  // PRIVATE_PARSER_H
```
**private_parse.cpp**

```
// Copyright 2021 Baidu Inc. All Rights Reserved.
// Authors: zhoujie19(zhoujie19@baidu.com)
// Date:    2021/02/18
// Des:     行内容解析文件头文件


#include "../include/parse.h"

#include <iostream>
#include <string>
#include <vector>

namespace parse {
bool Parser::parse_line(const std::string& line, const std::string& delim) {
    // 初始化
    init_words_vector();
    std::string::size_type pos1, pos2;
    pos2 = line.find(delim);
    pos1 = 0;
    while(std::string::npos != pos2) {
        _words_vector.push_back(line.substr(pos1, pos2-pos1));
        pos1 = pos2 + delim.size();
        pos2 = line.find(delim, pos1);
    }
    if(pos1 != line.length()) {
        _words_vector.push_back(line.substr(pos1));
    }
    _col_num = line.size();
    return true;
};

void Parser::init_words_vector() {
    std::vector<std::string> tmp;
    _words_vector.swap(tmp);
};

}  // namespace parse
```

