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
