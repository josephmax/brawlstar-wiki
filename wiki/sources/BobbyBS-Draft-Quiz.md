---
title: BobbyBS Draft Quiz 专家题库
type: source
status: development_reference
created: 2026-09-18
updated: 2026-09-20
tags:
  - wiki/source/bp-evaluation
---

# BobbyBS Draft Quiz 专家题库

作者频道：[bobby - brawl stars](https://www.youtube.com/@bobbybrawlstars/shorts)。2026-09-18 实际采集 19 条相关视频、56 道题；最新 Viewer Edition 两题，其余每片三题。确切发布日期/补丁尚未确认；不保证删除、私密或其他平台内容的全覆盖。

## 来源与可追溯性

- [原始采集清单与哈希](../../raw/sources/bobbybs-draft-quiz/capture-manifest.json)：19 份英文自动字幕与 15 张已采用的实际视频证据帧。
- [视频与 case 清单](../../evals/bobbybs-draft-quiz/manifest.json)：逐视频 URL、稳定 ID、题号映射与覆盖边界。
- [逐题核源与截图](../../evals/bobbybs-draft-quiz/analysis/SOURCE-VERIFICATION.md)：27 条字段确认/修正；以画面、内嵌文字和头像为依据，未独立完成原声听辨。
- [题库与考点索引](../../evals/bobbybs-draft-quiz/analysis/QUESTION-BANK.md)：56 题状态、作者参考、分析推断和局限。
- [2026-09-20 BP-index 全量充分性审计](../../evals/bobbybs-draft-quiz/analysis/bp-index-audit-2026-09-20/REPORT.md)：56 题、115 个候选记录、114 个方案（双选按组合，Bull 保留熟练度条件）；逐项保留支持链、失败条件、index 证据和源字段对照。

## 当前可用范围

55 道普通开发题（52 单手选人 + 3 禁用），第 2 题为 4/5 连选组合，另列探索输入。原 17 道隔离题中 16 道解除主要疑点；Viewer 两题仍有少量 ban 小 pin 未可靠识别。全量正式 gold 为 0，未运行模型基线。

这是历史专家接受集合及机制审题材料，不是当前版本唯一正确答案。作者标签、实际玩家选择、分析者推导和后续专家复核分开；反事实不自动增加真值样本。名字按 [[concepts/英雄名称归一化|英雄名称归一化]] 校准，Nita/Najia 冲突逐字段核验，不作全局替换。

2026-09-20 审阅使用覆盖全部题目地图的默认 35 图 index：51 题可组成合理主观方案；第 41/44/47 题缺关键闭环，第 4/48 题的部分选项与选位规则有张力。另有 29 个候选记录在对应选位桶缺失，加敌方关系查询仍缺 25 个；能力窗口等额外召回不在这两个探针内，不能视为生产 Agent 准确率。Jev 所用 S49 快照缺 3 张题目地图（影响 5 题）。本轮未改标答/机制，未新增视听核验，gold 仍为 0；已知答案审阅存在事后解释风险。

## 维护与隔离

后续[决策路径审计](../../evals/bobbybs-draft-quiz/analysis/decision-path-audit-2026-09-20/REPORT.md)专门检查“能否进入比较”：第六手 27 个参考候选记录有 7 个不在地图桶，桶+关系按 32 条预算漏 13 个；能力窗口可分别救回。确认地图资格、阈值、排序预算、关系方向存在过早排除路径；文本层还缺清楚的第六手团队增益优先规则。未将工具探针当模型最终选人结果；先前 51/3/2 仅是充分性解释，不是机制通过率。

使用 [BP 题库维护 skill](../../skills/brawl-stars-bp-eval-maintenance/SKILL.md) 更新。题库/来源材料不能被 `compile` 或 `decide` 用于推荐；正式评测需隔离文件访问。[评分协议](../../evals/bobbybs-draft-quiz/analysis/EVALUATION-PROTOCOL.md) 区分作者一致性、机制正确性与有限候选集合的非劣解。

## 交互练习清洗稿（2026-09-20）

[逐题确认稿](../../evals/bobbybs-draft-quiz/practice/REVIEW.md) 补充 56 题共 112 个中间档/反面方案；新增等级均为维护者推断，不是 Bobby 新证言。保留原始参考名单与争议分支，第 41/44/47 题暂缓；53 题输出 56 个 3–5 选项的无标签变体。当前索引机制与原答案审计逐卡一致；结构校验通过，用户确认与隔离模型回归尚未完成。全部练习题仍未启用，不改变历史 gold 状态。

### 练习确认与后续

用户已确认清洗分档，`practice/approval.json` 绑定确认哈希，`practice/bank.json` 导出 53 题；其余 3 题暂缓。应用侧本地抽题/评分已实现。[模型自洽 TODO](../../evals/bobbybs-draft-quiz/practice/TODO.md) 按用户要求延期，没有真实模型准确率。
