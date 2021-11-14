import pandas as pd
from scrape_linkedin import ProfileScraper

LI_AT = '****EC**FTkG///BfRtxT-*********....'

# FOR users
with ProfileScraper(cookie = LI_AT) as scraper:
    profile = scraper.scrape(user = 'alexandrebernard88')
profile = profile.to_dict()
df = pd.DataFrame(profile.items())
df.to_csv('result.csv')