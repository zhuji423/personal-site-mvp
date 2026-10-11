---
title: "一、背景"
description: "地图打车实战-AI+爱速搭：前端页面代码一键生成落地实践"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\地图打车实战-AI+爱速搭：前端页面代码一键生成落地实践.md"
---
地图打车实战-AI+爱速搭：前端页面代码一键生成落地实践

#### 🧑‍🏫 案例作者：[@王蒋煜](https://ku.baidu-int.com?t=mention&mt=contact&id=48ec63c0-fce4-11f0-9adc-e9b9869c3941)
#### 🎬 案例场景：开发
#### 🔧 使用工具：Comate
#### 📒 案例概要：本文介绍了在地图打车业务中，如何利用AI和爱速搭平台实现前端页面代码的一键生成。通过AI工具自动生成代码，提高了开发效率，减少了人工编写代码的工作量。文章详细描述了实现过程、技术路径及最佳实践，展示了AI在前端开发领域的巨大潜力。
# 一、背景
* 爱速搭平台要陆续下线，要对爱速搭页面进行本地 H5 转写， 但爱速搭页面较多，工作量较大；
* 爱速搭大部分页面的结构一致，故思考是否可以利用 AI 工具来做些处理；

# 二、目标
1、简单CRUD页面：全面实现AI自动化迁移；准确率要达 100%，多次生成结果一样。

2、复杂页面通过AI完成基础模块迁移；



# 三、DEMO演示
[附件]


# 四、最佳实践
## 4.0 格式处理
目前支持的功能项如下：以下这些功能项基本覆盖在每个页面中。





这里面以弹窗表单的部分进行举例。首先表单部分爱速搭的 JSON 代码如下，可以看到，表单的组成其实就只是 type, title, body,id, actions， 以及一些其他的默认配置。然后表单项则是 body.body的数组。



那么我们通过 AI 生成的思路就可以是，让 AI 去理解这个 JSON 结构，根据里面的属性去生成代码。比如如果定位到 type = dialog，那就调用表单的生成规则，表单的生成规则里面 title是表单标题，actions是表单的按钮。然后表单项则是在 body.body里面，识别到 input-text就表明是一个输入框，required就表明这个是必须的等等。



但是，可以看到，这里面的属性太多了，很多都是默认属性，因为要生成本地代码，这里的本地代码是我们自己开发的，与爱速搭的组件等都没有关系，而这里面很多属性其实并不需要展示出来，或者默认就是如此，加上这些属性，再加上 AI 生成结果的多样性，最后生成的内容可能会加很多不必要的内容。



因此，要先对爱速搭的 JSON 数据进行一遍处理

```
"dialog": {
                "type": "dialog",
                "title": "新增司机招募活动",
                "body": [
                    {
                        "type": "form",
                        "api": {
                            "method": "post",
                            "url": "${SERVER}/manage/recruit/task/create"
                        },
                        "body": [
                            {
                                "type": "input-text",
                                "name": "name",
                                "label": "活动名称",
                                "id": "u:2f76cf53ca88",
                                "required": true,
                                "size": "lg"
                            },
                            {
                                "type": "select",
                                "name": "open_city",
                                "label": "城市选择",
                                "size": "lg",
                                "required": true,
                                "id": "u:51a3948b3a5c",
                                "multiple": true,
                                "checkAll": true,
                                "defaultCheckAll": false,
                                "checkAllLabel": "全选",
                                "selectFirst": false,
                                "value": "",
                                "searchable": true,
                                "source": "${SERVER}/manage/aisuda/selectlist?req_type=city",
                                "joinValues": true,
                                "valuesNoWrap": false,
                                "className": "",
                                "placeholder": "请选择",
                                "inputClassName": "",
                                "mode": "inline",
                                "labelWidth": "var(--sizes-base-49)"
                            },
                            {
                                "type": "select",
                                "label": "车队",
                                "name": "fleet_id_list",
                                "id": "u:c7c683e320a5",
                                "multiple": true,
                                "required": true,
                                "checkAll": false,
                                "value": "",
                                "source": "${SERVER}/manage/task/fleetlist?req_type=fleet",
                                "clearable": true,
                                "searchable": true,
                                "placeholder": "请选择",
                                "joinValues": true,
                                "showInvalidMatch": false
                            },
                            {
                                "type": "select",
                                "label": "注册必传证件",
                                "name": "need_license",
                                "id": "u:8aea2a215272",
                                "multiple": true,
                                "size": "lg",
                                "required": true,
                                "checkAll": false,
                                "defaultCheckAll": false,
                                "checkAllLabel": "全选",
                                "selectFirst": false,
                                "value": "1",
                                "options": [
                                    {
                                        "label": "身份证",
                                        "value": 1,
                                        "disabled": true
                                    },
                                    {
                                        "label": "司机驾驶证",
                                        "value": 2
                                    },
                                    {
                                        "label": "司机行驶证",
                                        "value": 3
                                    },
                                    {
                                        "label": "网约车驾驶员证",
                                        "value": 4
                                    },
                                    {
                                        "label": "网约车运输证",
                                        "value": 5
                                    }
                                ]
                            }
                        ],
                        "id": "u:0121bd6e09ad",
                        "actions": [
                            {
                                "type": "submit",
                                "label": "提交",
                                "primary": true
                            }
                        ],
                        "feat": "Insert",
                        "dsType": "api",
                        "labelAlign": "left"
                    }
                ],
                "id": "u:60279c35acfe",
                "actions": [
                    {
                        "type": "button",
                        "actionType": "cancel",
                        "label": "取消",
                        "id": "u:1b8ffa8774ce"
                    },
                    {
                        "type": "button",
                        "actionType": "confirm",
                        "label": "确定",
                        "primary": true,
                        "id": "u:531a4bcbdbd4"
                    }
                ],
                "showCloseButton": true,
                "closeOnOutside": false,
                "closeOnEsc": false,
                "showErrorMsg": true,
                "showLoading": true,
                "draggable": false,
                "actionType": "dialog",
                "allowFullscreen": false
            },
```




