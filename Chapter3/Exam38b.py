#Install underthesea library
# pip install underthesea
from underthesea import word_tokenize

text="U20 Việt Nam kỳ vọng vào tấm vé đi tiếp ngay cả khi không thể có kết quả tốt trước Iran"
text_pre= word_tokenize(text, format="text")
print(text_pre)