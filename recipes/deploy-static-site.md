# Codex x 一键部署: 静态网页发布到公网

## 适合谁

适合已经有静态网页，想发布到 GitHub Pages、Vercel 或其他静态托管平台的人。

## 准备输入

- 静态站目录。
- 目标平台。
- 域名或路径要求。
- 构建命令，如果有。

## 提示词

```text
请检查这个静态站是否能部署到 GitHub Pages。
要求：不要删除原有 CNAME 和购买入口；先检查 _config.yml、GitHub Actions 和相对路径；
完成后给出部署步骤和本地验证命令。
```

## Codex 应该做什么

- 检查 `_config.yml`、`.github/workflows/`、`CNAME`。
- 检查静态资源路径。
- 修复明显的相对路径问题。
- 给出部署步骤。
- 不在仓库里写入任何密钥。

## 验证

```bash
python3 -m http.server 8765
```

如果使用 GitHub Pages，还要检查：

- Pages 分支。
- Actions 是否成功。
- 站点 URL 是否能访问。

## 风险

- baseurl 配错导致页面资源 404。
- CNAME 被误删。
- 把平台 token 写进仓库。

