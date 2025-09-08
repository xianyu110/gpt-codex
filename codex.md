

---

## **是时候转CodeX了！Codex 接入 GPT-5，平替 Claude Code**

一纸禁令让 Claude 对中国地区的封锁更加严格；**价格高、易封号**，让 **Claude Code** 的使用门槛持续走高。

![image-20250908130649877](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081306979.png)

与此同时，**Codex** 正在快速推进对接：

* **6 月 3 日**，OpenAI 宣布 **Codex 全面开放**，支持**联网执行**，把“AI 写代码”从**实验室**直接丢进**大众泳池**。
* **半个月后**，Anthropic 发布 **Claude 4.1 Code Agent**，号称能顶**半个资深后端**。
* **7 月中**，**GPT 系列模型**以**比 Claude 便宜 60%** 的姿态冲进 **API 榜首**！

学生、个人开发者、企业团队，都在寻找**最好用的 Code CLI**。了解完背景之后，直接上手教程。

---

## **Codex 国内成功跑通教程（以 Mac为例）**

面对 **绑卡 / 翻墙 / 账单** 的三连击，你可能会想：**“凭什么卡我？”**
下面这套流程，帮你**一把过痛点**，开箱即用。

### **前置环境**

1. **任意系统**：Windows / macOS / Linux 均可。

2. **获取 Codex 套餐**（不限量）：[https://agi.maynor1024.live/list/#/shop](https://agi.maynor1024.live/list/#/shop)
   **一个月仅需 80 元**，**无需魔法**即可使用。

   ![image-20250908122624219](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081226418.png)

3. **安装 Node.js ≥ 18**

---

### **步骤一：安装 Codex CLI**

```bash
node -v   # 检查 Node 版本
npm i -g @openai/codex  # 安装 Codex CLI
```

![image-20250908124545993](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081245055.png)

**设置环境变量：**

```bash
export OPENAI_BASE_URL="https://code.claude-opus.top/openai"
export OPENAI_API_KEY="你的API密钥"
```

**永久设置（按你的 Shell 选择）：**

```bash
# zsh（默认）
echo 'export OPENAI_BASE_URL="https://code.claude-opus.top/openai"' >> ~/.zshrc
echo 'export OPENAI_API_KEY="你的API密钥"' >> ~/.zshrc
source ~/.zshrc
```

```bash
# bash
echo 'export OPENAI_BASE_URL="https://code.claude-opus.top/openai"' >> ~/.bash_profile
echo 'export OPENAI_API_KEY="你的API密钥"' >> ~/.bash_profile
source ~/.bash_profile
```

![image-20250908124841124](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081248181.png)

---

### **步骤二：启动 Codex**

```bash
codex  # 定义你的模型
```

![图片](https://restname.oss-cn-hangzhou.aliyuncs.com/202509051025737.png)

**选择建议（强烈推荐选第 1 个）：**

* **选项 1（Full Access）**：Codex 可在 **/root 目录直接执行命令或修改文件**，**无需逐次确认**。**效率最高**。
* **选项 2（Ask for Approval）**：每次**改文件 / 执行命令**都会**先询问确认**，**安全性更高**，适合在生产机或关键目录操作。

![image-20250908124941369](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081249416.png)

---

### **步骤三：开始使用**

进入 **OpenAI Codex CLI** 交互界面后即可开干。

![图片](https://restname.oss-cn-hangzhou.aliyuncs.com/202509051025757.png)

界面提供了几条**常用命令**（**直接对话也可以直接输入消息**）：

* **`/init`**：在当前目录创建 **`AGENTS.md`**，放置 Codex 的说明与**配置模板**，方便复用。
* **`/status`**：查看当前会话配置（**模型**、**Token 消耗**等）。
* **`/approvals`**：设置哪些操作**需要手动确认**、哪些**可自动执行**（对应上面的“审批模式”）。
* **`/model`**：选择**模型**和**推理强度**（如 **GPT-4 / GPT-5**，**快速**或**深度**模式）。

**建议配置**：**`gpt-5` + `high`**；审批选择 **Full Access（充分授权）**，尽量减少打断。

> **Codex 额外配置（推荐）**
> 在 **`~/.codex/config.toml`** 中添加：
> `disable_response_storage = true`
> 这样可**禁用响应存储**，进一步提升**隐私与安全**。

![image-20250908125158662](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081251732.png)

![image-20250908125239367](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081252417.png)

![image-20250908130351652](https://restname.oss-cn-hangzhou.aliyuncs.com/202509081303713.png)

**常见坑位 & 解决：**

* **极少数 npm 包拉不下来**：在 `AGENTS.md` 写死
  `registry=https://registry.npmmirror.com/`，**一劳永逸**。

![图片](https://restname.oss-cn-hangzhou.aliyuncs.com/202509051025250.png)

---

## **行业趋势：你不用，隔壁团队也会用**

* **82% 的专业开发者**在过去一年**实际调用过 OpenAI 系列模型**；**Claude / Gemini 使用率明显更低**。
* **AI 生成代码**主要集中在 **单元测试 / 低风险重构 / 脚手架搭建** 三大场景，**平均节省 22% 工时**。
* **Gartner 预测**：**2026 年**软件团队将有 **50% 的代码行由 AI 产出**。不使用 AI，**就像程序员不用 Git**——**没人敢要**。

![图片](https://restname.oss-cn-hangzhou.aliyuncs.com/202509051025803.png)

---

## **Codex 能否平替 Claude Code？**

**统一测试环境**：**1C1G 云机** + **npm 镜像锁定**：[https://www.ikunyun.cn/aff/FQYOYHZM](https://www.ikunyun.cn/aff/FQYOYHZM)
**Codex 全程跑在云沙盒**，结果一目了然：**价格更狠、速度持平**。

| **任务**           | **Codex**           | **Claude Code** | **Gemini CLI**  |
| ---------------- | ------------------- | --------------- | --------------- |
| **100 行 Bug 修复** | **42 s / \$0.009**  | 55 s / \$0.045  | 68 s / \$0.014  |
| **300 行重构**      | **4m15s / \$0.12**  | 5m01s / \$0.48  | 6m40s / \$0.18  |
| **项目初始化**        | **10m58s / \$0.31** | 14m20s / \$1.35 | 16m05s / \$0.44 |

---

## **让 AI 替你“下班”，香吗？**

昨晚有位粉丝说：把最后一批测试交给 **Codex** 后去洗碗，回来发现 **PR 已合并、CI 全绿**。
他的原话：**“真切体会到科技的尽头不是裁员，而是准点下班。”**

**你觉得五年内，AI 能替你写 100% 代码吗？**
希望下一次陪你通宵的是**娱乐活动**，而不是 **Bug**。

**点赞 + 关注 + 分享**，你的支持就是我更新**更多 AI 实战教程**的动力，**帮你更好创业与就业**。

---
