import string

text="This is introduction to NLP. It is likely to be useful, to people, Machine learning is the new electrcity. There would be less hype around AI and more action going forward,python is the best tool! R is good langauage, I like this book, I want more books like this."

#Cach 2: Su dung thu vien string
for c in string.punctuation:
    text= text.replace(c,'')

text_pre=text   
print(text_pre)