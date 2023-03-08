#Install textblob library
#pip install textblob

#import libraries and use 'correct' function
from textblob import TextBlob
text="GFG is a good compny and alays value ttheir employees."

text_pre=TextBlob(text).correct()
print(text_pre)