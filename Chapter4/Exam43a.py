def generate_ngrams(text, n):
    # Tách các từ trong câu
    words = text.split()

    # Sử dụng hàm zip để tạo các cặp liên tiếp trong danh sách các từ
    ngrams = zip(*[words[i:] for i in range(n)])

    # Sử dụng list comprehension để tạo ra các n-grams
    return [" ".join(ngram) for ngram in ngrams]


text = "this is a test sentence"
print(generate_ngrams(text, 2))
