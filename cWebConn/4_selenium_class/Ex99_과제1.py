from selenium import webdriver
from bs4 import BeautifulSoup
import time
import cx_Oracle as oracle
import csv

driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('http://www.ejadam.co.kr/bbs/board.php?bo_table=store')
time.sleep(3)
driver.find_element_by_class_name('pg_end').click()
time.sleep(3)
last_page = int(driver.find_element_by_class_name('pg_current').text)
# print(last_page)

store_info = []
for page_no in range(1, last_page+1):
    driver.get('http://www.ejadam.co.kr/bbs/board.php?bo_table=store&page={}'.format(page_no))
    time.sleep(3)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    store_name = soup.select('table > tbody > tr > td:nth-child(1) > a')
    store_tel = soup.select('table > tbody > tr > td:nth-child(2)')
    store_addr = soup.select('table > tbody > tr > td:nth-child(3)')

    for name, tel, addr in zip(store_name, store_tel, store_addr):
        # print(name)
        if name.text.find('오픈 예정') == -1:
            store_info.append([name.text.strip(), tel.text.strip().replace(' ', ''), addr.text.strip()])

# print(store_info)
# print(len(store_info))

with open('./jadam/store_info.csv', 'wt', newline='', encoding='utf-8-sig') as file:
    csvout = csv.writer(file)
    csvout.writerows(store_info)

create_table_sql = '''
CREATE TABLE JADAM(
	STORE_NAME		VARCHAR2(50),
	STORE_TEL		VARCHAR2(20),
	STORE_ADDR		VARCHAR2(100),
	LONGITUDE		NUMBER,
	LATITUDE		NUMBER,
	CONSTRAINT PK_JADAM_NAME PRIMARY KEY (STORE_NAME)
)
'''
insert_sql = '''
INSERT INTO JADAM (STORE_NAME, STORE_TEL, STORE_ADDR)
VALUES (:0, :1, :2)
'''
conn = oracle.connect('choe/1234@localhost:1521/xe')
# print(conn.version)
cursor = conn.cursor()

try:
    cursor.execute(create_table_sql)
except:
    print('테이블이 이미 존재합니다.')

for info in store_info:
    # print(info)
    cursor.execute(insert_sql, info)

conn.commit()
cursor.close()
conn.close()
