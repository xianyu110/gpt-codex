# 命令 / 斜杠速查

这页放 Codex 教程站的速查命令。不同版本的 Codex App、CLI、IDE 扩展可能有差异，以当前界面和 `/help` 为准。

## Codex 内常用命令

| 命令 | 作用 | 示例 |
| --- | --- | --- |
| `/plan` | 进入规划模式 | 复杂任务先让 Codex 读仓库和列计划 |
| `/status` | 查看当前任务状态 | 长任务中途看进度、上下文、用量 |
| `/help` | 查看当前可用命令 | 不确定命令时先查 |
| `/model` | 查看或切换模型 | 需要更强推理或更快速度时 |

## 本地开发常用命令

```bash
git status --short
```

查看当前改动。

```bash
git diff -- README.md
```

查看某个文件的具体改动。

```bash
rg "关键词"
```

快速搜索仓库内容。

```bash
find docs recipes reference -maxdepth 2 -type f | sort
```

检查教程文件是否齐全。

```bash
python3 -m http.server 8765
```

预览静态站。

## 给 Codex 的常用提示词

```text
先只读检查项目结构，不要改文件。告诉我你会改哪些文件和怎么验证。
```

```text
请保留所有原有购买、中转、飞书教程链接，只改教程内容和导航。
```

```text
完成后请总结：改动文件、验证命令、未完成事项、风险。
```

