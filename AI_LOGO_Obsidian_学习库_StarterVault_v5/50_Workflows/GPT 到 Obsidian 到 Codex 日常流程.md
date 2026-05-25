# GPT 到 Obsidian 到 Codex 日常流程

> 核心原则：ChatGPT 负责“创作和判断”，Obsidian 负责“长期保存”，Codex 负责“本地落盘和整理”。

## 总流程

```text
ChatGPT 网页版 / Project
  ↓ 看图、生成图、改图、评分、输出 Markdown
Obsidian
  ↓ 保存图片、Prompt、Daily Note、案例复盘
Codex
  ↓ 每 2-3 天整理本地 Markdown、补链接、生成周复盘
Obsidian
  ↓ 成为长期知识库和作品集
```

## 为什么不建议每天用 zip 更新

每天上传 zip → GPT 修改 zip → 下载 zip → 覆盖本地 vault，这个流程能做，但不适合日常学习。

问题是：

- 容易覆盖本地新笔记；
- 图片文件和 Markdown 容易错位；
- 每天解压/替换会打断学习节奏；
- zip 更适合备份或大版本更新，不适合作为日常同步方式。

更好的方式是：

```text
每天：GPT 输出 Obsidian-ready Markdown
本地：你把 Markdown 放进 00_Inbox 或 01_Daily
整理：Codex 进入本地 vault 后移动、拆分、补链接
```

## 每天的具体操作

### 1. 在 ChatGPT 网页版做图片

使用 [[每日图片练习启动 Prompt]]，并上传参考图或生成图。

ChatGPT 负责：

- 分析参考图；
- 生成 Logo 方向；
- 修改图片；
- 优化 Prompt；
- 根据 [[Logo 质量检查表]] 打分。

### 2. 保存图片到 Obsidian

图片放入：

```text
80_Assets/01_References/  参考图
80_Assets/02_Generated/   生成过程图
80_Assets/03_Final/       最终图
80_Assets/04_SVG_AI_PDF/  矢量/交付文件
80_Assets/05_Mockups/     应用场景图
```

### 3. 把 GPT 输出放进 Obsidian

如果你今天没时间整理，先放到：

```text
00_Inbox/待整理_YYYY-MM-DD.md
```

如果已经是当天练习记录，放到：

```text
01_Daily/YYYY-MM-DD AI Logo 练习.md
```

### 4. 用 Codex 本地整理

进入本地 vault：

```bash
cd "你的 Obsidian Vault 路径"
codex
```

给 Codex 使用 [[Codex 每日与每周整理 Prompt]] 里的指令。

## 每周流程

周末让 Codex 做：

- 整理 `00_Inbox`；
- 生成 `70_Reviews/本周复盘.md`；
- 提取新增 Prompt 到 `30_Prompts`；
- 检查图片断链；
- 更新 `60_Portfolio`。

## 最重要的学习习惯

每张图都要留下：

- 为什么这样做；
- 用了什么 Prompt；
- 哪里失败；
- 下一版怎么改；
- 是否适合转 SVG / AI / PDF。

只保存图片不会进步，保存“判断过程”才会进步。
