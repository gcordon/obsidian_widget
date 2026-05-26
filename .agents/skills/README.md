# 当前项目 Skills 说明

这个目录保存当前项目专用的 Codex skills。它们只服务于本仓库，不再依赖全局安装。

## Codex 如何自动匹配项目内 Skill

Codex 启动时会读取当前项目里的 `.agents/skills/<skill-name>/SKILL.md`。

每个 `SKILL.md` 顶部都有 `name` 和 `description`。当你发起对话时，Codex 会根据你的请求内容和这些 description 自动判断是否要使用某个 skill。

要让自动匹配生效，注意三点：

1. 从项目根目录启动 Codex：`/Users/zengruilin/Downloads/obsidian_widget`
2. 启动 Codex 之前，skill 已经存在于 `.agents/skills/`
3. 如果是刚安装或刚修改 skill，需要重启 Codex 才会重新读取

如果你想强制使用某个 skill，可以在消息里直接写 `$skill-name`，例如：

```text
用 $obsidian-markdown 检查这个 README 的 Obsidian 链接写法
```

## 当前项目已安装的 Skills

### Obsidian 与知识库

- `obsidian-markdown`：处理 Obsidian wiki 链接、嵌入、callout、frontmatter 等 Markdown 写法。
- `obsidian-cli`：通过命令行读取、搜索、整理 Obsidian vault。
- `obsidian-bases`：设计 Obsidian Bases 数据库视图，例如案例库表格、作品集列表。
- `json-canvas`：创建 Obsidian Canvas 路线图、流程图、学习地图。
- `defuddle`：从网页或复杂内容中提取更干净的正文，适合整理资料来源。

### 内容整理与个人知识产品

- `content-strategy`：规划内容结构、主题路线、长期内容体系。
- `copy-editing`：润色、精简、修正表达，让笔记更清楚。
- `copywriting`：写 README、介绍文案、发布说明、项目说明。
- `customer-research`：分析目标用户和使用场景。个人项目里可用来明确“这个 vault 是为谁服务”。
- `product-marketing`：梳理定位、卖点和项目包装。
- `onboarding`：优化新手第一次打开项目时的引导路径。
- `marketing-ideas`：为内容、作品集、展示页生成推广或选题想法。

### 文档、版本与流程

- `markdown-documentation`：写标准 Markdown 文档，处理列表、链接、图片、折叠块等。
- `changelog-maintenance`：维护版本记录和更新日志。
- `git-auto-sync`：一键运行项目检查、创建 Git commit，并 push 当前分支。
- `git-hooks-setup`：设计 Git hooks 和提交前检查，例如 Markdown、Obsidian 链接、图片路径、敏感文件检查。
- `gh-address-comments`：使用 GitHub CLI 处理 PR / issue review comments。适合以后你在 GitHub 上处理协作反馈。
- `information-architecture`：整理目录结构、导航、信息架构。

### Skills 管理

- `skill-manager`：维护当前项目期望安装的 skill 清单，并检查是否安装成功。

## 如何检查当前项目 Skills

当前项目的真实清单是：

```text
.agents/skills/skill-manager/references/desired-skills.json
```

查看项目 scope 的 skills：

```bash
npx skills list --json
```

验证项目期望清单是否全部安装：

```bash
python3 .agents/skills/skill-manager/scripts/verify_manifest.py
```

如果以后更新了清单，需要补装缺失 skills：

```bash
python3 .agents/skills/skill-manager/scripts/install_manifest.py
```

## 全局 Skills 状态

本项目相关 skills 已迁移到 `.agents/skills/`。

全局目录 `~/.codex/skills/` 里当前只保留原先已有的 `brainstorming`，以及 Codex 系统内置的 `.system` skills。这样可以避免其他项目自动使用本项目专用的 Obsidian 和内容管理 skills。

## 使用建议

- 修改 Obsidian 笔记链接时，优先使用 `$obsidian-markdown`。
- 设计案例库、作品集表格时，使用 `$obsidian-bases`。
- 梳理 vault 目录和导航时，使用 `$information-architecture`。
- 改 README、说明文档、更新记录时，使用 `$markdown-documentation` 或 `$copy-editing`。
- 自动检查、commit、push 当前改动时，使用 `$git-auto-sync`。
- 设计提交前自动检查时，使用 `$git-hooks-setup`。
- 处理 GitHub PR / issue 评论时，使用 `$gh-address-comments`。
- 维护或检查 skills 安装状态时，使用 `$skill-manager`。
