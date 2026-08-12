# Fandom 来源摘要: Nori

## 来源信息

- 标题：Nori
- 来源：[Nori | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Nori)
- 读取日期：2026-07-11
- Fandom 页面最后编辑：2026-07-10T10:20:45Z
- 分类：Brawlers / Fandom hero page
- 上游 raw：[[../../raw/sources/fandom/heroes/nori-2026-07-11.md]]
- source_quality：direct_raw_capture
- source_type：official_or_wiki_mechanics

## 可用范围

- usable_for: stable_mechanics, ability_candidates, build_candidates_from_tips, mode_fit_candidates, map_feature_candidates
- not_usable_for: current_meta_strength_without_overlay, final_counter_claim, unconditional_bp_recommendation

## 页面核心字段

- 稀有度: Legendary
- 官方定位: Assassin
- 第 105 位 Brawler（Previous: Pierce，Next: Kaze）
- 移动速度: 820 (Very Fast)；984 (with His Mother's Son)
- 生命值: 3800
- 攻击距离: 8.33 (melee; Very Long)；13.33 (ranged; Very Long)；16.67 (hook; Very Long)
- 装填: 0.1 seconds (Very Fast)，ammo-bar 充能型（类似 Hank / Angelo），满充 2 秒
- 普攻 AttackSuperCharge: 26% (melee) / 16.67% (ranged) / 16.67% (hook)
- AttackSpeed / SuperSpeed: 4000

### 普攻：Fishing Fury（双形态，tap/hold 切换）

- Tap（Melee Damage 1100）：快速挥杆，近身弧形 AOE，可一次命中多敌并一次收多条鱼。
- Hold（Dash/Ranged Damage 720）：充能 ammo bar → 释放钩子；钩墙把自己拉过去（满充可跳墙），钩敌造成低伤并在位移途中碰撞造成伤害。每钩只收 1 条鱼。
- 充能期间不能自然回血（草丛隐身仍生效）；被 stun / push / knock 取消充能。

### 鱼资源系统

- 命中敌人收鱼，上限 10 条。Tap 可一次收多条，Hold 每次最多 1 条。
- 鱼是 Super 成长与 Gadget1（Sushi Snack）的燃料。

### Super：Catch of the Day

- 跳向目标点落地后消失，生成水坑，1 秒延迟后召唤巨鱼，对坑内敌人造成范围伤害。
- SuperSpread: 360°；SuperSuperCharge: 9-36% (min to max range)。
- Min Damage 1250 / Max Damage 1750。
- 成长机制：消耗全部鱼，每条鱼 +5% 坑半径、+4% 巨鱼伤害（即使空命中也消耗）。结束后 Nori 在坑中心重现。

### Gadgets

- Sushi Snack（G1，CD 12s）：吃最多 3 条鱼，每条治疗。**口径冲突**：Infobox `Gadget1` = 700/鱼，Quote = 1000/鱼；PLP payload 用 1000/鱼。不足 3 条则少吃少奶。
- Gonna Need a Bigger Net（G2，CD 20s）：投网，造成伤害并 root 1.25 秒。**口径冲突**：Infobox `Gadget2` = 480，Quote = 800；PLP payload 用 800。

### Star Powers

- Big Haul：Super 命中敌方 Brawler 时每名收 3 鱼（坑内人越多收越多，伤害结算后才收，不影响本次 Super）。
- His Mother's Son：普攻命中后 +20% 移速 1 秒（不叠加）→ 820 → 984 的来源。

## BP 建模可抽取信号

- `普攻 / Super / Gadget / Star Power` 可以拆成稳定机制原子。
- `Tips / Recommended Build` 只能进入候选层；如果涉及模式或地图，后续必须转成 objective contract 或 map feature hook。
- 本页不直接生成 counter 或 pick 顺位结论。

## 来源冲突审计

- Sushi Snack 治疗：Fandom Infobox `700/鱼` vs Fandom Quote `1000/鱼` vs PLP `1000/鱼`。当前以 Quote / PLP 的 `1000/鱼` 为较新值，但 Infobox 字段未闭合，断点审计只能用 Infobox 结构化值。
- Gonna Need a Bigger Net 伤害：Fandom Infobox `480` vs Fandom Quote `800` vs PLP `800`。同上。
- 2026-08-04 Supercell 维护笔记含 3 条 Nori bug fix（见 [[sources/Supercell-Maintenance-August-4-2026|Maintenance - August 4, 2026]]）：满充 NanoPower 后可跳越障碍、dash 中投出 Super 不再被取消、dash 不再打断 Gene Super。Fandom raw 拍摄于 2026-07-11，上述 fix 未反映在当前 Fandom 页面文本中。

## 抓取覆盖

- Lead excerpt
- Attack: Fishing Fury
- Attack: Fishing Fury / Tap Attack
- Attack: Fishing Fury / Hold Attack
- Attack: Fishing Fury / Fish
- Super: Catch of the Day
- Gadgets / Sushi Snack
- Gadgets / Gonna Need a Bigger Net
- Star Powers / Big Haul
- Star Powers / His Mother's Son

## 与本地 wiki 的意义

- `Nori` 的 Fandom 页面已有 direct raw，可作为稳定机制来源。
- 后续升级 [[entities/brawlers/Nori|Nori]] 时，应优先从本 raw 抽取机制事实，再与 [[sources/PLP-Nori|PLP 竞技信号]] 分层合并。

## 关联页面

- [[entities/brawlers/Nori|Nori]]
- [[sources/PLP-Nori|PLP 来源摘要: Nori]]
