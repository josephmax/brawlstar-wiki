# BobbyBS Draft Quiz 测评候选集

> **交互练习已确认（2026-09-20）：** [53 题练习导出与使用契约](practice/README.md)。用户确认前述分档，3 题暂缓；应用本地已接入抽题答题。BP skill 自洽回归按用户要求列为 [TODO](practice/TODO.md)，没有模型成绩。下方待确认段落保留为前一轮记录。

> **交互练习清洗稿（2026-09-20，待确认）：** [56 题逐题分档与补充选项](practice/REVIEW.md)；[数据、隔离回归及抽题契约](practice/README.md)。补充 112 个选项提案，53 题形成 56 个无标签题卡变体；第 41/44/47 题暂缓。新增等级未获用户确认、未通过真实模型回归，全部未启用。

本集合的唯一维护源现为本知识库仓。原始字幕/截图位于 `../../raw/sources/bobbybs-draft-quiz/`；当前机器清单中的知识路径相对仓库根，来源/截图路径相对集合目录，Markdown 链接相对当前文件。历史归档保留旧布局语义，不作运行输入。

[维护 skill](../../skills/brawl-stars-bp-eval-maintenance/SKILL.md) · [来源页](../../wiki/sources/BobbyBS-Draft-Quiz.md)

> **决策路径补审：** [现有机制是否会过早排除答案](analysis/decision-path-audit-2026-09-20/REPORT.md)。56 题实跑 784 次查询：第六手 18 题/27 个参考候选中，7 个不在地图桶；桶+敌方关系按 32 条预算漏 13 个。预设能力窗口可分别召回全部参考项，故问题是入口/阈值/排序/团队价值判断的组合，不能宣称工具全局禁止。上一轮 51/3/2 是解释充分性，**不是现行流程选出率**。本轮没有模型端到端成绩，未改决策规则。

> **2026-09-20 index 充分性审计：** [全量 56 题报告](analysis/bp-index-audit-2026-09-20/REPORT.md)。按主观方案可辩护标准，51 题成立、3 题部分成立、2 题的部分选项存在规则张力；115 个候选记录中 29 个未进入对应地图选位桶。附逐候选证据、反证、哈希与查询复现。此为已知答案的维护审阅，不是盲测或 Jev 准确率；题面、作者标签和 gold 状态未改。

> **2026-09-18 分析版已完成：** [56 题逐题考点](analysis/QUESTION-BANK.md)、[整体发现与改进方案](analysis/FINDINGS.md)、[评分协议](analysis/EVALUATION-PROTOCOL.md)。
>
> **第二轮核源：** [直接画面结果与证据截图](analysis/SOURCE-VERIFICATION.md)。原 17 题中 16 题解除阻断，第 2 题改为双选组合并单独导出。
>
> 当前使用 `cases.calibrated.jsonl` 与 `inputs.calibrated-dev.jsonl`：55 题普通开发输入，1 题单列双选复核，正式 gold 仍为 0。全部 56 题均有分析；部分名称/地图经过画面核对，其余推断和疑点明确分开。尚未运行模型基线，未修改知识库或 BP skill。
>
> 下文、`CASES.md`、`cases.jsonl`、`inputs.provisional.jsonl` 的 37/19 数字保留为**采集 v1 历史记录**，不代表本次校准结果。原始 case 另存于 `archive/cases.caption-v1.jsonl`。完整字段审计与知识文件哈希见 `analysis/`。

