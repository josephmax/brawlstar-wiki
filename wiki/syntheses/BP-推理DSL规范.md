# BP 推理 DSL 规范

这页定义本地知识库的 Ban Pick 推理协议。它的目标是让另一个 LLM 在没有当前聊天上下文时，也能按同一套结构理解局面、激活条件、生成候选，并输出可复盘的 BP 决策。

这份规范不是最终评分器，也不是英雄强度榜。它是 `map/mode/ban/pick/slot/brawler/build/matchup` 到 `当前最优 pick 或 ban` 的中间执行层。

## 执行合约

任何严肃 BP 推演都必须遵守这些前提：

- 默认双方都是高水平理性玩家；低分局炸鱼、段位噪音和对手低级失误不进入核心判断。
- 不允许直接把 `A counters B` 当作结论；必须说明机制、成立条件、失效条件和 BP 用途。
- 不允许只按英雄强度给答案；必须同时解释模式目标、地图结构、前序 pick、ban 位和当前 slot 的任务。
- 每轮输出必须给出 2 到 4 个可选决策，而不是只给一个孤立推荐。
- 每个推荐必须说明收益、风险、对手自然回应，以及是否依赖特定 build 或地图条件。
- 如果缺少地图、模式或 pick 顺位，必须显式标注不确定性，不能伪装成完整 BP 结论。

## Canonical Input

另一个 LLM 接到 BP 请求时，应先把用户输入转成这个结构。字段可以为空，但不能在推理中隐身。

```yaml
bp_case:
  mode_objective_profile:
    mode:
    primary_goal:
    required_roles:
    tempo_pressure:
    comeback_paths:
    objective_damage_importance:
    survival_importance:
    mobility_importance:
    control_importance:

  map_profile:
    name:
    mode:
    topology:
      zones:
      lanes:
      barriers:
      routes:
    objective_access:
      objective_type:
      direct_damage_lanes:
      base_entry_routes:
    tactical_features:
      - id:
        type:
        location:
        condition:
        enables:
        rewards_capabilities:
        punishes_capabilities:
        false_positive_capabilities:
        draft_implication:
    lane_dynamics:
      default_lane_assignment:
      congestion_triggers:
      split_pressure_value:
      grouping_punishers:
    map_rules:
      - if:
        then:
        because:
        bp_use:

  map_bp_factors:
    active_objective_contract:
    active_map_bp_factors:
      - id:
        source_feature:
        bp_relevance:
        current_owner: us | enemy | neutral | unknown
        urgency: hard_gate | core_duty | must_answer_route | plan_protection | slot_trap | conditional_opportunity | low_relevance
    duty_coverage:
      covered:
      missing:
      overexposed:
    terrain_state_plan:
      keep:
      transform:
      deny_enemy_transform:
    false_positive_alerts:

  ban_state:
    our_bans:
    enemy_bans:
    global_bans:
    unresolved_must_bans:

  draft_state:
    our_team:
    enemy_team:
    pick_order:
    current_global_slot:
    remaining_own_slots:
    remaining_enemy_slots:
    revealed_our_plan:
    revealed_enemy_plan:
    role_gaps:
    active_threats:
    protected_picks:
    exposed_picks:

  pick_slot_state:
    global_slot:
    team_side: first_pick_team | second_pick_team
    known_own_picks:
    known_enemy_picks:
    information_role:
    main_job:
    main_risk:

  available_pool:
    pickable_brawlers:
    banned_brawlers:
    unavailable_brawlers:
    version_overrides:

  knowledge_refs:
    brawler_profiles:
    build_profiles:
    conditional_matchups:
    source_notes:
```

## Knowledge Primitives

### map_profile / map_feature

地图不能只用 `open`、`wall_density`、`water_value` 这类粗分档表达。粗标签不进入 Canonical Input；真正参与 BP 的必须是具体地图特征如何打开路线、关闭路线、制造目标角度、奖励某类能力或制造假阳性。

完整 schema 见 [[syntheses/地图特征建模Schema|地图特征建模 Schema]]。最小可用对象如下：

```yaml
map_feature:
  id:
  type: river_crossing | long_sightline | lane_funnel | central_congestion | base_corner | bounce_wall | grass_anchor | thrower_pocket
  location:
  condition:
  route_effect:
    opens_routes_for:
    closes_routes_for:
    bypass_capabilities:
  combat_effect:
    rewards_capabilities:
    punishes_capabilities:
    false_positive_capabilities:
  objective_effect:
    enables_objective_pressure:
    enables_safe_positioning:
    required_followup:
  draft_implication:
    raises_pick_value:
    lowers_pick_value:
    creates_must_answer:
    creates_ban_reason:
```

