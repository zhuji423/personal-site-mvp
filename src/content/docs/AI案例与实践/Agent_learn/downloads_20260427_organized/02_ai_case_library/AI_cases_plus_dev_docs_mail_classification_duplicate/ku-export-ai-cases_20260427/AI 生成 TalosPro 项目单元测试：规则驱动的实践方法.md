---
title: "Talospro 项目单元测试最佳实践"
description: "AI 生成 TalosPro 项目单元测试：规则驱动的实践方法"
date: "2026-04-28"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\02_ai_case_library\\AI_cases_plus_dev_docs_mail_classification_duplicate\\ku-export-ai-cases_20260427\\AI 生成 TalosPro 项目单元测试：规则驱动的实践方法.md"
---
AI 生成 TalosPro 项目单元测试：规则驱动的实践方法

#### 🧑‍🏫 案例作者：[@柴延晨](https://ku.baidu-int.com?t=mention&mt=contact&id=422c2e80-f2cb-11f0-80f0-91056ee5134c)
#### 🎬 案例分类：开发、测试
#### 🔧 使用工具：Comate
#### 📒 案例概要：规则驱动的AI单元测试生成方法，成功解决了在TalosPro等强运行时依赖前端框架中单元测试的痛点。核心转变是从直接让AI写测试转为先设计测试规则，AI在规则约束下生成、修复和演进测试代码。通过三阶段迭代流程（规则设计→AI生成修复→规则优化），最终形成可复用的完整测试规范。实践表明，该方法能在1小时内实现80%+的行覆盖率，显著降低了mock成本和维护难度。更重要的是，该方法建立了一种可持续的工程化范式——AI测试能力的上限取决于规则质量而非prompt技巧，使得AI能够真正融入复杂项目的测试体系。虽然示例基于TalosPro，但该方法论可适配各种强运行时依赖的前端框架。

## 一、背景与问题
在 TalosPro 这类 **强运行时依赖** 的前端框架中，单元测试长期存在以下痛点：

* 依赖大量框架注入能力（San / TalosPro / JS API / Worklet）
* Node 环境与真实运行时存在显著差异
* 人工补齐 mock 成本高、维护难
* AI 虽然“会写测试”，但**不懂项目约束**，产出不稳定

**核心问题不是“怎么写单测”，而是：**

> 👉 如何让 AI 在一个复杂业务框架中，**稳定、可重复、低成本地生成可运行的单元测试？**


---

## 二、整体思路：从“写测试”到“设计规则”
本方案的核心转变是：

> 
> **不直接让 AI 写单测，而是先设计一套「单元测试规则（rules）」**，
> 再让 AI 在规则约束下生成、修复、演进测试代码。
> 
整体流程分为三步：

1. **人工定义初版 rules**（框架、结构、mock、基本规范）
2. **AI 批量生成 + 自我修复测试**，并记录遇到的问题
3. **基于问题反向迭代 rules**，形成可复用的最终规范

这是一套 **规则驱动（Rules-driven）** 的 AI 测试生产流程。



---

## 三、阶段一：调研并编写初版 rules
### 3.1 测试框架选型
* 单元测试框架：**Vitest**
* 目标环境：Node（不依赖真实运行时）
* 测试目标：
    * 覆盖整个 `src` 目录
    * 优先覆盖纯函数、computed、数据处理逻辑


### 3.2 初版 rules 的设计目标
初版 rules 只解决三件事：

1. **统一测试结构**（目录 / 配置 / 入口）
2. **抹平 TalosPro 与 Web API 的差异**（mock）
3. **给 AI 一个“最低正确性边界”**

> ⚠️ 初版 rules 不追求完整，只求“能跑 + 可迭代”
### 3.3 初版 rules 示例（节选）


```
---
description: 强制按照本规则生成单元测试代码
globs:
alwaysApply: false
---
# Talospro 项目单元测试最佳实践

## 注意事项

### 配置项
1. **配置文件**：项目应该在根目录生成`vitest.config.ts`配置文件
2. **单测风格**：保持单测文件隔离于项目`src`目录，应当在根目录生成`__tests__`文件夹，并将单测文件生成在此处
3. **测试范围**：测试文件的范围，应该包含整个`src`目录，优先保证纯函数校验
4. **setup**：规则提供了setup最佳实践，请严格按照它配置测试环境、初始化测试状态，添加 talospro 全局配置

### 测试用例
1. **测试隔离**：确保测试之间相互独立
2. **组件清理**：每个测试后调用 `component.dispose()` 避免内存泄漏
3. **Mock 清理**：在 `afterEach` 中清理所有 mock
4. **避免真实请求**：所有网络请求都应该被 mock
5. **测试完成**：首次完成所有测试用例后应当通过`pnpm test`校验，并修复非实际代码兼容导致的错误用例

## 参考资源

### 官方文档和最佳实践
- [Vitest 官方文档](https://vitest.dev/)
- [Vitest 最佳实践指南](https://vitest.dev/guide/best-practices.html)
- [Vitest API 参考](https://vitest.dev/api/)
- [Testing Library 最佳实践](https://testing-library.com/docs/guiding-principles)

## 基础配置

### 依赖安装
```json
{
  "devDependencies": {
    "vitest": "^1.0.0",
  }
}
```

### 配置文件 `vitest.config.ts`
```typescript
import { defineConfig } from 'vitest/config'

