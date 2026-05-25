# 先读我：AI Logo Obsidian 学习库启动说明 v4

这个文件夹是一个可以直接用 Obsidian 打开的 AI Logo / 图片设计学习库 starter vault。

v4 的重点不是只放资料，而是帮你建立：

```text
ChatGPT 网页版 / Project → Obsidian → Codex → 周复盘 / 作品集
```

的日常学习流程。

## 第一步：打开这个 Vault

1. 解压 zip。
2. 打开 Obsidian。
3. 选择 **Open folder as vault**。
4. 选择这个文件夹：`AI_LOGO_Obsidian_学习库_StarterVault_v4`。

## 第二步：先打开这些文件

进入 Obsidian 后，按顺序打开：

1. `00_Index/每天从这里开始.md`
2. `00_Index/AI Logo 设计 MOC.md`
3. `00_Index/GPT Project 长期学习教练设置.md`
4. `00_Index/图片学习工作流：ChatGPT + Obsidian + Codex.md`

## 第三步：开启核心插件

建议开启：

- Daily notes
- Templates
- Backlinks
- Outgoing links
- Graph view
- Canvas
- Search
- File recovery

## 第四步：设置模板文件夹

在 Obsidian 中设置：

- Settings → Core plugins → Templates → Template folder location
- 填写：`Templates`

如果你使用 Daily notes：

- Settings → Daily notes
- New file location：`01_Daily`
- Template file location：`Templates/ChatGPT 每日练习记录模板`

## 第五步：建立 ChatGPT Project

建议建立一个 Project：

```text
AI Logo 设计学习教练
```

然后把 `00_Index/GPT Project 长期学习教练设置.md` 里的固定指令复制到 Project instructions。

日常练习使用：

- `30_Prompts/每日图片练习启动 Prompt.md`
- `30_Prompts/练习结束导出 Obsidian Markdown Prompt.md`

## 第六步：用 Codex 打开这个 Vault

在终端进入这个文件夹，然后运行：

```bash
codex
```

第一次建议给 Codex：

```text
请阅读 AGENTS.md 和当前 Obsidian vault。不要修改文件。先告诉我这个 AI Logo 学习库的结构、核心入口，以及我今天应该从哪 3 篇笔记开始。
```

日常整理使用：

- `30_Prompts/Codex 每日与每周整理 Prompt.md`

## 每天的学习流程

1. 打开 `00_Index/每天从这里开始.md`。
2. 在 ChatGPT Project 里开始当天练习。
3. 上传参考图或生成图。
4. 用 ChatGPT 分析、生成、修改、评分。
5. 让 ChatGPT 输出 Obsidian Markdown。
6. 图片放到 `80_Assets/`。
7. Markdown 放到 `00_Inbox/` 或 `01_Daily/`。
8. 每 2-3 天用 Codex 整理一次。
9. 每周用 Codex 生成复盘和作品集草稿。

## 不要一开始做的事

- 不要马上装很多社区插件。
- 不要每天上传整个 zip 给 ChatGPT。
- 不要每天下载新 zip 覆盖本地 vault。
- 不要让 Codex 一次性重构全部文件。
- 不要只保存图片，不记录 Prompt 和复盘。

## v4 新增内容

- `00_Index/每天从这里开始.md`
- `00_Index/GPT Project 长期学习教练设置.md`
- `50_Workflows/GPT 到 Obsidian 到 Codex 日常流程.md`
- `50_Workflows/ZIP 更新与备份规则.md`
- `30_Prompts/每日图片练习启动 Prompt.md`
- `30_Prompts/练习结束导出 Obsidian Markdown Prompt.md`
- `30_Prompts/Codex 每日与每周整理 Prompt.md`
- `Templates/ChatGPT 每日练习记录模板.md`
- `Templates/ChatGPT 输出整理模板.md`
- `00_Inbox/` 和 `01_Daily/` 目录
- `90_System/ZIP 更新记录.md`

## 一句话原则

ChatGPT 负责图片创作和学习指导；Obsidian 负责长期沉淀；Codex 负责本地整理；zip 只做阶段性备份和大版本更新。


---

## v5 新增：更适合“打开就能学”的 Demo

本版新增了新手阅读路线和完整 Demo：

- [[学习路线与 Demo 导航]]
- [[Demo - 一次完整学习流]]
- [[Demo - 2026-05-25 AI Logo 练习]]
- [[Demo - 食艺焖味餐饮 Logo 复盘]]
- [[Demo - FOREST COFFEE 徽章 Logo 复盘]]
- [[Demo - 餐饮吉祥物 Logo Prompt 迭代]]
- [[Demo - AI Logo 作品集页面]]
- [[Demo - 第一周复盘]]

也新增了示例图片素材，放在 `80_Assets/` 下。示例图片只是为了演示 Obsidian 图片嵌入、案例复盘和作品集结构，不代表最终商业设计稿。

第一次学习建议顺序：

```text
README_先读我
↓
00_Index/每天从这里开始
↓
00_Index/学习路线与 Demo 导航
↓
Demo - 一次完整学习流
↓
Demo - 食艺焖味餐饮 Logo 复盘
↓
开始自己的每日练习
```
