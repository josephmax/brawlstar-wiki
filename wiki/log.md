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

## [2026-06-29] plan | 105 英雄 BP 建模升级任务计划

- 新增 `raw/inbox/2026-06-29-user-note-hero-bp-ingest-plan.md` 与 `wiki/sources/User-Note-Hero-BP-Ingest-Plan.md`，记录维护者要求：本会话只列计划不执行；后续按 105 位英雄完整 scope 处理；Fandom 与 PLP 详情页都应优先保留 raw。
- 新增 `wiki/syntheses/英雄BP建模升级任务计划.md`，定义交接目标、raw/source/entity/synthesis 分层、105 行 roster manifest、BP-ready 英雄页目标结构、Fandom/PLP 对齐标准、地图/模式/顺位中间层映射、阶段性执行批次和验收门槛。
- 更新 `wiki/syntheses/英雄BP建模覆盖审计.md`、`wiki/index.md` 与 `AGENTS.md`，把任务计划接入后续英雄 BP ingest 的必读路径。
- 本次未抓取 Fandom 或 PLP 页面，未批量修改英雄实体页。

## [2026-06-29] ingest | 英雄 BP 建模 Phase 0-3 启动

- 完成 Phase 0 roster manifest：新增 `raw/sources/roster/brawlers-roster-2026-06-29.md` 与 `wiki/sources/Brawler-Roster-2026-06-29.md`。
- Fandom `Category:Brawlers` 当前返回 105 个 Brawler 页面；PLP sitemap 返回 104 个英雄 guide URL；本地 72 个英雄实体页之外缺失 33 个；唯一 PLP URL gap 是 `Buzz Lightyear`。
- 完成 Phase 1 Batch A raw capture：为 `Brock`、`Gene`、`Otis`、`Belle`、`Colt`、`Angelo`、`Shade`、`Rico`、`Mico`、`Max`、`Stu` 新增 dated Fandom raw 与 PLP raw。
- 完成 Phase 2 Batch A source 摘要：更新上述 11 个 `wiki/sources/Fandom-*` 为 `direct_raw_capture`，新增 11 个 `wiki/sources/PLP-*` 来源页。
- 开始 Phase 3 BP 建模：为 `wiki/entities/brawlers/Brock.md`、`wiki/entities/brawlers/Gene.md`、`wiki/entities/brawlers/Otis.md` 新增 `bp_brawler_profile` 草案，状态均为 `profile_status: draft`。
- 新增 `wiki/syntheses/英雄BP建模执行状态.md`，记录 Phase 0-3 当前进度、Batch A 完成项和下一步建议。
- 更新 `wiki/index.md`，接入 roster source、PLP Batch A 来源页、英雄 BP 建模执行状态页，并补齐 Syntheses 中的英雄审计/计划入口。

## [2026-06-29] scope correction | Buzz Lightyear 不进入 BP 建模

- 新增 `raw/inbox/2026-06-29-user-note-buzz-lightyear-out-of-scope.md` 与 `wiki/sources/User-Note-Buzz-Lightyear-Out-of-Scope.md`，记录维护者校正：`Buzz Lightyear` 是临时英雄且已下架，不进入当前 BP 建模。
- 更新 `wiki/sources/Brawler-Roster-2026-06-29.md`，保留 Fandom raw roster count 为 105，但将 BP-active scope 修正为 104，并把 `Buzz Lightyear` 从 BP-active 缺失英雄列表移到 out-of-scope。
- 更新 `wiki/syntheses/英雄BP建模升级任务计划.md`、`wiki/syntheses/英雄BP建模覆盖审计.md` 与 `wiki/syntheses/英雄BP建模执行状态.md`，统一“105 行 manifest / 104 BP-active 英雄”的口径。
- 更新 `AGENTS.md` 与 `wiki/index.md`，明确未来全量英雄 BP 建模不追踪 `Buzz Lightyear` 的 PLP 缺口、对位边或地图适配。

## [2026-06-30] ingest | 104 个 BP-active 英雄 Fandom/PLP 全量抓取与 draft BP 建模

