# Chuck

## 基本信息

- 稀有度：Mythic
- 定位：Controller
- 类型：轨道冲刺型英雄

## 攻击特征

- 普通攻击是三团中距离蒸汽，穿透敌人
- 所有距离伤害一致（单团 540，Power 11 1080），近距离优势来自命中密度与压制，而不是伤害加成
- 弹速 2700，射程 6.67 格（Normal）
- 装填 2 秒（Slow），持续输出仍受限于装填

## 超级技能特征

- Trait：开局自带满 Super，共 4 充能
- 每次放 Post 或每次 dash 各消耗 1 充能；Super 不随时间自动充能，打空后只能靠命中回充（普攻 13.5%、Post 命中 10%、dash 命中 43.75%）
- 满充能时被击倒，重生保留全部充能；只要用过任意一次充能，被击倒后剩余充能清空
- dash 冲向 6.67 格内最近的 Post，若 10 格内还有无阻挡的下一根 Post 会连锁冲刺；冲撞对路径敌人造成 1600（Power 11）伤害，期间获得 35% 减伤，仍可被眩晕或减速，冲撞移速 3200
- 手动瞄准或范围内没有 Post 时，投出一根 Post：落地造成 1.83 格半径 800（Power 11）范围伤害，无击退；场上上限 4 根，超放时最早放置的消失
- Post 永久存在，直到 Brawl Ball 得分或 Knockout/Duels 回合结束

## 适合场景

- Heist 这类固定目标模式
- 需要转点或打路线的地图
- 对局节奏允许把开局 4 充能窗口兑换成目标伤害的场景

## 角色定位总结

Chuck 是靠预铺 Posts 和有限 4 充能 Super 建立“路径优势窗口”的控制英雄：开局满 Super 让路线随时可以启动，但每根杆、每次冲刺都是不可再生的资源，窗口打完前必须兑现目标伤害，之后只剩靠命中慢慢回充的弱势期。

## 与其他英雄的区别

- 不同于 `Darryl`：Chuck 的 4 充能同时承担放杆与冲刺两种用途，价值取决于杆网布局；Darryl 是自身翻滚突进
- 不同于 `Carl`：Chuck 更像路线控制，Carl 更像回旋持续输出
- 不同于 `Stu`：Chuck 的节奏偏预设路径的充能窗口，不是随打随走

## 关联页面

- [[sources/Fandom-Chuck|Fandom 来源摘要: Chuck]]
- [[sources/PLP-Chuck|Power League Prodigy 来源摘要: Chuck]]
- [[sources/Fandom-Release-Notes-August-2026|Release Notes August 2026]]
- [[concepts/Buffies|Buffies]]

## BP 建模草案

