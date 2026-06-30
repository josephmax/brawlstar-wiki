# 英雄 BP 建模覆盖审计

本页审计 `wiki/entities/brawlers/` 下英雄页是否足够支撑 [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]。审计日期：2026-06-29。

后续升级执行计划见 [[syntheses/英雄BP建模升级任务计划|英雄 BP 建模升级任务计划]]。该计划先保留 105 行 Fandom roster manifest 作为上游抓取事实，但按维护者校正排除临时下架的 `Buzz Lightyear`，以 104 个 BP-active 英雄为建模 scope。执行时仍要求先保留 Fandom 与 Power League Prodigy 详情页 raw，再做 BP 中间层抽象。

## 结论

当前英雄实体页不足以直接作为 BP-ready 输入。

它们能帮助 LLM 快速理解英雄大意，但还不能稳定支撑严肃 BP 推理。主要原因不是信息太少，而是信息没有被拆成可被 `hard_gate`、`required_capabilities`、`map_bp_factors`、`candidate_eval` 和 `conditional_matchup` 明确消费的结构。

这与 [[sources/User-Note-BP-Schema-Occam|BP Schema 奥卡姆剃刀]] 一致：不能因为一个字段“可能有帮助”就塞进 schema；英雄信息必须说明自己如何参与某个决策步骤。

## 当前覆盖

本地已存在：

- `wiki/entities/brawlers/`：72 个英雄实体页。
- `wiki/sources/Fandom-*.md`：这 72 个英雄都有对应 Fandom 来源摘要。
- `raw/sources/fandom/heroes/`：72 个英雄 raw 文件。

raw 层的来源质量需要分层看：

- `Shelly` 是 manual raw capture。
- 其余大多数英雄是 `provisional raw backfill`，即从既有 `wiki/sources/Fandom-*` 摘要页回填，不是完整网页正文。

因此，当前 Fandom 本地资料足够补“稳定机制事实”，但不应被误认为已经完整保留了 Fandom 网页所有细节。

## 当前英雄页能支持什么

现有英雄页通常可以支持：

- 英雄基础身份：稀有度、官方定位、粗角色类型。
- 主攻击和 Super 的核心机制。
- 若干自然语言适合场景，例如“开阔地图”“墙体多地图”“需要控区的模式”。
- 少量用户经验修正，例如 `Gene` 在 `Brawl Ball` 中不应被当作持球推进核心。
- 与少数相邻英雄的粗略差异，例如 `Brock` 与 `Colt`、`Barley` 的区别。

这些内容适合人读，也适合做第一轮能力抽取候选。

## 当前英雄页不能支持什么

现有英雄页不能稳定支持：

- `brawler_profile` 能力向量：例如射程、弹道可靠性、爆发、持续 DPS、objective damage、机动、生存、开团、脱战、反突、反坦、开墙、绕墙、控区、视野、团队支援等没有结构化。
- `build_profile`：Gadget、Star Power、Gear 如何改变能力、缓解什么失败条件、在哪些地图或模式中成立，基本没有沉淀。
- `conditional_matchup`：缺少“对谁有利、靠什么机制、有何地图条件、何时失效、BP 中用于先手/反手/ban/last pick”的结构。
- `map_feature_hooks`：英雄如何激活具体地图特征，例如 `long_sightline`、`wall_break_transform`、`thrower_pocket`、`grass_anchor`、`water_crossing`、`base_corner` 等，尚未和 26 张地图的 `map_bp_factor` 接起来。
- `failure_modes`：英雄在什么局面下会成为假阳性，例如短手过水但无目标压力、投掷遇到低成本开墙、慢弹道打高机动、坦克被反坦和减速链封死等。
- `slot_profile`：该英雄在 1 位、2-3 位、4-5 位、6 位分别适合承担什么任务、会暴露什么风险，还没有整理。

这意味着：当前英雄页不能直接用于候选排序，只能作为“机制事实 + 第一轮假设”的来源。

## Fandom 来源能补哪一层

Fandom 本地来源适合补：

- 主攻击 / Super / Gadget / Star Power / Hypercharge 的稳定机制。
- 弹道、范围、是否破墙、是否穿墙、是否召唤、是否位移、是否控制、是否治疗等能力事实。
- 官方或社区 tips 中的地图/模式适配候选。

Fandom 不适合直接补：

