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
my_driver = ("C:\practice_september\Personalexercises_september\Build Week 1\Day1_Webscraping and analysis\chromedriver.exe")


driver = webdriver.Chrome(my_driver)
driver.create_options()
driver.minimize_window()
driver.get(page)
sleep(3)

url_

table= driver.find_elements_by_xpath('//*[@id="all_votes"]/table')
all_elements = table.find
print(title)


