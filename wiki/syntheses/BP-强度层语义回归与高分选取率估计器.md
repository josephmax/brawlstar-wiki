# BP 强度层语义回归与高分选取率估计器

状态日期：2026-08-14。性质：`design_discussion_in_progress_non_runtime`。

本文记录一次围绕"强度榜被误用"展开的维护者讨论：从 Spike 三人池评价中暴露的强度误用，到重新界定强度层的领域与边界，再到提出用"高分选手选取率"作为强度层的揭示式估计器。它是活的维护者讨论页，不是 BP runtime 规则；只有被明确采纳的结论才会进入 skill references 和实现计划。

背景前置：[[syntheses/BP-知识压缩与决策质量演进复盘|BP 知识压缩与决策质量演进复盘]]（其中"第二次质量下降"记录了强度污染地图适配的历史）、[[syntheses/BP-下一阶段迭代方向决策记录|BP 下一阶段迭代方向决策记录]]。

## 一、讨论缘起：强度被误用进了"上分泛用性"判断

维护者要求评价"只精通 Emz / Spike / Rico 的强度与上分上下限"。初始回答以 iKaoss11 July 2026 强度榜为主轴，并引用了 `outputs/strength-profiles/ikaoss11-ranked-map-adapted-preview.json` 的"全图 C/D 矩阵"，据此把 Spike 判为三人中的短板。

用户提出两点纠正：

1. 强度榜是"非常没有共识的东西"（单一创作者的主观先验），不应作为主要依据；Spike 反而是难被后手 counter 的先手 pick。
2. 该"每英雄×每地图评级矩阵"并非维护者设计的评价体系，质疑其出处。

核实后确认：

- 该矩阵出自 `tools/strength-profile-editor/scripts/generate_map_strength_profile.py`，是 2026-07-07 生成的**机器底稿**，日志明确记录"供后续人工审计和逐图细调"，README 声明"地图强度需要显式维护；通用强度只表达版本先验，不能当作地图适配性证明"。
- 其推导逻辑（`adjusted_tier(global_tier, fit)`）是"全局档位 × 粗粒度 fit 桶"的确定性映射：Spike 的"全图 C/D"≈ 其全局 C 档的重表述，几乎不含独立地图信号。
- 因此把该草稿当"被采纳的评价体系"引用，属于对强度榜的二次循环论证。

## 二、结论 1：强度是"环境信号"，不是"英雄属性"

强度描述的不是"这个英雄有多好"，而是"**当前版本环境对它的临时升降**"。

| 表述 | 语义 |
| --- | --- |
| 强度 = 环境基线先验（base-rate prior） | 无其他条件时英雄在当前补丁环境中的平均可用性 |
| 强度 ≠ 英雄价值 | 英雄价值由稳定事实（能力/职责/对位条件）、局面对位、玩家执行决定 |

合法用途（均发生在结构门槛之后）：

1. 同层候选的 tie-break（已过图/模式/对位门槛的候选之间分高下）。
2. ban 与英雄池规划的参考面（"这版本谁整体上是环境宠儿/弃子"）。

禁止用途（延续既有设计红线）：地图适配 fit、模式资格 eligibility、对位结论、决策排序规则。任何 fallback 都不能把全局强度补成地图适配或候选资格。

## 三、结论 2：估计器视角——声明式 vs 揭示式

强度层本质是对同一潜在对象（当前环境的 meta 先验）的估计，不同来源是不同估计器：

| 估计器 | 类型 | 机制 | 优点 | 缺点 |
| --- | --- | --- | --- | --- |
| 职业/社区强度榜（如 iKaoss11） | 声明式（declarative） | 创作者说"我判断 X 强" | 快、显式、跟补丁 | 单人无共识、主观 |
| **高分选手 pick(+ban) rate** | 揭示式（revealed） | 高分玩家在真实 BP 约束下用行为投票 | 聚合、去主观、**与胜负有选择压力地因果耦合**（总输的 pick 被淘汰、总赢的 pick 扩散） | 滞后（创新边界处盲）、混淆项多、不可分解 |

关键论证：行为估计器与它要估的量因果耦合——"赢的人实际做什么"优于"某人说他信什么"。这是成熟 meta 统计（u.gg / op.gg 等）的标准做法：以高段位 pick/ban/win 为锚，而非主播榜单。

