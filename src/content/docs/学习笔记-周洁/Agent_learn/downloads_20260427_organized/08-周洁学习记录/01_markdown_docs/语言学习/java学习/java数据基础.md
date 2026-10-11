---
title: "java数据基础"
description: "java数据基础"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\语言学习\\java学习\\java数据基础.md"
---
java数据基础

本页面由v_姚宇辰于2022/03/02迁移自wiki 周洁空间
### 
### Java 的两大数据类型
* 内置数据类型
* 引用数据类型

**内置数据类型**

Java语言提供了八种基本类型。六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

|**数据类型**|**默认值**|
|-|-|
|byte|0|
|short|0|
|int|0|
|long|0L|
|float|0.0f|
|double|0.0d|
|char|'u0000'|
|String (or any object)|null|
|boolean|false|

**引用类型**

* 在Java中，引用类型的变量非常类似于C/C++的指针。引用类型指向一个对象，指向对象的变量是引用变量。这些变量在声明时被指定为一个特定的类型，比如 Employee、Puppy 等。变量一旦声明后，类型就不能被改变了。
* 对象、数组都是引用数据类型。
* 所有引用类型的默认值都是null。
* 一个引用变量可以用来引用任何与之兼容的类型。
* 例子：Site site = new Site("Runoob")。

### 常量
在 Java 中使用 final 关键字来修饰常量，声明方式和变量类似：

final double PI = 3.1415927;

byte、int、long、和short都可以用十进制、16进制以及8进制的方式来表示。

当使用字面量的时候，前缀 0 表示 8 进制，而前缀 0x 代表 16 进制, 例如：

int decimal = 100; int octal = 0144; int hexa = 0x64;

字符串常量和字符常量都可以包含任何Unicode字符。例如：

char a = '\u0001'; String a = "\u0001";

### 自动类型转换
整型、实型（常量）、字符型数据可以混合运算。运算中，不同类型的数据先转化为同一类型，然后进行运算。

转换从低级到高级。

低 ------------------------------------> 高 byte,short,char—> int —> long—> float —> double

数据类型转换必须满足如下规则：

1. 不能对boolean类型进行类型转换。

2. 不能把对象类型转换成不相关类的对象。

3. 在把容量大的类型转换为容量小的类型时必须使用强制类型转换。

4. 转换过程中可能导致溢出或损失精度，例如：

int i =128; byte b = (byte)i;

因为 byte 类型是 8 位，最大值为127，所以当 int 强制转换为 byte 类型时，值 128 时候就会导致溢出。

5. 浮点数到整数的转换是通过舍弃小数得到，而不是四舍五入，例如： 

(int)23.7 == 23;         (int)-45.89f == -45

### 变量类型
Java语言支持的变量类型有：

* 类变量：独立于方法之外的变量，用 static 修饰。
* 实例变量：独立于方法之外的变量，不过没有 static 修饰。 
* 局部变量：类的方法中的变量。

**局部变量**

* 局部变量声明在方法、构造方法或者语句块中；
* 局部变量在方法、构造方法、或者语句块被执行的时候创建，当它们执行完成后，变量将会被销毁；
* 访问修饰符不能用于局部变量；
* 局部变量只在声明它的方法、构造方法或者语句块中可见；
* 局部变量是在栈上分配的。
* 局部变量没有默认值，所以局部变量被声明后，必须经过初始化，才可以使用。

**实例变量**

* 实例变量声明在一个类中，但在方法、构造方法和语句块之外；
* 当一个对象被实例化之后，每个实例变量的值就跟着确定；
* 实例变量在对象创建的时候创建，在对象被销毁的时候销毁；
* 实例变量的值应该至少被一个方法、构造方法或者语句块引用，使得外部能够通过这些方式获取实例变量信息；
* 实例变量可以声明在使用前或者使用后；
* 访问修饰符可以修饰实例变量；
* 实例变量对于类中的方法、构造方法或者语句块是可见的。一般情况下应该把实例变量设为私有。通过使用访问修饰符可以使实例变量对子类可见；
* 实例变量具有默认值。数值型变量的默认值是0，布尔型变量的默认值是false，引用类型变量的默认值是null。变量的值可以在声明时指定，也可以在构造方法中指定；
* 实例变量可以直接通过变量名访问。但在静态方法以及其他类中，就应该使用完全限定名：ObejectReference.VariableName。

