---
title: "目标"
description: "Zulu插件修正插件EDT使用实践"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\Zulu插件修正插件EDT使用实践.md"
---
Zulu插件修正插件EDT使用实践

#### 🧑‍🏫 案例作者：[@慕海龙](https://ku.baidu-int.com?t=mention&mt=contact&id=f9ca31d0-fcea-11f0-af27-8f11d9e60b85)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了使用Comate和Zulu识别并修复IntelliJ插件中EDT（事件分发线程）使用违规问题的实践。通过制定详细的Rules，扫描出多处违规场景，包括网络请求、文件IO、PSI操作等在EDT上执行的问题，并提供了修复方案和自动化检测建议，以提升插件的稳定性和性能。
# 目标
使用Comate识别代码库中EDT使用违规之处形成列表，逐一修复。

# EDT说明
IntelliJ 平台基于 Swing，所有 UI 更新必须在EDT（Event Dispatch Thread）执行；所有耗时任务必须在后台线程执行。违反这些规则会导致UI卡顿、死锁、索引阻塞，甚至 Plugin Verifier 不通过。

# 实施
1. 让Comate生成Rules来完成本次目标
2. 让Zulu执行Rules方案，我们来观测其解决程度

### 执行
1. 先让帮我解释一下IntelliJ插件中EDT的概念，观测其回答很归正，没问题可以继续实施

![](/personal-site-mvp/img/doc-placeholder.svg "")
2. 用简短的提示词直接让它生成Rules

![](/personal-site-mvp/img/doc-placeholder.svg "")