export default defineConfig({
    test: {
        globals: true,
        setupFiles: ['./__test__/setup.ts'],
        include: ['__test__/**/*.{test,spec}.{js,ts}'],
        coverage: {
            include: [
                'src/**/*',
            ],
            reporter: ['text', 'json', 'html'],
        }
    }
})
```

## 测试文件结构

### 目录布局
```
__test__/
├── components/
│   └── text/
│       ├── index.test.ts
├── pages/
│   └── home/
│       ├── root.test.ts
└── setup.ts
```

## talospro 组件测试模板

### setup

请按照如下 setup 配置测试环境、初始化测试状态，添加 talospro 全局配置

```ts
import { vi } from 'vitest';

class Component {
    constructor(options = {}) {
        this.data = {
            _data: options.data || {},
            get: function(key) {
                return this._data[key];
            },
            set: function(key, value) {
                this._data[key] = value;
            }
        };
        this.options = options;
    }
    initData() {
        return {};
    }
    attached() {}
    detached() {}
    dispose() {
        this.data._data = {};
    }
    nextTick() {
        return Promise.resolve();
    }
    fire() {}
}

global.san = {
    Component
};

vi.mock('san', () => ({
    default: {
        Component
    },
    Component
}));

vi.mock('@baidu/talos-pro', () => ({
    defineApp: vi.fn((config) => config),
    definePage: vi.fn((config) => config.render || config),
    default: {
        defineApp: vi.fn((config) => config),
        definePage: vi.fn((config) => config.render || config)
    }
}));

vi.mock('*.module.less', () => ({
    default: new Proxy({}, {
        get: (target, prop) => `mock-${String(prop)}`
    })
}));

afterEach(() => {
    vi.clearAllMocks();
});
```

## 常见测试场景

### 必测场景
- 组件初始化和销毁
- 数据绑定和更新  
- 事件处理
- 条件渲染
- 错误处理

## 测试脚本配置

```json
{
  "scripts": {
    "test": "vitest",
  }
}
```
```


---

## 四、阶段二：AI 批量生成单元测试 & 自我修复
### 4.1 生成测试的 Prompt 设计
```
参考#初版rules 为整个项目补充单元测试，要求：
1. 行覆盖率达到80%；
2. 完成单元测试文件编写后执行命令进行自测，如果有报错需要进行修复，最终保证所有测试用例无报错；
3. 修复单元测试错误的过程中将遇到的问题以及对应的解决办法记录到本地 # test-trouble.mdr中
```
这个 prompt 有三个关键点：

* **明确质量目标**（覆盖率）
* **要求 AI 自测并修复**（不是只生成代码）
* **强制输出“问题文档”**（为规则演进提供素材）

### 4.2 人工 Review 与定向纠偏
AI 完成后，人工只做两件事：

1. 检查明显错误或逻辑缺失的测试用例
2. 用“指问题”的方式让 AI 重写

示例：

```
# xxx.ts 中的单元测试逻辑有问题：
- 未覆盖 xxx 分支
- 对运行时方法做了错误断言
请修正并重新生成
```
---

## 五、阶段三：基于问题反向迭代 rules
### 5.1 test-trouble.mdr 的角色
`test-trouble.mdr` 并不是简单的错误记录，而是：

> **AI 在当前 rules 下“踩坑”的集合**
它回答的是一个关键问题：

> 在现有规则下，AI 最容易在哪些地方犯错？
### 5.2 规则迭代 Prompt
```
参考# test-trouble.mdr，对我的项目中的单元测试规范 # 初版rules 进行进一步补充和修改
```
人工只需做最后一步：

* 删除不可泛化的问题
* 保留能沉淀为长期规则的部分



---

## 六、最终产出：可复用的 TalosPro 单元测试完整规范
经过 2～3 轮迭代后，最终 rules 覆盖了：

* 核心原则
* 项目配置（Vitest / Coverage）
* 测试目录结构
* TalosPro 测试运行时适配（setup.ts）
* 组件 / 页面 / 工具函数测试模式
* 常见错误与解决方案
* 覆盖率策略与分层目标

这份 rules 可以直接复制到其他 TalosPro 项目中使用。



