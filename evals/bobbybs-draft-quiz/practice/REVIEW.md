# BobbyBS BP 练习题清洗稿（待确认）

56 题均已补一项中间档和一项反面选项。所有新等级都是维护者提案，不是作者原话、当前版本 gold 或模型实测成绩。

**请先确认逐题分档；没有把风险大自动当成错误，也没有把作者名单外的英雄一律当错。** 中间档和反面选项仍需反证审阅及隔离模型回归。

第 4、48 题保留可解释的正确分支，争议分支单列；第 41 题 Bull 带熟练度前提，不默认替用户满足；第 44、47 题原答案闭环不足。这三题暂不进入正式抽题。

选项池可多于 5 项，实际题卡固定选出 3–5 项，至少各一项三档选项；正确分支轮换展示。一次选一个方案，不要求找齐所有正确答案；第 2 题选一个双人组合。

本稿暂以英雄／组合为选项标题，解释在答题后展示。新增等级与正确分支的比较不是全局最优证明。历史补丁未知，已知 ban 按题面，其余不假定已知。

## 1. Hard Rock Mine · Gem Grab · 第 6 手

己方：Griff、Starr Nova；敌方：Amber、Carl、Otis；已知禁用：Gus、Shade、Rico。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Pierce | 长线压矿与末发减速补 Griff/Starr Nova 的边路压力；队友争取安全捡壳空间。 条件：Amber 可封捡壳路线，Carl 可接近；不能让 Pierce 单独承担裸站矿和探草。 |
| 对 | Byron | 长线治疗维持两名边路的接触时间，并在开放中路消耗 Amber；支援控矿逻辑成立。 条件：需明确实际拾宝人和治疗线；Byron 卡明确不把治疗等同自己稳定站矿，Otis/Carl 的接近仍须防。 |
| 对 | Janet | Gem carrier 的飞行撤退、探草及侧草压迫对应地图的收宝与倒计时撤退。 条件：不能把飞行当消除既有持续伤害；Carl 接近和落地位置要由双边路保护。 |
| 合理，但是有改进空间 | Belle | 补长线和标记压力，但 Griff/Starr Nova 的双边路仍要求她处理持宝与侧切安全；缺少 Byron 的治疗或 Janet 的撤退工具。 |
| 不太合理 | El Primo | 再加近身边路仍缺稳定中路；Amber 封路线、Otis 沉默和 Carl 绕侧让接近与持宝同时吃紧。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 1 行。

## 2. Belle's Rock · Knockout · 第 4 手

己方：Gus；敌方：Piper、Wendy；已知禁用：Shade。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Sprout + R-T | 棋盘墙袋让投掷压缩 Piper/Wendy 的直线位置；Hedge 将空间优势转为首杀窗口。；分体近路守卫加标记跟伤，为 Sprout 提供入口保护；敌方 Piper 卡也记有 R-T 回答边。 条件：依赖完整墙袋，敌方还有第六手破墙或突进；必须与 R-T 或 Pearl 一起评价。；保护腿位，防第六手投掷/穿透；不能把敌方 Griff 这个事后选项当作当前已知敌人。 |
| 对 | Sprout + Pearl | 棋盘墙袋让投掷压缩 Piper/Wendy 的直线位置；Hedge 将空间优势转为首杀窗口。；Gus 保护蓄 Heat，Pearl 的近身反突 Super 和高热火力补 Sprout 的入口防守/击杀。 条件：依赖完整墙袋，敌方还有第六手破墙或突进；必须与 R-T 或 Pearl 一起评价。；投掷和超长线会迫使 Pearl 消耗 Heat；开墙需避免拆掉 Sprout 唯一口袋。 |
| 合理，但是有改进空间 | Edgar + Rico | 有切后排和弹墙压制的协同，但对方尚有末手拆墙回应；墙被打开后 Piper 的长线会更舒服。 |
| 不太合理 | Frank + Poco | 同时锁定近身身体与治疗，却仍缺穿过 Piper/Wendy 墙线的可靠接近手段；敌方第六手可再补反坦或控制。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 2 行。

## 3. Double Swoosh · Gem Grab · 第 6 手

己方：Jessie、Shade；敌方：Gray、Tara、Bull；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Nita | Bull 的窄路入场可被 Bruce/Bear Paws 惩罚；Tara 卡有被 Nita 资源/范围压制的条件边，草路让熊和穿透有目标。 条件：Gray 传送可绕开熊；Tara 拉人、Bull 爆发和无熊期都能反转。只能支持条件反制，不能证明无条件克制三人。 |
| 合理，但是有改进空间 | Emz | 范围伤害可压 Bull 的接近与狭口，但 Gray 传送、Tara 拉拽可能跳过最佳输出距离；较 Nita 更依赖推开资源。 |
| 不太合理 | Piper | 再补单发远程，无法稳定处理侧草中的 Bull 和传送接近；Jessie/Shade 也不能替她长期清出长线。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 3 行。

## 4. Shooting Star · Bounty · 第 1 手

己方：未选；敌方：未选；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Pierce | 开放长线提供低承诺拿星、慢速控制和 Super 收束路线，能作为后续补保护的首选核心。 条件：对稳定狙击镜像存在资源劣势，需保护空弹/捡壳；不是因为 map fit strong 就无条件一抢。 |
| 合理，但是有改进空间 | Brock | 能打长线并拆掩体，但慢弹道与有限保命使开阔对枪更依赖预判；需要后续队友保侧翼。 |
| 不太合理 | Bull | 首手在极开阔图暴露近身路线，又无已选队友提供接近工具；不能把高血量当成安全拿星和撤退。 |
| 待复核，不强行分档 | Colette | 卡里有 Super 位移和支援消耗方向，但缺从开局状态到先拿 Blue Star 再保星的可执行机制。 当前失败条件明确要求预算 Super 充能；题面未给开局 Super/特殊资源，不能把抢宝石 Super 类比成可立即抢蓝星。 |
| 待复核，不强行分档 | Mortis | dash 提供接近可能，但作者的蓝星首选理由未形成 index 内的抢星—撤退—后续价值闭环。 Mortis slot_1 写“不早手”；Shooting Star 规则写刺客反狙必须等最后手。需要补蓝星战术适用条件或核历史版本，不能静默忽略规则。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 4 行。

## 5. Ring of Fire · Hot Zone · 第 6 手

己方：Lou、Leon；敌方：Fang、Amber、Gray；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Poco | 单圈需要续航/探草；Poco 的治疗重置、状态净化与 Lou 的控区和 Leon 的压力可共同延长留圈时间。Fang 卡的击杀链依赖目标死亡，治疗阻断斩杀线是合理组合推论。 条件：只有定性支持：净化不等于消除 Amber 全部直伤，也不能无条件挡 Gray 位移；聚集会给 Fang 链跳，必须保持治疗覆盖而不送连跳。尚不能证明优于 Pam/Gale。 |
| 合理，但是有改进空间 | Pam | 可补治疗和站圈身体，但治疗区更固定，不能等同 Poco 的范围净化；需要防 Fang/Gray 集中进入治疗阵地。 |
| 不太合理 | Tick | 增加外围墙后消耗却难补持续站圈；Fang/Gray 的接近会进一步挤压 Lou/Leon 的保护资源。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 5 行。

## 6. Open Business · Hot Zone · 第 5 手

