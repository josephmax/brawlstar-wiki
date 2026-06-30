# 英雄 BP 建模升级任务计划

本计划用于把英雄知识从“人类可读机制摘要”升级为“可供 BP DSL 消费的结构化中间层”。本页只定义交接计划，不执行抓取、不批量修改英雄页。

计划日期：2026-06-29。维护者最初要求按当前 105 位 Fandom roster 建立完整 manifest；后续维护者校正指出 `Buzz Lightyear` 是临时英雄且已下架，不进入 BP 建模。当前执行规则是：先保留 105 行 roster manifest 作为上游抓取事实，再按 104 个非临时英雄作为 BP-active scope 执行。

## 交接目标

额度重置后的会话应能按本页直接开工，完成以下闭环：

1. 建立当前 105 行 Fandom roster manifest。
2. 对每个英雄保留 Fandom 详情页 raw capture。
3. 对每个 PLP 可达英雄保留 Power League Prodigy 详情页 raw capture。
4. 从 raw 生成 source 摘要，保留来源差异与证据强度。
5. 将 BP-active 英雄页升级为 BP-ready 中间层。
6. 将 build、地图、模式、对位、slot 风险接入 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]。
7. 更新索引和日志，确保后续 BP 查询能读到新结构。

## 当前状态

已有资产：

- `wiki/entities/brawlers/`：72 个英雄页。
- `wiki/sources/Fandom-*.md`：这 72 个英雄已有 Fandom 来源摘要。
- `raw/sources/fandom/heroes/`：72 个英雄 raw 文件。
- [[sources/Power-League-Prodigy-站点与抽检|PLP 站点与抽检]]：已抽检 `Brock`、`Gene`、`Otis`、`Shade`、`Belle`、`Kaze`、`Colt`、`Angelo`。
- `wiki/entities/maps/`：26 张 Ranked Season 46 地图已升级为 `bp_map_profile_v2`。

关键缺口：

- Fandom roster raw scope 为 105；BP-active scope 为 104，排除临时下架英雄 `Buzz Lightyear`。
- 本地缺 33 个 Fandom roster 实体页；其中 `Buzz Lightyear` 不进入 BP，因此 BP-active 缺 32 位英雄的实体页、source 摘要和 raw。
- 现有 72 个英雄页没有结构化 `bp_brawler_profile`。
- 71 个 Fandom hero raw 是 `provisional raw backfill`，不是完整网页正文。
- PLP 只做过抽检，没有全英雄详情页 raw。
- 当前英雄知识还没有系统接入 `map_bp_factors`、`candidate_eval`、`conditional_matchup` 和 slot policy。

## 不做什么

执行会话不得做这些事：

- 不直接把 Fandom tips 或 PLP counters 复制成最终 BP 结论。
- 不为凑完整而写粗标签，例如 `good_on_open_maps`、`counter_tank_high`、`mode_fit: high`。
- 不在没有 raw 证据的情况下生成看似结构化的 BP 字段。
- 不把版本强度写进稳定英雄事实；版本强度应进入 meta overlay。
- 不覆盖旧 raw；重抓时创建新的 dated raw capture。

## 信息分层

### raw 层

raw 层保存来源本体或可见摘录，不做模型判断。

建议目录：

```text
raw/sources/fandom/heroes/<slug>-2026-06-29.md
raw/sources/pl-prodigy/brawlers/<slug>-2026-06-29.md
raw/sources/roster/brawlers-roster-2026-06-29.md
```

每个 Fandom hero raw 至少保留：

- 页面标题与 URL。
- 抓取日期。
- 英雄稀有度、官方定位、移动速度等基础属性。
- 普攻、Super、Trait、Gadget、Star Power、Hypercharge。
- Usage / Tips / Strategy 中与地图、模式、对位、build 有关的原文片段。
- 页面的更新时间或版本提示，如可见。
- 抓取边界：完整正文、可见片段、或因页面限制只能部分摘录。

每个 PLP hero raw 至少保留：

- 页面标题与 URL。
- 抓取日期。
- 推荐 Gadget、Star Power、Gears。
- 推荐 Modes / Maps，如页面提供。
- `countersThese` / `counteredBy` 原始列表。
- notes / draft advice / pro preference，如页面提供。
- payload 字段名，避免丢失来源结构。
- 抓取边界和页面可达性。

