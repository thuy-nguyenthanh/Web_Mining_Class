import requests
url = 'https://vnexpress.net/arsenal-sap-dung-tuong-wenger-4554241.html'
content = requests.get(url)

print(content.text)
