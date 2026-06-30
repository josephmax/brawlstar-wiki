# 英雄 BP 建模质量审计

状态：`quality_gate_audit`。生成日期：2026-06-30。

本页由 `tools/audit_bp_profile_quality.py` 根据 [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]] 生成。它只审计结构和明显占位符，不替代人工机制复核。

## 汇总

- 审计英雄数：104
- 当前状态 `bp_ready`：66
- 当前状态 `draft_from_raw_signals`：35
- 当前状态 `reviewed`：3
- 可直接升级 reviewed：0
- 可直接升级 bp_ready：0

## 阻塞类型统计

- `auto_placeholder`：35
- `missing_map_route_or_objective`：35
- `source_traceability_gap`：19
- `missing_failure_modes`：6
- `missing_map_hooks`：1

## 英雄队列

| brawler | current_status | blocker_count | blocker_types | next action |
| --- | --- | ---: | --- | --- |
| [[entities/brawlers/Byron|Byron]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Edgar|Edgar]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Eve|Eve]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Glowy|Glowy]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Gray|Gray]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Leon|Leon]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Moe|Moe]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Najia|Najia]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Nani|Nani]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Pierce|Pierce]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Piper|Piper]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/R-T|R-T]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Ruffs|Ruffs]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Sirius|Sirius]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Spike|Spike]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Sprout|Sprout]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Surge|Surge]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Tara|Tara]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Trunk|Trunk]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Berry|Berry]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Bull|Bull]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Chester|Chester]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Dynamike|Dynamike]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/El Primo|El Primo]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Fang|Fang]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Frank|Frank]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Jacky|Jacky]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Juju|Juju]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Kit|Kit]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Larry & Lawrie|Larry & Lawrie]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Meeple|Meeple]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Tick|Tick]] | `draft_from_raw_signals` | 12 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Damian|Damian]] | `draft_from_raw_signals` | 11 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Griff|Griff]] | `draft_from_raw_signals` | 11 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Grom|Grom]] | `draft_from_raw_signals` | 11 | `auto_placeholder`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/8-Bit|8-Bit]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Alli|Alli]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Amber|Amber]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Angelo|Angelo]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Ash|Ash]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Barley|Barley]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Bea|Bea]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Belle|Belle]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Bibi|Bibi]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Bo|Bo]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Bolt|Bolt]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Bonnie|Bonnie]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Brock|Brock]] | `reviewed` | 0 | none | needs_reviewed_edges_and_ranked_map_hooks_for_bp_ready |
| [[entities/brawlers/Buster|Buster]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Buzz|Buzz]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Carl|Carl]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Charlie|Charlie]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Chuck|Chuck]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Clancy|Clancy]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Colette|Colette]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Colt|Colt]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Cordelius|Cordelius]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Crow|Crow]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Darryl|Darryl]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Doug|Doug]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Draco|Draco]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Emz|Emz]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Finx|Finx]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Gale|Gale]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Gene|Gene]] | `reviewed` | 0 | none | needs_reviewed_edges_and_ranked_map_hooks_for_bp_ready |
| [[entities/brawlers/Gigi|Gigi]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Gus|Gus]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Hank|Hank]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Jae-yong|Jae-yong]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Janet|Janet]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Jessie|Jessie]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Kaze|Kaze]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Kenji|Kenji]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Lily|Lily]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Lola|Lola]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Lou|Lou]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Lumi|Lumi]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Maisie|Maisie]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Mandy|Mandy]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Max|Max]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Meg|Meg]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Melodie|Melodie]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Mico|Mico]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Mina|Mina]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Mortis|Mortis]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Mr. P|Mr. P]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Nita|Nita]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Ollie|Ollie]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Otis|Otis]] | `reviewed` | 0 | none | needs_reviewed_edges_and_ranked_map_hooks_for_bp_ready |
| [[entities/brawlers/Pam|Pam]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Pearl|Pearl]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Penny|Penny]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Poco|Poco]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Rico|Rico]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Rosa|Rosa]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Sam|Sam]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Sandy|Sandy]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Shade|Shade]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Shelly|Shelly]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Squeak|Squeak]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Starr Nova|Starr Nova]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Stu|Stu]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Willow|Willow]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Ziggy|Ziggy]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |

## 关联页面

- [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]]
- [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]
- [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]
- [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]
