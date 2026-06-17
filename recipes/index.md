# Codex 实战案例库

这里是教程站的主体。入门教程解决“怎么装、怎么买、怎么配置”，案例库解决“装好以后能做什么”。

每个案例都按同一套结构写：

- 适合谁
- 准备输入
- 交给 Codex 的提示词
- Codex 应该执行什么
- 验证方式
- 常见风险

## 怎么选第一个案例

| 目标 | 推荐案例 |
| --- | --- |
| 先看到成果 | [README 变网页](readme-to-web.md) |
| 想发布到公网 | [静态网页部署](deploy-static-site.md) |
| 做内容表达 | [PPT](ppt-skill.md)、[Draw.io](drawio-diagram.md)、[动画视频](animation-video.md) |
| 整理知识库 | [Obsidian](obsidian.md)、[AI Wiki](ai-wiki.md)、[Notion MCP](notion-mcp.md) |
| 接工具 | [Playwright MCP](playwright-mcp.md)、[Figma MCP](figma-mcp.md)、[数据库 MCP](database-mcp.md) |
| 真实开发 | [真实仓库修 bug](fix-real-repo.md)、[GitHub Actions CI](github-actions-ci.md) |
| 自动化 | [网页采集](web-scrape.md)、[服务器巡检](server-patrol.md) |

## 案例清单

| 分类 | 案例 | 产出 |
| --- | --- | --- |
| 入门 | [README 变网页](readme-to-web.md) | 静态首页 |
| 入门 | [静态网页部署](deploy-static-site.md) | 公网访问链接 |
| 内容 | [一句话生成 PPT](ppt-skill.md) | 演示文稿 |
| 内容 | [Draw.io 架构图](drawio-diagram.md) | 可编辑图表 |
| 内容 | [CSV 变图表](data-viz.md) | 图表和分析说明 |
| 内容 | [代码生成动画视频](animation-video.md) | MP4 或网页动画 |
| 知识库 | [Obsidian 自动整理](obsidian.md) | 结构化笔记库 |
| 知识库 | [AI Wiki](ai-wiki.md) | 主题知识库 |
| 知识库 | [Notion MCP](notion-mcp.md) | Notion 工作区内容 |
| MCP | [Playwright MCP](playwright-mcp.md) | 浏览器自动化结果 |
| MCP | [Figma MCP](figma-mcp.md) | 设计稿解析和前端实现 |
| MCP | [数据库 MCP](database-mcp.md) | 查询结果和报表 |
| MCP | [GitHub MCP](github-mcp.md) | issue / PR 管理 |
| 浏览器 | [Chrome 控制](chrome-control.md) | 基于登录态的浏览器操作 |
| 浏览器 | [网页采集](web-scrape.md) | 定时抓取和入库 |
| 协作 | [飞书机器人](feishu-bot.md) | 多维表格或机器人流程 |
| 协作 | [公众号流程](wechat-mp.md) | 采集、排版、发布草稿 |
| 工程 | [真实仓库修 bug](fix-real-repo.md) | 修复代码和测试 |
| 工程 | [云服务器修 Bug](remote-bug-fix.md) | 远程排障记录 |
| 工程 | [GitHub Actions CI](github-actions-ci.md) | CI 修复 PR |
| 运维 | [服务器巡检](server-patrol.md) | 巡检报告和通知 |
| 移动 | [安卓远程操控](android-remote.md) | 手机自动化操作 |
| 研究 | [文献综述](literature-review.md) | 可复核证据表 |
| 研究 | [资料调研报告](research-report.md) | 带来源报告 |

## 通用提示词模板

```text
目标：请完成 [具体任务]。
上下文：相关文件在 [路径]，参考资料是 [链接或文件]。
约束：保留现有链接，不泄露密钥，不新增无关依赖。
完成标准：产出 [文件/页面/报告]，并运行 [验证命令]。
请先检查当前项目结构，再给出计划，确认后执行。
```