### source 层

source 层解释单个来源，不合并成最终结论。

建议目录：

```text
wiki/sources/Fandom-<Brawler>.md
wiki/sources/PLP-<Brawler>.md
wiki/sources/Brawler-Roster-2026-06-29.md
```

source 页必须标注：

- source_quality: `direct_raw_capture | provisional_backfill | partial_capture | inaccessible`
- source_type: `official_or_wiki_mechanics | third_party_competitive_guide`
- usable_for:
  - stable_mechanics
  - build_candidates
  - mode_fit_candidates
  - matchup_candidates
  - map_feature_candidates
- not_usable_for:
  - final_counter_claim
  - current_meta_strength_without_overlay
  - unconditional_bp_recommendation

### entity 层

英雄实体页保存稳定、可复用的英雄能力结构。

建议目录：

```text
wiki/entities/brawlers/<Brawler>.md
```

英雄页可以引用 Fandom 与 PLP source，但必须区分：

- 稳定机制事实：来自 Fandom。
- 竞技 build / mode fit / counter 候选：来自 PLP。
- 本地验证过的模式或对位修正：来自用户经验或复盘。
- 临时版本强度：不写入稳定实体页。

### synthesis 层

synthesis 层保存跨英雄、跨地图、跨模式的 BP 知识。

建议新增或维护：

```text
wiki/syntheses/英雄BP建模覆盖审计.md
wiki/syntheses/英雄BP建模升级任务计划.md
wiki/syntheses/BP-英雄能力词表.md
wiki/syntheses/BP-条件化对位边索引.md
wiki/syntheses/BP-英雄地图特征适配索引.md
```

其中后三个索引在执行阶段视需要创建，不在本计划会话创建。

## 105 行 roster manifest 与 104 BP-active scope

正式执行第一步必须建立 roster manifest，不要从本地 72 个英雄推断完整名单。

范围校正：[[sources/User-Note-Buzz-Lightyear-Out-of-Scope|维护者说明]] 已确认 `Buzz Lightyear` 是临时英雄且已下架。manifest 仍保留它，用于解释 Fandom 抓取为何返回 105 行；但它不进入 BP 建模、PLP 缺口追踪、英雄 raw 补抓批次、条件化对位边索引或地图适配索引。

manifest 字段：

```yaml
roster_row:
  canonical_name:
  aliases:
  fandom_url:
  plp_url:
  current_game_status: active | unavailable | unknown
  local_entity_status: exists | missing | needs_rename
  fandom_raw_status: direct_capture | provisional_backfill | missing | inaccessible
  plp_raw_status: direct_capture | missing | inaccessible | no_page_found
  fandom_source_status: exists | missing | stale
  plp_source_status: exists | missing
  bp_profile_status: none | partial | bp_ready
  notes:
```

验收条件：

- manifest 必须有 105 行。
- 本地已有 72 个英雄必须全部映射到 manifest。
- 缺失 33 个 Fandom roster 成员必须明确列出，并标出 `Buzz Lightyear` 为 `BP out-of-scope`。
- BP-active 缺口按 32 位非临时英雄处理。
- 名称差异要保留 aliases，不要用重命名覆盖历史链接。
- 每个英雄都要有 Fandom URL；PLP URL 可以是 `no_page_found`，但必须经过检查。

## BP-ready 英雄页目标结构

每个英雄页升级后应增加一个 `bp_brawler_profile` 区块。字段只保留有明确消费方的内容。

```yaml
bp_brawler_profile:
  profile_status: draft | reviewed | bp_ready
  source_quality:
    fandom:
    plp:
    user_notes:

  capability_vector:
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
    spawnable_or_pet:
    crowd_control:
    terrain_creation:
    terrain_destruction:

  build_switches:
    - build:
      source:
      changes_capabilities:
      enables:
      mitigates_failure_modes:
      best_when:
      poor_when:
      bp_use:

  map_feature_hooks:
    - map_feature_type:
      uses_feature_by:
      objective_conversion:
      active_when:
      fails_if:
      example_maps:
      bp_use:

  objective_contracts:
    - mode:
      can_fulfill:
      cannot_fulfill:
      needs_teammate_support:
      false_positive:

  failure_modes:
    - id:
      active_when:
      exposed_by:
      mitigation:
      bp_use:

  conditional_matchup_seeds:
    - target:
      direction:
      source:
      mechanism:
      active_when:
      fails_when:
      bp_use:

  slot_notes:
    slot_1:
    slot_2_3:
    slot_4_5:
    slot_6:
```

