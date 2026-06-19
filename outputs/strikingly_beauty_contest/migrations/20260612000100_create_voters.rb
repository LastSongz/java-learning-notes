class CreateVoters < ActiveRecord::Migration[5.0]
  def change
    create_table :voters do |t|
      # 字段来源于投票者注册页面。
      t.string :username, null: false, limit: 20
      t.string :cell_phone, null: false, limit: 20
      t.string :gender, null: false, limit: 10
      t.integer :year_of_birth, null: false
      t.string :password_digest, null: false, limit: 100
      t.bigint :created_by, null: false, default: 0
      t.bigint :last_updated_by, null: false, default: 0
      t.datetime :creation_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.datetime :last_update_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.integer :last_update_version, null: false, default: 0
      t.string :delete_flag, null: false, limit: 1, default: "N"
    end

    add_index :voters, :username, unique: true
    add_index :voters, :cell_phone, unique: true

    reversible do |dir|
      dir.up do
        execute <<~SQL
          COMMENT ON TABLE voters IS '投票者账户表，记录可登录并参与选美投票的用户';
          COMMENT ON COLUMN voters.id IS '主键';
          COMMENT ON COLUMN voters.username IS '登录用户名，长度 6 到 20 位，仅允许英文字母和数字';
          COMMENT ON COLUMN voters.cell_phone IS '香港手机号码，注册验证码发送号码，全表唯一';
          COMMENT ON COLUMN voters.gender IS '性别枚举值，male 表示男性，female 表示女性';
          COMMENT ON COLUMN voters.year_of_birth IS '出生年份，四位整数';
          COMMENT ON COLUMN voters.password_digest IS '加密后的密码摘要，配合 has_secure_password 使用';
          COMMENT ON COLUMN voters.created_by IS '创建人，注册成功后记录投票者自己的 id，0 表示系统用户';
          COMMENT ON COLUMN voters.last_updated_by IS '最后更新人，记录最后操作的投票者 id，0 表示系统用户';
          COMMENT ON COLUMN voters.creation_date IS '创建时间';
          COMMENT ON COLUMN voters.last_update_date IS '最后更新时间';
          COMMENT ON COLUMN voters.last_update_version IS '最后更新版本号，用于乐观更新控制';
          COMMENT ON COLUMN voters.delete_flag IS '删除标识，Y 表示已删除，N 表示有效';
        SQL
      end
    end
  end
end
