from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
[1]
http://www.pythonscraping.com/pages/warandpeace.html

녹색 글자만 추출하여 출력
'''
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# soup = BeautifulSoup(html, 'html.parser')
#
# green_texts = soup.select('span.green')
# # print(green_texts)
# for green in green_texts:
#     print(green.string)


'''
[2]
http://www.pythonscraping.com/pages/page3.html

아이템과 가격을 추출
'''
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# soup = BeautifulSoup(html, 'html.parser')
#
# rows = soup.select('table#giftList tr.gift')
# for row in rows:
#     item_title = row.select_one('td:nth-child(1)').text.strip()
#     cost = row.select_one('td:nth-child(3)').text.strip()
#     print('아이템 :', item_title)
#     print('가격 :', cost)
#     print('=' * 50)

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# soup = BeautifulSoup(html, 'html.parser')
# info = soup.select('#giftList tr.gift td:nth-child(3)')
# info2 = soup.select('#giftList tr.gift td:nth-child(1)')
# for x, y in zip(info, info2):
#     print(y.text.strip(), ': ', x.text.strip())

'''
[3]
https://wikidocs.net/

 1) 책 제목과 저자만 추출
 2) 이미지 다운
'''
# html = urlopen('https://wikidocs.net/').read()
# soup = BeautifulSoup(html, 'html.parser')
# medias = soup.select('div#books div.media')
# for media in medias:
#     book_name = media.select_one('a.book-subject').string
#     author = media.select_one('a.menu_link').string
#     print('책 제목 : {} - 저자 : {}'.format(book_name, author))
