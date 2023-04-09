import nltk
import re
import os

nltk.download('stopwords')
nltk.download('punkt')


from nltk.probability import FreqDist
from nltk.corpus import stopwords


#Read file text
path=os.path.dirname(__file__)
f = open(path+r"\data\textdata.txt", "r", encoding="utf-8")
text=f.read()

#################################
######## Text Processing ########
#################################
text_pre=text.replace("\n","")  # Remove the newline command
text_pre=text.lower() # Convert text to lowercase
text_pre=re.sub(r'[^\w\s]','',text_pre) # Remove punctuation
text_pre = re.sub("\d+", " ", text_pre) # Remove number
text_pre = re.sub(r"[!@#$[]()]'", "", text_pre) # Remove character: !@#$[]()
stop = stopwords.words('english')   # Remove StopWords
text_pre = " ".join(text_pre for text_pre in text_pre.split() if text_pre not in stop)
text_pre=nltk.word_tokenize(text_pre) # Tokenizing


#################################
##### Exploring Text Data #######
#################################
#print("List of Datasets:",text_pre)
print("Number of words: ",len(text_pre))

# Compute the frequency of all words
frequency_dist = FreqDist(word.lower() for word in text_pre)

## show only th top 50 results
print(frequency_dist.most_common(50))


## Consider words with length greater than 3 and plot
large_words = dict([(k,v) for k,v in frequency_dist.items() if len(k)>3])
frequency_dist = nltk.FreqDist(large_words)
frequency_dist.plot(50,cumulative=False)


## Build a word cloud
# install library
# pip install wordcloud

from wordcloud import WordCloud
wcloud = WordCloud().generate_from_frequencies(frequency_dist)
#plotting the wordcloud
import matplotlib.pyplot as plt
plt.imshow(wcloud, interpolation="bilinear")
plt.axis("off")
plt.show()