己方：Emz、Gray；敌方：Draco、Max；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Frank | Gray 送入目标、Emz 跟范围伤害，Frank 的 zone body/眩晕把支援转成计分；有 Frank 对 Draco 的近身交换边。 条件：Max 可以躲前摇，敌方仍留第六手反坦；不是仅靠高血量就能进圈。 |
| 合理，但是有改进空间 | Buster | 可借 Gray 接近，用护盾和身体帮 Emz 争圈；护盾朝向与持续时间有限，对 Draco 的持续承压不如 Frank 方案直接。 |
| 不太合理 | Piper | 再补外围点射仍缺可靠站圈身体；Draco 配 Max 的接近会压缩射程优势，Gray 的送人能力也难转为占区时间。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 6 行。

## 7. Pinball Dreams · Brawl Ball · 第 4 手

己方：Barley；敌方：8-Bit、Colette；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Lou | 足球合同明确冻结持球者掉球和冰面封门；Lou 对 8-Bit 的阵地消耗边与 Barley 的铺地形成防守闭环。 条件：对 Colette 不是明示硬克；仍要由第五手补进球/破门。地图 weak 与这些机制并不相符，属于投影漏召回风险。 |
| 合理，但是有改进空间 | Gale | 推开和风区能防守球路，但较 Lou 的持续冰面更依赖技能时机；后续仍需补破门与持球推进。 |
| 不太合理 | Frank | 面对已知 Colette 的比例伤害与 8-Bit 阵地火力，直上身体容易送资源；Barley 不能单独补足进场与解控。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 7 行。

## 8. Hideout · Bounty · 第 5 手

己方：Max、Pierce；敌方：Charlie、Penny；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Jae-yong | 速度/治疗维持 Pierce 的长线换血，Max 提供同步接触；对 Charlie 有支援型回答边，Bounty 合同含保星和速度站位。 条件：Penny 溅射惩罚抱团，Charlie 茧不能简单用治疗解除；“限制一切投掷/狙击”超出证据。 |
| 合理，但是有改进空间 | Gus | 护盾可帮 Pierce 维持线权，也能远程补伤害；但不能持续提供 Jae-yong 的治疗/节奏循环，仍需分散躲 Penny 溅射。 |
| 不太合理 | Bull | 己方已有 Max 但没有持续治疗；Bull 贸然接近 Charlie/Penny 的茧、桶与火力会把保星局变为高风险突入。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 8 行。

## 9. Hard Rock Mine · Gem Grab · 第 2 手

己方：未选；敌方：Rico；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Stu | Rico 卡记录 Stu 可用破墙/机动否定弹墙角；Stu 边路机动把开出的空间转成矿区安全。 条件：需要 Breakthrough 分支且保留撤退墙；后续补 carrier/身体，不能开墙后没有远程接管。 |
| 对 | Ruffs | Rico 卡明确记录 Air Superiority 选择性开墙、同廊对线和补给强化；直接覆盖作者拆墙理由。 条件：只拆 Rico 核心反弹墙，队友需拾取补给并接管；不把 Ruffs 所有墙体一起拆掉。 |
| 合理，但是有改进空间 | Colt | 拆墙也能削 Rico 弹射，但持续命中与启动拆墙资源更吃操作，缺 Stu 的位移或 Ruffs 的团队增益。 |
| 不太合理 | Frank | 第二手用大身体正面走 Rico 墙线，既不能稳定消除弹墙角，又易让对手后续补反坦；接近方案没有成立。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 9 行。

## 10. Shooting Star · Bounty · 第 4 手

己方：Nori；敌方：Belle、Byron；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Piper | 开放图满距离爆发补 Nori 的接触/控制，Piper 对 Belle 和 Byron 都有狙击镜像条件边。 条件：Byron 治疗和第五/六手可改变交换；Piper 需侧路保护、满距角度和逃生资源。 |
| 合理，但是有改进空间 | Brock | 能补长线并选择性开墙，但对 Belle/Byron 的持续换血更依赖命中与站位；不如 Piper 的极长线方案直接。 |
| 不太合理 | Bull | Nori 已有接近潜力，再加短手会让 Belle/Byron 长期掌控开放线，缺少安全压低敌方血线的角色。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 10 行。

## 11. Pit Stop · Heist · 第 6 手

己方：Colt、Shade；敌方：Bull、Rico、Kit；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | R-T | Heist 合同明确分体防入库而非主打库；Colt/Shade 已承担开线与入库，R-T 留守可处理 Bull/Kit 接触。 条件：要保腿位、避免 Rico 免费弹墙处理；弱地图投影不应抹掉防守职责，R-T 优先于 Cordelius 的排序没有充分证据。 |
| 对 | Cordelius | 对 Bull 的领域/禁技边、Kit 卡的领域反制边支持拆开近战载体；Colt/Shade 继续给金库压力。 条件：开领域后自家金库剩余 2v2 必须能守，不能把隔离当作稳定打库 DPS。 |
| 合理，但是有改进空间 | Gale | 推离可延缓 Bull/Kit 入库，减轻 Colt/Shade 回防负担；仍需处理 Rico 火线和技能空档，缺少 R-T 的近距爆发或隔离。 |
| 不太合理 | Tick | 慢节奏远程消耗难在 Bull/Kit 到库时立刻止损，第三人仍未补上己方缺少的近区防守。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 11 行。

## 12. Ring of Fire · Hot Zone · 第 1 手

己方：未选；敌方：未选；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Colette | Push It 清出站区身体、削高血目标，为后续占区者创造窗口；是可延展首选职责。 条件：后续需站区者、反投掷和清召唤物；当前没有敌人，不声称已满足某个克制关系。 |
| 对 | Crow | Ring of Fire 草控、压回复和减速入口对应 Crow 的两条地图 hook。 条件：后续补真正占区者和清点；ban 未知意味着无法声称已排除所有狙击/突进回应。 |
| 对 | Finx | L 墙支援口袋和队友弹道增益可延长控圈，作为围绕 projectile 队友展开的首选计划成立。 条件：Finx 不能独自占圈；后续明确补身体/输出，其早手限制要求组队计划而非看到 strong 就锁定。 |
| 合理，但是有改进空间 | Pam | 有站圈和治疗底座，但固定治疗阵地容易被后续投掷、反治疗或长线压制；首抢的结构弹性需要再检验。 |
| 不太合理 | Mortis | 一抢暴露近身进场且不能稳定持续站圈；未知对手可补反突，后两手同时承担控区和掩护负担。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 12 行。

## 13. Shooting Star · Bounty · 第 2 手

己方：未选；敌方：Colette；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Pierce | 敌方 Colette 首选时可用长线慢速/壳循环维持拿星压力，下一手保留补保护空间。 条件：Colette 位移和后续刺客仍需回答；没有证据表明它必胜 Colette。 |
| 对 | Byron | 长线支援和治疗换血能构筑 Bounty 保星队伍，不必与 Colette 在近身反坦轴竞争。 条件：第二/三手需补可吃治疗的输出，不能单凭治疗当首杀工具。 |
| 对 | Belle | 开放射线的低承诺消耗、标记跟伤与陷阱撤退能建立拿星计划。 条件：保持距离并补反突/跟伤；不是以缺少反向边证明克制 Colette。 |
| 合理，但是有改进空间 | Brock | 保持长线而非再堆反坦，方向成立；但慢弹道和保命压力使对枪稳定性与后续保护要求更高。 |
| 不太合理 | Frank | 主动送出高血身体给 Colette，在开阔图又缺接近工具；无法把耐久转换为保星优势。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 13 行。

## 14. Hard Rock Mine · Gem Grab · 第 6 手

