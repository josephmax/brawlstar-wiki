# Brawl Planet 站点与数据接口

## 来源信息

- 标题：Brawl Planet — Ranked stats & pick/use rate data source
- 来源：[Brawl Planet](https://brawlplanet.com)（HTTP 308 重定向到 `https://www.brawlplanet.com`）
- 相关页面：`/powerleague`（Diamond I+）、`/powerleague/pl-m1`（Mythic I+）、`/powerleague/pl-m3`（Mythic III+）、`/powerleague/pl-l1`（**Legendary I+**）
- 首次验证日期：2026-08-14
- 类型：第三方 Ranked 统计站（数据经 Google Cloud Storage 静态 JSON 公开）
- 状态：`environment_signal_pick_source_v1`（描述性信号源，非稳定事实、非 runtime 直接输入）

## 数据接口（实测发现）

页面为 Next.js App Router 客户端渲染，初始 RSC payload 不含统计数据；客户端 chunk（`2096819c4432fa86` 等）通过 `fetch` 拉取 **Google Cloud Storage 公开 bucket**：

```text
https://storage.googleapis.com/brawlanalyzer-public/<file>.json.gz
```

**`.json.gz` 是命名约定，实际内容是明文 JSON**（直接 `json.loads` 即可，gzip 解压会失败）。无需 headless browser。

### 文件清单

| 文件 | 段位口径 | 用途 |
| --- | --- | --- |
| `pl-l1-results.json.gz` | **Legendary I+（legendary_plus）** | 环境信号 pick 层主文件 |
| `pl-m1-results.json.gz` | Mythic I+ | 备选段位下限 |
| `pl-results.json.gz` | Diamond I+（powerleague 默认页） | 更宽口径参考 |
| `brawlers.json.gz` | — | 英雄目录（含 future 英雄标记） |

文件命名规律（从 chunk 代码 `"pl"===y?"pl-results.json.gz":`+"`${y}-results.json.gz`"` 得出）：`<tier>-results.json.gz`。

### 数据结构（pl-l1）

```jsonc
{
  "crystalarcade_gemgrab": {          // key = "<map>_<mode>"，小写去分隔符
    "individual": [                   // 单英雄统计（约 101 个）
      {"brawler": "GRIFF", "wr": 49.9, "ur": 43.1, "sr": 17.0}
      // wr = win rate %, ur = use rate %（pick rate）, sr = star player rate %
    ],
    "teams": [{"team": ["8-BIT","STU","BOLT"], "wr": 88.5}],  // 阵容胜率
    "mode": "gemgrab", "modeFormatted": "Gem Grab",
    "map": "Crystal Arcade",
    "match_count": 90887,             // 该图对局样本量
    "active": true,                   // 是否仍在轮换
    "latest_match_time": 1786706469,
    "recent_match_count": 90887
  },
  // ... 共 33 个图条目（29 active）
}
```

英雄名是全大写（`GRIFF` / `STARR NOVA` / `8-BIT`），需用 wiki canonical 名归一化（title-case 后与 `wiki/entities/brawlers/*.md` 匹配）；`brawlers.json.gz` 里 `future: true` 的英雄（如 Wendy）必须过滤。

## 抓取方法论

1. **直抓静态 JSON**，不渲染页面：`fetch_brawlplanet_pickrate.py`（见维护 skill）下载 `pl-l1-results.json.gz` + `brawlers.json.gz`。
2. **名称归一化**：Brawl Planet 大写名 → title-case → 与 wiki canonical 名 normalize-key 匹配；未匹配项丢弃并应记录（首次执行 0 失败）。
3. **future 英雄过滤**：`brawlers.json.gz` 的 `future` 标记。
4. **聚合**：逐图保留（`per_map`）；全局层按 `match_count` 加权平均 use/win rate（只统计 `active` 图），避免 inactive 退役图干扰。
5. **礼貌与稳定性**：GCS 静态文件、低频拉取；站点无公开 API 承诺，bucket/文件名可能变动，抓取脚本需保留可维护性并记录抓取时间。

## 首次执行结果（2026-08-14）

- 覆盖：33 图（29 active）/ **总样本 2,882,389 场** / 105 英雄全覆盖（名称归一化 0 失败）。
- 单图样本：Crystal Arcade（S47 featured 新图）**90,887 场** Legendary+。
- 全局 use rate top（按对局量加权）：Griff 29.4%、Brock 26.7%、Crow 23.8%、Surge 23.7%、Max 20.7%、Pierce 20.1%、Starr Nova 19.6%、Meg 19.4%、8-Bit 18.4%。
- 产物：`outputs/runtime-bp-index/environment-signal-pickrate-legendary-plus.json`（`brawlstar.environment_signal_pickrate.v1`）。

## 边界与限制

- **无 ban 数据**：Brawl Planet 全站（含 API/chunk）无 ban 字段；ban 信号由 Liquipedia 月赛补（见 `skills/brawl-stars-bp-knowledge-maintenance/references/environment-signal-ingest.md`）。
- **窗口**：10 周滚动窗口，非单月；与月赛 ban 信号合并时需标注窗口差异。
- **口径**：`rank_floor: legendary_plus`；"Diamond I+ 为 top 20%"等站点自述未经独立验证。
- **不可用边界**：不可生成 tier；不可直接作为 runtime 输入（需复核提升）；不可当作无条件强度结论。

## 关联页面

- [[syntheses/BP-强度层语义回归与高分选取率估计器|BP 强度层语义回归与高分选取率估计器]]
- `skills/brawl-stars-bp-knowledge-maintenance/scripts/fetch_brawlplanet_pickrate.py`
- `skills/brawl-stars-bp-knowledge-maintenance/references/environment-signal-ingest.md`
