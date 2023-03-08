import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

text = "I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds."

#Tokenization (step before stemming)
sentences = nltk.sent_tokenize(text)
print(sentences)
               
# Lemmatization
lemmatizer = WordNetLemmatizer()
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print(sentences)    