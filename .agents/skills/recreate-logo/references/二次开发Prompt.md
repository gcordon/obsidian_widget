# 二次开发 Prompt

用于基于已有资产改变用户授权的内容，形成新的派生 Logo 资产。

1. 填写 Prompt（提示词模板）前，按用户已确认规格区分允许变换与锁定属性。未授权的版式、内容和视觉特征继续保留。
2. 用户明确允许提取、缩放、居中或更换画布时，只开放对应变换；不得再用父画布或原位置锁定条款禁止这些已授权变化。
3. 同画布局部编辑或用户要求像素精确保留时，保留下方精确锁定条款，并执行 Skill 的精确不变量验证。允许展示变换不等于允许改变其他 Logo 设计特征。

```text
Task mode: secondary development
Output asset identity: <填写新资产代表的 Logo、品牌、版式或用途>

Input images:
- Image 1: root authoritative reference. It controls provenance and visual language.
- Image 2: direct parent asset and actual edit target. It controls the current layout and inheritable content.
- Image 3..N: <仅在实际使用其他输入时逐一填写角色；否则删除>

Authority:
- Follow Image 1 for the source identity and visual language.
- Follow Image 2 for the existing composition, geometry, and content marked for preservation.
- Follow the user-confirmed change specification below for all new content.
- If these authorities conflict, stop instead of inventing a resolution.

User-confirmed change specification:
- New content: <填写用户确认的新文字、品牌、版式或用途>
- Change only: <填写允许改变的内容>
- Preserve: <填写必须继承的内容、结构、位置、比例和视觉特征>

Locked invariants:
- Authorized edit regions: <填写允许改变内容在 Image 2 中的对应区域>
- Authorized presentation transforms: <仅填写用户明确允许的提取、缩放、居中或换画布；未授权时填 none>
- Preserved properties: <填写未授权改变的内容、字形、几何、配色、层级及布局；不得包含上方已允许的变换>
- Preservation precision: <填写视觉特征继承或明确要求的像素/几何精度；不得将精确保留降为视觉相似>

Exact locks for same-canvas local edits or explicitly pixel-exact preservation:
<适用时保留以下条款；已授权变换使其不适用时删除对应条款，并在上方明确仍须保留的属性>
- Treat every pixel outside the authorized edit regions as immutable.
- Reuse Image 2's canvas and background; do not regenerate them.
- Fit each replacement inside its corresponding original content region.
- Preserve the combined foreground bounding box, layer positions, element geometry, palette, and negative space except for explicitly authorized changes.

Primary request:
Edit Image 2 into the stated output asset. Apply only the confirmed changes and preserve every correct property not listed for change.

Constraints:
- Do not overwrite Image 2.
- Do not add, remove, redesign, or reinterpret unapproved content.
- Do not introduce extra text, symbols, effects, colors, or layout changes.
- Apply only the authorized presentation transforms; do not otherwise rescale, recenter, rearrange, redraw, or regenerate locked content.
- Render all user-provided content verbatim.

Output:
<填写本次确认的尺寸、格式和背景要求，并使用新的文件或版本>
```
