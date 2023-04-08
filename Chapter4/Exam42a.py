# -*- coding: utf-8 -*-
from functools import reduce

# ??u v�o l� m?t texts bao g?m 2 c�u v?n:
Data = ["The quick brown fox jumps over the lazy dog and",
        "Never jump over the lazy dog quickly"]

# B1. T�ch t?
texts=[]
for x in Data:
    texts.append([text for text in [x for x in x.lower().split()]])

# B2: X�y d?ng t? ?i?n
dictionary = sorted(list(set(reduce(lambda x, y: x + y, texts))))
print("Words in dictionary:",dictionary)

# B3: X�y d?ng vector TF-IDF
def bag_of_word(sentence):
    # Kh?i t?o m?t vector c� ?? d�i b?ng v?i t? ?i?n.
    vector = []

    # ??m c�c t? trong m?t c�u xu?t hi?n trong t? ?i?n.
    for word in dictionary:
        count = 0        
        
        # ??m s? t? xu?t hi?n trong m?t c�u.
        for w in sentence:
            if w == word:
                count += 1
        vector.append(count)
    return vector
            
print("Vector TF-IDF:")
for sentence in texts:
    print(bag_of_word(sentence))