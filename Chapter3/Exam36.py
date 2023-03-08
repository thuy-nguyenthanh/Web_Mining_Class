import re
lookup_dict = {'nlp':'natural language processing', 'ur':'your', "wbu" : "what about you"}

def text_std(input_text):
    words = input_text.split()
    # Get Abbreviations Words
    text_pre=""
    for word in words:
        w=word
        w = re.sub(r'[^\w\s]','',w) #Removing Punctuation
        if w.lower() in lookup_dict:
            word=lookup_dict[w]
        text_pre=text_pre + " " + word        
    return text_pre

text_pre=text_std("I like nlp it's ur choice.")
print(text_pre)