2026-09-18 从 [Bobby 的 Shorts 频道](https://www.youtube.com/@bobbybrawlstars/shorts)采集了 19 条相关视频，按局面拆成 56 个 case：53 个选人、3 个禁用。最新 Viewer Edition 有两题，其余每条三题。

这是**可追溯的候选数据集**，尚未成为逐题视听复核后的 gold benchmark。37 题可做字幕提取版初步试跑；19 题存在明确疑点，默认排除。没有运行模型测评，也未验证作者历史答案在当前补丁下是否仍然成立。

## 文件

- [CASES.md](CASES.md)：供人工浏览的逐题表，链接跳到题目时间。
- [manifest.json](manifest.json)：19 条视频清单、稳定视频 ID、采集范围与数量。
- [cases.jsonl](cases.jsonl)：56 题完整标注，包含局面、作者答案、时间点、理由与待复核事项；仅供维护者/评分者读取。
- [inputs.provisional.jsonl](inputs.provisional.jsonl)：37 道初步试跑输入，不含作者答案、原视频链接或提取备注。只把其中 `prompt` 发送给被测模型。
- `../../raw/sources/bobbybs-draft-quiz/transcripts/<video-id>.txt`：19 份带时间戳的英文自动字幕；保留原文，不覆盖自动识别错误。

## 采集边界

按频道 Latest Shorts 顺序查找 Draft Quiz、Can you Draft 与 Viewer Edition，向前读到 `02w4WJrpZOg`，后续可见内容已转为更早的普通精彩集锦。19 条是本次实际观察到的系列集合。未声称已覆盖删除、私密、其他平台独占或未以相同标题发布的视频；确切发布日期与游戏补丁尚未提取，保持 null。不要用相对发布时间猜补丁。

同名视频按 video ID 区分；一期多题按 `video-id + question_index` 区分。当前按用户要求持久化于知识库的独立 evals 层，禁止被 BP runtime 召回；不写进英雄/地图实体。

## 输入与标签约定

`allies/enemies` 仅表示当前已选集合，数组次序不代表历史选择顺序。部分位次由已知人数推定；4/5 连选只测下一手，不强制提供两手答案。空数组应结合 review 检查：信息缺失的 viewer 题已排除，不能当成敌方确实没有英雄。

禁用只记录明确提及的部分，`not_provided` 不等于无 ban。自动字幕中 `Dynamike/Damian`、`Nija` 等疑点不擅自归一化；受其全片条件影响的题目一并排除。常见简称如 RT、Cord、Daryl 规范为 R-T、Cordelius、Darryl，备注中保留提取背景。

`reference.accepted` 是作者当期接受的答案集合，不是穷尽所有合理选项。`conditional` 保留依赖熟练度等条件的候选。最新 viewer 题的实际玩家选择单独写在 `actual_player_pick`，不会自动作为参考答案。作者未解释理由的题目保留空 reasoning，不能由整理者补写后冒充作者观点。

## 初步使用与评分

1. 从 `inputs.provisional.jsonl` 逐行建立独立对话，只发送 `prompt`。禁止向被测模型提供 `cases.jsonl`、字幕、CASES 表或视频链接。若 Agent 有任意本地文件读取权限，需在运行环境中移除整个评测目录的读取权限；仅拆文件不能完全防止泄题。
2. 保留模型/provider、知识版本、调用时间、原始输出与工具轨迹。模型回答需明确首选及最多两个备选，不接受罗列所有英雄。
3. 分别统计首选命中率与 Top-3 命中率，选人/ban 分开报告。某题首选规范化后属于 `accepted` 计命中；Top-3 为最多三个候选中至少一个命中。分母仅为本次选定且成功获得输出的题数，同时另报运行失败率，不能把失败题静默删除。
4. 另外统计选择合法性：不得选已禁用/已选英雄。理由仅对作者有明确解释的题目做人工语义检查，检查是否识别同一局面约束，不能按文字相似度打分。
5. 没命中作者名单的合理替代解标为待专家复核，不直接宣称策略错误。历史作者一致性与当前补丁实战质量分开评估；当前能力评估还需固定补丁/地图池并重新审题。

`provisional_enabled` 只代表可试跑，不代表 gold。全部 `gold_enabled` 当前为 false。发布正式分数前，逐题用画面/听音核对双方英雄、地图、位次、ban、答案及配装条件，并记录证据时间，修正疑点后再升级。19 条字幕的完整采集不等同于 56 题的完整标注验收。
