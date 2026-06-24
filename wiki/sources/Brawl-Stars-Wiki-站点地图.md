# Brawl Stars Wiki 站点地图

## 来源信息

- 站点：Brawl Stars Wiki | Fandom
- 主页：[Brawl Stars Wiki](https://brawlstars.fandom.com/wiki/Brawl_Stars_Wiki)
- 读取日期：2026-04-06
- 用途：作为本知识库的外部来源总入口与信息架构参考

## 站点宏观结构

根据主页与分类页，当前站点主要由以下几大块组成：

### 1. Brawlers

- 主页将 Brawlers 作为一级入口
- 主页显示当前游戏内有 101 名 Brawlers
- 该类目既包含具体角色页，也包含按定位划分的子分类，例如 `Artillery Brawlers`、`Assassin Brawlers`

这说明在我们的 wiki 中：

- 单个英雄适合作为 `entities`
- 英雄定位、稀有度、职业划分适合作为 `concepts`

### 2. Events

- Events 是第二个一级入口
- 主页可见大量 3v3、Showdown、Solo、Special Event 等模式入口
- 这类目包含 `Gem Grab`、`Brawl Ball`、`Knockout`、`Ranked`、`Challenges`、`Mega Pig` 等

这说明在我们的 wiki 中：

- 具体模式或活动按稳定性可进入 `entities` 或 `concepts`
- 模式分类体系和胜负机制更适合写成 `concepts`
- 多个模式之间的比较适合写成 `syntheses`

### 3. Gameplay

- Gameplay 是第三个一级入口
- 分类页显示共有 21 个条目
- 主要覆盖 `Items`、`Abilities`、`Cosmetics`、`Brawl Pass`、`Pro Pass`、`Daily Streak`、`Records`
- `Items` 下包括 `Credits`、`Coins`、`XP`、`Power Points`、`Gems`、`Trophies`、`Bling`、`Starr Drops`
- `Abilities` 下包括 `Gears`、`Mutations`、`Power-ups` 等

这说明在我们的 wiki 中：

- 货币、升级材料、战斗能力系统优先进入 `concepts`
- 一次性或强时效活动能力系统可先挂在 `sources` 或专题页中

### 4. Community / Meta

- Community 中可见 `Beginner's Guide` 与 `Game Version History`
- 这类页面适合作为新手导览与版本演化的总索引

## 推荐的人类阅读顺序

为了让主 agent 按“从宏观到微观”的方式学习，建议采用以下顺序：

1. 先读站点主页与总分类页，建立地图
2. 先 ingest `Gameplay`，因为它定义资源、能力、系统，是底层概念层
3. 再 ingest `Events`，因为它定义玩法与胜负条件
4. 最后大规模 ingest `Brawlers`，因为角色知识会大量依赖前两者
5. `Community` 页面穿插处理，用于补足版本历史与新手路线

## 第一阶段优先 ingest 的主题

- 资源体系：`Credits`、`Coins`、`Power Points`、`Gems`、`Trophies`、`Bling`
- 成长系统：`Brawl Pass`、`Daily Streak`、`Starr Drops`
- 战斗能力：`Gears`
- 核心模式：`Gem Grab`、`Brawl Ball`、`Knockout`、`Showdown`
- 结构索引：`Game Version History`

## 暂时不急着大规模 ingest 的区域

- 全量英雄页
- 高波动、活动性较强的临时能力系统
- 只在特定联动或限定玩法中出现的机制

这些内容适合在基础概念页稳定后，再批量扩展。
