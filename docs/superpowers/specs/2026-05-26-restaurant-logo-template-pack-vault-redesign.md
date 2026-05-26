# 餐饮 Logo 模板包研发库改造设计

日期：2026-05-26

## 背景

当前 Obsidian vault 已经包含 AI Logo 学习所需的知识、Prompt、案例、工作流、作品集和系统说明，但内容入口较多，学习路径和商业资产沉淀路径没有收束到同一条主线。

新的目标不是单纯整理文档，而是把 vault 改造成一个长期可用的「AI 餐饮 Logo 模板包研发库」：

```text
学习餐饮 Logo 类型
→ 每日练习
→ 记录图片和 Prompt
→ 案例复盘
→ 总结可复用结构
→ 提炼 Prompt / 模板
→ 进入待售资产候选
```

## 目标

第一版改造要服务三个结果：

1. 打开 vault 后，能快速开始一次餐饮 Logo 学习练习。
2. 每次练习都能沉淀为案例、Prompt、经验或待售模板候选。
3. 每周复盘能回答：本周能力提升了什么，哪个方向更接近可售卖资产。

## 非目标

- 不重写所有笔记。
- 不删除原始资料和 Demo。
- 不把 vault 变成复杂项目管理系统。
- 不在第一版强制引入复杂 Obsidian Bases 或 Canvas。
- 不把重点放在接单流程；长期方向是模板包、Prompt 包、风格包和素材包。

## 推荐方案

采用「餐饮 Logo 模板包研发闭环」：

```text
餐饮专项学习工作台
→ 餐饮细分练习路线
→ 餐饮案例复盘
→ 餐饮 Prompt 索引
→ 待售资产候选
→ 每周商业化复盘
```

第一套模板包聚焦五个方向：

1. 外卖头像 Logo
2. 餐饮吉祥物 Logo
3. 圆形徽章 Logo
4. 咖啡 / 奶茶 Logo
5. 门店招牌 Logo

## 信息架构

### 第一层：每天使用

`00_Index/每天从这里开始.md` 改造成唯一主入口，名称可保持不变，但内容改为「餐饮 Logo 学习工作台」。

它只回答日常学习问题：

- 今天练什么餐饮 Logo 类型？
- 直接使用哪个 Prompt？
- 图片应该放哪里？
- 练完如何复盘？
- 哪个案例可以参考？
- 本周要沉淀什么资产？

### 第二层：学习和沉淀

这些页面服务学习复盘和资产沉淀：

- `10_Learning_Plan/30 天练习计划.md`
- `30_Prompts/Prompt 模板库.md`
- `40_Cases/案例复盘库.md`
- `60_Portfolio/我的作品集.md`
- `70_Reviews/每周复盘模板.md`

它们要围绕餐饮 Logo 模板包研发重排，而不是只作为普通资料列表。

### 第三层：系统维护

这些页面保留，但从日常主路径降级：

- `00_Index/Obsidian 与 Codex 使用指南.md`
- `50_Workflows/ZIP 更新与备份规则.md`
- `90_System/*`
- `AGENTS.md`

它们用于维护、规则说明和 Codex 协作，不应干扰每天学习。

## 文件改造范围

第一版修改这些文件：

- `AI_LOGO_Obsidian_学习库_StarterVault_v5/00_Index/每天从这里开始.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/00_Index/AI Logo 设计 MOC.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/00_Index/学习路线与 Demo 导航.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/00_Index/AI Logo 学习 Dashboard.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/10_Learning_Plan/30 天练习计划.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/30_Prompts/Prompt 模板库.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/40_Cases/案例复盘库.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/60_Portfolio/我的作品集.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/70_Reviews/每周复盘模板.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/Templates/ChatGPT 每日练习记录模板.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/Templates/案例复盘模板.md`
- `AI_LOGO_Obsidian_学习库_StarterVault_v5/90_System/Vault 体检报告.md`

第一版不修改：

- `Sources/AI_LOGO设计学习工作台_Notion版.md`
- 图片素材文件
- `.obsidian/`
- `.agents/skills/`

## 页面设计

### 餐饮 Logo 学习工作台

文件：`00_Index/每天从这里开始.md`

结构：

```text
# 每天从这里开始：餐饮 Logo 学习工作台

## 今日 15 分钟练习
## 本周餐饮方向
## 直接复制的 Prompt
## 今天结束前留下什么
## 最近可参考案例
## 待整理内容
## 本周资产沉淀
## 系统入口
```

工作台应减少解释性长文，优先放可执行清单和关键链接。

### 全局地图

文件：`00_Index/AI Logo 设计 MOC.md`

职责：

- 说明 vault 的模块。
- 链接学习、案例、Prompt、作品集和系统维护区。
- 不重复每日流程。

### 新手路线

文件：`00_Index/学习路线与 Demo 导航.md`

职责：

- 只服务第一次学习。
- 引导用户看一个 Demo、复制一个 Prompt、写一篇 Daily、整理一个案例。
- 让新手尽快完成一次完整闭环。

### Dashboard

文件：`00_Index/AI Logo 学习 Dashboard.md`

职责：

- 保留为学习状态页。
- 顶部明确指向 `每天从这里开始.md`，说明日常学习从主工作台开始。
- 不再与 `每天从这里开始.md` 竞争首页职责。

### 餐饮专项练习路线

文件：`10_Learning_Plan/30 天练习计划.md`

保留 30 天结构，但强化餐饮行业：