处理完后是这样的，可以看到处理完成后的数据少了很多，只留下有意义的字段。这里的处理逻辑是这样的。

* 先写完页面代码，然后根据实际情况去做取舍。
* 表单的取消和提交按钮，基本上每个表单都有这两个按钮，极少的会自定义，如果要适配这方面，调试耗费的时间和精力较长，且直接改生成后的代码更容易。故把操作按钮这块直接固定写死在规则里面。
* 其他字段的删减也是按照以上的逻辑来的。

```
 "dialog": {
        "title": "新增司机招募活动",
        "form": {
          "initApi": "",
          "api": "${SERVER}/manage/recruit/task/create",
          "body": [
            {
              "type": "input-text",
              "label": "活动名称",
              "name": "name",
              "required": true
            },
            {
              "type": "multi-select",
              "label": "城市选择",
              "name": "open_city",
              "required": true,
              "options": []
            },
            {
              "type": "multi-select",
              "label": "车队",
              "name": "fleet_id_list",
              "required": true,
              "options": []
            },
            {
              "type": "multi-select",
              "label": "注册必传证件",
              "name": "need_license",
              "required": true,
              "options": [
                {
                  "label": "身份证",
                  "value": 1,
                  "disabled": true
                },
                {
                  "label": "司机驾驶证",
                  "value": 2
                },
                {
                  "label": "司机行驶证",
                  "value": 3
                },
                {
                  "label": "网约车驾驶员证",
                  "value": 4
                },
                {
                  "label": "网约车运输证",
                  "value": 5
                }
              ]
            }
          ]
        }
      }
```


