import math
import pandas as pd

#Create Dictionary
def create_dict(doc_list):
    W={}
    for d in doc_list:
        bow = d.split(" ")  # Tokenization
        W = set(W).union(set(bow))

    return W

#Count the word in bads
def WCount(d, W):
    wordDict=dict.fromkeys(W, 0)
    for word in d.split():
        wordDict[word]+=1
    return wordDict

#Calculate TF
def compute_TF(W, d):
    tf_dict = {}
    
    bow_count = len(d.split())
    for word, count in W.items():
        tf_dict[word] = round(count/float(bow_count),3)
    
    return tf_dict    

#Calculate IDF   
def compute_IDF(doc_list):
    idf_dict = {}
    N = len(doc_list)
    
    #Count number of documents that contain this word
    idf_dict = dict.fromkeys(doc_list[0].keys(), 0)
    # print(idf_dict)

    for doc in doc_list:
        for word, count in doc.items():
            if count > 0:
                idf_dict[word] += 1
    # print(sorted(idf_dict.items()))

    for word, count in idf_dict.items():
        idf_dict[word] = round(math.log10(N/float(count)),3)

    return idf_dict

# Compute TF-IDF
def compute_TFIDF(tf_bow, idfs):
    tfidf = {}
    for word, val in tf_bow.items():
        tfidf[word] = round(val*idfs[word],3)
    return tfidf

#===================================================
#===================================================

d1 = "the quick brown fox jumps over the lazy dog and"
d2 = "never jump over the lazy dog quickly"
D=[d1,d2]

# Step 1
W= create_dict(D)
# print(W)

# Step 2.1
W1= WCount(d1,W)
W2= WCount(d2,W)
# print(sorted(W1.items()))
# print(sorted(W2.items()))

# Step 2.2 + 2.3: Compute TF
tf_d1 = compute_TF(W1, d1)
tf_d2 = compute_TF(W2, d2)
# print(sorted(tf_d1.items()))
# print(sorted(tf_d2.items()))

# Step 3: Compute IDF
idfs = compute_IDF([W1, W2])
# print(sorted(idfs.items()))

# Step 4: Compute TF-IDF
tfidf_d1 = compute_TFIDF(tf_d1, idfs)
tfidf_d2 = compute_TFIDF(tf_d2, idfs)
# print(tfidf_d1)
# print(tfidf_d2)

# Vector TF-IDF
df = pd.DataFrame([tfidf_d1, tfidf_d2])
print(df)