己方：Chester、Gus；敌方：Crow、Ruffs、Sandy；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Sirius | 影子税与护送路线对应矿区；Gus 可承担保护、Chester 惩罚近身，使影子压力有队友承接。 条件：Sandy 范围清理及敌方扫草会削弱收益，影子应分散且不能捡宝石；必须保留真实持宝人。 |
| 合理，但是有改进空间 | Jessie | 炮台能争矿区并增加敌方处理资源的成本；但需要充能、安全炮位，Sandy 的范围压力会削弱固定阵地。 |
| 不太合理 | Mortis | 第三人继续接触切入而缺稳定矿区资源；Crow 拉扯、Ruffs 沙包及 Sandy 范围伤害会使入场和撤退更难。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 14 行。

## 15. Shooting Star · Bounty · 第 6 手

己方：Belle、Gray；敌方：Pierce、Mortis、Leon；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Fang | 已有 Belle/Gray 的长线，Fang 可补近身反刺客；明确对 Mortis 的 Roundhouse/Corn-Fu 回答边支持保护己方后排，亦能威胁 Pierce。 条件：要安全攒 Super 并追踪 Leon/Fang 落点，不能将鞋子当主狙击或为追 Pierce 放弃保星。 |
| 合理，但是有改进空间 | Gale | 能给 Belle/Gray 反突保护，处理 Mortis 的接近；但很难同时威胁远端 Pierce，胜利路径更依赖两名队友对枪。 |
| 不太合理 | Tick | 面对 Mortis/Leon 再补需保护的脆后排，会让反突缺口更大；墙控无法代替近身处置。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 15 行。

## 16. Pinhole Punt · Brawl Ball · 第 3 手

己方：Nita；敌方：Crow；已知禁用：Otis、Colette。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Poco | Poco 对 Crow 的状态净化边直接存在；Nita 提供近区接触和熊资源，治疗/净化可维持足球推进。 条件：Crow 在净化用尽后仍能反治疗；尚需 scorer/射门窗口，不把被 ban 的 Colette/Otis 当已选队友。 |
| 合理，但是有改进空间 | Gale | 可帮助 Nita 防守球路、推走接触者，但不提供 Poco 的续航，球队连续推进与熊资源持续作战会更吃紧。 |
| 不太合理 | Piper | 在已有 Nita、对方 Crow 的阶段补慢装填长线，不能直接延长推进和身体控球窗口；墙草接触仍需另找解法。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 16 行。

## 17. Undermine · Gem Grab · 第 6 手

己方：Chester、Otis；敌方：Stu、Amber、Nita；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Lumi | Gem 合同的召回穿墙、退线 slow/root 能从草墙边改变矿区角度；Nita 卡含 Lumi 的清熊/墙压回答边。 条件：Chester/Otis 与 Lumi 要明确中路拾宝和侧路分工；Amber 烧草、Stu 机动会减值，root 不阻止攻击。 |
| 合理，但是有改进空间 | Barley | 能补墙后铺地和矿区封路，但面对 Stu 的机动和 Amber 改地形较依赖保护；缺 Lumi 的召回路径控制与爆发。 |
| 不太合理 | Piper | 单发长线受 Nita 熊和草墙角度消耗，无法稳定补全 Chester/Otis 缺少的绕墙控矿。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 17 行。

## 18. Hot Potato · Heist · 第 1 手

己方：未选；敌方：未选；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Colette | Heist 特殊目标伤害与往返 Super 打库给出直接目标转化，Hot Potato 边路赢线后可获得直线访问。 条件：必须开出 Super 路径并安全充能；投影缺 hook 不等于没有 Heist 工作。 |
| 对 | Crow | 草带探测、压回复和守入口帮助后续主 DPS 获得金库访问，可作为控线首选。 条件：现有 index 只支持辅助控制/防守，不能将历史选项解释为当前唯一主打库或无限 Hyper 输出。 |
| 合理，但是有改进空间 | Barley | 有持续墙后打库与守路能力，但首手暴露后需要队友处理突进和拆墙，不能默认安全持续输出。 |
| 不太合理 | Poco | 先手投入治疗却没有已定进库伙伴，自身目标输出不足；后两手要同时补打库与访问路线，结构负担大。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 18 行。

## 19. Dueling Beetles · Hot Zone · 第 2 手

己方：未选；敌方：Lou；已知禁用：Colette、Crow、Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Frank | 明确反向边 Lou→Frank 同时记有 Active Noise Canceling 例外；免控进区加高血身体、队友跟伤能构成条件方案。 条件：Colette/Crow 被 ban 只减少部分反制；不能说 Frank 无条件克 Lou，必须追踪免控与 Lou 冰面资源。 |
| 对 | Stu | Lou 卡明确机动横移能妨碍连续 Frost 命中；Speed Zone 回区与机动争点符合地图任务。 条件：窄口被迫踩冰仍会失败，后续队友补占区/清点；只躲弹不等于计分。 |
| 合理，但是有改进空间 | Pam | 可补身体与治疗让争圈不易断档，但固定站位容易给 Lou 积累冻结；治疗不能消除控制，需队友另开入口。 |
| 不太合理 | Tick | 慢节奏墙后消耗不能直接处理 Lou 的进圈控制，持续站圈仍依赖后两人，容易让对方保持先占优势。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 19 行。

## 20. Belle's Rock · Knockout · 第 2 手

己方：未选；敌方：Najia；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Edgar | Najia 卡明示 Edgar 可惩罚其低爆发；Belle's Rock 墙袋提供跳入路线，作为针对已暴露后排的早期计划成立。 条件：仅第二手，必须留队友回答后续反突；Super 启动、落地、逃生需成立，不能按无保镖的最终阵容计算。 |
| 对 | Mortis | 越障/长 dash 与墙后低爆发目标相接，Najia 对刺客/高速路线的失败条件支持低成本接触的方向。 条件：早手 KO 风险被卡片明确提示；必须规划后续反控制/压血。支持有风险的方案，不支持“安全必选”。 |
| 对 | Byron | 地图侧线和开墙后长线可供治疗消耗；Najia 卡也把 sustain 记为毒伤无法转化的机制，后续配可靠输出即可构筑回合优势。 条件：完整墙袋可能堵治疗和输出，需侧线/开墙计划及保镖；当下不能保证单独压过 Najia。 |
| 对 | Belle | KO 的低承诺消耗、标记和末圈陷阱与侧线/未来开墙结构相容，可保留远程配队路线。 条件：没有 Belle 直接克 Najia 的边；不能站在封闭墙袋正面期待射线穿墙，后续补开角/反突。 |
| 合理，但是有改进空间 | Brock | 开墙与远程压力可以改变 Najia 的墙袋收益，但可能同时牺牲己方后续接近路线；慢弹道与自保需队友支持。 |
| 不太合理 | Frank | 在淘汰赛早早暴露慢速身体，面对 Najia 墙后区域又缺已有接近工具；容易被消耗后再遭后手针对。 |

正确分支超过单次题卡容量，分批轮换；不删除未展示的正确答案。

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 20 行。

## 21. Ring of Fire · Hot Zone · 禁用题

