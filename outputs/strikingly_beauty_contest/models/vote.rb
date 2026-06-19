class Vote < ApplicationRecord
  # 不在数据库层创建外键，但在 Active Record 层保留关联语义。
  belongs_to :voter
  # 使用 counter_cache 自动维护 candidates.votes_count。
  belongs_to :candidate, counter_cache: true

  # 软删除数据默认不参与业务查询。
  scope :active, -> { where(delete_flag: "N") }

  # voter_id 唯一表示一个投票者只能投给一个候选人。
  validates :voter_id, uniqueness: true
  validates :created_by, :last_updated_by, :creation_date, :last_update_date, presence: true
  validates :last_update_version, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :delete_flag, inclusion: { in: %w[Y N] }
end
