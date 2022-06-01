
from unittest import result
from bs4 import BeautifulSoup
import urllib
import requests
import re 

def crawl(url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    result = []
    div = soup.find("div", class_ = "lst_wrap")
    movie_list = div.select("ul > li")
    rank = 0
    
    for movie in movie_list[:10]:
        title = movie.find('dt', class_ = 'tit').find('a').text
        genre = movie.find('span', class_ = 'link_txt').find('a').text
        ddList = movie.find_all('dd')
        cast = re.sub(r'[\r\n\t]','',str(ddList[5].text)) 
        rank = rank + 1        

        result.append([rank, title, genre, cast])
    return result

url = "https://movie.naver.com/movie/running/premovie.naver?order=interestRate"             #개봉예정
r = crawl(url)
print(r)


