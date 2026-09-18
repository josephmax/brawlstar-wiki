# 数据与评分契约

## 布局与路径

`raw/sources/<collection>/transcripts/` 与 `visual-evidence/` 是不可变来源层。`evals/<collection>/` 包含校准 case、输入、分析、审计与历史版本。`wiki/sources/<source>.md` 为该集合的来源入口。新增更强结论需要证据；不从题库直接晋升实体对位边。

JSON 中 `analysis.evidence[*].path` 和知识清单文件路径相对仓库根；case 的 `source.transcript`、审计的 `screenshot`、来源/图片哈希键相对集合目录。Markdown 链接相对当前文档。禁止开发机绝对路径。保存的知识哈希是当次分析快照；与当前文件不同须报告 drift，不能只更新哈希。

## case 的层次

- 身份：`id`、`video_id`、`question_index`、展示用 `ordinal`、`task`。
- `source`：URL、题面与答案时间点、字幕引用、采集日期；`published_at/patch` 未核实为 null。
- `input`：map、mode、pick_slot、allies、enemies、bans、ban_status；数组不暗示历史选取顺序。双选另外有 `decision_scope: paired_4_5` 与 `pick_slots: [4,5]`。
- `reference`：accepted、preferred、conditional、actual_player_pick、作者理由摘要。双选额外 `accepted_pairs`；名单不穷尽，条件解不按默认解评分。
- `calibration`：逐字段变化、field_checks、remaining_issues、完整视听验收标记。部分头像检查不将整题 `full_case_audiovisual_verified` 置 true。
- `analysis`：考点、机制链、逐题 rubric、错误示例、反事实及知识依据。都标为分析推断，不能写进作者理由。
- `scoring`：普通开发资格、双选探索资格、历史/当前版本轨道、gold/strict 标记。取消阻断需要依据；只有全部所需字段与适用版本通过对应专家审题，才允许正式评分升级。

普通输入仅导出局面白名单，prompt 由模板生成；不带来源、答案、分析、证据链接、来源校准备注或答案污染的 context。双选文件亦如此，但与普通输入分开。`provisional_enabled` 决定普通导出，带 unresolved issues 的题不得开启；paired exploratory 可保留明确缺口，不伪装为普通 gold。

## 分析更新

逐题解释“地图/路线 → 能力资源 → 队友分工/敌方回应 → 模式收益”。检查 Super 启动、构筑、落点、冷却、地形变化与未选完的对手。名字修正后重新阅读对应实体，不机械替换术语；ban 新增后检查首选合法性和反事实中的可用回应。

考点/rubric 是审题框架，不是额外专家标签。反事实必须随父题分组且由专家审订后才能成为 ground truth。历史作者一致性、机制正确性、当前版本策略质量分别报告。有限候选集内有证据的非劣解不等于全局游戏最优；未知维度应不可比，不计作零分。

已公开给开发者/本轮模型的题统一作开发回归。按视频及跨视频近重复分组，不能把同图同机制的十题当十份独立泛化证据。新的盲测必须封存未见资料；同仓保存时尤其要限制被测进程文件权限。

## 校验与提交

脚本检查：稳定 ID、数量与 manifest、canonical 实体、已知非法选择、组合合法性、输入白名单与确定性 prompt、原始哈希、知识快照 drift、Markdown 链接。`--strict-knowledge` 把当前知识漂移当失败；默认报告漂移仍保留历史依据。它不会理解全部自然语言机制，更不能证明答案/头像识别正确。

数量在 `manifest.json.analysis_revision` 及 evidence manifest 中同步；历史 caption-v1 数字只在明确标记的历史块保留。验证后人工浏览变动题面/标签/分析和 diff。提交只含授权题库、raw、来源页、索引/日志及 skill 路径；数据库脏状态另报。提交和推送需有用户授权，推送后核对远端 SHA，不把本地 commit 当远端交付。
