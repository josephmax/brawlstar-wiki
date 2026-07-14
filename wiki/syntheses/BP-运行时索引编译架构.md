# BP 运行时索引编译架构

状态日期：2026-07-10。性质：`runtime_architecture_implemented`。来源：[[sources/User-Note-BP-Runtime-Index-Compilation|用户经验来源摘要: BP 运行时索引应按版本语境编译]]。

本页记录 BP skill 的 compile-first 架构决策：长期 wiki 只维护稳定底层事实；每次 BP 前由 skill 将底层事实和用户 / 社区 / 选手的强度理解编译成运行时索引；正式 ban / pick 决策只消费该运行时索引。该架构已经落地；当前可执行 contract 以 `skills/brawl-stars-bp-slot-decision/` 为准，质量演进与踩坑见 [[syntheses/BP-知识压缩与决策质量演进复盘|BP 知识压缩与决策质量演进复盘]]。

## 核心结论

按奥卡姆剃刀，长期知识层不应保留人工维护的“决策索引”中间层。真正需要长期维护的是：

- 英雄底层 BP 能力：`capability_vector`、`build_switches`、`map_feature_hooks`、`objective_contracts`、`failure_modes`、`conditional_matchups`、`slot_notes`。
- 地图底层 BP 事实：`map_profile`、`map_bp_factors`、路线、位置、目标收益、地形状态计划、假阳性过滤。
- 版本 BP 审计：哪些补丁 / 重做 / Buffies / Hypercharge 改变了能力语义，哪些只是数值强弱或观察项。
- 外部或用户强度理解：作为 `strength_profile` 输入，不进入英雄百科或稳定地图页。

运行时索引仍然必要，但它应是可再生的编译产物，而不是手写 wiki 事实页。

## 分层模型

```text
Stable Wiki Source
  英雄页 + 地图页 + schema + 版本审计

Strength Profile
  用户 / 社区 / 选手输入的当前强度理解

Session Compile
  Stable Wiki Source + Strength Profile + 当前地图池
  -> runtime_bp_index

BP Decision
  runtime_bp_index + 当前 ban/pick/slot + strategy_bias
  -> ban / pick 候选与理由
```

## BP Skill 领域边界

BP skill 应从单一“决定这一手”扩展为两个明确子领域。

### 1. compile / understand-version

职责：理解当前版本语境，生成本次 BP 会使用的索引。

输入应包含：

```yaml
compile_input:
  patch_id:
  map_pool:
  available_brawlers:
  strength_profile:
    profile_id:
    owner:
    scope: global | mode | map | custom
    entries:
  source_policy:
    read_stable_wiki_only: true
```

输出是 `runtime_bp_index`，至少包含：

```yaml
runtime_bp_index:
  manifest:
    patch_id:
    map_pool_id:
    strength_profile_id:
    strength_profile_hash:
    source_hash:
    compiler_version:
    compiled_at:

  map_duties:
    map:
      objective_contracts:
      required_capabilities:
      route_gates:
      false_positive_filters:

  brawler_cards:
    brawler:
      capabilities:
      builds:
      failure_modes:
      strength_visibility:
      proof_threshold:

  map_brawler_edges:
    map + brawler:
      fit:
      payoff:
      fails_if:
      slot_notes:

  matchup_edges:
    subject + target:
      direction:
      active_when:
      fails_when:
      adjusted_confidence:

  ban_pressure:
    map:
      must_answer_routes:
      plan_protection_bans:
      overpowered_route_bans:

  query_keys:
    by_capability:
    by_map:
    by_slot:
    by_enemy_pick:
    by_own_gap:
```

编译阶段不能只是 LLM 自由总结。它必须有固定 schema、来源引用、hash 和校验器，否则会把 strength profile 与底层事实揉成不可审计的混合判断。

### 2. decide

职责：只消费 `runtime_bp_index`，在当前 draft 状态中做 ban 或 pick 决策。

输入应包含：

```yaml
decision_input:
  runtime_index:
  map:
  mode:
  current_slot:
  our_picks:
  enemy_picks:
  bans:
  strategy_bias:
```

决策阶段不应常规读取底层 wiki。如果 runtime index 缺失、过期或 hash 不匹配，应报告 `runtime_index_stale_or_missing`，而不是临场翻百科补答案。

## Strength Profile 的位置

强度理解是编译参数，不是事实源。它可以来自用户、社区、选手、赛事样本或自定义 agent，但必须在运行报告中可见。

