from sklearn.feature_extraction.text import CountVectorizer 

# Khởi tạo đối tượng CountVectorizer
# Tham số ngram_range=(1,2) cho biết chúng ta muốn sử dụng N-grams từ 1 đến 2.
vectorizer = CountVectorizer(ngram_range=(1,2))

# Tạo ra một list chứa các câu cần biểu diễn
Data = ["The quick brown fox jumps over the lazy dog and",
        "Never jump over the lazy dog quickly"]

# Biểu diễn vector đặc trưng cho các câu
features = vectorizer.fit_transform(Data)

# In ra các feature vector tương ứng với các câu
# Mỗi hàng trong ma trận tương ứng với một câu và mỗi cột tương ứng với một N-gram trong tất cả các câu. Giá trị của mỗi phần tử trong ma trận là số lần xuất hiện của N-gram đó trong câu tương ứng.
arr=features.toarray()

print("Vocabulary N-gram:")
# print(sorted(vectorizer.fit(["The quick brown fox jumps over the lazy dog and"]).vocabulary_))
print(vectorizer.fit(["The quick brown fox jumps over the lazy dog and"]).vocabulary_)
print(arr[0])

# print(sorted(vectorizer.fit(["Never jump over the lazy dog quickly"]).vocabulary_))
print(vectorizer.fit(["Never jump over the lazy dog quickly"]).vocabulary_)
print(arr[1])