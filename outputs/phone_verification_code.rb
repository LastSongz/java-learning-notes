class PhoneVerificationCode < ApplicationRecord
  # 软删除数据默认不参与业务查询。
  scope :active, -> { where(delete_flag: "N") }

  # 注册验证码发送前先校验手机号格式。
  validates :cell_phone,
            presence: true,
            format: { with: /\A(\+852)?\d{8}\z/ }

  validates :code, presence: true
  validates :expires_at, presence: true
  validates :created_by, :last_updated_by, :creation_date, :last_update_date, presence: true
  validates :last_update_version, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :delete_flag, inclusion: { in: %w[Y N] }

  # 判断验证码是否已经过期。
  def expired?
    Time.current > expires_at
  end

  # 判断验证码是否已经完成校验。
  def verified?
    verified_at.present?
  end

  # 规格要求同一手机号 30 秒内不能重复请求验证码。
  def can_request_again?
    creation_date.blank? || creation_date <= 30.seconds.ago
  end
end
