import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
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

url = 'https://www.realtor.com/realestateandhomes-search/Los-Angeles_CA'
# Open URL
driver.get(url)

# Scroll to the bottom of the page to load more listings


for _ in range(2):  # Adjust range to scroll more times if needed

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(10)  # Wait for the content to load

# Extract page source and close the driver
html_content = driver.page_source
driver.quit()

soup = BeautifulSoup(html_content, 'html.parser')

properties = []

# Find all property cards using data-testid attribute
property_cards = soup.find_all('div', {'data-testid': 'card-content'})

print(f"Found {len(property_cards)} property cards")

for card in property_cards:
    # Extract the required details
    listing_type = card.find('div', class_='base__StyledType-rui__sc-108xfm0-0 hRTvWe message')
    price = card.find('div', {'class': 'Pricestyles__StyledPrice-rui__btk3ge-0 kjbIiZ card-price', 'data-testid': 'card-price'})
    address1 = card.find('div', {'class': 'truncate-line', 'data-testid': 'card-address-1'})
    address2 = card.find('div', {'class': 'truncate-line', 'data-testid': 'card-address-2'})
    beds = card.find('li', {'data-testid': 'property-meta-beds'})
    baths = card.find('li', {'data-testid': 'property-meta-baths'})
    sqft = card.find('li', {'data-testid': 'property-meta-sqft'})
    lot_size = card.find('li', {'data-testid': 'property-meta-lot-size'})

    # Combine address parts
    address = ''
    if address1 and address1.text:
        address += address1.text
    if address2 and address2.text:
        address += ', ' + address2.text

    # Debugging statements
    print(f"Listing Type: {listing_type.text if listing_type else 'N/A'}")
    print(f"Price: {price.text if price else 'N/A'}")
    print(f"Address: {address if address else 'N/A'}")
    print(f"Beds: {beds.find('span', {'data-testid': 'meta-value'}).text if beds else 'N/A'}")
    print(f"Baths: {baths.find('span', {'data-testid': 'meta-value'}).text if baths else 'N/A'}")
    print(f"Sqft: {sqft.find('span', {'data-testid': 'meta-value'}).text if sqft else 'N/A'}")
    print(f"Acre Lot: {lot_size.find('span', {'data-testid': 'meta-value'}).text if lot_size else 'N/A'}")

    # Append the extracted details to the list
    properties.append({
        'Listing Type': listing_type.text if listing_type else 'N/A',
        'Price': price.text if price else 'N/A',
        'Address': address if address else 'N/A',
        'Beds': beds.find('span', {'data-testid': 'meta-value'}).text if beds else 'N/A',
        'Baths': baths.find('span', {'data-testid': 'meta-value'}).text if baths else 'N/A',
        'Sqft': sqft.find('span', {'data-testid': 'meta-value'}).text if sqft else 'N/A',
        'Acre Lot': lot_size.find('span', {'data-testid': 'meta-value'}).text if lot_size else 'N/A'
    })

# Convert to DataFrame
df = pd.DataFrame(properties)
df.to_csv('Real_Estate_Selenium.csv', index = False)