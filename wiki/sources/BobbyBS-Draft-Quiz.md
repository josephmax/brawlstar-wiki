---
title: BobbyBS Draft Quiz 专家题库
type: source
status: development_reference
created: 2026-09-18
updated: 2026-09-18
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

## 当前可用范围

55 道普通开发题（52 单手选人 + 3 禁用），第 2 题为 4/5 连选组合，另列探索输入。原 17 道隔离题中 16 道解除主要疑点；Viewer 两题仍有少量 ban 小 pin 未可靠识别。全量正式 gold 为 0，未运行模型基线。

这是历史专家接受集合及机制审题材料，不是当前版本唯一正确答案。作者标签、实际玩家选择、分析者推导和后续专家复核分开；反事实不自动增加真值样本。名字按 [[concepts/英雄名称归一化|英雄名称归一化]] 校准，Nita/Najia 冲突逐字段核验，不作全局替换。

## 维护与隔离

使用 [BP 题库维护 skill](../../skills/brawl-stars-bp-eval-maintenance/SKILL.md) 更新。题库/来源材料不能被 `compile` 或 `decide` 用于推荐；正式评测需隔离文件访问。[评分协议](../../evals/bobbybs-draft-quiz/analysis/EVALUATION-PROTOCOL.md) 区分作者一致性、机制正确性与有限候选集合的非劣解。
