---
title: "layout_example"
description: "@Entry @Component struct TestMain { build { / FrameLayout / RelativeContainer { / LinearLayout / Row { / <com.google.tes"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\harmony_gen\\knowledges\\single_xml\\examples\\layout_example.md"
---
### 输入主页面示例
* 主页面输入示例：
```test_main.xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tool="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:layout_width="65dp"
        android:layout_height="match_parent"
        android:layout_gravity="left"
        android:gravity="center_vertical"
        android:orientation="horizontal"
        tool:ignore="RtlHardcoded,UseCompoundDrawables">

        <com.google.test.TestImageView
            android:id="@+id/test_image1"
            android:layout_width="15dp"
            android:layout_height="23dp"
            android:layout_gravity="center_vertical"
            android:contentDescription="@string/test_txt1"
            android:src="@drawable/test_image1"
            app:actualImageScaleType="fitXY" />

        <com.baidu.test.TestTextView
            android:id="@+id/test_text1"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_vertical"
            android:layout_marginLeft="@dimen/test_num1"
            android:ellipsize="end"
            android:maxWidth="150dp"
            android:singleLine="true"
            android:textColor="@color/testColor1"
            android:textSize="@dimen/test_num_2dp"
            android:includeFontPadding="false"
            app:testIsRandom="true"
            tool:ignore="SpUsage"
            android:text="text1" />
                
        <EditView
            android:id="@+id/test_edit1"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="text2"
            android:imeOptions="actionDone"
            android:ellipsize="end"
            android:background="@drawable/test_edit_bg"
            android:layout_centerHorizontal="true" />
                
    </LinearLayout>
                
</FrameLayout>
```
* 关联背景设置输入：
```test_edit_bg.xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <corners
        android:topLeftRadius="@dimen/test_dimens_18dp"
        android:topRightRadius="@dimen/test_FS001" />
    <solid android:color="@color/test_white" />
</shape>
```
### 输出主页面示例
#### 注意
1. 示例中带`解释`关键词的注释仅供参考，在转换生成的过程中请忽略此类注释
2. 图片组件转换时，需设置`.fitOriginalSize(true)`，保证图片能够适配布局
* 输出主页面路径：`entry/src/main/ets/pages/test_main.ets`
* 转换输出代码示例：
```typescript
// 注意：引用路径中带`.baidu`关键词的自定义组件，需要导入使用，`<com.baidu.test.TestTextView`导入如下：
import { TestTextView } from "../components/test_text_view"


@Entry
@Component
struct TestMain {
  build() {
    /*
    * FrameLayout
     */
    RelativeContainer() {
      /*
      * LinearLayout
       */
      Row() {
        /*
        * <com.google.test.TestImageView
         */
                
        // 解释：其他不带关键词的均转换成对应默认组件直接使用，`<com.google.test.TestImageView`转换成`Image`，示例如下：
        Image($r('app.media.test_image1'))
          .id('test_image1')
          .width('15vp')
          .height('23vp')
          // 解释：app:actualImageScaleType="fitXY"图片适配，转换如下：
          .objectFit(ImageFit.Fill)
          // 解释：`.fitOriginalSize(true)`保证图片能够适配布局，因此图片组件转换时必须生成以下属性：
          .fitOriginalSize(true)
          // 解释：android:layout_gravity="center_vertical"相对布局垂直居中，转换如下：
          .alignRules(
            {center: {anchor: 'test_row', align: VerticalAlign.Center}}
          )
          // 解释：android:contentDescription="@string/test_txt1"，转换如下：
          .accessibilityDescription($r('app.string.test_txt1'))
                
        /*
        * com.baidu.test.TestTextView
        * FIXME 无法映射的属性：tool:ignore="SpUsage"
        * FIXME 无法映射的属性：android:includeFontPadding="false"
         */
                
        // 解释：引用路径带`.baidu`关键词的自定义组件，导入并使用，`<com.baidu.test.TestTextView`组件使用转换如下：
        TestTextView({
          text: "text1",
          textOverflow: TextOverflow.Ellipsis,
          maxLines: 1,
          fontColor: $r('app.color.testColor1'),
          // 解释：变量名若包含`dp`关键词，则需要适配从`dp`到`vp`的映射转换，如`test_num_2dp`转换如下：
          fontSize: $r('app.float.test_num_2vp'),
          testIsRandom: true
        })
          .id('test_txt1')
          // 解释：自定义组件的`margin`映射在组件外层，转换如下： 
          // 解释：不含`dp`关键词的常规变量名直接进行转换，如`test_num1`转换如下：
          .margin({left: $r('app.float.test_num1')})
          // 解释：自定义组件的最大宽度/高度映射，android:maxWidth="150dp"最大宽度转换如下：
          .constraintSize({maxWidth: '150vp'})
          // 注意区分中点对齐，垂直中点对齐设置`center`，示例如下：
          .alignRules(
            {center: {anchor: 'test_row', align: VerticalAlign.Center}}
          )
                
        /*
        * EditView
         */
                
        // 解释：TextInput的文本加载方式如下
        TextInput({ placeholder: 'text2'})
          .id('test_edit1')
          .enterKeyType(EnterKeyType.Done)
          // 注意区分Text和TextInput的溢出设置，TextInput组件的溢出设置如下：
          .textOverflow(TextOverflow.Ellipsis)
          // 注意区分中点对齐，水平中点对齐设置`middle`，示例如下：
          .alignRules(
            {middle: {anchor: 'test_row', align: HorizontalAlign.Center}}
          )
          // 解释：背景`android:background="@drawable/test_edit_bg"`需结合test_edit_bg.xml的内容进行解析转换，转换如下：
          // 背景颜色解析
          .backgroundColor($r('app.color.test_white'))
          // 背景圆角半径解析
          .borderRadius({
              // 注意：数值资源转换是`app.float`关键词开头
              topLeft: $r('app.float.test_dimens_18vp'),
              topRight: $r('app.float.test_FS001')
          })
      }
      /*
      * FIXME 无法映射的属性：tool:ignore="RtlHardcoded,UseCompoundDrawables">
       */
      .id('test_row')
      .width('65vp')
      .height('100%')
      // 解释：android:gravity="center_vertical"自身垂直居中，转换如下：
      .alignItems(VerticalAlign.Center)
      // 解释：android:layout_gravity="left"布局相对水平方向左对齐，转换如下：
      .alignRules(
        {left: {anchor: '__container__', align: HorizontalAlign.Start}}
      )
    }
    .width('100%')
    .height('100%')
  }
}
```
* 输出主页面路径配置路径：`entry/src/main/resources/base/profile/main_pages.json`
* 输出路径配置示例：
```json
{
  "src": [
    "pages/test_main"
  ]
}
```