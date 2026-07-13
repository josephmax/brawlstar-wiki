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
