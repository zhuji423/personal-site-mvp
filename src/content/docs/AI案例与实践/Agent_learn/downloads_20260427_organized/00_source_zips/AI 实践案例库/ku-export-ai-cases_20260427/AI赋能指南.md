---
title: "研发流程"
description: "与时俱进，不定期更新。"
date: "2026-10-11"
category: "AI案例与实践"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\AI 实践案例库\\ku-export-ai-cases_20260427\\AI赋能指南.md"
---
AI赋能指南

#### 🧑‍🏫 案例作者：多人共创
#### 🎬 案例场景：全流程
#### 🔧 使用工具：ChatGPT，Deepseek，Comate
#### 📒 案例概要：本文介绍了AI工具在研发流程中的应用指南，涉及PM、研发、QA等角色在不同阶段如PRD设计、会议纪要、代码解读、需求调研等的AI赋能实践。通过ChatGpt、deepseek等平台，结合具体案例展示了AI在需求文档生成、会议纪要自动整理、代码解读、需求调研等方面的优势与劣势，并提出了AI与人工结合的最佳实践，以提升研发效率和文档质量。
*参与人员： 李翛然、崔旭、刘思冰、王宇硕、杨玉帆、吴嘉东。*

*与时俱进，不定期更新。*

# 研发流程


[流程图]
# 角色选择
### 👩‍💼 PM
### 💻 研发
### ✅ QA
- 【[PRD 设计](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-235d7821-8317-11f0-8e26-f10b9d45b375)】

- 【[会议纪要](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7?block_id=docyg-3a881d81-831b-11f0-8e26-f10b9d45b375&type=card)】

- 【[代码解读](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-39484a81-831b-11f0-8e26-f10b9d45b375)】

- 【[需求调研](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-0603c2e1-831f-11f0-96a9-c52652e81f83)】

- 【[技术详设](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-7b67a0f0-831b-11f0-8e26-f10b9d45b375)】

- 【[实际开发](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-10165811-831f-11f0-96a9-c52652e81f83)】

- 【[CR 阶段](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-1d29d131-831f-11f0-96a9-c52652e81f83)】

- 【[上线阶段](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-24f8b7f1-831f-11f0-96a9-c52652e81f83)】

- 【[case list 阶段](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-ec9dafa1-831e-11f0-96a9-c52652e81f83)】

- 【[测试阶段](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/AfcHTn4uU_acj7#anchor-docyg-f29a9581-831e-11f0-96a9-c52652e81f83)】

# 📌 AI 工具
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f537e4893e2447838eda75e515162975&docGuid=AfcHTn4uU_acj7 "")
## ChatGpt
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5f1fd76c1f8549afba7510c44338e4cb&docGuid=AfcHTn4uU_acj7 "")
## deepseek
* 地址：[https://chatgpt.com/](https://chatgpt.com/?model=auto)
* 地址：[https://www.deepseek.com/](https://www.deepseek.com/)



![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e2c0d1c664de4c829859fd8131d143f9&docGuid=AfcHTn4uU_acj7 "")
## zulu & comate
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2b5e6a8b34454a6189170339dd159709&docGuid=AfcHTn4uU_acj7 "")
## panda
* 地址：[https://comate.baidu.com/zh/download](https://comate.baidu.com/zh/download)



* 操作手册：[https://cloud.baidu.com/doc/COMATE/s/Jlnvr7vgh](https://cloud.baidu.com/doc/COMATE/s/Jlnvr7vgh)
* 实际UI稿转代码体验：[zulu体验](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/a-XGS26e08O9Z4?t=mention&mt=doc&dt=doc)



小 Tips：

* Zulu 的生成的回答会在当前代码库中创建一个 md 类型的文件，可以使用 IDE 的「预览」功能直接展示有结构的文件类型，如图1
* Zulu 用在 IDE 里，所以要实现某个需求功能，可以直接选中相关代码文件进行提问，如下图2

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=167b5d9a8c8b46d984f25b72fe16d0b7&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f228df9c7dfd42fd823e086adac825b9&docGuid=AfcHTn4uU_acj7 "")


* 地址：[https://panda.baidu-int.com/llm?appId=gpt-4o](https://panda.baidu-int.com/llm?appId=gpt-4o)



* 介绍：**大模型助手，**可以直接访问当前主流的十余款大模型服务（场内）

# PRD设计
*AI平台：*[ChatGpt](https://chatgpt.com/)、[deepseek](https://www.deepseek.com/)



**所存在的问题： **

1、需求边界功能不清晰

2、需求功能点遗漏



**描述：**

举个🌰：我以“电商场景搜索直播、主播、商品名称时，支持展示推送关键词的需求，并需要将关键词与搜索词首部匹配，想通就高亮。根据我上面的描述，帮我写一份需求文档”

## AI赋能
[https://chatgpt.com/s/t_68abd012a26881919b3a6dd84ca87bb6](https://chatgpt.com/s/t_68abd012a26881919b3a6dd84ca87bb6)

TODO: 补充提问问题

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0e357512da8e4155be01b79ff60d0db2&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b3217ee49b714d0885b974fcd8f994c3&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=edd3aedb3fd445ae9b01b1b592d229b3&docGuid=AfcHTn4uU_acj7 "")
#### 优势
1、能够快速生成一个文档

2、文档包含多种结构

3、根据业内需求，快速定位整体概述、明确边界点等

4、更好量化收益统计

5、提前明确好埋点需要的数据、以及参与方

6、可以根据文档内容或流程快速生成流程图

7、明确出需求关键节点

### VS* *
## *传统实现*
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aba2eb6825714e02a21555b3aef5e6b2&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=46e5664e1ebf4b4ab7dc6a476b1b192f&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aa616322dac944cfae302465b91054ff&docGuid=AfcHTn4uU_acj7 "")
#### *劣势*
1、文档书写时间较长 => 产品需求效率

2、边界功能不清晰 => 研发、测试效率

3、没有流程图或画流程图较慢 => 需求遗漏

4、部分功能隐藏过深，研发、QA理解成本过高



#### 优势
1、背景和目标更加贴合业务现状

2、根据实际数据关注可落地收益

3、需求功能更加细致



☞AI 赋能主旨：AI 和人工两者优势联合，以达到产出需求文档的效率最高，产出需求文档的内容最好。



合理使用 AI 工具完成以下几个功能可以让文档更好：

1、AI 大纲生成与建议：使用 AI 提供结构完整、逻辑清晰的大纲，减少调整需求文档结构带来的成本，保证结构一致性，降低阅读成本

2、可视化与快速原型：使用 AI 帮助需求生成详细流程图，节省人工画图时间和成本，帮助各角色理清需求从头到尾的整个细枝末节，方便相关人员快速熟悉流程

3、功能覆盖与风险：根据功能描述，让 AI 生成功能的异常场景和边缘情况，提前发现业务逻辑漏洞，降低开发过程中的需求变更

# 会议纪要
**所存在的问题： **

1. 会议上有的问题总结续有人记录。
2. 会议上有的代办无人总结。
3. 产生的 AI 代办和会议总结可能无法及时找到。
4. ddl时间无人记录，期望根据会议总结，自动增加待办。

# **代码解读**
介绍怎么使用即可。

*AI平台：ZULU、*[ChatGpt](https://chatgpt.com/)、[deepseek](https://www.deepseek.com/)



TODO: 补充 zulu 的使用方式



**所存在的问题：**

面对逻辑难，调用层级深的代码，往往会遇到以下几个问题：

1、迷失在代码里：跟着函数调用链钻进去几层后，就忘了最初的核心目的是什么，忘记了主线任务。或者跳转到一个不熟悉的模块，完全不知道这个模块的职责是什么。

2、细节旋涡：过早地陷入每一行代码的细节（比如某个条件判断的精确逻辑），而无法跳出细节看清整体的业务流程和设计模式。

3、隐藏逻辑：代码的逻辑依赖于一些看不见的东西，比如：全局状态、外部配置、数据库的某个特定值、消息队列的特定事件、某个框架的“魔法”行为。这些逻辑不会明确写在代码里，但你不知道它就无法理解。

4、依赖地域：一个方法的执行，依赖多个外部服务（API、RPC）、中间件的返回结果，你不得不去了解这些外部组件的接口和行为，才能理清逻辑。



### ** 传统代码解读**
##### **🚩 **准备工作
---

1、明确目标：读代码的目的

2、读文档：读代码相关的架构图

3、找知情人：请教熟悉此代码的同事

##### **🚩 **阅读过程
---

1、自顶向下：从入口开始入手

2、理清主干流程：只看第一层调用画出流程图，弄清“先做什么，后做什么”

3、逐层深入：把主干流程上每个关键步骤视为新入口，重复上述过程

##### **🚩 **辅助工具 - 延伸你的大脑
---

1、擅用 IDE

2、动手画图

3、文档记录

##### **🚩 **长期修炼 - 成为代码侦探
---

1、多读代码

2、重构旧代码

3、学习设计原则和模式

↓

↓

↓

##### **🚩 **AI 辅助快速建立宏观认知
---

1、AI 工具分析代码

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1805a744281c42998c9215b1b0225dd4&docGuid=AfcHTn4uU_acj7 "")
2、AI 项目概述

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0349d4f1cc894796b12e70505f8b757d&docGuid=AfcHTn4uU_acj7 "")


##### **🚩 **AI 作为实时协作者
---

1、AI 生成流程图 or 时序图 or 其他

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b76aa8e5c49d47dc8ffb65eea0c1d5de&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c9c14d5f75234823a4a2248900c946d8&docGuid=AfcHTn4uU_acj7 "")
2、AI 解释代码

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=23a5aff2f935423b942066b04e4b5a39&docGuid=AfcHTn4uU_acj7 "")


