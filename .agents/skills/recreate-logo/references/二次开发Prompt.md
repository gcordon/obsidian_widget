# 二次开发 Prompt

用于基于已有资产改变用户授权的内容，形成新的派生 Logo 资产。

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
- Treat every pixel outside the authorized edit regions as immutable.
- Reuse Image 2's canvas and background; do not regenerate them.
- Fit each replacement inside its corresponding original content region.
- Unless explicitly authorized, do not change the combined foreground bounding box, layer positions, element geometry, palette, or negative space.

Primary request:
Edit Image 2 into the stated output asset. Apply only the confirmed changes and preserve every correct property not listed for change.

Constraints:
- Do not overwrite Image 2.
- Do not add, remove, redesign, or reinterpret unapproved content.
- Do not introduce extra text, symbols, effects, colors, or layout changes.
- Do not rescale, recenter, rearrange, redraw, or regenerate locked content.
- Render all user-provided content verbatim.

Output:
<填写本次确认的尺寸、格式和背景要求，并使用新的文件或版本>
```
