import requests
import re
import os
from urllib.parse import urlsplit

file_store="E:/Files_Crawl/"

url_fileRSS="https://vnexpress.net/rss/the-thao.rss"
domain= urlsplit(url_fileRSS).netloc

def url_to_file_name(url):
    url = str(url).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', url) + ".html"

def download(url):
    print("Saving file,...")
    content=requests.get(url).text    
    filename=os.path.join(file_store, url_to_file_name(url))    
    
    with open(filename, 'w',encoding='utf-8') as f:
            f.write(content)
    
def visit(url):
    print("** Now visiting:", url)    
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