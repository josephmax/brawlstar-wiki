# BP skill 的 GEPA 最小接入

本目录的 `gepa_trial.py` 使用官方 `gepa==0.1.4`。候选参数只是一段附加到现有 BP skill 后的**通用决策补充规则**；它不会改写正式 skill、知识实体、编译索引、题卡或私有标签。当前只用于验证自动调优链路，不发布 BP 质量提升结论。

## 范围与隔离

- 运行前用 `prepare_eval.py` 将公开题面和中性事实暂存到 `outputs/`。模型请求只包含 `system.txt`（现有 BP skill + 候选规则）和单题 JSON；`labels.draft.jsonl` 仅在评分进程内读取。模型没有文件或工具接口。
- 暂用 `practice-001-1`、`practice-003-1` 训练，`practice-006-1` 验证。三题只检验接入和反馈路径，标签是 `draft_not_gold`，不能作为泛化证据。完整评测仍需按 `analysis/EVALUATION-PROTOCOL.md` 和 `practice/README.md` 做视频分组、审题和独立盲测。
- 评分为各选项草稿分档准确率 70% + `best` 集合 F1 30%。格式、选项遗漏或重复得到 0。错误返回每个选项的预期/实际和草稿解释，供 GEPA 反思。该分数仅用于接线试验，不代表当前 BP 质量。
- `outputs/` 保存每次模型答卷、使用量、候选/实际系统输入哈希、GEPA 记录和最佳候选；不进入 git。候选绝不自动写回正式 skill。
- 真实调用会将 BP skill 和知识索引派生的机制卡发给所配置的外部模型。启动前必须确认该数据可以发送到所选服务及账号。2026-09-24 用户已明确授权向项目配置的 GLM 目的地进行本次试跑；结果见下方记录。

## 准备

在知识库仓库根目录执行，确保 `outputs/` 是忽略目录：

```bash
UV_CACHE_DIR=/tmp/bp-gepa-uv-cache uv venv /tmp/bp-gepa-venv
UV_CACHE_DIR=/tmp/bp-gepa-uv-cache uv pip install --python /tmp/bp-gepa-venv/bin/python 'gepa==0.1.4'
python3 evals/bobbybs-draft-quiz/practice/prepare_eval.py \
  --index outputs/runtime-bp-index/default-runtime-index.json \
  --out outputs/bp-gepa/stage
```

`prepare_eval.py` 已在 2026-09-24 实际暂存 56 个无标签题卡，校验了真实 query/hydrate。索引过期时先按 BP skill 的 compile 流程重编，不能把旧索引当当前事实。

## 真实试跑命令

在数据传输边界确认后，从环境变量提供模型密钥；命令及结果不得包含密钥。示例模型和地址可按实际已授权目的地替换：

```bash
/tmp/bp-gepa-venv/bin/python evals/bobbybs-draft-quiz/practice/gepa_trial.py \
  --stage outputs/bp-gepa/stage \
  --labels evals/bobbybs-draft-quiz/practice/labels.draft.jsonl \
  --out outputs/bp-gepa/trial-001 \
  --model glm-5.3-flash \
  --base-url https://open.bigmodel.cn/api/paas/v4 \
  --key-env GLM_API_KEY \
  --max-metric-calls 6 \
  --max-candidate-proposals 1
```

可选 `--env-file` 从本地未入库文件读取密钥，仅用于有意选定的本地环境。先看 `config.json` 与 `call-*.json`：应能对上候选哈希和 `effective_system_sha256`，每题有真实答案、评分反馈和 token 记录。`summary.json` 的 `candidate_changed` 只表示优化器生成了不同文本，不代表 BP 能力提升；必须审阅候选并在更大、经审订的集合上独立验证。

## 已完成的离线自检

- 官方 GEPA 在无网络 toy evaluator 上完成一次候选提案，验证集分数由 0 变为 1；这是引擎接线检查，与 BP 质量无关。
- 评分器用真实题卡结构和草稿标签检查：全对为 1，故意错一项为 0.86，漏项为 0。
- 先前外部请求曾因数据传输授权不明确被自动审批拦下；用户随后明确授权，本次才实际尝试在线请求。

## 2026-09-24 真实试跑结果

已使用项目配置的 `glm-5.3-flash` 发出实际请求。完整暂存输入的第一题约为 61KB skill 文本 + 题卡/事实 64KB；模型持续无响应，人工中止。随后仅使用源 skill 的核心边界和运行规则片段（12KB）及两道较短题，仍在首题等待中人工中止。第三次将单题请求缩到约 6KB 规则 + 14KB 中性题卡，仍未及时返回，人工中止。此前同目的地约 15 字的连通检查能在数秒内返回，说明密钥和目的地本身可用，但不能证明长 BP 请求可用。

三次均未收到可评分 BP 输出，GEPA 没有完成在线候选提案，也没有任何真实 BP 分数。上述“缩小版”只用于诊断调用尺寸，不能当完整 skill 评测。原脚本的 socket 空闲超时无法限制完整墙钟时间；现已改为每次模型调用 90 秒墙钟上限，超时后写失败记录并中止整轮搜索，不再盲目重试。需先确认服务端对长请求和输出预算的实际响应，再恢复在线优化。
