# Round 4 证据记录（Claude 侧）

日期：2026-11-07。任务：反馈、反思/自我调节的来源取证。范围限制：wellbeing/日常关怀资料由另一研究者负责，本文件不含。所有 PDF 原件留在本地临时目录（C:\Temp\im-round4\papers\），不入库分发。

## 一、论文（3篇，实际读取）

### 1. Hattie & Timperley (2007). The Power of Feedback. Review of Educational Research, 77(1), 81–112. DOI: 10.3102/003465430298487

- 来源URL：https://conselhopedagogico.tecnico.ulisboa.pt/files/sites/32/hattie-and-timperley-2007.pdf （大学托管全文PDF，33页，正式出版版）
- 读取范围：全文下载并提取文本；精读：模型部分（pp.83–90：效应量表1–3、三问题模型、四层次图1）、正负反馈与self层次（pp.97–99）、结论（pp.101–103）。逐行浏览了表格数据；中间部分（各层次教学示例细节、文化差异与反馈接受度、延迟反馈的题难度交互，pp.90–97）为通读非逐行。
- 支持的设计点：
  - 反馈平均效应量大（12个元分析 d=0.79），但 Kluger & DeNisi (1996) 131项研究、12,652名参与者，估计 **470个效应量**中 d=0.38，**其中32%的效应量为负**（是效应量层面，不是"32%的干预"）——反馈不是天然有益，需筛选层次。
  - 表扬/奖励/惩罚效应量低（d=0.14/0.31/0.20），针对任务的线索信息最高（d=1.10）；"设计来打击学生"的反馈 d=-0.14；高威胁自尊情境 d=0.08 vs 低威胁 d=0.47。控制式施加更差（Deci et al. 1999：控制式 -0.78）。
  - 有效反馈回答三问题：Where am I going（feed up）/ How am I going（feed back）/ Where to next（feed forward）（p.86，Figure 1）。
  - 四层次：任务层、过程层、自我调节层、自我层。**自我层（对人本身的夸奖/评价）几乎无效**，且把注意力引向自我会促使回避挑战、减少努力、害怕失败（pp.101–102）。
- 不支持/局限：
  - 研究对象是课堂与绩效场景，不是 AI 对话助手场景；不能直接证明"聊天里每日一次反馈邀请"有效。
  - d 值来自教育成就测量，不能照搬到学习习惯或计划执行。
  - "32%负效应"是干预层面的统计，不是"用户给AI反馈有32%概率有害"。

### 2. Zimmerman (2002). Becoming a Self-Regulated Learner: An Overview. Theory Into Practice, 41(2), 64–70. DOI: 10.1207/s15430421tip4102_2

- 来源URL：https://www.leiderschapsdomeinen.nl/wp-content/uploads/2016/12/Zimmerman-B.-2002-Becoming-Self-Regulated-Learner.pdf （第三方网站托管作者版全文，8页，含 ResearchGate 封面页）
- 读取范围：全文（pp.64–70 正文+参考文献）逐行读完。
- 支持的设计点：
  - 自我调节三阶段循环：前瞻（目标设定+策略计划）→执行（自我控制+自我观察/自我记录）→自反（自我评价+因果归因；自我反应：满意感、适应性 vs 防御性反应）。**自反结果回流到下一轮前瞻**——支持"反馈处理完要有明确去向"的闭环设计。
  - 因果归因：把失败归因固定能力会破坏动机；归因到可控过程（如策略选错）维持动机（p.68）——支持"反馈分析不做能力/人格归因，往策略层引"。
  - 专家对照个人目标自我评价、做策略归因；新手对照他人、做能力归因、防御性反应（p.69）——支持对比标准用"自己昨天/自己目标"而非外部标准。
  - 自我记录的反应性（reactivity）：仅要求自我记录就常带来自发改善（p.65，引 Shapiro 1984；文献内声明，非本文直接验证）。
  - 自我调节可教、不是固定特质；会自我调节的学习者主动求助，不是孤立学习（pp.69–70）。
- 不支持/局限：综述性质（概述+引证），非新实验；"每日反思频率"无涉及。

### 3. Nicol & Macfarlane-Dick. Formative assessment and self-regulated learning: a model and seven principles of good feedback practice.

