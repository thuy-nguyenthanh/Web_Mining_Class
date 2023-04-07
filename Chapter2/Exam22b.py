import re 
html = '<ul><li>Coffee</li><li>Tea</li><li>Milk</li></ul>' 
L = re.findall("<li>(.*?)</li>",html)

print(L)