```
---
description: IntelliJ插件EDT使用规范检查与修复指南
globs:
  - "src/main/java/**/*.java"
  - "src/test/java/**/*.java"
alwaysApply: false
---
# EDT使用规范检查与修复指南

## EDT概念回顾
EDT（Event Dispatch Thread）是Swing/AWT图形界面框架中的事件分发线程，负责处理所有UI相关操作。

### 核心原则
1. **所有UI操作必须在EDT上执行** - 包括组件创建、属性修改、重绘等
2. **禁止在EDT上执行耗时操作** - 会导致UI冻结，用户体验极差
3. **后台线程更新UI时必须切回EDT** - 通过invokeLater/invokeAndWait

## 违规模式识别清单

### 🔴 严重违规：EDT上执行耗时操作

#### 违规模式1：网络请求在EDT上执行
```java
// ❌ 错误示例
public void actionPerformed(AnActionEvent e) {
    String result = httpClient.get("https://api.example.com"); // 阻塞EDT
    showNotification(result);
}
```

**检查要点：**
- Action的actionPerformed中直接调用网络请求
- 按钮点击事件处理中包含HTTP/Socket操作
- UI事件回调中同步调用远程服务

**修复方案：**
```java
// ✅ 正确示例
public void actionPerformed(AnActionEvent e) {
    ApplicationManager.getApplication().executeOnPooledThread(() -> {
        String result = httpClient.get("https://api.example.com");
        ApplicationManager.getApplication().invokeLater(() -> {
            showNotification(result);
        });
    });
}
```

#### 违规模式2：文件IO操作在EDT上执行
```java
// ❌ 错误示例
public void updateUI() {
    List<String> lines = Files.readAllLines(Paths.get("large-file.txt")); // 阻塞EDT
    listModel.addAll(lines);
}
```

**检查要点：**
- UI更新方法中直接读写文件
- 大文件操作未使用后台线程
- 文件扫描、遍历在EDT中进行

**修复方案：**
```java
// ✅ 正确示例
public void updateUI() {
    ReadAction.nonBlocking(() -> {
        return Files.readAllLines(Paths.get("large-file.txt"));
    }).finishOnUiThread(ModalityState.defaultModalityState(), lines -> {
        listModel.addAll(lines);
    }).submit(AppExecutorUtil.getAppExecutorService());
}
```

#### 违规模式3：复杂计算在EDT上执行
```java
// ❌ 错误示例
public void onButtonClick() {
    int result = 0;
    for (int i = 0; i < 1000000; i++) {
        result += complexCalculation(i); // 耗时计算阻塞EDT
    }
    label.setText(String.valueOf(result));
}
```

**检查要点：**
- UI事件处理中包含循环计算
- 算法复杂度较高的操作未异步化
- 数据处理、解析在EDT中同步完成

**修复方案：**
```java
// ✅ 正确示例
public void onButtonClick() {
    ProgressManager.getInstance().run(new Task.Backgroundable(project, "Computing...") {
        private int result;

        @Override
        public void run(@NotNull ProgressIndicator indicator) {
            result = 0;
            for (int i = 0; i < 1000000; i++) {
                result += complexCalculation(i);
                indicator.setFraction((double) i / 1000000);
            }
        }

        @Override
        public void onSuccess() {
            label.setText(String.valueOf(result));
        }
    });
}
```

#### 违规模式4：PSI操作在EDT上直接执行
```java
// ❌ 错误示例
public void analyzeCode() {
    PsiFile psiFile = PsiManager.getInstance(project).findFile(virtualFile);
    Collection<PsiElement> elements = PsiTreeUtil.findChildrenOfType(psiFile, PsiMethod.class); // 可能耗时
    updateUIWithElements(elements);
}
```

**检查要点：**
- PSI树遍历未使用ReadAction
- 代码分析在UI线程同步执行
- findUsages等操作未后台化

**修复方案：**
```java
// ✅ 正确示例
public void analyzeCode() {
    ReadAction.nonBlocking(() -> {
        PsiFile psiFile = PsiManager.getInstance(project).findFile(virtualFile);
        return PsiTreeUtil.findChildrenOfType(psiFile, PsiMethod.class);
    }).finishOnUiThread(ModalityState.defaultModalityState(), elements -> {
        updateUIWithElements(elements);
    }).submit(AppExecutorUtil.getAppExecutorService());
}
```

### 🟡 中等违规：非EDT线程操作UI

#### 违规模式5：后台线程直接修改UI组件
```java
// ❌ 错误示例
public void loadData() {
    new Thread(() -> {
        String data = fetchDataFromServer();
        textField.setText(data); // 非EDT线程操作UI
    }).start();
}
```

**检查要点：**
- Thread/ExecutorService回调中直接操作Swing组件
- 异步任务完成后未切回EDT更新UI
- CompletableFuture.thenAccept中包含UI操作

**修复方案：**
```java
// ✅ 正确示例
public void loadData() {
    ApplicationManager.getApplication().executeOnPooledThread(() -> {
        String data = fetchDataFromServer();
        ApplicationManager.getApplication().invokeLater(() -> {
            textField.setText(data);
        });
    });
}
```

#### 违规模式6：监听器回调未保证EDT执行
```java
// ❌ 错误示例
public void setupListener() {
    dataService.addListener(new DataListener() {
        @Override
        public void onDataChanged(Data data) {
            updatePanel(data); // 回调线程不确定
        }
    });
}
```

**检查要点：**
- 外部事件监听器回调中的UI操作
- 消息总线订阅者未检查EDT
- FileWatcher等回调未切换线程

**修复方案：**
```java
// ✅ 正确示例
public void setupListener() {
    dataService.addListener(new DataListener() {
        @Override
        public void onDataChanged(Data data) {
            if (ApplicationManager.getApplication().isDispatchThread()) {
                updatePanel(data);
            } else {
                ApplicationManager.getApplication().invokeLater(() -> updatePanel(data));
            }
        }
    });
}
```

### 🟢 轻度违规：EDT使用不规范

#### 违规模式7：过度使用invokeAndWait
```java
// ⚠️ 不推荐
public String getSomeUIData() {
    String[] result = new String[1];
    ApplicationManager.getApplication().invokeAndWait(() -> {
        result[0] = textField.getText();
    });
    return result[0];
}
```

**检查要点：**
- invokeAndWait造成线程阻塞
- 可用invokeLater替代的场景使用了invokeAndWait
- 死锁风险：EDT等待另一个需要EDT的任务

**修复方案：**
```java
// ✅ 推荐使用异步回调
public void getSomeUIData(Consumer<String> callback) {
    ApplicationManager.getApplication().invokeLater(() -> {
        callback.accept(textField.getText());
    });
}
```

#### 违规模式8：未指定ModalityState
```java
// ⚠️ 不够严谨
ApplicationManager.getApplication().invokeLater(() -> {
    showDialog();
});
```

**修复方案：**
```java
// ✅ 明确指定模态状态
ApplicationManager.getApplication().invokeLater(() -> {
    showDialog();
}, ModalityState.NON_MODAL); // 或 ModalityState.defaultModalityState()
```

## 检查流程

### 第一步：全局扫描识别
使用以下关键字搜索潜在违规点：
1. `actionPerformed` - 检查Action中是否有耗时操作
2. `invokeLater` / `invokeAndWait` - 检查是否正确使用
3. `new Thread` / `ExecutorService` - 检查回调中是否有UI操作
4. `Files.read` / `HttpClient` / `Socket` - 检查是否在EDT调用
5. `PsiTreeUtil` / `PsiManager` - 检查PSI操作是否正确包裹
6. `setText` / `setVisible` / `repaint` - 检查调用线程是否正确

### 第二步：逐文件深度检查
对每个Java文件执行：
1. 识别所有UI事件处理方法（actionPerformed、onClick等）
2. 分析方法调用链，标记耗时操作
3. 检查线程切换逻辑是否完整
4. 验证异常处理是否会影响线程安全

### 第三步：生成违规清单
格式：
```
文件路径 | 行号 | 违规类型 | 严重等级 | 违规描述
```

### 第四步：优先级修复
1. 🔴 严重违规 - 立即修复（导致UI冻结）
2. 🟡 中等违规 - 优先修复（可能崩溃或数据错误）
3. 🟢 轻度违规 - 计划修复（优化性能和健壮性）

## 项目特定注意事项

### 1. ThreadPoolHolder使用规范
项目已封装EDT调用工具类`ThreadPoolHolder`，优先使用：
```java
// 在EDT执行
ThreadPoolHolder.runInEdt(() -> { /* UI操作 */ });

