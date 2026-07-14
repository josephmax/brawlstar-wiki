# Pinhole Punt

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Pinhole_Punt
- 来源：[[sources/Fandom-BSC-July-2026-Observed-Map-Pages|Fandom 来源摘要: BSC 2026 July 赛事补充地图页]]
- 赛事证据：[[sources/Liquipedia-Brawl-Stars-Championship-2026-July-South-America-Monthly-Finals|BSC 2026 July South America]]
- 适配复核：[[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 三张补充地图的适配复核]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-07-14

## BP-ready map_profile

```yaml
map_profile:
  name: Pinhole Punt
  mode: Brawl Ball
  summary: 中央方形草环、六个墙封草簇、横向 barricade 与双三格门口，使探草、中距离控球、前排推进、门前范围控制和选择性破门共同决定得分。
  topology:
    key_points:
      - 球出生点被厚实方形草边围住，开球阶段存在持续视野税和多方向 first contact。
      - 六个 2x3 草簇上下由墙封住，另有横墙、长墙与更小草簇提供阶段性掩体。
      - 每个球门有两个入口，每个入口只有三格宽，门前控制和破墙能直接改变射门角度。
  objective_access:
    objective_type: ball_control_and_goal_conversion
    stable_goal: 先扫清中央草环并建立球权，再通过前排/控场穿过墙封草簇，把线权转成窄门射门或选择性破门窗口。
  tactical_features:
    - id: center_square_bush_ring
      type: central_vision_tax
      location: thick_square_bush_border_around_ball_spawn
      condition: 中央草环完整，开球点和第一接触方向不可见
      combat_effect:
        rewards_capabilities: [bush_sweep, wide_spread, scouting_or_vision, area_control, mid_survivability]
        punishes_capabilities: [single_projectile_without_scout]
        false_positive_capabilities: [blind_short_range_entry]
      objective_effect:
        payoff: 先掌握草环视野的一方更容易拿球并逼出敌方控制
      draft_implication:
        bp_use: 阵容至少要有稳定探草或范围清场
    - id: six_wall_capped_bush_clusters
      type: protected_medium_range_staging
      location: six_2x3_bush_clusters_with_top_and_bottom_walls
      condition: 墙草完整，前排和中距离可分段推进但出口有限
      combat_effect:
        rewards_capabilities: [anti_aggro_poke, through_wall_or_over_wall_pressure, burst_from_short_cover, sustain_body]
        punishes_capabilities: [low_health_assassin_into_scout]
        false_positive_capabilities: [tank_without_support_or_exit]
      objective_effect:
        payoff: 给持球者/前排提供接近门区的中继点，也给防守方范围封口机会
      draft_implication:
        bp_use: 前排需要续航或队友控场，防守需要穿墙/范围处理
    - id: twin_three_tile_goal_entrances
      type: narrow_goal_chokes
      location: two_three_tile_openings_at_each_goal
      condition: 球必须经过三格门口，或阵容主动改变门前墙体
      combat_effect:
        rewards_capabilities: [goal_area_denial, knockback, slow_field, lane_block_super, wall_break_for_goal, score_window_creation]
        punishes_capabilities: [ball_carrier_without_reset_or_followup]
        false_positive_capabilities: [wall_break_without_scorer]
      objective_effect:
        payoff: 控制可制造防守 reset；选择性破墙可把一次赢线转成更宽射门角度
      draft_implication:
        bp_use: 必须同时覆盖进球转换与门前重置
    - id: side_bush_wait_and_counterpush
      type: side_ambush_and_counter_route
      location: upper_and_lower_side_bushes_behind_barricades
      condition: 正面推进被封时，侧草可保存身体并等待反击
      combat_effect:
        rewards_capabilities: [anti_flank_awareness, bush_sweep, counterpush, controlled_engage]
        punishes_capabilities: [vertical_only_push]
        false_positive_capabilities: [passive_bush_wait_without_ball_plan]
      objective_effect:
        payoff: 防守成功后从侧路接球反推，或逼敌方分散探草
      draft_implication:
        bp_use: 侧草价值必须连接球权或反推，不是单纯蹲草
  lane_dynamics:
    notes:
      - 开球阶段先处理中央草环，推进阶段利用墙封草簇分段接近，终结阶段围绕双窄门控制或破墙。
      - 中距离和高血身体比低血纯短手更稳定，但仍需要探草、控制与射门转换配合。
      - 防守方若只守垂直正面，会被侧草等待和反推路线拉开。
  map_rules:
    - if: 我方没有探草或范围清场
      then: 中央球权会被不可见 first contact 主导
      because: 球出生点被厚草环包围
      bp_use: hard_gate bush_sweep_or_vision
    - if: 我方前排进入墙封草簇但没有续航/控场跟进
      then: 会在有限出口被集火
      because: 草簇提供接近但不提供安全撤退
      bp_use: 前排必须绑定 support_or_control
    - if: 我方已经赢线但门口控制完整
      then: 需要击退、减速、封路或选择性破门制造射门窗口
      because: 两个三格入口容易被单个防守技能覆盖
      bp_use: slot_task.goal_conversion_or_reset
  false_positive:
    - 草多不代表 Edgar/Mortis/Kit 一类低血短手自动成立；Fandom 明确指出中远程与探草会限制其接近。
    - 破墙只有在己方有 scorer 或立即射门路线时才是收益，否则可能帮助敌方远程反推。
```

## BP 用法

- 第一任务是中央草环视野与球权，不满足时不应只靠近战猜草。
- 墙封草簇奖励有续航/控制支持的前排和中距离，不奖励无出口计划的单人突进。
- 双窄门要求阵容至少具备进球转换或门前 reset；破墙必须绑定 scorer。

## 变动层边界

本页不保存当前英雄强度或赛事胜率；逐 set 观察保留在 Liquipedia 来源，稳定英雄 map-fit 需经过机制与失效条件复核。
