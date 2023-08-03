from utils.data import generate_seq_feature
# 构建用户历史行为序列特征，内置函数generate_seq_feature只需指定数据，
# 和需要生成序列的特征，drop_short是选择舍弃行为序列较短的用户

train, val, test = generate_seq_feature(data, seq_feature_col=['item_id', 'cate_id'], drop_short=0)
# 创建历史点击序列，历史类别序列
# ctr_trainer()
# fit()
# evaluate()
