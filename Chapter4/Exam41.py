import pandas as pd

# Danh sách các từ trong văn bản
# text="We are learning Natural Language Processing"

text="both good and distinctive good but not distinctive distinctive but not good or neither good nor distinctive"

words=text.split()

# Tạo DataFrame từ danh sách các từ
df = pd.DataFrame({'word': words})

# Thực hiện one-hot encoding
one_hot = pd.get_dummies(df['word'])

# Ghép kết quả vào DataFrame gốc
df = pd.concat([df, one_hot], axis=1)

print(df)