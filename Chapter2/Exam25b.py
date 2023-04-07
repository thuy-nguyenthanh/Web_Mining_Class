import requests
import re
import os

url="https://phongtro123.com/tinh-thanh/da-nang"
html = requests.get(url).text

def get_LinksbyRegEx(url_visit):
    global Links_ToDo
    print("** Now visiting:",url_visit)
    
    Links_seen.append(url_visit)    
    html = requests.get(url_visit).text
    NextLinks=re.findall('<a class="page-link" href="(.*?)"', html)

    for Link in NextLinks:
        if  Link not in Links_ToDo and Link not in Links_seen:
            Links_ToDo.append(Link)
        
    if Links_ToDo:
        get_LinksbyRegEx(Links_ToDo.pop())
    else:
        return

#Cách 1: Lấy link tự động từ Biểu thức chính quy - Sử dụng thuật toán đệ quy
Links_ToDo=[url]
Links_seen=[]
get_LinksbyRegEx(Links_ToDo.pop())
print(len(Links_seen), "links found!")


#Cách 2: Dựa trên quy tắc cấu trúc url để tạo link
Links_ToDo=[url]
for i in range(2,49):
    Link="https://phongtro123.com/tinh-thanh/da-nang?page=" + str(i)
    Links_ToDo += [Link]

print(Links_ToDo)    
