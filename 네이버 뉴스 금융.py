from datetime import datetime, timedelta
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 원하는 날짜를 생성합니다. (년, 월, 일을 숫자로 지정)
desired_date = datetime(2023, 7, 1)

# 7월달의 첫 날인 2023년 7월 1일을 가져오려면 끝 날짜는 7월의 마지막 날을 계산해야 합니다.
# 따라서 다음 달인 8월 1일에서 하루를 빼서 7월 31일을 얻습니다.
end_date = datetime(2023, 8, 1) - timedelta(days=1)

# 날짜를 '년월일' 형식으로 변환합니다.
formatted_desired_date = desired_date.strftime('%Y%m%d')
formatted_end_date = end_date.strftime('%Y%m%d')

# 링크를 생성합니다.
link = f'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=259&sid1=101&date={formatted_desired_date}'

article_list = []
link_list = []

def article_Scraping():
    driver = webdriver.Chrome()
    for j in range(0, 1):
        for i in range(1, 11):
            driver.get('https://land.naver.com/news/expertColumn.naver?date='+str(int(formatted_desired_date) + j)+'&page=' + str(i))
            time.sleep(1)
            articles = driver.find_elements(By.CSS_SELECTOR, 'div.list_body newsflash_body > ul.type06_headline > li > dl > dt > a')
            print(articles)
            for article in articles:  # Using 'zip' to iterate through 'articles' and 'links' simultaneously
                print(article.text)
                article_list.append(article.text)
    driver.quit()

    for article in article_list:
        print(article)

article_Scraping()
