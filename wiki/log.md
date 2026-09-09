# Wiki Log

记录这套 wiki 的重要操作，便于回顾最近 ingest 了什么、形成了什么结论、做过哪些维护。

## [2026-04-06] bootstrap | 初始化 wiki

- 创建了 `raw/` 与 `wiki/` 的最小结构。
- 新增了 `AGENTS.md` 作为规则层。
- 新增了 `wiki/index.md` 与 `wiki/log.md` 作为导航与历史入口。

## [2026-04-06] synthesis | 新增 LLM Wiki 操作手册

- 新增 `wiki/syntheses/llm-wiki-操作手册.md`，总结初始化、ingest、query、lint、scale、剪枝与重构场景。
- 更新 `wiki/index.md`，加入操作手册入口。

## [2026-04-06] structure | 补充 Brawl Stars 分类约定

- 在 `AGENTS.md` 中补充 `heroes / modes / currencies / rarities` 的页面归类规则。
- 调整 `wiki/index.md`，把导航页改成更适合持续 ingest 的起步结构。

## [2026-04-06] source+synthesis | 建立 Fandom 学习路线

- 新增 `wiki/sources/Brawl-Stars-Wiki-站点地图.md`，记录 Brawl Stars Wiki 的一级结构与优先入口。
- 新增 `wiki/syntheses/Fandom-学习与摄取路线图.md`，定义双 agent 协作与分批 ingest 顺序。
- 更新 `wiki/index.md`，加入路线图与站点地图入口。

## [2026-04-06] ingest | 第一批 Gameplay 资源条目

- 读取 Fandom 条目 `Credits`、`Coins`、`Power Points`。
- 新增三篇来源摘要页，分别记录定义、来源方式、主要用途与系统关系。
- 新增三篇概念页，整理“解锁资源 / 通用强化货币 / 专用升级资源”的差异。
- 更新 `wiki/index.md`，加入第一批资源页入口。

## [2026-04-06] ingest | 第二小批 Gameplay 资源条目

- 读取 Fandom 条目 `Gems`、`Trophies`、`Bling`。
- 新增三篇来源摘要页，补充高级货币、进度指标与外观货币层。
- 新增三篇概念页，区分资源消耗体系与进度衡量体系。
- 更新 `wiki/index.md`，让基础资源层形成更完整的起步骨架。

## [2026-04-06] parallel ingest | 资源系统扩展与综述并行完成

- 并行新增 `Starr Drops`、`Brawl Pass`、`Daily Streak`、`Gears` 的来源摘要页与概念页。
- 新增 `wiki/syntheses/Brawl-Stars-资源系统综述.md`，将当前资源知识整理为“解锁 / 升级 / 高级货币 / 外观货币 / 进度指标”五层结构。
- 更新 `wiki/index.md`，加入新来源页、概念页与综述页入口。
- 修正综述页的链接形式，并记录下一批最值得补齐的关联系统。

## [2026-04-06] parallel ingest | 资源流向节点与进度入口补齐

- 并行新增 `Starr Road`、`Fame`、`Catalog`、`Quests`、`Mega Pig`、`Trophy Road` 的来源摘要页与概念页。
- 更新 `wiki/syntheses/Brawl-Stars-资源系统综述.md`，从资源分类图推进到初步资源流动图。
- 更新 `wiki/index.md`，加入本轮新来源页与概念页入口。
- 修正 `wiki/concepts/Starr Road.md` 中对 `Trophy Road` 的关联链接。

## [2026-04-06] parallel ingest | XP、排行与俱乐部生态补齐

- 并行新增 `XP`、`Daily Wins`、`Brawler Keys`、`Ranked`、`Club`、`Clubs` 的来源摘要页与概念页。
- 更新 `wiki/syntheses/Brawl-Stars-资源系统综述.md`，将 `XP` 提升为更明确的赛季进度资源节点，并补入排位与俱乐部生态。
- 更新 `wiki/index.md`，加入本轮新来源页与概念页入口。
- 记录 `Club` 与 `Clubs` 暂时并存，后续可在内容高度重叠时再剪枝。

## [2026-04-06] parallel ingest | 历史排位与历史俱乐部系统补齐

- 并行新增 `XP Doublers`、`Power League`、`Club League`、`Club Quests`、`Club Coins`、`Club Games` 的来源摘要页与概念页。
- 更新 `wiki/syntheses/Brawl-Stars-资源系统综述.md`，显式区分现行系统与历史系统，并将 `XP Doublers` 归入赛季推进加速层。
- 更新 `wiki/index.md`，加入本轮新来源页与概念页入口。
- 为后续补齐旧货币、旧商店与旧奖励容器建立了清晰的历史上下文。

## [2026-04-06] lint | 首次结构巡检

- 检查了概念页的互链密度、导航页负载、现行系统与历史系统的边界，以及潜在重复概念。
- 当前未发现明显冲突结论或失效链接。
- 识别出三类后续风险：`wiki/index.md` 导航过载、少数新概念页反向链接偏弱、`Club` / `Clubs` 后续可能出现边界重叠。

## [2026-04-06] refactor | 导航分组与弱链接修补

- 将 `wiki/index.md` 从长平铺列表重构为“现行资源与进度 / 竞技与社交 / 历史系统”分组导航。
- 为 `Brawler Keys`、`Catalog`、`XP Doublers` 等弱链接页补充来自上游概念页的入口。
- 保持 `Club` 与 `Clubs` 双页并存，暂不合并。

## [2026-04-06] parallel ingest | 切入核心玩法与首批英雄

- 新增 `Gem Grab`、`Brawl Ball`、`Knockout`、`Showdown` 的来源摘要页与概念页，开始从系统层转入玩法层。
- 新增 `Shelly`、`Colt`、`Bull`、`Nita` 的来源摘要页与实体页，开始让 `wiki/entities/` 承载可持续更新的英雄对象。
- 更新 `wiki/index.md`，加入玩法模式与英雄实体入口。

## [2026-04-06] ingest | 第二批英雄实体扩展

- 新增 `Jessie`、`Rosa`、`Rico`、`Penny` 的来源摘要页与实体页。
- 英雄层开始覆盖弹射、护盾推进、反弹射击、炮台封区等代表性玩法手感。
- 更新 `wiki/index.md`，让 `entities/` 从起始英雄扩展到更具战术差异的一批角色。

## [2026-04-06] ingest | 第三批英雄实体扩展

- 新增 `Brock`、`El Primo`、`Barley`、`Poco` 的来源摘要页与实体页。
- 英雄层进一步覆盖爆破拆墙、近战开团、投掷封路与团队治疗四种代表性玩法。
- 更新 `wiki/index.md`，继续扩展 `entities/` 的英雄谱系。

## [2026-04-06] parallel ingest | 五路并行扩展英雄主线

- 并行新增 `Dynamike`、`Tick`、`8-Bit`、`Darryl`、`Carl`、`Jacky`、`Piper`、`Pam`、`Frank`、`Bibi`、`Bea`、`Nani`、`Mortis`、`Gene`、`Max`、`Byron`、`Spike`、`Crow`、`Leon`、`Sandy` 的来源摘要页与实体页。
- `wiki/entities/` 从基础样本扩展为覆盖投掷、狙击、坦克、刺客、支援、传奇控场等多种玩法手感的英雄图谱。
- 更新 `wiki/index.md`，将英雄入口按玩法感受分组，避免实体层退化成长列表。

## [2026-04-06] synthesis | 英雄定位综述

- 新增 `wiki/syntheses/Brawl-Stars-英雄定位综述.md`，将已 ingest 的英雄按远程压线、前排开团、控场、刺客、支援与成长型分类。
- 更新 `wiki/index.md`，把英雄总图接入 `Start Here` 与 `Syntheses`。

## [2026-04-06] ingest | 英雄主线再扩容

- 新增 `Mr. P`、`Sprout`、`Squeak`、`Lou`、`Tara`、`Bo`、`Emz`、`Stu`、`Amber`、`Meg`、`Chester`、`Surge`、`Mandy`、`Maisie`、`Pearl`、`Angelo` 的来源摘要页与实体页。
- 英雄层继续覆盖召唤物、地形操控、延迟爆炸、冰冻控场、蓄力狙击、成长爆发与形态切换等差异化玩法。
- 更新 `wiki/index.md`，并继续细化英雄定位谱系。

## [2026-04-07] refactor | 回填 raw 层并补正 ingest 规则

- 在 `AGENTS.md` 中明确：网页来源必须优先落到 `raw/`，`wiki/sources/` 只负责来源摘要，不能代替原始抓取件。
- 新增 `raw/sources/fandom/README.md` 与 `raw/sources/fandom/_backfill-status.md`，建立 Fandom 网页回填规范和进度记录。
- 回填了首批代表性 raw capture 样板：站点主页、`Credits`、`Gem Grab`、`Shelly`、`Ranked`。
- 从本次补正开始，后续新一轮 ingest 应优先补 `raw/`，再更新 `wiki/`。

## [2026-04-07] refactor | 全量补齐历史来源的 raw backfill

- 基于现有 `wiki/sources/` 页面，为全部既有来源补齐了 `raw/sources/fandom/` 对应文件。
- 对首批关键页面保留 `manual raw capture` 样板，其余历史页面以 `provisional raw backfill` 形式回填，并明确标注来源于已有摘要页。
- 校准了 `raw/` 分桶目录，使英雄优先进入 `heroes/`，模式进入 `modes/`，资源与系统分别进入 `gameplay/` 与 `systems/`。
- 当前知识库已补上缺失的原始来源层，不再只有 `wiki/` 沉淀而缺失 `raw/` 证据层。

## [2026-04-07] ingest | 写入用户经验修正样板

- 新增一条来自当前维护者的 raw 笔记，记录 `Gene` 在 `Brawl Ball` 中不应被视为理想持球推进核心的实战判断。
- 基于这条笔记新增 `wiki/sources/User-Note-Gene-in-Brawl-Ball.md`，作为玩家经验型来源摘要页。
- 更新 `wiki/entities/Gene.md` 与 `wiki/concepts/Brawl Ball.md`，把这条经验写成“模式适配修正”而不是无来源断言。

## [2026-04-07] ingest | 写入足球模式评价框架

- 新增一条来自当前维护者的 raw 笔记，记录 `Brawl Ball` 更看重坦度、DPS、机动性至少一项突出，而非只看单点打断。
- 基于这条笔记新增 `wiki/sources/User-Note-Brawl-Ball-Evaluation-Framework.md`，作为玩家经验型模式判断来源。
- 更新 `wiki/concepts/Brawl Ball.md` 与 `wiki/syntheses/Brawl-Stars-英雄定位综述.md`，将这条经验写成模式评价框架。

## [2026-04-07] ingest | 写入足球模式的得分手框架

- 新增一条来自当前维护者的 raw 笔记，记录足球模式中“得分手”作为独立高权重角色的判断框架。
- 基于这条笔记新增 `wiki/sources/User-Note-Brawl-Ball-Scorer-Framework.md`，沉淀玩家验证过的强袭得分思路。
- 更新 `wiki/concepts/Brawl Ball.md` 与 `wiki/syntheses/Brawl-Stars-英雄定位综述.md`，把“得分手”写成足球模式的独立评价维度。

## [2026-04-07] ingest | 写入宝石模式评价框架

- 新增一条来自当前维护者的 raw 笔记，记录 `Gem Grab` 更看重生存能力、翻盘能力、机动性与前期中线作用的综合权重。
- 基于这条笔记新增 `wiki/sources/User-Note-Gem-Grab-Evaluation-Framework.md`，沉淀先手位与反例位的判断标准。
- 更新 `wiki/concepts/Gem Grab.md` 与 `wiki/syntheses/Brawl-Stars-英雄定位综述.md`，把这条经验写成宝石模式的评价框架。

## [2026-06-29] pilot ingest | Power League Prodigy 抽检与 BP 拆解

- 新增 `raw/sources/pl-prodigy/site-and-sample-2026-06-29.md`，记录 PLP sitemap、公开产品页、9 篇 blog 列表与 8 个角色页抽检字段。
- 新增 `raw/inbox/2026-06-29-user-note-ban-pick-high-level-assumption.md`，沉淀“正式 BP 应按高水平对局预设，不把低分局噪音作为核心维度”的本地原则。
- 新增 `wiki/sources/Power-League-Prodigy-站点与抽检.md` 与 `wiki/sources/User-Note-Ban-Pick-High-Level-Assumption.md`，把外部站点和用户经验接入来源层。
- 新增 `wiki/syntheses/Ban-Pick-问题拆分.md`，将 BP 拆成局面状态、地图模式胜利条件、英雄能力向量、build 条件能力、ban 路线拆解、pick 计划建立与完整阵容评估。
- 更新 `wiki/index.md` 与 `wiki/syntheses/Brawl-Stars-英雄定位综述.md`，为后续分批 ingest PLP blog 和角色攻略建立入口。
- 补充读取 `https://powerleagueprodigy.com/blog/feed.xml`，确认当前公开 RSS feed 覆盖 9 篇 blog，并把标题、日期、分类和 feed 摘要写入 raw 抽检页。
- 本次按用户要求只做抽检和 pilot ingest，没有全量抓取 100+ 个角色页。

## [2026-06-29] lint | 清理 wiki 边界外页面

- 复核 `wiki/syntheses/llm-wiki-操作手册.md`，确认其内容是知识库维护说明，不是《荒野乱斗》资料、概念、实体或跨来源专题结论。
- 删除该页面，并从 `wiki/index.md` 的 `Start Here`、`Syntheses` 与 `How To Use` 中移除入口。
- 后续维护规范继续以 `AGENTS.md` 为准，`wiki/syntheses/` 只保留 Brawl Stars 相关专题综合页。

## [2026-06-29] lint+ingest | 完成本地已有资料的内容层接入

- 删除 `wiki/syntheses/Fandom-学习与摄取路线图.md`，确认其属于摄取流程规划，不属于《荒野乱斗》专题知识。
- 新增 `wiki/syntheses/Brawl-Stars-模式机制综述.md`，把 `Gem Grab`、`Brawl Ball`、`Knockout`、`Showdown`、`Mega Pig` 与相关用户经验整合成模式机制对比。
- 重写 `wiki/index.md`，让 111 个来源页、32 个概念页、72 个实体页与 4 个综述页全部可从导航进入。
- 清理 `wiki/syntheses/` 与相关来源摘要中的流程性措辞，把“以后怎么 ingest”的表述改成当前知识边界、来源分层与可靠性说明。
- 修正 6 个 `wiki/sources/` 页面里的上游 `raw/` 追溯链接，使其从来源页正确指向仓库根目录下的原始资料。
- 本次未修改 `raw/`，完整接入范围限定为当前本地已经落盘的原始资料与来源摘要。

## [2026-06-29] synthesis | 条件化对位与 BP 推理中间层

- 新增 `raw/inbox/2026-06-29-user-note-bp-reasoning-intermediate-layer.md`，记录当前维护者关于 BP 知识库中间层的建模需求。
- 新增 `wiki/sources/User-Note-BP-Reasoning-Intermediate-Layer.md`，将这轮用户经验作为可追溯来源接入。
- 新增 `wiki/syntheses/条件化对位模型.md`，定义 `map_profile`、`mode_objective_profile`、`brawler_profile`、`build_profile`、`conditional_matchup`、`draft_state` 与 `draft_eval`。
- 更新 `wiki/syntheses/Ban-Pick-问题拆分.md`，明确静态 counter 表必须先转译为条件化对位边，再用于 BP 判断。
- 更新 `wiki/index.md`，把条件化对位模型接入 `Start Here`、`Sources`、`Syntheses` 与 BP 查询路径。

## [2026-06-29] correction | BP 顺位视角修正

- 新增 `raw/inbox/2026-06-29-user-note-bp-slot-perspective.md`，记录当前维护者对 `1-6` 号位信息状态的修正。
- 新增 `wiki/sources/User-Note-BP-Slot-Perspective.md`，明确 `4-5` 位已知的是己方 `1` 位和敌方 `2-3` 位，而不是“敌方 1-3 位”。
- 更新 `wiki/syntheses/条件化对位模型.md`，新增 `pick_slot_state`，把全局 slot 编号、队伍视角、已知己方 picks、已知敌方 picks 与剩余反制位拆开记录。
- 更新 `wiki/syntheses/Ban-Pick-问题拆分.md` 与 `wiki/index.md`，把 `pick_slot_state` 接入 BP 推理中间层。

## [2026-06-29] synthesis | BP 推理 DSL 固化

- 新增 `raw/inbox/2026-06-29-user-note-bp-dsl-requirement.md`，记录当前维护者希望把本轮 BP 建模固化为可复用 DSL / 执行文档的需求。
- 新增 `wiki/sources/User-Note-BP-DSL-Requirement.md`，将这条需求作为用户经验来源接入。
- 新增 `wiki/syntheses/BP-推理DSL规范.md`，定义 BP 推理的执行合约、Canonical Input、Hard Gates、Slot Policy、Decision Pipeline、Candidate Eval 与 Output Format。
- 更新 `wiki/syntheses/条件化对位模型.md` 和 `wiki/syntheses/Ban-Pick-问题拆分.md`，把对象模型与问题拆分连接到新的 DSL 执行规范。
- 更新 `wiki/index.md` 和 `AGENTS.md`，把 BP 推理 DSL 接入 `Start Here`、`Sources`、`Syntheses`、BP 查询路径与未来 session 的查询规则。

## [2026-06-29] synthesis | 地图特征建模 Schema

- 新增 `raw/inbox/2026-06-29-user-note-map-profile-schema.md`，记录当前维护者对 `map_profile` 粗分档不足的修正意见，并以 `Safe Zone` 为例说明河道、远程金库角度、中路拥挤和基地墙角等具体地形价值。
- 新增 `wiki/sources/User-Note-Map-Profile-Schema.md`，将这条地图建模经验作为用户经验来源接入。
- 新增 `wiki/syntheses/地图特征建模Schema.md`，定义 `map_profile`、`map_feature`、`objective_access`、`lane_dynamics` 和 `map_fit` 输出结构。
- 更新 `wiki/syntheses/BP-推理DSL规范.md`、`wiki/syntheses/条件化对位模型.md` 与 `wiki/syntheses/Ban-Pick-问题拆分.md`，要求地图适配必须说明具体路线、目标角度、站位收益、假阳性能力和 BP 用途。
- 更新 `wiki/index.md` 和 `AGENTS.md`，把地图特征建模 Schema 接入来源、专题入口、Start Here 与未来 BP 地图相关查询路径。

## [2026-06-29] source assessment | Fandom Ranked 地图页

- 新增 `raw/sources/fandom/maps/ranked-map-source-assessment-2026-06-29.md`，记录对 Fandom `Ranked` 页面和 8 个地图页的抽检结果。
- 新增 `wiki/sources/Fandom-Ranked-Map-Source-Assessment.md`，评估 Fandom 地图页对 `map_feature` 级建模的可用性、边界和当前 Ranked Season 46 地图池快照。
- 更新 `wiki/syntheses/地图特征建模Schema.md`，补充 Fandom 地图页的字段转换方式：`Layout` 进入 topology / objective_access / lane_dynamics，`Tips` 进入 tactical_features / map_rules / example_brawlers。
- 更新 `wiki/index.md`，把 Fandom Ranked 地图页建模价值评估接入外部竞技与 BP 来源。

## [2026-06-29] ingest | Ranked Season 46 全量地图 map_profile

- 用浏览器逐页读取 Fandom 当前 Ranked Season 46 的 26 张 active maps，覆盖 `Gem Grab`、`Heist`、`Bounty`、`Brawl Ball`、`Hot Zone` 与 `Knockout`。
- 清理此前脚本抓取失败生成的 403 JSON/MD 抓取件，改写为有效 raw capture：`raw/sources/fandom/maps/ranked-season-46-map-extracts-2026-06-29.md`。
- 新增 `wiki/sources/Fandom-Ranked-Season-46-Map-Pages.md`，记录全量地图页的来源范围、使用边界和结论去向。
- 新增 `wiki/syntheses/Ranked-Season-46-地图Map-Profile总览.md`，为 26 张排位地图沉淀 first-pass `map_profile` 结论，包括 `map_features`、`bp_value`、`hero_model_delta` 和 `false_positive`。
- 更新 `wiki/syntheses/地图特征建模Schema.md`、`wiki/index.md` 与 `AGENTS.md`，把全量地图 profile 接入地图建模、`Start Here`、BP 查询入口和未来 session 的 Ranked 地图查询规则。

## [2026-06-29] refactor | 地图实体分层治理

- 新增 `raw/inbox/2026-06-29-user-note-map-layered-governance.md` 与 `wiki/sources/User-Note-Map-Layered-Governance.md`，记录当前维护者关于地图稳定实体、赛季索引、版本 meta 和英雄 map-fit 分层治理的修正意见。
- 新增 `wiki/syntheses/地图知识分层治理.md`，定义地图知识的四层结构与更新规则。
- 新增 `wiki/entities/maps/` 下 26 张单地图实体页，把 Season 46 总览中的 first-pass `map_profile` 拆成稳定地图本体知识。
- 重写 `wiki/syntheses/Ranked-Season-46-地图Map-Profile总览.md`，将其降级为当前赛季地图池索引，不再承载地图本体结论。
- 更新 `wiki/sources/Fandom-Ranked-Season-46-Map-Pages.md`、`wiki/syntheses/地图特征建模Schema.md`、`wiki/index.md` 与 `AGENTS.md`，接入地图实体页与分层治理规则。

## [2026-06-29] raw compression | Fandom 地图旧抓取压缩

- 按当前维护者要求，将已经整理进入来源摘要、赛季索引和 26 张地图实体页的旧 Fandom 地图 raw 摘录压缩为 compact manifest。
- 压缩 `raw/sources/fandom/maps/ranked-season-46-map-extracts-2026-06-29.md`，保留 26 张地图 URL、覆盖范围、整理去向和重抓边界。
- 压缩 `raw/sources/fandom/maps/ranked-map-source-assessment-2026-06-29.md`，保留抽检 URL、评估去向和重抓边界。
- 更新 `wiki/sources/Fandom-Ranked-Season-46-Map-Pages.md` 与 `wiki/sources/Fandom-Ranked-Map-Source-Assessment.md`，标注 raw 已压缩，详细内容位于 wiki 层。

## [2026-06-29] raw compression | PLP 抽检旧抓取压缩

- 将 `raw/sources/pl-prodigy/site-and-sample-2026-06-29.md` 压缩为 compact manifest，仅保留站点、blog、抽检角色 URL 与整理去向。
- 更新 `wiki/sources/Power-League-Prodigy-站点与抽检.md`，把原 raw 中的公开产品入口、9 篇 blog 清单和 8 个角色抽检字段补入 wiki 层。
- 保留 PLP 作为第三方竞技攻略信号的边界：build、mode fit 与 counter 字段必须先转译为条件化对位候选，再进入 BP 推理。

## [2026-06-29] reingest | Ranked Season 46 26 张地图 BP-ready v2

- 将 `wiki/entities/maps/` 下 26 张 Ranked Season 46 地图实体页从 `first_pass_from_fandom_text` 升级为 `bp_map_profile_v2`。
- 每张地图补齐 Fandom URL、`summary_tags`、`topology`、`objective_access`、`tactical_features`、`lane_dynamics`、`map_rules`、`false_positive` 与 BP 用法。
- 重写重点是把地图信息转成“能力 -> 路线 / 位置 -> 目标收益 -> 失效条件 -> BP 用途”，用于后续 BP DSL 直接读取。
- 更新 `wiki/sources/Fandom-Ranked-Season-46-Map-Pages.md`，标注 26 张地图已完成二次 ingest。

## [2026-06-29] synthesis | 地图因素 BP 表达升级

- 新增 `raw/inbox/2026-06-29-user-note-map-factor-bp-expression.md` 与 `wiki/sources/User-Note-Map-Factor-BP-Expression.md`，记录当前维护者要求把 26 张地图战术关键点进一步升级为 BP 决策表达。
- 新增 `wiki/syntheses/地图因素BP表达规范.md`，定义 `map_feature -> map_bp_factor` 的转换、五层地图决策模型、模式化地图职责、地形状态、地图 hard gate、slot 地图任务、候选地图适配评估和假阳性库。
- 更新 `wiki/syntheses/地图特征建模Schema.md`，把地图结构化 schema 与 `map_bp_factor` 决策信号分层。
- 更新 `wiki/syntheses/BP-推理DSL规范.md`，在 Canonical Input、Decision Pipeline、Candidate Eval 和 Output Format 中加入 `map_bp_factors` / `map_factor_summary`。
- 更新 `wiki/syntheses/条件化对位模型.md`、`wiki/index.md` 与 `AGENTS.md`，把地图因素 BP 表达规范接入未来 BP 查询路径。

## [2026-06-29] refactor | 英雄实体目录分层

- 新增 `wiki/entities/brawlers/`，将原 `wiki/entities/` 根目录下的英雄实体页迁移到该子目录。
- 更新 `wiki/index.md`、英雄页互链和 `wiki/syntheses/Brawl-Stars-英雄定位综述.md` 中的英雄实体 wikilink，统一指向 `entities/brawlers/<英雄>`。
- 更新 `AGENTS.md`，明确英雄实体页归档到 `wiki/entities/brawlers/`，地图实体页归档到 `wiki/entities/maps/`。

## [2026-06-29] refactor | BP schema 奥卡姆剃刀降噪

- 新增 `raw/inbox/2026-06-29-user-note-bp-schema-occam.md` 与 `wiki/sources/User-Note-BP-Schema-Occam.md`，沉淀“schema 字段必须有明确消费方，否则不进入 Canonical Input”的维护原则。
- 从 `wiki/syntheses/地图特征建模Schema.md`、`wiki/syntheses/BP-推理DSL规范.md` 和 `wiki/syntheses/条件化对位模型.md` 中移除 `summary_tags` 作为 BP 可消费字段。
- 将 `map_bp_factors.urgency` 从 `hard_gate | high | medium | low` 改为 `hard_gate | core_duty | must_answer_route | plan_protection | slot_trap | conditional_opportunity | low_relevance`。
- 批量移除 26 张 `wiki/entities/maps/` 地图实体页中的 `summary_tags` 块，避免粗粒度摘要干扰后续地图 BP 推理。
- 更新 `wiki/sources/Fandom-Ranked-Season-46-Map-Pages.md`、`wiki/index.md` 与 `AGENTS.md`，明确粗标签不能作为 BP 判断信号。

## [2026-06-29] audit | 英雄页 BP 建模覆盖审计

- 新增 `wiki/syntheses/英雄BP建模覆盖审计.md`，审计 `wiki/entities/brawlers/` 下 72 个英雄页是否足够支撑 BP 推理。
- 结论：当前英雄实体页主要是人类可读机制摘要，不是 BP-ready 机器输入；它们缺少结构化 `brawler_profile`、`build_profile`、`conditional_matchup`、`map_feature_hooks`、`failure_modes` 和 `slot_profile`。
- 确认本地 72 个英雄均有 Fandom source 摘要和 raw 文件；其中 `Shelly` 是 manual raw capture，其余多数是从 source 摘要回填的 provisional raw backfill。
- 更新 `wiki/index.md` 与 `AGENTS.md`，要求涉及英雄能力、候选评估、build、失败条件或对位边时读取该审计页，不把当前英雄实体页直接当作 BP-ready 输入。

## [2026-06-29] plan | 104 英雄 BP 建模升级任务计划

- 新增 `raw/inbox/2026-06-29-user-note-hero-bp-ingest-plan.md` 与 `wiki/sources/User-Note-Hero-BP-Ingest-Plan.md`，记录维护者要求：本会话只列计划不执行；后续按 104 位 BP-active 英雄完整 scope 处理；Fandom 与 PLP 详情页都应优先保留 raw。
- 新增 `wiki/syntheses/英雄BP建模升级任务计划.md`，定义交接目标、raw/source/entity/synthesis 分层、104 行 roster manifest、BP-ready 英雄页目标结构、Fandom/PLP 对齐标准、地图/模式/顺位中间层映射、阶段性执行批次和验收门槛。
- 更新 `wiki/syntheses/英雄BP建模覆盖审计.md`、`wiki/index.md` 与 `AGENTS.md`，把任务计划接入后续英雄 BP ingest 的必读路径。
- 本次未抓取 Fandom 或 PLP 页面，未批量修改英雄实体页。