它允许影响：

- 候选可见性。
- 理论候选的证明门槛。
- 对位边的可信度排序。
- ban 压力。
- 低强度但结构成立英雄是否仍进入候选池。

它不能影响：

- 地图结构事实。
- 英雄技能机制事实。
- 已经写入英雄页的长期能力语义。
- `hard_gate` 的基本逻辑。

例如 `Jacky` 可以在稳定英雄页中保留“墙边、草路、球门、热区有条件接触惩罚”的结构事实；若 strength profile 认为当前版本 Jacky 极弱，compile 只应提高她进入候选池的证明门槛，而不是删除底层能力。相反，`Brock` 或 `Surge` 如果补丁改变了自保、启动、开团或对刺客的成立条件，则应先更新英雄稳定字段，再进入编译。

## 现有索引页审计

从 [[index|Wiki Index]] 的 BP Runtime 入口看，当前两个 Markdown 索引页不再适合作为长期运行时事实源。

| 文件 | 当前作用 | 问题 | 建议 |
| --- | --- | --- | --- |
| BP 条件化对位边索引（已删除） | 曾汇总英雄页 `conditional_matchups`，供 skill 检索对位边。 | 混合了结构对位、`bp_use`、候选用途、slot 语境和部分 build / 版本能力状态；与英雄页存在同步漂移风险。 | 已于 2026-07-02 从长期 wiki 中删除；之后由 compile 阶段从英雄页自动抽取。 |
| BP 英雄地图特征适配索引（已删除） | 曾汇总英雄 map hook 和具体 Ranked 地图 hook。 | 同时包含结构 hook、具体地图收益、失败条件、`candidate_eval` / `slot_task` 标签，已经接近运行时决策卡；与英雄页 / 地图页重复。 | 已于 2026-07-02 从长期 wiki 中删除；之后由 compile 阶段从英雄页和地图页自动抽取。 |
| BP 实战查询速度与模型形态评估（已归并） | 2026-07-01 的运行形态评估。 | 仍以 Markdown 检索索引为主要运行假设，已被本页的 compile-first 架构推进。 | 已归并到 [[syntheses/BP-维护归档|BP 维护归档]]；本页是新的 runtime 设计入口。 |
| [[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]] | 当前赛季地图池索引。 | 只记录地图池和入口，不混合强度或候选优先级。 | 保留；它是 compile 输入，不是噪声索引。 |

因此，已经删除的噪声索引是：

- `wiki/syntheses/BP-条件化对位边索引.md`
- `wiki/syntheses/BP-英雄地图特征适配索引.md`

它们本质上只是为了减少 BP 决策读取底层事实时的手写快速知识。方法论成熟后，等价信息应由 `bp compile` 子命令或等价流程从英雄页、地图页、模式页和强度输入中重新生成，而不是继续手写维护。

## 迁移步骤

1. 已将两个旧 Markdown 索引从 BP Runtime 入口移除并删除源文件。
2. 已在 `skills/brawl-stars-bp-slot-decision/` 中落地 `compile` 流程，生成 `runtime_bp_index`。
3. `decide` 已改为通过 precheck、query 和 hydrate 小窗口消费 `runtime_bp_index`，不全量读取 JSON。
4. 事实查询工具已收窄为中立召回；当前 draft 解释、候选比较和最终 ban/pick 由 LLM 负责。
5. 人类审计所需的厚数据继续作为 debug artifact 或独立 decision log 输出，不作为长期 wiki 页面维护。

## 历史过渡规则（已失效）

以下规则只记录 compile 落地前的过渡状态，当前 runtime 不再使用：

- 事实源仍是英雄页和地图页。
- 没有 `runtime_bp_index` 时，直接从英雄页的 `conditional_matchups`、`map_feature_hooks`、`objective_contracts`、`failure_modes` 和地图页的 `map_bp_factors` 派生候选。
- 不新建手写对位边索引、地图 hook 索引、候选排序表或固定 pick 优先级表。
- 任何“当前版本强度”相关判断必须等待 strength profile 或明确的版本审计输入。

## 关联页面

- [[sources/User-Note-BP-Runtime-Index-Compilation|用户经验来源摘要: BP 运行时索引应按版本语境编译]]
- [[syntheses/BP-推理DSL规范|BP 推理 DSL 规范]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- [[syntheses/BP-维护归档|BP 维护归档]]
- [[syntheses/BP-英雄建模标准流程|BP 英雄建模标准流程]]
