# AI 餐饮 Logo 商业学习系统改造设计

日期：2026-05-26

## 核心目标

当前项目要从「AI Logo 学习资料库」升级为「AI 餐饮 Logo 商业学习系统」。

最终目标不是单纯整理笔记，也不是只做练习，而是长期建立一套可以赚钱的资产生产能力：

```text
学习 AI Logo 能力
→ 每日餐饮 Logo 练习
→ 记录 Prompt、图片、判断过程
→ 案例复盘
→ 总结可复用结构和风格规律
→ 沉淀 Prompt 包 / 模板包 / 风格包 / 素材包
→ 形成可售卖资产
→ 用商业反馈继续驱动学习
```

第一条长期商业主线：餐饮 Logo 模板包。

第一阶段不追求马上接单，也不追求做复杂文档。重点是把每天的学习和练习变成未来可售卖资产的原材料。

## 设计原则

1. 学习优先，但学习必须通向商业资产。
2. 首页服务行动，不服务资料展示。
3. 案例是核心资产，Prompt、知识、图片和总结都围绕案例沉淀。
4. 每次练习都要留下可复用内容：Prompt、结构、错误、改进、可售卖判断。
5. 页面可以重写、合并、移动、归档或删除，只保留服务目标的内容。
6. 不为了 Obsidian 结构而复杂化；工具必须服务学习、总结和资产沉淀。
7. 所有重要资料要有清楚去向：保留、归档、合并、替代或删除原因明确。

## 允许的改造范围

本次允许彻底改造整个项目，包括：

- 当前所有 Markdown 笔记
- 目录结构
- 首页、MOC、Dashboard、导航页
- Prompt 库
- 案例库
- 复盘模板
- 作品集
- 系统说明
- Obsidian Bases 或 Canvas，如果它们能明显提升查看效率

谨慎处理：

- `.obsidian/`：除非需要改善 Obsidian 使用体验，否则不改内部配置。
- `.agents/skills/`：保留现有 skills 作为 Codex 协作能力，不随意重写 skill 实现。
- 图片素材：可以重组说明和引用路径，但实际图片文件应避免无意义删除。
- `Sources/`：可以归档或降级，但要保留原始资料入口。

## 目标用户和使用场景

目标用户是正在学习用 AI 做 Logo，并希望长期靠餐饮 Logo 模板、Prompt、素材包变现的人。

每天使用场景：

```text
打开 Obsidian
→ 进入餐饮 Logo 学习工作台
→ 选择今天练习方向
→ 复制 Prompt 到 ChatGPT
→ 保存图片
→ 写 Daily
→ 提炼案例 / Prompt / 资产候选
```

每周使用场景：

```text
查看本周练习
→ 选出最有价值案例
→ 提炼稳定 Prompt
→ 更新资产候选
→ 判断哪个方向最接近可售卖
→ 安排下周练习
```

每月使用场景：

```text
整理一个小型餐饮 Logo 资产包
→ 包含案例、Prompt、模板结构、风格说明、交付建议
→ 准备后续上架或推广
```

## 商业主线

第一条商业主线是餐饮 Logo 模板包，优先聚焦五类资产：

1. 外卖头像 Logo
2. 餐饮吉祥物 Logo
3. 圆形徽章 Logo
4. 咖啡 / 奶茶 Logo
5. 门店招牌 Logo

每个方向都要沉淀：

- 适用餐饮细分
- 参考构图
- 稳定 Prompt
- 常见错误
- 修改方法
- 质量评分标准
- 可售卖程度
- 还缺什么才能打包出售

## 新信息架构

推荐把 vault 重构成八个核心区：

```text
00_Home/              每天使用的入口和地图
10_Learning/          学习路线、能力清单、基础知识
20_Practice/          每日练习、Inbox、待整理内容
30_Cases/             餐饮 Logo 案例复盘
40_Prompts/           Prompt 包和 Prompt 索引
50_Assets/            待售资产、作品集、模板包规划
90_System/            规则、归档、维护报告、原始资料入口
```

如果暂时不重命名目录，也要在内容职责上按这个结构重排。

## 核心页面职责

### 餐饮 Logo 学习工作台

建议位置：`00_Home/每天从这里开始.md`

若暂不改目录，可继续使用：`00_Index/每天从这里开始.md`

这是唯一日常入口。

结构：

```text
# 每天从这里开始：餐饮 Logo 学习工作台

## 今天只做这 3 件事
## 本周餐饮 Logo 方向
## 今天复制这个 Prompt
## 图片保存位置
## 练完必须留下
## 最近案例
## 本周资产候选
## 周复盘入口
```

原则：

- 不放长篇教程。
- 不展示全部 vault。
- 只保留今天能推动学习和资产沉淀的链接。

### 全局地图

