import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.Xf-S30cvOUk')

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast')

items = week.find_all(class_='tombstone-container')

data_dictionary = {}


for item in items:
    data_list = []
    name = item.find(class_='period-name').get_text()
    description = item.find(class_='short-desc').get_text()
    temp = item.find(class_='temp').get_text()

    data_list.append(description)
    data_list.append(temp)

    data_dictionary.__setitem__(name, data_list)

print(data_dictionary)
