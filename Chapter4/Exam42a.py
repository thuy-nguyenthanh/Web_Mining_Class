from functools import reduce

# Dau vao la 2 cau van ban
Data = ["The quick brown fox jumps over the lazy dog and",
        "Never jump over the lazy dog quickly"]

# B1. Tach tu
texts=[]
for x in Data:
    texts.append([text for text in [x for x in x.lower().split()]])

# B2: Xay dung tu dien
dictionary = sorted(list(set(reduce(lambda x, y: x + y, texts))))
print("Words in dictionary:",dictionary)

# B3: Xay dung vector BOW
def bag_of_word(sentence):
    vector = []

    # Dem cac tu trong cau xuat hien trong tu dien.
    for word in dictionary:
        count = 0        
        
        # Dem so tu xuat hien trong cau.
        for w in sentence:
            if w == word:
                count += 1
        vector.append(count)
    return vector
            
print("Vector Bag-of-Word:")
for sentence in texts:
    print(bag_of_word(sentence))