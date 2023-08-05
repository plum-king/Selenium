from datetime import datetime, timedelta
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 오늘 날짜를 기준으로 역순으로 크롤링하도록 변경합니다.
desired_date = datetime.today()
end_date = datetime(2023, 8, 1)  #오늘 날짜로부터 2023년 8월 1일까지 크롤링하도록 설정

# 링크를 생성하는 부분은 날짜를 사용하므로 함수 내부로 이동합니다.
article_list = []
link_list = []

def article_Scraping():
    driver = webdriver.Chrome()
    current_date = desired_date

    while current_date >= end_date:
        formatted_date = current_date.strftime('%Y%m%d')
        link = f'https://finance.naver.com/news/news_list.naver?mode=LSS3D&section_id=101&section_id2=258&section_id3=401&date={formatted_date}'

        for i in range(1, 3):
            driver.get(link + f'&page={i}')
            time.sleep(1)
            articles = driver.find_elements(By.CSS_SELECTOR, '#contentarea_left > ul > li.newsList.top > dl > dd > a')
            for article in articles:
                # print(article.text)
                article_list.append(article.text)

        current_date -= timedelta(days=1)

    driver.quit()

    for article in article_list:
        print(article)

article_Scraping()

#csv로 결과값 추출