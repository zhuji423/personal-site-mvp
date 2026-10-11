---
title: "开源OCR算法（带位置信息）比较"
description: "2、详情Tesseract OCR1、安装Tesseract OCR：https://tesseract-ocr.github.io/tessdoc/Installation.html"
date: "2026-04-27"
category: "视觉与图像"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\06_llm_learning_notes\\ku_export\\开源OCR算法（带位置信息）比较\\开源OCR算法（带位置信息）比较.md"
---
# 开源OCR算法（带位置信息）比较
1、汇总| 模型名称 | 简介 | 位置信息输出格式 | GitHub 链接 | 效果 |
| --- | --- | --- | --- | --- |
| Tesseract OCR | 广泛使用的开源OCR引擎，支持多种语言。 | hOCR或 ALTO格式 | tesseract-ocr/tesseract |  |
| EasyOCR | 基于深度学习的OCR工具，支持多语言。 | 文本及其边界框坐标 | JaidedAI/EasyOCR |  |
| PaddleOCR | 百度开源的OCR工具，支持多语言和多种任务。 | 文本及其边界框坐标 | PaddlePaddle/PaddleOCR |  |
| MMOCR | OpenMMLab 的OCR工具箱，支持文本检测、识别和端到端OCR。 | 文本及其边界框坐标 | open-mmlab/mmocr |  |
| Kraken | 专为古籍和历史文档设计的OCR引擎。 | hOCR或 ALTO格式 | mittagessen/kraken |  |
| OCRopus | 基于Tesseract的OCR系统。 | hOCR格式 | tmbdev/ocropy |  |
| Calamari | 基于深度学习的OCR引擎。 | 文本及其边界框坐标 | Calamari-OCR/calamari |  |
| AttentionOCR | 基于注意力机制的OCR模型。 | 文本及其边界框坐标 | emedvedev/attention-ocr |  |
| TrOCR | 微软基于Transformer的OCR模型。 | 文本及其边界框坐标 | microsoft/unilm/tree/master/trocr |  |
| DocTR | 基于深度学习的OCR库，支持文档文本检测和识别。 | 文本及其边界框坐标 | mindee/doctr |  |

2、详情Tesseract OCR1、安装Tesseract OCR：https://tesseract-ocr.github.io/tessdoc/Installation.html

以Linux为例：

apt install tesseract-ocrtesseract -v# tesseract 4.1.1tesseract --list-langs # 查看是否支持中文：简体中文 (chi_sim) 和繁体中文 (chi_tra)若不支持中文，需安装语言包：

cd /usr/share/tesseract-ocr/4.00/tessdata/  # 默认语言包目录wget https://github.com/tesseract-ocr/tessdata/raw/main/chi_sim.traineddatawget https://github.com/tesseract-ocr/tessdata/raw/main/chi_tra.traineddata2、使用：

tesseract img/zh.png zh.html -l chi_sim+eng hocr 3、效果：

很差，别用



