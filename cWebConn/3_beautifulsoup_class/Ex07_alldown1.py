"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse, request

'''
    함수명 : enum_links
    인자  : html object, base url 
    리턴값 : url
    역할  : 페이지 내 <a>태그의 href 값을 parse.urljoin 을 사용하여 url로 변환 후 리스트에 담아 리턴
'''
def enum_links(html,base):
    #-------------------------------------
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a')
    result = []
    # print(links)
    for a_tag in links:
        href = a_tag.attrs['href']
        # print(href)
        url = parse.urljoin(base, href)
        # print(url)
        result.append(url)

    return result


if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)
