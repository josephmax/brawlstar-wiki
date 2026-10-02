# Brawl Planet 版本适用性复核：2026-10-03

## 来源和原始捕获

- 排位来源：https://www.brawlplanet.com/powerleague/pl-l1
- 数据：https://storage.googleapis.com/brawlanalyzer-public/pl-l1-results.json.gz
- 官方更新列表：https://supercell.com/en/games/brawlstars/blog/
- 官方维护：https://supercell.com/en/games/brawlstars/blog/release-notes/release-notes-august-2026/
- 不可变材料：`raw/sources/version-review/2026-10-03/`；provenance.json 保存 URL、抓取时间、SHA-256、Last-Modified。旧抓取不改写。

## 已核实与缺口

本次官方列表及发布说明核查到的最近相关维护仍是 September 16；未据此声称不存在未收录公告或全量英雄再次审计。已有 [[Fandom-Maintenance-September-16-2026]] 保存补丁账本，本次没有新增已证实的数值改动，不重写稳定英雄机制。

源仍为 Legendary only，返回 37 图、33 个 active 标记、源级 total_matches=6010835。固定 S49 池 26 图均在源中，11 张池外图排除，归一化覆盖 106 英雄。源级总数不是筛选后的英雄选用分母。S49 是本库固定池；这次没有独立验证十月当前游戏池，不能将覆盖齐全说成当前赛季验证通过。

仍只有 latest_match_time 等汇总字段，缺少完整样本起止及补丁分段。不得根据最新比赛或重新抓取时间生成补丁后胜率。`current_version_evidence=false` 如实保留。

## 消费策略更新

usable_for：展示来源最新返回的传奇统计、固定池覆盖、混合/未知窗口的描述性观察；必须就地标明范围。

not_usable_for：把十周混合统计或历史月赛直接当当前补丁强度/星级证据、推算补丁后胜率、声称覆盖传奇以上或当前游戏地图池。

此前消费者将证据不充分表现为查询不可用，且用 24 小时和逐快照哈希重复锁定。新增 `consumption_policy` 将查询可用性与当前补丁证据分开：允许描述性查询；快照哈希只用于精确证据归属，不作为滚动数据展示开关。维护过期应披露复核日期和缺口，不应拒绝返回实际查询数据。

## 维护闭环

更新归档、指针、版本复核、maintenance/runtime references 和契约测试。新补丁、Buffie/新英雄/规则或地图变化、来源口径变化触发重新维护；仅抓取更新不能刷新补丁有效性。若将来提供独立补丁后样本，再维护精确窗口证据。此前 [[Brawl-Planet-版本适用性复核-2026-09-30]] 保留为历史来源。
