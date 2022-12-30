import re
string = 'Lionel Messi was born on 24 June 1987 in Rosario, Santa Fe.In the 2022 FIFA World Cup final on 18 December, Messi made his record 26th World Cup finals appearance at Lusail Stadium'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)