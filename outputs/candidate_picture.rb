class CandidatePicture < ApplicationRecord
  # 不在数据库层创建外键，但在 Active Record 层保留关联语义。
  belongs_to :candidate

  # 软删除数据默认不参与业务查询。
  scope :active, -> { where(delete_flag: "N") }

  validates :image_url, presence: true

  # position 表示照片在 4 x 5 网格中的展示位置，同一候选人下不能重复。
  validates :position,
            presence: true,
            numericality: {
              only_integer: true,
              greater_than_or_equal_to: 1,
              less_than_or_equal_to: 20
            },
            uniqueness: { scope: :candidate_id }

  validates :created_by, :last_updated_by, :creation_date, :last_update_date, presence: true
  validates :last_update_version, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :delete_flag, inclusion: { in: %w[Y N] }
end
