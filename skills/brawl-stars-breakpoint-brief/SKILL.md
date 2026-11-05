---
name: brawl-stars-breakpoint-brief
description: 将荒野乱斗平衡补丁的机制亮点与 balance_breakpoint_audit.v1 结果制作成头像主导、可编辑的单屏 HTML 视觉快报并导出 PNG；适用于用户要求展示既有断点审计，数值计算和知识维护交由断点审计流程。
---

# 平衡断点视觉快报

先读取仓库 AGENTS.md 和断点审计 skill 的 `references/balance-breakpoint-audit.md`。断点只呈现现有 `balance_breakpoint_audit.v1`；机制亮点须来自经核对的官方补丁或可靠来源并显式人工编辑，不能自动声称审计完整、生成对位或强度结论，也不能将一次性/资源限制攻击变成连续发数。

以 Chosen Network 的紧凑分栏、头像优先、明确数值和颜色编码为视觉参考；不要复用其 logo、署名或图像。标题应标示版本、PL11、满盾口径；头像缺失按项目头像维护流程补齐，无法补齐则明确失败，禁止以占位图冒充完成。提供有名字的 hover/文本替代，避免头像歧义。对 exact-boundary 标记核验、对同补丁同时变化的目标标记联合驱动。

## 工作流

1. 确定补丁并读取对应机器账本（`outputs` 可重生成，不将它当持久知识源）。若缺失，先依照断点维护 skill 的完整版本链命令生成，不得编造；指出版本及审计本身的排除项和覆盖范围。
2. 区分攻击变化和受击变化：攻击包本身变化时按攻击方分组；生命或减伤变化时按受击方分组，展示哪些攻击包所需次数改变，不让未改伤害的攻击者各占卡片。同一关系若双方都变化可在两区出现并标记联合驱动。不要按命中次数、差值或数值规模排除任何变化。
3. 读取补丁公告，人工识别共同机制改动和其他非数值重点，写入独立的 patch-specific editorial JSON，附来源及具体英雄。审计 JSON 的排除项不是公告的完整替代；用户指出麦乐迪等以直击作为击杀方式价值有限，可以用人工编辑把该攻击包压缩成摘要，全部目标与次数保留在 HTML 详细表。未人工复核时不要伪装为智能重要性排序。
4. 图片可读性与容纳量发生冲突时，优先保证可读，不可静默省略、折叠或缩字到不可读。明确展示概览范围和完整数据入口；用户要求所有状态同时在图上时，可制作多屏或高分辨率长图并声明权衡。
5. 检查输入事件数、渲染明细行数、头像完整性、特殊条件、等值舍入和联合变化；打开 HTML 和 PNG 做视觉检查。提供二者路径、纳入范围和未展示在 PNG 的数据。

```sh
python3 skills/brawl-stars-breakpoint-brief/scripts/render.py \
  --audit outputs/balance-breakpoints/<audit>.json \
  --portraits /Users/bytedance/projects/skill-chat-agent/public/brawl-assets/brawlers \
  --manifest-source wiki/sources/<patch-source>.md \
  --editorial <patch-editorial.json> \
  --output-dir outputs/balance-brief/<patch> --title '版本断点快报' \
  --chrome '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
```

没有 Chrome 时生成 HTML 并报告 PNG 缺失；不要使用 AI 绘图生成数值或头像。`outputs/` 临时产物不写入 wiki 作为长期依赖；用户要求持久保存时另选明确路径。

11 月示例人工审校配置见 [2026-11-editorial.json](references/2026-11-editorial.json)；只适用于该补丁，不得套用于其他版本。未提供配置时应标明机制亮点尚未人工整理，不能静默宣称完整。