##### **🚩 **AI 帮助辅助思考
---

1、重构 & 优化代码

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cac917e1852a482da7a1aff84adafe22&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=46402140677f4a6288ec8eaaca680798&docGuid=AfcHTn4uU_acj7 "")
### AI 工具代码解读


Prompt 总结：

* 请分析这段代码/这个目录结构，为我总结这个项目的主要功能、核心模块以及它们之间的依赖关系，关键步骤请用流程图代替
* 我现在要阅读一个关于 XXX 的代码模块，我应该重点关注哪些核心类和方法？可能会用到哪些设计模式？
* 请将以下代码转换为一个清晰的时序图（使用 Mermaid 语法）或调用流程图
* 请用通俗易懂的语言解释以下代码的功能
* 这段代码里 某一块看不懂的位置 的作用是什么？
* 请帮我优化 某一块 代码

# 需求调研
*AI平台：*[ChatGpt](https://chatgpt.com/)、[deepseek](https://www.deepseek.com/)、zulu



**所存在的问题： **

1. 调研阶段只可以输入当前索要达到的效果，但是不能根据当前的项目技术栈实现想要的功能



**描述：**

举个🌰：帮生成一个视频播放器，要求是实时直播播放器、并且也兼容MP4。

## deepseek
## 🎁 deepseek 🎁
# **① **功能实现
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4ceb435099ef44eeb5fc48e1c1a4b9a8&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=32931f7b24744389aafe03f195d6ae85&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2e2bd5cd167d4757b04b7379f3ad21d1&docGuid=AfcHTn4uU_acj7 "")


