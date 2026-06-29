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