```
<template>
    <vxe-modal
        v-model="showPopup"
        show-footer
        show-confirm-button
        show-cancel-button
        destroy-on-close
        mask-closable
        :before-hide-method="beforeHideMethod"
        :draggable="false"
        title="新增司机招募活动"
    >
        <vxe-form ref="formRef" v-bind="formOptions">
            <template #open_city="params">
                <multi-select v-model="params.data.open_city" :options="cityOption" @change="changeEvent(params)"></multi-select>
            </template>
            <template #fleet_id_list="params">
                <multi-select v-model="params.data.fleet_id_list" :options="fleetOption" @change="changeEvent(params)"></multi-select>
            </template>
            <template #need_license="params">
                <multi-select v-model="params.data.need_license" :options="needLicenseOption" @change="changeEvent(params)"></multi-select>
            </template>
        </vxe-form>
    </vxe-modal>
</template>

<script setup>
import { ref, reactive, computed } from 'vue';
import XEUtils from 'xe-utils';
import { useSelectStore } from '@/store/select';
import { requestAjax } from '@/api/http';
import { VxeUI } from 'vxe-pc-ui';
import MultiSelect from '@/components/MultiSelect.vue';

const emit = defineEmits(['finish']);
const showPopup = ref(false);
const formRef = ref();
// select-options
const selectStore = useSelectStore();
const cityOption = computed(() => selectStore.cityList);
const fleetOption = computed(() => selectStore.fleetList);
const needLicenseOption = [
    { label: '身份证', value: 1, disabled: true },
    { label: '司机驾驶证', value: 2 },
    { label: '司机行驶证', value: 3 },
    { label: '网约车驾驶员证', value: 4 },
    { label: '网约车运输证', value: 5 }
];
const request = {
    getSelectList: () => {
        return Promise.all([
            selectStore.getCityList(),
            selectStore.getFleetList()
        ]);
    },
    recruitTaskCreate: params => {
        return requestAjax.post('/manage/recruit/task/create', params);
    }
};
const defaultData = {
    name: '',
    open_city: [],
    fleet_id_list: [],
    need_license: []
};
const formOptions = reactive({
    titleWidth: 'auto',
    titleColon: true,
    titleAlign: 'right',
    readonly: false,
    data: XEUtils.clone(defaultData, true),
    rules: {
        name: [{ required: true, message: '请输入活动名称' }],
        open_city: [{ required: true, message: '请选择城市选择' }],
        fleet_id_list: [{ required: true, message: '请选择车队' }],
        need_license: [{ required: true, message: '请选择注册必传证件' }]
    },
    items: [
        { field: 'name', title: '活动名称', span: 24, itemRender: { name: 'VxeInput', props: { placeholder: '请输入活动名称' } } },
        { field: 'open_city', title: '城市选择', span: 24, itemRender: {}, slots: { default: 'open_city' } },
        { field: 'fleet_id_list', title: '车队', span: 24, itemRender: {}, slots: { default: 'fleet_id_list' } },
        { field: 'need_license', title: '注册必传证件', span: 24, itemRender: {}, slots: { default: 'need_license' } }
    ]
});
const beforeHideMethod = async res => {
    if (res.type === 'confirm') {
        const errorMaps = await formRef.value.validate();
        if (errorMaps) {
            return Promise.reject(new Error());
        }
        console.log(formOptions.data);
        await request.recruitTaskCreate(formOptions.data);
        VxeUI.modal.message({ content: '提交成功', status: 'success' });
        showPopup.value = false;
        emit('finish');
    }
};
const changeEvent = params => {
    const $form = formRef.value;
    if ($form) {
        $form.updateStatus(params);
    }
};
defineExpose({
    open(row) {
        showPopup.value = true;
        if (row) {
            formOptions.data = XEUtils.clone({ ...defaultData, ...row }, true);
            if (typeof row.open_city === 'string') {
                formOptions.data.open_city = row.open_city.split(',');
            }
            if (typeof row.fleet_id_list === 'string') {
                formOptions.data.fleet_id_list = row.fleet_id_list.split(',');
            }
            if (typeof row.need_license === 'string') {
                formOptions.data.need_license = row.need_license.split(',');
            }
        } else {
            formOptions.data = XEUtils.clone(defaultData, true);
        }
    }
});
request.getSelectList();
</script>

<style scoped>
</style>
```
## 4.1 编写规则
那现在代码和 JSON 数据都准备好了，怎么去写规则呢？这里的弹窗规则可以参考这个文件。我这边的思路

* 按照 `<template>`、`<script setup>`、`<style scoped>` 三部分单独写逻辑。
* 精确到每一种情况的处理



```

---
description:
globs:
alwaysApply: false
---


# 表单弹窗（dialog/drawer）生成规则

本规则用于处理包含表单的弹窗组件，适用于 `dialog` 和 `drawer` 两种类型。
两者的**处理逻辑完全一致**，仅在 DOM 容器组件上有差异。

根据拿到的 popup_n_ref，在当前 vue 文件所属目录下新建 components 目录，并创建 popup_n.vue 文件。


## 整体规则说明

-   vue 固定由 `<template>`、`<script setup>`、`<style scoped>` 三部分组成。
-   严格按照规则来，不能有任何扩展，若是规则里面没有要求，不能去理解 JSON 里面某个字段、某个值的含义。
-   生成代码时，这里面所有情况都有规则，严格按照每一种情况的规则去做生成。
-   生成的代码要紧凑，减少空行和折行的出现。
-   不能漏掉任何内容。不能漏掉任何内容。不能漏掉任何内容。重要的事情说 3 遍。


## 5.0 弹窗类型判断（首先执行）

在生成代码之前，首先判断当前按钮的弹窗类型：

| JSON 字段 | 弹窗类型 | DOM 容器组件 |
|-----------|----------|--------------|
| `dialog`  | 对话框   | `<vxe-modal>` |
| `drawer`  | 抽屉     | `<vxe-drawer>` |

两种类型的差异**仅限于**：
1. DOM 容器组件名称不同（`vxe-modal` vs `vxe-drawer`）
2. 部分属性略有差异（见 5.2 节）

**其他所有逻辑（script、表单处理、校验等）完全一致**，统一按以下规则处理。


### 5.1 数据结构说明

dialog 和 drawer 数据结构完全一致，包含以下字段：
- `title`：弹窗标题
- `form`：表单配置对象
    - `initApi`：初始化接口
    - `api`：提交接口
    - `body`：表单项数组


### 5.2 template 结构

#### 5.2.1 dialog 类型（使用 vxe-modal）

```html
<template>
    <vxe-modal
        v-model="showPopup"
        show-footer
        show-confirm-button
        show-cancel-button
        destroy-on-close
        mask-closable
        :before-hide-method="beforeHideMethod"
        :draggable="false"
        title="对应 dialog.title 的值"
    >
        <vxe-form ref="formRef" v-bind="formOptions">
        </vxe-form>
    </vxe-modal>
