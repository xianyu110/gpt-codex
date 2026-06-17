# Codex 中文实战教程

这套教程把仓库改造成一个完整的 Codex 上手站点：先解决安装、订阅、权限和基础配置，再用实战案例把 Codex 变成可以持续交付的工作流。

原来的国内站、中转 API、套餐购买和飞书教程链接继续保留，不在教程改造中删除。它们主要放在入门安装、订阅、中转 API、设置速查和 FAQ 里。

## 学习路线

| 阶段 | 适合人群 | 先看 |
| --- | --- | --- |
| 0 到 1 入门 | 第一次接触 Codex | [guide/00-overview.md](guide/00-overview.md) |
| 安装和账号 | 需要把环境跑起来 | [guide/01-install.md](guide/01-install.md) |
| 国内访问和中转 | 不想自备网络环境或想接第三方 API | [guide/03-third-party-api.md](guide/03-third-party-api.md) |
| 会用 App | 想知道每个按钮干嘛 | [guide/04-app-tour.md](guide/04-app-tour.md) |
| 会组织任务 | 想用 Plan、Threads、斜杠命令 | [guide/07-plan-mode.md](guide/07-plan-mode.md) |
| 工程化使用 | 想沉淀 AGENTS.md、Skills、MCP、自动化 | [guide/11-skills-mcp.md](guide/11-skills-mcp.md) |
| 真实产出 | 想马上做案例 | [../recipes/index.md](../recipes/index.md) |

## 入门教程

- [00-overview.md](guide/00-overview.md): 学习路线和这份教程怎么用
- [01-install.md](guide/01-install.md): 下载与安装，桌面 App 和 CLI 二选一
- [02-subscribe.md](guide/02-subscribe.md): 订阅 ChatGPT Plus / Pro
- [03-third-party-api.md](guide/03-third-party-api.md): 连接第三方中转 API
- [04-app-tour.md](guide/04-app-tour.md): 桌面 App 界面总览
- [05-config.md](guide/05-config.md): General、个性化和 AGENTS.md
- [06-permissions.md](guide/06-permissions.md): 权限与沙盒
- [07-plan-mode.md](guide/07-plan-mode.md): Plan Mode
- [08-slash-commands.md](guide/08-slash-commands.md): 斜杠命令和状态
- [09-reasoning-depth.md](guide/09-reasoning-depth.md): 推理深度选择
- [10-threads.md](guide/10-threads.md): Threads 与并行
- [11-skills-mcp.md](guide/11-skills-mcp.md): Skills 与 MCP 入门
- [12-automation.md](guide/12-automation.md): 定时任务和自动化
- [13-cli.md](guide/13-cli.md): CLI 安装、登录与第一次改代码
- [14-first-task.md](guide/14-first-task.md): 第一个可验证任务

## 实战案例

案例库在 [recipes/index.md](../recipes/index.md)。建议顺序是：

1. 先做 [README 变网页](../recipes/readme-to-web.md)，建立“让 Codex 改文件并验证”的手感。
2. 再做 [静态站部署](../recipes/deploy-static-site.md)，把结果发布出去。
3. 然后按自己的工作场景选择 PPT、Obsidian、网页采集、飞书、CI 修复等案例。

## 速查

- [commands.md](../reference/commands.md): 命令和斜杠速查
- [settings.md](../reference/settings.md): 推荐设置速查
- [safety.md](../reference/safety.md): 安全与避坑
- [faq.md](../reference/faq.md): 常见问题

