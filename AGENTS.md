# Brawl Stars Knowledge Base Rules

这个仓库是一套由 LLM 维护的 Markdown Wiki，用来持续积累、整理和更新《荒野乱斗》相关知识。

## 三层结构

- `raw/`：原始资料层，只读不改。放截图、网页摘录、活动公告、版本说明、攻略原稿、数据表等。
- `wiki/`：知识页面层。这里放整理后的页面、摘要、概念说明、角色页、机制页、专题页。
- `AGENTS.md`：规则层。定义未来 session 中 LLM 应该如何 ingest、query 和 lint。

## 目录约定

```text
raw/
  inbox/
  sources/
  assets/
wiki/
  index.md
  log.md
  sources/
  concepts/
  entities/
    brawlers/
    maps/
  syntheses/
```

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

### Brawl Stars ingest 的建议顺序

为了适合从 Fandom 站点逐步学习，建议按这个顺序扩展：

1. 先从总览和基础概念开始。
2. 再进入稀有度、货币、模式、战斗规则等共用机制。
3. 然后逐个 ingest 英雄、地图、活动、组织和版本页面。
4. 最后再做专题综述，例如 meta、资源循环、模式对比和版本演化。

### Brawl Stars 页面粒度

- 英雄页应尽量承载单个英雄的稳定事实和版本变动。
- 英雄页归档到 `wiki/entities/brawlers/`，用于长期追踪单个英雄；版本强度、临时 meta 和 BP 结论应写入版本 / meta 覆盖层或专题页。
- 模式页应描述胜利条件、地图/局内规则和适用英雄类型。
- 货币和稀有度页应归入概念，不要拆成实体页。
- 版本更新页适合先作为来源页，再视需要沉淀成专题页或版本实体页。

### 2. Query 基于 Wiki 回答问题

当用户提出问题时：

1. 先读 `wiki/index.md`。
2. 再读相关 wiki 页面，而不是直接从聊天记忆回答。
3. 基于现有页面综合回答，并明确引用使用到的 wiki 页面。
4. 如果回答具有长期价值，将其沉淀到 `wiki/` 中。
5. 将重要的持久化分析记录到 `wiki/log.md`。

BP 推演、Ban Pick 建模、英雄克制关系、阵容评价和 draft 顺位相关问题，必须优先读取 `wiki/syntheses/BP-推理DSL规范.md`，再读取 `wiki/syntheses/条件化对位模型.md`、`wiki/syntheses/Ban-Pick-问题拆分.md` 以及相关地图、模式、英雄和来源页。涉及英雄能力、候选评估、build、失败条件或对位边时，还必须读取 `wiki/syntheses/英雄BP建模覆盖审计.md`，不要把当前英雄实体页当作 BP-ready 输入。涉及地图适配、地图机制、地图特征或 `map_profile` 抽象时，还必须读取 `wiki/syntheses/地图特征建模Schema.md`；涉及地图因素如何进入 BP 决策、hard gate、slot 任务、候选假阳性过滤时，还必须读取 `wiki/syntheses/地图因素BP表达规范.md`。涉及当前 Ranked 地图池时，还必须读取 `wiki/syntheses/Ranked-Season-46-地图Map-Profile总览.md`。

执行全量英雄 BP 建模、补抓 Fandom/Power League Prodigy 英雄详情页、扩展英雄覆盖、或批量升级 `wiki/entities/brawlers/` 时，必须先读取 `wiki/syntheses/英雄BP建模升级任务计划.md`。该任务必须先建立或读取 105 行 roster manifest，再按 104 个 BP-active 英雄分批保留 raw；`Buzz Lightyear` 是临时下架英雄，按 `BP out-of-scope` 处理，不进入 BP 建模、PLP 缺口追踪、对位边或地图适配索引。禁止直接批量生成 BP-ready 字段。

地图知识必须分层治理：稳定地图结构写入 `wiki/entities/maps/` 下的单地图实体页；Ranked 赛季页面只作为地图池索引；版本强势英雄、新英雄和 meta 变化写入版本 / meta 覆盖层或英雄页的 map-fit 覆盖层，不要反写成稳定地图事实。

BP schema 字段必须有明确消费方。没有明确进入 `hard_gate`、`required_capabilities`、`map_bp_factors`、`candidate_eval` 或输出解释的字段，不应放入 Canonical Input。`summary_tags`、`high/medium/low` 这类粗粒度摘要不能作为 BP 判断信号；地图因素必须落到具体路线、位置、目标收益、失效条件和 slot 任务上。

### 3. Lint 维护与巡检

定期检查：

- 页面之间是否存在冲突或互相矛盾的说法
- 旧结论是否已被新资料覆盖
- 是否存在孤儿页、弱链接页
- 是否有高频出现但尚未独立建页的概念
- `wiki/index.md` 是否遗漏重要入口

## 编辑规则

- 不修改 `raw/` 中的原始资料。
- 不把 `wiki/sources/` 当作 `raw/` 的替代品；来源摘要不能代替原始抓取件。
- 保持 `wiki/` 为 Markdown 页面。
- 优先创建小而互相链接的页面，而不是超大单页。
- 当来源不一致时，保留不确定性，不强行统一。
- 新增、重命名或明显重构页面时，必须同步更新 `wiki/index.md`。
- ingest、重要 query、lint 都要追加到 `wiki/log.md`。

## 命名建议

- 来源页：`wiki/sources/<来源主题>.md`
- 概念页：`wiki/concepts/<机制或术语>.md`
- 英雄实体页：`wiki/entities/brawlers/<英雄>.md`
- 地图实体页：`wiki/entities/maps/<地图>.md`
- 其他实体页：`wiki/entities/<角色或组织>.md`
- 综合页：`wiki/syntheses/<专题>.md`

命名优先使用清晰、稳定、可搜索的中文标题；必要时可带英文或版本号。
