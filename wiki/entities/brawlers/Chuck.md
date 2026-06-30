# Chuck

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：轨道冲刺型英雄

## 攻击特征

- 普通攻击是三团中距离蒸汽
- 近距离命中更痛，远距离伤害会下降
- 适合在贴近点位时做压制

## 超级技能特征

- Super 会放置 Posts，并在 Posts 之间冲刺
- Super 可自动充能
- 冲刺路线一旦铺好，就能反复制造压制和突进

## 适合场景

- Heist 这类固定目标模式
- 需要反复转点或打路线的地图
- 有足够墙体和路线结构的场景

## 角色定位总结

Chuck 是一种很特别的控制英雄，他靠预先布点和多段 Dash 建立“路径优势”，而不是靠单次爆发决定战斗。

## 与其他英雄的区别

- 不同于 `Darryl`：Chuck 的移动更依赖结构化 Posts
- 不同于 `Carl`：Chuck 更像路线控制，Carl 更像回旋持续输出
- 不同于 `Stu`：Chuck 的节奏更偏预设路径，不是随打随走

## 关联页面

- [[sources/Fandom-Chuck|Fandom 来源摘要: Chuck]]
- [[sources/PLP-Chuck|Power League Prodigy 来源摘要: Chuck]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "mid_short; 6.67-tile steam falls off hard at max range and wants close or route-based contact"
    projectile_reliability: "medium; three piercing steam clouds are consistent through bodies but slow reload punishes misses"
    burst: "high_on_dash_route; Super dash deals heavy line damage and can repeat through Posts"
    sustained_dps: "low_without_route; 2s reload and falloff make raw laning weaker than his post-cycle pressure"
    objective_damage: "very_high_if_heist_route_set; repeated post dashes can hit safe and retreat with 50% dash shield"
    mobility: "setup_dependent_very_high; auto-charging Super and Posts create repeated map-wide routes after setup"
    survivability: "medium_high_on_dash; 4700 health plus 50% damage reduction while dashing, but endpoints can be camped"
    engage: "high_after_posts; dash route reaches backline, thrower pocket, safe, or carrier if endpoint is safe"
    disengage: "high_with_retreat_post; own-side Posts let Chuck escape after safe hit or gem pickup"
    anti_aggro: "medium; post landing knockback and dash damage help, but true melee can camp endpoint"
    anti_tank: "low_medium; dash damage is meaningful but tanks with CC/burst punish predictable paths"
    wall_break: low
    throw_or_wall_bypass: "medium_high_with_posts_and_Ghost_Train; Posts can be thrown over walls and Ghost Train lets next dash connect through obstacles"
    area_control: "medium; visible post network reshapes where enemies can safely stand"
    scouting_or_vision: low
    team_support: "low_direct; Chuck creates route pressure and objective race, not buffs"
    spawnable_or_pet: "medium_as_route_anchor; Posts are persistent route anchors rather than damage pets"
    crowd_control: "medium; post landing knocks back and Tickets Please can drain enemy ammo on dash"
    terrain_creation: "medium; post network creates a persistent route graph"
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Chuck|Fandom-Chuck]]"
      - "[[sources/PLP-Chuck|PLP-Chuck]]"

  build_switches:
    - build: "Rerouting / Pit Stop / Shield, Damage"
      source: "[[sources/PLP-Chuck|PLP-Chuck]]"
      changes_capabilities:
        - "Rerouting removes the nearest Post and instantly recharges Super, letting Chuck fix predictable endpoints"
        - "Pit Stop raises the Post cap to 4, increasing route coverage and Heist safe-cycle options"
        - "Shield and Damage gears improve survival and safe-race pressure once the route is established"
      enables:
        - heist_safe_route_loop
        - endpoint_retargeting
        - long_route_objective_access
      mitigates_failure_modes:
        - post_route_predictability
        - endpoint_camp
      best_when: "Heist map lets Chuck place a recoverable route to safe and the enemy lacks cheap Super denial or endpoint camping"
      poor_when:
        - "enemy has Charlie/Otis/Cordelius-style denial or melee burst waiting at the final Post"
        - "team expects Chuck to win raw mid lane before his route exists"
      bp_use: default_reviewed_build_for_heist_post_routes
    - build: "Ghost Train / Tickets Please variants"
      source: "[[sources/Fandom-Chuck|Fandom-Chuck]]"
      changes_capabilities:
        - "Ghost Train lets Chuck's next dash connect through walls, opening one-time pocket or safe-entry paths"
        - "Tickets Please drains ammo from enemies hit by the dash, useful when the enemy endpoint defenders rely on full ammo"
      enables:
        - wall_bypass_entry
        - ammo_tax_on_defenders
      mitigates_failure_modes:
        - wall_pocket_blocks_route
        - endpoint_defender_full_ammo
      poor_when:
        - "Pit Stop's fourth Post is required to maintain the core Heist route"
      bp_use: situational_variant_for_wall_bypass_or_endpoint_ammo_tax

  map_feature_hooks:
    - map_feature_type: "heist_post_safe_route_loop"
      uses_feature_by: "Chuck sets Posts that let auto-charged Super repeatedly dash to safe and retreat"
      route_or_position: "side lane, safe-facing wall, or straight safe path where Posts can connect without exposing every endpoint"
      objective_conversion: "convert setup time into repeated safe damage and forced defensive attention"
      active_when: "Chuck can establish Posts before the race is lost and the enemy cannot cheaply camp or disable the final endpoint"
      fails_if: "enemy ignores Chuck and wins faster safe DPS, camps the last Post, or uses silence/cocoon/CC to stop the dash cycle"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Safe(r) Zone
      bp_use: candidate_eval.heist_objective_access
    - map_feature_type: "safe_barrier_wall_bypass_and_route_retarget"
      uses_feature_by: "Posts can be thrown over walls, Ghost Train can connect through obstacles, and Rerouting changes the final destination"
      route_or_position: "safe barrier, side wall pocket, or thrower angle that normal walking cannot cross safely"
      objective_conversion: "bypass protected Heist walls, punish a thrower pocket, or alter endpoint timing after defenders start camping"
      active_when: "walls are the main cost to target access and Chuck has Super/Gadget timing to change the route"
      fails_if: "the map opens into long-range DPS after wallbreak, Ghost Train is spent without objective contact, or the endpoint is guarded by anti-aggro"
      example_maps:
        - Pit Stop
        - Hot Potato
        - Safe(r) Zone
      bp_use: map_bp_factors.route_gate_and_endpoint_filter
    - map_feature_type: "post_rotation_carrier_or_zone_chase"
      uses_feature_by: "Fandom tips note own-side/enemy-side Posts can chase gem carriers or return quickly to Hot Zone"
      route_or_position: "center fort route, open-mid gem retreat lane, or single-zone entry path"
      objective_conversion: "catch a carrier, retreat with gems, or re-enter zone faster than normal rotation"
      active_when: "Chuck has time to set route anchors and the objective path remains predictable"
      fails_if: "round reset removes Posts, enemy camps endpoint, or route pressure does not convert into gems or zone time"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Dueling Beetles
        - Open Business
      bp_use: situational_map_fit_outside_primary_heist_role

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - repeated_post_safe_damage
        - safe_entry_and_retreat
        - defender_route_disruption
      cannot_fulfill:
        - stable_raw_lane_dps_before_setup
        - anti_control_self_protection_if_endpoint_is_camped
      needs_teammate_support:
        - early lane pressure while Chuck builds Posts
        - answers to silence, cocoon, knockback, or endpoint campers
      false_positive: "Chuck is a Heist route engine; if his route is denied or the race ends before setup, his raw DPS is not enough."
    - mode: "Gem Grab"
      can_fulfill:
        - carrier_chase_with_enemy_side_post
        - carrier_retreat_with_own_side_post
        - side_pressure_after_route_setup
      cannot_fulfill:
        - stable_mid_carrier_without_post_escape
        - early_mine_control_before_setup
      needs_teammate_support:
        - mid control that buys setup time
        - endpoint protection during countdown
      false_positive: "Fandom notes Gem Grab utility, but PLP only recommends Heist; treat Gem Grab as conditional route tech."
    - mode: "Hot Zone"
      can_fulfill:
        - fast_zone_return
        - zone_entry_dash_damage
        - endpoint_retarget_to_avoid_camp
      cannot_fulfill:
        - primary_zone_body_before_posts
        - wall_pocket_clear_without_followup
      needs_teammate_support:
        - zone body or area clear
        - anti-CC protection for dash endpoint
      false_positive: "Chuck can arrive quickly, but arrival is not zone control if enemies wait on the endpoint."

  failure_modes:
    - id: "setup_time_before_route_value"
      active_when: "enemy wins lanes or safe race before Chuck establishes Posts"
      exposed_by: "[[sources/Fandom-Chuck|Fandom-Chuck]] Super setup mechanics and slow reload"
      mitigation: "draft Chuck only when teammates cover early lane or the map gives safe setup time"
      bp_use: early_game_false_positive_filter
    - id: "post_route_predictability"
      active_when: "Chuck repeats the same route and enemies camp the final Post"
      exposed_by: "[[sources/Fandom-Chuck|Fandom-Chuck]] tips about enemies camping final destination and Rerouting usage"
      mitigation: "use Rerouting, alternate endpoint, or draft pressure that punishes endpoint campers"
      bp_use: endpoint_camp_check
    - id: "super_denial_or_control_interrupt"
      active_when: "enemy can mute, cocoon, knock back, slow, stun, or send Chuck away before dash value converts"
      exposed_by: "[[sources/Fandom-Chuck|Fandom-Chuck]] notes that dash can still be stunned/slowed plus [[sources/PLP-Chuck|PLP-Chuck]] counteredBy and avoid fields"
      mitigation: "avoid into cheap Super denial or force those tools on a different lane before committing"
      bp_use: must_avoid_or_ban_reason
    - id: "raw_laning_without_posts"
      active_when: "Chuck is forced into standard lane fighting without a useful post graph"
      exposed_by: "Fandom slow reload, falloff, and close-range damage profile"
      mitigation: "evaluate him by route-to-objective, not by generic lane DPS"
      bp_use: candidate_eval.route_dependency

  conditional_matchup_seeds:
    - target:
        - "Barley"
        - "Dynamike"
        - "Grom"
        - "Sprout"
        - "Mr. P"
        - "Squeak"
      direction: "subject_favored"
      source: "[[sources/PLP-Chuck|PLP-Chuck]]"
      mechanism: "Post routes and Ghost Train can bypass wall-control pockets and force throwers/control picks to answer an endpoint instead of free-casting."
      active_when: "map has a wall pocket or Heist route that Chuck can connect to without dying at the endpoint"
      fails_when: "the pocket has bodyguard peel, endpoint campers, or Chuck lacks time to set the route"
      bp_use: response_pick_candidate_against_wall_control_on_objective_maps
    - target:
        - "Byron"
        - "Colt"
      direction: "subject_favored"
      source: "[[sources/PLP-Chuck|PLP-Chuck]]"
      mechanism: "Chuck can bypass linear range with a prepared dash route and convert directly onto safe or backline before poke attrition matters."
      active_when: "objective route is fixed, post path is already placed, and enemy lacks endpoint CC or tank bodyguard"
      fails_when: "they outrun the setup with safe DPS, open the map into long lanes, or hold final Post with teammates"
      bp_use: heist_route_pressure_candidate
    - target:
        - "Charlie"
        - "Cordelius"
        - "Shelly"
        - "Bull"
        - "Fang"
        - "Otis"
        - "Gale"
        - "El Primo"
        - "Surge"
      direction: "target_favored"
      source: "[[sources/PLP-Chuck|PLP-Chuck]] / [[sources/Fandom-Chuck|Fandom-Chuck]]"
      mechanism: "Cocoon, mute, silence-like denial, knockback, close burst, or endpoint camping can stop Chuck's route before it becomes objective damage."
      active_when: "enemy can predict Chuck's endpoint or hold the safe lane with anti-aggro tools"
      fails_when: "Chuck changes route with Rerouting, attacks a different objective angle, or teammates punish the campers"
      bp_use: must_avoid_or_route_protection_requirement

  slot_notes:
    slot_1: "only on Heist maps where post-safe route is a core plan and the team can absorb obvious anti-route answers."
    slot_2_3: "usable as an early route-plan pick if paired with immediate lane/safe pressure so setup time is protected."
    slot_4_5: "best when enemy 2-3 lack Super denial or endpoint camping and the team still needs objective access."
    slot_6: "punishes drafts that cannot stop a fixed safe route after bans/picks have removed Charlie, Otis, Cordelius, or endpoint tanks."
```
