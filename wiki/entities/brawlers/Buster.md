# Buster

## 基本信息

- 稀有度：Mythic
- 定位：Tank
- 类型：保护型前排

## 攻击特征

- 主攻击是中距离锥形光束
- 近距离命中时伤害更高
- 适合在贴身和中距离交界处压线

## 超级技能特征

- Super 会在身前展开屏障
- 能阻挡并反射敌方投射物
- 对队友站位和敌方弹道都有很强的干扰作用

## 适合场景

- 队友集中推进的局面
- 对面投射物很多的对局
- 需要保护后排或卡住前线的模式
- 敌方依赖直线火力时

## 角色定位总结

Buster 是一个保护型坦克，强在靠近队友后更容易发挥，同时能用屏障把敌方投射物变成反击机会。和 `Frank` 比，他更强调防护和反射；和 `Jacky` 比，他更像控制型前排而不是纯贴身输出。

## 关联页面

- [[sources/Fandom-Buster|Fandom 来源摘要: Buster]]
- [[sources/PLP-Buster|Power League Prodigy 来源摘要: Buster]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "mid_short; 5.33-tile cone reaches farther than most tanks but loses damage at max range"
    projectile_reliability: "high_inside_cone; wide piercing cone is reliable in chokes, but does not solve long-range lane fights alone"
    burst: "medium; close-range cone can punish grouped or pulled targets, with Slo-Mo Replay converting one attack into engage"
    sustained_dps: "medium_low; 1.8s reload and damage falloff make him a space/support pick more than a pure damage carry"
    objective_damage: "low; PLP modes are Bounty, Knockout, and Brawl Ball rather than Heist safe race"
    mobility: low
    survivability: "high_if_barrier_faces_damage; 5000 health, Super shield, Kevlar Vest, and optional Utility Belt support team pushes"
    engage: "medium_high_with_slo_mo; pull converts a mid-range cone hit into close contact or ball-carrier disarm"
    disengage: "medium; barrier can cover retreat from projectiles but slows Buster and cancels if he attacks"
    anti_aggro: "medium; Slo-Mo pull and cone punish direct entry, but melee/area effects can bypass barrier"
    anti_tank: "low_medium; he can help hold a lane, but percent damage and true melee tanks punish him"
    wall_break: low
    throw_or_wall_bypass: low
    area_control: "medium; barrier changes projectile lanes and cone pressure taxes grouped chokes"
    scouting_or_vision: low
    team_support: "high; Trait charges near allies and Super shields allies from many projectile lanes"
    spawnable_or_pet: low
    crowd_control: "medium; Slo-Mo Replay pulls enemies and Kevlar Vest resists slows/stuns/knockbacks during Super"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Buster|Fandom-Buster]]"
      - "[[sources/PLP-Buster|PLP-Buster]]"

  build_switches:
    - build: "Slo-Mo Replay / Kevlar Vest / Shield, Damage"
      source: "[[sources/PLP-Buster|PLP-Buster]]"
      changes_capabilities:
        - "Slo-Mo Replay lets Buster pull enemies 3 tiles, turning a cone hit into ball-carrier disarm or close-range confirmation"
        - "Kevlar Vest gives damage reduction and immunity to slows, stuns, and knockbacks while Super is active"
        - "Shield and Damage gears support survival and close-range conversion without changing his ally-radius dependency"
      enables:
        - projectile_lane_screen
        - ball_carrier_disarm
        - choke_pull_confirmation
      mitigates_failure_modes:
        - super_interrupt_by_cc
        - projectile_lane_overload
      best_when: "enemy draft depends on projectile lanes and Buster's team can stay close enough to charge and use the screen"
      poor_when:
        - "enemy damage is mainly lobbed, melee, area, or side-angle pressure that bypasses the barrier"
        - "team composition spreads across lanes so Trait and barrier support do not charge or protect enough"
      bp_use: default_reviewed_build_for_projectile_screen_and_ball_disarm
    - build: "Utility Belt / Blockbuster variants"
      source: "[[sources/Fandom-Buster|Fandom-Buster]]"
      changes_capabilities:
        - "Utility Belt heals Buster and nearby allies, improving grouped sustain in Bounty or Gem-style retreats"
        - "Blockbuster increases attack damage per ally in Trait radius, raising grouped choke punishment"
      enables:
        - grouped_sustain
        - ally_radius_damage_pressure
      mitigates_failure_modes:
        - ally_health_race
      poor_when:
        - "the fight is split-lane or the team cannot cluster without being hit by throwers"
      bp_use: situational_variant_for_grouped_team_fights

  map_feature_hooks:
    - map_feature_type: "projectile_lane_screen_and_star_space"
      uses_feature_by: "Buster's Super deletes and reflects many projectiles when the barrier faces the lane"
      route_or_position: "Bounty or Knockout sightline where a teammate can play behind Buster's screen"
      objective_conversion: "protect star lead, cross a firing lane, or let a sniper/support hold space safely"
      active_when: "enemy pressure is projectile-heavy and Buster can face the lane without being flanked"
      fails_if: "enemy uses throwers, area effects, melee pressure, or side angles that hit around or over the barrier"
      example_maps:
        - Shooting Star
        - Hideout
        - Out in the Open
      bp_use: candidate_eval.projectile_screen_support
    - map_feature_type: "wall_choke_team_cover_and_slo_mo_pull"
      uses_feature_by: "walls and chokes let Buster walk into cone range, screen return fire, and use Slo-Mo Replay to pull a target off cover"
      route_or_position: "layered Knockout wall, Bounty pocket edge, or mid choke where grouped allies can follow"
      objective_conversion: "force a protected target out, secure first pick, or escort team across a dangerous choke"
      active_when: "walls remain and the enemy answer is projectile-based rather than thrower/melee"
      fails_if: "wallbreak opens long lanes, throwers control the pocket, or Buster is isolated from allies"
      example_maps:
        - Belle's Rock
        - Layer Cake
        - New Horizons
        - Hideout
      bp_use: map_bp_factors.choke_screen_and_pull
    - map_feature_type: "brawl_ball_carrier_disarm_and_goal_screen"
      uses_feature_by: "Slo-Mo Replay pulls the carrier while barrier screens projectile defenders during a push"
      route_or_position: "midfield lane, side grass push, or goal approach where ball possession is decided by one contact"
      objective_conversion: "disarm carrier, escort scorer, or shield a teammate during the last approach"
      active_when: "Buster has Super or Slo-Mo ready and a teammate is the actual carrier/scorer"
      fails_if: "Buster must carry while Super is active, goal is closed with no opener, or enemy uses melee/thrower control around the screen"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_disarm_and_projectile_screen

  objective_contracts:
    - mode: "Bounty"
      can_fulfill:
        - projectile_lane_screen
        - ally_peel_near_star_lead
        - controlled_choke_push
      cannot_fulfill:
        - primary_long_range_pick_damage
        - thrower_pocket_clear_without_teammate
      needs_teammate_support:
        - sniper or ranged damage protected by the screen
        - thrower/wall answer when barrier is bypassed
      false_positive: "Buster protects a Bounty plan; he does not replace the long-range kill threat."
    - mode: "Knockout"
      can_fulfill:
        - lane_crossing_screen
        - choke_pull_confirmation
        - late-round team cover
      cannot_fulfill:
        - safe isolated side-lane duel against snipers
        - area-control clear through walls
      needs_teammate_support:
        - damage teammate who shoots through the protected space
        - anti-melee or anti-thrower layer
      false_positive: "Barrier value drops sharply if the enemy's win condition is lobbed or melee damage."
    - mode: "Brawl Ball"
      can_fulfill:
        - ball_carrier_disarm
        - projectile_screen_for_scorer
        - choke_pull_on_defender
      cannot_fulfill:
        - carrying_ball_while_supering
        - solo_goal_opening
      needs_teammate_support:
        - dedicated scorer or ball carrier
        - wallbreak/control if the goal is closed
      false_positive: "Fandom notes Buster cannot carry the ball during Super, so draft him as escort/disarm rather than the carrier during screen timing."

  failure_modes:
    - id: "artillery_and_area_bypass_barrier"
      active_when: "enemy damage is lobbed, area-based, or comes from a side angle"
      exposed_by: "[[sources/Fandom-Buster|Fandom-Buster]] barrier notes that lobbed and area/self attacks bypass or ignore the screen"
      mitigation: "draft thrower answer, avoid relying on barrier as the only defense, or pick Buster only into projectile-heavy lanes"
      bp_use: hard_gate_against_thrower_or_area_damage
    - id: "melee_or_spawnable_ignores_screen"
      active_when: "enemy tank, assassin, spawnable, or self-centered attack walks inside or around the barrier"
      exposed_by: "[[sources/Fandom-Buster|Fandom-Buster]] list of attacks that are not blocked and [[sources/PLP-Buster|PLP-Buster]] target-favored tank list"
      mitigation: "pair with anti-tank damage and avoid using Buster as sole melee answer"
      bp_use: must_pair_with_anti_tank
    - id: "super_cancel_or_ball_lockout"
      active_when: "Buster attacks, is displaced before Kevlar value, or needs to carry the ball while Super is active"
      exposed_by: "[[sources/Fandom-Buster|Fandom-Buster]] Super cancellation and ball-carry limitation notes"
      mitigation: "assign another scorer, time Super only for screen/disarm, and use Kevlar into CC-heavy defenses"
      bp_use: objective_contract_filter
    - id: "ally_radius_dependency"
      active_when: "team spreads across lanes and Buster cannot charge Trait or protect teammates with barrier/Utility Belt"
      exposed_by: "Trait and Utility Belt range mechanics from [[sources/Fandom-Buster|Fandom-Buster]]"
      mitigation: "draft him on grouped-choke maps or with a teammate who can play behind the screen"
      bp_use: slot_fit_and_map_fit_filter

  conditional_matchup_seeds:
    - target:
        - "Carl"
        - "Spike"
        - "Lola"
        - "Rico"
      direction: "subject_favored"
      source: "[[sources/PLP-Buster|PLP-Buster]]"
      mechanism: "Barrier can delete or reflect many projectile lanes while Slo-Mo Replay punishes targets that must stand in Buster's cone."
      active_when: "fight is lane-based, Buster faces the projectile source, and allies can use the protected space"
      fails_when: "target attacks from side angle, uses wall/thrower support, or Buster has to cross open range without Super"
      bp_use: response_pick_candidate_against_projectile_lane
    - target:
        - "Cordelius"
        - "Tara"
        - "Charlie"
        - "Lily"
      direction: "subject_favored"
      source: "[[sources/PLP-Buster|PLP-Buster]]"
      mechanism: "Cone pressure, Slo-Mo pull, and team cover can punish short-to-mid engage tools when those targets must enter through Buster's front."
      active_when: "Buster is grouped with allies and the target's route is predictable through a choke or ball lane"
      fails_when: "Buster is isolated, the target flanks around the barrier, or their control lands before Kevlar/Super timing"
      bp_use: grouped_anti_engage_candidate
    - target:
        - "Colette"
        - "El Primo"
        - "Doug"
        - "Bull"
        - "Darryl"
        - "Frank"
        - "Jacky"
        - "Buzz"
      direction: "target_favored"
      source: "[[sources/PLP-Buster|PLP-Buster]]"
      mechanism: "Percent damage, true melee contact, area/self attacks, or hard engage can ignore or punish Buster's projectile screen."
      active_when: "objective forces repeated close contact or the enemy can enter from inside/behind the barrier"
      fails_when: "Buster has anti-tank teammate damage, pulls them before contact, or screens a separate projectile lane instead of dueling them"
      bp_use: avoid_as_primary_tank_answer

  slot_notes:
    slot_1: "risky unless map and mode strongly reward grouped projectile screening; early Buster invites thrower/melee answers."
    slot_2_3: "good when enemy first pick is projectile-lane dependent and your team can draft a protected damage dealer behind him."
    slot_4_5: "strong as a repair pick for Brawl Ball disarm, Knockout choke crossing, or Bounty star-lead protection."
    slot_6: "punishes drafts that lack throwers, melee bypass, side-angle pressure, or percent damage into Buster's team screen."
```
