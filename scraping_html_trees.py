import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

page = urlopen("http://www.pythonscraping.com/pages/page3.html")


soupObj = BeautifulSoup(page, 'html.parser')
