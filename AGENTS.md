# Brawl Stars Knowledge Base Rules

这个仓库是一套由 LLM 维护的 Markdown Wiki，用来持续积累、整理和更新《荒野乱斗》相关知识。

本文件是 agent 参与项目维护的完整信息索引。未来 session 应先读本文，再按任务读取 `wiki/index.md`、相关 wiki 页面和必要 skill references；目标是让维护路径不重不漏。

## Agent 维护入口

| 入口 | 作用 | 何时使用 |
| --- | --- | --- |
| `$markdown-llm-wiki` | 本库的通用 LLM-wiki 底座 skill，来源为 `https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki` | 所有通用 wiki ingest、query、lint、AGENTS 修复和结构治理 |
| `AGENTS.md` | 本仓库本地维护契约 | 每次维护先读，用来覆盖或细化 `$markdown-llm-wiki` 的通用规则 |
| `wiki/index.md` | 内容导航入口 | query、ingest、lint 时用来定位页面和检查导航覆盖 |
| `wiki/log.md` | 维护操作日志 | ingest、重要 query、lint、结构变更和 cleanup 后追加 |
| `skills/brawl-stars-bp-knowledge-maintenance/` | BP 知识维护 skill，`$markdown-llm-wiki` 的 Brawl Stars BP 领域子集 | source ingest、英雄/地图建模、BP profile 审计、runtime 边界治理 |
| `skills/run-brawl-stars-bp/` | BP 裁判 / 对局编排 skill | 运行模拟 BP、同步 ban、顺序 pick、生成 match report |
| `skills/brawl-stars-bp-slot-decision/` | 单手 BP 决策 skill | 执行 `compile` / `decide`，从稳定事实和 `runtime_bp_index` 做选手侧决策 |

## 项目目录索引

```text
raw/
  inbox/
  sources/
    fandom/
      heroes/
      maps/
      modes/
      gameplay/
      systems/
    pl-prodigy/
      brawlers/
    roster/
    supercell/
    liquipedia/
      events/
  assets/                  # optional
wiki/
  index.md
  log.md
  sources/
  concepts/
  entities/
    brawlers/
    maps/
    events/
  syntheses/
skills/
  brawl-stars-bp-knowledge-maintenance/
  run-brawl-stars-bp/
  brawl-stars-bp-slot-decision/
outputs/
  bp-simulations/
```

### 目录职责速查

| 目录 / 文件 | 职责 | 写入规则 |
| --- | --- | --- |
| `raw/inbox/` | 临时进入的用户输入、待归档资料 | ingest 前可新增；整理后应迁入合适 raw/source 层或保留为原始说明 |
| `raw/sources/fandom/heroes/` | Fandom 英雄 direct raw capture | 只新增或明确 cleanup；不反写整理结果 |
| `raw/sources/fandom/maps/` | Fandom 地图页和 Ranked 地图池 raw capture | 地图 ingest 的来源层；不写稳定 BP 结论 |
| `raw/sources/fandom/modes/`、`gameplay/`、`systems/` | Fandom 模式、资源、系统 raw capture | 用于概念页和来源页复核 |
| `raw/sources/pl-prodigy/brawlers/` | Power League Prodigy 英雄竞技 guide raw capture | 与 Fandom 英雄 raw 互补，不能互相覆盖 |
| `raw/sources/roster/` | 英雄集合 manifest 和来源覆盖清单 | 决定 BP-active 英雄集合的输入 |
| `raw/sources/supercell/` | Supercell 官方资料或公告 raw capture | 优先级高，但仍先进入 source 摘要 |
| `raw/sources/liquipedia/events/` | Liquipedia 赛事页面的 revision-specific MediaWiki raw capture | 仅通过 API 抓取；保留完整 wikitext、revision、许可归属和解析 JSON |
| `wiki/sources/` | 单篇来源摘要、解释、provenance 和可用范围 | ingest 必先更新；不替代 raw |
| `wiki/concepts/` | 模式、货币、机制、规则等抽象概念 | 保存稳定规则事实，不放临时 meta；`英雄名称归一化` 是跨 skill 的称谓归一化原语 |
| `wiki/entities/brawlers/` | 单英雄稳定事实、当前 BP 建模字段和经复核的 `combat_breakpoint_profile` | 不保存版本历史、批处理进度、全量斩杀矩阵或临时强度覆盖 |
| `wiki/entities/maps/` | 单地图稳定结构和 BP 可消费地图因素 | 不保存当前强势英雄或 season-only 状态 |
| `wiki/entities/events/` | 单项赛事的身份、赛区、赛制、结果和已进行 set 等事实 | 赛事频率不直接提升为英雄强度或 runtime 规则 |
| `wiki/syntheses/` | 维护者讨论、方法论、跨来源结论和归档 | 不是 BP runtime 依赖；执行规则采纳后复制进 skill references |
| `skills/*/` | 可执行 agent skill、references、scripts 和契约测试 | 运行时或维护规则以这里为准；大段 wiki 讨论不能替代 skill 规则 |
| `outputs/` | 审计报告、模拟报告、`runtime_bp_index`、临时交付物 | 已 gitignore；不写回长期 wiki |

