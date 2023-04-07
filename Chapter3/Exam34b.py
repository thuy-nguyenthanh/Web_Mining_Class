import os

text="Theo giới chuyên môn, lối chơi của U20 Việt Nam khá đa dạng, linh hoạt hơn trong sơ đồ đội hình và chiến thuật, có khả năng chuyển tình thế nhanh trong tấn công và phòng ngự."

path=os.path.dirname(__file__)
f = open(path+r"\vietnamese-stopwords.txt", "r", encoding="utf-8")

#Get Stop words Dictionaries
List_StopWords=f.read().split("\n")

#remove stop words
text_pre=" ".join(text for text in text.split() if text not in List_StopWords)
print(text_pre)