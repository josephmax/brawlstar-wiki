# Brawl Planet 版本适用性复核：2026-09-30

## 来源与原始材料

- 数据页：https://www.brawlplanet.com/powerleague/pl-l1
- 数据文件：https://storage.googleapis.com/brawlanalyzer-public/pl-l1-results.json.gz
- 官方补丁对照：https://supercell.com/en/games/brawlstars/blog/release-notes/release-notes-august-2026/
- 不可变抓取：`raw/sources/version-review/2026-09-30/` 的页面、ladder.json、brawlers.json；provenance.json 保存 URL、UTC 抓取时间、SHA-256 和 HTTP Last-Modified。
- 既有补丁账本：[[Fandom-Maintenance-September-16-2026]]；本次官方页仍包含 September 16 维护段。未发现可据此将统计窗口认定为补丁后的证据；不声称已重新审计所有英雄机制。

## 核查结果

- 源站明确各段位独立计量，l1 只覆盖传奇本段。撤销旧的传奇及以上解释，保留历史记录并标为已被替代。
- GCS 返回 37 张图，其中 33 张 active。固定 S49 池的 26 张图全部存在；池外 11 张图排除。active 图含旧轮换，不把 active 等同于游戏当前地图池。
- 归档按固定池生成，覆盖 106 个可归一化英雄。summary.map_entries、active_maps、total_matches 是源文件级审计字段，不是筛选后英雄分母。逐图 match_count 是地图对局量，不是某英雄选用次数。
- payload 字段包含 individual / teams / mode / modeFormatted / map / match_count / active / latest_match_time / recent_match_count。没有完整样本起点、独立补丁 ID 或补丁后分段。latest_match_time 只能说明最后一场；recent_match_count 没有足够窗口契约，不能推导补丁后胜率。
- 更新 `wiki/environment/pickrate.sqlite3`、`current.json` 和 `version_review.json`。`current_version_evidence` 保持 false；这是完成复核后的缺口，不是漏跑维护脚本。

## 适用边界

usable_for：源站当前返回统计的来源/段位说明、固定地图池覆盖核查、混合窗口描述性统计、维护缺口定位。

not_usable_for：当前补丁强度/星级/选人排序、传奇以上完整覆盖、仅根据最后比赛日期认定整个样本新鲜、用抓取日期代替比赛起点。

当消费者允许展示混合窗口统计时，仍需就地标明范围。该展示策略与 current_version_evidence 是两个不同判断；不能为了通过校验而修改已知事实。

## 下次维护

先查最新官方补丁和赛季来源，再抓取并检查源字段；保留旧 raw，新增捕获。发现上游提供精确样本分段后，核实段位、分母和样本全部位于相关补丁之后，才能生成肯定适用性记录。没有这种证据时复核结论仍为缺口，不循环重试同一数据。
