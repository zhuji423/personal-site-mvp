---
title: "当前示例仅用于框架转换的参考，不代表全部内容"
description: "build { // ViewStub组件转换示例如下： if this.isShow { Text'testViewStub' // ... } } } 9. xml中的<View/组件对应ArkUI中的Divider组件 Column布"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\harmony_gen\\knowledges\\single_xml\\rules\\layout_rules.md"
---
### 常用布局转换规则
#### 通用规范
1. 注意：引用路径中带`.baidu`关键词的组件需要先导入然后生成对应的使用代码，其他组件一律转换成对应直接使用的默认组件即可，无法识别的属性设置生成对应FIXME注释
2. 宽度/高度设置为`wrap_content`的属性转换为`auto`，组件类该属性一律不转换
3. 布局和组件最大/最小宽度等为通用属性，设置均通过`.constraintSize({})`实现，示例：`android:minWidth="0px"`->`.constraintSize({minWidth: '0vp'})`
4. 字体相关属性通过`.fontXXX()`来实现，示例：`android:textColor="#000000"`->`.fontColor('#000000')`
5. 通用边缘间距属性通过`.margin({方向: 'xxvp'})`来实现，特别注意左边距必须是设置`left`，右边距必须是设置`right`，示例：`android:layout_marginStart="1dp"`->`.margin({left: '1vp'})`
6. 注意仔细分析原始行/列布局逻辑和组件对齐逻辑，灵活运用RelativeContainer、Row/Column、Stack等布局，保证转换后的ArkUI布局行、列位置关系和原始xml保持一致
7. 布局必须包含子组件，子组件需存放在布局`{}`内，布局属性设置必须在其`{}`最后进行，注意遵守ArkUI开发规范，示例如下：
```typescript
RelativeContainer() {
    // 子组件位置，存放在{}内部
}
// 布局属性设置位置，放在{}最后
.width('100%')
// ...
```
8. xml中的`<ViewStub/>`组件无对应默认组件，需按照如下示例进行转换：
```typescript
@Entry
@Component
struct TestViewStub {
    // ViewStub需要通过参数确定是否显示
    @State isShow: boolean = false
    
    build() {
        // ViewStub组件转换示例如下：
        if (this.isShow) {
            Text('testViewStub')
                // ...
        }
    }
}
```
9. xml中的`<View/>`组件对应ArkUI中的`Divider`组件
#### Column布局
1. Column布局主轴方向为垂直方向，垂直对齐通过`.justifyContent(FlexAlign.XXX)`进行转换，可选参数：Start（默认值）、Center、End、SpaceEvenly、SpaceAround、SpaceBetween
2. Column布局交叉轴方向为水平方向，水平对齐通过`.alignItems(HorizontalAlign.XXX)`进行转换，可选参数：Start（默认值）、Center、End
#### Row布局
1. Row布局主轴方向为水平方向，水平对齐通过`.justifyContent(FlexAlign.XXX)`进行转换，可选参数：Start（默认值）、Center、End、SpaceEvenly、SpaceAround、SpaceBetween
2. Row布局交叉轴方向为垂直方向，垂直对齐通过`.alignItems(VerticalAlign.XXX)`进行转换，可选参数：Top（默认值）、Center、Bottom
#### Stack布局
1. Stack布局对齐通过`Stack({alignContent: Alignment.XXX})`的设置实现，可选参数：TopStart、Top、TopEnd、Start（默认值）、Center、End、BottomStart、Bottom、BottomEnd
2. xml中的`</androidx.constraintlayout.widget.ConstraintLayout>`布局必须转换成`Stack`布局
#### RelativeContainer布局
* 注意：生成的页面不包含`RelativeContainer`布局时，不要通过`.alignRules()`设置对齐，会导致失效
##### 只有`RelativeContainer`布局中的组件可以基于锚点通过`.alignRules()`设置对齐方式，但不同组件不能互为锚点，设置规则如下： 
1. 组件位置水平左（left）、水平中点（middle）、水平右（right），可对齐锚点水平方向左（HorizontalAlign.Start）、水平中（HorizontalAlign.Center）、水平右（HorizontalAlign.End）
2. 组件位置垂直上（top）、垂直中点（center）、垂直下（bottom），可对齐锚点垂直方向上（VerticalAlign.Top）、垂直中（VerticalAlign.Center）、垂直下（VerticalAlign.Bottom）
##### 采用`alignRules`方式实现对齐时，注意严格按照以下要求转换:
* 水平中点对齐必须通过`middle`->`HorizontalAlign.XXX`进行设置，参考示例为：`.alignRules({{middle: {{anchor: '锚点容器ID', align: HorizontalAlign.XXX}}}})`
* 对齐设置必须遵守格式：`.alignRules({{xxx: {{anchor: '锚点容器ID', align: HorizontalAlign.XXX（水平对齐）/VerticalAlign.XXX（垂直对齐）}}}})`
* 垂直中点对齐必须通过`center`->`VerticalAlign.XXX`进行设置，参考示例为：`.alignRules({{center: {{anchor: '锚点容器ID', align: VerticalAlign.XXX}}}})`
##### 注意：当前示例仅用于`RelativeContainer`布局框架转换的参考，若真实原始xml中有其他组件属性的设置，请注意参考输入xml完成完整的一对一转换
* xml布局框架示例：
```test_frame.xml
# 当前示例仅用于框架转换的参考，不代表全部内容
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <RelativeLayout
        android:id="@+id/test_frame"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:paddingLeft="15dp"
        android:paddingRight="15dp">

        <ImageView
            android:id="@+id/test_image"
            android:layout_width="74dp"
            android:layout_height="110dp"
            android:layout_alignParentLeft="true"
            android:layout_alignParentStart="true" 
            android:layout_marginBottom="@dimen/test_10dp"
            android:layout_marginTop="@dimen/test_FC_10" />

        <TextView
            android:id="@+id/test_text1"
            android:text="testText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignTop="@id/test_image"
            android:layout_toRightOf="@id/test_image"
            android:layout_toEndOf="@id/test_image" 
            android:layout_marginLeft="8dp"
            android:layout_marginTop="-4dp" />

        <TextView
            android:id="@+id/test_text2"
            android:text="@string/testText"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignLeft="@id/test_text1"
            android:layout_below="@id/test_text1"
            android:layout_toRightOf="@id/test_image"
            android:layout_toEndOf="@id/test_image"
            android:layout_alignStart="@id/test_text1" 
            android:layout_marginTop="9dp" />

        <TextView
            android:id="@+id/test_text3"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignLeft="@id/test_text1"
            android:layout_below="@id/test_text2"
            android:layout_toRightOf="@id/test_image"
            android:layout_toEndOf="@id/test_image"
            android:layout_alignStart="@id/test_text1" 
            android:layout_marginTop="2dp" />

        <TextView
            android:id="@+id/test_text4"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignBottom="@id/test_image"
            android:layout_alignParentRight="true"
            android:layout_alignParentEnd="true" 
            android:layout_marginBottom="2dp"
            android:layout_marginRight="3.3dp" />

    </RelativeLayout>

    <View
        android:id="@+id/test_divider"
        android:layout_width="match_parent"
        android:layout_height="1px"
        android:layout_below="@id/test_frame" />

</RelativeLayout>
```
* 转换后的ArkUI框架示例：
```typescript
/*
* 示例解释，当前示例中仅包含布局、对齐框架，仅用于复杂布局转换的参考
* 若真实原始xml中有其他组件属性的设置，请注意参考输入xml完成完整的一对一转换
*/

@Entry
@Component
struct TestFrame {
  build() {
    /*
    * RelativeLayout
     */
        
    // 解释：经解析当前布局是在同一列中，因此RelativeLayout()转换为Column()，若布局在同一行中，则转换为Row()
    Column() {
        /*
        * RelativeLayout
        */
      RelativeContainer() {
          /*
          * ImageView
           */
        Image('')
          .id('test_image')
          .width('77.39vp')
          .height('103.48vp')
          .margin({top: $r('app.float.test_10vp'), bottom: $r('app.float.test_FC_10')})
          // 解释：左边和父锚点容器的水平左边缘对齐
          .alignRules({
            left: { anchor: '__container__', align: HorizontalAlign.Start }
          })

        /*
        * TextView
         */
        Text('testText')
          .id('test_text1')
          .margin({left: '8vp', top: '-4vp'})
          // 解释：左边和test_image容器的水平右边缘对齐，上边和test_image容器的垂直上边对齐  
          .alignRules({
            left: { anchor: 'test_image', align: HorizontalAlign.End },
            top: { anchor: 'test_image', align: VerticalAlign.Top }
          })
                
        /*
        * TextView
         */
        Text($r('app.string.testText'))
          .id('test_text2')
          .margin({top: '9vp'})
          .alignRules({
            left: { anchor: 'test_text1', align: HorizontalAlign.Start },
            top: { anchor: 'test_text1', align: VerticalAlign.Bottom }
          })
        
        /*
        * TextView
         */
        Text('')
          .id('test_text3')
          .margin({top: '2vp'})
          .alignRules({
            left: { anchor: 'test_text1', align: HorizontalAlign.Start },
            top: { anchor: 'test_text2', align: VerticalAlign.Bottom }
          })
        
        /*
        * TextView
         */
        Text('')
          .id('test_text4')
          .margin({bottom: '2vp', right: '3.3vp'})
          .alignRules({
            right: { anchor: '__container__', align: HorizontalAlign.End },
            bottom: { anchor: 'test_image', align: VerticalAlign.Bottom }
          })
      }
      .id('test_frame')
      .backgroundColor('#0D000000')
      .alignSelf(ItemAlign.Stretch)
      .padding({left: '15vp', right: '15vp'})
      .width('100%')
      .height('auto')
        /*
        * View
         */
      Divider()
        .id('test_divider')
        .width('100%')
        .height('1vp')
        .alignSelf(ItemAlign.Stretch)
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          top: { anchor: 'test_frame', align: VerticalAlign.Bottom }
        })
    }
    .width('100%')
    .height('auto')
    .justifyContent(FlexAlign.Start)
    .clip(true)
  }
}
```
#### Tabs布局
1. 导航栏相关属性转换成`.barXXX()`属性设置，示例：`app:tabIndicatorHeight='10dp'`->`.barHeight('10vp')`
2. 导航栏颜色配置通过`.barBackgroundColor()`设置
#### List布局
1. `overScrollMode`属性转换示例：`android:overScrollMode="never"`->`.edgeEffect(EdgeEffect.None)`
### 常用组件转换规则
#### Text组件
1. 注意区分和TextInput设置的区别，Text文本溢出设置是在属性中设置，转换示例为：`android:ellipsize="end"`->`.textOverflow({overflow:TextOverflow.Ellipsis})`
2. 文本对齐通过`.alignSelf(ItemAlign.XXX)`进行转换，可选参数有：Auto、Start、Center、End、Baseline、Stretch
3. 文本组件显示内容转换示例：`android:text="testTxt"`->`Text('testTxt')`
#### TextInput组件
1. 文本框中文本对齐方式通过`.textAlign(TextAlign.XXX)`进行设置，可设置的值有：Start、End、Center、Justify
2. 注意区分和Text设置的区别，文本框溢出为直接设置，转换示例为：`android:ellipsize="end"`->`.textOverflow(TextOverflow.Ellipsis)`
3. 文本框imeOptions转换示例：`android:imeOptions="actionDone"`->`.enterKeyType(EnterKeyType.Done)`
#### Image组件
1. 图片对齐通过`.alignSelf(ItemAlign.XXX)`进行转换，可选参数有：`Auto、Start、Center、End、Baseline、Stretch`
2. 图片适配`ScaleType`模式转换成`.objectFit(ImageFit.XXX)`，可选参数：`Fill、Contain、Cover、Auto、ScaleDown、CENTER/TOP/...`等，转换示例：`app:actualImageScaleType="fitCenter"`->`.objectFit(ImageFit.CENTER)`
3. 图片描述转换示例：`android:contentDescription="desc"`->`.accessibilityDescription('desc')`
4. 图片组件必须对应生成`.fitOriginalSize(true)`属性配置来保证图片能够适配布局，注意遵守