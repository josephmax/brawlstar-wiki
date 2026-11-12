# 版本更新流程

游戏版本变动后，知识库要做的全部事情都在这一页。四类触发器共用一条固定流水线和一个状态检查脚本；其他参考文档只讲各步骤内部怎么做，不再各自定义“版本更新要做什么”。

## 起手式

任何版本相关的维护，第一步和最后一步都是同一条命令：

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/version_status.py --online
```

它只读，列出三类结果：

- **错误**：账本或数据本身有问题（英雄名不是 canonical、处置状态非法、暂缓没写原因、晚于账本启用日期的补丁没有账本）。先修错误。
- **待办**：流水线里还没做完的步骤，逐条对应下文的步骤编号。
- **说明**：账本启用前的历史补丁等不需要处理的事实。

`--online` 额外对比三处上游：Fandom `Ranked` 页修订号（地图池）、Fandom `Version History/<年>` 页修订号（补丁）、Liquipedia 当年赛事页列表（赛事）。不带 `--online` 时只做离线检查。`--strict` 在仍有待办时返回非零，用于发布前把关。`--json` 输出机器可读结果。

维护完成的判据只有一条：`version_status.py --online --strict` 返回 0，或者剩余每一项都是写明原因的 `deferred`。

## 四类触发器

| 触发器 | 怎么发现 | 走哪些步骤 |
| --- | --- | --- |
| 平衡补丁或维护（含新技能、重做、芭菲） | `upstream_version_history_changed`，或官方更新说明有新条目 | 1 → 2 → 3 → 4 → 6 → 7 |
| 新英雄 | 官方说明的 NEW Brawlers，或 roster 与 Fandom 分类不一致 | 1 → 2（记为环境项）→ 5a → 6 → 7 |
| 排位赛季地图池轮换 | `upstream_ranked_page_changed` 或 `ranked_pool_stale` | 5b → 6 → 7 |
| 赛事结束（月赛、LCQ、世界总决赛） | `upstream_event_not_archived` 或 `esports_event_stale` | 5c → 6 → 7 |

十周滚动排位数据不是维护步骤。它由应用定时抓取；知识库只负责提供“哪个英雄在哪天被改过”和“当前地图池是什么”，应用据此决定数据是否可用（见“动态数据有效性”）。

## 固定步骤

### 步骤 1：抓取

- 官方更新说明完整原文存入 `raw/sources/supercell/`。
- 从原文列出全部受影响英雄（平衡、重做、芭菲、新极限充能），逐个重抓 Fandom 和 PLP：

```bash
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/capture_brawler_sources.py \
  --names Hank Shade "Mr. P" --sites fandom plp
