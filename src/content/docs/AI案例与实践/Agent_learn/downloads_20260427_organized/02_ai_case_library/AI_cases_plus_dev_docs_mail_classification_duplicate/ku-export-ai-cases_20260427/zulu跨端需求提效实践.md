---
title: "一 方案概述"
description: "zulu跨端需求提效实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\zulu跨端需求提效实践.md"
---
zulu跨端需求提效实践

#### 🧑‍🏫 案例作者：[@张勇](https://ku.baidu-int.com?t=mention&mt=contact&id=3c14c280-fce1-11f0-8e48-677c8e34bef4)[@张士杰](https://ku.baidu-int.com?t=mention&mt=contact&id=4582da50-fce1-11f0-8e48-677c8e34bef4)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了Zulu跨端提效方案与规则体系。通过建立语言层、架构层、业务层及工具层的Rules，实现多端代码一致性。详细展示了Kotlin/Compose编码规范、View转Compose的迁移标准（如状态提升、UI一致性）以及Figma2Code的生成规则。此外，还提供了amis2Code的JSON转Objective-C代码规范，强调动态读取配置而非硬编码。
# 一 方案概述
## 1.1 背景
**客户端团队现状：**

* 多端业务逻辑不统一、功能完成度不统一
* 设计到开发转换效率低

**解决方案价值：**

* 保证多端代码一致性、鸿蒙快速追平android、ios功能

# 二、技术设计
## 2.1 rules整体设计
[流程图]
                                                                     跨端rule全景图

* **业务层（Business Layer）**
    * **描述**：包含各业务领域特定的Rules，针对不同业务场景定制化规则

* **工具层（Tool Layer）**
    * **新增代码： **根据设计稿、PM需求文档、server api文档等生成代码
    * **存量代码： **跨端转换工具相关的Rules，负责不同格式和平台间的代码转换

* **架构层（Architecture Layer）: **移动端架构最佳实践的Rules，确保代码结构统一和可维护性
* **语言层（Language Layer）:  **底层编程语言和公司部门编码标准的Rules，优先级最高

## 2.2 已实现功能技术细节
### 2.2.1 语言规范实践
使用的规则如下：

```
---
description: 
globs: 
alwaysApply: true
---
# Kotlin编码规范

## 前言
为统一公司Kotlin项目编码规范，提高可读性，增加代码质量，特制定本规范。
本规范主要适用于Android项目。
本规范基于：
- Android官方Kotlin Style Guide
- Kotlin官方编程规范  
- 百度Java开发规范
- 百度自研规范

## 1. 源文件规范

### 1.1 文件编码格式
[强制] 所有源文件编码必须是UTF-8

### 1.2 文件命名
[强制] 所有文件都必须以.kt作为后缀名
[强制] 如一个源码文件仅包含一个顶级类，则必须和它包含的顶层类名保持一致
[强制] 如包含多个顶级定义，请选择能够描述该文件内容的名字作为文件名，并符合帕斯卡命名法

### 1.3 特殊字符
[强制] 缩进必须使用4个空格，禁止使用Tab
[强制] 使用标准转义字符(\b, \n等)，禁止使用等价Unicode转义
[强制] 非ASCII字符优先使用可读性高的形式

## 2. 源文件组织结构
[强制] 源文件必须按顺序由以下部分组成：
1. 许可证/版权声明(可选)
2. 文件级注解
3. package语句
4. import语句
5. 顶层声明

## 3. 代码格式

### 3.1 花括号
[强制] 遵循K&R风格：
- 左花括号前不换行，后换行
- 右花括号前换行
- 空代码块也必须保持格式

### 3.2 缩进
[强制] 使用4个空格缩进

### 3.3 行长度
[强制] 单行不超过120字符

### 3.4 空白
[强制] 关键字与括号之间加空格
[强制] 操作符两侧加空格
[强制] 逗号、冒号后加空格

## 4. 命名规范

### 4.1 包名
[强制] 全小写，不使用下划线

### 4.2 类名
[强制] 帕斯卡命名法，使用名词或名词短语

### 4.3 方法名
[强制] 驼峰命名法，使用动词或动词短语

### 4.4 常量名
[强制] 全大写，下划线分隔

## 5. 文档注释
[强制] 公共API必须使用KDoc注释
[建议] 使用标准标签：@param, @return等

## 6. 编程实践

### 6.1 空安全
[强制] 避免使用!!操作符
[建议] 优先使用安全调用(?.)和Elvis操作符(?:)

### 6.2 性能
[建议] 集合操作使用序列(asSequence)
[强制] 私有成员变量必须设为private

### 6.3 异常处理
[建议] 使用runCatching处理异常
[强制] I/O操作必须使用use关闭资源

## 附录：规范来源
1. Android官方Kotlin Style Guide
2. Kotlin官方编程规范
3. 百度Java开发规范
4. 百度自研规范
```
```
---
description:
globs:
alwaysApply: true
---
# Compose编码规范

## 1. Composable函数命名规范

### 1.1 函数命名规则
[强制] 显示界面的Composable函数（无返回值）使用大驼峰命名
[强制] 有返回值的Composable函数使用小驼峰命名

```kotlin
// 显示界面的Composable函数
@Composable
fun TopAppBar(
    // ...
)

