# 10. Threads 与并行: 任务怎么组织

Thread 是 Codex 的任务容器。一个 Thread 里有目标、上下文、工具输出、文件改动和验证过程。

## 一条 Thread 做一件事

推荐：

- “把 README 改成网页”
- “修复登录页移动端布局”
- “给 GitHub Actions 失败补测试”
- “把公众号文章整理进 Obsidian”

不推荐：

- “帮我优化整个项目”
- “顺便把网站、部署、文案、SEO 都做了”

## 并行怎么用

可以并行的任务：

- 一个 Thread 写教程。
- 一个 Thread 做前端样式。
- 一个 Thread 检查链接。

不适合并行的任务：

- 多个 Thread 同时改同一个文件。
- 多个 Thread 同时重构同一模块。
- 一个任务还没定方向就开太多分支。

## 命名建议

Thread 标题最好能看出结果：

- `docs: build codex guide`
- `recipes: add mcp cases`
- `fix: mobile hero overflow`

## 完成标准

任务结束时让 Codex 回答：

- 目标完成了吗？
- 改了哪些文件？
- 跑了什么检查？
- 有什么没做？