**类变量（静态变量）**

* 类变量也称为静态变量，在类中以 static 关键字声明，但必须在方法之外。
* 无论一个类创建了多少个对象，类只拥有类变量的一份拷贝。
* 静态变量除了被声明为常量外很少使用，静态变量是指声明为 public/private，final 和 static 类型的变量。静态变量初始化后不可改变。
* 静态变量储存在静态存储区。经常被声明为常量，很少单独使用 static 声明变量。
* 静态变量在第一次被访问时创建，在程序结束时销毁。
* 与实例变量具有相似的可见性。但为了对类的使用者可见，大多数静态变量声明为 public 类型。
* 默认值和实例变量相似。数值型变量默认值是 0，布尔型默认值是 false，引用类型默认值是 null。变量的值可以在声明的时候指定，也可以在构造方法中指定。此外，静态变量还可以在静态语句块中初始化。
* 静态变量可以通过：ClassName.VariableName的方式访问。
* 类变量被声明为 public static final 类型时，类变量名称一般建议使用大写字母。如果静态变量不是 public 和 final 类型，其命名方式与实例变量以及局部变量的命名方式一致。

### 修饰符
Java语言提供了很多修饰符，主要分为以下两类：

* 访问修饰符
* 非访问修饰符

修饰符用来定义类、方法或者变量，通常放在语句的最前端。

**访问控制修饰符**

Java中，可以使用访问控制符来保护对类、变量、方法和构造方法的访问。Java 支持 4 种不同的访问权限。

