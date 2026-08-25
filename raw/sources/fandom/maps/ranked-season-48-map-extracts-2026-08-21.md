# Compact Raw Capture: Ranked Season 48 Map Pool

- Capture date: 2026-08-21
- Source: Brawl Stars Wiki / Fandom `Ranked` page, "Active maps (Season 48)" table
- Source URL: https://brawlstars.fandom.com/wiki/Ranked
- Source revision: revid 217144, last edited 2026-08-21T00:23:29Z (pageid 62172)
- Fetch method: MediaWiki API `action=parse&page=Ranked&prop=wikitext` (formatversion=2)
- Scope: full Season 48 active map pool per mode + Trial Brawlers anchor row
- Source reliability: community wiki. Use for map geometry, layout, and map-interaction seed rules; do not use as final BP advice without local DSL validation.

## Season 48 Active Maps (per Fandom Ranked page)

### Gem Grab (6)

- Crystal Arcade: https://brawlstars.fandom.com/wiki/Crystal_Arcade -> `wiki/entities/maps/Crystal Arcade.md`
- Double Swoosh: https://brawlstars.fandom.com/wiki/Double_Swoosh -> `wiki/entities/maps/Double Swoosh.md`
- Gem Fort: https://brawlstars.fandom.com/wiki/Gem_Fort -> `wiki/entities/maps/Gem Fort.md`
- Hard Rock Mine: https://brawlstars.fandom.com/wiki/Hard_Rock_Mine -> `wiki/entities/maps/Hard Rock Mine.md`
- Rustic Arcade: https://brawlstars.fandom.com/wiki/Rustic_Arcade -> `wiki/entities/maps/Rustic Arcade.md`（S48 仍保留；S47 已标记待 ingest，本轮补齐）
- Undermine: https://brawlstars.fandom.com/wiki/Undermine -> `wiki/entities/maps/Undermine.md`

### Heist (6)

- Bridge Too Far: https://brawlstars.fandom.com/wiki/Bridge_Too_Far -> `wiki/entities/maps/Bridge Too Far.md`
- Hot Potato: https://brawlstars.fandom.com/wiki/Hot_Potato -> `wiki/entities/maps/Hot Potato.md`
- Kaboom Canyon: https://brawlstars.fandom.com/wiki/Kaboom_Canyon -> `wiki/entities/maps/Kaboom Canyon.md`
- Pit Stop: https://brawlstars.fandom.com/wiki/Pit_Stop -> `wiki/entities/maps/Pit Stop.md`
- Safe Zone: https://brawlstars.fandom.com/wiki/Safe_Zone -> `wiki/entities/maps/Safe Zone.md`
- Safe(r) Zone: https://brawlstars.fandom.com/wiki/Safe%28r%29_Zone -> `wiki/entities/maps/Safe(r) Zone.md`

### Bounty (4)

- Dry Season: https://brawlstars.fandom.com/wiki/Dry_Season -> `wiki/entities/maps/Dry Season.md`
- Hideout: https://brawlstars.fandom.com/wiki/Hideout -> `wiki/entities/maps/Hideout.md`
- Layer Cake: https://brawlstars.fandom.com/wiki/Layer_Cake -> `wiki/entities/maps/Layer Cake.md`
- Shooting Star: https://brawlstars.fandom.com/wiki/Shooting_Star -> `wiki/entities/maps/Shooting Star.md`

### Brawl Ball — FEATURED (6)

- Beach Ball: https://brawlstars.fandom.com/wiki/Beach_Ball -> `wiki/entities/maps/Beach Ball.md`（S48 新增）
- Center Stage: https://brawlstars.fandom.com/wiki/Center_Stage -> `wiki/entities/maps/Center Stage.md`
- Pinball Dreams: https://brawlstars.fandom.com/wiki/Pinball_Dreams -> `wiki/entities/maps/Pinball Dreams.md`
- Sneaky Fields: https://brawlstars.fandom.com/wiki/Sneaky_Fields -> `wiki/entities/maps/Sneaky Fields.md`
- Spiraling Out: https://brawlstars.fandom.com/wiki/Spiraling_Out -> `wiki/entities/maps/Spiraling Out.md`（S48 新增）
- Triple Dribble: https://brawlstars.fandom.com/wiki/Triple_Dribble -> `wiki/entities/maps/Triple Dribble.md`

