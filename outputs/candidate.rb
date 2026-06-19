class Candidate < ApplicationRecord
  # 每个候选人有 20 张照片，按 position 展示成 4 x 5 网格。
  has_many :candidate_pictures, dependent: :destroy
  # 候选人可以收到多条投票记录。
  has_many :votes, dependent: :destroy
  has_many :voters, through: :votes

  # 软删除数据默认不参与业务查询。
  scope :active, -> { where(delete_flag: "N") }

  # 候选人姓名最多 200 个字符；介绍文本按规格限制最多 1000 个单词。
  validates :name, presence: true, length: { maximum: 200 }
  validates :age, presence: true, numericality: { only_integer: true }
  validates :video_url, presence: true
  validates :introduction, presence: true, length: { maximum: 1000 }
  validates :votes_count,
            numericality: {
              only_integer: true,
              greater_than_or_equal_to: 0
            }
  validates :created_by, :last_updated_by, :creation_date, :last_update_date, presence: true
  validates :last_update_version, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :delete_flag, inclusion: { in: %w[Y N] }

  # 候选人列表按数据库 id 倒序展示，每页 20 条由分页层处理。
  scope :ordered_for_listing, -> { active.order(id: :desc) }
end