```
<script>
  import { onMount, onDestroy } from 'svelte';
  import Hls from 'hls.js'; // 用于HLS直播流

  // 组件属性
  export let src = '';
  export let type = 'auto'; // 'auto', 'hls', 'mp4', 'dash'
  export let autoplay = false;
  export let muted = false;
  export let controls = true;
  export let poster = '';
  export let preload = 'auto';
  export let className = '';
  export let width = '100%';
  export let height = 'auto';

  let videoElement;
  let hls; // Hls.js实例
  let isPlaying = false;
  let currentTime = 0;
  let duration = 0;
  let volume = 1;
  let isMuted = muted;
  let isFullscreen = false;
  let isControlsVisible = controls;
  let controlsTimeout;
  let isLive = false;
  let playbackRate = 1;
  let showSettings = false;
  let qualityLevels = [];
  let currentQuality = 'auto';

  // 检测视频类型
  function detectVideoType(src) {
    if (type !== 'auto') return type;
    
    if (src.includes('.m3u8')) return 'hls';
    if (src.includes('.mpd')) return 'dash';
    if (src.includes('.mp4') || src.includes('.webm') || src.includes('.ogg')) return 'mp4';
    
    // 默认为MP4
    return 'mp4';
  }

  // 初始化视频
  function initVideo() {
    if (!videoElement) return;
    
    const videoType = detectVideoType(src);
    
    // 重置之前的实例
    if (hls) {
      hls.destroy();
      hls = null;
    }

    // 设置通用事件监听
    setupVideoEvents();

    if (videoType === 'hls') {
      if (Hls.isSupported()) {
        hls = new Hls({
          enableWorker: true,
          lowLatencyMode: true,
          backBufferLength: 90
        });
        hls.loadSource(src);
        hls.attachMedia(videoElement);
        hls.on(Hls.Events.MANIFEST_PARSED, () => {
          isLive = hls.levels.length > 0 ? hls.levels[0].details?.live : false;
          qualityLevels = hls.levels.map((level, index) => ({
            id: index,
            label: level.height + 'p',
            width: level.width,
            height: level.height,
            bitrate: level.bitrate
          }));
        });
      } else if (videoElement.canPlayType('application/vnd.apple.mpegurl')) {
        // Safari原生支持HLS
        videoElement.src = src;
        isLive = true; // 假设HLS流是直播
      }
    } else {
      // 标准视频格式
      videoElement.src = src;
      isLive = false;
    }

    // 设置初始音量
    videoElement.volume = volume;
    videoElement.muted = isMuted;
  }

  // 设置视频事件监听
  function setupVideoEvents() {
    if (!videoElement) return;
    
    videoElement.addEventListener('play', () => isPlaying = true);
    videoElement.addEventListener('pause', () => isPlaying = false);
    videoElement.addEventListener('timeupdate', updateProgress);
    videoElement.addEventListener('volumechange', updateVolume);
    videoElement.addEventListener('loadedmetadata', () => {
      duration = videoElement.duration;
      isLive = !isFinite(duration);
    });
    videoElement.addEventListener('click', togglePlay);
  }

  // 更新播放进度
  function updateProgress() {
    currentTime = videoElement.currentTime;
    if (!isLive) {
      duration = videoElement.duration;
    }
  }

  // 更新音量状态
  function updateVolume() {
    volume = videoElement.volume;
    isMuted = videoElement.muted;
  }

  // 播放/暂停
  function togglePlay() {
    if (isPlaying) {
      videoElement.pause();
    } else {
      videoElement.play().catch(e => {
        console.error('播放失败:', e);
        // 自动播放可能被浏览器阻止，需要用户交互
      });
    }
  }

  // 切换静音
  function toggleMute() {
    videoElement.muted = !videoElement.muted;
  }

  // 切换全屏
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      if (videoElement.requestFullscreen) {
        videoElement.requestFullscreen();
      } else if (videoElement.webkitRequestFullscreen) {
        videoElement.webkitRequestFullscreen();
      } else if (videoElement.msRequestFullscreen) {
        videoElement.msRequestFullscreen();
      }
      isFullscreen = true;
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
      } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
      }
      isFullscreen = false;
    }
  }

  // 设置播放速度
  function setPlaybackRate(rate) {
    playbackRate = rate;
    videoElement.playbackRate = rate;
    showSettings = false;
  }

  // 设置视频质量
  function setQuality(levelId) {
    if (hls && hls.levels.length > 0) {
      hls.currentLevel = levelId;
      currentQuality = levelId === -1 ? 'auto' : levelId;
    }
    showSettings = false;
  }

  // 跳转到指定时间
  function seekTo(time) {
    if (!isLive) {
      videoElement.currentTime = time;
    }
  }

  // 格式化时间显示
  function formatTime(seconds) {
    if (isLive || !isFinite(seconds)) return 'Live';
    
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  }

  // 显示控制条
  function showControls() {
    isControlsVisible = true;
    clearTimeout(controlsTimeout);
    controlsTimeout = setTimeout(() => {
      if (isPlaying) {
        isControlsVisible = false;
      }
    }, 3000);
  }

  // 组件挂载时初始化
  onMount(() => {
    initVideo();
    // 添加全局事件监听
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
    document.addEventListener('msfullscreenchange', handleFullscreenChange);
  });

  // 处理全屏状态变化
  function handleFullscreenChange() {
    isFullscreen = !!document.fullscreenElement;
  }

  // 组件销毁时清理
  onDestroy(() => {
    if (hls) {
      hls.destroy();
    }
    clearTimeout(controlsTimeout);
    document.removeEventListener('fullscreenchange', handleFullscreenChange);
    document.removeEventListener('webkitfullscreenchange', handleFullscreenChange);
    document.removeEventListener('msfullscreenchange', handleFullscreenChange);
  });

  // 当src发生变化时重新初始化
  $: if (src) {
    initVideo();
  }
</script>

<div class="video-player {className}" style="width: {width}; height: {height};">
  <div
    class="video-container"
    on:mousemove={showControls}
    on:touchstart|preventDefault={showControls}
  >
    <video
      bind:this={videoElement}
      {poster}
      {preload}
      {autoplay}
      {muted}
      class="video-element"
    ></video>

    {#if isControlsVisible || !isPlaying}
      <div class="video-controls">
        <div class="controls-top">
          <div class="live-indicator" class:live={isLive}>
            {isLive ? 'LIVE' : formatTime(currentTime)}
          </div>
        </div>

        <div class="progress-bar">
          <input
            type="range"
            class="seek-slider"
            min="0"
            max={isLive ? 100 : duration}
            value={currentTime}
            on:input={(e) => seekTo(parseFloat(e.target.value))}
            disabled={isLive}
          />
          <div
            class="progress-filled"
            style={`width: ${isLive ? 100 : (currentTime / duration) * 100}%`}
          ></div>
        </div>

        <div class="controls-bottom">
          <div class="left-controls">
            <button on:click={togglePlay} class="play-pause-btn" aria-label={isPlaying ? 'Pause' : 'Play'}>
              {#if isPlaying}
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
                </svg>
              {:else}
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M8 5v14l11-7z"/>
                </svg>
              {/if}
            </button>

            <button on:click={toggleMute} class="volume-btn" aria-label={isMuted ? 'Unmute' : 'Mute'}>
              {#if isMuted || volume === 0}
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M3.63 3.63a.996.996 0 000 1.41L7.29 8.7 7 9H4c-.55 0-1 .45-1 1v4c0 .55.45 1 1 1h3l3.29 3.29c.63.63 1.71.18 1.71-.71v-4.17l4.18 4.18c-.49.37-1.02.68-1.6.91-.36.15-.58.53-.58.92 0 .72.73 1.18 1.39.91.8-.33 1.55-.77 2.22-1.31l1.34 1.34a.996.996 0 101.41-1.41L5.05 3.63c-.39-.39-1.02-.39-1.42 0zM19 12c0 .82-.15 1.61-.41 2.34l1.53 1.53c.56-1.17.88-2.48.88-3.87 0-3.83-2.4-7.11-5.78-8.4-.59-.23-1.22.23-1.22.86v.19c0 .38.25.71.61.85C17.18 6.54 19 9.06 19 12zm-8.71-6.29l-.17.17L12 7.76V6.41c0-.89-1.08-1.33-1.71-.7zM16.5 12A4.5 4.5 0 0014 7.97v1.79l2.48 2.48c.01-.08.02-.16.02-.24z"/>
                </svg>
              {:else if volume <= 0.5}
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M18.5 12c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM5 9v6h4l5 5V4L9 9H5z"/>
                </svg>
              {:else}
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
                </svg>
              {/if}
            </button>

            <input
              type="range"
              class="volume-slider"
              min="0"
              max="1"
              step="0.01"
              bind:value={volume}
              on:input={(e) => videoElement.volume = parseFloat(e.target.value)}
            />

            <div class="time-display">
              {!isLive && <span>{formatTime(currentTime)} / {formatTime(duration)}</span>}
            </div>
          </div>

          <div class="right-controls">
            <div class="settings-menu">
              <button
                on:click={() => showSettings = !showSettings}
                class="settings-btn"
                aria-label="Settings"
              >
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/>
                </svg>
              </button>

              {#if showSettings}
                <div class="settings-dropdown">
                  <div class="settings-section">
                    <h4>播放速度</h4>
                    {#each [0.5, 0.75, 1, 1.25, 1.5, 2] as rate}
                      <button
                        on:click={() => setPlaybackRate(rate)}
                        class:active={playbackRate === rate}
                      >
                        {rate}x
                      </button>
                    {/each}
                  </div>

                  {#if qualityLevels.length > 0}
                    <div class="settings-section">
                      <h4>画质</h4>
                      <button
                        on:click={() => setQuality(-1)}
                        class:active={currentQuality === 'auto'}
                      >
                        自动
                      </button>
                      {#each qualityLevels as level}
                        <button
                          on:click={() => setQuality(level.id)}
                          class:active={currentQuality === level.id}
                        >
                          {level.label}
                        </button>
                      {/each}
                    </div>
                  {/if}
                </div>
              {/if}
            </div>

            <button on:click={toggleFullscreen} class="fullscreen-btn" aria-label="Fullscreen">
              {#if isFullscreen}
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z"/>
                </svg>
              {:else}
                <svg width="24" height="24" viewBox="0 0 24 24">
                  <path fill="currentColor" d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>
                </svg>
              {/if}
            </button>
          </div>
        </div>
      </div>
    {/if}
  </div>
</div>

<style>
  .video-player {
    position: relative;
    background: #000;
    max-width: 100%;
    margin: 0 auto;
    user-select: none;
  }

  .video-container {
    position: relative;
    width: 100%;
    height: 100%;
  }

  .video-element {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: contain;
  }

  .video-controls {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
    padding: 10px;
    color: white;
    transition: opacity 0.3s;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    z-index: 10;
  }

  .controls-top {
    display: flex;
    justify-content: flex-end;
  }

  .live-indicator {
    background: rgba(255, 0, 0, 0.7);
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: bold;
  }

  .live-indicator:not(.live) {
    background: transparent;
  }

  .progress-bar {
    position: relative;
    height: 5px;
    margin: 10px 0;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 2px;
    cursor: pointer;
  }

  .progress-filled {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background: #ff0000;
    border-radius: 2px;
  }

  .seek-slider {
    position: absolute;
    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: pointer;
    z-index: 2;
  }

  .controls-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .left-controls {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .right-controls {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  button {
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    padding: 5px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  button:hover {
    background: rgba(255, 255, 255, 0.1);
  }

  .volume-slider {
    width: 60px;
    height: 4px;
  }

  .time-display {
    font-size: 14px;
  }

  .settings-menu {
    position: relative;
  }

  .settings-dropdown {
    position: absolute;
    bottom: 100%;
    right: 0;
    background: rgba(28, 28, 28, 0.9);
    border-radius: 4px;
    padding: 10px;
    min-width: 150px;
    margin-bottom: 5px;
  }

  .settings-section {
    margin-bottom: 10px;
  }

  .settings-section:last-child {
    margin-bottom: 0;
  }

  .settings-section h4 {
    margin: 0 0 5px 0;
    font-size: 12px;
    color: #ccc;
  }

  .settings-section button {
    display: block;
    width: 100%;
    text-align: left;
    padding: 5px;
    font-size: 14px;
  }

  .settings-section button.active {
    color: #ff0000;
  }

  input[type="range"] {
    -webkit-appearance: none;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 2px;
    height: 4px;
  }

  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #fff;
    cursor: pointer;
  }

  input[type="range"]::-moz-range-thumb {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #fff;
    cursor: pointer;
    border: none;
  }
</style>
```


