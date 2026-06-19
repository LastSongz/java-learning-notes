# 香港选美投票系统 REST API 设计

## 设计说明

本文档按 Rails RESTful routing 的资源式设计原则组织 API。普通集合资源使用复数路径，例如 `/voters`、`/phone_verification_codes`、`/candidates`、`/votes`；当前登录会话是唯一资源，使用单数路径 `/session`。所有接口均使用 JSON 作为请求和响应格式。

需要登录的接口默认要求当前投票者已登录，可由 Rails Session 或其他认证机制实现，本文档不展开认证实现细节。

候选人列表每页 20 条，一共 100 名候选人时总页数为 5。候选人按数据库 `id` 倒序展示。候选人列表和详情接口都会返回当前投票者的投票状态，方便前端展示 `VOTE FOR ...`、`VOTED` 或隐藏其他候选人的投票按钮。

## 发送手机验证码 API

### URL

```http
POST /phone_verification_codes
```

### Request 示例

```http
POST /phone_verification_codes
```

```json
{
  "phone_verification_code": {
    "cell_phone": "+85261234567"
  }
}
```

### Response 示例

```json
{
  "phone_verification_code": {
    "cell_phone": "+85261234567",
    "expires_at": "2026-06-12T15:10:00Z",
    "next_request_after_seconds": 30
  }
}
```

## 投票者注册 API

### URL

```http
POST /voters
```

### Request 示例

```http
POST /voters
```

```json
{
  "voter": {
    "username": "mary123",
    "cell_phone": "+85261234567",
    "verification_code": "123456",
    "gender": "female",
    "year_of_birth": 1998,
    "password": "password123",
    "password_confirmation": "password123"
  }
}
```

### Response 示例

```json
{
  "voter": {
    "id": 1,
    "username": "mary123",
    "cell_phone": "+85261234567",
    "gender": "female",
    "gender_label": "女",
    "year_of_birth": 1998
  }
}
```

## 登录 API

### URL

```http
POST /session
```

### Request 示例

```http
POST /session
```

```json
{
  "session": {
    "username": "mary123",
    "password": "password123"
  }
}
```

### Response 示例

```json
{
  "voter": {
    "id": 1,
    "username": "mary123"
  }
}
```

## 登录用户名不存在错误 Response 示例

### URL

```http
POST /session
```

### Request 示例

```http
POST /session
```

```json
{
  "session": {
    "username": "unknown_user",
    "password": "password123"
  }
}
```

### Response 示例

```json
{
  "error": {
    "code": "INVALID_USERNAME",
    "message": "Invalid username"
  }
}
```

## 登录密码错误 Response 示例

### URL

```http
POST /session
```

### Request 示例

```http
POST /session
```

```json
{
  "session": {
    "username": "mary123",
    "password": "wrong_password"
  }
}
```

### Response 示例

```json
{
  "error": {
    "code": "WRONG_PASSWORD",
    "message": "Wrong password"
  }
}
```

## 登出 API

### URL

```http
DELETE /session
```

### Request 示例

```http
DELETE /session
```

### Response 示例

```json
{
  "message": "已登出"
}
```

## 候选人列表 API

### URL

```http
GET /candidates
```

### Request 示例

```http
GET /candidates?page=1
```

### Response 示例

```json
{
  "pagination": {
    "current_page": 1,
    "per_page": 20,
    "total_pages": 5,
    "total_count": 100,
    "previous_page": null,
    "next_page": 2
  },
  "current_voter": {
    "id": 1,
    "username": "mary123",
    "voted_candidate_id": 98
  },
  "candidates": [
    {
      "id": 100,
      "name": "Jane Doe",
      "age": 24,
      "video_url": "https://www.youtube.com/watch?v=example",
      "introduction": "<p>Candidate introduction...</p>",
      "votes_count": 36,
      "voted": false,
      "pictures": [
        {
          "id": 1,
          "image_url": "https://example.com/candidates/100/01.jpg",
          "position": 1
        },
        {
          "id": 2,
          "image_url": "https://example.com/candidates/100/02.jpg",
          "position": 2
        }
      ]
    }
  ]
}
```

## 候选人详情 API

### URL

```http
GET /candidates/:id
```

### Request 示例

```http
GET /candidates/100
```

### Response 示例

```json
{
  "current_voter": {
    "id": 1,
    "username": "mary123",
    "voted_candidate_id": 98
  },
  "candidate": {
    "id": 100,
    "name": "Jane Doe",
    "age": 24,
    "video_url": "https://www.youtube.com/watch?v=example",
    "introduction": "<p>Candidate introduction...</p>",
    "votes_count": 36,
    "voted": false,
    "pictures": [
      {
        "id": 1,
        "image_url": "https://example.com/candidates/100/01.jpg",
        "position": 1
      },
      {
        "id": 2,
        "image_url": "https://example.com/candidates/100/02.jpg",
        "position": 2
      }
    ]
  }
}
```

## 投票 API

### URL

```http
POST /votes
```

### Request 示例

```http
POST /votes
```

```json
{
  "vote": {
    "candidate_id": 100
  }
}
```

### Response 示例

```json
{
  "vote": {
    "id": 1,
    "voter_id": 1,
    "candidate_id": 100,
    "creation_date": "2026-06-12T15:20:00Z"
  },
  "candidate": {
    "id": 100,
    "votes_count": 37,
    "voted": true
  },
  "current_voter": {
    "id": 1,
    "username": "mary123",
    "voted_candidate_id": 100
  }
}
```

## 重复投票错误 Response 示例

### URL

```http
POST /votes
```

### Request 示例

```http
POST /votes
```

```json
{
  "vote": {
    "candidate_id": 99
  }
}
```

### Response 示例

```json
{
  "error": {
    "code": "ALREADY_VOTED",
    "message": "每个投票者只能投票一次"
  }
}
```

## Rails 路由参考

### URL

```ruby
resource :session, only: [:create, :destroy]
resources :phone_verification_codes, only: [:create]
resources :voters, only: [:create]
resources :candidates, only: [:index, :show]
resources :votes, only: [:create]
```

### Request 示例

```text
GET /candidates?page=1
GET /candidates/100
POST /votes
```

### Response 示例

```text
上述路由使用 Rails 资源式路由风格。当前会话使用单数资源 session；候选人、投票者、验证码、投票记录使用复数资源。
```

## 中文简要说明

数据库设计围绕投票者、验证码、候选人、候选人照片和投票记录五类核心资源展开。投票者通过用户名、手机号验证码、性别、出生年份和密码完成注册，密码只保存摘要。候选人保存姓名、年龄、视频链接、介绍文本和票数缓存，每个候选人通过候选人照片表维护 20 张照片，并使用 `position` 保证 4 x 5 网格中的展示顺序稳定。

API 设计遵循 Rails RESTful routing 的资源式原则：注册对应 `POST /voters`，当前会话登录对应单数资源 `POST /session`，登出对应 `DELETE /session`，候选人列表和详情分别对应 `GET /candidates` 与 `GET /candidates/:id`，投票对应 `POST /votes`。候选人列表和详情接口都会返回当前投票者的投票状态，便于前端根据是否已投票来展示 `VOTE FOR ...`、`VOTED` 或隐藏其他候选人的投票按钮。投票接口通过 `votes.voter_id` 唯一约束保证每个投票者只能投一次票。
