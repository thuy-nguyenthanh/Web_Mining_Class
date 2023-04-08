from sklearn.feature_extraction.text import CountVectorizer

# Dau vao la 2 cau van ban
Data = ["The quick brown fox jumps over the lazy dog and",
        "Never jump over the lazy dog quickly"]

# Xay dung vector BOW
vect = CountVectorizer()
X = vect.fit_transform(Data)

# Xay dung tu dien
dictionary=list(vect.get_feature_names_out())

print("Words in dictionary: ", dictionary)
print("Vector TF-IDF: \n", X.toarray())