建议位置：`00_Home/AI Logo 学习与资产地图.md`

职责：

- 展示整个系统有哪些区。
- 说明每个区做什么。
- 链接学习、练习、案例、Prompt、资产、系统维护。
- 不重复每日工作台内容。

### 新手第一次路线

建议位置：`00_Home/第一次打开先走这里.md`

职责：

```text
看 1 个 Demo
→ 复制 1 个餐饮 Logo Prompt
→ 完成 1 次练习
→ 写 1 篇 Daily
→ 生成 1 篇案例复盘
```

目标是让新手尽快完成一次闭环，而不是阅读大量说明。

### 餐饮 Logo 训练路线

建议位置：`10_Learning/餐饮 Logo 30 天训练路线.md`

结构：

```text
第 1 周：餐饮 Logo 基础判断
第 2 周：餐饮风格与行业细分
第 3 周：外卖头像、吉祥物、徽章专项
第 4 周：模板包、mockup、资产沉淀
```

每一天都要对应一个可复用产出，例如：

- 一个结构分析
- 一个 Prompt 版本
- 一个案例复盘
- 一个资产候选
- 一个常见错误总结

### 餐饮案例库

建议位置：`30_Cases/餐饮 Logo 案例库.md`

案例库是系统核心。

索引维度：

- 餐饮细分：小吃、奶茶、咖啡、烧烤、甜品、快餐、地方菜
- Logo 类型：头像、吉祥物、徽章、招牌、包装贴纸
- 商业状态：练习、案例、资产候选、可打包、可售卖
- 能力点：构图、文字、配色、风格、可矢量化、mockup

每个案例必须回答：

- 这个案例练了什么能力？
- 哪个 Prompt 有效？
- 哪个问题最影响商业可用性？
- 有什么可复用结构？
- 是否能进入模板包？
- 下一步要补什么？

### 餐饮 Prompt 包

建议位置：`40_Prompts/餐饮 Logo Prompt 包.md`

Prompt 不再只是收藏，而要按商业用途组织。

分类：

- 启动练习 Prompt
- 餐饮 Logo 生成 Prompt
- 餐饮吉祥物 Prompt
- 外卖头像 Prompt
- 圆形徽章 Prompt
- 咖啡 / 奶茶 Prompt
- 门店招牌 Prompt
- 高清复原 Prompt
- 文字修正 Prompt
- mockup Prompt
- Obsidian 导出 Prompt
- Codex 整理 Prompt

每个 Prompt 记录：

- 用途
- 适用餐饮类型
- Prompt 正文
- 可替换变量
- 效果稳定性
- 使用过的案例
- 商业化备注

### 待售资产库

建议位置：`50_Assets/待售资产库.md`

职责：

- 管理未来可售卖资产。
- 不是普通作品集，而是模板包研发列表。

资产状态：

```text
idea          想法
practice      已练习
candidate     资产候选
packaging     正在打包
sellable      可售卖
published     已发布
```

每个资产候选记录：

- 资产名称
- 餐饮细分
- 包含案例
- 包含 Prompt
- 包含图片 / mockup
- 缺失内容
- 目标买家
- 预计售卖形式

### 每周商业复盘

建议位置：`70_Reviews/每周商业复盘模板.md`

每周只回答关键问题：

- 本周练了哪些餐饮 Logo？
- 哪个案例最接近商业可用？
- 哪个 Prompt 最稳定？
- 哪个错误最常出现？
- 哪个方向值得做成资产包？
- 下周要补哪个能力？
- 下周推进哪个资产？

## 目录迁移建议

推荐新目录：

```text
AI_LOGO_Obsidian_学习库_StarterVault_v5/
  00_Home/
  10_Learning/
  20_Practice/
  30_Cases/
  40_Prompts/
  50_Assets/
  60_Reviews/
  80_Media/
  90_System/
  Templates/
```

旧目录映射：

```text
00_Index        → 00_Home
00_Inbox        → 20_Practice/Inbox
01_Daily        → 20_Practice/Daily
10_Learning_Plan→ 10_Learning
20_Knowledge    → 10_Learning/Knowledge
30_Prompts      → 40_Prompts
40_Cases        → 30_Cases
50_Workflows    → 90_System/Workflows 或 10_Learning/Workflows
60_Portfolio    → 50_Assets
70_Reviews      → 60_Reviews
80_Assets       → 80_Media
Sources         → 90_System/Sources
```

如果担心一次性重命名影响 Obsidian 链接，可以先保持旧目录，只重写入口和索引；第二阶段再做目录迁移。

## 元数据设计

统一 frontmatter 是后续筛选、Bases 和资产管理的基础。

通用字段：

```yaml
---
type: index | daily | case | prompt | knowledge | review | asset | workflow
status: active | draft | archived | demo
tags:
  - ai-logo
  - restaurant-logo
stage: learning | practice | review | asset-candidate | sellable
---
```

