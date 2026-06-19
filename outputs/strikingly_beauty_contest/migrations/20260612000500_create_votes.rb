class CreateVotes < ActiveRecord::Migration[5.0]
  def change
    create_table :votes do |t|
      # 每个投票者只能给一名候选人投票。
      t.bigint :voter_id, null: false
      t.bigint :candidate_id, null: false
      t.bigint :created_by, null: false, default: 0
      t.bigint :last_updated_by, null: false, default: 0
      t.datetime :creation_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.datetime :last_update_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.integer :last_update_version, null: false, default: 0
      t.string :delete_flag, null: false, limit: 1, default: "N"
    end

    add_index :votes, :candidate_id
    add_index :votes, :voter_id, unique: true

    reversible do |dir|
      dir.up do
        execute <<~SQL
          COMMENT ON TABLE votes IS '投票记录表，每个投票者只能给一名候选人投票';
          COMMENT ON COLUMN votes.id IS '主键';
          COMMENT ON COLUMN votes.voter_id IS '提交投票的投票者 id，不创建数据库外键约束';
          COMMENT ON COLUMN votes.candidate_id IS '被投票的候选人 id，不创建数据库外键约束';
          COMMENT ON COLUMN votes.created_by IS '创建人，记录实际提交投票的投票者 id';
          COMMENT ON COLUMN votes.last_updated_by IS '最后更新人，记录最后操作该投票记录的投票者 id';
          COMMENT ON COLUMN votes.creation_date IS '创建时间';
          COMMENT ON COLUMN votes.last_update_date IS '最后更新时间';
          COMMENT ON COLUMN votes.last_update_version IS '最后更新版本号，用于乐观更新控制';
          COMMENT ON COLUMN votes.delete_flag IS '删除标识，Y 表示已删除，N 表示有效';
        SQL
      end
    end
  end
end
