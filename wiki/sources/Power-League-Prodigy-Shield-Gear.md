# Power League Prodigy 来源摘要：Shield Gear

## 来源信息

- 来源：Power League Prodigy 多个英雄 guide payload 中重复出现的 Gear 定义
- 抽检上游 raw：[[../../raw/sources/pl-prodigy/brawlers/belle-2026-06-29|Belle PLP raw]]、[[../../raw/sources/pl-prodigy/brawlers/brock-2026-06-29|Brock PLP raw]]、[[../../raw/sources/pl-prodigy/brawlers/max-2026-06-29|Max PLP raw]]
- 读取日期：2026-07-17
- source_quality：direct_raw_payload_repeated_across_brawler_guides
- source_type：third_party_game_data / gear_definition

## 可用范围

- usable_for: Shield gear 满值为 900、它是可消耗护盾、满血时经过 10 秒恢复
- not_usable_for: 游戏内部护盾/减伤逐帧结算顺序、不同来源同时减伤的叠加方式、特定英雄是否应该装备 Shield、当前强度

## 稳定字段

PLP 的 Gear payload 在多个英雄 guide 中使用同一描述：Shield gear 提供额外 `900 HEALTH` 的可消耗护盾；英雄满血时，护盾用 10 秒恢复。

断点审计因此把“交战开始时护盾已回满”建成条件变体 `shield_gear_full`，其 `barrier_hp = 900` 且数值已经是装备绝对值，不随 Power Level 换算。它不代表整场常驻 900，也不代表该 Gear 是默认或最优构筑。

## 关联页面

- [[concepts/伤害与生存断点|伤害与生存断点]]
- [[sources/User-Note-Balance-Breakpoint-Audit|用户维护规则：平衡调整伤害—生存断点审计]]