己方：未选；敌方：未选；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Mortis | 作为禁用可移除切圈外支援/投掷的能力，保护己方准备围绕墙袋控圈的方案。 条件：这是可成立的假设首选计划，不冒充题面已选英雄；不是要求 Mortis 自己长期站圈。 |
| 对 | Edgar | 禁掉跳入清圈/贴脸控制位，能降低己方区域核心被越过正面防线的风险。 条件：需要明确自己准备抢的区域核心；地图弱投影不能推出无禁用价值。 |
| 对 | Stu | 机动换角与反复争圈能拆固定射线/冰面计划，ban 可以保护己方定点控区。 条件：应说明准备保护哪个入口计划；这不证明 Stu 是普遍最高 ban。 |
| 对 | Ruffs | Air Superiority 处理圈旁墙袋、补给强化敌方占区者，会改变己方围绕 L 墙的优势，作为预防性 ban 可成立。 条件：仅在己方依赖该地形/站区资源差时有意义；Ruffs 本人不是占区身体。 |
| 对 | Leon | 草/隐蔽与 Lollipop 改变进圈信息差，可威胁己方圈边后排；移除此路线有明确地图收益。 条件：如果己方已有充分探草，ban 边际价值下降；不强行替作者补一个唯一预选。 |
| 对 | Lumi | 区口 slow/root 与墙边召回能延迟己方回区、压制圈边站位，ban 可保护稳定重进场。 条件：冰面只有局部短窗口，不能把它写成永久封整圈；需要配合己方方案衡量。 |
| 合理，但是有改进空间 | Piper | 若准备短手站圈体系，禁远端点射有一定保护价值；但她本身站圈弱，通常不如先消除直接破坏核心进区的回应。 |
| 不太合理 | Tick | 未有墙后消耗威胁的具体计划时，优先禁掉难持续站圈的 Tick，仍留下突进、拆墙和反站圈回应，禁用收益不足。 |

正确分支超过单次题卡容量，分批轮换；不删除未展示的正确答案。

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 21 行。

## 22. Shooting Star · Bounty · 禁用题

己方：未选；敌方：未选；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Pierce | 禁止对手首选长线压制/减速与资源循环，减少末选方承受的开局火力压力。 条件：稳定狙击仍能对付 Pierce；合理 ban 不等于无反制或环境第一。 |
| 对 | Gene | 移除长线 poke、治疗/视野支援和抓高价值目标能力，能保护后续拿星阵容。 条件：需要抓人跟伤且怕更长狙；ban 判断不能套其 slot_6 的选人规则。 |
| 对 | Najia | 少量墙袋允许越墙投毒限制狙击安全位；ban 可排除这条条件反狙/退线压力路线。 条件：Shooting Star 开墙后毒弹易空且低爆发；只支持墙体保留分支，不支持纯开放图普遍强势。 |
| 合理，但是有改进空间 | Brock | 减少远程拆墙压力有价值，但未必优先于更稳定的首抢长线/抓人资源，取决于己方准备保留的末手路线。 |
| 不太合理 | Bull | 在开放赏金图把禁用花在无已知接近支援的短手，难以压低对方安全首抢的上限。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 22 行。

## 23. Safe Zone · Heist · 禁用题

己方：未选；敌方：未选；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Otis | 沉默近身入库路线会关闭己方可能的进场打库计划，因此 ban 有针对性防守价值。 条件：若己方拟走远程打库，该禁用收益下降；题目未指定唯一预选。 |
| 对 | Belle | 长线标记、入口陷阱和拥挤多目标换血会妨碍入库与输出搭档，禁用可保护己方进攻路线。 条件：Belle 非主打库，且投影 weak；合理的克制型 ban 不依赖把她判断成地图全能强势。 |
| 对 | Chuck | 布站提供有预算的打库突破和强制回防任务，移除此特殊访问路线可简化防守。 条件：当前卡是有限充能/命中补充的版本；旧分析的“长期路线压力”不能自动解释成无限自动循环。 |
| 合理，但是有改进空间 | Colt | 减少持续打库与开线威胁合理，但己方是首抢方，也可能自己拿下；需要解释为何禁优于抢。 |
| 不太合理 | Poco | 只为减少治疗而禁用，没针对长线金库访问、重复入库或反突窗口；机会成本高。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 23 行。

## 24. Belle's Rock · Knockout · 第 1 手

己方：未选；敌方：未选；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Gene | 墙后 Magic Hand 抓出安全口袋加探测，为 KO 首杀建立后续补爆发的方案。 条件：需选能接伤害的队友并防召唤物挡手；拉中不自动完成首杀。 |
| 对 | Najia | 地图明确存在棋盘墙袋和缩圈前固定入口，越墙毒区可安全压缩空间。 条件：后续必须补反突与终结；Damian 被 ban 不代表所有刺客已被限制。 |
| 对 | Pierce | 利用可用长线压血和 Super 收束，为墙图中的路线控制提供一种可延展远程核心。 条件：对墙控/召唤物和刺客需补答案；不是覆盖全部墙袋的无条件首选。 |
| 合理，但是有改进空间 | Brock | 能先建立长线并改变墙形，但早拆墙会影响后续队友选择，需处理慢弹道与侧路接近风险。 |
| 不太合理 | Frank | 淘汰赛首手暴露大身体和启动过程，没有已定保护或接近协同，对方有充分空间补远程和控制。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 24 行。

## 25. Goldarm Gulch · Knockout · 第 2 手

己方：未选；敌方：Pierce；已知禁用：Damian、Gene、Najia。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Belle | Goldarm Gulch 明确有双侧长射线；Belle 的 poke/标记给队友创造第一杀，与被禁掉的其他远程选项相容。 条件：需要保护侧草和缩圈撤退；纯地图字符串未匹配 hook 不应阻止此路线被考虑。 |
| 对 | Byron | 双侧长线可让 Byron 治疗核心并维持 KO 血量领先，避开与 Pierce 壳循环持续硬换。 条件：后续必须有吃治疗的输出/反突，不能隔中央墙治疗；不是证明单挑克 Pierce。 |
| 合理，但是有改进空间 | Ruffs | 沙包/增益能改变 Pierce 的弹药交换并支持后续队友，但自身长线对压有限，缩圈和侧草还需补保护。 |
| 不太合理 | Frank | 直接把大身体送进 Pierce 的直线弹药循环，未建立穿越开放线与侧草的接近方案。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 25 行。

## 26. Belle's Rock · Knockout · 第 6 手

己方：Spike、R-T；敌方：Gene、Rico、Pierce；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Sprout | 敌方 Rico/Pierce 均有被 Sprout 墙控干扰的边；Spike/R-T 补入口保护，墙袋投掷能制造首杀。 条件：Gene 拉人是明确反向证据；保留深口袋、挡手/压 Gene 充能，不能写成敌方完全无答案。 |
| 对 | Ziggy | 延迟落雷/风暴压退线和墙角，R-T/Spike 保护与跟伤可将逼位转为回合收益。 条件：需要固定退路与预判，Gene 拉人/开阔横移会削弱；不是稳定硬控。 |
| 对 | Grom | 地图墙簇和窄口限制横移，Grom 十字投掷压路；R-T/Spike 保护入口，KO 首杀链成立。 条件：需安全口袋和跟伤，Gene 的抓人威胁仍要处理，不能因无刺客就任意站位。 |
| 合理，但是有改进空间 | Tick | 有越墙和逼位能力，R-T 可护近身；但慢爆炸给机动和绕线更多时间，Gene 拉人后保命依然困难。 |
| 不太合理 | Piper | 继续以单发直线对抗 Gene/Rico/Pierce 的墙线，没利用己方已有防守去补墙后压制，资源容易被地形吃掉。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 26 行。

## 27. Dueling Beetles · Hot Zone · 第 1 手

