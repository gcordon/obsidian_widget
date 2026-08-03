# 修正 Prompt

用于按当前任务模式比较权威资产、用户确认目标与当前稿，并生成单轮修正稿。

```text
Task mode: <recreation or secondary development>

Input images:
- Image 1: root authoritative reference. It controls provenance and visual language.
- Image 2: <复刻时为当前稿；二次开发时为控制现有版式和可继承内容的直接父资产>
- Image 3: <仅在二次开发时填写当前稿；复刻时删除本行>

Current draft: <复刻填写 Image 2；二次开发填写 Image 3>
User-confirmed target: <复刻填写还原目标；二次开发填写新内容和允许变化范围>

按当前模式比较适用的权威资产、用户确认目标与当前稿，只修正最明显的 1—3 个差异。

本轮修正：
1. <具体差异与目标状态>
2. <具体差异与目标状态>
3. <具体差异与目标状态，可省略>

保持不变：
- <已经正确的部分>
- <已经正确的部分>

不要重新设计整个 Logo。
不要增加权威资产或用户确认目标中不存在的内容。
不要改动未列入本轮修正项的正确部分。
复刻时继续匹配根权威参考的全部确认特征。
二次开发时由根权威参考控制视觉语言、直接父资产控制现有版式和可继承内容、用户确认目标控制新内容；不得恢复已被确认替换的旧内容。
```
