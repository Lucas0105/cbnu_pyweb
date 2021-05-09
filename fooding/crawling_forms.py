import datetime
import time
import re

######### 함수 #########
# 함수 작성
def insta_searching(word) : 
    url = 'https://www.instagram.com/explore/tags/' + word
    return url

def select_first(driver):
    first = driver.find_element_by_css_selector('div._9AhH0') # 요소 찾기
    first.click()
    time.sleep(3) #로딩 3초

#본문 내용, 작성 일시, 위치 정보 및 해시태그(#) 추출
def get_content(driver):
    # 1. 현재 페이지의 HTML 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # 2. 본문 내용 가져오기
    try: # 여러 태그 중 첫번째([0]) 태그를 선택
        content = soup.select('div.C4VMK > span')[0].text
        # C4VMK아래에 있는 span 태그 모두 선택
    except:
        content = ' '
    # 3. 본문 내용에서 해시태그 가져오기(정규표현식 활용)
    tags = re.findall(r'#[^\s#,\\]+', content) # #으로 시작하며, #뒤에 연속된 문자를 모두 찾아 tags 변수에 저장
    # 4. 작성 일자 가져오기
    try:
        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10] # 앞에서부터 10자리 글자
    except:
        date = ' '
    # 5. 좋아요 수 가져오기
    try:
        like = soup.select('div.Nm9Fw > a > span')[0].text
    except:
        like = 0
    # 6. 위치 정보 가져오기
    try:
        place = soup.select('div.JF9hh')[0].text
    except:
        place = ''
    # 7. 수집한 정보 저장하기
    data = [content, date, like, place, tags]
    return data

# 다음 게시물로 이동
def move_next(driver):
    right = driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)

############### 본문 #############
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import pandas as pd

driver = webdriver.Chrome("./chromedriver.exe")
word = input("테그 이름을 입력해 주세요.")
url = insta_searching(word)
driver.get(url)
time.sleep(2)
#로그인 하기
login_section = '//*[@id="loginForm"]'
driver.find_element_by_xpath(login_section).click()
time.sleep(1)
elem_login = driver.find_element_by_name("username")
elem_login.clear()
elem_login.send_keys('01045120325')
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys('qlqjs753951!')
time.sleep(1)
xpath = '//*[@id="loginForm"]/div/div[3]/button'

driver.find_element_by_xpath(xpath).click()
time.sleep(4)
xpath1 = """//*[@id="react-root"]/section/main/div/div/div/div/button"""
driver.find_element_by_xpath(xpath1).click()
time.sleep(1)

#3. 검색페이지 점속
driver.get(url)
time.sleep(10)

#4. 첫번째 게시글 열기
select_first(driver)
#5. 리스트 만들기
results = []
#여러 게시물 크롤링 하기
target=5 # 크롤링할 게시물 수

for i in range(target):
    data = get_content(driver) #게시물 정보 가져오기
    df = pd.DataFrame(data=data)
    df.to_csv('./out.csv', mode='a', header = True)
    move_next(driver)
