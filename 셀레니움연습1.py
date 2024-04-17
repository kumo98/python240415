from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#크롬 드라이버 실행
driver = webdriver.Chrome()

#URL주소
driver.get('https://www.google.co.kr')

#3초 대기
time.sleep(3)

# searchBox = driver.find_element(By.CLASS_NAME,'gLFyf')
searchBox = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
# <textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="Search" value="" jsaction="paste:puy29d;" aria-label="Search" aria-autocomplete="both" aria-expanded="false" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwj1l-yOzciFAxXUaPUHHV3wCVcQ39UDCAw"></textarea>

searchBox.send_keys('어린이날')
searchBox.send_keys(Keys.ENTER)

time.sleep(10)