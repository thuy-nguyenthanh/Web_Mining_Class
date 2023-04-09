from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score

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

# Find the optimal number of clusters using the Silhouette Score
silhouette_scores = []
k_max=8
for i in range(2, k_max):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    labels = kmeans.labels_
    score = silhouette_score(X, labels)
    silhouette_scores.append(score)
    
# Plot the Silhouette Scores
import matplotlib.pyplot as plt
plt.plot(range(2, k_max), silhouette_scores)
plt.title('Silhouette Score')
plt.xlabel('Number of clusters')
plt.ylabel('Score')
plt.show()