- 新增 `tools/capture_brawler_sources.py`、`tools/ingest_brawler_sources.py`、`tools/ingest_brawler_bp_profiles.py`，用于可复跑地从 roster manifest 抓取 raw、生成 source 摘要和初始化英雄 BP 草案。
- 补抓 104 个 BP-active 英雄的 Fandom corrected direct raw 与 PLP direct raw；`Buzz Lightyear` 保持 out-of-scope。
- 修正 Fandom 抓取漂移：首轮 `2026-06-30` 发现单行 infobox 解析污染，新增 `2026-06-30-v2` corrected raw；`Chester` / `Kaze` 专属 infobox 再用 `2026-06-30-v3` 定点修正。
- 生成/更新 104 个 `wiki/sources/Fandom-*` 与 104 个 `wiki/sources/PLP-*` source 摘要，统一标注来源边界：Fandom 只作为稳定机制事实，PLP 只作为 build/mode/matchup 竞技信号。
- 新建 32 个缺失 BP-active 英雄实体页，给 69 个既有英雄页追加 `profile_status: draft_from_raw_signals`；保留 `Brock`、`Gene`、`Otis` 已有人工 `draft` 草案。当前 104 个 BP-active 英雄均有 `bp_brawler_profile`，但没有任何英雄标记为 `bp_ready`。
- 新增 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]] 与 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]，作为 seed-only 全局索引；它们不是最终 counter 表或地图适配结论。
- 更新 `wiki/syntheses/英雄BP建模执行状态.md` 与 `wiki/index.md`，记录当前验收快照、剩余质量门槛和全量导航。

## [2026-06-30] review | 英雄 BP 质量门槛与第一批 reviewed

- 新增 `wiki/syntheses/英雄BP建模质量门槛.md`，明确 `draft_from_raw_signals`、`reviewed`、`bp_ready` 的升级条件；`bp_ready` 必须有 reviewed 条件化对位边与 Ranked 地图 hook，不允许批量直升。
- 新增 `tools/audit_bp_profile_quality.py` 与 `wiki/syntheses/英雄BP建模质量审计.md`，用于审计 104 个英雄页的明显占位符、来源追溯、地图 hook、失败条件和 slot notes。
- 复核 `Brock`、`Gene`、`Otis` 三个已有人工草案，将其 `profile_status` 从 `draft` 升级为 `reviewed`，并把 Fandom raw 日期同步到 corrected `2026-06-30-v2`。
- 当前质量审计结果：104 个英雄均有 `bp_brawler_profile`；`reviewed` 3 个，`draft_from_raw_signals` 101 个，`bp_ready` 0 个。
- 更新 `wiki/syntheses/英雄BP建模执行状态.md` 与 `wiki/index.md`，把质量门槛、质量审计和第一批 reviewed 状态接入导航与交接页。

## [2026-06-30] review | Batch A 英雄升级到 bp_ready

- 复核 `Belle`、`Colt`、`Angelo`、`Rico` 四个 Batch A 英雄页，删除自动草案占位语句，补全能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；它们已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：新增 `reviewed_from_brawler_profiles` 区，记录 12 组 reviewed 条件化对位边。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：新增 `reviewed_from_brawler_profiles` 区，记录 12 条 reviewed Ranked 地图 hook。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 4 个、`reviewed` 3 个、`draft_from_raw_signals` 97 个。

## [2026-06-30] review | Batch A 机动组升级到 bp_ready

- 复核 `Max`、`Stu`、`Mico`、`Shade` 四个 Batch A 机动组英雄页，重点把团队速度、冲刺链、跳墙/穿墙、过水/越障等能力转成具体地图职责、目标收益和失效条件。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 12 增至 24。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 12 增至 24。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 8 个、`reviewed` 3 个、`draft_from_raw_signals` 93 个。

## [2026-06-30] review | Ash / Nita / Sandy 升级到 bp_ready

- 复核 `Ash`、`Nita`、`Sandy` 三个英雄页，将 Rage 前压、Bruce 召唤物、Sandstorm 团队隐身等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 24 增至 33。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 24 增至 33。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 11 个、`reviewed` 3 个、`draft_from_raw_signals` 90 个。

## [2026-06-30] review | Draco / Gigi / Poco 升级到 bp_ready

- 复核 `Draco`、`Gigi`、`Poco` 三个英雄页，将变身驻点、弹道充能传送、团队治疗净化等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 33 增至 42。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 33 增至 42。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 14 个、`reviewed` 3 个、`draft_from_raw_signals` 87 个。

