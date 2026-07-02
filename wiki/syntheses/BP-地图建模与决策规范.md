# BP 地图建模与决策规范

状态：稳定规范
最近整理：2026-07-02
适用范围：地图实体页建模、Ranked 地图池索引、BP runtime index 编译、BP 决策解释

本页合并原来的地图知识分层治理、地图特征建模 Schema、地图因素 BP 表达规范。它回答一个完整问题：一张地图的稳定事实如何进入 BP，并在每一手 ban / pick 中制造具体职责、硬门槛和候选风险。

## 设计原则

地图知识分三步消费：

1. 稳定事实：地图本身有哪些结构、路线、掩体、草、水、目标点和规则。
2. BP 因素：这些结构在当前模式和地图上制造了什么能力需求、失效条件、路线收益和 slot 任务。
3. 决策索引：结合当前版本强度理解、英雄能力页和对位模型，编译出本次 BP 可快速读取的候选、ban 风险和解释素材。

地图页不直接保存“当前版本强势英雄”。版本强度和临时 meta 只应进入来源页、审计页、日志或用户提供的强度层；只有当它改变能力类型、职责归类、硬门槛、对位成立条件、地图 hook 或 slot 策略时，才更新稳定英雄页或地图页。

## 知识层级

### 稳定地图实体

位置：`wiki/entities/maps/<地图名>.md`

职责：

- 保存地图的稳定结构和 BP 可消费地图事实。
- 使用 `map_profile` 描述地形、目标通路、战术特征、分路动态和地图规则。
- 不保存赛季入池状态、版本强势英雄、临时 counter 结论或未复核来源候选。

### 赛季地图池索引

位置：例如 [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]

职责：

- 说明当前 Ranked 地图池有哪些地图。
- 链接到单地图实体页。
- 只做入口和覆盖检查，不覆盖地图事实。

### 版本与来源层

位置：`raw/`、`wiki/sources/`、必要时的维护归档。

职责：

- 保存 Fandom、官方更新、用户经验、批量抓取、版本观察和审计过程。
- 承载不确定或临时的 meta 观察。
- 不作为 BP 决策默认读取路径，除非正在做 ingest、复核或模型升级。

### 英雄 map-fit 字段

位置：`wiki/entities/brawlers/<英雄>.md`

职责：

- 保存英雄和地图特征的长期 hook。
- 只写稳定能力，例如“可利用窄口溅射控线”“依赖连续墙体接近”“水域绕线价值高”。
- 不写“当前版本在某图强”这种短期判断。

## BP 查询路径

涉及 BP 推演、阵容评价、对位和 draft 顺位时，读取顺序应为：

