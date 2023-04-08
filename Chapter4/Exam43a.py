def generate_ngrams(text, n):
    # Tach tu
    words = text.split()

    # Su dung ham zip de tach cac cap tu lien tiep trong danh sach cac tu
    ngrams = zip(*[words[i:] for i in range(n)])

    # Su dung list comprehension de tao n-grams
    return [" ".join(ngram) for ngram in ngrams]

text = "this is a test sentence"
print(generate_ngrams(text, 2))
