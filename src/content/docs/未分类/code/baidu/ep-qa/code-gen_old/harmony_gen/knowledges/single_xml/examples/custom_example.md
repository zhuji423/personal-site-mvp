---
title: "custom_example"
description: "import android.content.Context import android.content.res.TypedArray import android.graphics.Color import android.util.A"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\harmony_gen\\knowledges\\single_xml\\examples\\custom_example.md"
---
### 输入自定义组件示例：
```TestTextView.kotlin
package com.baidu.test

import android.content.Context
import android.content.res.TypedArray
import android.graphics.Color
import android.util.AttributeSet
import android.util.TypedValue
import android.view.View
import android.widget.TextView
import kotlin.random.Random
import com.baidu.testmodule.TestComponent

/ **
* 自定义TextView
 * 该组件继承自TextView组件，并实现点击文本文本会随机变化的功能。
*/

class TestTextView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : TextView(context, attrs, defStyleAttr) {

    // 自定义属性
    private var testText: String? = null
    private var testIsRandom: Boolean = false

    // 随机文本数组
    private val testRandomTexts = arrayOf(
        "TestText",
        "RandomTestText",
        "..."
    )

    init {
        // 解析自定义属性
        val typedArray: TypedArray = context.obtainStyledAttributes(attrs, R.styleable.TestTextView, defStyleAttr, 0)

        // 获取自定义文本
        testText = typedArray.getString(R.styleable.TestTextView_testText)
        
        // 获取是否随机变化的属性
        testIsRandom = typedArray.getBoolean(R.styleable.TestTextView_testIsRandom, false)

        // 回收 TypedArray
        typedArray.recycle()

        // 应用自定义属性
        testApplyCustomAttributes()

        // 设置点击监听器
        testSetOnClickListener {
            if (testIsRandom) {
                testChangeTextRandomly(testIsRandom)
            }
        }
    }

    // 应用自定义属性到 TextView
    private fun testApplyCustomAttributes() {
        // 设置自定义文本
        this.text = testText
    }

    // 设置自定义文本
    fun testSetCustomText(text: String?) {
        this.text = text
    }

    // 随机改变文本内容
    private fun testChangeTextRandomly() {
        val randomIndex = Random.nextInt(testRandomTexts.size)
        testSetCustomText(testRandomTexts[randomIndex])
    }
}
```
### 输出自定义组件示例
* 输出路径：`entry/src/main/ets/components/test_text_view.ets`
* 输出代码示例：
```typescript
/*
* 自定义组件TestTextView
* 该组件继承至Text()组件，并实现点击文本文本会随机变化的功能。
 */

// 解释：`com.baidu`关键词开头的包需要从`components`导入
import { TestComponent } from '../components/test_component'

@Component
export struct TestTextView {
  // Text组件基础属性定义
  @Prop text: ResourceStr = 'Hello, Test Text!';
  @Prop fontColor: ResourceColor = '#000000';
  @Prop fontSize: number | string | Resource = 14;
  @State textOverflow: TextOverflow = TextOverflow.Ellipsis;
  @State maxLines: number = 1;
  @State testIsRandom: boolean = false;

  // 随机文本数组
  private testRandomTexts = [
    "TestText",
    "RandomTestText",
    "..."
  ];

  // 布局build函数
  build() {
    /*
    * 根据传入参数设置组件属性：init+testApplyCustomAttributes函数的转换
     */
    Text(this.text)
      .fontColor(this.fontColor)
      .fontSize(this.fontSize)
      // 解释：注意区分Text和TextInput的溢出设置，Text组件的溢出设置如下：
      .textOverflow({overflow: this.textOverflow})
      .maxLines(this.maxLines)
      //  // 控制文本随机变化自定义功能，以注释方式呈现
      // .onClick(() => {
      //  this.testChangeTextRandomly(this.testIsRandom)
      // })
  }
  
  // 自定义文本内容函数
  // 解释：注意文本类型变量均定义或声明成`ResourceStr`类型
  // testSetCustomText(text: ResourceStr): void {
  //   this.text = text;
  // }

  // 文本随机变换函数
  // private testChangeTextRandomly(value: boolean = false): void {
  //  if (value) {
  //    const randomIndex = Math.floor(Math.random() * this.testRandomTexts.length);
  //    this.text = this.testRandomTexts[randomIndex];
  //  }
  //}
}
```