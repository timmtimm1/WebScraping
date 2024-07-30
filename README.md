# WebScraping
Code Explanation:
Overview
This Python script utilizes Selenium and BeautifulSoup to scrape real estate listings from Realtor.com for properties in Los Angeles, CA. It automates the process of loading the webpage, scrolling to load more listings, and extracting relevant property information such as listing type, price, address, number of beds and baths, square footage, and lot size.
Prerequisites:

To run this script, ensure you have the following installed:

Python 3.x
Chrome WebDriver (compatible with your version of Chrome)
Required Python packages:

selenium
pandas
beautifulsoup4
You can install the required packages using pip:
bash
pip install selenium pandas beautifulsoup4
Setup
Download ChromeDriver:
Download the ChromeDriver executable from ChromeDriver Downloads and place it in a known directory (e.g., C:\Program Files (x86)\chromedriver-win64\).
Modify the Script:

Update the path to the ChromeDriver executable in the script:
python
service = Service("C:\\Program Files (x86)\\chromedriver-win64\\chromedriver.exe")
User-Agent Strings:

The script randomly selects a user-agent string from a predefined list to mimic different browsers and avoid detection.
Usage
Run the Script:
Execute the script in your terminal or command prompt:
bash
python real_estate_scraper.py
Output:
The script will output the number of property cards found and print details for each property. It will also save the extracted data to a CSV file named Real_Estate_Selenium.csv.
Imports: The script imports necessary libraries for web scraping and data manipulation.
User-Agent Selection: A random user-agent is selected from a list to avoid detection by the website.
WebDriver Setup: The Chrome WebDriver is configured with options, including the user-agent and referer.
Page Interaction: The script opens the specified URL, scrolls to load more listings, and extracts the HTML content.
Data Extraction: BeautifulSoup is used to parse the HTML and extract relevant property details using specific HTML attributes.
Data Storage: The extracted data is stored in a pandas DataFrame and saved to a CSV file.
Notes:
Ensure that you comply with the website's terms of service when scraping data.
The script may need adjustments if the website's HTML structure changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.