`false_positive_capabilities` 是必要字段。例如在 `Safe Zone` 这类地图中，“可过水”会打开路线，但“可过水且手短、过河后缺少生存锚点或目标压力”可能仍然是陷阱，而不是强适配。

### map_bp_factors

`map_profile` 记录稳定地图结构，`map_bp_factors` 记录这些结构在当前 BP 中制造的决策义务。完整规范见 [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]。

```yaml
map_bp_factors:
  active_objective_contract:
    - 当前地图把模式目标转成的具体赢法
  active_map_bp_factors:
    - id:
      source_feature:
      factor_class:
      bp_relevance:
      current_owner:
      urgency: hard_gate | core_duty | must_answer_route | plan_protection | slot_trap | conditional_opportunity | low_relevance
      creates_draft_obligation:
      false_positive_filter:
  duty_coverage:
    covered:
    missing:
    overexposed:
  terrain_state_plan:
    keep:
    transform:
    deny_enemy_transform:
  slot_pressure:
    current_slot_job:
    next_enemy_slot_can_punish:
```

BP 推理时，`map_bp_factors` 负责回答：

- 当前地图有哪些非做不可的职责？
- 敌方已选英雄是否激活了必须回答的地图路线或地形锚点？
- 我方候选是否只是命中粗标签，但无法转化为目标收益？
- 当前 slot 是应该抢稳定地图职责、补缺口、保护地形状态，还是惩罚敌方无法修复的地图破口？

### brawler_profile

英雄必须被表达成能力向量，而不是单一定位。

```yaml
brawler_profile:
  name:
  effective_range:
  projectile_reliability:
  burst:
  sustained_dps:
  objective_damage:
  mobility:
  survivability:
  engage:
  disengage:
  anti_aggro:
  anti_tank:
  wall_break:
  throw_or_wall_bypass:
  area_control:
  scouting_or_vision:
  team_support:
  role_tags:
  failure_modes:
```

### build_profile

Build 是能力条件，不是装饰字段。

```yaml
build_profile:
  brawler:
  gadget:
  star_power:
  gears:
  enables:
  mitigates:
  weakens:
  best_when:
  poor_when:
```

### conditional_matchup

所有外部 counter 表都只能先进入这个结构。

```yaml
conditional_matchup:
  subject:
  target:
  direction: subject_favored | target_favored | volatile | even
  confidence: structural | map_dependent | comp_dependent | build_dependent | weak_signal
  mechanism:
  active_when:
    map_conditions:
    mode_conditions:
    comp_conditions:
    build_conditions:
  fails_when:
    map_conditions:
    mode_conditions:
    comp_conditions:
    build_conditions:
  bp_use:
    as_first_pick:
    as_response_pick:
    as_last_pick:
    as_ban_reason:
```

## Hard Gates

在思考“当前位置最需要什么能力”之前，必须先过硬门槛。硬门槛是会直接扭曲整局 draft 的威胁或机会。

```yaml
hard_gate_result:
  must_pick:
    - brawler:
      reason:
      expires_after_slot:
  must_ban:
    - brawler:
      reason:
      protected_plan:
  must_answer:
    - enemy_pick_or_plan:
      required_answer_type:
      deadline_slot:
  must_avoid:
    - brawler_or_plan:
      reason:
      exposed_to:
```

四类硬门槛的含义：

- `must_pick`：地图、模式或版本使某英雄成为低成本高收益先手，且不抢会被对手抢走。
- `must_ban`：某英雄会以极低成本拆毁我方计划，或在该地图模式里过强且我方缺少可靠答案。
- `must_answer`：敌方前序 pick 已经暴露必须处理的威胁，例如无解 safe DPS、坦克推进、投掷控区、刺客收割、治疗前排。
- `must_avoid`：某候选虽然符合能力需求，但会被敌方剩余 slot 以低成本惩罚。

硬门槛不是替代能力推理，而是先把“不能放任”的项排出来。通过硬门槛后，再进入当前位置策略和能力匹配。

## Slot Policy

顺位决定信息量和风险暴露。标准六手 draft 写作：

```text
1
2-3
4-5
6
```

其中 `1/4/5` 属于先手队，`2/3/6` 属于后手队。

