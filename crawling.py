from selenium import webdriver
import time
from selenium.webdriver.common.by import By

article_list = []
link_list = []

def article_Scraping():
    driver = webdriver.Chrome()
    for i in range(1, 11):
        driver.get('https://land.naver.com/news/expertColumn.naver?page=' + str(i))
        time.sleep(1)
        articles = driver.find_elements(By.CSS_SELECTOR, 'div.table_list_column > table > tbody > tr > td.title > a')

        for article in articles:  # Using 'zip' to iterate through 'articles' and 'links' simultaneously
            article_list.append(article.text)
    driver.quit()

    for article in article_list:
        print(article)

article_Scraping()

#csv로 결과값 추출