// 有返回值的Composable函数
@Composable
fun topAppBarColors(
    // ...
): TopAppBarColors
```

### 1.2 函数参数排序
[强制] 强制参数在前，有默认值的参数在后
[强制] Modifier参数放在有默认值参数的第一位

```kotlin
@Composable
fun TopAppBar(
    title: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    navigationIcon: @Composable () -> Unit = {},
    actions: @Composable RowScope.() -> Unit = {},
    expandedHeight: Dp = TopAppBarDefaults.TopAppBarExpandedHeight,
    windowInsets: WindowInsets = TopAppBarDefaults.windowInsets,
    colors: TopAppBarColors = TopAppBarDefaults.topAppBarColors(),
    scrollBehavior: TopAppBarScrollBehavior? = null
)
```

## 2. Composable函数设计原则

### 2.1 依赖注入
[强制] 依赖应通过参数传递，不应在函数内部创建

```kotlin
// 反例
@Composable
private fun MyComposable() {
    val viewModel = viewModel<MyViewModel>()
    // ...
}

// 正例
@Composable
private fun MyComposable(
    viewModel: MyViewModel = viewModel(),
) {
    // ...
}
```

### 2.2 单一职责
[强制] Composable函数应只负责显示界面或返回值，不可同时兼顾两者

### 2.3 不可变类型
[强制] Composable函数之间不要传递可变类型（ArrayList<T>, MutableState<T>等）

### 2.4 内容完整性
[强制] Composable函数的内容正确性不能依赖调用方

```kotlin
// 反例
Column {
    InnerContent()
}

@Composable
private fun InnerContent() {
    Text(...)
    Image(...)
    Button(...)
}

// 正例
@Composable
private fun InnerContent() {
    Column {
        Text(...)
        Image(...)
        Button(...)
    }
}
```

## 3. CompositionLocal规范

### 3.1 命名规范
[强制] CompositionLocal命名应以Local前缀开头，格式：Local + 数据类型

```kotlin
val LocalDensity = staticCompositionLocalOf<Density> {
    noLocalProvidedFor("LocalDensity")
}
```

## 4. 预览函数规范

### 4.1 命名规范
[强制] 单个预览函数使用Preview后缀
[强制] 多个预览函数使用Previews后缀
[强制] 预览函数必须是private

## 5. State管理规范

### 5.1 状态提升
[强制] 所有逻辑应向上提升
[强制] 页面至少包含两个Composable函数：一个处理逻辑，一个负责显示
[强制] 状态持有者实例（ViewModel）、状态数据流实例只允许在逻辑处理函数中持有

```kotlin
@Composable
private fun LearnRoute(
    navController: NavController,
    viewModel: LearnVM = koinViewModel(),
) {
    // flow 使用方式
    val text = viewModel.text.collectAsStateWithLifecycle().value
    // LiveData 使用方式
    // val text = viewModel.text.asFlow().collectAsStateWithLifecycle().value

    LearnScreen(
        onBackClick = { navController.navigateUp() },
        text = text,
    )
}

@Composable
private fun LearnScreen(
    onBackClick: () -> Unit,
    text: String,
) {
    TitleBarWithBack(onBackClick = onBackClick) {
        Box(modifier = Modifier.fillMaxSize()) {
            Text(
                text = text,
                modifier = Modifier.align(Alignment.Center),
            )
        }
    }
}
```

### 5.2 remember使用
[强制] Compose state在Composable函数内必须使用remember

```kotlin
var isSuccess by remember { mutableStateOf(false) }
```

### 5.3 不可变类型
[建议] 尽可能使用@Immutable注解类
[建议] 避免使用不稳定的集合，推荐使用Kotlinx Immutable集合

```kotlin
@Immutable
data class StringList(val items: List<String>)
// ...
val list: StringList = StringList(yourList)
```

## 6. Modifier使用规范

### 6.1 参数暴露
[强制] 自定义公共组件必须暴露Modifier参数

### 6.2 唯一性原则
[强制] 一个Compose组件对应一个Modifier，不可重复使用

```kotlin
@Composable
private fun InnerContent(modifier: Modifier = Modifier) {
    Column(modifier) {
        Text(Modifier.clickable(), ...)
        Image(Modifier.size(), ...)
        Button(Modifier, ...)
    }
}
```

### 6.3 默认值
[强制] Modifier参数必须设置默认值
[强制] 不要使用Modifier扩展函数，使用Modifier.composed

## 7. 资源使用规范

### 7.1 图标资源
[建议] 简单小图标使用ImageVector矢量图
[建议] 使用Valkyrie插件将SVG转为ImageVector

### 7.2 资源命名
[强制] Compose资源命名需要带上模块名（如：search_ic_back）

## 8. 页面命名规范

### 8.1 导航相关命名
[强制] 导航目的地命名：`Route + 功能`
[强制] 导航目的地页面命名：`功能 + Route`
[强制] 导航注册命名：小驼峰格式的导航目的地页面命名

```kotlin
// 导航目的地
@Serializable
data class RouteMainSearch(
    val defaultSearchText: String = "",
)