## 知识架构与 BP Skill 边界

本仓库同时承载“人类 / 维护者可读的 wiki”和“agent skill 可执行的运行时知识”。两者不能混为一层。

### 层级职责

| 层 | 目录 / 文件 | 职责 | BP skill 是否可作为运行时依赖 |
| --- | --- | --- | --- |
| 原始来源层 | `raw/` | 保存不可变原始资料、抓取件、用户输入原文 | 不可读，除非执行 ingest / 复核任务 |
| 来源摘要层 | `wiki/sources/` | 对单篇来源做摘要、解释、索引和 provenance | 不可作为默认运行时依赖；仅维护 / 复核时读取 |
| 稳定事实层 | `wiki/entities/`、必要的 `wiki/concepts/` | 保存可持续追踪对象和稳定规则事实 | `compile` 可读，是 BP 索引事实源 |
| 维护综合层 | `wiki/syntheses/` | 维护者讨论、方法论、跨来源结论、架构决策和归档 | `compile` / `decide` 都不可直接读取 |
| Skill 规则层 | `skills/*/SKILL.md`、`skills/*/references/` | 可执行 skill 的渐进披露文档和操作规则 | skill 自己必须优先读取 |
| 运行产物层 | `outputs/` 或调用方指定路径 | 临时报告、审计输出、`runtime_bp_index` 编译产物 | `decide` 可读对应 runtime index；不写回 wiki |

### 单向同步规则

- `wiki/syntheses/` 可以讨论 BP 方法论，但讨论结论不会自动进入 skill。
- 只有当某条结论被明确采纳为执行规则时，才复制到 `skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md` 或 `runtime-decision-knowledge.md`，并同步更新契约测试。
- BP skill 执行时禁止临场读取 `wiki/syntheses/` 来补规则、候选或版本判断；否则 syntheses 会从维护层滑回运行时依赖，破坏奥卡姆剃刀原则。
- 稳定事实从 `wiki/entities/` 进入 `compile`，强度理解从用户 / 裁判 / 外部 profile 进入 `compile`，二者共同生成 `runtime_bp_index`。
- `decide` 只消费 `runtime_bp_index` 和 skill 自身运行时规则；如果索引缺失或覆盖不足，先重新 `compile`，不要绕回 wiki syntheses。

### 英雄名称归一化规则

凡是解析用户输入、外部榜单、ban/pick 文本、`strength_profile`、候选池或报告中的英雄称谓，先读取 `wiki/concepts/英雄名称归一化.md` 的 fenced YAML 映射，归一化到 `wiki/entities/brawlers/*.md` 的 canonical name。canonical name 自身默认合法；`aliases` 自动映射；`ambiguous` 不自动归一，需结合上下文或请求用户确认。禁止在 skill、工具或输出中复制维护第二份别名表。

## Brawl Stars 分类约定

优先用“对象是什么”来决定页面类型，而不是只看名字像不像资料。

- `wiki/entities/`：游戏中的可指认对象
  - `英雄`、`战队`、`俱乐部`、`赛事`、`版本/补丁`、`地图/活动实例`
  - 英雄实体页统一放在 `wiki/entities/brawlers/`。
  - 地图实体页统一放在 `wiki/entities/maps/`。
- `wiki/concepts/`：规则、机制、类别、抽象系统
  - `模式`、`稀有度`、`货币`、`战斗机制`、`资源系统`、`定位术语`
- `wiki/sources/`：单篇来源的摘要与索引
  - 官方公告、Fandom 条目、攻略原稿、人物/模式介绍页
- `wiki/syntheses/`：跨来源整合后的专题结论
  - meta 分析、模式对比、新手成长路线、版本演化、资源系统总览

赛事来源先写入 `raw/sources/liquipedia/events/` 和 `wiki/sources/`，可持续追踪的赛事事实进入 `wiki/entities/events/`。逐 set 选用、ban 和结果聚合生成 `outputs/esports/` 下的 `tournament_observation_profile.v1`；它只用于描述与知识缺口审计，不得自动生成 strength tier、稳定对位边、地图 fit 或 BP runtime 推荐。

