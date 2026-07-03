# BP strength_profile tier list maker 调研

## 结论摘要

本次调研目标是为 BP `compile` 前的用户侧强度输入寻找一个可落地的 tier list 输入端：用户能够方便地制作 Brawl Stars 英雄强度 tier list，并把结果导出为可被后续 `strength_profile` / `runtime_bp_index` 编译流程消费的结构化数据。

当前没有找到一个完全开箱满足“内置 Brawl Stars 数据 + 用户可自由制作 tier list + 原生 JSON 导出按钮”的第三方站点。最可行方案是把 `TierListMaker.online` 作为 UI 底座，配一个薄 adapter 完成 Brawl roster 预填与 JSON 导入 / 导出。

推荐路线：

1. 使用 `MetaCoreTroll` 或本库 roster 生成 Brawl Stars 英雄模板。
2. 将模板写入 `TierListMaker.online` 的 `localStorage.tlm_v3`。
3. 用户在 `TierListMaker.online` 页面拖拽调整 tier。
4. 从 `localStorage.tlm_v3` 导出 JSON。
5. 将该 JSON 转换为 BP `strength_profile`。

## 验证产物

可追踪附件：

- [TierListMaker.online 完整 Brawl Stars 带图标导出 JSON](assets/tierlist-maker-research/tierlistmaker-online-brawlstars-full-image-export.json)
- [TierListMaker.online 完整 Brawl Stars 带图标截图](assets/tierlist-maker-research/tierlistmaker-online-brawlstars-full-image.png)
- [MetaCoreTroll brawler API 导出 JSON](assets/tierlist-maker-research/metacoretroll-brawlers-api-export.json)
- [MetaCoreTroll community tier list 导出 JSON](assets/tierlist-maker-research/metacoretroll-community-tier-list-export.json)

本地临时调研目录为 `outputs/tierlist-maker-research/`，但 `outputs/` 被 `.gitignore` 忽略；长期交接只依赖本页和上面的可追踪附件。

## 已调研站点

| 站点 | Brawl Stars 数据 | 制作 tier list | JSON / 结构化导出 | 判断 |
| --- | --- | --- | --- | --- |
| `TierMaker` | 有大量 Brawl Stars 模板 | 方便 | 未找到 JSON，偏图片 / 分享 | 不适合作为结构化输入端 |
| `Noff.gg` | 有 Brawl Stars 专用 maker | 理论上方便 | 有 `tl=` 分享参数，但实际访问被 Cloudflare 挡，未稳定验证 | 暂不采用 |
| `MetaCoreTroll` | 有 92 个 brawler 数据和社区榜 | 公开榜可看；个人榜依赖账号和投票历史 | 后端 Supabase 接口返回 JSON | 可作为数据源，不适合作为无门槛手工输入器 |
| `BrawlHub` | 有社区 tier list | 不提供本页内手工 maker | 未发现 JSON；投票转 Discord | 不采用 |
| `PL Prodigy` | 有 Brawl Stars tier list 页面 | 页面 headless 下停在 Loading | 未稳定拿到 tier 数据 JSON | 暂不采用 |
| `TierListMaker.online` | 无 Brawl Stars 内置模板 | 方便，支持拖拽和图片项 | 完整状态保存在 `localStorage.tlm_v3`，天然是 JSON | 作为 UI 底座可用，需要 adapter |

## TierListMaker.online 可用性

`TierListMaker.online` 官方模板页显示，图片项格式非常简单：

```json
{
  "id": "shiroko",
  "type": "image",
  "src": "/templates/blue-archive/shiroko.webp",
  "name": "Shiroko"
}
```

因此可将 Brawl Stars 英雄写成：

```json
{
  "id": "lumi",
  "type": "image",
  "src": "https://raw.githubusercontent.com/Brawlify/CDN/refs/heads/master/brawlers/borderless/160000XX.png",
  "name": "Lumi"
}
```

完整状态保存在浏览器：

```text
localStorage.tlm_v3
```

关键状态结构：

```json
{
  "title": "Brawl Stars Strength Profile - MetaCoreTroll Export",
  "logo": null,
  "tiers": [
    {
      "id": "s",
      "label": "S",
      "color": "#f87171",
      "items": [
        {
          "id": "lumi",
          "type": "image",
          "src": "https://raw.githubusercontent.com/Brawlify/CDN/refs/heads/master/brawlers/borderless/160000XX.png",
          "name": "Lumi"
        }
      ]
    }
  ],
  "library": [],
  "format": "square",
  "showLabels": true
}
```

已验证结果：

- 92 个 brawler 全部可写入。
- 图片项可正常渲染。
- tier 分布可保留在 JSON 中。
- 页面刷新后状态仍在同一浏览器 `localStorage` 中。

限制：

- 不支持账号云同步。
- 换浏览器、换设备、无痕模式或清理浏览器数据后不会保留。
- 我们在自动化浏览器中写入的状态不会自动出现在用户自己的浏览器中。
- 没有原生 JSON 导入 / 导出按钮，需要 adapter。

## MetaCoreTroll 可用性

`MetaCoreTroll` 是 Brawl Stars 专用站点，提供：

- 92 个 brawler JSON 数据。
- brawler 图标 URL。
- 职业、稀有度、各模式 Elo rating。
- 公开 community tier list。

局限：

- 个人 tier list 需要账号。
- 个人 tier list 需要投票历史，页面说明每个模式至少 50 票才能解锁个人榜。
- 不适合作为“打开即可拖拽”的手工输入器。

因此 `MetaCoreTroll` 更适合作为模板数据源或参考数据源，不作为最终用户输入 UI。

## 推荐 adapter 设计

最小闭环需要三个动作：

1. `import-template`
   - 输入：Brawl roster JSON 或本库英雄集合。
   - 输出：可写入 `localStorage.tlm_v3` 的 `TierListMaker.online` 状态。

2. `export-tierlist`
   - 从用户浏览器读取 `localStorage.tlm_v3`。
   - 保存为 `tierlistmaker-online-export.json`。

3. `convert-to-strength-profile`
   - 将 tier label 和 hero names 转为 `strength_profile`。
   - 第一版只需要表达全局强度 tier。
   - 后续再扩展 mode-specific / map-specific / confidence / notes。

建议第一版 `strength_profile` 保持简单：

```json
{
  "schema": "brawlstar.strength_profile.v1",
  "source": {
    "kind": "tierlistmaker-online",
    "captured_at": "2026-07-03"
  },
  "global_tiers": {
    "S": ["Lumi", "Kenji"],
    "A": ["Max", "Squeak"],
    "B": [],
    "C": [],
    "D": [],
    "F": []
  }
}
```

## 下一步

下一步应先实现一个轻量 adapter，而不是继续寻找完美第三方站点：

- 生成 `brawlstars-tierlist-template.json`。
- 生成一个可复制的 bookmarklet 或小 HTML 导入页，将模板写入 `localStorage.tlm_v3`。
- 生成一个导出脚本，把 `localStorage.tlm_v3` 转成 `strength_profile`。
- 用 1 份完整 92 英雄样例和 1 份用户手工调整样例验证转换结果。

完成这个闭环后，再决定是否把 adapter 固化进 `skills/brawl-stars-bp-slot-decision/` 的 `compile` 输入流程。
