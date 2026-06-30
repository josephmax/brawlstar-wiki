# 英雄 BP 建模质量审计

状态：`quality_gate_audit`。生成日期：2026-06-30。

本页由 `tools/audit_bp_profile_quality.py` 根据 [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]] 生成。它只审计结构和明显占位符，不替代人工机制复核。

## 汇总

- 审计英雄数：104
- 当前状态 `bp_ready`：26
- 当前状态 `draft_from_raw_signals`：75
- 当前状态 `reviewed`：3
- 可直接升级 reviewed：0
- 可直接升级 bp_ready：0

## 阻塞类型统计

- `auto_placeholder`：75
- `missing_map_route_or_objective`：75
- `source_traceability_gap`：45
- `missing_failure_modes`：40
- `missing_map_hooks`：17

## 英雄队列

| brawler | current_status | blocker_count | blocker_types | next action |
| --- | --- | ---: | --- | --- |
| [[entities/brawlers/Jae-yong|Jae-yong]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Lily|Lily]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Mandy|Mandy]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Meg|Meg]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Melodie|Melodie]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Mina|Mina]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Mortis|Mortis]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Rosa|Rosa]] | `draft_from_raw_signals` | 15 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/8-Bit|8-Bit]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Bo|Bo]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Bolt|Bolt]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Bonnie|Bonnie]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Buzz|Buzz]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Carl|Carl]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Colette|Colette]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Finx|Finx]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Gale|Gale]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Hank|Hank]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Janet|Janet]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Jessie|Jessie]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Kaze|Kaze]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Kenji|Kenji]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Lola|Lola]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Lou|Lou]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Lumi|Lumi]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Maisie|Maisie]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Mr. P|Mr. P]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Ollie|Ollie]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Pam|Pam]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Pearl|Pearl]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Penny|Penny]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Shelly|Shelly]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Squeak|Squeak]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Starr Nova|Starr Nova]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Willow|Willow]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Ziggy|Ziggy]] | `draft_from_raw_signals` | 14 | `auto_placeholder`, `missing_failure_modes`, `missing_map_hooks`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Alli|Alli]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_failure_modes`, `missing_map_route_or_objective` | review_and_fix_blockers |
| [[entities/brawlers/Amber|Amber]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Barley|Barley]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
| [[entities/brawlers/Bea|Bea]] | `draft_from_raw_signals` | 13 | `auto_placeholder`, `missing_map_route_or_objective`, `source_traceability_gap` | review_and_fix_blockers |
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
| [[entities/brawlers/Angelo|Angelo]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Ash|Ash]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Belle|Belle]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Bibi|Bibi]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Brock|Brock]] | `reviewed` | 0 | none | needs_reviewed_edges_and_ranked_map_hooks_for_bp_ready |
| [[entities/brawlers/Buster|Buster]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Charlie|Charlie]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Chuck|Chuck]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Clancy|Clancy]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Colt|Colt]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Cordelius|Cordelius]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Crow|Crow]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Darryl|Darryl]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Doug|Doug]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Draco|Draco]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Emz|Emz]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Gene|Gene]] | `reviewed` | 0 | none | needs_reviewed_edges_and_ranked_map_hooks_for_bp_ready |
| [[entities/brawlers/Gigi|Gigi]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Gus|Gus]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Max|Max]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Mico|Mico]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Nita|Nita]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Otis|Otis]] | `reviewed` | 0 | none | needs_reviewed_edges_and_ranked_map_hooks_for_bp_ready |
| [[entities/brawlers/Poco|Poco]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Rico|Rico]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Sam|Sam]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Sandy|Sandy]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Shade|Shade]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |
| [[entities/brawlers/Stu|Stu]] | `bp_ready` | 0 | none | bp_ready_structural_gate_passed |

## 关联页面

- [[syntheses/英雄BP建模质量门槛|英雄 BP 建模质量门槛]]
- [[syntheses/英雄BP建模执行状态|英雄 BP 建模执行状态]]
- [[syntheses/BP-条件化对位边索引|BP 条件化对位边索引]]
- [[syntheses/BP-英雄地图特征适配索引|BP 英雄地图特征适配索引]]
