from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def create_dataframe(matrix, tokens):
    doc_names = [f'doc_{i+1}' for i, _ in enumerate(matrix)]
    df = pd.DataFrame(data=matrix, index=doc_names, columns=tokens)
    return(df)

# Define the Data
doc_1 = "Data is the oil of the digital economy"
doc_2 = "Data is a new oil"

data = [doc_1, doc_2]

# Vector matrix by CountVectorizer
count_vectorizer = CountVectorizer()

# Convert sparse vector matrix to numpy array to visualize the vectorized data of doc_1 and doc_2.
vector_matrix = count_vectorizer.fit_transform(data)

tokens = count_vectorizer. get_feature_names_out()
vector_matrix.toarray()
create_dataframe(vector_matrix.toarray(),tokens)

# Find Cosine Similarity
cosine_similarity_matrix = cosine_similarity(vector_matrix)
Similarity=create_dataframe(cosine_similarity_matrix,['doc_1','doc_2'])

print(Similarity)