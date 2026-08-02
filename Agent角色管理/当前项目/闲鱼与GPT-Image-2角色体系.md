# 闲鱼 × GPT Image 2：项目 Agent 角色体系

> 调研日期：2026-07-24；角色决策更新：2026-07-27  
> 调研范围：Agent 编排、创意图片生产、营销发布、质量门禁与数据反馈  
> 来源原则：优先采用厂商官方文档、官方工程博客与官方指南

> 文档定位：本文件保存角色体系的完整说明、设计依据和测试上下文。项目执行以根目录 [AGENTS.md](../../AGENTS.md) 为唯一规则源；日常速查请查看 [当前角色与流程](../../当前角色与流程.md)。

## OpenAI 官方文档索引

| 设计问题 | OpenAI 官方文档 | 当前项目的应用 |
|---|---|---|
| 多 Agent 的控制权与委派 | [Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) | 采用 `Manager / Agents-as-tools`，项目协调 Agent 保留最终答复和流程控制权 |
| 自动检查与人工批准 | [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | 生图、发布、改价、删除和下架保留用户批准，不由 Agent 自动放行 |
| 运行记录与可观测性 | [Integrations and observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability) | 记录本轮启动的角色、工具、来源、输出和流程偏差 |
| Agent 工作流评估 | [Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) | 质量与实验评估 Agent 检查角色选择、工具调用、单变量、指令与审批是否正确 |
| GPT Image 2 能力边界 | [GPT Image 2 model](https://developers.openai.com/api/docs/models/gpt-image-2) | `gpt-image-2` 只作为视觉生产工具，不承担项目编排或最终验收 |

> 上述页面已于 2026-07-27 通过 OpenAI Developer Docs 重新核对。官方文档提供通用能力与边界；表中“当前项目的应用”是基于项目约束作出的本地决策，不是 OpenAI 原文。

## 结论

本项目采用 **5 个固定逻辑角色（按需启动）+ 1 个真人决策门禁**：

1. 项目协调 Agent
2. 闲鱼市场情报 Agent
3. 闲鱼运营与数据 Agent
4. 视觉创作 Agent
5. 质量与实验评估 Agent
6. 用户本人：最终批准者，不计入 Agent 数量

编排方式采用 **Manager / Agents-as-tools**：项目协调 Agent 是唯一对话入口，按需调用四个专家，统一保存上下文、汇总结果和控制流程。专家不相互自由 handoff，也不要求同时运行。

这不是模拟一家完整广告公司，而是保留五个不可混同的责任：**决策、外部情报、内部增长、视觉生产、独立评估**。创意策略并入视觉创作，文案并入闲鱼运营，发布包整理并入项目协调。本项目不增加发布执行 Agent，实际发布和高影响线上操作仍由用户确认并手动执行。

## 一、来源事实

以下内容是来源明确表达的事实，不是本项目自行推断。

### 1. 多 Agent 的共同设计模式

- OpenAI 将常见多 Agent 编排分为两类：
  - `Agents as tools`：经理保留控制权，调用专家并综合输出；适合需要一个 Agent 持有最终答案和统一 guardrails 的场景。
  - `Handoffs`：分诊 Agent 把控制权转给专家；适合专家直接接管后续对话的场景。  
  来源：[OpenAI：Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)

- OpenAI 建议尽可能从单 Agent 开始；只有当新角色能实质改善能力隔离、策略隔离、提示清晰度或轨迹可读性时才拆分。过早拆分会增加提示、轨迹和审批面。  
  来源：[OpenAI：Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration#add-specialists-only-when-the-contract-changes)

- OpenAI 将 guardrails 用于自动检查，将 human review 用于敏感动作的批准；输入、输出和工具调用应在各自边界附近验证。  
  来源：[OpenAI：Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals)

- OpenAI 建议先用 traces 调试单次运行，再用 graders、datasets 和 eval runs 系统性评估工具选择、委派、指令和安全策略是否正确。  
  来源：[OpenAI：Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)

- Anthropic 的 `orchestrator-workers` 模式由中心 Agent 动态拆分、委派并综合；`evaluator-optimizer` 模式让生成者和评估者循环改进，但只适合评价标准清晰、迭代确有价值的任务。  
  来源：[Anthropic：Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

- Anthropic 的生产研究系统采用 lead agent、并行 subagents 和最终 citation agent；官方同时指出，多 Agent 适合真正独立、可并行、广度优先的高价值任务，并会显著增加 token 消耗。  
  来源：[Anthropic：How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

- Google ADK 的 collaborative workflow 由 coordinator 委派给职责明确的 subagents；子任务可选择完整对话、任务模式或隔离单轮模式，任务完成后返回父 Agent。  
  来源：[Google ADK：Collaborative workflows](https://adk.dev/workflows/collaboration/)、[Google ADK：Workflows](https://adk.dev/workflows/)

- LangChain 的 subagents 模式由 supervisor 统一路由、维护用户记忆并合并结果；官方明确提醒，复杂任务并不必然需要多 Agent，单 Agent 加合适工具经常足够。  
  来源：[LangChain：Subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)、[LangChain：Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent)

- Microsoft AutoGen 把 handoff、group chat、worker/aggregator 作为不同模式：handoff 转移任务与上下文，group chat 由 manager 决定下一位发言者，worker 结果由单一 orchestrator 聚合。  
  来源：[AutoGen：Handoffs](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/handoffs.html)、[Group Chat](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html)、[Mixture of Agents](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/mixture-of-agents.html)

- CrewAI 的 hierarchical process 由 manager 规划、委派并验证结果；官方建议把 delegation 开给协调者，专注型专家关闭 delegation，以降低反复转派和循环风险。  
  来源：[CrewAI：Processes](https://docs.crewai.com/en/concepts/processes)、[Hierarchical Process](https://docs.crewai.com/en/learn/hierarchical-process)、[Collaboration](https://docs.crewai.com/en/concepts/collaboration)

### 2. GPT Image 2 与创意生产

- GPT Image 2 支持文本和图片输入、图片输出，可用于高质量生成和编辑，并支持灵活尺寸和高保真图片输入；但模型本身不支持 function calling 或 structured outputs，因此它应作为视觉生产工具，而不是整个业务流程的编排者。  
  来源：[OpenAI：GPT Image 2 model](https://developers.openai.com/api/docs/models/gpt-image-2)

- OpenAI 建议广告提示写成创意 brief，包含品牌定位、目标受众、氛围、概念、构图和准确文案；复杂提示应按“背景/场景 → 主体 → 关键细节 → 约束”组织。  
  来源：[OpenAI：GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

- 官方建议显式区分“需要改变的内容”和“必须保持的不变量”，每轮重复 preserve 清单，并采用“只改 X、其他保持不变”的小步迭代来减少漂移。  
  来源：[OpenAI：GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

- GPT Image 模型仍可能在精确文字、跨轮品牌一致性、布局敏感构图上出错；提示和输出都会经过内容过滤。因此生成结果仍需要独立检查，不能视为自动通过。  
  来源：[OpenAI：Image generation—Limitations and Content Moderation](https://developers.openai.com/api/docs/guides/image-generation)

### 3. 营销生产、审批与数据闭环

- Adobe 的官方营销生成流程把品牌、产品、Persona、参考素材和模板作为生成上下文；生成变体后进行品牌、平台与无障碍检查，再送交利益相关者审批。  
  来源：[Adobe GenStudio：Create overview](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/create/overview)

- Adobe 把 Reviewer 和 Approver 分权：Reviewer 可以评论但不能批准；Approver 才拥有放行权，修改草稿会重新进入审批。  
  来源：[Adobe GenStudio：Reviews and approvals](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/approve/overview)

- Adobe 的自动验证能提供品牌、平台和无障碍检查结果，但客户仍对自身法律与无障碍合规负责；机器审校不能替代责任主体。  
  来源：[Adobe GenStudio：Brand validation](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/guidelines/brand-validation)

- Adobe Insights 将曝光、点击、CTR 等发布后数据回流到内容分析，并可按颜色、构图、主体和风格等属性比较表现，用于形成下一轮变体。  
  来源：[Adobe GenStudio：Insights overview](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/insights/overview)、[Attributes](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/insights/attributes/attributes)

- OpenAI 建议为失败次数过多以及敏感、不可逆或高风险操作设置人工介入；早期部署尤其需要 human-in-the-loop 来发现边界案例并建立评估循环。  
  来源：[OpenAI：A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)

## 二、针对本项目的推断

以下是依据上述事实和当前项目约束作出的设计判断，不是来源原话。

### 1. 最小充分角色体系

| 角色 | 职责 | 必要输入 | 标准输出 | 禁止事项 |
|---|---|---|---|---|
| 项目协调 Agent | 维护阶段和版本；拆解本轮唯一事项；调用专家；汇总并向用户提出一个明确决策 | 项目规则、用户目标、当前版本、专家结论 | 本轮任务 brief、执行顺序、单一建议、状态记录 | 不绕过审批；不同时改多个关键变量；不把自己的汇总当独立验收 |
| 闲鱼市场情报 Agent | 研究平台规则、同类商品、关键词、价格、首图和服务结构；保留来源和时间 | 研究问题、商品品类、样本标准、允许的网络/浏览器工具 | 事实表、样本表、来源、查询时间、不确定性 | 不把竞品做法当平台规则；不决定修改方案；不操作闲鱼 |
| 闲鱼运营与数据 Agent | 读取曝光、浏览、想要、咨询和成交；结合外部情报；提出可检验的单变量实验 | 商品版本、数据快照、观察窗口、市场情报输出 | 漏斗诊断、证据强度、一个假设、单变量实验和停止条件 | 不把小样本当确定结论；不直接改线上商品；不虚构平台规则或竞品数据 |
| 视觉创作 Agent | 把已确认目标整理成创意 brief 和 GPT Image 2 提示；生成或执行单变量编辑；记录版本与不变量 | 已确认方案、参考图、品牌不变量、文字、尺寸、输出格式 | 创意 brief、生成提示、候选图、修改清单、版本说明 | 未获当次“开始生图”不得调用生图；不擅自改定位；不发布；不自我批准 |
| 质量与实验评估 Agent | 独立检查图片、文案、发布包与数据实验；评估角色、工具、审批和单变量是否正确 | 验收标准、候选产物、数据起点、实验方案、执行记录 | `Pass` / `Needs work`、证据、阻断问题、返工指令、可重复评分标准 | 不参与生产；不直接改成品；不为通过而降低标准；不发布 |
| 用户本人 | 决定方向、批准生图方案、批准最终版本与线上动作 | 协调 Agent 汇总的完整决策包 | 明确批准、驳回或修改意见 | 最终责任不转交给自动审校 |

### 2. 为什么是 5 个 Agent，而不是 4 个或更多

**不能再少的原因：**

- 生产者不能成为唯一验收者，因此视觉创作和质量评估必须分开。
- 市场情报使用外部网络/浏览器证据，运营与数据使用项目内部漏斗；拆分后可以避免调研偏见直接变成修改结论。
- 运营与数据依赖实验设计，视觉创作依赖品牌、构图和 GPT Image 2 约束，两者的输入、工具和评价标准不同。
- 需要一个角色持续保存全局状态和审批边界，否则专家输出容易互相冲突或遗失上下文。

**暂时不再增加的原因：**

- “创意策略 / Prompt 工程师”并入视觉创作：当前只有一个商品和一个视觉生产链路。
- “文案 / SEO / 数据分析”并入闲鱼运营：目前数据规模不足以支持三个独立岗位同时优化。
- 本项目明确不增加“发布执行 Agent”：整理发布包由协调 Agent 完成，真正发布、改价、删除、下架和对外承诺由用户确认并手动执行。
- “流程观测 Agent”不单独设置：当前先由质量与实验评估 Agent 使用检查表；只有在形成可重复的自动运行轨迹后才引入独立 Evals 角色。

只有在以下情况出现时才继续拆分：同时运营多个商品；不同角色的提示出现大量冲突；工具经常选错；数据量足以支撑独立分析；发布动作形成稳定、可审计且获授权的自动化流程。

### 3. 推荐编排方式

```text
用户
  ↓ 目标 / 批准
项目协调 Agent（唯一入口、持有完整上下文）
  ├─ 调用闲鱼市场情报 Agent
  ├─ 调用闲鱼运营与数据 Agent
  ├─ 调用视觉创作 Agent
  └─ 调用质量与实验评估 Agent
  ↓ 汇总为一个决策包
用户批准
  ↓
用户手动执行线上动作并记录新数据
```

具体规则：

1. 默认按固定状态机推进：`观察 → 情报 → 诊断 → 方案 → 用户批准 → 生产 → 评估 → 用户批准 → 用户手动发布/修改 → 记录数据`。
2. 只有互不依赖的任务并行，例如市场资料搜索与视觉参考分析；生产、评估、批准和发布必须顺序执行。
3. 专家作为工具返回结构化结论，不接管用户对话；当前没有使用 handoff 的必要。
4. 每一轮只改变一个关键变量，确保数据变化能够归因。
5. 两道人工门不可省略：
   - 每次调用图片生成工具前，用户在当次方案汇总后明确回复“开始生图”。
   - 发布、改价、删除、下架、对外承诺或其他账号动作前，用户确认最终操作内容。
6. 评估不通过时回到对应生产角色；连续失败达到预设次数后停止自动重试并交还用户。
7. 本项目不设发布执行 Agent；所有闲鱼账号动作由用户确认并手动执行。

### 4. 角色如何在 Codex 中启用

这 5 个是固定的逻辑角色，不是 5 个长期运行的进程。实际增加方式如下：

1. 在项目根目录 `AGENTS.md` 中记录角色职责、权限和始终成立的不变量。
2. 项目协调 Agent 判断当前事项需要哪种独立上下文或工具，只启动必要角色。
3. 启动时根据本文档的“角色调用模板”组装一次性任务 brief，将角色职责与本轮具体问题合并。
4. 专家只读取完成子任务所需的文件和数据，按规定格式返回，不直接与用户对话。
5. 项目协调 Agent 检查输出是否越权、是否需要评估或用户批准，再决定下一步。

不需要立即为每个角色创建独立 Skill 或单独 Markdown 文件。当某个角色的流程跨多个案例重复出现，且拥有稳定的输入、输出和验证步骤时，再升级为独立 Skill。

#### 自动识别规则

角色不是由用户逐一选择，而是由项目协调 Agent 在每轮开始时根据任务信号自动取并集：

| 任务信号 | 自动加入的角色或门禁 |
|---|---|
| 记录、读取或分析内部商品数据 | 闲鱼运营与数据 Agent |
| 查询平台规则、竞品、关键词、市场价格等外部或时效性信息 | 闲鱼市场情报 Agent |
| 优化标题、价格、介绍或服务定位 | 闲鱼市场情报 Agent + 闲鱼运营与数据 Agent |
| 分析、生成或编辑视觉素材 | 视觉创作 Agent |
| 制定修改方案/实验、修改角色或流程规则、形成候选成品/发布材料 | 质量与实验评估 Agent，最后独立执行 |
| 发布、改价、删除、下架或其他账号副作用 | 账号操作本身不增加专家 Agent；按同时涉及的内容优化、图片修改或数据记录信号增加对应角色；进入用户批准门，由用户手动执行 |

项目协调 Agent 始终必需。纯外部事实查询不自动增加质量评估；当查询结果进一步形成项目决策、修改方案或交付物时才增加。图片任务还要叠加项目根目录 `AGENTS.md` 的当次生图授权规则。

开始实质工作前必须记录：

```yaml
task_type: 本轮任务类型
required_roles:
  - 项目协调 Agent
skipped_roles:
  - 未启动的固定角色
skip_reasons:
  未启动的固定角色: 与本轮任务无对应信号
```

这份记录既让用户看到实际调用计划，也让完成闸门能够检查是否漏调角色。角色计划形成后，协调 Agent 再按本文档的“角色调用模板”委派。

#### 完成闸门

提交结论前计算：

```text
missing_roles = required_roles - completed_roles
```

- 有缺失角色：先补调；无法补调时明确报告任务未完成，不得用协调 Agent 的自检代替专家调用。
- 涉及方案、实验、候选交付物、发布材料或角色/流程规则修改时，质量与实验评估 Agent 必须最后独立执行。
- 质量评估者不得参与被评内容的生产；`Needs work` 必须返工并重新评估。
- 用户批准门不属于 Agent，不能填补 `missing_roles`；账号操作仍由用户批准并手动执行。

常见路由：

| 当前事项 | 启动角色 | 顺序 |
|---|---|---|
| 记录新数据 | 项目协调、闲鱼运营与数据 | 记录 → 判断证据强度 |
| 调整标题/价格/文案 | 项目协调、市场情报、运营与数据、质量与实验评估 | 情报 → 单变量方案 → 评估 → 用户手动修改 |
| 调整商品图片 | 项目协调、视觉创作、质量与实验评估；仅在任务同时要求市场或数据诊断时叠加对应角色 | 汇总本次全部图片方案 → 用户明确回复“开始生图” → 生产 → 评估 → 用户批准；后续重生成需重新汇总和授权 |
| 发布、改价、删除或下架 | 项目协调；账号操作本身不增加专家 Agent，按同时涉及的内容优化、图片修改或数据记录信号增加对应角色 | 准备当前事项所需资料 → 用户确认并手动执行 |

## 三、可立即采用的角色调用模板

每次委派给专家时，项目协调 Agent 至少提供：

```text
目标：本次只解决什么问题
输入：允许使用的文件、数据、参考和来源
不变量：无论如何都不能改变的内容
输出：需要返回的格式和验收标准
权限：允许读取、生成、修改或发布到哪一步
停止条件：何时返回协调者或升级给用户
```

该模板把角色边界建立在目标、上下文、工具、权限和验收责任上，而不是建立在“模拟公司职位名称”上。它更适合当前项目，也更容易在真实数据增加后逐步扩展。

## 四、增加角色前后对比

### 1. 对比口径

- **增加前**：以 2026-07-27 的标题优化任务为已发生样本。现有问题记录能确认应独立启动的质量与实验评估角色缺失，但未完整保存其余角色的完成清单，因此不计算增加前的角色完整率。
- **增加后**：以自动路由的 6 个固定盲测用例为验证样本；盲测者只读取 `AGENTS.md`，最终由未参与规则生产的质量与实验评估 Agent 独立复验。
- **效率**分为角色参与效率和真实运行效率。当前只能计算角色参与次数；尚未持续记录总耗时、Token、返工轮次，因此不能宣称真实运行成本已经下降。
- **完善程度**按角色是否完整、是否独立评估、是否存在审批门、是否可追溯和是否失败关闭来判断。

### 2. 效率对比

| 指标 | 增加前 | 增加后 | 判断 |
|---|---|---|---|
| 角色选择方式 | 协调 Agent 临时判断 | 根据任务信号自动取并集 | 减少依赖临场记忆 |
| 标题优化任务的角色参与 | 已确认缺少质量与实验评估；其余完成角色未形成可独立复算的完整清单 | 规则要求 `4` 个，包含最后独立评估 | 补齐质量门，不把角色增加误写为提速 |
| 六类测试的角色参与 | 无固定路由，无法稳定计算 | 合计 `16` 次：`2+4+3+2+3+2` | 相比每次固定启动全部 5 个角色的 `30` 次，减少 `14` 次，即 `46.7%` |
| 无关角色调用 | 无强制跳过记录 | 每轮声明跳过角色及原因 | 提供避免过度调用的约束，并使其可审计 |
| 返工效率 | 本次已发生样本的问题在协调 Agent 汇总后暴露 | 候选方案先独立评估，`Needs work` 立即返回生产角色 | 理论上降低错误流入用户执行环节的概率；尚无长期返工数据 |

`46.7%` 是固定测试集相对“所有任务都启动全部角色”的结构估算，不是相对旧流程的真实 Token 或时间降幅。角色增加后的效率目标不是让每次调用更少，而是让简单任务保持最小角色集合、复杂任务补齐必要检查。

### 3. 完善程度对比

| 完整性检查 | 增加前 | 增加后 |
|---|---|---|
| 必需角色识别 | 没有确定性路由表 | 有任务信号与角色映射 |
| 跳过角色说明 | 未强制记录 | 每轮必须记录 `skipped_roles` 和 `skip_reasons` |
| 生产与验收分离 | 标题优化曾由协调 Agent 自检，独立评估缺失 | 方案、实验和候选交付物必须由非生产者最后评估 |
| 漏调阻断 | 漏调后仍可能提交结论 | `missing_roles` 非空时不得声称完成 |
| 评估失败关闭 | 没有完整返工闸门 | `Needs work → 返工 → 独立复验 → Pass 后提交`；连续失败达到预设条件后停止并交还用户 |
| 用户权限边界 | 账号动作由用户执行，但未与自动路由统一检查 | 生图、发布、改价、删除和下架均进入明确人工门禁 |
| 测试与追踪 | 只有事后问题记录 | 有 6 个固定用例、完整盲测结果、首轮问题和复验结果 |

已观测结果：增加前的标题优化任务能确认至少缺少 `1` 个必需角色，但由于历史完成清单不完整，不计算完整率；增加后的固定路由测试为 `6/6` 通过，独立复验为 `Pass`。两者样本性质不同，因此只能证明当前规则补上了已知缺口，不能直接推断所有后续生产任务都会达到 `100%`。

### 4. 后续测量

从下一次真实商品任务开始，每轮补记以下指标，累计至少 5 轮后再判断真实效率：

- 计划角色数、实际完成角色数和漏调角色数。
- 从任务开始到候选方案通过的总耗时。
- 质量评估的 `Needs work` 次数和返工轮次。
- 用户批准前发现的问题数，以及执行后才发现的问题数。
- 可获得时记录各角色的 Token 或工具调用次数；无法取得时标为“未记录”，不估算。
