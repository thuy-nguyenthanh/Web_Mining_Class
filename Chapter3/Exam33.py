#Installing emot library
#pip install emot
from emot.emo_unicode import UNICODE_EMOJI # For emojis
from emot.emo_unicode import EMOTICONS_EMO # For EMOTICONS
 
# Function for converting emojis into word
def converting_emojis(text):
    for x in EMOTICONS_EMO:
        text = text.replace(x, "_".join(EMOTICONS_EMO[x].replace(",","").replace(":","").split()))
        
    for x in UNICODE_EMOJI:
        text = text.replace(x, "_".join(UNICODE_EMOJI[x].replace(",","").replace(":","").split()))
            
    return text

text = "What are you saying 😂. I am the boss :), and why are you so 😒"
text_pre=converting_emojis(text)
print(text_pre)
