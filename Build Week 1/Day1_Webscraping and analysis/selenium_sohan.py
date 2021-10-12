from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


page = "https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_"
my_driver = ("chromedriver.exe")
driver = webdriver.Chrome(my_driver)
driver.create_options()
driver.minimize_window()
driver.get(page)
sleep(1)
all = []
title = driver.find_elements_by_xpath('//div[@id="all_votes"]/table/tbody/tr')
for i in title:
    print(i.text)
    all.append(i)
    print(all)