* **default **(即默认，什么也不写）: 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法。
* **private **: 在同一类内可见。使用对象：变量、方法。 注意：不能修饰类（外部类）
* **public **: 对所有类可见。使用对象：类、接口、变量、方法
* **protected **: 对同一包内的类和所有子类可见。使用对象：变量、方法。 注意：不能修饰类（外部类）。

访问控制

|修饰符|当前类|同一包内|子孙类(同一包)|子孙类(不同包)|其他包|
|-|-|-|-|-|-|
|`public`|Y|Y|Y|Y|Y|
|`protected`|Y|Y|Y|Y/N（[说明](https://www.runoob.com/java/java-modifier-types.html#protected-desc)）|N|
|`default`|Y|Y|Y|N|N|
|`private`|Y|N|N|N|N|

**访问控制和继承**

请注意以下方法继承的规则：

* 父类中声明为 public 的方法在子类中也必须为 public。
* 父类中声明为 protected 的方法在子类中要么声明为 protected，要么声明为 public，不能声明为 private。
* 父类中声明为 private 的方法，不能够被继承。

**非访问修饰符**

为了实现一些其他的功能，Java 也提供了许多非访问修饰符。

static 修饰符，用来修饰类方法和类变量。

final 修饰符，用来修饰类、方法和变量，final 修饰的类不能够被继承，修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的。

abstract 修饰符，用来创建抽象类和抽象方法。

synchronized 和 volatile 修饰符，主要用于线程的编程。

### 类型判断 instanceof
```
String name = "James";
boolean result = name instanceof String; // 由于 name 是 String 类型，所以返回真
```
### 增强 for 循环
```
for(int x : numbers ){
  System.out.print( x );
  System.out.print(",");
}
```
### Number & Math 类方法
 Number & Math 类常用的一些方法：

|类|方法与描述|例子|
|-|-|-|
|Number|[xxxValue()](https://www.runoob.com/java/number-xxxvalue.html) 将 Number 对象转换为xxx数据类型的值并返回。|Integer x = 5; // 返回 byte 原生数据类型x.byteValue() ;|
||[compareTo()](https://www.runoob.com/java/number-compareto.html) 将number对象与参数比较。|x.compareTo(3)|
||[equals()](https://www.runoob.com/java/number-equals.html) 判断number对象是否与参数相等。||
||[valueOf()](https://www.runoob.com/java/number-valueof.html) 返回一个 Number 对象指定的内置数据类型|Float a = Float.valueOf("80");|
||[toString()](https://www.runoob.com/java/number-tostring.html) 以字符串形式返回值。|x.toString()；|
||[parseInt()](https://www.runoob.com/java/number-parseInt.html) 将字符串解析为int类型。|int b = Integer.parseInt("444",16);//16进制|
|Math|[abs()](https://www.runoob.com/java/number-abs.html) 返回参数的绝对值。|Math.abs(a)；|
||[ceil()](https://www.runoob.com/java/number-ceil.html) 返回大于等于( >= )给定参数的的最小整数，类型为双精度浮点型。|Math.ceil(d)；|
||[floor()](https://www.runoob.com/java/number-floor.html) 返回小于等于（<=）给定参数的最大整数 。||
||[rint()](https://www.runoob.com/java/number-rint.html) 返回与参数最接近的整数。返回类型为double。|Math.rint(d)；|
||[round()](https://www.runoob.com/java/number-round.html) 它表示**四舍五入**，算法为 Math.floor(x+0.5)，即将原来的数字加上 0.5 后再向下取整，所以，Math.round(11.5) 的结果为12，Math.round(-11.5) 的结果为-11。||
||[min()](https://www.runoob.com/java/number-min.html) 返回两个参数中的最小值。|Math.min(12.123, 12.456）;|
||[max()](https://www.runoob.com/java/number-max.html) 返回两个参数中的最大值。||
||[exp()](https://www.runoob.com/java/number-exp.html) 返回自然数底数e的参数次方。|Math.E;Math.exp(x);|
||[log()](https://www.runoob.com/java/number-log.html) 返回参数的自然数底数的对数值。||
||[pow()](https://www.runoob.com/java/number-pow.html) 返回第一个参数的第二个参数次方。|Math.pow(2, 3); // 8|
||[sqrt()](https://www.runoob.com/java/number-sqrt.html) 求参数的算术平方根。||
||[sin()](https://www.runoob.com/java/number-sin.html) 求指定double类型参数的正弦值。||
||[random()](https://www.runoob.com/java/number-random.html) 返回一个随机数。|Math.random(); // 0~1.0|

### Character 类方法
下面是Character类的方法：

|方法与描述|例子|
|-|-|
|[isLetter()](https://www.runoob.com/java/character-isletter.html) 是否是一个字母|Character.isLetter('c');|
|[isDigit()](https://www.runoob.com/java/character-isdigit.html) 是否是一个数字字符||
|[isWhitespace()](https://www.runoob.com/java/character-iswhitespace.html) 是否是一个空白字符|Character.isWhitespace('\t');|
|[isUpperCase()](https://www.runoob.com/java/character-isuppercase.html) 是否是大写字母||
|[isLowerCase()](https://www.runoob.com/java/character-islowercase.html) 是否是小写字母||
|[toUpperCase()](https://www.runoob.com/java/character-touppercase.html) 指定字母的大写形式||
|[toLowerCase](https://www.runoob.com/java/character-tolowercase.html)() 指定字母的小写形式||
|[toString](https://www.runoob.com/java/character-tostring.html)() 返回字符的字符串形式，字符串的长度仅为1||

### String 类方法
String 创建的字符串存储在公共池中，而 new 创建的字符串对象在堆上：

**注意:**String 类是不可改变的。如果需要对字符串做很多修改，那么应该选择使用 StringBuffer & StringBuilder 类。

下面是 String 类支持的方法:

|方法描述|例子|
|-|-|
|[char charAt(int index)](https://www.runoob.com/java/java-string-charat.html) 返回指定索引处的 char 值。|char result = s.charAt(1);|
|[int compareTo(String anotherString)](https://www.runoob.com/java/java-string-compareto.html) 按字典顺序比较两个字符串。|int result = str1.compareTo( str2 );|
|[int compareToIgnoreCase(String str)](https://www.runoob.com/java/java-string-comparetoignorecase.html) 按字典顺序比较两个字符串，不考虑大小写。||
|[String concat(String str)](https://www.runoob.com/java/java-string-concat.html) 将指定字符串连接到此字符串的结尾。|s = s.concat("hello");|
|[boolean contentEquals(StringBuffer sb)](https://www.runoob.com/java/java-string-contentequals.html) 当且仅当字符串与指定的StringBuffer有相同顺序的字符时候返回真。|boolean result = str1.contentEquals( str3 );|
|[static String copyValueOf(char[] data, int offset, int count)](https://www.runoob.com/java/java-string-copyvalueof.html) 返回指定数组中表示该字符序列的 String。|char[] Str1 = {'h', 'e', 'l', 'l', 'o', ' ', 'r', 'u', 'n', 'o', 'o', 'b'};String Str2 = Str2.copyValueOf( Str1, 2, 6 ); // llo ru|
|[boolean endsWith(String suffix)](https://www.runoob.com/java/java-string-endswith.html) 测试此字符串是否以指定的后缀结束。|boolean retVal = Str.endsWith( "lo" );|
|[boolean equals(Object anObject)](https://www.runoob.com/java/java-string-equals.html) 将此字符串与指定的对象比较。||
|[byte[] getBytes(String charsetName)](https://www.runoob.com/java/java-string-getbytes.html) 使用指定的字符集将此 String 编码为 byte 序列，并将结果存储到一个新的 byte 数组中。|byte[] Str2 = Str1.getBytes( "UTF-8" );|
|[void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)](https://www.runoob.com/java/java-string-getchars.html) 将字符从此字符串复制到目标字符数组。|String Str1 = new String("www.runoob.com");char[] Str2 = new char[6];Str1.getChars(4, 10, Str2, 0); // runoob|
|[int indexOf(int ch, int fromIndex)](https://www.runoob.com/java/java-string-indexof.html) 返回在此字符串中第一次出现指定字符处的索引，从指定的索引开始搜索。|str.indexOf('a',3);|
|[int indexOf(String str, int fromIndex)](https://www.runoob.com/java/java-string-indexof.html) 返回指定子字符串在此字符串中第一次出现处的索引，从指定的索引开始。|str.indexOf('ab',3);|
|[int length()](https://www.runoob.com/java/java-string-length.html) 返回此字符串的长度。|str1.length();|
|[boolean matches(String regex)](https://www.runoob.com/java/java-string-matches.html) 告知此字符串是否匹配给定的正则表达式。||
|[String replace(char oldChar, char newChar)](https://www.runoob.com/java/java-string-replace.html) 返回一个新的字符串，它是通过用 newChar 替换此字符串中出现的所有 oldChar 得到的。|str.replace('o', 'T');|
|[char[] toCharArray()](https://www.runoob.com/java/java-string-tochararray.html) 将此字符串转换为一个新的字符数组。|str.toCharArray();|
|[contains(CharSequence chars)](https://www.runoob.com/java/java-string-contains.html) 判断是否包含指定的字符系列。|Str.contains("Run");|
|[isEmpty()](https://www.runoob.com/java/java-string-isempty.html) 判断字符串是否为空。||

### StringBuffer 类方法
StringBuffer sBuffer = new StringBuffer("hell0：");

sBuffer.append("world");

|方法描述|
|-|
|public StringBuffer append(String s) 将指定的字符串追加到此字符序列。|
|public StringBuffer reverse()  将此字符序列用其反转形式取代。|
|public delete(int start, int end) 移除此序列的子字符串中的字符。|
|public insert(int offset, int i) 将 `int` 参数的字符串表示形式插入此序列中。|
|replace(int start, int end, String str) 使用给定 `String` 中的字符替换此序列的子字符串中的字符。|