```yaml
slot_policy:
  slot_1:
    main_job:
      - 稳定先手
      - 建立可延展计划
      - 不暴露易被 2-3 位成组惩罚的单点弱点
    preferred_traits:
      - 地图模式基本面强
      - 多 build 或多职责可转向
      - 被 counter 条件窄
    avoid:
      - 需要大量队友保护才能成立
      - 在该图存在明显低成本反制

  slot_2_3:
    main_job:
      - 回答敌方 1 位
      - 成组建立己方第一层胜利路线
      - 尽量制造 4-5 位必须同时处理多个问题的压力
    preferred_traits:
      - 一个负责回答已知威胁
      - 一个负责打开己方模式目标或地图强点
    avoid:
      - 两手都只防守但没有胜利条件
      - 两手共享同一个明显弱点

  slot_4_5:
    known_info:
      - 己方 1 位
      - 敌方 2-3 位
    main_job:
      - 回应敌方 2-3 位的成组计划
      - 修复或保护己方 1 位路线
      - 补完己方阵容基本面
      - 避免把结构性破口留给敌方 6 位
    preferred_traits:
      - 能同时补职责和反制敌方计划
      - 暴露面可控
      - 不依赖 6 位之后才会出现的信息
    avoid:
      - 让己方三个 pick 被同一类 last pick 一手贯穿

  slot_6:
    known_info:
      - 己方 2-3 位
      - 敌方 1/4/5 位
    main_job:
      - 最终反制
      - 惩罚敌方无法再修复的结构问题
      - 在基本面已满足时选择高上限路线
    aggression_rule:
      allowed_when:
        - 己方 2-3 位已经覆盖模式核心职责
        - 敌方 1/4/5 暴露明确弱点
        - 地图条件锁定，敌方没有后续 slot 修复
        - 该候选的失败条件已被 ban 或被己方阵容压低
      forbidden_when:
        - 己方缺少模式核心职责
        - 高上限 pick 只在对手失误时成立
        - 敌方阵容仍有自然答案
```

`slot_6` 可以激进，但这种激进必须是“理性惩罚”，不是赌博。它利用的是信息优势和对手无修复位，而不是期待对手不会处理。

## Decision Pipeline

每轮 BP 按这个顺序执行：

1. 解析 `mode_objective_profile`：先确认这一局如何赢。
2. 解析 `map_profile`：确定哪些 `map_feature` 被激活，哪些路线、目标角度、拥挤收益和假阳性风险成立。
3. 派生 `map_bp_factors`：把地图特征转成当前 draft 的目标契约、职责覆盖、地形状态计划、硬门槛和 slot 风险。
4. 更新 `ban_state`：确认哪些威胁已经消失，哪些威胁必须处理。
5. 更新 `draft_state`：识别双方已暴露计划、角色缺口和被保护或暴露的 pick。
6. 更新 `pick_slot_state`：明确当前手的信息量、主要任务和后续反制风险。
7. 运行 `hard_gate_result`：先处理必须抢、必须 ban、必须回答、必须避免的项。
8. 激活 `conditional_matchup`：只保留在当前地图、模式、阵容、build 条件下成立的对位边。
9. 推导 `required_capabilities`：列出当前位置最需要的能力，而不是先锁死某个英雄。
10. 生成候选：从可用英雄池中找能满足硬门槛、slot 任务和能力需求的 pick 或 ban。
11. 评估候选：对每个候选写出收益、风险、需要的 build、对手自然回应和后续阵容影响。
12. 输出 2 到 4 个优先决策：按“最稳基本面”“最高收益惩罚”“最强路线保护”“必要 ban”区分用途。

## Candidate Eval

每个候选必须转成这个结构，避免只给一句“选 X 很强”。

```yaml
candidate_eval:
  candidate:
  action: pick | ban | hold | avoid
  purpose:
    - build_plan
    - repair_gap
    - protect_pick
    - answer_threat
    - punish_enemy_structure
    - remove_route
  mode_fit:
  map_fit:
    activated_features:
    enabled_routes:
    objective_access:
    false_positive_risks:
    required_support:
  map_factor_fit:
    map_duties_covered:
    activated_map_bp_factors:
    objective_conversion:
    terrain_state_dependency:
    false_positive_check:
  ban_leverage:
  prefix_synergy:
  matchup_value:
    activated_edges:
    disabled_edges:
  role_coverage:
  build_requirement:
  exposure_risk:
  slot_fit:
  likely_enemy_response:
  verdict: top | viable | situational | avoid
```

`prefix_synergy` 指这个候选与己方已选英雄形成的前缀阵容结构；`exposure_risk` 指它会不会让敌方剩余 slot 获得低成本反制。

## Output Format

最终回答用户时，优先使用这个格式。自然语言可以更流畅，但信息不能缺失。

