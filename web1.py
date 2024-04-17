#web1.py

from bs4 import BeautifulSoup

page = open('c:\\work\\Chap09_test.html','rt',encoding='utf-8').read()

soup = BeautifulSoup(page,'html.parser')

# print(soup.prettify())

# print(soup.find_all('p'))

# print(soup.find('p'))

# print(soup.find_all('p',class_='outer-text'))

# print( soup.find_all('p', attrs={'class':'outer-text'}) )

# print( soup.find_all('p', attrs={'id':'second'}) )

# print( soup.find_all(id='first') )

for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace('\n','')
    title = title.replace(' ','')
    print(title)