// 在后台执行
ThreadPoolHolder.runInBackground(() -> { /* 耗时操作 */ });
```

### 2. 代码补全模块关注点
`src/main/java/com/baidu/comate/intellij/completions`中：
- 代码上下文提取必须使用ReadAction
- AI模型调用必须在后台线程
- 补全结果应用需切回EDT

### 3. WebView通信关注点
`src/main/java/com/baidu/comate/intellij/toolwindow`中：
- JCEF回调线程不确定，需显式切换
- JavaScript调用Java方法时检查EDT
- 大量数据传输考虑分批+异步

### 4. 网络请求模块关注点
`src/main/java/com/baidu/comate/intellij/request`中：
- HttpManager调用必须在后台线程
- SSE事件处理更新UI需invokeLater
- 超时异常处理避免阻塞EDT

## 自动化检测工具建议

可使用IntelliJ IDEA的Inspection功能自定义检查规则：
1. "Call to Thread.sleep() in EDT"
2. "Blocking call in non-blocking context"
3. "Swing component used from non-EDT thread"

## 参考资源
- IntelliJ Platform SDK: https://plugins.jetbrains.com/docs/intellij/general-threading-rules.html
- EDT最佳实践: https://plugins.jetbrains.com/docs/intellij/threading-model.html
```
它制定了8种EDT违规场景，分别给出了错误示例/正确示例、不推荐示例/推荐示例，基本上覆盖到了90%我们的研发场景