案例字段：

```yaml
brand:
restaurant_type:
logo_type:
style:
asset_status:
commercial_score:
prompt_version:
related_asset:
```

Prompt 字段：

```yaml
prompt_type:
restaurant_type:
logo_type:
stability:
used_in:
asset_status:
```

资产字段：

```yaml
asset_type:
target_buyer:
package_status:
included_cases:
included_prompts:
missing:
```

## 模板设计

### 每日练习模板

必须短，降低记录成本。

结构：

```text
# {{date}} 餐饮 Logo 练习

## 今日目标
## 餐饮细分
## Logo 类型
## 使用 Prompt
## 图片记录
## 结果评分
## 今天学到什么
## 可复用点
## 是否进入案例 / 资产候选
## 下一步
```

### 案例复盘模板

案例模板比 Daily 更完整。

结构：

```text
# 案例 - 品牌名 - Logo 类型

## 基本信息
## 参考图 / 生成图 / 最终图
## Prompt 版本
## 结果问题
## 修改过程
## 质量评分
## 可复用结构
## 可复用 Prompt
## 商业化判断
## 是否进入资产包
## 下一步
```

### Prompt 模板

结构：

```text
# Prompt - 用途 - 餐饮类型

## 用途
## 适用场景
## Prompt 正文
## 可替换变量
## 使用案例
## 稳定性记录
## 商业化备注
```

### 资产模板

结构：

```text
# 资产 - 餐饮 Logo 模板包名称

## 资产定位
## 目标买家
## 包含内容
## 案例列表
## Prompt 列表
## 缺失内容
## 打包计划
## 发布准备
```

## Obsidian Bases / Canvas 策略

不为了炫技使用 Bases 或 Canvas。

可以使用 Bases 的场景：

- 查看所有案例的商业化状态
- 查看所有 Prompt 的稳定性
- 查看待售资产的完成度

可以使用 Canvas 的场景：

- 展示餐饮 Logo 学习路线
- 展示模板包从练习到出售的流程

如果引入，必须保持轻量：

- 只创建 1-3 个 `.base` 文件。
- 只创建 1 个学习路线 Canvas。
- 不依赖社区插件才能理解核心内容。

## Skills 配合方式

本项目内 `.agents/skills` 用于提高改造质量，但不应该成为学习负担。

使用方式：

- `brainstorming`：确认目标、范围和设计。
- `information-architecture`：重构入口、目录和页面职责。
- `onboarding`：让第一次打开和每天开始更顺。
- `obsidian-markdown`：保证 wikilink、嵌入和 frontmatter 正确。
- `obsidian-bases`：在确实需要表格视图时创建轻量 Bases。
- `json-canvas`：在需要学习路线图时创建 Canvas。
- `markdown-documentation`：让页面短、清楚、可扫描。
- `skill-manager`：验证 skills 是否完整。

## 实施策略

彻底改造可以做，但要分层推进，避免一口气把 vault 变成不可用状态。

建议顺序：

1. 确定新目录和核心页面命名。
2. 重写唯一主入口：餐饮 Logo 学习工作台。
3. 重写全局地图和第一次学习路线。
4. 重构 30 天餐饮训练路线。
5. 重构案例库、Prompt 包、待售资产库。
6. 重写 Daily、案例、Prompt、资产、周复盘模板。
7. 迁移或归档旧页面。
8. 补统一元数据。
9. 修复 Obsidian 链接和图片嵌入。
10. 生成新的体检报告。

## 验收标准

改造完成后，应满足：

1. 日常入口只有一个，打开后 1 分钟内知道今天做什么。
2. 每日练习能直接转为案例、Prompt 或资产候选。
3. 案例库能按餐饮类型、Logo 类型和商业状态查看。
4. Prompt 包能按用途快速复制。
5. 待售资产库能看出哪些内容接近可卖。
6. 周复盘能总结技能进步和商业资产进度。
7. 系统说明不干扰日常学习。
8. 重要旧内容有清楚归宿。
9. Obsidian 链接和图片引用不产生明显断链。
10. 结构简单到每天愿意用，而不是只适合维护。

## 成功画面

每天使用时：

```text
打开工作台
→ 看到今天练什么餐饮 Logo
→ 复制 Prompt
→ 在 ChatGPT 做图
→ 保存图片
→ 写一篇短 Daily
→ 判断是否进入案例或资产候选
```

每周使用时：

```text
打开周复盘
→ 选出 1-2 个最有商业价值案例
→ 更新 Prompt 包
→ 更新待售资产库
→ 决定下周练哪个餐饮细分
```

长期结果：

```text
学习记录不再只是笔记，
而是逐步变成餐饮 Logo 模板包、Prompt 包、风格包和素材包。
```
