# BP-index 对题库答案的证据充分性审计

审计日期：2026-09-20。覆盖 **56/56 题、19 张地图、115 个“题目—候选英雄”记录**。第 2 题按 `Sprout + R-T` / `Sprout + Pearl` 两个无序连选组合审查；第 41 题 Bull 保留作者的熟练度条件。合计 **114 个答案方案**，不把 Sprout 单独当成双选命中。

## 结论

按“关系边或机制组合足以构成可辩护的主观答案”，而非唯一最优/严格证明标答的标准：

|题目级结果|数量|含义|
|---|---:|---|
|成立 S|51|该题参考方案均能用 index 中的事实与正常条件组织出合理方案|
|部分成立 P|3|第 41、44、47 题有关键闭环未解释充分；不是判作者错|
|规则张力 T|2|第 4、48 题的部分早手选项与明确选位规则冲突；同题仍有成立选项|

候选记录为 **107 S / 6 P / 2 T**；合并双选后，答案方案为 **106 S / 6 P / 2 T**。这是本轮助手的定性审阅，不是专家复核结果、正确率或置信度。S 也可以带逆风边、操作要求和未知后手，不能读作“无条件成立”。

**更普遍的问题在编译投影/召回：29 个候选记录（24 题）被标为 weak，全部选位资格 false。** 不设返回数量上限的实际桶查询漏掉这 29 个；加入已知敌方关系后，仍漏 25 个（20 题）。这些记录并非都缺机制。Lou 防足球、R-T 守库、Charlie 蜘蛛消耗 Pierce 弹药、Gray 给 Bull/Emz 补进圈路线、Kenji 配 Max 推进，都有可用的目标合同/条件关系。

因此，不能把“Jev 没选参考答案”统一归因于推理弱，也不能把所有差异解释成知识缺边。应区分 **原始事实 → index 保留什么 → 查询实际给出什么 → 模型如何组合**。

## 审计边界与依据

- 主基线为 2026-09-18 编译的 `default-runtime-index.json`（35 图），覆盖全部题目；Jev 实验使用的 2026-09-17 `ranked-season-49.json` 只有 26 图，缺 Pit Stop、Pinhole Punt、Goldarm Gulch，对应第 11、16、25、40、52 题。
- 两快照中的 115 个相关英雄卡在移除 environment_evidence 后相同；共有题目地图上的候选投影也相同。换用完整默认地图池没有偷偷增加这些英雄的战术事实。
- 完整证据保存于 [index-evidence.jsonl](index-evidence.jsonl)，一题一行，包含真实 index 地图、己敌英雄卡、候选卡及双向存储的关系。已分离“与真实敌人的关系”和“与队友的对敌关系”，后者不能当协同。未选的其他参考选项也不能充当敌人。
- [source-only-comparison.jsonl](source-only-comparison.jsonl) 单独保存原实体编译前字段及既有题库分析，仅用于诊断信息在哪丢失；**不参与 index 内充分性判定**。作者标签也只在维护侧使用，没有写进 runtime。
- [reviews.jsonl](reviews.jsonl) 是逐候选结论及证据指针，[provenance.json](provenance.json) 固定 index、题库、脚本、实体与地图哈希；报告不依赖可被清理的 outputs 才能读懂。
- 本次是已知参考答案的维护审阅，存在事后解释风险，并非盲测；判定只使用题面与 index 机制，参考理由用于确定待检验命题。没有直接 A→B 边不自动判缺失：例如“蜘蛛能挡单体弹药”+“Pierce 怕召唤物浪费弹药”已可组成 Charlie 的方案。反过来，有一条克制边也不足以忽略地图、队友、启动资源或失败条件。
- 早手允许合理规划尚未选择的队友；末手不能靠再补第四人修复职责。操作上“等技能/换角”必须与 index 的失败例外相容，不能凭空添加开局 Super、隐藏 ban 或历史构筑。
- 当前 56 题补丁均未知；本轮沿用已校准题面，没有重新听辨 19 个视频或验证当前游戏事实。完整性校验通过不等于来源真值；正式 gold 仍为 0。

## 需要先处理的事项

### 1. 地图匹配没有命中，不应等价于所有选位不可选

编译器 `hook_applies_to_map` 通过示例地图/能力匹配建立 hook；`map_floor_fit` 无匹配就 weak，`slot_eligibility` 随之全部 false。`mode_contract_fit=evidence_only` 不会抬高候选。由此会丢失跨地图可迁移的职责，如：

|题号|选项|index 已有证据|投影|
|---|---|---|---|
|7|Lou|足球冻结掉球；对 8-Bit 阵地的条件回答|weak / 全 false|
|11|R-T|Heist 分体防入库；队友 Colt/Shade 负责进攻|weak / 全 false|
|38|Charlie|Spiders 挡弹/探草；Pierce 怕资源消耗弹药|weak / 全 false|
|46|Ziggy|延迟落雷需要 choke；Layer Cake 明确有层级 choke|weak / 全 false|
|50|Gray|传送队友入区；Bull 身体 + Emz 清场承接|weak / 全 false|
|52|Kenji|足球推进；对 Poco 条件边；Max/Chester 提供接触/跟伤|weak / 全 false|

`weak` 在这里首先表示**没匹配到编译器认可的地图信号**，并非经过完整阵容推理后的实力结论。不宜据此硬否决，也不宜把所有 weak 强行升级为 strong；应保留“地图未判定”和可由职责/机制召回的通道。

实际查询本身已有 include-id、能力/原型窗口等救回途径，所以这里不声称生产流程一定永远看不到这 29 个。此次只验证了两种明确查询策略，排除了 24/32 条数量预算的干扰。敌方关系查询又只查看当前候选自身存储的边，反向存储的边可能需要单独读取对手卡。详见 [retrieval-results.json](retrieval-results.json)。

### 2. 优先复核两个明确选位例外

- **第 4 题 Colette/Mortis 抢蓝星**：缺开局资源、到星时间、拾取和撤退机制。Mortis 还与自己的“不早手”和 Shooting Star 的刺客末选规则有张力。不能用比赛中已充好 Super 的追宝逻辑替代开局；Pierce 仍是合理参考分支。
- **第 48 题 Edgar 一抢 Hard Rock Mine**：草路解释了可玩性，但 index 的 slot_1 例外只允许特定 Brawl Ball 得分/ban 条件，本题没有满足；与此同时地图投影 early_pick=true。需要核作者当期条件和规则范围，不能直接决定删题或改规则迎合作者。其余 Sirius/Najia/Colette 可保留为有条件的构筑方案。

### 3. 三组关键闭环需要补清楚

- **第 41 题 Shade**：Kenji 越墙 Super、Nita 熊/反突和 Poco 续航均已在 index 可见；通用“缺穿墙答案时靠墙惩罚”不能原样套用。需要具体解释如何借 Chester/Najia 改变这组资源交换。条件替代 Bull 有贴 Poco/破门逻辑，但仍要处理 Nita 且保留熟练度条件。
- **第 44 题 Chester/Otis**：可解释反突补位，却未解释作者的“Colette 限制投掷，所以抢剩余反坦”。Colette 和 Otis 的卡反而警告墙控/投掷问题。应回原视频/历史构筑核这个关键前提，再决定是否修题面、说明或知识。
- **第 47 题 Edgar/Alli**：切 Pierce/Lumi 的窗口能解释；最终 Lou/Leon/刺客阵容的持续占区与再入场安排仍薄弱。需要一个明确占区分工，而不是再假设一个不存在的第四位 body。此处是证据不充分判断，不是证明阵容不能赢。

### 4. 有选择依据，不等于覆盖作者所有措辞

第 3 题 Nita、第 7 题 Lou、第 8 题 Jae-yong、第 55 题 Shade 可形成条件方案，但“同时克全部”“对面无法回答”等强措辞没有被无条件证明。仅 14 题在 reference 中有显式理由，其余 42 题的机制解释属于本次推论，不能冒充作者原话。

第 23/34 题 Chuck 需要特别避免时间混用：当前卡写有预算的充能窗口，失败模式提及命中补充；部分合同/关系措辞却写“does not refill”。这在 index 内也存在绝对化表述张力。旧题库分析里的长期/重复压力不能直接等同无限自动循环。当前证据可以支持一次有预算的打库方案，尚不能据此判作者原版本错误。

### 5. Poco 这一题的准确结论

**第 5 题足以支持 Poco 是合理主观答案。** 治疗/净化→延长留圈，以及目标没死→Fang 无法完成预期击杀重置，都可以从双方卡和地图合同组合；没有 Poco→Fang 直接边不是致命缺口。

但 index 缺少完整治疗/伤害时序、资源窗和覆盖范围，无法仅据它证明“始终奶得过 Fang/Amber/Gray”或“必然优于 Pam/Gale”。实体源里的 `changes_capabilities` 包含治疗、净化范围/时长等具体事实，编译成 `build_switches` 时这些内容被裁掉，保留的是名字/enables/失败缓解。建议补可迁移的中性技能原子事实和条件范围，不补“这题选 Poco”的结论句。

现阶段正确的评测问题是：**能否识别 Poco 的有效续航/净化路线并说明边界？** 若仍只判“是否唯一选 Poco”，就会把参考偏好、输入充分性和模型能力混在一起。此报告没有重新评价 Pam/Gale，也没有新跑 Jev。

## 后续修复顺序

1. 先修地图投影与召回语义：区分未匹配和否定；用目标职责/机制窗口补召回，保留逆风边。增加这些确定遗漏的回归样例，但不将题库答案写进编译规则。
2. 恢复被裁掉但可迁移的技能事实：作用对象、状态类型、持续/冷却/充能、路径与墙交互；事实带来源/版本和否定边界。地图/英雄事实到题目选择的组合仍交给运行时。
3. 独立复核第 4、41、44、47、48 题的关键条件和来源；历史专家偏好与当前机制应分轨，不为了自洽直接改成模型喜欢的答案。
4. 用本报告中 S 案例先做无标签输入的机制测评，单独记录候选召回、机制正确性、目标闭环和作者一致性。按视频与重复局面分组留出，避免同局面不同名单泄漏。

## 逐题结果

每题列出全部参考方案相关英雄。下面的证据摘录均来自 index；推论和条件分别写出。完整的反向边及失败条件见对应行的证据包。S 不要求候选优于所有替代；P/T 也不是错误标签。


<a id="case-01"></a>

### 01. Hard Rock Mine · Gem Grab · 成立

`bobby-JxRGZPCa8Us-q1`；pick / slot 6。己方：Griff, Starr Nova；敌方：Amber, Carl, Otis。已知 bans：Gus, Shade, Rico（partial）。

参考方案：Pierce；Byron；Janet。

参考理由：补足远程中路位；两名现有队友承担边路

地图证据：Gem carrier 需要在开放中路收宝石，同时依赖草带和墙体保护撤退；边路线权会决定中路安全。

**Pierce — 成立**

- index 摘录（模式合同）：`lane_pressure；last_ammo_slow_on_carrier_route；shell_cycle_mid_control`。
- 支持链：长线压矿与末发减速补 Griff/Starr Nova 的边路压力；队友争取安全捡壳空间。
- 条件／反证：Amber 可封捡壳路线，Carl 可接近；不能让 Pierce 单独承担裸站矿和探草。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Byron — 成立**

