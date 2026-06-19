class Voter < ApplicationRecord
  # 投票者登录使用 username + password，密码通过 bcrypt 摘要保存。
  has_secure_password

  # 数据库存英文枚举值，页面展示时可通过 gender_label 转成中文。
  enum gender: { male: "male", female: "female" }

  GENDER_LABELS = {
    "male" => "男",
    "female" => "女"
  }.freeze

  # 每个投票者最多只能产生一条投票记录。
  has_one :vote, dependent: :destroy
  has_one :voted_candidate, through: :vote, source: :candidate

  # 软删除数据默认不参与业务查询。
  scope :active, -> { where(delete_flag: "N") }

  # 用户名规则来自注册页：6 到 20 位，只允许英文字母和数字。
  validates :username,
            presence: true,
            uniqueness: true,
            length: { in: 6..20 },
            format: { with: /\A[a-zA-Z0-9]+\z/ }

  # 手机号要求唯一；这里按香港 8 位号码处理，允许可选 +852 前缀。
  validates :cell_phone,
            presence: true,
            uniqueness: true,
            format: { with: /\A(\+852)?\d{8}\z/ }

  # 出生年份按四位整数校验。
  validates :gender, presence: true

  validates :year_of_birth,
            presence: true,
            numericality: {
              only_integer: true,
              greater_than_or_equal_to: 1000,
              less_than_or_equal_to: 9999
            }

  validates :password, confirmation: true, allow_nil: true
  validates :password_digest, presence: true
  validates :created_by, :last_updated_by, :creation_date, :last_update_date, presence: true
  validates :last_update_version, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :delete_flag, inclusion: { in: %w[Y N] }

  # 返回性别中文展示文案。
  def gender_label
    GENDER_LABELS[gender]
  end
end