```yaml
bp_recommendation:
  context_summary:
    mode:
    map:
    current_slot:
    known_own:
    known_enemy:

  hard_gate_result:
    must_pick:
    must_ban:
    must_answer:
    must_avoid:

  active_conditions:
    map_conditions:
    activated_map_features:
    map_factor_summary:
      active_objective_contract:
      active_map_bp_factors:
      duty_coverage:
      terrain_state_plan:
      false_positive_alerts:
    mode_conditions:
    activated_matchups:
    disabled_matchups:

  required_capabilities:
    primary:
    secondary:
    avoid_exposing:

  candidate_evals:
    - candidate:
      action:
      verdict:
      reasons:
      risks:
      likely_enemy_response:

  top_decisions:
    - rank:
      action:
      candidate:
      why_now:
      required_build:
      risk_control:
      next_step_if_enemy_responds:

  draft_eval:
    our_win_condition:
    enemy_win_condition:
    role_coverage:
    exposed_weaknesses:
    qualitative_result: favored | even | risky | losing | uncertain

  uncertainty:
    missing_inputs:
    assumptions:
```

## Brock 对位样例

静态表可能写成：

```text
Mortis counters Brock
```

DSL 中必须改写为：

```yaml
conditional_matchup:
  subject: Mortis
  target: Brock
  direction: subject_favored
  confidence: map_dependent
  mechanism: Mortis 需要通过墙体、草丛、侧路或队友压迫缩短距离，绕过 Brock 的射程优势并贴脸击杀。
  active_when:
    map_conditions:
      - 墙体或草丛能切断 Brock 远程消耗
      - 侧路能让 Mortis 绕开正面火力
      - 接近路径不止一条
    comp_conditions:
      - Brock 缺少稳定反刺客队友
      - Mortis 队友能逼出 Brock 的保命资源
  fails_when:
    map_conditions:
      - 长线开阔
      - 过道明确
      - 接近路径单一
      - Brock 能提前开图和消耗
    comp_conditions:
      - Brock 队友有强 anti_aggro
  bp_use:
    as_response_pick: 只有地图允许接近且敌方保护不足时成立
    as_last_pick: 如果敌方三人都无法修复反刺客缺口，可以成为高收益惩罚
    as_ban_reason: 如果我方计划依赖 Brock 且地图允许刺客接近，Mortis 才成为合理 ban 候选
```

同理，`Stu` 或 `Max` 对 `Brock` 的压力更接近结构性高机动压制；`Cordelius` 或 `Mortis` 这类关系则更依赖地图接近路线。DSL 的任务就是保留这层差异。

## 禁止的捷径

- 不要在没有条件的情况下写“某英雄克制某英雄”。
- 不要把 PLP 等外部站点的 counter 字段直接复制为最终 BP 结论。
- 不要把段位预设写成严肃 BP 的核心因子。
- 不要因为某个英雄版本强，就忽略模式目标和地图结构。
- 不要把 `water_value: high`、`open: true`、`summary_tags` 这类粗标签放入 BP 输入或直接当成地图适配结论；必须解释具体路线、目标角度、站位收益和失效条件。
- 不要因为当前位置缺某种能力，就忽略 `must_ban`、`must_answer` 和 `must_avoid`。
- 不要把 `slot_6` 的激进选择理解成赌博；它必须建立在敌方无法修复结构问题的前提上。
- 不要输出没有风险说明的单点推荐。

## 来源接入规则

不同来源进入 DSL 的方式不同：

- Fandom：提供技能、机制、模式规则等稳定事实，主要进入 `brawler_profile`、`mode_objective_profile` 和基础概念页。
- Power League Prodigy：提供 build、mode fit、counter 候选、draft study 和版本强度信号，但 counter 必须先转成 `conditional_matchup`。
- 用户经验：用于修正模型边界、模式评价框架、顺位视角和静态 counter 的误用。
- 赛事或复盘：用于补充 `draft_eval` 样例，校准 ban 如何拆路线、pick 如何建立或破坏计划。
- 地图经验：进入 `map_profile` 与 `map_feature`，记录地形如何打开路线、制造目标角度、惩罚拥挤、产生假阳性适配和改变 ban / pick 价值。

## 关联页面

- [[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
- [[sources/User-Note-BP-DSL-Requirement|用户经验来源摘要: BP DSL 固化需求]]
- [[sources/User-Note-Map-Profile-Schema|用户经验来源摘要: 地图特征建模需要战术特征 Schema]]
- [[sources/User-Note-BP-Reasoning-Intermediate-Layer|用户经验来源摘要: BP 需要条件化推理中间层]]
- [[sources/User-Note-BP-Slot-Perspective|用户经验来源摘要: BP 位置视角修正]]
- [[sources/User-Note-Ban-Pick-High-Level-Assumption|用户经验来源摘要: BP 应按高水平对局预设]]
- [[sources/Power-League-Prodigy-站点与抽检|Power League Prodigy 站点与抽检]]
