import re
import requests
from bs4 import BeautifulSoup
import urllib


def crawl(url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    result = []
    
    div = soup.find("div", class_ = "news-lst")                     
    title_list = div.select("div")

    for obj in title_list[:3]:
        title = obj.find('em', class_ = 'subject').text
        title = title[8:]

        date = obj.find('em', class_ = "date").text
        date = re.sub(r'-', '.', str(date))
        date = date[:10]
        
        link = obj.find('a')['href']

        result.append(['시청',title, date, link])    # 카테고리 / 제목 / 년 월 구분 / 링크주소


    return result

url = "https://www.seoul.go.kr/realmnews/in/list.do"
r = crawl(url)
