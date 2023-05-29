from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs

def findMovieView(input):
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get("https://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do")
    driver.implicitly_wait(time_to_wait=5)

    search_box = driver.find_element(By.XPATH,'//*[@id="searchForm"]/div[1]/div[1]/div/input')
    search_box.send_keys(input)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

    element = driver.find_element(By.XPATH,'//*[@id="content"]/div[4]/table/tbody/tr[1]/td[1]/span/a')
    element.click()

    element2 = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/ul/li[2]/a')
    element2.click()

    time.sleep(10)
    soup = bs(driver.page_source,'html.parser')
    value = soup.select('div.item_tab.statistics > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(4)')

    #ui-id-1 > div > div.item_tab.statistics > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(4)
    movieView = value[0].string
    tmp = movieView.split(' ')
    movieView = tmp[0]
    tmp = movieView.split(',')
    movieView = ''
    for i in range(len(tmp)):
        if tmp[i]!=',':
            movieView+=tmp[i]

    movieView = int(movieView)

    return movieView
    # print(soup.body.div[3].div[2].div.div[2].div[1].table.tbody.tr[2].td[4].string)

    # element3 = driver.find_element(By.XPATH,'//*[@id="ui-id-1"]/div/div[2]/div[2]/table/tbody/tr[2]/td[4]')
    # val = element3.get_attribute('')
    # print(val)

# movieName = input()
# movieView = findMovieView(movieName)
# print(movieView)