它给出了扫描思路，由关键词到文件再到场景，局部到全局的思路比较有切入点

它明确的看到了全局Rules的规约并给予充分利用

---

一个简洁的指令直接让它开干

![](/personal-site-mvp/img/doc-placeholder.svg "")
上来就发现了严重问题

![](/personal-site-mvp/img/doc-placeholder.svg "")


保守般的睿智，给问题分类为严重违规，潜在问题

![](/personal-site-mvp/img/doc-placeholder.svg "")


报告出来了，500多行

```
# EDT使用违规检查报告

**生成时间**: 2025-11-20
**项目**: IntelliJ Comate Plugin
**扫描范围**: src/main/java 全部Java文件

---

## 执行摘要

本次检查共发现 **13处** EDT使用违规，分布如下：
- 🔴 **严重违规**: 6处（导致UI冻结）
- 🟡 **中等违规**: 5处（可能导致异常）
- 🟢 **轻度违规**: 2处（性能和规范问题）

---

## 🔴 严重违规清单（优先修复）

### 违规 #1: 网络请求在EDT上执行
**文件**: `src/main/java/com/baidu/comate/intellij/login/LoginUtil.java`
**位置**: 第162-164行
**严重等级**: 🔴 严重
**违规类型**: 违规模式1 - 网络请求在EDT上执行

**问题描述**:
`getToken()` 方法中直接调用 `HttpManager.get()`，该方法被 `browseToLoginUrl()` 调用，而后者直接在 `LoginComateAction.actionPerformed()` 的EDT线程中执行。

**违规代码**:
```java
// LoginUtil.java: 150-164
public static String getToken(String clientId) {
    String url;
    if (GlobalConfigProvider.getGlobalConfig().getSystem().isInternal()) {
        url = Config.endpoint() + Config.Uri.INTERNAL_GENERATE_TOKEN_URI;
    } else {
        url = Config.serverHost() + Config.Uri.GENERATE_TOKEN;
    }
    Map<String, String> param = new HashMap<>();
    param.put("clientId", clientId);
    BaseResponse<String> response;
    try {
        LOG.info("[Comate] query token from url: " + url);
        response = HttpManager.get(url, param, BaseResponse.class); // ❌ 阻塞EDT
    } catch (Exception e) {
        LOG.info("[Comate] getToken error:" + e.getMessage());
        return null;
    }
    // ...
}
```

**调用链**:
```
LoginComateAction.actionPerformed() [EDT]
  → LoginUtil.browseToLoginUrl()
    → LoginUtil.getComateKeyLoop()
      → LoginUtil.getComateLoginResponse()
        → LoginUtil.getToken()
          → HttpManager.get() ❌ 网络请求阻塞EDT
