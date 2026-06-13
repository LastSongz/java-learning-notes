---
title: "闪卡 - Strikingly 面试专项"
created: 2026-06-14
updated: 2026-06-14
tags:
  - 类型/闪卡
  - 分类/面试
  - 公司/Strikingly
  - 主题/Rails
status: active
category: interview
---

#flashcards/Strikingly面试专项

## Strikingly 这次面试的能力画像是什么？
?
不是纯 Java 八股，也不是纯 Rails 熟手面试。重点是：
1. Java 后端基本盘是否扎实
2. 数据库设计和 REST API 设计是否清楚
3. Ruby/Rails 不是主栈时，是否能快速迁移
4. 是否有 SaaS/Web 后端的性能、可用性和安全意识
5. 云平台经验能否从华为云迁移到其他主流云
6. AI 应用后端和 agentic coding 是否能讲成真实工程能力
> 来源：[[Strikingly中级后端工程师面试复习清单]]

---

## 为什么注册接口使用 POST /voters，而不是 /sign_up？
?
Rails RESTful 风格里，URL 尽量表示资源，HTTP Method 表示动作。注册本质是“创建一个 voter 资源”，所以使用：

```http
POST /voters
```

而不是动作式路径 `/sign_up` 或 `/voterSignUp`。
> 来源：[[Rails RESTful Routing 面试速记]]、[[Strikingly中级后端工程师面试复习清单]]

---

## 为什么登录使用 POST /session，而不是 POST /sessions？
?
登录对应“创建当前会话”。对当前用户来说，会话是唯一资源，不需要通过 id 区分多个 session，所以 Rails 中更适合用单数资源：

```ruby
resource :session, only: [:create, :destroy]
```

对应：

```http
POST /session
DELETE /session
```
> 来源：[[Rails RESTful Routing 面试速记]]

---

## Rails RESTful API 命名为什么用小写下划线？
?
Rails 的资源路由通常由 Ruby/Rails 命名约定生成。模型类用大驼峰，例如 `PhoneVerificationCode`；表名和路径用小写下划线复数，例如：

```ruby
resources :phone_verification_codes
```

对应：

```http
POST /phone_verification_codes
```

不是 `/phoneVerificationCodes`。
> 来源：[[Rails RESTful Routing 面试速记]]

---

## 为什么这次笔试设计拆成五张核心表？
?
按页面展示和操作流程拆：
1. `voters`：投票者注册、登录、基础资料
2. `phone_verification_codes`：手机号验证码、过期时间、30 秒重复发送限制
3. `candidates`：候选人姓名、年龄、视频链接、介绍、票数缓存
4. `candidate_pictures`：每个候选人的 20 张照片
5. `votes`：投票记录，一个 voter 只能投一次
> 来源：[[Strikingly笔试设计复盘]]

---

## 为什么候选人的 20 张照片要单独建 candidate_pictures 表？
?
因为一个候选人对应多张照片，是一对多关系。如果把 20 个图片字段直接放在 `candidates` 表里，会导致字段膨胀、扩展性差、维护困难。单独建表后：
1. 结构更符合一对多建模
2. 便于维护每张照片的 URL 和展示顺序
3. 后续增减照片数量也更自然
> 来源：[[Strikingly笔试设计复盘]]

---

## candidate_pictures 为什么保留 position 字段？
?
`position` 表示照片在 4 x 5 网格中的展示位置。它比依赖 `id` 或插入顺序更稳定：
1. 上传/导入顺序不一定等于展示顺序
2. 后续替换某张照片时不影响位置语义
3. 可以通过 `candidate_id + position` 唯一约束避免同一位置重复
> 来源：[[Strikingly笔试设计复盘]]

---

## 如何保证一个投票者只能投一次票？
?
前端隐藏按钮只能改善体验，不能作为最终保证。后端要在数据库层兜底：

```ruby
add_index :votes, :voter_id, unique: true
```

