# 第二轮证据报告：学习科学与教学安排（10 条）

- 取证人：Claude Code ｜ 日期：2026-11-05
- 授权范围：不限讲座，学习脑科学/教学安排知识 + GitHub 项目（项目部分见同目录 `repositories.md`）。
- **所读层级说明**（每条都标，不混用）：
  - **全文**：读到正文全文（本侧或 Codex 侧核实，注明核实方）。
  - **摘要**：读到官方摘要/数据库条目（PubMed、APA PsycNet、Semantic Scholar 摘要字段、多源一致的搜索结果）。
  - **元数据**：仅经 Crossref/Semantic Scholar API 核实题录（标题/作者/年份/卷期页），未读摘要。
- 数字纪律：只写核实来源里实际出现的样本数/效应量数字；写不出的不编。
- 与第一轮报告的关系：第一轮四场讲座为科普/实践层输入；本报告是其研究层支撑，两者不互相代替。

---

## E1. IES 实践指南：例题与解题交错、示例随熟练度渐退 【全文（Codex 侧）+本侧官方条目页】

- Pashler, H., Bain, P., Böttge, B., Graesser, A., Koedinger, K., Trautmann, S., & Vaughan, C. (2007). *Organizing Instruction and Study to Improve Student Learning*. IES Practice Guide, NCER 2007-2004. 官方 PDF: https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/20072004.pdf （指南页: https://ies.ed.gov/ncee/wwc/practiceguide/1）
- 层级：Codex 侧已读 Recommendation 2 全文并核实；本侧核实官方 URL 与推荐结构（7 条推荐，Rec 2 证据强度标注为 Strong）。
- 方法/内容：美国教育部下属 IES/WWC 系统综述型实践指南，7 条推荐各带证据强度评级。Rec 2 = **将完整解答的例题与解题练习交错安排，并随学生熟练度提高逐步撤去（fade）例题中的完成步骤**。
- 适用边界：
  - 支持"新手期先看全解例题、熟练后逐步撤提示"的**操作序列**（本套件缺口①的直接依据）。
  - 指南的 fading 概念 ≠ 不同题型混排的 interleaving（Brunmair & Richter 2019 那种），Codex 已明确区分，候选文件遵循该区分。
  - 指南面向 K-12 课堂教师（数学/科学/社科），大学 STEM 一对一场景可类比但强度不是 RCT 级保证；Rec 2 的 Strong 是 WWC 评级非效应量。

## E2. 专家反转效应：对新手有效的教学方式会随熟练度失效 【摘要（多源一致）】

- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. DOI: 10.1207/S15326985EP3801_4
- 层级：摘要级——APA PsycNet 条目 + 维基百科条目 + 伍伦贡大学仓储 PDF 链接（ro.uow.edu.au）多源描述一致；本侧未读全文正文。
- 方法/内容：认知负荷理论框架下的实证文献综述，正式命名"expertise reversal"：为新手设计的高支持教学（如详细引导、全解例题）在学习者熟练后变得冗余甚至有害，方向反转。
- 适用边界：
  - 支持"提示/脚手架必须随表现升级而撤除，长期固定不撤是负收益"——fading 的必要性论证（与 E1 互补：E1 给序列，E2 给反转机制）。
  - 不支持按单次表现频繁翻转教学方式；反转是"熟练度带"现象，判熟练度需要多次证据（对接 baseline 缺口④的分层状态字段）。
  - 摘要级：不引用其具体效应量/实验数。

## E3. 例题步骤渐退的随机对照实验 【摘要】

- Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. *Journal of Educational Psychology*, 95(4), 774–783. DOI: 10.1037/0022-0663.95.4.774
- 层级：摘要级——APA PsycNet 记录 + ERIC EJ678596 + 可获取的全文 PDF（mrbartonmaths.com 教研镜像，本侧未逐页读正文）。后续理论文：Renkl & Atkinson (2004) *Instructional Science* 同主题。
- 方法/内容：教学实验，对比从完整例题到独立解题的过渡方式；操纵两个因子：渐退（fading，先给全部解题步骤、逐步改为留空由学生补全）与自我解释提示。fading 条目在后测表现优于直接从例题跳到完整解题。
- 适用边界：
  - 支持"提示撤除要有中间台阶"——不是全解→裸题二元切换，而是逐步留空（本套件 checkpoint-bank 的"变式迁移"题可挂渐退梯度）。
  - 单一实验、单一领域（该研究用概率/统计类材料），不是普适常数；候选文件把它当**序列设计依据**而非效果承诺。

