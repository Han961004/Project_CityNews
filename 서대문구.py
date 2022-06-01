import re
import requests
from bs4 import BeautifulSoup
import urllib


def crawl(url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    result = []
    
    div = soup.find("table", class_ = "boardList")                     
    title_list = div.select("tbody > tr")
    
    for obj in title_list[:3]:
        title = obj.find('td', class_ = 'aleft').find('a').text
        title = re.sub(r'[\r\n\t]','',str(title))  
        title = title[1:-1]                     # 시작 끝 공백 제거

        date = obj.select('td')[3]
        date = re.sub(r'[</td>\r\n\t ]','',str(date))

        result.append(['구청',title, date, 'https://www.sdm.go.kr/news/news/notice.do'])    # 카테고리 / 제목 / 년 월 구분 / 링크주소


    return result

url = "https://www.sdm.go.kr/news/news/notice.do"
r = crawl(url)

