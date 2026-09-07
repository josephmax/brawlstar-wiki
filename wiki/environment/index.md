# 环境信号与赛事观察数据归档

本目录是环境信号与赛事观察数据的**持久归档层**（2026-08-14 架构转向后建立，2026-08-24 存储层改为 SQLite），是知识库的一部分，git 跟踪。它是 `compile` 折叠环境证据的唯一输入源；`decide` 不直接读本目录，只消费 `runtime_bp_index` 中由 compile 内嵌的证据。

## 层级定位

```text
raw/sources/liquipedia/events/ + raw/sources/brawlplanet/   ← 不可变抓取层
        │ maintenance: ingest → analyze → aggregate
        ▼
wiki/environment/<YYYY-MM>/                                ← 本目录：持久归档（SQLite 行列存储）
        │ compile（唯一聚合点）
        ▼
outputs/runtime-bp-index/<current>.json                    ← runtime_bp_index（decide 单向消费）
```

- 观测数据与信号**不在** `outputs/`（gitignored 临时产物层）；本目录是唯一 canonical 归档。
- `raw/` 保持不可变，本目录只放聚合/整理后的数据文件与索引页。
- 本目录只保存数据与 provenance，**不得**据此自动生成 strength tier、稳定对位边、地图 fit、slot eligibility 或 runtime 推荐。

## 存储格式：SQLite 行列归档（协议化）

归档使用单文件 SQLite（标准库 `sqlite3`），**sqlite 布局是一份生产/消费双方共享的协议**，而不是各写各的解析代码：

- **协议实现唯一**：`skills/brawl-stars-bp-knowledge-maintenance/scripts/_environment_sqlite.py`（schema 声明 + `SCHEMA_VERSION` + 生产写 + 消费读 + 版本守卫）。生产侧（analyze/aggregate/fetch）与消费侧（compile/audit/aggregate）都加载同一模块——compile 经 repo 相对路径 import，**不复制展开逻辑**，schema 演进不会漂移。
- **版本守卫**：`PRAGMA user_version`（当前 `1`）。消费侧遇到 `user_version != SCHEMA_VERSION` 的库抛 `EnvironmentProtocolError`，拒绝猜测未知布局；修复方式是重新生成归档或升级协议。
- **协议表集合**：`PROTOCOL_TABLES`（meta / event / series / series_ban / set / set_pick / set_ban / metric_global / metric_mode / metric_map / signal_brawler / ladder_global / ladder_per_map），契约测试锁定。
- **契约测试**：`test_environment_protocol.py`（版本守卫、写读一致、compile 消费路径一致性、表集合稳定、旧 `.json` 兼容）+ `test_environment_sqlite.py`（完整 round-trip）。
- **演进规则**：改表/列/meta 键必须同步 `_environment_sqlite.py` 并递增 `SCHEMA_VERSION`；消费侧（compile 等）无需改动（共用同一模块）；外部应用按本页表结构实现自己的读取。

优点（承接 2026-08-24 迁移）：

- **可迁移 / 其它应用可读**：任何语言/工具都能用 SQL 查询（如"某图被 pick 最多的英雄"）。
- **行列数据**：`metric_*`、`series`、`set`、`set_pick`、`set_ban`、`signal_brawler`、`ladder_*` 均为平铺关系表。
- **读取时展开**：`_environment_sqlite.py` 的 `load_profile` / `load_signal` / `load_pickrate` / `read_raw_events` 把行展开成与原 JSON 等价的 Python 结构；同一函数也接受 `.json` 路径，向后兼容。
- 体积：月度 archive ≈ 185 KB（原 JSON ≈ 800 KB，省 ~4 倍）；pickrate ≈ 500 KB（行列展开的固有开销，换取外部可查）。需要人类可读/审计导出时用生成脚本的 `--output` 写 JSON。

## 目录结构与指针

| 路径 | 内容 |
| --- | --- |
| `current.json` | `environment_archive_pointer.v1`：compile 只读此指针；维护更新归档后必须同步更新 |
| `<YYYY-MM>/archive.sqlite3` | 该月归档：`event`（source_events）+ `metric_*`（scopes 聚合）+ `series/set/set_pick/set_ban`（逐 set 行列，来自 raw 解析）+ `signal_brawler`（月赛信号） |
| `pickrate.sqlite3` | `brawlstar.environment_signal_pickrate.v1`：Legendary+ 滚动 10 周快照，**只含当前 Ranked 地图池**（`ladder_global` + `ladder_per_map` 行列表，带 `fetched_at`；池外/退役图在生产侧过滤） |
| `ranked_pool.json` | `brawlstar.ranked_pool_manifest.v1`：当前 Ranked 赛季地图池 manifest（30 图 + provenance）；`fetch_brawlplanet_pickrate.py` 默认按它过滤，赛季轮换后由维护者更新 |
| `index.md` | 本索引页 |

