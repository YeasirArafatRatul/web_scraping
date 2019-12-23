import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soupObj = BeautifulSoup(html, 'html.parser')
        title = soupObj.body.h1
    except AttributeError as e:
        return None
    return title


url = "http://www.pythonscraping.com/pages/page1.html"
title = getTitle(url)
if title == None:
    print("Title not found")
else:
    print(title)
