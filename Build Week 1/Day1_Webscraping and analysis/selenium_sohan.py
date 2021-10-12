from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


main_url = "https://www.goodreads.com/list/show/50.The_Best_Epic_Fantasy_fiction_"
driver = ("chromedriver.exe")
driver = webdriver.Chrome(driver)
urls= []
driver.create_options()
driver.minimize_window()
driver.get(main_url)
sleep(1)


for i in range(1,38):
    if i ==2:
        sleep(3)
        x_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button/img')
        x_button.click()
    book_table = driver.find_element_by_xpath('//table[@class="tableList js-dataTooltip"]')
    books = book_table.find_elements_by_tag_name('tr')

    for book in books:
        info = book.find_elements_by_tag_name('td')[2]
        b_title = info.find_element_by_class_name('bookTitle')
        urls.append(b_title.get_attribute('href'))
    next_button = driver.find_element_by_xpath('//a[@class="next_page"]')
    try:
        next_button.click()
    except:
        print(print('it was last one'))
    
    sleep(2)

def scraper(url_path):
    titles = []
    avg_ratings = []
    authors = []
    num_ratings = []
    num_revs = []
    num_pages = []
    publ_years = []
    is_series = []
    genres = []
    awards = []
    places = []
    pub_years_1 = []
    ################ starting point ############################
    driver = webdriver.Chrome()
    book_urls = url_path
    counter =0
    pl_check = 0
    place = ''
    for url in book_urls:
        counter +=1
        if counter %25==0:
            print('{} books are scraped, 2 seconds of rest'.format(counter))
            if counter%100==0:
                sleep(3)
            sleep(2)
        driver.get(url)
        box = driver.find_element_by_id('metacol')
        ######## extracting info about title ##############
        title = box.find_element_by_id('bookTitle').text
        titles.append(title)
        ######## extracting info about average rating ##############
        author_box = box.find_element_by_id('bookAuthors')
        author = author_box.find_elements_by_tag_name('a')[0].text
        authors.append(author)
        ######## extracting info about average rating ##############
        rat_rev_box = box.find_element_by_id('bookMeta')
        avg_rating = rat_rev_box.find_elements_by_tag_name('span')[6].text
        avg_ratings.append(float(avg_rating))
        ######## extracting info about number of ratings ##############
        num_rating = rat_rev_box.find_elements_by_tag_name('a')[1].text.split()[0].replace(',','')
        num_ratings.append(int(num_rating))
        ######## extracting info about number of reviews ##############
        num_rev = rat_rev_box.find_elements_by_tag_name('a')[2].text.split()[0].replace(',','')
        num_revs.append(int(num_rev))
        ########## finds element containing pages, pub year
        details = box.find_element_by_id('details')
        ######## is it aprt of book series ################
        series = box.find_element_by_id('bookSeries')
        if len(series.text)>0:
            is_series.append(1)
        else:
            is_series.append(0)
        ######## extracting info about pages ##############
        page_check = 0
        try:
            pages = details.find_elements_by_tag_name('div')[0].text.split()
            for i in pages:
                if i.isnumeric() :
                    num_pages.append(int(i))
                    page_check=1
        except:
            pass
        if not page_check:
            num_pages.append(None)
        ####### extracting info about pub year ##############
        year_check = 0
        try:
            years_info = details.find_elements_by_tag_name('div')[1]
            pub_years = years_info.text.split()
            for year in pub_years:
                if len(year)==4 and year.isnumeric():
                    publ_years.append(int(year))
                    year_check = 1
        except:
            pass
        if not year_check:
            publ_years.append(None)
        ####### extracting info about pub year first ##############
        year_check_1 = 0
        try:
            pub_years_first = years_info.find_elements_by_class_name('greyText')[0].text.replace('(','').replace(')','').split()
            for yr in pub_years_first:
                if len(yr)==4 and yr.isnumeric():
                    pub_years_1.append(int(yr))
                    year_check_1 = 1
        except:
            pass
        if not year_check_1:
            pub_years_1.append(None)
        ######## extracting info about genre ##############
        c = 0
        try:
            genres_box = driver.find_element_by_xpath('//div[@class="stacked"]').find_element_by_xpath('.//div[@class="bigBoxContent containerWithHeaderContent"]').find_elements_by_class_name('elementList')[:3]
            genre_complete=''
            for genre in genres_box:
                genre_complete+=',{}'.format(genre.find_elements_by_tag_name('div')[0].text)
            genres.append(genre_complete[1:])
            c=1
            
        except:
            pass
        if not c:
            genres.append(None)
        ######## extracting info about awards ##############
        more_info_button = details.find_element_by_id('bookDataBoxShow')
        try:
            more_info_button.click()
        except:
            pass
        award_places = details.find_elements_by_tag_name('div')[2].find_elements_by_tag_name('div')[0]
        award_box = award_places.find_elements_by_class_name('clearFloats')
        settings = award_places.find_elements_by_class_name('infoBoxRowItem')
        for box in award_box:
            check = 0
            try:
                award = box.find_element_by_xpath('.//div[@itemprop="awards"]')
                awards.append(award.text)
                check = 1
            except:
                pass
        if not check:
            awards.append(None)
        ####### extracting info about places ##############
        for setting in settings:
            plcs = setting.find_elements_by_tag_name('a')
            for plc in plcs:
                linking = plc.get_attribute('href')
                if '/places/' in linking:
                    place += ',{}'.format(plc.text)
                    pl_check =1

        if not pl_check:
            places.append(None)
        else:
            places.append(place[1:])
            place=''
        pl_check = 0

    data = {
    "title":titles,
    "author":authors,
    "num_reviews":num_revs,
    "num_ratings":num_ratings,
    "avg_rating":avg_ratings,
    "num_pages":num_pages,
    "publish_year":publ_years,
    "first_published":pub_years_1,
    "series":is_series,
    "genres":genres,
    "awards":awards,
    "places":places,
    "url": url_path
    }

    return data