并发请求同时进来时，只有一个 insert 能成功，另一个会因唯一约束失败，然后返回“已经投票”的错误。
> 来源：[[Strikingly笔试设计复盘]]、[[架构能力与工程实践面试清单]]

---

## 为什么 delete_flag 不建单列索引？
?
`delete_flag` 只有 `Y/N` 两种值，区分度很低。低基数字段建普通单列索引通常收益不大，优化器可能仍然选择全表扫描，还会增加写入维护成本。真正有查询压力时，可以考虑组合索引或 PostgreSQL partial index。
> 来源：[[MYSQL面试突击---索引]]、[[PostgreSQL面试速记]]

---

## PostgreSQL 的主键 id 默认都是 UUID 吗？
?
不是。PostgreSQL 支持 UUID，但不是默认主键类型。Rails + PostgreSQL 默认 `create_table` 通常会生成整数型主键，常见为 `bigint`/identity。因此关联字段使用 `bigint voter_id`、`bigint candidate_id` 是和 Rails 默认主键匹配的。

如果显式使用 UUID，需要：

```ruby
create_table :voters, id: :uuid
```

并配合 `pgcrypto` 等扩展。
> 来源：[[PostgreSQL面试速记]]

---

## 为什么这次设计不使用数据库外键？
?
这属于设计取舍。保留 Active Record 层的 `belongs_to` / `has_many` 关联语义，但 migration 不创建数据库外键约束，原因可以从工程侧解释：
1. 降低批量导入、数据修复、软删除时的约束耦合
2. 避免外键带来的写入顺序和迁移复杂度
3. 通过应用层校验、唯一索引和事务保证核心业务规则

注意：不建数据库外键不是不要关联，而是把约束更多放在应用层和索引层。
> 来源：[[Strikingly笔试设计复盘]]

---

## votes_count 为什么可以放在 candidates 表？
?
候选人列表需要频繁展示票数，如果每次都从 `votes` 表实时 `count`，访问量大时开销较高。`votes_count` 是计数缓存，配合 Rails `counter_cache` 可以在创建投票时自动维护，列表查询更快。

需要注意：核心事实仍然是 `votes` 表，`votes_count` 是为了读性能做的冗余。
> 来源：[[Strikingly笔试设计复盘]]

---

## Active Record validation 和数据库约束分别负责什么？
?
Validation 负责业务层的友好校验和错误提示，例如用户名长度、手机号格式、照片位置范围。数据库约束负责最后兜底，例如唯一索引、非空约束。高风险规则不能只靠 validation，因为并发下多个请求可能同时通过应用层校验，最终要靠数据库唯一约束保证一致性。
> 来源：[[Ruby与Rails面试速记]]

---

## Active Record association 在不建数据库外键时还有意义吗？
?
有意义。`has_many`、`belongs_to` 表达的是应用层对象关系，方便查询、级联操作和模型语义。即使数据库不建外键，Rails 仍然可以通过 `candidate_id`、`voter_id` 进行关联查询。只是数据完整性需要通过应用层校验、索引和业务流程来保证。
> 来源：[[Ruby与Rails面试速记]]

---

## 如何解释你愿意从 Java 转 Ruby/Rails？
?
可以这样说：

> 我过去主栈是 Java，但我不把后端能力绑定在某一种语言上。Web 后端核心还是业务建模、数据一致性、接口设计、性能和稳定性。Rails 和 Spring 写法不同，但很多工程问题是相通的。我愿意补 Ruby/Rails，是因为这个岗位更接近产品型 SaaS 后端，也能让我从外包项目经历转到自研产品长期演进。

> 来源：[[Strikingly面试动机与反问]]

---

## 如何表达华为云经验能迁移到主流云平台？
?
稳妥表达：

> 我主要是在华为云环境做业务系统开发，接触比较多的是 API 网关、对象存储、任务调度、日志监控和权限配置。虽然不是长期主用 AWS/Azure/GCP，但这些云产品的抽象比较接近，切换平台时重点是熟悉控制台、SDK、IAM 权限模型和具体产品差异。

