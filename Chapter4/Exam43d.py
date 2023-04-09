from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import euclidean

texts=['you have no dog', 'no, you have dog', 'you have a dog']

# bigram
bigram = CountVectorizer(ngram_range = (2, 2))
n1, n2, n3 = bigram.fit_transform(texts).toarray()

# trigram
trigram = CountVectorizer(ngram_range = (3, 3))
n1, n2, n3 = trigram.fit_transform(texts).toarray()

#Su dung Euclidean de do khoang cach giua cac vector, tim ra do tuong tu giua cac cau
print(euclidean(n1, n2), euclidean(n2, n3), euclidean(n1, n3))

#--> 2.0 1.0 1.7320508075688772
#--> Cap cau (n2,n3) co do tuong tu cao nhat