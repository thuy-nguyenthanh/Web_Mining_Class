import requests
import re
import os

url="https://phongtro123.com/tinh-thanh/da-nang"
html = requests.get(url).text


TieuDe=re.findall('<h3 class="post-title"><a.*?">(.*?)</a></h3>', html)
DonGia=re.findall('<span class="post-price">(.*?)</span>', html)
DienTich=re.findall('<span class="post-acreage">(.*?)</span>', html)
DiaChi=re.findall('<span class="post-location"><a.*?">(.*?)</a></span>', html)
NgayDang=re.findall('<time class="post-time" title=.*?">(.*?)</time>', html)

str=""
for i in range(len(TieuDe)):
    str+=TieuDe[i] + "\n"
    str+="- " + DonGia[i] + "\n"
    str+="- " + DienTich[i] + "\n"
    str+="- " + DiaChi[i] + "\n"
    str+="- " + NgayDang[i] + "\n"
    
    
filename=os.path.join("E:/Files_Crawl", "PhongTro123.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)