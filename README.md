# 写给 Codex 小白用户的全网最���细教程（2026年3月更新）

---

## 目录

- [一、什么是Codex？](#一什么是codex)
- [二、如何获取Codex](#二如何获取codex)
- [三、核心概念解析](#三核心概念解析)
- [四、项目文件夹管理](#四项目文件夹管理)
- [五、功能与配置项](#五功能与配置项)
- [六、设置配置](#六设置配置)
- [七、对话功能详解](#七对话功能详解)
- [八、开始 Vibe Coding](#八开始-vibe-coding)
- [九、总结](#九总结)

---

## 一、什么是Codex？

### 1.1 Codex简介

相信很多朋友都知道 **Claude Code** 和 **大龙虾 Clawdbot** 了对吧，这两者都可以理解为是一个 **Agent应用**，在上层封装了很多的工程化能力。

而 **Codex**，就是 **OpenAI对标Anthropic家的Claude Code产品**。

| 特性 | Codex | Claude Code |
|------|-------|-------------|
| 开发商 | OpenAI | Anthropic |
| 底层模型 | **GPT-5.3-codex** | Claude Opus 4.6 |
| 定位 | **编程Agent（趋近通用Agent）** | 编程Agent |

### 1.2 为什么编程Agent如此重要？

一个编程Agent，其实走到今天，**已经约等于通用Agent了**。因为这信息化30年，一切的东西几乎都构建于代码之上，**你的编程能力越强，就越趋近于通用Agent**。

这��是为什么最近美股那边天天吵着说"软件的逻辑变了"——一个Claude的Excel cowork插件能给华尔街吓个半死的原因。

### 1.3 模型对比

Codex和Claude Code都是上层的编程应用，应用本身需要搭配模型一起使用。正好两家都发了自己的新模型：

| 产品 | 模型 | 特点 |
|------|------|------|
| **Codex** | **GPT-5.3-codex** | 纯粹的编程特化模型，创作/事实核查/世界知识效果一般 |
| Claude Code | Claude Opus 4.6 | 通用能力更强 |

> ⚠️ **注意**：GPT-5.3-codex是纯粹的编程特化模型，所以在创作、事实核查、世界知识等方面效果并不好，所以OpenAI并没有把它放到ChatGPT里给所有人使用。**目前只有Codex中上线了GPT-5.3-codex。**

![图片](https://upload.maynor1024.live/file/1774358257887_image.png#imgIndex=8)

### 1.4 会员权限对比

| 会员类型 | Codex可用模型 |
|----------|---------------|
| **Plus会员 / Pro会员** | ✅ GPT-5.3-codex |
| 免费会员 / Go会员($8) | ⚠️ GPT-5.2-codex（非最新版） |

---

## 二、如何获取Codex

### 2.1 获取方式一：官网订阅

**codex 20刀充值链接（自备魔法）**：https://maynorai.tqfk.xyz/item/10

### 2.2 获取方式二：安装 cc-switch

| 步骤 | 说明 | 链接 |
|------|------|------|
| 1. 下载安装 | GitHub自行安装 | https://github.com/farion1231/cc-switch/releases/ |
| 2. 配置��转API | **每天100刀额度** | https://maynorai.tqfk.xyz/item/15 |
| 3. 详细配置教程 | 飞书文档 | https://ai.feishu.cn/wiki/JnefwEQRKiNyg6kTnN4cNphnnSh?from=from_copylink |

### 2.3 下载安装Codex

**下载Codex非常简单：**

1. 进入OpenAI的Codex官网：https://chatgpt.com/codex
2. 点击大大的"**下载应用**"按钮

![图片](https://upload.maynor1024.live/file/1774358235775_image.png#imgIndex=9)

3. 下载Mac安装包，安装、登录即可

![图片](https://upload.maynor1024.live/file/1774358277038_image.png#imgIndex=10)

> 💡 **提示**：Windows应用版本目前还没上线，只能使用命令行版本，不过应用版本应该也快了。

---

## 三、核心概念解析

### 3.1 Threads（线程）系统

当你下载好，登录到Codex的首页之后，你应该看到的，就是这个界面了：

![图片](https://upload.maynor1024.live/file/1774358264919_image.png#imgIndex=11)

在整个编程的逻辑中，有一个很核心的东西——**左边侧边栏的文件夹，叫做Threads（线程）**。

### 3.2 两层结构详解

在Codex的逻辑里，左边这栏其实**分两层**：

| 层级 | 名称 | 作用 | 类比 |
|------|------|------|------|
| **第一层** | **文件夹（工作区）** | 项目目录/主题盒子 | 像一个项目群 |
| **第二层** | **Thread** | 独立的对话任务线 | 像群里的具体话题贴 |

**整体关系：**
- 一个文件夹里可以有很多条Thread
- 每条Thread都在同一个工作区里，围绕一个明确目标推进
- **文件夹负责存放代码和资料，Thread负责存放思路和过程**

### 3.3 为什么这样设计？

这套设计对小白特别友好，因为它把两件容易混的东西拆开了：

| 传统方式的痛点 | Codex的解决方案 |
|----------------|-----------------|
| 上午写网页、下午算Excel、晚上改文案，所有东西搅成一锅粥 | **不同任务分到不同Thread** |
| 上下文污染严重 | **对话和目标互不污染** |
| AI开始胡编乱造 | **随时可以断点续写** |
| 找不到文件在哪 | **文件和资源井井有条** |

### 3.4 黄金法则

> 🎯 **同一个文件夹里可以做同一个大方向，同一个Thread里只推进一件具体的事，这样效果就最好。**

---

## 四、项目文件夹管理

### 4.1 推荐的文件夹结构

我非常建议大家在开始之前，先想好分类。比如我自己在电脑上建了一个叫 `dev` 的文件夹：

```
dev/
├── Learning/      # 学习资料
├── notes/         # 文章和笔记
├��─ Projects/      # 真实开发项目任务
├── sandbox/       # 沙盒（乱七八糟的东西）
└── tools/         # 通用脚本、可复用组件、小工具
```

![图片](https://upload.maynor1024.live/file/1774358310568_image.png#imgIndex=12)

### 4.2 Projects示例

在Project里有几个真实任务：

| 项目 | 说明 |
|------|------|
| AI热点 | 热点追踪项目 |
| 飞书机器人 | 多个不同功能的飞书机器人 |

![图片](https://upload.maynor1024.live/file/1774358254412_image.png#imgIndex=13)

比如周末刚做完的，**能把我公众号的数据按时全部爬下来存到多维表格里的飞书机器人**：

![图片](https://upload.maynor1024.live/file/1774358297085_image.png#imgIndex=14)

> ⚠️ **重要提醒**：前期的分类非常重要！一个好的分类，才是你后续开心的开始。千万千万不要什么对话都随手开新的，**Thread和项目文件夹一定一定要管理好！**

### 4.3 添加项目文件夹

当你在本地建好文件夹后，可以通过这个地方添加：

![图片](https://upload.maynor1024.live/file/1774358266229_image.png#imgIndex=15)

比如我想开发AI热点网站，就把这个项目文件夹添加进来，然后开一个Thread进行对话：

![图片](https://upload.maynor1024.live/file/1774358248581_image.png#imgIndex=16)

---

## 五、功能与配置项

Codex有一些非常棒的功能和配置项，这是**图形化界面带来的、对小白特别友好的东西**。

### 5.1 功能一：定时任务

![图片](https://upload.maynor1024.live/file/1774358230424_image.png#imgIndex=17)

**功能说明**：Codex会在特定的日期里去干一些特定的事。

**我的实际应用案例**：

| 场景 | 说明 |
|------|------|
| 服务器托管 | 我的好几个项目都跑在火山引擎云服务器上，但我对服务器完全不了解 |
| 自动化巡检 | **Codex每天早上9点自动对服务器进行巡检，检查报错** |
| 自动修复 | **如果有报错，会自己解决，然后总结原因** |
| 通知推送 | 通过飞书机器人发送给我 |

![图片](https://upload.maynor1024.live/file/1774358321275_image.png#imgIndex=18)

**实现效果**：完全托管，无需人工干预！

### 5.2 功能二：Skills（技能）

![图片](https://upload.maynor1024.live/file/1774358326352_image.png#imgIndex=19)

**Skills的重要性**：相信看我文章的老朋友们都知道，我写了很多Skills教程和分享。

**Codex的突破**：**这是第一次，Skills有了自己的可视化、图形化界面！**

| 对比项 | Codex | Claude Code / OpenCode |
|--------|-------|------------------------|
| Skills管理 | ✅ **图形化界面，轻松管理** | ❌ 不知道装了哪些、装到哪、有什么用 |
| Skills创建 | ✅ **内置Skill Creator** | ❌ 需要自己找、安装 |

### 5.3 Skill Creator使用

同时，Codex自带了 **Skill Creator**。在Codex上构建一个Skill，体验跟扣子几乎一样：

**步骤1**：点击右上角的"**New Skill**"

![图片](https://upload.maynor1024.live/file/1774358326136_image.png#imgIndex=20)

**步骤2**：用嘴告诉他，你想构建什么样的Skill

![图片](https://upload.maynor1024.live/file/1774358309454_image.png#imgIndex=21)

> 💡 **对比**：Claude Code和OpenCode非常呆逼的一点就是，明明支持Skill，但是构建Skill的Skill Creator，还需要我自己去找、去安装，这实在太蠢了。**OpenAI，还是懂用户的。**

---

## 六、设置配置

### 6.1 General设置

进入设置界面，在General里进行以下配置：

| 配置项 | 推荐设置 | 说明 |
|--------|----------|------|
| 保持电脑开机 | ✅ 打开 | 允许后台运行 |
| Follow-up behavior | 改成 **steer** | 开发过程中可随时发消息调整任务 |

![图片](https://upload.maynor1024.live/file/1774358287646_image.png#imgIndex=22)

### 6.2 Personalization（个性化设置）

在Personalization这一块，可以填**全局规则**，这个其实就是命令行界面中的 `AGENT.md`，只不过OpenAI单独拎出来了。

![图片](https://upload.maynor1024.live/file/1774358223960_image.png#imgIndex=23)

### 6.3 推荐的全局规则

新手可以直接复制粘贴以下规则：

```markdown
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
```

### 6.4 权限设置

在对话框的首页，把权限改成 **Full access**：

![图片](https://upload.maynor1024.live/file/1774358260172_image.png#imgIndex=24)

> 💡 **好处**：让Codex对你的电脑有最高的访问权限，这样就不会每次都要征求你同意，**直接开启收菜模式！**

---

## 七、对话功能详解

### 7.1 斜杠命令

在对话框中，输入 `/` 键就能调起一些特殊功能：

![图片](https://upload.maynor1024.live/file/1774358312531_image.png#imgIndex=25)

### 7.2 重要功能：Plan Mode（规划模式）

| 功能 | 说明 |
|------|------|
| **作用** | 只规划，不写代码 |
| **图标** | 会出现一个小图标 |
| **适用场景** | **每个大型项目（从0到1）的起始阶段** |

![图片](https://upload.maynor1024.live/file/1774358329472_image.png#imgIndex=26)

**推荐工作流**：

```
大型项目 → 先用Plan模式规划 → 形成规范文档和实现计划 → 再开始开发
```

**实际案例**：构建一个管理AI热点网站信源的Skill

![图片](https://upload.maynor1024.live/file/1774358329359_image.png#imgIndex=27)

一段时间后，你就可以得到这个计划：

![图片](https://upload.maynor1024.live/file/1774358281596_image.png#imgIndex=28)

Codex会询问你是否实施此计划，选择"**是**"即可���

Plan小图标消失后，**正式进入开发时间**：

![图片](https://upload.maynor1024.live/file/1774358293804_image.png#imgIndex=29)

> 💡 **建议**：等着收菜就行了！

### 7.3 重要功能：Status（状态查看）

输入 `/status` 能看到你**当前周期的用量和剩余额度**：

![图片](https://upload.maynor1024.live/file/1774358301530_image.png#imgIndex=30)

### 7.4 模型推理深度

![图片](https://upload.maynor1024.live/file/1774358245009_image.png#imgIndex=31)

**GPT-5.3-codex 跟之前一样，也是4个推理等级**：

| 等级 | 说明 | 推荐场景 |
|------|------|----------|
| Low | 最快最省 | 简单任务 |
| Medium | 平衡 | 一般任务 |
| **High** | **日常推荐** | **日常开发** |
| **Extra High** | 最稳最全 | **难活、硬活、大活** |

> 💡 **理解方式**：档位越高，模型在给出最终回答前，会用更多思考token做推理与自检，通常更稳更全，但也更慢、更贵。

> ⚠️ **建议**：日常使用 **High**，遇到超出日常范畴的难活、硬活、大活时，使用 **Extra High**。**这种大活，成功率和时间成本才是最值钱的，多出来的推理消耗可以忽略。**

---

## 八、开始 Vibe Coding

### 8.1 开发方式

Coding这块反���没啥可以说的了，**直接用嘴描述你的需求就行了**！

Codex右下角有个**麦克风**，我现在经常就是打开麦克风，然后用嘴说：

![图片](https://upload.maynor1024.live/file/1774358337645_image.png#imgIndex=32)

### 8.2 我的开发习惯

| 步骤 | 操作 |
|------|------|
| 1 | 在Codex上打开 **Plan模式** |
| 2 | 用嘴描述需求（涉及前端强调使用**Frontend Design Skill**，涉及服务器用**服务器管理Skill**） |
| 3 | 计划生成好后进行开发 |
| 4 | 开发完毕后第一时间看前端效果 |
| 5 | 效果可行→在Codex里用嘴修改；效果不好→打开Claude Code重制前端 |

### 8.3 前端问题的解决方案

> ⚠️ **现实情况**：有时候Codex的前端能力确实非常一般，**甚至奥特曼自己都这么说的**。

![图片](https://upload.maynor1024.live/file/1774358238088_image.png#imgIndex=33)

**解决方案对比**：

| 方案 | 适用条件 |
|------|----------|
| **Claude Code + Claude Opus 4.6** | 有Claude Opus 4.6（推荐） |
| **Claude Code + K2.5 + Frontend Design Skill** | 没有Claude Opus 4.6 |

重制完前端后，就可以回到Codex里，**继续快乐的口喷了**！

### 8.4 小技巧：并行开发

在Codex里，是**可以多个Threads一起并行开��**的：

![图片](https://upload.maynor1024.live/file/1774358284315_image.png#imgIndex=34)

---

## 九、总结

我一直觉得，**Vibe Coding这个东西，对非程序员来说可能比对程序员更有价值**。

| 人群 | AI的价值 |
|------|----------|
| 程序员 | 提效工具 |
| **非程序员** | **直接把一道原本过不去的坎给铲平了** |

**在未来，会用AI写代码会变成像会用Excel一样的基本技能。** 这是一个必然。

> 🎯 **希望人人都能发挥自己的创意。玩得开心！**

---

## 快速参考卡

### Codex vs Claude Code 快速对比

| 对比项 | Codex | Claude Code |
|--------|-------|-------------|
| 开发商 | OpenAI | Anthropic |
| 核心模型 | **GPT-5.3-codex** | Claude Opus 4.6 |
| 界面 | ✅ **图形化** | 命令行 |
| Skills管理 | ✅ **图形化界面** | 命令行 |
| 定时任务 | ✅ **支持** | 需配置 |
| 前端能力 | ⚠️ 一般 | ✅ 较强 |

### 推荐设置速查

| 设置项 | 推荐值 |
|--------|--------|
| Follow-up behavior | **steer** |
| 权限 | **Full access** |
| 推理深度（日常） | **High** |
| 推理深度（大活） | **Extra High** |

### 常用斜杠命令

| 命令 | 功能 |
|------|------|
| `/plan` | 进入规划模式 |
| `/status` | 查看用量和剩余额度 |

---

## 获取链接汇总

| 资源 | 链接 |
|------|------|
| Codex官网 | https://chatgpt.com/codex |
| 20刀充值 | https://maynorai.tqfk.xyz/item/10 |
| cc-switch下载 | https://github.com/farion1231/cc-switch/releases/ |
| 中转API配置 | https://maynorai.tqfk.xyz/item/15 |
| 飞书配置教程 | https://ai.feishu.cn/wiki/JnefwEQRKiNyg6kTnN4cNphnnSh?from=from_copylink |

---

*最后更新：2026年3月*
