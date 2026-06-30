# Poco

## 基本信息

- 稀有度：Rare
- 定位：Support
- 类型：治疗辅助英雄

## 攻击特征

- 主攻击是扇形音波
- 伤害不高，但能穿透多个目标
- 适合边打边给队伍充 Super

## 超级技能特征

- Super 会治疗自己和附近友军
- 是强力团队续航技能
- 在团战和推进时能显著抬高队伍容错

## 适合场景

- 需要持续推进的队伍
- 配合高血量前排的阵容
- 团战频繁、需要抬血的模式
- 强调阵容稳定性而非爆发的对局

## 角色定位总结

Poco 是典型的治疗支援英雄，核心不是打出最高伤害，而是让队伍活得更久、推进得更稳。和 `Barley`、`Brock` 这种压制型输出相比，他更像团队节奏的稳定器。

## 关联页面

- [[sources/Fandom-Poco|Fandom 来源摘要: Poco]]
- [[sources/PLP-Poco|PLP 来源摘要: Poco]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30-v2"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "mid_long_spread; Fandom attack range 7 with 65-degree cone and piercing multi-target coverage"
    projectile_reliability: "high_for_bush_check_low_for_single_target_burst; wide spread hits multiple bodies but low damage does not finish alone"
    burst: "low_without_Screeching_Solo; default PLP build is sustain-first"
    sustained_dps: "low_medium; normal reload and low attack damage, but repeated pierce charges Super quickly in grouped fights"
    objective_damage: "low; PLP recommended modes are Brawl Ball and Hot Zone, where healing and cleanse matter more than direct objective DPS"
    mobility: low
    survivability: "team_dependent_high; 4000 health backed by Super heal, Tuning Fork option, Da Capo attack healing, and Hypercharge overheal shield"
    engage: "supportive; enables tank or scorer pushes rather than initiating alone"
    disengage: "medium; instant long Super heal can reset retreat or save carrier/scorer"
    anti_aggro: "medium_with_team; wide cone and healing buy time, but Poco lacks hard CC"
    anti_tank: "low_by_self; needs teammate DPS into high-health targets"
    wall_break: low
    throw_or_wall_bypass: "medium_for_heal; Super travels through obstacles to heal allies"
    area_control: "medium; wide spread checks grass and clustered enemies but does not deny space by damage alone"
    scouting_or_vision: "medium; wide attack can check large bushes"
    team_support: "very_high; healing, cleanse, status immunity, and overheal shield define his pick value"
    spawnable_or_pet: low
    crowd_control: "medium_as_cleanse_answer; Protective Tunes removes slows, stuns, poison, burns, Frost, marks, and silence-like effects but does not displace enemies"
    terrain_creation: low
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Poco|Fandom-Poco]]"
      - "[[sources/PLP-Poco|PLP-Poco]]"

  build_switches:
    - build: "Protective Tunes / Da Capo / Shield, Damage"
      source: "[[sources/PLP-Poco|PLP-Poco]]"
      changes_capabilities:
        - "Protective Tunes cleanses adverse effects in a 6-tile radius and grants 4 seconds of immunity"
        - "Da Capo lets Poco's main attack heal allies it hits, enabling tank or scorer sustain even before Super"
        - "Shield gear improves Poco's own survival; Damage gear helps convert low-damage chip when he is already safe"
      enables:
        - tank_push_support
        - zone_sustain_anchor
        - anti_status_team_reset
      mitigates_failure_modes:
        - status_control_lock
        - ally_health_race
      best_when: "team has a high-health frontliner, scorer, or zone body that can stay near Poco's heal lines"
      poor_when:
        - "team lacks damage and expects Poco to kill tanks or clear thrower pockets alone"
        - "enemy can split the team so Da Capo and Protective Tunes cannot cover multiple lanes"
      bp_use: default_reviewed_build_for_brawl_ball_and_hot_zone_sustain
    - build: "Tuning Fork / Screeching Solo variants"
      source: "[[sources/Fandom-Poco|Fandom-Poco]]"
      changes_capabilities:
        - "Tuning Fork adds 5 seconds of local healing around Poco"
        - "Screeching Solo gives Super a low-damage finishing function, more useful when healing allies is less central"
      enables:
        - local_zone_heal
        - low_health_finish
      mitigates_failure_modes:
        - no_super_heal_window
      poor_when:
        - "enemy status effects are the main reason allies lose control, making Protective Tunes more valuable"
      bp_use: situational_variant_when_cleanse_is_not_required

  map_feature_hooks:
    - map_feature_type: "zone_sustain_and_cleanse_anchor"
      uses_feature_by: "Poco keeps allies standing on the zone through Super, Da Capo, Protective Tunes cleanse, and optional Tuning Fork"
      route_or_position: "single-zone edge, L-wall support pocket, or split-zone home anchor where allies can stay within heal/cleanse range"
      objective_conversion: "turn health resets into zone time and deny control effects that would normally force a retreat"
      active_when: "team can group around a zone body and enemy pressure relies on slow, poison, stun, burn, mark, Frost, or silence effects"
      fails_if: "enemy uses thrower pockets to split the formation, bursts through the heal window, or wins with raw anti-tank DPS"
      example_maps:
        - Dueling Beetles
        - Ring of Fire
        - Open Business
        - Parallel Plays
      bp_use: map_bp_factors.zone_sustain_and_status_cleanse
    - map_feature_type: "brawl_ball_tank_push_heal_lane"
      uses_feature_by: "Da Capo and Super keep a high-health carrier or scorer alive while Poco's wide attack chips and charges another heal"
      route_or_position: "center grass fight, side bush push, or goal approach where a tank/scorer can stay in Poco's cone or Super line"
      objective_conversion: "escort a carry, keep push tempo after first contact, or reset a defender's burst before a scoring attempt"
      active_when: "team has a frontliner/scorer and a real scoring-window creator"
      fails_if: "Poco is drafted without a damage carry, enemy knockback isolates the scorer, or the goal remains closed with no wallbreak/control"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.healer_for_ball_push
    - map_feature_type: "wide_spread_bush_check_and_retreat_support"
      uses_feature_by: "Poco's wide piercing attack checks large bushes and charges Super against grouped enemies, while long Super heals through obstacles during retreat"
      route_or_position: "bushy side lane, gem retreat grass, or Hot Zone grass edge where allies need safe movement through uncertain vision"
      objective_conversion: "protect carrier retreat, reveal flank pressure, or keep a zone ally alive while backing through cover"
      active_when: "map rewards bush checking and the team can convert a revealed enemy with damage"
      fails_if: "enemy outranges from open lines, burns grass first, or has enough burst to ignore repeated small heals"
      example_maps:
        - Double Swoosh
        - Undermine
        - Sneaky Fields
        - Ring of Fire
      bp_use: candidate_eval.vision_support_not_primary_damage

  objective_contracts:
    - mode: "Brawl Ball"
      can_fulfill:
        - tank_or_scorer_heal_support
        - anti_status_push_reset
        - wide_bush_check_before_entry
      cannot_fulfill:
        - reliable_wallbreak_goal_opening
        - solo_scoring_or_primary_burst
      needs_teammate_support:
        - frontliner, scorer, or hard-control finisher
        - enough team damage to punish enemies who walk through Poco's low damage
      false_positive: "Poco makes the push live longer; he does not create the goal opening by himself."
    - mode: "Hot Zone"
      can_fulfill:
        - zone_sustain
        - cleanse_against_control
        - wide_attack_bush_check
      cannot_fulfill:
        - solo_zone_clear_from_range
        - thrower_pocket_clear
      needs_teammate_support:
        - area damage or wall pressure
        - tank/body or mid-range damage dealer who can stand on zone
      false_positive: "Healing a losing zone fight only delays defeat if the team cannot remove enemy area control."
    - mode: "Gem Grab"
      can_fulfill:
        - carrier_retreat_heal
        - bush_check_with_wide_attack
        - cleanse_against_control_during_countdown
      cannot_fulfill:
        - primary_mid_damage
        - solo_side_lane_kill_pressure
      needs_teammate_support:
        - stable gem carrier
        - side-lane damage or control
      false_positive: "Fandom mentions control modes such as Gem Grab for Protective Tunes, but PLP does not list Gem Grab as a main mode; use only as conditional support fit."

  failure_modes:
    - id: "low_damage_no_carry"
      active_when: "team expects Poco to kill tanks, clear spawnables, or win lane without a damage partner"
      exposed_by: "[[sources/Fandom-Poco|Fandom-Poco]] lead and attack sections describing very low damage"
      mitigation: "draft Poco with a frontliner, scorer, or damage carry who converts the health advantage"
      bp_use: false_positive_filter
    - id: "split_formation_heal_loss"
      active_when: "map or enemy pressure splits allies beyond Da Capo, Super, or Protective Tunes coverage"
      exposed_by: "[[sources/Fandom-Poco|Fandom-Poco]] heal and cleanse ranges plus [[entities/maps/Parallel Plays|Parallel Plays]] split-objective rules"
      mitigation: "assign Poco to a clear home-zone or push-lane unit instead of three-lane independent play"
      bp_use: map_fit_filter
    - id: "burst_outpaces_sustain"
      active_when: "enemy focus fire kills the target before Super, Da Capo, or cleanse timing matters"
      exposed_by: "[[sources/PLP-Poco|PLP-Poco]] target-favored list with high-health and high-pressure enemies"
      mitigation: "add peel, anti-tank damage, or avoid drafting Poco as the only defensive layer"
      bp_use: must_pair_with_damage_or_peel
    - id: "thrower_or_wall_pocket_denies_cluster"
      active_when: "enemy thrower or wall-protected control forces Poco's team to spread and denies a shared push lane"
      exposed_by: "[[sources/Fandom-Poco|Fandom-Poco]] low damage and map pages with thrower/support pockets"
      mitigation: "draft wallbreak, dive, or stronger area clear before relying on Poco sustain"
      bp_use: must_answer_thrower_pocket_before_poco_plan

  conditional_matchup_seeds:
    - target:
        - "Lou"
        - "Crow"
        - "Byron"
        - "Ollie"
        - "Gale"
        - "Kit"
      direction: "subject_favored"
      source: "[[sources/PLP-Poco|PLP-Poco]]"
      mechanism: "Protective Tunes removes or prevents many control/status effects, while Super and Da Capo undo chip that these targets rely on to win objective fights."
      active_when: "fight is clustered around Hot Zone, Brawl Ball push, or carrier retreat and Poco's allies remain within cleanse/heal reach"
      fails_when: "enemy wins through raw burst, displacement that Protective Tunes does not interrupt, or anti-heal after Poco spends cleanse"
      bp_use: response_pick_candidate_against_status_control
    - target:
        - "Najia"
        - "Jae-Yong"
      direction: "subject_favored"
      source: "[[sources/PLP-Poco|PLP-Poco]]"
      mechanism: "PLP flags the matchup as favorable; Poco's BP-consumable reason is sustain tempo, where repeated heal waves can outlast poke if teammates provide the damage."
      active_when: "objective is grouped and Poco has a durable teammate converting the health lead"
      fails_when: "the fight spreads across lanes or Poco's team lacks damage after healing"
      bp_use: support_tempo_matchup_candidate
    - target:
        - "Rosa"
        - "Ash"
        - "Nita"
        - "Draco"
        - "Trunk"
        - "8-Bit"
        - "Hank"
      direction: "target_favored"
      source: "[[sources/PLP-Poco|PLP-Poco]]"
      mechanism: "High-health bodies, spawnables, sustained DPS, or tank pressure can absorb Poco's low damage and force his team to spend heals without removing the threat."
      active_when: "objective requires standing in close or mid range and Poco's teammates lack dedicated anti-tank damage"
      fails_when: "Poco is paired with anti-tank DPS and can keep that teammate alive through the first engage"
      bp_use: avoid_as_only_answer_to_tank_core
    - target:
        - "Barley"
      direction: "target_favored"
      source: "[[sources/PLP-Poco|PLP-Poco]]"
      mechanism: "Wall-protected thrower control can split Poco's team, deny shared heal lines, and punish his low personal damage from outside his attack path."
      active_when: "walls remain intact around zone, ball lane, or gem retreat and Poco's team lacks wallbreak or dive"
      fails_when: "Poco's team opens the pocket or pressures Barley before the heal cluster is separated"
      bp_use: must_answer_thrower_pocket_before_poco

  slot_notes:
    slot_1: "reasonable only when the map and planned comp already commit to Hot Zone/Brawl Ball sustain and bans protect against thrower pockets or tank overload"
    slot_2_3: "best paired early with a clear frontliner/scorer so Poco's support contract has a target"
    slot_4_5: "use to answer revealed status-control drafts or repair a comp that needs sustain, while checking enemy can still last-pick Barley/tank pressure"
    slot_6: "rarely a punish pick by himself; strongest when enemy already over-indexed on poison/slow/stun control and lacks burst through healing"
```
