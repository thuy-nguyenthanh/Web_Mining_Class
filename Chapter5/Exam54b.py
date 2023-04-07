# -*- coding: utf-8 -*-
#pip install underthesea
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import underthesea

def create_dataframe(matrix, tokens):
    doc_names = [f'doc_{i+4}' for i, _ in enumerate(matrix)]
    df = pd.DataFrame(data=matrix, index=doc_names, columns=tokens)
    return(df)

def read_file(filename):	
    file_store=os.getcwd() + "\\Chapter5\\Data"
    filename=os.path.join(file_store, filename)        
    with open(filename, 'r',encoding="utf-8") as f:
        data = f.read()

    return data.encode('utf-8')

def Text_Preprocessing(doc):
    text_pre = doc.lower()
    
    text_pre = underthesea.word_tokenize(text_pre, format="text")
    text_pre = underthesea.text_normalize(text_pre)
    
    ##Remove stop words
    path=os.path.dirname(__file__)
    f = open(path+r"\vietnamese-stopwords.txt", "r", encoding="utf-8")
    
    #Get Stop words Dictionaries
    List_StopWords=f.read().split("\n")
    text_pre=" ".join(text for text in text_pre.split() if text not in List_StopWords)
    
    return text_pre

# Define the Data
doc_4=read_file("doc4.txt")	#Crawl from: https://vi.wikipedia.org/wiki/X%E1%BB%AD_l%C3%BD_ng%C3%B4n_ng%E1%BB%AF_t%E1%BB%B1_nhi%C3%AAn
doc_5=read_file("doc5.txt") #Crawl from: https://en.wikipedia.org/wiki/Manchester_United_F.C.
doc_6=read_file("doc6.txt") #Crawl from: https://vi.wikipedia.org/wiki/Arsenal_F.C.


doc_4=Text_Preprocessing(doc_4)
doc_5=Text_Preprocessing(doc_5)
doc_6=Text_Preprocessing(doc_6)

data = [doc_4, doc_5, doc_6]

# Vector matrix by CountVectorizer
count_vectorizer = CountVectorizer()

# Convert sparse vector matrix to numpy array to visualize the vectorized data of doc_1 and doc_2.
vector_matrix = count_vectorizer.fit_transform(data)

tokens = count_vectorizer.get_feature_names_out()
vector_matrix.toarray()
create_dataframe(vector_matrix.toarray(),tokens)

# Computing Cosine Similarity
cosine_similarity_matrix = cosine_similarity(vector_matrix)
Similarity=create_dataframe(cosine_similarity_matrix,['doc_4','doc_5','doc_6'])

print(Similarity)