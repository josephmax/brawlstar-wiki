# 当前决策机制是否允许选出题库答案：路径审计

日期：2026-09-20。用户明确审计目标为“现有机制是否会在充分考虑对手克制与队友联动之前排除参考方案”，尤其第六手。本文补充并校正[上一轮证据充分性审阅](../bp-index-audit-2026-09-20/REPORT.md)的使用边界。

## 核心结论

**已确认存在过早排除路径。它们不是工具全局禁止选这些英雄，而是窗口定义、地图桶、排序预算以及后续规则的组合偏差。** 现行 skill 也存在保护：明确要求 Capability-Window First，允许弱地图候选进入比较，能力命中不截断。因此不能用“桶里没有”直接断言完整流程绝不可能选出。

上一轮 51/3/2 是“拿到所有事实后能否组织合理解释”的评级，**不是现有流程选出答案的能力评级**。尤其把“没补高血身体”等同占区闭环失败，本身可能沿用了过强的静态职责约束；第 41/47 题的 P 应保留为待解释项，不能升级成阻止候选进入比较的 gate。团队能通过清场、续航、保护或路线转换赢目标，补位者不必独立包办模式职责。

## 实测范围

同一份默认 35 图 index，56 题、115 个题目—候选记录；其中真正的第六手选人为 **18 题、27 个记录**（排除了 slot=6 但任务为 ban 的第 22 题）。每题实跑：

1. 对应选位桶 + 真实已知敌方 relation-target，按 skill 指定普通预算（早手/ban 24，4–6 手 32）。
2. 相同查询 limit=0，隔离预算截断。
3. 固定的 12 个能力轴各自 `@high` 查询：射程、爆发、目标伤害、机动、生存、反突、反坦、越墙、控区、支援、控制、视野。所有题使用相同轴；输入只使用地图和当前局面，不使用参考名字作 include。

合计 **784 次确定性事实查询**。12 轴是离线敏感性探针，**不是让正式每手查 12 遍**，也不是自动挑中正确窗口的模型运行。原始查询参数、完整返回 ID、参考项位置见 [matrix.jsonl](matrix.jsonl)，统计见 [summary.json](summary.json)。

|阶段|全量 115 记录|第六手 27 记录|能证明什么|
|---|---:|---:|---|
|不在地图选位桶|29|7|只走地图桶会先漏掉|
|桶 + 敌方关系，无预算上限，仍未出现|25|6|仅加当前关系查询仍不能补齐|
|桶 + 敌方关系，按 24/32 预算，未出现|61|13|实际排序截断进一步放大遗漏|
|至少一个预设高能力窗口能召回|115|27|工具存在合法召回路径，不证明模型会选对窗口或最终首选|

第 2 题两个无序组合在同一个 `effective_range@high` 探针均可见，不是把不同窗口里的单人命中冒充双选完成。所有参考项均不与题面已知已选/bans 冲突；bans 未提供/不完整不等于已确认全可用。

## 已定位的过早排除点

### A. 地图信号被编译成所有顺位共用的资格

`compile_runtime_index.py` 的 `slot_eligibility`（962 行）只看 map_floor。没有 hook/能力字符串匹配就 weak，早手、响应手、末手均 false。编译时还没有己敌阵容，因此这个资格不能表示“该完整对局不可选”。

第六手受影响的七个记录：**11 R-T、15 Fang、17 Lumi、35 Shade、37 Bull、46 Ziggy、50 Gray**。它们的末手职责分别可能是守库、反近身、清资源/控路、进库、侧路近身、墙后逼位、送现有前排进区。

现有能力窗口能绕过桶，所以这里是具体入口上的排除，不是全局硬禁用。决策者若把返回的 weak/全 false 当游戏否决，才会把入口问题扩大成策略问题。

### B. 有 counter 边，仍会被地图优先排序截掉

`query_runtime_facts.py`（196–214 行）按匹配标签是否存在、map fit、hook 数量等排序；当前对手关系和队友组合贡献不参与这个排序。非能力窗口再执行 24/32 条截断。

- **第 15 题 Fang**：对 Mortis 的边就在自己卡上。加 relation 后，在不截断窗口中排 **50**，32 条窗口不返回。
- **第 55 题 Shade**：地图本身 strong，也在不截断窗口中排 **70**，32 条窗口不返回。
- 全量有 **36** 个记录是“无限窗口存在、普通预算后消失”；其中第六手 **7** 个。因此不只是给 weak 改标签就能解决。

能力/floor 窗口有“命中不截断”的保护，不能把以上数字当生产完整策略漏召回率。

### C. 能力窗口本身会预先选择一种解题方法