```text
第 1 周：餐饮 Logo 结构分析
第 2 周：餐饮风格替换
第 3 周：外卖头像和高清复原
第 4 周：模板包、mockup 和资产沉淀
```

每天练习要尽量对应可商业化方向。

### 餐饮 Prompt 索引

文件：`30_Prompts/Prompt 模板库.md`

按使用场景重排：

- 开始一次餐饮 Logo 练习
- 生成餐饮 Logo
- 修改餐饮 Logo
- 高清复原
- 外卖头像优化
- 招牌 / 包装 mockup
- 导出 Obsidian Markdown
- 让 Codex 整理

保留已有 Prompt 文件，不在第一版删除。

### 餐饮案例库

文件：`40_Cases/案例复盘库.md`

结构：

```text
## 新手先看
## 按餐饮细分查看
## 按可售卖程度查看
## 案例如何变成 Prompt
## 案例如何进入作品集
```

案例复盘要重点总结：

- 这个案例适合哪个餐饮细分？
- 有哪些可复用结构？
- 哪句 Prompt 最有效？
- 是否有机会变成模板包资产？

### 待售资产与作品集

文件：`60_Portfolio/我的作品集.md`

从普通作品集升级为「待售资产与作品集」：

- Demo 作品
- 待售模板候选
- 还缺什么才能出售
- 可打包方向
- 已完成资产

第一版不做真实销售页，只做资产沉淀视图。

### 每周商业化复盘

文件：`70_Reviews/每周复盘模板.md`

新增复盘问题：

- 本周完成了哪些餐饮 Logo 练习？
- 哪个方向最稳定？
- 哪个 Prompt 最可复用？
- 哪个案例最接近可售卖模板？
- 下周要补哪个能力？
- 下周要推进哪个资产包？

## 模板设计

### Daily 模板

文件：`Templates/ChatGPT 每日练习记录模板.md`

新增或强化字段：

- 餐饮细分
- 目标资产类型
- Prompt 版本
- 结果评分
- 可复用点
- 下一步

### 案例复盘模板

文件：`Templates/案例复盘模板.md`

新增商业化字段：

- 餐饮细分
- 可复用结构
- 可复用 Prompt
- 是否可做模板
- 还缺什么才能出售
- 适合打包到哪个资产包

## 元数据策略

第一版只补核心页面的轻量 frontmatter，不追求全库一次补齐。

建议字段：

```yaml
---
type: daily | case-review | prompt | portfolio | review | index | workflow
status: active | draft | demo | archived
tags:
  - ai-logo
  - restaurant-logo
stage: learning | practice | review | asset-candidate | sellable
---
```

案例页可逐步增加：

```yaml
brand:
industry:
restaurant_type:
asset_type:
commercial_status:
```

## Skills 配合方式

- `brainstorming`：用于确认改造方向和设计，不直接实施。
- `information-architecture`：用于重新分配首页、地图、案例、Prompt、系统页职责。
- `onboarding`：用于优化第一次打开和每日开始路径。
- `obsidian-markdown`：用于保证 wikilink、嵌入、frontmatter 和模板格式正确。
- `markdown-documentation`：用于让页面短、清楚、可扫描。
- `obsidian-bases`：第一版不强制使用，仅为后续案例表、Prompt 表预留元数据。
- `skill-manager`：继续验证项目 skills 是否完整。

## 验证标准

改造完成后，至少满足：

1. 日常入口只有一个：`每天从这里开始.md`。
2. 用户能在主入口 1 分钟内知道今天练什么、用哪个 Prompt、练完如何复盘。
3. MOC 不再重复每日工作台内容。
4. 案例库能说明案例如何服务学习和模板包资产沉淀。
5. Prompt 库能按使用场景快速复制。
6. 周复盘能总结学习进步和商业资产进度。
7. 不删除原始资料和图片。
8. 不引入复杂维护负担。

## 风险与处理

### 风险：改造过度，学习压力更大

处理：第一版只重写核心入口和模板，不大规模改动所有知识笔记。

### 风险：商业化字段太多，记录成本高

处理：Daily 只保留少量必要字段，详细商业化判断放到案例复盘和周复盘。

### 风险：旧链接或 Demo 被破坏

处理：保留现有文件名，优先改内容和链接说明，不移动图片，不删除 Demo。

### 风险：未来需要 Bases 视图但当前元数据不完整

处理：第一版只补核心元数据；等真实案例增加后再创建 `.base` 视图。

## 实施顺序建议

1. 重写 `每天从这里开始.md` 为餐饮 Logo 学习工作台。
2. 简化 `AI Logo 设计 MOC.md` 为全局地图。
3. 调整新手路线和 Dashboard 职责。
4. 重排 30 天练习计划为餐饮专项路线。
5. 重排 Prompt 模板库和案例复盘库。
6. 更新作品集和周复盘模板。
7. 更新 Daily 和案例模板。
8. 更新体检报告，记录改造完成和后续建议。

## 成功画面

每天打开 vault 后，用户不需要重新理解整个系统，只需要进入 `每天从这里开始.md`：

```text
今天练一个餐饮 Logo 小方向
复制一个合适 Prompt
保存图片
写 Daily
沉淀一个案例或 Prompt
每周判断哪个方向能变成模板包
```

长期结果是：学习记录不再只是笔记，而是逐步累积成可售卖的餐饮 Logo 模板包、Prompt 包和风格资产。
