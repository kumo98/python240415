#Chap09_클리앙중고장터검색.py
# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

f = open('today.txt','wt',encoding='utf-8')

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,4):
        #오늘의 유머 주소 
        url ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(url)
        url = urllib.request.Request(url, headers=hdr)
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
# <td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=474652&amp;s_no=474652&amp;page=2" 
# target="_top">프랑스 아내를 위해 파스타를 만드는 남편</a><span class="list_memo_count_span"> [13]
        for item in list:
            try:
                title = item.find('a').text.strip()
                #키워드 검색
                if re.search('한국',title):
                    print(title)
                    # f.write(f'{title}\n')
            except:
                 pass

f.close()