己方：未选；敌方：未选；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Crow | 压回复与入口减速妨碍单圈重进场，为后续占区者争时间。 条件：必须有实际站圈身体和墙后答案，首选时属于可继续补齐的计划。 |
| 对 | Colette | 百分比削前排和 Push It 推离计分区，直接覆盖进圈身体争夺。 条件：需要队友站圈、清资源和反投掷，不能独自承担整个目标合同。 |
| 对 | Finx | 卡明确提供 Hot Zone 弹道减速/装填税和站圈支援，封闭入口可让后续射手/身体吃到收益。 条件：后续确立 projectile 队友并防近身/召唤物；当前地图投影 weak 是漏匹配而非否定支援机制。 |
| 合理，但是有改进空间 | Pam | 治疗阵地和身体能帮第一次进圈，但被反治疗/投掷回应后较难重开，后两手需承担清场和进区。 |
| 不太合理 | Mortis | 首抢把阵容押在近身击杀，缺持续占区且容易被反突回应，无法独立建立第一波进圈条件。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 27 行。

## 28. Open Business · Hot Zone · 第 2 手

己方：未选；敌方：Finx；已知禁用：Damian、Crow、Colette。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Emz | Finx 卡明确列 lingering area/墙压会绕过弹道场优势；Emz 入口喷雾和范围减速转成站圈窗口。 条件：先到安全喷雾边缘，后续处理投掷和远程，不在贴脸死角接战。 |
| 对 | Otis | 沉默、清圈与入口封锁可在后续组队中为占区提供防守层，满足地图目标的一种响应。 条件：当前 Finx 不是已暴露近战；不能写成 Otis 硬克 Finx，仍须补占区/反墙控。 |
| 对 | Chester | 墙旁中距离多铃爆发与随机 Super 入口惩罚，为队伍提供 Finx 弹道支援之外的接触威胁。 条件：预热和 Super 类型不保证；后续补实际占区者/远程。 |
| 对 | Lou | 单圈 Super 覆盖与冻结将目标停留转为己方计分机会，可围绕控区展开。 条件：不宣称弹道完全不受 Finx 影响；需队友站圈/击杀并回答墙后攻击。 |
| 对 | Stu | 机动换角、重复争点与墙侧接近能绕开固定弹道场交易，保留灵活的后续占区组合。 条件：不能独自长时间站圈，Finx 的队友后续控制仍可能限制 dash。 |
| 对 | Lumi | 区边墙角召回、局部 slow/root 给固定入口另一种控制轴；Lumi 被 Finx 压制边也保留墙角回收的失效例外。 条件：避免在无遮挡射线硬打 Finx；只在有视野、短召回和队友跟伤的角度成立。 |
| 合理，但是有改进空间 | Pam | 补治疗和身体有进区价值，但固定阵地容易被 Finx 的区域节奏牵制，需要后续队友解决入口和伤害。 |
| 不太合理 | Tick | 再加慢节奏外围消耗，很难迫使 Finx 让出圈内位置，且把站圈和防近身同时留给后两人。 |

正确分支超过单次题卡容量，分批轮换；不删除未展示的正确答案。

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 28 行。

## 29. Ring of Fire · Hot Zone · 第 6 手

己方：Lou、Byron；敌方：Stu、Leon、Pam；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Draco | Lou 控制、Byron 治疗已有，Draco 正好提供实际 zone body；对 Stu 的窄口近战交换有直接边。 条件：需 Super/Last Stand、治疗线和形态启动，敌方 Leon 绕后或 Pam 拖长交换不可忽略。 |
| 合理，但是有改进空间 | Buster | 护盾和身体能承接 Byron 治疗，配 Lou 争入口；但盾的方向/空档明显，面对 Stu/Leon 绕角难稳定替代 Draco 承压。 |
| 不太合理 | Tick | Lou/Byron 已有控制与续航，再补外围消耗仍没人把资源变成圈内身体，Leon 还会施加侧切压力。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 29 行。

## 30. Shooting Star · Bounty · 第 1 手

己方：未选；敌方：未选；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Gene | 长线 poke、抓人和支援可组成带跟伤的首选方案；地图仍留少量掩体可蓄资源。 条件：index 明确警告 Shooting Star 易被长狙压制，因此只是有风险的可选方案，不能推导为安全最优一抢。 |
| 对 | Pierce | 开放可见路线可产生拿星压力和末发减速，后续补保护使壳循环有机会启动。 条件：其纯开放狙击镜像劣势仍成立；选它不意味着无需回答更稳定长手。 |
| 对 | Najia | 地图保留的小墙袋与 Najia 的越墙毒区合同可组成条件反狙路线，给队友终结机会。 条件：开墙与高速横移会失效，早手需规划反突；这里支持残墙分支而非把整张图当墙图。 |
| 合理，但是有改进空间 | Brock | 长线和选择性拆墙能形成常规保星路线，但弹道命中和侧翼保护成本更高，需谨慎规划后两手。 |
| 不太合理 | Bull | 开放赏金图第一手没有接近搭档或已知可惩罚目标，耐久不能自动转换为拿星和撤退。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 30 行。

## 31. Shooting Star · Bounty · 第 2 手

己方：未选；敌方：Angelo；已知禁用：Gene、Pierce、Najia、Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Byron | 以治疗维持队友长线输出，给 Angelo 蓄力交换制造持续成本，属于组合响应而非对枪必赢。 条件：Angelo→Byron 是明确优势边；需安全角和搭档补伤，不能让 Byron 独自接蓄满箭。 |
| 对 | Belle | 稳定 poke/标记和队友跟伤可以在 Angelo 蓄力期间建立压力，符合地图长线职责。 条件：Angelo→Belle 优势边成立；第二手仅保留组队路线，不能称其硬反 Angelo。 |
| 对 | Gus | 护盾、伤害增益和长线 chip 为搭档制造首杀或保星交换，满足对 Angelo 的资源响应方向。 条件：必须由后续输出利用护盾，注意穿线与充灵体的安全；不能只按名义射程排序。 |
| 合理，但是有改进空间 | Brock | 能保持长线并逼 Angelo 调整角度，但慢弹道对高机动目标较不稳定，且不提供治疗或护盾换血。 |
| 不太合理 | Frank | 无支援大身体跨开放线容易给 Angelo 蓄力命中，既无可靠贴近也难保星。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 31 行。

## 32. Hideout · Bounty · 第 5 手

己方：Gene、Byron；敌方：Belle、Nani；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Mortis | Hideout 中央墙草给接触路线，Gene/Byron 提供压血、抓人和治疗；可针对 Belle/Nani 的后排窗口。 条件：Nani 卡有反 Mortis 预判爆发边，必须用草墙/已交资源例外；敌方第六手仍可补守卫。 |
| 合理，但是有改进空间 | Gray | 传送能制造接近角度，也保留远程功能；但 Gene/Byron 已有长线辅助，仍需明确谁负责贴近终结。 |
| 不太合理 | Poco | 再补治疗难迫使 Belle/Nani 离开安全射线，Gene/Byron 的低接触阵容仍缺把资源转为击杀的手段。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 32 行。

## 33. Kaboom Canyon · Heist · 第 1 手

己方：未选；敌方：未选；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Colt | 开阔长线持续打库与选择性破墙直接兑现 Heist 目标，符合地图主线。 条件：必须命中和有反突保护，不能为开墙帮敌方建立更强射线。 |
| 对 | Colette | 安全充 Super 后直线往返打库，对特殊目标高伤是明确合同。 条件：路径/充能/落点受控会失败；后续要开线和保护。 |
| 对 | Crow | 中草探测与持续压回复帮助后续 DPS 打到金库，能先建立控线和防入库层。 条件：不能当唯一 safe DPS；作者只给名字，不补造历史 Hyper 的数值理由。 |
| 合理，但是有改进空间 | Brock | 开线和远程打库有价值，但持续目标输出与命中要求使其更像线权组件，后续还需补主输出与守草。 |
| 不太合理 | Poco | 首抢治疗缺少已定进库身体和目标输出，开放金库路线不易靠治疗本身转换优势。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 33 行。

