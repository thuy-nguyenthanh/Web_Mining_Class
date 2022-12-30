import requests
from bs4 import BeautifulSoup

url="https://phongtro123.com/tinh-thanh/da-nang"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

TieuDe = soup.find_all("h3",class_="post-title")
DonGia = soup.find_all("span",class_="post-price")
DienTich = soup.find_all("span",class_="post-acreage")
DiaChi = soup.find_all("span",class_="post-location")
NgayDang = soup.find_all("time",class_="post-time")

for i in range(len(TieuDe)):
    print(TieuDe[i].text)
    print(" - " + DonGia[i].text)
    print(" - " + DienTich[i].text)
    print(" - " + DiaChi[i].text)
    print(" - " + NgayDang[i].text)