避免说“几天就能完全上手”，容易显得轻率。
> 来源：[[云平台经验面试表达]]

---

## 如果候选人列表访问量很大，怎么优化？
?
可以从几层回答：
1. 数据库：按 `id desc` 做分页，避免深分页；必要时游标分页
2. 票数：使用 `votes_count` 计数缓存，避免每次实时 count
3. 图片：图片走对象存储/CDN，数据库只保存 URL
4. 缓存：候选人基础信息可以缓存，投票状态按当前 voter 单独处理
5. 限流：对投票接口做限流和防重复提交
> 来源：[[Strikingly笔试设计复盘]]、[[中间件专题-Redis与MQ]]

---

## 如果用户并发点击投票按钮两次，完整处理流程是什么？
?
1. 前端点击后禁用按钮，减少重复请求
2. 后端收到请求后校验当前 voter 是否已登录
3. 在事务中创建 vote，并更新候选人票数缓存
4. 数据库 `votes.voter_id` 唯一约束兜底
5. 如果唯一约束冲突，返回 `ALREADY_VOTED`
6. 前端展示 `VOTED`，隐藏其他候选人投票按钮
> 来源：[[Strikingly笔试设计复盘]]

---

## AI 聊天助手项目里，为什么不能让模型直接操作业务系统？
?
模型输出存在幻觉和不确定性，不能直接拥有业务系统操作权限。更安全的方式是：
1. 把能力封装成后端 Tool
2. 模型只负责选择工具和生成参数
3. 后端在工具执行前做权限校验和参数校验
4. 写操作通过微组件让用户二次确认
5. 执行结果和调用日志可审计
> 来源：[[AI项目面试话术]]、[[19-微组件与工具调用设计]]

---

## SSE 和 WebSocket 在聊天助手场景中怎么选？
?
聊天助手如果主要是服务端持续输出文本，客户端只需要接收流式内容，SSE 更简单：基于 HTTP、自动重连、实现成本低。WebSocket 适合强双向实时通信，例如多人协作、实时游戏。AI 回复流式输出通常用 SSE 就够了。
> 来源：[[LC-06-Agent异步调用与流式输出]]

---

## agentic coding 面试时不要怎么说？
?
不要只说“我会用 AI 写代码”。更好的表达是：
1. 我会先给 AI 项目上下文和验收标准
2. 让 AI 先读代码再给方案
3. 分步骤改动，控制范围
4. 看 diff，跑测试，必要时人工 review
5. 高风险动作需要确认和可回滚
> 来源：[[03-VibeCoding与AI编程工程化面试]]

---

## 为什么想从外包项目转到产品公司？
?
可以强调成长方向，不抱怨：

> 外包项目让我接触了复杂业务和大客户系统，但更多是围绕项目交付。现在我希望参与一个自研产品的长期演进，从需求、架构、质量、稳定性到用户反馈形成闭环。Strikingly 是 SaaS 产品公司，岗位又涉及后端稳定性、云平台和 Ruby/Rails 学习，对我来说是一次比较合适的转型机会。

> 来源：[[Strikingly面试动机与反问]]

---

## 面试反问：关于 Ruby/Rails 转栈应该问什么？
?
可以问：
1. Java 背景入职后，Ruby/Rails 的上手周期通常怎么安排？
2. 是否会有 mentor 或 code review 帮助熟悉 Rails 代码风格？
3. 前三个月主要目标是修 bug、做小需求，还是直接参与核心模块？
4. 团队如何评估新成员从其他语言迁移到 Rails 的进度？
> 来源：[[Strikingly面试动机与反问]]

---

## 面试反问：关于团队和业务应该问什么？
?
可以问：
1. 成都后端团队现在大概多少人？
2. 这个岗位主要负责现有 Rails 系统维护，还是新功能开发？
3. 后端服务的发布频率和线上故障响应机制是怎样的？
4. 当前主要使用哪些云服务，后端团队负责到什么深度？
> 来源：[[Strikingly面试动机与反问]]