</template>
```

#### 5.2.2 drawer 类型（使用 vxe-drawer）

```html
<template>
    <vxe-drawer
        v-model="showPopup"
        show-footer
        show-confirm-button
        show-cancel-button
        destroy-on-close
        :mask-closable="false"
        :before-hide-method="beforeHideMethod"
        title="对应 drawer.title 的值"
    >
        <vxe-form ref="formRef" v-bind="formOptions">
        </vxe-form>
    </vxe-drawer>
</template>
```

#### 5.2.3 两者差异对比

| 属性 | dialog (vxe-modal) | drawer (vxe-drawer) |
|------|-------------------|---------------------|
| `mask-closable` | `mask-closable`（无冒号，为 true） | `:mask-closable="false"` |
| `:draggable` | `:draggable="false"` | 无此属性 |


#### 5.2.1 检查 dialog.body 里面是否有 type 为 multi-select 的 item。
如果 dialog.body 里面是否有 type 为 multi-select 的 item。则在`vxe-form` 中间加上`template`这个区块的信息，每项item都加。
- 这里面的 [] 标记的内容是需要填写的。 
- item.name 表示是取的name字段。
- xxOption 的命名方式如下
    - 情况 1：如果 `item.name` 是包含 city,sp,cp,agent,fleet 中的任意一个，则取这里面  cityOption,spOption,cpOption,agentOption,fleetOption 对应的值。
    - 情况 2： 明明方式是 `[item.name]Option`，其中 `[item.name]Option`转成驼峰式命名

```js
<vxe-form
    ref="formRef"
    v-bind="formOptions"
>
    <template #[item.name]="params">
        <multi-select
            v-model="params.data.[item.name]"
            :options="[xxOption]"
            @change="changeEvent(params)"
        ></multi-select>
    </template>
</vxe-form>
```


### 5.3 script 结构说明
- 不需要定义 props 接收 dialog 参数
- 所有数据（包括 title、formOptions、options）都在组件内部直接定义
- title 直接硬编码在 template 中

#### 5.3.0 固定变量定义
固定以下两个变量，同时要引入这些内容
```js
import { ref, reactive, computed } from 'vue';
import XEUtils from 'xe-utils';
import { useSelectStore } from '@/store/select';
import { requestAjax } from '@/api/http';
import { VxeUI } from 'vxe-pc-ui';

