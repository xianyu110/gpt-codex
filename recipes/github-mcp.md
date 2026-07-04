# Codex x GitHub MCP: 管理 issue 与 PR

## 适合谁

适合把 GitHub issue、PR review、CI 状态纳入 Codex 工作流的人。

## 准备输入

- GitHub MCP 或 gh CLI。
- 目标仓库。
- issue / PR 链接。
- 期望动作。

## 提示词

```text
请查看这个 PR 的失败检查和评论，整理需要修复的问题。
要求：先只读分析；不要关闭 issue，不要强推；给出最小修复计划。
```

## Codex 应该做什么

- 读取 PR 和检查状态。
- 总结失败原因。
- 修改代码。
- 跑测试。
- 更新 PR 说明。

## 验证

- CI 变绿。
- PR diff 符合问题范围。
- 没有误关 issue。

## 风险

- 权限过大。
- 把无关改动混进 PR。
- 没跑本地测试。

