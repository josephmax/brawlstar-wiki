# Fandom 来源摘要: Cosmo

![[../../raw/assets/brawlers/cosmo.webp]]

## 来源信息

- 标题：Cosmo
- 来源：[Cosmo | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Cosmo)
- 读取日期：2026-10-21
- Fandom 页面最后编辑：2026-10-01T06:37:23Z
- 分类：Brawlers / Fandom hero page
- 上游 raw：[[../../raw/sources/fandom/heroes/cosmo-2026-10-21.md|10-21 完整抓取]]；[[../../raw/sources/fandom/heroes/cosmo.md|10-16 抓取]]保留其当时的抽取覆盖，两次页面修订时间相同。
- source_quality：direct_raw_capture
- source_type：official_or_wiki_mechanics

## 可用范围

- usable_for: stable_mechanics, ability_candidates, build_candidates_from_tips, mode_fit_candidates, map_feature_candidates
- not_usable_for: current_meta_strength_without_overlay, final_counter_claim, unconditional_bp_recommendation

## 页面核心字段

- 稀有度: Mythic
- 官方定位: Controller
- 移动速度: 750 (Normal)
- 生命值: 3400
- 攻击距离: 9 (Long)
- 装填: 2 seconds (Slow)
- 普攻数值: 250
- 最大单弹普攻数值: 1000（以上数值均 Power 1；三枚公转弹、随距离成长，不把裸 Attack 乘弹数当完整一发）
- 发布状态：2026-09-10 提前获取，2026-10-01 常规获取；完整 History 原文已留存。
- Super 距离: 9.33 (Very Long)
- Super 数值: 500
- Gadgets: Planetary Pushback, Telescope Trap

## BP 建模可抽取信号

- `普攻 / Super / Gadget / Star Power / Hypercharge` 可以拆成稳定机制原子。
- `Tips / Recommended Build` 只能进入候选层；如果涉及模式或地图，后续必须转成 objective contract 或 map feature hook。
- 本页不直接生成 counter 或 pick 顺位结论。

## 抓取覆盖

- Lead excerpt
- Attack: Orbit
- Super: Gravitation Pull
- Gadgets / Planetary Pushback
- Gadgets / Telescope Trap
- Star Powers / Precession
- Star Powers / Ammo Attractor
- Tips / Game Modes and Maps
- Tips / Recommended Build
- Tips / Strategies
- Tips / Other

## 与本地 wiki 的意义

- `Cosmo` 的 Fandom 页面已有 direct raw，可作为稳定机制来源。
- 后续升级 [[entities/brawlers/Cosmo|Cosmo]] 时，应优先从本 raw 抽取机制事实，再与 [[sources/PLP-Cosmo|PLP 竞技信号]] 分层合并。

## 关联页面

- [[entities/brawlers/Cosmo|Cosmo]]
- [[sources/PLP-Cosmo|PLP 来源摘要: Cosmo]]

## BP 复核（2026-10-28）

以 10-21 抓取、10-01 页面修订为机制证据，本次没有将维护日期冒充来源更新日期。复核后建立 [[entities/brawlers/Cosmo|Cosmo BP profile]]：六模式职责、四条地图路线、两种妙具配装、失败条件及逐目标条件对位。

- 采纳 Orbit 距离成长、2 秒装填；Power 11 生命 6800，单弹随距离 500–2000，但不推定三弹全中。
- 采纳 Super 先命中目标、随后区域内弹道吸引、持续 6 秒；不推定穿墙、必中、瞬杀或同时穿透英雄打金库。
- Precession 增加公转速度，不是弹道前进速度。Telescope Trap 是有区域和持续时间的限制，不等于全场封锁或必定中断已开始的位移。
- 对位判断是维护者依据双方机制和 PLP 方向进行的条件推导，不是实测胜率结论；逐条记录见 [[PLP-Cosmo#逐目标复核（2026-10-28）]]。
- 地图依据来自 Hideout、Shooting Star、Out in the Open、Bridge Too Far 实体。LCQ 只证明在 Hideout 有选用，不证明该阵容或英雄占优。