// 导航注册
fun NavGraphBuilder.mainSearchRoute() {}

// 导航目的地页面
@Composable
private fun MainSearchRoute()
```

### 8.2 文件命名
[强制] 所有包含Compose页面的文件都以Screen为后缀（如：MainSearchScreen）

## 9. 文字大小规范
[强制] 文字使用单位DP，避免响应系统字体大小设置

```kotlin
fontSize = 24.dp
```

## 附录：规范优先级
本规范与kotlin.mdr规范共同使用，当规范冲突时：
1. 本规范中Compose相关规则优先
2. kotlin.mdr中通用Kotlin规则作为补充
```
#### 演示视频
[附件]
### 2.2.1  view2Comose 上的提效实践
将已有代码转成跨端UI代码

使用的规则如下：

```
# Zulu Compose 迁移规范

## 1. 迁移原则

### 1.1 兼容性保证
[强制] 必须保持与原组件完全相同的功能逻辑和交互行为
[强制] 必须使用相同的 ViewModel 和数据模型
[强制] 必须保持相同的统计埋点和日志输出

### 1.2 渐进式迁移
[建议] 优先从叶子节点组件开始迁移
[建议] 保持 XML 和 Compose 组件共存过渡期
[强制] 使用基础Compose组件,不允许使用无法引用的函数

## 2. 组件设计规范

### 2.1 状态管理
[强制] 必须使用状态提升模式，遵循 compose.mdr 5.1 规范
```kotlin
@Composable
private fun CatalogueComposeScreen(
    itemClickListener: CatalogueComposeFragment.OnItemClickListener,
    readerViewModel: ReaderViewModel?
) {
    // 状态处理逻辑
    CatalogueScreenContent(state, actions)
}

@Composable
private fun CatalogueScreenContent(
    state: CatalogueState,
    onItemClick: (CatalogueEntity) -> Unit,
    onSortClick: () -> Unit
) {
    // 纯UI展示
}
```

### 2.2 参数传递
[强制] 必须保留原 Fragment/Activity 的所有参数
[强制] 回调接口命名必须保持 `On[Action]Listener` 格式
```kotlin
interface OnItemClickListener {
    fun onItemClick(catalogueEntity: CatalogueEntity)
}
```

## 3. UI 一致性规范

### 3.1 样式匹配
[强制] 必须使用相同的尺寸、颜色和字体资源
[强制] 必须复现原交互效果（波纹、动画等）

### 3.2 布局结构
[强制] 必须保持相同的视图层级结构
[强制] 必须实现相同的滚动和焦点行为

## 4. 命名规范

### 4.1 文件命名
[强制] Compose Fragment 文件命名必须遵循 `[功能名]ComposeFragment.kt`
[强制] 必须包含配套的 README 文档

### 4.2 Composable 函数命名
[强制] 遵循 compose.mdr 1.1 规范，显示界面的 Composable 函数使用大驼峰命名
```kotlin
@Composable
fun CatalogueHeader(
    chapterCount: Int,
    isAscending: Boolean,
    isLoading: Boolean,
    currentProgress: Float,
    onSortClick: () -> Unit
)
```

### 4.3 参数排序
[强制] 遵循 compose.mdr 1.2 规范，Modifier 参数放在有默认值参数的第一位
```kotlin
@Composable
fun CatalogueItem(
    catalogue: CatalogueEntity,
    isHighlighted: Boolean,
    modifier: Modifier = Modifier,
    onClick: () -> Unit
)
```

## 5. 资源使用规范

### 5.1 字符串资源
[强制] 必须使用 `stringResource()` 引用字符串，禁止硬编码
```kotlin
Text(
    text = stringResource(R.string.catalog_sort_down_text),
    fontSize = 14.sp
)
```

### 5.2 图片资源
[强制] 必须使用 `painterResource()` 引用图片资源
```kotlin
Icon(
    painter = painterResource(id = R.drawable.reader_sort_icon),
    contentDescription = "排序"
)
```

## 6. 状态管理规范

### 6.1 remember 使用
[强制] Compose state 在 Composable 函数内必须使用 remember
```kotlin
var isAscending by remember { mutableStateOf(true) }
```
### 6.2 livedata by 使用
liveDate 使用
```
 val bookmarks:List<Bookmark> =
        bookmarkViewModel?.allBookmarksLiveData?.asFlow()?.collectAsState(emptyList<Bookmark>())?.value ?: emptyList()
