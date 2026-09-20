---
name: brawl-stars-bp-eval-maintenance
description: 采集、核验和更新荒野乱斗 BP 专家题库，校准视频中的英雄/地图/ban，拆解考点并维护无答案输入、证据与评分边界。用于题库维护和核源；不用于现场 BP 决策或自动修改英雄对位结论。
---

# BP 专家题库维护

维护者入口，与 `brawl-stars-bp-slot-decision` 并列存放。先读仓库 `AGENTS.md`、`wiki/index.md` 和目标题库 README。默认维护 `evals/bobbybs-draft-quiz/`；其他来源使用独立集合目录和稳定 ID。

## 维护边界

- `raw/sources/<collection>/` 保存原始字幕、抓取件、实际视频证据帧和来源清单；原文不被校准结果覆盖。
- `wiki/sources/` 记录来源身份、覆盖与局限；`evals/<collection>/` 保存题目状态、作者标签、分析推断、校准审计、评分协议与干净输入。
- 题库属于维护/评分层。`compile`、`decide` 不读取题库、字幕、截图、作者答案或本 skill。正式测评需隔离被测进程的文件读取权限；同仓存放不构成访问控制。
- 英雄名字以 `wiki/concepts/英雄名称归一化.md` 为唯一别名索引。合法名字也可能被转写成另一个合法英雄；只保存具体字段的纠错，不复制一份全局别名表。
- 作者接受名单不是穷尽最优解，知识库推导不是作者原话，派生反事实不是新增专家真值。确切日期/补丁未知就保留 null。

## 交互练习

维护已确认的三档练习数据或导出应用题库时，读 [练习契约](references/practice-contract.md)。确认记录、导出哈希和未解分支留在知识层；应用负责题序与用户作答。不要把练习标签提供给 BP decide。

## 工作方式

采集或补题时读 [采集与核源](references/acquisition-and-verification.md)。先按 video ID 去重，保留范围边界，再把每题拆成独立局面。画面未提供的字段不通过“BP 应该如此”补齐。优先核验可同时影响多题的全片 ban；再核单题身份和位次。

整理与纠错时读 [数据与评分契约](references/dataset-contract.md)。修改 `cases.calibrated.jsonl` 时同步字段审计、逐题分析和证据清单；Nita/Najia 这类修正必须检查机制链是否随身份改变。保留此前版本，避免将修正后的状态倒写为原字幕。

输入由确定性脚本从局面白名单生成，不复制维护侧 `prompt/context` 自由文本：

```bash
python3 skills/brawl-stars-bp-eval-maintenance/scripts/dataset.py export-inputs \
  --dataset evals/bobbybs-draft-quiz
python3 skills/brawl-stars-bp-eval-maintenance/scripts/dataset.py validate \
  --dataset evals/bobbybs-draft-quiz --strict-knowledge
```

`export-inputs` 只生成普通与双选输入，不改作者标签、证据哈希、纳入资格或 gold 状态。双选按无序组合另列，禁止混入单手命中率。数量或知识哈希变化必须审阅原因，不能靠重写预期值让校验通过。

知识随时间变化时，默认校验报告 drift；发布当前机制分析前用 `--strict-knowledge` 并复核变更实体。保存旧快照哈希/版本，不静默把新知识标成旧依据。数据完整性通过不等于游戏策略或模型基线通过。

完成后更新来源页、题库索引和 `wiki/log.md`。记录新增、修正、隔离、解禁、仍缺证据的数量及哪些能力实际验证。用户要求提交/推送时，先读 git 状态、核对远端，仅 stage 本次路径；已有数据库/其他修改不混入，不 force push。普通“更新题库”请求本身不授权额外发布。