能力窗口先于关系扩展执行，而且 `passes_windows` 同时要求 capability、archetype、floor 各组通过。`require-floor` 是 AND；低于阈值或缺字段都会失败。有关系也不能绕过这个筛选，除非另行 include。

|题号|若先把需求写成|会漏掉|另一条现有机制|
|---|---|---|---|
|5|反 Fang ⇒ anti_aggro@high|Poco（medium）|team_support 很高；续航/净化阻断预期斩杀链|
|15|保护后排 ⇒ anti_aggro@high|Fang（该轴缺失）|已有对 Mortis 关系；爆发/机动为 high|
|50|Hot Zone ⇒ area_control@high 或 survivability@high|Gray（low / medium_low）|team_support@high，给已选 Bull/Emz 改变进场路线|
|11|Heist ⇒ objective_damage@high|R-T（low）|anti_aggro/burst 很高，Colt/Shade 已负责进攻|

这些是**真实筛选结果 + 窗口误设反例**，不是声称现行模型每次都会发出这些窗口。关键问题是：单一高轴筛选可能先排掉另一种机制的 counter，例如控制、治疗、资源耗尽和队友接近都能解决同一个威胁。

Fang 缺 anti_aggro 量级不等于已知反突能力为零。缺字段与“已证实低于需要”应分开；不能让抽象标签覆盖具体技能/关系事实。

### D. 条件关系的存储方向影响发现路径

`conditional_relations`（102–117 行）只读候选自己卡上的边，不会自动把所有敌方卡上的反向存储关系并进来。

- 第 17 题：Nita 卡写有 Lumi 作为回答；Lumi 自己针对已知敌人的边为空。
- 第 35 题：Carl 卡写有 Shade 的路线/墙压回答；Shade 自己对应边为空。
- 第 50 题：Juju 卡写有 Gray 的传送/接近回答；Gray 自己针对该三人组的边为空。

它们恰好又在 weak 桶外，所以桶 + relation-target 无法找回。读取对手卡/census 可以揭示相关名字，但现有路径没有保证对每个第六手都做这次合并。全量 19 个记录有未在候选侧重复存储的有利敌方关系，另有逆风信息也受同样影响；不能只补有利边而丢失反证。

### E. 第六手仍被全局地图优先规则约束

Skill 的 Ordering logic（245 行起）同时要求：

- 模式职责/地图职责优于孤立对位；
- 有证据的地图适配优于泛化对位舒适度；
- 机制 strong 必须当前地图 hook 命中，且候选失败门未激活（runtime reference 188 行）。

“泛化克制不能无视地图”是合理约束；问题是规则没有清楚区分**泛化克制**与**完整 3v3 已知条件下、队友可以兑现的具体优势**，也没有为第六手规定独立的价值顺序。后者可能是最重要的正向证据，即使当前 map hook 未命中。

`mode-feature filter` 若在团队组合分析之前要求每个候选自带得分/占区能力，会误杀支援、反突和路线补位。模式胜利条件应当检查“加入该英雄后的三人组合”，不能反复要求每个人独立达到地图模板。

### F. 地图失败门只应是待检查的先验

`failure_gate_activation` 是编译器按失败文本关键词和地图草/开阔特征估计的（994–1045 行），没有考虑当前队友传送、加速、治疗、敌方真实控制资源及谁守哪条路。

因此 `low` 不能直接证明实际阵容无法接近，`high` 也不能证明存在无法缓解的致命弱点。First-Response Discipline 的 gate/census 限制本来面向早手；第六手不能机械套用“继续保留 counter 给后手”。本轮没有发现脚本显式在第六手执行早手纪律；这里是文本适用范围及解释风险，不是已经发生的硬拒绝。

## 第六手更合适的决策顺序

推荐的是改顺序和排除责任，而非武断设定一组百分比权重：

1. **先读五个已选英雄，确定这局的胜利路径。** 己方已有何种输出、控场、续航/接近？对手靠哪条资源链或站位赢？现有两人卡在哪一步？
2. **按多种解决机制并列产生候选。** 压制敌人、保护己方核心、给队友接近、打断回复/击杀循环、处理召唤物、补目标输出都可以成为入口。入口之间应取并集，不先用单一能力阈值筛掉另一类解。
3. **比较候选带来的团队变化。** 谁让对手哪条赢法失效？谁让己方现有资源真正用得上？候选是保镖/传送者时，收益由队友完成也是有效目标贡献。
4. **在具体方案下检查地图与执行可行性。** 路线能否到达、技能能否启动、落点能否存活、计分由谁完成？地图在此提供实际约束，不以泛化 weak 作为入场券。
5. **只有具体失败链才允许淘汰。** 写出“因为哪个敌人/位置/资源导致方案无法兑现，现有队友与构筑为何不能缓解”。仅说不适合这图、没高血 body、缺直接边、没样本，不够。
6. **比较剩余方案并保留风险。** 真实不可达、完全没有模式贡献且队友也无法承接，仍应淘汰；不用为题库答案强行豁免。

