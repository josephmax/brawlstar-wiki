# Brawl Stars BP Agent Prompts

本仓库维护《荒野乱斗》BP 知识库、一套知识维护 skill 与两个运行 skill：

- `brawl-stars-bp-knowledge-maintenance`：维护 skill，负责 source ingest、英雄/地图稳定事实建模、审计和 runtime 边界治理。
- `run-brawl-stars-bp`：裁判 skill，只负责发牌、维护隐藏信息、cue 流程、记录选手提交内容和回合指标。
- `brawl-stars-bp-slot-decision`：选手 BP skill，负责先编译 `runtime_bp_index`，再基于该索引对单个 ban / pick slot 做决策。

## 如何使用

运行侧主要使用两个 skill：`run-brawl-stars-bp` 负责开局和裁判编排，`brawl-stars-bp-slot-decision` 负责单手 ban / pick 决策。

### 使用裁判 skill 开一局 BP

```text
使用 $run-brawl-stars-bp 开一局 Ranked BP 模拟，地图从当前 Ranked 地图池里随机选。

跑完整局后给我报告。
```

如果想固定双方风格，可以这样说：

```text
使用 $run-brawl-stars-bp 在 Center Stage 开一局 BP。

blue_strategy_bias: balanced
red_strategy_bias: aggressive

其他流程按 skill 默认规则执行。
```

### 直接调用 BP skill

```text
使用 $brawl-stars-bp-slot-decision compile 当前版本默认强度索引。

地图池用当前 Ranked 地图池，英雄池用当前 BP-active 英雄集合。
我没有额外强度表；请按当前稳定 wiki 事实做默认版本理解，不要凭记忆补 tier。

产出 runtime_bp_index，后续 decide 都用这个索引。
```

如果要带用户自己的强度理解，可以预留成这样。这个能力还在开发中，当前先作为输入格式占位：

```text
使用 $brawl-stars-bp-slot-decision compile，并使用我提供的强度理解。

strength_profile:
- Spike 在 Gem Grab 里按 A 级处理，理由是当前版本中距控图稳定。
- Max 在开阔图按 A 级处理，但遇到硬控路线时证明门槛提高。
- Jacky 当前版本按低优先级处理，除非地图明确有墙边接触和目标收益。

请把这些只作为 strength layer，不要改写英雄或地图稳定事实。
```

做单手决策时这样调用 `decide`：

```text
使用 $brawl-stars-bp-slot-decision decide 帮我判断这一手怎么选。

当前局面：
- Double Swoosh，Gem Grab
- 我方蓝队，当前是 4-5 两手
- 我方已有 Gene
- 对面已有 Max、Sandy
- 已 ban：Kenji、Moe、Rico、Lily、Angelo、Sprout
- strategy_bias: aggressive
- 我没有额外版本强度表；强度来源先按 unknown 处理

给我 2-4 个候选组合，说明首选、备选、各自解决什么问题、会暴露什么风险，以及对面最后一手最需要防什么。
```

`decide` 会自己先做 runtime index 预检查：已有可用索引就直接用；没有索引就由一个进程上锁并执行默认 `compile`；其他并发 `decide` 只轮询等待，超出重试次数会失败退出，不会一直卡住。

## 拓扑信息

本仓库当前维护三类 BP skill：知识维护、选手决策、裁判编排。三者共享同一套资料层，但运行边界不同：维护 skill 生产稳定英雄/地图事实；选手 skill 把稳定事实编译成运行时索引并做单手决策；裁判 skill 不做 BP 判断，只编排对局并记录选手提交。

### `brawl-stars-bp-knowledge-maintenance`

维护 skill 负责把来源资料整理成稳定 BP 事实。它不直接生产 pick/ban 决策，也不把 BP 维护结果写成概念页或专题页；它的核心产物是给 `compile` 消费的英雄页和地图页。

```mermaid
flowchart TD
  A["原始资料<br/>(raw/)"] --> B["来源摘要<br/>(wiki/sources/)"]
  C["英雄/地图/名单/补丁来源<br/>(raw/sources/)"] --> B
  D["维护规则<br/>(skills/.../references/)"] --> E["知识维护命令<br/>$brawl-stars-bp-knowledge-maintenance"]
  B --> E

  E --> F["英雄稳定事实<br/>(wiki/entities/brawlers/)"]
  E --> G["地图稳定事实<br/>(wiki/entities/maps/)"]
  E --> H["审计和临时产物<br/>(outputs/)"]
  E --> I["运行规则修订<br/>(skills/*/references/)"]

  F --> J["供索引编译消费<br/>slot-decision compile"]
  G --> J
  I --> K["供运行 skill 执行<br/>slot-decision / run-bp"]
  H --> L["供维护者复核<br/>不进入 runtime"]

  classDef command fill:#f6d365,stroke:#8a5a00,stroke-width:2px,color:#111;
  class E command;
```