## E4. 提取练习改善长期保持 【元数据】

- Roediger, H. L., III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255. DOI: 10.1111/j.1467-9280.2006.01693.x
- 层级：元数据级（Crossref 核实题录）；本侧未读摘要正文，不引用其具体样本与间隔参数。
- 内容方向：重复测试比重复学习更有利于延迟保持（测试效应），方向广为引用。
- 适用边界：支持"验证学习=闭卷提取而非重读/看过"；与套件现有"看过只记接触"原则一致。本套件引用它只为方向支撑，操作规程（每日回顾 2-3 题）是教学设计不是该文结论。

## E5. 间隔效应综述 【元数据】

- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380. DOI: 10.1037/0033-2909.132.3.354
- 层级：元数据级（Crossref 核实题录；Semantic Scholar 无摘要字段，本侧未读摘要正文）。
- 内容方向：言语回忆任务中分散练习优于集中练习的综述与定量合成（间隔效应）。
- 适用边界：
  - 支持"错题池出池要求跨时间""回顾按 D-1/D-3/D-7 到期"这类**跨时间重做**设计的方向性依据。
  - 不支持具体间隔数值——本套件的 D-1/D-3/D-7 是教学默认值（可校准），不是从该文推的常数；具体最优间隔因材料/目标保持期而异，候选文件明确标注这一点。
  - 该文限定 verbal recall 任务；程序性技能（写代码）外推需谨慎，候选文件不据此外推。

## E6. 交错练习元分析：相似性是关键调节变量 【摘要（PubMed）】

- Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin*, 145(11), 1029–1052. DOI: 10.1037/bul0000209 （PubMed: https://pubmed.ncbi.nlm.nih.gov/31556629）
- 层级：摘要级（PubMed 摘要；数字 238 个效应量/59 项研究出自摘要原文）。
- 方法/结果：多层元分析。交错练习练习期表现常更差、延迟测试更优；总体中等效应，但**高度依赖材料相似性**：对视觉分类类材料（如绘画辨别）最强，对数学任务收益较小，对文本/词汇类无效或负向。
- 适用边界：
  - 支持"错题池出池要求换问法"（跨表征重取）与"多考点混合小测"的方向，但**不承诺数学线大量换题必有收益**——摘要明确数学任务收益较小。
  - 操作化含义（候选文件采用）：交错用于**相似考点混合检查点/小测**（分辨哪类概念用哪个方法），不用于打断单一新概念的首次学习。此边界与 IES Rec 2 的"例题渐退"是不同机制（呼应 E1 边界）。

## E7. 提取练习系统综述： Classroom 证据与反馈时机的不确定性 【全文（Codex 侧）+本侧 Crossref】

- Agarwal, P. K., Nunes, L. D., & Blunt, J. R. (2021). Retrieval practice consistently benefits student learning: A systematic review of applied research in schools and classrooms. *Educational Psychology Review*, 33, 1409–1453. DOI: 10.1007/s10648-021-09595-9 （作者全文 PDF: https://poojaagarwal.com/Agarwal_etal_2021_EDPR.pdf）
- 层级：全文——Codex 侧已读作者官方 PDF（50 experiments / 49 effects / n=5374，数字来自 Codex 核实）；本侧 Crossref 题录一致。
- 方法/结果：对真实学校课堂中提取练习的系统综述。提取练习收益方向高度一致；但**无法从该综述确定最佳反馈时机/格式**（原文结论）。
- 适用边界：
  - 支持"检查点/小测/每日回顾"的提取式验证主线。
  - **不支持**给反馈时机定固定规则（如"必须 5 秒内反馈"）；套件任何"反馈时机"条款不得声称有最优间隔依据。
  - 样本主体为学校课堂场景，大学一对一为类比外推。

## E8. 自我调节学习（SRL）模型综述 【全文（Codex 侧）+本侧 Crossref】

