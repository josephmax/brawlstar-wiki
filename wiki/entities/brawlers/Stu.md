# Stu

## 基本信息

- 稀有度：Epic
- 定位：Damage Dealer
- 类型：机动型输出英雄

## 攻击特征

- 主攻击命中后能快速建立位移节奏
- 适合边打边换位置
- 很依赖操作和节奏把控

## 超级技能特征

- Super 会进行短距离冲刺
- 可以用来穿越危险区域或追击
- 很适合连续切换进攻和撤退节奏

## 适合场景

- 需要频繁转点的模式
- 地图中有很多可利用路径时
- 适合高操作、快节奏的对局

## 角色定位总结

Stu 是一个靠命中触发冲刺、持续改位来打节奏的机动输出英雄，强在速度感和连贯操作。

## 关联页面

- [[sources/Fandom-Stu|Fandom 来源摘要: Stu]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-29"
    user_notes: "none"

  capability_vector:
    effective_range: mid_long
    projectile_reliability: high_if_first_projectile_lands; one hit fully charges Super
    burst: high_in_short_windows
    sustained_dps: medium; normal reload but repeated dash poke creates uptime
    objective_damage: low_medium
    mobility: very_high_if_hits_land
    survivability: medium_high_with_dash_chain_or_Gaso_Heal
    engage: high; dash chain turns hit into immediate reposition
    disengage: high; one hit can reset escape
    anti_aggro: high_against_linear_close_range_if_Super_charged
    anti_tank: medium; kites but can be body-blocked or out-sustained
    wall_break: conditional_with_Breakthrough
    throw_or_wall_bypass: low
    area_control: medium; fire trail and Speed Zone control routes
    scouting_or_vision: low
    team_support: medium_high_with_Speed_Zone
    terrain_destruction: conditional
    source_trace:
      - "[[sources/Fandom-Stu|Fandom-Stu]]"
      - "[[sources/PLP-Stu|PLP-Stu]]"

  build_switches:
    - build: "Speed Zone / Zero Drag / Shield, Damage"
      source: "[[sources/PLP-Stu|PLP-Stu]]"
      changes_capabilities:
        - "Speed Zone creates a protected team speed anchor"
        - "Zero Drag extends dash range for sniper lanes, self-pass and anti-aggro spacing"
        - "Shield/Damage supports repeated skirmishes"
      enables:
        - dash_chain_lane_pressure
        - team_speed_anchor
        - Brawl_Ball_self_pass_and_defense
      mitigates_failure_modes:
        - low_range_vs_snipers
        - linear_close_range_pressure
      poor_when:
        - "地图非做不可职责是开墙，或敌方能轻易摧毁 Speed Zone"
      bp_use: default_reviewed_build_for_mobility_control
    - build: "Breakthrough / Gaso-Heal terrain or sustain variant"
      source: "[[sources/Fandom-Stu|Fandom-Stu]]"
      changes_capabilities:
        - "Breakthrough lets next Super destroy walls and send debris"
        - "Gaso-Heal restores health every Super use"
      enables:
        - selective_wallbreak
        - self_sustain_dash_loop
      mitigates_failure_modes:
        - wall_blocked_escape_or_goal
        - chip_damage_during_dash_cycle
      poor_when:
        - "需要团队速度或长 dash 进出，而不是单次开墙/回血"
      bp_use: map_or_enemy_specific_build_switch

  map_feature_hooks:
    - map_feature_type: "dash_chain_lane_pressure"
      uses_feature_by: "one projectile hit fully charges dash, enabling poke-in and dash-out loops"
      route_or_position: "semi-open lane where Stu can land first hit and choose retreat or engage"
      objective_conversion: "Hot Zone contest, Gem side lane pressure, Brawl Ball tempo"
      active_when: "enemy cannot hard CC the dash and Stu has room to chain angles"
      fails_if: "shots are blocked by summons/walls or enemy can body him after dash"
      example_maps:
        - Ring of Fire
        - Open Business
        - Hard Rock Mine
        - Center Stage
        - Crystal Arcade
      bp_use: required_capabilities.mobile_lane_pressure
    - map_feature_type: "wall_break_transform"
      uses_feature_by: "Breakthrough can destroy obstacles during Super"
      route_or_position: "goalpost, escape wall, or thin wall protecting a thrower/pocket"
      objective_conversion: "Brawl Ball scoring lane, escape route, or anti-cover answer"
      active_when: "specific wall removal benefits our team immediately"
      fails_if: "wallbreak exposes Stu's team to stronger enemy range or removes friendly cover"
      example_maps:
        - Sneaky Fields
        - Triple Dribble
        - Gem Fort
        - Shooting Star
      bp_use: terrain_state_plan.transform
    - map_feature_type: "speed_zone_anchor"
      uses_feature_by: "Speed Zone turret grants allied speed in a protected radius"
      route_or_position: "protected wall near mid, spawn route, or zone approach"
      objective_conversion: "faster return to zone, stronger lane dodge, team collapse window"
      active_when: "turret can be protected from free shots and team path crosses its radius"
      fails_if: "enemy instantly destroys turret or map routes do not pass through anchor"
      example_maps:
        - Parallel Plays
        - Dueling Beetles
        - Hard Rock Mine
        - Center Stage
      bp_use: map_bp_factors.team_speed_anchor

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - mobile_side_lane_pressure
        - speed_anchor_for_mid_return
        - chase_exposed_carrier
      cannot_fulfill:
        - safe_gem_carrier
        - hard_bush_vision
      needs_teammate_support:
        - mid_anchor_or_carrier
        - anti_tank_if_enemy_can_body_mid
      false_positive: "Dash pressure does not secure gems if mid lacks carrier safety"
    - mode: "Brawl Ball"
      can_fulfill:
        - self_pass_and_dash
        - anti_scorer_kite
        - optional_goal_wall_break_with_Breakthrough
      cannot_fulfill:
        - tank_body_score_without_space
        - guaranteed_knockback_defense
      needs_teammate_support:
        - scorer_or_wallbreak_if_Stu_uses_Speed_Zone
        - anti_tank_or_area_clear
      false_positive: "Dash mobility is not enough if Stu cannot charge Super before a defensive moment"
    - mode: "Hot Zone"
      can_fulfill:
        - zone_touch_and_escape
        - speed_zone_return
        - poke_to_force_enemies_off_zone
      cannot_fulfill:
        - pure_body_on_zone
        - long_duration_area_denial
      needs_teammate_support:
        - zone_body_or_thrower_clear
        - protection_for_Speed_Zone
      false_positive: "Stu can contest zone repeatedly but may not hold it alone"

  failure_modes:
    - id: "dash_chain_requires_hit"
      active_when: "Stu cannot land the first projectile due to walls, summons, or strong dodge pattern"
      exposed_by: "[[sources/Fandom-Stu|Fandom-Stu]] Super charges from attack hit"
      mitigation: "pick maps with hittable lanes or pair with slow/pull"
      bp_use: "candidate_eval.execution_risk"
    - id: "body_or_control_interrupts_dash_plan"
      active_when: "enemy tanks, slows, pulls, or stuns on the route Stu must dash through"
      exposed_by: "[[sources/PLP-Stu|PLP-Stu]] counteredBy tank/control signals"
      mitigation: "avoid hard control lanes, keep Super for escape, or draft anti-tank"
      bp_use: "must_avoid_or_needs_support"
    - id: "terrain_transform_backfires"
      active_when: "opened lane improves enemy range or engage more than ours"
      exposed_by: "[[sources/Fandom-Stu|Fandom-Stu]] Breakthrough wall destruction"
      mitigation: "define exact wall and follow-up before using Breakthrough"
      bp_use: "terrain_state_plan_check"
    - id: "speed_zone_removed"
      active_when: "enemy can shoot or throw onto Speed Zone for free"
      exposed_by: "[[sources/Fandom-Stu|Fandom-Stu]] Speed Zone is a decaying 1000-health turret"
      mitigation: "place behind protected wall or use another gadget/build"
      bp_use: "map_factor_false_positive_check"

  conditional_matchup_seeds:
    - target:
        - "Sprout"
        - "Dynamike"
        - "Piper"
        - "Tick"
        - "Ziggy"
        - "Gigi"
        - "Mandy"
        - "Squeak"
      direction: "subject_favored"
      source: "[[sources/PLP-Stu|PLP-Stu]]"
      mechanism: "dash chain lets Stu dodge skillshots, close onto throwers/snipers, or break their cover timing"
      active_when: "Stu can land one hit and target lacks protected pocket or hard peel"
      fails_when: "walls/summons deny hit, or target has teammate control on Stu's dash route"
      bp_use: "response_pick_candidate_against_skillshot_or_thrower"
    - target:
        - "Rosa"
        - "Damian"
        - "Ash"
        - "Poco"
        - "8-Bit"
        - "Ollie"
        - "Frank"
        - "Nita"
      direction: "target_favored"
      source: "[[sources/PLP-Stu|PLP-Stu]]"
      mechanism: "high health, area control, spawnables or sustain can absorb Stu's poke and punish dash endpoints"
      active_when: "objective forces Stu into short range or enemy can body-block lanes"
      fails_when: "Stu has open kiting space, anti-tank teammate, or wallbreak isolates target"
      bp_use: "avoid_or_pair_with_anti_tank"
    - target:
        - "Edgar"
        - "Kit"
        - "Mortis"
        - "Mico"
      direction: "subject_favored"
      source: "[[sources/Fandom-Stu|Fandom-Stu]]"
      mechanism: "one-hit Super charge and Zero Drag can dodge direct jump/dash engage and kite out of range"
      active_when: "Stu keeps Super charged or can land a projectile before contact"
      fails_when: "enemy chains CC, catches Stu without ammo/Super, or blocks retreat path"
      bp_use: "anti_aggro_response_candidate"

  slot_notes:
    slot_1: "可在 Brawl Ball/Hot Zone/Gem 作为高机动先手，但要避开敌方 2-3 位坦克控制组合。"
    slot_2_3: "适合回答长线/投掷或给队伍 Speed Zone 节奏，需确认有队友补站点/目标身体。"
    slot_4_5: "用于修补机动、开墙或反突进；注意不要把墙开给敌方长线。"
    slot_6: "当敌方缺硬控、缺召唤物且后排暴露时，Stu 可作为高操作惩罚位。"
```

## 关联页面

- [[sources/Fandom-Stu|Fandom 来源摘要: Stu]]
- [[sources/PLP-Stu|PLP 来源摘要: Stu]]
- [[sources/BSC-2026-July-Observed-Map-Fit-Review|BSC 2026 July 地图适配复核]]
