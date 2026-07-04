# 03. 连接第三方中转 API

第三方中转 API 是本仓库原来的重要入口，改造成教程站后也不要丢。它的定位是：帮助不想自备网络环境、不想处理海外支付、不想从零配置 API 的用户更快跑通。

## 现有入口

| 用途 | 链接 |
| --- | --- |
| 国内站登录 | `https://codex.chatgpt-plus.top/login` |
| 备用入口 | `https://codex2.chatgpt-plus.top/login` |
| Codex&GPTimage2 套餐 | `https://maynorai.jichiyun.sbs/buy/30` |
| 配置中转 API | `https://maynorai.jichiyun.sbs/buy/13` |
| cc-switch 下载 | `https://github.com/farion1231/cc-switch/releases/` |
| 飞书配置教程 | `https://ai.feishu.cn/wiki/JnefwEQRKiNyg6kTnN4cNphnnSh?from=from_copylink` |
| 完整上手教程 | `https://my.feishu.cn/wiki/Vjulwif06izNiMkPor0cM9uYn1e` |

## 它解决什么问题

- 不想自己处理网络访问环境。
- 不想研究官方订阅和支付路径。
- 想直接配置 API 后开始使用。
- 想把 Codex、图像模型和日常工具放到一个可用方案里。

## 它不是什么

第三方中转不是 OpenAI 官方订阅。教程里要说清楚这一点，避免用户误解。

推荐表达：

> 国内站和中转 API 属于第三方接入方案，不是 OpenAI 官方订阅。它的价值是快速可用、低门槛和更省配置时间。

## 安全配置原则

- API Key 只通过环境变量或工具配置页保存。
- 不要把 API Key 写进仓库。
- 不要把 API Key 发给 Codex 让它直接贴到代码里。
- 不要在截图、日志、README 中暴露 key。
- 如果要让 Codex 帮你排查，提供错误类型，不提供完整密钥。

## 完成标准

你完成这一章时，应该能回答：

- 我现在走的是官方订阅，还是第三方中转？
- 登录入口是哪一个？
- API 配置在哪里？
- 哪些信息不能发给 Codex？

