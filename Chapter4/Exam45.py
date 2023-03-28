#import library
#pip install gensim
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

#Example sentences
text=[  'I love nlp',
        'I will learn nlp in 2 months',
        'nlp is future',
        'nlp saves time and solves lot of',
        'industry problems',
        'nlp uses machine learning']
sentences=[]
for x in text:
    sentences.append(x.split())
# print(sentences)

# training the model
skipgram = Word2Vec(sentences, vector_size =50, window = 3, min_count=1,sg = 1)
# print(skipgram.wv.get_vector('nlp'))
# print(skipgram.wv.most_similar(positive=["love"]))


# save model
# skipgram.save('skipgram.bin')

# # load model
# skipgram = Word2Vec.load('skipgram.bin')


# T – SNE plot
X = skipgram.wv[skipgram.wv.index_to_key]
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(skipgram.wv.index_to_key)

for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))

pyplot.show()