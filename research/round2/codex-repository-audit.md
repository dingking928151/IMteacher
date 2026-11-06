# GitHub源码核查与采用映射

固定提交经GitHub公开API核实；Codex另取13个指定文件，读相关正文与函数，文件SHA256见 `sources/manifest.json`。未克隆依赖、未运行仓库、未复制算法或题库到技能。以下是借鉴机制，**不是安装这些项目**。

| 项目/提交 | 实际查读 | 采用/不采用 |
|---|---|---|
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor/tree/e24c8456e5f75c07b6048159ea9e128b036f673d) `e24c8456e5f75c07b6048159ea9e128b036f673d` | README、LICENSE；`src/models/BKT/BKT-brain.js` 的update；`src/components/problem-layout/HintSystem.js` 的isLocked/unlockSubHint/submitSubHint；`src/models/BKT/problem-select-heuristics/defaultHeuristic.js` 的heuristic | 借鉴KC、提示使用与作答分开、基于当前缺口选任务。没有搬入BKT更新概率、固定阈值、Firebase、随机最低掌握题或求助惩罚。代码MIT；README另声明题目内容CC BY4.0，并有逐项署名，不能把全仓一律说MIT |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT/tree/0f4ea412e18f6bcbd396fdf2be68fdd43aebebb6) `0f4ea412e18f6bcbd396fdf2be68fdd43aebebb6` | README、LICENSE；`source-py/pyBKT/models/Model.py` 的fit/partial_fit/predict/evaluate；`source-py/pyBKT/util/data_helper.py` 的convert_data | 借鉴按技能、时间顺序和来源整理作答。拟合、预测、评估有明确流程；本套件没有训练/运行它，不把聊天印象换算成概率。顶层MIT，依赖另有许可；未下载/分发依赖 |
| [open-spaced-repetition/fsrs4anki](https://github.com/open-spaced-repetition/fsrs4anki/tree/ff7c85cee735472d1c9cec0b9252d184087f74d8) `ff7c85cee735472d1c9cec0b9252d184087f74d8` | README、LICENSE；`fsrs4anki_scheduler.js` 与`fsrs4anki_scheduler_qt5.js`，重点forgetting_curve/next_interval/next_recall_stability/next_forget_stability及默认参数 | 借鉴回忆历史、间隔、不同结果后更新的思路；不实现/声称已实现FSRS。所读Qt6脚本头为v6.1.1，并非所有当前FSRS实现的版本。默认调度≠个性化拟合；卡片回忆≠复杂解题迁移。MIT |

## 落到哪里

- OATutor提示/任务结构 → teacher的teaching-design、checkpoint-bank、知识账中的最高帮助字段。
- pyBKT数据组织/评估边界 → adaptive-practice的KC/顺序/独立性/来源；明确不输出伪掌握概率。
- FSRS状态/历史观念 → adaptive-practice、quiz-and-review的透明人工复习与冷启动规则；明确未接调度器。
- 所有策略试用 → 四技能共用adaptation-loop，反例/范围/撤回机制；不是把开源项目整套移植进来。

后续若真接引擎，另行做数据语义、兼容版本、许可、评估、迁移与预算设计；本轮不安装或重配置用户的Anki/学习平台。