```
---
description: TalosPro项目单元测试完整规范与实践指南
globs:
alwaysApply: false
---
# TalosPro 项目单元测试规范与实践指南

## 目录

1. [核心原则](#核心原则)
2. [项目配置](#项目配置)
3. [测试文件结构](#测试文件结构)
4. [环境设置](#环境设置)
5. [测试类型与实践](#测试类型与实践)
6. [常见问题与解决方案](#常见问题与解决方案)
7. [最佳实践](#最佳实践)
8. [测试覆盖率要求](#测试覆盖率要求)

---

## 核心原则

1. **全面覆盖**: 测试应覆盖所有组件、页面和功能模块，行覆盖率目标80%以上
2. **独立性**: 每个测试用例应该独立运行，不依赖其他测试的状态
3. **可维护性**: 测试代码应易于理解和维护，使用清晰的命名和结构
4. **快速反馈**: 测试应该快速运行，提供即时反馈
5. **模拟依赖**: 所有外部依赖应被正确模拟，确保测试的隔离性
6. **实用主义**: 根据实际情况调整测试策略，重点关注核心功能和业务逻辑

---

## 项目配置

### 依赖安装
```json
{
  "devDependencies": {
    "vitest": "^1.0.0",
    "@vitest/coverage-v8": "^1.0.0"
  },
  "scripts": {
    "test": "vitest",
    "test:coverage": "vitest run --coverage"
  }
}
```

### 配置文件 `vitest.config.ts`
```typescript
import { defineConfig } from 'vitest/config'

export default defineConfig({
    test: {
        globals: true,
        setupFiles: ['./__test__/setup.ts'],
        include: ['__test__/**/*.{test,spec}.{js,ts}'],
        coverage: {
            provider: 'v8',
            include: [
                'src/**/*',
            ],
            exclude: [
                'src/**/*.d.ts',           // 排除类型声明文件
                'src/**/*.module.less',    // 排除样式文件
                'src/pages/*/root.ts',     // 排除复杂的页面根组件
            ],
            reporter: ['text', 'json', 'html'],
            // 设置覆盖率阈值（根据实际情况调整）
            thresholds: {
                statements: 80,   // 语句覆盖率
                branches: 70,     // 分支覆盖率
                functions: 80,    // 函数覆盖率
                lines: 80         // 行覆盖率
            }
        }
    }
})
```

**配置说明**：
- `exclude` 字段排除了不需要测试的文件类型
- 覆盖率阈值设置为80%是一个合理的目标，既能保证代码质量，又不会过于苛刻
- 对于复杂的页面根组件（如包含大量运行时依赖的），可以考虑排除以提高测试效率

## 测试文件结构

### 目录布局
```
__test__/
├── components/                  # 组件测试
│   ├── component-name/
│   │   └── index.test.ts        # 组件测试文件
├── pages/                       # 页面测试
│   ├── page-name/
│   │   ├── index.test.ts        # 页面入口测试
│   │   └── root.test.ts         # 页面根组件测试
├── src/                         # 源码目录测试
│   └── index.test.ts            # 主入口文件测试
└── setup.ts                     # 测试环境配置文件
```

## 环境设置

### setup.ts 配置
必须创建并配置`__test__/setup.ts`文件，用于初始化测试环境：

```typescript
import { vi } from 'vitest';

// 模拟 San 组件基类
class Component {
    constructor(options = {}) {
        this.data = {
            _data: options.data || {},
            get: function(key) {
                if (key === undefined) return this._data;
                return key.includes('.') 
                    ? key.split('.').reduce((obj, k) => obj && obj[k], this._data)
                    : this._data[key];
            },
            set: function(key, value) {
                if (key.includes('.')) {
                    const parts = key.split('.');
                    const lastKey = parts.pop();
                    const obj = parts.reduce((o, k) => {
                        if (!o[k]) o[k] = {};
                        return o[k];
                    }, this._data);
                    obj[lastKey] = value;
                } else {
                    this._data[key] = value;
                }
            }
        };
        this.options = options;
    }
    initData() {
        return {};
    }
    attached() {}
    detached() {}
    dispose() {
        this.data._data = {};
    }
    nextTick() {
        return Promise.resolve();
    }
    fire() {}
    ref(name) { return null; }
}

// 全局模拟
global.san = {
    Component
};

// 模拟 San
vi.mock('san', () => ({
    default: {
        Component
    },
    Component
}));

// 模拟 TalosPro 框架
vi.mock('@baidu/talos-pro', () => ({
    defineApp: vi.fn((config) => config),
    definePage: vi.fn((config) => config.render || config),
    injectPage: vi.fn(() => (target) => target),
    default: {
        defineApp: vi.fn((config) => config),
        definePage: vi.fn((config) => config.render || config),
        injectPage: vi.fn(() => (target) => target)
    }
}));

