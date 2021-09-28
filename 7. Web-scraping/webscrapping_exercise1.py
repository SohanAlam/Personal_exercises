import requests
import json
from bs4 import BeautifulSoup


page = requests.get("https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YVLktZrP1D8")
soup = BeautifulSoup(page.content, 'html.parser')
#print(page)


day_name = soup.find_all('p', class_='period-name')
#print(day_name)
date = soup.find_all('p', class_='text-right') #problem when i am trying to add date
#print(date)
short_description = soup.find_all('p', class_='panel-body')
#print(short_description)
temp1 = soup.find_all('p', class_='myforecast-current-lrg')
temp2 = (temp1 - 32) * 5/9
celsius = round(temp2,2)
print(celsius)


