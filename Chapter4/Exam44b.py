#Reference source: https://www.learndatasci.com/glossary/tf-idf-term-frequency-inverse-document-frequency/

# import required module
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# assign documents
d1 = 'data science is one of the most important fields of science'
d2 = 'this is one of the best data science courses'
d3='data scientists analyze data'
D=[d1, d2, d3]

tr_idf_model  = TfidfVectorizer()
tf_idf_vector = tr_idf_model.fit_transform(D)

tf_idf_array = tf_idf_vector.toarray()
# print(tf_idf_array)

W = tr_idf_model.get_feature_names_out()
# print(W)

df_tf_idf = pd.DataFrame(tf_idf_array, columns = W)
print(df_tf_idf)
