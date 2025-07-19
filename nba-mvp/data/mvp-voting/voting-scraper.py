# %%

# Imports
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
import chromedriver_binary

# %%
# Algorithm

# Getting the html for the required MVP voting pages from Basketball Reference and converting it into soup
year = 1980
url = f"https://www.basketball-reference.com/awards/awards_{year}.html"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(100)
page = driver.page_source()
soup = BeautifulSoup(page.text, "html.parser")

# %%
