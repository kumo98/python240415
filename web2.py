#web2.py

import requests

from bs4 import BeautifulSoup

url = 'https://www.daangn.com/fleamarket/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

f = open('daangn.txt','a+',encoding='utf-8')

posts = soup.find_all('div',attrs={'class':'card-desc'})

for post in posts:
    titleElem = post.find('h2',attrs={'class':'card-title'})
    title = titleElem.text.strip()
    priceElem = post.find('div',attrs={'class':'card-price'})
    price = priceElem.text.strip()
    addrElem = post.find('div',attrs={'class':'card-region-name'})
    addr = addrElem.text.strip()
    print(f"{title:<30}, {price:<30}, {addr:<30}")
    # f.write(f"{title:<50}, {price}, {addr}\n")

#파일 닫기
f.close()