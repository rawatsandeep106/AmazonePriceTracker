import requests
from bs4 import BeautifulSoup

overall_dict = {}
html = requests.get('https://www.worldometers.info/coronavirus/')
bs = BeautifulSoup(html.text,'html.parser')

for link in bs.find_all(class_='maincounter-number'):
    print(link.span.text)





