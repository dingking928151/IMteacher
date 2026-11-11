# v0.6–v0.7 来源采用说明（公共版）

2026-11-11。本页汇总 v0.6（项目工作与协作）与 v0.7（科研闭环与工作流构筑）引入规则时实际阅读的公开来源、采用范围与边界。完整逐条审核保留在维护目录，不随本仓库分发。所有来源均为公开官方材料；本套件只独立概述与外链，不暗示任何来源方的背书。

## 来源与采用边界

### 1. ScientistTwo（arXiv 预印本）

来源：[ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI](https://arxiv.org/html/2609.19644v1)（arXiv:2609.19644v1，作者单位含 Google Cloud AI Research）。

采用：同条件小规模基线先行、按实际日志改进、消融解释增益来源、方法改动后重核下游证据、有限预算结束循环。

**明确边界：论文中的自动审稿分数（ScholarPeer 等）不是现实会议录用**；其成本与完整性结果属作者实验，不代表 IM 达到同等能力；IM 不采用"反复改到评审高分"的目标，保留失败与负结果。

### 2. DeepSeek super-agent 原型（官方文档）

来源：[官方仓库 README](https://github.com/deepseek-ai/dsh-superagent-prototype) 及其 [理念](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/000-philosophy.md)、[领域模型](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/001-domain.md)、[授权](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/002-authorization.md)、[执行](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/003-execution.md) 文档。

采用：来源事件与获准任务分开、任务与执行会话分开、保留决策理由与授权版本、事件去重、阻塞与待人审核分开、恢复时查真实状态。

**明确边界：官方 README 自述为研究原型，与设计文章及内部版本不完全一致**；设计文章的原始 X 地址本轮返回 403 未直接读取，不把转载当已核实原文。原型中以 OS 用户免确认执行、嵌套子智能体、自动合并等**不采用**；IM 维持单层、限定并发与逐次预览批准。

### 3. Anthropic 团队案例（官方 PDF）

来源：[How Anthropic teams use Claude Code（官方 PDF）](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)。

采用：已验证用法与项目约定写进项目正本、工作前定位相关代码/输入、短迭代与可恢复检查点、按研究问题构建可溯源可视化。

**明确边界：内部团队案例与经验自述，非对照实验，不证明 IM 效果**；不采用效率倍数作承诺；恢复时先保留已有产物；MCP 权限按实际部署核查。

### 4. 开发流程与科研流水线视频（既有字幕路径）

来源：[How the Claude Code team uses Claude Code（Claude 官方频道）](https://www.youtube.com/watch?v=S-sYlFiGFv8) 与 [An Introduction to Nextflow and nf-core（SIB 官方频道）](https://www.youtube.com/watch?v=Gr49rbuuDvc)。均经平台既有字幕读取，未审阅画面；讲者口述数字未独立核查。采用：审查分层（机器已核/需人核）、产物附验证证据、最小测试数据与版本标识作为阶段门禁；**容器化有助于固定依赖和运行环境，结果仍可能受硬件、配置、数据与随机性影响；复现不等于正确**。

### 5. 工作栈结构（官方文档）

来源：[GitHub reusable workflows 文档](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows) 与 [Claude Code subagents 文档](https://code.claude.com/docs/en/sub-agents)。采用：命名工作栈按历史/模板/当次授权/宿主能力分层、权限只收窄不升格、引用的 agent 缺失时停下报告而非静默顶替。

## 共同局限

以上来源均为经验案例、预印本、原型文档或产品文档，**没有一项构成 IM 套件有效性的实验验证**。行为演练使用虚构项目与假工具状态；长期科研与协作效果留待真实使用按适配协议评估。