早手则不同：因为对手未定，广泛适配、保留阵容空间和被反制风险应更重要。这里的提议不是“所有位置降低地图权重”，而是**按已知阵容重新解释地图约束，给第六手的组合/反制价值优先进入比较的权利**。

## 下一轮应怎样验证“能否选出”

本轮证实了工具与规则路径的风险，但没有运行 Jev/GLM 等模型，不报告答案命中率。真正的端到端验证需记录可核查的过程结果：

- 当前状态、index/skill 版本和实际查询参数；
- 候选是否出现，以及从 counter、协同、目标缺口或地图基础方案哪条入口出现；
- 未进入比较时，究竟被可用性、软窗口、方向漏读、预算还是模式判定挡住；
- 进入比较后，给出具体可核查的选择/否决依据与不确定性；
- 最终首选、备选及作者名单一致性单独计分。

**记录 should_consider 与最终是否选中两件事。** 题库答案应先作为维护侧检查“是否有充分比较机会”的目标，不要求每题必须强选作者答案。对同图同位置换队友/换敌人的局面做敏感性测试，也能检验机制是否真的会根据组合改变结果。

应用层另有一个实现细节：当前本地 `server/tools.ts` schema 没有 effort 参数，wrapper 只转发 limit，未指定 limit 时脚本默认 24。即使上游文字说第六手 high=32，也需要调用方显式 limit=32 才落地。能力命中不截断仍有效。应用固定知识 commit，不能把本文本地知识库快照的数字直接宣称为 NAS 实测。

## 56 题路径台账

下表是每个参考候选的阶段记录，非选人推荐。`桶+关系预算` 按 slot 采用 24/32；`无限` 用于定位预算影响；能力轴列只证明至少有相应合法查询可见，不代表模型已自主找到。所有查询未指定答案 include。参考答案只在输出后用于审计比对。

|题|顺位/任务|参考候选|地图桶|桶+关系预算|无限|可见的 high 能力轴|
|---:|---|---|---|---|---|---|

