# OpenAI Codex 最全入门教程：从下载到上手

OpenAI的Codex终于来了。

等了这么久，终于有人能跟Claude Code打一打了。

我用了一周，说说感受。

---

## 一、Codex是啥？

简单说，就是OpenAI版的Claude Code。

都是编程Agent，都能帮你写代码、跑命令、管项目。

但有个关键区别——Codex用的模型不一样。

它跑的是GPT-5.3-codex。一个专门为编程优化的模型。ChatGPT上没有这个，只有GPT-5.2。

为啥？因为这个模型不擅长创作、不擅长查资料、不擅长聊闲天。它就一件事做得好：写代码。

![图片](https://upload.maynor1024.live/file/1774358257887_image.png)

目前只有Codex能用到这个模型。

---

## 二、怎么下载？

两条路。

**第一条：官方订阅**

Plus或者Pro会员直接下。

官网：https://chatgpt.com/codex

点那个大大的"下载应用"按钮就行。

![图片](https://upload.maynor1024.live/file/1774358235775_image.png)

Mac用户最省事，下下来装好登录就能用。

Windows用户再等等，应用版还在路上，现在只能用命令行版。

![图片](https://upload.maynor1024.live/file/1774358277038_image.png)

**第二条：第三方方案**

不想花20刀？有别的办法。

1. 安装 cc-switch：https://github.com/farion1231/cc-switch/releases/
2. 配个中转API
3. 详细教程看这：https://ai.feishu.cn/wiki/JnefwEQRKiNyg6kTnN4cNphnnSh

---

## 三、界面长啥样？

打开之后，你会看到这个界面。

![图片](https://upload.maynor1024.live/file/1774358264919_image.png)

左边栏有两层东西，得搞清楚。

**第一层：文件夹（工作区）**

就是项目目录。你的AI热点项目、爬虫项目、测试项目，都放这儿。

**第二层：Thread（线程）**

点开文件夹，里面的每一条对话就是一个Thread。每个Thread是独立的任务线。

这设计有个好处：**不串味**。

以前用ChatGPT那种，上午聊网页，下午聊Excel，晚上改文案。全混一块，AI也懵，你也懵。

现在不会了。

一个文件夹管一个大方向，一个Thread只干一件事。

举个栗子：

文件夹 = 项目群
Thread = 群里的话题贴

你在A话题里聊需求，换到B话题就是另一条线。文件共享，上下文不污染。

**强烈建议：开始之前，先想好怎么分类。**

我自己电脑上有个dev文件夹，结构是这样的：

- Learning：学习资料
- notes：文章和笔记
- Projects：真实项目
- sandbox：乱七八糟的测试
- tools：通用脚本和小工具

![图片](https://upload.maynor1024.live/file/1774358310568_image.png)

Project里面再细分：

![图片](https://upload.maynor1024.live/file/1774358254412_image.png)

比如这个飞书机器人，周末刚做完，自动把公众号数据爬到多维表格里。

![图片](https://upload.maynor1024.live/file/1774358297085_image.png)

分类这事儿看着烦，但真的很重要。别问我怎么知道的。

---

## 四、几个关键功能

### 1. 定时任务

![图片](https://upload.maynor1024.live/file/1774358230424_image.png)

Codex能在特定时间自动干活。

我自己的用法：服务器托管。

我的项目跑在火山引擎上。但我对运维一窍不通。于是我把服务器交给Codex管。

它自己建了个自动化任务，每天早上9点巡检。有报错就修，修完发飞书通知我。

![图片](https://upload.maynor1024.live/file/1774358321275_image.png)

完全托管，爽。

### 2. Skills管理

![图片](https://upload.maynor1024.live/file/1774358326352_image.png)

Skills这东西，老粉都懂。

Codex第一次给Skills做了图形��面。不用再像Claude Code那样，连自己装了啥都不知道。

还有个Skill Creator，点右上角New Skill。

![图片](https://upload.maynor1024.live/file/1774358326136_image.png)

直接用嘴说你要啥skill，它就帮你建。

![图片](https://upload.maynor1024.live/file/1774358309454_image.png)

Claude Code支持skill，但skill creator得自己装。这设计真的很呆。

OpenAI这次确实懂用户。

### 3. 几个必改的设置

**General里：**

- "保持电脑开机"打开
- Follow-up behavior改成steer

这样你在开发过程中也能随时插话调整。

![图片](https://upload.maynor1024.live/file/1774358287646_image.png)

**Personalization里：**

填全局规则。这玩意儿就是命令行版的AGENT.md。

![图片](https://upload.maynor1024.live/file/1774358223960_image.png)

我常用的规则，直接复制：

\`\`\`
# Global rules for codex
## Operating principles
- Prefer small, reviewable diffs. Avoid sweeping refactors unless explicitly requested.
- Before editing, identify the file(s) to change and state the plan in 3-6 bullets.
- Never invent APIs, configs, or file paths. If unsure, search the repo first.
- Keep changes consistent with existing style and architecture.

## Safety and secrets
- Never paste secrets, tokens, private keys, .env values, or credentials into code or logs.
- If a task requires secrets, ask me to provide them via environment variables.
- Do not add analytics, telemetry, or network calls unless I ask.

## Code quality bar
- Add or update tests for behavior changes when the project has tests.
- Prefer type safety and explicit error handling.
- Add comments only when the intent is non-obvious.

## Build and run etiquette
- If you need to run commands, propose the exact command and why.
- When you make changes that may break build, run the fastest relevant check first.

## Output formatting
- For code changes: include a short summary + list of files changed.
- For debugging: include hypotheses, experiments run, and the minimal fix.

## My preferences
- I like concise explanations, concrete steps, and copy-pastable commands.
- Default language for explanations: Chinese.
\`\`\`

**权限设置：**

把权限改成Full access。

不然每次操作都要问你一遍，真的很烦。

![图片](https://upload.maynor1024.live/file/1774358260172_image.png)

### 4. 斜杠命令

输入 \`/\` 可以调出一些特殊功能。

![图片](https://upload.maynor1024.live/file/1774358312531_image.png)

**重点说两个：**

**Plan mode**

只规划，不写代码。

![图片](https://upload.maynor1024.live/file/1774358329472_image.png)

大项目开始之前，我强烈建议先用Plan模式过一遍。

让它出个方案，你再决定要不要执行。

比如我要做个管理信源的skill：

![图片](https://upload.maynor1024.live/file/1774358329359_image.png)

等它出计划：

![图片](https://upload.maynor1024.live/file/1774358281596_image.png)

然后点"是"，开始干活。

![图片](https://upload.maynor1024.live/file/1774358293804_image.png)

**Status**

看用量和余额。

![图片](https://upload.maynor1024.live/file/1774358301530_image.png)

### 5. 推理深度

![图片](https://upload.maynor1024.live/file/1774358245009_image.png)

GPT-5.3-codex有4个档位。

档位越高，想得越多，越稳，但也越慢越贵。

日常用High就够了。

遇到难活大活，上Extra High。成功率比省那点钱重要。

---

## 五、开始写代码

终于到正题了。

其实没啥好说的——直接用嘴描述需求就行。

Codex右下角有个麦克风按钮。

![图片](https://upload.maynor1024.live/file/1774358337645_image.png)

我现在基本不打了，直接说。

**说下我的工作流：**

1. 先开Plan模式，用嘴说需求
2. 涉及前端就强调用Frontend Design skill
3. 涉及服务器就用服务器管理skill
4. 计划出来后开始开发
5. 开发完看前端效果
6. 效果不行？切到Claude Code，用Opus 4.6重做前端
7. 前端搞定，回Codex继续

说个实话：Codex的前端能力确实一般。

奥特曼自己都承认。

![图片](https://upload.maynor1024.live/file/1774358238088_image.png)

没有Opus 4.6的话，Claude Code + K2.5 + Frontend Design skill也行。

**还有个技巧：**

Codex支持多Thread并行开发。

![图片](https://upload.maynor1024.live/file/1774358284315_image.png)

同时开好几个任务，效率更高。

---

## 写在最后

我之前说过一个观点：

Vibe Coding这东西，对非程序员的价值可能比对程序员还大。

程序员本来就会写代码，AI只是让他们更快。

但对我们这些不会写代码的人，AI直接把门槛给铲平了。

未来，用AI写代码会变成像用Excel一样的基本技能。

这是迟早的事。

希望每个人都能把自己的想法变成现实。

玩得开心。
