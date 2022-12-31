'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from urllib import request as req
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

# 교보문고 > '파이썬' 검색 > 국내도서
driver = webdriver.Chrome('D:/devTools/chromedriver')
driver.implicitly_wait(3)
driver.get("https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total")
html = driver.page_source
# html = urlopen("https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total")
soup = BeautifulSoup(html, 'html.parser')
prod_item = soup.select('ul.prod_list  li.prod_item')

book_name_list = []
for prod_info in prod_item:
    if prod_info.select_one('a.prod_info > span[id*=cmdtName_]') is not None:
        # img_tag = prod_info.select_one('img')
        # img_path = img_tag.attrs['src']
        book_name = [prod_info.select_one('a.prod_info > span[id*=cmdtName_]').string]
        book_name_list.append(book_name)
        # req.urlretrieve(img_path, 'imgs/{}.jpg'.format(book_name[0]))

# print(book_name)

with open('csv/books.csv', 'xt', newline='', encoding='utf-8-sig') as file:
    csv_out = csv.writer(file)
    csv_out.writerows(book_name)
