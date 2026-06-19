class CreatePhoneVerificationCodes < ActiveRecord::Migration[5.0]
  def change
    create_table :phone_verification_codes do |t|
      # 注册前用于发送和校验短信验证码。
      t.string :cell_phone, null: false
      t.string :code, null: false
      t.datetime :expires_at, null: false
      t.datetime :verified_at
      t.bigint :created_by, null: false, default: 0
      t.bigint :last_updated_by, null: false, default: 0
      t.datetime :creation_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.datetime :last_update_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.integer :last_update_version, null: false, default: 0
      t.string :delete_flag, null: false, limit: 1, default: "N"
    end

    add_index :phone_verification_codes, :cell_phone
    add_index :phone_verification_codes, [:cell_phone, :code]

    reversible do |dir|
      dir.up do
        execute <<~SQL
          COMMENT ON TABLE phone_verification_codes IS '手机验证码表，记录投票者注册前请求的短信验证码';
          COMMENT ON COLUMN phone_verification_codes.id IS '主键';
          COMMENT ON COLUMN phone_verification_codes.cell_phone IS '接收验证码的手机号码';
          COMMENT ON COLUMN phone_verification_codes.code IS '短信验证码';
          COMMENT ON COLUMN phone_verification_codes.expires_at IS '验证码过期时间';
          COMMENT ON COLUMN phone_verification_codes.verified_at IS '验证码成功校验时间';
          COMMENT ON COLUMN phone_verification_codes.created_by IS '创建人，注册前尚无投票者账户时使用 0 表示系统流程';
          COMMENT ON COLUMN phone_verification_codes.last_updated_by IS '最后更新人，注册前尚无投票者账户时使用 0 表示系统流程';
          COMMENT ON COLUMN phone_verification_codes.creation_date IS '创建时间';
          COMMENT ON COLUMN phone_verification_codes.last_update_date IS '最后更新时间';
          COMMENT ON COLUMN phone_verification_codes.last_update_version IS '最后更新版本号，用于乐观更新控制';
          COMMENT ON COLUMN phone_verification_codes.delete_flag IS '删除标识，Y 表示已删除，N 表示有效';
        SQL
      end
    end
  end
end