const emit = defineEmits(['finish']);
const showPopup = ref(false);
const formRef = ref();
```

#### 5.3.1 select-options 处理（严格规则）
- 在这里的开头加一个js 注释，内容就写 select-options
- 统计 JSON中的body数组，分为以下 2 类去处理，每个只能选择其中一类。按照顺序判断。严格按照顺序来，如果匹配到其中一类，就不要再取考虑其他两类的情况了，即这 2 类情况都是完全独立的，不能有任何干扰。检查是针对每一个type为select和radios的数据进行检查！！！

- **第一类（模糊匹配）**：如果 `name` 字段**包含** city、sp、cp、agent、fleet 这 5 个关键字中的任意一个（如 `open_city` 包含 `city`，`fleet_id_list` 包含 `fleet`，`xx_agent_xx` 包含 `agent` 等），则生成对应的 Option。
    - 需要加以下 selectStore 的引用。注意别忘了引入 computed
    ```js
    import { useSelectStore } from '@/store/select';
    // select-options
    const selectStore = useSelectStore();
    ```
    - 如果匹配到 city 就加 `const cityOption = computed(() => selectStore.cityList);`.
    - 如果匹配到 sp 就加 `const spOption = computed(() => selectStore.spList);`.
    - 如果匹配到 cp 就加 `const cpOption = computed(() => selectStore.cpList);`.
    - 如果匹配到 agent 就加 `const agentOption = computed(() => selectStore.agentList);`.
    - 如果匹配到 fleet 就加 `const fleetOption = computed(() => selectStore.fleetList);`.
    - 以上这5 个name对应的 Option 是不可改变的。不能做任何改变，即使是特殊情况

- **第二类（剩余字段）**：前提是 name 不属于第一类（即不包含以上 5 个关键字），则：
    - 命名规则：用驼峰的方式命名 Option，不添加任何后缀
    - **取值规则（强制）**：必须从 JSON 数据中复制 options 字段的完整数组内容，即使数组为空也要写成 `const xxxOption = [];`
    - 示例：
        ```js
        // 如果 JSON 中有: "options": [{"label": "身份证", "value": 1}, {"label": "驾驶证", "value": 2}]
        const needLicenseOption = [
            { label: "身份证", value: 1 },
            { label: "驾驶证", value: 2 }
        ];
        // 如果 JSON 中有: "options": []
        const xxxOption = [];
        ```

**关键提醒**：
- 绝对不能写成 `const xxxOption = options` 或 `const xxxOption = []` 然后不填写内容
- 必须将 JSON 中的 options 数组内容完整复制过来
- 这是强制规则，没有任何例外情况

**注意**：此处的"包含"是模糊匹配（includes），与主页面（rule2.5.mdr）中的精确匹配（等于）不同。

#### 5.3.2 request 变量处理
根据 JSON 中的 dialog.api 去处理。
- 在 request 里面新增一个方法，方法名根据 api 的内容去生成即可。
- 方法内容如下代码。其中 post(api,params)里api的值是要去掉原api里面的 ${SERVER}。
- 还需要在 script 最上面引入 `import { requestAjax } from '@/api/http';`
- 如果 5.3.1 里面有定义 cityOption,spOption,cpOption,agentOption,fleetOption任意一个。那就需要给request里面加这个函数。这五个数组对应的[selectStore.getCityList(),selectStore.getSpList(),selectStore.getCpList(),selectStore.getAgentList(),selectStore.getFleetList()]是这些，是用到了哪些字段就哪些。

```js
const request = {
    getSelectList: () => {
        return Promise.all([
            selectStore.getCityList(),
            selectStore.getSpList(),
            selectStore.getCpList(),
            selectStore.getAgentList(),
            selectStore.getFleetList()
        ]);
    },
    xxx: params => {
        return requestAjax.post(api , params)
    }
}
```

#### 5.3.4 表单相关数据处理

##### 5.3.4.1 定义 defaultData
收集JSON中的 `dialog.body` 中所有 `name` 和 `extraName`（若有），初始值均为 `''`。如果type为 multi-select，那初始值就是 []。
```js
const defaultData = {

}
```

##### 5.3.4.2 定义 formOptions
其要在 JS 里面定义变量为 formOptions，定义方式为 
```js
const formOptions = reactive({
    // 这些是以下的内容
    titleWidth: 'auto',
    titleColon: true,
    titleAlign: 'right',
    readonly: false,
    data: XEUtils.clone(defaultData, true),
    rules: {
        // TODO
    },
    items: [
        // TODO
        // demo
        /**
         * {
         *  field,
         *  title,
         *  span,
         *  itemRender: { name: '', props: {placeholder} }
         * }
         */
    ]
})
```

-   基础配置：
    - 固定包含 `titleWidth: 'auto'`。
    - `titleColon: true`
    - `titleAlign: 'right'`
    - `readonly: false`
-   data 字段：`XEUtils.clone(defaultData, true)`
-   rules 字段。与 JSON 里面的 `dialog.body` 一一对应，判断每个 item 的 required 属性，如果为 ture 就加。
    - rules 是一个对象。其 key 值就是 item.name。然后对应的数据按照这个来 `[{ required: true, message: '请输入活动名称' }]`。message根据item.type来处理。
        - 如果 type 里面含有 input ，那就是请输入 xxx。
        - 如果 type 里面含有 select, 那就是请选择 xxx。
```js
    rules: {
        input_text: [{ required: true, message: '请输入活动名称' }],
        open_city: [{ required: true, message: '请选择城市' }],
    }
