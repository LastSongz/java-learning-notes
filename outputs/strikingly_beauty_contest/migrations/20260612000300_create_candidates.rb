class CreateCandidates < ActiveRecord::Migration[5.0]
  def change
    create_table :candidates do |t|
      # 候选人列表每页展示 20 名候选人，并按 id 倒序排列。
      t.string :name, null: false, limit: 200
      t.integer :age, null: false
      t.string :video_url, null: false
      t.text :introduction, null: false
      t.integer :votes_count, null: false, default: 0
      t.bigint :created_by, null: false, default: 0
      t.bigint :last_updated_by, null: false, default: 0
      t.datetime :creation_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.datetime :last_update_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.integer :last_update_version, null: false, default: 0
      t.string :delete_flag, null: false, limit: 1, default: "N"
    end

    reversible do |dir|
      dir.up do
        execute <<~SQL
          COMMENT ON TABLE candidates IS '选美候选人表，记录候选人列表中展示的参赛人信息';
          COMMENT ON COLUMN candidates.id IS '主键，同时用于候选人列表倒序展示';
          COMMENT ON COLUMN candidates.name IS '候选人姓名，最大 200 个字符';
          COMMENT ON COLUMN candidates.age IS '候选人年龄，整数';
          COMMENT ON COLUMN candidates.video_url IS '候选人介绍视频链接';
          COMMENT ON COLUMN candidates.introduction IS '候选人富文本介绍，业务规则限制最多 1000 个单词';
          COMMENT ON COLUMN candidates.votes_count IS '候选人票数缓存，用于列表快速展示';
          COMMENT ON COLUMN candidates.created_by IS '创建人，候选人数据由系统初始化或导入时使用 0 表示系统用户';
          COMMENT ON COLUMN candidates.last_updated_by IS '最后更新人，候选人数据由系统初始化或导入时使用 0 表示系统用户';
          COMMENT ON COLUMN candidates.creation_date IS '创建时间';
          COMMENT ON COLUMN candidates.last_update_date IS '最后更新时间';
          COMMENT ON COLUMN candidates.last_update_version IS '最后更新版本号，用于乐观更新控制';
          COMMENT ON COLUMN candidates.delete_flag IS '删除标识，Y 表示已删除，N 表示有效';
        SQL
      end
    end
  end
end
