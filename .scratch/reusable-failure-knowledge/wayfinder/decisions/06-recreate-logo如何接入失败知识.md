# recreate-logo 如何接入失败知识

## Question

recreate-logo 在哪些节点处理图片失败知识？

## Decision

1. 在源资产预检和修正分流处引用图片失败条目。
2. 任一精确不变量与父资产不一致时停止全图生成修正。
3. 不得只加强 Prompt 后重复相同生成路径。
4. 返回直接父资产，使用授权区域内的局部编辑或确定性处理。
5. 修正 Prompt 明确不适用于精确不变量偏差。
6. Skill 不保存具体案例过程。

## Rationale

精确不变量需要可验证的局部或确定性方法，全图生成不能保证锁定内容不漂移。

## Consequences

普通视觉差异与精确不变量偏差必须在进入修正 Prompt 前分流。

## Status

Accepted
