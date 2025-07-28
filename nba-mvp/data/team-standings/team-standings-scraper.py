

# Setup
from bs4 import BeautifulSoup
import pandas as pd
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

# Set path to chrome/chromedriver as per your configuration
homedir = os.path.expanduser("~")
chrome_options.binary_location = f"{homedir}/chrome-linux64/chrome"
webdriver_service = Service(f"{homedir}/chromedriver-linux64/chromedriver")
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)


# Create soup
year = 2000

while year <= 2025:
    if year == 1999:
        continue
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_standings.html"
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    tables = soup.find_all("table")

    for table in tables:
        headers = table.find_all("th")
        headers = [header.text for header in headers]
        # If expanded standings table is found
        if 'Overall' in headers:
            estable = table
            break

    s1 = headers.index("Rk")
    e1 = headers.index("W")
    s2 = headers.index("Pre")
    e2 = headers.index("≥10")

    headers = headers[s1:e1+1] + headers[s2:e2+1]

    df = pd.DataFrame(columns=headers)

    rows = table.find_all("tr")
    dfsize = 0
    for row in rows:
        rowdata = []
        for cell in row:
            rowdata.append(cell.text.strip())
        print(rowdata)
        if rowdata[0] != '':
            df.loc[dfsize] = rowdata[0:e1-s1+1] + rowdata[s2-s1:e2-s1+1]
            dfsize += 1

    df.to_csv(f"{year-1}-{year}-team-standings.csv", index=False)

    year += 1

# 1999 lockout season led to complications with pre and post all star
# game record as there was no all star game. Pre record estimated by
# adding Feb and March record. Post record estimated by adding Apr
# and May record. (This was all done manually)