## 四、结论 3：高分选取率是强度的"更合理估计器"，不是"替代品"

选取率不能整体替代强度层的原因（与既有设计红线一致）：

1. **它是合成数，不是分解**：选取率 = 版本强弱 + 先手安全性/counter 抵抗性 + 阵容灵活性 + 拥有/练度 + 流行度 + 本赛季地图池构成 + ban 交互，熔成一个数。系统审计需求（"这手为什么这么选"）无法由聚合输出回答。注意：它测的是"draft 偏好"，不是"强度"——用选取率替代强度榜会静默合并这两个概念。
2. **它在补丁边界和新英雄上最慢最盲**，恰是强度层最该灵敏的地方：8/4 削 8 英雄后选率要数周才下移；新英雄开局选率≈0 与实际强度无关。强度层的快 override 价值（补丁账本）不可被慢信号替代。
3. **它混入账号可用性**（大家是否已满级该英雄），重复了"strength_profile 与用户账号约束是两个领域对象，不应合并"的既有决定。
4. **它被本赛季地图池污染**：逐图决策系统中，若环境信号已带地图池影响，会双重计算地图因素。

正确设计：**强度层 = 当前版本环境证据的开放槽位，允许多来源类型并存，各自携带认识论元数据**。

| 来源类型 | 测什么 | 合法角色 |
| --- | --- | --- |
| 专家 tier list | 声明式版本判断 | 快 override（补丁期、新英雄期） |
| 高分 pick+ban 统计 | 聚合显性 draft 偏好 | 慢基线（稳态期，tie-break 级） |
| 用户手工调校 | 自己的版本理解 | 终审 |

三通道失效区互补：行为估计器治"无共识"，补丁账本治"滞后"，用户调校治"样本盲区"。

## 五、结论 4：(pick, ban) 必须成对使用

单一 pick rate 会把"强势但被禁"误读成"弱"（压制性英雄被 ban 多 → 裸选率被压低）。二维对能表达 tier list 表达不了的结构：

- 高 pick + 低 ban = 灵活的安全先手（Spike 型）
- 高 pick + 高 ban = 压制但被争抢（削弱前的 Meg / 8-Bit 型）
- 低 pick + 高 ban = 冷门但被忌惮的 counter

## 六、残余误差与兜底

揭示式估计器唯一的系统性弱点：**创新边界处的滞后**——新强策略（补丁刚改、新英雄刚出）在均衡形成前选率≈0。补丁账本（`balance_breakpoint_manifest.v1`、维护清单）是结构化的快通道，负责在均衡形成前 override。iKaoss11 榜降级为"快 override 的候选来源之一"，不再是默认慢基线。

## 七、认识论元数据要求（schema 待落地）

强度档案必须自报置信边界，任何下游不得再无声把它当硬事实：

- `consensus`：single-creator | community | aggregate
- `recency` / `captured_at` / `patch_id`：距最近补丁多久
- `derived`：是否从其他层推导（如生成的 map 底稿）
- `status`：final | draft-not-audited
- 若来源为统计：`rank_floor`（大师/神话+）、`window`、`sample_size`、`companion_ban_rate`（是否成对）

## 八、教训：强度会渗入每个"没有证据归属"的问题类

这是同一疾病的第二次发作。第一次是地图适配（已由 [[syntheses/BP-知识压缩与决策质量演进复盘|BP 知识压缩与决策质量演进复盘]] 修复，含 Damian/Backyard Bowl 回归测试）；第二次是"上分泛用性 / 英雄池规划"。两类问题的共同点：**缺少明确证据契约**，于是强度成为默认 fallback。

英雄池规划问题类应补的证据契约（主驱动）：counter 抵抗性（counter 集窄度 × 频率 × 地图条件）+ 模式/地图覆盖广度 + 操作上限 + 账号状态；强度在该问题类中只做"版本相关性检查"（patch relevance：被削/被抬/中性），不做排名。

## 九、待决问题

> [!question] 1
> 是否确认强度层重定义为"环境基线先验 + 多来源开放槽 + 认识论元数据"，并把 iKaoss11 榜降级为快 override 候选来源？

