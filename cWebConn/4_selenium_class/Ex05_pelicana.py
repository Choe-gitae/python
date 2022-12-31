from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

'''
# [연습]
driver.get('https://pelicana.co.kr/store/stroe_search.html')
html = driver.page_source
# print(html)

time.sleep(3)

soup = BeautifulSoup(html, 'html.parser')
shop_name = soup.select('table > tbody > tr > td:nth-child(1)')
shop_tel = soup.select('table > tbody > tr > td:nth-child(3)')

pelicana_shops = {shop_name.text.strip(): shop_tel.text.strip() for shop_name, shop_tel in zip(shop_name, shop_tel)}
# print(pelicana_shops)
'''

pelicana_shops = {}
for page_no in range(1, 11):
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page={}&branch_name=&gu=&si='.format(page_no))
    time.sleep(3)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    shop_name = soup.select('table > tbody > tr > td:nth-child(1)')
    shop_tel = soup.select('table > tbody > tr > td:nth-child(3)')

    for shop_name, shop_tel in zip(shop_name, shop_tel):
        pelicana_shops[shop_name.text.strip()] = shop_tel.text.strip()

print(pelicana_shops)
print(len(pelicana_shops))
