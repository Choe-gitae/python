"""
    기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
        - 데이타 가져오기     ` requests 모듈
                             ` urllib.request 모듈의 urlopen() 이용
        - 데이타 추출    BeautifulSoup 이용
"""

from bs4 import BeautifulSoup
from urllib import request as req


# 1. 데이타 가져오기
#  http://www.kma.go.kr > [생활과산업] > [서비스] > [인터넷] > RSS
rssUrl = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
res = req.urlopen(rssUrl)
# print(res)  # [결과] http.client.HTTPResponse object

# 2. 필요 데이타 추출하기
soup = BeautifulSoup(res, 'html.parser')
# print(soup) # 파싱 결과확인
# print('-'*100)

# 제목 / 도시 / 시간대별 날씨상태등 추출하여 출력
title = soup.select_one('title').string
locations = soup.select('location')
print(title)
for location in locations:
    city = location.select_one('city').string
    print(city)
    datas = location.select('data')
    for data in datas:
        print(data.select_one('tmEf').string)
        print(data.select_one('wf').string)
    print('=' * 50)
