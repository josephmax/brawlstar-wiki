# Fandom 来源摘要: Quick Travel

## 来源信息

- 标题：Quick Travel
- 来源：[Quick Travel | Brawl Stars Wiki | Fandom](https://brawlstars.fandom.com/wiki/Quick_Travel)
- 抓取日期：2026-09-17（revid 219106，2026-09-17T06:58:48Z）
- 类型：地图来源 / Hot Zone 地图页 / 社区攻略来源
- 上游 raw：[[../../raw/sources/fandom/maps/quick-travel-2026-09-17.md]]
- 关联地图实体：[[entities/maps/Quick Travel|Quick Travel]]

## 范围

本页覆盖 Fandom `Quick Travel` 地图页中的：

- 模式与环境：`Hot Zone`，`Canyon`（2025-11-20 起）。
- 障碍概况：Infobox `Block1=30`、`Block2=8`、`Box=4`、`Barrel=4`、`Fence=26`、`RopeFence=7`、`Misc=6`、`Lake=2`、`Bush=146`、`LaunchPad=4`。
- Layout：两个区域由细绳网（rope fencing）分割；连接两区的是向内延伸至弹射垫的 S 形草簇；一处弹射垫把英雄弹到最近区域、另一处把英雄弹到对面区域墙后；全图对角对称。
- Tips：防守困难、应主动前压；两簇 S 形草是关键地带；低血量英雄慎用弹射垫；Emz 攻击可穿绳网且覆盖大、适合支援与防守、大招可扫草簇；Amber 大招提供区域控制、面对重装可拆草；Gale 弹射器妙具便于机动但需防止敌方借用；Rosa 妙具可探草减速伏击。
- History：2021-01-27 加入、2021-04-07 移除；2025-11-20 回归 Ranked（地图页编号 Season 21，环境改 Canyon）；2026-04-16 / 2026-09-17 再次入池（地图页编号 Season 26 / Season 31；Season 31 即本库 Season 49）。

## 可用范围

- `usable_for`:
  - `stable_map_structure`（绳网分割、S 形草簇、双向弹射垫、对角对称）
  - `zone_connectivity_and_launchpad_factors`
  - `bush_cluster_control_and_scout_factors`
  - `rope_fence_penetration_factor`（攻击可穿绳网，掩体不挡弹道）
  - `ranked_or_event_history_reference`
- `not_usable_for`:
  - 当前版本强势英雄 tier、ban 优先级。
  - 英雄当前数值、构筑强度或补丁后胜率。
  - 地图图片级坐标校验。

## BP 建模要点

- **绳网不是墙**：Fence/RopeFence 类掩体不挡 Emz 类穿透攻击，"有掩体=短手安全"在本图要按穿透与范围覆盖复核。
- **弹射垫是双向资源**：既是我方切入/回防工具，也是敌方突进通道；低血量英雄占用弹射垫被 Tips 显式标为高风险——这是"机动资源误用"型 false positive。
- **草簇是区域连接资源**：S 形草簇连接两区，控制/扫描草簇（Emz 大招、Rosa 妙具类）直接改变区域争夺的接近成本；但草簇被拆（Amber 类）后进入更开阔的对峙。
- **防守姿态困难**：Tips 明示"cluttering in zones 不可取"，站区型被动打法在本图要以前压能力为前提。
- Fandom 英雄 Tips 只作为 map-feature 候选；具体英雄适配回到英雄实体页与当前稳定事实层。

## 关联页面

- [[entities/maps/Quick Travel|Quick Travel]]
- [[concepts/Hot Zone|Hot Zone]]
- [[syntheses/Ranked-Season-49-地图Map-Profile总览|Ranked Season 49 地图 Map Profile 总览]]
- [[syntheses/BP-地图建模与决策规范|BP 地图建模与决策规范]]
