from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_'
driver = webdriver.Chrome()
e_info = 'soghuniy@gmail.com'
pass_info = 'soghuniy_96'

############### scraping info about books #####################################
titles = []
urls = []
authors = []
avg_ratings = []
num_ratings = []
driver.get(url)

for i in range(1,3):
    if i ==2:
        sleep(3)
        x_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button/img')
        x_button.click()
    book_table = driver.find_element_by_xpath('//table[@class="tableList js-dataTooltip"]')
    books = book_table.find_elements_by_tag_name('tr')

    for book in books:
        info = book.find_elements_by_tag_name('td')[2]
        b_title = info.find_element_by_class_name('bookTitle')
        titles.append(b_title.text)
        urls.append(b_title.get_attribute('href'))
        author = info.find_elements_by_tag_name('span')[2].find_element_by_tag_name('span')
        authors.append(author.text)
        rating_text = info.find_elements_by_class_name('minirating')[0].text
        # this text consists of -> avg rating + 'avg rating' +'-' + num rating + 'ratings', we should split and choose only info we need
        avg_ratings.append(rating_text.split()[0])
        num_ratings.append(rating_text.split()[4].replace(',',''))
    next_button = driver.find_element_by_xpath('//a[@class="next_page"]')
    try:
        next_button.click()
    except:
        print(print('it was last one'))

    sleep(2)

print(titles)
print(urls)
print(authors)
print(avg_ratings)
print(num_ratings)
# driver.quit()