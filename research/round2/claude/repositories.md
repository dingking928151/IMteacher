# 第二轮 GitHub 项目报告（3 项目）

- 取证人：Claude Code ｜ 日期：2026-11-05
- 方式：GitHub API 元数据（license/star/head SHA，PowerShell Invoke-RestMethod 直连）+ raw.githubusercontent.com 源码快照阅读。**未 clone、未安装依赖、未运行任何仓库代码。**
- 源码快照位置：`research/round2/claude/repos/`（10 个文件，文件名带仓库前缀）。
- 声明：以下"读过"仅指本报告列出的文件；不凭 star/README 宣称运行过或深度掌握全仓库。

---

## R1. CAHLR/OATutor —— 层级提示 + 帮助后作答记录的前端自适应辅导系统

- URL: https://github.com/CAHLR/OATutor ｜ branch: main ｜ head commit: `e24c8456e5f7...`（API 取得）｜ LICENSE: MIT ｜ ~276 stars
- 论文（README 提供，未读正文）：Pardos et al. 2023, CHI '23, DOI 10.1145/3544548.3581574；期刊版（学习收益+LLM 提示）DOI 10.1371/journal.pone.0304013
- 读过的文件与关键发现：
  1. **`src/components/HintSystem.js`**（快照 19KB）：
     - `isLocked(hintNum)`：提示按**依赖链**递进——hint 0 恒解锁，hint N 需其 dependencies 全部已看（`hintStatus[dep]===1`）才解锁。学生不能跳级直接看最终答案。
     - `unlockSubHint(hintNum, i, isScaffold)`：子提示分两类——scaffold 型（引导小题）解锁记 0.5、直接给答案型记 1；**帮助程度在事件层就被分级记录**。
     - `submitSubHint(...)`：scaffold 子提示可含作答框，学生提交后经 `firebase.hintLog` 单独记录（含对错、提示路径）；**帮助后作答与独立作答是两条日志流**。
     - `shouldPenalizeSubHintPanelOpen/Unlock`：是否对看提示计惩罚由 `hintPenaltyMode` 配置决定（可开关）——帮助惩罚是策略选项不是硬编码。
  2. **`src/models/BKT/BKT-brain.js`**（快照 592B，全读）：`update(model, isCorrect)` 标准 BKT 贝叶斯后验更新，4 参数（mastery/slip/guess/transit）。**参数由 `bktParams.js` 人工按技能配置，前端无拟合**。
- 可借鉴：①提示分级依赖链（全解→scaffold→无提示，与 E1/E3 fading 序列同构）；②帮助程度与帮助后作答在记录层分离（对应套件证据维度"有提示作答"）；③惩罚可配置。
- 不可照搬：**前端 BKT 无参数拟合**——其参数是人工按技能设定的，且需要大量 per-skill 作答数据才有意义。本套件学习数据稀疏，**不得伪造 BKT 掌握概率**，只借记录结构。

## R2. CAHLR/pyBKT —— BKT 及变体的参数拟合库（EM）

- URL: https://github.com/CAHLR/pyBKT ｜ branch: master ｜ head commit: `0f4ea412e18f...` ｜ LICENSE: MIT ｜ ~291 stars
- 论文（README 提供）：Badrinath, Wang, & Pardos 2021, EDM, pp. 468–474（未读正文）
- 读过的文件与关键发现：
  1. **`pyBKT/Model.py`**（快照 27KB）：每技能参数集 `{prior, learns[], guesses[], slips[], forgets[]}`，learns/forgets 可按 resource 区分（multilearn）、guess/slip 可按题目区分（item 类变体）。`fit()` 默认从随机初始化出发用 EM 拟合；`partial_fit()` 支持增量。参数也可人工预置（`INITIALIZABLE_PARAMS`）。
  2. **`pyBKT/EM_fit.py`**（快照 11KB）：`EM_fit(model, data, tol=0.005, maxiter=100)`——Baum-Welch 式 EM，按对数似然增量收敛。README 明确：**拟合远比预测吃数据**（需学生作答序列），纯 Python 版拟合慢、有 C++ 加速。
- 可借鉴：参数集的**语义结构**（初始掌握/学习率/猜/滑/遗忘）——候选文件用它定义"经后续表现支持的个性化默认"应挂在什么字段上（不拟合数值，但字段语义对齐）；`predict`/`evaluate`（AUC/RMSE/accuracy）提示我们：任何掌握判定都该报告验证方式。
- 不可照搬：**EM 拟合需每技能充足作答序列**；单学习者单会话数据远不够拟合条件。本套件不引入 BKT 数值估计。

## R3. open-spaced-repetition/fsrs4anki + py-fsrs —— FSRS 调度核心

- fsrs4anki: https://github.com/open-spaced-repetition/fsrs4anki ｜ main ｜ head `ff7c85cee735...` ｜ MIT ｜ ~4124 stars
- py-fsrs: https://github.com/open-spaced-repetition/py-fsrs ｜ main ｜ head `9446cb06605c...` ｜ MIT ｜ ~522 stars（fsrs4anki README 指向的关联调度库）
- 读过的文件与关键发现：
  1. **`src/fsrs/scheduler.py`**（py-fsrs，快照 30KB）：
     - `review_card(card, rating)`：Learning/Review 状态机；同日重复习走 `_short_term_stability`，跨日走 `_next_stability`（需 retrievability）。
     - `get_card_retrievability`：幂律遗忘曲线 `(1 + FACTOR·elapsed/stability)^DECAY`；`_next_interval` 由 `desired_retention` 反解下次间隔；`_next_difficulty` 带线性阻尼+均值回归（难度不无限漂移）。
     - 21 个模型权重 `parameters`；README 明示非专家不要手改默认值。
  2. **`src/fsrs/review_log.py` + `card.py`**（快照 3-5KB）：每次复习落 ReviewLog（含时间戳/评分/时长）；Optimizer（可选 extra `fsrs[optimizer]`）从 ReviewLog 集合拟合个性化参数与 optimal retention。
- 可借鉴：①**复习日志驱动**——间隔决策基于带时间戳的完整复习记录，本套件"出池需跨时间换问法两连"的日志化依据；②retrievability/时间衰减直觉支持"同表征重复正确≠长期保持"（baseline 缺口②）；③冷启动用默认参数、个体化需足够历史——对应本套件"个性化默认需后续表现支持"的三层状态设计。
- 不可照搬：**FSRS 数值调度是卡片复习模型**（21 参数遗忘曲线），本套件教学回合数/颗粒度完全不同；**不声称套件已 FSRS 优化**——未运行 Optimizer、无复习日志数据集，仅借其结构思想（时间加权+日志驱动+冷启动默认）。

---

## 三项目共同边界（候选文件遵循）

1. 只借**记录结构与决策逻辑**（帮助分级、日志驱动、冷启动默认），不引入数值模型。
2. 套件数据稀疏（一对一会话、非平台级作答流），任何"掌握概率/优化调度"宣称都不成立。
3. 三项目的共同前提是**先有作答/复习流水，再谈个性化**——这正是候选文件把画像条目分层（明确偏好/暂定假设/表现支持默认）的结构来源。
