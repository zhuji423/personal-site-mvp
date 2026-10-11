---
title: "使用 CNAP CLI 对部署单进行排障"
description: "应用场景：用户给了一个部署单地址URL（通常为 console.cloud.baidu-int.com/devops/appspace 路径下，并且路径中包含'deploy'字样），并提出了相关问题。"
date: "2026-04-30"
category: "平台与接入文档"
source: "F:\\百度工作\\06_comate_aiide_config\\.comate\\skills\\cnap-comate\\references\\deploy-troubleshoot.md"
---
# 使用 CNAP CLI 对部署单进行排障

**应用场景**：用户给了一个部署单地址URL（通常为 `console.cloud.baidu-int.com/devops/appspace` 路径下，并且路径中包含'deploy'字样），并提出了相关问题。

## 典型解决思路

1. 使用 `cnap query url` 命令，通过用户给定的URL，获取到其对应的账号、环境、应用、部署单ID。
2. 使用 `cnap deploy get <部署单ID> -o json` 命令，获取部署单详情。
3. 找到有问题的步骤对应的stage和task，根据信息中带'log'的字段，获取其log文件地址。
4. 访问log地址，获取log文件并阅读，确认可能的问题点，特别要确认有问题的集群名。
5. 使用 `cnap env switch -A <账号> -C <集群名> -E <环境>` 切换到对应的环境上下文。
6. 根据上面分析到的问题，可选通过 `cnap exec` 去容器中执行命令，或者借助 `kubectl` 命令，进一步排查确认问题原因。
7. 给用户简要地解释原因，并给出解决方案。
   - 如果是偶发问题期望可通过重试解决的，向用户确认是否重试，得到肯定回答后可通过 `cnap depoly redo-stage <deployment-id> <stage-id>` 或 `cnap depoly redo-task <deployment-id> <task-id>` 进行重试。
   - 如果是外部平台的问题，可以引导通过 `zhiban-search` Skill，查询对应平台的值班表，提示用户找相关人员，相关平台值班信息，详见 `references/oncall.md`。