总结：deepseek 生成的组件功能过于冗余复杂，无法贴合我的项目，导致复用性很差，调研需要浪费大量时间。不懂我的代码库是什么。



## Zulu
## 🎁 Zulu 🎁
# **① 实现能力**
可以直接生成视频播放组件，并且自动把需要的依赖全部搞定。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e0f1680113964bf495a78bab491f367e&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c0cb90ef8b6746c08bd94a8eed0c7da6&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3160244a87fd42c7a500d80bf494976f&docGuid=AfcHTn4uU_acj7 "")
总结：生成时间略长，大概几分钟，不过更加贴合于项目，会读取代码库，生成的组件可以直接在代码库使用，无需从其他平台复制粘贴，并且可以根据自己的要求随时mock数据。



# 技术详设
*AI平台：*[ChatGpt](https://chatgpt.com/)、[deepseek](https://www.deepseek.com/)、zulu



**所存在的问题： **

1. 把设计思路转换成书面化的文档费时；
2. 前置调研多种实现方案时费时；
3. 画数据流转、交互流程等流程图费时；



**描述：**

举个🌰：以“帮我根据 XXX（电商场景搜索直播、主播、商品名称时，支持展示推送关键词的）需求，并需要 XXX 功能（将关键词与搜索词首部匹配，相同就高亮的需求），帮我写一份使用 XXX框架结构（ sveltejs 的框架）的（前端）技术详设文档，要求包含数据流转、数据设计、交互设计的相关内容，必要部分用流程图展示”为 prompt 进行提问



**以下是各个 AI 引擎回复对比：**

## ChatGpt
## 🎁 Chatgpt 🎁
# **① **目标 & 范围 
粗略描写需求功能作为目标

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e5bc1af740f7456888ef1c40edad62d6&docGuid=AfcHTn4uU_acj7 "")
# **② **架构与组件设计 
拆分实现本次功能所涉及到的组件设计及其功能（实际无法与代码库中的组件对应）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bcb1570747c3487b91e149a7afccfa33&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=af8127c5c4464f159be5db33c31266ce&docGuid=AfcHTn4uU_acj7 "")
# **③ **数据与接口设计
默认会设计出 TS 类型的设计结构，更加直观，定义了接口的出入参以及接口名，默认会用前端框架存储状态

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=12f854e130d14a81a9a2fd7032a76f3c&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6438c11bd139479393efa0cb82f215b1&docGuid=AfcHTn4uU_acj7 "")
# **④ **数据流转设计
提供 mermaid 形式的数据流程图（有的时候无法直接使用，可能存在格式问题），提供伪代码实现关键功能

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4a12119dd74c4040be5a849aae23a75f&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3723feafd0504a16a453231474a55850&docGuid=AfcHTn4uU_acj7 "")


# **⑤ **匹配与高亮算法
拆分核心前端实现的逻辑做为文档某一模块，代码实现里会提供必要解释和说明，甚至会补充说明，为什么代码实现采取方案 A 而不采取方案 B

（优点：对比方案）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=66a2560a8b6a4289af6b34f267700d9c&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=53c80ee7fe154be3807304fe77787c79&docGuid=AfcHTn4uU_acj7 "")
# **⑥ **交互设计
交代需求功能展示各个不同操作（功能）可能会触发的不同形式的交互形态

（优点：展示很多细节）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d42b358fb7d54b1f9354b163cef7dcfc&docGuid=AfcHTn4uU_acj7 "")
# **⑦ 性能与容错**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a76f2f92c8e945648f99b497ee431cca&docGuid=AfcHTn4uU_acj7 "")
# **⑧ 埋点与可观测性**
提示哪些行为和阶段上报埋点，以及上报的关键信息

