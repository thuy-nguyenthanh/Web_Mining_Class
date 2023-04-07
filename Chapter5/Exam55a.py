import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt

# Example text data
text_data = [
    "The quick brown fox jumps over the lazy dog.",
    "The quick brown fox jumps over the lazy dog.",
    "The quick brown fox jumps over the lazy dog and runs away.",
    "The lazy dog is not always quick to jump.",
    "The brown fox is quick and agile.",
    "The quick brown fox is a symbol of speed and cunning.",
    "The lazy dog is a symbol of relaxation and leisure."
]

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text_data)

# Find the optimal number of clusters using the elbow method
wcss = []
k_max=8
for i in range(2, k_max):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(2, k_max), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()