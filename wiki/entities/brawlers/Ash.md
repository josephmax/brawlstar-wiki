# Ash

## 基本信息

- 稀有度：Epic
- 定位：Tank
- 类型：怒气成长型前排

## 攻击特征

- 主攻击是前方扫地式冲击波
- Rage 越高，攻击越强
- 适合持续贴近敌人并滚动压线

## 超级技能特征

- Super 会召唤机器人老鼠追击敌人
- 老鼠接触后爆炸
- 能持续制造站位压力和混乱

## 适合场景

- 需要持续前压的模式
- 需要抗压并推进的对局
- 敌方阵型容易被逼散的地图

## 角色定位总结

Ash 是会随着战斗推进而越来越强的前排。和 `Frank` 相比，他不靠单次重锤定局，而是靠怒气把自己推成越来越难处理的威胁。

## 关联页面

- [[sources/Fandom-Ash|Fandom 来源摘要: Ash]]
- [[sources/PLP-Ash|PLP 来源摘要: Ash]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: short_mid; Fandom attack range 4.67 with piercing shockwave
    projectile_reliability: medium_in_choke_low_in_open; 0.3s wind-up and 0.7s attack cycle make open-field burst less reliable
    burst: high_after_rage; damage scales from 800 to 1600 as Rage rises
    sustained_dps: high_if_rage_is_maintained; fast reload becomes faster with Mad As Heck
    objective_damage: low_medium; contributes through lane pressure, ball carry, and body presence rather than safe race
    mobility: conditional_high; Rage raises speed from normal to very fast
    survivability: high_health_body_with_Chill_Pill_reset
    engage: high_after_rage_or_cover_entry
    disengage: medium; Chill Pill can reset health but consumes Rage
    anti_aggro: conditional; rats block shots and body pressure but Ash can be outburst at low Rage
    anti_tank: conditional; needs Rage and tip-of-range spacing to avoid being outburst
    wall_break: low
    throw_or_wall_bypass: low
    area_control: medium_high; piercing attack, rat swarm, and body pressure tax chokepoints
    scouting_or_vision: low_medium; rats can reveal pressure by chasing but no true reveal
    team_support: low_medium; mainly bodyguard, projectile block, and ammo tax
    spawnable_or_pet: high; Super spawns five rats, ten during Rat King Hypercharge
    crowd_control: low; pressure is movement and ammo tax rather than stun or slow
    source_trace:
      - "[[sources/Fandom-Ash|Fandom-Ash]]"
      - "[[sources/PLP-Ash|PLP-Ash]]"

  build_switches:
    - build: "Chill Pill / First Bash / Damage, Speed"
      source: "[[sources/PLP-Ash|PLP-Ash]]"
      changes_capabilities:
        - "First Bash accelerates the first Rage cycle when Ash hits with full ammo"
        - "Chill Pill converts stored Rage into a large heal, then requires a new Rage cycle"
        - "Damage and Speed gears support close-range lane pressure after Ash reaches cover or grass"
      enables:
        - rage_lane_entry
        - ball_carry_pressure
        - repeated_choke_pressure
      mitigates_failure_modes:
        - low_rage_short_range
        - burst_window_after_taking_damage
      poor_when:
        - "enemy can kite from open range or burst Ash before he converts Rage into pressure"
      bp_use: default_reviewed_build_for_grass_choke_and_ball_pressure
    - build: "Rotten Banana / healer-backed rage acceleration"
      source: "[[sources/Fandom-Ash|Fandom-Ash]]"
      changes_capabilities:
        - "Rotten Banana gives immediate Rage at a health cost"
        - "healer support offsets the self-damage and lets Ash enter fights with speed and damage already online"
      enables:
        - precharged_entry
        - aggressive_lane_guard
      mitigates_failure_modes:
        - slow_first_rage_cycle
      poor_when:
        - "team lacks healing or enemy burst can punish the health payment before Ash connects"
      bp_use: situational_build_requirement_if_team_has_healer

  map_feature_hooks:
    - map_feature_type: "grass_choke_rage_entry"
      uses_feature_by: "Ash uses grass, walls, and lane funnels to survive the first approach, then converts damage taken or dealt into Rage speed and damage"
      route_or_position: "center grass, side grass lane, or Gem Grab choke where enemies must step into piercing range"
      objective_conversion: "Brawl Ball ball carry, Gem Grab side pressure, and enemy mid retreat after Rage turns online"
      active_when: "cover compresses range and teammates can prevent free kiting"
      fails_if: "grass is swept, route is fully open, or enemy has constant slow, knockback, or burst before Rage is built"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Double Swoosh
        - Hard Rock Mine
      bp_use: map_bp_factors.grass_entry_and_lane_funnel_pressure
    - map_feature_type: "zone_body_rage_sustain"
      uses_feature_by: "high health, Rage speed, Chill Pill, and rat ammo tax let Ash contest narrow Hot Zone entries"
      route_or_position: "single-zone entrance or wall-adjacent approach where enemies must fight through Ash's body"
      objective_conversion: "stand on zone, force defenders off entry, or buy time for area-control teammates"
      active_when: "Ash has healer or control support and the zone approach is not a pure long-range crossfire"
      fails_if: "enemy clears him with thrower control, anti-tank burst, or repeated slows before he can refresh Rage"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
      bp_use: candidate_eval.zone_body_with_failure_filter
    - map_feature_type: "spawnable_ammo_tax_and_choke_disruption"
      uses_feature_by: "Little Helpers chase targets, interrupt healing, block non-piercing shots, and charge Rage when they connect"
      route_or_position: "Gem Fort center entrances, Triple Dribble mid push lane, or zone/gem chokepoints where rats force enemy shots"
      objective_conversion: "open an entry window, protect low-health Ash from key projectiles, or force ammo before a team push"
      active_when: "enemy damage is mostly non-piercing or the objective forces them to stand near the rats"
      fails_if: "enemy has pierce, splash, chained attacks, or enough area damage to clear rats without losing position"
      example_maps:
        - Gem Fort
        - Triple Dribble
        - Dueling Beetles
        - Hard Rock Mine
      bp_use: map_factor_fit.spawnable_ammo_tax

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - ball_carry_after_rage
        - grass_or_wall_entry_pressure
        - anti_projectile_bodyguard_with_rats
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - instant_burst_without_rage
      needs_teammate_support:
        - wallbreak_or_scoring_window_creator
        - healer_or_control_to_keep_Rage_cycle_alive
      false_positive: "Ash can hold the ball only if the map gives cover or grass; open-field ball carry exposes his short range."
    - mode: "Gem Grab"
      can_fulfill:
        - side_lane_pressure
        - choke_bodyguard
        - rat_pressure_to_force_ammo
      cannot_fulfill:
        - safe_primary_gem_carrier
        - long_range_mid_control
      needs_teammate_support:
        - reliable mid or gem carrier
        - vision or sweep on grass maps
      false_positive: "Rage pressure does not replace a stable gem carrier; Ash should pressure side lanes or protect retreats."
    - mode: "Hot Zone"
      can_fulfill:
        - zone_body
        - entry_disruption
        - anti_heal_pressure_with_rats
      cannot_fulfill:
        - long-range zone clear
        - thrower_pocket_answer_by_himself
      needs_teammate_support:
        - area clear or thrower answer
        - sustain or peel against anti-tank
      false_positive: "High health alone fails if enemies can clear zone from behind walls or maintain anti-tank fire."

  failure_modes:
    - id: "low_rage_short_range"
      active_when: "Ash starts a fight without Rage and must cross open space into longer range"
      exposed_by: "[[sources/Fandom-Ash|Fandom-Ash]] short range and low initial damage before Rage"
      mitigation: "draft him where cover, grass, or first-hit Rage tools let him start the cycle safely"
      bp_use: "false_positive_filter"
    - id: "windup_burst_exposure"
      active_when: "enemy has fast burst, shotgun range, or mobility that dodges the delayed swing"
      exposed_by: "[[sources/Fandom-Ash|Fandom-Ash]] attack wind-up and tips warning about burst/aggressive Brawlers"
      mitigation: "fight at tip range, pair with slow/control, or avoid open close-range mirrors"
      bp_use: "must_avoid_or_pair_with_control"
    - id: "rat_clear_without_position_loss"
      active_when: "enemy attacks pierce, splash, bounce, or chain through rats"
      exposed_by: "[[sources/Fandom-Ash|Fandom-Ash]] tips that multi-entity attacks can eliminate rats easily"
      mitigation: "do not count rats as protection into splash/chain comps; use them after enemy ammo is spent"
      bp_use: "conditional_matchup_filter"
    - id: "rage_sustain_dependency"
      active_when: "Ash spends Rage on Chill Pill or takes too much damage while trying to build it"
      exposed_by: "[[sources/Fandom-Ash|Fandom-Ash]] Chill Pill resets Rage and taking damage to charge Rage can leave him vulnerable"
      mitigation: "use healer support, retreat routes, and First Bash timing before committing to objective"
      bp_use: "candidate_eval.required_support"

  conditional_matchup_seeds:
    - target:
        - "Nita"
        - "Otis"
        - "Mr. P"
        - "Sandy"
      direction: "subject_favored"
      source: "[[sources/PLP-Ash|PLP-Ash]]"
      mechanism: "Rage-backed speed and piercing swings can walk through mid-range control once Ash reaches cover, while rats tax ammo and prevent clean retreats."
      active_when: "map has grass/chokes, Ash can build Rage before the all-in, and target lacks immediate anti-tank burst"
      fails_when: "target controls open distance, has protected wall pressure, or Ash enters at low Rage with no healer"
      bp_use: "response_pick_candidate_against_mid_control"
    - target:
        - "Shelly"
        - "El Primo"
        - "Rosa"
        - "Spike"
        - "Amber"
        - "Rico"
        - "Crow"
      direction: "target_favored"
      source: "[[sources/PLP-Ash|PLP-Ash]]"
      mechanism: "close-range burst, anti-tank damage, slow, pierce, or area denial punish Ash before he converts Rage into sustained pressure."
      active_when: "map is open enough for kiting or objective forces Ash into their preferred range"
      fails_when: "Ash has cover, healer support, and can force them through rats or choke points"
      bp_use: "avoid_first_pick_or_require_protection"
    - target:
        - "Darryl"
        - "Leon"
        - "Sam"
        - "Cordelius"
      direction: "volatile"
      source: "[[sources/PLP-Ash|PLP-Ash]]"
      mechanism: "Ash can outscale bruisers after Rage, but loses if their burst or displacement lands before his swing cycle stabilizes."
      active_when: "Ash is pre-raged, has tip-range spacing, and the fight happens in a lane funnel"
      fails_when: "enemy baits the first swing, isolates Ash from healer, or forces him to fight before Rage"
      bp_use: "lane_execution_and_slot_6_check"

  slot_notes:
    slot_1: "只能在草丛/墙体和模式目标都支持前排基本面时先手；否则会把短手低 Rage 破口暴露给敌方 2-3 位。"
    slot_2_3: "适合作为回答纯中长手或低爆发控制的压力位，同时另一手要补远程或控场。"
    slot_4_5: "用于修复缺身体、缺进圈或缺球权压力的阵容；必须检查敌方 6 位是否还能补 anti-tank 或 thrower。"
    slot_6: "当敌方缺反坦、缺扫草且必须过窄口时，Ash 可以作为惩罚性 last pick。"
```