（优点：可以全方面的罗列一些必要的埋点数据）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a532af0704294fb7ac83ed2c859566ec&docGuid=AfcHTn4uU_acj7 "")
# **⑨ 测试清单**
列举与需求功能相关的测试功能

（优点：适合联调阶段测试边界case）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4c7bcf1c00a14c78b92c8716dfa4cdc6&docGuid=AfcHTn4uU_acj7 "")
# ⑩ UI 示意与流程
使用 mermaid 展示详细的交互流程

（优点：展示很多细节）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ab47ad570d2b4e259b231e415af66b19&docGuid=AfcHTn4uU_acj7 "")
# ⑪** 目录结构**
不推荐

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1ebb071a3e8f4925889657a01c35cb51&docGuid=AfcHTn4uU_acj7 "")
# ⑫** **关键代码片段
提供与需求功能相关的关键代码片段

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e0cf2545e64348f1908e7f81614a0d87&docGuid=AfcHTn4uU_acj7 "")
总结：ChatGpt 生成的详设文档拆分点比较细致，涵盖了上述的 12 个模块。详设文档优缺点并存。



优点：

1、功能拆分较为细致，可以把背景、核心代码片段、数据和组件设计的比较细节

2、提供测试清单、埋点思路，非重要的内容在文档中也有标识“建议”

3、代码实现提供对比方案



但是其中存在以下问题：

1、ChatGpt 生成的流程图提供的是 mermaid 源码，但是少数情况此源码因为结构问题，无法直接转换成流程图，对不会 mermaid 语法的开发者来说，并不方便

2、上述 12 个模块有的功能定义并不清晰，可能存在讲的是「同一功能或同一归类」但却分成了多个模块，比如说「关键代码片段」和「匹配与高亮算法」，这两个模块本质都是功能代码的实现，但是却分成了两个部分。

3、因为我的 prompt 里有写「数据流转、数据设计、交互设计」，所以 ChatGpt 帮我生成的文档里有包含我问的问题的模块有「数据与接口设计、数据流转设计、交互设计、UI 示意与流程」，这些模块可以满足我的问题，但是功能区分上却差强人意，尤其是 UI 示意与流程，内容其实与上面的流程高度相似。



## deepseek
## 🎁 deepseek 🎁
# **① **功能概述
粗略描写需求功能作为目标

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=c9e9d3ecb97d4bf6a039f43199406357&docGuid=AfcHTn4uU_acj7 "")


# **② 数据设计与流转**
使用 TS 类型定义关键的数据结构，并且提供了可 mock 的数据，同时提供了前端组件设计的 props

（优点：流程图清晰可见）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0c4d903f5da7497dab881ca681b2bd8b&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4a4868fdc7164533a2570d373a561faa&docGuid=AfcHTn4uU_acj7 "")


# **③ 交互与功能设计**
用文字形式描写功能的起始态到终态的一个流程，并且提供了需求功能关键的代码实现

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2031beded50a42c18d650c1f7601bde1&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=41fcd47b37154ea783a38dc7b2ba2d4e&docGuid=AfcHTn4uU_acj7 "")


# **④ Svelte 组件详细设计**
此处代码实现了完整的组件设计和代码实现

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2acf42cc65b549c0a1bd21242804eea6&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=692f780ddaad41cbbe67719529fedff4&docGuid=AfcHTn4uU_acj7 "")
# **⑤ 注意事项**
简短的介绍了性能方面的注意事项

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=101889e20af14d88a5821cc231a82392&docGuid=AfcHTn4uU_acj7 "")
总结：deepseek 生成的详设文档使用 5 大模块就完成了整个功能的设计，其中包含了数据结构设计，（还贴心的提供了 mock 数据），提供的流程图直观可见，无需转义，全篇虽然只有一个图，但是可以清晰明了的展示交互和数据流转的流程。





## Zulu
## 🎁 Zulu 🎁
# **① **需求概述
粗略描写需求功能作为目标

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d4407e55dde5485e93629e5ad92e3231&docGuid=AfcHTn4uU_acj7 "")


# **② 系统架构**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4630f6110196484885ecc1befde92f45&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f018289dbcb140698b1da2eb71256b90&docGuid=AfcHTn4uU_acj7 "")
# **③ **数据设计
设计数据结构以及接口路径

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=946a376b6f0b416a863afe90bced4027&docGuid=AfcHTn4uU_acj7 "")


# **④ 组件设计系统架构**
在原有组件（**SearchInput**）上增加新的功能，同时新增新组件（**SuggestionList**）进行功能扩展

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=04711784f96c48f89e999e93fe6ba1fa&docGuid=AfcHTn4uU_acj7 "")


# **⑤ 交互流程**
详细画出交互流程图

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b1c7d5ca463b4938bb16e99271a0bd9b&docGuid=AfcHTn4uU_acj7 "")


# **⑥ 核心算法**
提供需求功能所需的核心逻辑

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3251edad93554d26afc1326e83df756f&docGuid=AfcHTn4uU_acj7 "")


# **⑦ 样式设计**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aa1e957ebafe4686961e693e58dc1496&docGuid=AfcHTn4uU_acj7 "")
# **⑧ 性能优化**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=439a0d16829c40d7ae2beb22d5279da5&docGuid=AfcHTn4uU_acj7 "")
# **⑨ 错误处理**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=883aef10f3834b4ebdb6d10477aef269&docGuid=AfcHTn4uU_acj7 "")
# ⑩** 测试策略**
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3f9779c1e4fe494d90091b036b2dfc17&docGuid=AfcHTn4uU_acj7 "")
# ⑪** 部署说明**
其实就是 Zulu 添加的每个文件的路径

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a41979cefaf8479b969a4dc37291ecb6&docGuid=AfcHTn4uU_acj7 "")
# ⑫** 后续优化**


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d062ccaf10f1471b93315eeed1a60613&docGuid=AfcHTn4uU_acj7 "")


总结：因为 Zulu 是运行在 IDE 里的内容，所以，他在帮助我生成详设文档时，也快速的帮我生成了功能代码。

## 终极对比
一般研发写详设时更多的是把需求文档的背景和目标作为详设的第一部分，也就是「目标 & 范围」、「功能概述」、「需求概述」模块，所以三种 AI 工具的详设文档第一部分都不做具体的分析。

### 文档结构 & 内容设计
## ChatGpt
## deepseek
## Zulu
总结：

1、拆分的模块较细，且有一部分模块内容语义不清，有点重复（「UI示意与流程」「数据流转设计」），一部分不具有参考意义（「目录结构」）

2、细节拆分较为散乱（「关键代码」和「匹配高亮算法」「组件设计」模块之间没有连续性，总会插入其他内容）

3、👍🏻具有埋点功能、提供测试（联调）case

4、👍🏻核心逻辑实现可以对比方案

总结：

1、👍🏻模块少但有逻辑性，前后衔接较为明确

2、👍🏻提供完整的详细设计代码

3、👍🏻提供 mock 数据



