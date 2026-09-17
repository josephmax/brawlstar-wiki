# In the Liminal

## 基础信息

- 类型：地图实体 / 稳定 map profile（**部分覆盖：布局级证据缺失**）
- 模式：`Hot Zone`
- Fandom URL：https://brawlstars.fandom.com/wiki/In_the_Liminal
- 来源：[[sources/Fandom-In-the-Liminal|Fandom 来源摘要: In the Liminal]]
- 当前赛季索引：[[syntheses/Ranked-Season-49-地图Map-Profile总览|Ranked Season 49 地图 Map Profile 总览]]
- 地图规范：[[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
- 状态：`bp_map_profile_v2`（`layout_coverage_gap`：源页面 Layout/Tips 章节为空，路线级结论禁止建模）
- 更新日期：2026-09-17

## BP-ready map_profile

```yaml
map_profile:
  name: In the Liminal
  mode: Hot Zone
  summary: 仅有 infobox 可证结构的 Hot Zone 图：草丛（112）对实体掩体（38 墙 + 6 围栏）比例显著偏高，木箱（12）可破坏物量中等；布局、草簇连接与区域相邻关系无来源证据，路线级结论一律缺源待补。
  topology:
    key_points:
      - Infobox 数值：`Block1=38`、`Box=12`、`Fence=6`、`Bush=112`。
      - 草丛量级在同模式池内偏显著（Bush=112 对照 Ring of Fire / Dueling Beetles 等图），实体墙 + 围栏合计 44。
      - 环境：`Hub`（2026-02-25 起）；布局描述、草簇连接、区域相邻关系：**源页面无证据**。
  objective_access:
    objective_type: zone
    stable_goal: 未知——区域进入路径无来源证据，不得默认"草多=可潜伏接近"。
  tactical_features:
    - id: bush_heavy_tile_composition
      type: tile_composition_signal
      location: whole_map
      condition: 草丛 tile 占比显著（Bush=112 对实体掩体 44），仅当草与区域入口实际连通时才转化为伏击/接近收益
      combat_effect:
        rewards_capabilities: [bush_sweep, scout_or_reveal, area_denial]
        punishes_capabilities: [bush_reliant_comp_if_connectivity_absent]
        false_positive_capabilities: [grass_auto_assassin, grass_auto_short_range]
      objective_effect:
        payoff: 未证实——连接性证据补齐前，草量只支持"扫草/探草工具具有保底价值"这一保守结论
      draft_implication:
        bp_use: 扫草/探草工具按保底价值评估；潜伏/短手接近结论必须等布局证据
  lane_dynamics:
    notes:
      - 无来源证据；路线、分路与区域间的通道结构一律不建模。
  map_rules: []
  false_positive:
    - "草量高不等于短手/刺客图：草簇与区域的连接关系无证据，禁止从 Bush=112 直接推出接近收益。"
    - "本页存在 layout_coverage_gap：任何'草路连接区域''墙后口袋''区域相邻'表述在证据补齐前都不成立。"
    - "历史环境更替（Arcade→Hub）不改变当前结构证据边界。"
```

## 覆盖缺口（needs source coverage）

- 源页面 Layout / Tips 章节为空，本页按维护规范不脑补路线与战术特征。
- 待补：布局描述或可用的结构化地图数据；补齐前本图在 BP 判断中只消费"扫草/探草保底价值"一条保守规则。

## BP 用法

- 唯一可消费结论：`扫草/探草工具具有保底价值`（草量显著）；其余地图适配问题在证据补齐前按"结构未知"处理，不得生成 fit 结论。

## 变动层边界

本页只记录可证稳定结构。Season 49 池内状态见赛季索引；版本强势英雄与 meta 结论不写入本页。