## 34. Safe Zone · Heist · 第 2 手

己方：未选；敌方：Angelo；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Chuck | 用布站和有预算的 Super 把射线对枪改为金库访问，Angelo 只占一个长线位时保留该进攻方向合理。 条件：不是无限循环：当前卡限制充能池，需布站成本、过河/墙路线与终点安全；原分析“补充充能”必须按实际命中条件解释。 |
| 合理，但是有改进空间 | Colt | 持续打库与开线能争 race，但仍要经过 Angelo 控制的射线；较 Chuck 的重复路线方案更依赖对枪命中。 |
| 不太合理 | Poco | 对 Angelo 长线和金库目标都没有直接处理手段，先投入治疗会让后续同时补访问、输出和防守。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 34 行。

## 35. Hot Potato · Heist · 第 6 手

己方：Spike、Otis；敌方：Rico、Nita、Carl；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Shade | 墙草与侧路可转为入库，Spike/Otis 已提供防接触，Shade 的特殊路线和对 Carl 的墙压边提供进攻补位。 条件：Rico 弹墙、Nita 熊与 Carl 进场仍能限制启动/落点；须保证短手真正打到库，不是仅仅跨过地形。 |
| 合理，但是有改进空间 | Barley | 补墙后输出和打库方向合理，但 Carl 接近与 Rico 绕角可压缩安全炮位，需 Spike/Otis 额外回防。 |
| 不太合理 | Poco | Spike/Otis 已能拖延近身，继续补续航却没有新增可靠进库或墙后压力，容易丢失打库节奏。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 35 行。

## 36. Double Swoosh · Gem Grab · 第 3 手

己方：Sandy；敌方：Colette；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Crow | Crow→Colette 的毒伤/反治疗惩罚方向存在，草路显形配合 Sandy 争矿区和撤退线。 条件：Sandy 与 Crow 的对敌关系不能当队内相克；后续需要实际 carrier/输出，毒伤不自动收割。 |
| 合理，但是有改进空间 | Bo | 探草和地雷可支援 Sandy 的侧路空间，但缺 Crow 持续压回复，地雷启动和命中也更受预判限制。 |
| 不太合理 | Frank | 给敌方 Colette 明确的高血目标，Sandy 不能独自消除比例削血与未定后手控制，接触成本偏高。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 36 行。

## 37. Hard Rock Mine · Gem Grab · 第 6 手

己方：Rico、Chester；敌方：Ruffs、Gene、Shade；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Edgar | 地图侧草/墙和跳入追宝合同能让 Rico/Chester 的压力转为针对 Ruffs/Gene 后排的接触窗口。 条件：Gene 击退、Ruffs 沙包与 Shade 特殊位移都需先消耗；完成阵容还要指定安全拾宝人，不能让 Edgar 裸当稳定中路。 |
| 对 | Bull | 侧草高血近身压力与护送/追宝职责，可配 Rico 走廊火力和 Chester 接触爆发逼退敌方中路。 条件：需处理 Gene 推退和 Shade 墙内窗口、保护实际持宝者；强行直线冲进去不成立。 |
| 合理，但是有改进空间 | Darryl | 能补身体与接近威胁，但滚动终点仍可能遭 Gene 击退、Shade 控制和 Ruffs 资源层；需先逼出关键技能。 |
| 不太合理 | Tick | Rico/Chester 已有固定区域压力，再加脆投掷难主动改变对方站位，还会给 Shade 更多近身目标。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 37 行。

## 38. Undermine · Gem Grab · 第 4 手

己方：Crow；敌方：Pierce、Otis；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Charlie | Spiders 的 shot tank/bush scout 与 Pierce 的 spawnable ammo waste 失败模式可直接组合；茧承担载体/反进场移除。 条件：无需新增 Charlie→Pierce 答案边；Otis 不一定同样被蜘蛛克制，下一手补输出/拾宝且避免茧被溅射提前打破。 |
| 合理，但是有改进空间 | Jessie | 炮台能消耗 Pierce 弹药并争区域，但必须先充能、找到安全炮位；没有 Charlie 直接放蜘蛛的即时资源窗口。 |
| 不太合理 | Frank | 大身体正面走 Pierce 火线，又面对 Otis 的沉默，难把血量转成矿区推进。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 38 行。

## 39. Triple Dribble · Brawl Ball · 第 1 手

己方：未选；敌方：未选；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Colette | 足球合同明确清守门、反高血持球者和推离得分线，为首选后的破门/scorer 创造窗口。 条件：后续必须处理门前墙和投掷/召唤物；目前只支持一个可完成的首选计划。 |
| 合理，但是有改进空间 | Gale | 推离和球路防守稳定，但首手后仍要补开门与得分，持续削高血身体不如 Colette 路线直接。 |
| 不太合理 | Tick | 首抢薄身慢节奏投掷，控球、反推进与破门负担都交给后两手，易被对方主动切入。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 39 行。

## 40. Pinhole Punt · Brawl Ball · 第 5 手

己方：Lumi、Kaze；敌方：Edgar、Amber；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Chester | 对 Edgar 的高铃/控制反进场边明确，Lumi/Kaze 提供角度和切入，Chester 补球路接触惩罚。 条件：保高铃/匹配 Super；Amber 持续消耗与末手长线仍须防。 |
| 对 | Otis | Edgar 卡明确被 Otis 沉默关闭贴脸；足球合同的断连招/控球路补 Lumi/Kaze 的防守。 条件：Amber 烧草会削弱草锚 hook，不能只依赖草；进球转换由队友承担。 |
| 合理，但是有改进空间 | Gale | 能帮助处理 Edgar 贴近并稳住球权，但持续终结与对 Amber 的压迫更弱，需 Lumi/Kaze 完成击杀转进球。 |
| 不太合理 | Tick | 面对 Edgar 和 Amber 再加需要保护的投掷，Lumi/Kaze 的切入资源会被迫回防，球权缺口扩大。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 40 行。

## 41. Center Stage · Brawl Ball · 第 6 手

己方：Chester、Najia；敌方：Kenji、Poco、Nita；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 合理，但是有改进空间 | Gale | 能推开 Kenji/熊并帮 Chester/Najia 争球权，但缺少直接拆门与突入终结；仍需把防守收益转成进球。 |
| 不太合理 | Piper | 面对 Kenji/Poco/Nita 的身体、续航和熊，再加单发远程容易被资源层与接近压垮，球路防守也吃紧。 |
| 待复核，不强行分档 | Shade | 穿墙接近、近身得分压力有正向机制，Chester/Najia 可提供爆发和毒区。 但敌方 Kenji 有越墙 Super、Nita 有熊/反突、Poco 有续航，直接触发 Shade 依赖的墙内安全/短手交易疑点。index 尚缺这一完整对局如何压过清场与续航的具体闭环，不能直接套“敌方无答案”。 |
| 待复核，不强行分档 | Bull | 作者限熟练度；Bull→Poco 的路线贴脸边与破门/自传球合同支持一种进攻替代，Chester/Najia 提供跟伤。 必须保留熟练度条件；Nita→Bull 反突边要求骗熊/换角，Kenji 与 Poco 的续航会延长交换，并非无条件优于 Shade。；玩家前提：作者说熟练使用时也可奏效 |

**暂不开放抽题：原答案尚无充分支持的分支。**

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 41 行。

## 42. Belle's Rock · Knockout · 第 1 手