// 模拟 TalosPro JS API（包含 Platform 信息）
vi.mock('@baidu/talos-pro-js', () => ({
    callNative: vi.fn(),
    invokeScheme: vi.fn(),
    Platform: {
        OS: 'ios',
        hostVersion: '1.5.0.0'  // 重要：必须提供版本号
    },
    localStorage: {
        getItem: vi.fn(),
        setItem: vi.fn(),
        removeItem: vi.fn()
    }
}));

// 模拟外部组件库
vi.mock('@baidu/talospro-component', () => ({
    EmptyPage: 'MockedEmptyPage',
    ErrorPage: 'MockedErrorPage',
    FeedItem: 'MockedFeedItem',
    LoadingPage: 'MockedLoadingPage',
    LoadMore: 'MockedLoadMore',
    MovieSwiper: 'MockedMovieSwiper'
}));

// 模拟样式文件
vi.mock('*.module.less', () => ({
    default: new Proxy({}, {
        get: (target, prop) => `mock-${String(prop)}`
    })
}));

// 模拟图片文件
vi.mock('*.png', () => ({ default: 'mocked-image-path' }));
vi.mock('*.jpg', () => ({ default: 'mocked-image-path' }));
vi.mock('*.gif', () => ({ default: 'mocked-image-path' }));

// 测试后清理
afterEach(() => {
    vi.clearAllMocks();
});
```

**重要提示**：
- `Platform.hostVersion` 必须提供，否则使用 `compareVersion` 的组件会报错
- 模拟对象应该在 `vi.mock` 内部直接创建，不要引用外部变量

## 测试类型与实践

### 1. 组件测试

#### 基本组件测试模板
```typescript
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import ComponentName from '../../../src/components/component-name/index';

describe('ComponentName', () => {
    let component;
    
    beforeEach(() => {
        // 在每个测试前创建新的组件实例
        component = new ComponentName();
    });
    
    afterEach(() => {
        // 在每个测试后清理组件
        component.dispose();
    });
    
    it('should initialize with default data', () => {
        // 验证组件初始化时的默认数据
        const data = component.data.get();
        expect(data).toHaveProperty('styles');
        // 验证其他预期的默认属性
    });
    
    it('should have correct template structure', () => {
        // 验证模板结构包含所有必要的元素
        const template = ComponentName.template;
        expect(template).toContain('expected-class-or-element');
    });
    
    // 其他测试用例...
});
```

#### 必须测试的方面
1. **初始化状态**：验证组件初始化时的默认数据和状态
2. **模板结构**：验证组件模板的DOM结构是否符合预期
3. **数据绑定**：验证数据变化是否正确反映在组件上
4. **事件处理**：验证组件能正确响应事件
5. **生命周期方法**：验证生命周期方法的正确执行
6. **边界情况**：验证组件在边界情况下的行为（如空数据、异常值等）

### 2. 页面测试

#### 页面入口文件测试
```typescript
import { describe, it, expect, vi } from 'vitest';
import PageIndex from '../../../src/pages/page-name/index';
import RootComponent from '../../../src/pages/page-name/root';

// 模拟 RootComponent
vi.mock('../../../src/pages/page-name/root', () => ({
    default: 'MockedRootComponent'
}));

describe('Page Index', () => {
    it('should export the result of definePage', () => {
        expect(PageIndex).toBeDefined();
    });
    
    it('should pass RootComponent as render prop', () => {
        expect(PageIndex.render).toBe('MockedRootComponent');
    });
    
    it('should have all required lifecycle methods', () => {
        expect(PageIndex).toHaveProperty('onBeforeRender');
        expect(PageIndex).toHaveProperty('onLoad');
        expect(PageIndex).toHaveProperty('onShow');
        // 验证其他生命周期方法
    });
    
    // 其他测试用例...
});
```

#### 页面根组件测试
遵循组件测试的模式，但需额外测试页面特有的功能：
1. **页面路由**：测试页面路由和导航功能
2. **页面状态管理**：测试页面状态的正确管理
3. **页面交互**：测试页面级别的用户交互

### 3. 特殊场景测试

#### 处理异步操作
```typescript
it('should handle async operations correctly', async () => {
    // 模拟异步操作
    const mockPromise = Promise.resolve({ data: 'success' });
    someAsyncFunction.mockResolvedValue(mockPromise);
    
    // 触发包含异步操作的方法
    component.handleAsyncOperation();
    
    // 等待异步操作完成
    await mockPromise;
    
    // 验证结果
    expect(component.data.get('result')).toBe('success');
});
```

#### 测试Worklet相关代码
```typescript
it('should handle worklet correctly', () => {
    // 模拟worklet对象
    const mockWorklet = {
        __addEventListener: vi.fn((pageId, targetId, eventName, handler) => {
            // 存储事件处理函数
            mockWorklet.eventHandler = handler;
        }),
        __updateElementStyles: vi.fn(),
        eventHandler: null
    };
    
    // 替换全局worklet
    const originalWorklet = global.worklet;
    global.worklet = mockWorklet;
    
    // 调用初始化方法
    component.initWorklet();
    
    // 验证worklet方法被调用
    expect(mockWorklet.__addEventListener).toHaveBeenCalled();
    
    // 手动调用事件处理函数
    const mockEvent = { /* 模拟事件对象 */ };
    mockWorklet.eventHandler(mockEvent);
    
    // 验证样式更新被调用
    expect(mockWorklet.__updateElementStyles).toHaveBeenCalled();
    
    // 恢复原始worklet
    global.worklet = originalWorklet;
});
```

#### 模拟图片导入
```typescript
// 在测试文件顶部
vi.mock('../../../src/assets/img/image.png', () => ({
    default: 'mocked-image-path'
}));