总结：

1、👍🏻可直接在代码库生成代码

2、有些模块并没用处（「部署说明」）

3、除了核心关注的数据流转交互设计外其他的模块提供的内容很泛泛，没有借鉴用处（「测试策略」、「错误处理」）

||ChatGpt|deepseek|Zulu|
|-|-|-|-|
|文档可读性|▼|▲|▲|
|文档结构性|▼|▲|▼|
|核心代码生成能力|▼|▲|▲|
|细节处理|▲|▲|▲|

### 流程图
## ChatGpt
## deepseek
## Zulu
总结：

1、提供 mermaid 源码，但是无法原地预览成图片，需要复制到别处预览

2、👍🏻预览后内容逻辑较为完整，

3、提供的流程图过多，需要检索哪个图更好，更有可用性

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f1ca97c1535a4e129bbba7ff48c66dbe&docGuid=AfcHTn4uU_acj7 "")
预览：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f532d0b608d04344ac5303acac272485&docGuid=AfcHTn4uU_acj7 "")
总结：

1、👍🏻可直接原地预览

2、内容表述上较弱，流程并不完整

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7e43504cb2ad434c9f257a7518724413&docGuid=AfcHTn4uU_acj7 "")


总结：

1、可在 IDE 里预览 mermaid 源码，并且可生成流程图、👍🏻序列图

2、👍🏻使用序列图描述功能更加直观，表达的内容较完整

3、流程图内容和展示形态一般，不具参考意义

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=788cea7461b64b26820dc7f98c2bafb4&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8c87a1d560994dff9cb09585f3b92e34&docGuid=AfcHTn4uU_acj7 "")


||ChatGpt（取最好的图）|deepseek|Zulu（取序列图）|
|-|-|-|-|
|便捷性|▼|▲|▲|
|完整性|▲|▼|▲|
|逻辑性|▲|▲|▲|



# 实际开发


##### UI 稿自动生成
根据figma的链接让zulu生成组件

# zulu
### 输入
1、复制figma链接

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=908c1ee0e7c34be3a524093484233844&docGuid=AfcHTn4uU_acj7 "")
2、选择f2c

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=52aeb8004e7d4919b0f635d42305416c&docGuid=AfcHTn4uU_acj7 "")
3、开始输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=75f65c76c45747a887b2ca0aefdd5f93&docGuid=AfcHTn4uU_acj7 "")
输入figma链接然后开始执行

### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7a76559cc2f94565941fc333ab9acd16&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=da123dbbcf66445b91c395212122cb70&docGuid=AfcHTn4uU_acj7 "")




### 效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=87abeb263b514d04ae0dba5222c49ba7&docGuid=AfcHTn4uU_acj7 "")


创建某个组件

# zulu
### 输入
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=502893b4adf34f9c989566be0946f5ea&docGuid=AfcHTn4uU_acj7 "")
### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=610c7238e7b64a78a1e6b7b76873b095&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=175a5db4db62498db55d4917a6b71ffd&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=a6165a122f984ecbab35fdad90c8b29a&docGuid=AfcHTn4uU_acj7 "")
### 效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=208203311e134eeab02b0e5f6982afdf&docGuid=AfcHTn4uU_acj7 "")
生成效果图：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=375521db96e74fb59b4d2f37425792e4&docGuid=AfcHTn4uU_acj7 "")


##### *逻辑补全*
js功能生成

# zulu
### 输入
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=09f41c1984714b21973d1bfcd70fbc31&docGuid=AfcHTn4uU_acj7 "")


### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=520cd0c94843415294b2280a0f652a0b&docGuid=AfcHTn4uU_acj7 "")
生成mock数据



# gpt
### 输入
1、打开官网

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bba3b3f241b743a186a45aa833739e3d&docGuid=AfcHTn4uU_acj7 "")




2、开始输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b8e7499e9f9244e3bb6ddac68ca6ae65&docGuid=AfcHTn4uU_acj7 "")
输入需求然后回车开始执行

### 生成


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=378ad212ae074e1e8d68ba242f12a7d1&docGuid=AfcHTn4uU_acj7 "")




### 效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fa3f341e766046ed838ffffd3bc86f00&docGuid=AfcHTn4uU_acj7 "")


代码自动补全

# **copliot**
### 输入
1、打开开发工具拓展 搜索Copliot

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=aab2e3058a2e4da6b7b70c56adcf6d97&docGuid=AfcHTn4uU_acj7 "")




2、点击安装 激活组件

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=376db2b62c784b1e8ae43ec0edc313a2&docGuid=AfcHTn4uU_acj7 "")
3、打开聊天 登陆账号激活免费版

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=974562ded1fb4daca44bb9c4aa7bf8e8&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=44ad357b915b469e9973c7fe5c6e90f5&docGuid=AfcHTn4uU_acj7 "")
4、编码自动触发补全

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=91f206d6ebde489c9c85ecc236cadfc6&docGuid=AfcHTn4uU_acj7 "")
### 生成


样式回车后可自动继续补全

写好注释可以帮助补全 js 和 html





### 效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bfddbfc664c24b1cb245faea16a90271&docGuid=AfcHTn4uU_acj7 "")




组件添加某个功能



# zulu
### 输入
1、打开拓展，搜索并安装好插件，然后点击拓展组件图标打开对话框

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=532ba7079dfa406c871befd42bb01884&docGuid=AfcHTn4uU_acj7 "")
2、开始输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=30b8b5a5a252473d962429807cabd698&docGuid=AfcHTn4uU_acj7 "")
输入需求然后回车开始执行

### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1550aec728234ec2b7a2485057ead5ab&docGuid=AfcHTn4uU_acj7 "")






### 效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bda2e6f9737d4db691ff014313a9002c&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=297f944264f1497c85f728ac3d69ce2f&docGuid=AfcHTn4uU_acj7 "")
##### *代码优化*
ui组件库调整



# gpt
### 输入
1、打开官网

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bba3b3f241b743a186a45aa833739e3d&docGuid=AfcHTn4uU_acj7 "")


2、开始输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8f1579f331c24b84a4138db0e60be57e&docGuid=AfcHTn4uU_acj7 "")
输入需求然后回车开始执行

### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5ec8583aab7c40fdba6d19029698033c&docGuid=AfcHTn4uU_acj7 "")






数据结构调整



# cursor
### 输入
1、打开官网 下载软件 将文件拖入cursor内，打开要更改的文件，右键鼠标选第二个，创建AI对话

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6e1093a7eadc4125b225161662aff191&docGuid=AfcHTn4uU_acj7 "")




2、在右侧对话框输入需求

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=87545e8af7044d7b87fbd486ae18a9dd&docGuid=AfcHTn4uU_acj7 "")
输入需求然后回车开始执行



### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=9a152ad279b540459ca8dc7be5fc7356&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1df527b2492f42b5aa188d6775fd387c&docGuid=AfcHTn4uU_acj7 "")






