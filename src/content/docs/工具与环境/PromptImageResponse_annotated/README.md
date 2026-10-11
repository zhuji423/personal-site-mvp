---
title: "Image Annotation Processor"
description: "Automated image annotation tool using ByteDance's multimodal API."
date: "2026-10-11"
category: "工具与环境"
source: "F:\\百度工作\\05_downloads_keep\\PromptImageResponse_annotated\\README.md"
---
# Image Annotation Processor

Automated image annotation tool using ByteDance's multimodal API.

## Features
- Batch processing of images
- API-based annotation using ByteDance's multimodal model
- JSONL output format matching existing schema
- Incremental processing support
- Comprehensive error handling and logging

## Requirements
- Python 3.8+
- Required packages: `requests`, `pyyaml`, `Pillow`

## Installation
1. Install dependencies:
```bash
pip install requests pyyaml Pillow
```

2. Configure API access:
- Get your API key from ByteDance
- Update `config.yaml` with your credentials

## Configuration
Edit `config.yaml` to customize:
- API endpoint and parameters
- Input/output directories
- Processing options

Example configuration:
```yaml
api_key: "your_api_key"
api_endpoint: "https://api.volcengine.com/multimodal/v1/caption"
input_dir: "images"
output_path: "output/annotations.jsonl"
```

## Usage
Run the processor:
```bash
python image_processor.py
```

The script will:
1. Process all images in the input directory
2. Generate annotations in JSONL format
3. Skip already processed files (incremental mode)

## Output Format
Output matches the demo_pic.jsonl format:
```json
{
  "images": ["path/to/image.jpg"],
  "messages": [
    {
      "role": "user",
      "content": "请为这张图片生成详细的描述"
    },
    {
      "role": "assistant",
      "content": "{\"description\":\"...\",\"tags\":[...],\"confidence\":0.95}"
    }
  ]
}
```

## Incremental Processing
The processor tracks processed files in `processed_files.txt`. To reprocess all files:
1. Delete `processed_files.txt`
2. Run the processor again