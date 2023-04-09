from gensim.models import Word2Vec

# Tạo dữ liệu mẫu
doc_1='Data is the oil of the digital economy'
doc_2='Data is a new oil'
docs=[doc_1,doc_2]

sentences=[]
for doc in docs:
    sentences.append([w for w in doc.lower().split()])

# Tạo mô hình CBOW
# Tham số sg=0 : CBOW, sg=1 : Skip-Ngram
model = Word2Vec(sentences, min_count=1, sg=0)

# Biểu diễn câu văn bản dưới dạng vector đặc trưng CBOW
vector_1 = model.wv[doc_1.lower().split()]
print("Vector đặc trưng của câu 1: ", vector_1)

vector_2 = model.wv[doc_2.lower().split()]
print("Vector đặc trưng của câu 2: ", vector_2)