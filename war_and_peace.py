import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


page = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

soupObj = BeautifulSoup(page, "html.parser")

nameList = soupObj.find_all("span", {"class": "green"})

# list_comprehension
names = [name.get_text() for name in nameList]
print(names)
