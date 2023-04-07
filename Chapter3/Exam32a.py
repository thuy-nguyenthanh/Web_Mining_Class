import re

text="This is introduction to NLP. It is likely to be useful, to people, Machine learning is the new electrcity. There would be less hype around AI and more action going forward,python is the best tool! R is good langauage, I like this book, I want more books like this."

#Cach 1: Su dung thu vien re
text_pre=re.sub(r'[^\w\s]','',text)
print(text_pre)