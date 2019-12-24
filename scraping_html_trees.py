import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

page = urlopen("http://www.pythonscraping.com/pages/page3.html")


soupObj = BeautifulSoup(page, 'html.parser')

title = soupObj.body.h1
# gifts = soupObj.find_all

gifts = soupObj.findAll(class_="gift")

# print(title.get_text())
# for gift in gifts:
#     print(gift.get_text())

expression = r'\$[0-9]*\,?[0-9]*?\.[0-9]+'

prices = re.findall(expression, str(gifts))
print(prices)
