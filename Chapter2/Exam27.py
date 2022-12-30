import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit

file_store="E:/Files_Crawl/"

links_seen=[]
url_fileRSS="https://vnexpress.net/rss/the-thao.rss"
domain= urlsplit(url_fileRSS).netloc

def url_to_file_name(url):
    url = str(url).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', url) + ".html"

def download(url):
    print("Saving file,...")
    filename=os.path.join(file_store, url_to_file_name(url))    
    with open(filename, 'w',encoding='utf-8') as the_html:
            the_html.write(requests.get(url).text)
    
def visit(url):
    print("** Now visiting:", url)    
    html = requests.get(url).text
    html_soup = BeautifulSoup(html, "html.parser")
    download(url)


def getURL_from_fileRSS(url_fileRSS):
    xml = requests.get(url_fileRSS).text
    links=re.findall('<a href="(.*?)"', xml)
    
    links_todo=[]    
    for link_url in links:
        if link_url is None:
            continue      
        
        if urlsplit(link_url).netloc != domain:
            continue
        
        if link_url in links_todo:
            continue
        
        links_todo.append(link_url)

    return links_todo


links_todo = getURL_from_fileRSS(url_fileRSS)
while links_todo:
    url_to_visit = links_todo.pop()
    new_links = visit(url_to_visit)    