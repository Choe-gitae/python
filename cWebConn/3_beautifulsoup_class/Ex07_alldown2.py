"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

'''
    함수명 : download_file
    인자  : url
    리턴값 : 저장경로 or None
    역할  : 인자 url 페이지 내용을 파일로 만든다
'''
def download_file(url):
    p = parse.urlparse(url)
    # print(p)
    save_path = './' + p.netloc + p.path
    # print(save_path)
    if re.search('/$', save_path):
        save_path += 'index.html'
        # print(save_path)

    if os.path.exists(save_path):
        return save_path

    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    try:
        request.urlretrieve(url, save_path)
        print('download -', url)
        time.sleep(2.0)
    except Exception:
        print('fail download :', url)
        return None


if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)