```

完成判据：`version_status.py` 不再报 `raw_stale`。

### 步骤 2：立账

在该补丁的 `wiki/sources/` 来源页写两个 JSON 块：

- `balance_patch_manifest`：断点可计算的数值行，规则见 `balance-breakpoint-audit.md`。
- `version_fold_ledger`：本页定义的并入账本。官方说明里每个受影响英雄一行，`rows` 逐字抄官方原文，初始 `fold` 一律为 `pending`；地图、新英雄、排位规则变化写进 `environment`；只影响非排位玩法的改动写进 `excluded`。

完成判据：账本英雄数等于官方说明排位相关部分的英雄数；`version_status.py` 没有 `ledger_missing`、`ledger_incomplete`、`unknown_brawler`。

### 步骤 3：数值并入

- 按官方原文更新英雄页里的当前数值（YAML 文本里的数字和 `combat_breakpoint_profile`）。
- 运行断点审计并检查连续性，命令见 `balance-breakpoint-audit.md`。

完成判据：断点测试通过；审计的 current-state 一致性没有新增失配。

### 步骤 4：定性并入

逐英雄判断改动是否改变 BP 模型（`capability_vector`、`build_switches`、`map_feature_hooks`、`objective_contracts`、`failure_modes`、`conditional_matchups`、`slot_notes`）。重做和芭菲类改动必须按 `source-ingest.md` 的社区证据复查和 `balance-breakpoint-audit.md` 的能力成立型对位复核来做，不从补丁字面推断对位故事。

每个英雄处置完，把账本里的 `fold` 改成终态之一，并在 `note` 写一句依据：

| `fold` | 含义 | `note` |
| --- | --- | --- |
| `pending` | 还没处理 | 可空 |
| `partial` | 做了一部分 | 必填：做了什么、还差什么 |
| `model_changed` | BP 模型字段已改写 | 建议写改了哪些字段 |
| `numbers_only` | 只需更新数值，模型不变 | 建议写核对过的字段 |
| `no_model_change` | 核对后无需任何改动 | 建议写理由 |
| `deferred` | 明确暂缓 | 必填：原因和恢复条件 |
| `folded` | 已并入，但当时没有逐英雄分类（仅用于回填历史补丁） | 必填：依据的日志条目 |

处置状态只记在来源页的账本里。英雄页不写版本记录、补丁来源或“本次更新”段落。

完成判据：该补丁没有 `fold_pending`、`fold_partial`。

### 步骤 5：环境项

**5a 新英雄**：按 `source-ingest.md` 更新 roster、抓双源、建来源页和机制实体页；完整 BP profile 按 `brawler-modeling.md` 复核后才标 `bp_ready`。上线日期和排位资格写进 roster 来源页。完成后把账本里对应环境项的 `status` 改为 `done`。

**5b 地图池**：重抓 Fandom `Ranked` 页，更新 `wiki/environment/ranked_pool.json`（赛季号、地图清单、`source.revision_id`、`source.captured_at`）；新地图按 `map-modeling.md` 建来源页和地图实体页。完成判据：`ranked_pool_stale` 和 `upstream_ranked_page_changed` 消失。

**5c 赛事**：赛事打完后按 `esports-event-ingest.md` 抓取、ingest、分析并写入 `wiki/environment/<YYYY-MM>/archive.sqlite3`，更新 `current.json` 和 `wiki/environment/index.md`。月赛还要按 `environment-signal-ingest.md` 聚合月赛信号；其他赛事登记为 `observations`。没打完的赛事不归档。完成判据：`upstream_event_not_archived` 只剩尚未开赛的页面。

环境项的 `status` 取值：`pending`、`done`、`not_applicable`、`deferred`（必须写原因）。

### 步骤 6：校验

```bash
cd skills/brawl-stars-bp-knowledge-maintenance/scripts
python3 -m unittest discover -p 'test_*.py'
cd ../../brawl-stars-bp-slot-decision/scripts
python3 -m unittest discover -p 'test_*.py'
cd ../../..
python3 skills/brawl-stars-bp-knowledge-maintenance/scripts/version_status.py --online --strict
```

把核对过的 Fandom `Version History` 修订号写进最新账本的 `upstream.fandom_version_history_revision`，否则下次仍会提示上游有变化。

### 步骤 7：发布

1. 更新 `wiki/index.md`（仅当导航变化）并在 `wiki/log.md` 追加一条记录，写明补丁 ID、已结和暂缓的英雄数、环境项状态。
2. 提交知识库。
3. 应用侧执行 `python3 scripts/knowledge-workspace.py sync` 固定新的知识版本。英雄速查卡按知识版本自动重建，不需要手工生成。
4. 对账本里 `model_changed` 的英雄，在应用侧重放涉及它们的回归题。

## `version_fold_ledger` 字段

```json
{
  "version_fold_ledger": {
    "schema": "brawlstar.version_fold_ledger.v1",
    "patch_id": "2026-11-03-release",
    "effective_at": "2026-11-03",
    "official_source": "https://…",
    "raw": "raw/sources/supercell/….html",
    "upstream": {"fandom_version_history_revision": 222450},
    "brawlers": [
      {
        "brawler": "Hank",
        "kinds": ["balance"],
        "direction": "buff",
        "rows": ["Health increased from 5500 to 6000"],
        "fold": "numbers_only",
        "note": "survivability 与断点 profile 已改为 6000"
      }
    ],
    "environment": [
      {"id": "new_maps", "kind": "map_rotation", "status": "pending", "rows": ["…"], "note": "…"}
    ],
    "bug_fixes": ["…"],
    "excluded": [{"scope": "Brawl Arena Only", "brawlers": ["…"], "reason": "…"}]
  }
}
```

- `patch_id`、`effective_at` 与同页 `balance_patch_manifest` 一致。
- `brawler` 必须是 `wiki/entities/brawlers/` 的 canonical 页名；一个英雄一行，多类改动合并进 `kinds` 和 `rows`。
- `kinds`：`balance`、`buffie_rework`、`new_hypercharge`、`rework`、`new_gadget_or_star_power`。
- `direction`：`buff`、`nerf`、`adjust`、`mixed`、`new_kit`。它只是官方说明的分类，不是强度判断。
- `rows`：官方原文，逐字保留，不翻译、不合并。下游在改动尚未并入时会把这些原文直接展示给用户。
- `environment[].kind`：`new_brawler`、`map_rotation`、`ranked_rules`、`mode_rules`。
- `bug_fixes` 只作记录，默认不算英雄直接改动。某条修复确实改变了英雄的实战表现时，把它提升为 `brawlers` 里的一行。
- 新英雄还没有实体页时写进 `environment`，不写进 `brawlers`。

晚于 2026-09-16 的补丁必须有账本。更早的四个补丁只有断点清单，脚本把它们标为历史补丁，受影响英雄按清单识别，可能不完整。

## 动态数据有效性

系统里只有两份动态数据：十周滚动的传奇段排位统计，和最近一次归档赛事的选用、禁用、胜率。它们是否还能用，完全由账本决定，口径如下（2026-11-12 维护者决定，严格口径）：

- **排位统计**：窗口为最新比赛时间往前 70 天。某英雄在窗口起点之后有任何账本行（`brawlers` 里出现），该英雄的排位统计整体不展示，因为聚合数据无法拆出改动后的部分。窗口完全越过改动日期后自动恢复。
- **赛事统计**：赛事结束日早于某英雄的改动生效日，该英雄在这次赛事里的数据不展示。
- 其他英雄的改动不使本英雄的数据失效，只附一句环境提示。
- 数据被扣下时，下游必须说明是哪次补丁、附上账本里的官方原文行，并继续用英雄页的机制、构筑和对位事实作答。任何情况下都不允许以“版本未验证”为由不回答。
- 账本里 `pending` 或 `partial` 的英雄，下游在回答里注明“该补丁的改动尚未并入知识库”并展示原文行。

这条规则取代了 `wiki/environment/version_review.json` 的人工复核。那个文件暂时保留给尚未升级的应用版本读取，不再更新；应用升级后删除。

## 不做什么

- 不因为补丁生成强度等级、tier、地图适配或对位边；晋升规则仍以 `balance-breakpoint-audit.md` 和 `brawler-modeling.md` 为准。
- 不在英雄页保留版本历史。
- 不把 `outputs/` 下的审计产物当作知识库内容。
- 不为了让状态检查变绿而把没核对过的英雄标成 `no_model_change`；来不及做就写 `deferred` 和原因。
