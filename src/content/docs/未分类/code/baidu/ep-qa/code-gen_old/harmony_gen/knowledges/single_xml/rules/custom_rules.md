---
title: "必须保留的Text组件基础属性定义&初始化"
description: "// 内部接口定义 interface testInterface { // ... }"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\harmony_gen\\knowledges\\single_xml\\rules\\custom_rules.md"
---
### 命名规范
1. 类名、接口名、类型别名使用大驼峰；函数名及函数的参数、全局变量和局部变量都使用小驼峰；
2. 静态常量需使用全大写，单词间用下划线隔开；文件目录名全用小写，单词间用下划线隔开。
### 语法规范
1. 变量定义或方法中的参数均需要类型声明，且定义的变量必须初始化；
2. 所有字符串类型变量均声明成`ResourceStr`类型；
3. 所有未识别类型的变量均通过`undefined`进行声明，示例：`testUnknown : undefined | null`;
4. 转换生成的代码中，自定义的方法和类及其使用语句等内容都以注释的形式呈现
5. ArkTS语言不支持内部类、接口等的定义，需提取输入自定义组件中的内部类、接口等，然后定义为独立的类、接口等，并在需要的地方进行实例化，示例如下：
* 包含内部类、接口的自定义组件输入示例：
```kotlin
public class testComponent extends ImageView {
    //...
    
    // 内部接口定义
    interface testInterface {
        // ...
    } 
    
    // 内部类定义
    private static final class TestInnerClass implements testInterface {
        // ...
    }
    
    //...
}
```
* 包含内部类、接口的自定义组件转换成ArkTS语言的输出示例：
```typescript
/*
* 自定义testComponent
* 组件继承至ImageView
 */


@Component
export struct TestComponent {
  // ...
  
  // 接口实例化示例：
  @State testInterface: TestInterface | null = null;
  
  // 类实例化示例：
  @Private testInnerClass: TestInnerClass = new TestInnerClass();
  
  build() {
    Image()
    //...
  }

  // ...
}

// 内部接口独立定义，示例如下：
// interface TestInterface {
    // // ...
// }

// 内部类独立定义，示例如下：
// class TestInnerClass implements TestInterface {
    // //...
// }
```
6. ArkTS语言自定义组件内不支持同名方法的定义，需找到输入自定义组件中的同名方法，在转换时添加数字后缀以示区分，示例如下：
* 包含同名方法的自定义组件输入示例：
```java
public class testComponent extends ImageView {
    // ...
    
    // 以下是自定义组件内的两个同名函数
    // public testComponent testFunc(@Nullable String testParam) {
    //    return this;
    //}
    
    // public testComponent testFunc(@Nullable String testParam1, Object testParam2) {
    //     return this;
    // }
    
    // ...
}
```
* 包含同名方法的自定义组件转换成ArkTS语言的输出示例：
```typescript
/*
* 自定义testComponent
* 组件继承至ImageView
 */
@Component
export struct TestComponent {
  // ...

  build() {
    Image()
    // ...
  }

  // 转换后的同名函数，添加数字后缀1，testFunc1：
  testFunc1(testParam: ResourceStr | null): TestComponent {
    return this;
  }
  // 转换后的同名函数，添加数字后缀2，testFunc2：
  testFunc2(testParam1: ResourceStr | null, testParam2: undefined | null): TestComponent {
    return this;
  }

  // ...
}
```
7. 请从组件引用路径和属性设置深入解析组件功能并定位至对应的默认组件，在自定义组件中实现默认组件的基础属性声明和初始化，在`build`方法中实现默认组件基础参数设置，常用默认组件转换示例：
#### Text组件
```typescript
@Component
export struct TestText {
    // 常量定义
    // ...
    
    # 必须保留的Text组件基础属性定义&初始化
    @Prop text: ResourceStr = 'Hello, Test Text!';
    @Prop fontColor: ResourceColor = '#000000';
    @Prop fontSize: number | string | Resource = 14;
    @State textOverflow: TextOverflow = TextOverflow.Ellipsis;
    @State maxLines: number = 1;
    
    // 自定义组件其他自定义属性定义&初始化
    // ...
    
    build() {
        // 在build方法中实现基础组件的功能
        Text(this.text)
          .fontColor(this.fontColor)
          .fontSize(this.fontSize)
          .maxLines(this.maxLines)
          .textOverflow({overflow: this.textOverflow})
    }
    
    // 自定义组件的自定义方法的实现
    // ...
}

// 解释：若存在内部类、接口等，则需将内部类单独定义，并在需要的地方进行实例化
```
#### TextInput组件
```typescript
@Component
export struct TestTextInput {
  // 常量定义
  // ...
    
  // 必须保留的TextInput组件基础属性定义&初始化
  @Prop text: ResourceStr = '请输入文本';
  @Prop fontColor: ResourceColor = '#000000';
  @Prop fontSize: number | string | Resource = 14;
  @State textOverflow: TextOverflow = TextOverflow.Ellipsis;
  @State maxLines: number = 1;
  @State textAlign: TextAlign = TextAlign.Start;
  @State imeOptions: EnterKeyType = EnterKeyType.Go;

  // 自定义组件其他自定义属性定义&初始化
  // ...

  build() {
    // 在build方法中实现基础组件的功能
    TextInput({placeholder: this.text})
      .fontColor(this.fontColor)
      .fontSize(this.fontSize)
      .textOverflow(this.textOverflow)
      .maxLines(this.maxLines)
      .textAlign(this.textAlign)
      .enterKeyType(this.imeOptions)
  }

  // 自定义组件的自定义方法的实现
  // ...
}

// 解释：若存在内部类、接口等，则需将内部类单独定义，并在需要的地方进行实例化
```
#### Image组件
```typescript
@Component
export struct TestImage {
  // 常量定义
  // ...
    
  // 必须保留的Image组件基础属性设置
  @State objectFit: ImageFit = ImageFit.Auto;
  // 解释：若存在资源图的加载，则需要定义加载占位图相关属性
  @State src: ResourceStr = "https://example.com/image.jpg";

  // 自定义组件其他自定义属性定义&初始化，示例：
  @State placeholder: ResourceStr = '';
  @State isImageLoaded: boolean = false;
  // ...

  build() {
    Column() {
      // 解释：若存在加载占位图的自定义功能，实现示例：
      // if (!this.isImageLoaded) {
      //  Image(this.placeholder)
      //    .objectFit(this.objectFit)
      //}
      // 基础组件功能，加载src资源图
      Image(this.src)
        .objectFit(this.objectFit)
        // 控制占位图的显示的自定义功能，实现示例
        // .onAppear(() => {
        //  this.isImageLoaded = true;
        // })
        // .onDisAppear(() => {
        //  this.isImageLoaded = false;
        //})
      }
      .height('auto')
      .width('auto')
  }


  // 自定义组件的自定义方法的实现
  // ...
}

// 解释：若存在内部类、接口等，则需将内部类单独定义，并在需要的地方进行实例化
```
