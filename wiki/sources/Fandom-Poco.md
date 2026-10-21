# Fandom 来源摘要: Poco

## 来源信息

- 标题：Poco
- 来源：[Poco | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Poco)
- 读取日期：2026-10-21
- Fandom 页面最后编辑：2026-10-19T09:18:37Z
- 分类：Brawlers / Fandom hero page
- 上游 raw：[[../../raw/sources/fandom/heroes/poco.md]]
- source_quality：direct_raw_capture
- source_type：official_or_wiki_mechanics

## 可用范围

- usable_for: stable_mechanics, ability_candidates, build_candidates_from_tips, mode_fit_candidates, map_feature_candidates
- not_usable_for: current_meta_strength_without_overlay, final_counter_claim, unconditional_bp_recommendation

## 页面核心字段

- 稀有度: Rare
- 官方定位: Support
- 移动速度: 750 (Normal)
- 生命值: 4000
- 攻击距离: 7 (Long)
- 装填: 1.6 seconds (Normal)
- 普攻数值: 760
- Super 距离: 9.33 (Very Long)
- Super 数值: 2100
- Gadgets: Tuning Fork, Protective Tunes

## BP 建模可抽取信号

- `普攻 / Super / Gadget / Star Power / Hypercharge` 可以拆成稳定机制原子。
- `Tips / Recommended Build` 只能进入候选层；如果涉及模式或地图，后续必须转成 objective contract 或 map feature hook。
- 本页不直接生成 counter 或 pick 顺位结论。

## 抓取覆盖

- Lead excerpt
- Attack: Power Chord
- Super: Encore
- Gadgets / Tuning Fork
- Gadgets / Protective Tunes
- Star Powers / Da Capo!
- Star Powers / Screeching Solo
- Hypercharge: Medic's Melody
- Tips / Game Modes and Maps
- Tips / Recommended Build
- Tips / Strategies
- Tips / Other

## 与本地 wiki 的意义

- `Poco` 的 Fandom 页面已有 direct raw，可作为稳定机制来源。
- 后续升级 [[entities/brawlers/Poco|Poco]] 时，应优先从本 raw 抽取机制事实，再与 [[sources/PLP-Poco|PLP 竞技信号]] 分层合并。

## 来源差异备注（2026-09-03）

- 官方 Release Notes August 2026 与当前 Fandom 页在 Poco 重做数值上存在明显口径差，本库以当前 direct raw 为稳定事实：Tuning Fork raw 为治疗 `1000`×3（12.5% 最大生命/秒、3 秒 buff、3.33 格半径；release notes 写 400×3/6 秒）；Tuning Fork Buffied 加速 raw 为 `3 秒`（release notes 写 2 秒）；Da Capo! raw 为额外治疗 `640`（约 13% 最大生命；release notes 写基线 300+220）；Screeching Solo raw 为 `1520`（release notes 写 760）。Protective Tunes 与沉默时长两源一致。

## 关联页面

- [[entities/brawlers/Poco|Poco]]
- [[sources/PLP-Poco|PLP 来源摘要: Poco]]

## 2026-10-21 补丁 BP 修复复核

Tuning Fork 引语/正文每波 1400，启动时及 2、4 秒各一波，共三波；不是每秒一次。Da Capo 引语额外 800，加基础 400 后 Power 11 合计 1200（8000 HP 的 15%）。Gadget/Star infobox 与引语混用等级，不机械翻倍。