字段消费方：

- `capability_vector` -> `required_capabilities`、候选生成。
- `build_switches` -> `build_requirement`、`must_avoid`、`candidate_eval.risks`。
- `map_feature_hooks` -> `map_factor_fit`、地图假阳性过滤。
- `objective_contracts` -> `mode_fit`、阵容职责覆盖。
- `failure_modes` -> `must_avoid`、`false_positive_check`、ban 理由。
- `conditional_matchup_seeds` -> `conditional_matchup` 激活前的候选边。
- `slot_notes` -> `slot_fit`、暴露风险、last pick 惩罚。

## Fandom 对齐标准

Fandom 负责稳定机制事实，不负责最终 BP 判断。

抽取规则：

- 普攻 / Super / Gadget / Star Power / Hypercharge 先转为机制原子。
- 每个机制原子再转成能力影响，例如 `wall_break`、`knockback`、`slow`、`reload_pressure`、`pierce`、`bounce_wall`、`water_crossing`。
- Fandom usage tips 只能转成候选，不得直接进入最终结论。
- 如果 Fandom 给出“适合某地图/模式”的描述，必须继续拆成 map feature 或 objective contract。

示例转换：

```yaml
fandom_mechanic:
  text: Super destroys obstacles
  extracted_capability: terrain_destruction
  possible_bp_use:
    - transform_map_state
    - counter_thrower_pocket
    - expose_short_range_pick
  needs_context:
    - 当前地图开墙后谁收益更大
    - 我方是否有开墙后的 follow-up
```

## PLP 对齐标准

PLP 负责竞技 guide 信号，不负责最终真理。

抽取规则：

- 推荐 build 进入 `build_switches`。
- Modes 进入 `objective_contracts` 候选。
- `countersThese` / `counteredBy` 进入 `conditional_matchup_candidates`。
- Draft study 进入 `slot_notes`、ban 理由、路线保护或 last pick 惩罚样例。
- PLP 的强度、counter 和 mode fit 必须标注为第三方竞技信号。

示例转换：

```yaml
plp_counter:
  subject:
  target:
  raw_direction:
  converted_to_candidate:
    mechanism:
    active_when:
    fails_when:
    bp_use:
  status: candidate_only_not_final
```

## 与地图中间层对齐

英雄能力必须接到 [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]，不要只写“适合开阔图/墙多图”。

地图 hook 的目标表达：

```yaml
hero_map_factor_link:
  brawler:
  map_feature_type:
  capability_used:
  route_or_position:
  objective_payoff:
  failure_condition:
  false_positive_filter:
  example_maps:
```

典型 hook：

- `long_sightline`：长线压制、远程点杀、低成本目标输出。
- `wall_break_transform`：开墙后远程接管或反投掷。
- `thrower_pocket`：隔墙控区、迫使敌方绕路。
- `bounce_wall`：弹墙角度、走廊压制。
- `grass_anchor`：Speed / Vision / 伏击 / 探草。
- `water_crossing`：过水路线、绕后、目标访问。
- `base_corner`：目标附近持续生存。
- `central_congestion`：连锁、穿透、召唤物、线性压制收益。

每个 hook 必须有 `failure_condition`，否则容易制造假阳性。

## 与模式目标对齐

英雄不是只适合“某模式”，而是能否履行该模式的目标契约。

```yaml
mode_objective_link:
  mode:
  objective_contract:
  brawler_can_do:
  brawler_cannot_do:
  needs_support:
  failure_mode:
```

模式目标示例：

