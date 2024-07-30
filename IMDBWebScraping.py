import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition std-1)"
]
random_user_agent = random.choice(user_agents)
service = Service("C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()

options.add_argument(f'user-agent={random_user_agent}')
options.add_argument('--referer=https://www.google.com/')

driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=50'
driver.get(url)

while True:
    try:
        # Scroll to the bottom of the page to load more listings
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)  # Wait for the content to load

        # Try to find and click the "Load More" button
        load_more_button = driver.find_element(By.CLASS_NAME, 'ipc-see-more__button')
        load_more_button.click()
        time.sleep(1)  # Wait for new content to load

    except (NoSuchElementException, ElementClickInterceptedException):
        # Break the loop if no more "Load More" button is found or click is intercepted
        break

html_content = driver.page_source

driver.quit()

list = []

soup = BeautifulSoup(html_content, 'html.parser')
movies = soup.find_all('li', class_='ipc-metadata-list-summary-item')

for movie in movies:
    title = movie.find('div', class_ = 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 bnSrml dli-title').text[3:]
    year = movie.find('div', class_="sc-b189961a-7 btCcOY dli-title-metadata").text[0:4]
    duration = movie.find('div', class_="sc-b189961a-7 btCcOY dli-title-metadata").text[4:10]
    rating = movie.find('div', class_='sc-e2dbc1a3-0 jeHPdh sc-b189961a-2 bglYHz dli-ratings-container').text[0:3]
    list.append({'Title': title, 'Year': year, 'Duration': duration, 'Rating': rating})

df = pd.DataFrame(list)

print(df.head())

df.to_csv('Top_1000_IMDB.csv', index = False)



