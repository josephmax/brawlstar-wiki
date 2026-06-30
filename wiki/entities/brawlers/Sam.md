# Sam

## 基本信息

- 稀有度：Epic
- 定位：Assassin
- 类型：拳套投掷回收型刺客

## 攻击特征

- 主攻击是双拳近距离打击
- 装备 Knuckle Busters 时输出更高、范围更宽
- 拆分为“带拳套”和“空拳套”两种不同手感

## 超级技能特征

- Super 会把 Knuckle Busters 投出去或召回
- 投出后会获得加速
- 回收过程也会造成伤害
- 可以通过拾回拳套瞬间重置节奏

## 适合场景

- 需要快速切入和撤出的对局
- 中近距离乱战
- 想通过武器回收不断刷新进攻节奏的模式

## 角色定位总结

Sam 是靠拳套投掷与回收打出节奏变化的近战刺客。和 `Mortis` 相比，他更像“循环型切入者”；和 `Darryl` 相比，他更依赖 Super 状态管理而不是纯冲锋。

## 关联页面

- [[sources/Fandom-Sam|Fandom 来源摘要: Sam]]
- [[sources/PLP-Sam|Power League Prodigy 来源摘要: Sam]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "short; 3-tile main attack means Sam needs a route, wall loop, or forced objective contact"
    projectile_reliability: "medium_for_super_line; thrown and recalled Knuckle Busters pierce enemies and walls, but value depends on recovery path"
    burst: "medium_high_at_contact; two 800-damage punches with Knuckle Busters plus throw/recall damage punish targets that cannot kite"
    sustained_dps: "cycle_dependent; 1.6s reload with busters and 0.9s without, but losing busters lowers punch damage until retrieval"
    objective_damage: "conditional_heist_entry; PLP lists Heist, but Sam needs lane win or side access before safe damage matters"
    mobility: "high_after_throw; Super throw grants a short speed boost and starts charged at spawn for early Brawl Ball tempo"
    survivability: "high_when_cycle_intact; 5700 health plus Hearty Recovery on pickup supports repeated wall-loop trades"
    engage: "high_on_choke_or_ball_route; Magnetic Field pull or Pulse Repellent knockback converts close entry into contact"
    disengage: "medium; speed after throw and heal on pickup help reset, but separated busters leave Sam weaker"
    anti_aggro: "medium; knockback/pull can disrupt a carrier or diver if busters are placed on the route"
    anti_tank: "medium; close DPS and control can punish some bruisers, but hard anti-tank burst and CC beat him"
    wall_break: low
    throw_or_wall_bypass: "medium_for_recall_only; busters can return through walls and enemies, but Sam himself does not cross terrain"
    area_control: "medium; grounded busters plus Magnetic Field threaten a small choke or objective entrance"
    scouting_or_vision: "low_medium_with_remote_recharge_variant; grounded busters can reveal pressure by Super charge behavior but are not stable vision"
    team_support: "low_direct; Sam mostly creates displacement and body pressure rather than buffs"
    spawnable_or_pet: low
    crowd_control: "medium; Magnetic Field pull and Pulse Repellent knockback are build-specific route tools"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Sam|Fandom-Sam]]"
      - "[[sources/PLP-Sam|PLP-Sam]]"

  build_switches:
    - build: "Magnetic Field / Hearty Recovery / Shield, Damage"
      source: "[[sources/PLP-Sam|PLP-Sam]]"
      changes_capabilities:
        - "Magnetic Field pulls enemies near grounded Knuckle Busters, turning chokes and ball routes into forced-contact spaces"
        - "Hearty Recovery heals 20% missing health on pickup, making wall-loop and repeated entry patterns draftable"
        - "Shield and Damage gears support the bruiser entry plan without changing Sam's route dependency"
      enables:
        - choke_pull
        - ball_tempo_entry
        - repeat_pickup_sustain
      mitigates_failure_modes:
        - pickup_cycle_denied_by_chip
        - objective_route_without_contact
      best_when: "map has walls, bushes, or objective entrances where Sam can throw, pull, regrab, and continue pressure"
      poor_when:
        - "open lanes let enemies kite before Sam reaches pickup range"
        - "water or blocked retrieval route leaves busters away from Sam for too long"
      bp_use: default_reviewed_build_for_choke_and_ball_pressure
    - build: "Pulse Repellent / Remote Recharge variants"
      source: "[[sources/Fandom-Sam|Fandom-Sam]]"
      changes_capabilities:
        - "Pulse Repellent adds a knockback around thrown busters for objective displacement or emergency peel"
        - "Remote Recharge helps when grounded busters cannot be collected safely, including open or awkward terrain states"
      enables:
        - ball_clear_or_goal_denial
        - objective_displacement
        - recovery_when_pickup_path_is_unsafe
      mitigates_failure_modes:
        - busters_unreachable_or_water_trap
      poor_when:
        - "Sam gives up Magnetic Field pull on maps where forced contact is the main reason to pick him"
      bp_use: situational_variant_for_displacement_or_recovery

  map_feature_hooks:
    - map_feature_type: "opening_super_ball_tempo"
      uses_feature_by: "Sam starts with Super and can use throw speed plus immediate tempo to contest ball routes"
      route_or_position: "midfield ball race, side grass entry, or goal approach where first contact decides possession"
      objective_conversion: "win early ball possession, force defender displacement, or create a scorer escort window"
      active_when: "team has a scorer or follow-up clear and enemy lacks immediate knockback or anti-tank burst on the entry"
      fails_if: "the goal remains closed, Sam is forced to fight in open lane after speed expires, or hard CC stops pickup timing"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.ball_tempo_and_entry_body
    - map_feature_type: "wall_loop_hearty_recovery_choke"
      uses_feature_by: "Sam throws busters through or around cover, reclaims them for Hearty Recovery, and uses Magnetic Field at entrances"
      route_or_position: "Gem Grab fort entrance, side grass choke, or wall edge where busters can be recovered safely"
      objective_conversion: "hold side pressure, pull enemies off mine access, or survive repeated carrier-countdown contests"
      active_when: "walls or bushes shorten entry and Sam can regrab without crossing an exposed long lane"
      fails_if: "throwers or snipers deny the pickup, terrain opens into long range, or busters land across water/unreachable space"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Double Swoosh
      bp_use: map_bp_factors.choke_pull_and_recovery_loop
    - map_feature_type: "heist_short_entry_safe_window"
      uses_feature_by: "Sam converts lane contact, speed boost, and close damage into temporary safe access rather than long-range safe DPS"
      route_or_position: "side lane grass, safe-facing wall, or base entry pocket after the enemy lane is forced back"
      objective_conversion: "create a burst safe window or pull defenders off their preferred safe angle"
      active_when: "Sam can win the side lane and collect busters near the safe without being kited through open water lanes"
      fails_if: "Bridge-style separated lanes, water barriers, or long open safe angles prevent repeated close contact"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Safe(r) Zone
      bp_use: candidate_eval.heist_entry_not_stable_ranged_dps

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - side_lane_body_pressure
        - choke_pull_around_mine_entrance
        - carrier_countdown_disruption
      cannot_fulfill:
        - safe_mid_carrier_role
        - long_range_mine_control
      needs_teammate_support:
        - stable mid or long-range carrier
        - follow-up damage after Magnetic Field pull
      false_positive: "Sam pressures routes; he is not a default gem carrier or open-mid controller."
    - mode: "Brawl Ball"
      can_fulfill:
        - opening_ball_tempo
        - scorer_bodyguard
        - defender_displacement_with_pull_or_knockback
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - stable ranged defense after losing busters
      needs_teammate_support:
        - wallbreak or scoring finisher on closed goals
        - lane damage that punishes pulled defenders
      false_positive: "Starting Super creates tempo, but Sam still needs a real scoring conversion plan."
    - mode: "Heist"
      can_fulfill:
        - side_lane_entry
        - short_safe_burst_after_lane_win
        - defender_pull_or_knockback
      cannot_fulfill:
        - long_range_safe_race
        - water_separated_lane_pressure
      needs_teammate_support:
        - ranged safe DPS or wall pressure
        - lane control that lets Sam reach pickup range
      false_positive: "Draft Sam for Heist only when the map offers entry and recovery, not as a remote safe-damage pick."

  failure_modes:
    - id: "busters_unreachable_or_water_trap"
      active_when: "Sam throws Knuckle Busters into water, behind an unsafe long lane, or into a pocket he cannot enter"
      exposed_by: "[[sources/Fandom-Sam|Fandom-Sam]] warning that water can prevent manual collection and severely reduce damage/Gadget access"
      mitigation: "avoid water-separated routes, use Remote Recharge only as a patch, or draft a different entry hero"
      bp_use: map_route_hard_gate
    - id: "short_range_open_kite"
      active_when: "enemy can hold long open lanes and never contests Sam's pull radius"
      exposed_by: "3-tile attack range and PLP target-favored long/control answers"
      mitigation: "reserve Sam for grass, walls, ball routes, or forced objective contact"
      bp_use: false_positive_filter
    - id: "pickup_cycle_denied"
      active_when: "enemy thrower, sniper, slow, silence, or knockback controls the buster pickup point"
      exposed_by: "[[sources/Fandom-Sam|Fandom-Sam]] pickup/recharge mechanics and [[sources/PLP-Sam|PLP-Sam]] target-favored list"
      mitigation: "pair with lane control, bait CC before throw, or keep busters on recoverable side of the route"
      bp_use: must_protect_cycle_or_avoid_pick
    - id: "pull_without_followup"
      active_when: "Magnetic Field pulls a target but Sam's team cannot finish or convert the objective"
      exposed_by: "Fandom pull radius and PLP mode signals"
      mitigation: "draft follow-up damage or objective finisher before relying on pull pressure"
      bp_use: candidate_eval.followup_requirement

  conditional_matchup_seeds:
    - target:
        - "Stu"
        - "Squeak"
        - "Belle"
        - "Poco"
        - "Rico"
        - "Sprout"
        - "Byron"
        - "Mr. P"
      direction: "subject_favored"
      source: "[[sources/PLP-Sam|PLP-Sam]]"
      mechanism: "Speed entry, Magnetic Field pull, and wall-loop recovery punish fragile, utility, or low-burst control picks when Sam can compress the route."
      active_when: "cover, grass, or objective entrances force the target to hold ground within Sam's recoverable buster path"
      fails_when: "target keeps open spacing, sits in a deeper protected pocket, has bodyguard peel, or Sam cannot recover busters safely"
      bp_use: response_pick_candidate_against_control_pocket
    - target:
        - "Surge"
        - "Shelly"
        - "Gale"
        - "Otis"
        - "Lou"
      direction: "target_favored"
      source: "[[sources/PLP-Sam|PLP-Sam]]"
      mechanism: "Anti-tank burst, slow, knockback, silence, and freeze-like control interrupt Sam's pickup cycle or punish his forced close entry."
      active_when: "objective requires Sam to enter their control radius or recover busters under pressure"
      fails_when: "Sam baits the key control tool first or attacks a separate lane with teammate damage"
      bp_use: avoid_first_pick_or_require_control_bait
    - target:
        - "Griff"
        - "El Primo"
        - "Colette"
      direction: "target_favored"
      source: "[[sources/PLP-Sam|PLP-Sam]]"
      mechanism: "High close damage, percent damage, or tank mirror body pressure can win the forced contact that Sam must create."
      active_when: "map funnels Sam into repeated melee trades or safe-lane defense without a clean pickup loop"
      fails_when: "Sam has wall-loop sustain, pulls them into teammate damage, or chooses an objective route away from their body"
      bp_use: tank_mirror_and_percent_damage_warning

  slot_notes:
    slot_1: "rare; only on maps where the team is already committing to close objective tempo and can cover anti-tank answers."
    slot_2_3: "usable as a route-setting bruiser after seeing an enemy control/backline pick that must hold a choke or ball lane."
    slot_4_5: "strongest when answering exposed thrower/control lanes while repairing Brawl Ball or Gem Grab body pressure."
    slot_6: "punishes drafts with no knockback, silence, anti-tank burst, or safe way to deny buster pickup."
```