- `Heist`：safe DPS、远程打库、开墙、入库、生存牵制、回防。
- `Brawl Ball`：控球、推进、破门、清球、反推进、得分窗口、加时开图。
- `Gem Grab`：中路控矿、gem carrier 安全、边路压制、倒计时防守。
- `Bounty`：低成本拿星、长线消耗、反刺客、保命、控制中星。
- `Knockout`：生存空间、缩圈前位置、减员确认、反投掷、反刺客。
- `Hot Zone`：站圈、清圈、分兵、轮转、远圈压力、本方圈锚点。

## 与顺位对齐

每个英雄都要回答：什么时候先手安全，什么时候反手强，什么时候 last pick 才能释放上限。

```yaml
slot_model:
  slot_1:
    value:
    risk:
    requires:
  slot_2_3:
    value:
    risk:
    pairs_with:
  slot_4_5:
    value:
    risk:
    protects_or_repairs:
  slot_6:
    value:
    risk:
    aggressive_when:
```

原则：

- `slot_1` 不追求花，追求低反制面和可延展计划。
- `slot_2_3` 既要回答敌方 1 位，也要建立己方第一层路线。
- `slot_4_5` 要修复己方 1 位、回答敌方 2-3 位，并避免被 6 位一手贯穿。
- `slot_6` 可以激进，但只在敌方无法修复结构问题时激进。

## 执行批次

### Phase 0: 准备与冻结

目标：只建立执行上下文，不抓详情。

步骤：

