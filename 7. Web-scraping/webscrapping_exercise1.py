import requests
import json
from bs4 import BeautifulSoup


page = requests.get("https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YVLktZrP1D8")
soup = BeautifulSoup(page.content, 'html.parser')
#print(page)


day_name = soup.find('div', class_='col-sm-2 forecast-label')
#print(day_name.text)
date = soup.find_all('p', class_='text-right') #problem when i am trying to add date
#print(date)
short_description = soup.find('div',id='detailed-forecast')
#print(short_description.text)
#temp1 = soup.find('p', class_='myforecast-current-lrg')
#print(temp1.get_text())

#temp2 = ((int(temp1) - 32) * 5/9)
#celsius = round(temp2,2)
#print(celsius)
results = soup.find(class_='contentArea')
dates = results.find('div', class_='panel-body', id='seven-day-forecast-body')
#print(dates.text)
day_forecast = soup.find('div', class_="panel-body",id = "seven-day-forecast-body")
print(day_forecast.text)



