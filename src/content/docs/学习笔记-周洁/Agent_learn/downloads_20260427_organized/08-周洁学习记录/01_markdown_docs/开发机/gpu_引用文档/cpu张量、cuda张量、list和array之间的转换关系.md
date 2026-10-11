---
title: "int -> tensor -> int"
description: "cpu张量、cuda张量、list和array之间的转换关系"
date: "2026-04-28"
category: "学习笔记-周洁"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\08-周洁学习记录\\01_markdown_docs\\开发机\\gpu_引用文档\\cpu张量、cuda张量、list和array之间的转换关系.md"
---
cpu张量、cuda张量、list和array之间的转换关系

```
import torch
import numpy as np
# int -> tensor -> int
a = torch.Tensor(1)
b = a.item()
 
# list -> tensor(cpu)
l0 = [1, 2, 3]
t = torch.Tensor(l0)
 
# tensor(cpu) -> numpy -> list
a = t.numpy()
l1 = t.numpy().tolist()
 
# list -> numpy
a0 = np.array(l0)
 
# numpy -> tensor(cpu)
t1 = torch.from_numpy(a0)
 
# tensor(cpu) -> tensor(cuda)
tc = t1.cuda()
 
# tensor(cuda) -> list
l2 = tc.cpu().numpy().tolist()
```

