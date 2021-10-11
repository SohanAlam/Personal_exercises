import requests
import json
from bs4 import BeautifulSoup


page = requests.get("https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_")
soup = BeautifulSoup(page.content, 'html.parser')

url=[]
title=[]
author=[]
reviews=[]
rating=[]

for i in range(1,3):
    page1 = requests.get("https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_?page={i}")
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    all=soup1.find_all('table',class_='tableList js-dataTooltip')

    for item in all():
        for link in item.find_all('a',class_='bookTitle',href=true):
            url.append(baseurl+link[href])
            

print(len(url))

