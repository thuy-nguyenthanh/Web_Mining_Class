#install and import libraries
#pip install nltk
import nltk

#Download nltk libraries
#nltk.download()
from nltk.corpus import stopwords

text="This is introduction to NLP. It is likely to be useful, to people, Machine learning is the new electrcity. There would be less hype around AI and more action going forward,python is the best tool! R is good langauage, I like this book, I want more books like this."

#remove stop words
stop = stopwords.words('english')
text_pre = " ".join(text for text in text.split() if text not in stop)

print(text_pre)