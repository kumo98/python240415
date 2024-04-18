# demoForm.py
# 화면 + 로직

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup

# 디자인한 파일 로딩
form_class = uic.loadUiType('DemoForm2.ui')[0]

# 윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        self.label.setText('첫번째 버튼 클릭')

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
            f.write(f"{title:<30}, {price:<30}, {addr:<30}\n")

        #파일 닫기
        f.close()

        self.label.setText('당근마켓크롤링완료')
    def secondClick(self):
        self.label.setText('두번째 버튼 클릭')
    def thirdClick(self):
        self.label.setText('세번째 버튼 클릭')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()