# Strength Profile Editor

本工具是本地 `strength_profile` 输入端，用来编辑 Brawl Stars BP `compile` 前的三层强度理解：

- 通用强度
- 模式强度
- 地图强度

导出的 profile 按 `global`、`mode`、`map` 三种 scope 独立保存强度理解。地图强度需要显式维护；通用强度只表达版本先验，不能当作地图适配性证明。

导出前会做完整性校验：

- `global` 必须排完全部 104 个英雄。
- 已填写的 `mode` / `map` profile 也必须排完全部 104 个英雄。
- 不允许 `Unknown` 档位。
- 校验通过后会下载 JSON，并把同一份 JSON 写入剪贴板，用户可直接粘贴到 agent 客户端。

## 启动

从仓库根目录启动静态 server：

```bash
python3 -m http.server 4173
```

然后打开：

```text
http://localhost:4173/tools/strength-profile-editor/
```

## 更新数据

编辑器数据来自本库 wiki：

- 英雄：`wiki/entities/brawlers/*.md`
- 别名：`wiki/concepts/英雄名称归一化.md`
- 地图：`wiki/entities/maps/*.md`
- 远端图片：`wiki/syntheses/assets/tierlist-maker-research/*.json`
- 最新头像补齐：`tools/strength-profile-editor/data/brawlapi-brawler-images.json`

重新生成 catalog：

```bash
python3 tools/strength-profile-editor/scripts/generate_catalog.py
```

## 生成排位地图强度底稿

从已编译的 `runtime_bp_index` 生成一份可导入本编辑器的地图级 `strength_profile`：

```bash
python3 tools/strength-profile-editor/scripts/generate_map_strength_profile.py \
  --repo . \
  --base-profile skills/brawl-stars-bp-slot-decision/references/default-strength-profile.json \
  --runtime-index outputs/runtime-bp-index/default-tierlist-all-maps-thin.json \
  --output outputs/strength-profiles/ikaoss11-ranked-map-adapted-preview.json
```

生成结果保留 iKaoss global tier list 作为 `global`，并为当前 Ranked 地图池的每张地图补齐完整 104 英雄 `map` profile，方便逐图预览和人工细调。

## 测试

```bash
python3 tools/strength-profile-editor/scripts/test_generate_catalog.py
python3 tools/strength-profile-editor/scripts/test_generate_map_strength_profile.py
/Users/bytedance/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node tools/strength-profile-editor/scripts/test_profile_core.mjs
```