```


- items 字段：是一个数组。其中每一个值需要遍历 `form.body` 里的每一个 item 进行处理，
    -  其中placeholder处理方式如下 ，根据 item.type来处理。
        - 如果 type 里面含有 input ，那就是请输入 xxx。
        - 如果 type 里面含有 select, 那就是请选择 xxx。
    -   `field`：若当前项含 `extraName`（范围选择），格式为 `_${name}And${extraName}`；否则为 `name`。
    -   `title`：对应 `filter.body` 中的 `label`。
    -   `span`：固定为 24
    -   `startField`/`endField`：含 `extraName` 时，分别对应 `name` 和 `extraName`。
    -   `itemRender` 需要根据 `item.type` 去做不同逻辑的处理。具体处理规则如下

###### 5.3.4.2.1 type 为 input-data-range 字段处理
itemRender 值为 `{name: 'VxeDateRangePicker', props: {placeholder}}`

###### 5.3.4.2.2 type 为 input-data 字段处理
itemRender 值为 `{name: 'VxeDatePicker', props: {placeholder}}`

###### 5.3.4.2.3 type 为 input-datetime-range 字段处理
itemRender 值为 `{name: 'VxeDateRangePicker', props: {placeholder}}`

###### 5.3.4.2.4 type 为 input-time-range 字段处理
itemRender 值为 `{name: 'VxeDateRangePicker', props: {placeholder}}`

###### 5.3.4.2.5 type 为 input-text 字段处理
itemRender 值为 `{name: 'VxeInput', props: {placeholder}}`

###### 5.3.4.2.6 type 为 select 字段处理
itemRender 值为 `{name: 'VxeSelect', props: {placeholder}, options: xxOption}`.options定义如下，分两种情况
- 情况 1：如果 `item.name` 是包含 city,sp,cp,agent,fleet 中的任意一个，则取这里面  cityOption,spOption,cpOption,agentOption,fleetOption 对应的值。
- 情况 2： 命名方式是 `[item.name]Option`，其中 `[item.name]Option`转成驼峰式命名


###### 5.3.4.2.7 type 为 multi-select 字段处理
itemRender 值为 `{}`，并与itemRender 同级的加一个slots字段，如 `slots: {default: item.name}`， 其中default 的值就取 field里面的值就行。还需要再script最上方引入 `import MultiSelect from '@/components/MultiSelect.vue';`


###### 5.3.4.2.8 type 为 input-image 字段处理
itemRender 的值为 `{ name: 'VxeUpload', props: { placeholder: '请输入背景图片', mode: "image" } }`


###### 5.3.4.2.9 type 为 radios 字段处理
itemRender 的值为 `{ name: 'VxeRadioGroup', props: {options: xxOption} }`.options定义如下,`[item.name]Option`，其中 `[item.name]Option`转成驼峰式命名


##### 5.3.4.4 **核心规则（强制）**：
- 在 `formOptions.items` 中引用 `computed` 定义的 Option 变量时，**严禁**添加 `.value`
- Vue 3 在 `reactive` 对象内部会自动解包 `computed` ref，手动加 `.value` 会导致错误
- **正确写法**：
  ```js
  // ❌ 错误
  options: cityOption.value,
  options: fleetOption.value,
  
  // ✅ 正确
  options: cityOption,
  options: fleetOption,
  ```
- 这是核心规则，没有任何例外情况，必须严格执行

#### 5.3.4 beforeHideMethod 变量定义
- 其中调用 request 方法那里， 用的是在 5.3.2 里面用api定义的方法。其他的固定就行

```js
const beforeHideMethod = async (res) => {
    if (res.type === 'confirm') {
        const errorMaps = await formRef.value.validate();
        if (errorMaps) {
            reject(new Error());
        }        
        console.log(formOptions.data);
        await request.xxxxxx(formOptions.data);
        VxeUI.modal.message({ content: '提交成功', status: 'success' });
        showPopup.value = false;
        emit('finish');
    }   
}
```

#### 5.3.5 changeEvent 和 defineExpose 变量定义

```js
const changeEvent = params => {
    const $form = formRef.value;
    if ($form) {
        $form.updateStatus(params);
    }
};
defineExpose({
    open(row) {
        showPopup.value = true;
        if (row) {
            formOptions.data = XEUtils.clone({ ...defaultData, ...row }, true);
            // 处理数组类型字段：将字符串转换为数组
            // TODO: 根据 defaultData 中初始值为数组的字段进行处理
        } else {
            formOptions.data = XEUtils.clone(defaultData, true);
        }
    }
});
```

##### 5.3.5.1 数组字段处理规则（编辑模式）
当 `open(row)` 方法接收到 row 数据时（编辑模式），需要对 defaultData 中**初始值为数组**的字段进行特殊处理：

**处理逻辑**：
1. 遍历 `defaultData` 中所有初始值为 `[]` 的字段
2. 对于每个数组字段，检查 `row` 中对应字段的值
3. 如果 `row` 中该字段是字符串类型，使用 `split(',')` 转换为数组

**生成代码示例**：
```js
defineExpose({
    open(row) {
        showPopup.value = true;
        if (row) {
            formOptions.data = XEUtils.clone({ ...defaultData, ...row }, true);
            // 处理数组类型字段
            if (typeof row.page_type_list === 'string') {
                formOptions.data.page_type_list = row.page_type_list.split(',');
            }
            if (typeof row.sp_list === 'string') {
                formOptions.data.sp_list = row.sp_list.split(',');
            }
            // ... 其他数组字段同理
        } else {
            formOptions.data = XEUtils.clone(defaultData, true);
        }
    }
});
```

**判断依据**：
- 只处理在 `defaultData` 中定义为 `[]`（空数组）的字段
- 常见的数组字段类型：`multi-select` 类型的表单项
- 不需要处理非数组类型的字段

#### 5.3.6 方法调用
如果在 5.3.1 定义了 cityOption,spOption,cpOption,agentOption,fleetOption任意一个。那就需要调用 `request.getSelectList()`
```


