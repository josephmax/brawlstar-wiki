# Fandom 学习与摄取路线图

这份路线图定义我们如何把 Brawl Stars Wiki 的内容，按人类阅读顺序逐批沉淀进本地 LLM Wiki。

## 目标

- 不追求一次性搬空全站
- 追求稳定的“读一批、整理一批、索引一批、剪枝一批”节奏
- 优先让本地 wiki 长出可导航的概念骨架

## 双 Agent 分工

### 主 Agent

- 负责阅读外部站点
- 先建立站点宏观地图
- 再按主题批量学习
- 决定某条知识应进入哪个本地页面

### 子 Agent

- 负责把已经确认的知识，沉淀为本地 wiki 页面
- 更新 `wiki/index.md`
- 维护链接结构与日志
- 避免伪造主 agent 尚未读取的内容

## 批次顺序

### Phase 0. 站点地图

- 主页
- All Pages
- `Category:Brawlers`
- `Category:Events`
- `Category:Gameplay`

产出：

- 来源页：站点地图
- 综述页：学习与摄取路线图

### Phase 1. Gameplay 基础概念

优先条目：

- `Credits`
- `Coins`
- `Power Points`
- `Gems`
- `Trophies`
- `Bling`
- `Starr Drops`
- `Brawl Pass`
- `Daily Streak`
- `Gears`

产出：

- `wiki/concepts/` 下的基础概念页
- 一页总览型综述，例如资源系统综述

### Phase 2. Events 玩法系统

优先条目：

- `Gem Grab`
- `Brawl Ball`
- `Knockout`
- `Showdown`
- `Ranked`
- `Challenges`

产出：

- 模式机制页
- 模式比较页

### Phase 3. Brawlers 角色体系

顺序建议：

1. 先建立“英雄定位”“稀有度”“职业分类”等概念页
2. 再按稀有度或职业批量 ingest 角色页
3. 每批 ingest 后做一次轻量 lint

## 节奏建议

- 每批处理 3 到 10 篇页面
- 每批结束后：
  - 更新 `wiki/index.md`
  - 更新 `wiki/log.md`
  - 检查是否出现重复概念或页面边界混乱

## 什么时候算“没有新的知识可以输入”

不是指全站完全读完，而是当前批次内：

- 新页面只是在重复已知定义
- 新内容更适合补充旧页而不是建新页
- 新页面不再显著改变知识结构

这时就进入下一层级，或者转入剪枝与重构。

## 剪枝规则

- 两个页面长期解释同一概念时，考虑合并
- 单页过大时，拆成概念页加综述页
- 高波动内容优先保留在来源页或专题页，不急着抽象成核心概念

## 当前推荐下一步

从 `Gameplay` 开始，优先 ingest 基础资源与成长系统。