己方：未选；敌方：未选；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Gene | 墙袋抓人、探草与后续爆发伙伴可形成 KO 首杀计划。 条件：拉中后要能杀且防召唤物挡手；本题名单未含 Najia 不代表排斥所有其他答案。 |
| 对 | Pierce | 长线 chip/末发减速与资源准备后的 Super 可为墙图提供远程首杀压力。 条件：后续处理墙控/突进、保护空弹；不把地图 strong 当免疫克制。 |
| 合理，但是有改进空间 | Brock | 能建立长线并选择性开墙，但首手后必须协调地形计划与侧翼保护，不能先拆掉潜在投掷队友的安全墙。 |
| 不太合理 | Frank | 第一手在淘汰赛给出明显可消耗和控制的大身体，对方仍有完整反制空间，己方未建立接近保障。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 42 行。

## 43. Hot Potato · Heist · 第 6 手

己方：Nita、Lumi；敌方：Berry、Emz、Rico；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Dynamike | 安全墙后攻击对付固定控制点并转金库爆发；Nita/Lumi 已给接触与路径限制，敌方当前无直接刺客。 条件：Satchel/Super 时机、Berry 范围互压和墙体变化需处理；不要为了开墙破坏自己的安全位。 |
| 对 | Barley | 持续投掷和 Heist Super 打库分支可从墙后处理敌方防守，Rico 卡有被 Barley 墙控的边。 条件：需要 Extra Noxious/安全投掷角，保护 Super 完整释放；Berry 镜像和 Emz 推进不等于免费优势。 |
| 合理，但是有改进空间 | Grom | 也能越墙处理 Berry/Emz/Rico，但落点节奏和近身自保较依赖队友，持续铺地或即时爆发的执行成本不同。 |
| 不太合理 | Piper | 直线单发难处理这组墙后持续压力，Nita/Lumi 已有接触，缺口是越墙清守卫而非再补对枪。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 43 行。

## 44. Layer Cake · Bounty · 第 5 手

己方：Belle、Colette；敌方：Gus、Penny；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 合理，但是有改进空间 | Gale | 可防末手近身并保护 Belle，但对 Gus/Penny 的长线和炮位压迫有限，且仍未解决敌方可能补投掷的情况。 |
| 不太合理 | Frank | 己方已有 Colette 的身体约束，再补容易被长线消耗的大身体，未建立接近 Gus/Penny 或清炮位的路径。 |
| 待复核，不强行分档 | Chester | Belle 提供长线，Chester 的中近爆发能防对方最后手近战；泛化防守补位有根据。 作者关键前提“Colette 限制敌方投掷，抢余下反坦”没有充分支撑；Colette 卡反而警告墙控/召唤物稀释。Layer Cake 依赖墙，最终队伍如何防敌方投掷仍未闭合。 |
| 待复核，不强行分档 | Otis | 沉默/持续输出可补长线阵容的单点防守，Bounty 合同支持保星跟伤。 Otis 自身也要求反投掷/开墙，不能靠同样怕墙控的 Colette 直接宣布封掉敌方投掷；需要具体构筑/可达性或原视频上下文。 |

**暂不开放抽题：原答案尚无充分支持的分支。**

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 44 行。

## 45. Double Swoosh · Gem Grab · 第 2 手

己方：未选；敌方：Crow；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Chester | 草路的多铃接触与矿区护卫能构筑应对 Crow 探测的范围压力，后续补 carrier/长线。 条件：不声称硬克 Crow；先探明路线再近身，避免被持续显形后远端磨血。 |
| 对 | Lumi | 召回穿墙与退线控制可借地图草墙改换攻击角度，避免只与 Crow 站开放线互耗。 条件：Lumi 卡明确怕 Crow 毒伤；其例外是墙角短召回/队友视野控制，需依该分支而非忽略负边。 |
| 合理，但是有改进空间 | Bo | 探草和地雷能建立侧路信息与入口压力，但不直接解决 Crow 拉扯，需要后续队友完成携宝和终结。 |
| 不太合理 | Poco | 第二手只用续航回应 Crow 反治疗而未定推进伙伴，净化窗口外仍受压，团队接触和输出都尚未闭合。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 45 行。

## 46. Layer Cake · Bounty · 第 6 手

己方：Gus、Kaze；敌方：Juju、Belle、Chester；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Ziggy | Layer Cake 的层级窄口限制横移，Ziggy 延迟落雷逼退，Gus 护盾与 Kaze 侧压帮助拿星/保星。 条件：必须预判退路并保护本体，Juju 资源与 Chester 近身不可无视；index 弱投影遗漏了明确的 choke 连接。 |
| 合理，但是有改进空间 | Barley | 墙后持续铺地可配 Gus/Kaze 逼位，但对 Juju 的角度与地形选择需额外处理，不能只靠投掷标签判优。 |
| 不太合理 | Bull | Gus/Kaze 已有保护和侧切，再加短手要经过 Juju/Belle/Chester 的区域与近距惩罚，缺安全接近路径。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 46 行。

## 47. Ring of Fire · Hot Zone · 第 5 手

己方：Lou、Leon；敌方：Pierce、Lumi；已知禁用：Damian。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 合理，但是有改进空间 | Pam | 能补 Lou/Leon 缺的站圈和治疗，但固定站位容易被 Pierce 长线与 Lumi 锤路压制，需要先争安全阵地。 |
| 不太合理 | Tick | 第三人再做外围消耗，Lou/Leon 仍缺持续占区承接，对方 Pierce/Lumi 可继续控制入口。 |
| 待复核，不强行分档 | Edgar | 跳入 Pierce 空弹或 Lumi 布锤窗口有方向，Lou 控制/Leon 同步能帮助清圈。 己方最终 Lou/Leon/Edgar 的持续占区和再入场成本没有充分闭环，各卡都向队友索取 body/保护；对手还有第六手反突。支持清场候选，暂不足以完整支持该补位。 |
| 待复核，不强行分档 | Alli | 草路追猎半血目标与 Lou/Leon 压血可联成清理窗口。 同样缺最终持续占区安排；Alli 明确需要压血来源且不能清满血 sustain body，敌方第六手未定。不能把进场成功等于赢计分。 |

**暂不开放抽题：原答案尚无充分支持的分支。**

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 47 行。

## 48. Hard Rock Mine · Gem Grab · 第 1 手

己方：未选；敌方：未选；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Sirius | 矿区影子护送与侧草资源压力能先确定一种后续补 carrier/清场保护的结构。 条件：其 slot_1 明确不宜无条件先手，故只支持有后续应对 splash/pierce 的计划，不支持安全无脑首选。 |
| 对 | Najia | 矿区入口/墙角毒区给队友争收宝和退线，地图提供了明确固定接触路径。 条件：后续须补保镖、终结和实际 carrier，未知 bans 不证明刺客池已受限。 |
| 对 | Colette | 反高血护送与应急拾宝合同，可在草路接触地图作为后续补 carrier 的前排约束手。 条件：不是默认 carrier；缺敌方时只支持开放的反身体计划，后续需清资源/墙控。 |
| 合理，但是有改进空间 | Bo | 可用探草与地雷争矿区，功能完整但启动和命中较依赖预判，后续仍需补稳定持宝与接触处理。 |
| 不太合理 | Bull | 首手暴露近身计划且无已定接近支援，容易被后续反坦/控制限制，矿区中路职责也没有解决。 |
| 待复核，不强行分档 | Edgar | 地图侧草与跳入追宝给出后手惩罚路线，但无法独立解释当前裸一抢。 slot_1 仅允许“明确奖励 Brawl Ball scorer 且高优先反制已 ban”的例外；本题是 Gem Grab 且 bans 未知，投影却 early_pick=true。要核早手规则/版本/作者条件。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 48 行。

