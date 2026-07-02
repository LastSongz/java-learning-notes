---
title: "OpenCode与OpenSpec训练稿-20分钟"
created: 2026-07-02
updated: 2026-07-02
tags:
  - 分类/ai
  - 主题/AI编程
  - 主题/VibeCoding
  - 主题/工程化
status: draft
category: training
---

# OpenCode + OpenSpec + Superpowers：20 分钟 Vibe Coding 工程化培训稿

> 适用场景：团队内部分享、AI 编程工作流培训、面试/项目复盘讲解。
> 核心目标：把 Vibe Coding 从“靠感觉让 AI 写代码”，升级成“有需求、有规范、有测试、有验收证据”的工程化流程。

## 一、培训目标

听完这 20 分钟后，学员应该能回答三个问题：

1. 为什么直接让 AI 写代码容易跑偏？
2. OpenCode、OpenSpec、Superpowers 分别解决什么问题？
3. 一个真实需求应该如何从想法走到实现、验证和归档？

一句话结论：

> OpenCode 是执行器，OpenSpec 是需求和规格层，Superpowers 是工程纪律层。三者组合后，人负责意图、边界和验收，AI 负责探索、实现和重复劳动。

## 二、20 分钟时间安排

| 时间 | 主题 | 讲解目标 |
| --- | --- | --- |
| 0:00 - 2:00 | 开场：Vibe Coding 的机会和风险 | 先建立问题意识 |
| 2:00 - 5:00 | 三个工具的定位 | 说明 OpenCode、OpenSpec、Superpowers 的职责 |
| 5:00 - 10:00 | 标准工作流 | 讲清楚从需求到代码的步骤 |
| 10:00 - 16:00 | 示例：订单取消需求 | 用一个后端需求串完整流程 |
| 16:00 - 18:00 | 质量门禁 | 强调 TDD、verify、人工 review |
| 18:00 - 20:00 | 总结和落地建议 | 给出团队采用方式 |

## 三、开场：为什么 Vibe Coding 需要工程化

可以这样开场：

> 现在 AI Coding Agent 已经不只是补全代码了，它能读仓库、改文件、跑命令、生成 PR。问题是，能力越强，跑偏的代价也越大。如果需求不清楚，它会很认真地写错；如果没有测试，它会很自信地说完成；如果没有规范，它每次都像换了一个新人。

传统 Vibe Coding 的常见问题：

- 需求只在聊天记录里，后续无法追踪。
- AI 先写代码，之后才补测试，测试容易验证实现而不是验证需求。
- 一次改太大，diff 很难 review。
- 没有明确验收标准，最后只能靠感觉判断“差不多”。
- 长对话后上下文污染，AI 忘记前面的约束。

要强调的观点：

> 高质量 Vibe Coding 不是少写代码，而是把人的工程判断前置，把 AI 的执行能力放进可控流程里。

## 四、三个工具的职责分工

### 1. OpenCode：执行器

OpenCode 是开源 AI coding agent，可以在终端、IDE、桌面端使用。它的价值是把 AI 放到真实工程环境里：

- 通过 `/init` 读取项目并生成 `AGENTS.md`。
- 使用 Plan agent 做只读分析和方案设计。
- 使用 Build agent 写代码、改文件、跑命令。
- 使用 subagents 做探索、外部文档查询、并行任务。
- 支持 skills、commands、MCP、LSP。

讲解话术：

> OpenCode 解决的是“AI 如何进入我的工程现场”。它能读文件、改代码、运行测试，但它本身不保证需求正确，也不保证工程纪律。所以我们还需要 OpenSpec 和 Superpowers。

### 2. OpenSpec：需求和规格层

OpenSpec 是轻量级 spec-driven development 工具。它把一次需求变成仓库里的可审查文件：

```text
openspec/changes/add-order-cancel/
├── proposal.md  # 为什么做、范围是什么
├── design.md    # 技术方案和设计决策
├── tasks.md     # 实现任务清单
└── specs/       # 需求规格 delta
```

常用命令：

```text
/opsx:explore   # 需求还不清楚时，先探索方案
/opsx:propose   # 生成 proposal/spec/design/tasks
/opsx:apply     # 按 tasks 实现
/opsx:verify    # 检查实现是否匹配规格
/opsx:sync      # 把 delta 合并到主 specs
/opsx:archive   # 归档已完成 change
```

讲解话术：

> OpenSpec 解决的是“需求不要只活在聊天里”。它让需求、设计、任务和验收标准进入 Git，变成可以 review、可以复用、可以追责的工程资产。

### 3. Superpowers：工程纪律层

Superpowers 不是另一个编码工具，而是一组强制流程 skill。它解决的是 AI Coding 最容易偷懒的地方：

- `brainstorming`：需求不清楚时，先问问题、做方案比较，不急着写代码。
- `writing-plans`：把需求拆成小任务，每一步都有文件、测试和验证命令。
- `test-driven-development`：先写失败测试，再写实现。
- `verification-before-completion`：没有新鲜验证证据，不允许说“完成”。
- `subagent-driven-development`：大任务按子任务派发，每步做规格 review 和代码质量 review。

