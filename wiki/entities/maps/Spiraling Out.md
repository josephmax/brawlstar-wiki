# Spiraling Out

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Brawl Ball`
- Fandom URL：https://brawlstars.fandom.com/wiki/Spiraling_Out
- 来源：[[sources/Fandom-Spiraling-Out|Fandom 来源摘要: Spiraling Out]]
- 当前赛季索引：[[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-08-21
- 覆盖声明：Fandom 本页 Tips 段为空，本 profile 仅基于 Layout + Infobox 的结构层结论，不含任何英雄适配派生。

## BP-ready map_profile

```yaml
map_profile:
  name: Spiraling Out
  mode: Brawl Ball
  summary: 中部多组长角形墙并附着草丛（隐身+掩体二合一），球门相对开放、门前墙少的 Brawl Ball 图；结构层信息完整，英雄交互层暂缺来源。
  topology:
    key_points:
      - 中部多组长角形墙（corner-shaped wall pieces），草丛附着在墙上，同时提供隐身与掩体。
      - 球门相对开放，门前守护墙较少，直接射门角度比常规球门图更大。
      - 全图对角对称；`Box=48`、`Barrel=4`、`Bush=36`。
  objective_access:
    objective_type: goal
    stable_goal: 中部墙草结合体决定争夺球权与推进路线；开放球门使直接射门/射门窗口更容易成立，防守更需要主动拦截而非依赖地形。
  tactical_features:
    - id: mid_corner_wall_bush_combos
      type: wall_grass_cover_combo
      location: mid_corner_shaped_wall_pieces_with_attached_bushes
      condition: 中部墙草结合体未被清草或拆墙，提供掩体和隐身双重价值
      combat_effect:
        rewards_capabilities: [bush_sweep, scouting_or_vision, wall_use, mid_survivability]
        punishes_capabilities: [pure_open_lane_linear_comp]
        false_positive_capabilities: [short_range_without_scout_or_exit]
      objective_effect:
        payoff: 控住中部墙草结合体的一方获得推进与防守的双重位置优势
      draft_implication:
        bp_use: 中后手需检查清草/侦察与墙边对抗能力
    - id: open_goal_direct_score
      type: goal_open_access
      location: goal_front_few_walls
      condition: 门前守护墙少，直接射门角度相对开放
      combat_effect:
        rewards_capabilities: [goal_area_denial, long_range_pressure, anti_aggro_poke]
        punishes_capabilities: [wall_break_for_goal_as_only_score_tool]
        false_positive_capabilities: [scorer_without_ball_support]
      objective_effect:
        payoff: 得分窗口更依赖线权与射门兑现，而非破门
      draft_implication:
        bp_use: 防守端更需要主动拦截/清球，进攻端直接射门价值升高
  lane_dynamics:
    notes:
      - 中部墙草结合体是主要地形争夺点，边路结构信息不足（来源无 Tips 支撑）。
      - 球门开放意味着守门/反突进和清球能力权重上升。
  map_rules:
    - if: 我方无法清掉中部墙边草丛
      then: 敌方可反复利用隐身+掩体重组位置
      because: 墙草结合体同时提供覆盖和接近起点
      bp_use: 需要 bush_sweep / scouting_or_vision
    - if: 球门开放且我方无主动拦截
      then: 敌方直接射门窗口更易兑现
      because: 门前地形对得分限制小
      bp_use: 需要 goal_area_denial / 清球与反突进
  false_positive:
    - "Tips 缺失：本页不派生任何英雄适配或'强图'结论，只有结构层事实。"
    - "中部有墙+草不等于投掷图：角形墙几何与球门开放度未验证投掷角度收益。"
    - "'Box=48 墙多'不等于掩体多：墙集中在角形结构，球门区反而开放。"
```

## BP 用法

- 中部墙草结合体未被清草时，敌方获得隐身+掩体双重位置优势；BP 上用于：补 bush sweep / scouting。
- 球门开放时，直接射门窗口更易兑现；BP 上用于：补主动拦截 / 清球 / 反突进。
- 本页结构层信息完整、英雄交互层无来源，候选评估时按 low-evidence 处理，不以本页作为强适配依据。

## 变动层边界

本页只记录稳定地图结构和能力交互。Fandom Tips 补齐或获得赛事/高分证据后，再按正常 ingest 流程增量更新英雄交互层；当前版本强势英雄、ban 优先级不写入本页。
