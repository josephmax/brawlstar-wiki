# Rustic Arcade

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Gem Grab`
- Fandom URL：https://brawlstars.fandom.com/wiki/Rustic_Arcade
- 来源：[[sources/Fandom-Rustic-Arcade|Fandom 来源摘要: Rustic Arcade]]
- 当前赛季索引：[[syntheses/Ranked-Season-48-地图Map-Profile总览|Ranked Season 48 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-08-21
- 背景：Season 47 索引标记的"待 ingest 缺口"已于本轮补齐；S47/S48 均为 Gem Grab 池内图。

## BP-ready map_profile

```yaml
map_profile:
  name: Rustic Arcade
  mode: Gem Grab
  summary: 中央六边形墙环 + 贴墙草 + 两跳板两湖的 Gem Grab 图：控中与墙边范围压力是核心，跳板改变接近路线，短手与纯投掷在开阔空间挣扎。
  topology:
    key_points:
      - 中央六边形墙区：墙朝中心、草贴外墙，墙草环与宝石矿之间留空。
      - 靠出生点六处带草 enclave，两个跳板（Launch Pad）可把英雄送到中心。
      - 两处湖（`Lake=2`）与不可破墙（`IndestructibleWall=18`）限制穿越路线。
      - 全图对角对称；`Block2=12`、`Barrel=4`、`Breakable=2`、`Bush=50`。
  objective_access:
    objective_type: gem_mine
    stable_goal: 控制中央六边形墙边与草环视野，把线权转成收宝、保护 carrier，并利用跳板路线管理倒计时撤退。
  tactical_features:
    - id: hexagon_center_wall_ring
      type: center_wall_control
      location: central_hexagon_walls_facing_center_with_bushes_outside
      condition: 中央墙环完整，目标必须从墙边或墙间入口接近宝石矿
      combat_effect:
        rewards_capabilities: [gem_mid_control, through_wall_or_over_wall_pressure, wide_spread, spawnable_or_pet]
        punishes_capabilities: [artillery_and_short_range_in_open]
        false_positive_capabilities: [thrower_without_flank_protection]
      objective_effect:
        payoff: 高展开/穿墙/范围英雄可在墙环外侧低风险影响矿区
      draft_implication:
        bp_use: 阵容至少需要墙边处理或范围控制，不能只靠正面单线对枪
    - id: launch_pad_center_routes
      type: mobility_route
      location: two_launch_pads_toward_center
      condition: 跳板可用且落点未被覆盖，改变进入/离开中心的路线成本
      combat_effect:
        rewards_capabilities: [mobility, gem_mid_control, carrier_safety]
        punishes_capabilities: [static_anchor_comp]
        false_positive_capabilities: [jump_into_uncovered_center]
      objective_effect:
        payoff: 跳板可加速抢矿/回防，也会让落点成为被预瞄的固定窗口
      draft_implication:
        bp_use: 需要评估双方对跳板落点的覆盖能力
    - id: enclave_bush_pockets_and_corner_pinch
      type: carrier_retreat_pocket
      location: six_bush_enclaves_near_spawns
      condition: 草丛被用作撤退/重组或夹击入口
      combat_effect:
        rewards_capabilities: [bush_sweep, pinch_pressure, scouting_or_vision, carrier_safety]
        punishes_capabilities: [single_angle_chase]
        false_positive_capabilities: [retreat_without_side_lane_control]
      objective_effect:
        payoff: 角草可保 carrier 倒计时，但侧路全失时变成困点
      draft_implication:
        bp_use: carrier 与护送不能同时缺视野或脱离工具
    - id: wall_break_extends_sniper_range
      type: terrain_state_choice
      location: six_breakable_barriers
      condition: 拆除可破墙会延长长手射程并开放射界
      combat_effect:
        rewards_capabilities: [long_range_after_opening, controlled_wall_break]
        punishes_capabilities: [automatic_wall_break]
        false_positive_capabilities: [overbreaking_if_center_control_depends_on_walls]
      objective_effect:
        payoff: 破墙放大长手护 carrier 与压制能力，但会削弱墙环对己方短手的保护
      draft_implication:
        bp_use: 开墙前比较双方远程/短手对墙环净收益
  lane_dynamics:
    notes:
      - 中路负责控矿和 carrier 安全，边路负责探草、夹击与阻止角草撤退。
      - 跳板与湖改变常规进入路线：中路接触不是纯线性对枪。
      - Fandom 提示 Tara/Bo/Griff/Carl 在中上墙后更激进、可夹击角草撤退，与 Crystal Arcade 的 2x2 墙结构形成对照。
  map_rules:
    - if: 我方没有墙边处理或范围控制
      then: 中央六边形墙环会切断单一射线
      because: 墙环与贴墙草限制正面直线接触
      bp_use: 补 through-wall / wide-spread / 可验证的草环路线
    - if: 敌方 carrier 退入角草
      then: 先保住两侧出口再扫草
      because: 单角追击容易被墙草反打或拖完倒计时
      bp_use: 需要 pinch_pressure 与 bush_sweep
    - if: 我方依赖墙环接近矿区
      then: 不应默认破掉六面墙
      because: 破墙可能让对方长手接管矿区并移除我方掩体
      bp_use: terrain_state_plan.preserve_or_selective_break
  false_positive:
    - "跳板存在不等于'机动图'：落点可能被预瞄，路线收益取决于双方覆盖。"
    - "中央有墙不等于投掷图：墙环与宝石矿之间留空，纯投掷缺乏墙后目标收益。"
    - "Fandom 推荐英雄（Pam/Emz/Frank/Poco、长手等）只是机制提示，不构成当前强度结论。"
```

## BP 用法

- 中央墙环完整时优先覆盖墙边控制、范围压力和探草；开墙后长手射程与交叉火力权重上升。
- 跳板路线要按"落点覆盖"双向评估，不能默认正收益。
- 与 [[entities/maps/Crystal Arcade|Crystal Arcade]] 互为结构对照：Crystal Arcade 中央 2x2 墙簇 vs Rustic Arcade 六边形墙环+跳板。

## 变动层边界

本页只记录稳定地图结构和能力交互。Season 47/48 池内状态见赛季索引；当前版本强势英雄、ban 优先级和英雄 map-fit 覆盖写入英雄页或版本 / meta 层，不反写成稳定地图事实。