> [!question] 2
> 是否接受"英雄池规划"问题类证据契约（counter 抵抗性 + 覆盖广度 + 上限 + 账号状态为主驱动，强度仅做 patch relevance 检查）？

> [!question] 3
> "高分"的粒度定义：大师起还是神话+起？第三方站点（如 MetaCoreTroll）在大师段的逐图样本较薄，是否接受"神话+/传奇+ 全局 pick/ban"作为实际粒度，逐图的事交给 map fit 层？

> [!question] 4
> `ikaoss11-ranked-map-adapted-preview.json` 这类生成底稿的处理：加 `status: draft-not-audited` 标记保留，还是移出 outputs 消费路径？

## 十、已采纳决定（2026-08-14）：减法方案

维护者拍板：**整个体系不再消费 strength，也不保留任何 tier 概念**。环境信号固定命名为 high-rank pickrate，当前为空槽，先改实现。

具体采纳内容：

1. **概念删除**：`strength` / `tier` / `strength_profile` / `strength_weight` / `proof_threshold` 从代码、schema、skill 文档、决策规则、manifest 中移除；不向后兼容旧 schema。
2. **唯一环境信号 = high_rank_pickrate**（与 ban rate 成对）；数据槽当前为空（`manifest.pickrate_status: "empty"`），接入后作为独立证据层，仍不能升级 fit / eligibility / slot。
3. **旧档案退役**：iKaoss11 来源页标注 deprecated；`default-strength-profile.json` 删除；`outputs/strength-profiles/`、`outputs/runtime-bp-index/strength-profile-with-nori.json` 及旧编译产物移入 `outputs/_retired/`。
4. **编辑器只删消费路径**：`tools/strength-profile-editor/` 保留代码，但产物不再被 compile 消费。
5. **无环境信号时不补造**：候选排序纯由地图证据（fit → hook/capability 信号 → 名称确定性）决定；ban_pressure 仅由 `fit: strong` + 地图信号驱动。
6. **契约测试加固**：`test_bp_skill_contract.py` 增加减法红线断言——runtime 产物中不得出现 `strength_weight` / `strength_tier` / `strength_rank` / `strength_context` / `default-strength-profile` 等消费性 token。

实施状态（2026-08-14，feature 分支 `feature/brawlstar-remove-strength`）：

- ✅ compile_runtime_index.py：删除强度输入 / tier / rank / strength_context / proof_threshold / avoid_without_proof，manifest 记录 pickrate 空槽
- ✅ runtime_index_tools.py / query_runtime_facts.py / hydrate_runtime_facts.py / runtime_index_precheck.py：删除 strength 字段与参数
- ✅ compile-knowledge.md / runtime-decision-knowledge.md / SKILL.md（slot-decision 与 run-brawl-stars-bp）同步重写
- ✅ AGENTS.md / README.md / 契约测试更新；slot-decision 21 个测试 + bp skill contract 全绿
- ✅ 生成新索引 `outputs/runtime-bp-index/default-runtime-index.json`（30 图 / 105 英雄 / pickrate_status=empty / 无 tier）
- ⏳ 待办：pickrate 数据源调研与接入（待决问题 3）；编辑器退役标注；`BP-运行时索引编译架构.md` 同步

## 关联页面

- [[syntheses/BP-知识压缩与决策质量演进复盘|BP 知识压缩与决策质量演进复盘]]
- [[syntheses/BP-下一阶段迭代方向决策记录|BP 下一阶段迭代方向决策记录]]
- [[syntheses/BP-运行时索引编译架构|BP 运行时索引编译架构]]
- [[syntheses/Ban-Pick-问题拆分|Ban Pick 问题拆分]]
- [[syntheses/条件化对位模型|条件化对位模型]]
- [[sources/iKaoss11-July-2026-Strength-Profile|iKaoss11 July 2026 Strength Profile]]
- [[sources/Supercell-Maintenance-August-4-2026|Supercell 来源摘要: Maintenance - August 4, 2026]]

执行规则入口（修改时须保持与本文一致）：

- `skills/brawl-stars-bp-slot-decision/references/compile-knowledge.md`
- `skills/brawl-stars-bp-slot-decision/references/runtime-decision-knowledge.md`
- `tools/strength-profile-editor/`
