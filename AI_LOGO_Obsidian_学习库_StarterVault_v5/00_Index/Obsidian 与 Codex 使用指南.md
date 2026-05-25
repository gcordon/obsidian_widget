# Obsidian 与 Codex 使用指南

这篇是给你自己看的操作说明：你日常仍然用 Notion 管生活和任务，把 Obsidian 当成学习知识库，把 Codex 当成本地 Markdown 整理助手。

## 1. 三个工具的分工

| 工具 | 负责什么 | 不建议做什么 |
|---|---|---|
| Notion | 日常任务、项目、临时收集、手机端随手记 | 不建议承载全部长期学习知识 |
| Obsidian | AI Logo 学习笔记、Prompt、案例复盘、作品集、知识链接 | 不要当成另一个复杂 Notion |
| Codex | 读取、整理、拆分、归类 Obsidian 里的 Markdown 文件 | 不要无备份地一次性重构整个库 |

你的核心流程是：

```text
手机/日常灵感 → Notion 临时收集
电脑学习 → Obsidian 正式整理
批量整理/复盘 → Codex 处理 Markdown
最终沉淀 → Prompt、案例、作品集、复盘
```

## 2. 这个 Vault 的核心入口

每天先打开：

```text
00_Index/AI Logo 设计 MOC.md
```

它是总导航页。学习顺序建议是：

```text
AI Logo 设计 MOC
→ 30 天练习计划
→ Prompt 模板库
→ Logo 质量检查表
→ 案例复盘模板
→ 我的作品集模板
```

## 3. Obsidian 第一次设置

打开 Obsidian 后：

```text
Open folder as vault
```

选择这个文件夹：

```text
AI_LOGO_Obsidian_学习库_StarterVault
```

然后开启核心插件：

```text
Settings → Core plugins
```

建议开启：

- Daily notes
- Templates
- Backlinks
- Outgoing links
- Graph view
- Canvas
- Search
- File recovery

### Templates 设置

```text
Settings → Core plugins → Templates
Template folder location: Templates
```

### Daily notes 设置

```text
Settings → Daily notes
New file location: 01_Daily
Template file location: Templates/每日 AI Logo 练习模板
Date format: YYYY-MM-DD
```

## 4. 每天怎么用 Obsidian 学 AI Logo

每天固定走这个流程：

```text
打开 MOC
→ 查看 30 天练习计划
→ 新建当天 Daily Note
→ 套 Prompt 做图
→ 用质量检查表打分
→ 写案例复盘
→ 每周整理作品集
```

当天练习笔记建议放在：

```text
01_Daily/
```

案例复盘放在：

```text
40_Cases/
```

可复用 Prompt 放在：

```text
30_Prompts/
```

作品集放在：

```text
60_Portfolio/
```

## 5. Codex 如何打开这个 Vault

打开终端，进入这个文件夹。

macOS / Linux 示例：

```bash
cd "/你的路径/AI_LOGO_Obsidian_学习库_StarterVault"
codex
```

Windows PowerShell 示例：

```powershell
cd "D:\你的路径\AI_LOGO_Obsidian_学习库_StarterVault"
codex
```

第一次不要让 Codex 直接改文件，先让它只读扫描。

复制给 Codex：

```text
请阅读 AGENTS.md 和当前 Obsidian vault。
不要修改任何文件。

请告诉我：
1. 这个 AI Logo 学习库有哪些主要模块；
2. 每个文件夹分别是做什么的；
3. 我今天应该从哪 3 篇笔记开始学习；
4. 我应该如何用 Daily notes 记录一次 Logo 练习。
```

## 6. Codex 已经有项目规则

这个 Vault 根目录里已经有：

```text
AGENTS.md
```

它会告诉 Codex：

- 这是 Obsidian 学习库，不是普通代码项目；
- 输出用中文；
- 保留 `[[双向链接]]`；
- 不要删除原始资料；
- Prompt 放进 `30_Prompts/`；
- 案例放进 `40_Cases/`；
- 复盘放进 `70_Reviews/`；
- 批量修改前先说明计划。

## 7. Codex 安全配置

这个 Vault 里已经有：

```text
.codex/config.toml
```

当前配置是：

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "disabled"
model_reasoning_effort = "high"
personality = "pragmatic"
```

意思是：Codex 主要在当前工作区内读写，遇到越权操作需要确认；整理本地 Obsidian 时默认不联网。

## 8. 常用 Codex 任务

### 任务 A：整理今天的练习

```text
请帮我整理今天的 AI Logo 练习。

要求：
1. 读取 01_Daily 中今天的练习笔记；
2. 提取品牌信息、Prompt、生成结果和问题；
3. 生成一篇案例复盘，放到 40_Cases；
4. 如果有可复用 Prompt，整理到 30_Prompts；
5. 添加相关 Obsidian 双向链接；
6. 不要删除原始笔记。
```

### 任务 B：提取可复用 Prompt

```text
请扫描 01_Daily 和 40_Cases 中最近的练习记录。

要求：
1. 找出可以复用的 Logo Prompt；
2. 每个 Prompt 单独整理成一篇笔记；
3. 放到 30_Prompts；
4. 每篇包含：用途、适用场景、Prompt 正文、可替换变量、注意事项、使用记录；
5. 不要改动原始案例。
```

### 任务 C：生成每周复盘

```text
请根据 40_Cases 中最近 7 天的案例，生成一篇本周 AI Logo 学习复盘。

要求：
1. 放到 70_Reviews；
2. 总结本周完成案例数量；
3. 找出最常见问题；
4. 总结本周最有效的 Prompt；
5. 给出下周重点练习方向；
6. 用 [[ ]] 链接相关案例和知识笔记。
```

### 任务 D：检查孤立笔记

```text
请扫描整个 vault，找出没有任何 [[内部链接]] 的笔记。

先不要修改文件，只生成一份报告：
1. 哪些笔记是孤立的；
2. 它们可能应该链接到哪些主题；
3. 哪些笔记适合加入 AI Logo 设计 MOC。
```

### 任务 E：生成作品集页面

```text
请根据 40_Cases 中完成度最高的案例，帮我生成一个作品集页面。

要求：
1. 放到 60_Portfolio；
2. 每个作品包含品牌名称、行业、风格、设计关键词、主色、辅助色、输出格式；
3. 每个作品写一段设计说明；
4. 链接对应的案例复盘；
5. 不要编造没有记录的信息。
```

## 9. 推荐每周节奏

```text
周一到周五：
每天做 1 个 Logo 练习
每天写 1 篇 Daily Note
每天保存 Prompt + 结果 + 问题

周六：
用 Codex 整理本周案例
提取可复用 Prompt
补充风格关键词库

周日：
生成每周复盘
选 1-3 个作品放入作品集
规划下周练习方向
```

## 10. 重要提醒

- 不要一开始装太多 Obsidian 社区插件。
- 不要让 Codex 一次性修改整个 Vault。
- 不要删除原始资料，原始资料放进 `Sources/` 或 `90_Archive/`。
- 做商业交付时，不要只给 PNG；真正可编辑的 Logo 应该至少保留 SVG / PDF / AI 或 EPS。
- AI 负责快速给你大量视觉可能性，你负责判断哪个方向像品牌、能落地、能长期使用。
