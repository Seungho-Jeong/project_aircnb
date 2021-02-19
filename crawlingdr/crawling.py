from urllib.request import urlopen
from urllib.parse   import quote_plus
from bs4            import BeautifulSoup
from selenium       import webdriver

import time


driver = webdriver.Chrome("./chromedriver")
url = "https://www.pexels.com/ko-kr/search/"
driver.get(url)

time.sleep(2)
search_box = driver.find_element_by_name("s")
search_box.send_keys("residence")
driver.find_element_by_xpath('//*[@id="search-action"]').click()
time.sleep(2)
#    html = driver.page_source
#    soup = BeautifulSoup(html, "html.parser")
#    a = soup.select('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
#    a = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[8]/div/div[1]/span[3]/span[3]')
a = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[5]/div[1]/div[1]/div[1]/article/a[1]/img').get_attribute("src")
print(a)
driver.close()