每次平衡补丁中的英雄血量、离散伤害包、固定护盾和减伤变化，先在对应 `wiki/sources/` 页面建立 `balance_breakpoint_manifest.v1` 版本账本，再用英雄当前数值事实与 `wiki/concepts/伤害与生存断点.md` 规则生成 `outputs/balance-breakpoints/` 下的 `balance_breakpoint_audit.v1`。伤害变化应覆盖全部已索引目标状态；血量/减伤变化只能声明覆盖已复核攻击包，不得把裸 `Attack` 字段当完整一发。生成结果不得自动生成 strength tier、稳定 map fit、hard gate、slot eligibility、条件化对位边或 runtime 推荐。

如果一个词既像实体又像概念，按下面的优先级决定：

1. 能否被当作独立对象持续追踪。能，就放 `entities/`。
2. 它主要描述规则或分类体系。能，就放 `concepts/`。
3. 它是多页输入的整合结论。能，就放 `syntheses/`。

## 工作流

### 1. Ingest 新来源

当有新资料进入知识库时：

1. 优先把原始资料落到 `raw/` 中，再开始整理。
2. 对网页来源，如果没有现成导出文件，先在 `raw/sources/` 中创建一个 `raw capture` 文件，保存页面标题、URL、抓取日期、可见原文片段和必要元数据。
3. 只读取 `raw/` 中的原始资料，不把整理结果反写进 `raw/`。
4. 在 `wiki/sources/` 创建或更新对应的来源摘要页。
5. 更新受影响的概念页、实体页、专题页。
6. 更新 `wiki/index.md`，保证导航完整。
7. 在 `wiki/log.md` 追加一条操作记录。

### Web 来源补充规则

- `raw/` 与 `wiki/sources/` 不是同一层：
  - `raw/` 保存来源本体或来源抓取件
  - `wiki/sources/` 保存对来源的摘要、解释与索引
- 如果历史页面已经写入 `wiki/sources/`，但没有 `raw/` 对应文件，允许分批回填 `raw`。
- 对 Fandom 站点，优先放到 `raw/sources/fandom/` 下，并按主题分目录，例如 `heroes/`、`modes/`、`gameplay/`、`systems/`。
- `raw capture` 文件应尽量保持不可变；如果需要重抓，新增新文件或在文件头注明抓取日期，不要把旧抓取静默改写成新版本。

### 来源版本与覆盖清理规则

- 同一来源的纠错重抓或增量重抓可以在临时工作阶段使用后缀区分，但不能成为长期 wiki 概念或 canonical 文件名。
- `raw/` 归档完成后，同一来源只保留稳定 canonical 抓取件，例如 `raw/sources/fandom/heroes/<hero>-2026-06-30.md`；纠错过程、覆盖关系和删除记录写入 `wiki/log.md`。
- `wiki/sources/` 不应保留同一来源的平行版本摘要页。若新版摘要完整覆盖旧版，应合并到稳定 canonical source page，例如 `wiki/sources/Fandom-<Hero>.md`，删除旧摘要页并清理所有引用。
- `raw/` 清理的首要判断标准是语义冗余，而不是是否被当前 wiki、skill 或脚本文件直接引用。断链检查只能作为执行删除前的成本检查，不能作为“该不该删”的主要理由。
- 只有当同一来源的新抓取件被确认完整覆盖旧抓取件，或旧抓取件只是纠错前的重复版本时，才允许删除旧 raw；典型例子是同一 Fandom 英雄页的初版、日期版、纠错重抓覆盖链。
- 如果两个 raw 来源提供互补信息，即使它们描述同一个对象也不能互相删除。例如 Fandom 英雄页承载底层机制、定位和经验信息，Power League Prodigy 英雄页承载对位关系与常见构筑信息，二者应共同保留。
- 如果新版不是覆盖关系，而是补充不同字段、不同时间点、不同页面状态、不同来源视角或不同维护者判断，不能删除旧版；应在 source 摘要中说明差异，并把稳定结论整合到实体页或专题页。
- 删除 raw 时必须同步更新 `wiki/sources/` 的上游 raw 链接、实体页 provenance 和 `wiki/log.md`；但这些是执行层动作，不改变“是否冗余”的判断。
- 对 BP skill 运行时而言，raw 版本号不可作为强度或优先级信号；skill 只能通过 source 摘要、实体页稳定字段或 `runtime_bp_index` 消费已整理结论。

### Brawl Stars ingest 的建议顺序

为了适合从 Fandom 站点逐步学习，建议按这个顺序扩展：