讲解话术：

> Superpowers 解决的是“AI 太想直接完成”。它强制 AI 像一个严谨工程师那样工作：先理解，再设计，再测试，再实现，再验证。

## 五、标准工作流

这套组合推荐的开发链路如下：

```text
需求想法
  ↓
OpenSpec explore / Superpowers brainstorming
  ↓
OpenSpec propose 生成 proposal/spec/design/tasks
  ↓
人工 review 需求和方案
  ↓
Superpowers writing-plans 拆成 TDD 小步骤
  ↓
OpenCode Build agent / opsx apply 实现
  ↓
Superpowers TDD + 测试验证
  ↓
OpenSpec verify 检查规格一致性
  ↓
人工 review diff
  ↓
OpenSpec sync/archive 沉淀规格
```

可以把它压缩成一句话：

> 先把“想做什么”固定下来，再让 AI 做“怎么实现”，最后用测试和规格反查“有没有做对”。

## 六、示例讲解：订单取消需求

假设我们要给 Java 后端订单系统增加“取消订单”能力。

### 1. 不推荐的做法

直接对 AI 说：

```text
帮我加一个订单取消接口。
```

这个提示太模糊。AI 可能会自己猜：

- 哪些订单状态允许取消？
- 已支付订单能不能取消？
- 取消后库存是否回滚？
- 需要写操作日志吗？
- 是否影响退款流程？
- 接口幂等怎么做？

讲解重点：

> AI 不怕写代码，怕的是它在没有业务答案时替你做业务决策。

### 2. 使用 OpenSpec 先探索

在 OpenCode 的 Plan agent 中输入：

```text
/opsx:explore 我们要给订单系统增加取消订单能力。
请先阅读订单状态流转、支付状态、库存扣减相关代码。
不要写代码，只提出关键问题和可选方案。
```

期望 AI 先输出类似问题：

- 待支付订单取消：是否直接关闭？
- 已支付未发货订单取消：是否进入退款流程？
- 已发货订单取消：是否禁止？
- 重复取消：是否返回成功还是报错？
- 是否需要记录取消原因？

这一步可以结合 Superpowers `brainstorming`：

```text
请按 brainstorming 流程推进：
一次只问一个关键问题；
给出 2-3 种方案和取舍；
最后形成推荐设计，不要实现。
```

### 3. 生成 OpenSpec change

需求明确后，创建 change：

```text
/opsx:propose add-order-cancel
```

应生成：

```text
openspec/changes/add-order-cancel/
├── proposal.md
├── design.md
├── tasks.md
└── specs/order-lifecycle/spec.md
```

可以要求规格写成 Given / When / Then：

```md
### Requirement: Cancel unpaid order
The system SHALL allow a user to cancel an unpaid order.

#### Scenario: Cancel pending payment order
- GIVEN an order is in PENDING_PAYMENT status
- WHEN the user cancels the order
- THEN the order status becomes CANCELLED
- AND no refund is created
```

讲解重点：

> 这时我们 review 的不是代码，而是意图。越早发现需求错，返工成本越低。

### 4. 用 Superpowers 强化任务拆解

对 AI 说：

```text
请读取 openspec/changes/add-order-cancel/tasks.md、design.md 和 specs。
使用 writing-plans 的粒度，把任务拆成 TDD 小步骤：
先写失败测试，再最小实现，再运行验证。
不要扩大 scope。
```

理想任务应该类似：

```text
1. 写 OrderCancelServiceTest：待支付订单取消后状态变为 CANCELLED。
2. 运行测试，确认因为 cancel 方法不存在而失败。
3. 实现 OrderCancelService.cancel(orderId, userId)。
4. 再运行该测试，确认通过。
5. 增加已发货订单不可取消测试。
6. 实现状态校验。
7. 增加重复取消幂等测试。
8. 跑订单模块完整测试。
```

讲解重点：

> tasks.md 不是简单 todo，而是 AI 的施工图。施工图越清楚，AI 越不容易自由发挥。

### 5. 实现阶段

执行：

```text
/opsx:apply add-order-cancel
```

同时加约束：

```text
执行时必须使用 test-driven-development：
每个行为先写测试并运行到失败；
再写最小实现；
最后运行对应测试和相关回归测试。
```

如果是 Java 后端，可以要求验证命令明确：

```bash
mvn test -Dtest=OrderCancelServiceTest
mvn test -pl order-service
```

讲解重点：

> TDD 对 AI 更重要。人写代码还能凭经验停一下，AI 经常会一口气写完。测试先行是在给 AI 铺轨道。

### 6. 验收阶段

先跑 OpenSpec 验证：

```text
/opsx:verify add-order-cancel
```

检查三件事：