- **版本说明（重要）**：实际全文读取的是 **2004 年讨论稿**（"Rethinking Formative Assessment in HE"，Villanova 大学托管 PDF，9页：https://www.villanova.edu/content/dam/villanova/vital/vitalinks/7principlesofgoodfeedback04.pdf ，需浏览器UA）。**2006 期刊正式版**（Studies in Higher Education, 31(2), 199–218, DOI: 10.1080/03075070600579090）仅有题录+检索摘要（Strathclyde 机构库被 Cloudflare 拦截，出版商页付费墙）。两版核心模型与七原则一致，但**七原则的排序两版不同**（2004版第1条是"促进自评"，2006版第1条是"澄清好的表现标准"）；引用时按 2004 版内容陈述，注明版本差异。
- 读取范围：2004 版全文逐行读完。
- 支持的设计点：
  - 概念模型（承 Butler & Winne 1995）：**学生始终主动**——监控目标差距产生内部反馈；外部反馈必须被学生解释、内化后才影响行为；外部反馈可以增强、一致或**冲突**于学生自己的理解（p.3）——直接支持"反馈需分析而非盲从"是双向的：AI 对用户反馈也要解释后采取行动，不自动执行。
  - Sadler 三条件：(a) 有目标/标准概念 (b) 对比现状与标准 (c) 采取行动缩差（p.1–2）。
  - 七原则（2004版）：促进自评、鼓励师生对话、澄清好表现的标准、提供缩差机会、交付高质量信息、维护积极动机与自尊、向教师回馈以改教学。
  - **闭环是反馈最常被遗忘的一环**（p.5，引 Boud 2000："判断反馈是否产生学习的唯一方法，是学生做出某种回应来完成反馈循环"）——支持"每条反馈必须有去向：改/不改+复审条件，不收集不处理"。
  - 数量控制：Lunsford (1997) 主张每篇作文仅给约3条深思过的评语；反馈过多导致无法行动（p.6）——支持"一次邀请只问一个问题"（作为设计类比，非直接研究）。
  - Butler (1987,1988)：只给评语优于给分数；分数引发与他人比较（自我卷入），评语指向任务——支持邀请**不打分、不评级**（设计类比，对象是作业反馈）。
  - 好实践示例含"**让学生在提交时主动索取想要的反馈**"与"让学生基于刚收到的反馈自己提出行动点"（pp.3–4, 6, 8）——支持邀请由用户选话题、行动点由用户确认。
- 不支持/局限：对象是高校作业评估，不是日常学习计划；2004版为讨论稿非同行评审终稿（模型与原则在2006版延续，但我们未逐行读2006正文）。

### 补充：套件已引用的 Panadero (2017) 与 adaptation-loop 的关系
本轮三篇与既有 shared/adaptation-loop.md 引用的 Panadero (2017) 同属自我调节文献脉络，未发现与本套件现有设计冲突的结论；本轮新增价值主要在反馈层次（H&T）、归因方向（Zimmerman）、闭环与数量控制（Nicol）。

## 二、视频（1个，实际处理）

### Tasha Eurich: "Increase your self-awareness with one simple fix"（TEDxMileHigh, 2017-11 发布）

- 处理方式：既有 watch 技能，`--detail transcript --no-whisper`（仅原生字幕，**无云音频转写，未下载视频，无抽帧**——画面覆盖为0，如实声明）。
- URL：https://www.youtube.com/watch?v=tGdsOXZpyWE （TEDx Talks 官方频道，时长 1037秒≈17:17，上传 2017-12-19）
- 另注：ted.com 官方页（https://www.ted.com/talks/tasha_eurich_increase_your_self_awareness_with_one_simple_fix ）的 yt-dlp 提取器报 JSON 解析错误（本机 yt-dlp 2026.07.04，按约束不升级不装依赖），改用 YouTube 官方频道镜像成功。
- 字幕：`video.en.vtt`（原生英文字幕，人工上传轨道；同时存在 en-orig 自动轨道）。字幕原件与元数据已存 `research/round4/claude/video-evidence/`。
- 关键内容（时间戳为字幕时间）：
  - 00:01:02–01:10：研究规模自述："My research team surveyed quantitatively thousands of people. We analyzed nearly 800 scientific studies."
  - 03:03–03:15："95% of people think they're self-aware, but the real number is closer to 10 to 15%."
  - 04:50–05:45：内省（introspection）≠自我觉察；其团队研究内省与幸福感/压力/工作满意度的关系。
  - 12:10–12:26：分析高自我觉察者的逐字稿，"why"出现少于150次、"what"超过1000次。
  - 15:52–15:57："Why-questions trap us in that rearview mirror. What questions move us forward to our future."
  - 16:10–16:18：高自我觉察者的共同点只剩两条：相信自我觉察的重要性 + **每天**投入发展它（daily commitment）。
- 支持的设计点：反馈/反思邀请用 What 式问句（"这次哪一步和预想不一样？""下次保留哪个改动？"）优于 Why 式审问（"你为什么没做到？"）；每日小投入的框架可引用为设计取向。
- 不支持/局限：TEDx 是研究者对自己著作（Insight, 2017）的通俗转述，**非同行评审**；95%/10–15%、why/what 词频均为其团队自述，本会话无法核查原始研究；仅字幕、无画面（幻灯片内容未知）；"每日承诺"是访谈发现中的共性描述，不构成频率处方。

## 三、读取失败/未完成项

1. Nicol & Macfarlane-Dick 2006 期刊版全文：机构库与出版商均不可达（Cloudflare/付费墙），以 2004 同作者讨论稿全文替代，版本差异已注明。
2. TED.com 官方站字幕提取失败（yt-dlp TED 提取器 JSON 错误），已用 YouTube 官方频道等效替代；未升级 yt-dlp（遵守不装依赖约束）。
3. 第二个视频未处理：Codex 更新指示为"优先保证1个实际视频"，1个已完成即够最低要求；如需第二个（自主支持/反馈主题）再分派。
4. Semantic Scholar API 限流（429），未影响（PDF 已直接可得）。
