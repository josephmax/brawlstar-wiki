# Fandom Raw Backfill Status

## 状态

当前知识库已经有大量 `wiki/sources/` 页面，但过去的工作流没有先把原始网页回填到 `raw/`。

这份文件用来记录回填进度。

## 已回填样板

- `systems/brawl-stars-wiki-home.md`
- `gameplay/credits.md`
- `modes/gem-grab.md`
- `heroes/shelly.md`
- `systems/ranked.md`

## 当前覆盖

- 当前 `wiki/sources/` 中的既有页面，已全部拥有对应的 `raw/` 回填文件。
- 对于首批手工样板，采用 `manual raw capture`。
- 对于历史遗留来源，采用 `provisional raw backfill`，并在文件中显式注明来源于已有 `wiki/sources/` 摘要页。
- 当前目录已按 `heroes / modes / gameplay / systems` 重新归位，避免英雄与模式混入系统目录。

## 回填策略

1. 先回填高频入口页和代表性页，建立格式样板
2. 再按主题批量补：
   - 英雄
   - 模式
   - 资源与系统
   - 排位与俱乐部
3. 新 ingest 默认先落 `raw/`，不再只写 `wiki/`

## 备注

现阶段允许 `wiki/` 比 `raw/` 更完整；但从本次补正开始，目标是逐步把差距补平。