## 当前归档

| 归档 | 内容 | provenance |
| --- | --- | --- |
| `2026-07/archive.sqlite3` | BSC 2026 July 四赛区（EMEA + South America + East Asia + North America）：27 场已进行 series / 98 个已进行 set；7 月月赛信号（89 英雄有样本） | Liquipedia revisions 263360 / 263153 / 264095 / 264554；generated 2026-07-21 |
| `2026-08/archive.sqlite3` | BSC 2026 August 四赛区：28 场已进行 series / 110 个已进行 set，零弃权；8 月月赛信号（87 英雄有样本；ban 前列 Bolt / Lumi / Max / Meg / Starr Nova） | Liquipedia revisions 268338 / 269181 / 269178 / 269180；generated 2026-08-24。冠军：FUT Esports / LOUD / Crazy Raccoon / Tribe |
| `pickrate.sqlite3` | Brawl Planet Legendary+ 全局 + **Ranked 池内 30 图**逐图 use/win rate，106 英雄全覆盖；池过滤自 2026-09-07 生效（`ranked_pool.json`，S48） | GCS `pl-l1-results.json.gz`；fetched 2026-09-07；window rolling_10_weeks；`summary.excluded_maps` 保留 5 张池外图审计记录（Canal Grande / Deathcap Trap / Last Stop / Penalty Kick / Snake Prairie） |

归档历史：
- 2026-07-13 两赛区（EMEA + SA）初版 observation profile 已被 2026-07 四赛区版**完整覆盖**，原 JSON 已删除（数据迁入 `2026-07/archive.sqlite3`）。
- 2026-08-14 EMEA 试点聚合信号已退役至 `outputs/_retired/`（当时当月未打完）；2026-08-24 四赛区打完后重建完整 8 月归档。
- 2026-08-24 存储层由 JSON 迁移为 SQLite（`archive.sqlite3` + `pickrate.sqlite3`）；`current.json` 指向 `2026-08`。
- 2026-09-07 pick 层加入 Ranked 池过滤：新增 `ranked_pool.json`（S48，30 图），`pickrate.sqlite3` 以池过滤口径整体重建（30 图，前快照 fetched 2026-08-24 的 33 图全梯数据由 git 历史保留）。
- `current.json` 当前指向 `2026-08`。

## 维护规则

- 每月赛区打完后：`analyze_esports_event.py --db wiki/environment/<YYYY-MM>/archive.sqlite3`（写入 profile + 逐 set 行列）；当月全部赛区打完再 `aggregate_environment_signal.py --profile wiki/environment/<YYYY-MM>/archive.sqlite3 --db wiki/environment/<YYYY-MM>/archive.sqlite3`（写入月赛信号）。
- pick 层刷新：`fetch_brawlplanet_pickrate.py --tier l1 --db wiki/environment/pickrate.sqlite3`（默认按 `ranked_pool.json` 只保留当前 Ranked 池：global 只累计池内 active 图，归档 per_map 只写池内行，池外图记入 `summary.excluded_maps`；`--no-ranked-pool-filter` 可取未过滤的天梯全量数据）。
- 赛季轮换时：先更新 `ranked_pool.json`（同步 [[syntheses/Ranked-Season-XX-地图Map-Profile总览|Season 索引页]] 的池清单与 provenance），再刷新 pick 层；manifest 指向源数据里已不存在的图时脚本会在 stderr 打 WARNING。
- 需要人类可读导出（审查 / git diff / 交付）时加 `--output` 写 JSON，不入 canonical 归档。
- 每次归档变更后更新 `current.json` 指针与 `index.md` 表格，并在 `wiki/log.md` 追加记录。
- 名称归一化：信号与归档内英雄名使用 `wiki/concepts/英雄名称归一化.md` 的 canonical name；future-only 英雄（如 Wendy）不入信号。
- 档案更新即触发 `compile` 重新折叠：新的 runtime index 会带上新 provenance，`manifest.pickrate_status` 反映信号状态。

## 消费边界

- `compile`（`compile_runtime_index.py --environment-manifest wiki/environment/current.json`）：唯一读取方，读 `archive.sqlite3` / `pickrate.sqlite3` 并折叠为 per-brawler `environment_evidence`（`ladder_anchor` / `monthly_finals`，带 window / rank_floor / fetched_at / captured_at 标注）与 `environment_ladder_per_map`。
- `decide`：只经 `query_runtime_facts.py` / `hydrate_runtime_facts.py` 读 index 内嵌证据；不直接读本目录。
- 外部应用可直接 `sqlite3 wiki/environment/2026-08/archive.sqlite3` 查询行列数据。
- 环境证据**永远不能**生成 tier、推翻机制约束、改变 fit / eligibility、升级 slot 资格。