### 效果
修改前

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=340746a7146848cfbb29198d428995e2&docGuid=AfcHTn4uU_acj7 "")


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1c81c2572e284c27a4b864d3ecd5e650&docGuid=AfcHTn4uU_acj7 "")
数据定义类型部分拆分



# cursor
### 输入
1、打开要更改的文件，右键鼠标选第二个，创建AI对话

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=6e1093a7eadc4125b225161662aff191&docGuid=AfcHTn4uU_acj7 "")




2、 在右侧对话框输入需求（可选需要更改文件）

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1bcafec600c64ca5baf490c460794332&docGuid=AfcHTn4uU_acj7 "")
输入需求然后回车开始执行

### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2d0e1752d5d34ed38e56acf55b2d0e67&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0105c03f5e5d429e8b2f60471c358b83&docGuid=AfcHTn4uU_acj7 "")




### 效果
修改前

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3c2948a133534748830780c9f0fdbfef&docGuid=AfcHTn4uU_acj7 "")
修改后

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1c81c2572e284c27a4b864d3ecd5e650&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fa422739bbcf44b8bcbc0656a88575fd&docGuid=AfcHTn4uU_acj7 "")
代码逻辑简化



# Deepseek
### 输入
1、打开官网 手机号注册，进入对话框聊天界面







2、开始输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=779c739f2d7444eead78bd6553ea894c&docGuid=AfcHTn4uU_acj7 "")
输入需求然后回车开始执行

### 生成


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=0db4d8274ee046e580bcc939e5786ec0&docGuid=AfcHTn4uU_acj7 "")




对已有结构进行改造后复用



# zulu
### 输入
1、打开拓展，搜索并安装好插件，然后点击拓展组件图标打开对话框

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=532ba7079dfa406c871befd42bb01884&docGuid=AfcHTn4uU_acj7 "")




2、开始输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=48f4c46d2fdd4a6d9aa44cd81890e91c&docGuid=3Pt9ghhFkMIZA4 "")
输入需求然后回车开始执行

### 生成


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e858a4a178d34b348787ba0e67dbe0db&docGuid=AfcHTn4uU_acj7 "")




复杂页面组件拆分



# zulu
### 输入
1、打开拓展，搜索并安装好插件，然后点击拓展组件图标打开对话框

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=532ba7079dfa406c871befd42bb01884&docGuid=AfcHTn4uU_acj7 "")




2、开始输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=57d5e0f57cf64f6abad5d156e431f97c&docGuid=AfcHTn4uU_acj7 "")
输入需求然后回车开始执行

### 生成


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=299bbf67342c4f9e8eab7d832cbdf964&docGuid=AfcHTn4uU_acj7 "")




### 效果
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=820872b4fc2647d1823be118c5dbf4bf&docGuid=AfcHTn4uU_acj7 "")




##### 改错能力
解决报错

# gpt
### 输入
使用方式：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=939c7b960a50401ba7bfc1ced0b3e7dd&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1dbba34feb6d46e4976a01cd710ccecf&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f084cb0f234b4b7c8424197a605d4407&docGuid=AfcHTn4uU_acj7 "")
注释：一次性发送相关代码以及问题 或者先发送问题再追加相关代码

### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=695bdce2a6b04ce5a917f9054ebaf69a&docGuid=AfcHTn4uU_acj7 "")


### 备注
优点：

1、快速指出问题所在，并给出解决问题的方案

2、减少试错时间与次数，有效的节省开发时间

缺点：

1、不能使用最高级Ai

2、需要使用代理



场景问题

# 豆包
### 输入
对话框输入

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=50f0299886f54c429b3c7f79767f6fb5&docGuid=AfcHTn4uU_acj7 "")


### 生成
给出场景问题，给出几个方案

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d0a9855aee0241dcb11d09241e97a3d6&docGuid=AfcHTn4uU_acj7 "")


定义问题所在

# sider
### 输入
有问题的代码放在输入框内，问其存在的问题

### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8d74de223c2b434cb975fd6350f2929c&docGuid=AfcHTn4uU_acj7 "")
定义问题所在

# zulu
### 输入


![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=194e9d09ed2a40ada6607836e975190e&docGuid=AfcHTn4uU_acj7 "")
### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=69f812f94a86416bb6dc5009675eb7a3&docGuid=AfcHTn4uU_acj7 "")


# CR阶段
检索差错

# cr平台
### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d06ae9eae128493bb954a70f9afe2ed9&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f75ac402efc24e149e60fc9b790128df&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ed621abaf0fd441db24e81df1e22a383&docGuid=AfcHTn4uU_acj7 "")
### 优点
1、流水线检测，报错时自动触发

2、快速定位问题所在，并尝试解决问题

cr修正

# cr平台
### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4937fa8190a5454a99f6fe31126d8b9b&docGuid=AfcHTn4uU_acj7 "")
问题收集：[CR问题记录](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/eHqYxS5Gga/ljTWnfgngQMGSk?t=mention&mt=doc&dt=doc)

### 优点
1、能快速的对本次修正的代码进行一个质量评估

2、分析出所有可能出现的问题，在根据实际情况看是否采纳建议







# 上线阶段
上线注意事项

# zulu
### 生成
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=e5874ca1a1044a2a8d3352f34af85ce7&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=62adaea474e740a89efb7be969a31874&docGuid=AfcHTn4uU_acj7 "")
### 使用教程
1、安装baidu Comate插件

2、可以让zulu分析上线注意事项

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=23618a0f9d184c84b804d5c1a3eabbb9&docGuid=AfcHTn4uU_acj7 "")


### 优点
能快速速的定位到上线时需要注意的一些文件，比如环境变量、定制备份策略和回滚计划等



# case list 编写
*AI平台：*[QAMate平台](https://qamate.baidu-int.com/lazymind/#/case/index)



**背景： **

在电商等产品线中，整理和留存接口 castlist 是项目测试的基本要求。如果需要从详细设计文档中手动摘抄接口内容并梳理测试点，这一过程耗费大量时间和精力。为了降低工作成本，提高测试效率，可以用QAMate智能生成接口测试用例，降低测试用例梳理的成本。

****

## AI赋能
[QAMate平台地址](https://qamate.baidu-int.com/lazymind/#/iteration/case/mind-case?caseId=69326&modelId=71549&planId=495&status=edi)

1. 点击智能用例生成
2. 将接口文档的接口信息粘贴到文本框内
3. 选择生成策略选择
4. 点击生成按钮

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8f90a72cf4fd4d088c39a144b9f598c3&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=fbcf48923ccd421eb48540898cce310c&docGuid=AfcHTn4uU_acj7 "")
**生成效果图如下：**

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=afbcbc24e50a452b9ef18dcc03908bbd&docGuid=AfcHTn4uU_acj7 "")
#### 优势
1. 快速生成用例，节省 80%时间
2. 结构统一，降低阅读成本
3. 自动识别基础测试点
4. 修改接口后重新生成即可
5. 需要人工校验参数层级

