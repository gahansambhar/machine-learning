from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

# Setting up the driver for the algorithm
year = 2025
while year <= 2025:
    # Getting the html for the required MVP voting pages from Basketball Reference
    # to convert to soup
    url = f"https://www.basketball-reference.com/awards/awards_{year}.html"
    page = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(page.text, "html.parser")

    # Finding the required mvp voting table
    table = soup.find_all("table", limit=1)[0]

    # Extracting the headers from the table
    headers = table.find_all("th")
    headers = [header.text for header in headers]

    # Finding the headers needed
    s = headers.index("Player")
    e = headers.index("Share")
    headers = headers[s:e+1]

    # creating the data frame to store the mvp voting data
    df = pd.DataFrame(columns=headers)

    # Extracting rws from the table
    rows = table.find_all("tr")

    # Extracting cell data from each row and adding to the dataframe
    dfsize = 0
    for row in rows:

        rowdata = []
        for cell in row:
            rowdata.append(cell.text.strip())

        if rowdata[0] != "":
            df.loc[dfsize] = rowdata[1:8]
            dfsize += 1

    # Exporting to a csv for use in machine learning
    df.to_csv(f"{year-1}-{year}-mvp-voting.csv", index=False)
    year += 1
    time.sleep(3)
