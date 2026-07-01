# Brawl Stars BP Agent Prompts

本仓库维护《荒野乱斗》BP 知识库与两个运行 skill：

- `run-brawl-stars-bp`：裁判 skill，只负责发牌、维护隐藏信息、cue 流程、记录选手提交内容和回合指标。
- `brawl-stars-bp-slot-decision`：选手 BP skill，负责读取 BP 运行时资料并对单个 ban / pick slot 做决策。

## 示例 1：调用裁判 skill 开一局 BP

```text
使用 $run-brawl-stars-bp 开一局 Ranked BP 模拟。

请从 `wiki/syntheses/Ranked-Season-46-地图Map-Profile总览.md` 的地图池里随机选一张地图，并读取对应地图实体页来确定 mode。

裁判只做 neutral_recorder / deal_cards_only：
- 红蓝各 3 个 ban 位，同时提交 ban，允许重复 ban。
- ban 后按 blue_slot1 -> red_slot2_3 -> blue_slot4_5 -> red_slot6 顺序 cue 双方选手。
- 创建红蓝子 agent 时就固定各自 `strategy_bias`，从 conservative / balanced / aggressive / high_variance 中随机分配；后续不要额外校验风格合规。
- 子 agent 使用 $brawl-stars-bp-slot-decision 进行 ban / pick 思考。
- 每轮记录 actor、model、started_at、ended_at、elapsed_ms、token_usage；如果精确 token 不可见，写 `exact_token_usage_unavailable`，并记录 files/pages/commands/index hits。
- 完整逐局报告只作为临时运行产物写到 `outputs/bp-simulations/match-<地图名>.md`；不要写进 `wiki/syntheses/`。如果需要沉淀到 wiki，只提炼关键结论到 `wiki/syntheses/BP-模拟样本关键结论汇总.md`。

报告只中立记录选手提交的结论、理由、风险和最终陈述；裁判不要补充自己的 BP 分析，不要判断 favored side。
```

## 示例 2：直接调用 BP skill 做单手选择

```text
使用 $brawl-stars-bp-slot-decision 充分思考当前 BP slot，给出 2-4 个候选选择，并排序推荐。

输入：
- map: Double Swoosh
- mode: Gem Grab
- current_global_slot: 4-5，也就是蓝方两选
- our_picks: [Gene]
- enemy_picks: [Max, Sandy]
- bans:
  - blue_bans: [Kenji, Moe, Rico]
  - red_bans: [Lily, Angelo, Sprout]
- unavailable_pool: [Kenji, Moe, Rico, Lily, Angelo, Sprout, Gene, Max, Sandy]
- strategy_bias: aggressive
- strength_context:
  source: unknown
  meta_pressure: []
  overpowered_or_t0_exception: none
  counter_availability: unknown
  balance_volatility: unknown

请按 skill 要求读取 BP runtime 页面、地图页、相关英雄页、条件化对位边索引和地图 hook 索引。输出：
- context_summary
- hard_gate_result
- required_capabilities
- 2-4 个 candidate_evals
- top_decisions
- 每个候选的 construct_direction、capabilities_provided、answers_enemy_picks、answers_map_factors、risks_removed、new_risks_created、followup_needs、rejected_options
- 最终推荐、理由、风险和下一手需要防什么
```
