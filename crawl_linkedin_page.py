from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Credentials
browser = webdriver.Chrome('/path/to/chromedriver')
username = 'yourlinkedin@email.com'
password = 'your_password'

# Set up crawler
# Go to lobby
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# Get username spot and fill it
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
# Get password spot and fill it
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
# Click connect
elementID.submit()
# Link of page to go to (page to crawl, here it's the page of people working in linkedin)
browser.get('https://www.linkedin.com/search/results/people/?currentCompany=%5B%221337%22%5D&origin=FACETED_SEARCH&sid=w%3AR')

#Get page source code
src = browser.page_source
soup = BeautifulSoup(src, 'lxml')
print(soup)
#Strip text from source code
results = soup.find('small', {'class': 'display-flex t-12 t-black--light t-normal'}).get_text().strip().split()[0]
results = int(results.replace(',', ''))