1. 读取本页、[[syntheses/英雄BP建模覆盖审计|英雄 BP 建模覆盖审计]]、[[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]、[[syntheses/条件化对位模型|条件化对位模型]]、[[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]。
2. 建立 105 行 roster manifest。
3. 对照本地 72 个英雄页，列出 33 个 Fandom roster 缺失项，并标注 `Buzz Lightyear` 为 BP out-of-scope。
4. 不改英雄页，只更新 manifest 和 log。

验收：

- roster 行数为 105。
- BP-active scope 为 104。
- 每行有 Fandom URL。
- 每行有 PLP URL 状态。

### Phase 1: 来源保留

目标：先保留原始信息。

步骤：

1. 分批抓 Fandom hero detail raw。
2. 分批抓 PLP hero detail raw。
3. 每批不超过 10 到 15 个英雄。
4. 对不可达页面写 `inaccessible` manifest，不伪造内容。
5. 不从 raw 直接生成 BP 结论。

验收：

- 每个英雄至少有 Fandom raw。
- PLP 可达页面有 PLP raw。
- raw 文件注明抓取日期、URL、字段边界。

### Phase 2: source 摘要

目标：把单来源转成可审计摘要。

步骤：

1. 为每个 Fandom raw 创建或更新 `wiki/sources/Fandom-<Brawler>.md`。
2. 为每个 PLP raw 创建 `wiki/sources/PLP-<Brawler>.md`。
3. 每个 source 页都写 `usable_for` 与 `not_usable_for`。
4. Fandom 和 PLP 意见不一致时保留冲突，不强行统一。

验收：

- 104 个 BP-active 英雄均有 Fandom source；`Buzz Lightyear` 不要求 source。
- PLP 有页面的英雄均有 PLP source。
- 每个 source 页可以追溯到 raw。

### Phase 3: BP-ready 英雄实体页

目标：升级英雄页，但仍保持单英雄稳定事实边界。

步骤：

1. 先处理高频样本英雄，不全量批量生成。
2. 每个英雄增加 `bp_brawler_profile`。
3. 所有字段必须带 source 或可追溯出处。
4. 不确定字段留空或 `unknown`，不使用粗标签补齐。
5. 将临时版本强度放到 meta overlay，不进入稳定英雄页。

建议首批：

- `Brock`
- `Gene`
- `Otis`
- `Belle`
- `Colt`
- `Angelo`
- `Shade`
- `Rico`
- `Mico`
- `Max`
- `Stu`

验收：

- 每个样本英雄能生成 `candidate_eval`。
- 每个样本英雄至少有 3 个 `failure_modes` 或明确说明缺证据。
- 每个 PLP counter 都只是原始候选，不是最终 counter。

### Phase 4: 条件化对位索引

目标：把 counter 候选从英雄页抽成可查询边。

步骤：

1. 建立 `BP-条件化对位边索引`。
2. 每条边必须有 `mechanism / active_when / fails_when / bp_use`。
3. 将 PLP counter、Fandom tips、用户经验分别标注来源。
4. 只收录能说明条件的边；不能说明条件的保留在 source，不进入索引。

验收：

- 没有无条件 `A counters B`。
- 每条边都能在当前地图/模式/build 下被激活或关闭。

### Phase 5: 地图适配索引

目标：把英雄能力接到具体地图因素。

步骤：

1. 建立 `BP-英雄地图特征适配索引`。
2. 以 26 张 Ranked Season 46 地图为第一批校验集。
3. 每条适配必须说明 route/position、objective payoff 和 failure condition。
4. 优先处理 Heist、Bounty、Knockout、Brawl Ball 的高 BP 影响地图。

验收：

- 不出现“水多所以过水英雄都强”这类粗结论。
- 每条 map hook 都能进入 `candidate_eval.map_factor_fit`。

### Phase 6: 全量扩展

目标：从样本扩到 104 个 BP-active 英雄。

步骤：

1. 按模式和地图影响优先级分批，不按字母机械执行。
2. 每批结束做 lint：字段是否有消费方、source 是否可追溯、是否出现粗标签。
3. 更新 index 和 log。

建议批次：

- Batch A：已抽检 / 高 BP 影响样本。
- Batch B：地图强依赖英雄，例如投掷、弹墙、过水、开墙、草丛。
- Batch C：模式目标强绑定英雄，例如 Heist 打库、Brawl Ball 推进、Hot Zone 站圈。
- Batch D：高机动 / 刺客 / 反刺客链。
- Batch E：剩余英雄补全。

## 单英雄执行模板

每处理一个英雄，按这个 checklist：

1. 读取 roster manifest 行。
2. 读取 Fandom raw。
3. 读取 PLP raw，如可达。
4. 读取既有 `wiki/entities/brawlers/<Brawler>.md`。
5. 读取相关 source 页和用户经验页。
6. 抽取机制原子。
7. 转成 `capability_vector`。
8. 抽取 build switches。
9. 抽取 objective contracts。
10. 抽取 map feature hooks。
11. 抽取 failure modes。
12. 抽取 conditional matchup candidates。
13. 写 slot notes。
14. 更新英雄实体页。
15. 更新或创建 source 页。
16. 更新索引和 log。

## 质量门槛

一个英雄不能标记为 `bp_ready`，除非满足：

- Fandom raw 已直接抓取或明确说明为何只能使用 provisional source。
- 如果 PLP 页面可达，PLP raw 已保留。
- `capability_vector` 至少覆盖核心能力与核心短板。
- 至少有一个 `objective_contract`。
- 至少有一个 `failure_mode`，或明确说明该英雄缺少足够证据。
- 所有 counter 关系都是 `conditional_matchup_candidate`，没有无条件 counter。
- 至少一个 map hook 能连接到现有 map schema，或明确说明该英雄目前不依赖地图结构。
- `slot_notes` 覆盖四类顺位。
- 页面引用 source，source 可追溯 raw。

## 交接提醒

下一会话开始时，不要直接抓 105 个详情页。先读 Phase 0 的 roster manifest 和 [[sources/User-Note-Buzz-Lightyear-Out-of-Scope|Buzz Lightyear 范围校正]]。确认 105 行、URL、slug、已有 72 页映射、33 个 Fandom roster 缺口，以及 32 个 BP-active 缺口之后，再分批抓取。

本计划的核心不是“让资料看起来更全”，而是让每条英雄信息都能回答：它在 BP 中改变了什么决策。

## 关联页面

- [[syntheses/英雄BP建模覆盖审计|英雄 BP 建模覆盖审计]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
- [[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- [[sources/User-Note-Hero-BP-Ingest-Plan|用户经验来源摘要: 英雄 BP 建模 ingest 计划要求]]
- [[sources/User-Note-Buzz-Lightyear-Out-of-Scope|用户经验来源摘要: Buzz Lightyear 不进入 BP 建模]]
- [[sources/Power-League-Prodigy-站点与抽检|Power League Prodigy 站点与抽检]]