```


### 6.2 状态提升
[强制] 所有逻辑应向上提升，遵循 compose.mdr 5.1 规范
[强制] 页面至少包含两个 Composable 函数：一个处理逻辑，一个负责显示

## 7. Modifier 使用规范

### 7.1 参数暴露
[强制] 自定义公共组件必须暴露 Modifier 参数
[强制] Modifier 参数必须设置默认值

### 7.2 唯一性原则
[强制] 一个 Compose 组件对应一个 Modifier，不可重复使用

## 8. 测试验证规范

### 8.1 测试覆盖
[强制] 必须通过原有单元测试
[强制] 必须新增 Compose 专项测试

### 8.2 验证清单
1. [ ] 功能逻辑验证
2. [ ] 交互行为验证
3. [ ] 性能基准测试
4. [ ] 内存泄漏检测

## 9. 文档规范

### 9.1 迁移文档
[强制] 必须包含以下章节：
- 功能对照表
- API 变更说明
- 集成指南
- 已知问题

### 9.2 代码注释
[强制] 必须标注迁移来源
```kotlin
// Migrated from CatalogueFragment
// Commit: xxxxxx
```

## 附录：状态栏适配最佳实践

### 问题描述
当 Compose Fragment 在 Dialog、BottomSheetDialog 或全屏 Activity 中使用时，可能出现 UI 显示在状态栏区域的问题。

### 解决方案
[强制] 所有 Compose Fragment 必须在 ComposeView 上设置 `fitsSystemWindows = true`

```kotlin
override fun onCreateView(
    inflater: LayoutInflater,
    container: ViewGroup?,
    savedInstanceState: Bundle?
): View {
    return ComposeView(requireContext()).apply {
        // 适配状态栏，防止UI显示在状态栏区域
        fitsSystemWindows = true
        setContent {
            MyComposeContent()
        }
    }
}
```

### 验证清单
1. [ ] ComposeView 是否设置了 `fitsSystemWindows = true`
2. [ ] 在 Dialog/BottomSheetDialog 中显示时是否正常
3. [ ] 在全屏 Activity 中显示时是否正常
4. [ ] 状态栏颜色和背景是否正确适配

## 附录：迁移流程

### 阶段一：准备阶段
1. 分析原组件依赖关系
2. 检查 Compose 依赖配置
3. 不允许修改其他项目文件，不允许添加项目没有依赖
4. 不允许虚构原文件没有的函数或者变量
5. 保持相同变量名称以及函数名称
6. 制定迁移计划

### 阶段二：实现阶段
[强制] 仅允许修改新生成文件，不允许改动其他文件来实现功能
1. 创建 Compose Fragment 骨架
2. 逐步迁移子组件
3. 使用 Compose 原生的布局组件
4. 实现状态管理
5. [强制] 必须适配状态栏样式，在 ComposeView 上设置 `fitsSystemWindows = true`
```kotlin
override fun onCreateView(
    inflater: LayoutInflater,
    container: ViewGroup?,
    savedInstanceState: Bundle?
): View {
    return ComposeView(requireContext()).apply {
        // 适配状态栏，防止UI显示在状态栏区域
        fitsSystemWindows = true
        setContent {
            // Compose 内容
        }
    }
}
```
6. [强制] 需要适配Activity顶部状态栏样式，保持和原有文件相同逻辑，保证相同使用场景下，UI展示时宽高相同
7. 检查生成文件是否有编译错误，是否全部正确import

## 规范优先级
本规范与 compose.mdr、kotlin.mdr 规范共同使用，当规范冲突时：
1. 本规范中 Zulu 迁移相关规则优先
2. compose.mdr 中 Compose 相关规则作为补充
3. kotlin.mdr 中通用 Kotlin 规则作为基础

### 检查错误
当所有代码生成完毕之后，再次检查是否有import等编译问题
```
#### **演示视频**
[附件]
### 2.2.3 Figma2Code的提效实践
主要围绕Figma上的UI稿来生成跨端代码