### `brawl-stars-bp-slot-decision`

选手 skill 有两个主命令：`compile` 生成本局可消费的能力索引，`decide` 用索引和当前 BP 状态输出 ban/pick 推荐。当前 `bp_index.py` 只是定位稳定页面的辅助工具，不是完整 compiler。

```mermaid
flowchart TD
  A["编译输入<br/>patch、地图池、可用英雄、强度理解"] --> B["主命令：compile<br/>生成 runtime_bp_index"]
  C["编译规则<br/>(references/compile-knowledge.md)"] --> B
  D["地图稳定事实<br/>(wiki/entities/maps/)"] --> B
  E["英雄稳定事实<br/>(wiki/entities/brawlers/)"] --> B
  F["强度输入<br/>(strength_profile)"] --> B

  B --> G["运行时能力索引<br/>(runtime_bp_index)"]
  G --> H["临时索引文件<br/>(outputs/ 或调用方路径)"]

  I["决策输入<br/>slot、双方 picks、bans、候选池、策略偏好"] --> N["索引预检查和锁协调<br/>(scripts/runtime_index_precheck.py)"]
  H --> N
  N --> J["主命令：decide<br/>输出当前手推荐"]
  N -.缺索引时触发默认编译.-> B
  K["决策规则<br/>(references/runtime-decision-knowledge.md)"] --> J

  J --> L["BP 推荐<br/>候选评估、hard gate、职责覆盖、风险和 top decisions"]
  M["页面定位辅助<br/>(scripts/bp_index.py)"] -.辅助查页.-> B
  M -.不是 compiler.-> G

  classDef command fill:#f6d365,stroke:#8a5a00,stroke-width:2px,color:#111;
  class B,J command;
```

### `run-brawl-stars-bp`

裁判 skill 负责读取对局配置、启动选手子 agent、维护隐藏信息和写报告。它不读取英雄/地图页面做自己的 BP 判断；所有 ban/pick 理由都来自选手侧 `brawl-stars-bp-slot-decision`。

```mermaid
flowchart TD
  A["对局配置<br/>map、mode、模型、策略偏好、pick 顺序"] --> B["主命令：run BP<br/>裁判编排"]
  C["报告规则<br/>(references/match-report-schema.md)"] --> B
  D["报告渲染器<br/>(scripts/render_match_report.py)"] --> B

  B --> E["同步 ban<br/>隐藏信息、允许重复 ban"]
  E --> F["不可用池<br/>unique bans"]
  F --> G["按顺序发起回合<br/>蓝1、红2-3、蓝4-5、红6"]

  G --> H["选手子 agent<br/>调用 slot-decision"]
  H --> I["选手执行<br/>precheck / compile -> decide"]
  I --> J["选手提交<br/>ban/pick、理由、build、风险、备选"]
  J --> B

  B --> K["对局报告<br/>(outputs/bp-simulations/)"]
  K --> L["可选维护摘要<br/>只做人工沉淀，不是 runtime 输入"]

  classDef command fill:#f6d365,stroke:#8a5a00,stroke-width:2px,color:#111;
  class B command;
```

## 维护命令示例

维护侧使用 `brawl-stars-bp-knowledge-maintenance`。它适合补抓来源、整理 source summary、升级英雄/地图稳定事实、跑审计和维护 runtime 边界。维护前先读 `AGENTS.md`、`wiki/index.md` 和该 skill 的相关 reference。

### 维护某个英雄的 BP 资料

```text
使用 $brawl-stars-bp-knowledge-maintenance 更新 Brock 的 BP 资料。
```

这就够了。来源检查、source summary、英雄实体页、审计和日志都是 skill 内化流程。只有当你有明确关注点时，再加一句：

```text
使用 $brawl-stars-bp-knowledge-maintenance 更新 Brock 的 BP 资料，重点看构筑和对位信息。
```

### 维护某张地图的 BP 资料

```text
使用 $brawl-stars-bp-knowledge-maintenance 更新 Center Stage 的 BP 地图资料。
```

如果你想指定关注点，可以这样说：

```text
使用 $brawl-stars-bp-knowledge-maintenance 更新 Center Stage 的 BP 地图资料，重点看中场路线和球门入口。
```
