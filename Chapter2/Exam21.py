import requests
url = 'https://vnexpress.net/rss/khoa-hoc.rss'
r = requests.get(url)

print(r.text)
