# Fandom Raw Capture Rules

这个目录保存从 Brawl Stars Fandom 回填或新增的网页原始抓取件。

## 目的

- 为 `wiki/sources/` 提供上游原始证据
- 让后续能够重查页面原文、对比页面变动、重跑 ingest
- 让 `raw/ -> wiki/sources/ -> wiki/entities|concepts|syntheses/` 三层闭环成立

## 目录约定

- `heroes/`：英雄页面抓取件
- `modes/`：模式页面抓取件
- `gameplay/`：货币、成长、资源、道具等页面抓取件
- `systems/`：总览、排行、活动、制度性页面抓取件

## 文件格式

每个抓取件至少包含：

1. 页面标题
2. 原始 URL
3. 抓取日期
4. 抓取类型
5. 原文可见片段
6. 备注，例如是否只是首批回填样板

## 说明

由于当前是从外部网页直接 ingest 回填，本目录中的首批文件采用 `raw capture` 形式，
即保存页面关键可见原文与页面元数据，而不是完整 HTML 镜像。

后续如果需要更严格的归档，可以在此基础上继续补完整导出版本。
