import requests
import re
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit

links_seen=[]
links_todo = ["https://vnexpress.net/"]

domain= urlsplit(links_todo[0]).netloc
file_store="E:/Files_Crawl/"

def url_to_file_name(url):
    url = str(url).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', url) + ".html"

def download(url):
    print("Saving file,...")
    filename=os.path.join(file_store, url_to_file_name(url))    
    with open(filename, 'w',encoding='utf-8') as the_html:
            the_html.write(requests.get(url).text)
    
def visit(url):
    global links_todo
    
    links_seen.append(url)
    print("** Now visiting:", url)
    
    html = requests.get(url).text
    html_soup = BeautifulSoup(html, "html5lib")
    download(url)
    
    Count=0
    for link in html_soup.find_all("a"):
        link_url = link.get("href")  
        if link_url is None:
            continue
        
        full_url = urljoin(url, link_url)
        
        if urlsplit(full_url).netloc != domain:
            continue

        if urlsplit(full_url).query !="":
            continue
        
        if full_url in links_todo or full_url in links_seen:
            continue
        
        Count=Count+1
        links_todo.append(full_url)

    print(" + ",Count, "new link(s) found")
    print(" + ",len(links_seen), "link(s) seen/", len(links_todo), "link(s) need to do.")
    
    print("Enter to continues, ...")
    input()


while links_todo:
    url_to_visit = links_todo.pop()
    visit(url_to_visit)