|1|6/pick|Pierce|有|无|有|burst|
|1|6/pick|Byron|有|有|有|effective_range, survivability, team_support|
|1|6/pick|Janet|有|有|有|mobility, survivability, throw_or_wall_bypass, scouting_or_vision|
|2|4/pick|Sprout|有|无|有|effective_range, throw_or_wall_bypass, area_control, team_support|
|2|4/pick|R-T|有|有|有|effective_range, burst, anti_aggro, anti_tank|
|2|4/pick|Pearl|有|无|有|effective_range, burst, anti_aggro|
|3|6/pick|Nita|有|有|有|burst, objective_damage, anti_aggro, area_control|
|4|1/pick|Pierce|有|无|有|burst|
|4|1/pick|Colette|无|无|无|effective_range, burst, objective_damage, anti_aggro, anti_tank|
|4|1/pick|Mortis|无|无|无|mobility, throw_or_wall_bypass|
|5|6/pick|Poco|有|有|有|survivability, team_support|
|6|5/pick|Frank|有|有|有|burst, survivability|
|7|4/pick|Lou|无|无|有|effective_range, anti_aggro, anti_tank, area_control, team_support, crowd_control|
|8|5/pick|Jae-yong|有|有|有|mobility, team_support|
|9|2/pick|Stu|有|有|有|burst, mobility, anti_aggro|
|9|2/pick|Ruffs|有|无|有|team_support|
|10|4/pick|Piper|有|有|有|effective_range, burst, team_support|
|11|6/pick|R-T|无|无|无|effective_range, burst, anti_aggro, anti_tank|
|11|6/pick|Cordelius|有|有|有|burst, mobility, anti_aggro, anti_tank, team_support, crowd_control|
|12|1/pick|Colette|有|无|有|effective_range, burst, objective_damage, anti_aggro, anti_tank|
|12|1/pick|Crow|有|有|有|effective_range, mobility, anti_tank, scouting_or_vision|
|12|1/pick|Finx|有|无|有|effective_range, area_control, team_support|
|13|2/pick|Pierce|有|无|有|burst|
|13|2/pick|Byron|有|有|有|effective_range, survivability, team_support|
|13|2/pick|Belle|有|有|有|effective_range, burst, anti_tank, team_support|
|14|6/pick|Sirius|有|无|有|area_control|
|15|6/pick|Fang|无|无|有|burst, mobility, survivability|
|16|3/pick|Poco|有|有|有|survivability, team_support|
|17|6/pick|Lumi|无|无|无|effective_range, burst, anti_aggro, throw_or_wall_bypass, area_control, crowd_control|
|18|1/pick|Colette|无|无|无|effective_range, burst, objective_damage, anti_aggro, anti_tank|
|18|1/pick|Crow|有|有|有|effective_range, mobility, anti_tank, scouting_or_vision|
|19|2/pick|Frank|有|有|有|burst, survivability|
|19|2/pick|Stu|有|无|有|burst, mobility, anti_aggro|
|20|2/pick|Edgar|有|有|有|burst, objective_damage, survivability, anti_tank|
|20|2/pick|Mortis|有|无|有|mobility, throw_or_wall_bypass|
|20|2/pick|Byron|无|无|无|effective_range, survivability, team_support|
|20|2/pick|Belle|无|无|无|effective_range, burst, anti_tank, team_support|
|21|1/ban|Mortis|有|有|有|mobility, throw_or_wall_bypass|
|21|1/ban|Edgar|无|无|无|burst, objective_damage, survivability, anti_tank|
|21|1/ban|Stu|有|有|有|burst, mobility, anti_aggro|
|21|1/ban|Ruffs|无|无|无|team_support|
|21|1/ban|Leon|有|无|有|burst, mobility, anti_tank|
|21|1/ban|Lumi|有|有|有|effective_range, burst, anti_aggro, throw_or_wall_bypass, area_control, crowd_control|
|22|6/ban|Pierce|有|有|有|burst|
|22|6/ban|Gene|有|有|有|throw_or_wall_bypass, team_support, scouting_or_vision|
|22|6/ban|Najia|有|有|有|throw_or_wall_bypass, area_control|
|23|1/ban|Otis|有|有|有|objective_damage, anti_aggro, anti_tank, crowd_control|
|23|1/ban|Belle|无|无|无|effective_range, burst, anti_tank, team_support|
|23|1/ban|Chuck|无|无|无|burst, objective_damage, mobility, throw_or_wall_bypass|
|24|1/pick|Gene|有|有|有|throw_or_wall_bypass, team_support, scouting_or_vision|
|24|1/pick|Najia|有|无|有|throw_or_wall_bypass, area_control|
|24|1/pick|Pierce|有|无|有|burst|
|25|2/pick|Belle|无|无|无|effective_range, burst, anti_tank, team_support|
|25|2/pick|Byron|无|无|无|effective_range, survivability, team_support|
|26|6/pick|Sprout|有|无|有|effective_range, throw_or_wall_bypass, area_control, team_support|
|26|6/pick|Ziggy|有|无|有|effective_range, throw_or_wall_bypass, area_control|
|26|6/pick|Grom|有|有|有|effective_range, burst, objective_damage, throw_or_wall_bypass, area_control|
|27|1/pick|Crow|有|无|有|effective_range, mobility, anti_tank, scouting_or_vision|
|27|1/pick|Colette|有|无|有|effective_range, burst, objective_damage, anti_aggro, anti_tank|
|27|1/pick|Finx|无|无|无|effective_range, area_control, team_support|
|28|2/pick|Emz|有|无|有|burst, anti_aggro, anti_tank, area_control, crowd_control|
|28|2/pick|Otis|无|无|无|objective_damage, anti_aggro, anti_tank, crowd_control|
|28|2/pick|Chester|有|有|有|burst, anti_aggro, anti_tank|
|28|2/pick|Lou|有|无|有|effective_range, anti_aggro, anti_tank, area_control, team_support, crowd_control|
|28|2/pick|Stu|有|无|有|burst, mobility, anti_aggro|
|28|2/pick|Lumi|有|无|有|effective_range, burst, anti_aggro, throw_or_wall_bypass, area_control, crowd_control|
|29|6/pick|Draco|有|有|有|mobility, survivability, anti_tank|
|30|1/pick|Gene|有|有|有|throw_or_wall_bypass, team_support, scouting_or_vision|
|30|1/pick|Pierce|有|无|有|burst|
|30|1/pick|Najia|有|无|有|throw_or_wall_bypass, area_control|
|31|2/pick|Byron|有|有|有|effective_range, survivability, team_support|
|31|2/pick|Belle|有|有|有|effective_range, burst, anti_tank, team_support|
|31|2/pick|Gus|有|有|有|effective_range, burst, survivability, anti_aggro, team_support|
|32|5/pick|Mortis|无|无|无|mobility, throw_or_wall_bypass|
|33|1/pick|Colt|有|有|有|effective_range, burst, objective_damage, anti_tank|
|33|1/pick|Colette|有|有|有|effective_range, burst, objective_damage, anti_aggro, anti_tank|
|33|1/pick|Crow|有|有|有|effective_range, mobility, anti_tank, scouting_or_vision|
|34|2/pick|Chuck|无|无|无|burst, objective_damage, mobility, throw_or_wall_bypass|
|35|6/pick|Shade|无|无|无|burst, mobility, throw_or_wall_bypass|
|36|3/pick|Crow|有|有|有|effective_range, mobility, anti_tank, scouting_or_vision|
|37|6/pick|Edgar|有|有|有|burst, objective_damage, survivability, anti_tank|
|37|6/pick|Bull|无|无|无|burst, objective_damage, survivability, anti_aggro, anti_tank|
|38|4/pick|Charlie|无|无|无|burst, anti_aggro, team_support, crowd_control|
|39|1/pick|Colette|无|无|无|effective_range, burst, objective_damage, anti_aggro, anti_tank|
|40|5/pick|Chester|有|有|有|burst, anti_aggro, anti_tank|
|40|5/pick|Otis|有|无|有|objective_damage, anti_aggro, anti_tank, crowd_control|
|41|6/pick|Shade|有|无|有|burst, mobility, throw_or_wall_bypass|
|41|6/pick|Bull|有|有|有|burst, objective_damage, survivability, anti_aggro, anti_tank|
|42|1/pick|Gene|有|有|有|throw_or_wall_bypass, team_support, scouting_or_vision|
|42|1/pick|Pierce|有|无|有|burst|
|43|6/pick|Dynamike|有|有|有|effective_range, burst, objective_damage, anti_aggro, anti_tank, throw_or_wall_bypass|
|43|6/pick|Barley|有|有|有|effective_range, objective_damage, throw_or_wall_bypass, area_control|
|44|5/pick|Chester|有|有|有|burst, anti_aggro, anti_tank|
|44|5/pick|Otis|无|无|无|objective_damage, anti_aggro, anti_tank, crowd_control|
|45|2/pick|Chester|有|有|有|burst, anti_aggro, anti_tank|
|45|2/pick|Lumi|无|无|有|effective_range, burst, anti_aggro, throw_or_wall_bypass, area_control, crowd_control|
|46|6/pick|Ziggy|无|无|无|effective_range, throw_or_wall_bypass, area_control|
|47|5/pick|Edgar|无|无|无|burst, objective_damage, survivability, anti_tank|
|47|5/pick|Alli|有|有|有|burst, mobility, scouting_or_vision|
|48|1/pick|Sirius|有|无|有|area_control|
|48|1/pick|Najia|有|无|有|throw_or_wall_bypass, area_control|
|48|1/pick|Edgar|有|有|有|burst, objective_damage, survivability, anti_tank|
|48|1/pick|Colette|有|无|有|effective_range, burst, objective_damage, anti_aggro, anti_tank|
|49|5/pick|Nita|有|有|有|burst, objective_damage, anti_aggro, area_control|
|49|5/pick|Emz|有|有|有|burst, anti_aggro, anti_tank, area_control, crowd_control|
|50|6/pick|Gray|无|无|无|anti_aggro, anti_tank, team_support|
|51|1/pick|Crow|有|有|有|effective_range, mobility, anti_tank, scouting_or_vision|
|52|5/pick|Kenji|无|无|有|burst, mobility, survivability, throw_or_wall_bypass|
|53|6/pick|Nani|有|有|有|effective_range, burst, objective_damage|
|54|1/pick|Finx|有|无|有|effective_range, area_control, team_support|
|54|1/pick|Lou|有|有|有|effective_range, anti_aggro, anti_tank, area_control, team_support, crowd_control|
|54|1/pick|Crow|有|有|有|effective_range, mobility, anti_tank, scouting_or_vision|
|55|6/pick|Shade|有|无|有|burst, mobility, throw_or_wall_bypass|
|56|6/pick|Bull|有|有|有|burst, objective_damage, survivability, anti_aggro, anti_tank|
|56|6/pick|Darryl|有|有|有|burst, objective_damage, mobility, survivability|

## 复现和范围

`probe.py --output-dir <临时目录>` 重跑同一 index 的 784 次查询；`matrix.jsonl` 与 `summary.json` 应一致。此脚本只读 runtime 数据、读取维护侧标签用于结果比对，不修改 BP skill、编译器、实体或题库答案；不能提供给正常 decide 作为答案查询器。