1. 先从总览和基础概念开始。
2. 再进入稀有度、货币、模式、战斗规则等共用机制。
3. 然后逐个 ingest 英雄、地图、活动、组织和版本页面。
4. 最后再做专题综述，例如 meta、资源循环、模式对比和版本演化。

### Brawl Stars 页面粒度

- 英雄页应尽量承载单个英雄的稳定事实和当前最新 BP 建模字段。
- 英雄页归档到 `wiki/entities/brawlers/`，用于长期追踪单个英雄；版本强度、临时 meta 和 BP 结论不能作为历史覆盖层写入英雄页，若未形成定性 BP 模型变化，只能留在来源页、审计页、专题页或日志中。
- 模式页应描述胜利条件、地图/局内规则和适用英雄类型。
- 货币和稀有度页应归入概念，不要拆成实体页。
- 版本更新页适合先作为来源页，再视需要沉淀成专题页或版本实体页。

### 2. Query 基于 Wiki 回答问题

默认所有日常问答都是只读查询：只读 `wiki/index.md` 和相关页面后回答，不写 `wiki/`，不更新 `wiki/log.md`。

只有用户明确要求“维护知识库 / 记录 / 沉淀 / ingest / 更新页面 / 修复结构”，或明确提供新来源并要求纳入知识库时，才允许写入 wiki。

如果只是解释已有内容、列名单、做临时分析、回答 BP 问题、模拟 BP、评价阵容或讨论英雄强弱，不视为维护型 query；除非用户要求保存，否则不得创建 syntheses、修改实体页或追加日志。

不要自行用“长期价值”“重要”“以后可能有用”作为写入理由。是否持久化由用户显式触发；不确定时默认不写。

只有发生实际 wiki/raw/source/skill 变更时，才追加 `wiki/log.md`。

当用户提出问题时：

1. 先读 `wiki/index.md`。
2. 再读相关 wiki 页面，而不是直接从聊天记忆回答。
3. 基于现有页面综合回答，并明确引用使用到的 wiki 页面。
4. 只有维护型 query 才写入 `wiki/`。
5. 只有实际写入或结构变更才更新 `wiki/log.md`。

BP 推演、Ban Pick 建模、英雄克制关系、阵容评价和 draft 顺位相关问题分两类处理：

- 维护者讨论 / wiki 查询：先读 `wiki/index.md`，再读相关 syntheses、来源页、地图页、英雄页，并把有长期价值的结论沉淀回 wiki。
- BP skill 执行：不得把 `wiki/syntheses/` 作为运行时依赖。`brawl-stars-bp-slot-decision` 必须遵循自身 `compile` / `decide` 分治：`compile` 只读取 skill 内 `references/compile-knowledge.md`、`wiki/entities/maps/`、`wiki/entities/brawlers/` 与用户 / 裁判提供的强度输入，生成 `runtime_bp_index`；`decide` 只读取 skill 内 `references/runtime-decision-knowledge.md`、当前草稿状态和已生成的 `runtime_bp_index`。如果没有 runtime index，先编译或声明信息不足，不得临场改读 syntheses 来补决策。

执行全量英雄 BP 建模、补抓 Fandom/Power League Prodigy 英雄详情页、扩展英雄覆盖、地图 source ingest、平衡补丁断点审计、或批量升级 `wiki/entities/brawlers/` / `wiki/entities/maps/` 时，必须使用 `skills/brawl-stars-bp-knowledge-maintenance/`。先读该 skill 的 `SKILL.md`，再按任务读取 `references/source-ingest.md`、`brawler-modeling.md`、`map-modeling.md`、`balance-breakpoint-audit.md`、`audit-and-validation.md` 或 `runtime-boundary.md`。`wiki/syntheses/BP-英雄建模标准流程.md` 和 `wiki/syntheses/BP-维护归档.md` 只作为维护背景 / 历史归档，不是执行入口。该任务必须先读取 roster manifest，再按当前 BP-active 英雄集合分批保留 raw；已下架或无有效来源覆盖的 roster 行不进入 BP 英雄集合、PLP 缺口追踪、对位边或运行时编译索引。禁止直接批量生成 BP-ready 字段。

英雄页治理：`wiki/entities/brawlers/` 只保存当前最新的 BP 建模结果和当前稳定数值输入，不保存版本记录、补丁来源、更新过程、历史状态、`版本覆盖`、`当前 BP 判断` 或类似覆盖层段落。第一份 `bp_brawler_profile` YAML 只含 runtime 可编译字段；可追加第二份 fenced JSON `combat_breakpoint_profile`，只保存经复核的当前 target states、离散 damage packets、专属 defense modifiers/variants 和明确 exclusion，由 maintainer 断点脚本消费，runtime 必须忽略。版本 / meta 资料如果足以改变 BP 模型，必须直接内联改写该英雄已有的 `capability_vector`、`build_switches`、`map_feature_hooks`、`objective_contracts`、`failure_modes`、`conditional_matchups` 或 `slot_notes` 等稳定字段；如果不能确定定性影响，只能留在来源页、审计页或日志，不能写进英雄页。

