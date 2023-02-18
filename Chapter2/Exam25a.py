import requests
import os
from bs4 import BeautifulSoup

url="https://phongtro123.com/tinh-thanh/da-nang"
html = requests.get(url).text
#Tối ưu hóa code HTML bằng thư viện html5lib 
soup = BeautifulSoup(html, 'html5lib')

#Sử dụng thư viện BeautifulSoup để bóc tách dữ liệu
TieuDe = soup.find_all("h3",class_="post-title")
DonGia = soup.find_all("span",class_="post-price")
DienTich = soup.find_all("span",class_="post-acreage")
DiaChi = soup.find_all("span",class_="post-location")
NgayDang = soup.find_all("time",class_="post-time")

str=""
for i in range(len(TieuDe)):
    str+=TieuDe[i].text + "\n"
    str+="- " + DonGia[i].text + "\n"    
    str+="- " + DienTich[i].text + "\n"
    str+="- " + DiaChi[i].text + "\n"
    str+="- " + NgayDang[i].text + "\n"
print(str)

#Ghi nội dung vào file
filename=os.path.join("E:/Files_Crawl", "PhongTro123.txt")    
with open(filename, 'w',encoding='utf-8') as f:
    f.write(str)