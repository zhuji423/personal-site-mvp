---
title: "关联代码集"
date: "2026-10-11"
category: "Agent与RAG"
source: "F:\\百度工作\\01_code\\code\\baidu\\ep-qa\\code-gen_old\\web_code_gen\\prompt\\rag_edit\\gen_code_simple.md"
---
# 关联代码集
<context>
{{search_context}}
</context>

# 用户关注信息
{{conf_context}}
{{history_context}}
{{file_context}}

# 任务目标
结合用户关注信息和需求描述，从关联代码集中精准提取相关的代码，精确理解用户需求意图并完成解答。

# 需求描述
{{query}}