地图知识必须分层治理：稳定地图结构写入 `wiki/entities/maps/` 下的单地图实体页；Ranked 赛季页面只作为地图池索引；版本强势英雄、新英雄和 meta 变化先写入来源页、审计页或日志。只有当它们改变能力类型、职责归类、硬门槛、对位成立条件、地图 hook 或 slot 策略时，才直接更新对应英雄页或地图页的稳定 BP 字段。运行时 BP 决策默认读取这些稳定页面，或读取由这些稳定页面和强度输入编译出的 `runtime_bp_index`；不要读取中央覆盖层，不临场叠加历史补丁记录，不要把临时版本强势反写成稳定地图事实。

BP schema 字段必须有明确消费方。没有明确进入 `hard_gate`、`required_capabilities`、`map_bp_factors`、`candidate_eval`、breakpoint maintainer audit 或输出解释的字段，不应放入 Canonical Input。`combat_breakpoint_profile` 的明确消费方是 `scripts/audit_balance_breakpoints.py`，不是 runtime compiler。`summary_tags`、`high/medium/low` 这类粗粒度摘要不能作为 BP 判断信号；地图因素必须落到具体路线、位置、目标收益、失效条件和 slot 任务上。

BP 维护文件职责：

- `wiki/syntheses/条件化对位模型.md` 是长期维护 schema，定义 BP 推理对象和维护规则；不承载版本差分、补丁翻译、临时观察名单或批量 ingest 过程记录。
- `wiki/syntheses/BP-运行时索引编译架构.md` 定义 BP skill 如何把稳定事实层和用户输入的版本强度理解编译为 `runtime_bp_index`；它是方法论页面，不是手写候选表。
- 旧的手写条件化对位边索引和英雄地图特征适配索引已在 2026-07-02 删除；它们的长期信息必须回到英雄页、地图页、模式页或编译产物中。
- BP skill 的执行规则必须复制到 skill 自身 references；syntheses 只作为维护者讨论与 wiki 治理层，不能成为 skill 的渐进披露读取路径。
- 编译 / ingest 过程中的原始候选、审计和交接内容只能放在来源页、审计页、任务计划、日志或临时工作文件；完成 ingest 后，不应出现在 BP DSL 入口或长期手写运行时索引中。

### 3. Lint 维护与巡检

定期检查：

- 页面之间是否存在冲突或互相矛盾的说法
- 旧结论是否已被新资料覆盖
- 是否存在孤儿页、弱链接页
- 是否有高频出现但尚未独立建页的概念
- `wiki/index.md` 是否遗漏重要入口
- `wiki/sources/` 是否有对应 raw 链接、来源边界和 provenance
- `wiki/log.md` 是否记录了重要 ingest、query、lint、cleanup 和 skill 规则变更
- `AGENTS.md`、`skills/*/references/` 与 `wiki/syntheses/` 是否出现执行规则冲突
- `outputs/` 是否只保存临时产物，并保持 gitignore

## 编辑规则

- 不修改既有 `raw/` 原始内容；只允许新增 raw capture，或在明确 cleanup 任务中删除 / 归档已确认冗余的 raw。
- 不把 `wiki/sources/` 当作 `raw/` 的替代品；来源摘要不能代替原始抓取件。
- 保持 `wiki/` 为 Markdown 页面。
- 优先创建小而互相链接的页面，而不是超大单页。
- 当来源不一致时，保留不确定性，不强行统一。
- 新增、重命名或明显重构页面时，必须同步更新 `wiki/index.md`。
- ingest、lint、cleanup、skill 规则变更，以及明确声明为维护型 query 的写入操作，才追加到 `wiki/log.md`。
- 日常问答即使读取了 wiki，也不追加日志。

## 命名建议

- 来源页：`wiki/sources/<来源主题>.md`
- 概念页：`wiki/concepts/<机制或术语>.md`
- 英雄实体页：`wiki/entities/brawlers/<英雄>.md`
- 地图实体页：`wiki/entities/maps/<地图>.md`
- 其他实体页：`wiki/entities/<角色或组织>.md`
- 综合页：`wiki/syntheses/<专题>.md`

命名优先使用清晰、稳定、可搜索的中文标题；必要时可带英文或版本号。
