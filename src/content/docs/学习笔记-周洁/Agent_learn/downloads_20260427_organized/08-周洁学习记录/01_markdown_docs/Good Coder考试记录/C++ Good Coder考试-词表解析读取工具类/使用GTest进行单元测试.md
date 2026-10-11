---
title: "使用GTest进行单元测试"
description: "使用GTest进行单元测试"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\Good Coder考试记录\\C++ Good Coder考试-词表解析读取工具类\\使用GTest进行单元测试.md"
---
使用GTest进行单元测试

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
## 
## 1、介绍
gtest是一个跨平台的C++单元测试框架。它提供了丰富的断言、致命和非致命判断、参数化、死亡测试等等。

地址：[https://github.com/google/googletest](https://github.com/google/googletest)

## 2、安装
```
git clone https://github.com/google/googletest
cd googletest
mkdir build
cd build
cmake ..
make
make install
```
## 3、测试用例
单测编写

**main.cpp**

```
#include <iostream>
#include <gtest/gtest.h>


int add(int a, int b)
{
  return a + b;
}

int sub(int a, int b)
{
  return a - b;
}

// case1
TEST(test, c1)
{
  EXPECT_EQ(3, add(1, 2));
  EXPECT_EQ(12, add(2, 6));
}

// case2
TEST(test, c2)
{
  EXPECT_EQ(-1, sub(1, 2));
}

GTEST_API_ int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
```
**CMakeLists.txt**

```
cmake_minimum_required(VERSION 3.0)
set(CMAKE_CXX_STANDARD 11)


project(demo)

find_package(GTest REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} ${GTEST_LIBRARIES})
```
编译运行

```
mkdir build
cd build
cmake ..
make
./demo
```
![](../../../../_remote_images/08-周洁学习记录/local_assets/ZA1qL-2RVgPk8y/image_001.bin "")
## 4、使用详情
### 4.1 断言
 gtest中，断言的宏可以理解为分为两类，一类是ASSERT系列，一类是EXPECT系列。一个直观的解释就是：

* ASSERT_* 系列的断言，当检查点失败时，退出当前函数（注意：并非退出当前案例）。 
* EXPECT_* 系列的断言，当检查点失败时，继续往下执行。

####  <<操作符
如示例中的：

```
EXPECT_EQ(12, add(2, 6));
```
输出：

![](../../../../_remote_images/08-周洁学习记录/local_assets/ZA1qL-2RVgPk8y/image_002.bin "")
使用<<操作符自定义输出。就可以定位到在 i 时出现了错误，这样的输出结果看起来容易理解：

```
for (int i = 0; i < x.size(); ++i)
{
    EXPECT_EQ(x[i], y[i]) << "Vectors x and y differ at index " << i;
}
```
#### **布尔值检查**
|**Fatal assertion**|**Nonfatal assertion**|**Verifies**|
|-|-|-|
|ASSERT_TRUE(*condition*); |EXPECT_TRUE(*condition*); |*condition* is true |
|ASSERT_FALSE(*condition*); |EXPECT_FALSE(*condition*); |*condition* is false|

#### 数值型数据检查
|**Fatal assertion**|**Nonfatal assertion**|**Verifies**|
|-|-|-|
|ASSERT_EQ(*expected*, *actual*);|EXPECT_EQ(*expected*, *actual*);|*expected* == *actual*|
|ASSERT_NE(*val1*, *val2*);|EXPECT_NE(*val1*, *val2*);|*val1* != *val2*|
|ASSERT_LT(*val1*, *val2*);|EXPECT_LT(*val1*, *val2*);|*val1* < *val2*|
|ASSERT_LE(*val1*, *val2*);|EXPECT_LE(*val1*, *val2*);|*val1* <= *val2*|
|ASSERT_GT(*val1*, *val2*);|EXPECT_GT(*val1*, *val2*);|*val1* > *val2*|
|ASSERT_GE(*val1*, *val2*);|EXPECT_GE(*val1*, *val2*);|*val1* >= *val2*|

#### 字符串检查
|**Fatal assertion**|**Nonfatal assertion**|**Verifies**|
|-|-|-|
|ASSERT_STREQ(*expected_str*, *actual_str*);|EXPECT_STREQ(*expected_str*, *actual_str*);|the two C strings have the same content |
|ASSERT_STRNE(*str1*, *str2*);|EXPECT_STRNE(*str1*, *str2*);|the two C strings have different content |
|ASSERT_STRCASEEQ(*expected_str*, *actual_str*);|EXPECT_STRCASEEQ(*expected_str*, *actual_str*);|the two C strings have the same content, ignoring case |
|ASSERT_STRCASENE(*str1*, *str2*);|EXPECT_STRCASENE(*str1*, *str2*);|the two C strings have different content, ignoring case|

注意：*STREQ和*STRNE同时支持char*和wchar_t*类型的，*STRCASEEQ和*STRCASENE却只接收char*

```
TEST(StringCmpTest, Demo)
{
    char* pszCoderZh = "CoderZh";
    wchar_t* wszCoderZh = L"CoderZh";
    std::string strCoderZh = "CoderZh";
    std::wstring wstrCoderZh = L"CoderZh";

    EXPECT_STREQ("CoderZh", pszCoderZh);
    EXPECT_STREQ(L"CoderZh", wszCoderZh);

    EXPECT_STRNE("CnBlogs", pszCoderZh);
    EXPECT_STRNE(L"CnBlogs", wszCoderZh);

    EXPECT_STRCASEEQ("coderzh", pszCoderZh);
    //EXPECT_STRCASEEQ(L"coderzh", wszCoderZh);    不支持

    EXPECT_STREQ("CoderZh", strCoderZh.c_str());
    EXPECT_STREQ(L"CoderZh", wstrCoderZh.c_str());
}
```
#### 异常检查
|**Fatal assertion**|**Nonfatal assertion**|**Verifies**|
|-|-|-|
|ASSERT_THROW(*statement*, *exception_type*);|EXPECT_THROW(*statement*, *exception_type*);|*statement* throws an exception of the given type |
|ASSERT_ANY_THROW(*statement*);|EXPECT_ANY_THROW(*statement*);|*statement* throws an exception of any type |
|ASSERT_NO_THROW(*statement*);|EXPECT_NO_THROW(*statement*);|*statement* doesn't throw any exception|

```
int Foo(int a, int b)
{
    if (a == 0 || b == 0)
    {
        throw "don't do that";
    }
    int c = a % b;
    if (c == 0)
        return b;
    return Foo(b, c);
}

TEST(FooTest, HandleZeroInput)
{
    EXPECT_ANY_THROW(Foo(10, 0));
    EXPECT_THROW(Foo(0, 5), char*);
}
```
#### 浮点型检查
|**Fatal assertion**|**Nonfatal assertion**|**Verifies**|
|-|-|-|
|ASSERT_FLOAT_EQ(*expected, actual*);|EXPECT_FLOAT_EQ(*expected, actual*);|the two float values are almost equal |
|ASSERT_DOUBLE_EQ(*expected, actual*);|EXPECT_DOUBLE_EQ(*expected, actual*);|the two double values are almost equal|

对相近的两个数比较：

|**Fatal assertion**|**Nonfatal assertion**|**Verifies**|
|-|-|-|
|ASSERT_NEAR(*val1, val2, abs_error*);|EXPECT_NEAR*(val1, val2, abs_error*);|the difference between *val1* and *val2* doesn't exceed the given absolute error|

同时，还可以使用：

```
EXPECT_PRED_FORMAT2(testing::FloatLE, val1, val2);
EXPECT_PRED_FORMAT2(testing::DoubleLE, val1, val2);
```
### 4.2 事件机制
gtest提供了多种事件机制，非常方便在案例之前或之后做一些操作。gtest的事件一共有3种：

* 全局的，所有案例执行前后。
* TestSuite级别的，在某一批案例中第一个案例前，最后一个案例执行后。
* TestCase级别的，每个TestCase前后。

#### 全局事件
要实现全局事件，必须写一个类，继承testing::Environment类，实现里面的SetUp和TearDown方法。

1. SetUp()方法在所有案例执行前执行
2. TearDown()方法在所有案例执行后执行

```
class FooEnvironment : public testing::Environment
{
public:
    virtual void SetUp()
    {
        std::cout << "Foo FooEnvironment SetUP" << std::endl;
    }
    virtual void TearDown()
    {
        std::cout << "Foo FooEnvironment TearDown" << std::endl;
    }
};
```
还需要告诉gtest添加这个全局事件，在main函数中通过testing::AddGlobalTestEnvironment方法将事件挂进来。

```
int main(int argc, char **argv)
{
    testing::AddGlobalTestEnvironment(new FooEnvironment);
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```
#### TestSuite事件
需要写一个类，继承testing::Test，然后实现两个静态方法

1. SetUpTestCase() 方法在第一个TestCase之前执行
2. TearDownTestCase() 方法在最后一个TestCase之后执行

```
class TestAge : public testing::Test
{
public:
    static void SetUpTestCase()
    {
        cout << "SetUpTestCase()" << endl;
    }

    static void TearDownTestCase()
    {
        cout << "TearDownTestCase()" << endl;
    }
};
```
在编写测试案例时，需要使用TEST_F这个宏，第一个参数必须是上面类的名字，代表一个TestSuite。

```
TEST_F(TestAge, Test1)
{
    cout << "***********175159144**********" << endl;
}
```
#### TestCase事件
TestCase事件是挂在每个案例执行前后的，实现方式和上面的几乎一样，不过需要实现的是SetUp方法和TearDown方法：

1. SetUp()方法在每个TestCase之前执行
2. TearDown()方法在每个TestCase之后执行

```
TEST_F(TestMap, Test1)
{
    s->print();
}


TEST_F(TestMap, Test2)
{
    s->print();
}

TEST_F(TestAge, Test1)
{
    cout << "***********175159144**********" << endl;
}
```
通过继承Test类，使用TEST_F宏，可以在案例之间共享一些通用方法，共享资源。使得我们的案例更加的简洁，清晰。

#### 样例代码
完整代码：

```
#include <gtest/gtest.h>
#include <map>
#include <iostream>
using namespace std;


class Student
{
public:
    Student()
    {
        age = 0;
    }
    Student(int a)
    {
        age = a;
    }
    void print()
    {
        cout << "*********** " << age << " **********" << endl;
    }

private:
    int age;
};

class FooEnvironment : public testing::Environment
{
public:
    virtual void SetUp()
    {
        std::cout << "Foo FooEnvironment SetUP" << std::endl;
    }
    virtual void TearDown()
    {
        std::cout << "Foo FooEnvironment TearDown" << std::endl;
    }
};

static Student *s;
//在第一个test之前，最后一个test之后调用SetUpTestCase()和TearDownTestCase()
class TestMap : public testing::Test
{
public:
    static void SetUpTestCase()
    {
        cout << "SetUpTestCase()" << endl;
        s = new Student(23);
    }

    static void TearDownTestCase()
    {
        delete s;
        cout << "TearDownTestCase()" << endl;
    }
    void SetUp()
    {
        cout << "SetUp() is running" << endl;
    }
    void TearDown()
    {
        cout << "TearDown()" << endl;
    }
};

class TestAge : public testing::Test
{
public:
    static void SetUpTestCase()
    {
        cout << "SetUpTestCase()" << endl;
    }

    static void TearDownTestCase()
    {
        cout << "TearDownTestCase()" << endl;
    }
};

TEST_F(TestMap, Test1)
{
    s->print();
}

TEST_F(TestMap, Test2)
{
    s->print();
}

TEST_F(TestAge, Test1)
{
    cout << "***********175159144**********" << endl;
}

int main(int argc, char **argv)
{
    testing::AddGlobalTestEnvironment(new FooEnvironment);
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```
运行：

![](../../../../_remote_images/08-周洁学习记录/local_assets/ZA1qL-2RVgPk8y/image_003.bin "")
### 4.3 参数化 
在设计测试案例时，经常需要考虑给被测函数传入不同的值的情况。如：

```
TEST(IsPrimeTest, HandleTrueReturn)
{
    EXPECT_TRUE(IsPrime(3));
    EXPECT_TRUE(IsPrime(5));
    EXPECT_TRUE(IsPrime(11));
    EXPECT_TRUE(IsPrime(23));
    EXPECT_TRUE(IsPrime(17));
}
```
上面的写法产生的是1个测试案例，里面有5个检查点，假如要把5个检查变成5个单独的案例，将会更加累人。

#### 使用参数化后的方案
1. 确定参数类型

添加一个类，继承testing::TestWithParam<T>，其中T就是你需要参数化的参数类型，比如上面的例子，需要参数化一个int型的参数

```
class IsPrimeParamTest : public::testing::TestWithParam<int>
{

};
```
2. 确定具体做些什么样的测试

这里，我们要使用一个新的宏（嗯，挺兴奋的）：TEST_P，关于这个"P"的含义，Google给出的答案非常幽默，就是说你可以理解为”parameterized" 或者 "pattern"。我更倾向于 ”parameterized"的解释，呵呵。在TEST_P宏里，使用GetParam()获取当前的参数的具体值。

```
TEST_P(IsPrimeParamTest, HandleTrueReturn)
{
    int n =  GetParam();
    EXPECT_TRUE(IsPrime(n));
}
```
3. 测试的参数范围

使用INSTANTIATE_TEST_CASE_P宏来告诉gtest要测试的参数范围：

```
INSTANTIATE_TEST_CASE_P(TrueReturn, IsPrimeParamTest, testing::Values(3, 5, 11, 23, 17));
```
第一个参数是测试案例的前缀，可以任意取。

第二个参数是测试案例的名称，需要和之前定义的参数化的类的名称相同，如：IsPrimeParamTest

第三个参数是可以理解为参数生成器，上面的例子使用test::Values表示使用括号内的参数。Google提供了一系列的参数生成的函数：

|ge(begin, end[, step])|范围在begin~end之间，步长为step，不包括end|
|-|-|
|Values(v1, v2, ..., vN)|v1,v2到vN的值|
|ValuesIn(container) and ValuesIn(begin, end)|从一个C类型的数组或是STL容器，或是迭代器中取值|
|Bool()|取false 和 true 两个值|
|Combine(g1, g2, ..., gN)|这个比较强悍，它将g1,g2,...gN进行排列组合，g1,g2,...gN本身是一个参数生成器，每次分别从g1,g2,..gN中各取出一个值，组合成一个元组(Tuple)作为一个参数。说明：这个功能只在提供了<tr1/tuple>头的系统中有效。gtest会自动去判断是否支持tr/tuple，如果你的系统确实支持，而gtest判断错误的话，你可以重新定义宏GTEST_HAS_TR1_TUPLE=1。|

#### 样例代码
完整代码：

```
#include<gtest/gtest.h>


bool IsPrime(int n)
{
    if (n <= 1) return false;
    if (n % 2 == 0) return n == 2;
    for (int i = 3; ; i += 2) {
        if (i > n/i) break;
        if (n % i == 0) return false;
    }
    return true;
}

class IsPrimeParamTest : public::testing::TestWithParam<int>{};

TEST_P(IsPrimeParamTest, HandleTrueReturn)
{
 int n =  GetParam();
 EXPECT_TRUE(IsPrime(n));
}

//被测函数须传入多个相关的值
INSTANTIATE_TEST_CASE_P(TrueReturn, IsPrimeParamTest, testing::Values(3, 5, 11, 23, 17));

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```
运行结果：

![](../../../../_remote_images/08-周洁学习记录/local_assets/ZA1qL-2RVgPk8y/image_004.bin "")
## 5、实际应用
```
#include <gtest/gtest.h>
#include <map>
#include <iostream>
#include "../include/read_file_line_by_line.h"
#include "../include/parse.h"


using namespace std;
using namespace parse;

class GCTestEnvironment : public testing::Environment
{
public:
    virtual void SetUp()
    {
        std::cout << "cpp_good_coder_test GCTestEnvironment SetUP" << std::endl;
    }
    virtual void TearDown()
    {
        std::cout << "cpp_good_coder_test GCTestEnvironment TearDown" << std::endl;
    }
};

class TestReadFileLineByLine : public testing::Test
{
public:
    static void SetUpTestCase()
    {
        cout << "SetUpTestCase ReadFileLineByLine()" << endl;
    }

    static void TearDownTestCase()
    {
        cout << "TearDownTestCase ReadFileLineByLine()" << endl;
    }

    ReadFileLineByLine file_reader;
};

class TestParser : public testing::Test
{
public:
    static void SetUpTestCase()
    {
        cout << "SetUpTestCase()" << endl;
    }

    static void TearDownTestCase()
    {
        cout << "TearDownTestCase()" << endl;
    }

    Parser parser;
};

TEST_F(TestReadFileLineByLine, Test1)
{
    string file_name = "../data/data.txt";
    EXPECT_TRUE(file_reader.open_file(file_name)); 
}

TEST_F(TestReadFileLineByLine, Test2)
{
    string line1 = "test1\t123\t2.4\n";
    string res = file_reader.get_index_line(1);
    EXPECT_STREQ(line1.c_str(), res.c_str());
}

TEST_F(TestReadFileLineByLine, Test3)
{
    string line5 = "test5\t123\t2.4\tzhoujie 26 153.8\t11 22 33\n";
    string res = file_reader.get_index_line(5);
    EXPECT_STREQ(line5.c_str(), res.c_str());
}

TEST_F(TestParser, Test1)
{
    string line1 = "test1\t123\t2.4\n";
    parser.parse_line(line1);
    int y = 0;
    parser.get_column(1, &y);
    EXPECT_EQ(123, y);
}

TEST_F(TestParser, Test2)
{
    string line1 = "test1\t123\t2.4\n";
    parser.parse_line(line1);
    float z = 0;
    parser.get_column(2, &z);
    EXPECT_FLOAT_EQ(2.4, z);
}


int main(int argc, char **argv)
{
    testing::AddGlobalTestEnvironment(new GCTestEnvironment);
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```
![](../../../../_remote_images/08-周洁学习记录/local_assets/ZA1qL-2RVgPk8y/image_005.bin "")
## 参考
可以参考的系列目录：

[1.玩转Google开源C++单元测试框架Google Test系列(gtest)之一 - 初识gtest](http://www.cnblogs.com/coderzh/archive/2009/03/31/1426758.html)

[2.玩转Google开源C++单元测试框架Google Test系列(gtest)之二 - 断言](http://www.cnblogs.com/coderzh/archive/2009/04/06/1430364.html)

[3.玩转Google开源C++单元测试框架Google Test系列(gtest)之三 - 事件机制](http://www.cnblogs.com/coderzh/archive/2009/04/06/1430396.html)

[4.玩转Google开源C++单元测试框架Google Test系列(gtest)之四 - 参数化](http://www.cnblogs.com/coderzh/archive/2009/04/08/1431297.html)

[5.玩转Google开源C++单元测试框架Google Test系列(gtest)之五 - 死亡测试](http://www.cnblogs.com/coderzh/archive/2009/04/08/1432043.html) 

[6.玩转Google开源C++单元测试框架Google Test系列(gtest)之六 - 运行参数](http://www.cnblogs.com/coderzh/archive/2009/04/10/1432789.html)

[7.玩转Google开源C++单元测试框架Google Test系列(gtest)之七 - 深入解析gtest](http://www.cnblogs.com/coderzh/archive/2009/04/11/1433744.html)

[8.玩转Google开源C++单元测试框架Google Test系列(gtest)之八 - 打造自己的单元测试框架](http://www.cnblogs.com/coderzh/archive/2009/04/12/1434155.html)

其他参考链接：

[GTest的安装与使用](https://www.cnblogs.com/helloworldcode/p/9606838.html)

[编写优美的GTest测试案例](https://www.cnblogs.com/coderzh/archive/2010/01/09/beautiful-testcase.html)


