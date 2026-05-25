# 图片学习工作流：ChatGPT + Obsidian + Codex

> 目标：把「图片生成」和「学习复盘」分开处理。ChatGPT 负责看图、生成图、改图；Obsidian 负责保存知识、Prompt、案例复盘；Codex 负责批量整理本地文件和 Markdown 笔记。

## 三个工具的分工

| 工具 | 最适合做什么 | 不适合做什么 |
|---|---|---|
| ChatGPT 网页版 | 上传参考图、看图分析、生成 Logo、局部修改图片、做风格变体、解释图片问题 | 批量整理本地文件、长期保存所有作品、维护大量 Markdown 笔记 |
| Obsidian | 保存 Prompt、案例复盘、学习计划、质量检查表、作品集说明、图片链接 | 直接生成图片、直接编辑图片 |
| Codex | 扫描本地 vault、整理 Markdown、批量创建案例笔记、生成周复盘、统一命名、检查缺漏 | 直接创作图片、做主观视觉审美判断、替代 ChatGPT 网页版看图改图 |

## 推荐流程

```text
1. 在 ChatGPT 网页版上传参考图
2. 让 ChatGPT 分析构图、颜色、字体、风格
3. 让 ChatGPT 生成 / 修改 Logo 图片
4. 把最终图保存到 Obsidian vault 的 80_Assets 目录
5. 在 Obsidian 里写案例复盘
6. 每周让 Codex 整理案例、Prompt、作品集页面
```

## 图片保存目录

```text
80_Assets/
├── 01_References/     参考图
├── 02_Generated/      AI 生成过程图
├── 03_Final/          最终 PNG / JPG
├── 04_SVG_AI_PDF/     SVG、AI、PDF、EPS 等交付文件
└── 05_Mockups/        包装、招牌、头像等应用场景图
```

## 图片命名规则

建议使用：

```text
日期_品牌名_用途_版本.格式
```

例子：

```text
2026-05-25_食艺焖味_reference_01.png
2026-05-25_食艺焖味_generated_v01.png
2026-05-25_食艺焖味_generated_v02.png
2026-05-25_食艺焖味_final_logo.png
2026-05-25_食艺焖味_svg_v01.svg
2026-05-25_食艺焖味_mockup_storefront.png
```

## 在案例笔记里引用图片

Obsidian Markdown 可以这样引用图片：

```md
![[80_Assets/01_References/2026-05-25_食艺焖味_reference_01.png]]
![[80_Assets/02_Generated/2026-05-25_食艺焖味_generated_v01.png]]
![[80_Assets/03_Final/2026-05-25_食艺焖味_final_logo.png]]
```

## 每次图片练习要记录什么

每次练习不要只保存图，要记录：

- 品牌名
- 行业
- 目标风格
- 参考图路径
- 第一次 Prompt
- 第一次结果图路径
- 发现的问题
- 修改 Prompt
- 第二次结果图路径
- 最终图路径
- 是否需要 SVG / PDF / AI
- 质量评分
- 我学到了什么

## ChatGPT 网页版适合的图片任务

- 上传参考图，让它分析构图、色彩、字体、风格
- 让它生成 Logo 初稿
- 让它做 3-6 个风格方向
- 局部修改图片，例如换文字、简化线条、改颜色
- 高清复原模糊 Logo
- 生成应用场景图，例如包装、招牌、头像
- 帮你判断图片是否像 Logo、是否太复杂、是否适合缩小

## Codex 适合的本地任务

- 扫描 `80_Assets`，找出未写复盘的图片
- 按命名规则重命名图片文件
- 为每组图片生成一篇案例复盘笔记
- 从案例笔记中提取可复用 Prompt
- 每周生成学习复盘
- 生成作品集页面
- 检查 Markdown 中的图片链接是否失效
- 统一案例笔记格式

## 推荐每周固定动作

```text
周一到周五：在 ChatGPT 网页版生成 / 修改图片，并在 Obsidian 记录练习
周六：让 Codex 整理本周图片和案例
周日：让 Codex 生成周复盘和作品集候选清单
```

## 重要原则

- 图片生成和修改优先在 ChatGPT 网页版做。
- 长期知识、Prompt、复盘、作品集说明放 Obsidian。
- 批量文件整理、复盘生成、链接检查交给 Codex。
- 不要让 Codex 替你判断所有审美，它更适合做结构化整理。


## ChatGPT Project 的作用

建议把 ChatGPT 网页版当成长期学习教练，而不是每天重新上传整个 zip。

Project 里放关键说明和 Prompt：

- [[GPT Project 长期学习教练设置]]
- [[每日图片练习启动 Prompt]]
- [[练习结束导出 Obsidian Markdown Prompt]]
- [[Logo 质量检查表]]
- [[图片案例记录规范]]

每天在 Project 中上传图片、做图、改图、评分；练习结束后让它输出 Obsidian Markdown。

## 为什么 zip 不适合每天更新

zip 适合阶段性备份和大版本更新，不适合日常同步。每天更好的流程是：

```text
ChatGPT 输出 Markdown → 放到 00_Inbox 或 01_Daily → Codex 本地整理 → Obsidian 长期保存
```

详见：[[ZIP 更新与备份规则]]
