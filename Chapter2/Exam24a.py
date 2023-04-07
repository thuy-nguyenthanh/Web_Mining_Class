from bs4 import BeautifulSoup

broken_html = '<ul><li>Coffee<li>Tea</li><li>Milk</li></ul>'
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()

print(fixed_html)