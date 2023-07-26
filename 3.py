import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://www.avito.ru/ufa/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1')
html = BS(r.content, 'html.parser')

for el in html.select('items > .items-kAJAg'):
    title = el.select('.iva > a')
    print(title[0].text)