#### 示例一
###### 参考UI稿
![](/personal-site-mvp/img/doc-placeholder.svg "")
[https://www.figma.com/design/RL1uqrROB8u6eXAmIp4enD/Terabox-AI%E7%BE%8E%E5%9B%BE%E7%BC%96%E8%BE%91--Copy-?node-id=6231-2001&t=rfXz9j2LadYBnS4l-0](https://www.figma.com/design/RL1uqrROB8u6eXAmIp4enD/Terabox-AI%E7%BE%8E%E5%9B%BE%E7%BC%96%E8%BE%91--Copy-?node-id=6231-2001&t=rfXz9j2LadYBnS4l-0)

###### 使用的规则
```
## 技术栈要求
遵循Kotlin和Android开发的最佳实践和代码规范，符合Compose Multiplatform 和 Kotlin Multiplatform Mobile的最佳实践和代码规范。 信息类Rule

## 任务要求
项目开发规范（Kotlin / Android / Compose Multiplatform） 信息类Rule

1. 技术栈要求  信息类Rule
- 遵循 Kotlin 与 Android 开发最佳实践及代码规范。
- 符合 Compose Multiplatform 和 Kotlin Multiplatform Mobile (KMM) 的最佳实践与代码规范。
- 项目整体架构采用 MVI 模式。

2. 模块与代码组织
1) 新增 Compose Multiplatform 业务代码统一放在：kmp/business/kmm-ai-images. 信息类Rule
2) 主题与样式： 指令类Rule
    - 颜色优先从 com.mars.united.international.kmm.theme.TeraBoxColors 查找，不存在可在末尾新增
    - 字体大小、间距优先从 com.mars.united.international.kmm.theme.Dimens 查找，不存在可在末尾新增。
    - 所有字体、颜色、间距、Font、多语言等主题信息统一放在 kmp/services/theme/ 模块。
3) 公共组件统一存放在 kmp/ui-widget/common-widget 模块（吸顶、Dialog、骨架屏、刷新加载、WebView 等）。 指令类Rule

3. Compose 使用规范. 信息类Rule/指令类Rule
   3.1 基础规则
- 所有 Text 使用 com.dubox.drive.common.widget.cmp.widget.TeraText
- 点击事件使用 Modifier.clickableSmart（import com.dubox.drive.common.widget.cmp.extended.clickableSmart）
- 遵循 androidx.compose.material3 组件体系
- 符合 Compose 重组机制，代码保持简洁精炼
- 编写布局时，顺序按照 UI 稿从左到右、从上到下
- 学会使用 fillMaxSize()、fillMaxWidth() 等函数填充布局

3.2 尺寸与样式引用  约束类Rule
- 间距：禁止直接写 16.dp，统一使用 Dimens，如 padding(Dimens.dimen_16dp)
- 宽高：禁止直接写 width(16.dp)，统一使用 width(Dimens.dimen_16dp) / height(Dimens.dimen_16dp)
- 字体大小：fontSize = Dimens.text_16sp
- 颜色：color = TeraBoxColors.gc06，若不存在需新增 dynamicColor 格式的颜色定义
- 不要在com.mars.united.international.kmm.theme.Dimens中新增

3.3 图片与资源引用  指令类Rule
- 使用 androidx.compose.foundation.Image 替换 Icon（import androidx.compose.foundation.Image）
- Image中的contentDescription属性 可直接写字符串，如 "图片"，例如contentDescription = "图片"
- painterResource 导入 dev.icerock.moko.resources.compose.painterResource
- MR 导入 com.kmm.terabox.MR
- 如果使用网络图片，使用rememberAsyncImagePainter时，自动添加import coil3.compose.rememberAsyncImagePainter

3.4 字符串与多语言  指令类Rule
- 所有新增的text字符串追加到 kmp/services/theme/src/commonMain/moko-resources/base/strings.xml，不能删除已有的字符串
- TeraText 中使用 stringResource（import dev.icerock.moko.resources.compose.stringResource）
- 多语言字符串使用 MR.strings.xxx 格式，其中xxx来自于新增的strings.xml文件中的key值

3.5 预览与注解. 指令类Rule
- 所有 @Composable 函数需额外提供 @Preview 方法（import org.jetbrains.compose.ui.tooling.preview.Preview）
- 所有 fun 方法必须添加 /** ... */ 格式的注释

4. ViewModel 与架构. 指令类Rule
- ViewModel 继承 androidx.lifecycle.ViewModel
- Compose 承载的 Activity 中不创建 ViewModel，在 setContent {} 中仅传递 ComposeView

5. 构建与文件要求.  约束类Rule
- 使用 build.gradle，不使用 build.gradle.kts
- 不修改 build.gradle 中版本信息
- 不新增图片资源文件
- 不新增xml文件

6. 自动导包规范 指令类Rule
   clickableSmart -> com.dubox.drive.common.widget.cmp.extended.clickableSmart
   stringResource -> dev.icerock.moko.resources.compose.stringResource
   MR -> com.kmm.terabox.MR
   painterResource -> dev.icerock.moko.resources.compose.painterResource
   Image -> androidx.compose.foundation.Image
   background -> androidx.compose.foundation.background
   Alignment -> androidx.compose.ui.Alignment
   Preview -> org.jetbrains.compose.ui.tooling.preview.Preview
   rememberAsyncImagePainter -> coil3.compose.rememberAsyncImagePainter


## 其他
```
###### 演示视频
[附件]


#### 示例二
###### 参考UI稿
![](/personal-site-mvp/img/doc-placeholder.svg "")
[https://www.figma.com/design/fpjkTGsWPkBvek2s9mfVeZ/Terabox-AI%E4%B8%93%E9%A1%B9--Copy-?node-id=12556-134362&t=ifv4yYdv051hQ28Z-0](https://www.figma.com/design/fpjkTGsWPkBvek2s9mfVeZ/Terabox-AI%E4%B8%93%E9%A1%B9--Copy-?node-id=12556-134362&t=ifv4yYdv051hQ28Z-0)



###### 使用的规则
```
## 技术栈要求
遵循Kotlin和Android开发的最佳实践和代码规范，符合Compose Multiplatform 和 Kotlin Multiplatform Mobile的最佳实践和代码规范。

## 任务要求
项目开发规范（Kotlin / Android / Compose Multiplatform）

1. 技术栈要求
- 遵循 Kotlin 与 Android 开发最佳实践及代码规范。
- 符合 Compose Multiplatform 和 Kotlin Multiplatform Mobile (KMM) 的最佳实践与代码规范。
- 项目整体架构采用 MVI 模式。

2. 模块与代码组织
1) 新增 Compose Multiplatform 业务代码统一放在：kmp/business/kmm-ai-images
2) 主题与样式：
    - 颜色优先从 com.mars.united.international.kmm.theme.TeraBoxColors 查找，不存在可在末尾新增
    - 字体大小、间距优先从 com.mars.united.international.kmm.theme.Dimens 查找，不存在可在末尾新增。
    - 所有字体、颜色、间距、Font、多语言等主题信息统一放在 kmp/services/theme/ 模块。
3) 公共组件统一存放在 kmp/ui-widget/common-widget 模块（吸顶、Dialog、骨架屏、刷新加载、WebView 等）。

3. Compose 使用规范
   3.1 基础规则
- 所有 Text 使用 com.dubox.drive.common.widget.cmp.widget.TeraText
- 点击事件使用 Modifier.clickableSmart（import com.dubox.drive.common.widget.cmp.extended.clickableSmart）
- 遵循 androidx.compose.material3 组件体系
- 符合 Compose 重组机制，代码保持简洁精炼
- 编写布局时，顺序按照 UI 稿从左到右、从上到下
- 学会使用 fillMaxSize()、fillMaxWidth() 等函数填充布局

3.2 尺寸与样式引用
- 间距：禁止直接写 16.dp，统一使用 Dimens，如 padding(Dimens.dimen_16dp)
- 宽高：禁止直接写 width(16.dp)，统一使用 width(Dimens.dimen_16dp) / height(Dimens.dimen_16dp)
- 字体大小：fontSize = Dimens.text_16sp
- 颜色：color = TeraBoxColors.gc06，若不存在需新增 dynamicColor 格式的颜色定义
- 不要在com.mars.united.international.kmm.theme.Dimens中新增

3.3 图片与资源引用
- 使用 androidx.compose.foundation.Image 替换 Icon（import androidx.compose.foundation.Image）
- Image中的contentDescription属性 可直接写字符串，如 "图片"，例如contentDescription = "图片"
- painterResource 导入 dev.icerock.moko.resources.compose.painterResource
- MR 导入 com.kmm.terabox.MR
- 如果使用网络图片，使用rememberAsyncImagePainter时，自动添加import coil3.compose.rememberAsyncImagePainter

3.4 字符串与多语言
- 所有新增的text字符串追加到 kmp/services/theme/src/commonMain/moko-resources/base/strings.xml，不能删除已有的字符串
- TeraText 中使用 stringResource（import dev.icerock.moko.resources.compose.stringResource）
- 多语言字符串使用 MR.strings.xxx 格式，其中xxx来自于新增的strings.xml文件中的key值

3.5 预览与注解
- 所有 @Composable 函数需额外提供 @Preview 方法（import org.jetbrains.compose.ui.tooling.preview.Preview）
- 所有 fun 方法必须添加 /** ... */ 格式的注释

4. ViewModel 与架构
- ViewModel 继承 androidx.lifecycle.ViewModel
- Compose 承载的 Activity 中不创建 ViewModel，在 setContent {} 中仅传递 ComposeView

5. 构建与文件要求
- 使用 build.gradle，不使用 build.gradle.kts
- 不修改 build.gradle 中版本信息
- 不新增图片资源文件
- 不新增xml文件

6. 自动导包规范
   clickableSmart -> com.dubox.drive.common.widget.cmp.extended.clickableSmart
   stringResource -> dev.icerock.moko.resources.compose.stringResource
   MR -> com.kmm.terabox.MR
   painterResource -> dev.icerock.moko.resources.compose.painterResource
   Image -> androidx.compose.foundation.Image
   background -> androidx.compose.foundation.background
   Alignment -> androidx.compose.ui.Alignment
   Preview -> org.jetbrains.compose.ui.tooling.preview.Preview
   rememberAsyncImagePainter -> coil3.compose.rememberAsyncImagePainter


## 其他
```


###### 演示视频
[附件]


###### 和ChatGpt上生成的对比
```
@Composable
fun UserCard(
    avatarUrl: String,
    name: String,
    title: String,
    followers: String,
    files: String,
    onSubscribeClick: () -> Unit
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // Avatar
        AsyncImage(
            model = avatarUrl,
            contentDescription = "Avatar",
            modifier = Modifier
                .size(40.dp)
                .clip(CircleShape)
        )

        Spacer(modifier = Modifier.width(8.dp))

        Column(
            modifier = Modifier.weight(1f)
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    text = name,
                    color = Color(0xFF1E88E5), // 蓝色
                    fontWeight = FontWeight.Medium,
                    fontSize = 14.sp
                )
                Spacer(modifier = Modifier.width(4.dp))
                Text(
                    text = title,
                    color = Color.Black,
                    fontWeight = FontWeight.Medium,
                    fontSize = 14.sp
                )
            }

            Spacer(modifier = Modifier.height(4.dp))

            Row(verticalAlignment = Alignment.CenterVertically) {
                Icon(
                    painter = painterResource(id = R.drawable.ic_followers), // 自定义图标
                    contentDescription = null,
                    modifier = Modifier.size(14.dp),
                    tint = Color.Gray
                )
                Spacer(modifier = Modifier.width(4.dp))
                Text(
                    text = followers,
                    fontSize = 12.sp,
                    color = Color.Gray
                )

                Spacer(modifier = Modifier.width(12.dp))

                Icon(
                    painter = painterResource(id = R.drawable.ic_files), // 自定义图标
                    contentDescription = null,
                    modifier = Modifier.size(14.dp),
                    tint = Color.Gray
                )
                Spacer(modifier = Modifier.width(4.dp))
                Text(
                    text = files,
                    fontSize = 12.sp,
                    color = Color.Gray
                )
            }
        }

        Spacer(modifier = Modifier.width(8.dp))

        Button(
            onClick = onSubscribeClick,
            colors = ButtonDefaults.buttonColors(
                backgroundColor = Color(0xFF1E88E5),
                contentColor = Color.White
            ),
            shape = RoundedCornerShape(8.dp),
            contentPadding = PaddingValues(horizontal = 16.dp, vertical = 4.dp)
        ) {
            Text(text = "Subscribe", fontSize = 14.sp)
        }
    }
}
```
### 2.2.4 amis2Code
#### 使用的规则
```
### 技术栈要求
遵循iOS的Objective-C开发的最佳实践和代码规范。

### 任务说明
根据提供的JSON配置数据,自动生成Objective-C配置类的头文件和实现文件。**所有配置值都通过BDPanConfigService动态读取,不硬编码任何业务数据。**

---

### 第一步: 分析JSON结构
**识别文件**
1.读取并解析 amis_config.json 文件内容

**识别三层结构:**
1. **区域 (Area)**: JSON最外层的key
2. **节点 (Node)**: 每个`cfg_list`数组项中`node_key`字段的value
3. **字段 (Field)**: 每个`cfg_list`数组项中除`cfg_version`、`node_key`、`node_name`之外的所有key

**排除字段:**
- `cfg_version`: 版本字段,不生成方法
- `node_name`: 仅用于生成注释,不生成对应方法

---

### 第二步: 命名转换规则

**驼峰命名转换:**
- 区域: 将下划线命名转为小驼峰 → **驼峰区域**
- 节点: 将下划线命名转为小驼峰 → **驼峰节点**
- 字段: 将下划线命名转为小驼峰 → **驼峰字段**

**方法名生成公式:**
```
方法名 = 驼峰区域 + "_" + 驼峰节点 + "_" + 驼峰字段
```

**方法类型:**
- 全部使用类方法(以`+`开头)

---

### 第三步: 返回值类型判断规则

**按以下优先级顺序判断字段的value:**

1. **JSON对象字符串** (value以`{`开头且以`}`结尾)
   - 返回类型: `NSDictionary *`
   - 实现: 通过配置服务读取后,调用`dictionaryFromJSONString:`转换

2. **JSON数组字符串** (value以`[`开头且以`]`结尾)
   - 返回类型: `NSArray *`
   - 实现: 通过配置服务读取后,调用`arrayFromJSONString:`转换

3. **纯数字类型** (value是数字,不带引号)
   - 返回类型: `NSInteger`
   - 实现: 通过配置服务读取数字值

4. **字符串类型** (value是带引号的字符串)
   - 返回类型: `NSString *`
   - 实现: 通过配置服务读取字符串值

---

### 第四步: 注释规范

**区域注释:**
- 位置: 每个新区域开始前空2行
- 格式: `// 区域的原始key`

**方法注释:**
- 格式: `// node_name的值 + 空格 + 驼峰字段`

---

### 第五步: 动态配置读取规则

**关键原则: 所有数据通过BDPanConfigService动态读取,使用原始的区域key、节点key和字段key。**

**配置读取路径:**
```
区域原始key → node_key → 字段原始key
```

**实现模式:**
```objective-c
// 通过配置服务读取值
NSString *value = [BDPanConfigService getValueForArea:@"区域原始key" 
                                               nodeKey:@"节点原始key" 
                                              fieldKey:@"字段原始key"];
```

---

### 第六步: 方法实现模板

**字典类型实现模板:**
```objective-c
// [node_name值] [驼峰字段]
+ (NSDictionary *)方法名 {
    NSString *jsonString = [BDPanConfigService getValueForArea:@"区域原始key" 
                                                       nodeKey:@"节点原始key" 
                                                      fieldKey:@"字段原始key"];
    return [self dictionaryFromJSONString:jsonString];
}
```

**数组类型实现模板:**
```objective-c
// [node_name值] [驼峰字段]
+ (NSArray *)方法名 {
    NSString *jsonString = [BDPanConfigService getValueForArea:@"区域原始key" 
                                                       nodeKey:@"节点原始key" 
                                                      fieldKey:@"字段原始key"];
    return [self arrayFromJSONString:jsonString];
}
```

**字符串类型实现模板:**
```objective-c
// [node_name值] [驼峰字段]
+ (NSString *)方法名 {
    return [BDPanConfigService getValueForArea:@"区域原始key" 
                                       nodeKey:@"节点原始key" 
                                      fieldKey:@"字段原始key"];
}
```

**数字类型实现模板:**
```objective-c
// [node_name值] [驼峰字段]
+ (NSInteger)方法名 {
    NSString *value = [BDPanConfigService getValueForArea:@"区域原始key" 
                                                  nodeKey:@"节点原始key" 
                                                 fieldKey:@"字段原始key"];
    return [value integerValue];
}
```

---

### 第七步: 完整实现文件结构

```objective-c
#import "BDPanAmisConfig.h"
@import BDPanConfigService;

@implementation BDPanAmisConfig

#pragma mark - Private Helper Methods

+ (NSDictionary *)dictionaryFromJSONString:(NSString *)jsonString {
    if (!jsonString || jsonString.length == 0) {
        return @{};
    }
    NSData *data = [jsonString dataUsingEncoding:NSUTF8StringEncoding];
    NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
    return dict ?: @{};
}

+ (NSArray *)arrayFromJSONString:(NSString *)jsonString {
    if (!jsonString || jsonString.length == 0) {
        return @[];
    }
    NSData *data = [jsonString dataUsingEncoding:NSUTF8StringEncoding];
    NSArray *array = [NSJSONSerialization JSONObjectWithData:data options:0 error:nil];
    return array ?: @[];
}

#pragma mark - Public Configuration Methods


// [第一个区域的原始key]
// [方法注释]
+ (返回类型)方法名 {
    // 使用BDPanConfigService动态读取配置
    // 参数使用: 区域原始key, 节点原始key, 字段原始key
}

@end
```

---

### 第八步: 具体示例说明

**假设有如下JSON数据片段:**
```json
{
  "tool_sug_area": {
    "cfg_list": [{
      "node_key": "toolsug_mapper",
      "node_name": "工具推荐映射",
      "category_mapper_value": "{\"picture_tool\": \"0\"}"
    }]
  }
}
```

**应该生成:**
```objective-c
// tool_sug_area
// 工具推荐映射 categoryMapperValue
+ (NSDictionary *)toolSugArea_toolsugMapper_categoryMapperValue {
    NSString *jsonString = [BDPanConfigService getValueForArea:@"tool_sug_area" 
                                                       nodeKey:@"toolsug_mapper" 
                                                      fieldKey:@"category_mapper_value"];
    return [self dictionaryFromJSONString:jsonString];
}
```

**关键点:**
- 区域原始key: `"tool_sug_area"` (保持下划线格式)
- 节点原始key: `"toolsug_mapper"` (保持下划线格式)
- 字段原始key: `"category_mapper_value"` (保持下划线格式)
- 方法名: `toolSugArea_toolsugMapper_categoryMapperValue` (驼峰格式)

---

### 关键规则总结

**必须遵守:**
1. **所有配置值通过BDPanConfigService动态读取,绝对不能硬编码JSON字符串或具体值**
2. 配置服务的参数使用原始key(保持下划线格式),不转换为驼峰
3. 方法名使用驼峰格式,但配置读取使用原始key
4. 区域注释使用原始英文key
5. 方法注释格式: `node_name值` + `空格` + `驼峰字段`
6. `node_name`和`cfg_version`不生成方法
7. 字典和数组转换统一调用公共辅助方法
8. 数字类型需要调用`integerValue`转换

**绝对禁止:**
1. **禁止硬编码任何JSON字符串值在代码中**
2. **禁止直接return具体的业务数据**
3. 禁止在提示词中包含具体业务参数

---

### 配置服务API说明

假设BDPanConfigService提供以下方法:
```objective-c
// 获取配置值
+ (NSString *)getValueForArea:(NSString *)areaKey 
                      nodeKey:(NSString *)nodeKey 
                     fieldKey:(NSString *)fieldKey;
```

所有方法实现都应该通过此API动态获取配置值,而不是硬编码。

---
```
#### 演示视频
[附件]


# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
