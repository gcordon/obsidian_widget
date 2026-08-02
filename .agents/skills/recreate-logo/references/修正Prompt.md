# 修正 Prompt

用于比较唯一权威参考图与当前稿，并生成单轮修正稿。

```text
Input images:
Image 1 is the only authoritative reference.
Image 2 is the current draft.

比较 Image 1 与 Image 2，只修正当前稿中最明显的 1—3 个差异。

本轮修正：
1. <具体差异与目标状态>
2. <具体差异与目标状态>
3. <具体差异与目标状态，可省略>

保持不变：
- <已经正确的部分>
- <已经正确的部分>

不要重新设计整个 Logo。
不要增加参考图中不存在的内容。
不要改动未列入本轮修正项的正确部分。
继续匹配原图的构图、文字、颜色、比例、位置、间距和视觉效果。
```