## [2026-06-29] ingest | 英雄 BP 建模 Phase 0-3 启动

- 完成 Phase 0 roster manifest：新增 `raw/sources/roster/brawlers-roster-2026-06-29.md` 与 `wiki/sources/Brawler-Roster-2026-06-29.md`。
- Fandom `Category:Brawlers` 与 PLP sitemap 均按 104 个 BP-active 英雄处理；本地 72 个英雄实体页之外缺失 32 个。
- 完成 Phase 1 Batch A raw capture：为 `Brock`、`Gene`、`Otis`、`Belle`、`Colt`、`Angelo`、`Shade`、`Rico`、`Mico`、`Max`、`Stu` 新增 dated Fandom raw 与 PLP raw。
- 完成 Phase 2 Batch A source 摘要：更新上述 11 个 `wiki/sources/Fandom-*` 为 `direct_raw_capture`，新增 11 个 `wiki/sources/PLP-*` 来源页。
- 开始 Phase 3 BP 建模：为 `wiki/entities/brawlers/Brock.md`、`wiki/entities/brawlers/Gene.md`、`wiki/entities/brawlers/Otis.md` 新增 `bp_brawler_profile` 草案，状态均为 `profile_status: draft`。
- 新增 `wiki/syntheses/英雄BP建模执行状态.md`，记录 Phase 0-3 当前进度、Batch A 完成项和下一步建议。
- 更新 `wiki/index.md`，接入 roster source、PLP Batch A 来源页、英雄 BP 建模执行状态页，并补齐 Syntheses 中的英雄审计/计划入口。

## [2026-06-29] scope correction | 统一 104 个 BP-active 英雄建模范围

- 更新 roster manifest 与当时的 source 摘要，按 104 个 BP-active 英雄统一建模范围。
- 更新 `wiki/syntheses/英雄BP建模升级任务计划.md`、`wiki/syntheses/英雄BP建模覆盖审计.md` 与 `wiki/syntheses/英雄BP建模执行状态.md`，统一 104 个 BP-active 英雄的口径。
- 更新 `AGENTS.md` 与 `wiki/index.md`，明确未来全量英雄 BP 建模只追踪 BP-active 英雄的 PLP 缺口、对位边或地图适配。

## [2026-06-30] ingest | 104 个 BP-active 英雄 Fandom/PLP 全量抓取与 draft BP 建模

- 新增 `skills/brawl-stars-bp-knowledge-maintenance/scripts/capture_brawler_sources.py`、`skills/brawl-stars-bp-knowledge-maintenance/scripts/ingest_brawler_sources.py`、`skills/brawl-stars-bp-knowledge-maintenance/scripts/ingest_brawler_bp_profiles.py`，用于可复跑地从 roster manifest 抓取 raw、生成 source 摘要和初始化英雄 BP 草案。
- 补抓 104 个 BP-active 英雄的 Fandom corrected direct raw 与 PLP direct raw。
- 修正 Fandom 抓取漂移：首轮抓取发现单行 infobox 解析污染，后续用 corrected raw 覆盖；`Chester` / `Kaze` 专属 infobox 另做定点修正。
- 生成/更新 104 个 `wiki/sources/Fandom-*` 与 104 个 `wiki/sources/PLP-*` source 摘要，统一标注来源边界：Fandom 只作为稳定机制事实，PLP 只作为 build/mode/matchup 竞技信号。
- 新建 32 个缺失 BP-active 英雄实体页，给 69 个既有英雄页追加 `profile_status: draft_from_raw_signals`；保留 `Brock`、`Gene`、`Otis` 已有人工 `draft` 草案。当前 104 个 BP-active 英雄均有 `bp_brawler_profile`，但没有任何英雄标记为 `bp_ready`。
- 新增 BP 条件化对位边索引（已删除旧手写索引） 与 BP 英雄地图特征适配索引（已删除旧手写索引），作为 seed-only 全局索引；它们不是最终 counter 表或地图适配结论。
- 更新 `wiki/syntheses/英雄BP建模执行状态.md` 与 `wiki/index.md`，记录当前验收快照、剩余质量门槛和全量导航。

## [2026-06-30] review | 英雄 BP 质量门槛与第一批 reviewed

- 新增 `wiki/syntheses/英雄BP建模质量门槛.md`，明确 `draft_from_raw_signals`、`reviewed`、`bp_ready` 的升级条件；`bp_ready` 必须有 reviewed 条件化对位边与 Ranked 地图 hook，不允许批量直升。
- 新增 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py` 与 `wiki/syntheses/英雄BP建模质量审计.md`，用于审计 104 个英雄页的明显占位符、来源追溯、地图 hook、失败条件和 slot notes。
- 复核 `Brock`、`Gene`、`Otis` 三个已有人工草案，将其 `profile_status` 从 `draft` 升级为 `reviewed`，并把 Fandom raw 日期同步到 corrected `2026-06-30`。
- 当前质量审计结果：104 个英雄均有 `bp_brawler_profile`；`reviewed` 3 个，`draft_from_raw_signals` 101 个，`bp_ready` 0 个。
- 更新 `wiki/syntheses/英雄BP建模执行状态.md` 与 `wiki/index.md`，把质量门槛、质量审计和第一批 reviewed 状态接入导航与交接页。

## [2026-06-30] review | Batch A 英雄升级到 bp_ready

- 复核 `Belle`、`Colt`、`Angelo`、`Rico` 四个 Batch A 英雄页，删除自动草案占位语句，补全能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；它们已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：新增 `reviewed_from_brawler_profiles` 区，记录 12 组 reviewed 条件化对位边。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：新增 `reviewed_from_brawler_profiles` 区，记录 12 条 reviewed Ranked 地图 hook。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 4 个、`reviewed` 3 个、`draft_from_raw_signals` 97 个。

## [2026-06-30] review | Batch A 机动组升级到 bp_ready

- 复核 `Max`、`Stu`、`Mico`、`Shade` 四个 Batch A 机动组英雄页，重点把团队速度、冲刺链、跳墙/穿墙、过水/越障等能力转成具体地图职责、目标收益和失效条件。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 12 增至 24。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 12 增至 24。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 8 个、`reviewed` 3 个、`draft_from_raw_signals` 93 个。

## [2026-06-30] review | Ash / Nita / Sandy 升级到 bp_ready

- 复核 `Ash`、`Nita`、`Sandy` 三个英雄页，将 Rage 前压、Bruce 召唤物、Sandstorm 团队隐身等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 24 增至 33。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 24 增至 33。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 11 个、`reviewed` 3 个、`draft_from_raw_signals` 90 个。

## [2026-06-30] review | Draco / Gigi / Poco 升级到 bp_ready

- 复核 `Draco`、`Gigi`、`Poco` 三个英雄页，将变身驻点、弹道充能传送、团队治疗净化等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 33 增至 42。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 33 增至 42。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 14 个、`reviewed` 3 个、`draft_from_raw_signals` 87 个。

## [2026-06-30] review | Sam / Bibi / Buster 升级到 bp_ready

- 复核 `Sam`、`Bibi`、`Buster` 三个英雄页，将拳套回收/拉拽、Home Run 击退/弹墙泡泡、屏障反射/队伍护送等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 42 增至 51。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 42 增至 51。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 17 个、`reviewed` 3 个、`draft_from_raw_signals` 84 个。

## [2026-06-30] review | Charlie / Chuck / Clancy 升级到 bp_ready

- 复核 `Charlie`、`Chuck`、`Clancy` 三个英雄页，将 Cocoon 单体移除与蜘蛛视野、Post 路线与 Heist 打库循环、token 阶段成长与 Stage 3 区域接管等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 51 增至 60。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 51 增至 60。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 20 个、`reviewed` 3 个、`draft_from_raw_signals` 81 个。

## [2026-06-30] review | Cordelius / Crow / Darryl 升级到 bp_ready

- 复核 `Cordelius`、`Crow`、`Darryl` 三个英雄页，将 Shadow Realm 隔离与沉默、毒伤反治疗/探草/残局跳杀、滚桶路线/击退/近身爆发等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 3 组 reviewed 条件化对位边和至少 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 60 增至 72。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 60 增至 71。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 23 个、`reviewed` 3 个、`draft_from_raw_signals` 78 个。

## [2026-06-30] review | Doug / Emz / Gus 升级到 bp_ready

- 复核 `Doug`、`Emz`、`Gus` 三个英雄页，将复活支援、喷雾控场/反突进、远程护盾支援等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 72 增至 84。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 71 增至 80。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 26 个、`reviewed` 3 个、`draft_from_raw_signals` 75 个。

## [2026-06-30] review | Jae-yong / Lily / Mandy / Meg 升级到 bp_ready

- 复核 `Jae-yong`、`Lily`、`Mandy`、`Meg` 四个英雄页，将团队加速/治疗支援、Vanish 突袭、Focus 超长线、Mecha 目标区身体等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 84 增至 100。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 80 增至 96。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 30 个、`reviewed` 3 个、`draft_from_raw_signals` 71 个。

## [2026-06-30] review | Melodie / Mina / Mortis / Rosa 升级到 bp_ready

- 复核 `Melodie`、`Mina`、`Mortis`、`Rosa` 四个英雄页，将音符叠层三段冲刺、三段连段与 Windmill、dash 收割、Grow Light 草丛前排等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 100 增至 116。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 96 增至 112。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 34 个、`reviewed` 3 个、`draft_from_raw_signals` 67 个。

## [2026-06-30] review | 8-Bit / Bo / Bolt / Bonnie 升级到 bp_ready

- 复核 `8-Bit`、`Bo`、`Bolt`、`Bonnie` 四个英雄页，将 Booster 阵地增伤、地雷/视野控口、动量接触路线、Clyde/Bonnie 双形态跳入爆发等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 116 增至 132。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 112 增至 128，hook seed 条目数从 201 增至 207。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 38 个、`reviewed` 3 个、`draft_from_raw_signals` 63 个，并完成本批占位符扫描。

## [2026-06-30] review | Buzz / Carl / Colette / Finx 升级到 bp_ready

- 复核 `Buzz`、`Carl`、`Colette`、`Finx` 四个英雄页，将常驻 Buzz 的抓钩眩晕、Carl 的回旋镐/墙边循环、Colette 的百分比伤害与 special target 伤害、Finx 的 Time Warp 投射物速度控制等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 132 增至 148。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 128 增至 144，hook seed 条目数从 207 增至 217。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 42 个、`reviewed` 3 个、`draft_from_raw_signals` 59 个，并完成本批占位符扫描。

## [2026-06-30] review | Gale / Hank / Janet / Jessie 升级到 bp_ready

- 复核 `Gale`、`Hank`、`Janet`、`Jessie` 四个英雄页，将推离/减速/Twister、蓄力水泡与近身鱼雷、空中携宝/草区 speaker、Scrappy 炮台与弹射等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 148 增至 164。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 144 增至 160，hook seed 条目数从 217 增至 226。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 46 个、`reviewed` 3 个、`draft_from_raw_signals` 55 个，并完成本批占位符扫描。

## [2026-06-30] review | Kaze / Kenji / Lola / Lou 升级到 bp_ready

- 复核 `Kaze`、`Kenji`、`Lola`、`Lou` 四个英雄页，将 Kaze 双形态风暴与标记、Kenji dash/slash 吸血与 Super 免疫、Lola Ego 分身交叉火力、Lou Frost / Hot Zone 冰冻控场等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 164 增至 180。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 160 增至 176，hook seed 条目数从 226 增至 236。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 50 个、`reviewed` 3 个、`draft_from_raw_signals` 51 个，并完成本批占位符扫描。

## [2026-06-30] review | Lumi / Maisie / Mr. P / Ollie 升级到 bp_ready

- 复核 `Lumi`、`Maisie`、`Mr. P`、`Ollie` 四个英雄页，将 Lumi 双锤召回/root、Maisie Shockwave 反突进、Mr. P Porter 弹药税、Ollie Hypnotize 控制坦克等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 180 增至 196。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 176 增至 192，hook seed 条目数从 236 增至 246。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 54 个、`reviewed` 3 个、`draft_from_raw_signals` 47 个，并完成本批占位符扫描。

## [2026-06-30] review | Pam / Pearl / Penny / Shelly 升级到 bp_ready

- 复核 `Pam`、`Pearl`、`Penny`、`Shelly` 四个英雄页，将治疗炮台和 Scrapsucker 弹药剥夺、Heat 条成长输出、Old Lobber 炮台控图、近身霰弹反坦/破门等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 196 增至 212。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 192 增至 208，hook seed 条目数从 246 增至 254。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 58 个、`reviewed` 3 个、`draft_from_raw_signals` 43 个，并完成本批占位符扫描。

## [2026-06-30] review | Squeak / Starr Nova / Willow / Ziggy 升级到 bp_ready

- 复核 `Squeak`、`Starr Nova`、`Willow`、`Ziggy` 四个英雄页，将延迟粘弹与 Residue、Starr Nova Super 剑形态与 Floaty Time、Willow Hex 心控位移、Ziggy 延迟落雷与移动 storm 等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 212 增至 228。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 208 增至 224，hook seed 条目数从 254 增至 264。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 62 个、`reviewed` 3 个、`draft_from_raw_signals` 39 个，并完成本批占位符扫描。

## [2026-06-30] review | Alli / Amber / Barley / Bea 升级到 bp_ready

- 复核 `Alli`、`Amber`、`Barley`、`Bea` 四个英雄页，将草/水跳跃追猎、燃油火墙控区、墙后投掷 puddle、Supercharged 长线 slow 等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 228 增至 244。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 224 增至 240，hook seed 条目数从 264 增至 271。
- 重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 66 个、`reviewed` 3 个、`draft_from_raw_signals` 35 个，并完成本批占位符扫描。

## [2026-06-30] audit | 英雄 BP 建模当前进度检查

- 复跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py` 并抽样检查 `bp_ready`、`reviewed`、`draft_from_raw_signals` 三类英雄页，确认当前质量审计结果仍为 `bp_ready` 66 个、`reviewed` 3 个、`draft_from_raw_signals` 35 个。
- 新增 英雄 BP 建模进度审计 2026-06-30（已归并），记录抓取、来源摘要、实体页、BP profile、条件化对位边索引和地图 hook 索引的当前进度。
- 判断当前主要缺口已从抓取转为质量复核：剩余 35 个 draft 英雄需要清理占位符、补具体地图路线/目标收益/失效条件、补 source traceability 和失败条件。
- 更新 [[index|Wiki Index]]，加入本次进度审计入口。

## [2026-06-30] review | Brock / Gene / Otis 升级到 bp_ready

- 复核 `Brock`、`Gene`、`Otis` 三个 `reviewed` 英雄页，将 Brock 的远程打库/选择性开墙/破门窗口、Gene 的拉人抓单/宝石位倒计时打断、Otis 的沉默反进场和草口/金库入口防守补成可消费的地图 hook 与条件化对位边。
- 将上述三个英雄从 `profile_status: reviewed` 升级为 `profile_status: bp_ready`；当前 `reviewed` 中间态归零。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 244 增至 256。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 240 增至 249，hook seed 条目数从 271 增至 273。
- 更新 英雄 BP 建模执行状态（已归并） 与 英雄 BP 建模进度审计 2026-06-30（已归并）；下一步进入 35 个 `draft_from_raw_signals` 英雄的分批质量复核。

## [2026-06-30] review | Byron / Nani / Piper / Spike 升级到 bp_ready

- 复核 `Byron`、`Nani`、`Piper`、`Spike` 四个自动草稿英雄页，将 Byron 的长线治疗/反坦 poke、Nani 的远距爆发与 Peep 开墙、Piper 的极长线击杀窗口、Spike 的控区减速与反坦能力转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和至少 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 256 增至 272。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 249 增至 262，hook seed 条目数从 273 增至 276。
- 更新 英雄 BP 建模执行状态（已归并） 与 英雄 BP 建模进度审计 2026-06-30（已归并）；重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 73 个、`reviewed` 0 个、`draft_from_raw_signals` 31 个。

## [2026-06-30] review | Sprout / Surge / Tara / Ruffs 升级到 bp_ready

- 复核 `Sprout`、`Surge`、`Tara`、`Ruffs` 四个自动草稿英雄页，修正 Sprout 被误抽成泛水/机动、Surge 被误抽成投掷、Tara 和 Ruffs 被泛化成粗长线/开墙标签的问题。
- 将 Sprout 的投掷口袋与 Hedge 封路、Surge 的阶段成长与反近身、Tara 的 Gravity 聚怪/探草/召唤物、Ruffs 的弹墙/补给包/沙包/Air Superiority 开墙转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和至少 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 272 增至 288。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 262 增至 276，hook seed 条目数从 276 增至 281。
- 更新 英雄 BP 建模执行状态（已归并） 与 英雄 BP 建模进度审计 2026-06-30（已归并）；重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 77 个、`reviewed` 0 个、`draft_from_raw_signals` 27 个。

## [2026-06-30] review | Edgar / Eve / Gray / Leon 升级到 bp_ready

- 复核 `Edgar`、`Eve`、`Gray`、`Leon` 四个自动草稿英雄页，修正 Edgar / Leon 被泛化成错误投掷或长线标签、Eve 的水域价值未绑定目标收益、Gray 的传送门未绑定落点安全的问题。
- 将 Edgar 的跳跃贴脸/足球得分窗口、Eve 的水域远程与 hatchling 清理税、Gray 的传送门路线改写与 Walking Cane 拉人、Leon 的隐身信息差与单抓/偷目标转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 288 增至 304。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 276 增至 292，hook seed 条目数从 281 增至 288。
- 更新 英雄 BP 建模执行状态（已归并）、英雄 BP 建模进度审计 2026-06-30（已归并） 与 [[index|Wiki Index]]；重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 81 个、`reviewed` 0 个、`draft_from_raw_signals` 23 个。

## [2026-06-30] review | Bull / El Primo / Fang / Frank / Jacky 升级到 bp_ready

- 复核 `Bull`、`El Primo`、`Fang`、`Frank`、`Jacky` 五个自动草稿英雄页，将前排/切入英雄从粗粒度短手标签改写为目标接触、控球/站圈/打库转化、进场资源、地形变换、反坦失效条件和 slot 风险。
- 将上述五个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 304 增至 324。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 292 增至 312，hook seed 条目数从 288 增至 294。
- 更新 英雄 BP 建模执行状态（已归并）、英雄 BP 建模进度审计 2026-06-30（已归并） 与 [[index|Wiki Index]]；重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 86 个、`reviewed` 0 个、`draft_from_raw_signals` 18 个。

## [2026-06-30] review | Moe / Trunk / R-T / Pierce / Glowy / Najia / Sirius 升级到 bp_ready

- 复核 `Moe`、`Trunk`、`R-T`、`Pierce`、`Glowy`、`Najia`、`Sirius` 七个自动草稿英雄页，将 Moe 的 Driller 出土资源门槛、Trunk 的蚂蚁区域身体、R-T 的分体腿部风险、Pierce 的弹壳循环、Glowy 的牵线支援、Najia 的毒区控路、Sirius 的影子经济分别改写为可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述七个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 324 增至 352。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 312 增至 340，hook seed 条目数从 294 增至 308。
- 更新 英雄 BP 建模执行状态（已归并）、英雄 BP 建模进度审计 2026-06-30（已归并） 与 [[index|Wiki Index]]；重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 93 个、`reviewed` 0 个、`draft_from_raw_signals` 11 个。

## [2026-06-30] review | Berry / Chester / Dynamike / Griff / Grom / Tick 升级到 bp_ready

- 复核 `Berry`、`Chester`、`Dynamike`、`Griff`、`Grom`、`Tick` 六个自动草稿英雄页，将 Berry 的治疗铺地与 Super 位移限制、Chester 的随机 Super 与铃铛序列、Dynamike 的 Satchel / Super 开墙、Griff 的 Piggy Bank 与近中距离爆发、Grom 的固定十字线和 Radio Check、Tick 的雷区封路与 Last Hurrah 自保分别改写为可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述六个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 352 增至 376。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 340 增至 364，hook seed 条目数从 308 增至 314。
- 更新 英雄 BP 建模执行状态（已归并）、英雄 BP 建模进度审计 2026-06-30（已归并） 与 [[index|Wiki Index]]；重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 99 个、`reviewed` 0 个、`draft_from_raw_signals` 5 个。

## [2026-06-30] review | Damian / Juju / Kit / Larry & Lawrie / Meeple 升级到 bp_ready

- 复核 `Damian`、`Juju`、`Kit`、`Larry & Lawrie`、`Meeple` 五个剩余自动草稿英雄页，将 Mosh Pit / Wall of Sound、元素地形投掷、附身支援、Lawrie 召唤物经济、Meeple 规则区域和 Mansions / Ragequit 等机制改写为可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述五个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 BP 条件化对位边索引（已删除旧手写索引）：reviewed 对位边组从 376 增至 396。
- 更新 BP 英雄地图特征适配索引（已删除旧手写索引）：reviewed Ranked 地图 hook 从 364 增至 384，hook seed 条目数从 314 增至 319。
- 更新 英雄 BP 建模执行状态（已归并）、英雄 BP 建模进度审计 2026-06-30（已归并） 与 [[index|Wiki Index]]；重跑 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 104 个、`reviewed` 0 个、`draft_from_raw_signals` 0 个。

## [2026-06-30] ingest | June 2026 版本 BP 影响覆盖

- 读取 `raw/sources/fandom/systems/release-notes-june-2026-2026-06-30.md`，只抽取会影响 BP 决策、失败条件、build 资源门槛或条件化对位边的变化；未把普通血量/伤害数值变动照搬为英雄结论。
- 新增 [[sources/Fandom-Release-Notes-June-2026|Fandom 来源摘要: Release Notes June 2026]] 与 [[syntheses/2026-06-30版本BP影响评估|2026-06-30 版本 BP 影响评估]]，作为版本 / meta 覆盖层。
- 给 `Rico`、`Brock`、`8-Bit`、`Meg`、`Max`、`Surge`、`Bolt`、`Meeple`、`Damian`、`Colette`、`Crow`、`Mortis`、`Edgar`、`Chester`、`R-T`、`Spike`、`Griff` 写入结构或对位阈值版本覆盖。
- 给 `Leon`、`Lumi`、`Najia`、`Pierce`、`Mina` 写入次级资源门槛版本覆盖；`Larry & Lawrie`、`Juju`、`Ruffs`、`Shade` 等暂留观察名单，等待玩家开发、对局样本或更明确阈值后再更新条件化对位边。
- `Brawl Arena Only` 变化未进入 Ranked BP；后续如分析 Brawl Arena，应另建模式覆盖层。

## [2026-06-30] compile | 固化 BP 当前有效模型

- 根据维护者反馈，将 `version_override` 从 BP 运行时输入改为版本 ingest 的编译输入；当时曾尝试让 BP 决策运行时默认读取 BP 当前有效模型，后续已删除该中央覆盖层。
- 更新 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]] 和 [[syntheses/条件化对位模型|条件化对位模型]]：新增 `effective_bp_model`，并将 `candidate_eval.version_fit` 改为 `candidate_eval.effective_model_fit`。
- 新增 BP 当前有效模型（已删除），把 2026-06-30 版本的 22 条 BP-relevant delta 编译为 `hard_gate_deltas`、`capability_deltas`、`build_deltas`、`matchup_deltas`、`map_hook_deltas` 和 `slot_policy_deltas`。
- 更新 BP 条件化对位边索引（已删除旧手写索引）、BP 英雄地图特征适配索引（已删除旧手写索引）、英雄 BP 建模执行状态（已归并）、[[index|Wiki Index]] 与 `AGENTS.md`，固定“稳定底座 + 版本编译输入 -> 当前有效模型 -> BP 运行时”的治理规则。

## [2026-06-30] repair | 移除 BP 运行时增量模型

- 根据维护者反馈，删除 BP 当前有效模型和后续误建的 `BP-当前决策模型.md`；运行时不再读取中央版本覆盖层。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、BP 条件化对位边索引（已删除旧手写索引）、BP 英雄地图特征适配索引（已删除旧手写索引） 与 英雄 BP 建模执行状态（已归并），固定“版本资料先审计；只有定性 BP 影响，且必须直接融入英雄 / 地图 / 对位 / hook 稳定字段”的规则。
- 撤回所有英雄页中的“版本覆盖”与“当前 BP 判断”页尾覆盖段，避免决策语料混入补丁式解释。
- 重新审计 2026-06-30 版本资料：`Rico`、`Brock`、`8-Bit`、`Meg`、`Max`、`Surge`、`Bolt`、`Damian`、`Spike` 仅标记为 `profile_merge_candidate`，等待逐字段内联；`Meeple`、`Colette`、`Crow`、`Mortis`、`Edgar`、`Chester`、`R-T`、`Griff`、`Leon`、`Lumi`、`Najia`、`Pierce`、`Mina` 保留在版本审计页，不进入运行时 BP 模型。
- 追加 `AGENTS.md` 英雄页治理规则：`wiki/entities/brawlers/` 只保存当前最新 BP 建模结果；版本 / meta 资料若不能直接内联改写稳定字段，只能留在来源、审计或日志层。

## [2026-06-30] repair | 清理 BP 运行索引和维护边界

- 将 BP 条件化对位边索引（已删除旧手写索引） 改为 `runtime_reviewed_index_from_brawler_profiles`，删除原始候选总览和待复核口径，只保留从英雄页稳定 `conditional_matchups` 派生的 reviewed 对位边。
- 将 BP 英雄地图特征适配索引（已删除旧手写索引） 改为运行时派生索引，明确只用于候选检索和地图因素连接，不保存版本差分或临时强度判断。
- 更新 [[syntheses/条件化对位模型|条件化对位模型]]：版本资料接入门槛改为维护规则，不再作为运行对象；对象编号回到 `map_profile / mode_objective_profile / brawler_profile / build_profile / conditional_matchup / draft_state / pick_slot_state / draft_eval`。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]、[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]、英雄 BP 建模执行状态（已归并）、英雄 BP 建模进度审计 2026-06-30（已归并） 和 英雄 BP 建模质量门槛（已归并），把运行时读取路径固定为稳定英雄页、地图页、对位索引和地图 hook 索引；来源候选、版本观察和审计交接只留在维护层。
- 统一英雄页和对位索引中的 `bp_use` 命名，将旧抓取阶段的候选标签改为 `candidate` / `signal` 口径，避免运行语料继续暴露原始候选阶段术语。

## [2026-06-30] skill | 新增 BP slot 决策 skill

- 新增 `skills/brawl-stars-bp-slot-decision/SKILL.md`，固化 BP 查询时的必读运行时页面、slot policy、hard gate、候选评估和输出格式，要求每手输出 2-4 个可复盘决策。
- 新增 `skills/brawl-stars-bp-slot-decision/scripts/bp_index.py`，提供只读检索辅助，用于定位 Season 46 地图实体页、英雄实体页、条件化对位边索引和英雄地图 hook 索引命中；脚本只做召回，不替代 BP 排序。
- 新增 `skills/brawl-stars-bp-slot-decision/tests/test_bp_index.py`，覆盖必读页面声明和 `Safe Zone / Brock / Mortis` 样例索引召回。
- 已运行 `python3 skills/brawl-stars-bp-slot-decision/tests/test_bp_index.py` 与 `quick_validate.py`，均通过。

## [2026-07-01] query | BP 实战查询速度与模型形态评估

