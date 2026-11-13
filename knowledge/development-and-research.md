# 开发与科研：可选参考题材

> **可选参考题材：本次未加入技能规则、不自动加载/执行。**
> 各卡"状态"是历史审核记录中的采用/拒绝决定（日期见卡内），只说明当时以何种范围采用；与本目录本次的候选身份无关。

整理日期：2026-11-13。输入快照：`research/work-mode/codex-audit.md`（2026-11-09，本地维护目录）、`research/research-workflow/codex-audit.md`（2026-11-11，同上；其 v0.7 摘要见仓库 [research/adoption-v0.7.md](../research/adoption-v0.7.md)）。

## 想解决什么问题 → 可从哪项看起

| 想解决什么问题 | 可从哪项看起 |
|---|---|
| 让 agent 干的活可验证、可审查 | [DR-02](development-and-research.md#dr-02)、[DR-03](development-and-research.md#dr-03)、[DR-05](development-and-research.md#dr-05)、[DR-07](development-and-research.md#dr-07) |
| 并行多个 agent 怎么不冲突 | [DR-01](development-and-research.md#dr-01)、[DR-06](development-and-research.md#dr-06) |
| 科研流程先小样再正式跑 | [DR-08](development-and-research.md#dr-08) |
| 自动科研能信到什么程度 | [DR-09](development-and-research.md#dr-09)、[DR-10](development-and-research.md#dr-10)（两篇不同论文） |
| AI 提效数据怎么读 | [DR-11](development-and-research.md#dr-11) |
| 团队用法经验（自述级） | [DR-12](development-and-research.md#dr-12) |

## 个人开发工作流

<a id="dr-01"></a>

### DR-01 · Stripe：Minions 系列（上、下篇）

- **机构**：Stripe 工程博客
- **类型**：团队工程博客（内部栈自述，上下两篇合并为一卡）
- **链接**：上篇 <https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents>；下篇 <https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2>
- **核对范围**：读两篇；内容为团队公开描述内部栈——任务入口、隔离 devbox、代码上下文、确定性检查、模型修正、供人审核的 PR；上下文预取、CI 与有限修复是栈的一部分
- **讨论价值/可能帮助 IM 的范围**：任务输入明确、隔离写入、留下 CI 记录、限制修复次数
- **局限**：内部平台与作者规模数据不能当本地可用能力或效率保证
- **历史状态**：已采用（取舍记录）｜**核对日期**：2026-11-09

<a id="dr-02"></a>

### DR-02 · Simon Willison：Red/green TDD

- **作者**：Simon Willison（开发者本人）
- **类型**：个人工程模式指南
- **链接**：<https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/>
- **核对范围**：开发者本人把先观察预期的测试失败、再让测试通过，作为让 agent 自证行为的办法
- **讨论价值/可能帮助 IM 的范围**：可复现的缺陷优先保留失败前证据与修复后记录；不为每个文案小改强行写测试
- **历史状态**：已采用｜**核对日期**：2026-11-09

<a id="dr-03"></a>

### DR-03 · Simon Willison：个人 Newsletter 工具实录

- **作者**：Simon Willison
- **类型**：个人工程实录
- **链接**：<https://simonwillison.net/guides/agentic-engineering-patterns/adding-a-new-content-type/>
- **核对范围**：用独立目录中的公开博客源码作参照改生成器；起本地服务，用浏览器自动化把生成内容与真实博客首页比对
- **讨论价值/可能帮助 IM 的范围**：可比对的独立参照比"看起来完成了"更有用；工作流可以小到一个改动加一个行为核对，无需企业基础设施
- **历史状态**：已采用｜**核对日期**：2026-11-09

<a id="dr-04"></a>

### DR-04 · Simon Willison：从头做终端分享工具（录屏）

- **作者**：Simon Willison
- **类型**：作者公开录屏（约 11 分钟）
- **链接**：<https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/>
- **核对范围**：**列为选看，未取得字幕、未计入字幕任务（待核对入口）**
- **讨论价值/可能帮助 IM 的范围**：如后续观看，可作为小型工具工作流的补充示例
- **历史状态**：未核对（入口已记录）｜**记录日期**：2026-11-09

<a id="dr-05"></a>

### DR-05 · Anthropic：test-failure-analysis.yml 示例

- **机构**：Anthropic（claude-code-action 仓库示例）
- **类型**：开源仓库示例文件
- **链接**：<https://github.com/anthropics/claude-code-action/blob/main/examples/test-failure-analysis.yml>（审核读到的 blob：`1bd07290f50186ab6d5cf27c402a3e00e8349b6b`）
- **核对范围**：实际读源码——失败 CI 触发读取日志，模型输出结构化分类，示例基于阈值触发重跑
- **讨论价值/可能帮助 IM 的范围**：结构化诊断和失败日志
- **局限/不采用**：样例未见按任务限制重跑次数；不复制"把动态输出插入 shell"的做法；模型判断本身不能授权重跑
- **历史状态**：已采用（有限）｜**核对日期**：2026-11-09

<a id="dr-06"></a>

### DR-06 · Boris Cherny 谈 Claude Code 工作方式

- **作者**：Boris Cherny；访谈方 Pragmatic Engineer
- **类型**：公开访谈（一手）；X 原帖仅作线索
- **链接**：X 原帖 <https://x.com/bcherny/status/2007179832300581177>（**直开 403，仅列为线索**）；核对用访谈 <https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny>
- **核对范围**：访谈为独立一手来源，核对其对并行、审查和日常工作方式的叙述
- **讨论价值/可能帮助 IM 的范围**：并行是可选手段；相同文件、账本或素材版本先定一个写入负责人；不照抄并行规模
- **局限**：属于个人经验
- **历史状态**：已采用（个人经验参考）｜**核对日期**：2026-11-09

## 科研自动化

<a id="dr-07"></a>

### DR-07 · How the Claude Code team uses Claude Code（官方视频）

- **机构**：Claude 官方视频
- **类型**：团队访谈视频
- **链接**：<https://www.youtube.com/watch?v=S-sYlFiGFv8>
- **核对范围**：**字幕级核对**——英文上传轨道 657 个字幕段（至约 22:17）；定位近似点：10:05（API 结构与服务边界的历史理由→交接写清需人提供的上下文）、18:01/18:23（PR 携测试与截图、之后自己检出抽查→证据随产物，自动检查与人工复核分开，抽查依风险选择）；**未分析画面**
- **讨论价值/可能帮助 IM 的范围**：交接记录减少重复检查；交付物携带证据；人工复核按风险抽查
- **局限/不采纳**："模型自己有把握就写入"、固定多人扇出、每个小任务强制抽查、"容器保证所有跨硬件结果相同"均不采纳
- **备用选片入口**：AI Engineer《Claude Code 的演进》<https://www.ai.engineer/talks/Lue8K2jqfKk-claude-code-evolution-agentic-coding>（仅备用入口，未核对，不单独计数）
- **历史状态**：已采用（字幕级）｜**核对日期**：2026-11-09

<a id="dr-08"></a>

### DR-08 · Nextflow/nf-core 官方训练资料（演示页＋视频＋活动页）

- **机构**：Nextflow 官方训练站 / nf-core
- **类型**：课程页＋讲座视频＋训练活动页（同一课程生态，合并为一卡并逐链接标注）
- **链接**：演示运行页 <https://training.nextflow.io/latest/nfcore_use/01_run_demo/>；视频 <https://www.youtube.com/watch?v=Gr49rbuuDvc>；活动页 <https://nf-co.re/events/2025/training-foundational-march>
- **核对范围**：训练页——小型 test profile 验证流程，运行结果配套 report/timeline/trace；视频——**自动英文字幕 2907 段（至约 64:15，平台时间可能取整）**，定位近似点 16:26/43:17（运行一致性与正确性之别；CI 配套最小测试数据）；**未分析画面**；平台术语另与课程文档对照
- **讨论价值/可能帮助 IM 的范围**：先小样本再正式运行；输入、参数、环境、日志和图表来源记录；最小样本与正式结果分别验收
- **局限**：不规定所有科研都用 Nextflow
- **历史状态**：已采用（页面＋字幕级）｜**核对日期**：2026-11-09

<a id="dr-09"></a>

### DR-09 · The AI Scientist-v2

- **类型**：学术论文（arXiv）
- **链接**：<https://arxiv.org/abs/2504.08066>（审核读 HTML v1 的 §4–5）
- **核对范围**：作者实验从主题提示生成假设、实验、分析和稿件；三篇送审中一篇达到特定 workshop 的接受标准，随后按预先约定撤回
- **讨论价值/可能帮助 IM 的范围**：agent 可产出试验候选、分析草稿和证据目录；研究问题、划分、主张强度和对外提交单独判断
- **局限**：该实验不证明系统能独立完成高质量科研
- **历史状态**：已采用（边界明确）｜**核对日期**：2026-11-09
- **注意**：与 DR-10 是**不同资源**，勿混。

<a id="dr-10"></a>

### DR-10 · ScientistTwo

- **标题**：ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI（arXiv:2609.19644）
- **机构**：作者单位包含 Google Cloud AI Research
- **类型**：学术论文（arXiv 预印本）
- **链接**：<https://arxiv.org/abs/2609.19644>（审核读 HTML v1）
- **核对范围**：题录、§3.1–3.6、§4 的评估与完整性检查、§4.3 成本讨论；**未复跑代码、未逐项核验上游结果**
- **讨论价值/可能帮助 IM 的范围**：先做同条件小规模基线与候选实验；按实际日志改进；消融解释增益来源；改方法后重新检查下游；以有限预算结束循环；§4 完整性审核区分分数复跑、任务规范、引用真实性和方法—代码一致性
- **局限**：主要针对 AI/ML 基准问题；ScholarPeer 同时参与优化和评估，Stanford Agentic Reviewer 为另一评估器——**这些评分不是现实会议录用**；论文报告的成本与完整性结果属作者实验，不代表 IM 已达同等能力；不采用"反复改到评审给高分"的目标，保留失败、负结果与不确定性
- **IM 另加（本套件工程补充，非论文已验证结论）**：预先明确指标与否定条件、验证集与最终测试的用途、可比条件、尝试次数、结论范围
- **历史状态**：已采用（方法框架与工程补充分列）｜**核对日期**：2026-11-11
- **审核页**：[research/adoption-v0.7.md](../research/adoption-v0.7.md)

<a id="dr-11"></a>

### DR-11 · METR：早期 2025 开发者实验及 2026 跟进

- **机构**：METR
- **类型**：实证研究论文＋官方跟进博客（同一研究线，合并为一卡）
- **链接**：论文 <https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf>；跟进 <https://metr.org/blog/2026-02-24-uplift-update/>
- **核对范围**：16 名熟悉自己开源仓库的开发者完成 246 个真实任务，使用当时的 AI 工具平均慢 19%；2026 跟进指出后续存在选样及并行任务计时问题，难以可靠估计新的增益幅度
- **讨论价值/可能帮助 IM 的范围**：分开记录人力、等待、审查、返工与质量
- **局限**：不能用该百分比预测 IM 或今天的工具
- **历史状态**：已采用（限制明确）｜**核对日期**：2026-11-09

<a id="dr-12"></a>

### DR-12 · Anthropic：How Anthropic teams use Claude Code（官方 PDF）

- **机构**：Anthropic
- **类型**：团队案例集（官方 23 页 PDF）
- **链接**：<https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf>
- **核对范围**：**只核可提取文本的相关页**——印刷页 3–4、11–14、17–20；不是视频观看或逐页画面审阅
- **讨论价值/可能帮助 IM 的范围**：把已验证工具用法和项目约定写进项目说明；工作前定位相关代码/输入；短迭代与可恢复检查点；按研究问题构建能追到原数据的可视化；审阅错误状态和边界情况；**项目知识写到唯一获准正本，不在每个宿主复制另一套历史**
- **局限**：内部团队案例和经验自述，**非对照试验**；不采用效率倍数作 IM 成效承诺；"让模型自行运行一段时间"不作默认时长；不照搬先丢弃再重来的恢复方式（恢复先保留已有产物与用户改动）；MCP 权限须按实际部署核查
- **历史状态**：已采用（团队自述级）｜**核对日期**：2026-11-11
- **审核页**：[research/adoption-v0.7.md](../research/adoption-v0.7.md)

## 页面级说明

- 视频类条目均为字幕级核对；**选片不是观看**。原始字幕仅作本地研究材料，不随技能包分发。
- 科研类审核均未运行三套上游系统，也未做实际科研成效比较。

## 候选议题（原创讨论，非外部研究结论）

- **科研要点**：可否定的假设、可比基线、有界迭代、消融、负结果、方法—代码与指标核对。历史状态：其中对应要点已按 2026-11-11 审核并入 v0.7 的 `skills/imwork/references/research-cycle.md`（见 [research/adoption-v0.7.md](../research/adoption-v0.7.md)）；此处仅作题材索引，便于按需重读，不新增承诺。

## 跨主题

- 工作流卡、授权预算与最小上下文议题见 [智能体与工作流](agents-and-workflows.md)。
- DR-12"项目知识写唯一正本"与 [知识连续性](knowledge-continuity.md) 的正本/指针思路一致。
