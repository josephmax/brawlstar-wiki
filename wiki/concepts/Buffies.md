# Buffies

社区俗称：芭菲（中文社区音译，指 Brawler 的 Buffied 强化条目，不是英雄名）。

## 系统规则

- Buffie 是加在单个能力条目上的强化层，覆盖三类槽位：`Gadget`（每个 Gadget 一条）、`Star Power`（每个 Star Power 一条）、`Hypercharge`（每条 Hypercharge 一条）。Fandom 英雄页用 `{{Buffie|Gadget}}`、`{{Buffie|Star}}`、`{{Buffie|Hyper}}` 模板标记每个 Buffied 条目。
- Buffied 效果改变的是既有能力的数值或行为（伤害倍率、额外弹体、冷却行为、附加减速/护盾/治疗等），不引入新的可交互实体类别；同一个 Brawler 的不同能力可各自拥有 Buffie。
- Buffied 数值随平衡补丁独立变动（例：2026-08-04 维护中 Griff Buffied Piggy Bank 爆炸半径 25%→30%、Max Buffied Phase Shifter 第二段窗口 3s→2s、8-Bit Buffied Plugged In 队友加速 15%→10%），必须与基础能力数值分开追踪。
- 获取与升级路径未在本库来源覆盖内，不写入稳定事实。

## 本库建模边界

- Buffied 效果只有改变能力语义（命中可靠性、控制窗口、资源生成、减伤/护盾变体、地形交互）时才折叠进 `wiki/entities/brawlers/` 的 `capability_vector` / `build_switches` / `failure_modes` 等稳定字段；纯数值变化走来源层 manifest 与断点审计。
- 断点审计（`combat_breakpoint_profile`）里，Buffied 防御变体用独立 `loadout_group`（现有先例 `star_buffie`，见 Bibi / Max），遵循 `wiki/concepts/伤害与生存断点` 的加法与互斥规则。
- Buffie 的上线波次是来源层清单（见 [[sources/Fandom-Release-Notes-June-2026|Release Notes June 2026]]：Rico、Brock、8-Bit、Meg、Max、Surge；[[sources/Fandom-Release-Notes-August-2026|Release Notes August 2026]]：Poco、El Primo、Amber、Gus、Chuck、Shade），不是 runtime 强度信号；runtime 只消费英雄页编译结果。
- Buffied 条目不构成独立的 `conditional_matchups` 目标或 tier 依据。

## 关联页面

- [[concepts/Gears|Gears]]
- [[concepts/伤害与生存断点|伤害与生存断点]]
- [[sources/Fandom-Release-Notes-June-2026|Fandom 来源摘要: Release Notes June 2026]]
- [[sources/Fandom-Release-Notes-August-2026|Fandom 来源摘要: Release Notes August 2026]]