it('should load images correctly', () => {
    expect(component.data.get('imageSrc')).toBe('mocked-image-path');
});
```

## 测试覆盖率要求

### 覆盖率目标

**推荐目标**（平衡质量与效率）：
- **行覆盖率**：80%以上
- **语句覆盖率**：80%以上
- **分支覆盖率**：70%以上
- **函数覆盖率**：根据实际情况，建议50%以上

**说明**：
- 100%覆盖率是理想状态，但在实际项目中可能难以达到
- 许多组件方法需要运行时环境（如 `dispatch`、`fire`、DOM操作等），在单元测试中难以完全模拟
- 应优先保证核心业务逻辑和工具函数的高覆盖率

### 覆盖率分层策略

1. **核心层（目标：90%+）**
   - 工具函数（utils/）
   - 常量定义（const.ts）
   - 存储逻辑（storage.ts）
   - 应用入口（index.ts）

2. **业务层（目标：80%+）**
   - 组件的 computed 属性
   - 组件的数据处理方法
   - 页面入口文件（index.ts）

3. **视图层（目标：60%+）**
   - 组件的生命周期方法
   - 事件处理方法
   - DOM 操作相关方法

### 提高覆盖率的策略

1. **组件测试重点**：
   - ✅ 测试 `initData` 方法和默认数据
   - ✅ 测试所有 `computed` 属性的各种分支
   - ✅ 测试模板结构包含关键元素
   - ✅ 测试数据变化和状态管理
   - ⚠️ 运行时方法（如 dispatch、fire）只验证存在性即可

2. **页面测试重点**：
   - ✅ 测试页面配置导出正确
   - ✅ 测试页面与根组件的连接
   - ⚠️ 复杂的页面根组件可考虑排除在覆盖率之外

3. **工具函数测试重点**：
   - ✅ 测试所有正常情况
   - ✅ 测试所有边界情况
   - ✅ 测试所有异常情况和错误处理
   - ✅ 测试异步操作的各种状态

4. **使用覆盖率报告定位问题**：
   ```bash
   # 生成详细的覆盖率报告
   pnpm test:coverage
   
   # 查看 coverage/index.html 找到未覆盖的代码行
   # 针对性地补充测试用例
   ```

## 模拟策略

### 外部依赖模拟
1. **模拟框架API**：模拟San和TalosPro框架API
2. **模拟资源导入**：模拟样式文件、图片等资源的导入
3. **模拟网络请求**：使用vi.mock模拟fetch、axios等网络请求
4. **模拟DOM API**：模拟window、document等全局对象和API

### 常用模拟技术
```typescript
// 模拟方法
const mockMethod = vi.fn();
component.someMethod = mockMethod;

// 模拟返回值
mockMethod.mockReturnValue('mock result');

// 模拟Promise
mockMethod.mockResolvedValue({ data: 'success' });
mockMethod.mockRejectedValue(new Error('failure'));

// 监视现有方法
const spy = vi.spyOn(component, 'someMethod');
```

## 常见问题与解决方案

### 问题1: 模拟变量初始化顺序错误

**症状**: `ReferenceError: Cannot access 'mockVariable' before initialization`

**原因**: 在 `vi.mock` 工厂函数中引用了外部变量

**❌ 错误示例**:
```typescript
const mockLocalStorage = { getItem: vi.fn() };
vi.mock('@baidu/talos-pro-js', () => ({
    localStorage: mockLocalStorage  // 错误！
}));
```

**✅ 正确做法**:
```typescript
// 直接在 vi.mock 内部创建
vi.mock('@baidu/talos-pro-js', () => ({
    localStorage: {
        getItem: vi.fn(),
        setItem: vi.fn()
    }
}));