```




以  【5.3.4.2 定义 formOptions】这一个举例，formOptions里面rules，和items是需要根据body.body里面的type去生成的，而每种type生成的方式也不一样，

```
const formOptions = reactive({
    titleWidth: 'auto',
    titleColon: true,
    titleAlign: 'right',
    readonly: false,
    data: XEUtils.clone(defaultData, true),
    rules: {
        name: [{ required: true, message: '请输入活动名称' }],
        open_city: [{ required: true, message: '请选择城市选择' }],
        fleet_id_list: [{ required: true, message: '请选择车队' }],
        need_license: [{ required: true, message: '请选择注册必传证件' }]
    },
    items: [
        { field: 'name', title: '活动名称', span: 24, itemRender: { name: 'VxeInput', props: { placeholder: '请输入活动名称' } } },
        { field: 'open_city', title: '城市选择', span: 24, itemRender: {}, slots: { default: 'open_city' } },
        { field: 'fleet_id_list', title: '车队', span: 24, itemRender: {}, slots: { default: 'fleet_id_list' } },
        { field: 'need_license', title: '注册必传证件', span: 24, itemRender: {}, slots: { default: 'need_license' } }
    ]
});
```


那这里是这样设计的，

* 首先，指出哪些值时固定的，这部分不会有任何改动。



* 然后 定义 rules 的生成规则，其实它就是根据 required来进行处理的。但因为是 AI 生成，且要求无论多少次生成代码都是一样的，那就需要在这里规范好有哪些内容，这些内容的规则是什么



* 然后是 items。同样，这里面也是区分固定不受影响的值。然后有变动的地方则根据每个type去写好说明

```
##### 5.3.4.2 定义 formOptions
其要在 JS 里面定义变量为 formOptions，定义方式为 
```js
const formOptions = reactive({
    // 这些是以下的内容
    titleWidth: 'auto',
    titleColon: true,
    titleAlign: 'right',
    readonly: false,
    data: XEUtils.clone(defaultData, true),
    rules: {
        // TODO
    },
    items: [
        // TODO
        // demo
        /**
         * {
         *  field,
         *  title,
         *  span,
         *  itemRender: { name: '', props: {placeholder} }
         * }
         */
    ]
})
```

-   基础配置：
    - 固定包含 `titleWidth: 'auto'`。
    - `titleColon: true`
    - `titleAlign: 'right'`
    - `readonly: false`
-   data 字段：`XEUtils.clone(defaultData, true)`
-   rules 字段。与 JSON 里面的 `dialog.body` 一一对应，判断每个 item 的 required 属性，如果为 ture 就加。
    - rules 是一个对象。其 key 值就是 item.name。然后对应的数据按照这个来 `[{ required: true, message: '请输入活动名称' }]`。message根据item.type来处理。
        - 如果 type 里面含有 input ，那就是请输入 xxx。
        - 如果 type 里面含有 select, 那就是请选择 xxx。
```js
    rules: {
        input_text: [{ required: true, message: '请输入活动名称' }],
        open_city: [{ required: true, message: '请选择城市' }],
    }
```