## [2026-06-30] review | Sam / Bibi / Buster 升级到 bp_ready

- 复核 `Sam`、`Bibi`、`Buster` 三个英雄页，将拳套回收/拉拽、Home Run 击退/弹墙泡泡、屏障反射/队伍护送等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 42 增至 51。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 42 增至 51。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 17 个、`reviewed` 3 个、`draft_from_raw_signals` 84 个。

## [2026-06-30] review | Charlie / Chuck / Clancy 升级到 bp_ready

- 复核 `Charlie`、`Chuck`、`Clancy` 三个英雄页，将 Cocoon 单体移除与蜘蛛视野、Post 路线与 Heist 打库循环、token 阶段成长与 Stage 3 区域接管等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已各自具备 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 51 增至 60。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 51 增至 60。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 20 个、`reviewed` 3 个、`draft_from_raw_signals` 81 个。

## [2026-06-30] review | Cordelius / Crow / Darryl 升级到 bp_ready

- 复核 `Cordelius`、`Crow`、`Darryl` 三个英雄页，将 Shadow Realm 隔离与沉默、毒伤反治疗/探草/残局跳杀、滚桶路线/击退/近身爆发等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 3 组 reviewed 条件化对位边和至少 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 60 增至 72。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 60 增至 71。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 23 个、`reviewed` 3 个、`draft_from_raw_signals` 78 个。

## [2026-06-30] review | Doug / Emz / Gus 升级到 bp_ready

- 复核 `Doug`、`Emz`、`Gus` 三个英雄页，将复活支援、喷雾控场/反突进、远程护盾支援等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述三个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 3 组 reviewed 条件化对位边和 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 72 增至 84。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 71 增至 80。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 26 个、`reviewed` 3 个、`draft_from_raw_signals` 75 个。

## [2026-06-30] review | Jae-yong / Lily / Mandy / Meg 升级到 bp_ready

- 复核 `Jae-yong`、`Lily`、`Mandy`、`Meg` 四个英雄页，将团队加速/治疗支援、Vanish 突袭、Focus 超长线、Mecha 目标区身体等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 84 增至 100。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 80 增至 96。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 30 个、`reviewed` 3 个、`draft_from_raw_signals` 71 个。

## [2026-06-30] review | Melodie / Mina / Mortis / Rosa 升级到 bp_ready

- 复核 `Melodie`、`Mina`、`Mortis`、`Rosa` 四个英雄页，将音符叠层三段冲刺、三段连段与 Windmill、dash 收割、Grow Light 草丛前排等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备至少 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 100 增至 116。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 96 增至 112。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 34 个、`reviewed` 3 个、`draft_from_raw_signals` 67 个。

## [2026-06-30] review | 8-Bit / Bo / Bolt / Bonnie 升级到 bp_ready

- 复核 `8-Bit`、`Bo`、`Bolt`、`Bonnie` 四个英雄页，将 Booster 阵地增伤、地雷/视野控口、动量接触路线、Clyde/Bonnie 双形态跳入爆发等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 116 增至 132。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 112 增至 128，hook seed 条目数从 201 增至 207。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 38 个、`reviewed` 3 个、`draft_from_raw_signals` 63 个，并完成本批占位符扫描。

## [2026-06-30] review | Buzz / Carl / Colette / Finx 升级到 bp_ready

- 复核 `Buzz`、`Carl`、`Colette`、`Finx` 四个英雄页，将常驻 Buzz 的抓钩眩晕、Carl 的回旋镐/墙边循环、Colette 的百分比伤害与 special target 伤害、Finx 的 Time Warp 投射物速度控制等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 132 增至 148。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 128 增至 144，hook seed 条目数从 207 增至 217。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 42 个、`reviewed` 3 个、`draft_from_raw_signals` 59 个，并完成本批占位符扫描。

## [2026-06-30] review | Gale / Hank / Janet / Jessie 升级到 bp_ready

- 复核 `Gale`、`Hank`、`Janet`、`Jessie` 四个英雄页，将推离/减速/Twister、蓄力水泡与近身鱼雷、空中携宝/草区 speaker、Scrappy 炮台与弹射等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 148 增至 164。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 144 增至 160，hook seed 条目数从 217 增至 226。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 46 个、`reviewed` 3 个、`draft_from_raw_signals` 55 个，并完成本批占位符扫描。

