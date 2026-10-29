# IMteacher —— 交互式精通教学法 Skill

**IM（Interactive Mastery）教学法**：面向大学理工科（编程 / 算法 / AI-ML / 系统 / 数学）的
AI 系统教学技能。适用于"把一门课、一个单元**教会我**"这类系统性学习任务，而不是单题答疑。

目标是**精通，不是完成**——学习者能独立重做、能讲清为什么、错了知道错在哪一层。

## 核心机制

| 机制 | 一句话 |
|------|--------|
| 诊断优先 | 开单元先定位学科→知识体系→缺口，查前置对账单，缺什么先补什么 |
| teach-check-continue 硬节奏 | 小块讲解（一次一个概念）→ 检查点 3-8 题 → **通过才前进** |
| 错误分类学 | 批改不是打分是分诊：拼写/API 类、约定类、结构类、概念类、静默类，分类施治 |
| 代码三段式 | 读码标注 → 填空 → 终局手搓（只给任务书独立写整段），跳段 = 背代码不是会代码 |
| 实敲预测-对账 | 机器能跑就亲手跑：先预测再执行，预测与输出一起交，数据说话 |
| 留痕 + 画像双账 | 留痕记"学到哪"（跨会话续接），画像记"怎么教最有效"（有效类比/失效讲法/病灶疗法，跨单元复利） |
| 滚动回顾 + 每周小测 | 错题池 + D-1/D-3/D-7 间隔复习；单元收官前小测验收，"讲过没考过"必补考 |
| 多线并行 | 一线一对话一文件；盘点六节模板（漏线 = 教学事故）；线 × 每日分钟时间预算 |
| 日开 + 任务看板 | 每天第一次学习自动出当日计划表，对话末尾挂任务看板到清空 |

## 安装

### Claude Code

```bash
git clone https://github.com/dingking928151/IMteacher.git
cp -r IMteacher ~/.claude/skills/
```

Windows（PowerShell）：

```powershell
git clone https://github.com/dingking928151/IMteacher.git
Copy-Item -Recurse IMteacher "$env:USERPROFILE\.claude\skills\"
```

装好后对 Claude 说"用 IMteacher 教我 XXX"或"开始 Week 1"即触发。

### 其他 Agent / 任意对话框

纯 Markdown、零依赖、无脚本。把 `SKILL.md` 全文贴进 system prompt 即可；
`references/` 是按需加载的详细规程（检查点题型库、留痕模板、画像模板、回顾规程等），
讲哪块贴哪块。

## 使用方式

1. **开新单元**：直接说"用 IMteacher 教我《操作系统》文件系统这一章"，它会先诊断
   前置、建留痕文件、确认你的机器能不能实跑，然后按小块讲解 + 检查点推进。
2. **续课**：换会话/隔天回来，说"继续上课"，它读留痕文件从第一个未过项续接，
   开场先来 2-3 道滚动回顾。
3. **多门课并行**：每条学习线开一个专属对话，各线留各自的留痕文件，盘点时自动全景。

## 文件结构

```
IMteacher/
├── SKILL.md                     # 主规程：开场五件事、教学循环、错误分类学、九大机制
└── references/
    ├── teaching-loop.md         # 讲解深度控制、批改格式、约定冲突调解、三犯换表征
    ├── code-three-stage.md      # 代码三段式各段规格与终局手搓模板
    ├── hands-on-mode.md         # 实敲任务设计、预测-对账纪律、debug 教学
    ├── checkpoint-bank.md       # 检查点题型库（11 种题型）与出题原则
    ├── record-keeping.md        # 留痕文件模板（知识地图/流水/错题池）与更新时机
    ├── learner-profile.md       # 学习者画像模板与更新规则
    ├── quiz-and-review.md       # 每日滚动回顾、每周小测、错题池规程
    └── multi-line-review.md     # 多线对话分工、盘点六节模板、时间预算
```

## 来源与致谢

方法内核受 [universal-diagnostic-tutor-skill](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill)
（诊断式教学：先找缺口、再选下一步最值得教的内容）启发，在此之上经多周次系统教学实战
打磨出 IM 流程（硬节奏检查点、代码三段式、实敲对账、双账续接）。教学原则参考认知科学
研究（生成效应、预测学习、间隔重复、认知负荷管理），关键处已在文中注明依据。

## License

MIT
