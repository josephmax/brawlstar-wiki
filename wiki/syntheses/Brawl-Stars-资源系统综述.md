# Brawl Stars 资源系统综述

这篇综述基于当前已落盘的资源概念页，目标是把《荒野乱斗》的资源系统从“解锁 / 升级 / 高级货币 / 外观货币 / 进度指标”五个角度整理成一个可持续维护的总图。

## 总体结构

目前可以把资源系统理解成五层分工：

1. `解锁资源`
2. `升级资源`
3. `高级货币`
4. `外观货币`
5. `进度指标`

这五层不是完全彼此隔离，而是围绕英雄获取、成长、外观消费和长期推进形成一套交叉系统。

从当前已 ingest 的页面来看，资源流动大致可以概括为：

- `Quests` 提供 `XP`，推动 `Brawl Pass`
- `Daily Wins` 作为日常胜利机制，会发放与 `Starr Drops` 相关的奖励
- `XP Doublers` 会放大部分 `XP` 获取效率
- `Brawl Pass`、`Daily Streak`、`Trophy Road`、`Mega Pig` 会发放 `Credits`、`Coins`、`Power Points`、`Bling`、`Starr Drops`
- `Credits` 流向 `Starr Road`
- `Brawler Keys` 作为补充解锁资源，可直接用于部分英雄兑换
- 英雄全解锁后，额外 `Credits` 会流向 `Fame`
- `Coins` 与 `Power Points` 流向英雄升级和战力组件
- `Gems` 与 `Bling` 流向 `Catalog`
- `Trophies` 推进 `Trophy Road`
- `Ranked` 使用独立的 `Rank / Elo` 体系推进，不消耗也不增加 `Trophies`

## 解锁

当前最明确的解锁资源是 [[concepts/Credits|Credits]]。

它的核心作用是通过 `Starr Road` 解锁英雄。和升级资源不同，Credits 不直接提升战力，而是负责把英雄从“未拥有”推进到“已拥有”。

这一层的关键特点是：

- 资源的目标是“获取新英雄”
- 资源的终点是“完成解锁”
- 多余 Credits 在英雄全解锁后会转向 `Fame`
- `Starr Road` 是这一层最核心的结构化出口

## 升级

当前已确认的升级资源是 [[concepts/Power Points|Power Points]] 与 [[concepts/Coins|Coins]]。

其中 Power Points 是专用升级资源，Coins 是更广泛的通用强化货币。二者共同构成英雄从低等级到高等级的成长成本。

这一层的关键特点是：

- `Power Points` 更像“等级推进材料”
- `Coins` 更像“通用强化资金”
- 两者一起决定英雄成长速度
- Coins 还会延伸到多个战力组件的购买
- `Gears` 等战力组件让 Coins 的用途超出单纯升级

## 赛季推进燃料

当前已经可以把 [[concepts/XP|XP]] 视为一类单独的重要进度资源。

XP 不直接解锁英雄，也不直接提升英雄战力，但它决定 `Brawl Pass` 的推进速度，因此影响玩家获得赛季奖励的节奏。

这一层的关键特点是：

- `XP` 是赛季进度燃料
- `Quests` 是 XP 的关键入口
- `Brawl Pass` 是 XP 的主要承接结构
- `Daily Wins`、活动奖励等系统会与这一层发生间接联动
- `XP Doublers` 是这一层最典型的进度加速器

## 高级货币

当前已确认的高级货币是 [[concepts/Gems|Gems]]。

Gems 的特征不是“只做一件事”，而是兼具付费、加速、补差和跨系统购买能力。它能购买英雄、外观、资源包，也能购买 Coins 或 Power Points。

这一层的关键特点是：

- `Gems` 覆盖面最广
- 它既是购买货币，也是加速货币
- 它能插入到解锁和升级链条里

## 外观货币

当前已确认的外观货币是 [[concepts/Bling|Bling]]。

Bling 更专注于 cosmetic 消费，用于 Catalog 中的皮肤、Pins、Sprays、Profile Icons。它把外观消费从核心战力资源中进一步拆出来。

这一层的关键特点是：

