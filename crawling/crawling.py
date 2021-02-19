from urllib.request import urlopen
from urllib.parse   import quote_plus
from bs4            import BeautifulSoup
from selenium       import webdriver

import time

#baseUrl = "https://www.pexels.com/ko-kr/search/"
#plusUrl = input("검색어를 입력하세요 ")
#url = baseUrl + quote_plus(plusUrl)

url = "https://www.pexels.com/ko-kr/search/hotel%20room/"
driver = webdriver.Chrome("./chromedriver")
driver.get(url)

time.sleep(3)

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

#while True:
#    # Scroll down to bottom
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#    # Wait to load page
#    time.sleep(3)
#
#    # Calculate new scroll height and compare with last scroll height
#    new_height = driver.execute_script("return document.body.scrollHeight")
#    if new_height == last_height:
#        break
#    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html)

pexels = soup.select(".hide-featured-badge.hide-favorite-badge")

for i in pexels:
    imgUrl = i.select_one(".js-photo-link.photo-item__link").img["src"]
    print(imgUrl)

driver.close()