// 在测试中使用
describe('Test', () => {
    let mockLocalStorage;
    beforeEach(async () => {
        const { localStorage } = await import('@baidu/talos-pro-js');
        mockLocalStorage = localStorage;
    });
});
```

### 问题2: 测试环境缺少 DOM API

**症状**: `ReferenceError: document is not defined`

**原因**: Vitest 默认运行在 Node 环境，没有 DOM API

**解决方案**: 避免直接使用 DOM API，使用模拟对象

```typescript
// ❌ 不推荐
beforeEach(() => {
    component.el = document.createElement('div');
});

// ✅ 推荐
beforeEach(() => {
    component.el = {};  // 使用简单对象模拟
    component.fire = vi.fn();  // 模拟方法
});
```

### 问题3: 组件 initData 返回空对象

**症状**: 测试断言 `expect(data).toHaveProperty('styles')` 失败

**原因**: 某些组件的 `initData` 方法返回空对象或没有该方法

**解决方案**: 不强制要求特定属性，只验证基本结构

```typescript
// ❌ 可能失败
it('should have styles', () => {
    const data = component.data.get();
    expect(data).toHaveProperty('styles');
});

// ✅ 更灵活
it('should have data object', () => {
    expect(component.data).toBeDefined();
});

it('should initialize correctly', () => {
    const initData = component.initData();
    expect(initData).toBeDefined();
    // 只在确定有该属性时才断言
    if (initData.styles) {
        expect(initData.styles).toBeDefined();
    }
});
```

### 问题4: Platform.hostVersion 未定义导致测试失败

**症状**: `TypeError: Cannot read properties of undefined (reading 'split')`

**原因**: 某些组件使用 `compareVersion(Platform.hostVersion, '1.4.0.0')` 进行版本比较

**解决方案**: 在 setup.ts 中为 Platform 提供完整的模拟

```typescript
vi.mock('@baidu/talos-pro-js', () => ({
    Platform: {
        OS: 'ios',
        hostVersion: '1.5.0.0'  // 必须提供！
    },
    // ... 其他模拟
}));
```

### 问题5: 组件方法依赖运行时环境

**症状**: `dispatch does not exist` 或类似错误

**原因**: 组件的某些方法（如 dispatch、fire）在运行时由框架注入

**解决方案**: 在测试中手动模拟这些方法

```typescript
beforeEach(() => {
    component = new Component();
    component.dispatch = vi.fn();  // 手动添加
    component.fire = vi.fn();
});

// 只验证方法被调用，不验证实现
it('should call dispatch', () => {
    component.someMethod();
    expect(component.dispatch).toHaveBeenCalled();
});
```

### 问题6: 异步测试不稳定

**症状**: 测试有时通过，有时失败

**原因**: 没有正确等待异步操作完成

**解决方案**: 使用 async/await 或 vi.useFakeTimers

```typescript
// ✅ 方案1: 使用 async/await
it('should handle async operation', async () => {
    const { asyncFn } = await import('@baidu/talos-pro-js');
    vi.mocked(asyncFn).mockResolvedValue('result');
    
    const result = await myAsyncFunction();
    
    expect(result).toBe('expected');
});

// ✅ 方案2: 使用 fake timers
it('should handle setTimeout', () => {
    vi.useFakeTimers();
    
    component.delayedAction();
    vi.advanceTimersByTime(1000);
    
    expect(component.data.get('completed')).toBe(true);
    
    vi.useRealTimers();
});
```

### 常见错误速查表

| 错误信息 | 可能原因 | 解决方案 |
|---------|---------|---------|
| `Cannot find module '@baidu/talos-pro'` | 缺少模拟 | 在 setup.ts 中添加 vi.mock |
| `Cannot access 'mockVar' before initialization` | 模拟变量顺序错误 | 在 vi.mock 内部直接创建对象 |
| `document is not defined` | 使用了 DOM API | 使用模拟对象替代 |
| `dispatch does not exist` | 方法依赖运行时 | 手动添加模拟方法 |
| `Cannot read properties of undefined` | 缺少必要的模拟属性 | 补充完整的模拟对象 |
| `expected {} to have property "styles"` | initData返回空对象 | 改为验证对象存在即可 |

### 测试失败排查流程

1. **查看错误信息** → 定位是哪个测试用例失败
2. **检查模拟对象** → 确认所有依赖都已正确模拟
3. **检查异步操作** → 确认使用了正确的异步处理方式
4. **查看组件实现** → 理解组件的实际行为
5. **简化测试** → 从最简单的断言开始，逐步添加
6. **查阅文档** → 参考 test-troubleshooting.mdr 获取更多解决方案

## 最佳实践

### 1. 测试文件组织原则

```
__test__/
├── setup.ts                    # 全局配置（必需）
├── src/
│   └── index.test.ts          # 应用入口
├── utils/                      # 工具函数（优先级高）
│   ├── const.test.ts
│   ├── index.test.ts
│   └── storage.test.ts
├── components/                 # 组件测试
│   └── component-name/
│       └── index.test.ts
└── pages/                      # 页面测试
    └── page-name/
        └── index.test.ts