```yaml
bp_brawler_profile:
  profile_status: bp_ready
  source_quality:
    fandom: "direct_raw_capture_2026-09-03"
    plp: "direct_raw_capture_2026-06-30"
    user_notes: "none"

  capability_vector:
    effective_range: "mid; 6.67-tile steam with 2700 projectile speed and identical damage at every range, so 1080 per cloud (Power 11) holds full value at max range"
    projectile_reliability: "medium_high; three piercing steam clouds stay consistent through bodies, but 2s slow reload still punishes misses"
    burst: "high_in_charge_window; each dash deals 1600 (Power 11) and the opening 4-charge pool converts into a multi-dash burst before any passive refill exists"
    sustained_dps: "low; 2s reload and a finite charge pool make raw laning weaker than timed route pressure"
    objective_damage: "high_if_route_ready; safe and turret dashes are planned bursts of 1600 each (Power 11) paid from the charge pool, not a free repeating cycle"
    mobility: "charge_limited_very_high; the Super starts full, every Post throw or dash spends one of four charges, and there is no time-based refill"
    survivability: "medium; 8800 health (Power 11) plus 35% damage reduction only while dashing, and remaining charges are wiped once any charge has been used before a knockout"
    engage: "high_with_charges; dash routes reach backline, thrower pocket, safe, or carrier without first charging the Super, but engagement ends when the pool is empty"
    disengage: "medium_high_with_charges; own-side Posts still enable escape, and each retreat dash consumes a charge that cannot be restored mid-life"
    anti_aggro: "low_medium; Post landing carries no knockback and only 800 (Power 11) landing damage, so diving melee is answered by dash damage or by burning a disengage charge"
    anti_tank: "low_medium; dash damage of 1600 (Power 11) is meaningful, but tanks with CC/burst punish predictable paths against only 35% dash damage reduction"
    wall_break: low
    throw_or_wall_bypass: "high_with_Ghost_Train; Posts can be thrown over walls, Ghost Train opens 8 seconds of wall-crossing dashes, and the Buffied fire trail adds 2400 (Power 11) of path denial"
    area_control: "medium; up to 4 Posts reshape where enemies can safely stand, and the Buffied Pit Stop burn zone adds 400 (Power 11) of post-denial damage"
    scouting_or_vision: low
    team_support: "low_direct; Chuck creates route pressure and objective races, not buffs"
    spawnable_or_pet: "medium_as_route_anchor; Posts are persistent route anchors dealing 800 (Power 11) on landing rather than damage pets, capped at 4"
    crowd_control: "low_medium; Post landing carries no knockback, so remaining control is Pit Stop's 20% slow on Post hits and the Tickets Please ammo steal"
    terrain_creation: "medium; the 4-Post network is a persistent route graph, but every node costs one finite Super charge to place"
    terrain_destruction: low
    source_trace:
      - "[[sources/Fandom-Chuck|Fandom-Chuck]]"
      - "[[sources/Fandom-Release-Notes-August-2026|Release Notes August 2026]]"
      - "[[sources/PLP-Chuck|PLP-Chuck]]"

  build_switches:
    - build: "Rerouting / Pit Stop / Shield, Damage"
      source: "[[sources/PLP-Chuck|PLP-Chuck]]"
      changes_capabilities:
        - "Rerouting removes the nearest Post and refunds 50% of one Super charge; the Buffie adds a 20% damage-reduction shield for 5 seconds on activation"
        - "Pit Stop slows enemies hit by Post placement by 20% for 1 second; the Buffie leaves a 4-second burn area on placement dealing 400 (Power 11)"
        - "Shield and Damage gears improve survival and safe-race pressure while the route stands"
      enables:
        - heist_safe_route_burst
        - endpoint_retargeting_with_partial_charge_refund
        - post_denial_zone_with_buffie
      mitigates_failure_modes:
        - charge_budget_exhaustion
        - post_route_predictability
        - endpoint_camp
      best_when: "Heist map lets Chuck spend the opening charge pool on a recoverable route to safe and the enemy lacks cheap Super denial or endpoint camping"
      poor_when:
        - "enemy has Charlie/Otis/Cordelius-style denial or melee burst waiting at the final Post"
        - "team expects Chuck to win raw mid lane after his charge pool is spent"
      bp_use: default_reviewed_build_for_heist_post_routes
    - build: "Ghost Train / Tickets Please variants (with Buffies)"
      source: "[[sources/Fandom-Chuck|Fandom-Chuck]]"
      changes_capabilities:
        - "Ghost Train lets every dash of the current Super connect through walls for 8 seconds; the Buffie makes those dashes leave a fire trail dealing 2400 (Power 11) that can tick 3 times"
        - "Tickets Please steals 33% of ammo from enemies hit by dashes and refunds it to Chuck; the Buffie raises dash speed by 25%"
      enables:
        - wall_bypass_entry
        - burning_wall_bypass_path
        - ammo_tax_on_defenders
      mitigates_failure_modes:
        - wall_pocket_blocks_route
        - endpoint_defender_full_ammo
      poor_when:
        - "Pit Stop's post-denial zone or the fourth-Post route coverage is more valuable than a one-window wall entry"
      bp_use: situational_variant_for_wall_bypass_or_endpoint_ammo_tax
    - build: "Hypercharge Full Steam Ahead! (with Buffie)"
      source: "[[sources/Fandom-Chuck|Fandom-Chuck]]"
      changes_capabilities:
        - "Every Post Chuck reaches during a dash explodes for 3200 (Power 11) area damage, stacking objective burst onto the route itself"
        - "The Buffie fires 3 cone-spread attack clouds and extends Hypercharge duration by 2 seconds"
      enables:
        - post_impact_objective_burst
        - cone_attack_trade
      mitigates_failure_modes:
        - charge_budget_exhaustion
      best_when: "the route ends on or beside the objective so Post explosions convert into safe/turret damage inside the same charge window"
      poor_when:
        - "route endpoints face enemies instead of objectives, so explosion value lands on trades rather than objective damage"
      bp_use: hypercharge_window_for_objective_route_burst

  map_feature_hooks:
    - map_feature_type: "heist_post_safe_route_loop"
      uses_feature_by: "Chuck spends the opening full Super on Posts, then converts the remaining charges into dashes to safe and back"
      route_or_position: "side lane, safe-facing wall, or straight safe path where Posts can connect without exposing every endpoint"
      objective_conversion: "convert the opening charge pool into a bounded safe-damage burst and forced defensive attention"
      active_when: "Chuck can place route Posts before the race is lost and the charge budget covers the dashes the plan needs"
      fails_if: "the pool is spent on setup and lane trades before safe contact, the enemy wins faster safe DPS, camps the last Post, or silence/cocoon/CC stops the dash cycle"
      example_maps:
        - Hot Potato
        - Pit Stop
        - Safe(r) Zone
      bp_use: candidate_eval.heist_objective_access
    - map_feature_type: "safe_barrier_wall_bypass_and_route_retarget"
      uses_feature_by: "Posts can be thrown over walls, Ghost Train connects dashes through obstacles for 8 seconds, and Rerouting moves the route while refunding 50% of a charge"
      route_or_position: "safe barrier, side wall pocket, or thrower angle that normal walking cannot cross safely"
      objective_conversion: "bypass protected Heist walls, punish a thrower pocket, or alter endpoint timing after defenders start camping"
      active_when: "walls are the main cost to target access and Chuck still holds a charge plus Ghost Train timing to change the route"
      fails_if: "the map opens into long-range DPS after wallbreak, Ghost Train is spent without objective contact, or the endpoint is guarded by anti-aggro"
      example_maps:
        - Pit Stop
        - Hot Potato
        - Safe(r) Zone
      bp_use: map_bp_factors.route_gate_and_endpoint_filter
    - map_feature_type: "post_rotation_carrier_or_zone_chase"
      uses_feature_by: "own-side and enemy-side Posts let Chuck chase gem carriers or return to Hot Zone inside the current charge window"
      route_or_position: "center fort route, open-mid gem retreat lane, or single-zone entry path"
      objective_conversion: "catch a carrier, retreat with gems, or re-enter zone faster than normal rotation"
      active_when: "Chuck holds enough charges to place route anchors and still dash, and the objective path remains predictable"
      fails_if: "charges run out mid-rotation, a goal or round reset removes Posts, the enemy camps the endpoint, or route pressure does not convert into gems or zone time"
      example_maps:
        - Gem Fort
        - Hard Rock Mine
        - Dueling Beetles
        - Open Business
      bp_use: situational_map_fit_outside_primary_heist_role

  objective_contracts:
    - mode: "Heist"
      can_fulfill:
        - charge_bounded_multi_dash_safe_damage
        - safe_entry_and_retreat_inside_one_pool
        - defender_route_disruption
      cannot_fulfill:
        - unbounded_auto_charged_safe_cycle
        - stable_raw_lane_dps_once_the_pool_is_spent
        - anti_control_self_protection_if_endpoint_is_camped
      needs_teammate_support:
        - early lane pressure while Chuck spends charges on Posts
        - answers to silence, cocoon, knockback, or endpoint campers
      false_positive: "Chuck is a Heist burst-route pick: the opening pool buys one bounded safe window, and once charges are gone he has neither the cycle nor the raw DPS to keep racing."
    - mode: "Gem Grab"
      can_fulfill:
        - carrier_chase_with_enemy_side_post
        - carrier_retreat_with_own_side_post
        - side_pressure_after_route_setup
      cannot_fulfill:
        - stable_mid_carrier_without_post_escape
        - early_mine_control_that_trades_away_route_charges
        - repeated_rotations_after_the_opening_pool_is_used
      needs_teammate_support:
        - mid control that buys time to place route Posts
        - endpoint protection during countdown
      false_positive: "Fandom notes Gem Grab utility, but every rotation burns a finite charge; treat Gem Grab as conditional route tech, not a repeating chase engine."
    - mode: "Hot Zone"
      can_fulfill:
        - fast_zone_return_inside_charge_window
        - zone_entry_dash_damage
        - endpoint_retarget_to_avoid_camp
      cannot_fulfill:
        - primary_zone_body_after_charges_run_out
        - wall_pocket_clear_without_followup
      needs_teammate_support:
        - zone body or area clear
        - anti-CC protection for dash endpoint
      false_positive: "Chuck arrives quickly on the opening pool, but arrival is not zone control if enemies wait on the endpoint or the pool is spent on rotations."
    - mode: "Brawl Ball"
      can_fulfill:
        - midfield_route_dash_pressure_on_carrier_or_defender
        - side_post_escape_for_ball_recovery
        - endpoint_ammo_tax_with_tickets_please_on_goal_entry
      cannot_fulfill:
        - stable_wallbreak_goal_opening
        - safe_carrier_role_while_charges_fund_the_route
        - scoring_geometry_resolution_without_scorer
      needs_teammate_support:
        - scorer and wallbreak/control if goal geometry is closed
        - early lane pressure while Chuck places Posts
      false_positive: "Chuck's route dash can disrupt a ball lane, but PLP recommends only Heist; he does not solve scoring or carrying, and Posts reset on every goal so each possession costs fresh charges."
    - mode: "Bounty"
      can_fulfill:
        - post_route_poke_or_chase_on_overextended_target
        - fast_rotation_back_to_lane_after_a_pick
      cannot_fulfill:
        - stable_star_pressure_on_open_sightline_maps
        - safe_long_range_lane_control_while_charges_fund_the_route
        - repeated_engages_after_the_opening_pool_is_spent
      needs_teammate_support:
        - marksman or long-range teammate to control open sightlines
        - lane protection during the setup window
      false_positive: "Bounty maps reward low-commitment star pressure; Chuck's value is one bounded route window, so he is a weak Bounty fit that should not be drafted as a star source."
    - mode: "Knockout"
      can_fulfill:
        - full_pool_route_picks_in_round_one
        - post_route_pick_confirmation_on_overextended_backline
        - ghost_train_wall_bypass_into_pocket
      cannot_fulfill:
        - safe_first_pick_into_open_or_control_heavy_comps
        - repeated_route_engages_within_a_round_after_charges_are_spent
        - engage_if_endpoint_is_camped_by_cc_or_close_burst
      needs_teammate_support:
        - ranged lane teammate to hold space and force predictable routes
        - bait or ban for Charlie, Otis, Cordelius-style denial before Chuck commits
      false_positive: "Every round starts with a full pool, but Knockout deaths are unrecoverable and spent charges are lost with them; the route dash is a round-one punish tool, not a stable lane pick, and first-picking him invites denial answers."

  failure_modes:
    - id: "charge_budget_exhaustion"
      active_when: "the opening 4-charge pool is spent on Posts, lane trades, or early dashes before objective value converts, with refill limited to hit-based Super charge"
      exposed_by: "[[sources/Fandom-Chuck|Fandom-Chuck]] Super charge model: four charges, no time-based charging, and a knockout wipes remaining charges once any has been used"
      mitigation: "sequence Posts and dashes so the decisive objective dash still has a charge, and use Rerouting's 50% refund to stretch the pool"
      bp_use: charge_window_false_positive_filter
    - id: "post_route_predictability"
      active_when: "Chuck repeats the same route and enemies camp the final Post"
      exposed_by: "[[sources/Fandom-Chuck|Fandom-Chuck]] tips about enemies camping the final destination and Rerouting usage"
      mitigation: "use Rerouting to move a Post while refunding 50% of a charge, alternate endpoints, or draft pressure that punishes endpoint campers"
      bp_use: endpoint_camp_check
    - id: "super_denial_or_control_interrupt"
      active_when: "enemy can mute, cocoon, knock back, slow, stun, or send Chuck away before dash value converts, wasting charges from a non-refillable pool"
      exposed_by: "[[sources/Fandom-Chuck|Fandom-Chuck]] notes that dashes can still be stunned or slowed plus [[sources/PLP-Chuck|PLP-Chuck]] counteredBy and avoid fields"
      mitigation: "avoid into cheap Super denial or force those tools on a different lane before committing the charge pool"
      bp_use: must_avoid_or_ban_reason
    - id: "raw_laning_without_posts"
      active_when: "Chuck is forced into standard lane fighting after his charges are spent and no useful post graph remains"
      exposed_by: "Fandom 2s slow reload and mid range; steady full-value attack damage does not replace route pressure"
      mitigation: "evaluate him by route-to-objective, not by generic lane DPS, and time the charge pool around objective spawns"
      bp_use: candidate_eval.route_dependency

  conditional_matchups:
    - target:
        - "Barley"
        - "Dynamike"
        - "Grom"
        - "Sprout"
        - "Mr. P"
        - "Squeak"
      direction: "subject_favored"
      source: "[[sources/PLP-Chuck|PLP-Chuck]]"
      mechanism: "Post routes and Ghost Train bypass wall-control pockets and force throwers/control picks to answer an endpoint instead of free-casting; the Buffied Ghost Train fire trail punishes pocket campers for standing in the entry path."
      active_when: "the map has a wall pocket or Heist route Chuck can connect to without dying at the endpoint, and charges remain for the entry"
      fails_when: "the pocket has bodyguard peel, endpoint campers, or Chuck spends the pool before the pocket angle exists"
      bp_use: response_pick_candidate_against_wall_control_on_objective_maps
    - target:
        - "Byron"
        - "Colt"
      direction: "subject_favored"
      source: "[[sources/PLP-Chuck|PLP-Chuck]]"
      mechanism: "A prepared dash route converts directly onto safe or backline before poke attrition matters, and full-value steam at range with 2700 projectile speed lets Chuck trade back instead of free-chipping."
      active_when: "objective route is fixed, Posts are placed, and enemy lacks endpoint CC or a tank bodyguard"
      fails_when: "they force Chuck to spend charges on poke trades, open the map into long lanes, or hold the final Post with teammates"
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
      mechanism: "Cocoon, mute, silence-like denial, knockback, close burst, or endpoint camping stops the route inside a charge pool that does not refill, and Post placement carries no knockback to peel divers."
      active_when: "enemy can predict Chuck's endpoint or hold the safe lane with anti-aggro tools"
      fails_when: "Chuck changes route with Rerouting, attacks a different objective angle, holds a charge for disengage, or teammates punish the campers"
      bp_use: must_avoid_or_route_protection_requirement

  slot_notes:
    slot_1: "only on Heist maps where the post-safe route is a core plan and the opening charge window can be spent on the safe before denial answers arrive."
    slot_2_3: "usable early because the Super starts full, but pair with immediate lane/safe pressure so the finite pool is not traded away before the route exists."
    slot_4_5: "best when enemy 2-3 lack Super denial or endpoint camping and the team still needs a bounded objective-access window."
    slot_6: "punishes drafts that cannot stop a fixed safe route after bans/picks have removed Charlie, Otis, Cordelius, or endpoint tanks; the opening full pool makes late picks immediately live."
```