- 回答“当前数据量是否能满足实战 BP 思考速度，以及实时 skill 查询和直接微调哪个更快”的问题。
- 读取 [[index|Wiki Index]]、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、[[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]、[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]、BP 条件化对位边索引（已删除旧手写索引）、BP 英雄地图特征适配索引（已删除旧手写索引）、[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]、英雄 BP 建模执行状态（已归并） 与 `skills/brawl-stars-bp-slot-decision/`。
- 新增 BP 实战查询速度与模型形态评估（已归并），结论为当前数据量足够支撑实战 BP 的有依据思考；推荐 `skill + 本地检索 + 预热上下文 + 小范围候选评估`，不建议把可变事实库直接作为微调主载体。
- 更新 [[index|Wiki Index]] 增加该 synthesis 入口。

## [2026-07-01] skill | 固化 run-bp 裁判与 BP 选手扩展

- 新增 `skills/run-brawl-stars-bp/SKILL.md`，将 BP 模拟固定为裁判编排：红蓝 ban 阶段同步提交并允许重复 ban，随后按 `blue_slot1 -> red_slot2_3 -> blue_slot4_5 -> red_slot6` 顺序轮流决策。
- 新增 `skills/run-brawl-stars-bp/references/match-report-schema.md`，统一 match report 的 Match Header、Ban Phase、Pick Turn Schema、Turn Metrics 和 Final Draft Evaluation；报告开头必须记录 `blue_model`、`red_model` 与双方 `strategy_bias`。
- 更新 `skills/brawl-stars-bp-slot-decision/SKILL.md`，新增 `strength_context`、`meta_pressure`、`overpowered_or_t0_exception` 和 `strategy_bias`；强度信号必须有来源，策略偏好只在 hard gate 与地图适配之后改变候选排序。
- 新增 `skills/brawl-stars-bp-knowledge-maintenance/scripts/test_bp_skill_contract.py`，用契约测试覆盖裁判同步 ban、报告格式、回合指标、强度语境和保守 / 均衡 / 激进 / 高方差偏好字段。

## [2026-07-01] skill | 收窄 run-bp 裁判职责

- 根据实跑反馈，将 `skills/run-brawl-stars-bp/SKILL.md` 明确改为 `neutral_recorder` / `deal_cards_only`：裁判只维护隐藏信息、发起子 agent、cue 回合、记录指标和整理选手提交内容。
- 明确 `no_judge_draft_evaluation`：裁判不读取地图 / 英雄 / 对位页面来形成 BP 判断，不评价 ban/pick 好坏，不修补选手逻辑，不给出 favored side。
- 明确 `style_bias_assigned_at_spawn` 与 `do_not_validate_style_compliance`：选手风格在创建子 agent 时固定，后续不再额外校验是否符合保守 / 激进风格。
- 将报告结尾从裁判生成的 `Final Draft Evaluation` 改为 `Player Final Statements`，只记录双方选手提交的胜利条件、风险和不确定性。

## [2026-07-01] docs | 新增 BP skill 调用 README

- 新增 `README.md`，给 agent 提供两段可直接复制的提示词：一段通过 `$run-brawl-stars-bp` 从 Ranked Season 46 地图池随机选图并开完整 BP；一段通过 `$brawl-stars-bp-slot-decision` 针对指定地图、ban 位和当前 slot 做单手 BP 决策。
- README 明确裁判只做中立记录和流程 cue，不做 BP 评价；单手 BP 示例要求输出候选、理由、风险、后续需求和被排除选项。

## [2026-07-01] skill | 固化 BP 对局人类报告模板

- 更新 `skills/run-brawl-stars-bp/SKILL.md`：裁判默认在发起选手子 agent 前随机分配双方 `strategy_bias`，并把选定值传入后续所有选手 prompt；只有用户明确要求 deterministic / balanced 时才固定为 `balanced`。
- 重写 `skills/run-brawl-stars-bp/references/match-report-schema.md`：最终 match report 改为纯 Markdown 人类可读报告，固定包含 Match Summary、Ban Phase、Draft Timeline、Player Final Statements、Stable Knowledge Refs，并禁止 YAML、raw structured log、match header、favored side 与裁判侧 Draft Evaluation。
- 新增 `skills/run-brawl-stars-bp/scripts/render_match_report.py`：用 `REPORT_TEMPLATE` 和变量注入生成稳定格式报告，保留中间数据在渲染输入中，不把 raw structured log 交付给人类读者。
- 更新 `skills/brawl-stars-bp-knowledge-maintenance/scripts/test_bp_skill_contract.py`：加入报告模板契约测试，覆盖随机 / 显式 strategy bias、人类可读段落、禁用旧评价字段和渲染脚本存在性。

## [2026-07-01] skill | 修正 balanced BP 对坦刺的系统性降权

- 更新 `skills/brawl-stars-bp-slot-decision/SKILL.md`：在候选生成阶段加入 `balanced_threat_probe`，要求每轮 2-4 个候选中主动评估至少一个 `route_based_tank_or_assassin` / `proactive_threat_candidate`，除非 `hard_gate_result.must_avoid` 或地图假阳性过滤明确排除。
- 明确 `route_endpoint_payoff`：坦刺路线必须说明可转化为进球、打库、掉宝、拿星、清投掷、翻圈、保护 carrier 或迫使防守资源，避免只按“短手能接近”粗判。
- 明确 `do_not_demote_tank_assassin_for_style_alone`：不能因为 `balanced` 风格本身把坦克 / 刺客降权；必须指出失败路线、缺少目标收益或敌方剩余低成本反制。
- 更新 `skills/brawl-stars-bp-knowledge-maintenance/scripts/test_bp_skill_contract.py`，把 balanced 主动威胁探针和坦刺候选要求加入契约测试，避免后续模拟继续收敛到单调长手 / 控制 / 续航壳。

## [2026-07-01] cleanup | 提炼并移除逐局 BP 模拟报告

- 新增 [[syntheses/BP-模拟样本关键结论汇总|BP 模拟样本关键结论汇总]]，将 14 份临时 match report 提炼为单页摘要，仅保留每图 ban 位、slot 1 / 2-3 / 4-5 / 6 选出和关键构筑理由。
- 删除 `wiki/syntheses/bp-simulations/` 临时报告目录；该目录不再作为 wiki 知识层的一部分。
- 更新 [[index|Wiki Index]]，移除 14 个逐局报告链接，只保留汇总页入口。
- 更新 `README.md`：逐局完整报告以后写入 `outputs/bp-simulations/` 作为临时运行产物；只有提炼后的关键结论进入 `wiki/syntheses/`。

## [2026-07-02] architecture | BP 运行时索引编译架构

- 新增 `raw/inbox/2026-07-02-user-note-bp-runtime-index-compilation.md` 与 [[sources/User-Note-BP-Runtime-Index-Compilation|用户经验来源摘要: BP 运行时索引应按版本语境编译]]，记录维护者关于 BP runtime 的新版分层思路。
- 新增 [[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]，将 BP skill 领域拆成 `compile / understand-version` 与 `decide` 两阶段：前者结合稳定 wiki 事实与 strength profile 编译 runtime index，后者只消费 runtime index 做 ban / pick 决策。
- 审计入口中的索引噪声：BP 条件化对位边索引（已删除旧手写索引） 与 BP 英雄地图特征适配索引（已删除旧手写索引） 当前混合了结构、slot 用途和候选语境，应在 compile 子命令落地后从长期 BP Runtime 入口移除，转为生成调试产物或删除。
- 更新 [[index|Wiki Index]]，加入新版 runtime 编译架构和对应用户经验来源入口；本次初步审计曾保留旧索引作为过渡检索视图，随后按维护者确认见下一条 cleanup 直接删除。

## [2026-07-02] cleanup | 删除旧手写 BP 运行时索引

- 删除 `wiki/syntheses/BP-条件化对位边索引.md` 与 `wiki/syntheses/BP-英雄地图特征适配索引.md`；这两个文件不再作为长期 wiki 页面维护，等价信息后续由 `bp compile` 从英雄页、地图页、模式页和 strength profile 重新生成。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、[[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]、[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]、英雄 BP 建模执行状态（已归并）、英雄 BP 建模质量门槛（已归并） 等入口，将运行时读取路径切换为稳定英雄页 / 地图页和可再生成的 `runtime_bp_index`。
- 更新 `skills/brawl-stars-bp-slot-decision/` 与 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py`，移除旧索引必读和脚本检索依赖；`bp_index.py` 现在只定位稳定页面和页面内命中，不再搜索已删除索引。

## [2026-07-02] cleanup | 归并过期 BP 维护任务页

- 新增 [[syntheses/BP-维护归档|BP 维护归档]]，归并 4 个已经完成或被替代的临时任务页：英雄 BP 建模覆盖审计、英雄 BP 建模升级任务计划、英雄 BP 建模进度审计 2026-06-30、BP 实战查询速度与模型形态评估。
- 删除上述 4 个原始 syntheses 页面；保留 [[syntheses/2026-06-30版本BP影响评估|2026-06-30 版本 BP 影响评估]] 与 [[syntheses/BP-模拟样本关键结论汇总|BP 模拟样本关键结论汇总]] 作为非运行时归档页。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、[[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]、英雄 BP 建模执行状态（已归并）、英雄 BP 建模质量门槛（已归并） 和相关来源页，修复已归并页面的入口链接。

## [2026-07-02] cleanup | 清理 BP-active scope 的显式排除项

- 删除 `wiki/sources/` 中专门描述显式排除项的 source 摘要，并移除 `AGENTS.md`、[[index|Wiki Index]]、英雄 BP 建模执行状态（已归并）、[[syntheses/BP-维护归档|BP 维护归档]]、英雄页、skill、检索脚本和 ingest 工具中的命名提醒。
- 将 BP-active 英雄集合定义改为“有有效来源覆盖的常驻英雄集合”；脚本通过有效 Fandom / PLP source 行自然得到 104 个 active 英雄。
- 长期 wiki 和 BP 运行层不再保留需要反复排除的对象。

## [2026-07-02] cleanup | 将英雄 BP 建模记录页归并为标准流程

- 新增 [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]]，沉淀英雄 BP 建模的输入边界、标准流程、`draft_from_raw_signals` / `reviewed` / `bp_ready` 质量状态和临时审计输出规范。
- 删除英雄 BP 建模执行状态、英雄 BP 建模质量门槛、英雄 BP 建模质量审计三个完成态 / 进度型 syntheses 页面；可复用内容已进入标准流程，历史说明保留在 [[syntheses/BP-维护归档|BP 维护归档]]。
- 更新 `skills/brawl-stars-bp-knowledge-maintenance/scripts/audit_bp_profile_quality.py`：`--write` 现在输出到 `outputs/bp-profile-quality-audit.md`，不再写回 `wiki/syntheses/`。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、`skills/brawl-stars-bp-slot-decision/`、[[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]] 和来源页，移除运行时读取完成态看板的依赖。

## [2026-07-02] cleanup | 归并地图建模与 BP 表达规范

- 新增 [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]，将地图知识分层、`map_profile` / `map_feature` schema、`map_bp_factor`、地图 hard gate、slot 策略、候选地图适配评估和假阳性过滤合并为一个稳定入口。
- 删除地图知识分层治理、地图特征建模 Schema、地图因素 BP 表达规范三个拆散的 syntheses 页面；它们此前表达的是同一条链路的不同层，现在统一到一份规范。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、`skills/brawl-stars-bp-slot-decision/`、地图实体页、英雄页、来源页和 BP 相关 syntheses 的链接，运行时读取路径改为单一地图规范页。

## [2026-07-02] skill | BP skill 脱离 syntheses 运行时依赖

- 重构 `skills/brawl-stars-bp-slot-decision/SKILL.md`：将选手 skill 明确拆成 `compile` 与 `decide` 两个模式，禁止把 syntheses 作为运行时渐进披露路径。
- 新增 `skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md` 与 `skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md`，把原本散在 syntheses 中的编译时规则和运行时决策规则复制进 skill 自身文档。
- 更新 `skills/brawl-stars-bp-slot-decision/scripts/bp_index.py`：脚本只定位 skill references、地图实体页和英雄实体页，不再输出 syntheses runtime pages 或依赖赛季专题页判断地图池。
- 更新 `AGENTS.md`、[[index|Wiki Index]] 与 `README.md`：区分维护者 wiki 查询和 BP skill 执行；skill 执行只依赖自身 references、`wiki/entities/` 和已生成的 `runtime_bp_index`。

## [2026-07-03] governance | 明确 wiki 与 BP skill 架构边界

- 更新 `AGENTS.md`，新增“知识架构与 BP Skill 边界”，用访问矩阵区分 `raw/`、`wiki/sources/`、`wiki/entities/`、`wiki/syntheses/`、skill references 和 `outputs/` 的职责。
- 明确 `wiki/syntheses/` 是维护综合层，不是 BP skill 的运行时依赖；syntheses 中被采纳的执行规则必须先复制到 skill references，并用契约测试固定。
- 更新 [[index|Wiki Index]]，将原 `BP Runtime` 改为 `BP Methodology`，并新增 `BP Skill Runtime` 区块，避免把 syntheses 误标为运行时知识。

## [2026-07-03] governance | 明确 source 版本清理规则

- 审计 source 命名：`wiki/sources/` 没有平行版本摘要页；抓取纠错应作为临时过程，不应成为长期 canonical 命名。
- 更新 `AGENTS.md`，明确 source 摘要页如果新版完整覆盖旧版，应合并为 canonical source page 并删除旧摘要；raw 抓取件默认保留 provenance，只有用户明确要求 raw 清理且确认覆盖关系时才删除。
- 明确 raw 临时版本号不能作为 BP skill 运行时信号；skill 只能通过 source 摘要、实体页稳定字段或 `runtime_bp_index` 消费已整理结论。

## [2026-07-03] governance | 修正 raw source 清理判断标准

- 修正 raw 清理准则：判断 `raw/` 是否可删时，首要依据是同一来源是否存在完整覆盖或纠错替代，而不是删除后是否造成 `wiki/`、`skills/`、`skills/brawl-stars-bp-knowledge-maintenance/scripts/` 的路径断链。
- 明确 Fandom 英雄页与 Power League Prodigy 英雄页属于互补来源：前者偏底层机制、定位和经验，后者偏对位关系与常见构筑；即使同属一个英雄，也不能互相替代。
- 将 Fandom gameplay / modes / systems raw 归为独立来源信息，不再按“无直接引用”列入 raw 删除候选；这类内容如有重复，应先在 `wiki/sources/`、`wiki/concepts/` 或 `wiki/syntheses/` 层做合并整理。

## [2026-07-03] cleanup | 删除被新版覆盖的 Fandom 英雄旧 raw

- 删除 `raw/sources/fandom/heroes/` 中 178 个被当前最新版完整覆盖的旧抓取件：72 个无日期初版、104 个日期基础版，以及 2 个被定点修正覆盖的中间抓取件。
- 保留 104 个当前最新版 Fandom 英雄 raw，每个 BP-active 英雄一份；保留 PLP 英雄 raw、Fandom gameplay / modes / systems raw、地图 raw、补丁 raw、roster raw 和 user note raw。
- 同步清理本地 `.DS_Store` 文件；该类文件不属于 source provenance。

## [2026-07-03] cleanup | 归一 Fandom 英雄 raw 命名并清除显式排除项

- 将 104 个当前最新版 Fandom 英雄 raw 统一命名为 `raw/sources/fandom/heroes/<hero>-2026-06-30.md`，不再保留纠错阶段后缀作为长期文件名或 wiki 概念。
- 同步更新 `wiki/sources/Fandom-*` 上游 raw 链接和 `wiki/entities/brawlers/` 中的 `fandom` provenance 字段，统一到 `direct_raw_capture_2026-06-30`。
- 从 roster manifest、roster source 摘要、raw inbox 和 Buzz 英雄 raw 中清除显式排除项残留；当前 BP-active roster 统一按 104 个常驻英雄处理。

## [2026-07-03] skill | 新增 BP 知识维护 skill

- 新增 `skills/brawl-stars-bp-knowledge-maintenance/`，将 LLM-wiki intake gate 作为 BP 维护者 skill 的前置 contract。
- 将 source ingest、英雄 BP 建模、地图 BP 建模、审计验证和 runtime 边界拆入 skill references，保持 `SKILL.md` 只负责路由和核心边界。
- 更新 `skills/brawl-stars-bp-knowledge-maintenance/scripts/test_bp_skill_contract.py`，用契约测试固定维护 skill 的 references、工具脚本归属和 `wiki/syntheses/` 与 `runtime_bp_index` 的边界。
- 更新 [[index|Wiki Index]]，在 `BP Skill Runtime` 中登记维护者 skill。

## [2026-07-03] cleanup | 移除根级辅助脚本目录范式

- 将 BP 维护脚本迁入 `skills/brawl-stars-bp-knowledge-maintenance/scripts/`，由维护者 skill 统一承载抓取、ingest、profile 初始化、质量审计和契约测试。
- 清理 wiki 与 skill references 中对旧根级辅助脚本目录的引用，后续只通过维护者 skill 的 `scripts/` 入口运行。
- 新增 `.gitignore`，忽略 `outputs/` 临时运行产物目录。

## [2026-07-03] skill | 补强 BP 知识维护 skill 的来源 ingest 边界

- 更新 `skills/brawl-stars-bp-knowledge-maintenance/references/source-ingest.md`，明确英雄来源默认结合 Fandom 与 Power League Prodigy，二者互补且不能互相覆盖；地图来源从 Brawl Stars Fandom 地图页和 Ranked 地图池页进入 `raw/sources/fandom/maps/`。
- 更新 `references/map-modeling.md` 和 `references/brawler-modeling.md`，把 Fandom map raw/source 到地图实体页、Fandom/PLP source 到英雄 BP 字段的路径写成执行规则。
- 更新 `references/audit-and-validation.md` 和 `scripts/test_bp_skill_contract.py`，固定脚本根路径、canonical knowledge writes 与 `outputs/` 生成产物边界。

## [2026-07-03] governance | 将 AGENTS.md 升级为完整维护索引

- 将 `AGENTS.md` 从旧三层概述升级为 agent 维护入口索引，显式列出 `$markdown-llm-wiki`、三个 BP skills、`wiki/index.md`、`wiki/log.md` 和真实目录职责。
- 在 `AGENTS.md` 与 `skills/brawl-stars-bp-knowledge-maintenance/` 中声明 `$markdown-llm-wiki` 的远端来源：`https://github.com/josephmax/skills/tree/main/skills/markdown-llm-wiki`。
- 将全量英雄 / 地图 BP 维护的执行入口调整为 `skills/brawl-stars-bp-knowledge-maintenance/` references；相关 syntheses 只作为维护背景和历史归档。

## [2026-07-03] research | 沉淀 strength_profile tier list maker 调研

- 新增 [[syntheses/BP-strength-profile-tierlist-maker调研|BP strength_profile tier list maker 调研]]，记录用户侧强度输入工具的调研目标、候选站点、验证结论和 adapter 路线。
- 将 `TierListMaker.online` 完整 Brawl Stars 带图标 JSON / 截图、`MetaCoreTroll` brawler API 导出和 community tier list 导出复制到 `wiki/syntheses/assets/tierlist-maker-research/`，避免依赖被 `.gitignore` 忽略的 `outputs/` 临时目录。
- 结论：未找到完全开箱满足“Brawl Stars 内置数据 + 自由制作 tier list + 原生 JSON 导出”的第三方站点；推荐用 `TierListMaker.online` 作为 UI 底座，并通过轻量 adapter 完成 roster 预填、JSON 导出和 `strength_profile` 转换。

## [2026-07-06] skill | 明确 patch ingest 的 Fandom 取证顺序

- 更新 `skills/brawl-stars-bp-knowledge-maintenance/references/source-ingest.md`：版本总页 / 官方 release note 只作为受影响英雄索引；逐英雄机制、数值和 History 细节必须读取对应 Fandom 英雄页。

## [2026-07-06] ingest | 补充 Backyard Bowl 地图 BP 知识

- 新增 `raw/sources/fandom/maps/backyard-bowl-2026-07-06.md`，保存 Fandom `Backyard Bowl` 地图页 raw capture。
- 新增 [[sources/Fandom-Backyard-Bowl|Fandom 来源摘要: Backyard Bowl]]，记录来源范围、可用边界和 BP 建模要点。
- 新增 [[entities/maps/Backyard Bowl|Backyard Bowl]] 地图实体页，沉淀开阔球路、球门前可破障碍、小草墙入口、门前 choke 防守和投掷 false-positive 过滤。
- 更新 [[index|Wiki Index]]，登记 Backyard Bowl 的来源页和地图实体页。

## [2026-07-06] governance | 新增英雄名称归一化概念页

- 新增 [[concepts/英雄名称归一化|英雄名称归一化]]，用单一 fenced YAML 映射维护中文俗称、emoji、平台写法到 brawler canonical name 的归一化规则。
- 更新 `AGENTS.md` 和三个 BP skills 的入口说明，要求用户输入、外部榜单、ban/pick 文本中的英雄称谓先归一化到 `wiki/entities/brawlers/*.md`。
- 移除临时 `tools/strength-profile-editor/data/brawler-aliases.json`，避免别名表在工具层和 wiki 层重复维护。

## [2026-07-06] ingest | 入库第一版通用版本强度先验并落地 BP compile

- 新增 `raw/inbox/ikaoss11-july-2026-tier-list-screenshot-transcription.md` 和 [[sources/iKaoss11-July-2026-Strength-Profile|iKaoss11 July 2026 Strength Profile]]，保存 iKaoss11 July 2026 tier list 截图转录后的 104 英雄全局强度 profile。
- 将该 profile 复制为 `skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json`，作为第一版默认通用版本强度先验；后续地图强度需要显式维护，不能由 global 排名推断地图适配性。
- 新增 `skills/brawl-stars-bp-slot-decision/scripts/compile_runtime_index.py`，把稳定地图/英雄事实与 strength profile 编译为 `runtime_bp_index`，并保留同档左强于右的 `tier_rank` / `total_rank` / `ordered_score`。

## [2026-07-07] skill | 将 BP compile 产物收敛为 thin runtime index

- 调整 `compile_runtime_index.py`：主产物以 `map_pool_signature`、`capability_index` 和 `evidence_refs` 为核心，用于 BP runtime 快速路由。
- 厚的 `brawler_cards`、`map_brawler_edges`、`draft_edges` 改为可选 `--debug-output` 调试产物，不进入默认 decide 路径。
- 在 `tests/test_compile_runtime_index.py` 中增加体积门槛：单图 thin index 小于 100KB，当前全地图池小于 300KB。
- 移除主产物中的 `strength_layers`、`effective_scope` 和 `scope_key`；runtime 不把 scope 选择过程暴露为决策依据。

## [2026-07-07] skill | 新增 BP runtime index 小窗口查询工具

- 新增 `query_runtime_index.py` 和 `hydrate_runtime_evidence.py`，让 BP decide 通过候选短名单与少量证据片段消费 `runtime_bp_index`，避免模型全量读取 JSON。
- 两个工具都会输出 `retrieval_log`，记录召回片段数和返回 payload KB，便于评估 JSON 是否可以继续加厚。
- 更新 `brawl-stars-bp-slot-decision` 的 decide 文档与契约测试，要求流程为 `runtime_index_precheck` -> `query_runtime_index.py` -> `hydrate_runtime_evidence.py` -> `candidate_eval`。

## [2026-07-07] skill | 将 BP runtime index 升级为 v2 工具消费结构

- 将 `compile_runtime_index.py` 的主产物升级为 `runtime-v2`：每张地图包含 `map_context`、短名单 `candidate_projection` 和覆盖全英雄的 `candidate_index`。
- 新增全局 `brawler_runtime_cards`、`matchup_index` 和 `audit_summary`，供 `query_runtime_index.py` / `hydrate_runtime_evidence.py` 按需召回，不要求模型全量读取 JSON。
- 删除默认主产物中的 `capability_index`，避免保留未被消费的宽泛倒排表；详细 raw 提取结果仍只进入可选 `--debug-output`。
- 重新生成 `outputs/runtime-bp-index/default-tierlist-all-maps-thin.json`，文件名沿用历史，内容形态为 `runtime-v2`。

## [2026-07-07] skill | 接通 BP runtime tools 到本地对局流程

- 新增 `decide_with_runtime_index.py`，把单手 pick / ban 决策固定为 `query_runtime_index.py` 召回候选短名单、`hydrate_runtime_evidence.py` 补证据，再输出 `bp_slot_decision`。
- 新增 `run_local_bp_match.py`，按 ban、蓝 1、红 2-3、蓝 4-5、红 6 的固定顺序调用单手决策脚本，并复用 match report renderer 输出本地 BP 报告。
- 更新 `brawl-stars-bp-slot-decision` 与 `run-brawl-stars-bp` 的 skill 文档和契约测试，要求 runtime 决策只通过工具小窗口消费编译产物，不临场全量读取 runtime JSON 或 wiki syntheses。

## [2026-07-07] skill | 为本地 BP 对局新增独立决策审计日志

- `decide_with_runtime_index.py` 在 `bp_slot_decision` 中附带 `decision_trace`，记录输入状态、候选短名单、过滤项、选择规则、选中英雄、地图上下文和 hydrated evidence。
- `run_local_bp_match.py` 新增 `--decision-log-output`，把每个 ban / pick slot 的工具召回量、候选排序、强度 rank/score、地图 fit、hooks、对位命中和入选理由渲染到独立 Markdown 日志。
- 保持原 match report 不变；报告面向对局阅读，decision log 面向维护者审计决策质量和权重问题。

## [2026-07-07] skill | 修正 compile 中强度输入和地图适配权重

- 调整 `compile_runtime_index.py` 的 `candidate_fit`：`mode_contract_hit` 只表示模式资格，不能把全局 S/A 英雄单独抬成地图 `strong`；`strong`、`early_pick` 和 `ban_pressure` 必须先有 `active_hook_ids` 或 `matched_capabilities` 这类具体地图信号。
- 新增回归测试，固定 `Damian` 在 `Backyard Bowl` 不应因全局 S 档 + Brawl Ball 模式契约进入 `strong`、`early_pick` 或 `ban_pressure`。
- 新增 `tools/strength-profile-editor/scripts/generate_map_strength_profile.py`，基于修正后的 runtime index 生成 27 张 Ranked 地图完整 `map` strength_profile 底稿。
- 重新生成 `outputs/runtime-bp-index/default-tierlist-all-maps-thin.json` 和 `outputs/strength-profiles/ikaoss11-ranked-map-adapted-preview.json`，供后续人工审计和逐图细调。

## [2026-07-07] skill | 增加后手 counter 条件抬升并压缩 runtime 字段

- 调整 `compile_runtime_index.py`：候选索引拆分 `map_floor_fit`、`mode_contract_fit`、`slot_eligibility`、`conditional_lift` 和 `failure_gates`，避免把版本强度输入误解释为地图强势。
- 调整 `decide_with_runtime_index.py`：候选先按地图 / 模式适配、slot 资格、敌方已选对位、失败门槛排序，强度分只作为次级 tie-breaker；`enemy_targets_answered_by_candidate` 只在 response / late pick 且敌方阵容有多个可回答目标时触发。
- 将候选索引中的重复 `risk_ids` 移除，`conditional_lift` 压缩为触发器字符串数组，保持全地图 runtime index 小于 3MB 体积门槛。

## [2026-07-07] skill | 引入可调强度权重和中文 BP 日志

- `decide_with_runtime_index.py` 新增 `--strength-weight`，按 `final=(1-weight)*职责分+weight*强度分` 归一化混合排序；`0` 表示忽略强度只看职责 / 地图 / 对位 / 风险，`1` 表示纯强度优先，默认基准值为 `0.4`。
- `compile_runtime_index.py` 不再用 tier 升级 `fit`、`map_floor_fit` 或 `slot_eligibility`；强度只保留为地图候选的独立 rank/score，并由 runtime 权重决定影响程度。
- `run_local_bp_match.py` 将 `seed` 接入每手决策的可复现 `decision_noise`，避免同输入同 bias 总是生成完全一致标准答案；同时对战报告和独立决策审计日志改为中文格式。
- 重新生成 `outputs/runtime-bp-index/default-tierlist-all-maps-thin.json`、`outputs/runtime-bp-index/user-tuned-1783418598989.json` 和 `outputs/runtime-bp-index/safe-zone-default.json`。

## [2026-07-07] skill | 修复后手 counter 在 runtime 决策中被弱化的问题

- `query_runtime_index.py` / `runtime_index_tools.py` 在敌方已选可见时，为 `answers_enemy_picks` 候选预留召回窗口，避免低强度但能回答敌方核心的候选在 `top_n` 截断前消失。
- `decide_with_runtime_index.py` 在 `strength_weight < 1` 的 response / late pick 中先覆盖可回答的敌方已选目标，再用混合分补位；双 pick 不再允许两个候选只回答同一个敌方目标而漏掉另一个有合法 answer 的目标。
- 新增回归测试覆盖 Safe Zone 回答 Byron 的 counter 召回，以及 `Byron + Colette` 已暴露时 paired response 必须覆盖两个不同敌方目标。

## [2026-07-08] skill | 重构 BP runtime 查询面为能力 brief 优先

- `compile_runtime_index.py` 的 `candidate_projection` 不再按强度前排截断，而是保留每个合法 slot 的全部具体地图能力候选；默认全地图产物约 4.05MB。
- `query_runtime_index.py` 将 `judgment_brief` 拆成主候选 `candidate_judgments` 和例外探针 `counter_watchlist`，并在 brief 中直接暴露 `ability_gate`，避免纯 counter-only 候选混入主候选。
- `decide_with_runtime_index.py` 将 slot eligibility 后置到 counter 条件之后，允许弱地图但多目标成立的后手 counter 进入可讨论层；blind ban 新增 `ban_selection_windows`，在近似同分目的桶内用 side/seed 稳定轮换。
- `decide_with_runtime_index.py` 修正 paired pick 的 counter 覆盖规则：只有 `counter_answer` 的候选不再强制占用第二个补位槽，避免 Backyard Bowl 中 Ash / Pam 这类只为覆盖敌方目标而牺牲阵容计划的组合。
- 新增 PLP 对位覆盖审计脚本，生成 `outputs/plp-matchup-coverage-audit.md`；PLP-only 关系只作为 `needs_mechanism_review` 种子，不直接进入 runtime 对位边。

## [2026-07-08] skill | 分离 BP 报告摘要与决策审计细节

- `decide_with_runtime_index.py` 为入选候选和 top decision 增加 `report_summary`、`priority_factors`、`risk_summary`、`build_summary`，让选手侧输出人类报告可读的一句话摘要和少量高权重因素。
- `render_match_report.py` / `run_local_bp_match.py` 改为在对战报告中只展示短摘要、关键因素、主要风险和构筑提示；`construct_direction`、`why_now`、能力缺口、候选短名单和分数细节继续只进入 `.decision-log.md`。
- 更新 `run-brawl-stars-bp` 与 `brawl-stars-bp-slot-decision` 规则：局中可见状态只传 picks / bans / unavailable pool，不向下一位选手暴露前手报告摘要或审计理由。

## [2026-07-08] skill | 将 BP 对局报告改为中文概括与角色配装说明

- `decide_with_runtime_index.py` 的报告摘要层不再输出原始 hook / failure / build id，而是把能力证据归纳为金库输出、长线压制、开墙改地形、续航守线、反突保护等中文概念。
- `render_match_report.py` 删除重复禁用提示、草稿流程、本地推演不确定性和裁判备注；对局报告只保留双方 ban 位、选择摘要、关键因素、主要风险、构筑提示、最终阵容职责与配装说明。
- `side_summary` 根据每个入选英雄的 `report_summary` 和 `build_summary` 生成最终陈述中的“角色职责与配装”，把星辉 / 小工具 / 装备方向放到赛后总结而不是局中状态。

## [2026-07-08] skill | 为 BP 决策审计日志增加回合级可读解释

- `run_local_bp_match.py` 在每个 ban/pick 回合的 `.decision-log.md` 中新增“回合概要”“Skill 调用过程”“工具调用摘要”“工具入参”“工具出参摘要”“召回信息解释”“工具原始出参”。
- 审计日志的前置解释层使用 `report_summary`、`priority_factors`、`risk_summary`、`build_summary` 生成中文概括，避免读者必须直接解析内部能力短语和下划线字段。
- 原始工具返回、候选包、候选短名单、能力缺口和内部分数字段仍保留在后续审计段，便于复查具体召回与排序证据。

## [2026-07-08] skill | 将 BP 本地决策从混合分改为分层裁决

- `decide_with_runtime_index.py` 不再生成或暴露 `decision_score` / ability-role-strength 混合分，改为输出 `adjudication.final_bucket`、`status`、`strength_use` 和分层证据。
- 强度只在同一裁决层内作为 tie-break；`early_pick` 以及没有 active counter value 的 `response_pick` 中，命中进场 / 控制 / 无退路 / 目标转化误判风险的路线型候选会降为 `early_exposure_watch`。
- `run_local_bp_match.py` 的独立审计日志改为展示裁决层、裁决状态和强度用途；重新跑了 Bridge Too Far、Backyard Bowl、Ring of Fire 三张图的本地 BP 报告和 decision log。

## [2026-07-10] synthesis | 复盘 BP 知识压缩与决策质量演进

- 新增 [[syntheses/BP-知识压缩与决策质量演进复盘|BP 知识压缩与决策质量演进复盘]]，整理从全量 wiki 阅读、手写索引、compile/runtime index、小窗口工具到中立事实召回 + LLM 条件化裁决的架构演进。
- 记录强度 fallback 污染地图适配、混合分制造标准答案、`mode_contract_fit` 粗化模式职责、counter 先丢失后被过度硬化、ban 只封强度榜和报告不可审计等主要质量下降及其修正。
- 明确当前恢复质量所依赖的三条原则：能力模型与目标职责先行；synergy/counter 只形成条件偏好；中间层只召回事实、不替模型决策。
- 修正 [[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]] 的旧 `pending_implementation` 状态，将迁移步骤更新为当前已落地的 compile、precheck、query、hydrate 和中立事实召回边界。
- 更新 [[index|Wiki Index]]，将该复盘接入 BP Methodology。

## [2026-07-10] design | 启动 BP 下一阶段迭代方向 grilling

- 新增 [[syntheses/BP-下一阶段迭代方向决策记录|BP 下一阶段迭代方向决策记录]]，作为持续更新的非运行时设计讨论页。
- 将模糊的“BP 质量”拆为事实可靠性、目标有效性、阵容整体性、对位利用、计划连续性、版本强度利用和可审计性，明确这些维度不能重新合成单一总分。
- 记录四个候选方向：质量评估闭环、底层知识清洗、选手推理流程和批量运行性能；当前待确认主张是先建立非唯一答案的固定场景 A/B 盲审闭环。
- 记录用户对下一阶段的两条新方向：以地图、队友和对手关系的全面利用提高 BP 质量；读取用户账号英雄数据并在召回侧遮罩不可执行候选。
- 对照当前代码确认：英雄—地图和英雄—对手已有一等关系，英雄—队友仍主要由 LLM 从能力事实临时推断；账号侧已有 `candidate_pool`、`known_player_constraints` 和 `exclude-id` 接口，但尚无账号读取与拥有/资源/熟练度分层。
- 将“关系边数量”收窄为待确认的“决策相关关系覆盖”，并提出显式英雄特有关系 + 通用能力派生关系的混合模型；将评估闭环调整为伴随关系迭代的验证底座，而非独占产品里程碑。
- 根据用户纠偏，明确当前评价对象是 ban / pick 决策质量，不是 Fandom / PLP ground truth 的数据建设质量；撤回以数据供给和场景召回为主的评价表述。
- 将单手决策表示为 map/objective/ally/enemy/exposure/failure 关系组合，提出 `decision_relation_depth`、`decision_relation_breadth`、`considered_relation_coverage`、`non_dominated_selection_rate` 和 `hard_failure_rate`。
- 提出用 Pareto 偏序而不是混合总分量化决策：代码识别被其他 serious candidate 全面支配的明显劣选，LLM 只处理前沿内部价值方向不同的真实策略取舍。
- 更新 [[index|Wiki Index]]，将讨论页接入 BP Methodology。

## [2026-07-10] ingest | 复核第 105 位英雄与 7 月 8 日平衡调整

- 新增 `raw/sources/roster/brawlers-roster-audit-2026-07-10.md`，复核 Fandom 当前已有 105 位正式英雄：Nori 已于 2026-07-09 开放训练场与提前获取，Wendy 仍为未来更新；PLP guide sitemap 仍只有 104 位英雄。
- 将旧日期化 roster 来源摘要收敛为稳定 canonical 页面 [[sources/Brawler-Roster|Brawler Roster]]，同步更新 [[index|Wiki Index]]；本地仍维持 104 个已闭环 `bp_ready` 英雄，Nori 记录为 `active_but_strength_unknown`，不在来源和强度输入补齐前直接生成 BP-ready 实体。
- 新增 `raw/sources/fandom/systems/maintenance-july-8-2026-2026-07-10.md` 与 [[sources/Fandom-Maintenance-July-8-2026|Fandom Maintenance - July 8, 2026]]，整理 Jacky、Bonnie、Jessie、8-Bit、Surge、Brock、Meg、Crow、Colette、Starr Nova、Max 的平衡调整及与官方 release notes 的冲突。
- 重抓上述 11 位英雄的 Fandom direct raw，并刷新对应 Fandom 来源摘要；对 8-Bit、Surge、Meg、Max、Colette、Crow、Starr Nova 内联更新有稳定语义影响的构筑或能力字段，其余英雄仅更新 provenance，不把纯数值变化误写成新的能力类型。
- 修正 [[sources/iKaoss11-July-2026-Strength-Profile|iKaoss11 July 2026 Strength Profile]] 的 roster 边界：其 2026-07-06 输入仍为 104 人；Nori 此后进入正式 roster，但没有保留下来的档位 / 分数，因此强度仍未知；Wendy 继续排除。
- 新增 `raw/sources/pl-prodigy/site-audit-2026-07-10.md` 并更新 [[sources/Power-League-Prodigy-站点与抽检|Power League Prodigy 站点与抽检]]：复核发现 8-Bit、Brock、Max 的推荐构筑发生变化，且 67 / 104 份动态 matchup 列表变化；但 sitemap / payload 时间戳无法证明变化发生于 7 月，因此只 ingest 站点审计，没有覆盖 per-Brawler canonical PLP 来源摘要，也没有把动态 matchup 直接提升为稳定对位边。
- 保留来源冲突：Starr Nova 超级技能充能次数、Surge 超充削弱覆盖、Brock 击退描述、Colette Buffie 名称等只在来源层记录，未写入稳定事实层。
- 运行 `audit_bp_profile_quality.py`：104 / 104 个本地英雄保持 `bp_ready`、零 blocker；运行 `test_bp_skill_contract.py` 通过，`git diff --check` 无格式错误。

## [2026-07-11] ingest | 补齐 Nori Fandom 原始页与三份 PLP canonical guide

- 使用维护脚本新增 `raw/sources/fandom/heroes/nori-2026-07-11.md` 与 [[sources/Fandom-Nori|Fandom-Nori]]，确认 Nori 的双形态攻击、钩墙 / 钩人位移、鱼资源、Super 范围 / 伤害成长、治疗 / 定身 Gadget 与两项 Star Power 机制。
- PLP 仍没有 Nori guide，现有 strength profile 也没有保留 Nori 档位；因此未绕过脚本的双源保护生成 Nori 实体或 `bp_ready` profile，runtime 默认池继续保持 104 人。
- 新增 `raw/sources/pl-prodigy/brawlers/8bit-2026-07-11.md`、`brock-2026-07-11.md`、`max-2026-07-11.md`，刷新 [[sources/PLP-8-Bit|PLP-8-Bit]]、[[sources/PLP-Brock|PLP-Brock]]、[[sources/PLP-Max|PLP-Max]]。
- 内联更新三个稳定英雄页的 PLP provenance 与 build：8-Bit 当前为 Extra Credits / Boosted Booster / Damage + Health，Brock 为 Rocket Laces / More Rockets / Damage + Shield，Max 为 Sneaky Sneakers / Super Charged / Shield + Damage；8-Bit 的动态 matchup 只在补足机制、成立条件和失效条件后更新。
- 更新 [[sources/Brawler-Roster|Brawler Roster]]、[[sources/Power-League-Prodigy-站点与抽检|Power League Prodigy 站点与抽检]] 与 [[index|Wiki Index]]，将 Nori 缺口从“缺 direct raw”收窄为“缺竞技来源 / strength / reviewed profile”。
- 新增 `raw/sources/fandom/heroes/wendy-2026-07-11.md`、`raw/sources/supercell/wendy-announcement-june-2026-2026-07-11.md`、[[sources/Fandom-Wendy|Fandom-Wendy]] 与 [[sources/Supercell-Wendy-Announcement-June-2026|Supercell Wendy Announcement]]；确认 Wendy 仍为 `FutureUpdate`，并保留普攻伤害、自身护盾、Gadget 冷却三项预发布冲突，不创建英雄实体或 runtime 候选。
- 修复 `audit_plp_matchup_coverage.py`：每位英雄只读取最新 dated direct raw，旧抓取继续作为历史 provenance，不再与当前 matchup 集合合并；新增回归测试并同步维护 skill / audit reference。
- 2026-07-11 增量核对：Fandom category API 仍为 107 个页面，过滤 future Wendy 与已移除 Buzz Lightyear 后 released roster 仍为 105；Supercell 当前 release notes 仅有 `Maintenance - July 8`；PLP sitemap 仍无 Nori / Wendy guide，Blog 最新日期仍为 2026-06-30。
- 最终验证：`audit_bp_profile_quality.py` 为 104 / 104 `bp_ready`、零 blocker；临时 runtime index 编译为 104 人、零 missing input、Nori / Wendy 均未混入；PLP audit 为 104 个最新页面 / 107 个历史 raw 文件；`test_plp_matchup_coverage.py`、`test_bp_skill_contract.py` 与 `git diff --check` 全部通过。

## [2026-07-13] ingest | 落地 Liquipedia 赛事摄取与 BSC 7 月双赛区实战观察

- 扩展 `skills/brawl-stars-bp-knowledge-maintenance/`，新增 Liquipedia MediaWiki API capture、纯解析、赛事 source/entity ingest、`tournament_observation_profile.v1` 与知识缺口审计；将 API 限流、User-Agent、gzip、CC BY-SA attribution、series/set/game、global/local ban 和 first-pick 语义写入 `references/esports-event-ingest.md`。
- 新增 EMEA revision `263360` 与 South America revision `263153` 两份不可变 raw capture，并建立对应 [[sources/Liquipedia-Brawl-Stars-Championship-2026-July-EMEA-Monthly-Finals|EMEA 来源页]]、[[sources/Liquipedia-Brawl-Stars-Championship-2026-July-South-America-Monthly-Finals|南美来源页]]和赛事实体。
- EMEA 记录 7 场实际 series / 24 个实际 set，FUT Esports 夺冠；南美记录 6 场实际 series + 1 场弃权 / 24 个实际 set，RED Canids 夺冠。`winner=skip` 与弃权均未进入 played-set 分母。
- 生成但不纳入 git 的 observation profile 与 gap audit：当前稳定地图层缺 `Crystal Arcade`、`Goldarm Gulch`、`Pinhole Punt` 三张赛事地图；另有 17 条重复实战选用与现有 compiled `map_floor_fit` 不一致的 VOD / draft-context review seeds。
- 明确赛事观察不得自动生成 strength tier、稳定地图 fit、hard gate、slot eligibility、对位边或 runtime 推荐；只有经过机制与录像复核的结论才能更新稳定英雄 / 地图事实，版本强度解释仍需单独维护者评审。

## [2026-07-14] ingest | 补齐三张赛事地图并提升可解释的 map-fit

- 新增 `Crystal Arcade`、`Goldarm Gulch`、`Pinhole Punt` 三份 Fandom revision-specific raw capture，建立 [[sources/Fandom-BSC-July-2026-Observed-Map-Pages|联合来源摘要]] 与三个 `bp_map_profile_v2` 稳定地图实体，补齐中央墙 / 侧草 / carrier 撤退、Knockout 墙袋 / 毒圈退出、Brawl Ball 草环 / 窄门转换等 BP 职责。
- 新增 [[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 三张补充地图的适配复核]]，联合 EMEA / South America 的逐 set 观察与稳定地图结构，不以 pick 频率或 set 胜场自动生成强度。
- 将机制、目标转化和失效条件可解释的五条关系内联到稳定英雄页：Crystal Arcade 的 Griff、Stu、Pearl、Meeple，以及 Goldarm Gulch 的 Charlie；只激活条件化 map hook，不改变全局 strength tier。
- Glowy / Crystal Arcade（2 picks、0 set wins）与 Damian / Goldarm Gulch（2 picks、0 set wins）继续保留为 review seeds；Pinhole Punt 的每位英雄只有 1 个 set，未复制单场阵容为稳定英雄特例。
- 重新编译 `outputs/runtime-bp-index/bsc-2026-july-three-ingested-maps.json`：3 张地图、104 个 BP-active 英雄、零 missing input；知识缺口审计从地图 ingest 后的 7 条收敛为上述 2 条刻意保留的弱证据。

## [2026-07-15] run | 用新裁判 skill 随机开 3 把排位 BP 模拟

- 用户更新 `skills/run-brawl-stars-bp`（裁判）与 `skills/brawl-stars-bp-slot-decision`（选手）skill 后，按新 skill 随机开 3 把排位 BP 模拟。地图与双方 strategy_bias 随机分配：Shooting Star（Bounty）蓝 conservative vs 红 aggressive；Double Swoosh（Gem Grab）蓝 conservative vs 红 balanced；Ring of Fire（Hot Zone）蓝 high_variance vs 红 conservative。
- 裁判只做中立记录与流程 cue：每场用 8 个真实 player subagent（蓝/红 ban、blue1、red2-3、blue4-5、red6、双方终评），选手读 `brawl-stars-bp-slot-decision` 的 decide 流程，只通过中性事实工具 `query_runtime_facts.py` / `hydrate_runtime_facts.py` 自主决策；裁判不读地图/英雄/对位页形成 BP 判断，不评价 pick 好坏，不给出 favored side。
- 直接复用已编译的 `outputs/runtime-bp-index/user-tuned-1783418598989.json`（patch season-52-2026-07-05，覆盖 27 图 / 104 英雄，strength_profile user-tuned），未重新 compile。
- 本环境无跨轮 subagent 复用能力：每个 turn 用独立 player subagent + 完整可见状态（裁判只传公开 picks/bans/unavailable pool，不传他方隐藏推理），这一点在每份报告的执行元数据里如实标注。
- 逐局完整报告写入 `outputs/bp-simulations/match-shooting-star.md`、`match-double-swoosh.md`、`match-ring-of-fire.md`；按 2026-07-01 cleanup 约定逐局报告为临时运行产物，不进 wiki syntheses，关键结论如需沉淀再单独提炼。
- 三场阵容：Shooting Star 蓝 Brock/Nani/Colt vs 红 Piper/8-Bit/Angelo（长线狙击镜像）；Double Swoosh 蓝 Meg/Charlie/Sandy vs 红 Meeple/Surge/Najia（机甲+茧+沙暴 vs 规则区+阶段控线+越墙毒区）；Ring of Fire 蓝 Poco/Max/Griff vs 红 Damian/Emz/Berry（续航+探草+清点 vs 突进+喷雾+续航锚）。

## [2026-07-17] ingest | 全量复核 43 名受平衡调整影响英雄的稳定 BP 模型

- 按 2026 年 6 月底版本更新与 7 月 8 日维护的去重并集，逐页扫描 43 名直接受改动英雄；判断顺序以补丁改动逻辑、当前 Fandom 机制和既有 PLP 竞技资料为主，月赛选用只作事实佐证，不从出场率、胜负或样本频率推导 strength tier。
- 为 43 人各新增一份不可变的 `raw/sources/fandom/heroes/*-2026-07-17.md` 抓取件，并将对应 43 个 `wiki/sources/Fandom-*.md` 摘要切到当前 raw provenance；未覆盖或删除历史 raw。
- 38 人的当前机制足以改变稳定能力字段、资源门槛、地图 hook、failure mode、条件对位或 slot 任务：Surge、Meg、Rico、Brock、8-Bit、Max、Jessie、Mandy、Gale、Tara、Shelly、Dynamike、Larry & Lawrie、Sprout、Barley、Juju、Gray、Starr Nova、Buzz、Lou、Pearl、R-T、Mortis、Colette、Crow、Leon、Chester、Edgar、Mina、Ruffs、Meeple、Lumi、Najia、Pierce、Bolt、Spike、Griff、Damian。
- Piper、Carl、Jacky、Bonnie、Shade 记为 `no_change_after_review`：本轮数值 breakpoint 或 Hypercharge 频率变化没有改变其稳定职责、地图成立条件、条件对位或 slot 任务，因此只刷新来源复核标记，不把纯数值变化硬写成能力类型变化。
- 关键纠偏包括：Surge 的 Stage 0 为 680、Stage 1 为 820，Serve Ice Cold 让开局直接持有满 Super，首个门槛是安全使用而不是先充能；Meg 的 Mecha swing / Heavy Metal 是受 2.703% 单枚命中充能约束的低频资源；Lou 的约 0.4 格弹体降低窄口命中门槛，但 0.7 秒卸弹和 Frost 衰减仍保留；Rico、Brock、8-Bit、Max 的 rework 机制已直接重写到当前能力与地图适配层。
- 本轮没有编辑或生成任何 strength profile、tier、玩家偏好结论，也没有重新编译 `runtime_bp_index`；强度输入继续保留给玩家，runtime 等玩家确认强度层后再编译。
- 验证：43/43 英雄页、43/43 source summary、43/43 新 raw 均带 2026-07-17 provenance；全库 104 个 `bp_ready` profile 审计为 0 blockers，BP skill contract 通过，`git diff --check` 通过。

## [2026-07-17] skill+ingest | 落地平衡补丁伤害—生存断点审计

- 新增用户维护规则 raw/source、[[concepts/伤害与生存断点|伤害与生存断点]] 概念页与 maintainer `references/balance-breakpoint-audit.md`，将 Power Level 换算、满值 Shield gear `+900`、不同合法减伤加法叠加、精确分数 EHP、死亡等号与舍入复核固化为可执行语义；Power Points 数值成长来源如实标为 search-result excerpt capture，不冒充 direct export。
- 在六月末与 7 月 8 日 patch source 页面加入 `balance_breakpoint_manifest.v1`，使用 `type + change_class` 区分可计算 damage packet / target state / defense modifier 与 DoT、多段 cycle、召唤物、时间轴、来源冲突等排除项；Crow 连续伤害链按 P1 `320 -> 420 -> 380` 回放，而不是只从当前值反推历史。
- 新增 `combat_breakpoint_profile` 作为英雄页第二个、维护期专用 JSON 块；当前共 20 个 combat profile，覆盖 15 个带伤害包的页面和 7 个带 10 项专属防御 modifier 的页面。Bibi 的两项 20% 条件减伤、Pearl Heat Shield、Mandy Hard Candy、Colette Mass Tax、Jacky Hard Hat、Meg Force Field、R-T 分体减伤等均保留成立条件与合法叠加关系；R-T 腿部默认 29% 与 Recording 替换为 50%，不生成不存在的 0% 减伤状态。
- 新增 `audit_balance_breakpoints.py` 与 10 项回归测试。基础血量索引覆盖 roster 104 / 104，并额外纳入已发布但尚未进入 BP runtime 的 Nori，合计 105 个目标；当前物化 109 个目标形态、242 个条件生存状态、17 个已复核伤害包，其中 10 个允许按相同包重复计算。伤害、血量、减伤都校验补丁链连续性和 latest-after 与当前稳定输入的一致性。
- 本次联合回放生成 `outputs/balance-breakpoints/2026-june-july-balance-breakpoints.{json,md}`：1162 条整数命中数变化、493 条构筑压力变化、18 条带英雄 / 变更 ID / 原因的显式排除，且没有 current-after mismatch。基础形态三包内斩杀覆盖中，Gray `38 -> 63`、Mandy `68 -> 81`、Piper 最大距离 `92 -> 98`、Sprout `24 -> 33`、Carl `0 -> 2`、Bonnie Clyde `33 -> 49`；这些计数是唯一英雄分母，不重复计算护盾或多形态。
- 高价值卡线包括：Crow P11 血量 `6000 -> 5600` 后，Bibi P11 完整挥棒 `2800` 从 3 次变 2 次，满值 Shield gear 仍维持 3 次；Mandy 对 Barley / Bea / Crow、Gray 对 Nani / Tick、Bonnie 对 Meg / Tick，以及 Piper 最大距离对一批中血量英雄也出现 3 次变 2 次与 Shield 维持旧线的构筑压力。
- 只把机制、成立条件、失效条件与既有 BP 消费字段都明确的确定性事实内联到 Bibi、Pearl、Mandy、Colette、Jacky、Crow、Piper、Gray、Bonnie、Sprout 的当前能力字段；断点产物没有自动生成 strength tier、稳定 map fit、无条件对位边、slot eligibility 或 runtime 推荐，Nori 也没有因此进入 BP-active 集合。
- 验证：断点测试 10 / 10、BP skill contract、104 个 BP profile 质量审计、maintainer skill quick validation、Python syntax 与 `git diff --check` 均通过；独立首次使用者前向复跑通过且联合输出确定性一致。

## [2026-07-17] synthesis | 沉淀六月至七月断点双向加强评估

- 新增 [[syntheses/2026六月至七月平衡性断点双向评估|2026 六月至七月平衡性断点双向评估]]，按105个基础目标整理 Carl、Gray、Bonnie、Mandy、Piper、Sprout 的全部 `n→n-1` 当前净断点，并将 Gray 对 Jacky 的六月 `5→4` 与七月反转 `4→5` 合并为无净收益。
- 攻击方按唯一基础目标覆盖排序为 Carl 54、Gray 38、Bonnie 23、Mandy 22、Piper 17、Sprout 17；同时保留 `3→2`、更高发数和精确等号复核行，避免重新把三发阈值误当成全部变化。
- 受击方将纯 `target_health` 与同补丁 `damage_packet + target_health` 联合结果分开；任一已复核合法状态的唯一攻击包覆盖为 Jacky 4、Starr Nova 3、Piper 1，裸本体则为 Starr Nova 2、Jacky/Piper 各1。
- 更新 [[index|Wiki Index]] 接入 BP Archive；本页保持 maintainer synthesis / non-runtime 边界，不生成 strength tier、稳定对位边、地图适配或 BP 推荐。

## [2026-07-21] ingest+synthesis | 补齐 BSC 7 月东亚与北美月赛并更新坦度实战修正

- 通过 Liquipedia MediaWiki API 新增东亚 revision `264095` 与北美 revision `264554` 两份不可变 raw capture，并建立对应来源摘要与赛事实体。
- 东亚记录 7 场实际 series / 26 个实际 set，ZETA DIVISION 夺冠；北美记录 7 场实际 series / 24 个实际 set，Team Elektros 夺冠。
- 将 EMEA、South America、East Asia 和 North America 重建为 27 场已进行 series / 98 个已进行 set 的 `tournament_observation_profile.v1`，并生成新的知识缺口审计；产物保留在 gitignored `outputs/esports/`。
- 更新 [[syntheses/2026六月至七月平衡性断点双向评估|2026 六月至七月平衡性断点双向评估]]：坦度加强的四赛区实战修正为 Piper > Starr Nova > Jacky。Piper 的 7 个选用 set 中有 1 个对到 Gray，但双方同补丁前后都是 3 发；Starr Nova 的 4 次选用与 Jacky 的 0 次选用均未直接实现已索引纯 HP 跨线。
- 保留口径边界：选用 / ban 只作实战相关性修正，不归因补丁、不生成 strength tier、稳定 map fit、对位边或 runtime 推荐；同 set 对手也不等于实际对线。

## [2026-08-10] ingest | 更新 8 月 4 日平衡调整与断点账本

- 新增 Supercell 官方 direct raw `raw/sources/supercell/maintenance-august-4-2026-2026-08-10.md` 与 [[sources/Supercell-Maintenance-August-4-2026|Maintenance - August 4, 2026]]，完整整理 8 位常规英雄削弱、22 位英雄的 23 项 NanoPower 活动调整与 7 项 bug fix；更新 [[index|Wiki Index]] 导航。
- 强制刷新 Crow、Griff、Starr Nova、Damian、Max、Bolt、8-Bit、Surge 的 2026-08-10 Fandom direct raw 和 canonical Fandom source summary；历史 raw 保持不变。
- 将当前稳定语义内联回 8 位英雄页：Crow 单匕首 P1 `320`；Starr Nova P1 `3700 HP`、`1.6s` 装填、叠伤 4% / 20%；Damian 强化拳 P1 `800`、爆炸 P1 `400`、speaker bounce P1 `400`；Bolt Overdrive 官方 30% 减伤；另同步 Griff 半径/散布、Max 双 dash 2 秒窗口、8-Bit 18 秒 Extra Credits / 10% 队友加速、Surge 470 unload / 1 ammo refund 的资源语义。
- 在 `balance_breakpoint_manifest.v1` 中建立第 3 段补丁链；6 项变化进入可计算层（Crow 1 个 damage packet、Damian 3 个 damage packet、Starr Nova 1 个 target state、Bolt 1 个 defense modifier），其余 reload、charge、spawnable、临时活动能力、时序叠层与来源冲突均显式排除。
- 保留三项关键冲突：Crow Slowing Toxin 官方 `800 -> 600` 与 Fandom structured fields 未闭合；Bolt Fandom 说明仍写 40% 而官方已是 30%；Damian Fandom Super quote 仍写 800 而官方与 infobox 已是 400。
- 生成 gitignored `outputs/balance-breakpoints/2026-june-august-balance-breakpoints.{json,md}`：105 个 active targets、244 个条件生存状态、19 个已复核伤害包；联合回放 1442 条整数命中数变化、605 条构筑压力变化与 34 条显式排除。8 月补丁自身对应 267 条整数变化、108 条构筑压力变化，且没有补丁链或 current-after mismatch。
- 验证：断点测试 10 / 10、104 / 104 `bp_ready` 且零 blocker、BP skill contract 与 `git diff --check` 全部通过；本轮没有生成 strength tier、稳定 map fit、无条件对位边、slot eligibility 或 runtime 推荐。

## [2026-08-11] ingest | 补齐 Nori 双源闭环并对齐 105 英雄口径

- 运行时复核发现 PLP 已上线 Nori guide（`https://powerleagueprodigy.com/nori` 在 2026-07-11 仍为 404，2026-08-11 已为有效页面，含完整 build/matchup/mode 结构）；因此走正常双源路径，不再需要单源例外机制。
- 新增 `raw/sources/roster/brawlers-roster-2026-08-11.md` 作为含 Nori 的新基线 manifest（105 行，Nori 行的 Fandom + PLP URL 均有效）；基线 `brawlers-roster-2026-06-29.md` 保持只读。
- 通过维护脚本抓取 `raw/sources/pl-prodigy/brawlers/nori-2026-08-11.md`（PLP direct raw，含 Gadget/SP/Gears/Modes/8 counters/8 countered_by 完整 payload）。
- 生成 [[sources/PLP-Nori|PLP 来源摘要: Nori]]；补全 [[sources/Fandom-Nori|Fandom 来源摘要: Nori]] 的"页面核心字段"，加入双形态第二伤（Dash/Ranged 720）、Super 成长公式（每鱼 +5% 半径 / +4% 伤害，空命中也消耗）、SuperSuperCharge 9-36%、Gadget 数值与 CD、两项 Star Power、鱼资源系统、充能机制限制，以及 Gadget 数值在 Fandom Infobox vs Quote vs PLP 之间的口径冲突；回灌 2026-08-04 维护笔记的 3 条 Nori bug fix。
- 新建 [[entities/brawlers/Nori|Nori]] 实体页并升级为 `profile_status: bp_ready`：基于 Fandom 双形态机制 + PLP 竞技信号 + 8/4 补丁 fix，写入完整 capability_vector、2 个 build_switches、3 条 map_feature_hooks（Hot Zone 成长水坑清区 / Heist 成长 Super 打库 / hook 跳墙刺杀）、4 个 objective_contracts、4 条 failure_modes、2 组 conditional_matchups（覆盖 PLP 的 8 counters + 8 countered_by）和四档 slot_notes。
- 更新 [[index|Wiki Index]]：第 105 位英雄口径从"104 bp_ready + Nori 缺口"改为"105 bp_ready"；Nori 加入英雄列表和来源清单。
- 更新 [[sources/Brawler-Roster|Brawler Roster]]：数量口径表 PLP guide coverage 从 104 升到 105、本地 bp_ready 实体从 104 升到 105、roster ingest 缺口从 1 降到 0；新增 2026-08-11 基线 raw 指针。
- 更新 [[sources/iKaoss11-July-2026-Strength-Profile|iKaoss11 July 2026 Strength Profile]]：Nori 描述从 `active_but_strength_unknown` 更新为"已有 bp_ready 实体页但 strength 档位仍缺，runtime tier=unknown"。
- 更新 `test_plp_matchup_coverage.py` 的 PLP raw 页数断言从 104 到 105（Nori 已进入 PLP 覆盖范围）。
- 保留的审计缺口：Nori 缺 strength profile 档位（iKaoss11 July 输入早于 Nori 发布），runtime compile 时 tier=unknown；补齐玩家 strength 输入后即可进 runtime 池排序。本轮未重新 compile runtime index。
- 验证：质量审计 105 / 105 `bp_ready` 且零 blocker、BP skill contract、断点测试 10 / 10、PLP matchup coverage 2 / 2、`git diff --check` 全部通过。

## [2026-08-12] ingest+synthesis | 新建 Ranked Season 47 地图池索引并标记 Season 46 过期

- 经浏览器直读 Fandom Ranked 页（`https://brawlstars.fandom.com/wiki/Ranked`，"Active maps (Season 47)" 表）确认当前赛季为 Season 47（2026-07-16 起，2026-08-20 换 Season 48），featured 模式从 Season 46 的 Heist 切换为 Gem Grab；Trial Brawlers 表锚点 `#47 | July 16, 2026 | Berry, Tara, Meg | Gem Grab`、`#48 | August 20, 2026 | Trunk, Willow, Kaze | Brawl Ball`。
- 新增 [[syntheses/Ranked-Season-47-地图Map-Profile总览|Ranked Season 47 地图 Map Profile 总览]]：记录当前 6 模式 28 张图完整池（Gem Grab 6、Heist 6、Bounty 4、Brawl Ball 4、Hot Zone 4、Knockout 4）与 S46→S47 差异表。
- 与 Season 46 的差异：featured 机制是在原有基数上额外增加图，不从别的模式抢图；因此 Gem Grab 从 4 张扩到 6 张（新增 Crystal Arcade、Rustic Arcade，原 4 张全部保留），其余五个模式图数和图名完全不变。Heist 降回常规仍保持 6 张，无图被移除。
- 在 [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]] 顶部加过期标注，指向 S47 索引；S46 页保留作历史索引。
- 更新 [[index|Wiki Index]]：BP Methodology 区、Syntheses 区和 BP 维护者导航行接入 S47 索引。
- 待 ingest 缺口：`Rustic Arcade` 为 Season 47 Gem Grab featured 新增图，仓库尚无 `raw/sources/fandom/maps/` raw capture、source 摘要或地图实体页（Fandom 页有效 `https://brawlstars.fandom.com/wiki/Rustic_Arcade`，地图图 `Rustic_Arcade-Map.png` revision `20260225223748`）；S47 索引已标注待 ingest，本轮不凭空建模。
- 保留口径边界：本页只作为赛季轮换索引，不生成 strength tier、稳定 map fit、无条件对位边或 runtime 推荐；Rustic Arcade 的稳定 map_profile 需按正常地图 ingest 流程补齐 raw + source 后才能进入 BP 稳定层。

## [2026-08-13] governance+fix | 全排位模式适配性完备性治理

### 背景

运行 BP 预跑（Crystal Arcade / Gem Grab / Nori S 档末）时发现 Nori 的 compile `fit=weak` 是假阴性：根因是 Nori 实体页只有 PLP 推荐模式（Hot Zone/Heist/Bounty/Brawl Ball）的 `objective_contract` 和 `map_feature_hooks`，缺 Gem Grab 和 Knockout。系统性扫描确认 105/105 bp_ready 英雄全部缺至少一个排位模式的 contract（平均缺 2.3 个，Knockout 79 人缺、Bounty 62 人缺、Gem Grab 28 人缺），compile 对所有缺 contract 的模式一律输出 `fit=weak`，无法区分"数据缺口"和"真实弱"。

### 改动（4 文件）

1. `scripts/audit_bp_profile_quality.py`：新增 `RANKED_MODES` 常量（6 个硬编码排位模式）和 `incomplete_ranked_mode_coverage` blocker。审计提取每个英雄的 `objective_contracts` 模式集合，对比 6 个排位模式，缺失的报 blocker；负向/false_positive contract 计为有效覆盖。新 blocker 对所有 status 检查，但在 `bp_ready` 判定中是硬门槛。
2. `references/brawler-modeling.md`：`bp_ready` 门槛新增"必须对全部排位模式有 `objective_contract`"要求；Modeling Flow 步骤 3-4 补充"PLP 推荐是反向验证不是评估范围来源，每个排位模式都要独立评估"。
3. `references/audit-and-validation.md`：blocker 列表同步加入 `incomplete_ranked_mode_coverage`、`missing_profile`、`missing_map_hooks`（脚本产出但文档缺失），移除 `unreviewed_matchup_candidate`、`unreviewed_build_delta`（文档列出但脚本不产出）。
4. `scripts/ingest_brawler_bp_profiles.py`：`objective_contracts()` 函数末尾新增逻辑——为 PLP 未推荐但属于排位池的模式生成 `needs_review` 占位 contract（`not_inferred_from_source` 标记），使缺口在 draft 页面可见而非隐形；占位 contract 会触发 `auto_placeholder` blocker，保证升级 bp_ready 前被替换。

### 止氪验证（Nori）

给 [[entities/brawlers/Nori|Nori]] 补建 `gem_grab_hook_dive_and_zone_control` map_feature_hook（hook 追 gem carrier + root 断倒计时 + 水坑封矿，example_maps 指 Crystal Arcade/Double Swoosh/Hard Rock Mine）和 Gem Grab + Knockout 两个 `objective_contract`。重新 compile Crystal Arcade 后 Nori 的 `fit` 从 `weak` 升到 `strong`，`map_floor_fit=strong`、`active_hook_ids=['gem_grab_hook_dive_and_zone_control']`、`matched_capabilities=['grass_flank']`、四个 projection bucket 全激活、`slot_eligibility` 全 true。审计确认 Nori 成为 105 英雄中唯一 6 模式全覆盖且零 blocker 的英雄。

### 设计原则

完备性是 compile 入口的先决条件，不带入 runtime：compile 产物的 `fit` 保持 strong/weak 二值（都是已评估的），runtime 永远不会遇到"未评估"。6 个排位模式硬编码（地图池动态由 compile 按图逐张评估，不在审计范围）。PLP 推荐是反向验证不是评估范围来源。

### 不改动的地方

`compile_runtime_index.py`、`compile-knowledge.md`、`runtime-decision-knowledge.md` 不改动——compile 忠实执行实体页事实的设计是正确的；现有规则（`mode_contract_hit` 只是证据不是 eligibility）不变。

### 验证

审计脚本 Python 编译通过、105 英雄全部检出 `incomplete_ranked_mode_coverage` blocker（分布：缺 1 模式 2 人、缺 2 模式 33 人、缺 3 模式 51 人、缺 4 模式 13 人、缺 5 模式 4 人、缺 6 模式 2 人）；契约测试 `bp skill contract ok`；Nori compile fit 升级确认。

### 后续（不在本轮）

105 英雄的模式覆盖缺口（约 250 个 contract）补齐是批量维护任务，审计脚本输出已生成精确工单；按 Season 47 featured 模式（Gem Grab 28 人缺口）优先分批补。

## [2026-08-13] fix+governance | Power Level 11 统一口径：方法论 + 脏数据清洗

### 背景

讨论 Nori 强度时发现其 `capability_vector.survivability` 写的"3800 血"是 Power Level 1 裸值（Fandom infobox 基准），而 Ranked 实际在 Power Level 11 下血量应为 7600（Level 1 × 2.0，规则见 [[concepts/伤害与生存断点|伤害与生存断点]]：`multiplier(power) = 1 + 0.10 * (power - 1)`，`multiplier(11) = 2.0`）。系统性扫描确认这是全库问题：58 个英雄、77 处 BP 评价字段（`survivability`、`failure_modes.exposed_by`、`objective_contracts.cannot_fulfill`、`build_switches` 等）使用了 Power Level 1 裸血量，只有 6 个英雄（Bibi、Colette、Crow、Jacky、Mandy、Pearl）正确标注了 Power 11。`burst` 字段的伤害数值无此问题（已统一用 Power 11）。`combat_breakpoint_profile` JSON 块的 `at_power_level: 1` 是断点审计的原始记录、不是 BP 评价字段，不在清洗范围。

### 方法论改动

1. `references/brawler-modeling.md`：`bp_ready` 门槛新增一条——所有 BP 评价字段（`capability_vector`、`objective_contracts`、`failure_modes`、`map_feature_hooks`、`build_switches`、`conditional_matchups`、`slot_notes`）的血量/伤害/EHP 数值必须是 Power Level 11 口径（Fandom infobox 值乘 2.0），首次出现标注"Power 11"；`combat_breakpoint_profile` JSON 块的 `at_power_level: 1` 原始记录豁免。`Common Mistakes` 新增一条——禁止在 BP 评价字段引用 Power Level 1 裸值，Power Level 是养成产物不是 BP 因素。
2. `wiki/concepts/伤害与生存断点.md` 第 11 行规则扩展适用范围声明：不仅断点审计用 Power 11，英雄页全部 BP 评价字段也必须用 Power 11。

### 脏数据清洗

批量清洗 58 个英雄 77 处 Power Level 1 裸血量 → Power Level 11（×2.0 并标注"Power 11"）。覆盖 `capability_vector.survivability`（56 处）和 `failure_modes.exposed_by` / `objective_contracts.cannot_fulfill` / `build_switches.changes_capabilities` / `conditional_matchups.mechanism`（21 处）。多形态英雄（Bonnie: Clyde 5000→10000 + Bonnie 形态 3100→6200；Meg: 本体 2400→4800 + 机甲 3700→7400；Larry & Lawrie: Larry 3000→6000 + Lawrie 3300→6600）两套形态血量同时修正。残留检查确认零 Power 1 本体血量裸值。

### 验证

审计脚本 Python 编译通过；残留 grep 零结果（排除召唤物/炮台/装备值等非本体血量）；契约测试 `bp skill contract ok`；Nori 重新 compile Crystal Arcade 确认 `fit: strong` 不受影响。

## [2026-08-13] maintenance | 补齐 8 英雄缺失模式 objective_contract

### 变更

按模式覆盖缺口工单为 8 个英雄页补充缺失的 `objective_contract`（插入在 `objective_contracts` 末尾、`failure_modes:` 之前），每条含 `mode` / `can_fulfill` / `cannot_fulfill` / `needs_teammate_support` / `false_positive`，基于各页已有 mechanics、failure_modes 与 map_feature_hooks 写诚实契约（含负向契约）：

- [[entities/brawlers/Penny|Penny]]：Brawl Ball、Bounty、Knockout
- [[entities/brawlers/Poco|Poco]]：Heist、Bounty、Knockout
- [[entities/brawlers/Rosa|Rosa]]：Heist、Bounty、Knockout；原合并的 `Bounty/Knockout` 薄契约拆为两条独立 per-mode 契约（保留原负向结论并展开），与全库 one-entry-per-mode 约定一致
- [[entities/brawlers/Sam|Sam]]：Bounty、Hot Zone、Knockout
- [[entities/brawlers/Shelly|Shelly]]：Heist、Bounty、Knockout
- [[entities/brawlers/Squeak|Squeak]]：Gem Grab、Brawl Ball、Heist
- [[entities/brawlers/Stu|Stu]]：Heist、Bounty、Knockout
- [[entities/brawlers/Tara|Tara]]：Bounty、Hot Zone、Knockout

### 验证

脚本校验 8 页 fenced YAML 全部可解析，8 英雄目标模式全部存在，所有 contract（新旧）五字段齐全。

## [2026-08-13] maintenance | 补齐 7 英雄缺失模式 objective_contract

### 变更

延续 [[#2026-08-13 maintenance 补齐 8 英雄缺失模式 objective_contract|上一轮]] 的模式覆盖缺口治理，为 7 个英雄页补充缺失的 `objective_contract`（插入在 `objective_contracts` 末尾、`failure_modes:` 之前），每条含 `mode` / `can_fulfill` / `cannot_fulfill` / `needs_teammate_support` / `false_positive`，基于各页已有 mechanics、failure_modes 与 map_feature_hooks 写诚实契约（含负向契约），HP 统一按 Power 11 口径：

- [[entities/brawlers/Bea|Bea]]：Gem Grab、Heist、Bounty、Knockout
- [[entities/brawlers/Bibi|Bibi]]：Gem Grab、Bounty、Hot Zone、Knockout
- [[entities/brawlers/Brock|Brock]]：Gem Grab、Bounty、Hot Zone、Knockout（保留原 `Bounty_or_Knockout` 合并条目作为 Rocket No. 4 节奏上下文）
- [[entities/brawlers/Gene|Gene]]：Heist、Bounty、Hot Zone、Knockout（保留原 `Bounty_or_Knockout` 合并条目）
- [[entities/brawlers/Glowy|Glowy]]：Gem Grab、Heist、Bounty、Knockout（保留原 `Bounty_or_Knockout` 合并条目）
- [[entities/brawlers/Kit|Kit]]：Brawl Ball、Heist、Bounty、Hot Zone（保留原 `Brawl Ball_or_Hot Zone` 合并条目作为 Cheeseburger 变体上下文）
- [[entities/brawlers/Lola|Lola]]：Gem Grab、Bounty、Hot Zone、Knockout（保留原 `Bounty/Knockout` 合并条目）

### 设计说明

新增条目按全库 one-entry-per-mode 约定写成独立 per-mode 契约；对已有合并条目（`Bounty_or_Knockout`、`Brawl Ball_or_Hot Zone`、`Bounty/Knockout`）采取保留策略，因其承载了独特 build/gadget 上下文（如 Kit 的 Cheeseburger 变体说明、Brock 的 Rocket No. 4 间歇射程警告），删除会丢失信息。若后续治理决定全库清理合并条目，可统一合并并迁移上下文到独立条目的 `false_positive` 或 `needs_teammate_support`。

### 验证

逐页 Edit 后确认插入位置正确（`failure_modes:` 之前）；YAML 缩进与各页既有 `objective_contracts` 一致（4 空格基线 + 每 mode 列表项 4 空格）；五字段齐全；HP 描述全部用 Power 11 口径（Bea 5600、Kit 6200、Lola 8000 等）。

## [2026-08-13] maintenance | 补齐 8 英雄缺失模式 objective_contract（第三批 Busters–Dougs）

### 变更

延续 [[#2026-08-13 maintenance 补齐 7 英雄缺失模式 objective_contract|上一轮]] 的模式覆盖缺口治理，为 8 个英雄页补充缺失的 `objective_contract`（插入在 `objective_contracts` 末尾、`failure_modes:` 之前），每条含 `mode` / `can_fulfill` / `cannot_fulfill` / `needs_teammate_support` / `false_positive`，基于各页已有 mechanics、failure_modes、map_feature_hooks 与相关地图实体页（Dry Season、Hideout、Belle's Rock 等）写诚实契约（含负向契约），HP 统一按 Power 11 口径：

- [[entities/brawlers/Buster|Buster]]：Gem Grab、Heist、Hot Zone
- [[entities/brawlers/Buzz|Buzz]]：Bounty、Hot Zone、Knockout
- [[entities/brawlers/Chuck|Chuck]]：Brawl Ball、Bounty、Knockout
- [[entities/brawlers/Clancy|Clancy]]：Heist、Bounty、Knockout
- [[entities/brawlers/Colt|Colt]]：Bounty、Hot Zone、Knockout
- [[entities/brawlers/Damian|Damian]]：Heist、Bounty、Knockout
- [[entities/brawlers/Darryl|Darryl]]：Gem Grab、Bounty、Hot Zone
- [[entities/brawlers/Doug|Doug]]：Heist、Bounty、Hot Zone

### 契约设计说明

- 短手英雄（Buzz 刺客、Damian 短手坦、Darryl 滚桶坦、Doug 3.33 格支援）的 Bounty/Heist/Hot Zone 契约多为强负向：开放长线图（如 Dry Season、Bridge Too Far）风筝短手，故标为高风险 last-pick 而非稳定 source；Bounty/Knockout 死亡不可恢复使进场落点被守即送头。
- Chuck 的 Brawl Ball/Bounty/Knockout 契约强调 route-based 且 setup-dependent，PLP 只推荐 Heist，故非常规 lane pick。
- Colt 的 Bounty/Hot Zone/Knockout 契约为正向：长线 + 开墙 + tracking burst 匹配开放图，但仍标注 mobility/flank 会打断 tracking window 的失败条件。
- Clancy 的 Heist/Bounty/Knockout 契约强调 Stage 1 ramp 弱势与 7600 Power 11 低血聚焦风险，PLP 推荐模式不含这三项。
- Buster 的 Heist 契约明确 barrier 不能 race safe、lobbed/area 绕过 screen，PLP 不列 Heist，仅作 projectile-safe plan 的防御屏。

### 验证

`audit_bp_profile_quality.py`：8 英雄全部 `bp_ready_structural_gate_passed`（0 blocker）；逐页 fenced YAML 全部可解析（`yaml.safe_load` 通过），8 英雄各 6 个 Ranked 模式齐全，所有 contract（新旧）五字段齐全。库内残留 `incomplete_ranked_mode_coverage` 的 12 个英雄（Bonnie、El Primo、Eve、Frank、Gale、Gray、Grom、Kaze、Kenji、Larry & Lawrie、Mr. P、Ollie）为本任务范围外的既有缺口，未改动。

## [2026-08-13] maintenance | 补齐 8 英雄缺失模式 objective_contract（第四批 Hank–Larry & Lawrie）

### 变更

延续前三批的模式覆盖缺口治理，为 8 个英雄页补充缺失的 `objective_contract`（插入在 `objective_contracts` 末尾、`failure_modes:` 之前），每条含 `mode` / `can_fulfill` / `cannot_fulfill` / `needs_teammate_support` / `false_positive`，基于各页已有 mechanics、failure_modes 与 map_feature_hooks 写诚实契约（含负向契约），HP 统一按 Power 11 口径：

- [[entities/brawlers/Hank|Hank]]：Heist、Bounty、Knockout
- [[entities/brawlers/Jacky|Jacky]]：Heist、Bounty、Knockout
- [[entities/brawlers/Janet|Janet]]：Heist、Bounty、Knockout
- [[entities/brawlers/Jessie|Jessie]]：Brawl Ball、Bounty、Knockout
- [[entities/brawlers/Kenji|Kenji]]：Heist、Bounty、Knockout
- [[entities/brawlers/Larry & Lawrie|Larry & Lawrie]]：Heist、Bounty、Knockout

### 与前批合并条目处理策略的差异（重要）

前批（第二批 Bea–Lola）对已有合并条目（`Bounty_or_Knockout`、`Brawl Ball_or_Hot Zone`、`Bounty/Knockout`）采取**保留**策略。本轮对两个含合并条目的英雄采取**拆分替换**策略：

- [[entities/brawlers/Juju|Juju]]：原 `Bounty_or_Knockout` 合并条目拆分为独立 `Bounty` 与 `Knockout`，并新增 `Gem Grab` 条目；合并条目被删除。
- [[entities/brawlers/Kaze|Kaze]]：原 `Bounty/Knockout/Heist` 三合一合并条目拆分为独立 `Heist`、`Bounty`、`Knockout`；合并条目被删除。

选择拆分而非保留的理由：Juju / Kaze 的合并条目仅是模式名拼接的占位，未承载独特 build/gadget 上下文（不像 Kit 的 Cheeseburger 变体说明或 Brock 的 Rocket No. 4 警告），拆分后信息无损且符合 one-entry-per-mode 约定。这一策略差异已记录在此，若后续全库治理决定统一为保留策略，需要把这两个英雄的独立条目重新合并并迁移到合并形式。

### 契约设计说明

- Heist 契约统一按"objective_damage 是近身/窗口型，不是稳定 race"建模；坦克/刺客/投掷型英雄均明确 `cannot_fulfill` 远程 safe race，并把主 DPS 列入 `needs_teammate_support`。
- Bounty / Knockout 契约区分"星差/首杀压力"与"首杀爆发"：长线 poke 型（Janet、Jessie）列为可提供 poke/信息但 `cannot_fulfill` 高爆发首杀；短手进场型（Hank、Jacky、Kaze、Kenji、Larry & Lawrie）明确 `cannot_fulfill` 开阔图正面输出，价值绑定到草墙/窄口/进场路线。
- `false_positive` 均指向该英雄最易被高估的能力（如 Hank 的身体≠进球、Janet 的空中免伤≠race 输出、Larry & Lawrie 的控区≠Larry 本体输出、Kaze/Kenji 的 mark/中心命中延迟）。

### 验证

逐页 Edit 后用 Python 脚本 `yaml.safe_load` 解析全部 8 页 fenced YAML，确认：8 英雄各含 6 个 Ranked 模式独立条目（无残留合并条目），所有 contract（新旧）五字段齐全，YAML 缩进与各页既有 `objective_contracts` 一致（4 空格基线）。

## [2026-08-13] batch-complete | 全排位模式适配性 contract 全量补齐完成

### 背景

承接同日 `incomplete_ranked_mode_coverage` 审计 blocker 上线，对全库 105 个英雄的 `objective_contracts` 执行全量补齐。起始状态：104/105 英雄缺至少一个排位模式的 contract，总缺口 303 个。

### 执行

分三批 14 组并行 agent 完成，共补齐约 303 个 `objective_contract`：
- 第一批（缺 1-2 模式）：34 英雄，约 67 contract
- 第二批（缺 3 模式）：51 英雄，约 153 contract
- 第三批（缺 4-6 模式）：19 英雄，约 83 contract（含 Mr. P 和 Ollie 从 0 补全部 6 模式）

每个 contract 基于英雄 `capability_vector`、`failure_modes`、`map_feature_hooks` 和地图 `required_capabilities` 独立评估产出，不依赖 PLP 推荐结论（PLP 推荐仅作反向验证）。负向/false_positive contract 计为有效覆盖。所有血量引用 Power 11 口径。部分英雄的历史合并条目（如 `Bounty_or_Knockout`）被拆分为独立模式条目。

### 最终验证

- 审计脚本：**105/105 英雄全部 6 模式覆盖，零 `incomplete_ranked_mode_coverage` blocker，105 个英雄零 blocker**
- 契约测试：`bp skill contract ok`
- Crystal Arcade compile：`mode_contract_hit=True: 105/105`，fit 分布 strong 47 / weak 58（均为已评估结论，不再有数据缺口造成的假 weak）


## [2026-08-14] synthesis | BP 强度层语义回归与高分选取率估计器讨论

### 背景

维护者要求评价"只精通 Emz / Spike / Rico 的强度与上分上下限"。初始回答误用了 iKaoss11 强度榜及其衍生的 `outputs/strength-profiles/ikaoss11-ranked-map-adapted-preview.json`"全图 C/D 矩阵"（该文件是 2026-07-07 `generate_map_strength_profile.py` 生成的机器底稿，日志注明"供后续人工审计和逐图细调"，非被采纳的评价体系）。用户纠正：强度榜无共识；Spike 反而是难被后手 counter 的先手 pick。

### 本轮结论（讨论中，未全部采纳）

- 强度 = 环境基线先验（base-rate prior），不是英雄属性；合法用途仅限同层 tie-break 与 ban/英雄池规划参考面。
- 估计器视角：tier list 是声明式估计器，高分选手 pick(+ban) rate 是揭示式估计器（与胜负有选择压力地因果耦合）；后者是强度层更合理的测量来源，但不能整体替代（合成数不可分解、补丁边界滞后、混入账号可用性、被赛季地图池污染）。
- 正确设计：强度层 = 多来源开放槽（专家榜 / 高分统计 / 用户调校三通道）+ 认识论元数据（consensus / recency / derived / status / rank_floor / window / sample_size / companion_ban_rate）。
- (pick, ban) 必须成对使用，二维对可表达"灵活安全先手 / 压制被争抢 / 冷门被忌惮"结构。
- 教训：强度会渗入每个"没有证据归属"的问题类——本轮的"上分泛用性/英雄池规划"是继地图适配（2026-07-07 已修复）后的第二次发作；该问题类应补证据契约（counter 抵抗性 + 覆盖广度 + 操作上限 + 账号状态为主驱动，强度仅做 patch relevance 检查）。

### 动作

- 新增 `wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md`（design_discussion_in_progress_non_runtime）。
- 更新 `wiki/index.md` 加入该页入口。
- 记录 4 个待决问题（强度层重定义 / 英雄池规划证据契约 / 高分粒度定义 / 生成底稿处理）。
- 架构修正评估与落地计划待维护者确认后执行（涉及 compile-knowledge.md、编辑器 schema、compile_runtime_index.py、测试与底稿治理）。

## [2026-08-14] refactor | BP 系统移除 strength/tier 层（减法方案落地）

### 决策

承接同日合成页讨论，维护者拍板减法方案：整个体系不再消费 strength，不保留 tier 概念；环境信号固定命名为 high-rank pickrate（与 ban rate 成对），数据槽当前为空，先改实现。feature 分支：`feature/brawlstar-remove-strength`。

### 代码变更

- `compile_runtime_index.py`：删除 strength profile 输入、tier/rank/score/proof_threshold、strength_context、avoid_without_proof 桶；manifest 记录 `pickrate_source: null` / `pickrate_status: empty`；候选排序仅由地图证据决定。
- `runtime_index_tools.py` / `query_runtime_facts.py` / `hydrate_runtime_facts.py` / `runtime_index_precheck.py`：删除 strength 字段、`strength_tier/rank`、`--strength-profile-*` 参数；manifest 校验改为 pickrate_status。
- 文档：`compile-knowledge.md`、`runtime-decision-knowledge.md`、slot-decision SKILL.md、run-brawl-stars-bp SKILL.md / match-report-schema / renderer、AGENTS.md、README.md、`BP-运行时索引编译架构.md` 同步重写。
- 契约测试：`test_bp_skill_contract.py` 增加减法红线（runtime 产物不得含 `strength_weight` / `strength_tier` / `strength_rank` / `strength_context` / `default-strength-profile` / `--strength-profile` / `ikaoss11-july-2026-screenshot` 等消费性 token）。

### 退役

- 删除 `skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json`。
- `wiki/sources/iKaoss11-July-2026-Strength-Profile.md` 标注 deprecated（保留历史）。
- `outputs/strength-profiles/`、`outputs/runtime-bp-index/strength-profile-with-nori.json` 及旧编译产物（default-tierlist-all-maps-thin / user-tuned / safe-zone-default / bsc-* / crystal-arcade-s47）移入 `outputs/_retired/`。
- `tools/strength-profile-editor/` 保留代码，README 与生成脚本标注退役，不进入 runtime 消费路径。

### 验证

- slot-decision 21 个 unittest 通过；bp skill contract 通过；maintenance 各脚本测试通过（含 test_plp_matchup_coverage 移除 --strength-profile 后修复）。
- 新索引 `outputs/runtime-bp-index/default-runtime-index.json`：30 图 / 105 英雄 / `pickrate_status: empty` / 候选层无 tier/rank。

### 待办

- pickrate 数据源调研与接入（高分粒度定义待决）；编辑器 UI 退役标注；`BP-下一阶段迭代方向决策记录` 待决问题待更新。

## [2026-08-14] decision | 环境信号数据源方案拍板

维护者确认（承接同日减法方案）：

- 高分定义 = **Legendary+**，段位限定不可让步。
- 数据源 = **Liquipedia 月赛**，每月单独统计 pick 与 ban（成对）；第三方高频抓取（Brawl Planet / BrawlPulse 等）不采用。
- ban 信息月度更新，**不写入英雄信息页**（与 esports-event-ingest 规则一致）。
- 聚合产物作为环境信号输入层（pickrate_source / pickrate_status），口径：`rank_floor: legendary_plus`、`window: monthly`、`companion_ban_rate: true`。
- 实施路径：复用 `ingest_liquipedia_event.py` + `outputs/esports/` 基建，月度输出成对 pick/ban 汇总；落地时写入 skill references。

动作：更新 `wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md`（待决问题 1-4 全部已决 + 新增"十一、数据源决定"）。

## [2026-08-14] ingest+draft | Brawl Planet Legendary+ pick 数据验证（修正数据源分工）

### 背景

维护者指出上一轮把"数据源 = Liquipedia 月赛"记错了：段位限定（Legendary+）不可让步指的是 **Brawl Planet 高分段 pick 抓取**为主源，月赛只负责 ban。已修正合成页"十一、数据源决定"。

### 抓取验证（全部实测）

- Brawl Planet 数据实为其 GCS 静态 JSON：`https://storage.googleapis.com/brawlanalyzer-public/pl-l1-results.json.gz`（`.gz` 为命名约定，实际明文 JSON；`pl-l1`=Legendary I+、`pl-m1`=Mythic I+、`pl-results`=Diamond+），无需 headless browser。
- 新增抓取脚本 `skills/brawl-stars-bp-knowledge-maintenance/scripts/fetch_brawlplanet_pickrate.py`（下载 pl-l1 + brawlers.json.gz，用 wiki 英雄页 canonical 名归一化，过滤 future 英雄，输出逐图 + 全局加权 use/win rate）。
- 新增月度聚合脚本 `skills/brawl-stars-bp-knowledge-maintenance/scripts/aggregate_environment_signal.py`（从 tournament_observation_profile.v1 聚合成对 pick/ban 信号）。
- 8 月（Season 6）EMEA Monthly Finals raw capture 已抓取（27 sets，revision 268338），analyze 出 observation profile。

### 信号质量

- Legendary+ pick 信号：33 图 / 29 active / **总样本 2,882,389 场** / 105 英雄全覆盖（名称归一化 0 失败）。Crystal Arcade（S47 featured 新图）单图 90,887 场。
- 7 月月赛 ban 信号：4 赛区 98 sets，89 英雄有样本。
- 合并视图交叉验证：高 use+高 ban（压制型）= Starr Nova/Max/8-Bit/Surge/Meg/Griff，**几乎全是 8/4 削弱名单**；高 use+低 ban（灵活安全先手）= Brock(26.7%/0%)/Pierce/Meeple/Stu/Rico/Edgar。印证"(pick, ban) 二维对"框架。

### 产物（outputs/，gitignored）

- `outputs/runtime-bp-index/environment-signal-pickrate-legendary-plus.json`
- `outputs/runtime-bp-index/environment-signal-2026-07.json`（月赛 ban 聚合）
- `outputs/runtime-bp-index/environment-signal-2026-08-emea.json`（8 月 EMEA 试点）
- `outputs/esports/bsc-2026-aug-emea-observation-profile.json`

### 待办

- 完整环境信号 schema（pick 层 + ban 层合并、窗口差异标注）待确认；进 runtime 前需复核提升。
- 8 月其余 3 赛区月赛页可探测后抓取。

## [2026-08-14] ingest | Brawl Planet 抓取方法论与首次执行结果沉淀

- 新增 `wiki/sources/Brawl-Planet-站点与数据接口.md`：站点与 GCS 静态 JSON 接口（`storage.googleapis.com/brawlanalyzer-public/pl-l1-results.json.gz` 等，`.gz` 为命名约定实为明文）、文件命名规律、数据结构（per-map `individual` 的 wr/ur/sr + match_count）、抓取方法论、首次执行结果（33 图/29 active/2,882,389 场/105 英雄全覆盖/Crystal Arcade 90,887 场）、边界（无 ban、10 周滚动窗口、不可 runtime 直消费）。
- 新增 `skills/brawl-stars-bp-knowledge-maintenance/references/environment-signal-ingest.md`：环境信号两层结构（pick=Brawl Planet Legendary+、ban=Liquipedia 月赛）、月度流程、字段口径、禁则（不写英雄页、不生成 tier、名称归一化、过滤 future 英雄）。
- `skills/brawl-stars-bp-knowledge-maintenance/SKILL.md` 登记新 reference；`wiki/index.md` 加入来源页入口。

## [2026-08-14] decision | 环境信号仅人类参考，不接入 BP 决策

维护者拍板（承接数据源方案）：
- 环境信号（Brawl Planet Legendary+ pick + 月赛 ban）**只作为人类参考**，先不接入 BP 决策；compile 的 `pickrate_status` 槽保持 `empty`，`decide` 不消费；看不清楚的事情保持模糊，不预支未来接入。
- 8 月（Season 6）其余赛区月赛**未比完，暂不抓取**；完整月度 ban 信号等当届打完再聚合。
- 更新 `wiki/syntheses/BP-强度层语义回归与高分选取率估计器.md`（新增"十二、落地边界"）与 `skills/brawl-stars-bp-knowledge-maintenance/references/environment-signal-ingest.md`（状态改为 human-reference only，去掉 promotion gate 预支）。

## [2026-08-14] audit+docs | BP 提升第一性论证：转录审计、三维证据协议、README 核心理念

维护者围绕"消除个人局限对体系影响"做了多轮双向钢人论证，结论：知识侧（事实与解释分层、机械忠实拆解、社区溯源）已到位，剩余杠杆在决策侧。落地三件事：

- **转录审计（抽查 12 英雄）**：PLP countersThese/counteredBy 16 对位 vs 页面 `conditional_matchups`/`conditional_matchup_seeds` 覆盖对照。结果：9 个 16/16 完美（Bolt/Griff/Brock/Bibi/Nori/Surge/Starr Nova/Meeple/Max），8-Bit 缺 Glowy、Ash 缺 Barley、Angelo 缺 Pearl/Ruffs/Lola（均为低选取率对位目标，低风险缺口）；部分页面有社区原文之外的 Fandom/合成增补条目。抽查脚本即兴执行，未落盘正式报告。
- **三维证据协议进 skill**：`skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md` 新增 "Evidence Roles and Confidence" 章节——月赛=低权重思路提示、传奇+=强度锚（10 周滞后标注）、机制=最高权重可行性约束，冲突裁决顺序机制→传奇→月赛；`turn_decision_trace` 加 `evidence_roles`（三维度状态+conflict_resolution+confidence），`bp_recommendation.uncertainty` 结构化（evidence_gaps/decisiveness_boundary/outcome_vs_decision_quality）；Common Mistakes 加"不声明证据维度"条目。`test_bp_skill_contract.py` 通过。
- **README 核心理念**：`README.md` 新增"核心设计理念"五条——事实与解释分层（混合函数刻意不明确）、决策质量可观测 vs 单局结果不可观测、证据累积式信心更新（三维证据等级表）、环境信号只校准不裁决、转录损失不在决策路径。

- 维护者决策补充：转录损失按 wiki 完备性任务治理（低优先级），不占决策预算；数据 vs 页面差异清单作为未来复核触发器候选，本次未实现。

## [2026-08-14] audit+fix | volatile 对位语义修复 + 全量补缺 PLP 对位（105 英雄 100% 覆盖）

承接上轮转录审计，维护者确认两件事必须做：volatile 语义在 compile 里被误当单向克制是真 bug；PLP 对位缺口按"最新版本 raw"口径全量补齐。落地：

- **volatile 语义修复（compile + query）**：`compile_runtime_index.py` 的 `compile_draft_edges` 与 `build_matchup_index` 原将 `direction: volatile`（含变体 `volatile_subject_favored`）归入单向 `answers`（我克谁），把"条件性双向"误报成"单向克制"喂给决策。修复：edge 带 `volatile: true` 标记存 answers（不复制 mechanism 文本），`query_runtime_facts.py` 的 `conditional_relations` 在查询时把 volatile 边展开为 outgoing + incoming 两条关系。函数级验证：Angelo↔Kit 从 0 条变 2 条（outgoing+incoming），Mandy 仍 1 条 incoming 未被误伤。涉及 22 个页面 24 处 volatile 条目。
- **全量补齐 PLP 对位缺口**：用 workflow 分发 4 个子代理合成 28 条缺失对位条目（方向来自 PLP 最新 raw，mechanism/active_when/fails_when/bp_use 基于各英雄页 capability_vector 合成），写入 15 个英雄页。13 页追加进 `conditional_matchup_seeds`；8-Bit/Rico 是 `conditional_matchups` 字段（bp_ready），先误建 seeds 导致 compile 优先读 seeds 跳过原 matchups（8-Bit runtime 边一度只剩 1 条），已修正为合并进 matchups 并删除 seeds 块，恢复且扩充（8-Bit 16 边、Rico 18 边）。
- **官方审计脚本口径修复**：`audit_plp_matchup_coverage.py` 两处 bug——(1) pair key 未归一化导致 Jae-Yong/Jae-yong 等大小写变体假阳性（63 条 plp_only 中 57 条是假）；(2) volatile 边在 index 只存 answers，审计把 PLP 的 is_answered_by 期望与 volatile 的 answers 比较产生假阳性。修复后按 normalize_key 比较、volatile 边同时计入两个方向。`test_plp_matchup_coverage.py` 重写：合成 fixture 验证缺口检测（plp_only=1 的 Glowy seed），真实数据测试断言 105 页全覆盖且 plp_only=0。
- **最终结果**：官方审计 `plp_pairs=1536, overlap=1536, plp_only=0`——105 个英雄、1536 条 PLP 对位边全部被 compile 后 runtime index 覆盖，零缺口。测试全绿：契约测试 + 维护 18 tests + slot-decision 21 tests。
- 遗留：audit 的 `compiled_pairs=1841`（含页面非 PLP 增补边，如 Fandom 来源），> plp_pairs 属正常；多版本 PLP raw（8-Bit/Bo/Brock/Max）由 `latest_plp_raw_paths` 正确取最新版，旧版不进对比。

## [2026-08-14] governance | 对位字段分类治理：非英雄 target 移出 + direction 白名单 + ally_synergy 归位

维护者指出：对位字段里混入了"另一类知识"（模式目标/召唤物/类型描述/队友配合），且 compile 对未知方向静默落 else（当"我克谁"），是消费方错误。做减法式治理（数据+审计+消费+文档四层同修）：

- **数据侧（22 个英雄页，31 条条目）**：`conditional_matchup_seeds` 中 25 条 ALL-NONHERO（Heist safe / Ball carrier / Zone holder / Open_map_snipers 等模式目标、类型描述、机制碎片）整体移除——这些是模式/目标维度知识，不属于英雄对英雄对位，且 query 按英雄名召回永远无法命中；5 条 MIXED 拆分为仅英雄 target（如 Pierce 的 `Mr_P_or_Jessie_or_Penny_or_spawnable_core` → `["Mr. P","Jessie","Penny"]`）；Meeple 1 条 `ally_synergy` 保留（队友配合是合理英雄页知识），target 从 `Thrower_or_Rico_teammate_combo` 修正为英雄列表 `["Dynamike","Barley","Tick","Larry & Lawrie","Rico"]`。
- **命名统一**：顺手修正 4 个页面的 `Larry_and_Lawrie` 拼写变体为 canonical `Larry & Lawrie`（Otis/Ruffs/Sirius/Spike）；全量扫描确认所有 target 均 normalize 到 canonical 英雄（0 残留）。`brawler-modeling.md` 明确：`conditional_matchups` 是唯一对位字段（`conditional_matchup_seeds` 为历史别名，勿混用）、target 只允许 canonical 英雄名、方向白名单 `subject_favored/target_favored/volatile/volatile_subject_favored`。
- **消费侧**：`compile_runtime_index.py` 的 `build_matchup_index` 加两层白名单——target 必须 normalize 到 roster 英雄（非英雄跳过 + warning）、direction 必须合法（未知/ally_synergy 跳过 + warning，不再静默当 answers）。结果：runtime index 从 1847 → 1782 条边，**0 条非英雄边**；Meeple 的 ally_synergy 不再进 answers。
- **验证**：官方审计 `plp_pairs=1536, overlap=1536, plp_only=0`（清理未破坏 PLP 英雄对位覆盖）；compile 警告从 65 → 1（仅 Meeple ally_synergy 预期跳过）；slot-decision 23 tests（新增 2 个：非英雄 target 过滤、未知方向过滤）、维护 3 tests、契约测试全绿。
- **模式维度去向**：模式/目标召回不加重英雄页负担，按维护者决策走环境信号层（Brawl Planet per-map 传奇+数据）承载，本页不承载。

## [2026-08-14] governance | volatile 消除为 win/fail 条件单向边 + conditional_matchup_seeds 收敛 + target 格式统一

维护者三项要求全部落地：

1. **`conditional_matchup_seeds` 收敛为 `conditional_matchups`**：62 页字段名统一（0 页同时使用两个），compile 删 seeds 优先分支只读 `conditional_matchups`，`ingest_brawler_bp_profiles.py` 模板字段同步（并删除违反方向白名单的 `direction: unknown` 空条目回退块），`brawler-modeling.md` 明确 seeds 为已合并历史别名禁止再引入。
2. **volatile 消除（消费端提权修复）**：23 条 volatile 条目全部移除并转化为标准单向边——按 PLP 锚定方向优先（17 条），无 PLP 锚定按机制倾向判断（6 条），组内方向混合的按 target 拆分（Eve/Gus/Nita/Sandy/Shade）。转化保留每条完整 `active_when`（win 条件）+ `fails_when`（fail 条件），实现"win/fail 条件应对关系边"。消费端：compile 方向白名单只剩 `subject_favored/target_favored`，volatile/ally_synergy/未知一律跳过+warning 不再静默当 answers；query 删 volatile 双向展开；audit 删 volatile 双向计数。`brawler-modeling.md` 记录 volatile 移除理由（避免对不恰当角色提权）。
3. **target 格式统一**：85 条 `_or_` 字符串 + 1 条裸串全部转换为标准双引号列表 `["canonical", "name"]`，修正 `Larry_and_Lawrie` 等拼写变体为 canonical（Otis/Ruffs/Sirius/Spike）。全量验证：所有 target 均为双引号列表且 normalize 到 canonical 英雄（0 残留）。

- **验证结果**：官方审计 `plp_pairs=1536, overlap=1536, plp_only=0`（volatile 移除曾暴露 45 条方向缺口，全部经拆分转化恢复覆盖）；compile 警告仅 1 条（Meeple ally_synergy 预期跳过）；slot-decision 23 tests、维护 3 tests、契约测试全绿。

## [2026-08-14] runtime | 环境信号升级为三维决策证据（decide 按需查询，不进 compile）

维护者认知升级：机制事实层已完备，月赛/传奇+数据是"更新佐证"而非污染源，因此"环境信号仅人类参考"的保守定位让位于三维证据判断框架——证据强度随数据迭代变化，但框架本身不变。落地：

- **新增 `skills/brawl-stars-bp-slot-decision/scripts/query_environment_evidence.py`**：decide 按需查询环境证据的只读工具。`--hero X [--mode M] [--map MAP]` 返回传奇+强度锚（全局 ur/wr + 按模式/地图过滤的 per-map）+ 月赛 ban 层（pick/ban/win_rate_when_picked + 分母），带 window/rank_floor/fetched_at 标注；无样本时返回 `no_ladder_sample` / `no_monthly_sample`。不排名、不生成建议、不改 fit/eligibility。
- **`runtime-decision-knowledge.md`**：Evidence Roles and Confidence 章节升级为真实执行流程——三维证据表加入检索工具列（月赛=低权重提示、传奇+=强度锚带滞后标注、机制=最高权重约束）；LLM Decision Pipeline 新增第 9 步（高 stakes slot 4-6 / 争议开局时查询环境证据）；`evidence_roles` 字段取值更新（ladder_anchor 支持 supporting/contradicting/no_ladder_sample，monthly_finals 支持 hint/corroborating/contradicting/no_monthly_sample）；Common Mistakes 新增"凭记忆背选取率"和"小样本当锚"两条；样本量诚实规则（ur<2% 或月赛 picks<5 为轶事级）。
- **`SKILL.md`**：decide Read 列表登记 `query_environment_evidence.py`，标注"佐证证据、绝非排名或指令"。
- **`compile-knowledge.md` / `environment-signal-ingest.md` / `README.md`**：同步从"仅人类参考/空槽/不进 decide"改为"三维决策证据、decide 按需查询、compile 仍保持 empty"；README 架构图环境信号流向 decide（虚线按需查询），不进 compile。
- **边界不变**：数据永进 compile（compile 只产稳定事实）、不生成 tier、不改 fit/eligibility、不推翻机制约束；证据强度迭代只更新 confidence 不改变框架。契约测试新增 `query_environment_evidence.py`/`ladder_anchor`/`monthly_finals`/`no_*_sample`/`evidence_roles` 断言。
- **验证**：工具端到端（Griff 全局 ur 29.4%/wr 49.5% + 逐图；Starr Nova 三维齐备：ur 19.6%/wr 52.7%/月赛 ban 55.6%）；契约测试 + slot-decision 23 tests + 维护 3 tests 全绿。

## [2026-08-14] runtime | confidence 规则修正：机制强度独立于环境样本评估

维护者指出框架的结构性偏差：文档原规则 "Mechanism-only (no ladder sample, no monthly presence) → low confidence; theory pick" 用"环境维度齐全度"绑架了机制证据强度——新英雄/冷门特化/刚补丁英雄（环境样本天然缺失）会被结构性压成 low，而这恰恰是机制独立思考价值最高的场景。

修正（`runtime-decision-knowledge.md`）：
- 新增 "Mechanism Strength Is Judged Independently of Environment Samples" 小节：机制强度分 strong（地图专属 hook + 显式对位边 + 失败门不激活）/ medium / weak 三档，独立评估不看环境样本；环境佐证只在一定范围内调节 confidence，不决定机制是否成立。
- 环境缺失从"负面证据"改为"中性缺失"：机制 strong + 环境双缺 → medium（`environment_unverified` 标注）而非 low theory pick。
- confidence 矩阵：strong+全齐=high / strong+缺一或双缺=medium / medium+薄=medium-low / weak 或证据不足=low。
- `evidence_roles` 更新：mechanism 取值为 strong|medium|weak + mechanism_basis（依据：hook/关系边/失败门）+ environment_unverified 标记；confidence 增 medium-low 档。
- 这使文档的 confidence 规则与"机制约束 > 传奇+锚 > 月赛提示"的裁决顺序重新一致（此前裁决顺序说机制最高、confidence 分级却惩罚机制-only）。

## [2026-08-14] judge | 裁判 turn prompt 模板规范化：输入层=对局信息，零思考引导，可独立交付

维护者指出：此前裁判（本 agent）在 spawn subagent 时在 prompt 里塞了大量思考引导（"先读 X 章节""查 Y bucket""你需要应对 Z""你的反制池还剩..."），把 decision skill 该自己做的推理替做了，导致每手查询冗余、思考冗长、决策质量未提升。且决策 skill 的架构原则是"上下文输入只有对局信息一层，其余全部 skill 自主查询"。

落地：
- 新增 `skills/run-brawl-stars-bp/references/turn-prompt-template.md`（canonical 模板，160 行）：
  - spawn prompt（ban 阶段）与 pick-turn prompt 两个可复制模板，只填 `对局信息` 块（地图/模式/阵营/策略偏置/本手/已ban/不可用池/已选/runtime index/环境工具）
  - "What the judge must never add" 清单：禁止加策略提示、查询建议、对手分析、推理引导、上手的对方 trace
  - 精简输出契约：decision / mechanism / evidence / evidence_roles / confidence / conflict / bias_effect / rejected / retrieval 九字段（trace 瘦身，审计友好）
  - Judge operation steps（独立可跑：准备 index → match config → spawn → ban 合并 → 严格 pick 顺序 → final review → 报告）
  - 完整 worked example（蓝方 ban 阶段完整 prompt）
- `run-brawl-stars-bp/SKILL.md` Turn Prompt Contract 重写：强制使用 canonical 模板、只填对局信息块、声明"输入层=对局信息、其余 skill 自主检索"。
- 契约测试新增 JUDGE_TURN_TEMPLATE 校验（模板存在 + 含对局信息/输出契约/不可用池/evidence_roles/bias_effect/never-add 清单/操作步骤等 9 词）。
- 验证：契约测试 + slot-decision 23 tests 全绿。
- 交付性：模板不依赖任何会话上下文，陌生裁判按 Judge operation steps + 模板即可复现相同流程。

## [2026-08-21] run | 裁判 skill 跑 1 局 Crystal Arcade（Gem Grab）BP 模拟

- 按 `skills/run-brawl-stars-bp` 裁判流程跑 1 局排位 BP：Crystal Arcade（Gem Grab，S47 featured）。用户要求双方策略不同：蓝方 `aggressive` vs 红方 `conservative`（使用 `assign_strategy_bias` 随机分配并保证不同）。
- 蓝/红各 1 个 match-scoped player subagent 贯穿整局（ban → 4 个 pick turn → final review），复用 `send_message` 续轮，不跨局复用；裁判只传公开 picks/bans/unavailable pool，不传他方隐藏推理。
- runtime index 直接复用已编译的 `outputs/runtime-bp-index/default-runtime-index.json`（manifest 覆盖 Crystal Arcade，`pickrate_status=empty`，precheck ready），未重新 compile。
- 禁用阶段（simultaneous，互不可见）：蓝方 ban `Griff`/`Emz`/`Charlie`；红方 ban `Griff`/`Crow`/`Stu`；重复 ban：`Griff`。不可用池：Griff/Emz/Charlie/Crow/Stu。
- 选择：蓝1 `Bo` → 红2-3 `Meeple`+`Ash` → 蓝4-5 `Otis`+`Mortis` → 红6 `Pearl`。最终阵容：蓝 `Bo/Otis/Mortis` vs 红 `Meeple/Ash/Pearl`。
- 逐局完整报告与 decision log 写入 `outputs/bp-simulations/match-crystal-arcade.md` 与 `match-crystal-arcade.decision-log.md`（临时运行产物，按 2026-07-01 cleanup 约定不进 wiki syntheses）；本局关键结论如需沉淀再单独提炼。

## [2026-08-21] tooling | 项目内 skill 注册修复：DSH 项目根判定

- 问题：`scripts/register-skills.sh` 把三个 BP skills 软链到 `brawlstar/.dsh/skills/` 后，新会话仍找不到——根因是 DSH `dsh-skill-filesystem` 的 `findProjectRoot(cwd)` 从 cwd 向上找最近含 `.git` 的祖先作为项目根，再扫描 `<项目根>/.dsh/skills`。本仓库位于无 `.git` 的 vault 内（git 根在上级 `vaults/`），DSH 把项目根判定为 `vaults/`，永远扫不到 `brawlstar/.dsh/skills`。
- 修复：在仓库根创建 gitlink 文件 `.git`（内容 `gitdir: ../.git`），使 `findProjectRoot` 从 brawlstar 向上第一层即命中；git 本身支持该文件形式（同 submodule）。同时 `register-skills.sh` 新增 `ensure_dsh_project_root_marker()` 自动创建该标记，并把 dsh 注册扩展为双路径：`.dsh/skills/`（rank 100）+ `.agents/skills/`（rank 200，与用户根 `~/.agents/skills` 同源更稳）。
- 验证：skill 目录已出现 `brawl-stars-bp-knowledge-maintenance`、`brawl-stars-bp-slot-decision`、`run-brawl-stars-bp` 三项，`skill` 工具可正常加载（base dir 指向 `brawlstar/.dsh/skills/<name>`）。三个 BP skills 现可在本仓库任意新会话中被 DSH 发现并使用。

## [2026-08-21] ingest+synthesis | 新建 Ranked Season 48 地图池索引并标记 Season 47 过期；补齐三张缺图

- 确认当前赛季为 Season 48（2026-08-20 起），featured 模式从 Season 47 的 Gem Grab 切换为 Brawl Ball；Trial Brawlers 锚点 `#48 | August 20, 2026 | Trunk, Willow, Kaze | Brawl Ball`。来源：Fandom Ranked 页 "Active maps (Season 48)" 表（MediaWiki API，revid 217144，2026-08-21T00:23:29Z）。
- S48 地图池：6 模式 30 张图（Gem Grab 6 / Heist 6 / Bounty 4 / Brawl Ball 6 / Hot Zone 4 / Knockout 4）。与 S47 差异：Brawl Ball +2（`Beach Ball`、`Spiraling Out`），总图数 28 → 30；Gem Grab 失去 featured 后保留 6 张图（与 Heist S46→S47 行为一致）。
- 新增 raw：`raw/sources/fandom/maps/ranked-season-48-map-extracts-2026-08-21.md`（compact manifest，含池表、S48 vs S47 diff、Trial Brawlers 锚点、编号冲突说明）+ `beach-ball-2026-08-21.md`、`spiraling-out-2026-08-21.md`、`rustic-arcade-2026-08-21.md` 三张 per-map raw capture（含 revision 元数据）。
- 新增 source 摘要：`Fandom-Ranked-Season-48-Map-Pages.md`、`Fandom-Beach-Ball.md`、`Fandom-Spiraling-Out.md`、`Fandom-Rustic-Arcade.md`。
- 新增地图实体页（`bp_map_profile_v2`）：`wiki/entities/maps/Beach Ball.md`、`Spiraling Out.md`、`Rustic Arcade.md`。Spiraling Out 因 Fandom Tips 为空，实体页只写结构层结论并显式声明低证据；Rustic Arcade 关闭 Season 47 页标记的"待 ingest 缺口"。
- 新增 `wiki/syntheses/Ranked-Season-48-地图Map-Profile总览.md`（当前赛季索引）；`Ranked-Season-47-地图Map-Profile总览.md` 顶部加过期标注并指向 S48，Rustic Arcade 缺口条目更新为已补齐；`wiki/index.md` 同步赛季行、地图实体列表与来源列表。
- 编号说明：单地图页 History 使用另一套赛季编号（2026-08-20 条目写作 "Season 30 Ranked"），与 Ranked 页 "Season 48" 并存；本库以 Ranked 页编号为准，已写入 raw manifest 与来源页。
- 后续动作：Season 48 地图池落盘后需重新编译 `outputs/runtime-bp-index/default-runtime-index.json`，使三张新图进入可查询稳定层（见 runtime 条目）。

## [2026-08-21] runtime | Season 48 地图池落盘后重编译 default runtime index

- 判断：runtime index 由稳定实体页编译（`wiki/entities/maps/` + `wiki/entities/brawlers/`），不读赛季索引。Season 48 落盘新增 3 张地图实体页（Beach Ball / Spiraling Out / Rustic Arcade），稳定事实层发生变化，`decide` 要能查询新池内图，必须重编译 `outputs/runtime-bp-index/default-runtime-index.json`。旧索引编译于 2026-08-14（S48 开始前），不覆盖新图。
- 执行：`compile_runtime_index.py --repo . --output outputs/runtime-bp-index/default-runtime-index.json`。manifest 更新：`map_pool_id` 30 -> 33 张、`compiled_at` 2026-08-21；`pickrate_status=empty`、`missing_inputs=[]` 不变；仅 1 条已知 Meeple ally_synergy 警告。
- 验证：新索引 33 张图，三张新图 candidate_index 各 105 英雄；`query_runtime_facts.py` 对 Beach Ball / Rustic Arcade 冒烟通过（hook 经能力 token 匹配命中，如 Brock goal_wallbreak、Bo bush_vision、Charlie gem_carrier_cocoon 等）；fit 分布与既有地图同量级（Beach Ball 53/105、Spiraling Out 59/105、Rustic Arcade 41/105 strong，对照 Triple Dribble 65、Safe Zone 29、Undermine 1）；契约测试通过。
- 顺带修正：26 张旧地图实体页"当前赛季索引"导航链接从 Season 46 批量更新到 Season 48（S47 落盘时遗漏）；来源行保持指向 S46 source 页不变。

## [2026-08-21] run | 裁判 skill 跑 1 局 Out in the Open（Knockout）BP 模拟

- 按 `skills/run-brawl-stars-bp` 裁判流程跑 1 局排位 BP：Out in the Open（Knockout，S48 池内既有图）。用户要求双方策略不同：蓝方 `aggressive` vs 红方 `conservative`。
- 蓝/红各 1 个 match-scoped player subagent 贯穿整局（ban → 4 个 pick turn → final review），复用 `send_message` 续轮，不跨局复用；裁判只传公开 picks/bans/unavailable pool，不传他方隐藏推理。
- runtime index 复用已编译的 `outputs/runtime-bp-index/default-runtime-index.json`（2026-08-21 重编译，33 图覆盖 Out in the Open，`pickrate_status=empty`，precheck ready），未重新 compile。
- 禁用阶段（simultaneous，互不可见）：蓝方 ban `Brock`/`Pearl`/`Mandy`；红方 ban `Brock`/`Angelo`/`8-Bit`；重复 ban：`Brock`（双方均刻意 deny，镜像非重叠浪费）。不可用池：Brock/Pearl/Mandy/Angelo/8-Bit。
- 选择：蓝1 `Piper` → 红2-3 `Nani`+`Gene` → 蓝4-5 `Max`+`Gus` → 红6 `Carl`。最终阵容：蓝 `Piper/Max/Gus` vs 红 `Nani/Gene/Carl`。
- 逐局完整报告与 decision log 写入 `outputs/bp-simulations/match-out-in-the-open.md` 与 `match-out-in-the-open.decision-log.md`（临时运行产物，按 2026-07-01 cleanup 约定不进 wiki syntheses）；本局关键结论如需沉淀再单独提炼。

## [2026-08-21] skill | 裁判/选手 BP 输出契约改为"精简返回 + 选手日志"两通道

- 动机：跑 Out in the Open 模拟时发现每手 decision 输出过重——每手 trace 1-3KB，其中 `examined_options`（每条含 why_examined/evidence_used/verdict_reason）占 60-70%，且每手重复写叙述；这些"记日志+总结理由"占每手生成时间与 token 的大头。用户要求：单手下发要简略清晰、最小化上下文（跑得快），详细思考过程记在选手自己日志里，裁判最后分别读双方日志给详细 verbose decision log。
- 改动（`skills/run-brawl-stars-bp/references/turn-prompt-template.md` + `SKILL.md` + `references/match-report-schema.md`；`skills/brawl-stars-bp-slot-decision/SKILL.md` + `references/runtime-decision-knowledge.md`）：
  - 决策阶段每手只回 `decision` + `key_reason`（每项一句最强依据）+ ban 加一行 `side_asymmetric_ban_strategy` + `confidence` + `retrieval`（一行）；不再展开未选理由，上下文最小化。
  - 每手详细思考过程（查验了哪些选项、每项为什么被查、关键证据、查验结果排序 ranking、verdict、被否决/推迟项，可含 evidence_roles / bias_effect）【追加】写入选手 side-local 日志 `{PLAYER_LOG_PATH}`（裁判 spawn 时分配，如 `outputs/bp-simulations/match-<map>.blue.player-log.md` / `...red.player-log.md`），每手 append 不覆盖。
  - 裁判整局结束后分别读取双方日志，据此组装详细 `.decision-log.md`；日志缺失标 `player_log_missing`，不重建。final_draft_review 仍返回获胜条件/打法/风险/配装，并追加到日志。
  - standalone 单手 BP（slot-decision 自带 decide）仍返回完整 `turn_decision_trace` + `examined_options`；match-scoped 走精简契约 + 选手日志，二者在 slot-decision SKILL.md 中显式区分。
- 验证：`test_bp_skill_contract.py` 通过（模板含 对局信息/输出契约/不可用池/strategy_bias/evidence_roles/bias_effect/never-add/Judge operation steps/visible_state_only_between_players 等契约词，新增 选手日志/PLAYER_LOG_PATH/player_log_missing/ranking）；slot-decision 23 tests 全绿。

## [2026-08-21] cleanup | runtime-bp-index 目录清理：死锁与一次性产物

- 用户确认清理 `outputs/runtime-bp-index/` 历史遗留：
  - 删除 5 个无对应索引的死锁（`rt-final.lock`、`safe-zone-current.lock`、`safe-zone-heist-final.lock`、`belles-rock-knockout-blue-v1.lock`、`crystal-arcade-s47-gg.lock`，均为 2026-08-20~21 一次性 decide/compile 实验遗留，`state: compiling` 但 `<key>.json` 均不存在；同名旧索引 crystal-arcade-s47.json 已在 `outputs/_retired/`）。
  - `environment-signal-2026-08-emea.json`（8 月 EMEA 试点月赛层，非任何脚本默认）归档至 `outputs/_retired/environment-signal-2026-08-emea.json`；原始聚合输入保留在 `outputs/esports/bsc-2026-aug-emea-observation-profile.json`，可随时重新聚合。
  - 删除 `ranked-s48-pool.json`（本会话"理解版本"用 S48 30 图快照，无脚本消费，被 33 图 default 索引覆盖）。
- 剩余 3 个在用文件：`default-runtime-index.json`（运行时主索引）、`environment-signal-pickrate-legendary-plus.json` 与 `environment-signal-2026-07.json`（query_environment_evidence.py 的两个默认证据层）。

## [2026-08-21] run | 裁判 skill 跑 1 局 Beach Ball（Brawl Ball）BP 模拟

- 按 `skills/run-brawl-stars-bp` 裁判流程跑 1 局排位 BP：Beach Ball（Brawl Ball，Season 48 新增图，S48 featured 模式）。用户要求双方策略不同且地图选 48 赛季新图：蓝方 `aggressive` vs 红方 `conservative`。
- 蓝/红各 1 个 match-scoped player subagent 贯穿整局（ban → 4 个 pick turn → final review），复用 `send_message` 续轮，不跨局复用；裁判只传公开 picks/bans/unavailable pool，不传他方隐藏推理。
- runtime index 复用已编译的 `outputs/runtime-bp-index/default-runtime-index.json`（2026-08-21 重编译，33 图覆盖 Beach Ball，`pickrate_status=empty`，precheck ready），未重新 compile。
- 禁用阶段（simultaneous，互不可见）：蓝方 ban `Brock`/`Griff`/`Amber`；红方 ban `Brock`/`Amber`/`Bo`；重复 ban：`Brock`、`Amber`（双方均刻意 deny/保护，镜像非重叠浪费）。不可用池：Brock/Griff/Amber/Bo。
- 选择：蓝1 `Damian` → 红2-3 `Frank`+`Janet` → 蓝4-5 `Emz`+`Bull` → 红6 `Lou`。最终阵容：蓝 `Damian/Emz/Bull` vs 红 `Frank/Janet/Lou`。
- 逐局完整报告与 decision log 写入 `outputs/bp-simulations/match-beach-ball.md` 与 `match-beach-ball.decision-log.md`（临时运行产物，按 2026-07-01 cleanup 约定不进 wiki syntheses）；双方选手日志 `match-beach-ball.{blue,red}.player-log.md` 保留完整 examined_options 审计；本局关键结论如需沉淀再单独提炼。

## [2026-08-21] architecture | 环境信号归档层 + compile 折叠：消除 maintenance 与 slot-decision 的目录/文件名耦合

维护者拍板架构转向（承接 2026-08-14 环境信号方案），目标是让"抓 esports 数据 → 生成 runtime index"收敛为单向数据流：maintenance 只写持久归档，compile 是唯一聚合点，decide 只消费索引内嵌证据。

- **新增持久归档层 `wiki/environment/`**（git 跟踪，知识库一部分，不在 gitignored `outputs/`）：
  - `2026-07/observation-profile.json`（四赛区 canonical，由原 `outputs/esports/bsc-2026-july-four-regions-observation-profile.json` 迁入；7-13 两赛区初版为其严格子集，迁至 `outputs/_retired/`）
  - `2026-07/environment-signal.json`（月赛 pick/ban 聚合，由原 `outputs/runtime-bp-index/environment-signal-2026-07.json` 迁入）
  - `2026-08/observation-profile.json`（8 月 EMEA，revision 268338；当月其余赛区未打完，暂不聚合 signal）
  - `pickrate-legendary-plus.json`（Brawl Planet Legendary+ 快照，由原 `outputs/runtime-bp-index/environment-signal-pickrate-legendary-plus.json` 迁入）
  - `current.json`（`environment_archive_pointer.v1` 指针）+ `index.md`（归档索引与 provenance 表格）
- **`compile` 成为环境信号唯一聚合点**（`compile_runtime_index.py`）：默认读 `wiki/environment/current.json`，折叠 per-brawler `environment_evidence`（`ladder_anchor` / `monthly_finals`，带 window / rank_floor / fetched_at / captured_at 标注）+ `environment_ladder_per_map` 进索引；manifest 新增 `pickrate_status: loaded|empty`、`environment_provenance`（指针、归档月、窗口、样本分母），`source_hash` 纳入信号内容。`--no-environment` / `--environment-manifest` 可覆盖。
- **`runtime_index_precheck.py` 不再硬编码 `empty`**：默认从 `wiki/environment/current.json` 解析期望 `pickrate_status`（与 compile 一致，调用方无需感知信号状态）。
- **`hydrate_runtime_facts.py` 透出内嵌证据**：per-entity `environment_evidence` + 当前图 `environment_ladder`（按请求英雄投影）。
- **`query_environment_evidence.py` 完全退役**（删除脚本与全部引用）；decide 只经 query/hydrate 读索引。
- 文档同步：AGENTS.md（目录速查、层级表新增环境归档层、单向同步规则、esports 段落、"wiki/ 为 Markdown"例外）、`compile-knowledge.md`、`runtime-decision-knowledge.md`、slot-decision SKILL.md、`environment-signal-ingest.md`、`esports-event-ingest.md`、`audit-and-validation.md`、`source-ingest.md`、run-brawl-stars-bp turn-prompt-template、README 架构图、`wiki/environment/index.md`、`wiki/index.md`、两篇 syntheses（落地边界、运行时索引编译架构）、Brawl Planet 来源页、维护 SKILL.md 与脚本 docstring。
- 测试与验证：契约测试通过；slot-decision 24 tests（新增 `test_manifest_folds_environment_signal_from_archive`，空槽测试改用 `--no-environment`，体积阈值按实测上调）全绿；maintenance 15 tests 全绿；`default-runtime-index.json` 重编译：`pickrate_status=loaded`、provenance 记录 2026-07 月赛 + 2026-08-14 ladder、105 卡 / 33 图 / 33 图 ladder 行、零 missing input。

## [2026-08-24] ingest | 补齐 BSC 8 月（Season 6）其余三赛区月赛并刷新环境信号

按 `environment-signal-ingest.md` 月度流程执行（8 月四赛区现已全部打完）：

- **抓取**：Liquipedia MediaWiki API 新增 South America（rev 269181 / 27 sets）、East Asia（rev 269178 / 27 sets）、North America（rev 269180 / 29 sets）三份 revision-specific raw capture；与既有 EMEA（rev 268338 / 27 sets）构成 8 月四赛区全集。当月 4 赛区全部打完、零弃权（EMEA FUT Esports、South America LOUD、East Asia Crazy Raccoon、North America Tribe）。
- **ingest**：为四赛区补齐 source summary 与 event entity（8 月 EMEA 此前只有观察产物、缺来源页/实体页，本次补齐）。
- **analyze**：重建 `wiki/environment/2026-08/observation-profile.json` 为四赛区 canonical（28 series / 110 sets / 88 英雄 global 观察），完整覆盖 2026-08-14 的 EMEA-only 版。
- **aggregate**：新增 `wiki/environment/2026-08/environment-signal.json`（28 series / 110 sets / 88 英雄；ban 前列 Bolt 53.6%、Lumi 46.4%、Max 39.3%、Meg/Starr Nova 32.1%）——8 月 EMEA 试点期"当月未打完不聚合"的待办就此关闭。
- **排位层刷新**：`fetch_brawlplanet_pickrate.py --tier l1` 更新 `wiki/environment/pickrate-legendary-plus.json`（fetched 2026-08-24，105 英雄 / 33 图；ur 前列 Griff 28.9%、Brock 26.9%、Surge 23.3%、Max 21.0%、Meg 20.5%）。
- **指针与索引**：`current.json` 切到 `2026-08`；`wiki/environment/index.md` 归档表与 provenance 更新；重编译 `outputs/runtime-bp-index/default-runtime-index.json`（`pickrate_status: loaded`，provenance 记录 2026-08 月赛 + 2026-08-24 ladder；105 卡 / 33 图 / 零 missing）。
- **知识缺口审计**：`outputs/esports/bsc-2026-aug-knowledge-gap-audit.md` 共 60 条 review seeds（`observed_without_concrete_map_fit`，需 VOD/draft-context 复核）+ 1 条 `missing_brawler_entity: Glowbert`（maintenance_blocker，不自动建页，待来源 ingest 单独处理）；均不自动升级实体或 runtime。
- 收尾：`wiki/index.md` 加入 8 月四赛区来源页入口。

## [2026-08-24] cleanup | 英雄改名归一化：Glowbert → Glowy 统一，未知名显式告警

审计发现 8 月 profile 出现 `missing_brawler_entity: Glowbert`。排查确认是**改名 + alias 拼写错误**叠加：

- **改名事实**：Glowbert 是 Glowy 的曾用名，Liquipedia 东亚月赛页（7 月、8 月）沿用旧名 `Glowbert`，其余赛区用 `Glowy`，导致同一英雄在 profile 里分成两条。
- **拼写错误根源**：`wiki/concepts/英雄名称归一化.md` 的 Glowy 段已有 alias `"Clowbert"`（C 开头，未覆盖实际出现的 Glowbert）。
- **修复**：
  - YAML Glowy 段注册 `"Glowbert"`（保留 `"Clowbert"` 变体，注明曾用名关系）。
  - `_liquipedia_event.py`：`canonicalize_brawler` 对未注册名字打印 `warning: unrecognized brawler name`（去重、stderr）；新增 `renormalize_event_names()`。
  - `analyze_esports_event.py`：聚合前按**当前**归一化规则重新映射名字（raw 保持不可变，alias 修复后重跑即生效；未知名显式暴露，不再静默歧义）。
- **产物重建**：7 月与 8 月 observation-profile / environment-signal 重新生成——Glowbert 全部合并进 Glowy（8 月 Glowy 6 picks / 7 月 11 picks，无 Glowbert 残留）；重编译 `default-runtime-index.json`（`monthly_finals.picks=6` 等）；重跑审计，`missing_brawler_entity: Glowbert` 消失，剩余 60 条 review seeds 不变。
- **验证**：`test_liquipedia_event.py` 5 tests（补 `import sys` 修复告警路径）、slot-decision compile 11 tests（折叠测试 archive_id 断言更新为 2026-08）、契约测试全绿；未知名字告警实测生效（`Zedbert` 触发 warning 且返回原名，审计仍可兜底暴露）。
- 规则补充：`esports-event-ingest.md` 写明 analyze 按活规则重映射 + 未知名告警；今后改名字一律走 `英雄名称归一化.md` 单一别名表，禁止脚本本地第二份表。

## [2026-08-24] architecture | 环境归档存储层迁移：JSON → SQLite 行列库

维护者拍板：环境/观察数据从嵌套 JSON 迁移到本地可读的 db 格式（可迁移、供其它应用访问、行列数据），读取时再展开成结构数据。

- **新增 `skills/brawl-stars-bp-knowledge-maintenance/scripts/_environment_sqlite.py`**（schema `PRAGMA user_version = 1`）：
  - 月度 `archive.sqlite3`：`event`（source_events 平铺）、`metric_global/mode/map`（scopes 聚合）、`series`/`set`/`set_pick`/`set_ban`（逐 set 行列，来自 raw 解析，含 winner/score/vod 等完整字段）、`signal_brawler`（月赛信号）、`meta`（schema/策略/provenance）。
  - 滚动 `pickrate.sqlite3`：`ladder_global` + `ladder_per_map`（`source_key` 保留 GCS 原始 key，含 `Safe Zone` / `Safe(r) Zone` 变体）。
  - 读函数 `load_profile` / `load_signal` / `load_pickrate` / `read_raw_events`：把行展开成与原 JSON 完全等价的 Python 结构（round-trip 测试逐字段验证）；同样接受 `.json` 路径，向后兼容。
- **生成脚本加 `--db`**：`analyze_esports_event.py`、`aggregate_environment_signal.py`、`fetch_brawlplanet_pickrate.py` 直接写 sqlite；`--output` 保留为可选 JSON 导出（人类审查 / git diff）。
- **读层适配**：`compile_runtime_index.py` 的 `resolve_environment` 内联 sqlite 读取（按 meta 键判别 signal/ladder，避免空表误判；自包含不跨 skill import）；`audit_tournament_observations.py` 与 `aggregate_environment_signal.py` 走 `envdb.load_profile`。
- **指针**：`current.json` 的 `monthly.db` / `ladder` 指向 sqlite；compile 兼容新旧键名。
- **迁移**：7 月 / 8 月 `archive.sqlite3`（含逐 set 行列）+ `pickrate.sqlite3` 生成；旧 JSON（observation-profile / environment-signal / pickrate-legendary-plus）删除。
- **体积**：月度 archive ≈ 185 KB（原 JSON ≈ 800 KB，省 ~4 倍）；pickrate ≈ 500 KB（行列展开 + PK 索引的固有开销，略大于紧凑 JSON，换取外部应用可 SQL 查询；极限压缩仍可用 gzip）。
- **测试**：新增 `test_environment_sqlite.py`（3 tests：profile/raw-events/signal/pickrate 完整 round-trip + SQL 查询示例 + Safe(r) Zone 变体保留）；契约测试、liquipedia 5 tests、slot-decision 24 tests 全绿。
- **文档**：`wiki/environment/index.md`（存储格式/目录/维护命令）、`environment-signal-ingest.md`、`esports-event-ingest.md`、`audit-and-validation.md`、`compile-knowledge.md`、`AGENTS.md`（目录职责/层级表/Markdown 例外）、`BP-运行时索引编译架构.md`、Brawl Planet 来源页、fetch/aggregate docstring 全部同步 sqlite。
- 重编译 `default-runtime-index.json`（`loaded`，provenance 指向 archive.sqlite3 / pickrate.sqlite3）；hydrate 端到端验证（Bolt ban 53.6%、Max ban 39.3%、Glowy picks 6 均来自 sqlite 折叠）。

## [2026-08-24] architecture | 环境归档 sqlite 协议化：统一生产侧与消费侧读取

维护者指出：sqlite 数据格式应作为**协议**统一生产侧与消费侧，而不是各自维护解析逻辑。此前 compile 为保持 skill 自包含而内联复制了一份展开代码，存在 schema 演进漂移风险。

- **协议单一实现**：`_environment_sqlite.py` 作为唯一实现，新增 `EnvironmentProtocolError`、`PROTOCOL_TABLES`（13 张协议表）、`META_KEY_PREFIXES`；`connect()` 加 **user_version 守卫**——已存在库的 `user_version` 既非 0 也非 `SCHEMA_VERSION` 时拒绝打开（消费侧不得猜测未知布局）。
- **compile 安装协议**：删除 `compile_runtime_index.py` 的内联 `_read_environment_signal`（约 60 行复制），改为 `_environment_protocol()` 经 repo 相对路径动态 import 共享模块，用 `load_signal` / `load_pickrate` 读取；schema 演进只改一处。
- **契约测试** `test_environment_protocol.py`（4 tests）：未知 user_version 拒绝、协议表集合稳定、compile 消费路径与协议模块读取完全一致（真实 8 月库）、旧 `.json` 路径仍兼容。
- **文档**：`wiki/environment/index.md` 新增"协议契约"章节（协议表、版本守卫、演进规则：改 schema 须同步模块并递增 `SCHEMA_VERSION`；消费侧无需改动；外部应用按表结构自实现）。
- 验证：契约测试、sqlite 3 tests、协议 4 tests、liquipedia 5 tests、slot-decision 24 tests 全绿；compile 经协议模块读取真实归档正常（hydrate 端到端不变）。

## [2026-08-25] run | 裁判 skill 跑 1 局 Spiraling Out（Brawl Ball）BP 模拟

- 按 `skills/run-brawl-stars-bp` 裁判流程跑 1 局排位 BP：Spiraling Out（Brawl Ball，Season 48 新增图，S48 featured 模式）。用户要求选本赛季新增图用当前 BP skill 跑一局；Beach Ball（另一张 S48 新增图）已于 2026-08-21 跑过，本轮选 Spiraling Out。策略偏置随机分配：蓝方 `high_variance` vs 红方 `aggressive`。
- 蓝/红各 1 个 match-scoped player subagent 贯穿整局（ban → 4 个 pick turn → final review），复用 `send_message` 续轮，不跨局复用；裁判只传公开 picks/bans/unavailable pool，不传他方隐藏推理。
- runtime index 复用已编译的 `outputs/runtime-bp-index/default-runtime-index.json`（2026-08-24 重编译，33 图覆盖 Spiraling Out，`pickrate_status=loaded`——2026-08 月赛 archive + Legendary+ 10 周 ladder 折叠，precheck ready），未重新 compile；本图无逐图 ladder 行（无 Legendary+ 样本），环境证据仅为全局锚点 + monthly finals 双维。
- 禁用阶段（simultaneous，互不可见）：蓝方 ban `Brock`/`Bo`/`Buzz`（protect_first_pick——保留环境最强的 Griff 作蓝 1，ban 红方对首手的三组廉价反制）；红方 ban `Bo`/`Brock`/`Griff`（deny_blue_safe_opener——剥夺蓝 1 安全开局者）；重复 ban：`Brock`、`Bo`（蓝方动机=保护首手，红方动机=deny，独立成立）。不可用池：Brock/Bo/Buzz/Griff。
- 选择：蓝1 `Meeple`（穿墙改写中部角墙 + Ragequit 眩晕制造开放球门射门窗口，双 route gate 命中，monthly 20 选全场最高）→ 红2-3 `Ash`+`Crow`（Ash→Meeple 失败门反向命中 + Crow 反疗减速反制规则区推进兼探草）→ 蓝4-5 `Emz`+`Rico`（Emz 喷雾反 Ash 笨重目标 + Rico 弹射反突进，两者投射物配合 Meeple 穿墙规则区）→ 红6 `Grom`（越墙 thrower 反 Rico 失败门 + Grom→Emz 明确边 + 补侦察缺口，environment_unverified 但机制独立成立）。最终阵容：蓝 `Meeple/Emz/Rico` vs 红 `Ash/Crow/Grom`。
- 逐局完整报告与 decision log 写入 `outputs/bp-simulations/match-spiraling-out.md` 与 `match-spiraling-out.decision-log.md`（临时运行产物，按 2026-07-01 cleanup 约定不进 wiki syntheses）；双方选手日志 `match-spiraling-out.{blue,red}.player-log.md` 保留完整 examined_options 审计；本局核心对局结构为「Meeple 穿墙规则区 vs Grom 越墙」的墙几何争夺，关键结论如需沉淀再单独提炼。

## [2026-08-25] skill | slot-decision 加 Capability-Window First 检索层（能力窗口 + 排序修复）

用户对 Spiraling Out 模拟（红方 6 楼 Grom）提出质疑：既然选 Grom 的理由是"投手/越墙反制"，Willow（fit=strong、Brawl Ball 专属 hook `brawl_ball_hex_carrier_or_goalkeeper_displacement` 心控持球者/守门员）明显更优，为何漏选。核查发现工具层 bug + 检索范式缺口：

- **字典序截断 bug**：`query_runtime_facts.py` 的 `candidate_sort_key` 只有两级排序（`(0 if map_signal else 1, name)`），limit=32 截断时"有信号"组内按英雄名字典序取前 32 个 → W-Z 开头的英雄（Willow）永远出局；重放红方 6 楼查询证实窗口是 A-M 连续字典序，Grom（G）侥幸入围。
- **检索范式缺口**：人类选手按"能力窗口"组织候选（本手需要投手能力 → 圈投手子集 → 池内按模式特征/阵容交互筛选），工具只有"地图信号全池扫描"，没有"按能力查人"的原语。

**第一层（工具）**：
- `query_runtime_facts.py` 新增 `--capability` 检索原语（可重复、OR 语义）：按英雄 `runtime_card.capability_tags` 过滤，能力命中者**不受 `--effort`/`--limit` 截断**（保证 Willow 这类晚字母英雄可见）；`--include-id` 显式点名始终绕过能力过滤。
- `candidate_sort_key` 重写为证据排序：能力命中数 → fit 等级（strong<medium<weak<None）→ hook 数 → 能力匹配数 → 名字 tiebreaker。字典序只作同分稳定性，不再主导截断。
- 验证：crowd_control 窗口 53 人（Willow 可见）；throw_or_wall_bypass 窗口含 Willow/Grom/Barley/Juju/Dynamike/Mico/Sprout；Larry & Lawrie 因本图 fit=weak 正确排除（能力过滤不硬拉 weak-fit）。

**第二层（决策规则）**：
- `runtime-decision-knowledge.md`：LLM Decision Pipeline 插入 **Capability-Window First** 步骤（从地图 required_capabilities + 阵容缺口 + 对方已选推导能力窗口 → `--capability` 圈池 → 池内做模式特征过滤 → 地图职责/关系/失败门比较）；Neutral Fact Tools 文档补 `--capability`；Reasoning Rules 加"能力标签不是选人结论"与"能力窗口是显式入池方式"两条。
- `brawl-stars-bp-slot-decision/SKILL.md`：Decide Summary 声明 Capability-Window First 为默认入池方式；Ordering logic 插入能力窗口 fit 与模式特征 fit 两条（能力池内模式目标参与度是硬过滤）。
- 测试：slot-decision 新增 5 条契约测试（能力过滤生效/能力命中不截断/include-id 绕过/排序非字典序/无能力参数保持旧行为），29 条全绿；maintenance 契约测试补 `--capability`/`capability-window`/`Capability-Window First` 术语锁定，契约通过。

**第三层（能力×能力对抗边）未动**：基于 `capability_vector`（18 个带量级维度）+ 现有条件化对位边结构评估可行，留待单独迭代（需设计能力对抗条件与 compile 折叠，维护成本可控：能力维度封闭，远小于 105×105 英雄全对位）。

## [2026-09-03] ingest | 2026-08 补丁全量 ingest：Wendy/Nori 极限充能、6 个新芭菲、平衡调整与新英雄入册

用户要求更新 Wendy/Nori 极限充能、最新一期平衡性调整和 6 个芭菲（= Buffies）。本次补丁源为 Fandom `Version_History/2026` 的 `Release Notes August 2026` section（revid 217944）。

- **raw 层新增 10 件**：`release-notes-august-2026-2026-09-03.md`（section 抓取，boundary 明确排除 Brawl Arena——维护者决定本库不追踪 Brawl Arena；season/skin/mode 亦不入）；Wendy Fandom+PLP（发布后状态，页面已无 `FutureUpdate`）、Nori Fandom+PLP、Poco/El Primo/Amber/Gus/Chuck/Shade 六人 Fandom 最新 raw（经 MediaWiki API `capture_brawler_sources.py` 通道，Fandom HTML 仍 403）。
- **roster**：category API 恢复可直连，released roster `105 → 108`（+Wendy/+Cosmo/+Vince，Buzz Lightyear 仍排除）；新 manifest `brawlers-roster-2026-09-03.md`；[[sources/Brawler-Roster]] 刷新。Cosmo/Vince PLP 404，按规则只入 ingest 队列不建实体。Wendy PLP `/wendy` 已上线，双源闭环。
- **source 层**：新增 [[sources/Fandom-Release-Notes-August-2026]]（含 `balance_patch_manifest`：15 条 breakpoint_supported + 30 条显式排除/非断点行，effective_order 4）；Wendy/Nori 四个来源页以发布后状态重建；六人 Fandom 来源摘要从 09-03 raw 重生成；Poco/El Primo/Amber/Shade 四页追加「来源差异备注」——官方 release notes 文案与线上页存在大量口径差（如 Asteroid Belt 1s 完全免伤 vs notes 2s 拦截投射物、Tuning Fork 1000×3 vs 400×3、El Fuego Buffie +4s vs +1.5s、Jump Scare 恐惧 1s vs 0.5s 等），一律以 direct raw 为稳定事实、notes 差异保留在备注，不静默统一。
- **entity 层**：新建 [[entities/brawlers/Wendy]] `bp_ready`（全字段 + `combat_breakpoint_profile`：body 2000/P1、main 1000/P1、出生等量护盾作 barrier_hp 变体、发生器 redirect/队友盾/Hypercharge 全部显式排除）；`Nori` 纳入 Hypercharge MASTER FISHERMAN 并校准削弱后数值（7000/2000 P11、Sushi Snack 18s）；六个芭菲英雄按 raw 把重做与 Buffie 折叠进稳定字段（Gus Kooky Popper 缴弹、Knockback Spirit 重做、Spirit Animal +15% 移速窗口、Spooky Pop 穿墙气球；Chuck 全 Super 4 充能模型重写；Poco/El Primo/Amber/Shade 各自重做+Buffie；初稿误用 notes 值的 Poco/El Primo 已逐条改回 raw 值）。Wendy 对位边补齐 PLP 全部 16 个种子（Bo/Surge/Pierce/Frank/Lola 后补评审边），PLP 覆盖审计恢复零缺口。
- **concept 层**：新建 [[concepts/Buffies]]（芭菲系统规则与建模边界；「芭菲」是 Buffies 的社区俗称、非英雄名，故不进英雄名称归一化表，只在该页记录）。
- **断点审计**：`audit_balance_breakpoints.py` 全链 4 份 manifest 重跑，8 月补丁渲染 18 个 supported 行；产出 `outputs/balance-breakpoints/2026-june-august-balance-breakpoints.{json,md}`（106 目标、757 pairwise deltas、321 build-pressure deltas、75 显式排除；Nori 斩击 3 发阈值目标 33→19 等真实变化正常）。
- **计数锁与运行时**：roster 变更后更新三处编译计数锁（slot-decision 编译测试 105→106 ×3）与 PLP 覆盖审计计数锁（105→106）；重编译 `outputs/runtime-bp-index/default-runtime-index.json`（106 brawlers，Wendy 卡片含 build/capability/hooks/contracts）。全部验证：profile 审计 106/106 `bp_ready` 零 blocker；维护+slot-decision 测试 58/58 通过；`test_balance_breakpoints.py` 10 tests 通过。

## [2026-09-03] cleanup | 英雄 raw 去重：每个英雄只保留最新日期抓取件

维护者决定：多版本英雄页只保留最新，历史日期版不再保留。按「新抓取件完整覆盖同一页面状态」的冗余标准执行显式 cleanup。

- **删除 74 件旧日期 raw**：`raw/sources/fandom/heroes/` 70 件（50 个英雄的多版本，如 crow/max/8-bit/surge/starr-nova 各 3-4 版 → 只留最新；wendy-2026-07-11 future 页、nori-2026-07-11 早期页一并按此决定删除，其预发布差异证据已闭合保留在 [[sources/Supercell-Wendy-Announcement-June-2026]] 与 [[sources/Fandom-Release-Notes-August-2026]]）；`raw/sources/pl-prodigy/brawlers/` 4 件（8bit-2026-06-30、max-2026-06-29、brock-2026-06-29、nori-2026-08-11）。删后每目录 106 件 = 每英雄恰 1 份最新抓取，与 106 个 `bp_ready` 实体一一对应。
- **引用修复**：删除前全库精确检查，`wiki/` 与 `skills/` 对被删文件的活引用为零（`wiki/log.md` 历史条目按 append-only 原则保留原文；`test_plp_matchup_coverage.py` 中的 `8bit-2026-06-30.md` 是 tempfile 夹具字符串，与真实 raw 无关）。
- **审计语义不受影响**：`audit_plp_matchup_coverage.py` 与断点审计本就只读每英雄最新 direct raw；`plp_raw_files >= plp_raw_pages` 断言在 106=106 下成立。验证：维护+slot-decision 全部测试 58/58 通过，多版本残留检查为空。
- 本条为删除记录；被删文件内容如需追溯，见 git 历史或对应英雄的现行 raw 与来源摘要页。

## [2026-09-07] maintenance | pick 层加入 Ranked 池过滤 + Brawl Planet 接口复查（无大师/电竞精英档）

维护者要求 pick 层查询只统计当前 Ranked 地图池；同时复查 Brawl Planet 段位覆盖（回应"为什么只查到传奇"的疑问）。

- **接口复查**（`[[sources/Brawl-Planet-站点与数据接口]]` 更新）：站点改版 turbopack，GCS bucket 不变。HEAD 探测确认统计文件全集为 `pl` / `pl-d1`（新发现）/ `pl-m1` / `pl-m3`（nav 已摘但文件仍在）/ `pl-l1` + `brawlers`；`pl-l2`/`pl-ma1`/`pl-masters`/`pl-e1`/`pl-elite`/`pl-pro` 全部 403，nav 只挂 d1/m1/l1。**结论：本源无法产出大师/电竞精英逐段位切分**；`pl-l1` 是"传奇 I 及以上"下限口径，样本已含大师及以上对局。
- **Ranked 池 manifest**：新建 `wiki/environment/ranked_pool.json`（`brawlstar.ranked_pool_manifest.v1`，S48 30 图 + Fandom Ranked 页 revid 217144 provenance），来源同步 [[syntheses/Ranked-Season-48-地图Map-Profile总览]]。数据源的 35 图是天梯轮换池，与排位池本就不等（Deathcap Trap 天梯 active 但不在 S48 池；Snake Prairie 等 4 图 `active:false` 为滚动窗口退役残留）。
- **fetch 脚本**（`fetch_brawlplanet_pickrate.py`）：默认按 manifest 过滤——global 只累计池内 active 图、per_map 只保留池内行、池外图记入 `summary.excluded_maps`（含 reason），池图缺失时 stderr WARNING（赛季翻新信号）；`--ranked-pool-manifest` / `--no-ranked-pool-filter` 可选；`--tier` 扩为 l1/m1/m3/d1/default；`--db` 改为临时文件 + `os.replace` 原子快照，防旧赛季行残留。`pool_key` 地图名保留标点（区分 Safe Zone / Safe(r) Zone）、模式名去标点空格（raw `brawlball` == 显示 `Brawl Ball`，首版实现漏掉该归一导致 16 图误判池外，已修复并加回归测试）。归档协议（`_environment_sqlite.py`、SCHEMA_VERSION）零改动——过滤在生产侧完成，compile 折叠自动生效。
- **归档刷新**：`pickrate.sqlite3` 以池过滤口径重建（fetched 2026-09-07，30 图 / 106 英雄；Charlie 2.61% / 47.45%，Edgar 15.36% / 51.54%）；`current.json` bumped；`outputs/runtime-bp-index/default-runtime-index.json` 重编译折叠新 provenance。
- **测试**：新增 `test_ranked_pool_filter.py` 7 条（global 加权、per_map 池内限定+标注、summary 排除/缺失、stale manifest、未过滤直通、manifest 校验、pool_key 变体）；维护 + slot-decision 全量测试通过。
- **文档**：[[environment/index|环境归档索引]]（目录表 + 当前归档 + 维护规则 + 归档历史）、`skills/brawl-stars-bp-knowledge-maintenance/references/environment-signal-ingest.md`（Signal 结构、Monthly Workflow step 1、Rules 各加池过滤与 manifest 赛季维护条款）。

## [2026-09-03] cleanup | PLP raw slug 统一：按 canonical name 推导，消除 8bit/mrp/elprimo 类命名

维护者指出 `8bit-2026-06-30.md` 这类 URL 原样 slug（PLP 页面 URL 即 `/8bit`）与 canonical 名 `8-Bit` 对不上、观感差。核查后统一：

- **改名 7 件 PLP raw**（日期不变）：`8bit→8-bit`、`elprimo→el-primo`、`jaeyong→jae-yong`、`larrylawrie→larry-lawrie`、`mrp→mr-p`、`rt→r-t`、`starrnova→starr-nova`。fandom 目录 106 件本就全部符合 name-slug，无需改名；改后两目录 slug 与 `brawlers-roster-2026-09-03.md` 的 canonical 名一一对应。
- **slug 规则统一**：`capture_brawler_sources.py` 与 `ingest_brawler_sources.py` 的 `slug_from_url_or_name` 改为按 canonical name 推导（不再用页面 URL 原样 leaf），今后新抓取不会再产生 URL 风格命名；`direct_capture_exists` / `latest_direct_raw` 在新规则下能正确命中改名后的文件（capture 对 Mr. P 实测 `skip_existing_direct`，ingest 对改名英雄 dry-run planned 正常无 FileNotFoundError）。
- **引用修复**：7 个 `wiki/sources/PLP-*.md` 的上游 raw 链接同步改名；PLP 覆盖审计按 raw 内 JSON `name` 字段解析 canonical 名，不依赖文件名，审计与全部测试 71/71 通过。

## [2026-08-25] architecture | 第三层落地：能力维度量化 + 对抗原型 + 天敌清点 + 失败门地形激活

承接同日 Capability-Window First 检索层。用户以"神秘流星 Squeak 一选如何回应"实战测试检索范式，暴露四个缺口后拍板全部落地（五步计划），并先完成 24 能力维度 MECE 摸底（五轴分类：自身属性 / 伤害输出 / 控制压制 / 地形 / 信息团队；关键发现：16 个标签 105/105 全覆盖零区分度、112 个 none 值误收、中英量级词混用）。

- **步骤 1（维度清洗，compile）**：新增 `parse_capability_level`（中英量级词映射 none/low/medium_low/medium/medium_high/high/very_high，保守 unknown）、`extract_range_tiles`（"7.33 格"数值提取）。`capability_tags` 只收非 none/unknown 维度（wall_break 105→30，El Primo 不再带投掷标签）；新增 `capability_levels`/`range_tiles` 结构化字段进 card 与 hydrate/query。
- **步骤 2（天敌清点，新工具）**：新增 `query_matchup_census.py`——输入 hero + banned 集，输出 `answered_by`/`answers` 幸存名单与计数（alive/removed_by_bans + mechanism/active_when/fails_when 边原文）。实测纠正一处叙事幻觉：Squeak 的 8 条天敌边（Bibi/Edgar/Bull/Bolt/Ollie/Trunk/Willow/Rosa）与本次 ban 位无交集——"ban 清了它的天敌"是脑补，数据不支持。
- **步骤 3（时序纪律，规则）**：runtime-decision-knowledge 新增 **First-Response Discipline** 章节（暴露诊断 → 天敌清点 → 预算纪律三步，专 counter 须三条件同时满足否则 structure-first）；SKILL.md Ordering logic 同步。
- **步骤 4（失败门×地形，compile）**：`gate_prereq_type` 从 active_when 文本分类前提（close_approach/open_exposure/unknown），`map_approach_profile` 从 route_gates 推断地图接近特征，逐图生成 `failure_gate_activation`（high/medium/low/unknown）进 candidate_index 与 fact window。验证：同一 Squeak 贴脸门在神秘流星=low、Beach Ball=high——"纸面弱点 vs 真实弱点"机械可判。
- **步骤 5（原型 + floor）**：`ARCHETYPE_RULES` 谓词合取（assassin/sniper/thrower_core/tank_front/area_controller/vision_controller/dual_duty_mid），compile 自动派生 `archetypes`（不手写名单，新英雄自动归类，谓词可解释可测试）；谓词语义：下界缺失不满足、上界缺失不违反。查询工具新增 `--archetype`（OR）与 `--require-floor "dims@level"`（无短板轴下限查询，R-T/Pearl 型）；窗口命中者不被 effort 截断。
- **测试**：slot-decision 新增 6 条（量级序双副本一致/none 剔除/archetype 过滤/floor 过滤/gate activation 透出/census banned 过滤），35 tests 全绿；maintenance 契约加 `--archetype`/`--require-floor`/`First-Response Discipline`/`query_matchup_census`/`capability_levels`/`failure_gate_activation` 术语锁定，契约通过（maintenance 32 tests 亦全绿）。
- **审计移交**：`outputs/bp-simulations/capability-level-unknown-audit-2026-08-25.md`——94 英雄 / 405 维度为纯描述无量级词（如 Edgar mobility），按"查询驱动维护"原则列为后续批修队列；unknown 维度保守排除出阈值查询，不做猜测。

## [2026-09-03] cleanup | 英雄 raw 文件名去日期化：每英雄一份 `<hero>.md` 现行抓取

维护者决定：既然每英雄永远只保留一份最新抓取，文件名不再携带日期版本号。

- **改名 212 件**：`raw/sources/fandom/heroes/<slug>-<date>.md` → `<slug>.md`、`raw/sources/pl-prodigy/brawlers/<slug>-<date>.md` → `<slug>.md`。抓取时间仍记录在文件头 `- Capture date:` 元数据，时间信息不丢失。
- **脚本适配**：`capture_brawler_sources.py`（输出路径 `<slug>.md`、存在即 `skip_exists`、`direct_capture_exists` 优先精确名并兼容旧日期名）与 `ingest_brawler_sources.py`（`latest_direct_raw` 优先精确名、兼容旧日期名）同步更新；实测 8-Bit capture 返回 `skip_exists -> raw/sources/fandom/heroes/8-bit.md`、ingest dry-run planned 正常。时间点敏感文档（patch notes、roster manifest、赛事抓取）保留日期命名。
- **引用修复**：212 个 wiki 文件的上游 raw 链接批量去日期化（`wiki/log.md` 历史条目保留原文）；`AGENTS.md`「来源版本与覆盖清理规则」的 canonical 抓取件示例同步改为无日期命名约定。
- **验证**：维护 + slot-decision 全部测试通过；全库英雄 raw 多版本与日期残留检查为空。

## [2026-08-25] fix | 能力窗口全池扫描 + 量级阈值查询姿势（投手池 26 人误报修复）

用户质疑神秘流星局 `--capability throw_or_wall_bypass` 捞出 26 个"投手"（真实投手远少于此）。诊断出两层问题并修复：

- **标签≠阈值**：capability 标签匹配不筛量级，7 个 low（Stu/Colt/Byron 等"技能勉强碰墙"）混入。正确姿势是 `--require-floor "throw_or_wall_bypass@high"`（26→10）。
- **维度语义混杂**：`throw_or_wall_bypass` 建模"任何越墙手段"（真投手普攻 / 技能弹穿墙 / 位移越墙三类混在一个维度），Gene 魔手、Mandy 妙具也被记 high。根治需英雄页维度拆分（arc_throwing / utility_wall_pierce / mobility_wall_cross），已记入 capability 审计文件作为后续队列；查询层先用 floor 阈值缓解。
- **窗口全池扫描（本条核心修复）**：发现 Willow/Barley/Mico/Larry & Lawrie 等真投手在开阔图 `fit=weak` 不进任何投影桶，能力窗口完全看不到他们——违背"能力圈人、地图适配是圈内排序"的范式。修复：capability/archetype/floor 任一窗口激活时，候选扫描扩大到全 candidate_index（`retrieval_matches` 标 `capability_window`，weak fit 照常透出并按 fit 排序靠后）；无窗口时保持原 bucket 行为。实测神秘流星投掷@high 窗口 10 strong + 18 weak 全量可见，含全部四位真投手。
- 文档：runtime-decision-knowledge.md `--capability` 条目补"Tag ≠ threshold（优先 floor 形式）"与"窗口全池扫描、weak fit 是信息不是不存在"两条使用规则。
- 测试：slot-decision 35 tests 全绿，maintenance 契约通过。

## [2026-09-08] skill | 窗口纪律规则 + Meeple ally_synergy 编译警告清账

- 背景：Belle's Rock（Knockout）模拟局后复盘发现，capability v2 的"窗口全池扫描"落地后出现两类开销退行——选手在同一手内对 bucket 窗口（`ban_pressure` 等）已覆盖的候选池再做第二个全池 `--capability` 窗口复核（重复付费），以及 Meeple 英雄页一条 `ally_synergy` 协同条目误放在 `conditional_matchups` 编译字段内导致每次编译输出 skip 警告。
- `skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md` 查询参数区新增"Window discipline"条目：每手只做一次认真的能力窗口；bucket 窗口与 `--capability` 窗口在同池高度重叠，第一个窗口已返回本手所需候选时不得再扫第二个全池窗口；担心截断时的正确动作是收窄（`--relation-target` / `--exclude-id`）或定向 hydrate `--include-id`，`--limit` 用作单手显式召回预算；确需第二次扩窗必须在检索审计中说明第一个窗口答不了什么。（`.dsh/skills/` 为指向 `skills/` 的挂载链接，一份编辑即双份生效。）
- `wiki/entities/brawlers/Meeple.md`：将 Meeple → Dynamike / Barley / Tick / Larry & Lawrie / Rico 的协同条目从 `conditional_matchups`（runtime 编译字段）迁出为"组合协同备注（维护层，不入 runtime 对位索引）"prose 段，字段语义保持（队友协同非一-way counter 边）；知识不删除，仅离开无消费方的 schema 字段。
- 验证：重编译 stderr 无任何警告；新旧索引逐字段 diff 仅 `manifest.source_hash`（源文件变更）与 `compiled_at` 两处，运行时 payload 完全一致——该条目此前即被跳过、从未进过对位索引，本次为纯数据卫生修复；slot-decision 35 tests 全绿，maintenance 契约测试通过。

## [2026-09-08] skill | ban_pressure 召回排序改按本图环境行（effort 截断落在决策相关轴）

- 背景：Belle's Rock 复盘发现第一窗（`--bucket ban_pressure --effort low`）按钩子数/字母序从 53 个 strong-fit 成员截前 24，最终三 ban 之一的 Mortis 与环境第二强的 Rico 都被字母序挤在窗外，选手被迫追加两次全池能力扫描补救——召回层的排序依据与决策依据不相关。
- 改动（`skills/brawl-stars-bp-slot-decision/scripts/query_runtime_facts.py`）：新增 `map_environment_row`（与 hydrate 同源解析 `environment_ladder_per_map`）与 `ban_pressure_env_sort_key`；当请求 bucket 含 `ban_pressure` 时，桶内排序改为"激活环境行优先，按本图 use_rate → win_rate 降序，无激活行的名字按原证据相关序垫底"。桶成员资格不变（仍需 fit=strong + 地图信号），只改呈现序与因此被 effort 截断的名字；其余 bucket 行为不变。
- 测试：新增 `test_ban_pressure_window_orders_by_map_environment_ladder`（自校准：取基线窗尾两名注入合成环境行，断言重查后置顶），slot-decision 36 tests 全绿，maintenance 契约通过。
- 实测（Belle's Rock / Knockout，局内同款索引）：新窗口 24 人含全部最终三 ban（Edgar/Brock/Mortis，旧窗缺 Mortis）与红方实际选用的 Meeple/Gene/Sprout；14 进 14 出，被挤出者为环境冷门位（Bea/Buster/Doug/Dynamike 等）。 Doug 类低使用率结构手的第一窗可见性下降，但其发现渠道本就是 census/定向 hydrate，不受此排序影响。
- 文档：runtime-decision-knowledge.md `--bucket` 条目同步排序规则说明。

## [2026-09-08] skill + syntheses | "outputs 永不持久化"原则落地 + 六月至八月断点审计消化

- 架构原则（维护者裁决）：`outputs/`（含 `runtime_bp_index` 与断点审计账本）永不持久化——不入 git、即编即用、可随时删除重建，永远不是知识库组成部分或任何页面的依赖；wiki 页面不得链接或引用 outputs 路径；syntheses 消化页必须自包含携带结论，只沉淀有价值的审计报告和结论。
- 原则落位：`AGENTS.md` 平衡补丁工作流段落新增"outputs 永不持久化原则"；`skills/brawl-stars-bp-knowledge-maintenance/references/balance-breakpoint-audit.md` 输入归属表更新并新增 Durability rule。
- 修旧页：`wiki/syntheses/2026六月至七月平衡性断点双向评估.md` 移除指向 `outputs/balance-breakpoints/` 的 JSON/MD 链接，改为自包含声明（账本可再生、按维护命令重生成）。
- 新增消化页：`wiki/syntheses/2026六月至八月平衡性断点双向评估.md`（`version_breakpoint_synthesis_non_runtime`），自包含消化 2026-08-04 维护断点审计增量：Janet 三发线 19→33 为唯一大幅增强，Nori −14 / Lumi −4 为最深削弱；Nori/Melodie/Chuck/Hank/Jacky 的血量与减伤状态联合驱动；满盾对 Janet 从可选变保线必需、对 Lumi/Nori 边际价值归零；5 英雄 manifest/profile 失配排除与 NanoPower 23 项限时排除如实声明。页面无任何 outputs 链接。
- `wiki/index.md` BP Archive 区登记新页。

## [2026-09-08] fix | 原型筛选保留 schema 下划线

- 应用集成真实 CLI 发现 `--archetype thrower_core` 被英雄名称归一化器改为 `throwercore`，与编译卡片的 schema ID 不一致，导致带下划线的原型全部空召回；旧测试只覆盖不含下划线的 `sniper`。
- 查询原型参数改为仅 trim/lower，保留 schema 下划线；新增大写 `THROWER_CORE` + floor + include/exclude + limit=1 的真实编译/查询回归，核实匹配候选不被通用预算截断。

## [2026-09-08] skill | 玩家候选蒙版与个人英雄池接口

- query 的 bucket/include/relation/全池窗口及 hydrate 共用 candidate_mask.v1 硬约束；空池与不限分离，版本不符/未知名称/缺文件明确失败；关系目标不裁掉。
- census 保留全池 answered_by/answers，新增 selectable_answered_by 投影。
- resolve_player_pool 复用唯一实体/alias 数据，输出 P11+ 名单和未匹配/等级不足原因；不保存用户资料。
- 修复查询缓存遗漏能力/原型/阈值参数及仅按索引路径缓存的问题，加入蒙版和索引内容身份；同步 skill references 与真实 CLI 契约测试。

## [2026-09-09] skill | 将玩家 API 数据适配与资格策略移回应用层

- 修正 2026-09-08 引入的层级边界：删除 resolve_player_pool.py 及其玩家资料测试；官方 API 字段适配、等级筛选和排除原因全部由应用实现。
- 知识库仅保留现有通用实体/别名索引与 candidate_mask.v1 的 canonical allowlist 消费契约；不接收玩家英雄等级行。
- 同步蒙版 reference 与 skill 说明，保留 query/hydrate/census 的通用硬约束及缓存隔离。