## [2026-06-30] review | Kaze / Kenji / Lola / Lou 升级到 bp_ready

- 复核 `Kaze`、`Kenji`、`Lola`、`Lou` 四个英雄页，将 Kaze 双形态风暴与标记、Kenji dash/slash 吸血与 Super 免疫、Lola Ego 分身交叉火力、Lou Frost / Hot Zone 冰冻控场等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 164 增至 180。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 160 增至 176，hook seed 条目数从 226 增至 236。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 50 个、`reviewed` 3 个、`draft_from_raw_signals` 51 个，并完成本批占位符扫描。

## [2026-06-30] review | Lumi / Maisie / Mr. P / Ollie 升级到 bp_ready

- 复核 `Lumi`、`Maisie`、`Mr. P`、`Ollie` 四个英雄页，将 Lumi 双锤召回/root、Maisie Shockwave 反突进、Mr. P Porter 弹药税、Ollie Hypnotize 控制坦克等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 180 增至 196。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 176 增至 192，hook seed 条目数从 236 增至 246。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 54 个、`reviewed` 3 个、`draft_from_raw_signals` 47 个，并完成本批占位符扫描。

## [2026-06-30] review | Pam / Pearl / Penny / Shelly 升级到 bp_ready

- 复核 `Pam`、`Pearl`、`Penny`、`Shelly` 四个英雄页，将治疗炮台和 Scrapsucker 弹药剥夺、Heat 条成长输出、Old Lobber 炮台控图、近身霰弹反坦/破门等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 196 增至 212。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 192 增至 208，hook seed 条目数从 246 增至 254。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 58 个、`reviewed` 3 个、`draft_from_raw_signals` 43 个，并完成本批占位符扫描。

## [2026-06-30] review | Squeak / Starr Nova / Willow / Ziggy 升级到 bp_ready

- 复核 `Squeak`、`Starr Nova`、`Willow`、`Ziggy` 四个英雄页，将延迟粘弹与 Residue、Starr Nova Super 剑形态与 Floaty Time、Willow Hex 心控位移、Ziggy 延迟落雷与移动 storm 等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 212 增至 228。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 208 增至 224，hook seed 条目数从 254 增至 264。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 62 个、`reviewed` 3 个、`draft_from_raw_signals` 39 个，并完成本批占位符扫描。

## [2026-06-30] review | Alli / Amber / Barley / Bea 升级到 bp_ready

- 复核 `Alli`、`Amber`、`Barley`、`Bea` 四个英雄页，将草/水跳跃追猎、燃油火墙控区、墙后投掷 puddle、Supercharged 长线 slow 等机制转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 228 增至 244。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 224 增至 240，hook seed 条目数从 264 增至 271。
- 重跑 `tools/audit_bp_profile_quality.py --write`；当前质量审计结果为 `bp_ready` 66 个、`reviewed` 3 个、`draft_from_raw_signals` 35 个，并完成本批占位符扫描。

## [2026-06-30] audit | 英雄 BP 建模当前进度检查

- 复跑 `tools/audit_bp_profile_quality.py` 并抽样检查 `bp_ready`、`reviewed`、`draft_from_raw_signals` 三类英雄页，确认当前质量审计结果仍为 `bp_ready` 66 个、`reviewed` 3 个、`draft_from_raw_signals` 35 个。
- 新增 [[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]]，记录抓取、来源摘要、实体页、BP profile、条件化对位边索引和地图 hook 索引的当前进度。
- 判断当前主要缺口已从抓取转为质量复核：剩余 35 个 draft 英雄需要清理占位符、补具体地图路线/目标收益/失效条件、补 source traceability 和失败条件。
- 更新 [[index|Wiki Index]]，加入本次进度审计入口。

## [2026-06-30] review | Brock / Gene / Otis 升级到 bp_ready

- 复核 `Brock`、`Gene`、`Otis` 三个 `reviewed` 英雄页，将 Brock 的远程打库/选择性开墙/破门窗口、Gene 的拉人抓单/宝石位倒计时打断、Otis 的沉默反进场和草口/金库入口防守补成可消费的地图 hook 与条件化对位边。
- 将上述三个英雄从 `profile_status: reviewed` 升级为 `profile_status: bp_ready`；当前 `reviewed` 中间态归零。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 244 增至 256。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 240 增至 249，hook seed 条目数从 271 增至 273。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]] 与 [[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]]；下一步进入 35 个 `draft_from_raw_signals` 英雄的分批质量复核。

