import pandas as pd
from scrape_linkedin import CompanyScraper

LI_AT = '****EC**FTkG///BfRtxT-*********....'

# FOR COMPANIES
with CompanyScraper(cookie = LI_AT) as scraper:
    company = scraper.scrape(company = 'facebook')
print(company.to_dict())