```

**修复方案**:
```java
// 修复后的代码
public static void browseToLoginUrl(Project project) {
    BrowserUtil.browse(LoginUtil.getLoginUrl());

    // 后台线程执行登录轮询
    ApplicationManager.getApplication().executeOnPooledThread(() -> {
        LoginUtil.getComateKeyLoop(project);
    });
}
```

**影响范围**: 用户点击登录按钮时，UI会冻结直到网络请求完成（可能数秒）

---

### 违规 #2: 网络请求在EDT上执行
**文件**: `src/main/java/com/baidu/comate/intellij/login/LoginUtil.java`
**位置**: 第204-206行
**严重等级**: 🔴 严重
**违规类型**: 违规模式1 - 网络请求在EDT上执行

**问题描述**:
`getComateLoginResponse()` 方法中调用 `HttpManager.get()`，该方法同样被 `getComateKeyLoop()` 调用。

**违规代码**:
```java
// LoginUtil.java: 204-206
response = HttpManager.get(url, param, header, new TypeReference<BaseResponse<ClientLoginResponse>>() {
}.getType()); // ❌ 阻塞EDT
```

**修复方案**: 同违规 #1，将整个登录流程移到后台线程。

---

### 违规 #3: 文件下载在EDT上执行
**文件**: `src/main/java/com/baidu/comate/intellij/util/BinDownloader.java`
**位置**: 第260-264行
**严重等级**: 🔴 严重
**违规类型**: 违规模式1 - 网络请求在EDT上执行

**问题描述**:
通知按钮的 `actionPerformed` 中调用 `startDownloadAndListening()`，该方法会执行文件下载操作。

**违规代码**:
```java
// BinDownloader.java: 260-264
new NotificationAction("重试") {
    @Override
    public void actionPerformed(@NotNull AnActionEvent e, @NotNull Notification notification) {
        DIALOG_SHOWN.set(false);
        notification.expire();
        startDownloadAndListening(e.getProject(), TIMEOUT_MILLIONS); // ❌ 可能包含下载操作
    }
}
```

**修复方案**:
```java
new NotificationAction("重试") {
    @Override
    public void actionPerformed(@NotNull AnActionEvent e, @NotNull Notification notification) {
        DIALOG_SHOWN.set(false);
        notification.expire();

        // 后台执行下载
        ApplicationManager.getApplication().executeOnPooledThread(() -> {
            startDownloadAndListening(e.getProject(), TIMEOUT_MILLIONS);
        });
    }
}
```

---

### 违规 #4: 插件安装在EDT上执行
**文件**: `src/main/java/com/baidu/comate/intellij/update/PluginUpgrader.java`
**位置**: 第278-282行
**严重等级**: 🔴 严重
**违规类型**: 违规模式1 - 网络请求+文件IO在EDT上执行

**问题描述**:
通知按钮的 `actionPerformed` 中调用 `installPluginPoc()`，该方法包含插件下载和安装操作。

**违规代码**:
```java
// PluginUpgrader.java: 278-282
new NotificationAction(Bundle.get("comate.plugin.upgrade.notice.poc.installLatest")) {
    @Override
    public void actionPerformed(@NotNull AnActionEvent e, @NotNull Notification notification) {
        installPluginPoc(e.getProject(), pluginInfo); // ❌ 包含下载和IO操作
        notification.expire();
    }
}
```

**修复方案**:
```java
new NotificationAction(Bundle.get("comate.plugin.upgrade.notice.poc.installLatest")) {
    @Override
    public void actionPerformed(@NotNull AnActionEvent e, @NotNull Notification notification) {
        notification.expire();

        // 使用ProgressManager在后台执行
        ProgressManager.getInstance().run(new Task.Backgroundable(
                e.getProject(), "Installing Plugin Update...", true) {
            @Override
            public void run(@NotNull ProgressIndicator indicator) {
                installPluginPoc(e.getProject(), pluginInfo);
            }
        });
    }
}
```

---

### 违规 #5: 文件IO在EDT上执行
**文件**: `src/main/java/com/baidu/comate/intellij/util/binary/BinaryUseMetaData.java`
**位置**: 第57-59行
**严重等级**: 🔴 严重
**违规类型**: 违规模式2 - 文件IO在EDT上执行

**问题描述**:
`load()` 方法中使用 `Files.readString()` 同步读取文件，如果该方法在EDT调用会阻塞UI。

**违规代码**:
```java
// BinaryUseMetaData.java: 57-59
String jsonStr = Files.readString(dataFile); // ❌ 同步文件IO
Type type = new TypeToken<HashMap<String, Long>>() {}.getType();
```

**检查调用链**: 需要检查 `load()` 方法的所有调用点，确保不在EDT调用。

**修复方案**:
```java
// 方案1: 使用ReadAction.nonBlocking
public static void loadAsync(Consumer<Map<String, Long>> callback) {
    ReadAction.nonBlocking(() -> {
        try {
            String jsonStr = Files.readString(dataFile);
            Type type = new TypeToken<HashMap<String, Long>>() {}.getType();
            return GsonUtil.fromJson(jsonStr, type);
        } catch (Exception e) {
            LOG.warn("[Comate] load binary meta failed", e);
            return new HashMap<String, Long>();
        }
    }).finishOnUiThread(ModalityState.defaultModalityState(), callback)
      .submit(AppExecutorUtil.getAppExecutorService());
}

