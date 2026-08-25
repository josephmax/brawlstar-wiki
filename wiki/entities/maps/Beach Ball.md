# Beach Ball

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Beach_Ball
- 来源：[[sources/Fandom-Beach-Ball|Fandom 来源摘要: Beach Ball]]
- 当前赛季索引：[[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-08-21

## BP-ready map_profile

```yaml
map_profile:
  name: Beach Ball
  mode: Brawl Ball
  summary: 大量草簇与长窄墙交织、球门三格窄口的 Brawl Ball 图：草路支撑推进/伏击，破墙扩大得分窗口，但墙体本身价值低，开阔对抗权重高。
  topology:
    key_points:
      - 左右两侧各三组草簇和两排墙，形成可借草推进的边路。
      - 中路两处小墙草块，近中心两大墙草簇、球置正中。
      - 球门开口三格，破墙可扩大到七格；墙体多而细长、价值低且易被拆。
      - 全图对角对称；`Box=42`、`Barrel=24`、`Bush=82`，草密度高。
  objective_access:
    objective_type: goal
    stable_goal: 先利用草路建立边路推进与球权，再用破墙扩大球门窗口或强控/位移绕过窄口完成进球。
  tactical_features:
    - id: goal_narrow_opening_wall_break
      type: goal_barrier
      location: goal_front_three_tile_opening
      condition: 球门默认三格开口，破墙可扩到七格
      combat_effect:
        rewards_capabilities: [wall_break_score_window, knockback_score, dash_or_jump_score, goal_area_denial]
        punishes_capabilities: [poke_without_score_tool]
        false_positive_capabilities: [breaking_when_enemy_open_field_stronger]
      objective_effect:
        payoff: 破墙或强控/位移是稳定扩大射门窗口的前提
      draft_implication:
        bp_use: BP 至少需要一个 scoring window creator 或破门手段
    - id: side_bush_route_and_ambush
      type: grass_flank_route
      location: three_bush_clusters_and_two_wall_rows_per_side
      condition: 侧草未被持续扫除，短手可借草推进到球门或伏击
      combat_effect:
        rewards_capabilities: [bush_sweep, wide_spread, area_denial, grass_flank]
        punishes_capabilities: [pure_linear_shooter_without_side_control]
        false_positive_capabilities: [short_range_without_scout_or_exit]
      objective_effect:
        payoff: 草路连接球门方向时提供推进/伏击，被扫草英雄覆盖时草路价值塌缩
      draft_implication:
        bp_use: 需要同时检查草路推进方和扫草反制方
    - id: low_value_easy_break_walls
      type: terrain_state_choice
      location: scattered_long_narrow_wall_placements
      condition: 墙体价值低且易被 Frank/Colt/Bull/Shelly 类英雄拆掉
      combat_effect:
        rewards_capabilities: [controlled_wall_break, long_range_after_opening, wide_spread]
        punishes_capabilities: [wall_dependent_comp]
        false_positive_capabilities: [overbreaking_if_our_comp_needs_cover]
      objective_effect:
        payoff: 拆墙降低掩体密度，开阔后长线和宽弹道收益上升
      draft_implication:
        bp_use: 开墙需比较双方远程/宽弹道对净收益
    - id: bush_pathway_pressure
      type: lane_choke_pressure
      location: bush_pathways_and_center_bush_wall_clusters
      condition: 英雄主要活动在草路上而非开阔区
      combat_effect:
        rewards_capabilities: [wide_spread, pierce, area_denial, turret_or_pet_pressure]
        punishes_capabilities: [single_target_low_area]
        false_positive_capabilities: [clump_punish_if_enemy_splits_properly]
      objective_effect:
        payoff: 高展开或范围技能可把敌人逼出草位并压制推进
      draft_implication:
        bp_use: 后手可补宽弹道/范围控制反制草路抱团
  lane_dynamics:
    notes:
      - 三路职责清晰：重装走左路、斗士走中路、射手/支援走右路。
      - 短手依赖两侧草接近，但草路不连接出口时会被宽弹道扫空。
      - 中距离高血量英雄（Nita/Frank/Carl 类）可同时压短手和长手，是混合地形下的机制候选。
      - 破门前墙体英雄价值高；破门后开阔长线和射门窗口价值上升。
  map_rules:
    - if: 我方没有破门或绕门手段
      then: 三格窄口会让进球窗口很难打开
      because: 球门结构限制直接射门角度
      bp_use: 补 wall_break / dash / knockback 类得分工具
    - if: 敌方草路成型且我方无扫草
      then: 短手会从两侧持续获得接近成本优势
      because: 草路连接球门方向且未被覆盖
      bp_use: response pick bush_sweep / wide_spread
    - if: 我方拆掉大量墙
      then: 需要确认我方宽弹道/长线能接管开阔区
      because: 墙被拆后双方进入更纯粹的开阔对抗
      bp_use: 开墙前比较双方开阔收益
  false_positive:
    - "草多不等于纯短手图：草路被扫、出口被卡时短手接近成本极高。"
    - "墙体价值低，'有墙=投掷图'是错误信号；投掷需要说明草路逼退或墙后控制的具体用法。"
    - "Fandom 英雄 Tips（Nita/Frank/Carl 等）只是机制提示，不构成当前强度结论。"
```

## BP 用法

- 如果 `我方没有破门或绕门手段`，则 `进球窗口难以打开`；BP 上用于：补 scoring window creator。
- 如果 `敌方草路成型且我方无扫草`，则 `短手接近成本优势上升`；BP 上用于：response pick bush sweep / wide spread。
- 开墙是双向地形选择：拆墙降低掩体后，长线与宽弹道权重上升。

## 变动层边界

本页只记录稳定地图结构和能力交互。Season 48 池内状态见赛季索引；当前版本强势英雄、ban 优先级和英雄 map-fit 覆盖写入英雄页或版本 / meta 层，不反写成稳定地图事实。
