# Double Swoosh

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Gem Grab`
- Fandom URL：https://brawlstars.fandom.com/wiki/Double_Swoosh
- 来源：[[sources/Fandom-Ranked-Season-46-Map-Pages|Fandom 来源摘要: Ranked Season 46 全量地图页]]
- 当前赛季索引：[[syntheses/Ranked-Season-46-地图Map-Profile总览|Ranked Season 46 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-06-29

## BP-ready map_profile

```yaml
map_profile:
  name: Double Swoosh
  mode: Gem Grab
  summary: 双螺旋草丛和侧路草带把宝石争夺变成视野、侧压、探草和草丛否定的地图。
  topology:
    key_points:
      - 中路宝石矿被两组螺旋草丛包围，中心不是纯对枪区，而是持续探草区。
      - 左右侧草带能绕到敌方半场，侧路压力会反复压缩 gem carrier 的安全半径。
      - 部分草丛受墙体保护，直线远程不能稳定清点。
  objective_access:
    objective_type: gem_mine
    stable_goal: Gem Grab 的目标访问依赖中路站位与倒计时撤退；侧路击杀和探草能改变宝石持有者的退路。
  tactical_features:
    - id: spiral_bush_approach
      type: grass_anchor
      location: center_spiral_bushes
      condition: 中心双螺旋草丛提供连续接近和伏击路线
      combat_effect:
        rewards_capabilities: [bush_scouting, bush_sweeping, wide_spread_control, trap_placement, speed_gear_flank]
        punishes_capabilities: [pure_marksman_without_vision, static_thrower_without_peel]
        false_positive_capabilities: [tank_without_bush_control_after_grass_removed]
      objective_effect:
        payoff: 允许侧路或中路英雄逼退宝石矿附近站位
      draft_implication:
        bp_use: 必须优先确认队伍是否有探草/扫草；没有视野时长手价值降级
    - id: side_flank_bush_lane
      type: flank_route
      location: left_and_right_side_bush_lanes
      condition: 侧路草带连接敌我半场，允许多角度绕后
      combat_effect:
        rewards_capabilities: [flank_pressure, ambush_burst, gem_carrier_chase, bush_heal_or_stealth]
        punishes_capabilities: [slow_rotation, single_lane_mid_stack]
        false_positive_capabilities: [assassin_without_exit_after_failed_flank]
      objective_effect:
        payoff: 通过侧压迫使敌方 gem carrier 后撤或交资源
      draft_implication:
        bp_use: 适合中后手补侧路压力，也会制造必须 answer 的探草需求
    - id: terrain_denial_against_flank
      type: terrain_denial
      location: enemy_side_bushes
      condition: 烧草、破草或显形会直接降低敌方绕后价值
      combat_effect:
        rewards_capabilities: [terrain_destruction, vision_reveal, persistent_area_check]
        punishes_capabilities: [grass_dependent_tank, hidden_thrower]
        false_positive_capabilities: [overbreaking_own_retreat_bushes]
      objective_effect:
        payoff: 降低敌方倒计时伏击和侧路包夹
      draft_implication:
        bp_use: 可作为保护中路核心的反 flank 选择
  lane_dynamics:
    notes:
      - 默认一人中路控宝石，两侧负责探草、压线和截断敌方撤退。
      - 如果敌方三人堆中，宽弹道、连锁、穿透和范围控制收益提高。
      - 如果我方缺探草，所有中路长手和投掷都必须按高风险处理。
  map_rules:
    - if: 我方没有可靠探草或扫草
      then: 不要把纯长手当作稳定先手
      because: 侧路草带会让远程视野被反复压缩
      bp_use: 优先补 vision / sweep / spread control
    - if: 敌方拿到 gem lead 并准备倒计时撤退
      then: 侧路 flank 和显形能力升值
      because: 倒计时时宝石持有者常借草丛撤退
      bp_use: 后手可用探草、拉人或绕后制造翻盘窗口
    - if: 敌方依赖草丛坦克或刺客
      then: 破草/烧草可以成为 ban/pick 依据
      because: 地形一旦被否定，敌方接近路线成本上升
      bp_use: 可保护中路宝石核心
  false_positive:
    - 只写“草多所以坦克强”不够；高水平对局会持续探草，坦克需要路线、队友压制或视野资源。
    - 纯投掷若没有队友保护，容易被侧路草丛压死。
```

## BP 用法

- 如果 `我方没有可靠探草或扫草`，则 `不要把纯长手当作稳定先手`；BP 上用于：优先补 vision / sweep / spread control。
- 如果 `敌方拿到 gem lead 并准备倒计时撤退`，则 `侧路 flank 和显形能力升值`；BP 上用于：后手可用探草、拉人或绕后制造翻盘窗口。
- 如果 `敌方依赖草丛坦克或刺客`，则 `破草/烧草可以成为 ban/pick 依据`；BP 上用于：可保护中路宝石核心。

## 变动层边界

本页只记录稳定地图结构和能力交互。当前版本强势英雄、具体数值、ban 优先级和英雄 map-fit 覆盖应写入英雄页或版本 / meta 覆盖层，不反写成稳定地图事实。
