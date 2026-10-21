# Fandom 来源摘要: Nori

## 来源信息

- 标题：Nori
- 来源：[Nori | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Nori)
- 读取日期：2026-10-21
- Fandom 页面最后编辑：2026-10-13T20:14:49Z
- 分类：Brawlers / Fandom hero page
- 上游 raw：[[../../raw/sources/fandom/heroes/nori.md]]
- source_quality：direct_raw_capture
- source_type：official_or_wiki_mechanics
- 本次修复：原摘要链接的 canonical raw 缺失，2026-10-21 新抓当前原文；P1 HP 3500、满蓄力 2.5 秒、基础移速 855、Hypercharge 参数 28%。
- 来源冲突：Sushi Snack infobox 每鱼 800 与引语 1000、网 Gadget infobox 640 与引语 800 存在量纲/成长口径差异；本次不自动建立对应伤害/治疗包。

## 可用范围

- usable_for: stable_mechanics, ability_candidates, build_candidates_from_tips, mode_fit_candidates, map_feature_candidates
- not_usable_for: current_meta_strength_without_overlay, final_counter_claim, unconditional_bp_recommendation

## 页面核心字段

- 稀有度: Legendary
- 官方定位: Assassin
- 移动速度: 855 (Very Fast)<br>1026 (with His Mother's Son)
- 生命值: 3500
- 攻击距离: 8.33 (melee; Very Long)<br>13.33 (ranged; Very Long)<br>16.67 (hook; Very Long)
- 装填: 0.1 seconds (Very Fast)
- 普攻数值: 1000
- Super 距离: unknown
- Super 数值: 1250
- Gadgets: Sushi Snack, Gonna Need a Bigger Net

## BP 建模可抽取信号

- `普攻 / Super / Gadget / Star Power / Hypercharge` 可以拆成稳定机制原子。
- `Tips / Recommended Build` 只能进入候选层；如果涉及模式或地图，后续必须转成 objective contract 或 map feature hook。
- 本页不直接生成 counter 或 pick 顺位结论。

## 抓取覆盖

- Lead excerpt
- Attack: Fishing Fury
- Super: Catch of the Day
- Gadgets / Sushi Snack
- Gadgets / Gonna Need a Bigger Net
- Star Powers / Big Haul
- Star Powers / His Mother's Son
- Hypercharge: Master Fisherman
- Tips

## 与本地 wiki 的意义

- `Nori` 的 Fandom 页面已有 direct raw，可作为稳定机制来源。
- 后续升级 [[entities/brawlers/Nori|Nori]] 时，应优先从本 raw 抽取机制事实，再与 [[sources/PLP-Nori|PLP 竞技信号]] 分层合并。

## 关联页面

- [[entities/brawlers/Nori|Nori]]
- [[sources/PLP-Nori|PLP 来源摘要: Nori]]

## 2026-10-21 补丁 BP 修复复核

当前 Infobox 妙具值与引语、PLP 不同：不能混用 640/800/1000 等数值计算一套爆发。BP 只保留消耗鱼治疗与 root 机制；移速按同页 855→1026，满充 2.5 秒。