- Completeness：所有任务是否完成，所有需求是否有实现。
- Correctness：实现是否匹配 spec，边界条件是否覆盖。
- Coherence：代码结构是否符合 design.md。

再跑 Superpowers 的 completion gate：

```text
使用 verification-before-completion。
请运行订单模块测试和完整构建。
只有看到 exit 0，才允许说完成。
```

最后同步和归档：

```text
/opsx:sync add-order-cancel
/opsx:archive add-order-cancel
```

讲解重点：

> 完成不是 AI 说完成，而是证据说完成。证据包括测试输出、diff、spec verify、人工 review。

## 七、团队落地建议

### 第一阶段：先固定入口

每个项目先做三件事：

```bash
opencode
/init
openspec init --tools opencode
```

然后把 `AGENTS.md` 提交进仓库，写清楚：

- 构建命令
- 测试命令
- 分层约定
- 代码风格
- 高风险操作限制
- 必须使用 OpenSpec 的场景

### 第二阶段：规定需求分级

| 需求类型 | 推荐流程 |
| --- | --- |
| 小修小补 | OpenCode Plan -> Build -> 测试 |
| 普通功能 | `/opsx:propose` -> review -> `/opsx:apply` -> `/opsx:verify` |
| 核心业务规则 | OpenSpec + Superpowers TDD + 人工 review |
| 大型重构 | OpenSpec 分多个 change + subagent-driven-development |

### 第三阶段：建立质量红线

建议团队明确这些规则：

- 没有 spec 的复杂需求，不允许直接实现。
- 没有失败测试的行为变更，不允许直接写生产代码。
- 没有新鲜验证输出，不允许说完成。
- AI 生成的代码必须 review diff。
- OpenSpec change 完成后必须 sync/archive，让规格沉淀下来。

## 八、常见误区

### 误区 1：OpenSpec 会拖慢开发

正确理解：

> 它会增加前 10 分钟，但减少后面 2 小时返工。尤其是业务规则多、边界条件多的需求，先写 spec 反而更快。

### 误区 2：Plan mode 已经够了，不需要 OpenSpec

正确理解：

> Plan mode 适合当前会话；OpenSpec 适合跨会话、跨人、跨 PR。计划如果只在聊天里，长任务中断后就很难恢复。

### 误区 3：测试可以最后补

正确理解：

> 测试最后补，容易测试你已经写出来的实现；测试先写，才是在验证需求本身。

### 误区 4：AI 越自动越好

正确理解：

> 生产开发不是追求 AI 自动写最多代码，而是让 AI 在边界内快速产出可验证结果。

## 九、结尾总结

最后 1 分钟可以这样收束：

> Vibe Coding 的上限不取决于你会不会写提示词，而取决于你能不能设计一套让 AI 稳定工作的工程系统。OpenCode 让 AI 进入项目现场，OpenSpec 把需求和设计变成可追踪资产，Superpowers 把 TDD、计划、验证这些纪律强制执行。三者组合后，我们不是把代码交给 AI，而是把重复劳动交给 AI，把工程判断留在人手里。

三个关键词：

- **Spec first**：先对齐意图，再写代码。
- **Test first**：先证明需求会失败，再让实现通过。
- **Evidence first**：先跑验证，再说完成。

## 十、演示命令速查

```bash
# 安装
npm install -g opencode-ai
npm install -g @fission-ai/openspec@latest

# 进入项目
cd your-project
opencode

# 初始化 OpenCode 项目规则
/init

# 初始化 OpenSpec，并为 OpenCode 生成命令和 skill
openspec init --tools opencode

# 需求探索
/opsx:explore

# 生成需求变更
/opsx:propose add-order-cancel

# 实现
/opsx:apply add-order-cancel

# 验证实现与规格一致
/opsx:verify add-order-cancel

# 合并规格并归档
/opsx:sync add-order-cancel
/opsx:archive add-order-cancel
```

## 十一、讲师提示

- 不要把这节课讲成工具安装课，重点是开发思想。
- 示例一定要选有业务状态和边界条件的需求，比如订单取消、审批流、权限控制。
- 多强调“AI 不应该替人做业务决策”。
- 现场可以让学员说一个需求，然后当场演示如何把一句话需求拆成 spec 场景。
- 讲完后留一个小练习：让学员把“用户可以修改手机号”写成 3 条 Given / When / Then 场景。

## 参考资料

- OpenCode 官方文档：https://opencode.ai/docs/
- OpenCode Rules：https://opencode.ai/docs/rules/
- OpenCode Agents：https://opencode.ai/docs/agents/
- OpenCode Agent Skills：https://opencode.ai/docs/skills/
- OpenSpec 官网：https://openspec.dev/
- OpenSpec Commands：https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md
- OpenSpec Supported Tools：https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md

---

**相关笔记**：[[03-VibeCoding与AI编程工程化面试]] | [[08-Agent与Multi-Agent面试题]] | [[10-AI Agent]] | [[15-AI工作流]] | [[MOC-AI与大模型学习]]