- items 字段：是一个数组。其中每一个值需要遍历 `form.body` 里的每一个 item 进行处理，
    -  其中placeholder处理方式如下 ，根据 item.type来处理。
        - 如果 type 里面含有 input ，那就是请输入 xxx。
        - 如果 type 里面含有 select, 那就是请选择 xxx。
    -   `field`：若当前项含 `extraName`（范围选择），格式为 `_${name}And${extraName}`；否则为 `name`。
    -   `title`：对应 `filter.body` 中的 `label`。
    -   `span`：固定为 24
    -   `startField`/`endField`：含 `extraName` 时，分别对应 `name` 和 `extraName`。
    -   `itemRender` 需要根据 `item.type` 去做不同逻辑的处理。具体处理规则如下

###### 5.3.4.2.1 type 为 input-data-range 字段处理
itemRender 值为 `{name: 'VxeDateRangePicker', props: {placeholder}}`

###### 5.3.4.2.2 type 为 input-data 字段处理
itemRender 值为 `{name: 'VxeDatePicker', props: {placeholder}}`

###### 5.3.4.2.3 type 为 input-datetime-range 字段处理
itemRender 值为 `{name: 'VxeDateRangePicker', props: {placeholder}}`

###### 5.3.4.2.4 type 为 input-time-range 字段处理
itemRender 值为 `{name: 'VxeDateRangePicker', props: {placeholder}}`

###### 5.3.4.2.5 type 为 input-text 字段处理
itemRender 值为 `{name: 'VxeInput', props: {placeholder}}`

###### 5.3.4.2.6 type 为 select 字段处理
itemRender 值为 `{name: 'VxeSelect', props: {placeholder}, options: xxOption}`.options定义如下，分两种情况
- 情况 1：如果 `item.name` 是包含 city,sp,cp,agent,fleet 中的任意一个，则取这里面  cityOption,spOption,cpOption,agentOption,fleetOption 对应的值。
- 情况 2： 命名方式是 `[item.name]Option`，其中 `[item.name]Option`转成驼峰式命名


###### 5.3.4.2.7 type 为 multi-select 字段处理
itemRender 值为 `{}`，并与itemRender 同级的加一个slots字段，如 `slots: {default: item.name}`， 其中default 的值就取 field里面的值就行。还需要再script最上方引入 `import MultiSelect from '@/components/MultiSelect.vue';`


###### 5.3.4.2.8 type 为 input-image 字段处理
itemRender 的值为 `{ name: 'VxeUpload', props: { placeholder: '请输入背景图片', mode: "image" } }`


###### 5.3.4.2.9 type 为 radios 字段处理
itemRender 的值为 `{ name: 'VxeRadioGroup', props: {options: xxOption} }`.options定义如下,`[item.name]Option`，其中 `[item.name]Option`转成驼峰式命名


```




## 4.3 规则迭代和调优方式
那写的规则效果好不好，效果不满意怎么办？则有以下几种方式，具体也可以参考贴出来的实例。







方法一：AI 生成出错了，可以让 AI 自己检查一遍，或者是自己指出，然后问 AI，怎么修改规则可以避免。

方法二：生成成功后，让 AI 自己去检查一遍规则，把可能会导致歧义的地方指出来，并要指出怎么修改





参考一: 新增了一个功能，此时逻辑有些冗余和复杂，需要 AI 进行优化 ： [https://console.cloud.baidu-int.com/comatestack/share/4279?token=de88918f](https://console.cloud.baidu-int.com/comatestack/share/4279?token=de88918f)

参考二: 有一个功能不知道怎么写规则，或者写的比较模糊，AI 生成后的代码正是想要的，让 AI 把这块规则优化：[https://console.cloud.baidu-int.com/comatestack/share/4282?token=ad556147](https://console.cloud.baidu-int.com/comatestack/share/4282?token=ad556147)

参考三: 让 AI 自己识别规则中的歧义、不明确的地方，指出来并改正：[https://console.cloud.baidu-int.com/comatestack/share/4281?token=0060acdd](https://console.cloud.baidu-int.com/comatestack/share/4281?token=0060acdd)

# 五、完整实践
然后可以参考这一部分在本地运行起来，模型建议使用 Claude Opus 4.5。



代码库：

[附件]


## 5.1 安装依赖运行项目


npm install

npm run dev





## 5.2 格式化处理
```
cd data
node handle.cjs list8.json


以上做完会在 data/real 下生成list8.json数据，即格式化后的数据
```


## 5.3 zulu生成代码


选中规则文件，mock.vue文件，刚刚生成的list8.json文件，输入以下内容。等待页面生成完成即可

用rule2.5 在mock.vue下生成页面，数据源是 list8.json

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0123d1176cec4c06a967b374ed86335c&docGuid=hSZfep-uUHDfHu "")




# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