## [2026-06-30] review | Byron / Nani / Piper / Spike 升级到 bp_ready

- 复核 `Byron`、`Nani`、`Piper`、`Spike` 四个自动草稿英雄页，将 Byron 的长线治疗/反坦 poke、Nani 的远距爆发与 Peep 开墙、Piper 的极长线击杀窗口、Spike 的控区减速与反坦能力转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和至少 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 256 增至 272。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 249 增至 262，hook seed 条目数从 273 增至 276。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]] 与 [[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]]；重跑 `tools/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 73 个、`reviewed` 0 个、`draft_from_raw_signals` 31 个。

## [2026-06-30] review | Sprout / Surge / Tara / Ruffs 升级到 bp_ready

- 复核 `Sprout`、`Surge`、`Tara`、`Ruffs` 四个自动草稿英雄页，修正 Sprout 被误抽成泛水/机动、Surge 被误抽成投掷、Tara 和 Ruffs 被泛化成粗长线/开墙标签的问题。
- 将 Sprout 的投掷口袋与 Hedge 封路、Surge 的阶段成长与反近身、Tara 的 Gravity 聚怪/探草/召唤物、Ruffs 的弹墙/补给包/沙包/Air Superiority 开墙转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和至少 3 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 272 增至 288。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 262 增至 276，hook seed 条目数从 276 增至 281。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]] 与 [[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]]；重跑 `tools/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 77 个、`reviewed` 0 个、`draft_from_raw_signals` 27 个。

## [2026-06-30] review | Edgar / Eve / Gray / Leon 升级到 bp_ready

- 复核 `Edgar`、`Eve`、`Gray`、`Leon` 四个自动草稿英雄页，修正 Edgar / Leon 被泛化成错误投掷或长线标签、Eve 的水域价值未绑定目标收益、Gray 的传送门未绑定落点安全的问题。
- 将 Edgar 的跳跃贴脸/足球得分窗口、Eve 的水域远程与 hatchling 清理税、Gray 的传送门路线改写与 Walking Cane 拉人、Leon 的隐身信息差与单抓/偷目标转成可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述四个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 288 增至 304。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 276 增至 292，hook seed 条目数从 281 增至 288。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]、[[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]] 与 [[index|Wiki Index]]；重跑 `tools/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 81 个、`reviewed` 0 个、`draft_from_raw_signals` 23 个。

## [2026-06-30] review | Bull / El Primo / Fang / Frank / Jacky 升级到 bp_ready

- 复核 `Bull`、`El Primo`、`Fang`、`Frank`、`Jacky` 五个自动草稿英雄页，将前排/切入英雄从粗粒度短手标签改写为目标接触、控球/站圈/打库转化、进场资源、地形变换、反坦失效条件和 slot 风险。
- 将上述五个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 304 增至 324。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 292 增至 312，hook seed 条目数从 288 增至 294。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]、[[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]] 与 [[index|Wiki Index]]；重跑 `tools/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 86 个、`reviewed` 0 个、`draft_from_raw_signals` 18 个。

## [2026-06-30] review | Moe / Trunk / R-T / Pierce / Glowy / Najia / Sirius 升级到 bp_ready

- 复核 `Moe`、`Trunk`、`R-T`、`Pierce`、`Glowy`、`Najia`、`Sirius` 七个自动草稿英雄页，将 Moe 的 Driller 出土资源门槛、Trunk 的蚂蚁区域身体、R-T 的分体腿部风险、Pierce 的弹壳循环、Glowy 的牵线支援、Najia 的毒区控路、Sirius 的影子经济分别改写为可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述七个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 324 增至 352。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 312 增至 340，hook seed 条目数从 294 增至 308。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]、[[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]] 与 [[index|Wiki Index]]；重跑 `tools/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 93 个、`reviewed` 0 个、`draft_from_raw_signals` 11 个。

## [2026-06-30] review | Berry / Chester / Dynamike / Griff / Grom / Tick 升级到 bp_ready

- 复核 `Berry`、`Chester`、`Dynamike`、`Griff`、`Grom`、`Tick` 六个自动草稿英雄页，将 Berry 的治疗铺地与 Super 位移限制、Chester 的随机 Super 与铃铛序列、Dynamike 的 Satchel / Super 开墙、Griff 的 Piggy Bank 与近中距离爆发、Grom 的固定十字线和 Radio Check、Tick 的雷区封路与 Last Hurrah 自保分别改写为可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述六个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 352 增至 376。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 340 增至 364，hook seed 条目数从 308 增至 314。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]、[[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]] 与 [[index|Wiki Index]]；重跑 `tools/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 99 个、`reviewed` 0 个、`draft_from_raw_signals` 5 个。

