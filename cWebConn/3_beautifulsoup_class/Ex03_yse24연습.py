from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen('https://www.yes24.com/product/search?domain=all&query=python')

soup = BeautifulSoup(html, 'html.parser')

# [1]
# infos = soup.select('#yesSchList  div.itemUnit  a.gd_name')
# for info in infos:
#     print(info.text)
#
# print('총 {}권이 검색되었습니다.'.format(len(infos)))

# [2]
img_urls = soup.select('#yesSchList div.itemUnit img')
# print(img_urls)
for img_url in img_urls:
    # 이미지 링크 : data-original
    # 책제목 : alt
    book_name = img_url.attrs['alt'].strip().replace('/', '_')
    img_path = img_url.attrs['data-original']
    print(book_name, img_path)
    request.urlretrieve(img_path, 'imgs/' + book_name + '.jpg')
