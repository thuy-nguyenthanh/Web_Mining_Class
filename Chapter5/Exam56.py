# -*- coding: utf-8 -*-
import re
import os
from unidecode import unidecode
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.manifold import MDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import random

# Ham tach tu va chuan hoa
def tokenize_and_stem(text):
    stemmer = SnowballStemmer("english")
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
            
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

# Ham tach tu
def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

# Ham tien xu ly van ban
def TextPreprocessing(corpus):
    stopwords = nltk.corpus.stopwords.words("english")
    stemmer = SnowballStemmer("english")
    
    for document in corpus:
        index = corpus.index(document)
        
        corpus[index] = corpus[index].replace('XXXX', '')        
        corpus[index] = corpus[index].replace(u'\ufffd', '8')   # Replaces the ASCII symbol with '8'
        corpus[index] = corpus[index].replace(',', '')          # Removes commas
        corpus[index] = corpus[index].rstrip('\n')              # Removes line breaks
        corpus[index] = corpus[index].casefold()                # Makes all letters lowercase
        
        corpus[index] = re.sub('\W_',' ', corpus[index])        # removes specials characters and leaves only words
        corpus[index] = re.sub("\S*\d\S*"," ", corpus[index])   # removes numbers and words concatenated with numbers IE h4ck3r. Removes road names such as BR-381.
        corpus[index] = re.sub("\S*@\S*\s?"," ", corpus[index]) # removes emails and mentions (words with @)
        corpus[index] = re.sub(r'http\S+', '', corpus[index])   # removes URLs with http
        corpus[index] = re.sub(r'www\S+', '', corpus[index])    # removes URLs with www

        listOfTokens = word_tokenize(corpus[index])
        listOfTokens = [token for token in listOfTokens if token not in stopwords]
        listOfTokens = [stemmer.stem(token) for token in listOfTokens] #applyStemming(listOfTokens, param_stemmer)        
        
        corpus[index]   = " ".join(listOfTokens)
        corpus[index] = unidecode(corpus[index])
    return corpus

def Silhouette_Score(X):
    # Find the optimal number of clusters using the Silhouette Score
    silhouette_scores = []
    for i in range(2, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        labels = kmeans.labels_
        score = silhouette_score(X, labels)
        silhouette_scores.append(score)
        
    # Plot the Silhouette Scores
    import matplotlib.pyplot as plt
    plt.plot(range(2, 11), silhouette_scores)
    plt.title('Silhouette Score')
    plt.xlabel('Number of clusters')
    plt.ylabel('Score')
    plt.show()
    
def Read_Data():    
    # Doc du lieu
    path=os.path.dirname(__file__)
    Data = pd.read_csv(path + "\\Data\\consumer_complaints.csv",encoding='latin-1', low_memory=False)
    # Thiet lap du lieu
    Data = Data[['consumer_complaint_narrative']]
    Data = Data[pd.notnull(Data['consumer_complaint_narrative'])]
    
    print(Data[:10])
    
    # Chon 1000 dong du lieu de xu ly
    Data_sample=Data.sample(1000)
    print(Data_sample)

    # Convert dataframe to list
    complaints = Data_sample['consumer_complaint_narrative'].tolist()    
    return complaints

def Vectorize_TFIDF(corpus):
    # Xay dung vector dac trung TF-IDF
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,min_df=0.2, use_idf=True, ngram_range=(1,3))
    X = tfidf_vectorizer.fit_transform(corpus)
    terms = tfidf_vectorizer.get_feature_names_out()
    print(X.shape)    
    return X, terms


def Elbow_Score(X):
    # Find the optimal number of clusters using the elbow method
    wcss = []
    for i in range(2, 1):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(2, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

def Elbow_Score(X):
    # Find the optimal number of clusters using the elbow method
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
    
def Run_KMeans(X,num_clusters):
    km = KMeans(n_clusters=num_clusters, n_init=8)
    km.fit(X)
    return km

def Presentation_Data(complaints,km,num_clusters):
    ranks = []
    for i in range(1, len(complaints)+1):
        ranks.append(i)
        
    clusters = km.labels_.tolist()
    complaints_data = { 'rank': ranks, 'complaints': complaints,'cluster': clusters }
    frame = pd.DataFrame(complaints_data, index = [clusters] , columns =['rank', 'cluster'])

    # Thong ke so luong van ban o moi cum
    print("Numbers of Docs per cluster:")
    print(frame['cluster'].value_counts().sort_index())

    # Xac dinh 5 tu o gan tam cua moi cum nhat    
    totalvocab_stemmed = []
    totalvocab_tokenized = []
    for i in complaints:
        allwords_stemmed = tokenize_and_stem(i)
        totalvocab_stemmed.extend(allwords_stemmed)
        allwords_tokenized = tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)
        
    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index =totalvocab_stemmed)

    #sort cluster centers by proximity to centroid
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    print("Top 5 words closest to the cluster centers:")
    for i in range(num_clusters):
        print("Cluster %d words: " % i, end='')
        for ind in order_centroids[i, :6]:
            print(vocab_frame.loc[terms[ind].split(' ')].values.tolist()[0][0], end=', ')
        print()        

    # Bieu dien tren bang do nhiet
    similarity_distance = 1 - cosine_similarity(X)

    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(similarity_distance)
    xs, ys = pos[:, 0], pos[:, 1]

    # Thiet lap mau cho moi cum
    cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e', 5: '#2300FF', 6: '#FF88AE', 7: '#FFED88', 8: '#FF88FA', 9: '#88FF9F'}    

    # Thiet lap ten cho moi cum
    cluster_names=dict()
    for i in range(0,num_clusters):
        cluster_names[i]= "Cluster" + str(i)

    df = pd.DataFrame(dict(x=xs, y=ys, label=clusters))
    groups = df.groupby('label')

    # Set up plot
    fig, ax = plt.subplots(figsize=(17, 9))
    for name, group in groups:
        ax.plot(group.x, group.y, marker="o", linestyle='',ms=20,label=cluster_names[name], color=cluster_colors[name],mec='none')
        ax.set_aspect('auto')
        ax.tick_params(axis= 'x', which='both', bottom='off', top='off', labelbottom='off')
        ax.tick_params(axis= 'y', which='both', left='off', top='off',labelleft='off')
        
    ax.legend(numpoints=1)
    plt.show()
    

#######################################################################################
#??c d? li?u
complaints=Read_Data()

#Ti?n x? lý
complaints=TextPreprocessing(complaints)

# Trích xu?t ??c tr?ng v?n b?n
X, terms= Vectorize_TFIDF(complaints)

# Ch?m ?i?m giá tr? K c?a thu?t toán K-Means - Ph??ng pháp Silhouette Score (?i?m bóng)
# Elbow_Score(X)
Silhouette_Score(X)


# Ch?y gi?i thu?t K-Means
num_clusters = 8
km=Run_KMeans(X,num_clusters)

# Bi?u di?n d? li?u
Presentation_Data(complaints,km,num_clusters)