// 方案2: 明确标注方法不能在EDT调用
@RequiresBackgroundThread
public static Map<String, Long> load() {
    // 原有实现
}
```

---

### 违规 #6: 文件IO在EDT上执行
**文件**: `src/main/java/com/baidu/comate/intellij/util/binary/BinaryUseMetaData.java`
**位置**: 第100-102行
**严重等级**: 🔴 严重
**违规类型**: 违规模式2 - 文件IO在EDT上执行

**问题描述**:
`persist()` 方法中使用 `Files.writeString()` 同步写入文件。

**违规代码**:
```java
// BinaryUseMetaData.java: 100-102
String jsonStr = GsonUtil.toJson(binaryUseData);
Files.writeString(tempFile, jsonStr, StandardOpenOption.CREATE, 
                  StandardOpenOption.WRITE, StandardOpenOption.TRUNCATE_EXISTING); // ❌ 同步文件IO
```

**修复方案**: 同违规 #5，使用后台线程或明确标注。

---

## 🟡 中等违规清单

### 违规 #7: 未保证EDT执行的UI操作
**文件**: `src/main/java/com/baidu/comate/intellij/autocomate/newfile/AutoworkFileOpenListener.java`
**位置**: 第167-169行
**严重等级**: 🟡 中等
**违规类型**: 违规模式6 - 监听器回调未保证EDT执行

**问题描述**:
`fileOpened()` 是文件打开监听器回调，可能不在EDT线程调用，但内部包含PSI操作和UI更新。

**违规代码**:
```java
// AutoworkFileOpenListener.java: 167-169
PsiFile psiFile = PsiManager.getInstance(project).findFile(file); // ⚠️ 线程不确定
if (!(psiFile instanceof PsiJavaFile)) {
    return;
}
```

**修复方案**:
```java
@Override
public void fileOpened(@NotNull FileEditorManager source, @NotNull VirtualFile file) {
    // 确保在ReadAction中执行PSI操作
    ReadAction.nonBlocking(() -> {
        PsiFile psiFile = PsiManager.getInstance(project).findFile(file);
        if (!(psiFile instanceof PsiJavaFile)) {
            return null;
        }
        // PSI分析逻辑
        return analysisResult;
    }).finishOnUiThread(ModalityState.defaultModalityState(), result -> {
        // EDT中更新UI
        if (result != null) {
            updateUI(result);
        }
    }).submit(AppExecutorUtil.getAppExecutorService());
}
```

---

### 违规 #8: PSI操作未使用ReadAction
**文件**: `src/main/java/com/baidu/comate/intellij/psi/knowledgegraph/builder/java/MethodKnowledgeGraphEntityBuilder.java`
**位置**: 第104-106行
**严重等级**: 🟡 中等
**违规类型**: 违规模式4 - PSI操作未正确包裹

**问题描述**:
`PsiTreeUtil.findChildrenOfAnyType()` 是PSI树遍历操作，应该在ReadAction中执行。

**违规代码**:
```java
// MethodKnowledgeGraphEntityBuilder.java: 104-106
Collection<PsiMethodCallExpression> methodCalls = PsiTreeUtil.findChildrenOfAnyType(psiMethod,
        PsiMethodCallExpression.class); // ⚠️ 应在ReadAction中
