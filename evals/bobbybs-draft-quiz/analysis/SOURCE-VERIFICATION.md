# 第二轮核源：直接画面检查

2026-09-18。本轮回看原视频，使用播放后的真实视频帧、内嵌文字、英雄头像和本地头像资源对照；保存截图与文件哈希。**没有独立完成原声听辨**，自动字幕继续作为次级证据。已排除播放器未解码时显示的封面，未把封面或评论当作题目时间帧。

原来 17 道隔离题中，**16 道已解除原字段疑点**。普通开发输入由 39 增至 **55 题（52 单手选人 + 3 禁用）**。第 2 题确认是 4/5 连选组合，另存 `inputs.paired-review.jsonl`，暂不混入单手命中率；小 ban 图标还有待辨认。正式 gold 仍为 0：本轮不等于所有字段、历史补丁与当前版本答案的全面验收。

[完整字段审计](source-verification-v2.json) · [题库索引](QUESTION-BANK.md) · [证据哈希](evidence-manifest.json)

## 逐项结果

| 题号 | 核验结论 | 直接证据 |
|---|---|---|
| 1 | 补齐敌方 Amber、Carl、Otis；完整二友三敌状态支持第六手。补认 Shade、Rico bans | [20s 阵容与 ban](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-20-q1.png) |
| 2 | 己方 Gus，敌方 Piper/Wendy，处于 4/5 连选。参考为 Sprout + R-T 或 Sprout + Pearl；两手顺序不判错 | [51s 题面](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-51-q2.png)、[65s Sprout](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/JxRGZPCa8Us-65-q2-pair.png)；原字幕 49—64s 的配对口述 |
| 17 | 敌方确实是 Nita，保留原名 | [约44s 完整题面](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/c7C6B5cjD9o-43-q3.png) |
| 18、19、20 | Easy 全片 ban 为 Damian，字幕 Dynamike 错误 | [5.5s 头像](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/ZdWs3kiDrJ8-5.50-ban.png) |
| 20 | 敌方首选为 Najia，修正 Nita | [31.12s 题面](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/ZdWs3kiDrJ8-31.12-q3-Najia.png) |
| 22 | 禁用参考第三名为 Najia | [29.4s 三名答案](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/8CGXicuVjbs-29.4-q2-answer.png) |
| 24 | 首选参考中的 Nita 改为 Najia | [11s NAJIA 文字与头像](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/qajAIs6gTLM-11-q1-answer.png) |
| 25 | 题内 ban 为 Gene、Najia，加全片 Damian | [17s NAJIA 文字与灰色头像](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/qajAIs6gTLM-17-q2-bans.png) |
| 30、31、32 | Bounty 全片 ban 为 Damian，字幕 Dynamike 错误 | [2.6s 头像](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/5HP07EygUio-2.60-ban.png) |
| 31 | 题内第三个 ban 为 Najia | [16s NAJIA 文字与禁用栏](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/5HP07EygUio-16-q2-bans.png) |
| 35 | 敌方确实是 Nita，保留原名 | [约29s 完整题面](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/m4P2v_NfmlY-29-q3.png) |
| 49 | 作者接受 Nita / Emz，保留 Nita；另补回字幕遗漏的 Najia、Colette、Lola bans | [29.5s 答案与禁用栏](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/StONtQp8uZ4-29.5-q2-answer.png) |
| 51、52、53 | 全片 Nija ban 确认为 Najia | [5s Najia 头像](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/uw_BQfFSFZY-5-ban.png) |
| 52 | Meepo 确认为 Meeple | [23s 完整题面](../../../raw/sources/bobbybs-draft-quiz/visual-evidence/uw_BQfFSFZY-23-q2.png) |

截图中的页面可能含推荐视频，但核验只使用当前播放器内题面。文件名时间是请求定位时间，实际观察时间写在审计中；第 17、35 题截图捕获时仍在播放，分别约 44、29 秒，不将其声称为逐帧精确时间。

## 尚未确认的内容

- Viewer 第 1 题额外橙色护目镜 ban 小 pin 尚未可靠匹配；已识别 Gus、Shade、Rico。它可在**部分 bans 已知**的条件下开发试跑，不能声称还原了全部禁用。
- Viewer 第 2 题除 Shade 外的三个不同 ban 小 pin 尚未逐一取得可靠实体对应。已保存完整画面；没有把先后猜测直接写进状态。组合参考已清楚，恢复此题正式评分还需要组合评分器与禁用复核。
- 没有核实每条视频的确切发布日期、对应补丁、所有构筑，以及全部 56 题的每个画面字段。当前清除的是本次列出的阻断问题。
- 知识库的机制分析不是原作者逐字解释。第 20 题已随 Nita→Najia 重写；第 1 题补入完整对手风险；第 49 题禁止把已 ban 的 Lola 等当可用后续回应。

## 复现与数据版本

- 当前：`cases.calibrated.jsonl`、`inputs.calibrated-dev.jsonl`、`inputs.paired-review.jsonl`。
- 核源前分析版保存在 `archive/analysis-v1-*`；最初字幕版与原始字幕保持不变。
- `source-verification-v2.json` 记录 27 条字段更新/确认，含原值、新值、截图、时间点和依据。值未变化的 Nita 确认也保留，避免以后被全局替换。
- 执行 `python evals/bobbybs-draft-quiz/tools/validate_analysis.py` 检查数量、已知合法性、模型输入隔离、知识/字幕/截图哈希与链接。该验证不运行模型、不证明策略最优。
