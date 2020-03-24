from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTagdata(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.h1
    except AttributeError as e:
        print(e)
        return None
    return title

print(getTagdata("http://www.pythonscraping.com/pages/page1.html"))

