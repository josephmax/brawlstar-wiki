# Sandy

## 基本信息

- 稀有度：Legendary
- 定位：Controller
- 类型：隐身控场英雄

## 攻击特征

- 主攻击是中距离穿透石子
- 伤害不算高，但可以同时压到多个目标
- 适合边打边建立场面控制

## 超级技能特征

- Super 会生成一片沙暴
- 沙暴中的自己和队友会隐身
- 还能通过星徽与 Hypercharge 强化团队推进、治疗或压制效果

## 适合场景

- 需要团队推进的 3v3 模式
- 需要埋伏、占点和控图的地图
- 适合围绕一个区域打节奏的对局

## 角色定位总结

Sandy 是最典型的团队控场型隐身英雄。和 `Leon` 比，他不是单人偷袭型，而是团队推进型；和 `Crow` 比，他不是持续消耗型，而是区域节奏型；和 `Spike` 比，他更偏控图而不是爆发。

## 关联页面

- [[sources/Fandom-Sandy|Fandom 来源摘要: Sandy]]
- [[sources/PLP-Sandy|PLP 来源摘要: Sandy]]

## BP 建模资料

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-06-30"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: mid; Fandom attack range 6 and Super range 7.33
    projectile_reliability: high_into_grouping_medium_at_max_range; wide piercing cone is easy to tag but low damage limits finish
    burst: low_medium; Sweet Dreams creates pick window rather than raw burst
    sustained_dps: low_medium; normal reload and low damage
    objective_damage: low; Heist value is support only, not primary safe race
    mobility: high; fast base speed and Hypercharge storm speed
    survivability: medium; Sleep Stimulator can fully heal but immobilizes Sandy and is interruptible
    engage: high_with_Sandstorm_team_cover
    disengage: medium_high_with_Sandstorm_or_Sweet_Dreams
    anti_aggro: conditional; Sweet Dreams and sandstorm concealment can stop rushes, but damage is low
    anti_tank: low_medium; needs team damage or Rude Sands area tax
    wall_break: low
    throw_or_wall_bypass: low
    area_control: high; Sandstorm, Rude Sands, Healing Winds, and wide pierce control zones
    scouting_or_vision: medium_high_with_Rude_Sands_or_Vision_Gear
    team_support: very_high; invisibility, healing variant, speed Hypercharge, and engage cover
    spawnable_or_pet: low
    crowd_control: conditional_stun_from_Sweet_Dreams_and_silence_from_Hypercharge
    source_trace:
      - "[[sources/Fandom-Sandy|Fandom-Sandy]]"
      - "[[sources/PLP-Sandy|PLP-Sandy]]"

  build_switches:
    - build: "Sweet Dreams / Rude Sands / Shield, Damage, Speed"
      source: "[[sources/PLP-Sandy|PLP-Sandy]]"
      changes_capabilities:
        - "Sweet Dreams gives a one-attack stun that can stop a rush, score window, or zone entry"
        - "Rude Sands turns Sandstorm into anti-heal, reveal, and area denial"
        - "Shield/Damage/Speed keep Sandy alive while cycling Super and entering grass"
      enables:
        - sandstorm_objective_cover
        - bush_edge_reveal
        - scoring_or_zone_stun_window
      mitigates_failure_modes:
        - low_damage_no_finish
        - enemy_heals_inside_control_area
      poor_when:
        - "enemy has persistent reveal, area control, or can punish Sandy before Super is charged"
      bp_use: default_reviewed_build_for_3v3_control_maps
    - build: "Healing Winds / Sleep Stimulator support variant"
      source: "[[sources/Fandom-Sandy|Fandom-Sandy]]"
      changes_capabilities:
        - "Healing Winds converts Sandstorm into team sustain"
        - "Sleep Stimulator fully heals Sandy if he can hide safely during the channel"
      enables:
        - sustain_push
        - reset_after_lane_trade
      mitigates_failure_modes:
        - team_dies_during_hidden_push
        - Sandy_low_health_after_trade
      poor_when:
        - "enemy can scout the storm, interrupt the channel, or outdamage the healing"
      bp_use: support_build_switch_if_team_needs_sustain_more_than_reveal

  map_feature_hooks:
    - map_feature_type: "sandstorm_objective_cover"
      uses_feature_by: "Sandy places Sandstorm over the objective approach so teammates can enter unseen while Rude Sands taxes enemies inside"
      route_or_position: "gem mine, Hot Zone circle, or central fort entrance where enemy must contest a fixed area"
      objective_conversion: "Gem mine access, zone time, hidden retreat, or team collapse after first tag"
      active_when: "team has follow-up damage or bodies that can use the concealment"
      fails_if: "enemy has reveal, persistent area control, item carriers stay visible, or team lacks damage after entering"
      example_maps:
        - Double Swoosh
        - Gem Fort
        - Dueling Beetles
        - Ring of Fire
      bp_use: map_bp_factors.objective_cover_and_area_denial
    - map_feature_type: "brawl_ball_scoring_window"
      uses_feature_by: "Sandstorm covers ball vicinity and Sweet Dreams can stun a defender long enough for a pass, carry, or shot"
      route_or_position: "midfield grass, side-bush approach, or goal entry where defenders must reveal to touch the ball"
      objective_conversion: "turn ball control into a scoring attempt or force defenders to give ground"
      active_when: "team includes a scorer, dash, wallbreak, or close-range teammate that converts the hidden entry"
      fails_if: "goal geometry stays closed, enemy has knockback/reveal, or Sandy's team cannot finish after the stun"
      example_maps:
        - Center Stage
        - Sneaky Fields
        - Triple Dribble
      bp_use: slot_task.scoring_window_creator
    - map_feature_type: "bush_edge_vision_denial_and_reveal"
      uses_feature_by: "Sandy places storm touching bush edges, letting allies exit into grass while Rude Sands or Vision Gear reveals enemies who enter"
      route_or_position: "spiral bush, side grass lane, or large center bush mass"
      objective_conversion: "protect gem carrier retreat, deny bush campers, or create a hidden flank to clear zone"
      active_when: "bush control is contested and Sandy can cycle Super before enemy fully sweeps grass"
      fails_if: "enemy burns/sweeps grass first, controls outside angles, or uses thrower pressure that ignores concealment"
      example_maps:
        - Double Swoosh
        - Ring of Fire
        - Sneaky Fields
        - Gem Fort
      bp_use: candidate_eval.vision_tax_and_flank_cover

  objective_contracts:
    - mode: "Gem Grab"
      can_fulfill:
        - sandstorm_mid_access
        - carrier_retreat_cover
        - Rude_Sands_bush_reveal
      cannot_fulfill:
        - primary_long_range_gem_carrier_by_default
        - high_burst_pick_without_teammate
      needs_teammate_support:
        - damage finisher
        - anti-tank or anti-thrower depending on map
      false_positive: "Sandstorm gives access, but Sandy still needs teammates to convert hidden movement into kills or gem security."
    - mode: "Brawl Ball"
      can_fulfill:
        - hidden_team_push
        - Sweet_Dreams_defender_stun
        - ball_vicinity_cover
      cannot_fulfill:
        - wallbreak_goal_opening
        - reliable solo burst scorer
      needs_teammate_support:
        - scorer, wallbreak, dash, or knockback
        - anti-aggro defense after storm expires
      false_positive: "Covering the ball is not enough if the comp has no actual scoring tool."
    - mode: "Hot Zone"
      can_fulfill:
        - zone_area_denial
        - team_concealment_on_entry
        - sustain_or_reveal_build_switch
      cannot_fulfill:
        - solo zone body against tanks
        - thrower_pocket_clear_without_help
      needs_teammate_support:
        - body on zone
        - wallbreak or dive against protected throwers
      false_positive: "Rude Sands controls space but does not replace a durable zone holder."
    - mode: "Heist"
      can_fulfill:
        - support_push_cover
        - defensive anti-heal or reveal near safe
      cannot_fulfill:
        - primary_safe_DPS
        - stable wallbreak_or_safe_access
      needs_teammate_support:
        - real safe damage
        - lane winner that benefits from invisibility
      false_positive: "Fandom notes Heist utility, but Sandy's low damage makes him a support pick, not a race anchor."

  failure_modes:
    - id: "low_damage_no_finish"
      active_when: "Sandy reveals or stuns a target but team has no burst follow-up"
      exposed_by: "[[sources/Fandom-Sandy|Fandom-Sandy]] low damage output and slow reload"
      mitigation: "pair with scorer, tank, burst, or long-range finisher before treating Sandstorm as win condition"
      bp_use: "candidate_eval.required_support"
    - id: "invisibility_limitations"
      active_when: "enemy is within reveal radius, target carries an item, or spawnables/turrets do not become concealed"
      exposed_by: "[[sources/Fandom-Sandy|Fandom-Sandy]] Sandstorm visibility rules"
      mitigation: "do not rely on invisibility for item carriers or close enemy proximity; use storm as area tax instead"
      bp_use: "false_positive_check"
    - id: "super_cycle_dependency"
      active_when: "Sandy cannot charge Super before the first objective fight"
      exposed_by: "[[sources/Fandom-Sandy|Fandom-Sandy]] Super-centric kit and low direct DPS"
      mitigation: "draft him where wide pierce can tag grouped enemies or pair with early control"
      bp_use: "slot_1_risk"
    - id: "area_reveal_or_thrower_denies_storm"
      active_when: "enemy controls storm edges with persistent damage, thrower arcs, reveal, or mines"
      exposed_by: "[[sources/PLP-Sandy|PLP-Sandy]] counteredBy area/control picks and Fandom Rude Sands mirror note"
      mitigation: "add wallbreak/dive or avoid relying on storm path through the same pocket"
      bp_use: "must_answer_or_avoid"

  conditional_matchup_seeds:
    - target:
        - "Jae-Yong"
        - "Piper"
        - "Nani"
        - "Squeak"
        - "Sprout"
        - "Mr. P"
      direction: "subject_favored"
      source: "[[sources/PLP-Sandy|PLP-Sandy]]"
      mechanism: "Sandstorm compresses sightlines and lets Sandy's team cross into fragile long-range or wall-control targets, while Sweet Dreams punishes the first defender who steps forward."
      active_when: "Sandy has Super or can charge it on grouped enemies, and the map objective forces the target to contest a zone, ball, or gem area"
      fails_when: "target holds a deeper wall pocket, Sandy lacks follow-up damage, or open range prevents Super cycle"
      bp_use: "team_cover_response_pick_candidate"
    - target:
        - "Nita"
        - "Bo"
        - "Crow"
        - "Emz"
        - "Larry & Lawrie"
      direction: "target_favored"
      source: "[[sources/PLP-Sandy|PLP-Sandy]]"
      mechanism: "spawnables, mines, poison, cone control, and persistent area damage reveal or tax Sandstorm paths and punish Sandy's low damage."
      active_when: "enemy controls the storm edge or can damage hidden allies without needing exact line of sight"
      fails_when: "Sandy lands first Super with teammate collapse and removes the area-control anchor before it stabilizes"
      bp_use: "must_answer_area_reveal_before_sandy_plan"
    - target:
        - "Rosa"
        - "Mortis"
        - "Damian"
        - "Darryl"
        - "Fang"
      direction: "volatile"
      source: "[[sources/Fandom-Sandy|Fandom-Sandy]]"
      mechanism: "Sandy can hide a team anti-aggro response and stop a dive with Sweet Dreams, but close-range threats can also exploit the storm if Sandy lacks damage support."
      active_when: "Sandy has Sweet Dreams, allies are ready to punish the entry, and the route is predictable"
      fails_when: "diver enters from multiple angles, baits the stun, or reaches Sandy before Super/stun is available"
      bp_use: "anti_aggro_resource_and_team_damage_check"

  slot_notes:
    slot_1: "可在 Gem/Ball/Hot Zone 的团队推进图先手，但要确认敌方 2-3 位不会低成本拿 reveal、area control 或 thrower pocket。"
    slot_2_3: "适合作为团队推进或回答长手控制的计划位；另一手最好补爆发、身体或得分工具。"
    slot_4_5: "用于补隐身推进、草控和站圈入口；必须检查敌方 6 位是否还能补 Nita/Bo/Crow/Emz 类揭示或区域惩罚。"
    slot_6: "当敌方缺 reveal、缺区域控制且目标必须进固定区域时，Sandy 可以作为团队进场和得分窗口的惩罚性选择。"
```