## 49. Double Swoosh · Gem Grab · 第 5 手

己方：Lumi、Sirius；敌方：Mortis、Sandy；已知禁用：Najia、Colette、Lola。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Nita | 有 Nita 对 Mortis/Sandy 的条件边，Bruce/Bear Paws 与穿透保护 Lumi/Sirius 的资源展开并争草路。 条件：无熊期与第六手清召唤物是代价；实际持宝和熊/影子分散仍要安排。 |
| 对 | Emz | 宽喷雾与区域慢速惩罚 Sandy 草路，Sirius 资源掩护可使 Emz 不孤立，帮助保护矿区。 条件：Mortis→Emz 优势边不可删除；必须保 Friendzoner/队友资源守近身，而非声称 Emz 单人硬克 Mortis。 |
| 合理，但是有改进空间 | Gale | 能推开 Mortis 并守资源展开窗口，但对 Sandy 隐蔽与持续矿区压迫的处理仍需队友，自己不替代携宝安排。 |
| 不太合理 | Tick | 已有 Lumi/Sirius 需要时间展开资源，再补被 Mortis 追切的脆后排会进一步拉大近身保护负担。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 49 行。

## 50. Dueling Beetles · Hot Zone · 第 6 手

己方：Bull、Emz；敌方：Lumi、Juju、Chester；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Gray | Bull 的身体和 Emz 的清圈已齐，Gray 传送补进区路线；Juju 卡有被 Gray 传送/接近回答的边。 条件：出口避开 Lumi/Chester 的预封，门启动需保护；不把 Gray→Emz 对敌边误当队内协同证据。 |
| 合理，但是有改进空间 | Max | 加速可帮助 Bull/Emz 争入口，方向合理；但仍须穿过 Lumi/Juju/Chester 的实际火力区，不能像 Gray 一样改变进场位置。 |
| 不太合理 | Piper | 外围点射无法补 Bull/Emz 的低成本进区，现有身体和区域输出仍卡在敌方控制的入口。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 50 行。

## 51. Kaboom Canyon · Heist · 第 1 手

己方：未选；敌方：未选；已知禁用：Najia。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Crow | 中心草探测/压回复帮助后续真正 safe DPS 获得射线，ban Najia 减少一个墙角压力来源。 条件：仅支持控制型首选，不推导当前必然最高伤害/唯一最优；仍补 DPS 与反突。 |
| 合理，但是有改进空间 | Brock | 长线开墙和打库可以形成目标贡献，但中心草与持续输出仍要队友承接，不能单靠开墙赢 race。 |
| 不太合理 | Poco | 未有已选打库身体就先投入治疗，在开放金库图难独立建立线权或目标输出。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 51 行。

## 52. Pinhole Punt · Brawl Ball · 第 5 手

己方：Chester、Max；敌方：Poco、Meeple；已知禁用：Najia。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Kenji | Kenji→Poco 的近身资源战边明确，Max 加速和 Chester 跟伤帮助足球推进、清守门与得分。 条件：Meeple 的陷阱/控制和末手反突要追踪，Kenji 回返位置需安全；弱投影不应盖过这些机制。 |
| 合理，但是有改进空间 | Bibi | 可借 Max 加速接触并推开防守，但启动和击退时机更受 Meeple 控制影响，需 Chester 跟伤才容易转成进球。 |
| 不太合理 | Tick | Chester/Max 的接触速度难被慢节奏投掷转为球路推进，Poco 可重置消耗，Meeple 又能限制位置。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 52 行。

## 53. Shooting Star · Bounty · 第 6 手

己方：Tick、R-T；敌方：Gray、Pierce、Byron；已知禁用：Najia。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Nani | Tick 墙控/R-T 近身守路已有，Nani 补超远收束爆发和 Peep 开角；Gray 卡有被 Nani 长线爆发回答的方向。 条件：Gray 传送可改角，Pierce/Byron 不会静止接满伤；控制 Peep 时保护本体。 |
| 合理，但是有改进空间 | Brock | 能补长线和开角，但终结 Byron 治疗线下的目标较依赖连续命中，需 Tick/R-T 创造输出窗口。 |
| 不太合理 | Bull | 己方已有 R-T 防近身，补短手仍无法触及 Gray/Pierce/Byron 的安全长线，Tick 的压制缺少远程终结。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 53 行。

## 54. Ring of Fire · Hot Zone · 第 1 手

己方：未选；敌方：未选；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Finx | L 墙支援与弹道场可作为围绕后续射手/占区身体构筑的单圈开局。 条件：需要把支援转为计分；敌方近身/召唤物分支仍需后续回答。 |
| 对 | Lou | 单圈 Super 控区、冻结与削输出直接创造踩区窗口，适合随后补身体/击杀。 条件：Lou 不是独自长期站圈的全能答案；防远端投掷、净化与长线。 |
| 对 | Crow | 持续草区显形、压回复和减速回区直接对应地图入口安全。 条件：后续补真正占区/范围清点，未知 bans 不保证安全。 |
| 合理，但是有改进空间 | Pam | 先抢站圈与治疗有结构价值，但固定阵地容易被后手压回复或越墙，应保留重开入口的搭档。 |
| 不太合理 | Mortis | 首抢押近身击杀，无法稳定占区且给对方反突回应空间，需要后两人承担过多目标职责。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 54 行。

## 55. Hard Rock Mine · Gem Grab · 第 6 手

己方：Chester、Ruffs；敌方：Rico、Max、Lily；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Shade | 墙路/虚体避正面射线并威胁敌方矿区，Chester 近战惩罚和 Ruffs 增益为启动提供支撑。 条件：敌方 Max/Lily 可换角，Rico 可守出墙；作者“无法应对”只能读为缺便宜稳定答案。Ruffs 选择性开墙不能拆掉 Shade 路线。 |
| 合理，但是有改进空间 | Darryl | 能形成接近和身体压力，但面对 Rico/Max/Lily 的机动与爆发，滚动终点更容易暴露，缺 Shade 的墙路窗口。 |
| 不太合理 | Tick | Rico/Max/Lily 能持续逼近或改角，新增脆投掷迫使 Chester/Ruffs 回防，难把已有资源转成主动压迫。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 55 行。

## 56. Belle's Rock · Knockout · 第 6 手

己方：Gus、Tick；敌方：Kit、Mortis、Angelo；已知禁用：未提供。

| 提议评价 | 选项 | 解释与边界 |
|---|---|---|
| 对 | Bull | Kit 与 Mortis 卡都记录被 Bull 近身身体/爆发惩罚，能保护 Gus/Tick 墙后输出并把防切转为 KO 生存。 条件：不要为了追 Angelo 离开后排；保留草墙，冲锋不免伤。 |
| 对 | Darryl | 双霰弹近身接触、保护性进场和回合路线控制可给 Gus/Tick 提供身体，并威胁被墙控限制的后排。 条件：需守好 Mortis/Kit 接近终点再择机滚入，不把滚动当任意无伤开团；保留队友接应。 |
| 合理，但是有改进空间 | Gale | 推开 Mortis/Kit 可保护 Gus/Tick，但爆发收口和持续身体挡位有限，技能空档要更谨慎防二次切入。 |
| 不太合理 | Piper | 再补需要保护的单发远程会让 Kit/Mortis 的切后排收益扩大，Gus/Tick 仍缺近身终结与挡位。 |

依据：[原题与既有分析](../analysis/QUESTION-BANK.md)；[原答案索引审计](../analysis/bp-index-audit-2026-09-20/REPORT.md)；新增方案对应 `index-evidence.jsonl` 第 56 行。
