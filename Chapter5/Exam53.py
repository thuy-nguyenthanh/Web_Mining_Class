import pandas as pd
import numpy as np
from scipy.spatial import distance

text_1 = "I love ice cream"
text_2 = "I like ice cream"
text_3 = "I offer ice cream to the lady that I love"

## Create a list of the sentences
texts = [text_1, text_2, text_3]

from sklearn.feature_extraction.text import CountVectorizer

## Firstly let's count the words using the CountVectorizer
count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer = CountVectorizer()
matrix = count_vectorizer.fit_transform(texts)

## we can create a dataframe to represent the number of the words in every sentence
table = matrix.todense()
df = pd.DataFrame(table, 
                  columns=count_vectorizer.get_feature_names_out(), 
                  index=['text_1', 'text_2', 'text_2'])
print(df)


## Compute the Euclidean distance of these sentences
matrix = distance.cdist(df, df, 'euclidean')

df_eucl = pd.DataFrame(matrix, 
                  columns= ["Text_1", "Text_2", "Text_3"],
                  index=['text_1', 'text_2', 'text_3'])
print(df_eucl)