```

### 2. 组件测试模板（推荐）

```typescript
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import Component from '../../../src/components/component-name/index';

describe('ComponentName Component', () => {
    let component;

    beforeEach(() => {
        component = new Component();
        // 模拟运行时方法
        component.dispatch = vi.fn();
        component.fire = vi.fn();
        component.el = {};  // 不使用 document
    });

    afterEach(() => {
        if (component && typeof component.dispose === 'function') {
            component.dispose();
        }
    });

    // 基础测试
    it('should create component instance', () => {
        expect(component).toBeDefined();
    });

    it('should have data object', () => {
        expect(component.data).toBeDefined();
    });

    it('should have correct template structure', () => {
        const template = Component.template;
        expect(template).toBeDefined();
        expect(typeof template).toBe('string');
        expect(template).toContain('expected-element');
    });

    // 测试 initData
    it('should initialize with correct data', () => {
        const initData = component.initData();
        expect(initData).toBeDefined();
        // 只在确定存在时才断言具体属性
    });

    // 测试 computed 属性的各种分支
    it('should compute property correctly', () => {
        component.data.set('someData', 'value');
        const result = Component.computed.someProperty.call(component);
        expect(result).toBe('expected');
    });

    // 测试事件处理（只验证调用）
    it('should handle event correctly', () => {
        component.handleClick();
        expect(component.fire).toHaveBeenCalled();
    });
});
```

### 3. 工具函数测试模板

```typescript
describe('Utility Function', () => {
    beforeEach(() => {
        vi.clearAllMocks();
    });

    // 正常情况
    it('should handle normal case', () => {
        const result = utilityFunction('input');
        expect(result).toBe('output');
    });

    // 边界情况
    it('should handle empty input', () => {
        const result = utilityFunction('');
        expect(result).toBe('default');
    });

    it('should handle null input', () => {
        const result = utilityFunction(null);
        expect(result).toBe('default');
    });

    // 异常情况
    it('should handle error gracefully', async () => {
        const mockFn = vi.fn().mockRejectedValue(new Error('test'));
        const result = await functionWithErrorHandling(mockFn);
        expect(result).toBe('fallback');
    });
});
```

### 4. 测试编写原则

1. **描述性测试名称**
   - ✅ `'should compute isSingle as true when watchHistory has one item'`
   - ❌ `'test1'`

2. **一个测试一个概念**
   - 每个 it 只测试一个功能点
   - 避免在一个测试中断言多个不相关的事情

3. **避免测试实现细节**
   - ✅ 测试行为：组件显示正确的内容
   - ❌ 测试实现：组件调用了内部的私有方法

4. **保持测试简单**
   - 测试代码应该比被测代码更简单
   - 避免在测试中使用复杂的逻辑

5. **测试应该快速**
   - 避免真实的网络请求和文件I/O
   - 使用模拟对象加速测试

6. **测试应该独立**
   - 每个测试用例独立运行
   - beforeEach 中初始化，afterEach 中清理

7. **优先级排序**
   - 高优先级：工具函数、核心业务逻辑
   - 中优先级：组件的 computed 和数据处理
   - 低优先级：事件处理、生命周期方法

### 5. 异步测试最佳实践

```typescript
// ✅ 推荐：使用 async/await
it('should handle async operation', async () => {
    const { asyncFn } = await import('@baidu/talos-pro-js');
    vi.mocked(asyncFn).mockResolvedValue('result');
    
    const result = await myAsyncFunction();
    expect(result).toBe('expected');
});

// ✅ 推荐：测试错误处理
it('should handle async error', async () => {
    const { asyncFn } = await import('@baidu/talos-pro-js');
    vi.mocked(asyncFn).mockRejectedValue(new Error('error'));
    
    const result = await myAsyncFunction();
    expect(result).toBe('fallback');
});

// ✅ 推荐：使用 fake timers 处理延时
it('should handle timeout', () => {
    vi.useFakeTimers();
    
    component.delayedAction();
    vi.advanceTimersByTime(1000);
    
    expect(component.data.get('done')).toBe(true);
    
    vi.useRealTimers();
});
```

### 6. 模拟对象的最佳实践

```typescript
// ✅ 在 setup.ts 中统一模拟外部依赖
vi.mock('@baidu/talos-pro-js', () => ({
    callNative: vi.fn(),
    invokeScheme: vi.fn(),
    Platform: { OS: 'ios', hostVersion: '1.5.0.0' }
}));

