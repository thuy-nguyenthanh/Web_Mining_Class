from sklearn.feature_extraction.text import CountVectorizer
import nltk

# Text
text = "The quick brown fox jumps over the lazy dog And Never jump over the lazy dog quickly"

#Tokenization
sentences = nltk.sent_tokenize(text)

# create the transform
vectorizer = CountVectorizer()

# tokenizing
vectorizer.fit(sentences)

# encode document
vector = vectorizer.transform(sentences)

# summarize & generating output
vectorizer.vocabulary_ =sorted(vectorizer.vocabulary_)

print(vectorizer.vocabulary_)
print(vector.toarray())