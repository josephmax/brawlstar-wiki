# Dry Season

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Bounty`
- Fandom URL：https://brawlstars.fandom.com/wiki/Dry_Season
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Dry Season
  mode: Bounty
  summary: 极开阔低掩体 Bounty 图，远程命中率、薄掩体破坏、领先后保命和短手失效判断最关键。
  topology:
    key_points:
      - 中路和边路长线开阔，掩体少且多为薄墙。
      - 星星模式放大生存和低风险消耗，死亡成本高。
      - 墙体一旦被打开，短手接近路线更少。
  objective_access:
    objective_type: bounty_star
    stable_goal: Bounty 的目标是低风险拿星并保领先；地图开阔使远程命中和视野控制优先于爆发进场。
  tactical_features:
    - id: extreme_open_mid
      type: long_sightline
      location: whole_mid
      condition: 极开阔中路奖励远程命中率和走位
      combat_effect:
        rewards_capabilities: [marksman_range, projectile_reliability, long_range_support, low_commitment_poke]
        punishes_capabilities: [short_range_engage, grass_dependent_assassin]
        false_positive_capabilities: [sniper_with_slow_unreliable_projectile_against_mobility]
      objective_effect:
        payoff: 远程能在不交身位的情况下拿星
      draft_implication:
        bp_use: 先手应优先稳定长线或能保护长线的支援
    - id: thin_cover_break_value
      type: wall_break_transform
      location: thin_cover_pieces
      condition: 少量掩体被破后会显著扩大长线优势
      combat_effect:
        rewards_capabilities: [wall_break_snowball, range_after_opening, thrower_denial]
        punishes_capabilities: [thrower_if_cover_removed, short_range_after_cover_removed]
        false_positive_capabilities: [overbreaking_if_our_comp_needs_cover]
      objective_effect:
        payoff: 破墙会让领先方更容易控线
      draft_implication:
        bp_use: 开墙可作为反投掷/反短手工具
    - id: short_range_false_positive
      type: false_positive_feature
      location: all_lanes
      condition: 短手缺少接近路线，除非 draft 已提供硬控或掩护
      combat_effect:
        rewards_capabilities: [forced_push_with_teammate_cc, last_pick_into_no_peel]
        punishes_capabilities: [blind_assassin_pick, tank_without_cover]
        false_positive_capabilities: [counter_pick_based_only_on_target_name]
      objective_effect:
        payoff: 短手通常难以稳定拿星
      draft_implication:
        bp_use: 只有最后手惩罚脆弱三远程时才考虑
  lane_dynamics:
    notes:
      - 默认长线分散站位，避免被单个技能多目标命中。
      - 领先方应减少进攻承诺，迫使敌方穿越开阔区。
      - 墙体存在时投掷有局部价值，墙体被破后迅速贬值。
  map_rules:
    - if: 我方没有远程命中或支援
      then: BP 基本面不合格
      because: 地图不提供短手免费接近路线
      bp_use: 优先补极长线
    - if: 敌方有投掷依赖薄墙
      then: 开墙会同时削弱投掷和短手
      because: 掩体数量少，破掉后难以恢复
      bp_use: wall_break 是高价值回答
    - if: 敌方无 peel 且三远程极脆
      then: 短手只能作为高风险最后手
      because: 需要确认接近路线或队友开路
      bp_use: 不适合作早手
  false_positive:
    - 用“刺客克制狙击”套这张图很危险；没有草/墙/跳板时刺客接近成本过高。
    - 投掷不能在墙被破后继续按强势处理。
```

## BP 用法

- 如果 `我方没有远程命中或支援`，则 `BP 基本面不合格`；BP 上用于：优先补极长线。
- 如果 `敌方有投掷依赖薄墙`，则 `开墙会同时削弱投掷和短手`；BP 上用于：wall_break 是高价值回答。
- 如果 `敌方无 peel 且三远程极脆`，则 `短手只能作为高风险最后手`；BP 上用于：不适合作早手。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