- `Bling` 服务于外观而不是战力
- 它和 `Gems` 在外观购买上有部分重叠
- 它更适合被理解成“cosmetic progression 货币”
- `Catalog` 是这一层最清晰的消费入口

## 进度指标

当前已确认的进度指标是 [[concepts/Trophies|Trophies]]。

Trophies 不是消耗型货币，而是表现与推进的量化记录。它既反映单个英雄的推进，也汇总成玩家总 Trophy 数，并影响部分匹配和分段体验。

这一层的关键特点是：

- `Trophies` 记录进度，不负责消费
- 它同时和英雄、账户、模式表现有关
- 它是后续理解 Trophy Road 和 Ranked 的基础
- `Trophy Road` 是 Trophies 最直接的长期奖励轨道

## 历史系统层

除了现行系统之外，当前 wiki 里已经出现一层重要的历史机制：

- `Power League`
- `Club Games`
- `Club League`
- `Club Quests`
- `Club Coins`

这一层的价值不在于指导当前玩法，而在于解释系统演化：

- `Power League` 是 `Ranked` 的前史
- `Club Games` 与 `Club League` 解释了俱乐部竞技系统如何演化到 `Mega Pig`
- `Club Coins` 解释了旧俱乐部奖励为何与当前资源结构不同

把这层独立出来，能避免把历史规则误当成现行规则。

## 现在已经比较清楚的边界

- `Credits` 负责解锁
- `Starr Road` 承接 Credits 并把解锁过程结构化
- `Fame` 承接全解锁后的 Credits 溢出
- `Power Points` 负责升级
- `Coins` 负责更广泛的强化和购买
- `XP` 负责赛季推进
- `XP Doublers` 负责加速赛季推进
- `Gems` 负责高级购买、加速和补差
- `Bling` 负责外观消费
- `Catalog` 是 Gems / Bling 的关键消费场景
- `Trophies` 负责记录推进
- `Trophy Road` 负责把 Trophies 转为里程碑奖励
- `Quests` 与 `Brawl Pass` 共同构成赛季推进入口
- `Daily Wins` 是日常奖励循环的一部分
- `Brawler Keys` 为英雄解锁提供了补充路径
- `Mega Pig` 是偏俱乐部协作型的周期资源入口
- `Ranked` 是独立于 Trophy 体系的竞技进度入口
- `Club` 是单个俱乐部组织单位
- `Clubs` 是俱乐部系统总称
- `Power League` 是历史排位系统
- `Club Games` / `Club League` / `Club Quests` / `Club Coins` 属于历史俱乐部竞技层

这套边界已经足够支撑下一阶段的 ingest，但还不是最终版。

## 仍然开放的问题

- `Gems` 和 `Coins` 的边界在实践中并不完全对称，尤其在“购买什么”与“可替代什么”上还需要继续补充更多页面。
- `Bling` 和 `Gems` 在外观消费上的分工仍有重叠，需要后续通过更多 `Catalog` 子页面、皮肤页和活动页进一步厘清。
- `Trophies` 和 `Ranked` 的关系已经初步明确为“相互独立但存在解锁门槛关联”，后续仍需更多模式页补充细节。
- `Mega Pig`、`Daily Streak`、`Starr Drops` 三者之间的奖励边界仍有继续细化的空间。
- `Club` 与 `Clubs` 目前采取“单个组织 / 系统总称”双页并存，后续如果内容高度重叠，可再做剪枝合并。
- `Brawler Keys` 与 `Credits`、`Starr Road` 的关系仍值得继续观察，尤其是它在解锁路径中的稀缺性和定位。
- `XP Doublers` 对哪些 XP 来源生效、哪些不生效，后续仍值得更细地校准。
- 历史俱乐部系统和现行 `Mega Pig` 之间已经建立演化关系，但仍可继续补充更细的过渡信息。

## 下一步建议

下一步最值得补齐的是：

- `Star Points`
- `Boxes`
- `Club Shop`
- `Daily Freebie`
- `Records`

这些页面补完后，这篇综述就可以从“资源分类图”升级成“资源流动图”，也就是进一步回答资源从哪里来、流向哪里、为什么会这样流动。