- Panadero, E. (2017). A review of self-regulated learning: Six models and four directions for research. *Frontiers in Psychology*, 8:422. DOI: 10.3389/fpsyg.2017.00422
- 层级：全文——Codex 侧核实（SRL 循环三阶段：前置计划/表现控制/自我反思）；本侧 Crossref 题录一致。
- 方法/内容：六种 SRL 理论模型的结构化综述，提出四个研究方向（含负反馈如何被处理、社会性维度等）。
- 适用边界：
  - 支持"预测→执行→对账→反思"的循环结构与"复盘=学习者自答为主"的分工（supervisor 的对账轮符合前置-表现-反思结构）。
  - **不支持**"AI 监工=有效 SRL 支持的因果结论"——SRL 模型综述不是干预有效性 RCT（Codex 明确此边界，候选文件遵守：imsupervisor 的对账是结构借鉴，不声称机制有效性）。

## E9. 学习风格（meshing hypothesis）证据评估 【摘要（Codex 侧）+本侧 Crossref】

- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest*, 9(3), 105–119. DOI: 10.1111/j.1539-6053.2009.01038.x
- 层级：摘要级——Codex 侧已读 APS 页摘要；本侧 Crossref 题录一致。
- 方法/内容：PSPI 系统综述，专门检验"按学习风格匹配教学能提升效果"（meshing hypothesis）的研究：几乎未发现符合严格交叉设计标准的支持证据；**风格偏好与实际学习效果是两件事**。
- 适用边界：
  - 支持 baseline 情境⑤的处置：不认定"右脑/视觉型"并据此教学；自我报告偏好≠能力类型。
  - **不夸大**：Codex 明确"读到摘要级，仅支持风格匹配证据不足/偏好和效果不同，不声称否定所有个体差异"。候选文件措辞遵循此边界——拒绝的是"类型认定+匹配教学"，保留"把视觉表征当偏好试验并用表现检验"的路径。
  - 另注：此 Pashler 2008（PSPI 学习风格）与 E1 的 IES 指南（Pashler 等 2007）是两份不同出版物，不混引。

## E10. 反馈模型：效果取决于类型与情境 【摘要（Semantic Scholar）+Crossref 全元数据】

- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112. DOI: 10.3102/003465430298487
- 层级：摘要级（Semantic Scholar 摘要字段）+ Crossref 全题录。
- 方法/内容：反馈研究综述，提出反馈的三问题模型（Where am I going / How am I going / Where to next）与四层次（任务/过程/自我调节/自我）。摘要要点：反馈是最强影响之一，但**正负向皆可能**，效果取决于类型与交付方式；时机是复杂问题。
- 适用边界：
  - 支持"批改=指出错在哪层+下一步动作"（任务/过程层反馈），而非笼统对错或人格评价（与 supervisor 禁人格标签一致）。
  - 不支持固定反馈时机规则（呼应 E7 边界）；提示按层级递进而非一次性给全（对接 OATutor 的层级提示设计，见 repositories.md）。

---

## 取证状态汇总

| # | 文献 | 层级 | 核实方 |
|---|------|------|--------|
| E1 | IES 2007 指南 | 全文（Rec 2） | Codex 全文 + 本侧官方页 |
| E2 | Kalyuga 2003 | 摘要 | 本侧多源一致 |
| E3 | Atkinson/Renkl/Merrill 2003 | 摘要 | 本侧 |
| E4 | Roediger & Karpicke 2006 | 元数据 | 本侧 Crossref |
| E5 | Cepeda 2006 | 元数据 | 本侧 Crossref |
| E6 | Brunmair & Richter 2019 | 摘要（PubMed） | 本侧 |
| E7 | Agarwal 2021 | 全文 | Codex 全文 + 本侧 Crossref |
| E8 | Panadero 2017 | 全文 | Codex 全文 + 本侧 Crossref |
| E9 | Pashler 2008 PSPI | 摘要 | Codex + 本侧 Crossref |
| E10 | Hattie & Timperley 2007 | 摘要 | 本侧 |

- **未收入**：Howard-Jones (2014, Nature Reviews Neuroscience)——本侧与 Codex 侧均被登录墙挡住，只有元数据级，达不到本报告"支撑候选条款"的门槛，不补造其内容。
- **夸大红线**（候选文件遵循）：不推固定反馈时机（E7/E10）；不推具体间隔常数（E5）；数学任务交错不承诺收益（E6）；风格类型认定+匹配教学被拒、但保留偏好试验路径（E9）；SRL 只借结构不声称 AI 监工有效性（E8）；fading 序列是设计依据非效果承诺（E1/E2/E3）。
