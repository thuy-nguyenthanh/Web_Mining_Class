import pandas as pd
import os
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def create_dataframe(matrix, tokens):
    doc_names = [f'doc_{i+1}' for i, _ in enumerate(matrix)]
    df = pd.DataFrame(data=matrix, index=doc_names, columns=tokens)
    return(df)

def read_file(filename):	
    file_store=os.getcwd() + "\\Chapter5\\Data"
    filename=os.path.join(file_store, filename)        
    with open(filename, 'r',encoding="utf-8") as f:
        data = f.read()
    return data
    
def Text_Preprocessing(doc):
    text_pre=doc.lower()
    text_pre=re.sub(r'[^\w\s]','',text_pre)
    text_pre=re.sub("\d+", " ", text_pre)

    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text_pre)
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    text_pre = ' '.join(words)

    return text_pre

# Define the Data
doc_1=read_file("doc1.txt")	#Crawl from: https://www.nytimes.com/2023/03/31/technology/chatgpt-italy-ban.html
doc_2=read_file("doc2.txt") #Crawl from: https://www.abc.net.au/news/2023-04-01/chatgpt-ai-chatbot-blocked-itay-over-privacy-concerns/102175640
doc_3=read_file("doc3.txt") #Crawl from: https://en.wikipedia.org/wiki/Manchester_United_F.C.

doc_1=Text_Preprocessing(doc_1)
doc_2=Text_Preprocessing(doc_2)
doc_3=Text_Preprocessing(doc_3)

data = [doc_1, doc_2, doc_3]

# Vector matrix by CountVectorizer
count_vectorizer = CountVectorizer()

# Convert sparse vector matrix to numpy array to visualize the vectorized data of doc_1 and doc_2.
vector_matrix = count_vectorizer.fit_transform(data)

tokens = count_vectorizer. get_feature_names_out()
vector_matrix.toarray()
create_dataframe(vector_matrix.toarray(),tokens)

# Computing Cosine Similarity
cosine_similarity_matrix = cosine_similarity(vector_matrix)
Similarity=create_dataframe(cosine_similarity_matrix,['doc_1','doc_2','doc_3'])

print(Similarity)