### Hot Zone (4)

- Dueling Beetles: https://brawlstars.fandom.com/wiki/Dueling_Beetles -> `wiki/entities/maps/Dueling Beetles.md`
- Open Business: https://brawlstars.fandom.com/wiki/Open_Business -> `wiki/entities/maps/Open Business.md`
- Parallel Plays: https://brawlstars.fandom.com/wiki/Parallel_Plays -> `wiki/entities/maps/Parallel Plays.md`
- Ring of Fire: https://brawlstars.fandom.com/wiki/Ring_of_Fire -> `wiki/entities/maps/Ring of Fire.md`

### Knockout (4)

- Belle's Rock: https://brawlstars.fandom.com/wiki/Belle%27s_Rock -> `wiki/entities/maps/Belle's Rock.md`
- Flaring Phoenix: https://brawlstars.fandom.com/wiki/Flaring_Phoenix -> `wiki/entities/maps/Flaring Phoenix.md`
- New Horizons: https://brawlstars.fandom.com/wiki/New_Horizons -> `wiki/entities/maps/New Horizons.md`
- Out in the Open: https://brawlstars.fandom.com/wiki/Out_in_the_Open -> `wiki/entities/maps/Out in the Open.md`

## Trial Brawlers anchor (Season 48)

- `#48 | August 20, 2026 | Trunk, Willow, Kaze | Brawl Ball (featured)`（Ranked 页 Trial Brawlers 表）

## S48 vs S47 diff（以库内 S47 索引为准）

| 模式 | S47 图数 | S48 图数 | 变化 | 新增 | 移除 |
| --- | --- | --- | --- | --- | --- |
| Brawl Ball (featured) | 4 | 6 | +2 | Beach Ball, Spiraling Out | 无 |
| Gem Grab | 6 | 6 | 0（失去 featured 但图数保留） | — | — |
| Heist | 6 | 6 | 0 | — | — |
| Bounty | 4 | 4 | 0 | — | — |
| Hot Zone | 4 | 4 | 0 | — | — |
| Knockout | 4 | 4 | 0 | — | — |

- 总图数：28 -> 30。
- featured 模式从 Season 47 的 Gem Grab 切换为 Season 48 的 Brawl Ball；与 Heist（S46 featured -> S47 保留 6 张）一致，Gem Grab 失去 featured 后保留其 6 张图。
- Rustic Arcade 是 S47 已存在、S48 继续保留的 Gem Grab 图，此前因缺 raw/source/entity 一直停留在"待 ingest"缺口，本轮一并补齐。

## 编号说明（provenance 冲突）

- Fandom `Ranked` 页（Active maps 表 + Trial Brawlers 表）用 Season 46/47/48 编号，是本库赛季编号的既定基准。
- 单地图页 `History` 段落使用另一套编号（例如 Beach Ball / Spiraling Out / Rustic Arcade 在 2026-08-20 的条目写作 "Season 30 Ranked"）。两套编号并存，落盘时以 Ranked 页 "Season 48" 为准；地图 History 的 "Season N Ranked" 仅作为"该图曾进入 Ranked"的历史证据，不用于本库赛季编号换算。

## Organized Destinations

- Source summary: `wiki/sources/Fandom-Ranked-Season-48-Map-Pages.md`
- Season index: `wiki/syntheses/Ranked-Season-48-地图Map-Profile总览.md`
- New stable map entities: `wiki/entities/maps/Beach Ball.md`、`wiki/entities/maps/Spiraling Out.md`、`wiki/entities/maps/Rustic Arcade.md`
- Per-map raw captures: `raw/sources/fandom/maps/beach-ball-2026-08-21.md`、`spiraling-out-2026-08-21.md`、`rustic-arcade-2026-08-21.md`

## Extraction Boundary

本轮 raw 直接写成 compact manifest（S46 压缩后形态），单图细节见独立 per-map raw capture。若后续重抓，新增新日期文件，不静默改写本文件。
