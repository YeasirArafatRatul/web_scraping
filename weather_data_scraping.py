import requests
import pandas as pd
from bs4 import BeautifulSoup


page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.Xf-S30cvOUk')

soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast')

items = week.find_all(class_='tombstone-container')

data_dictionary = {}


# for item in items:
#     data_list = []
#     name = item.find(class_='period-name').get_text()
#     description = item.find(class_='short-desc').get_text()
#     temp = item.find(class_='temp').get_text()

#     data_list.append(description)
#     data_list.append(temp)

#     data_dictionary.__setitem__(name, data_list)

# print(data_dictionary)

'''
#output_of_above_procedure

{'Today': ['Mostly Cloudy', 'High: 66 °F'], 'Tonight': ['Rain', 'Low: 51 °F'], 'Monday': ['Showers', 'High: 58 °F'], 
'MondayNight': ['ChanceShowers', 'Low: 48 °F'], 'Tuesday': ['Partly Sunny', 'High: 59 °F'], 'TuesdayNight': ['Slight ChanceShowers', 'Low: 47 °F'], 
'ChristmasDay': ['Chance Rain', 'High: 59 °F'], 'WednesdayNight': ['Rain Likely', 'Low: 46 °F'], 'Thursday': ['Rain Likely', 'High: 60 °F']}
'''


period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [
    item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

# using_panda_for_tabular_represntation
weather_stuff = pd.DataFrame(
    {'Period': period_names,
     'Short Descriptions': short_descriptions,
     'Temperatures': temperatures
     }
)

print(weather_stuff)

# output_using_panda
'''
           Period    Short Descriptions Temperatures
0           Today         Mostly Cloudy  High: 66 °F
1         Tonight                  Rain   Low: 51 °F
2          Monday               Showers  High: 58 °F
3     MondayNight         ChanceShowers   Low: 48 °F
4         Tuesday          Partly Sunny  High: 59 °F
5    TuesdayNight  Slight ChanceShowers   Low: 47 °F
6    ChristmasDay           Chance Rain  High: 59 °F
7  WednesdayNight           Rain Likely   Low: 46 °F
8        Thursday           Rain Likely  High: 60 °F

'''

# converting_to_csv(Comma Separated Value)
weather_stuff.to_csv("weather.csv")

# a csv file will be genrated