## [2026-06-30] review | Damian / Juju / Kit / Larry & Lawrie / Meeple 升级到 bp_ready

- 复核 `Damian`、`Juju`、`Kit`、`Larry & Lawrie`、`Meeple` 五个剩余自动草稿英雄页，将 Mosh Pit / Wall of Sound、元素地形投掷、附身支援、Lawrie 召唤物经济、Meeple 规则区域和 Mansions / Ragequit 等机制改写为可消费的能力向量、build delta、地图 hook、目标契约、失败条件、条件化对位边和 slot notes。
- 将上述五个英雄从 `profile_status: draft_from_raw_signals` 升级为 `profile_status: bp_ready`；每页已具备 4 组 reviewed 条件化对位边和 4 条接入 Ranked Season 46 地图的 reviewed hook。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]：reviewed 对位边组从 376 增至 396。
- 更新 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]：reviewed Ranked 地图 hook 从 364 增至 384，hook seed 条目数从 314 增至 319。
- 更新 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]、[[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]] 与 [[index|Wiki Index]]；重跑 `tools/audit_bp_profile_quality.py --write` 后，当前质量审计结果为 `bp_ready` 104 个、`reviewed` 0 个、`draft_from_raw_signals` 0 个。

## [2026-06-30] ingest | June 2026 版本 BP 影响覆盖

- 读取 `raw/sources/fandom/systems/release-notes-june-2026-2026-06-30.md`，只抽取会影响 BP 决策、失败条件、build 资源门槛或条件化对位边的变化；未把普通血量/伤害数值变动照搬为英雄结论。
- 新增 [[sources/Fandom-Release-Notes-June-2026|Fandom 来源摘要: Release Notes June 2026]] 与 [[syntheses/2026-06-30版本BP影响评估|2026-06-30 版本 BP 影响评估]]，作为版本 / meta 覆盖层。
- 给 `Rico`、`Brock`、`8-Bit`、`Meg`、`Max`、`Surge`、`Bolt`、`Meeple`、`Damian`、`Colette`、`Crow`、`Mortis`、`Edgar`、`Chester`、`R-T`、`Spike`、`Griff` 写入结构或对位阈值版本覆盖。
- 给 `Leon`、`Lumi`、`Najia`、`Pierce`、`Mina` 写入次级资源门槛版本覆盖；`Larry & Lawrie`、`Juju`、`Ruffs`、`Shade` 等暂留观察名单，等待玩家开发、对局样本或更明确阈值后再更新条件化对位边。
- `Brawl Arena Only` 变化未进入 Ranked BP；后续如分析 Brawl Arena，应另建模式覆盖层。

## [2026-06-30] compile | 固化 BP 当前有效模型

