# 01. 下载与安装: 桌面 App / CLI 二选一

Codex 可以从多个入口使用。新手建议先选一个入口跑通，不要同时折腾 App、CLI、IDE、云端和中转。

## 入口怎么选

| 入口 | 适合谁 | 优点 | 注意 |
| --- | --- | --- | --- |
| 桌面 App | 小白、内容创作者、需要图形界面的人 | 看得见 Thread、计划、文件和结果 | 需要登录账号 |
| CLI | 开发者、经常在终端改项目的人 | 速度快，适合真实仓库 | 需要懂基本命令行 |
| ChatGPT / Web | 想在云端并行跑任务的人 | 适合远程跟进和 review | 本地文件访问方式不同 |
| IDE 扩展 | 已经在编辑器里工作的人 | 和代码编辑器更贴近 | 需要编辑器环境 |

## 桌面 App 安装

1. 打开 Codex 官方入口：`https://chatgpt.com/codex`
2. 下载适合系统的安装包。
3. 安装后登录 ChatGPT 账号。
4. 添加一个项目文件夹。
5. 新建 Thread，输入一个小任务。

本仓库原有教程中保留了这些入口：

- macOS 安装包：`https://persistent.oaistatic.com/codex-app-prod/Codex.dmg`
- Windows 安装包：`https://pan.quark.cn/s/0f1763fe2ac9?pwd=rTQw`

如果下载链接变化，以官方页面或你当前教程站首页展示为准。

## CLI 安装

如果你更习惯终端，可以先看 [13-cli.md](13-cli.md)。

最小使用路径是：

```bash
codex
```

进入项目目录后启动 Codex，让它读取当前仓库并执行任务。

## 完成标准

你完成这一章时，应该能做到：

- 打开 Codex App 或 CLI。
- 登录成功。
- 让 Codex 看到一个本地项目目录。
- 新建一条 Thread。
- 让它读 README 并总结项目结构。

## 常见坑

- 不要一开始就开 Full access 去跑陌生项目。
- 不要把 token、cookie、API key 贴到聊天窗口。
- 如果登录或访问不稳定，再看 [03-third-party-api.md](03-third-party-api.md)。

