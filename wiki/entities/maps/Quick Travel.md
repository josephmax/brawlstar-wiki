# Quick Travel

## 基础信息

- 类型：地图实体 / 稳定 map profile
- 模式：`Hot Zone`
- Fandom URL：https://brawlstars.fandom.com/wiki/Quick_Travel
- 来源：[[sources/Fandom-Quick-Travel|Fandom 来源摘要: Quick Travel]]
- 当前赛季索引：[[syntheses/Ranked-Season-49-地图Map-Profile总览|Ranked Season 49 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`
- 更新日期：2026-09-17

## BP-ready map_profile

```yaml
map_profile:
  name: Quick Travel
  mode: Hot Zone
  summary: 细绳网分割双区、S 形草簇连接两区、双弹射垫提供跨区突进的 Hot Zone 图：绳网不挡穿透与范围覆盖，草簇控制直接改变区域接近成本，弹射垫是攻防双向的高风险资源；防守姿态困难，前压型阵容权重高。
  topology:
    key_points:
      - 两个区域由细绳网（RopeFence=7、Fence=26）分割；绳网不阻挡穿透类与覆盖类攻击。
      - 两簇 S 形草丛（Bush=146，草量显著）从两区之间向内延伸、连接到弹射垫。
      - 两处弹射垫（LaunchPad=4 个垫位）：一处弹向最近区域，另一处弹到对面区域墙后。
      - 全图对角对称；Block1=30、Block2=8、Box=4、Barrel=4、Lake=2、Misc=6，实体掩体总量低。
  objective_access:
    objective_type: zone
    stable_goal: 借草簇与弹射垫建立跨区进入与区域人口优势；绳网提供的是假性掩体，区域站场要按穿透覆盖复核。
  tactical_features:
    - id: rope_fence_penetrable_split
      type: zone_barrier_penetrable
      location: two_zone_rope_fence_line
      condition: 攻击可穿过细绳网并覆盖大范围（Emz 类），绳网不提供对穿透/覆盖攻击的掩体价值
      combat_effect:
        rewards_capabilities: [pierce, wide_spread, area_denial, zone_coverage_support]
        punishes_capabilities: [short_range_cover_reliance_without_pierce_answer]
        false_positive_capabilities: [treating_fence_as_wall_cover]
      objective_effect:
        payoff: 穿透/覆盖英雄可跨线压制站区目标，防守方绳网后的站位不安全
      draft_implication:
        bp_use: 对线绳网分割图时检查双方穿透覆盖差；绳网掩体价值按零评估
    - id: s_bush_cluster_connectors
      type: grass_connector_route
      location: two_s_shaped_bush_clusters_between_zones
      condition: S 形草簇是两区之间的主要连接路径，未被扫除时支撑接近与伏击
      combat_effect:
        rewards_capabilities: [bush_sweep, scout_or_reveal, ambush, area_denial]
        punishes_capabilities: [passive_zone_sitting_without_bush_control]
        false_positive_capabilities: [grass_auto_assassin_without_zone_entry]
      objective_effect:
        payoff: 控制草簇的一方控制区域接近成本；草簇被拆后进入更开阔对峙
      draft_implication:
        bp_use: 双方都要检查草簇控制/扫描工具（覆盖型大招、探草妙具）与拆草对价
    - id: dual_launchpad_axis
      type: launchpad_dual_edge
      location: two_launchpads_between_zones
      condition: 一垫弹向最近区、一垫弹到对面墙后；重装/高血量占用收益为正，低血量占用被源页 Tips 显式标为高风险
      combat_effect:
        rewards_capabilities: [heavyweight_engage, tanky_pad_entry, mobility_flank]
        punishes_capabilities: [squishy_pad_reliance, low_health_pad_travel]
        false_positive_capabilities: [pads_as_free_mobility_for_any_comp]
      objective_effect:
        payoff: 弹射垫是突进与回防的双向通道，控制垫区即控制跨区节奏
      draft_implication:
        bp_use: 评估垫区控制者（通常为高血量/机动位）；假 设敌方同样能用垫
    - id: defensive_posture_penalty
      type: stance_pressure
      location: whole_map
      condition: 源页 Tips 明示防守困难、应前压而非缩区抱团
      combat_effect:
        rewards_capabilities: [push_pressure, zone_entry_burst, sustain_forward_presence]
        punishes_capabilities: [passive_zone_stacking, low_mobility_camping]
        false_positive_capabilities: [pure_hold_comp_without_pressure_answer]
      objective_effect:
        payoff: 前压把战线推离己方区域，缩区抱团会被草簇与垫位两翼包抄
      draft_implication:
        bp_use: 阵容需要至少一个前压支点；纯站区被动位在本图折价
  lane_dynamics:
    notes:
      - 两区各自的争夺围绕草簇入口展开，S 形草簇是事实上的中路。
      - 弹射垫提供第二条跨区轴，绕过草簇对峙直接换区。
      - 拆草（如持续烧灼/范围清除）会把图推向更开阔的穿透对射，绳网侧的假掩体价值进一步下降。
  map_rules:
    - if: 我方无草簇控制/扫描工具
      then: 敌方经 S 草簇的接近成本低于我方，区域入口被单方面选择
      because: 草簇是两区之间的事实连接路径
      bp_use: 补 bush_sweep / scout / area_denial
    - if: 敌方有穿透或大范围覆盖
      then: 绳网后的站位不构成掩体，站区人口被跨线消耗
      because: RopeFence 不阻挡穿透类攻击
      bp_use: 站区位改选机动/高血量，或对掉穿透源
    - if: 我方低血量依赖弹射垫机动
      then: 垫上暴露窗口被高血量占用者惩罚
      because: 源页 Tips 明示低血量占垫是高风险选项
      bp_use: 垫位交给重装/高血量，机动位走草簇轴
  false_positive:
    - "绳网不是墙：'有掩体=短手安全'在本图不成立，穿透与覆盖直接跨线。"
    - "草多不等于纯短手图：草簇的价值在区域连接，控制与扫描权重高于潜伏。"
    - "弹射垫不是免费机动：垫是攻防双向资源，低血量占用是明确负收益。"
    - "Fandom 英雄 Tips（Emz/Amber/Gale/Rosa）只是机制提示，不构成当前强度结论。"
```

## BP 用法

- 如果 `我方无草簇控制/扫描工具`，则 `区域入口被敌方单方面选择`；BP 上用于：补 bush sweep / scout。
- 如果 `敌方有穿透或大范围覆盖`，则 `绳网后站位不构成掩体`；BP 上用于：站区位改机动/高血量。
- 弹射垫是双向资源：垫位控制权评估按"谁占用更划算"，不按"我方能否用"。

## 变动层边界

本页只记录稳定地图结构和能力交互。Season 49 池内状态见赛季索引；当前版本强势英雄、ban 优先级和英雄 map-fit 覆盖写入英雄页或版本 / meta 层，不反写成稳定地图事实。