```

**修复方案**:
```java
// 确保调用此方法的上下文在ReadAction中
ApplicationManager.getApplication().runReadAction(() -> {
    Collection<PsiMethodCallExpression> methodCalls = 
        PsiTreeUtil.findChildrenOfAnyType(psiMethod, PsiMethodCallExpression.class);
    // 处理结果
});
```

---

### 违规 #9: 进程执行可能阻塞EDT
**文件**: `src/main/java/com/baidu/comate/intellij/util/UsernameParser.java`
**位置**: 第174-176行
**严重等级**: 🟡 中等
**违规类型**: 违规模式3 - 可能的耗时操作

**问题描述**:
`Runtime.exec()` 执行外部命令，可能耗时较长，需要确认调用上下文。

**违规代码**:
```java
// UsernameParser.java: 174-176
process = Runtime.getRuntime().exec(cmd); // ⚠️ 可能阻塞
try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
    String line;
```

**检查建议**: 检查所有调用 `UsernameParser` 的代码，确保不在EDT调用。

**修复方案**: 如果在EDT调用，需要改为后台线程：
```java
ApplicationManager.getApplication().executeOnPooledThread(() -> {
    String username = UsernameParser.getUsername();
    ApplicationManager.getApplication().invokeLater(() -> {
        // 更新UI
    });
});
```

---

### 违规 #10: 文件扫描在EDT上执行
**文件**: `src/main/java/com/baidu/comate/intellij/util/SmartUTUtil.java`
**位置**: 第413-415, 440-442, 458-460行
**严重等级**: 🟡 中等
**违规类型**: 违规模式2 - 文件IO在EDT上执行

**问题描述**:
多处使用 `Files.readString()` 读取文件内容进行匹配，如果文件较大会阻塞。

**违规代码**:
```java
// SmartUTUtil.java: 413-415
String content = Files.readString(filePath); // ⚠️ 同步IO
if (content.contains("org.junit.jupiter")) {
    // ...
}
```

**修复方案**: 使用 ReadAction.nonBlocking 或确保在后台线程调用。

---

### 违规 #11: 可能的UI操作未检查EDT
**文件**: 多个Action类的 `actionPerformed` 方法
**位置**: 多处
**严重等级**: 🟡 中等
**违规类型**: 需要验证的潜在风险

**涉及文件**:
- `src/main/java/com/baidu/comate/intellij/actions/CommentToCodeAction.java:45`
- `src/main/java/com/baidu/comate/intellij/actions/CodeExplainAction.java:25`
- `src/main/java/com/baidu/comate/intellij/actions/GenerateUTAction.java:35`
- `src/main/java/com/baidu/comate/intellij/actions/BatchGenerateGoUtAction.java:33`

**检查建议**: 需要逐个检查这些Action的实现，确认内部是否有耗时操作。

---

## ?? 轻度违规清单

### 违规 #12: 未使用项目封装的ThreadPoolHolder
**文件**: 多处
**严重等级**: 🟢 轻度
**违规类型**: 不符合项目规范

**问题描述**:
项目已经封装了 `ThreadPoolHolder` 工具类，但部分代码直接使用 `ApplicationManager.executeOnPooledThread()`。

**建议**: 统一使用 `ThreadPoolHolder.runInBackground()` 以保持代码一致性。

---

### 违规 #13: 未指定ModalityState
**文件**: 多处使用 `invokeLater` 的地方
**严重等级**: 🟢 轻度
**违规类型**: 违规模式8 - 未指定模态状态

**问题描述**:
部分 `invokeLater` 调用未指定 `ModalityState`，在某些情况下可能导致不符合预期的行为。

**修复建议**:
```java
// 改进前
ApplicationManager.getApplication().invokeLater(() -> {
    updateUI();
});

