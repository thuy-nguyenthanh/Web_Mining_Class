# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer

# ??u v�o l� m?t texts bao g?m 2 c�u v?n:
Data = ["The quick brown fox jumps over the lazy dog and",
        "Never jump over the lazy dog quickly"]

# X�y d?ng vector TF-IDF
vect = CountVectorizer()
X = vect.fit_transform(Data)

# X�y d?ng t? ?i?n
dictionary=list(vect.get_feature_names_out())

print("Words in dictionary: ", dictionary)
print("Vector TF-IDF: \n", X.toarray())