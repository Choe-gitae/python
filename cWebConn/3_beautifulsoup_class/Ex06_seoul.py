"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""

from urllib import request as req
from bs4 import BeautifulSoup

url = 'https://www.seoul.go.kr/seoul/autonomy.do'
site = req.urlopen(url)
html = site.read()

soup = BeautifulSoup(html, "html.parser")
lis = soup.select('div.call-list li.tabcont')

# 아래 리스트에 각 구청의 상세 정보를 저장하고 출력하기
구청이름=[]
구청주소=[]
구청전화번호=[]
구청홈페이지=[]

for li in lis:
    구청이름.append(li.select_one('strong').string)
    구청주소.append(li.select_one('li:nth-child(1)').string)
    구청전화번호.append(li.select_one('li:nth-child(2)').string)
    구청홈페이지.append(li.select_one('li:nth-child(3) > a').string)

# print(구청이름)
# print(구청주소)
# print(구청전화번호)
# print(구청홈페이지)

'''
1. 추출한 결과를 위 리스트에 저장한다.

2. 리스트 출력 결과 예시- 아래처럼 각 구청의 정보를 추출
      ex)
      구청이름 : 강동구
      구청주소 : (우) 04558 / 서울시 중구 창경궁로 17 (예관동)
      구청전화번호 : TEL. 02-3396-4114
      구청홈페이지 : http://www.junggu.seoul.kr
'''

for data in zip(구청이름, 구청주소, 구청전화번호, 구청홈페이지):
    print('구청이름 :', data[0])
    print('구청주소 :', data[1])
    print('구청전화번호 :', data[2])
    print('구청홈페이지 :', data[3])
    print('=' * 60)


구청이름 = [temp.text for temp in soup.select('.tabcont strong')]
구청주소 = [temp.text for temp in soup.select('.tabcont li:first-child')]
구청전화번호 = [temp.text for temp in soup.select('.tabcont li:nth-of-type(2)')]
구청홈페이지 = [temp.text for temp in soup.select('.tabcont li:nth-of-type(3)')]

for a, b, c, d in zip(구청이름, 구청주소, 구청전화번호, 구청홈페이지):
    print('구청이름 : {}\n구청주소 : {}\n구청전화번호 : {}\n구청홈페이지 : {}'.format(a, b, c, d))

