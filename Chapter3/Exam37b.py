#install autocorrect library
# pip install autocorrect
from autocorrect import spell
text="GFG is a good compny and alays value ttheir employees."

text_pre=spell(text)
print(text_pre)