// ✅ 在测试中获取并配置模拟
describe('Test', () => {
    let mockInvokeScheme;

    beforeEach(async () => {
        vi.clearAllMocks();
        const { invokeScheme } = await import('@baidu/talos-pro-js');
        mockInvokeScheme = invokeScheme;
    });

    it('should call invokeScheme', async () => {
        vi.mocked(mockInvokeScheme).mockResolvedValue('result');
        // ... 测试逻辑
    });
});
```

### 7. 持续改进

- 定期review测试代码，重构重复的测试逻辑
- 遇到新问题时，更新 test-troubleshooting.mdr
- 保持测试代码与业务代码同步更新
- 团队内分享测试经验和最佳实践

## 参考资源

### 官方文档与指南
- [Vitest 官方文档](https://vitest.dev/)
- [Vitest 最佳实践指南](https://vitest.dev/guide/best-practices.html)
- [Vitest API 参考](https://vitest.dev/api/)
- [Testing Library 最佳实践](https://testing-library.com/docs/guiding-principles)

### 测试命令
```bash
# 运行所有测试
pnpm test

# 运行特定测试文件
pnpm test path/to/test/file.test.ts

# 生成覆盖率报告
pnpm test:coverage

# 监视模式
pnpm test --watch
```

## 测试流程图

```
开始测试 → 设置测试环境 → 创建组件实例 → 执行测试用例 → 验证结果 → 清理测试环境 → 结束测试
```

## 测试检查清单

### 基础测试（必须）
- [ ] ✅ 组件/函数能够正确实例化
- [ ] ✅ 模板结构包含关键元素
- [ ] ✅ 数据对象存在且可访问
- [ ] ✅ initData 方法返回正确的初始数据

### 业务逻辑测试（重点）
- [ ] ✅ 所有 computed 属性的各种分支情况
- [ ] ✅ 数据处理方法的正常、边界和异常情况
- [ ] ✅ 工具函数的各种输入输出组合
- [ ] ✅ 异步操作的成功和失败情况

### 交互测试（可选）
- [ ] ⚠️ 事件处理方法被正确调用（只验证调用，不验证实现）
- [ ] ⚠️ 生命周期方法存在（不强制测试运行时行为）
- [ ] ⚠️ 组件间的数据传递（如能模拟）

### 覆盖率目标
- [ ] ✅ 行覆盖率达到 80% 以上
- [ ] ✅ 分支覆盖率达到 70% 以上
- [ ] ✅ 核心工具函数达到 95% 以上

### 质量检查
- [ ] ✅ 所有测试用例命名清晰明确
- [ ] ✅ 没有被跳过的测试（.skip）
- [ ] ✅ 测试运行快速（< 2秒）
- [ ] ✅ 测试结果稳定可重复

### 文档完善
- [ ] ✅ 复杂测试场景有注释说明
- [ ] ✅ 遇到的问题记录在 test-troubleshooting.mdr
- [ ] ✅ 新的测试模式补充到本文档

---

## 参考文档

- [test-troubleshooting.mdr](.comate/rules/test-troubleshooting.mdr) - 详细的问题排查指南
- [Vitest 官方文档](https://vitest.dev/)
- [Vitest API 参考](https://vitest.dev/api/)

```


调用方式非常简单：

按照 #rules 给该项目补充单元测试

---

## 七、效果验证
在「梯子的影视频道」业务中实践：

* 单测覆盖范围：核心组件 + 页面 + 工具函数
* **行覆盖率：80%+**
* 全流程（规则 + 生成 + 修复 + 迭代）耗时约 **1 小时**

![](/personal-site-mvp/img/doc-placeholder.svg "")
---

## 八、经验总结与可持续演进
### 8.1 本方案解决了什么
* ❌ 不再手写大量模板化单测
* ❌ 不再反复补运行时 mock
* ❌ 不依赖某一个“懂测试的人”
* ✅ 单测生成可自动化
* ✅ 规则可持续演进
* ✅ AI 能逐渐“学会”项目约束

### 8.2 一个重要认知转变
> **AI 写单测的上限，取决于 rules 的质量，而不是 prompt 的花哨程度**
当规则足够清晰：

* AI 会写测试
* AI 会修测试
* AI 还能帮你改规则



---

## 九、适用范围
虽然示例基于 TalosPro，但该方法同样适用于：

* 小程序 / Hybrid 框架
* 内部低代码 / DSL 框架
* 任意“强运行时依赖 + Node 单测”的前端体系

只需要替换：

* setup.ts 的运行时适配层
* 覆盖率策略
* 页面测试模板



---

## 十、结语


这不是一套“怎么用 AI 写单测”的技巧，

而是一种：



> **把 AI 变成可被工程化管理的测试生产力的方法论**。


当测试规则成为第一公民，

AI 才真正能在复杂工程里稳定发挥价值。







# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI内容点击上方，即刻跳转
