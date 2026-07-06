# Backyard Bowl

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Backyard_Bowl
- 来源：[[sources/Fandom-Backyard-Bowl|Fandom 来源摘要: Backyard Bowl]]
- 辅助来源：[[sources/Fandom-Brock|Fandom 来源摘要: Brock]]、[[sources/Fandom-Otis|Fandom 来源摘要: Otis]]、[[entities/brawlers/Bea|Bea]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-07-06

## BP-ready map_profile

```yaml
map_profile:
  name: Backyard Bowl
  mode: Brawl Ball
  summary: 开阔 Brawl Ball 图，长线压制、有限草墙入口、球门前可破障碍和门前防冲控制决定 BP。
  topology:
    key_points:
      - 地图整体开阔，只有许多小草块和很少墙体掩护。
      - 每个球门前都有一条长障碍带，默认只留 3 格进球开口，破墙后可扩到 7 格。
      - 右侧球门附近有 L 形草，中心入口附近每侧各有墙草簇。
      - 地图对角对称，开墙会快速把局面推向更纯粹的开阔长线。
  objective_access:
    objective_type: goal
    stable_goal: 目标是先用长线或宽弹道压出球权，再通过破门、强控、传球或位移把线权转为进球；防守侧要守住门前窄口和中心入口。
  tactical_features:
    - id: open_ball_long_lanes
      type: long_sightline_ball_lane
      location: mid_and_side_approach_lanes
      condition: 地图开阔且墙体掩护少，持球路线必须暴露在中远距离火力下
      combat_effect:
        rewards_capabilities: [long_range_pressure, projectile_reliability, wide_spread, anti_aggro_poke, open_lane_slow]
        punishes_capabilities: [short_range_without_speed_or_control, thrower_without_safe_pocket]
        false_positive_capabilities: [pure_scorer_with_no_lane_control]
      objective_effect:
        payoff: 远程压血能逼退守门人、保护持球者或迫使敌方交球
      draft_implication:
        bp_use: BP 需要至少一个能稳定占开阔球路的长线或宽弹道角色
    - id: goal_front_breakable_strip
      type: goal_barrier_transform
      location: front_of_each_goal
      condition: 球门前长条障碍把默认开口限制为 3 格，破墙后可扩到 7 格
      combat_effect:
        rewards_capabilities: [wall_break_for_goal, controlled_wall_break, long_range_after_opening, score_window_creation]
        punishes_capabilities: [poke_without_score_conversion, wall_break_that_opens_better_enemy_lanes]
        false_positive_capabilities: [breaking_goal_when_enemy_open_field_stronger]
      objective_effect:
        payoff: 破门可以扩大射门角度、减少绕门成本，并把敌方掩体转化为暴露点
      draft_implication:
        bp_use: 破门是重要但需评估双方长线强弱的 scoring-window 工具
    - id: small_bush_and_center_clusters
      type: limited_cover_entry
      location: small_bush_patches_and_center_opening_clusters
      condition: 小草块和中心入口墙草簇提供短暂藏身、拿球和充能点，但不形成连续安全草路
      combat_effect:
        rewards_capabilities: [bush_sweep, burst_from_short_cover, anti_flank_awareness, through_wall_or_over_wall_pressure]
        punishes_capabilities: [static_long_range_without_scout, mid_range_charging_behind_predictable_cover]
        false_positive_capabilities: [assassin_pick_because_some_bush_exists]
      objective_effect:
        payoff: 局部草墙可以制造抢球或侧路突进窗口，但必须接上控人/传球/破门
      draft_implication:
        bp_use: 短手和中程只在有速度、强控、扫草或队友破墙配合时成立
    - id: narrow_goal_choke_defense
      type: goal_choke_control
      location: goal_opening_and_near_goal_choke
      condition: 默认球门开口较窄，敌方持球冲门需要穿过门前窄口
      combat_effect:
        rewards_capabilities: [silence_or_stun_on_ball_carrier, knockback, slow_field, lane_block_super, goal_area_denial]
        punishes_capabilities: [dash_scorer_without_cleanse_or_support]
        false_positive_capabilities: [control_tool_if_enemy_can_shoot_from_opened_goal]
      objective_effect:
        payoff: 门前控制能迫使持球者停球、断传或只能步行进门，给防守方集火时间
      draft_implication:
        bp_use: 后手可用门前控制回答冲门阵容；若球门已被大幅打开，控制价值需重新评估
    - id: thrower_pocket_false_positive
      type: false_positive_feature
      location: limited_mid_walls
      condition: 地图缺少封闭空间，投掷主要只能借中场 1x3 墙或不可破墙短暂输出
      combat_effect:
        rewards_capabilities: [thrower_only_with_specific_mid_wall, temporary_cover_use]
        punishes_capabilities: [generic_lobber_without_peel]
        false_positive_capabilities: [drafting_thrower_because_brawl_ball_has_walls]
      objective_effect:
        payoff: 投掷难以长期保护球权或稳定制造进球窗口
      draft_implication:
        bp_use: 投掷必须作为条件后手，并确认敌方缺开墙/突脸/长线惩罚
  lane_dynamics:
    notes:
      - 默认以开阔中线和两侧推进线争球，长线换血会直接影响持球权。
      - 球门前障碍完整时，进球更依赖控人、传球、绕门或破门；破墙后长线和直射角度升值。
      - 小草块只能提供短暂进场和视野博弈，不能无条件保护短手穿过整条路线。
      - 中场墙草簇是中程充能和短手抢节奏点，但会被过墙、穿墙、投掷或破墙工具惩罚。
  map_rules:
    - if: 我方没有长线或宽弹道占球路
      then: 前期球权和防守站位都会被压缩
      because: 地图开阔且缺少可长期躲避的墙体
      bp_use: 优先补 open_lane_pressure 或 wide_spread_control
    - if: 我方无法破门或制造门前控制
      then: 击杀优势不一定能转化为进球
      because: 球门前障碍让默认射门窗口较窄
      bp_use: 补 wall_break_for_goal / knockback / slow / silence / dash_scorer
    - if: 敌方选择短手冲门
      then: 用扫草、减速、击退或门前沉默评估是否能守窄口
      because: 草墙只给局部接近，最终仍要穿过门前控制区
      bp_use: response pick anti_aggro_goal_defense
    - if: 准备用投掷
      then: 必须确认中场墙位能保护输出且敌方缺开墙回答
      because: Fandom 明确该图缺少投掷需要的封闭空间
      bp_use: thrower_as_conditional_last_pick_only
  false_positive:
    - “Brawl Ball 需要得分手”不等于纯短手可用；这张图的接近路线暴露，很容易被开阔长线压退。
    - “有草就能刺客”只在草块能接到目标、传球或门前控制时成立。
    - 破门不是无脑收益；如果敌方开阔长线更强，破墙可能帮对方获得更简单的防守和反推角度。
    - 投掷不是默认答案；本图墙体少，投掷需要具体中场口袋和队友保护。
```

## BP 用法

- 如果 `我方没有长线或宽弹道占球路`，则 `前期球权和防守站位都会被压缩`；BP 上用于：优先补 open_lane_pressure 或 wide_spread_control。
- 如果 `我方无法破门或制造门前控制`，则 `击杀优势不一定能转化为进球`；BP 上用于：补 wall_break_for_goal / knockback / slow / silence / dash_scorer。
- 如果 `敌方选择短手冲门`，则 `用扫草、减速、击退或门前沉默评估是否能守窄口`；BP 上用于：response pick anti_aggro_goal_defense。
- 如果 `准备用投掷`，则 `必须确认中场墙位能保护输出且敌方缺开墙回答`；BP 上用于：thrower_as_conditional_last_pick_only。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页、版本 / meta 覆盖层或 runtime strength profile，不反写成稳定地图事实。