- 当前版本强度。
- 高水平 BP 中的先手/反手价值。
- 静态 counter 的最终结论。
- 精细地图适配，因为 tips 需要再经过本地 map schema 校验。

更关键的是：当前 71 个英雄 raw 是 provisional backfill。如果要精修重点英雄，最好重新抓取对应 Fandom 页面或使用已有 source 摘要时明确标注证据深度有限。

## PLP 来源能补哪一层

[[sources/Power-League-Prodigy-站点与抽检|Power League Prodigy 站点与抽检]] 比 Fandom 更接近 BP 层，已经抽检到：

- 推荐 Gadget。
- 推荐 Star Power。
- 推荐 Gears。
- 适合 Modes。
- `countersThese` / `counteredBy` 候选边。
- Safe Zone draft study 这类赛事 BP 复盘。

但 PLP 的 counter 仍不能直接写成最终 `conditional_matchup`。它只能作为候选边，必须继续补：

- 对位机制。
- 成立地图条件。
- 失效地图条件。
- 是否依赖 build。
- 在当前 slot 中是回答威胁、保护计划、拆路线，还是 last pick 惩罚。

## BP-ready 英雄页最小结构

后续改造英雄页时，建议只增加下面这类有明确消费方的结构：

```yaml
bp_brawler_profile:
  source_quality: fandom_summary | fandom_raw_capture | plp_sample | user_verified | mixed

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

  build_switches:
    - build:
      changes_capabilities:
      mitigates_failure_modes:
      best_when:
      poor_when:

  map_feature_hooks:
    - map_feature_type:
      uses_feature_by:
      objective_conversion:
      fails_if:
      example_maps:

  objective_contracts:
    - mode:
      can_fulfill:
      cannot_fulfill:
      needs_teammate_support:

  failure_modes:
    - id:
      active_when:
      bp_use: must_avoid | false_positive_filter | ban_reason | needs_protection

  conditional_matchup_seeds:
    - target:
      direction:
      mechanism:
      active_when:
      fails_when:
      source:

  slot_notes:
    slot_1:
    slot_2_3:
    slot_4_5:
    slot_6:
```

这些字段都有明确用途：

- `capability_vector` 进入 `required_capabilities` 和候选生成。
- `build_switches` 进入 `build_requirement`。
- `map_feature_hooks` 进入 `map_factor_fit`。
- `objective_contracts` 进入 `mode_fit`。
- `failure_modes` 进入 `must_avoid` 和 `false_positive_check`。
- `conditional_matchup_seeds` 进入 `conditional_matchup`，但必须在当前地图/模式/build 下激活。
- `slot_notes` 进入 `slot_fit` 和暴露风险判断。

## 改造优先级

不建议一次性把 72 个英雄都机械改成 BP-ready。更好的顺序是：

1. 先做高频 BP 样本英雄：`Brock`、`Gene`、`Otis`、`Belle`、`Colt`、`Angelo`、`Shade`、`Rico`、`Mico`、`Max`、`Stu`。
2. 每个英雄先用 Fandom 补稳定机制，再用 PLP 或用户经验补 build / counter 候选。
3. 优先接入已经完成 `bp_map_profile_v2` 的地图特征，尤其是 Heist、Bounty、Knockout、Brawl Ball 的明确目标契约。
4. 每条 counter 只保留为条件化边，不写无条件克制。
5. 对证据不足的字段用 `unknown` 或不写，不用粗标签凑完整。

## 对当前 BP 推理的实际影响

在完成英雄页升级前，BP 推理应这样读取英雄信息：

- 英雄实体页：只当作机制摘要和能力候选。
- Fandom source/raw：用于补技能事实，不直接补 BP 结论。
- PLP：用于 build、mode fit、counter 候选和 draft study，但必须转译。
- 地图实体页：提供稳定地图因素。
- BP DSL：负责把上述来源合成为当前局面的候选评估。

因此，当前最重要的缺口是“英雄能力与地图因素之间的中间层”，不是再增加粗粒度英雄标签。

## 关联页面

- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/英雄BP建模升级任务计划|英雄 BP 建模升级任务计划]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/地图因素BP表达规范|地图因素 BP 表达规范]]
- [[syntheses/地图特征建模Schema|地图特征建模 Schema]]
- [[sources/User-Note-BP-Schema-Occam|用户经验来源摘要: BP Schema 奥卡姆剃刀]]
- [[sources/Power-League-Prodigy-站点与抽检|Power League Prodigy 站点与抽检]]
