# iKaoss11 July 2026 Strength Profile

## Source

- 类型：外部 tier list 截图转录 / 通用版本强度先验
- 创作者：iKaoss11
- 视频：https://www.youtube.com/watch?v=dYE3tTni8Gk
- 抓取/转录日期：2026-07-06
- Raw capture：[[../../raw/inbox/ikaoss11-july-2026-tier-list-screenshot-transcription|ikaoss11-july-2026-tier-list-screenshot-transcription]]
- Runtime copy：`skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json`

## Scope And Use

本页保存第一版 BP `compile` 可消费的通用版本强度先验。它不是英雄稳定事实，不写入 `wiki/entities/brawlers/`；它只作为独立强度层参与 `runtime_bp_index` 编译。

`map` / `mode` / `global` strength 都只在其声明 scope 内表达版本理解；更细的地图强度需要显式维护，不能把本页 global 排名当作地图适配性证明。

同一档内按从左到右排序，左侧强于右侧。编译时必须保留 `tier_rank` 和 `total_rank`，不能只保留档位。

## Normalization Notes

- `Colonel Ruffs` 归一为 `Ruffs`。
- `Twins` 归一为 `Larry & Lawrie`。
- `MisterP` 归一为 `Mr. P`。
- `Clowbert` 归一为 `Glowy`。
- 2026-07-06 转录时 `Wendy`、`Nori` 都未进入当时的 104 英雄 catalog。2026-07-10 roster 复核后，`Nori` 已是第 105 位已发布英雄，但本转录没有保留其 tier 位置，因此仍不把 Nori 写入这份 104-entry strength payload；运行时只能视为 `active_but_strength_unknown`。`Wendy` 仍为 future-only。
- 截图中的 `F` 档暂并入当前 schema 的 `E` 档。

## strength_profile

```json
{
  "schema": "brawlstar.strength_profile.v1",
  "profile_id": "ikaoss11-july-2026-screenshot",
  "patch_id": "season-52-2026-07-05",
  "tier_order": ["S", "A", "B", "C", "D", "E"],
  "profiles": {
    "global": {
      "scope": "global",
      "tiers": {
        "S": ["Brock", "8-Bit", "Meg", "Max", "Surge", "Damian", "Starr Nova", "Crow", "Ruffs", "Pierce"],
        "A": ["Poco", "Glowy", "Emz", "Stu", "Griff", "Colette", "Belle", "Byron", "Pearl", "Meeple", "Moe", "Lumi", "Finx", "Chester", "Sandy", "Gale", "Kaze", "Berry", "Charlie", "Edgar"],
        "B": ["Otis", "Rico", "Colt", "Angelo", "Leon", "Barley", "Nita", "Bibi", "Kenji", "Piper", "Nani", "Lola", "Shade", "Mortis", "Gene", "Lou", "Buzz", "R-T", "Willow", "Lily", "Jae-yong", "Najia", "Kit", "Penny"],
        "C": ["Fang", "Cordelius", "Spike", "Gus", "Amber", "Sirius", "Draco", "Gray", "Janet", "Larry & Lawrie", "Bea", "Carl", "Trunk", "Bull", "Darryl", "Ash", "Bo", "Maisie", "Juju", "Ziggy", "Squeak", "Eve", "Buster", "Melodie", "Ollie", "Alli", "Mina"],
        "D": ["Pam", "Tara", "Gigi", "Clancy", "Mr. P", "Hank", "Frank", "Dynamike", "Tick", "Sprout", "Shelly", "Jessie", "Bonnie", "Doug"],
        "E": ["Mandy", "El Primo", "Rosa", "Jacky", "Grom", "Sam", "Bolt", "Chuck", "Mico"]
      }
    },
    "modes": {},
    "maps": {}
  }
}
```