1. [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
2. [[syntheses/条件化对位模型|条件化对位模型]]
3. 本页
4. 当前赛季地图池索引，例如 [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
5. 具体地图实体页
6. 相关英雄页、模式页和已编译的 `runtime_bp_index`

如果存在本次 BP 的 `runtime_bp_index`，决策阶段优先消费它。若不存在，必须从英雄页、地图页和模式页即时派生候选，不依赖手写 Markdown 决策索引。

## map_profile

`map_profile` 是地图实体页的核心结构。它描述地图有什么，不直接替 BP 做选择。

```yaml
map_profile:
  schema_version: bp_map_profile_v2
  source_status: stable_from_fandom_text | manual_bp_reviewed | needs_recheck
  topology:
    openness:
      mid: open | semi_open | closed | mixed
      left_lane: open | semi_open | closed | mixed
      right_lane: open | semi_open | closed | mixed
    wall_distribution:
      mid: sparse | medium | dense | fragmented
      lanes: sparse | medium | dense | fragmented
      notable_blocks:
        - id: string
          location: mid | left_lane | right_lane | spawn_side | objective_side
          function: cover_anchor | choke_creator | thrower_pocket | approach_wall | bounce_wall
    bush_distribution:
      density: none | low | medium | high | asymmetric
      notable_patches:
        - id: string
          location: mid | lane | objective_side | spawn_side
          function: ambush | rotation_cover | gem_control | flank_entry | scouting_tax
    water_or_void:
      presence: none | low | medium | high
      functions:
        - route_split | thrower_denial | mobility_shortcut | projectile_block | objective_barrier
  objective_access:
    primary_objective:
      type: gem_mine | safe | star_feed | zone | ball_goal | knockout_center | siege_bolt
      access_routes:
        - route_id: string
          lane: mid | left | right | diagonal
          exposure: low | medium | high
          required_capabilities:
            - long_range_pressure | wall_break | throw | bush_scout | burst_entry | sustain | mobility
          denied_by:
            - thrower_lock | sniper_angle | tank_wall_hold | trap_control | spawn_pinch
      conversion_windows:
        - condition: string
          reward: objective_damage | gem_pickup | zone_time | goal_attempt | kill_confirm | lane_lock
          failure_mode: string
  tactical_features:
    map_features:
      - feature_id: string
        type: lane_angle | choke | thrower_pocket | sniper_lane | tank_corridor | bush_path | water_path | wall_break_target | spawn_trap | objective_funnel
        location: mid | left_lane | right_lane | objective_side | spawn_side
        enables:
          - capability: string
            for_team: first_pick | counter_pick | last_pick | both
            condition: string
            payoff: string
        punishes:
          - draft_pattern: string
            condition: string
            punishment: string
  lane_dynamics:
    default_lane_tasks:
      mid:
        expected_role: gem_carrier | sniper_control | anti_throw | scouting | zone_anchor | damage_race
        pressure_type: poke | burst | sustain | area_denial | dive_threat
      left:
        expected_role: lane_hold | flank_threat | wall_break_setup | thrower_anchor | tank_entry
      right:
        expected_role: lane_hold | flank_threat | wall_break_setup | thrower_anchor | tank_entry
    rotation_rules:
      - trigger: wall_broken | bush_removed | first_kill | objective_opened | super_available
        route_change: string
        bp_impact: string
  map_rules:
    hard_gates:
      - condition: string
        rejects:
          - candidate_pattern: string
            reason: string
    soft_preferences:
      - condition: string
        boosts:
          - candidate_pattern: string
            reason: string
```

### map_feature

`map_feature` 是从地图结构中抽出来的可判断特征。每个 feature 必须有位置、路线、收益和失效条件。

```yaml
map_feature:
  feature_id: string
  type: lane_angle | choke | thrower_pocket | sniper_lane | tank_corridor | bush_path | water_path | wall_break_target | spawn_trap | objective_funnel
  location: mid | left_lane | right_lane | objective_side | spawn_side
  enables:
    - capability: string
      condition: string
      payoff: string
  punishes:
    - draft_pattern: string
      condition: string
      punishment: string
```

不能把 `open`、`wall_density: high`、`water_presence: medium` 这类粗标签当成 BP 判断信号。它们必须继续落到“哪条路线、哪个位置、带来什么目标收益、什么条件下失效”。

## map_bp_factor

`map_bp_factor` 是 `map_feature` 的 BP 适配层。它描述地图因素如何影响具体 pick / ban，而不是重复地图结构。

```yaml
map_bp_factor:
  factor_id: string
  source_features:
    - map_feature_id
  mode_context: gem_grab | heist | bounty | knockout | hot_zone | brawl_ball
  affected_slots:
    - early_pick | mid_pick | late_pick | ban | counter_pick
  required_capabilities:
    - capability: string
      reason: string
      minimum_condition: string
  boosted_candidate_patterns:
    - pattern: string
      why: string
      failure_if: string
  punished_candidate_patterns:
    - pattern: string
      why: string
      exception_if: string
  terrain_state_plan:
    before_break:
      value_shifts:
        - candidate_pattern: string
          shift: boost | nerf | hard_reject
          reason: string
    after_break:
      value_shifts:
        - candidate_pattern: string
          shift: boost | nerf | hard_reject
          reason: string
  explanation_hooks:
    - concise_sentence_for_bp_output
```

转换规则：

- `map_profile` 负责说明地图有什么。
- `map_feature` 负责说明结构制造了什么能力窗口。
- `map_bp_factor` 负责说明这个窗口在当前模式中影响哪些 slot、候选、ban 和解释。

## 五层决策模型

地图因素进入 BP 时必须经过五层判断：

1. Objective contract：这张图的获胜目标要求什么。
2. Lane and route contract：默认分路、可用路线、风险路线和转换窗口是什么。
3. Terrain state：墙、草、水、目标通路在开局、中盘和被破坏后的状态如何改变候选价值。
4. Draft slot pressure：这些因素对 early pick、mid pick、late pick 和 ban 分别制造什么义务。
5. Counter and failure audit：候选在什么敌方配置、地图改造或节奏失败下会变成假阳性。

输出解释必须能追溯到这五层中的至少一层。

## 模式化地图职责

### Heist

重点看：

- safe 通路和可输出角度。
- 墙体是否保护推进，还是保护防守侧。
- 是否存在稳定远程输出位、投掷位、弹射位或爆发近身路线。
- 防守是否需要 knockback、slow、wall break、pierce 或 spawn trap 解除能力。

常见 BP 因素：

- open safe angle 提升远程 DPS 和安全消耗。
- wall-protected approach 提升坦克、刺客或高爆发近身。
- thrower pocket 提升投掷压制，但必须检查敌方 dive 和 wall break。
- narrow safe funnel 提升 AoE、防守控场、弹射和穿透。

### Brawl Ball

重点看：

- goal 前墙体、草、窄口和水域是否改变射门路线。
- 中路是否允许强开团，还是奖励远程控线。
- 哪些英雄能稳定拿球、破墙、制造二次射门或防守反推。

常见 BP 因素：

- intact goal walls 提升破墙和近身推进；也提升能守窄口的控场。
- open mid 提升远程控线和 anti-dive。
- bush flank 提升潜伏进场，但要求 scout 或抗 burst。

### Hot Zone

重点看：

- zone 的宽度、遮挡、可站位数量和回防路线。
- 控区英雄能否在不被越位击杀的情况下持续站区。
- 区域控制是否依赖墙体完整。

常见 BP 因素：

- narrow zone 提升 AoE、slow、knockback 和区域封锁。
- open zone 提升远程压制和持续输出。
- wall-protected zone 提升投掷、坦克和近身压迫，但需要审计 wall break 后价值。

### Gem Grab

重点看：

- mine 周围是否开阔，谁能稳定拾取和撤退。
- 两翼是否能绕后切 gem carrier。
- 草、水、墙体是否制造 scout tax。

常见 BP 因素：

- open mine 提升长射程 mid、稳定 poke 和 anti-dive。
- bush flank 提升刺客和近身威慑，但要求可接近且能撤退。
- thrower pocket 提升 mine 控制，但怕 dive、wall break 和快速换线。

### Bounty

重点看：

- 首星、长射程角度、草丛侦查和安全撤退路径。
- 领先后是否能稳住线，落后后是否能创造击杀窗口。
- 哪些路线会把短手候选暴露在无法兑换的位置。

常见 BP 因素：

- long sniper lane 提升狙击、视野和低风险换血。
- bush approach 提升刺客 surprise value，但必须有 scout plan。
- hard choke 提升投掷和 trap，要求审计能否被突进或破墙处理。

### Knockout

重点看：

- 毒圈推进前的站位收益，毒圈推进后的强制交战路线。
- 首杀后的收缩能力和落后时的强开能力。
- 末圈地形是否反转远程、投掷或近身价值。

常见 BP 因素：

- early open angle 提升远程压低血线。
- late choke 提升控制、knockback、burst engage 和抗压站位。
- asymmetrical pocket 提升单边压迫，但要检查换边后价值是否成立。

## Terrain State

地形不是静态标签。至少要区分：

```yaml
terrain_state:
  wall_state:
    intact:
      favors:
        - thrower_lock
        - tank_approach
        - goal_wall_play
      punishes:
        - low_wall_break_team
    broken:
      favors:
        - sniper_angle
        - ranged_dps
      punishes:
        - wall_dependent_thrower
        - slow_tank_without_cover
  bush_state:
    uncleared:
      favors:
        - ambush
        - scouting_tax
      punishes:
        - no_scout_backline
    cleared:
      favors:
        - range_control
      punishes:
        - bush_dependent_assassin
  objective_route_state:
    locked:
      favors:
        - area_denial
        - thrower_pocket
    opened:
      favors:
        - burst_entry
        - direct_dps
```

如果候选只在某个地形状态下成立，报告必须写出状态条件。例如“墙未破前有价值，破墙后会暴露为低机动短手”。

## Hard Gate

地图 hard gate 是强过滤条件。它不问候选强不强，只问候选是否无法完成地图任务。

常见 gate：

- Heist 需要有效 safe pressure；完全无目标输出的候选必须有明确防守或反推职责。
- Gem Grab 需要 mid control 或稳定侧翼职责；无法拾取、无法控 mine、无法威胁 gem carrier 的候选不应早选。
- Bounty 需要低风险换血、视野或稳定击杀窗口；短手候选必须证明可接近。
- Hot Zone 需要站区、清区或反清区能力；只会远程消耗但不能转化 zone time 的候选要降权。
- Brawl Ball 需要进攻转换、防守解围或球门结构处理；纯输出候选必须说明 goal pressure 来源。
- Knockout 需要首杀、收缩、残局或强开能力；只在常规对线强但无法处理毒圈阶段的候选要降权。

## Slot 策略

### Early Pick

地图允许早选的英雄应满足：

- 能覆盖地图核心 objective contract。
- 暴露的 counter 面可控。
- 不依赖单一地形状态。
- 即使敌方破墙、扫草、换线，也仍有可解释职责。

地图不应把高风险 late pick 包装成 early pick。刺客、坦克、投掷和极端地图专精英雄只有在地图强约束足够明确且 counter 面可控时才可提前。

### Mid Pick

mid pick 应用于：

- 补齐地图 hard gate。
- 回应敌方已暴露的分路、墙体计划或输出类型。
- 锁定某个地图 feature 的收益。
- 阻断敌方最自然的地图答案。

### Late Pick

late pick 应用于：

- 利用敌方阵容缺少 scout、wall break、anti-dive、thrower answer 或 objective DPS 的缺口。
- 选择地图特化英雄。
- 选择高 upside 但容易被 ban / counter 的构筑。

late pick 的解释必须写清“为什么现在可以选”，而不是只写英雄在地图上好。

### Ban

地图 ban 应优先考虑：

- 敌方最容易围绕地图 hard gate 拿到的稳定答案。
- 能同时惩罚我方计划和地图结构的英雄。
- 让某类地图 feature 失去自然解法的英雄。

不要因为我方想玩某体系就机械 ban 掉全部 counter。ban 需要兼顾敌方最可能的高质量路径和我方阵容可修补性。

## candidate_map_factor_eval

候选评估必须把地图适配写成可审计对象。

```yaml
candidate_map_factor_eval:
  candidate: string
  slot: early_pick | mid_pick | late_pick | ban
  satisfied_factors:
    - factor_id: string
      evidence: string
  exposed_factors:
    - factor_id: string
      risk: string
      mitigation: string
  terrain_state_dependency:
    depends_on:
      - intact_wall | broken_wall | uncleared_bush | cleared_bush | open_goal | closed_goal
    failure_if: string
  objective_contract_fit:
    primary_job: string
    backup_job: string
    cannot_do:
      - string
  decision:
    verdict: prefer | playable | conditional | reject | ban_priority
    reason: string
```

## 假阳性库

以下情况必须降权或拒绝：

- “有墙就适合投掷”：如果墙位不保护目标、敌方可轻易 dive、或破墙收益更高，投掷不是稳定答案。
- “有草就适合刺客”：如果草不能连接到目标、敌方天然带 scout、或进场后无法撤退，刺客只是一次性赌局。
- “开阔就选狙”：如果目标需要站点、护送、近身爆发或处理墙后单位，纯远程可能无法转化优势。
- “水多就选水上英雄”：如果水域不形成有效路线、无法威胁目标、或只是阻挡双方通路，水上能力价值有限。
- “Heist 只看 DPS”：如果没有防守、换线或 safe access，纸面 DPS 可能无法接触目标。
- “Brawl Ball 只看破墙”：破墙可能同时释放敌方远程角度，必须说明破墙后的收益归属。
- “Hot Zone 只看能站区”：站区英雄如果没有反清区、续航或队友覆盖，会变成送节奏。
- “Bounty / Knockout 只看击杀”：击杀窗口若不能稳定接近，或领先后无法保星 / 收缩，不能高估。

## 输出格式

BP 报告中可以使用 `map_factor_summary`：

```yaml
map_factor_summary:
  decisive_map_factors:
    - factor: string
      bp_impact: string
      affected_slots:
        - early_pick
        - ban
  hard_gates:
    - gate: string
      passed_by:
        - candidate
      failed_by:
        - candidate
  terrain_state_assumptions:
    - state: string
      consequence: string
  candidate_notes:
    - candidate: string
      map_fit: string
      risk: string
```

人类可读报告不需要暴露完整 YAML，但内部交付中间产物应能稳定产出同等字段。

## 来源 ingest

Fandom 地图页通常能提供：

- `Layout`：墙体、草、水、地图结构和目标区位置。
- `Tips`：推荐打法、路线、英雄类型和常见风险。
- `History`：地图更名、池子轮换或结构调整。

转换规则：

- `Layout` 进入 `topology`、`objective_access` 和 `lane_dynamics`。
- `Tips` 进入 `tactical_features`、`map_rules` 和 `example_brawlers`。
- 示例英雄只作为候选线索，不能直接变成版本强度结论。
- 如果来源只支持粗判断，标记 `source_status: needs_recheck` 或 `first_pass_from_fandom_text`。
- 只有经过 BP 复核的地图实体页才能作为 runtime index 编译的稳定输入。

## 更新规则

当地图来源更新时：

1. 先保存或引用 raw / source 层证据。
2. 如果地图结构、目标通路、墙草水位置或模式规则改变，更新地图实体页。
3. 如果只影响赛季入池状态，更新赛季地图池索引。
4. 如果版本强度改变某些英雄的地图适配，但能力类型未变，保留在来源层或强度层，不改地图页。
5. 如果平衡性改动让英雄和地图 hook 发生定性变化，更新对应英雄页稳定字段。
6. 更新 [[index|Wiki Index]] 和 [[log|Wiki Log]]。

## 关联页面

- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]
- [[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]
- [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- [[sources/Fandom-Ranked-Map-Source-Assessment|Fandom Ranked Map Source Assessment]]
- [[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom Ranked Season 46 Map Pages]]
- [[sources/User-Note-Map-Profile-Schema|User Note - Map Profile Schema]]
- [[sources/User-Note-Map-Factor-BP-Expression|User Note - Map Factor BP Expression]]
- [[sources/User-Note-Map-Layered-Governance|User Note - Map Layered Governance]]