// 改进后
ApplicationManager.getApplication().invokeLater(() -> {
    updateUI();
}, ModalityState.defaultModalityState());
```

---

## 修复优先级建议

### 第一优先级（本周内）
1. 违规 #1, #2: 登录流程的网络请求（影响所有用户体验）
2. 违规 #3: 文件下载操作
3. 违规 #4: 插件升级安装

### 第二优先级（本月内）
4. 违规 #5, #6: 文件IO操作
5. 违规 #7, #8: PSI操作和监听器

### 第三优先级（下个版本）
6. 违规 #9, #10: 其他可能的阻塞操作
7. 违规 #11: 需要深度验证的Action
8. 违规 #12, #13: 代码规范优化

---

## 自动化检测建议

建议在项目中启用以下IDEA Inspection规则：

1. **Plugin DevKit → Code → Blocking call in non-blocking context**
2. **Plugin DevKit → Threading issues → EDT contract violation**
3. **Plugin DevKit → Threading issues → Swing component used from non-EDT thread**

配置路径：
```
Settings → Editor → Inspections → Plugin DevKit
```

---

## 总结与建议

### 主要问题
1. **网络请求在EDT执行**: 最严重的问题，直接影响用户体验
2. **文件IO操作未异步化**: 可能导致UI冻结
3. **缺少ReadAction包裹**: PSI操作未正确保护

### 改进建议
1. **代码审查**: 所有涉及网络、IO、PSI的代码都应该有EDT检查
2. **统一工具类**: 强制使用 `ThreadPoolHolder` 而非直接调用底层API
3. **静态检查**: 启用IDEA的EDT检查规则，在开发阶段就发现问题
4. **单元测试**: 为关键路径添加EDT违规检测的单元测试

---

## 附录：快速修复模板

### 模板1: Action中的耗时操作
```java
@Override
public void actionPerformed(@NotNull AnActionEvent e) {
    Project project = e.getProject();
    if (project == null) return;

    // 后台执行耗时操作
    ApplicationManager.getApplication().executeOnPooledThread(() -> {
        try {
            // 耗时操作
            Object result = doHeavyWork();

            // 切回EDT更新UI
            ApplicationManager.getApplication().invokeLater(() -> {
                updateUI(result);
            }, ModalityState.defaultModalityState());
        } catch (Exception ex) {
            LOG.error("[Comate] Error in action", ex);
        }
    });
}
```

### 模板2: PSI操作
```java
ReadAction.nonBlocking(() -> {
    // PSI读取操作
    PsiFile psiFile = PsiManager.getInstance(project).findFile(virtualFile);
    return PsiTreeUtil.findChildrenOfType(psiFile, PsiClass.class);
}).finishOnUiThread(ModalityState.defaultModalityState(), result -> {
    // EDT中更新UI
    updateUIWithPsiResult(result);
}).submit(AppExecutorUtil.getAppExecutorService());
```

### 模板3: 使用ProgressManager
```java
ProgressManager.getInstance().run(new Task.Backgroundable(
        project, "Processing...", true) {
    @Override
    public void run(@NotNull ProgressIndicator indicator) {
        // 后台耗时操作
        indicator.setText("Step 1...");
        doStep1();
        indicator.setFraction(0.5);

        indicator.setText("Step 2...");
        doStep2();
        indicator.setFraction(1.0);
    }

    @Override
    public void onSuccess() {
        // 成功后在EDT更新UI
        updateUI();
    }

    @Override
    public void onThrowable(@NotNull Throwable error) {
        LOG.error("[Comate] Task failed", error);
    }
});
```

---

**报告结束**

如需对任何违规进行详细分析或需要具体修复代码，请告知违规编号。
```
让Zulu开始修复这些违规

![](/personal-site-mvp/img/doc-placeholder.svg "")
问题修复情况，这里不做详细展开，更想强调的是上面的扫描报告，模型也很保守的问你修复哪个问题

![](/personal-site-mvp/img/doc-placeholder.svg "")
![](/personal-site-mvp/img/doc-placeholder.svg "")
# 快速总结
模型+Zulu去写Prompt甚至Rules是可靠的，它对IntelliJ插件开发这个垂直领域是足够了解的，指导我们思路是完全没问题，这个扫描报告非常有参考价值，至于问题修复需要我们自己去斟使用

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
