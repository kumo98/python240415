import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_naver_blog(search_keyword, max_page=100):
    wb = Workbook()
    ws = wb.active
    ws.append(["블로그명", "블로그주소", "제목", "포스팅날짜"])

    for page in range(1, max_page + 1):
        # 검색어와 페이지 번호를 이용하여 블로그 검색 페이지에 접속
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 블로그 포스트 목록 가져오기
        post_list = soup.find_all('li', class_='sh_blog_top')
        
        # 페이지에 포스트가 없으면 크롤링 중단
        if not post_list:
            break
        
        # 블로그 포스트 정보 추출
        for post in post_list:
            # 블로그명
            blog_name = post.find('a', class_='sh_blog_title').text
            
            # 블로그 주소
            blog_url = post.find('a', class_='sh_blog_title')['href']
            
            # 제목
            title = post.find('a', class_='sh_blog_title')['title']
            
            # 포스팅 날짜
            post_date = post.find('span', class_='date').text
            
            # 결과를 엑셀 파일에 추가
            ws.append([blog_name, blog_url, title, post_date])

    # 엑셀 파일 저장
    wb.save("c:/work/result.xlsx")

# 사용자로부터 검색어 입력받기
search_keyword = input("검색어를 입력하세요: ")

# 크롤링 실행 (1페이지부터 100페이지까지)
crawl_naver_blog(search_keyword, max_page=100)
