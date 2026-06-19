class CreateCandidatePictures < ActiveRecord::Migration[5.0]
  def change
    create_table :candidate_pictures do |t|
      # 每个候选人有一个 4 x 5 的图片网格，共 20 张照片。
      t.bigint :candidate_id, null: false
      t.string :image_url, null: false
      t.integer :position, null: false
      t.bigint :created_by, null: false, default: 0
      t.bigint :last_updated_by, null: false, default: 0
      t.datetime :creation_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.datetime :last_update_date, null: false, default: -> { "CURRENT_TIMESTAMP" }
      t.integer :last_update_version, null: false, default: 0
      t.string :delete_flag, null: false, limit: 1, default: "N"
    end

    add_index :candidate_pictures, [:candidate_id, :position], unique: true

    reversible do |dir|
      dir.up do
        execute <<~SQL
          COMMENT ON TABLE candidate_pictures IS '候选人照片表，记录每个候选人 4 x 5 图片网格中的 20 张照片';
          COMMENT ON COLUMN candidate_pictures.id IS '主键';
          COMMENT ON COLUMN candidate_pictures.candidate_id IS '候选人 id，不创建数据库外键约束';
          COMMENT ON COLUMN candidate_pictures.image_url IS '照片链接';
          COMMENT ON COLUMN candidate_pictures.position IS '照片展示位置，取值范围 1 到 20';
          COMMENT ON COLUMN candidate_pictures.created_by IS '创建人，照片数据由系统初始化或导入时使用 0 表示系统用户';
          COMMENT ON COLUMN candidate_pictures.last_updated_by IS '最后更新人，照片数据由系统初始化或导入时使用 0 表示系统用户';
          COMMENT ON COLUMN candidate_pictures.creation_date IS '创建时间';
          COMMENT ON COLUMN candidate_pictures.last_update_date IS '最后更新时间';
          COMMENT ON COLUMN candidate_pictures.last_update_version IS '最后更新版本号，用于乐观更新控制';
          COMMENT ON COLUMN candidate_pictures.delete_flag IS '删除标识，Y 表示已删除，N 表示有效';
        SQL
      end
    end
  end
end