- index 摘录（模式合同）：`carrier 和矿区前排的长线续航；Malaise 反敌方重进场回复保护倒计时拾宝`。
- 支持链：长线治疗维持两名边路的接触时间，并在开放中路消耗 Amber；支援控矿逻辑成立。
- 条件／反证：需明确实际拾宝人和治疗线；Byron 卡明确不把治疗等同自己稳定站矿，Otis/Carl 的接近仍须防。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Janet — 成立**

- index 摘录（模式合同）：`安全 carrier 和倒计时升空；草区 speaker reveal；长线蓄力 poke 与阻断回血`。
- 支持链：Gem carrier 的飞行撤退、探草及侧草压迫对应地图的收宝与倒计时撤退。
- 条件／反证：不能把飞行当消除既有持续伤害；Carl 接近和落地位置要由双边路保护。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 1 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 1 行。来源：[题目视频](https://www.youtube.com/watch?v=JxRGZPCa8Us&t=13s)。

<a id="case-02"></a>

### 02. Belle's Rock · Knockout · 成立

`bobby-JxRGZPCa8Us-q2`；pick / slot 4。己方：Gus；敌方：Piper, Wendy。已知 bans：Shade（partial）。

参考方案：Sprout + R-T；Sprout + Pearl。

参考理由：投掷压制 Piper 与 Wendy；后续搭配 R-T 或 Pearl / Edgar+Rico 有压制与阻止投掷的价值，但对方 Griff 拆墙后 Piper 获益

地图证据：Knockout 重视生存和缩圈前空间；墙体完整时控场强，墙体破后远程强。

**Sprout — 成立**

- index 摘录（模式合同）：`墙后口袋投掷压缩空间；Hedge 封单一 choke 制造第一减员窗口；领先后的撤退路线封锁`。
- 支持链：棋盘墙袋让投掷压缩 Piper/Wendy 的直线位置；Hedge 将空间优势转为首杀窗口。
- 条件／反证：依赖完整墙袋，敌方还有第六手破墙或突进；必须与 R-T 或 Pearl 一起评价。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**R-T — 成立**

- index 摘录（模式合同）：`round_space_control；first_pick_focus_fire；split_form_close_route_guard`。
- 支持链：分体近路守卫加标记跟伤，为 Sprout 提供入口保护；敌方 Piper 卡也记有 R-T 回答边。
- 条件／反证：保护腿位，防第六手投掷/穿透；不能把敌方 Griff 这个事后选项当作当前已知敌人。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Pearl — 成立**

- index 摘录（模式合同）：`回合计时内蓄 Heat 后威胁 first pick；Heat Shield 持线保护血量优势；Super 近身反突进和开墙`。
- 支持链：Gus 保护蓄 Heat，Pearl 的近身反突 Super 和高热火力补 Sprout 的入口防守/击杀。
- 条件／反证：投掷和超长线会迫使 Pearl 消耗 Heat；开墙需避免拆掉 Sprout 唯一口袋。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

双选判定：**Sprout + R-T：S；Sprout + Pearl：S**。Sprout 提供墙控，两种第五手分别提供分体入口保护或高热近身反打；单独推荐 Sprout 不算完成本题。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 2 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 2 行。来源：[题目视频](https://www.youtube.com/watch?v=JxRGZPCa8Us&t=39s)。

<a id="case-03"></a>

### 03. Double Swoosh · Gem Grab · 成立

`bobby-BzIBRZCMiMM-q1`；pick / slot 6。己方：Jessie, Shade；敌方：Gray, Tara, Bull。已知 bans：未提供（not_provided）。

参考方案：Nita。

参考理由：作者认为 Nita 同时克制对面三人

地图证据：Gem Grab 的目标访问依赖中路站位与倒计时撤退；侧路击杀和探草能改变宝石持有者的退路。

**Nita — 成立**

- index 摘录（模式合同）：`center_or_side_pierce_control；Bruce_carrier_pressure；bush_scouting`。
- 支持链：Bull 的窄路入场可被 Bruce/Bear Paws 惩罚；Tara 卡有被 Nita 资源/范围压制的条件边，草路让熊和穿透有目标。
- 条件／反证：Gray 传送可绕开熊；Tara 拉人、Bull 爆发和无熊期都能反转。只能支持条件反制，不能证明无条件克制三人。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 3 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 3 行。来源：[题目视频](https://www.youtube.com/watch?v=BzIBRZCMiMM&t=6s)。

<a id="case-04"></a>

### 04. Shooting Star · Bounty · 存在未解规则张力

`bobby-BzIBRZCMiMM-q2`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：未提供（not_provided）。

参考方案：Pierce；Colette；Mortis。

参考理由：Colette/Mortis 的理由为抢蓝星，Pierce 为另一可接受首选

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Pierce — 成立**

- index 摘录（模式合同）：`long_range_star_pick_pressure；last_ammo_slow_on_peeking_target；Super_homing_star_lead_hold`。
- 支持链：开放长线提供低承诺拿星、慢速控制和 Super 收束路线，能作为后续补保护的首选核心。
- 条件／反证：对稳定狙击镜像存在资源劣势，需保护空弹/捡壳；不是因为 map fit strong 就无条件一抢。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Colette — 部分成立／缺关键闭环**

- index 摘录（模式合同）：`对高血量后排稳定削血；Push It 把目标推到队友射线；Na-ah! 拉近创造收割窗口`。
- 支持链：卡里有 Super 位移和支援消耗方向，但缺从开局状态到先拿 Blue Star 再保星的可执行机制。
- 条件／反证：当前失败条件明确要求预算 Super 充能；题面未给开局 Super/特殊资源，不能把抢宝石 Super 类比成可立即抢蓝星。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Mortis — 存在未解规则张力**

- index 摘录（模式合同）：`最后手惩罚孤立低血后排和投掷；长 dash + Super 穿墙收割墙后保星位`。
- 支持链：dash 提供接近可能，但作者的蓝星首选理由未形成 index 内的抢星—撤退—后续价值闭环。
- 条件／反证：Mortis slot_1 写“不早手”；Shooting Star 规则写刺客反狙必须等最后手。需要补蓝星战术适用条件或核历史版本，不能静默忽略规则。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 4 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 4 行。来源：[题目视频](https://www.youtube.com/watch?v=BzIBRZCMiMM&t=22s)。

<a id="case-05"></a>

### 05. Ring of Fire · Hot Zone · 成立

`bobby-BzIBRZCMiMM-q3`；pick / slot 6。己方：Lou, Leon；敌方：Fang, Amber, Gray。已知 bans：未提供（not_provided）。

参考方案：Poco。

参考理由：持续治疗对抗对方伤害；保护类妙具处理控制/火焰

地图证据：目标是持续站圈并控制草丛视野；缺探草会让任何圈外压制都不稳定。

**Poco — 成立**

- index 摘录（模式合同）：`zone_sustain；cleanse_against_control；wide_attack_bush_check`。
- 支持链：单圈需要续航/探草；Poco 的治疗重置、状态净化与 Lou 的控区和 Leon 的压力可共同延长留圈时间。Fang 卡的击杀链依赖目标死亡，治疗阻断斩杀线是合理组合推论。
- 条件／反证：只有定性支持：净化不等于消除 Amber 全部直伤，也不能无条件挡 Gray 位移；聚集会给 Fang 链跳，必须保持治疗覆盖而不送连跳。尚不能证明优于 Pam/Gale。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 5 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 5 行。来源：[题目视频](https://www.youtube.com/watch?v=BzIBRZCMiMM&t=36s)。

<a id="case-06"></a>

### 06. Open Business · Hot Zone · 成立

`bobby-ai3KY3I5xRY-q1`；pick / slot 5。己方：Emz, Gray；敌方：Draco, Max。已知 bans：未提供（not_provided）。

参考方案：Frank。

参考理由：己方围绕占区时间；用更高血量前排应对 Draco / Emz 可对抗敌方末手的反坦克选择

地图证据：目标是既能站圈，又能处理圈旁墙体后的控制点；只在外围消耗不够。

**Frank — 成立**

- index 摘录（模式合同）：`zone_body；zone_clear_stun；入口封锁`。
- 支持链：Gray 送入目标、Emz 跟范围伤害，Frank 的 zone body/眩晕把支援转成计分；有 Frank 对 Draco 的近身交换边。
- 条件／反证：Max 可以躲前摇，敌方仍留第六手反坦；不是仅靠高血量就能进圈。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 6 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 6 行。来源：[题目视频](https://www.youtube.com/watch?v=ai3KY3I5xRY&t=2s)。

<a id="case-07"></a>

### 07. Pinball Dreams · Brawl Ball · 成立

`bobby-ai3KY3I5xRY-q2`；pick / slot 4。己方：Barley；敌方：8-Bit, Colette。已知 bans：未提供（not_provided）。

参考方案：Lou。

参考理由：作者认为 Lou 同时应对这两个对手，并有足球模式价值

地图证据：目标是利用墙体或开墙制造进球窗口；地图不是简单越开越好。

**Lou — 成立**

- index 摘录（模式合同）：`冻结持球者掉球；Super 封球落点/门前`。
- 支持链：足球合同明确冻结持球者掉球和冰面封门；Lou 对 8-Bit 的阵地消耗边与 Barley 的铺地形成防守闭环。
- 条件／反证：对 Colette 不是明示硬克；仍要由第五手补进球/破门。地图 weak 与这些机制并不相符，属于投影漏召回风险。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 7 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 7 行。来源：[题目视频](https://www.youtube.com/watch?v=ai3KY3I5xRY&t=24s)。

<a id="case-08"></a>

### 08. Hideout · Bounty · 成立

`bobby-ai3KY3I5xRY-q3`；pick / slot 5。己方：Max, Pierce；敌方：Charlie, Penny。已知 bans：未提供（not_provided）。

参考方案：Jae-yong。

参考理由：作者认为与 Max 协同限制投掷/狙击，Max 与 Pierce 应对高血量

地图证据：Bounty 要在拿星后保命；中路控墙和边路远程同时提供得分路线。

**Jae-yong — 成立**

- index 摘录（模式合同）：`开局加速争 Blue Star 和长线站位；用治疗/速度维持星差，Weekend Warrior 收残血`。
- 支持链：速度/治疗维持 Pierce 的长线换血，Max 提供同步接触；对 Charlie 有支援型回答边，Bounty 合同含保星和速度站位。
- 条件／反证：Penny 溅射惩罚抱团，Charlie 茧不能简单用治疗解除；“限制一切投掷/狙击”超出证据。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 8 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 8 行。来源：[题目视频](https://www.youtube.com/watch?v=ai3KY3I5xRY&t=41s)。

<a id="case-09"></a>

### 09. Hard Rock Mine · Gem Grab · 成立

`bobby-aItvGu49FEo-q1`；pick / slot 2。己方：尚未选择；敌方：Rico。已知 bans：未提供（not_provided）。

参考方案：Stu；Ruffs。

参考理由：拆墙削弱 Rico 的地形优势

地图证据：Gem carrier 需要在开放中路收宝石，同时依赖草带和墙体保护撤退；边路线权会决定中路安全。

**Stu — 成立**

- index 摘录（模式合同）：`mobile_side_lane_pressure；speed_anchor_for_mid_return；chase_exposed_carrier`。
- 支持链：Rico 卡记录 Stu 可用破墙/机动否定弹墙角；Stu 边路机动把开出的空间转成矿区安全。
- 条件／反证：需要 Breakthrough 分支且保留撤退墙；后续补 carrier/身体，不能开墙后没有远程接管。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Ruffs — 成立**

- index 摘录（模式合同）：`buff_gem_carrier_or_mid_body_with_supply_drop；bounce_wall_lane_pressure_on_corridor_maps；Take_Cover_sandbag_to_tax_non_piercing_mine_defenders`。
- 支持链：Rico 卡明确记录 Air Superiority 选择性开墙、同廊对线和补给强化；直接覆盖作者拆墙理由。
- 条件／反证：只拆 Rico 核心反弹墙，队友需拾取补给并接管；不把 Ruffs 所有墙体一起拆掉。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 9 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 9 行。来源：[题目视频](https://www.youtube.com/watch?v=aItvGu49FEo&t=3s)。

<a id="case-10"></a>

### 10. Shooting Star · Bounty · 成立

`bobby-aItvGu49FEo-q2`；pick / slot 4。己方：Nori；敌方：Belle, Byron。已知 bans：未提供（not_provided）。

参考方案：Piper。

参考理由：补射程以对抗敌方两名狙击

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Piper — 成立**

- index 摘录（模式合同）：`max_range_star_pick_on_fragile_long_range；long_lane_star_lead_protection_with_super_escape；Homemade_Recipe_bush_angle_burst`。
- 支持链：开放图满距离爆发补 Nori 的接触/控制，Piper 对 Belle 和 Byron 都有狙击镜像条件边。
- 条件／反证：Byron 治疗和第五/六手可改变交换；Piper 需侧路保护、满距角度和逃生资源。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 10 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 10 行。来源：[题目视频](https://www.youtube.com/watch?v=aItvGu49FEo&t=19s)。

<a id="case-11"></a>

### 11. Pit Stop · Heist · 成立

`bobby-aItvGu49FEo-q3`；pick / slot 6。己方：Colt, Shade；敌方：Bull, Rico, Kit。已知 bans：未提供（not_provided）。

参考方案：R-T；Cordelius。

参考理由：补充防守能力

作者偏好：R-T；本次不把该排序当作已证明事实。

地图证据：目标访问高度依赖能否越过、绕过或破坏金库屏障；普通射手需要开线后才有稳定价值。

**R-T — 成立**

- index 摘录（模式合同）：`mark_amplification_on_safe_defender；split_anti_entry_pulse_on_safe_lane`。
- 支持链：Heist 合同明确分体防入库而非主打库；Colt/Shade 已承担开线与入库，R-T 留守可处理 Bull/Kit 接触。
- 条件／反证：要保腿位、避免 Rico 免费弹墙处理；弱地图投影不应抹掉防守职责，R-T 优先于 Cordelius 的排序没有充分证据。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Cordelius — 成立**

- index 摘录（模式合同）：`defender_isolation_for_safe_entry；replanting_or_shadow_route_to_safe；anti_aggro_defense_against_short_range_safe_threat`。
- 支持链：对 Bull 的领域/禁技边、Kit 卡的领域反制边支持拆开近战载体；Colt/Shade 继续给金库压力。
- 条件／反证：开领域后自家金库剩余 2v2 必须能守，不能把隔离当作稳定打库 DPS。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

地图覆盖限制：Jev 所用 S49 index 没有本图，本条依默认 35 图快照审查。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 11 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 11 行。来源：[题目视频](https://www.youtube.com/watch?v=aItvGu49FEo&t=40s)。

<a id="case-12"></a>

### 12. Ring of Fire · Hot Zone · 成立

`bobby-sGgIg02ctoU-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：未提供（not_provided）。

参考方案：Colette；Crow；Finx。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：目标是持续站圈并控制草丛视野；缺探草会让任何圈外压制都不稳定。

**Colette — 成立**

- index 摘录（模式合同）：`反站圈身体；Push It 赶人出圈`。
- 支持链：Push It 清出站区身体、削高血目标，为后续占区者创造窗口；是可延展首选职责。
- 条件／反证：后续需站区者、反投掷和清召唤物；当前没有敌人，不声称已满足某个克制关系。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Crow — 成立**

- index 摘录（模式合同）：`anti_heal_zone_edge；slow_first_entry；bush_reveal_around_zone`。
- 支持链：Ring of Fire 草控、压回复和减速入口对应 Crow 的两条地图 hook。
- 条件／反证：后续补真正占区者和清点；ban 未知意味着无法声称已排除所有狙击/突进回应。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Finx — 成立**

- index 摘录（模式合同）：`Time Warp 站圈支援；reload tax 和 projectile slow`。
- 支持链：L 墙支援口袋和队友弹道增益可延长控圈，作为围绕 projectile 队友展开的首选计划成立。
- 条件／反证：Finx 不能独自占圈；后续明确补身体/输出，其早手限制要求组队计划而非看到 strong 就锁定。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 12 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 12 行。来源：[题目视频](https://www.youtube.com/watch?v=sGgIg02ctoU&t=2s)。

<a id="case-13"></a>

### 13. Shooting Star · Bounty · 成立

`bobby-sGgIg02ctoU-q2`；pick / slot 2。己方：尚未选择；敌方：Colette。已知 bans：未提供（not_provided）。

参考方案：Pierce；Byron；Belle。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Pierce — 成立**

- index 摘录（模式合同）：`long_range_star_pick_pressure；last_ammo_slow_on_peeking_target；Super_homing_star_lead_hold`。
- 支持链：敌方 Colette 首选时可用长线慢速/壳循环维持拿星压力，下一手保留补保护空间。
- 条件／反证：Colette 位移和后续刺客仍需回答；没有证据表明它必胜 Colette。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Byron — 成立**

- index 摘录（模式合同）：`长线治疗支援维持脆皮后排站线和星压；低承诺远程 chip 和 Malaise 削弱敌方回复；领先后的血量 swing 保星`。
- 支持链：长线支援和治疗换血能构筑 Bounty 保星队伍，不必与 Colette 在近身反坦轴竞争。
- 条件／反证：第二/三手需补可吃治疗的输出，不能单凭治疗当首杀工具。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Belle — 成立**

- index 摘录（模式合同）：`low_commitment_star_pressure；force_enemy_spacing；focus_mark_for_pick`。
- 支持链：开放射线的低承诺消耗、标记跟伤与陷阱撤退能建立拿星计划。
- 条件／反证：保持距离并补反突/跟伤；不是以缺少反向边证明克制 Colette。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 13 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 13 行。来源：[题目视频](https://www.youtube.com/watch?v=sGgIg02ctoU&t=11s)。

<a id="case-14"></a>

### 14. Hard Rock Mine · Gem Grab · 成立

`bobby-sGgIg02ctoU-q3`；pick / slot 6。己方：Chester, Gus；敌方：Crow, Ruffs, Sandy。已知 bans：未提供（not_provided）。

参考方案：Sirius。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Gem carrier 需要在开放中路收宝石，同时依赖草带和墙体保护撤退；边路线权会决定中路安全。

**Sirius — 成立**

- index 摘录（模式合同）：`carrier_bodyguard；mine_entry_shadow_tax；side_bush_shadow_pressure`。
- 支持链：影子税与护送路线对应矿区；Gus 可承担保护、Chester 惩罚近身，使影子压力有队友承接。
- 条件／反证：Sandy 范围清理及敌方扫草会削弱收益，影子应分散且不能捡宝石；必须保留真实持宝人。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 14 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 14 行。来源：[题目视频](https://www.youtube.com/watch?v=sGgIg02ctoU&t=21s)。

<a id="case-15"></a>

### 15. Shooting Star · Bounty · 成立

`bobby-c7C6B5cjD9o-q1`；pick / slot 6。己方：Belle, Gray；敌方：Pierce, Mortis, Leon。已知 bans：未提供（not_provided）。

参考方案：Fang。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Fang — 成立**

- index 摘录（模式合同）：`low_hp_chain_finisher；backline_threat`。
- 支持链：已有 Belle/Gray 的长线，Fang 可补近身反刺客；明确对 Mortis 的 Roundhouse/Corn-Fu 回答边支持保护己方后排，亦能威胁 Pierce。
- 条件／反证：要安全攒 Super 并追踪 Leon/Fang 落点，不能将鞋子当主狙击或为追 Pierce 放弃保星。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 15 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 15 行。来源：[题目视频](https://www.youtube.com/watch?v=c7C6B5cjD9o&t=9s)。

<a id="case-16"></a>

### 16. Pinhole Punt · Brawl Ball · 成立

`bobby-c7C6B5cjD9o-q2`；pick / slot 3。己方：Nita；敌方：Crow。已知 bans：Otis, Colette（partial）。

参考方案：Poco。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：先扫清中央草环并建立球权，再通过前排/控场穿过墙封草簇，把线权转成窄门射门或选择性破门窗口。

**Poco — 成立**

- index 摘录（模式合同）：`tank_or_scorer_heal_support；anti_status_push_reset；wide_bush_check_before_entry`。
- 支持链：Poco 对 Crow 的状态净化边直接存在；Nita 提供近区接触和熊资源，治疗/净化可维持足球推进。
- 条件／反证：Crow 在净化用尽后仍能反治疗；尚需 scorer/射门窗口，不把被 ban 的 Colette/Otis 当已选队友。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

地图覆盖限制：Jev 所用 S49 index 没有本图，本条依默认 35 图快照审查。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 16 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 16 行。来源：[题目视频](https://www.youtube.com/watch?v=c7C6B5cjD9o&t=21s)。

<a id="case-17"></a>

### 17. Undermine · Gem Grab · 成立

`bobby-c7C6B5cjD9o-q3`；pick / slot 6。己方：Chester, Otis；敌方：Stu, Amber, Nita。已知 bans：未提供（not_provided）。

参考方案：Lumi。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：中路负责稳定拿宝石，边路负责阻止敌方从草丛推进；倒计时撤退通常依赖己方半场墙后草丛。

**Lumi — 成立**

- index 摘录（模式合同）：`矿区穿墙召回压力；carrier 退线 slow/root`。
- 支持链：Gem 合同的召回穿墙、退线 slow/root 能从草墙边改变矿区角度；Nita 卡含 Lumi 的清熊/墙压回答边。
- 条件／反证：Chester/Otis 与 Lumi 要明确中路拾宝和侧路分工；Amber 烧草、Stu 机动会减值，root 不阻止攻击。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 17 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 17 行。来源：[题目视频](https://www.youtube.com/watch?v=c7C6B5cjD9o&t=35s)。

<a id="case-18"></a>

### 18. Hot Potato · Heist · 成立

`bobby-ZdWs3kiDrJ8-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Damian（partial）。

参考方案：Colette；Crow。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Heist race 不只看 DPS，还看谁能从草丛或侧路安全转入金库输出。

**Colette — 成立**

- index 摘录（模式合同）：`special target safe burst；Super 往返打库；Push It 推开防守者或 Mass Tax 扛伤`。
- 支持链：Heist 特殊目标伤害与往返 Super 打库给出直接目标转化，Hot Potato 边路赢线后可获得直线访问。
- 条件／反证：必须开出 Super 路径并安全充能；投影缺 hook 不等于没有 Heist 工作。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Crow — 成立**

- index 摘录（模式合同）：`lane_attrition_and_anti_heal；defender_slow_for_safe_dps_teammate；anti_short_range_safe_entry`。
- 支持链：草带探测、压回复和守入口帮助后续主 DPS 获得金库访问，可作为控线首选。
- 条件／反证：现有 index 只支持辅助控制/防守，不能将历史选项解释为当前唯一主打库或无限 Hyper 输出。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 18 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 18 行。来源：[题目视频](https://www.youtube.com/watch?v=ZdWs3kiDrJ8&t=6s)。

<a id="case-19"></a>

### 19. Dueling Beetles · Hot Zone · 成立

`bobby-ZdWs3kiDrJ8-q2`；pick / slot 2。己方：尚未选择；敌方：Lou。已知 bans：Colette, Crow, Damian（partial）。

参考方案：Frank；Stu。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Hot Zone 的目标是持续站圈；这张图惩罚无法进圈或无法把敌人赶出圈的阵容。

**Frank — 成立**

- index 摘录（模式合同）：`zone_body；zone_clear_stun；入口封锁`。
- 支持链：明确反向边 Lou→Frank 同时记有 Active Noise Canceling 例外；免控进区加高血身体、队友跟伤能构成条件方案。
- 条件／反证：Colette/Crow 被 ban 只减少部分反制；不能说 Frank 无条件克 Lou，必须追踪免控与 Lou 冰面资源。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Stu — 成立**

- index 摘录（模式合同）：`zone_touch_and_escape；speed_zone_return；poke_to_force_enemies_off_zone`。
- 支持链：Lou 卡明确机动横移能妨碍连续 Frost 命中；Speed Zone 回区与机动争点符合地图任务。
- 条件／反证：窄口被迫踩冰仍会失败，后续队友补占区/清点；只躲弹不等于计分。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 19 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 19 行。来源：[题目视频](https://www.youtube.com/watch?v=ZdWs3kiDrJ8&t=14s)。

<a id="case-20"></a>

### 20. Belle's Rock · Knockout · 成立

`bobby-ZdWs3kiDrJ8-q3`；pick / slot 2。己方：尚未选择；敌方：Najia。已知 bans：Damian（partial）。

参考方案：Edgar；Mortis；Byron；Belle。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Knockout 重视生存和缩圈前空间；墙体完整时控场强，墙体破后远程强。

**Edgar — 成立**

- index 摘录（模式合同）：`最后手刺杀无保护投掷/远程；利用墙草制造一次击杀确认`。
- 支持链：Najia 卡明示 Edgar 可惩罚其低爆发；Belle's Rock 墙袋提供跳入路线，作为针对已暴露后排的早期计划成立。
- 条件／反证：仅第二手，必须留队友回答后续反突；Super 启动、落地、逃生需成立，不能按无保镖的最终阵容计算。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Mortis — 成立**

- index 摘录（模式合同）：`最后手切掉孤立投掷或低血后排；Super 穿墙收割墙后回末站位；Combo Spinner 补无 ammo 时的收割`。
- 支持链：越障/长 dash 与墙后低爆发目标相接，Najia 对刺客/高速路线的失败条件支持低成本接触的方向。
- 条件／反证：早手 KO 风险被卡片明确提示；必须规划后续反控制/压血。支持有风险的方案，不支持“安全必选”。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Byron — 成立**

- index 摘录（模式合同）：`长线治疗支援保血量领先和回合节奏；Malaise 反治疗拖慢敌方回复循环`。
- 支持链：地图侧线和开墙后长线可供治疗消耗；Najia 卡也把 sustain 记为毒伤无法转化的机制，后续配可靠输出即可构筑回合优势。
- 条件／反证：完整墙袋可能堵治疗和输出，需侧线/开墙计划及保镖；当下不能保证单独压过 Najia。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Belle — 成立**

- index 摘录（模式合同）：`opening_poke；marked_target_finish；trap_final_ring_entry`。
- 支持链：KO 的低承诺消耗、标记和末圈陷阱与侧线/未来开墙结构相容，可保留远程配队路线。
- 条件／反证：没有 Belle 直接克 Najia 的边；不能站在封闭墙袋正面期待射线穿墙，后续补开角/反突。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 20 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 20 行。来源：[题目视频](https://www.youtube.com/watch?v=ZdWs3kiDrJ8&t=27s)。

<a id="case-21"></a>

### 21. Ring of Fire · Hot Zone · 成立

`bobby-8CGXicuVjbs-q1`；ban / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：未提供（not_provided）。

参考方案：Mortis；Edgar；Stu；Ruffs；Leon；Lumi。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：目标是持续站圈并控制草丛视野；缺探草会让任何圈外压制都不稳定。

**Mortis — 成立**

- index 摘录（模式合同）：`切掉圈外投掷/低血支援，帮助队友进圈`。
- 支持链：作为禁用可移除切圈外支援/投掷的能力，保护己方准备围绕墙袋控圈的方案。
- 条件／反证：这是可成立的假设首选计划，不冒充题面已选英雄；不是要求 Mortis 自己长期站圈。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Edgar — 成立**

- index 摘录（模式合同）：`跳入站圈抱团打出一次清场窗口；贴脸处理圈旁投掷/控制`。
- 支持链：禁掉跳入清圈/贴脸控制位，能降低己方区域核心被越过正面防线的风险。
- 条件／反证：需要明确自己准备抢的区域核心；地图弱投影不能推出无禁用价值。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Stu — 成立**

- index 摘录（模式合同）：`zone_touch_and_escape；speed_zone_return；poke_to_force_enemies_off_zone`。
- 支持链：机动换角与反复争圈能拆固定射线/冰面计划，ban 可以保护己方定点控区。
- 条件／反证：应说明准备保护哪个入口计划；这不证明 Stu 是普遍最高 ban。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Ruffs — 成立**

- index 摘录（模式合同）：`buff_zone_body_or_zoner_with_supply_drop；Air_Superiority_wallbreak_on_zone_adjacent_pocket_or_thrower_cover；Take_Cover_sandbag_to_tax_zone_entry_projectiles`。
- 支持链：Air Superiority 处理圈旁墙袋、补给强化敌方占区者，会改变己方围绕 L 墙的优势，作为预防性 ban 可成立。
- 条件／反证：仅在己方依赖该地形/站区资源差时有意义；Ruffs 本人不是占区身体。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Leon — 成立**

- index 摘录（模式合同）：`Lollipop Drop 保护圈边站位；草丛伏击和侧路切入`。
- 支持链：草/隐蔽与 Lollipop 改变进圈信息差，可威胁己方圈边后排；移除此路线有明确地图收益。
- 条件／反证：如果己方已有充分探草，ban 边际价值下降；不强行替作者补一个唯一预选。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Lumi — 成立**

- index 摘录（模式合同）：`单区口 Grim and Frostbitten 冰面与 Super root 延迟进区；区边召回穿墙跟伤`。
- 支持链：区口 slow/root 与墙边召回能延迟己方回区、压制圈边站位，ban 可保护稳定重进场。
- 条件／反证：冰面只有局部短窗口，不能把它写成永久封整圈；需要配合己方方案衡量。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 21 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 21 行。来源：[题目视频](https://www.youtube.com/watch?v=8CGXicuVjbs&t=8s)。

<a id="case-22"></a>

### 22. Shooting Star · Bounty · 成立

`bobby-8CGXicuVjbs-q2`；ban / slot 6。己方：尚未选择；敌方：尚未选择。已知 bans：未提供（not_provided）。

参考方案：Pierce；Gene；Najia。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Pierce — 成立**

- index 摘录（模式合同）：`long_range_star_pick_pressure；last_ammo_slow_on_peeking_target；Super_homing_star_lead_hold`。
- 支持链：禁止对手首选长线压制/减速与资源循环，减少末选方承受的开局火力压力。
- 条件／反证：稳定狙击仍能对付 Pierce；合理 ban 不等于无反制或环境第一。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Gene — 成立**

- index 摘录（模式合同）：`分裂弹长线 poke 建立星差；Magic Hand 抓失位或高价值长手；Vision Gear 探草和 Magic Puffs 治疗维持对线`。
- 支持链：移除长线 poke、治疗/视野支援和抓高价值目标能力，能保护后续拿星阵容。
- 条件／反证：需要抓人跟伤且怕更长狙；ban 判断不能套其 slot_6 的选人规则。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Najia — 成立**

- index 摘录（模式合同）：`wall_arc_poison_pressure_from_safe_angle；retreat_route_poison_to_punish_star_holders_or_chasers；grouped_target_zone_denial_with_puddles_and_snakes`。
- 支持链：少量墙袋允许越墙投毒限制狙击安全位；ban 可排除这条条件反狙/退线压力路线。
- 条件／反证：Shooting Star 开墙后毒弹易空且低爆发；只支持墙体保留分支，不支持纯开放图普遍强势。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 22 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 22 行。来源：[题目视频](https://www.youtube.com/watch?v=8CGXicuVjbs&t=21s)。

<a id="case-23"></a>

### 23. Safe Zone · Heist · 成立

`bobby-8CGXicuVjbs-q3`；ban / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：未提供（not_provided）。

参考方案：Otis；Belle；Chuck。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Heist 目标访问有两条主线：可过水/越墙进入敌方半场，或远程/抛物线不进半场也能打库。

**Otis — 成立**

- index 摘录（模式合同）：`defend_enemy_entry_route；mute_aggro_near_safe；conditional_safe_dps_with_Ink_Refills`。
- 支持链：沉默近身入库路线会关闭己方可能的进场打库计划，因此 ban 有针对性防守价值。
- 条件／反证：若己方拟走远程打库，该禁用收益下降；题目未指定唯一预选。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Belle — 成立**

- index 摘录（模式合同）：`long_range_lane_pressure；anti_tank_or_aggro_mark_if_enemy_entries；choke_trap_route_delay`。
- 支持链：长线标记、入口陷阱和拥挤多目标换血会妨碍入库与输出搭档，禁用可保护己方进攻路线。
- 条件／反证：Belle 非主打库，且投影 weak；合理的克制型 ban 不依赖把她判断成地图全能强势。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Chuck — 成立**

- index 摘录（模式合同）：`charge_bounded_multi_dash_safe_damage；safe_entry_and_retreat_inside_one_pool；defender_route_disruption`。
- 支持链：布站提供有预算的打库突破和强制回防任务，移除此特殊访问路线可简化防守。
- 条件／反证：当前卡是有限充能/命中补充的版本；旧分析的“长期路线压力”不能自动解释成无限自动循环。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 23 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 23 行。来源：[题目视频](https://www.youtube.com/watch?v=8CGXicuVjbs&t=31s)。

<a id="case-24"></a>

### 24. Belle's Rock · Knockout · 成立

`bobby-qajAIs6gTLM-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Damian（partial）。

参考方案：Gene；Najia；Pierce。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Knockout 重视生存和缩圈前空间；墙体完整时控场强，墙体破后远程强。

**Gene — 成立**

- index 摘录（模式合同）：`Magic Hand 抓孤立目标制造 first pick；分裂弹长线 poke 保护回合；VisionGear 和 Lamp Blowout 探草/防突进`。
- 支持链：墙后 Magic Hand 抓出安全口袋加探测，为 KO 首杀建立后续补爆发的方案。
- 条件／反证：需选能接伤害的队友并防召唤物挡手；拉中不自动完成首杀。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Najia — 成立**

- index 摘录（模式合同）：`wall_arc_poison_control_on_Belle's_Rock_or_New_Horizons；locked_space_denial_with_puddles_and_snakes_before_gas_close；retreat_route_poison_to_protect_a_lead`。
- 支持链：地图明确存在棋盘墙袋和缩圈前固定入口，越墙毒区可安全压缩空间。
- 条件／反证：后续必须补反突与终结；Damian 被 ban 不代表所有刺客已被限制。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Pierce — 成立**

- index 摘录（模式合同）：`long_lane_first_pick_pressure；Super_finish_window_after_shell_setup；last_ammo_slow_to_force_collapse`。
- 支持链：利用可用长线压血和 Super 收束，为墙图中的路线控制提供一种可延展远程核心。
- 条件／反证：对墙控/召唤物和刺客需补答案；不是覆盖全部墙袋的无条件首选。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 24 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 24 行。来源：[题目视频](https://www.youtube.com/watch?v=qajAIs6gTLM&t=3s)。

<a id="case-25"></a>

### 25. Goldarm Gulch · Knockout · 成立

`bobby-qajAIs6gTLM-q2`；pick / slot 2。己方：尚未选择；敌方：Pierce。已知 bans：Damian, Gene, Najia（partial）。

参考方案：Belle；Byron。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：用双侧路线与中央墙压制造成第一杀，领先后保持交叉角度；毒圈收缩前必须有离开出生墙袋和处理突进的方案。

**Belle — 成立**

- index 摘录（模式合同）：`opening_poke；marked_target_finish；trap_final_ring_entry`。
- 支持链：Goldarm Gulch 明确有双侧长射线；Belle 的 poke/标记给队友创造第一杀，与被禁掉的其他远程选项相容。
- 条件／反证：需要保护侧草和缩圈撤退；纯地图字符串未匹配 hook 不应阻止此路线被考虑。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Byron — 成立**

- index 摘录（模式合同）：`长线治疗支援保血量领先和回合节奏；Malaise 反治疗拖慢敌方回复循环`。
- 支持链：双侧长线可让 Byron 治疗核心并维持 KO 血量领先，避开与 Pierce 壳循环持续硬换。
- 条件／反证：后续必须有吃治疗的输出/反突，不能隔中央墙治疗；不是证明单挑克 Pierce。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

地图覆盖限制：Jev 所用 S49 index 没有本图，本条依默认 35 图快照审查。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 25 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 25 行。来源：[题目视频](https://www.youtube.com/watch?v=qajAIs6gTLM&t=11s)。

<a id="case-26"></a>

### 26. Belle's Rock · Knockout · 成立

`bobby-qajAIs6gTLM-q3`；pick / slot 6。己方：Spike, R-T；敌方：Gene, Rico, Pierce。已知 bans：Damian（partial）。

参考方案：Sprout；Ziggy；Grom。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Knockout 重视生存和缩圈前空间；墙体完整时控场强，墙体破后远程强。

**Sprout — 成立**

- index 摘录（模式合同）：`墙后口袋投掷压缩空间；Hedge 封单一 choke 制造第一减员窗口；领先后的撤退路线封锁`。
- 支持链：敌方 Rico/Pierce 均有被 Sprout 墙控干扰的边；Spike/R-T 补入口保护，墙袋投掷能制造首杀。
- 条件／反证：Gene 拉人是明确反向证据；保留深口袋、挡手/压 Gene 充能，不能写成敌方完全无答案。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Ziggy — 成立**

- index 摘录（模式合同）：`墙角 delayed pick；末圈退线区域压迫；Super storm 封 round 收缩路径`。
- 支持链：延迟落雷/风暴压退线和墙角，R-T/Spike 保护与跟伤可将逼位转为回合收益。
- 条件／反证：需要固定退路与预判，Gene 拉人/开阔横移会削弱；不是稳定硬控。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Grom — 成立**

- index 摘录（模式合同）：`wall_cluster_area_control；late_round_choke_pressure；Super_knockback_finish`。
- 支持链：地图墙簇和窄口限制横移，Grom 十字投掷压路；R-T/Spike 保护入口，KO 首杀链成立。
- 条件／反证：需安全口袋和跟伤，Gene 的抓人威胁仍要处理，不能因无刺客就任意站位。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 26 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 26 行。来源：[题目视频](https://www.youtube.com/watch?v=qajAIs6gTLM&t=26s)。

<a id="case-27"></a>

### 27. Dueling Beetles · Hot Zone · 成立

`bobby-itE4PAuap_E-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Damian（partial）。

参考方案：Crow；Colette；Finx。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Hot Zone 的目标是持续站圈；这张图惩罚无法进圈或无法把敌人赶出圈的阵容。

**Crow — 成立**

- index 摘录（模式合同）：`anti_heal_zone_edge；slow_first_entry；bush_reveal_around_zone`。
- 支持链：压回复与入口减速妨碍单圈重进场，为后续占区者争时间。
- 条件／反证：必须有实际站圈身体和墙后答案，首选时属于可继续补齐的计划。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Colette — 成立**

- index 摘录（模式合同）：`反站圈身体；Push It 赶人出圈`。
- 支持链：百分比削前排和 Push It 推离计分区，直接覆盖进圈身体争夺。
- 条件／反证：需要队友站圈、清资源和反投掷，不能独自承担整个目标合同。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Finx — 成立**

- index 摘录（模式合同）：`Time Warp 站圈支援；reload tax 和 projectile slow`。
- 支持链：卡明确提供 Hot Zone 弹道减速/装填税和站圈支援，封闭入口可让后续射手/身体吃到收益。
- 条件／反证：后续确立 projectile 队友并防近身/召唤物；当前地图投影 weak 是漏匹配而非否定支援机制。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 27 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 27 行。来源：[题目视频](https://www.youtube.com/watch?v=itE4PAuap_E&t=4s)。

<a id="case-28"></a>

### 28. Open Business · Hot Zone · 成立

`bobby-itE4PAuap_E-q2`；pick / slot 2。己方：尚未选择；敌方：Finx。已知 bans：Damian, Crow, Colette（partial）。

参考方案：Emz；Otis；Chester；Lou；Stu；Lumi。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：目标是既能站圈，又能处理圈旁墙体后的控制点；只在外围消耗不够。

**Emz — 成立**

- index 摘录（模式合同）：`deny zone entrances with spray and slowing Super；heal through multi-target fights with Hype`。
- 支持链：Finx 卡明确列 lingering area/墙压会绕过弹道场优势；Emz 入口喷雾和范围减速转成站圈窗口。
- 条件／反证：先到安全喷雾边缘，后续处理投掷和远程，不在贴脸死角接战。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Otis — 成立**

- index 摘录（模式合同）：`zone_clear；entry_denial；anti_tank_or_anti_assassin_zone_defense`。
- 支持链：沉默、清圈与入口封锁可在后续组队中为占区提供防守层，满足地图目标的一种响应。
- 条件／反证：当前 Finx 不是已暴露近战；不能写成 Otis 硬克 Finx，仍须补占区/反墙控。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Chester — 成立**

- index 摘录（模式合同）：`zone_entry_burst；random_super_area_or_stun_window；anti_body_clear`。
- 支持链：墙旁中距离多铃爆发与随机 Super 入口惩罚，为队伍提供 Finx 弹道支援之外的接触威胁。
- 条件／反证：预热和 Super 类型不保证；后续补实际占区者/远程。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Lou — 成立**

- index 摘录（模式合同）：`区内 Super 覆盖和快速冰冻；Hypothermia 削站区者输出；Vision gear 草边持续标记`。
- 支持链：单圈 Super 覆盖与冻结将目标停留转为己方计分机会，可围绕控区展开。
- 条件／反证：不宣称弹道完全不受 Finx 影响；需队友站圈/击杀并回答墙后攻击。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Stu — 成立**

- index 摘录（模式合同）：`zone_touch_and_escape；speed_zone_return；poke_to_force_enemies_off_zone`。
- 支持链：机动换角、重复争点与墙侧接近能绕开固定弹道场交易，保留灵活的后续占区组合。
- 条件／反证：不能独自长时间站圈，Finx 的队友后续控制仍可能限制 dash。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Lumi — 成立**

- index 摘录（模式合同）：`单区口 Grim and Frostbitten 冰面与 Super root 延迟进区；区边召回穿墙跟伤`。
- 支持链：区边墙角召回、局部 slow/root 给固定入口另一种控制轴；Lumi 被 Finx 压制边也保留墙角回收的失效例外。
- 条件／反证：避免在无遮挡射线硬打 Finx；只在有视野、短召回和队友跟伤的角度成立。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 28 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 28 行。来源：[题目视频](https://www.youtube.com/watch?v=itE4PAuap_E&t=14s)。

<a id="case-29"></a>

### 29. Ring of Fire · Hot Zone · 成立

`bobby-itE4PAuap_E-q3`；pick / slot 6。己方：Lou, Byron；敌方：Stu, Leon, Pam。已知 bans：Damian（partial）。

参考方案：Draco。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：目标是持续站圈并控制草丛视野；缺探草会让任何圈外压制都不稳定。

**Draco — 成立**

- index 摘录（模式合同）：`zone_body；entry_denial_with_dragon_cone；damage_absorption_for_teammate_area_control`。
- 支持链：Lou 控制、Byron 治疗已有，Draco 正好提供实际 zone body；对 Stu 的窄口近战交换有直接边。
- 条件／反证：需 Super/Last Stand、治疗线和形态启动，敌方 Leon 绕后或 Pam 拖长交换不可忽略。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 29 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 29 行。来源：[题目视频](https://www.youtube.com/watch?v=itE4PAuap_E&t=28s)。

<a id="case-30"></a>

### 30. Shooting Star · Bounty · 成立

`bobby-5HP07EygUio-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Damian（partial）。

参考方案：Gene；Pierce；Najia。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Gene — 成立**

- index 摘录（模式合同）：`分裂弹长线 poke 建立星差；Magic Hand 抓失位或高价值长手；Vision Gear 探草和 Magic Puffs 治疗维持对线`。
- 支持链：长线 poke、抓人和支援可组成带跟伤的首选方案；地图仍留少量掩体可蓄资源。
- 条件／反证：index 明确警告 Shooting Star 易被长狙压制，因此只是有风险的可选方案，不能推导为安全最优一抢。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Pierce — 成立**

- index 摘录（模式合同）：`long_range_star_pick_pressure；last_ammo_slow_on_peeking_target；Super_homing_star_lead_hold`。
- 支持链：开放可见路线可产生拿星压力和末发减速，后续补保护使壳循环有机会启动。
- 条件／反证：其纯开放狙击镜像劣势仍成立；选它不意味着无需回答更稳定长手。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Najia — 成立**

- index 摘录（模式合同）：`wall_arc_poison_pressure_from_safe_angle；retreat_route_poison_to_punish_star_holders_or_chasers；grouped_target_zone_denial_with_puddles_and_snakes`。
- 支持链：地图保留的小墙袋与 Najia 的越墙毒区合同可组成条件反狙路线，给队友终结机会。
- 条件／反证：开墙与高速横移会失效，早手需规划反突；这里支持残墙分支而非把整张图当墙图。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 30 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 30 行。来源：[题目视频](https://www.youtube.com/watch?v=5HP07EygUio&t=4s)。

<a id="case-31"></a>

### 31. Shooting Star · Bounty · 成立

`bobby-5HP07EygUio-q2`；pick / slot 2。己方：尚未选择；敌方：Angelo。已知 bans：Gene, Pierce, Najia, Damian（partial）。

参考方案：Byron；Belle；Gus。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Byron — 成立**

- index 摘录（模式合同）：`长线治疗支援维持脆皮后排站线和星压；低承诺远程 chip 和 Malaise 削弱敌方回复；领先后的血量 swing 保星`。
- 支持链：以治疗维持队友长线输出，给 Angelo 蓄力交换制造持续成本，属于组合响应而非对枪必赢。
- 条件／反证：Angelo→Byron 是明确优势边；需安全角和搭档补伤，不能让 Byron 独自接蓄满箭。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Belle — 成立**

- index 摘录（模式合同）：`low_commitment_star_pressure；force_enemy_spacing；focus_mark_for_pick`。
- 支持链：稳定 poke/标记和队友跟伤可以在 Angelo 蓄力期间建立压力，符合地图长线职责。
- 条件／反证：Angelo→Belle 优势边成立；第二手仅保留组队路线，不能称其硬反 Angelo。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Gus — 成立**

- index 摘录（模式合同）：`long-range chip while protecting high-star teammate；shield and damage boost to win first-pick exchange`。
- 支持链：护盾、伤害增益和长线 chip 为搭档制造首杀或保星交换，满足对 Angelo 的资源响应方向。
- 条件／反证：必须由后续输出利用护盾，注意穿线与充灵体的安全；不能只按名义射程排序。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 31 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 31 行。来源：[题目视频](https://www.youtube.com/watch?v=5HP07EygUio&t=11s)。

<a id="case-32"></a>

### 32. Hideout · Bounty · 成立

`bobby-5HP07EygUio-q3`；pick / slot 5。己方：Gene, Byron；敌方：Belle, Nani。已知 bans：Damian（partial）。

参考方案：Mortis。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 要在拿星后保命；中路控墙和边路远程同时提供得分路线。

**Mortis — 成立**

- index 摘录（模式合同）：`最后手惩罚孤立低血后排和投掷；长 dash + Super 穿墙收割墙后保星位`。
- 支持链：Hideout 中央墙草给接触路线，Gene/Byron 提供压血、抓人和治疗；可针对 Belle/Nani 的后排窗口。
- 条件／反证：Nani 卡有反 Mortis 预判爆发边，必须用草墙/已交资源例外；敌方第六手仍可补守卫。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 32 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 32 行。来源：[题目视频](https://www.youtube.com/watch?v=5HP07EygUio&t=25s)。

<a id="case-33"></a>

### 33. Kaboom Canyon · Heist · 成立

`bobby-m4P2v_NfmlY-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Damian（partial）。

参考方案：Colt；Colette；Crow。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：主要目标是建立长线 safe DPS，同时防止敌方从中心草或局部墙体绕开正面对枪。

**Colt — 成立**

- index 摘录（模式合同）：`sustained_safe_dps；wallbreak_to_create_safe_angle；lane_duel_into_safe_pressure`。
- 支持链：开阔长线持续打库与选择性破墙直接兑现 Heist 目标，符合地图主线。
- 条件／反证：必须命中和有反突保护，不能为开墙帮敌方建立更强射线。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Colette — 成立**

- index 摘录（模式合同）：`special target safe burst；Super 往返打库；Push It 推开防守者或 Mass Tax 扛伤`。
- 支持链：安全充 Super 后直线往返打库，对特殊目标高伤是明确合同。
- 条件／反证：路径/充能/落点受控会失败；后续要开线和保护。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Crow — 成立**

- index 摘录（模式合同）：`lane_attrition_and_anti_heal；defender_slow_for_safe_dps_teammate；anti_short_range_safe_entry`。
- 支持链：中草探测与持续压回复帮助后续 DPS 打到金库，能先建立控线和防入库层。
- 条件／反证：不能当唯一 safe DPS；作者只给名字，不补造历史 Hyper 的数值理由。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 33 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 33 行。来源：[题目视频](https://www.youtube.com/watch?v=m4P2v_NfmlY&t=2s)。

<a id="case-34"></a>

### 34. Safe Zone · Heist · 成立

`bobby-m4P2v_NfmlY-q2`；pick / slot 2。己方：尚未选择；敌方：Angelo。已知 bans：Damian（partial）。

参考方案：Chuck。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Heist 目标访问有两条主线：可过水/越墙进入敌方半场，或远程/抛物线不进半场也能打库。

**Chuck — 成立**

- index 摘录（模式合同）：`charge_bounded_multi_dash_safe_damage；safe_entry_and_retreat_inside_one_pool；defender_route_disruption`。
- 支持链：用布站和有预算的 Super 把射线对枪改为金库访问，Angelo 只占一个长线位时保留该进攻方向合理。
- 条件／反证：不是无限循环：当前卡限制充能池，需布站成本、过河/墙路线与终点安全；原分析“补充充能”必须按实际命中条件解释。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 34 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 34 行。来源：[题目视频](https://www.youtube.com/watch?v=m4P2v_NfmlY&t=10s)。

<a id="case-35"></a>

### 35. Hot Potato · Heist · 成立

`bobby-m4P2v_NfmlY-q3`；pick / slot 6。己方：Spike, Otis；敌方：Rico, Nita, Carl。已知 bans：Damian（partial）。

参考方案：Shade。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Heist race 不只看 DPS，还看谁能从草丛或侧路安全转入金库输出。

**Shade — 成立**

- index 摘录（模式合同）：`short_range_safe_pressure_if_route_exists；wall_or_water_entry_to_base；defender_disruption`。
- 支持链：墙草与侧路可转为入库，Spike/Otis 已提供防接触，Shade 的特殊路线和对 Carl 的墙压边提供进攻补位。
- 条件／反证：Rico 弹墙、Nita 熊与 Carl 进场仍能限制启动/落点；须保证短手真正打到库，不是仅仅跨过地形。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 35 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 35 行。来源：[题目视频](https://www.youtube.com/watch?v=m4P2v_NfmlY&t=22s)。

<a id="case-36"></a>

### 36. Double Swoosh · Gem Grab · 成立

`bobby-BiABMt4w2qI-q1`；pick / slot 3。己方：Sandy；敌方：Colette。已知 bans：Damian（partial）。

参考方案：Crow。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Gem Grab 的目标访问依赖中路站位与倒计时撤退；侧路击杀和探草能改变宝石持有者的退路。

**Crow — 成立**

- index 摘录（模式合同）：`bush_reveal_for_carrier_safety；anti_heal_mid_chip；low_health_cleanup_after_countdown_pressure`。
- 支持链：Crow→Colette 的毒伤/反治疗惩罚方向存在，草路显形配合 Sandy 争矿区和撤退线。
- 条件／反证：Sandy 与 Crow 的对敌关系不能当队内相克；后续需要实际 carrier/输出，毒伤不自动收割。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 36 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 36 行。来源：[题目视频](https://www.youtube.com/watch?v=BiABMt4w2qI&t=2s)。

<a id="case-37"></a>

### 37. Hard Rock Mine · Gem Grab · 成立

`bobby-BiABMt4w2qI-q2`；pick / slot 6。己方：Rico, Chester；敌方：Ruffs, Gene, Shade。已知 bans：Damian（partial）。

参考方案：Edgar；Bull。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Gem carrier 需要在开放中路收宝石，同时依赖草带和墙体保护撤退；边路线权会决定中路安全。

**Edgar — 成立**

- index 摘录（模式合同）：`侧路追击 gem carrier；倒计时翻盘进场；短时间抢矿后撤`。
- 支持链：地图侧草/墙和跳入追宝合同能让 Rico/Chester 的压力转为针对 Ruffs/Gene 后排的接触窗口。
- 条件／反证：Gene 击退、Ruffs 沙包与 Shade 特殊位移都需先消耗；完成阵容还要指定安全拾宝人，不能让 Edgar 裸当稳定中路。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Bull — 成立**

- index 摘录（模式合同）：`侧草压迫；保护/追击 gem carrier`。
- 支持链：侧草高血近身压力与护送/追宝职责，可配 Rico 走廊火力和 Chester 接触爆发逼退敌方中路。
- 条件／反证：需处理 Gene 推退和 Shade 墙内窗口、保护实际持宝者；强行直线冲进去不成立。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 37 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 37 行。来源：[题目视频](https://www.youtube.com/watch?v=BiABMt4w2qI&t=12s)。

<a id="case-38"></a>

### 38. Undermine · Gem Grab · 成立

`bobby-BiABMt4w2qI-q3`；pick / slot 4。己方：Crow；敌方：Pierce, Otis。已知 bans：Damian（partial）。

参考方案：Charlie。

参考理由：蜘蛛针对 Pierce 应对召唤物弱点；补一名反坦克

地图证据：中路负责稳定拿宝石，边路负责阻止敌方从草丛推进；倒计时撤退通常依赖己方半场墙后草丛。

**Charlie — 成立**

- index 摘录（模式合同）：`gem_carrier_cocoon_disarm；side_grass_spider_scout；countdown_comeback_pick`。
- 支持链：Spiders 的 shot tank/bush scout 与 Pierce 的 spawnable ammo waste 失败模式可直接组合；茧承担载体/反进场移除。
- 条件／反证：无需新增 Charlie→Pierce 答案边；Otis 不一定同样被蜘蛛克制，下一手补输出/拾宝且避免茧被溅射提前打破。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 38 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 38 行。来源：[题目视频](https://www.youtube.com/watch?v=BiABMt4w2qI&t=32s)。

<a id="case-39"></a>

### 39. Triple Dribble · Brawl Ball · 成立

`bobby-K7iG6U18pR4-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Damian（partial）。

参考方案：Colette。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：核心是打开球门角度或用强控/弹墙/位移绕过防线；不处理墙体就难以稳定进球。

**Colette — 成立**

- index 摘录（模式合同）：`清守门人；打断持球和反前排；把高血量 scorer 推出得分线`。
- 支持链：足球合同明确清守门、反高血持球者和推离得分线，为首选后的破门/scorer 创造窗口。
- 条件／反证：后续必须处理门前墙和投掷/召唤物；目前只支持一个可完成的首选计划。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 39 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 39 行。来源：[题目视频](https://www.youtube.com/watch?v=K7iG6U18pR4&t=2s)。

<a id="case-40"></a>

### 40. Pinhole Punt · Brawl Ball · 成立

`bobby-K7iG6U18pR4-q2`；pick / slot 5。己方：Lumi, Kaze；敌方：Edgar, Amber。已知 bans：Damian（partial）。

参考方案：Chester；Otis。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：先扫清中央草环并建立球权，再通过前排/控场穿过墙封草簇，把线权转成窄门射门或选择性破门窗口。

**Chester — 成立**

- index 摘录（模式合同）：`ball_carrier_burst_or_stun；goal_defender_knockback_or_area_control；anti_aggro_midfield_trade`。
- 支持链：对 Edgar 的高铃/控制反进场边明确，Lumi/Kaze 提供角度和切入，Chester 补球路接触惩罚。
- 条件／反证：保高铃/匹配 Super；Amber 持续消耗与末手长线仍须防。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Otis — 成立**

- index 摘录（模式合同）：`anti_scorer_defense；pass_or_dash_denial；chokepoint_block`。
- 支持链：Edgar 卡明确被 Otis 沉默关闭贴脸；足球合同的断连招/控球路补 Lumi/Kaze 的防守。
- 条件／反证：Amber 烧草会削弱草锚 hook，不能只依赖草；进球转换由队友承担。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

地图覆盖限制：Jev 所用 S49 index 没有本图，本条依默认 35 图快照审查。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 40 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 40 行。来源：[题目视频](https://www.youtube.com/watch?v=K7iG6U18pR4&t=10s)。

<a id="case-41"></a>

### 41. Center Stage · Brawl Ball · 部分成立／缺关键闭环

`bobby-K7iG6U18pR4-q3`；pick / slot 6。己方：Chester, Najia；敌方：Kenji, Poco, Nita。已知 bans：Damian（partial）。

参考方案：Shade；Bull（作者说熟练使用时也可奏效）。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Brawl Ball 的目标不是杀人，而是制造持球推进、破门或强控得分窗口。

**Shade — 部分成立／缺关键闭环**

- index 摘录（模式合同）：`wall_phase_defender_disruption；short_range_scoring_pressure；fear_or_center_hit_chase`。
- 支持链：穿墙接近、近身得分压力有正向机制，Chester/Najia 可提供爆发和毒区。
- 条件／反证：但敌方 Kenji 有越墙 Super、Nita 有熊/反突、Poco 有续航，直接触发 Shade 依赖的墙内安全/短手交易疑点。index 尚缺这一完整对局如何压过清场与续航的具体闭环，不能直接套“敌方无答案”。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Bull — 成立**

- index 摘录（模式合同）：`wallbreak_score_window；self_pass_scorer；goal_front_body_pressure`。
- 支持链：作者限熟练度；Bull→Poco 的路线贴脸边与破门/自传球合同支持一种进攻替代，Chester/Najia 提供跟伤。
- 条件／反证：必须保留熟练度条件；Nita→Bull 反突边要求骗熊/换角，Kenji 与 Poco 的续航会延长交换，并非无条件优于 Shade。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 41 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 41 行。来源：[题目视频](https://www.youtube.com/watch?v=K7iG6U18pR4&t=25s)。

<a id="case-42"></a>

### 42. Belle's Rock · Knockout · 成立

`bobby-58k8-_o9sKU-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Damian（partial）。

参考方案：Gene；Pierce。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Knockout 重视生存和缩圈前空间；墙体完整时控场强，墙体破后远程强。

**Gene — 成立**

- index 摘录（模式合同）：`Magic Hand 抓孤立目标制造 first pick；分裂弹长线 poke 保护回合；VisionGear 和 Lamp Blowout 探草/防突进`。
- 支持链：墙袋抓人、探草与后续爆发伙伴可形成 KO 首杀计划。
- 条件／反证：拉中后要能杀且防召唤物挡手；本题名单未含 Najia 不代表排斥所有其他答案。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Pierce — 成立**

- index 摘录（模式合同）：`long_lane_first_pick_pressure；Super_finish_window_after_shell_setup；last_ammo_slow_to_force_collapse`。
- 支持链：长线 chip/末发减速与资源准备后的 Super 可为墙图提供远程首杀压力。
- 条件／反证：后续处理墙控/突进、保护空弹；不把地图 strong 当免疫克制。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 42 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 42 行。来源：[题目视频](https://www.youtube.com/watch?v=58k8-_o9sKU&t=2s)。

<a id="case-43"></a>

### 43. Hot Potato · Heist · 成立

`bobby-58k8-_o9sKU-q2`；pick / slot 6。己方：Nita, Lumi；敌方：Berry, Emz, Rico。已知 bans：Damian（partial）。

参考方案：Dynamike；Barley。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Heist race 不只看 DPS，还看谁能从草丛或侧路安全转入金库输出。

**Dynamike — 成立**

- index 摘录（模式合同）：`wall_pocket_safe_damage；Satchel_defense_against_safe_entry；Super_burst_and_wall_transform`。
- 支持链：安全墙后攻击对付固定控制点并转金库爆发；Nita/Lumi 已给接触与路径限制，敌方当前无直接刺客。
- 条件／反证：Satchel/Super 时机、Berry 范围互压和墙体变化需处理；不要为了开墙破坏自己的安全位。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Barley — 成立**

- index 摘录（模式合同）：`Super safe burst；普攻多跳固定目标伤害；防守近战 safe hitter 的路线`。
- 支持链：持续投掷和 Heist Super 打库分支可从墙后处理敌方防守，Rico 卡有被 Barley 墙控的边。
- 条件／反证：需要 Extra Noxious/安全投掷角，保护 Super 完整释放；Berry 镜像和 Emz 推进不等于免费优势。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 43 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 43 行。来源：[题目视频](https://www.youtube.com/watch?v=58k8-_o9sKU&t=18s)。

<a id="case-44"></a>

### 44. Layer Cake · Bounty · 部分成立／缺关键闭环

`bobby-58k8-_o9sKU-q3`；pick / slot 5。己方：Belle, Colette；敌方：Gus, Penny。已知 bans：Damian（partial）。

参考方案：Chester；Otis。

参考理由：作者认为 Colette 限制敌方投掷；抢走剩余反坦克选择

地图证据：Bounty 中每层掩体都能保护领先方；落后方需要开墙、投掷或越墙制造击杀窗口。

**Chester — 部分成立／缺关键闭环**

- index 摘录（模式合同）：`多铃近身爆发惩罚无 peel 后排；随机 Super (stun/knockback) 创造拿星窗口；草/墙路线反切残血`。
- 支持链：Belle 提供长线，Chester 的中近爆发能防对方最后手近战；泛化防守补位有根据。
- 条件／反证：作者关键前提“Colette 限制敌方投掷，抢余下反坦”没有充分支撑；Colette 卡反而警告墙控/召唤物稀释。Layer Cake 依赖墙，最终队伍如何防敌方投掷仍未闭合。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Otis — 部分成立／缺关键闭环**

- index 摘录（模式合同）：`Super mute 封锁保星后排或长手操作；Ink Refills 在长线持续压低血目标；Phat Splatter 暴露墙后保星位`。
- 支持链：沉默/持续输出可补长线阵容的单点防守，Bounty 合同支持保星跟伤。
- 条件／反证：Otis 自身也要求反投掷/开墙，不能靠同样怕墙控的 Colette 直接宣布封掉敌方投掷；需要具体构筑/可达性或原视频上下文。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 44 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 44 行。来源：[题目视频](https://www.youtube.com/watch?v=58k8-_o9sKU&t=34s)。

<a id="case-45"></a>

### 45. Double Swoosh · Gem Grab · 成立

`bobby-SoRLuUmTPG4-q1`；pick / slot 2。己方：尚未选择；敌方：Crow。已知 bans：Damian（partial）。

参考方案：Chester；Lumi。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Gem Grab 的目标访问依赖中路站位与倒计时撤退；侧路击杀和探草能改变宝石持有者的退路。

**Chester — 成立**

- index 摘录（模式合同）：`mine_entry_bodyguard；carrier_chase_punish；mid_close_burst_pick`。
- 支持链：草路的多铃接触与矿区护卫能构筑应对 Crow 探测的范围压力，后续补 carrier/长线。
- 条件／反证：不声称硬克 Crow；先探明路线再近身，避免被持续显形后远端磨血。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Lumi — 成立**

- index 摘录（模式合同）：`矿区穿墙召回压力；carrier 退线 slow/root`。
- 支持链：召回穿墙与退线控制可借地图草墙改换攻击角度，避免只与 Crow 站开放线互耗。
- 条件／反证：Lumi 卡明确怕 Crow 毒伤；其例外是墙角短召回/队友视野控制，需依该分支而非忽略负边。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 45 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 45 行。来源：[题目视频](https://www.youtube.com/watch?v=SoRLuUmTPG4&t=7s)。

<a id="case-46"></a>

### 46. Layer Cake · Bounty · 成立

`bobby-SoRLuUmTPG4-q2`；pick / slot 6。己方：Gus, Kaze；敌方：Juju, Belle, Chester。已知 bans：Damian（partial）。

参考方案：Ziggy。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 中每层掩体都能保护领先方；落后方需要开墙、投掷或越墙制造击杀窗口。

**Ziggy — 成立**

- index 摘录（模式合同）：`退线区域压迫；墙后长线 delayed pick；Electric Shuffle 对可见目标追压`。
- 支持链：Layer Cake 的层级窄口限制横移，Ziggy 延迟落雷逼退，Gus 护盾与 Kaze 侧压帮助拿星/保星。
- 条件／反证：必须预判退路并保护本体，Juju 资源与 Chester 近身不可无视；index 弱投影遗漏了明确的 choke 连接。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 46 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 46 行。来源：[题目视频](https://www.youtube.com/watch?v=SoRLuUmTPG4&t=16s)。

<a id="case-47"></a>

### 47. Ring of Fire · Hot Zone · 部分成立／缺关键闭环

`bobby-SoRLuUmTPG4-q3`；pick / slot 5。己方：Lou, Leon；敌方：Pierce, Lumi。已知 bans：Damian（partial）。

参考方案：Edgar；Alli。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：目标是持续站圈并控制草丛视野；缺探草会让任何圈外压制都不稳定。

**Edgar — 部分成立／缺关键闭环**

- index 摘录（模式合同）：`跳入站圈抱团打出一次清场窗口；贴脸处理圈旁投掷/控制`。
- 支持链：跳入 Pierce 空弹或 Lumi 布锤窗口有方向，Lou 控制/Leon 同步能帮助清圈。
- 条件／反证：己方最终 Lou/Leon/Edgar 的持续占区和再入场成本没有充分闭环，各卡都向队友索取 body/保护；对手还有第六手反突。支持清场候选，暂不足以完整支持该补位。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

**Alli — 部分成立／缺关键闭环**

- index 摘录（模式合同）：`草/水边缘击杀；清残血回区者；逼迫敌方后排远离区边`。
- 支持链：草路追猎半血目标与 Lou/Leon 压血可联成清理窗口。
- 条件／反证：同样缺最终持续占区安排；Alli 明确需要压血来源且不能清满血 sustain body，敌方第六手未定。不能把进场成功等于赢计分。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 47 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 47 行。来源：[题目视频](https://www.youtube.com/watch?v=SoRLuUmTPG4&t=30s)。

<a id="case-48"></a>

### 48. Hard Rock Mine · Gem Grab · 存在未解规则张力

`bobby-StONtQp8uZ4-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：未提供（not_provided）。

参考方案：Sirius；Najia；Edgar；Colette。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Gem carrier 需要在开放中路收宝石，同时依赖草带和墙体保护撤退；边路线权会决定中路安全。

**Sirius — 成立**

- index 摘录（模式合同）：`carrier_bodyguard；mine_entry_shadow_tax；side_bush_shadow_pressure`。
- 支持链：矿区影子护送与侧草资源压力能先确定一种后续补 carrier/清场保护的结构。
- 条件／反证：其 slot_1 明确不宜无条件先手，故只支持有后续应对 splash/pierce 的计划，不支持安全无脑首选。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Najia — 成立**

- index 摘录（模式合同）：`mine_entry_poison；carrier_route_pressure；wall_angle_control`。
- 支持链：矿区入口/墙角毒区给队友争收宝和退线，地图提供了明确固定接触路径。
- 条件／反证：后续须补保镖、终结和实际 carrier，未知 bans 不证明刺客池已受限。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Edgar — 存在未解规则张力**

- index 摘录（模式合同）：`侧路追击 gem carrier；倒计时翻盘进场；短时间抢矿后撤`。
- 支持链：地图侧草与跳入追宝给出后手惩罚路线，但无法独立解释当前裸一抢。
- 条件／反证：slot_1 仅允许“明确奖励 Brawl Ball scorer 且高优先反制已 ban”的例外；本题是 Gem Grab 且 bans 未知，投影却 early_pick=true。要核早手规则/版本/作者条件。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Colette — 成立**

- index 摘录（模式合同）：`反高血量护送；应急拾宝返回`。
- 支持链：反高血护送与应急拾宝合同，可在草路接触地图作为后续补 carrier 的前排约束手。
- 条件／反证：不是默认 carrier；缺敌方时只支持开放的反身体计划，后续需清资源/墙控。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 48 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 48 行。来源：[题目视频](https://www.youtube.com/watch?v=StONtQp8uZ4&t=4s)。

<a id="case-49"></a>

### 49. Double Swoosh · Gem Grab · 成立

`bobby-StONtQp8uZ4-q2`；pick / slot 5。己方：Lumi, Sirius；敌方：Mortis, Sandy。已知 bans：Najia, Colette, Lola（partial）。

参考方案：Nita；Emz。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Gem Grab 的目标访问依赖中路站位与倒计时撤退；侧路击杀和探草能改变宝石持有者的退路。

**Nita — 成立**

- index 摘录（模式合同）：`center_or_side_pierce_control；Bruce_carrier_pressure；bush_scouting`。
- 支持链：有 Nita 对 Mortis/Sandy 的条件边，Bruce/Bear Paws 与穿透保护 Lumi/Sirius 的资源展开并争草路。
- 条件／反证：无熊期与第六手清召唤物是代价；实际持宝和熊/影子分散仍要安排。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Emz — 成立**

- index 摘录（模式合同）：`hold mid entrance and punish grouped gem escorts；sweep grass routes with wide spray`。
- 支持链：宽喷雾与区域慢速惩罚 Sandy 草路，Sirius 资源掩护可使 Emz 不孤立，帮助保护矿区。
- 条件／反证：Mortis→Emz 优势边不可删除；必须保 Friendzoner/队友资源守近身，而非声称 Emz 单人硬克 Mortis。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 49 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 49 行。来源：[题目视频](https://www.youtube.com/watch?v=StONtQp8uZ4&t=17s)。

<a id="case-50"></a>

### 50. Dueling Beetles · Hot Zone · 成立

`bobby-StONtQp8uZ4-q3`；pick / slot 6。己方：Bull, Emz；敌方：Lumi, Juju, Chester。已知 bans：未提供（not_provided）。

参考方案：Gray。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Hot Zone 的目标是持续站圈；这张图惩罚无法进圈或无法把敌人赶出圈的阵容。

**Gray — 成立**

- index 摘录（模式合同）：`把队友送入热区或从 L 墙支援口袋撤出；拉出圈内关键目标；通过传送改变支援角度`。
- 支持链：Bull 的身体和 Emz 的清圈已齐，Gray 传送补进区路线；Juju 卡有被 Gray 传送/接近回答的边。
- 条件／反证：出口避开 Lumi/Chester 的预封，门启动需保护；不把 Gray→Emz 对敌边误当队内协同证据。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：无。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 50 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 50 行。来源：[题目视频](https://www.youtube.com/watch?v=StONtQp8uZ4&t=30s)。

<a id="case-51"></a>

### 51. Kaboom Canyon · Heist · 成立

`bobby-uw_BQfFSFZY-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：Najia（partial）。

参考方案：Crow。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：主要目标是建立长线 safe DPS，同时防止敌方从中心草或局部墙体绕开正面对枪。

**Crow — 成立**

- index 摘录（模式合同）：`lane_attrition_and_anti_heal；defender_slow_for_safe_dps_teammate；anti_short_range_safe_entry`。
- 支持链：中心草探测/压回复帮助后续真正 safe DPS 获得射线，ban Najia 减少一个墙角压力来源。
- 条件／反证：仅支持控制型首选，不推导当前必然最高伤害/唯一最优；仍补 DPS 与反突。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 51 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 51 行。来源：[题目视频](https://www.youtube.com/watch?v=uw_BQfFSFZY&t=7s)。

<a id="case-52"></a>

### 52. Pinhole Punt · Brawl Ball · 成立

`bobby-uw_BQfFSFZY-q2`；pick / slot 5。己方：Chester, Max；敌方：Poco, Meeple。已知 bans：Najia（partial）。

参考方案：Kenji。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：先扫清中央草环并建立球权，再通过前排/控场穿过墙封草簇，把线权转成窄门射门或选择性破门窗口。

**Kenji — 成立**

- index 摘录（模式合同）：`dash 带球和抢中路；Super 清守门人或躲关键控制；Hyper 拉人团灭窗口`。
- 支持链：Kenji→Poco 的近身资源战边明确，Max 加速和 Chester 跟伤帮助足球推进、清守门与得分。
- 条件／反证：Meeple 的陷阱/控制和末手反突要追踪，Kenji 回返位置需安全；弱投影不应盖过这些机制。
- 地图投影：`weak`；本次选位桶召回：无；加敌方关系后：有。

地图覆盖限制：Jev 所用 S49 index 没有本图，本条依默认 35 图快照审查。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 52 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 52 行。来源：[题目视频](https://www.youtube.com/watch?v=uw_BQfFSFZY&t=15s)。

<a id="case-53"></a>

### 53. Shooting Star · Bounty · 成立

`bobby-uw_BQfFSFZY-q3`；pick / slot 6。己方：Tick, R-T；敌方：Gray, Pierce, Byron。已知 bans：Najia（partial）。

参考方案：Nani。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Bounty 中远程拿星和保星是主线；落后方需要开墙、投掷角度或强制进场。

**Nani — 成立**

- index 摘录（模式合同）：`extreme_range_burst_pick_on_fragile_long_range；peep_wallbreak_or_retarget_to_open_star_lane；return_to_sender_sniper_mirror_answer`。
- 支持链：Tick 墙控/R-T 近身守路已有，Nani 补超远收束爆发和 Peep 开角；Gray 卡有被 Nani 长线爆发回答的方向。
- 条件／反证：Gray 传送可改角，Pierce/Byron 不会静止接满伤；控制 Peep 时保护本体。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 53 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 53 行。来源：[题目视频](https://www.youtube.com/watch?v=uw_BQfFSFZY&t=36s)。

<a id="case-54"></a>

### 54. Ring of Fire · Hot Zone · 成立

`bobby-02w4WJrpZOg-q1`；pick / slot 1。己方：尚未选择；敌方：尚未选择。已知 bans：未提供（not_provided）。

参考方案：Finx；Lou；Crow。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：目标是持续站圈并控制草丛视野；缺探草会让任何圈外压制都不稳定。

**Finx — 成立**

- index 摘录（模式合同）：`Time Warp 站圈支援；reload tax 和 projectile slow`。
- 支持链：L 墙支援与弹道场可作为围绕后续射手/占区身体构筑的单圈开局。
- 条件／反证：需要把支援转为计分；敌方近身/召唤物分支仍需后续回答。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Lou — 成立**

- index 摘录（模式合同）：`区内 Super 覆盖和快速冰冻；Hypothermia 削站区者输出；Vision gear 草边持续标记`。
- 支持链：单圈 Super 控区、冻结与削输出直接创造踩区窗口，适合随后补身体/击杀。
- 条件／反证：Lou 不是独自长期站圈的全能答案；防远端投掷、净化与长线。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Crow — 成立**

- index 摘录（模式合同）：`anti_heal_zone_edge；slow_first_entry；bush_reveal_around_zone`。
- 支持链：持续草区显形、压回复和减速回区直接对应地图入口安全。
- 条件／反证：后续补真正占区/范围清点，未知 bans 不保证安全。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 54 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 54 行。来源：[题目视频](https://www.youtube.com/watch?v=02w4WJrpZOg&t=4s)。

<a id="case-55"></a>

### 55. Hard Rock Mine · Gem Grab · 成立

`bobby-02w4WJrpZOg-q2`；pick / slot 6。己方：Chester, Ruffs；敌方：Rico, Max, Lily。已知 bans：未提供（not_provided）。

参考方案：Shade。

参考理由：敌方无法有效应对 Shade 超级技能

地图证据：Gem carrier 需要在开放中路收宝石，同时依赖草带和墙体保护撤退；边路线权会决定中路安全。

**Shade — 成立**

- index 摘录（模式合同）：`wall_side_pressure；punish_gem_carrier_near_wall；route_denial_with_Radius_trait`。
- 支持链：墙路/虚体避正面射线并威胁敌方矿区，Chester 近战惩罚和 Ruffs 增益为启动提供支撑。
- 条件／反证：敌方 Max/Lily 可换角，Rico 可守出墙；作者“无法应对”只能读为缺便宜稳定答案。Ruffs 选择性开墙不能拆掉 Shade 路线。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 55 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 55 行。来源：[题目视频](https://www.youtube.com/watch?v=02w4WJrpZOg&t=18s)。

<a id="case-56"></a>

### 56. Belle's Rock · Knockout · 成立

`bobby-02w4WJrpZOg-q3`；pick / slot 6。己方：Gus, Tick；敌方：Kit, Mortis, Angelo。已知 bans：未提供（not_provided）。

参考方案：Bull；Darryl。

参考理由：reference 未记录具体理由；以下为本次机制推论。

地图证据：Knockout 重视生存和缩圈前空间；墙体完整时控场强，墙体破后远程强。

**Bull — 成立**

- index 摘录（模式合同）：`草/墙路线伏击首杀；Super 破墙改变对位结构；Stomper 停位收低血目标`。
- 支持链：Kit 与 Mortis 卡都记录被 Bull 近身身体/爆发惩罚，能保护 Gus/Tick 墙后输出并把防切转为 KO 生存。
- 条件／反证：不要为了追 Angelo 离开后排；保留草墙，冲锋不免伤。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

**Darryl — 成立**

- index 摘录（模式合同）：`route_based_last_pick_engage；protected_first_contact；anti_thrower_or_sniper_punish`。
- 支持链：双霰弹近身接触、保护性进场和回合路线控制可给 Gus/Tick 提供身体，并威胁被墙控限制的后排。
- 条件／反证：需守好 Mortis/Kit 接近终点再择机滚入，不把滚动当任意无伤开团；保留队友接应。
- 地图投影：`strong`；本次选位桶召回：有；加敌方关系后：有。

证据定位：[index-evidence.jsonl](index-evidence.jsonl) 第 56 行，候选键 `candidates/<英雄名>`；[结构化审阅](reviews.jsonl) 第 56 行。来源：[题目视频](https://www.youtube.com/watch?v=02w4WJrpZOg&t=35s)。

## 验证与复现

本报告未修改题面、作者答案、实体机制、编译器或 runtime；未新增/删除题目、未升级 gold。数据结构、计数、证据指针和文件哈希由本目录 `verify_audit.py` 核对；检索结果可用 `reproduce_retrieval.py --index <同哈希 index> --output <新路径>` 重跑。语义评级是本轮审阅判断，不会由验证脚本自动证明。

本轮实测：题库 `--strict-knowledge` 通过（56 题、19 字幕、15 截图、91 知识文件，无漂移，890 本地链接）；审计覆盖/实时哈希校验通过；112 次查询复现与归档完全一致。见 [validation.json](validation.json)。