- 根据维护者反馈，将 `version_override` 从 BP 运行时输入改为版本 ingest 的编译输入；BP 决策运行时默认读取 [[syntheses/BP-当前有效模型|BP 当前有效模型]]。
- 更新 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]] 和 [[syntheses/条件化对位模型|条件化对位模型]]：新增 `effective_bp_model`，并将 `candidate_eval.version_fit` 改为 `candidate_eval.effective_model_fit`。
- 新增 [[syntheses/BP-当前有效模型|BP 当前有效模型]]，把 2026-06-30 版本的 22 条 BP-relevant delta 编译为 `hard_gate_deltas`、`capability_deltas`、`build_deltas`、`matchup_deltas`、`map_hook_deltas` 和 `slot_policy_deltas`。
- 更新 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]、[[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]、[[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]、[[index|Wiki Index]] 与 `AGENTS.md`，固定“稳定底座 + 版本编译输入 -> 当前有效模型 -> BP 运行时”的治理规则。

## [2026-06-30] repair | 移除 BP 运行时增量模型

- 根据维护者反馈，删除 [[syntheses/BP-当前有效模型|BP 当前有效模型]] 和后续误建的 `BP-当前决策模型.md`；运行时不再读取中央版本覆盖层。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、[[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]、[[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]] 与 [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]，固定“版本资料先审计；只有定性 BP 影响，且必须直接融入英雄 / 地图 / 对位 / hook 稳定字段”的规则。
- 撤回所有英雄页中的“版本覆盖”与“当前 BP 判断”页尾覆盖段，避免决策语料混入补丁式解释。
- 重新审计 2026-06-30 版本资料：`Rico`、`Brock`、`8-Bit`、`Meg`、`Max`、`Surge`、`Bolt`、`Damian`、`Spike` 仅标记为 `profile_merge_candidate`，等待逐字段内联；`Meeple`、`Colette`、`Crow`、`Mortis`、`Edgar`、`Chester`、`R-T`、`Griff`、`Leon`、`Lumi`、`Najia`、`Pierce`、`Mina` 保留在版本审计页，不进入运行时 BP 模型。
- 追加 `AGENTS.md` 英雄页治理规则：`wiki/entities/brawlers/` 只保存当前最新 BP 建模结果；版本 / meta 资料若不能直接内联改写稳定字段，只能留在来源、审计或日志层。

## [2026-06-30] repair | 清理 BP 运行索引和维护边界

- 将 [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]] 改为 `runtime_reviewed_index_from_brawler_profiles`，删除原始候选总览和待复核口径，只保留从英雄页稳定 `conditional_matchups` 派生的 reviewed 对位边。
- 将 [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]] 改为运行时派生索引，明确只用于候选检索和地图因素连接，不保存版本差分或临时强度判断。
- 更新 [[syntheses/条件化对位模型|条件化对位模型]]：版本资料接入门槛改为维护规则，不再作为运行对象；对象编号回到 `map_profile / mode_objective_profile / brawler_profile / build_profile / conditional_matchup / draft_state / pick_slot_state / draft_eval`。
- 更新 `AGENTS.md`、[[index|Wiki Index]]、[[syntheses/地图知识分层治理|地图知识分层治理]]、[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]、[[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]、[[syntheses/英雄BP建模进度审计-2026-06-30|英雄 BP 建模进度审计 2026-06-30]] 和 [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]]，把运行时读取路径固定为稳定英雄页、地图页、对位索引和地图 hook 索引；来源候选、版本观察和审计交接只留在维护层。
- 统一英雄页和对位索引中的 `bp_use` 命名，将旧抓取阶段的候选标签改为 `candidate` / `signal` 口径，避免运行语料继续暴露原始候选阶段术语。

## [2026-06-30] skill | 新增 BP slot 决策 skill

- 新增 `skills/brawl-stars-bp-slot-decision/SKILL.md`，固化 BP 查询时的必读运行时页面、slot policy、hard gate、候选评估和输出格式，要求每手输出 2-4 个可复盘决策。
- 新增 `skills/brawl-stars-bp-slot-decision/scripts/bp_index.py`，提供只读检索辅助，用于定位 Season 46 地图实体页、英雄实体页、条件化对位边索引和英雄地图 hook 索引命中；脚本只做召回，不替代 BP 排序。
- 新增 `skills/brawl-stars-bp-slot-decision/tests/test_bp_index.py`，覆盖必读页面声明和 `Safe Zone / Brock / Mortis` 样例索引召回。
- 已运行 `python3 skills/brawl-stars-bp-slot-decision/tests/test_bp_index.py` 与 `quick_validate.py`，均通过。

## [2026-07-01] query | BP 实战查询速度与模型形态评估

- 回答“当前数据量是否能满足实战 BP 思考速度，以及实时 skill 查询和直接微调哪个更快”的问题。
- 读取 [[index|Wiki Index]]、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、[[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]、[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]、[[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]、[[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]、[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]、[[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]] 与 `skills/brawl-stars-bp-slot-decision/`。
- 新增 [[syntheses/BP-实战查询速度与模型形态评估|BP 实战查询速度与模型形态评估]]，结论为当前数据量足够支撑实战 BP 的有依据思考；推荐 `skill + 本地检索 + 预热上下文 + 小范围候选评估`，不建议把可变事实库直接作为微调主载体。
- 更新 [[index|Wiki Index]] 增加该 synthesis 入口。