### VS* *
## *传统实现*
选择用例模板，根据需求内容手动编写用例

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d76f2d2894664ad8a596961721251bc8&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1902947aefd845259cb033d76a47c52a&docGuid=AfcHTn4uU_acj7 "")
#### *劣势*
1. 手动编写耗时较长
2. 依赖个人习惯，差异较大
3. 可能遗漏边缘情况 
4. 修改接口后，需要人工逐项更新
5. 需要人工校验参数层级
6. 人工编写更准确但易出错

#### 优势
1. **准确性更高**：人工编写的测试用例能更精确地反映业务逻辑和特殊场景需求
2. **灵活性更强**：可以根据具体业务场景定制化设计测试用例
3. **深度验证**：人工可以设计更复杂的测试场景和边界条件
4. **上下文理解**：QA同学对系统整体架构和业务逻辑有更深入的理解



☞AI 赋能主旨：AI 和人工优势结合，达到用例生成效率最高、内容最优的效果。



**⚠️ 使用注意事项：**

1. 粘贴格式要求：

    * 接口信息应包含：接口名、接口路径、request json、response json
    * 表格形式说明请求参数和返回参数
    * 对于升级接口，如果只有返回值，需备注"返回："帮助模型理解

2. 调优手段：

    * 如果生成效果不符合预期，可尝试重新生成
    * 参数层级超过 2 层时可能需要手动调整层级关系
    * 返回值校验可能较简单，需要人工补充
    * 详设中升级接口只写了返回值时，需明确标注



**✍️ 最佳实践**

关注QAMate相关团队发布的使用文档[接口脑图用例生成说明](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/idq01nNOS2/NvEFhklV-m/-6NvR8KBCamQ6z?t=mention&mt=doc&dt=doc)，包含使用方式和一些业务方的实验数据，有助于用例生成和调优。

# 测试阶段
*AI平台：数字员工、智能交付助手*

上官测测：电商测试团队数字员工，支持需求交付推进、智能问答、环境搭建/更新、数据构造等。



### ** 数字员工「上官测测」使用场景**
使用方式：搜索后拉入群聊即可使用，具体使用方式参考[营销智能构造工具使用手册](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/xjMBfz2EF4/srQyMBPKxc/WEAoHR2CwVjdGz?t=mention&mt=doc&dt=doc)[上官测测使用说明（持续更新）](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/yowPX4M1kS/1QvY-0s6YSzyKZ?t=mention&mt=doc&dt=doc)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=7543d02766ad4e2f91f0f5cf591a1a18&docGuid=AfcHTn4uU_acj7 "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=8e39bbc0862b4de5844b28511304c0a4&docGuid=AfcHTn4uU_acj7 "")
##### **🚩 代码更新提醒&测试环境更新**
---

1. 代码更新提醒

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f503a533d15b4fafb8616094f69525ae&docGuid=AfcHTn4uU_acj7 "")
2. 环境更新

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=21db0eda746f4ce5a46a964a7de1c0ea&docGuid=AfcHTn4uU_acj7 "")
##### **🚩 优惠券**
---

1. 创建优惠券：“创建一张优惠券”

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b1f305815453485fa587e82b3575a8f1&docGuid=AfcHTn4uU_acj7 "")
2. 核销优惠券：“核销用户已领取未使用优惠券：pass_id=xx, batch_id=xx”

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=22bc0f30e81941b0858ed2248b90d076&docGuid=AfcHTn4uU_acj7 "")
##### **🚩 黑名单设置**
---

1. 黑名单查询

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f17c7429543646ec81b48cc40703e3fc&docGuid=AfcHTn4uU_acj7 "")
2. 黑名单设置

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=1ee1c2ffffe4411396cce36a23cb8e49&docGuid=AfcHTn4uU_acj7 "")
3. 黑名单删除

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=dc7540a4b2f6459aab6aa76263fb9606&docGuid=AfcHTn4uU_acj7 "")
##### 
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=d78e84179e97469fb6787a428fab7e98&docGuid=AfcHTn4uU_acj7 "")


##### **🚩 其他**
---

1、pass投流店铺设置

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=3df5cb4141bf40e0a34c85a5bf6e86a0&docGuid=AfcHTn4uU_acj7 "")
2、资源位配置

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2278e7a770b94fc39db8723affd03649&docGuid=AfcHTn4uU_acj7 "")
3、信息查询

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=37f6f3377f4544d3a45a1f31ef5b37ef&docGuid=AfcHTn4uU_acj7 "")






# 有奖互动
即日起至**9月24日18:00**，在评论区留言，任选下方2个问题回复：

####  1.你有哪些AI Coding技巧？
####  2.你对AI Coding看法或期待是什么？
我们将挑选5个走心评论，特别送上【BIT蛇年小熊或国潮小马摆件盲盒】～

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=2a7c5b9ff7d243d8b692b4c792305038&docGuid=r1nLoPXfl6WVyP "")
![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=171d9294cef444d1adcf00fcbbf6c758&docGuid=r1nLoPXfl6WVyP "")
### 本期获奖公示
恭喜[@陈小珊](https://ku.baidu-int.com?t=mention&mt=contact&id=bad72720-99b8-11f0-a497-c335850b5156)[@莫子桓](https://ku.baidu-int.com?t=mention&mt=contact&id=d194afa0-99b8-11f0-a497-c335850b5156)[@符琴](https://ku.baidu-int.com?t=mention&mt=contact&id=dd3e5f90-99b8-11f0-a497-c335850b5156)[@高瑜](https://ku.baidu-int.com?t=mention&mt=contact&id=f4c44120-99b8-11f0-a497-c335850b5156)[@刘思冰](https://ku.baidu-int.com?t=mention&mt=contact&id=fb78de40-99b8-11f0-a497-c335850b5156)在本期评论中获奖，

请联系[@李思晗](https://ku.baidu-int.com?t=mention&mt=contact&id=536e8780-9545-11f0-8779-377dcb67db40)领取奖品（非科技园工区伙伴可邮寄）~❤️

# [AI+社区首页](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/opdELIFv2_oFZg)
## [📒 查看/分享更多案例](https://ku.baidu-int.com/knowledge/HFVrC7hq1Q/pKzJfZczuc/WjGjiS_SK_/_U6EhhLx7F5_DI)
更多厂内AI实践案例、案例投递入口

## [📪 创作者投稿](https://ku.baidu-int.com/share/shr5MRDhohjq9dAlY9MCQ/fomaWTzCTogCK4wkc3&spaceId=spcC9AM3yK7rD)
产研干货文章、AI洞察、个人AI技巧

## [🔧 AI工具箱](https://tools.baidu-int.com/)
厂内外热门工具，一键使用

###### **🌟欢迎星标本文、评论区点赞、投币、留言**   [👗社区如流群](https://applink-infoflow.baidu.com/share/contact/open/?token=ZDbWqAs7nQEaXdmgxb6vizK7WFPKWNeibo75Ua-D0_M)    👆更多AI板块点击上方，即刻跳转
