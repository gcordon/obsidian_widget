# ZIP 更新与备份规则

> zip 是阶段性备份和大版本更新工具，不是日常同步工具。

## zip 适合什么时候用

适合：

1. 第一次搭建 Obsidian 学习库；
2. 每周或每月让 GPT 帮你整体检查；
3. 需要生成新版 starter vault；
4. 需要备份完整学习系统；
5. 想把当前学习系统发给别人或迁移到另一台电脑。

不适合：

- 每天更新；
- 每天覆盖本地 Obsidian；
- 每次练习后都重新打包；
- 用来替代 Codex 本地整理。

## 推荐版本节奏

```text
v1：基础 Obsidian 学习库
v2：加入 Codex 使用指南
v3：加入图片工作流和 80_Assets 图片目录
v4：加入 ChatGPT Project、日常学习流程、zip 使用规则
```

## 每次更新 zip 前要做什么

1. 本地 Obsidian 先不要有未保存内容；
2. 如果使用 Git，先提交一次：

```bash
git status
git add .
git commit -m "更新 zip 前备份"
```

3. 不要直接覆盖旧 vault，建议新版本单独解压；
4. 确认无误后，再把新文件合并到旧 vault。

## 每次让 GPT 更新 zip 时，应该提供什么

优先提供：

- 最近新增的 Markdown；
- 当前目录结构；
- 你想新增的工作流；
- 你觉得混乱的部分；
- 需要保留的旧文件；
- 不允许删除的内容。

不一定每次都要上传所有图片。图片学习时，图片最好直接单独上传给 ChatGPT 做视觉分析。

## 本地合并建议

如果新版 zip 是一个 starter vault，不建议无脑覆盖旧 vault。

更稳的做法：

```text
1. 解压新版 zip 到新文件夹
2. 用 Obsidian 打开新文件夹检查
3. 只把新增指南、Prompt、模板复制到旧 vault
4. 旧 vault 的 Daily、Cases、Assets 不要被覆盖
```

## 对你当前系统的建议

你当前应该把 zip 当成：

- 每月大版本备份；
- 大结构更新工具；
- 给 ChatGPT 理解系统的资料包。

日常学习仍然应该走：

```text
ChatGPT 图片练习 → Obsidian 保存 → Codex 整理
```
