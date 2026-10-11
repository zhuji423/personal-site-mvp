---
title: "benchmark_res"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\01_code\\code\\cs336\\assignment1-basics\\reference\\Stanford-CS336-spring25\\assignment2-systems\\benchmark_res.md"
---
|    | Size   | Mode                 |   d_model |   d_ff |   num_layers |   num_heads |   Context Length |   Avg Time (s) |   Std Dev (s) |   Warmup Steps |
|---:|:-------|:---------------------|----------:|-------:|-------------:|------------:|-----------------:|---------------:|--------------:|---------------:|
|  0 | small  | forward              |       768 |   3072 |           12 |          12 |              256 |       0.010419 |      0.00015  |              5 |
|  1 | small  | forward_and_backward |       768 |   3072 |           12 |          12 |              256 |       0.041006 |      0.0047   |              5 |
|  2 | medium | forward              |      1024 |   4096 |           24 |          16 |              256 |       0.023246 |      0.001855 |              5 |
|  3 | medium | forward_and_backward |      1024 |   4096 |           24 |          16 |              256 |       0.095739 |      0.009315 |              5 |
|  4 | large  | forward              |      1280 |   5120 |           36 |          20 |              256 |       0.039647 |      0.005054 |              5 |
|  5 | large  | forward_and_backward |      1280 |   5120 |           36 |          20 |              256 |       0.997725 |      0.111382 |              5 |